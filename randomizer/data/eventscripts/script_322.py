from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_322_set_action_script_sync_0',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_322_set_bit_7_offset_1',
        "command": 'set_bit_7_offset',
        "args": [0x015c, []]
    },
    {
        "identifier": 'EVENT_322_set_bit_7_offset_2',
        "command": 'set_bit_7_offset',
        "args": [0x015e, []]
    },
    {
        "identifier": 'EVENT_322_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 2, 'EVENT_322_jmp_if_bit_set_20']
    },
    {
        "identifier": 'EVENT_322_set_bit_4',
        "command": 'set_bit',
        "args": [0x7081, 2]
    },
    {
        "identifier": 'EVENT_322_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_322_action_queue_sync_5_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_322_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_322_action_queue_sync_6_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_322_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_322_action_queue_sync_7_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_322_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_322_action_queue_sync_8_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_322_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_322_action_queue_sync_9_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [14, 33, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_322_action_queue_sync_9_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_322_action_queue_sync_9_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_322_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_322_action_queue_async_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_322_action_queue_async_10_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_322_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_322_action_queue_sync_11_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_322_action_queue_sync_11_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_322_action_queue_sync_11_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_322_action_queue_sync_11_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [16]
            }
        ]
    },
    {
        "identifier": 'EVENT_322_fade_in_from_black_sync_12',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_322_remember_last_object_13',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_322_run_dialog_14',
        "command": 'run_dialog',
        "args": [554, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_322_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_322_action_queue_async_15_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_322_action_queue_async_15_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_322_action_queue_async_15_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_322_action_queue_async_15_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_322_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_322_action_queue_sync_16_SUBSCRIPT_shift_northwest_steps_0',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_322_action_queue_sync_16_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_322_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_322_action_queue_async_17_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_322_action_queue_async_17_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_322_remember_last_object_18',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_322_ret_19',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_322_jmp_if_bit_set_20',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 1, 'EVENT_322_jmp_if_bit_set_32']
    },
    {
        "identifier": 'EVENT_322_jmp_if_bit_clear_21',
        "command": 'jmp_if_bit_clear',
        "args": [0x7081, 5, 'EVENT_322_jmp_if_bit_set_32']
    },
    {
        "identifier": 'EVENT_322_remove_from_current_level_22',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_322_remove_from_current_level_23',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_322_remove_from_current_level_24',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_322_remove_from_current_level_25',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_322_remove_from_current_level_26',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_322_action_queue_async_27',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_322_action_queue_async_27_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [15, 29, 4, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_322_set_action_script_sync_28',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 128]
    },
    {
        "identifier": 'EVENT_322_set_action_script_sync_29',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 138]
    },
    {
        "identifier": 'EVENT_322_fade_in_from_black_async_30',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_322_ret_31',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_322_jmp_if_bit_set_32',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 5, 'EVENT_322_remove_from_current_level_22']
    },
    {
        "identifier": 'EVENT_322_jmp_if_bit_set_33',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 6, 'EVENT_322_remove_from_current_level_22']
    },
    {
        "identifier": 'EVENT_322_jmp_to_event_34',
        "command": 'jmp_to_event',
        "args": [257]
    }
]
