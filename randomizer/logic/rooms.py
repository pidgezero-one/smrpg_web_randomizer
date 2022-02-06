import copy
import enum
import difflib

from . import utils
from randomizer.data import palettes, items, chests, npcs
from randomizer.data.packets import packets
from randomizer.data.rooms import rooms
from randomizer.data.rooms.room import Buffer, Partition, DestinationProps, RoomExit, MapExit, Event, BattlePackNPC, RegularNPC, ChestNPC, BattlePackClone, RegularClone, ChestClone, Room, Clone
from randomizer.helpers.flag_helpers import BoosterTowerGating
from randomizer.helpers.misc_helpers import ExtraSpriteActions


from randomizer.logic import flags
from randomizer.helpers.roomobjecttables import ObjectType, ExitType, PartitionBufferTypes

def validate_chain(chain):
    c = copy.deepcopy(chain)
    c.sort()
    return (max(c) - min(c) <= 8)
    

def get_clone_sequence(ids):

    def get_next_id(cursor=0, existing_ids=[]):
        possibilities = []
        for id in ids[cursor]:
            chain = existing_ids + [id]
            if cursor >= len(ids) - 1:
                if validate_chain(chain):
                    possibilities.append(chain)
            else:
                c = get_next_id(cursor+1, chain)
                if len(c) > 0:
                    possibilities.extend(c)
        return possibilities

    p = get_next_id()
    if len(p) > 0:
        return p[0]
    else:
        raise Exception("could not find consecutive npc IDs for clones %r" % ids)


def assemble_npc(model):
    if model is None:
        return [0xFF] * 7
    output = bytearray([])
    output.append(model.occupant.sprite_id & 0xFF)
    output.append(
        (model.vram_size << 5)
        + (model.directions << 2)
        + (model.occupant.sprite_id >> 8)
    )
    output.append(
        (model.priority_2 << 7)
        + (model.priority_1 << 6)
        + (model.priority_0 << 5)
        + (model.byte2_bit4 << 4)
        + (model.byte2_bit3 << 3)
        + (model.byte2_bit2 << 2)
        + (model.byte2_bit1 << 1)
        + model.byte2_bit0
    )
    if model.y_shift < 0:
        byte4 = (1 << 4) + (model.y_shift + 16)
    else:
        byte4 = model.y_shift
    byte4 += model.shadow_size << 5
    byte4 += model.cannot_clone << 7
    output.append(byte4)
    output.append((model.obtuse_axis << 4) + model.acute_axis)
    output.append(
        (model.byte5_bit7 << 7)
        + (model.byte5_bit6 << 6)
        + (model.show_shadow << 5)
        + model.height
    )
    output.append(model.byte6_bit2 << 2)
    return output

class CloneGroup:
    npcs = []
    ids = []

    def __init__(self, npcs, ids=[]):
        self.npcs = copy.deepcopy(npcs)
        self.ids = copy.deepcopy(ids)

class SingleNPC:
    npc = None
    id = None

    def __init__(self, npc, id):
        self.npc = copy.deepcopy(npc)
        self.id = id


class AmbiguousCoin:
    none = enum.auto()
    one = enum.auto()
    multi = enum.auto()

def list_unique(arr):
    l = set()
    l_add = l.add
    return [x for x in arr if not (x in l or l_add(x))]

partition_priority = [
    PartitionBufferTypes.TREASURE_CHEST,
    PartitionBufferTypes.COINS,
    PartitionBufferTypes.EMPTY_3,
    PartitionBufferTypes._4_SPRITES_PER_ROW,
    PartitionBufferTypes._3_SPRITES_PER_ROW
]

needs_base_packet_size = {
    27: 1,
    35: 1,
    36: 1,
    39: 0,
    41: 1,
    54: 0,
    # 57: 1,
    # 58: 1,
    # 60: 1,
    # 62: 1,
    68: 1,
    69: 0,
    71: 0,
    # 72: 0,
    73: 0,
    # 77: 1,
    79: 2,
    82: 0, # might be 1
    92: 0,
    # 95: 1,
    100: 0,
    105: 1,
    108: 1,
    116: 1,
    119: 1,
    123: 1,
    124: 1,
    125: 1,
    127: 1,
    # 128: 1,
    # 129: 1,
    136: 1,
    137: 0,
    138: 1,
    139: 3,
    142: 0,
    # 144: 1,
    # 157: 1,
    # 158: 1,
    # 159: 0,
    # 161: 1,
    # 165: 1,
    # 168: 2,
    # 169: 1,
    # 171: 1,
    # 174: 1,
    # 175: 1,
    # 178: 2,
    # 179: 0,
    # 180: 2,
    181: 2,
    # 184: 1,
    # 185: 1,
    187: 0,
    188: 1,
    # 196: 1,
    # 198: 0,
    # 199: 1,
    # 204: 1,
    # 207: 0,
    # 221: 0,
    # 222: 1,
    230: 1,
    # 233: 1,
    # 235: 1,
    # 236: 1,
    # 238: 0,
    251: 1,
    254: 1,
    262: 0,
    # 263: 0,
    # 264: 0,
    # 265: 0,
    # 267: 1,
    268: 0,
    # 275: 1,
    # 276: 2,
    # 277: 1,
    # 278: 1,
    # 279: 1,
    # 280: 1,
    # 281: 1,
    # 282: 1,
    # 283: 2, - probably just 1, no bomb in rando
    284: 0,
    # 286: 1,
    289: 0,
    # 317: 0,
    318: 0,
    319: 0,
    # 321: 0,
    322: 0, # might be 1
    # 335: 0,
    # 337: 1,
    338: 1,
    # 339: 2,
    352: 2,
    354: 1,
    # 355: 0, # normally 1, but will never have lava and 2 chests active at once
    # 356: 0,
    358: 0,
    359: 0,
    361: 0,
    364: 0,
    # 367: 1,
    # 369: 1,
    370: 1,
    # 371: 1,
    # 372: 1,
    # 373: 1,
    # 374: 1,
    376: 1,
    377: 1,
    383: 1,
    384: 0,
    385: 0,
    389: 0,
    394: 1,
    # 395: 1,
    402: 0,
    403: 0,
    404: 0,
    # 405: 0,
    407: 0,
    # 408: 0, 
    # 411: 1,
    418: 0,
    420: 1,
    422: 0,
    423: 0,
    424: 0,
    426: 0,
    # 427: 0,
    428: 1,
    442: 2,
    # 445: 0,
    448: 0,
    455: 0, # plus chests - originally 1
    456: 2,
    457: 0,
    458: 1,
    459: 1,
    460: 1,
    461: 1,
    462: 1,
    # 463: 1,
    # 464: 1,
    # 465: 1,
    # 467: 1,
    # 468: 1,
    470: 0,
    472: 0,
    473: 2,
    474: 1,
    # 475: 1,
    478: 0,
    # 497: 0,
    # 501: 0,
    509: 1,
}

