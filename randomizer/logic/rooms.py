import copy
import enum
import difflib

from . import utils
from randomizer.data import palettes, items, chests, graphics, npcs
from randomizer.data.rooms import room, rooms

from randomizer.logic import flags
from randomizer.helpers.roomobjecttables import ObjectType, ExitType

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
    byte4 += model.occupant.shadow_size << 5
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
                for npc in this_room.objects:

                    model = npc.model
                    assembled = assemble_npc(model)

                    if (
                        utils.isclass_or_instance(npc, room.Clone)
                        and not last_object_was_clone
                    ):  # begin new clone group
                        clone_group = [last_object]
                        if last_object != assembled:
                            clone_group.append(assembled)
                        clone_group.sort()
                    elif (
                        utils.isclass_or_instance(npc, room.Clone)
                        and last_object_was_clone
                    ):  # continue clone group
                        if assembled not in clone_group:
                            clone_group.append(assembled)
                            clone_group.sort()
                    elif (  # end clone group
                        not utils.isclass_or_instance(npc, room.Clone)
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
                    last_object_was_clone = utils.isclass_or_instance(npc, room.Clone)
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
                            utils.isclass_or_instance(npc, room.Clone)
                            and not last_object_was_clone
                        ):  # begin new clone group
                            clone_group = [last_object_ids, possible_ids]
                            class_clone_group = CloneGroup([last_object, npc])
                        elif (
                            utils.isclass_or_instance(npc, room.Clone)
                            and last_object_was_clone
                        ):  # continue clone group
                            clone_group.append(possible_ids)
                            class_clone_group.npcs.append(npc)
                        elif (  # end clone group
                            not utils.isclass_or_instance(npc, room.Clone)
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
                            npc, room.Clone
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
                                base_action_script = min([n.action_script for n in npc.npcs])
                                action_script_offset = this_npc.action_script - base_action_script
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
                                    event_offset = this_npc.event_script = min(event_group)
                                    
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
                            room_bytes.append((action_script_offset << 3) + model_offset)
                        elif this_npc.type == ObjectType.CHEST:
                            room_bytes.append((event_offset << 5) + (this_npc.upper_70A7 << 4) + this_npc.lower_70A7)
                        elif this_npc.type == ObjectType.BATTLE:
                            room_bytes.append((battle_pack_offset << 4) + action_script_offset)
                        room_bytes.append((this_npc.visible << 7) + this_npc.x)
                        room_bytes.append((this_npc.z_half << 7) + this_npc.y)
                        room_bytes.append((this_npc.direction << 5) + this_npc.z)

                        # write clones

                        if utils.isclass_or_instance(npc, CloneGroup):
                            for clone_index in range(1, len(npc.npcs)):
                                this_clone = npc.npcs[clone_index]
                                if this_clone.type != this_npc.type:
                                    raise Exception("room %i: mismatched clone type found" % i)
                                if this_clone.type != ObjectType.CHEST:
                                    action_script_offset = this_clone.action_script - base_action_script
                                if this_clone.type == ObjectType.OBJECT:
                                    new_event_id = new_event_group[clone_index]
                                    model_offset = npc.ids[clone_index] - base_model_id
                                    event_offset = new_event_id - min(new_event_group)
                                    assert model_offset <= 7
                                    assert action_script_offset <= 3
                                    assert event_offset <= 7
                                    #if i == 5:
                                    #    print(clone_index, this_clone.model.occupant, npc.ids[clone_index], base_model_id, model_offset, event_offset)
                                    room_bytes.append((event_offset << 5) + (action_script_offset << 3) + model_offset)
                                elif this_clone.type == ObjectType.CHEST:
                                    assert this_clone.upper_70A7 <= 15
                                    assert this_clone.lower_70A7 <= 15
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
        npcs = [roomdata_pointers, bytearray(roomdata_output)]

 
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

        return npcs, eventtiles, exits, bytearray([p for partition in partitions for p in partition]), model_output, event_table
