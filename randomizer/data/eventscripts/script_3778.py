from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3778_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_0_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_0_SUBSCRIPT_shift_xy_pixels_1',
                "command": 'shift_xy_pixels',
                "args": [250, 253]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_0_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3778_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_2_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [9]
            },
        ]
    },
    {
        "identifier": 'EVENT_3778_set_short_3',
        "command": 'set_short',
        "args": [0x703e, 0x0010],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 59],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_run_dialog_6',
        "command": 'run_dialog',
        "args": [1912, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_jmp_if_dialog_option_b_7',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3778_set_bit_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_run_dialog_8',
        "command": 'run_dialog',
        "args": [1913, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_set_bit_9',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_10_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_10_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [38]
            },
        ]
    },
    {
        "identifier": 'EVENT_3778_set_11',
        "command": 'set',
        "args": [0x7000, 49151],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_jmp_if_7000_any_bits_set_12',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0], 'EVENT_3778_jmp_if_7000_any_bits_set_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_13_SUBSCRIPT_dec_short_0',
                "command": 'dec_short',
                "args": [0x703e]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_13_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_13_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_13_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_13_SUBSCRIPT_end_all_4',
                "command": 'end_all',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3778_jmp_if_7000_any_bits_set_14',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[1], 'EVENT_3778_jmp_if_7000_any_bits_set_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_15_SUBSCRIPT_dec_short_0',
                "command": 'dec_short',
                "args": [0x703e]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_15_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_15_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_15_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_15_SUBSCRIPT_end_all_4',
                "command": 'end_all',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3778_jmp_if_7000_any_bits_set_16',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[2], 'EVENT_3778_jmp_if_7000_any_bits_set_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_17_SUBSCRIPT_dec_short_0',
                "command": 'dec_short',
                "args": [0x703e]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_17_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_17_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_17_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_17_SUBSCRIPT_end_all_4',
                "command": 'end_all',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3778_jmp_if_7000_any_bits_set_18',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[3], 'EVENT_3778_jmp_if_7000_any_bits_set_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_19_SUBSCRIPT_dec_short_0',
                "command": 'dec_short',
                "args": [0x703e]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_19_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_19_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_19_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_19_SUBSCRIPT_end_all_4',
                "command": 'end_all',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3778_jmp_if_7000_any_bits_set_20',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[4], 'EVENT_3778_jmp_if_7000_any_bits_set_22'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_21_SUBSCRIPT_dec_short_0',
                "command": 'dec_short',
                "args": [0x703e]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_21_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_21_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_21_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_21_SUBSCRIPT_end_all_4',
                "command": 'end_all',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3778_jmp_if_7000_any_bits_set_22',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[5], 'EVENT_3778_jmp_if_7000_any_bits_set_24'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_23_SUBSCRIPT_dec_short_0',
                "command": 'dec_short',
                "args": [0x703e]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_23_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_23_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_23_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_23_SUBSCRIPT_end_all_4',
                "command": 'end_all',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3778_jmp_if_7000_any_bits_set_24',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[6], 'EVENT_3778_jmp_if_7000_any_bits_set_26'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_25',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_25_SUBSCRIPT_dec_short_0',
                "command": 'dec_short',
                "args": [0x703e]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_25_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_25_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_25_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_25_SUBSCRIPT_end_all_4',
                "command": 'end_all',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3778_jmp_if_7000_any_bits_set_26',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_3778_jmp_if_7000_any_bits_set_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_27',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_27_SUBSCRIPT_dec_short_0',
                "command": 'dec_short',
                "args": [0x703e]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_27_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_27_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_27_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_27_SUBSCRIPT_end_all_4',
                "command": 'end_all',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3778_jmp_if_7000_any_bits_set_28',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[8], 'EVENT_3778_jmp_if_7000_any_bits_set_30'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_29',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_29_SUBSCRIPT_dec_short_0',
                "command": 'dec_short',
                "args": [0x703e]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_29_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_29_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_29_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_29_SUBSCRIPT_end_all_4',
                "command": 'end_all',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3778_jmp_if_7000_any_bits_set_30',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[9], 'EVENT_3778_jmp_if_7000_any_bits_set_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_31_SUBSCRIPT_dec_short_0',
                "command": 'dec_short',
                "args": [0x703e]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_31_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_31_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_31_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_31_SUBSCRIPT_end_all_4',
                "command": 'end_all',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3778_jmp_if_7000_any_bits_set_32',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[10], 'EVENT_3778_jmp_if_7000_any_bits_set_34'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_33',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_33_SUBSCRIPT_dec_short_0',
                "command": 'dec_short',
                "args": [0x703e]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_33_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_33_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_33_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_33_SUBSCRIPT_end_all_4',
                "command": 'end_all',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3778_jmp_if_7000_any_bits_set_34',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[11], 'EVENT_3778_jmp_if_7000_any_bits_set_36'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_35',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_35_SUBSCRIPT_dec_short_0',
                "command": 'dec_short',
                "args": [0x703e]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_35_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_35_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_35_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_35_SUBSCRIPT_end_all_4',
                "command": 'end_all',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3778_jmp_if_7000_any_bits_set_36',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[12], 'EVENT_3778_jmp_if_7000_any_bits_set_38'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_37',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_37_SUBSCRIPT_dec_short_0',
                "command": 'dec_short',
                "args": [0x703e]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_37_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_37_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_37_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_37_SUBSCRIPT_end_all_4',
                "command": 'end_all',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3778_jmp_if_7000_any_bits_set_38',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[13], 'EVENT_3778_jmp_if_7000_any_bits_set_40'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_39',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_14],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_39_SUBSCRIPT_dec_short_0',
                "command": 'dec_short',
                "args": [0x703e]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_39_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_39_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_39_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_39_SUBSCRIPT_end_all_4',
                "command": 'end_all',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3778_jmp_if_7000_any_bits_set_40',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[14], 'EVENT_3778_jmp_if_7000_any_bits_set_42'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_41',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_41_SUBSCRIPT_dec_short_0',
                "command": 'dec_short',
                "args": [0x703e]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_41_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_41_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_41_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_41_SUBSCRIPT_end_all_4',
                "command": 'end_all',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3778_jmp_if_7000_any_bits_set_42',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[15], 'EVENT_3778_action_queue_async_44'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_43',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_43_SUBSCRIPT_dec_short_0',
                "command": 'dec_short',
                "args": [0x703e]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_43_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_43_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_43_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_43_SUBSCRIPT_end_all_4',
                "command": 'end_all',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_44',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_44_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [9]
            },
        ]
    },
    {
        "identifier": 'EVENT_3778_play_music_default_volume_45',
        "command": 'play_music_default_volume',
        "args": [Music._36_EXPLANATION],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_ret_46',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_47',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_48',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_49',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_50',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_51',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_52',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_53',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_54',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_55',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_56',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_57',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_58',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_59',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_60',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_61',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_62',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_63',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_64',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_65',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_66',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_67',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_68',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_69',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_70',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_71',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_72',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_73',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_74',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_75',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_stop_sound_76',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3778_ret_77',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
