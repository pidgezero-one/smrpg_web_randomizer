
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1178_pause_0',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'EVENT_1178_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_sync_1_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_1_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_1_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_1_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [45]
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_sync_2_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_2_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_2_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_2_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [45]
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_sync_3_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_3_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_3_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_3_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [45]
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_sync_4_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_4_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_4_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_4_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [45]
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_sync_5_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_5_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_5_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_5_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [45]
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_sync_6_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_6_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_6_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [85]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_6_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [45]
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_async_7_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_7_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_7_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [112]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_7_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [45]
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_async_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_8_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [4, 19, 0]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_8_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_8_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_run_dialog_9',
        "command": 'run_dialog',
        "args": [2883, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1178_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_async_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_10_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_10_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_10_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_pause_11',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1178_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_async_12_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_12_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [4, 19, 0]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_12_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_12_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_run_dialog_13',
        "command": 'run_dialog',
        "args": [2884, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1178_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_async_14_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_14_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_14_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_14_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_pause_15',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1178_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_async_16_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_16_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [4, 19, 0]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_16_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_16_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_run_dialog_17',
        "command": 'run_dialog',
        "args": [2885, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1178_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_async_18_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_18_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_18_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_18_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_pause_19',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1178_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_sync_20_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_20_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [4, 19, 0]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_20_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_20_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_async_21_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_21_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [5, 20, 0]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_21_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_21_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_run_dialog_22',
        "command": 'run_dialog',
        "args": [2886, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1178_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_sync_23_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_23_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_23_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_23_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_async_24_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_24_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_24_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_pause_25',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1178_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_async_26_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_26_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_26_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_26_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_run_dialog_27',
        "command": 'run_dialog',
        "args": [2887, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1178_action_queue_async_28',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_async_28_SUBSCRIPT_shift_southeast_steps_0',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_28_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_28_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_pause_29',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1178_action_queue_async_30',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_async_30_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_30_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_30_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_30_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_run_dialog_31',
        "command": 'run_dialog',
        "args": [2888, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1178_set_7000_to_70A0_short_mem_32',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70bc]
    },
    {
        "identifier": 'EVENT_1178_jmp_if_7000_equals_short_33',
        "command": 'jmp_if_7000_equals_short',
        "args": [0, 'EVENT_1178_run_dialog_37']
    },
    {
        "identifier": 'EVENT_1178_jmp_if_7000_equals_short_34',
        "command": 'jmp_if_7000_equals_short',
        "args": [1, 'EVENT_1178_run_dialog_42']
    },
    {
        "identifier": 'EVENT_1178_jmp_if_7000_equals_short_35',
        "command": 'jmp_if_7000_equals_short',
        "args": [2, 'EVENT_1178_run_dialog_47']
    },
    {
        "identifier": 'EVENT_1178_jmp_if_7000_equals_short_36',
        "command": 'jmp_if_7000_equals_short',
        "args": [3, 'EVENT_1178_run_dialog_52']
    },
    {
        "identifier": 'EVENT_1178_run_dialog_37',
        "command": 'run_dialog',
        "args": [2889, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1178_set_38',
        "command": 'set',
        "args": [0x70a7, 117]
    },
    {
        "identifier": 'EVENT_1178_set_39',
        "command": 'set',
        "args": [0x7000, 2894]
    },
    {
        "identifier": 'EVENT_1178_run_event_as_subroutine_40',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_1178_jmp_41',
        "command": 'jmp',
        "args": ['EVENT_1178_action_queue_async_58']
    },
    {
        "identifier": 'EVENT_1178_run_dialog_42',
        "command": 'run_dialog',
        "args": [2890, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1178_set_43',
        "command": 'set',
        "args": [0x70a7, 116]
    },
    {
        "identifier": 'EVENT_1178_set_44',
        "command": 'set',
        "args": [0x7000, 2895]
    },
    {
        "identifier": 'EVENT_1178_run_event_as_subroutine_45',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_1178_jmp_46',
        "command": 'jmp',
        "args": ['EVENT_1178_action_queue_async_58']
    },
    {
        "identifier": 'EVENT_1178_run_dialog_47',
        "command": 'run_dialog',
        "args": [2891, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1178_set_48',
        "command": 'set',
        "args": [0x70a7, 115]
    },
    {
        "identifier": 'EVENT_1178_set_49',
        "command": 'set',
        "args": [0x7000, 2896]
    },
    {
        "identifier": 'EVENT_1178_run_event_as_subroutine_50',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_1178_jmp_51',
        "command": 'jmp',
        "args": ['EVENT_1178_action_queue_async_58']
    },
    {
        "identifier": 'EVENT_1178_run_dialog_52',
        "command": 'run_dialog',
        "args": [2892, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1178_play_sound_53',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6]
    },
    {
        "identifier": 'EVENT_1178_run_dialog_54',
        "command": 'run_dialog',
        "args": [2897, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1178_set_55',
        "command": 'set',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_1178_add_coins_56',
        "command": 'add_coins',
        "args": [0x7000]
    },
    {
        "identifier": 'EVENT_1178_jmp_57',
        "command": 'jmp',
        "args": ['EVENT_1178_action_queue_async_58']
    },
    {
        "identifier": 'EVENT_1178_action_queue_async_58',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_async_58_SUBSCRIPT_shift_southeast_steps_0',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_58_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_58_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_set_bit_59',
        "command": 'set_bit',
        "args": [0x7086, 6]
    },
    {
        "identifier": 'EVENT_1178_pause_60',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'EVENT_1178_ret_61',
        "command": 'ret'
    }
]
