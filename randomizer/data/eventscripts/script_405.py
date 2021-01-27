from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_405_set_bit_0',
        "command": 'set_bit',
        "args": [0x704a, 2]
    },
    {
        "identifier": 'EVENT_405_set_7000_to_70A0_short_mem_1',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70a8]
    },
    {
        "identifier": 'EVENT_405_set_70A0_short_mem_to_7000_2',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70a9]
    },
    {
        "identifier": 'EVENT_405_start_battle_3',
        "command": 'start_battle',
        "args": [0x000a, 11]
    },
    {
        "identifier": 'EVENT_405_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [1010]
    },
    {
        "identifier": 'EVENT_405_jmp_if_object_in_level_5',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_3, Rooms._480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F, 'EVENT_405_fade_in_from_black_async_24']
    },
    {
        "identifier": 'EVENT_405_pause_action_script_6',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_405_pause_action_script_7',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_405_pause_action_script_8',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_405_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_405_action_queue_sync_9_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_405_action_queue_sync_9_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [5, 20, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_405_action_queue_sync_9_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_405_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_405_action_queue_sync_10_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_405_action_queue_sync_10_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [4, 21, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_405_action_queue_sync_10_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_405_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_405_action_queue_sync_11_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_405_action_queue_sync_11_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [5, 22, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_405_action_queue_sync_11_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_405_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_405_action_queue_async_12_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 19, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_405_action_queue_async_12_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_405_remember_last_object_13',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_405_set_bit_14',
        "command": 'set_bit',
        "args": [0x7049, 6]
    },
    {
        "identifier": 'EVENT_405_run_event_as_subroutine_15',
        "command": 'run_event_as_subroutine',
        "args": [276]
    },
    {
        "identifier": 'EVENT_405_fade_in_from_black_async_16',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_405_jmp_if_object_not_in_level_17',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F, 'EVENT_405_stop_sound_26']
    },
    {
        "identifier": 'EVENT_405_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_405_action_queue_async_18_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_405_action_queue_async_18_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_405_unsync_dialog_19',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_405_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_405_action_queue_async_20_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_405_action_queue_async_20_SUBSCRIPT_add_z_coord_1_step_1',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_405_action_queue_async_20_SUBSCRIPT_dec_z_coord_1_step_2',
                "command": 'dec_z_coord_1_step'
            }
        ]
    },
    {
        "identifier": 'EVENT_405_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_405_action_queue_async_21_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_405_action_queue_async_21_SUBSCRIPT_floating_on_1',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_405_action_queue_async_21_SUBSCRIPT_walk_1_step_northwest_2',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_405_action_queue_async_21_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_405_action_queue_async_21_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_405_action_queue_async_21_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_405_action_queue_async_21_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_405_set_bit_22',
        "command": 'set_bit',
        "args": [0x7082, 6]
    },
    {
        "identifier": 'EVENT_405_ret_23',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_405_fade_in_from_black_async_24',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_405_ret_25',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_405_stop_sound_26',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_405_stop_sound_27',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_405_stop_sound_28',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_405_stop_sound_29',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_405_stop_sound_30',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_405_stop_sound_31',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_405_stop_sound_32',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_405_stop_sound_33',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_405_stop_sound_34',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_405_stop_sound_35',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_405_stop_sound_36',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_405_stop_sound_37',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_405_stop_sound_38',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_405_stop_sound_39',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_405_stop_sound_40',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_405_stop_sound_41',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_405_stop_sound_42',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_405_set_43',
        "command": 'set',
        "args": [0x70a7, 115]
    },
    {
        "identifier": 'EVENT_405_set_44',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_405_run_event_as_subroutine_45',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_405_ret_46',
        "command": 'ret'
    }
]