special_case_rooms = [37, 57, 70, 71, 72, 73, 79, 205, 230, 232, 233, 236, 463, 466, 477]
# 205 - complicated spiney sequence
# 463, 466 - barrel count room and logic problem room need this for some reason
requires_coin_buffer = [71, 72, 242] # maybe 199. 199 needed all NPCs restored bc the graphics interact weirdly with the save box animation
# 301 - breaks chest sprites if you use extra sprite buffer for coins

always_requires_coin_buffer = [71, 72, 73]

def finalize_packet(size):
    if size > 0:
        return True, size - 1
    return False, 0

def get_ally_buffer(world, current_size, sprite_id, prop_id, sequence=True):
    if sequence:
        mold_size = utils.get_min_vram_from_animation(world.sprites[sprite_id], prop_id)
    else:
        mold_size = utils.get_min_vram_from_mold(world.sprites[sprite_id], prop_id)
    if mold_size > current_size:
        return mold_size
    return current_size

def is_party_member(model):
    return utils.isclass_or_instance(model, npcs.Mario) or    utils.isclass_or_instance(model, npcs.Mallow) or    utils.isclass_or_instance(model, npcs.Geno) or    utils.isclass_or_instance(model, npcs.Bowser) or    utils.isclass_or_instance(model, npcs.Toadstool) 

