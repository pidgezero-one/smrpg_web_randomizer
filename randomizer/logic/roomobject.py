import copy
import enum

from . import utils
from randomizer.data import palettes, items, chests, graphics
from randomizer.data.roomobjecttables import ObjectType, Initiator, PostBattle, RadialDirection, Music, Edge, ExitType, Locations, Rooms, PartitionBufferTypes, PartitionMainSpace
from randomizer.logic import flags

class RoomObjects:
    def __init__(self):
        self.output = []

    def assemble_from_table(table):

        #NPCs

        pointers = bytearray()
        eventtile_pointers = bytearray()
        exit_pointers = bytearray()

        output = []
        eventtile_output = []
        exit_output = []

        partitions = []

        for i in range(len(table)):
            room = table[i]

            #print("")
            #print("")
            #print("")

            offset = 0x148400 + len(output)
            #print("%i: 0x%x" % (i, offset))
            #print(len(output))
            ptr_bytes = bytearray([offset & 0xFF, (offset >> 8) & 0xFF])
            #print(' '.join('{:02x}'.format(x) for x in ptr_bytes))

            eventtile_offset = 0x20E400 + len(eventtile_output)
            eventtile_ptr_bytes = bytearray([eventtile_offset & 0xFF, (eventtile_offset >> 8) & 0xFF])

            exit_offset = 0x1D3166 + len(exit_output)
            exit_ptr_bytes = bytearray([exit_offset & 0xFF, (exit_offset >> 8) & 0xFF])

            pointers += ptr_bytes
            eventtile_pointers += eventtile_ptr_bytes
            exit_pointers += exit_ptr_bytes

            if room is not None:

                #objects

                npcs = room["objects"]
                room_bytes = bytearray([])

                if room["partition"] is not None:
                    p = room["partition"]
                    partition_byte_1 = p["allow_extra_sprite_buffer"] * 0x10 
                    partition_byte_1 += (p["ally_sprite_buffer_size"] << 5)
                    partition_byte_1 += (p["extra_sprite_buffer_size"] & 0x0F)
                    partition_byte_1 += p["full_palette_buffer"] * 0x80 
                    partition_byte_2 = p["buffer_a"]["type"] & 0x07
                    partition_byte_2 += (p["buffer_a"]["main_buffer_space"] << 4)
                    partition_byte_2 += p["buffer_a"]["index_in_main_buffer"] * 0x80
                    partition_byte_3 = p["buffer_b"]["type"] & 0x07
                    partition_byte_3 += (p["buffer_b"]["main_buffer_space"] << 4)
                    partition_byte_3 += p["buffer_b"]["index_in_main_buffer"] * 0x80
                    partition_byte_4 = p["buffer_c"]["type"] & 0x07
                    partition_byte_4 += (p["buffer_c"]["main_buffer_space"] << 4)
                    partition_byte_4 += p["buffer_c"]["index_in_main_buffer"] * 0x80
                    partition_bytes = [partition_byte_1, partition_byte_2, partition_byte_3, partition_byte_4]
                    partition_index = None
                    for index in range(len(partitions)):
                        if partition_bytes == partitions[index]:
                            partition_index = index
                    # print(i, p)
                    if partition_index is None:
                        partition_index = len(partitions)
                        partitions.append(partition_bytes)
                    print("room: %i, partition: %i," % (i, partition_index))
                    print(p)
                    print("\n")
                    room_bytes = bytearray([partition_index])

                if len(npcs) > 0:
                    for n in npcs:
                       # print(n)
                        room_bytes.append((n["type"] << 4) | len(n["clones"]))
                        room_bytes.append((n["cant_float"] << 7) | (n["set_sequence_playback"] << 6) | (n["byte2_bit5"] << 5) | (n["cant_enter_doors"] << 4) | (n["face_on_trigger"] << 3) | n["speed"])
                        room_bytes.append((n["byte3_bit7"] << 7) | (n["cant_walk_through"] << 6) | (n["byte3_bit5"] << 5) | (n["cant_pass_npcs"] << 4) | (n["cant_jump_through"] << 3) | (n["cant_pass_walls"] << 2) | (n["cant_walk_under"] << 1) | n["cant_walk_up_stairs"])
                        #print(i)
                        room_bytes.append(((n["model"] << 2) & 0xFF) | (n["cant_move_if_in_air"] << 1) | n["slidable_along_walls"])
                        room_bytes.append(((n["action_script"] & 0x0F) << 4) | (n["model"] >> 6))
                        room_bytes.append((n["byte7_upper2"] << 6) | (n["action_script"] >> 4))
                        if (n["type"] <= 1):
                            room_bytes.append(n["event_script"] & 0xFF)
                            room_bytes.append((n["initiator"] << 4) | (n["event_script"] >> 8))
                        else:
                            room_bytes.append(n["battle_pack"] & 0xFF)
                            room_bytes.append((n["initiator"] << 4) | n["after_battle"])
                        if (n["type"] == 0):
                            room_bytes.append((n["event_offset"] << 5) | (n["action_offset"] << 3) | n["npc_id_offset"])
                        elif (n["type"] == 1):
                            room_bytes.append((n["item_offset"] << 4) | n["star_offset"])
                        elif (n["type"] == 2):
                            room_bytes.append((n["pack_offset"] << 4) | n["action_offset"])
                        room_bytes.append((n["visible"] << 7) | n["x"])
                        room_bytes.append((n["z_half"] << 7) | n["y"])
                        room_bytes.append((n["direction"] << 5) | n["z"])
                        for c in n["clones"]:
                            if (n["type"] == 0):
                                try:
                                    room_bytes.append((c["event_offset"] << 5) | (c["action_offset"] << 3) | c["npc_id_offset"])
                                except Exception as e:
                                    print(room)
                                    raise e
                            elif (n["type"] == 1):
                                room_bytes.append((c["item_offset"] << 4) | c["star_offset"])
                            elif (n["type"] == 2):
                                room_bytes.append((c["pack_offset"] << 4) | c["action_offset"])
                            room_bytes.append((c["visible"] << 7) | c["x"])
                            room_bytes.append((c["z_half"] << 7) | c["y"])
                            room_bytes.append((c["direction"] << 5) | c["z"])
                #print(' '.join('{:02x}'.format(x) for x in room_bytes))
                #print(len(output))
                output += room_bytes
                #print(len(output))


                # event tiles

                # bytes 0-2
                event_tile_bytes = bytearray([room["music"], room["entrance_event"] & 0xFF, room["entrance_event"] >> 8])
                event_tiles = room["event_tiles"]
                #print(room)
                for e in event_tiles:
                    # byte 3
                    event_tile_bytes.append(e["event"] & 0xFF)
                    # byte 4
                    byte_4 = e["event"] >> 8
                    if e["length"] > 1:
                        byte_4 |= 0x80
                    event_tile_bytes.append(byte_4)
                    # byte 5
                    event_tile_bytes.append(e["x"] | (e["nw_se_edge_active"] << 7))
                    # byte 6
                    event_tile_bytes.append(e["y"] | (e["ne_sw_edge_active"] << 7))
                    # byte 7
                    event_tile_bytes.append(e["z"] | (e["height"] << 5))
                    # byte 8 (optional)
                    if e["length"] > 1:
                        if "byte_8_bit_4" in e:
                            byte_8_bit_4 = (e["byte_8_bit_4"] << 4)
                        else:
                            byte_8_bit_4 = 0
                        event_tile_bytes.append(((e["length"] - 1) & 0x0F) | byte_8_bit_4 | (e["f"] << 7))
                eventtile_output += event_tile_bytes


                # exits

                exit_bytes = bytearray()
                exits = room["exit_fields"]

                for e in exits:

                    # byte 0
                    exit_bytes.append(e["destination"] & 0xFF)
                    # byte 1
                    byte_1 = (e["destination"] >> 8)
                    if e["length"] > 1 or e["f"] > 0:
                        byte_1 |= 0x80
                    if e["destination_type"] == 0:
                        byte_1 |= 0x20
                    else:
                        byte_1 |= 0x40
                        if e["destination_props"]["byte_2_bit_0"]:
                            byte_1 |= 0x01
                        if e["destination_props"]["byte_2_bit_1"]:
                            byte_1 |= 0x02
                    if e["show_message"]:
                        byte_1 |= 0x08
                    if e["byte_2_bit_2"]:
                        byte_1 |= 0x04
                    exit_bytes.append(byte_1)
                    #byte_2
                    exit_bytes.append((e["x"] & 0x7F) | (e["nw_se_edge_active"] << 7))
                    #byte_3
                    exit_bytes.append((e["y"] & 0x7F) | (e["ne_sw_edge_active"] << 7))
                    #byte_4
                    exit_bytes.append((e["z"] & 0x1F) | (e["height"] << 5))
                    if (e["destination_type"] == 0):
                        #byte_5
                        exit_bytes.append((e["destination_props"]["x"] & 0x7F) | (e["destination_props"]["x_bit_7"] << 7))
                        #byte_6
                        exit_bytes.append((e["destination_props"]["y"] & 0x7F) | (e["destination_props"]["z_half"] << 7))
                        #byte_7
                        exit_bytes.append((e["destination_props"]["z"] & 0x1F) | (e["destination_props"]["f"] << 5))
                    #final byte (optional)
                    if e["length"] > 1 or e["f"] > 0:
                        exit_bytes.append(((e["length"] - 1) & 0x0F) | (e["f"] << 7))
                exit_output += exit_bytes




        empty_space = 0x0400 - len(pointers)
        if (empty_space < 0):
            #pointers = pointers[0:(empty_space)]
            raise Exception("NPC pointer table too long: %i bytes (expected up to %i)" % (len(pointers), 0x0400))
        else:
            for i in range(0, empty_space, 2):
                pointers += ptr_bytes
        empty_space = 0x7C00 - len(output)
        #empty_space = 0x6C17 - len(output)
        if (empty_space < 0):
            #output = output[0:(empty_space)]
            #raise Exception("NPC data too long: %i bytes (expected up to %i)" % (len(output), 0x6C17))
            raise Exception("NPC data too long: %i bytes (expected up to %i)" % (len(output), 0x7C00))
        else:
            output += bytearray([0xFF for x in range(empty_space)])
        npcs = [pointers, bytearray(output)]

 
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
            raise Exception("Too many partitions (got %i, expected up to 120)" % len(partitions))
        for _ in range(len(partitions), 128): # bumped up to 128 from 120
            partitions.append([0xFF, 0xFF, 0xFF, 0xFF])

        return npcs, eventtiles, exits, bytearray([p for partition in partitions for p in partition])


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

