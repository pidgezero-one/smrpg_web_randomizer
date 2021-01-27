from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1178_pause_0',
        "command": 'pause',
        "args": [1]
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
                "args": [1]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_1_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_1_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
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
                "args": [1]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_2_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_2_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
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
                "args": [1]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_3_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_3_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
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
                "args": [1]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_4_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_4_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
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
                "args": [1]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_5_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_5_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
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
                "args": [1]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_6_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [85]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_6_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
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
                "args": [1]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_7_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [112]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_7_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
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
        "identifier": 'EVENT_1178_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_async_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_9_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_9_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_9_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_pause_10',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1178_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_async_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_11_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [4, 19, 0]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_11_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_11_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            }
        ]
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
                "identifier": 'EVENT_1178_action_queue_async_12_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_12_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_12_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_pause_13',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1178_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_async_14_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_14_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [4, 19, 0]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_14_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_14_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_async_15_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_15_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_15_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_15_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_pause_16',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1178_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_sync_17_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_17_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [4, 19, 0]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_17_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_17_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_async_18_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_18_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [5, 20, 0]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_18_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_18_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_sync_19_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_19_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_19_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1178_action_queue_sync_19_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_async_20_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_20_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_20_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_pause_21',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1178_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_async_22_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_22_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_22_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_22_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_async_23_SUBSCRIPT_shift_southeast_steps_0',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_23_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_23_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_pause_24',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1178_action_queue_async_25',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_async_25_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_25_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_25_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_25_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_set_7000_to_70A0_short_mem_26',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70bc]
    },
    {
        "identifier": 'EVENT_1178_jmp_if_7000_equals_short_27',
        "command": 'jmp_if_7000_equals_short',
        "args": [0, 'EVENT_1178_set_31']
    },
    {
        "identifier": 'EVENT_1178_jmp_if_7000_equals_short_28',
        "command": 'jmp_if_7000_equals_short',
        "args": [1, 'EVENT_1178_set_35']
    },
    {
        "identifier": 'EVENT_1178_jmp_if_7000_equals_short_29',
        "command": 'jmp_if_7000_equals_short',
        "args": [2, 'EVENT_1178_set_39']
    },
    {
        "identifier": 'EVENT_1178_jmp_if_7000_equals_short_30',
        "command": 'jmp_if_7000_equals_short',
        "args": [3, 'EVENT_1178_play_sound_43']
    },
    {
        "identifier": 'EVENT_1178_set_31',
        "command": 'set',
        "args": [0x70a7, 117]
    },
    {
        "identifier": 'EVENT_1178_set_32',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_1178_run_event_as_subroutine_33',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_1178_jmp_34',
        "command": 'jmp',
        "args": ['EVENT_1178_action_queue_async_48']
    },
    {
        "identifier": 'EVENT_1178_set_35',
        "command": 'set',
        "args": [0x70a7, 116]
    },
    {
        "identifier": 'EVENT_1178_set_36',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_1178_run_event_as_subroutine_37',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_1178_jmp_38',
        "command": 'jmp',
        "args": ['EVENT_1178_action_queue_async_48']
    },
    {
        "identifier": 'EVENT_1178_set_39',
        "command": 'set',
        "args": [0x70a7, 115]
    },
    {
        "identifier": 'EVENT_1178_set_40',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_1178_run_event_as_subroutine_41',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_1178_jmp_42',
        "command": 'jmp',
        "args": ['EVENT_1178_action_queue_async_48']
    },
    {
        "identifier": 'EVENT_1178_play_sound_43',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6]
    },
    {
        "identifier": 'EVENT_1178_run_dialog_44',
        "command": 'run_dialog',
        "args": [2897, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1178_set_45',
        "command": 'set',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_1178_add_coins_46',
        "command": 'add_coins',
        "args": [0x7000]
    },
    {
        "identifier": 'EVENT_1178_jmp_47',
        "command": 'jmp',
        "args": ['EVENT_1178_action_queue_async_48']
    },
    {
        "identifier": 'EVENT_1178_action_queue_async_48',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1178_action_queue_async_48_SUBSCRIPT_shift_southeast_steps_0',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_48_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1178_action_queue_async_48_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1178_set_bit_49',
        "command": 'set_bit',
        "args": [0x7086, 6]
    },
    {
        "identifier": 'EVENT_1178_pause_50',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1178_ret_51',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_52',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_53',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_54',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_55',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_56',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_57',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_58',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_59',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_60',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_61',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_62',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_63',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_64',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_65',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_66',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_67',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_68',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_69',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_70',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_71',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_72',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_73',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_74',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_75',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_76',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_77',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_78',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_79',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_80',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_81',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_82',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_83',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_84',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_85',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_86',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_87',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_88',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_89',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_stop_sound_90',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1178_ret_91',
        "command": 'ret'
    }
]