def set_partitions(world):
    pandorite_rooms = []
    hidon_rooms = []
    for c in world.chest_locations:
        if utils.isclass_or_instance(c.item, items.PandoriteFight):
            pandorite_rooms.extend(c.rooms)
        elif utils.isclass_or_instance(c.item, items.HidonFight):
            hidon_rooms.extend(c.rooms)

    # get rooms which need star packet
    rooms_with_star_packet = []
    for c in world.chest_locations:
        if utils.isclass_or_instance(c.item, items.InvincibilityStar):
            rooms_with_star_packet.extend(c.nearby_star_rooms)
    rooms_with_star_packet = list(set(rooms_with_star_packet))

    # get vram sizes of packets per room, denote coin chests
    chest_packets = {}
    chest_coins = {}
    for c in world.chest_locations:
        if items.is_coin(c.item):
            for i, r in c.rooms:
                if r not in chest_coins:
                    chest_coins[r] = []
                npc_id = c.npc_ids[i]
                coords = world.rooms[r].objects[npc_id]
                chest_coins[r].append((npc_id, coords.x, coords.y))
        elif utils.isclass_or_instance(c.item, items.SlotMachineChest):
            continue
        else:
            npc_model = c.item.model
            packet_number = npc_model.chest_packet
            sprite_id = packets[packet_number]["sprite"]
            vram_size =  utils.get_min_vram_from_animation(world.sprites[sprite_id], 0)
            for r in c.rooms:
                if r not in chest_contents:
                    chest_contents[r] = []
                npc_id = c.npc_ids[i]
                coords = world.rooms[r].objects[npc_id]
                chest_contents[r].append((npc_id, vram_size, coords.x, coords.y))
            

    for room_index, room in enumerate(world.rooms):

        if room_index in [68]:
            continue

        # Get the ally buffer required size

        ally_buffer = 0
        for seq_id in [0, 1, 6, 7, 8, 9, 10, 11, 12]:
            ally_buffer = get_ally_buffer(world, ally_buffer, 0, seq_id)
        for seq_id in range(0,10):
            ally_buffer = get_ally_buffer(world, ally_buffer, 1, seq_id)

        if ExtraSpriteActions.Swim in room.extra_required_actions:
            for seq_id in range(10, 15):
                ally_buffer = get_ally_buffer(world, ally_buffer, 1, seq_id)
        if ExtraSpriteActions.Wobble in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 0, 4)
        if ExtraSpriteActions.Sleep in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 0, 13)
            ally_buffer = get_ally_buffer(world, ally_buffer, 0, 14)
        if ExtraSpriteActions.HoldStar in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 0, 5)
        if ExtraSpriteActions.Whirl in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 1, 15)
        if ExtraSpriteActions.StandingSleep in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 2, 3)
        if ExtraSpriteActions.SurpriseFrame in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 3, 0)
        if ExtraSpriteActions.StandingSleep in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 2, 6)
        if ExtraSpriteActions.Defend in room.extra_required_actions:
            seq = world.sprites[2].animation.properties.sequences[5]
            frame = seq.frames[0].mold_id
            ally_buffer = get_ally_buffer(world, ally_buffer, 2, frame, False)
        if ExtraSpriteActions.LeanBack in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 2, 13)
        if ExtraSpriteActions.LeanBack2 in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 2, 14)
        if ExtraSpriteActions.LeanForward in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 2, 15)
        if ExtraSpriteActions.Salute in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 2, 10)
        if ExtraSpriteActions.Flop in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 2, 8)
        if ExtraSpriteActions.SurpriseFrameBack in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 2, 7, False)
        if ExtraSpriteActions.DownPipe in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 2, 30, False)
        if ExtraSpriteActions.Dizzy in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 2, 7)
        if ExtraSpriteActions.PraiseFront in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 2, 9)
        if ExtraSpriteActions.Mute in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 2, 12)
        if ExtraSpriteActions.PraiseBack in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 3, 2)
        if ExtraSpriteActions.DispleasedFront in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 3, 3)
        if ExtraSpriteActions.DispleasedBack in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 3, 4)
        if ExtraSpriteActions.TumbleFront in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 3, 6)
        if ExtraSpriteActions.TumbleBack in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 3, 7)
        if ExtraSpriteActions.Exor in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 3, 10)
        if ExtraSpriteActions.Challenge in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 4, 2)
        if ExtraSpriteActions.ChallengeNimbus in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 4, 10, False)
            ally_buffer = get_ally_buffer(world, ally_buffer, 4, 11, False)
        if ExtraSpriteActions.Crouch in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 6, 0, False)
        if ExtraSpriteActions.Yoshi in room.extra_required_actions:
            for seq_id in range(2, 7):
                ally_buffer = get_ally_buffer(world, ally_buffer, 6, seq_id)
        if ExtraSpriteActions.Climb in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 6, 7)
            ally_buffer = get_ally_buffer(world, ally_buffer, 6, 8)
        if ExtraSpriteActions.Blackjack in room.extra_required_actions:
            for seq_id in range(9, 12):
                ally_buffer = get_ally_buffer(world, ally_buffer, 6, seq_id)
        if ExtraSpriteActions.LookAtDoll in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 6, 12)
        if ExtraSpriteActions.ClimbFrame in room.extra_required_actions:
            ally_buffer = get_ally_buffer(world, ally_buffer, 6, 13)

        ally_buffer += 1
        # if room_index in [184, 189, 202, 204, 225, 226, 229, 238, 255, 284, 351, 397, ]:
        #     ally_buffer += 1
        # elif room_index in [456]:
        #     ally_buffer += 2

        extra_sprite_buffer = 0
        if room_index in needs_base_packet_size:
            extra_sprite_buffer = needs_base_packet_size[extra_sprite_buffer] + 1
        if room_index in rooms_with_star_packet:
            extra_sprite_buffer += 1

        # add chest packets where necessary
        if room_index in chest_packets:
            extra_sprite_buffer += 1
            min_packet_size = 0
            for chest in chest_packets[room_index]:
                npc_id = chest[0]
                vram = chest[1]
                if vram > min_packet_size:
                    min_packet_size = vram
                x = chest[2]
                y = chest[3]

                # account for chests that are close together and may need packets active at the same time
                min_second_packet_size = 0
                for other_chest in chest_packets[room_index]:
                    other_npc_id = chest[0]
                    other_vram = chest[1] + 1
                    other_x = chest[2]
                    other_y = chest[3]
                    if abs(other_x - x) <= 3 and abs(other_y - y) <= 4 and other_vram > min_second_packet_size:
                        min_second_packet_size = other_vram
                if min_packet_size < min_packet_size + min_second_packet_size:
                    min_packet_size = min_packet_size + min_second_packet_size
            extra_sprite_buffer += min_packet_size

        
        # elif room_index in [376, 377, 459, 460, 461, 462, 202] or (room is not None and len(room.objects) == 0): # rooms that always need triple empty + ex 1
        #     partition = Partition(ally_sprite_buffer_size=ally_buffer, allow_extra_sprite_buffer=True, extra_sprite_buffer_size=extra_sprite_buffer)
        #     world.rooms[room_index].partition = copy.deepcopy(partition)
        if room_index in [192, 205, 104]: # rooms that always need triple empty
            # 205 - Trying this out. A seed where partitions didn't assemble correctly actually made the spinies render correctly.
            # May not work with all boss/ally combos.
            packet_on, packet_size = finalize_packet(extra_sprite_buffer)
            world.rooms[room_index].partition = Partition(ally_sprite_buffer_size=ally_buffer, allow_extra_sprite_buffer=packet_on, extra_sprite_buffer_size=packet_size)
            continue

        if room is not None and len(room.objects) > 0:

            original_partition = None 
            if partition is not None:
                original_partition = copy.deepcopy(room.partition)

            partition = Partition(ally_sprite_buffer_size=ally_buffer)

            if original_partition is not None:
                partition.full_palette_buffer = original_partition.full_palette_buffer

            room_npcs = room.objects

            priority_buffers = []
            npc_buffers = []
            packet_buffers = []

            if room_index in special_case_rooms:
                priority_buffers.append(PartitionBufferTypes.EMPTY_3)

            ambiguous_coin_chest = AmbiguousCoin.none

            has_conundrum_clones = False
            for npc_id, npc in enumerate(room_npcs):
                if (utils.isclass_or_instance(npc, Clone) or (npc_id+1 < len(room_npcs) and utils.isclass_or_instance(room_npcs[npc_id+1], Clone))) and npc.model.cannot_clone:
                    has_conundrum_clones = True


            # consider chest contents and packets
            for c in world.chest_locations:
                if room_index in c.rooms or (512 in c.rooms and room_index in pandorite_rooms) or (513 in c.rooms and room_index in hidon_rooms):
                    if utils.isclass_or_instance(c, chests.PacketItem):
                        packet_size += 1
                    if (utils.isclass_or_instance(c.item, items.FrogCoin) or utils.isclass_or_instance(c.item, items.InfiniteCoins) or (not world.settings.is_flag_enabled(flags.QuickHitCoins) and (utils.isclass_or_instance(c.item, items.MultiFrogCoin) or utils.isclass_or_instance(c.item, items.Coins)))) and (utils.isclass_or_instance(c, chests.Chest) or utils.isclass_or_instance(c, chests.PacketItem)):
                        if (utils.isclass_or_instance(c.item, items.Coins) and c.item.chest_70A7_lower != 1) or utils.isclass_or_instance(c.item, items.MultiFrogCoin) or utils.isclass_or_instance(c.item, items.InfiniteCoins):
                            ambiguous_coin_chest = AmbiguousCoin.multi
                        elif utils.isclass_or_instance(c.item, items.FrogCoin) or (utils.isclass_or_instance(c.item, items.Coins) and c.item.chest_70A7_lower == 1):
                            ambiguous_coin_chest = AmbiguousCoin.one
                    elif utils.isclass_or_instance(c, chests.Chest) and utils.isclass_or_instance(c.item, items.SlotMachineChest):
                        packet_buffers.append(PartitionBufferTypes.COINS) # slot frog coin
                    elif utils.isclass_or_instance(c, chests.Chest) and room_index not in requires_coin_buffer and (utils.isclass_or_instance(c.item, items.RegularItem) or utils.isclass_or_instance(c.item, items.ProgressiveItem) or utils.isclass_or_instance(c.item, items.Beetlemania) or utils.isclass_or_instance(c.item, items.StarPiece)):
                        packet_size = max(1, packet_size) # apparently this might work???
            if has_star_chest:
                packet_size += 1
                # todo: invincibility stars

            last_sprite = -1

            existing_formats_in_room = []
            buffer_order = []

            # clones can have diff gridplane dimensions... what to do?


            # get all npc models
            for npc_index, npc in enumerate(room_npcs):
                #print(room_index, npc_index)
                model = npc.model.occupant
                # print(npc_index, room_index, model)
                if not npc.model.cannot_clone:
                    sprite = model.sprite_id
                    animation_pack = world.sprites[sprite].animation

                    buf = None
                    if is_party_member(model):
                        if room_index in [203, 204, 205]:
                            world.rooms[room_index].objects[npc_index].model.cannot_clone = True
                            continue
                    #else:
                    if utils.isclass_or_instance(model, npcs.TreasureChest):
                        priority_buffers.append(PartitionBufferTypes.TREASURE_CHEST)
                    elif utils.isclass_or_instance(model, npcs.Coin):
                        priority_buffers.append(PartitionBufferTypes.COINS)
                    elif not animation_pack.properties.molds[0].gridplane:
                        priority_buffers.append(PartitionBufferTypes.EMPTY_3)
                    else:
                        if animation_pack.properties.molds[0].tiles[0].format <= 1:
                            buf = PartitionBufferTypes._4_SPRITES_PER_ROW
                        else:
                            buf = PartitionBufferTypes._3_SPRITES_PER_ROW
                        if buf not in existing_formats_in_room:
                            existing_formats_in_room.append(buf)
                            if utils.isclass_or_instance(model, Clone):
                                npc_buffers.append(buf)
                        elif sprite != last_sprite:
                            npc_buffers.append(buf)
                        elif len(npc_buffers) == 0 or npc_buffers[len(npc_buffers) - 1] != buf:
                            npc_buffers.append(buf)
                    last_sprite = sprite 

            priority_buffers = list_unique(priority_buffers)
            # npc_buffers = list_unique(npc_buffers) # should this be disabled or not?
            packet_buffers = list_unique(packet_buffers)

            # special case - this kero sewers room needs a partition just for the fish
            # because it has special buffer space properties
            if room_index in [56, 57, 58]:
                npc_buffers.insert(0, PartitionBufferTypes._4_SPRITES_PER_ROW)
            # can't figure out why 301 needs 2 3sprite buffers to make button push graphic work
            elif room_index == 301:
                npc_buffers.append(PartitionBufferTypes._3_SPRITES_PER_ROW)

            if room_index == 202:
                if world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.toadstool): # booster tower bomb explosion
                    packet_size = max(2, packet_size)

            if room_index in always_requires_coin_buffer:
                if PartitionBufferTypes.COINS not in packet_buffers:
                    packet_buffers.append(PartitionBufferTypes.COINS)
            elif ambiguous_coin_chest is not AmbiguousCoin.none:
                if has_conundrum_clones or room_index in requires_coin_buffer: # 301 and 401 both have Treasure-3SPRITE-3SPRITe but only 301 breaks w. coins in EX buffer
                    packet_buffers.append(PartitionBufferTypes.COINS)
                    # Why does 301 need this but not 401?
                    # Only difference I see is that 301 hasclone buffer of un-cloneable sprite
                elif ambiguous_coin_chest == AmbiguousCoin.multi:
                    packet_size = max(4, packet_size)
                elif ambiguous_coin_chest == AmbiguousCoin.one:
                    packet_size = max(2, packet_size)

            if PartitionBufferTypes.COINS in priority_buffers and PartitionBufferTypes.COINS in packet_buffers:
                priority_buffers.remove(PartitionBufferTypes.COINS)

            final_buffers = [None] * 3

            buffers = priority_buffers + npc_buffers + packet_buffers

            if PartitionBufferTypes.TREASURE_CHEST in priority_buffers:
                final_buffers[0] = Buffer(PartitionBufferTypes.TREASURE_CHEST)
                buffers.remove(PartitionBufferTypes.TREASURE_CHEST)
            elif PartitionBufferTypes.EMPTY_3 in priority_buffers:
                final_buffers[0] = Buffer(PartitionBufferTypes.EMPTY_3)
                buffers.remove(PartitionBufferTypes.EMPTY_3)

            if PartitionBufferTypes.COINS in buffers:
                final_buffers[2] = Buffer(PartitionBufferTypes.COINS)
                buffers.remove(PartitionBufferTypes.COINS)

            idx = 0
            for i in range(0, 3):
                if final_buffers[i] is None and idx < len(buffers):
                    final_buffers[i] = Buffer(buffers[idx])
                    idx += 1

            for i in range(0, 3):
                if final_buffers[i] is None:
                    final_buffers[i] =Buffer(PartitionBufferTypes.EMPTY_3)

            for i, buf in enumerate(final_buffers):
                if original_partition is not None:
                    for obuf in original_partition.buffers:
                        if obuf.buffer_type == final_buffers[i].buffer_type and obuf.main_buffer_space > buf.main_buffer_space:
                            buf.main_buffer_space = obuf.main_buffer_space
                            buf.index_in_main_buffer = obuf.index_in_main_buffer
                            break
                    partition.buffers[i] = buf


            
            if packet_size > 0:
                partition.allow_extra_sprite_buffer = True
                partition.extra_sprite_buffer_size = packet_size - 1
            else:
                partition.allow_extra_sprite_buffer = False
                partition.extra_sprite_buffer_size = 0

            world.rooms[room_index].partition = copy.deepcopy(partition)
            




