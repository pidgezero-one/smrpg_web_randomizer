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

        for i in range(len(table)):
            room = table[i]

            offset = 0x148400 + len(output)
            ptr_bytes = bytearray([offset & 0xFF, (offset >> 8) & 0xFF])

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

                if len(npcs) > 0:
                    room_bytes = bytearray([room["partition"]])

                    for n in npcs:
                        room_bytes.append((n["type"] << 4) | len(n["clones"]))
                        room_bytes.append((n["cant_float"] << 7) | (n["set_sequence_playback"] << 6) | (n["byte2_bit5"] << 5) | (n["cant_enter_doors"] << 4) | (n["face_on_trigger"] << 3) | n["speed"])
                        room_bytes.append((n["byte3_bit7"] << 7) | (n["cant_walk_through"] << 6) | (n["byte3_bit5"] << 5) | (n["cant_pass_npcs"] << 4) | (n["cant_jump_through"] << 3) | (n["cant_pass_walls"] << 2) | (n["cant_walk_under"] << 1) | n["cant_walk_up_stairs"])
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
                                room_bytes.append((c["event_offset"] << 5) | (c["action_offset"] << 3) | c["npc_id_offset"])
                            elif (n["type"] == 1):
                                room_bytes.append((c["item_offset"] << 4) | c["star_offset"])
                            elif (n["type"] == 2):
                                room_bytes.append((c["pack_offset"] << 4) | c["action_offset"])
                            room_bytes.append((c["visible"] << 7) | c["x"])
                            room_bytes.append((c["z_half"] << 7) | c["y"])
                            room_bytes.append((c["direction"] << 5) | c["z"])
                    output += room_bytes


                # event tiles

                # bytes 0-2
                event_tile_bytes = bytearray([room["music"], room["entrance_event"] & 0xFF, room["entrance_event"] >> 8])
                event_tiles = room["event_tiles"]
                for e in event_tiles:
                    # byte 3
                    event_tile_bytes.append(e["event"] & 0xFF)
                    # byte 4
                    byte_4 = e["event"] >> 8
                    if e["length"] > 1 or e["f"] > 0:
                        byte_4 |= 0x80
                    event_tile_bytes.append(byte_4)
                    # byte 5
                    event_tile_bytes.append(e["x"] | (e["nw_se_edge_active"] << 7))
                    # byte 6
                    event_tile_bytes.append(e["y"] | (e["ne_sw_edge_active"] << 7))
                    # byte 7
                    event_tile_bytes.append(e["z"] | (e["height"] << 5))
                    # byte 8 (optional)
                    if e["length"] > 1 or e["f"] != 0:
                        event_tile_bytes.append(((e["length"] - 1) & 0x0F) | (e["f"] << 7))
                eventtile_output += event_tile_bytes


                # exits

                exit_bytes = bytearray()
                exits = room["exit_fields"]
                print("")
                print("")
                print(i)
                print('0x%x' % exit_offset)
                for e in exits:
                    print(e)
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
                        
                print(' '.join('{:02x}'.format(x) for x in exit_bytes))
                print("")
                print("")
                exit_output += exit_bytes




        empty_space = 0x0400 - len(pointers)
        if (empty_space < 0):
            #pointers = pointers[0:(empty_space)]
            raise Exception("NPC pointer table too long: %i bytes (expected up to %i)" % (len(pointers), 0x0400))
        else:
            for i in range(0, empty_space, 2):
                pointers += ptr_bytes
        empty_space = 0x6C17 - len(output)
        if (empty_space < 0):
            #output = output[0:(empty_space)]
            raise Exception("NPC data too long: %i bytes (expected up to %i)" % (len(output), 0x6C17))
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
        empty_space = 0x19C8 - len(eventtile_output)
        if (empty_space < 0):
            #eventtile_output = eventtile_output[0:(empty_space)]
            raise Exception("Event tile data too long: %i bytes (expected up to %i)" % (len(eventtile_output), 0x19C8))
        else:
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

        return npcs, eventtiles, exits


