from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2526_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2526_action_queue_sync_0_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2526_action_queue_sync_0_SUBSCRIPT_shift_west_pixels_1',
                "command": 'shift_west_pixels',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_2526_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_2526_action_queue_sync_1_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2526_action_queue_sync_1_SUBSCRIPT_shift_west_pixels_1',
                "command": 'shift_west_pixels',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_2526_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2526_action_queue_sync_2_SUBSCRIPT_shift_west_pixels_0',
                "command": 'shift_west_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2526_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_14],
        "subscript": [
            {
                "identifier": 'EVENT_2526_action_queue_async_3_SUBSCRIPT_shift_southeast_pixels_0',
                "command": 'shift_southeast_pixels',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_2526_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x708b, 6, 'EVENT_2526_fade_in_from_black_async_26']
    },
    {
        "identifier": 'EVENT_2526_set_bit_5',
        "command": 'set_bit',
        "args": [0x708b, 6]
    },
    {
        "identifier": 'EVENT_2526_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2526_summon_to_current_level_7',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_16]
    },
    {
        "identifier": 'EVENT_2526_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_2526_action_queue_async_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2526_action_queue_async_8_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2526_action_queue_async_8_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2526_run_dialog_9',
        "command": 'run_dialog',
        "args": [3117, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2526_pause_script_resume_on_next_dialog_page_a_10',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_2526_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_2526_action_queue_async_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2526_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2526_unsync_dialog_12',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_2526_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x7091, 6, 'EVENT_2526_run_dialog_16']
    },
    {
        "identifier": 'EVENT_2526_run_dialog_14',
        "command": 'run_dialog',
        "args": [3153, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2526_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_2526_action_queue_async_17']
    },
    {
        "identifier": 'EVENT_2526_run_dialog_16',
        "command": 'run_dialog',
        "args": [3118, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2526_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_2526_action_queue_async_17_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2526_pause_18',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'EVENT_2526_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_2526_action_queue_async_19_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2526_action_queue_async_19_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2526_action_queue_async_19_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2526_action_queue_async_19_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [27, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2526_unsync_dialog_20',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_2526_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_2526_action_queue_async_21_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2526_run_dialog_22',
        "command": 'run_dialog',
        "args": [3119, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2526_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_2526_action_queue_async_23_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2526_action_queue_async_23_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2526_action_queue_async_23_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2526_action_queue_async_23_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2526_remove_from_current_level_24',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_16]
    },
    {
        "identifier": 'EVENT_2526_ret_25',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2526_fade_in_from_black_async_26',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2526_ret_27',
        "command": 'ret'
    }
]
