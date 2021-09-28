import copy

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
                        print("{room: %i, json: \"%r\", id: %i}," % (i, p, len(partitions)))
                        partition_index = len(partitions)
                        partitions.append(partition_bytes)
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

        if len(partitions) > 120:
            raise Exception("Too many partitions (got %i, expected up to 120)" % len(partitions))
        for _ in range(len(partitions), 120):
            partitions.append([0, 0, 0, 0])

        return npcs, eventtiles, exits, bytearray([p for partition in partitions for p in partition])


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

def set_partitions(world):
    pandorite_rooms = []
    hidon_rooms = []
    for c in world.chest_locations:
        if utils.isclass_or_instance(c.item, items.PandoriteFight):
            pandorite_rooms.extend(c.rooms)
        elif utils.isclass_or_instance(c.item, items.HidonFight):
            hidon_rooms.extend(c.rooms)


    for room_index, room in enumerate(world.rooms):
        if room is not None and len(room["objects"]) > 0:
            partition = room["partition"]
            if partition is None:
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


            packet_size = partition["extra_sprite_buffer_size"]
            npcs = room["objects"]
            # 512, 513, 518

            # get all npc models
            models = []
            for npc in npcs:
                models.append(npc["model"])
                if len(npc["clones"]) > 0:
                    for clone in npc["clones"]:
                        if "npc_id_offset" in clone:
                            models.append(npc["model"] + clone["npc_id_offset"])

            has_star_chest = False

            npc_buffers = []
            packet_buffers = []

            # consider chest contents and packets
            for c in world.chest_locations:
                if room_index in c.rooms or (512 in c.rooms and room_index in pandorite_rooms) or (513 in c.rooms and room_index in hidon_rooms):
                    if utils.isclass_or_instance(c, chests.Chest):
                        if utils.isclass_or_instance(c.item, items.StarPiece):
                            has_star_chest = True
                    elif utils.isclass_or_instance(c, chests.PacketItem):
                        packet_size += 1
                    if not world.settings.is_flag_enabled(flags.QuickHitCoins) and (utils.isclass_or_instance(c, chests.Chest) or utils.isclass_or_instance(c, chests.PacketItem)) and (utils.isclass_or_instance(c.item, items.Coins) or utils.isclass_or_instance(c.item, items.FrogCoin) or utils.isclass_or_instance(c.item, items.MultiFrogCoin)):
                        packet_buffers.append(PartitionBufferTypes.COINS) # coin chests
            if has_star_chest:
                packet_size += 1
                # todo: invincibility stars

            models = list_unique(models)
            models = [world.models[m] for m in models]

            for model in models:
                if model["sprite"] < 512:
                    sprite = graphics.sprites[model["sprite"]]
                    animation_pack = graphics.animations[sprite.animation_num]

                    if model["sprite"] == 94:
                        npc_buffers.append(PartitionBufferTypes.TREASURE_CHEST)
                    elif model["sprite"] in [192, 193, 194, 202]:
                        npc_buffers.append(PartitionBufferTypes.COINS)
                    elif animation_pack.properties.vram_size > 2048 or not animation_pack.properties.molds[0].gridplane:
                        npc_buffers.append(PartitionBufferTypes.EMPTY_3)
                    elif animation_pack.properties.molds[0].tiles[0].format <= 1:
                        npc_buffers.append(PartitionBufferTypes._4_SPRITES_PER_ROW)
                    else:
                        npc_buffers.append(PartitionBufferTypes._3_SPRITES_PER_ROW)

            npc_buffers = list_unique(npc_buffers)
            packet_buffers = list_unique(packet_buffers)

            if PartitionBufferTypes.COINS in npc_buffers and PartitionBufferTypes.COINS in packet_buffers:
                npc_buffers.remove(PartitionBufferTypes.COINS)

            print(room_index, npc_buffers, packet_buffers)

            buffers = npc_buffers + packet_buffers

            if len(buffers) > 3:
                order = copy.deepcopy(partition_priority)
                order.reverse()
                for o in order:
                    if o in buffers:
                        buffers.remove(o)
                        if len(buffers) <= 3:
                            break

            if len(buffers) < 3:
                buffers += [PartitionBufferTypes.EMPTY_3] * (3 - min(3, len(buffers)))

            print(room_index, buffers)

            partition["buffer_a"]["type"] = buffers[0]
            partition["buffer_b"]["type"] = buffers[1]
            partition["buffer_c"]["type"] = buffers[2]

            partition['ally_sprite_buffer_size'] = 1
            
            if packet_size > 0:
                partition["allow_extra_sprite_buffer"] = True
                partition["extra_sprite_buffer_size"] = packet_size

            world.rooms[room_index]["partition"] = partition
