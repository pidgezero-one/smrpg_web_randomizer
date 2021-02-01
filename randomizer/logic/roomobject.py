class RoomObjects:
    def __init__(self):
        self.output = []

    def assemble_from_table(table):
        pointers = bytearray()
        output = []
        for room in table:
            offset = 0x148400 + len(output)
            ptr_bytes = bytearray([offset & 0xFF, (offset >> 8) & 0xFF])
            pointers += ptr_bytes
            if room is not None:
                room_bytes = bytearray([room["partition"]])
                npcs = room["objects"]
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
        offset = len(output)
        ptr_bytes = bytearray([offset & 0xFF, (offset >> 8) & 0xFF])
        pointers += ptr_bytes
        empty_space = 0x0400 - len(pointers)
        if (empty_space < 0):
            pointers = pointers[0:(empty_space)]
        else:
            for i in range(0, empty_space, 2):
                pointers += ptr_bytes
        empty_space = 0x7C00 - len(output)
        if (empty_space < 0):
            output = output[0:(empty_space)]
        else:
            output += bytearray([0xFF for x in range(empty_space)])
        return [pointers, bytearray(output)]