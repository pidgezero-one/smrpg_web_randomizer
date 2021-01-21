from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1077_set_action_script_async_0',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_1077_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7093, 0, 'EVENT_1077_ret_17']
    },
    {
        "identifier": 'EVENT_1077_pause_2',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1077_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1077_action_queue_async_3_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1077_action_queue_async_3_SUBSCRIPT_sequence_looping_off_1',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_1077_action_queue_async_3_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1077_pause_4',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1077_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1077_action_queue_async_5_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1077_run_dialog_6',
        "command": 'run_dialog',
        "args": [2582, AreaObjects.NPC_12, [_0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1077_pause_script_resume_on_next_dialog_page_a_7',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_1077_pause_script_resume_on_next_dialog_page_a_8',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_1077_pause_script_resume_on_next_dialog_page_a_9',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_1077_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1077_action_queue_async_10_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1077_pause_script_resume_on_next_dialog_page_a_11',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_1077_unsync_dialog_12',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_1077_close_dialog_13',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_1077_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1077_action_queue_sync_14_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1077_action_queue_sync_14_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1077_action_queue_sync_14_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1077_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1077_action_queue_async_15_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1077_action_queue_async_15_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1077_action_queue_async_15_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1077_action_queue_async_15_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [16, 29]
            },
            {
                "identifier": 'EVENT_1077_action_queue_async_15_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1077_action_queue_async_15_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [19]
            },
            {
                "identifier": 'EVENT_1077_action_queue_async_15_SUBSCRIPT_shift_northwest_steps_6',
                "command": 'shift_northwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1077_jmp_16',
        "command": 'jmp',
        "args": ['EVENT_1071_jmp_if_bit_clear_0']
    },
    {
        "identifier": 'EVENT_1077_ret_17',
        "command": 'ret'
    }
]
