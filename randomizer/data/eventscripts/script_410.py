from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_410_set_bit_0',
        "command": 'set_bit',
        "args": [0x704a, 2]
    },
    {
        "identifier": 'EVENT_410_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8]
    },
    {
        "identifier": 'EVENT_410_set_short_mem_2',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000]
    },
    {
        "identifier": 'EVENT_410_start_battle_3',
        "command": 'start_battle',
        "args": [0x000b, 11]
    },
    {
        "identifier": 'EVENT_410_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [1010]
    },
    {
        "identifier": 'EVENT_410_set_bit_5',
        "command": 'set_bit',
        "args": [0x7082, 6]
    },
    {
        "identifier": 'EVENT_410_jmp_if_present_in_current_level_6',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_2, 'EVENT_410_fade_in_from_black_async_48']
    },
    {
        "identifier": 'EVENT_410_set_bit_7',
        "command": 'set_bit',
        "args": [0x7082, 7]
    },
    {
        "identifier": 'EVENT_410_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_410_action_queue_async_8_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_410_action_queue_async_8_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [7, 44, 6, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_410_action_queue_async_8_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_410_fade_in_from_black_async_9',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_410_pause_action_script_10',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_410_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_410_action_queue_async_11_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_410_action_queue_async_11_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_410_action_queue_async_11_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_410_pause_12',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_410_set_action_script_async_13',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_410_pause_14',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_410_pause_15',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_410_set_16',
        "command": 'set',
        "args": [0x70a7, 115]
    },
    {
        "identifier": 'EVENT_410_set_17',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_410_run_event_as_subroutine_18',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_410_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_410_action_queue_async_19_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_410_action_queue_async_19_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_410_action_queue_async_19_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_410_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_410_action_queue_async_20_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_410_pause_action_script_21',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_410_set_22',
        "command": 'set',
        "args": [0x70a9, 20]
    },
    {
        "identifier": 'EVENT_410_run_event_as_subroutine_23',
        "command": 'run_event_as_subroutine',
        "args": [278]
    },
    {
        "identifier": 'EVENT_410_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_410_action_queue_async_24_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_410_action_queue_async_24_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_410_pause_25',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_410_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 23]
    },
    {
        "identifier": 'EVENT_410_action_queue_async_27',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_410_action_queue_async_27_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_410_action_queue_async_27_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_410_action_queue_async_27_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_410_action_queue_async_27_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_410_action_queue_async_27_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_410_set_action_script_sync_28',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_410_ret_29',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_410_stop_sound_30',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_410_stop_sound_31',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_410_stop_sound_32',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_410_stop_sound_33',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_410_stop_sound_34',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_410_stop_sound_35',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_410_stop_sound_36',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_410_stop_sound_37',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_410_stop_sound_38',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_410_stop_sound_39',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_410_stop_sound_40',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_410_stop_sound_41',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_410_stop_sound_42',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_410_stop_sound_43',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_410_stop_sound_44',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_410_stop_sound_45',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_410_stop_sound_46',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_410_ret_47',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_410_fade_in_from_black_async_48',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_410_set_action_script_sync_49',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_410_ret_50',
        "command": 'ret'
    }
]
