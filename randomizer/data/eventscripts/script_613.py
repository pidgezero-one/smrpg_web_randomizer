from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_613_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_613_action_queue_async_0_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 248, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_613_action_queue_async_0_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_613_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x709f, 0, 'EVENT_613_action_queue_async_34']
    },
    {
        "identifier": 'EVENT_613_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 4, 'EVENT_257_fade_in_from_black_async_0']
    },
    {
        "identifier": 'EVENT_613_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 3, 'EVENT_613_action_queue_async_6']
    },
    {
        "identifier": 'EVENT_613_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_613_action_queue_async_4_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [4, 19, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_613_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_613_jmp_if_bit_set_7']
    },
    {
        "identifier": 'EVENT_613_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_613_action_queue_async_6_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [4, 20, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_613_action_queue_async_6_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_613_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 3, 'EVENT_257_fade_in_from_black_async_0']
    },
    {
        "identifier": 'EVENT_613_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 320]
    },
    {
        "identifier": 'EVENT_613_fade_in_from_black_async_9',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_613_unsync_action_script_10',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_613_set_short_mem_11',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70d7]
    },
    {
        "identifier": 'EVENT_613_jmp_if_var_equals_short_12',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_613_run_dialog_18']
    },
    {
        "identifier": 'EVENT_613_run_dialog_13',
        "command": 'run_dialog',
        "args": [999, AreaObjects.NPC_0, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_613_pause_14',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_613_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_613_action_queue_async_15_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_613_action_queue_async_15_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_613_action_queue_async_15_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_613_action_queue_async_15_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_613_run_dialog_16',
        "command": 'run_dialog',
        "args": [1000, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_613_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_613_set_action_script_sync_30']
    },
    {
        "identifier": 'EVENT_613_run_dialog_18',
        "command": 'run_dialog',
        "args": [980, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_613_pause_19',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_613_set_action_script_async_20',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_613_pause_21',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_613_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_613_action_queue_sync_22_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_613_action_queue_sync_22_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_613_action_queue_sync_22_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_613_action_queue_sync_22_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_613_action_queue_sync_22_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_613_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_613_action_queue_sync_23_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_613_action_queue_sync_23_SUBSCRIPT_face_north_1',
                "command": 'face_north'
            }
        ]
    },
    {
        "identifier": 'EVENT_613_remember_last_object_24',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_613_run_dialog_25',
        "command": 'run_dialog',
        "args": [2476, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_613_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_613_action_queue_sync_26_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_613_action_queue_sync_26_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_613_action_queue_async_27',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_613_action_queue_async_27_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_613_action_queue_async_27_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_613_action_queue_async_27_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_613_action_queue_async_27_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_613_pause_28',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_613_run_dialog_29',
        "command": 'run_dialog',
        "args": [989, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_613_set_action_script_sync_30',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 321]
    },
    {
        "identifier": 'EVENT_613_set_bit_31',
        "command": 'set_bit',
        "args": [0x709f, 1]
    },
    {
        "identifier": 'EVENT_613_set_bit_32',
        "command": 'set_bit',
        "args": [0x7042, 3]
    },
    {
        "identifier": 'EVENT_613_ret_33',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_613_action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_613_action_queue_async_34_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 21, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_613_set_action_script_sync_35',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 978]
    },
    {
        "identifier": 'EVENT_613_fade_in_from_black_async_36',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_613_ret_37',
        "command": 'ret'
    }
]