class Rooms:
    def __init__(self):
        self.output = []

    def assemble_from_table(table, event_table):

        roomdata_pointers = bytearray()
        eventtile_pointers = bytearray()
        exit_pointers = bytearray()

        model_output = bytearray([])
        roomdata_output = bytearray([])
        eventtile_output = bytearray([])
        exit_output = bytearray([])

        partitions = []
        partition_output = bytearray([])

        standalone_npcs = []
        clone_groups = []

        reserved_event_IDS = [
            range(2823, 3072),
            range(3950, 4095),
            range(2675, 2793),
            range(1972, 2047),
            range(1466, 1520),
            range(1523, 1536),
        ]

        # collect all NPC model definitions

        for i in range(len(table)):
            this_room = table[i]

            last_object = None
            last_object_was_clone = False
            clone_group = []

            if this_room is not None and len(this_room.objects) > 0:
                for npc_i, npc in enumerate(this_room.objects):

                    model = npc.model
                    assembled = assemble_npc(model)

                    if (
                        utils.isclass_or_instance(npc, Clone)
                        and not last_object_was_clone
                    ):  # begin new clone group
                        clone_group = [last_object]
                        if last_object != assembled:
                            clone_group.append(assembled)
                        clone_group.sort()
                    elif (
                        utils.isclass_or_instance(npc, Clone)
                        and last_object_was_clone
                    ):  # continue clone group
                        if assembled not in clone_group:
                            clone_group.append(assembled)
                            clone_group.sort()
                    elif (  # end clone group
                        not utils.isclass_or_instance(npc, Clone)
                        and last_object_was_clone
                    ):
                        if len(clone_group) == 1:
                            if clone_group[0] not in standalone_npcs:
                                standalone_npcs.append(clone_group[0])
                        elif clone_group not in clone_groups:
                            clone_groups.append(clone_group)
                        clone_group = []
                    else:  # no clone group
                        if (
                            last_object is not None
                            and last_object not in standalone_npcs
                        ):
                            standalone_npcs.append(last_object)

                    last_object = assembled
                    last_object_was_clone = utils.isclass_or_instance(npc, Clone)
                if len(clone_group) > 0:
                    if len(clone_group) == 1:
                        if clone_group[0] not in standalone_npcs:
                            standalone_npcs.append(clone_group[0])
                    elif clone_group not in clone_groups:
                        clone_groups.append(clone_group)
                else:
                    standalone_npcs.append(last_object)

        clone_groups.sort(key=lambda x: len(x), reverse=True)

        # consolidate clone groups
        clonegroup_index = 0
        indexes_to_remove = []
        while clonegroup_index < len(clone_groups):
            clone_group = clone_groups[clonegroup_index]
            # consider expanding existing clone groups instead of this
            best_match = 0
            best_match_index = None
            for match_index, cg in enumerate(clone_groups[0:clonegroup_index]):
                if match_index not in indexes_to_remove:
                    sm = difflib.SequenceMatcher(
                        None,
                        tuple([tuple(c) for c in cg]),
                        tuple([tuple(c) for c in clone_group]),
                    )
                    similarity = sm.ratio()
                    if (
                        similarity > best_match
                        and len(
                            set(
                                tuple([tuple(c) for c in cg])
                                + tuple([tuple(c) for c in clone_group])
                            )
                        )
                        <= 8
                    ):
                        best_match = similarity
                        best_match_index = match_index
            if best_match_index is not None:
                indexes_to_remove.append(clonegroup_index)
                for cg_ in clone_group:
                    if cg_ not in clone_groups[best_match_index]:
                        clone_groups[best_match_index].append(cg_)
            clonegroup_index += 1
        clonegroups_to_remove = [clone_groups[i] for i in indexes_to_remove]
        for c in clonegroups_to_remove:
            clone_groups.remove(c)

        # create indexes for npc definitions
        all_npcs = [item for sublist in clone_groups for item in sublist]
        if len(all_npcs) > 1389:
            raise Exception("too many NPC definitions")
        for s in standalone_npcs:
            if s not in all_npcs:
                all_npcs.append(s)

        # write npc table to rom
        for s in all_npcs:
            model_output += s
        while len(model_output) < 0x2600:
            model_output.append(0xFF)

        event_assignment_cursor = [0, 0]

        # assemble rooms
        for i in range(len(table)):
            this_room = table[i]
            offset = 0x148400 + len(roomdata_output)
            ptr_bytes = bytearray([offset & 0xFF, (offset >> 8) & 0xFF])

            eventtile_offset = 0x20E400 + len(eventtile_output)
            eventtile_ptr_bytes = bytearray(
                [eventtile_offset & 0xFF, (eventtile_offset >> 8) & 0xFF]
            )
            exit_offset = 0x1D3166 + len(exit_output)
            exit_ptr_bytes = bytearray([exit_offset & 0xFF, (exit_offset >> 8) & 0xFF])
            roomdata_pointers += ptr_bytes
            eventtile_pointers += eventtile_ptr_bytes
            exit_pointers += exit_ptr_bytes

            if this_room is not None:

                # write partition bytes if new, get partition ID

                # if i == 205:
                #     print(this_room.partition)

                p = this_room.partition
                partition_byte_1 = p.allow_extra_sprite_buffer * 0x10
                partition_byte_1 += p.ally_sprite_buffer_size << 5
                partition_byte_1 += p.extra_sprite_buffer_size & 0x0F
                partition_byte_1 += p.full_palette_buffer * 0x80
                partition_byte_2 = p.buffers[0].buffer_type & 0x07
                partition_byte_2 += p.buffers[0].main_buffer_space << 4
                partition_byte_2 += p.buffers[0].index_in_main_buffer * 0x80
                partition_byte_3 = p.buffers[1].buffer_type & 0x07
                partition_byte_3 += p.buffers[1].main_buffer_space << 4
                partition_byte_3 += p.buffers[1].index_in_main_buffer * 0x80
                partition_byte_4 = p.buffers[2].buffer_type & 0x07
                partition_byte_4 += p.buffers[2].main_buffer_space << 4
                partition_byte_4 += p.buffers[2].index_in_main_buffer * 0x80
                partition_bytes = bytearray(
                    [
                        partition_byte_1,
                        partition_byte_2,
                        partition_byte_3,
                        partition_byte_4,
                    ]
                )
                partition_index = None
                if partition_bytes in partitions:
                    partition_index = partitions.index(partition_bytes)
                if partition_index is None:
                    partition_index = len(partitions)
                    partitions.append(partition_bytes)
                # if i == 204:
                #     print(p, partition_index)
                #     print(partitions[partition_index])

                room_bytes = bytearray([partition_index])

                # match NPCs to NPC IDs

                clone_group = []
                class_clone_group = None

                npcs_in_assembly_order = []

                if len(this_room.objects) > 0:
                    last_object = None
                    last_object_ids = []
                    last_object_was_clone = False
                    for npc in this_room.objects:

                        model = npc.model
                        assembled = assemble_npc(model)

                        possible_ids = [
                            i for i, val in enumerate(all_npcs) if val == assembled
                        ]

                        #print(i, model.occupant, possible_ids)

                        if (
                            utils.isclass_or_instance(npc, Clone)
                            and not last_object_was_clone
                        ):  # begin new clone group
                            clone_group = [last_object_ids, possible_ids]
                            class_clone_group = CloneGroup([last_object, npc])
                        elif (
                            utils.isclass_or_instance(npc, Clone)
                            and last_object_was_clone
                        ):  # continue clone group
                            clone_group.append(possible_ids)
                            class_clone_group.npcs.append(npc)
                        elif (  # end clone group
                            not utils.isclass_or_instance(npc, Clone)
                            and last_object_was_clone
                        ):
                            class_clone_group.ids = get_clone_sequence(clone_group)
                            npcs_in_assembly_order.append(class_clone_group)
                            clone_group = []
                            class_clone_group = []
                        else:  # no clone group
                            if len(last_object_ids) > 0 and last_object is not None:
                                npcs_in_assembly_order.append(SingleNPC(last_object, last_object_ids[0]))

                        last_object = npc
                        last_object_ids = possible_ids
                        last_object_was_clone = utils.isclass_or_instance(
                            npc, Clone
                        )
                    if len(clone_group) > 0:
                        class_clone_group.ids = get_clone_sequence(clone_group)
                        npcs_in_assembly_order.append(class_clone_group)
                    else:
                        npcs_in_assembly_order.append(SingleNPC(last_object, last_object_ids[0]))

                    # start writing NPC data

                    for npc in npcs_in_assembly_order:

                        # write standalone npc

                        model_offset = 0
                        action_script_offset = 0
                        battle_pack_offset = 0
                        event_offset = 0
                        clone_length = 0
                        event_id = 256
                        event_group = []
                        new_event_group = []
                        #if i == 5:
                        #    print(npc)
                        if utils.isclass_or_instance(npc, CloneGroup):

                            this_npc = npc.npcs[0]
                            clone_length = len(npc.npcs) - 1
                            assert clone_length <= 15

                            if this_npc.type != ObjectType.CHEST:
                                #print(i, [n.model.occupant for n in npc.npcs], [n.action_script for n in npc.npcs])
                                base_action_script = min([n.action_script for n in npc.npcs])
                                action_script_offset = this_npc.action_script - base_action_script
                                if this_npc.type == ObjectType.BATTLE:
                                    assert action_script_offset <= 15
                                else:
                                    assert action_script_offset <= 7
                            else:
                                base_action_script = npc.npcs[0].action_script

                            if this_npc.type != ObjectType.OBJECT:
                                base_model_id = npc.ids[0]

                            if this_npc.type == ObjectType.OBJECT:
                                event_group = [n.event_script for n in npc.npcs]
                                new_event_group = [n.event_script for n in npc.npcs]
                                base_model_id = min(npc.ids)
                                model_offset = npc.ids[0] - base_model_id
                                assert model_offset <= 7
                                if max(event_group) - min(event_group) > 7:
                                    if len(reserved_event_IDS[event_assignment_cursor[0]]) - event_assignment_cursor[1] < len(npc.npcs):
                                        event_assignment_cursor[0] += 1
                                        event_assignment_cursor[1] = 0

                                    new_event_id = reserved_event_IDS[event_assignment_cursor[0]][event_assignment_cursor[1]]
                                    event_assignment_cursor[1] += 1
                                    event_table[new_event_id] = [utils.new_command(new_event_id, "jmp_to_event", [this_npc.event_script])]
                                
                                    new_event_group = [new_event_id]
                                    event_id = new_event_id
                                    #print(i, new_event_id)

                                    for clone_index, clone in enumerate(npc.npcs[1:]):
                                        if clone.event_script not in event_group[0:clone_index]:
                                            new_event_id = reserved_event_IDS[event_assignment_cursor[0]][event_assignment_cursor[1]]
                                            event_assignment_cursor[1] += 1
                                            event_table[new_event_id] = [utils.new_command(new_event_id, "jmp_to_event", [clone.event_script])]
                                        else:
                                            ind = event_group[0:clone_index].index(clone.event_script)
                                            new_event_id = new_event_group[ind]
                                        new_event_group.append(new_event_id)
                                

                                else:
                                    event_id = min(event_group)
                                    event_offset = this_npc.event_script - min(event_group)
                                    
                                #if i == 5:
                                #    print(new_event_group)
                            elif this_npc.type == ObjectType.CHEST:
                                event_id = this_npc.event_script
                            elif this_npc.type == ObjectType.BATTLE:
                                base_battle_pack = min([n.battle_pack for n in npc.npcs])
                                battle_pack_offset = this_npc.battle_pack - base_battle_pack
                                assert battle_pack_offset <= 7

                        else:
                            this_npc = npc.npc
                            base_model_id = npc.id
                            base_action_script = this_npc.action_script
                            if this_npc.type != ObjectType.BATTLE:
                                event_id = this_npc.event_script
                            else:
                                base_battle_pack = this_npc.battle_pack
                        #if i == 5:
                        #    print(clone_length)

                        room_bytes.append((this_npc.type << 4) + clone_length)
                        room_bytes.append((this_npc.cant_float << 7) + (this_npc.set_sequence_playback << 6) + (this_npc.byte2_bit5 << 5) + (this_npc.cant_enter_doors << 4) + (this_npc.face_on_trigger << 3) + this_npc.speed)
                        room_bytes.append((this_npc.byte3_bit7 << 7) + (this_npc.cant_walk_through << 6) + (this_npc.byte3_bit5 << 5) + (this_npc.cant_pass_npcs << 4) + (this_npc.cant_jump_through << 3) + (this_npc.cant_pass_walls << 2) + (this_npc.cant_walk_under << 1) + this_npc.cant_walk_up_stairs)

                        room_bytes.append(((base_model_id << 2) & 0xFF) + (this_npc.cant_move_if_in_air << 1) + this_npc.slidable_along_walls)
                        room_bytes.append(((base_action_script & 0x0F) << 4) + (base_model_id >> 6))
                        room_bytes.append((this_npc.byte7_upper2 << 6) + (base_action_script >> 4))

                        if this_npc.type != ObjectType.BATTLE:
                            room_bytes.append(event_id & 0xFF)
                            room_bytes.append((this_npc.initiator << 4) + (event_id >> 8))
                        else:
                            room_bytes.append(base_battle_pack & 0xFF)
                            room_bytes.append((this_npc.initiator << 4) + this_npc.after_battle)

                        if this_npc.type == ObjectType.OBJECT:
                            room_bytes.append((event_offset << 5) + (action_script_offset << 3) + model_offset)
                        elif this_npc.type == ObjectType.CHEST:
                            room_bytes.append((this_npc.upper_70A7 << 4) + this_npc.lower_70A7)
                            #print(i, (this_npc.upper_70A7 << 4) + this_npc.lower_70A7)
                        elif this_npc.type == ObjectType.BATTLE:
                            room_bytes.append((battle_pack_offset << 4) + action_script_offset)
                        room_bytes.append((this_npc.visible << 7) + this_npc.x)
                        room_bytes.append((this_npc.z_half << 7) + this_npc.y)
                        room_bytes.append((this_npc.direction << 5) + this_npc.z)

                        # write clones

                        if utils.isclass_or_instance(npc, CloneGroup):
                            #print(npc.npcs[0].model.occupant)
                            for clone_index in range(1, len(npc.npcs)):
                                this_clone = npc.npcs[clone_index]
                                if this_clone.type != this_npc.type:
                                    raise Exception("room %i: mismatched clone type found" % i)
                                if this_clone.type != ObjectType.CHEST:
                                    action_script_offset = this_clone.action_script - base_action_script
                                    #print (this_clone.action_script, base_action_script)
                                if this_clone.type == ObjectType.OBJECT:
                                    new_event_id = new_event_group[clone_index]
                                    model_offset = npc.ids[clone_index] - base_model_id
                                    event_offset = new_event_id - min(new_event_group)
                                    #print(i, npc, this_clone.model.occupant)
                                    assert model_offset <= 7
                                    assert action_script_offset <= 3
                                    assert event_offset <= 7
                                    #if i == 5:
                                    #    print(clone_index, this_clone.model.occupant, npc.ids[clone_index], base_model_id, model_offset, event_offset)
                                    room_bytes.append((event_offset << 5) + (action_script_offset << 3) + model_offset)
                                elif this_clone.type == ObjectType.CHEST:
                                    assert (this_clone.upper_70A7 << 4) + this_clone.lower_70A7 <= 255
                                    room_bytes.append((this_clone.upper_70A7 << 4) + this_clone.lower_70A7)
                                elif this_clone.type == ObjectType.BATTLE:
                                    battle_pack_offset = this_clone.battle_pack - base_battle_pack
                                    assert battle_pack_offset <= 15
                                    assert action_script_offset <= 15
                                    room_bytes.append((battle_pack_offset << 4) + action_script_offset)
                                room_bytes.append((this_clone.visible << 7) + this_clone.x)
                                room_bytes.append((this_clone.z_half << 7) + this_clone.y)
                                room_bytes.append((this_clone.direction << 5) + this_clone.z)
                        

                        # if utils.isclass_or_instance(npc, SingleNPC):
                        #     print(i, npc.npc.model.occupant, npc.id)
                        # else:
                        #     print(i, [n.model.occupant for n in npc.npcs], npc.ids)
                
                roomdata_output += room_bytes             

                event_tile_bytes = bytearray([this_room.music, this_room.entrance_event & 0xFF, this_room.entrance_event >> 8])
                event_tiles = this_room.event_tiles
                for e in event_tiles:
                    # byte 3
                    event_tile_bytes.append(e.event & 0xFF)
                    # byte 4
                    byte_4 = (e.event >> 8) & 0x0F
                    if e.length > 1:
                        byte_4 += 0x80
                    event_tile_bytes.append(byte_4)
                    # byte 5
                    event_tile_bytes.append(e.x + (e.nw_se_edge_active << 7))
                    # byte 6
                    event_tile_bytes.append(e.y + (e.ne_sw_edge_active << 7))
                    # byte 7
                    event_tile_bytes.append(e.z + (e.height << 5))
                    # byte 8 (optional)
                    if e.length > 1:
                        event_tile_bytes.append(((e.length - 1) & 0x0F) + (e.byte_8_bit_4 << 4) + (e.f << 7))
                eventtile_output += event_tile_bytes

                exit_bytes = bytearray([])
                exits = this_room.exit_fields

                for e in exits:

                    # byte 0
                    exit_bytes.append(e.destination & 0xFF)
                    # byte 1
                    byte_1 = (e.destination >> 8)
                    if e.length > 1 or e.f > 0:
                        byte_1 += 0x80
                    if e.destination_type == ExitType.ROOM:
                        byte_1 += 0x20
                    else:
                        byte_1 += 0x40
                        if e.byte_2_bit_0:
                            byte_1 += 0x01
                        if e.byte_2_bit_1:
                            byte_1 += 0x02
                    if e.show_message:
                        byte_1 += 0x08
                    if e.byte_2_bit_2:
                        byte_1 += 0x04
                    exit_bytes.append(byte_1)
                    #byte_2
                    exit_bytes.append((e.x & 0x7F) + (e.nw_se_edge_active << 7))
                    #byte_3
                    exit_bytes.append((e.y & 0x7F) + (e.ne_sw_edge_active << 7))
                    #byte_4
                    exit_bytes.append((e.z & 0x1F) + (e.height << 5))
                    if e.destination_type == ExitType.ROOM:
                        #byte_5
                        exit_bytes.append((e.destination_props.x & 0x7F) + (e.destination_props.x_bit_7 << 7))
                        #byte_6
                        exit_bytes.append((e.destination_props.y & 0x7F) + (e.destination_props.z_half << 7))
                        #byte_7
                        exit_bytes.append((e.destination_props.z & 0x1F) + (e.destination_props.f << 5))
                    #final byte (optional)
                    if e.length > 1 or e.f > 0:
                        exit_bytes.append(((e.length - 1) & 0x0F) + (e.f << 7))
                exit_output += exit_bytes


        empty_space = 0x0400 - len(roomdata_pointers)
        if (empty_space < 0):
            raise Exception("NPC pointer table too long: %i bytes (expected up to %i)" % (len(roomdata_pointers), 0x0400))
        else:
            for i in range(0, empty_space, 2):
                roomdata_pointers += ptr_bytes
        empty_space = 0x7C00 - len(roomdata_output)
        if (empty_space < 0):
            raise Exception("NPC data too long: %i bytes (expected up to %i)" % (len(roomdata_output), 0x7C00))
        else:
            roomdata_output += bytearray([0xFF for x in range(empty_space)])
        npcs_data = [roomdata_pointers, bytearray(roomdata_output)]

 
        empty_space = 0x0400 - len(eventtile_pointers)
        if (empty_space < 0):
            #eventtile_pointers = eventtile_pointers[0:(empty_space)]
            raise Exception("Event pointer table too long: %i bytes (expected up to %i)" % (len(eventtile_pointers), 0x0400))
        else:
            for i in range(0, empty_space, 2):
                eventtile_pointers += eventtile_ptr_bytes
        #empty_space = 0x19C8 - len(eventtile_output)
        empty_space = 0x1C00 - len(eventtile_output)
        if (empty_space < 0):
            #eventtile_output = eventtile_output[0:(empty_space)]
            #raise Exception("Event tile data too long: %i bytes (expected up to %i)" % (len(eventtile_output), 0x19C8))
            raise Exception("Event tile data too long: %i bytes (expected up to %i)" % (len(eventtile_output), 0x1C00))
        else:
            if (empty_space >= 3):
                eventtile_output += bytearray([0x00, 0x0F, 0x00]) # necessary to match 512th room header in vanilla, room does not actually exist
                empty_space = 0x1C00 - len(eventtile_output)
                #empty_space = 0x19C8 - len(eventtile_output)
            eventtile_output += bytearray([0xFF for x in range(empty_space)])
        eventtiles = [eventtile_pointers, bytearray(eventtile_output)]


        empty_space = 0x0402 - len(exit_pointers)
        if (empty_space < 0):
            #exit_pointers = exit_pointers[0:(empty_space)]
            raise Exception("Exit pointer table too long: %i bytes (expected up to %i)" % (len(exit_pointers), 0x0402))
        else:
            for i in range(0, empty_space, 2):
                exit_pointers += exit_ptr_bytes
        empty_space = 0x179F - len(exit_output)
        if (empty_space < 0):
            #exit_output = exit_output[0:(empty_space)]
            raise Exception("Exit data too long: %i bytes (expected up to %i)" % (len(exit_output), 0x179F))
        else:
            exit_output += bytearray([0xFF for x in range(empty_space)])
        exits = [exit_pointers, bytearray(exit_output)]

        if len(partitions) > 128: # bumped up to 128 from 120
            raise Exception("Too many partitions (got %i, expected up to 128)" % len(partitions))
        for _ in range(len(partitions), 128): # bumped up to 128 from 120
            partitions.append([0xFF, 0xFF, 0xFF, 0xFF])

        return npcs_data, eventtiles, exits, bytearray([p for partition in partitions for p in partition]), model_output, event_table
