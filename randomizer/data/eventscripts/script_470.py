from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_470_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7085, 4, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_jmp_fork_mario_on_object_2',
        "command": 'jmp_fork_mario_on_object',
        "args": ['EVENT_470_jmp_if_bit_set_32', 'EVENT_470_jmp_if_bit_set_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 4, 'EVENT_470_action_queue_async_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7084, 0, 'EVENT_470_play_sound_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_set_bit_5',
        "command": 'set_bit',
        "args": [0x7084, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_play_sound_6',
        "command": 'play_sound',
        "args": [Sounds._063_YOSHI_TALK, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_run_dialog_8',
        "command": 'run_dialog',
        "args": [2512, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_jmp_9',
        "command": 'jmp',
        "args": ['EVENT_470_start_embedded_action_script_async_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_play_sound_10',
        "command": 'play_sound',
        "args": [Sounds._063_YOSHI_TALK, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_unsync_dialog_11',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_close_dialog_12',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_run_event_as_subroutine_13',
        "command": 'run_event_as_subroutine',
        "args": [3587],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_run_dialog_14',
        "command": 'run_dialog',
        "args": [897, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_jmp_if_dialog_option_b_15',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_470_run_event_as_subroutine_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_set_action_script_async_16',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_run_dialog_17',
        "command": 'run_dialog',
        "args": [898, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_pause_action_script_18',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_start_embedded_action_script_async_20',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_470_start_embedded_action_script_async_20_SUBSCRIPT_set_700C_to_object_coord_0',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.NPC_9, Coords.F]
            },
            {
                "identifier": 'EVENT_470_start_embedded_action_script_async_20_SUBSCRIPT_add_1',
                "command": 'add',
                "args": [0x700c, 4]
            },
            {
                "identifier": 'EVENT_470_start_embedded_action_script_async_20_SUBSCRIPT_mem_700C_and_const_2',
                "command": 'mem_700C_and_const',
                "args": [0x0007]
            },
            {
                "identifier": 'EVENT_470_start_embedded_action_script_async_20_SUBSCRIPT_face_east_3',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_470_start_embedded_action_script_async_20_SUBSCRIPT_set_short_mem_4',
                "command": 'set_short_mem',
                "args": [0x703e, 0x700c]
            },
            {
                "identifier": 'EVENT_470_start_embedded_action_script_async_20_SUBSCRIPT_fixed_f_coord_on_5',
                "command": 'fixed_f_coord_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_470_set_bit_21',
        "command": 'set_bit',
        "args": [0x7044, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_ret_22',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_run_event_as_subroutine_23',
        "command": 'run_event_as_subroutine',
        "args": [3587],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_pause_24',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_set_action_script_async_25',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_run_dialog_26',
        "command": 'run_dialog',
        "args": [899, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_ret_27',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_action_queue_async_28',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_470_action_queue_async_28_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_470_action_queue_async_28_SUBSCRIPT_face_mario_1',
                "command": 'face_mario',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_470_play_sound_29',
        "command": 'play_sound',
        "args": [Sounds._063_YOSHI_TALK, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_run_dialog_30',
        "command": 'run_dialog',
        "args": [900, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_jmp_31',
        "command": 'jmp',
        "args": ['EVENT_470_start_embedded_action_script_async_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_jmp_if_bit_set_32',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 4, 'EVENT_470_pause_action_script_34'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_ret_33',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_pause_action_script_34',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_pause_action_script_35',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_action_queue_async_36',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_470_action_queue_async_36_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_470_action_queue_async_36_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
        ]
    },
    {
        "identifier": 'EVENT_470_db_37',
        "command": 'db',
        "args": [0xfd, 0x45],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_freeze_camera_38',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_set_bit_39',
        "command": 'set_bit',
        "args": [0x7044, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_set_bit_40',
        "command": 'set_bit',
        "args": [0x7044, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_set_7016_to_object_xyz_41',
        "command": 'set_7016_to_object_xyz',
        "args": [0x9d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_add_short_42',
        "command": 'add_short',
        "args": [0x701a, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_action_queue_async_43',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_470_action_queue_async_43_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_470_action_queue_async_43_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_470_action_queue_async_43_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_470_action_queue_async_43_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_470_action_queue_async_43_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_470_action_queue_async_43_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x98]
            },
            {
                "identifier": 'EVENT_470_action_queue_async_43_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_470_action_queue_async_43_SUBSCRIPT_jmp_7',
                "command": 'jmp',
                "args": ['EVENT_470_non_embedded_action_queue_46']
            },
        ]
    },
    {
        "identifier": 'EVENT_470_action_queue_async_44',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_470_action_queue_async_44_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_470_jmp_45',
        "command": 'jmp',
        "args": ['EVENT_470_action_queue_async_47'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_non_embedded_action_queue_46',
        "command": 'non_embedded_action_queue',
        "args": [bytearray(b'\xfd\x9e')],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_action_queue_async_47',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_470_action_queue_async_47_SUBSCRIPT_transfer_to_object_xy_0',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.MARIO]
            },
            {
                "identifier": 'EVENT_470_action_queue_async_47_SUBSCRIPT_sequence_looping_off_1',
                "command": 'sequence_looping_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_470_remember_last_object_48',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_apply_solidity_mod_49',
        "command": 'apply_solidity_mod',
        "args": [Rooms._034_YOSTER_ISLE, 3, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_apply_solidity_mod_50',
        "command": 'apply_solidity_mod',
        "args": [Rooms._034_YOSTER_ISLE, 5, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_apply_solidity_mod_51',
        "command": 'apply_solidity_mod',
        "args": [Rooms._034_YOSTER_ISLE, 7, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_run_background_event_52',
        "command": 'run_background_event',
        "args": [469, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_470_ret_53',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
