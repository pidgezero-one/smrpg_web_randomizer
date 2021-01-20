from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_293_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x709c, 7, 'EVENT_395_run_dialog_37'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 3, 'EVENT_293_run_dialog_45'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_293_jmp_if_bit_clear_30'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 7, 'EVENT_395_jmp_if_bit_set_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_pause_action_script_4',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 5, 'EVENT_293_pause_action_script_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 6, 'EVENT_293_pause_action_script_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_jmp_if_bit_clear_7',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 6, 'EVENT_293_run_dialog_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_run_dialog_8',
        "command": 'run_dialog',
        "args": [532, AreaObjects.NPC_3, [_0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_jmp_9',
        "command": 'jmp',
        "args": ['EVENT_293_action_queue_sync_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_run_dialog_10',
        "command": 'run_dialog',
        "args": [64, AreaObjects.NPC_3, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_jmp_if_bit_set_0',
                "command": 'jmp_if_bit_set',
                "args": [0x7043, 6, 'EVENT_293_action_queue_sync_11_SUBSCRIPT_start_loop_n_times_6']
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_set_700C_to_object_coord_1',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.NPC_3, Coords.F]
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_add_2',
                "command": 'add',
                "args": [0x700c, 2]
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_mem_700C_and_const_3',
                "command": 'mem_700C_and_const',
                "args": [0x0007]
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_face_east_4',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_start_loop_n_times_6',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_add_7',
                "command": 'add',
                "args": [0x700c, 6]
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_mem_700C_and_const_8',
                "command": 'mem_700C_and_const',
                "args": [0x0007]
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_face_east_9',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_end_loop_11',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_start_loop_n_times_12',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_add_13',
                "command": 'add',
                "args": [0x700c, 2]
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_mem_700C_and_const_14',
                "command": 'mem_700C_and_const',
                "args": [0x0007]
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_face_east_15',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_end_loop_17',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_start_loop_n_times_18',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_add_19',
                "command": 'add',
                "args": [0x700c, 6]
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_mem_700C_and_const_20',
                "command": 'mem_700C_and_const',
                "args": [0x0007]
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_face_east_21',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_end_loop_23',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_293_action_queue_sync_11_SUBSCRIPT_face_mario_24',
                "command": 'face_mario',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_293_jmp_if_bit_set_12',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'EVENT_293_remember_last_object_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_run_dialog_13',
        "command": 'run_dialog',
        "args": [65, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_set_bit_14',
        "command": 'set_bit',
        "args": [0x7043, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_remember_last_object_15',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_unsync_dialog_16',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_close_dialog_17',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_resume_action_script_18',
        "command": 'resume_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_ret_19',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_pause_action_script_20',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_set_action_script_sync_21',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 99],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_run_dialog_22',
        "command": 'run_dialog',
        "args": [578, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_pause_action_script_23',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_pause_24',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_jmp_if_object_in_air_25',
        "command": 'jmp_if_object_in_air',
        "args": [AreaObjects.MEM_70A8, 'EVENT_293_pause_24'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_run_dialog_26',
        "command": 'run_dialog',
        "args": [579, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_start_embedded_action_script_async_27',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_293_start_embedded_action_script_async_27_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_293_start_embedded_action_script_async_27_SUBSCRIPT_floating_on_1',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_293_start_embedded_action_script_async_27_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            },
        ]
    },
    {
        "identifier": 'EVENT_293_set_action_script_sync_28',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 21],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_ret_29',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_jmp_if_bit_clear_30',
        "command": 'jmp_if_bit_clear',
        "args": [0x7083, 2, 'EVENT_395_jmp_if_bit_set_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_run_dialog_31',
        "command": 'run_dialog',
        "args": [2231, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_pause_32',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_jmp_if_bit_set_33',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 2, 'EVENT_293_set_40'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_add_frog_coins_34',
        "command": 'add_frog_coins',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_play_sound_35',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_set_bit_36',
        "command": 'set_bit',
        "args": [0x705d, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_run_dialog_37',
        "command": 'run_dialog',
        "args": [2243, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_set_bit_38',
        "command": 'set_bit',
        "args": [0x705d, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_ret_39',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_set_40',
        "command": 'set',
        "args": [0x7000, 524],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_set_41',
        "command": 'set',
        "args": [0x70a7, 116],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_run_event_as_subroutine_42',
        "command": 'run_event_as_subroutine',
        "args": [3828],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_set_bit_43',
        "command": 'set_bit',
        "args": [0x705d, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_ret_44',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_run_dialog_45',
        "command": 'run_dialog',
        "args": [2242, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_293_ret_46',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