special_case_rooms = [205, 463, 466, 477, 233, 236, 230, 232]
# 205 - complicated spiney sequence
# 463, 466 - barrel count room and logic problem room need this for some reason
requires_coin_buffer = [242]
# 301 - breaks chest sprites if you use extra sprite buffer for coins

def set_partitions(world):
    pandorite_rooms = []
    hidon_rooms = []
    for c in world.chest_locations:
        if utils.isclass_or_instance(c.item, items.PandoriteFight):
            pandorite_rooms.extend(c.rooms)
        elif utils.isclass_or_instance(c.item, items.HidonFight):
            hidon_rooms.extend(c.rooms)


    for room_index, room in enumerate(world.rooms):
        if room_index in [376, 377, 459, 460, 461, 462]: # rooms that always need triple empty + ex 1
            partition = {
                "ally_sprite_buffer_size": 1,
                "allow_extra_sprite_buffer": True,
                "extra_sprite_buffer_size": 1,
                "buffer_a": {
                    "type": PartitionBufferTypes.EMPTY_3,
                    "main_buffer_space": PartitionMainSpace._0_BYTES,
                    "index_in_main_buffer": True,
                },
                "buffer_b": {
                    "type": PartitionBufferTypes.EMPTY_3,
                    "main_buffer_space": PartitionMainSpace._0_BYTES,
                    "index_in_main_buffer": True,
                },
                "buffer_c": {
                    "type": PartitionBufferTypes.EMPTY_3,
                    "main_buffer_space": PartitionMainSpace._0_BYTES,
                    "index_in_main_buffer": True,
                },
                "full_palette_buffer": True,
            }
            world.rooms[room_index]["partition"] = partition
        # elif room_index in [477]: # I assume this terra cotta room needs this because it uses high sequence #s
        #     partition = {
        #         "ally_sprite_buffer_size": 1,
        #         "allow_extra_sprite_buffer": False,
        #         "extra_sprite_buffer_size": 0,
        #         "buffer_a": {
        #             "type": PartitionBufferTypes.EMPTY_3,
        #             "main_buffer_space": PartitionMainSpace._0_BYTES,
        #             "index_in_main_buffer": True,
        #         },
        #         "buffer_b": {
        #             "type": PartitionBufferTypes.EMPTY_3,
        #             "main_buffer_space": PartitionMainSpace._0_BYTES,
        #             "index_in_main_buffer": True,
        #         },
        #         "buffer_c": {
        #             "type": PartitionBufferTypes.EMPTY_3,
        #             "main_buffer_space": PartitionMainSpace._0_BYTES,
        #             "index_in_main_buffer": True,
        #         },
        #         "full_palette_buffer": True,
        #     }
        #     world.rooms[room_index]["partition"] = partition
        elif room is not None and len(room["objects"]) > 0:
            partition = room["partition"]
            original_partition = copy.deepcopy(partition)
            partition = {
                "ally_sprite_buffer_size": 1,
                "allow_extra_sprite_buffer": False,
                "extra_sprite_buffer_size": 0,
                "buffer_a": {
                    "type": PartitionBufferTypes.EMPTY_3,
                    "main_buffer_space": PartitionMainSpace._0_BYTES,
                    "index_in_main_buffer": True,
                },
                "buffer_b": {
                    "type": PartitionBufferTypes.EMPTY_3,
                    "main_buffer_space": PartitionMainSpace._0_BYTES,
                    "index_in_main_buffer": True,
                },
                "buffer_c": {
                    "type": PartitionBufferTypes.EMPTY_3,
                    "main_buffer_space": PartitionMainSpace._0_BYTES,
                    "index_in_main_buffer": True,
                },
                "full_palette_buffer": True,
            }
            if original_partition is not None:
                partition["extra_sprite_buffer_size"] = original_partition["extra_sprite_buffer_size"]
                partition["allow_extra_sprite_buffer"] = original_partition["allow_extra_sprite_buffer"]
                partition["full_palette_buffer"] = original_partition["full_palette_buffer"]

            ally_buffer = 1
            
            packet_size = partition["extra_sprite_buffer_size"]
            if partition["allow_extra_sprite_buffer"]:
                packet_size += 1
            npcs = room["objects"]
            # 512, 513, 518

            has_star_chest = False

            priority_buffers = []
            npc_buffers = []
            packet_buffers = []

            if room_index in special_case_rooms:
                priority_buffers.append(PartitionBufferTypes.EMPTY_3)

            ambiguous_coin_chest = AmbiguousCoin.none
            has_conundrum_clones = False
            for npc in npcs:
                model = world.models[npc["model"]]
                if model["cannot_clone"] and len(npc["clones"]) > 0:
                    has_conundrum_clones = True


            # consider chest contents and packets
            for c in world.chest_locations:
                if room_index in c.rooms or (512 in c.rooms and room_index in pandorite_rooms) or (513 in c.rooms and room_index in hidon_rooms):
                    if utils.isclass_or_instance(c, chests.Chest):
                        if utils.isclass_or_instance(c.item, items.StarPiece):
                            has_star_chest = True
                    elif utils.isclass_or_instance(c, chests.PacketItem):
                        packet_size += 1
                    if not world.settings.is_flag_enabled(flags.QuickHitCoins) and (utils.isclass_or_instance(c, chests.Chest) or utils.isclass_or_instance(c, chests.PacketItem)) and (utils.isclass_or_instance(c.item, items.FrogCoin) or utils.isclass_or_instance(c.item, items.MultiFrogCoin) or utils.isclass_or_instance(c.item, items.InfiniteCoins) or utils.isclass_or_instance(c.item, items.Coins)):
                        if (utils.isclass_or_instance(c.item, items.Coins) and c.item.chest_70A7_lower != 1) or utils.isclass_or_instance(c.item, items.MultiFrogCoin) or utils.isclass_or_instance(c.item, items.InfiniteCoins):
                            ambiguous_coin_chest = AmbiguousCoin.multi
                        elif utils.isclass_or_instance(c.item, items.FrogCoin) or (utils.isclass_or_instance(c.item, items.Coins) and c.item.chest_70A7_lower == 1):
                            ambiguous_coin_chest = AmbiguousCoin.one
                        # if room_index not in requires_coin_buffer:
                        #     ambiguous_coin_chest = True
                        #     packet_size = max(4, packet_size) # apparently this might work???
                        # else:
                        #     packet_buffers.append(PartitionBufferTypes.COINS)
                    elif utils.isclass_or_instance(c, chests.Chest) and utils.isclass_or_instance(c.item, items.SlotMachineChest):
                        packet_buffers.append(PartitionBufferTypes.COINS) # slot frog coin
            if has_star_chest:
                packet_size += 1
                # todo: invincibility stars

            last_sprite = -1

            existing_formats_in_room = []
            buffer_order = []

            # clones can have diff gridplane dimensions... what to do?

            decloned = []
            for npc in npcs:
                decloned.append(npc)
                if len(npc["clones"]) > 0:
                    for c in npc["clones"]:
                        clone = copy.deepcopy(npc)
                        clone["clones"] = []
                        if "npc_id_offset" in c:
                            clone["model"] += c["npc_id_offset"]
                        if "event_offset" in c:
                            clone["event_script"] += c["event_offset"]
                        if "action_offset" in c:
                            clone["action_script"] += c["action_offset"]
                        if "battle_pack" in c:
                            clone["action_offset"] += c["pack_offset"]
                        decloned.append(clone)


            # get all npc models
            for npc_index, npc in enumerate(decloned):
                model = world.models[npc["model"]]
                print(npc_index, room_index, model)
                if model["sprite"] < 575 and not model["cannot_clone"]:
                    sprite = graphics.sprites[model["sprite"]]
                    animation_pack = graphics.animations[sprite.animation_num]

                    buf = None
                    if model["sprite"] <= 30:
                        # ally_buffer += 1
                        if room_index in [203, 204, 205]:
                            world.models[npc["model"]]["cannot_clone"] = True
                            continue
                        elif room_index == 230:
                            if model["sprite"] < 7:
                                packet_size = max(4, packet_size)
                            else:
                                packet_size = max(3, packet_size)
                    #else:
                    if model["sprite"] == 94:
                        priority_buffers.append(PartitionBufferTypes.TREASURE_CHEST)
                    elif model["sprite"] in [192, 193, 194, 202]:
                        priority_buffers.append(PartitionBufferTypes.COINS)

                    # if len(npc["clones"]) > 0: # might need to consider non-clones too
                    #     if not animation_pack.properties.molds[0].gridplane:
                    #         print("warning: room %i has non-gridplane clones" % room_index)
                    #     else:
                    #         if animation_pack.properties.molds[0].tiles[0].format <= 1:
                    #             buf = PartitionBufferTypes._4_SPRITES_PER_ROW
                    #         else:
                    #             buf = PartitionBufferTypes._3_SPRITES_PER_ROW
                    #         if buf != last_type:
                    #             last_type = buf
                    #             npc_buffers.append(buf)


                    # if len(npc["clones"]) > 0: # might need to consider non-clones too
                    #     if not animation_pack.properties.molds[0].gridplane:
                    #         print("warning: room %i has non-gridplane clones" % room_index)
                    elif not animation_pack.properties.molds[0].gridplane:
                        priority_buffers.append(PartitionBufferTypes.EMPTY_3)
                    else:
                        # if len(npc["clones"]) > 0: # doing this because it fixed the broken goomba animation in BW1. Revisit if it doesnt work for other rooms
                        if animation_pack.properties.molds[0].tiles[0].format <= 1:
                            buf = PartitionBufferTypes._4_SPRITES_PER_ROW
                        else:
                            buf = PartitionBufferTypes._3_SPRITES_PER_ROW
                        #if model["sprite"] != last_sprite:
                        # do we always need to initiate a new buffer if format >= 3?
                        # if (model["sprite"] != last_sprite and (buf in existing_formats_in_room or len(npc["clones"]) > 0)) or (len(npc["clones"]) > 0 and buf == PartitionBufferTypes._3_SPRITES_PER_ROW):
                        if buf not in existing_formats_in_room:
                            existing_formats_in_room.append(buf)
                            if len(npc["clones"]) > 0:
                                npc_buffers.append(buf)
                        elif model["sprite"] != last_sprite:
                            npc_buffers.append(buf)
                        elif len(npc_buffers) == 0 or npc_buffers[len(npc_buffers) - 1] != buf:
                            npc_buffers.append(buf)
                    last_sprite = model["sprite"] # might need to use npc id and not sprite id
                    
                        # use Cannot Clone version of party member in mushroom way 2?



            # models = []
            # for model in models:
            #     if model["sprite"] < 512:
            #         sprite = graphics.sprites[model["sprite"]]
            #         animation_pack = graphics.animations[sprite.animation_num]

            #         if model["sprite"] == 94:
            #             npc_buffers.append(PartitionBufferTypes.TREASURE_CHEST)
            #         elif model["sprite"] in [192, 193, 194, 202]:
            #             npc_buffers.append(PartitionBufferTypes.COINS)
            #         elif animation_pack.properties.vram_size > 2048 or not animation_pack.properties.molds[0].gridplane:
            #             npc_buffers.append(PartitionBufferTypes.EMPTY_3)
            #         elif 
            #         elif animation_pack.properties.molds[0].tiles[0].format <= 1:
            #             npc_buffers.append(PartitionBufferTypes._4_SPRITES_PER_ROW)
            #         else:
            #             npc_buffers.append(PartitionBufferTypes._3_SPRITES_PER_ROW)
            # models = list_unique(models)
            # models = [world.models[m] for m in models]

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

            if ambiguous_coin_chest is not AmbiguousCoin.none:
                #if if PartitionBufferTypes.TREASURE_CHEST in priority_buffers and npc_buffers[0:2] == [PartitionBufferTypes._3_SPRITES_PER_ROW] * 2:
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

            print(room_index, priority_buffers, npc_buffers, packet_buffers)

            final_buffers = [None] * 3

            buffers = priority_buffers + npc_buffers + packet_buffers

            if PartitionBufferTypes.TREASURE_CHEST in priority_buffers:
                final_buffers[0] = PartitionBufferTypes.TREASURE_CHEST
                buffers.remove(PartitionBufferTypes.TREASURE_CHEST)
            elif PartitionBufferTypes.EMPTY_3 in priority_buffers:
                final_buffers[0] = PartitionBufferTypes.EMPTY_3
                buffers.remove(PartitionBufferTypes.EMPTY_3)

            if PartitionBufferTypes.COINS in buffers:
                final_buffers[2] = PartitionBufferTypes.COINS
                buffers.remove(PartitionBufferTypes.COINS)

            idx = 0
            for i in range(0, 3):
                if final_buffers[i] is None and idx < len(buffers):
                    final_buffers[i] = buffers[idx]
                    idx += 1

            for i in range(0, 3):
                if final_buffers[i] is None:
                    final_buffers[i] = PartitionBufferTypes.EMPTY_3


            # if len(buffers) > 3:
            #     order = copy.deepcopy(partition_priority)
            #     order.reverse()
            #     for o in order:
            #         if o in buffers:
            #             buffers.remove(o)
            #             if len(buffers) <= 3:
            #                 break

            # if len(buffers) < 3:
            #     buffers += [PartitionBufferTypes.EMPTY_3] * (3 - min(3, len(buffers)))

            print(room_index, final_buffers)

            found = False
            buffers_indexes = ["buffer_a", "buffer_b", "buffer_c"]
            for i, dex in enumerate(buffers_indexes):
                partition[dex]["type"] = final_buffers[i]
                if original_partition is not None and not found:
                    for j in buffers_indexes:
                        if original_partition[j]["type"] == final_buffers[i] and original_partition[j]["main_buffer_space"] > partition[dex]["main_buffer_space"] and not found:
                            partition[dex]["main_buffer_space"] = original_partition[j]["main_buffer_space"]
                            partition[dex]["index_in_main_buffer"] = original_partition[j]["index_in_main_buffer"]
                            found = True


            partition['ally_sprite_buffer_size'] = ally_buffer
            
            if packet_size > 0:
                partition["allow_extra_sprite_buffer"] = True
                partition["extra_sprite_buffer_size"] = packet_size - 1
            else:
                partition["allow_extra_sprite_buffer"] = False
                partition["extra_sprite_buffer_size"] = 0

            world.rooms[room_index]["partition"] = partition
