from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3192_move_script_to_main_thread_0',
        "command": 'move_script_to_main_thread',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3192_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3192_set_short_2',
        "command": 'set_short',
        "args": [0x700e, 0x008d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3192_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [18],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3192_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_face_mario_2',
                "command": 'face_mario',
                "args": []
            },
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [56]
            },
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_jump_to_height_8',
                "command": 'jump_to_height',
                "args": [56]
            },
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_jmp_if_bit_clear_11',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 1, 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_pause_10']
            },
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_sequence_looping_on_14',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_jump_to_height_15',
                "command": 'jump_to_height',
                "args": [56]
            },
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_play_sound_17',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_shift_southeast_steps_18',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_shift_southwest_steps_19',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_shift_southeast_steps_20',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_visibility_off_21',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_object_memory_set_bit_22',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3192_action_queue_sync_4_SUBSCRIPT_ret_23',
                "command": 'ret',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3192_run_dialog_5',
        "command": 'run_dialog',
        "args": [1644, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3192_set_bit_6',
        "command": 'set_bit',
        "args": [0x7056, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3192_set_bit_7',
        "command": 'set_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3192_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_3192_close_dialog_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3192_set_9',
        "command": 'set',
        "args": [0x70a7, 115],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3192_play_sound_10',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3192_run_dialog_11',
        "command": 'run_dialog',
        "args": [1645, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3192_put_inventory_12',
        "command": 'put_inventory',
        "args": [0x70a7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3192_close_dialog_13',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3192_clear_bit_14',
        "command": 'clear_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3192_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
