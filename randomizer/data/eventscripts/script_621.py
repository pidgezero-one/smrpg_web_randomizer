from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_621_set_7000_to_current_level_0',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_621_jmp_if_7000_equals_short_1',
        "command": 'jmp_if_7000_equals_short',
        "args": [12, 'EVENT_621_jmp_if_bit_set_86']
    },
    {
        "identifier": 'EVENT_621_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 1, 'EVENT_621_jmp_if_bit_set_109']
    },
    {
        "identifier": 'EVENT_621_run_dialog_3',
        "command": 'run_dialog',
        "args": [1011, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_621_pause_4',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_621_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_621_action_queue_async_5_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_621_action_queue_async_5_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_621_action_queue_async_5_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_621_action_queue_async_5_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_621_action_queue_async_5_SUBSCRIPT_walk_to_xy_coords_4',
                "command": 'walk_to_xy_coords',
                "args": [6, 62]
            },
            {
                "identifier": 'EVENT_621_action_queue_async_5_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_621_set_7000_to_70A0_short_mem_6',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70b8]
    },
    {
        "identifier": 'EVENT_621_jmp_if_7000_equals_short_7',
        "command": 'jmp_if_7000_equals_short',
        "args": [3, 'EVENT_621_set_10']
    },
    {
        "identifier": 'EVENT_621_set_8',
        "command": 'set',
        "args": [0x70a9, 27]
    },
    {
        "identifier": 'EVENT_621_jmp_9',
        "command": 'jmp',
        "args": ['EVENT_621_action_queue_sync_11']
    },
    {
        "identifier": 'EVENT_621_set_10',
        "command": 'set',
        "args": [0x70a9, 26]
    },
    {
        "identifier": 'EVENT_621_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_621_action_queue_sync_11_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_11_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_11_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_11_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_11_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_621_pause_12',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_621_play_sound_13',
        "command": 'play_sound',
        "args": [Sounds._004_JUMP, 6]
    },
    {
        "identifier": 'EVENT_621_set_action_script_async_14',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 636]
    },
    {
        "identifier": 'EVENT_621_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_621_action_queue_sync_15_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_15_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_15_SUBSCRIPT_floating_on_2',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_15_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_621_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_621_action_queue_sync_16_SUBSCRIPT_shift_southeast_steps_0',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_16_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_621_pause_17',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_621_fade_out_to_black_async_18',
        "command": 'fade_out_to_black_async'
    },
    {
        "identifier": 'EVENT_621_enter_area_19',
        "command": 'enter_area',
        "args": [Rooms._006_MARRYMORE_INN_2F, RadialDirections.NORTHEAST, 15, 52, 1, [_0x68Flags.Z_HALF]]
    },
    {
        "identifier": 'EVENT_621_fade_in_from_black_sync_20',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_621_set_7000_to_70A0_short_mem_21',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70b8]
    },
    {
        "identifier": 'EVENT_621_jmp_if_7000_equals_short_22',
        "command": 'jmp_if_7000_equals_short',
        "args": [3, 'EVENT_621_set_25']
    },
    {
        "identifier": 'EVENT_621_set_23',
        "command": 'set',
        "args": [0x70a9, 22]
    },
    {
        "identifier": 'EVENT_621_jmp_24',
        "command": 'jmp',
        "args": ['EVENT_621_pause_26']
    },
    {
        "identifier": 'EVENT_621_set_25',
        "command": 'set',
        "args": [0x70a9, 21]
    },
    {
        "identifier": 'EVENT_621_pause_26',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_621_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_621_action_queue_sync_27_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_27_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_27_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_27_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_27_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_621_action_queue_sync_28',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_621_action_queue_sync_28_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_28_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_28_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_28_SUBSCRIPT_floating_on_3',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_28_SUBSCRIPT_transfer_to_xyzf_4',
                "command": 'transfer_to_xyzf',
                "args": [15, 52, 3, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_28_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_28_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_28_SUBSCRIPT_walk_1_step_northeast_7',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_28_SUBSCRIPT_shift_northwest_steps_8',
                "command": 'shift_northwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_621_remember_last_object_29',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_621_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_621_action_queue_sync_30_SUBSCRIPT_shift_northwest_steps_0',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_30_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_621_action_queue_sync_31',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_621_action_queue_sync_31_SUBSCRIPT_shift_northwest_steps_0',
                "command": 'shift_northwest_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_621_pause_32',
        "command": 'pause',
        "args": [50]
    },
    {
        "identifier": 'EVENT_621_fade_out_to_black_async_33',
        "command": 'fade_out_to_black_async'
    },
    {
        "identifier": 'EVENT_621_enter_area_34',
        "command": 'enter_area',
        "args": [Rooms._011_MARRYMORE_INN_3F, RadialDirections.NORTHEAST, 12, 73, 1, [_0x68Flags.Z_HALF]]
    },
    {
        "identifier": 'EVENT_621_set_7000_to_70A0_short_mem_35',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70b8]
    },
    {
        "identifier": 'EVENT_621_jmp_if_7000_equals_short_36',
        "command": 'jmp_if_7000_equals_short',
        "args": [3, 'EVENT_621_set_39']
    },
    {
        "identifier": 'EVENT_621_set_37',
        "command": 'set',
        "args": [0x70a9, 25]
    },
    {
        "identifier": 'EVENT_621_jmp_38',
        "command": 'jmp',
        "args": ['EVENT_621_pause_40']
    },
    {
        "identifier": 'EVENT_621_set_39',
        "command": 'set',
        "args": [0x70a9, 24]
    },
    {
        "identifier": 'EVENT_621_pause_40',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_621_fade_in_from_black_sync_41',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_621_action_queue_sync_42',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_621_action_queue_sync_42_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_42_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_42_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_42_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_42_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_42_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_42_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_42_SUBSCRIPT_face_southwest_7',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_42_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_42_SUBSCRIPT_clear_solidity_bits_9',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_42_SUBSCRIPT_shift_northeast_steps_10',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_621_action_queue_sync_43',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_621_action_queue_sync_43_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_43_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_43_SUBSCRIPT_floating_on_2',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_43_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_43_SUBSCRIPT_transfer_to_xyzf_4',
                "command": 'transfer_to_xyzf',
                "args": [12, 73, 3, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_43_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_43_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_43_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_43_SUBSCRIPT_shift_southeast_steps_8',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_43_SUBSCRIPT_shift_southeast_pixels_9',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_43_SUBSCRIPT_shift_northeast_steps_10',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_621_pause_44',
        "command": 'pause',
        "args": [52]
    },
    {
        "identifier": 'EVENT_621_play_sound_45',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_621_apply_tile_mod_46',
        "command": 'apply_tile_mod',
        "args": [Rooms._011_MARRYMORE_INN_3F, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_621_apply_solidity_mod_47',
        "command": 'apply_solidity_mod',
        "args": [Rooms._011_MARRYMORE_INN_3F, 1, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_621_pause_48',
        "command": 'pause',
        "args": [70]
    },
    {
        "identifier": 'EVENT_621_fade_out_to_black_async_49',
        "command": 'fade_out_to_black_async'
    },
    {
        "identifier": 'EVENT_621_enter_area_50',
        "command": 'enter_area',
        "args": [Rooms._012_MARRYMORE_INN_SUITE_ROOM, RadialDirections.NORTHEAST, 3, 21, 0, []]
    },
    {
        "identifier": 'EVENT_621_action_queue_async_51',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_621_action_queue_async_51_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 248, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_621_action_queue_async_51_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_621_set_bit_52',
        "command": 'set_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'EVENT_621_set_7000_to_70A0_short_mem_53',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70b8]
    },
    {
        "identifier": 'EVENT_621_jmp_if_7000_equals_short_54',
        "command": 'jmp_if_7000_equals_short',
        "args": [3, 'EVENT_621_set_57']
    },
    {
        "identifier": 'EVENT_621_set_55',
        "command": 'set',
        "args": [0x70a9, 22]
    },
    {
        "identifier": 'EVENT_621_jmp_56',
        "command": 'jmp',
        "args": ['EVENT_621_fade_in_from_black_sync_58']
    },
    {
        "identifier": 'EVENT_621_set_57',
        "command": 'set',
        "args": [0x70a9, 21]
    },
    {
        "identifier": 'EVENT_621_fade_in_from_black_sync_58',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_621_action_queue_sync_59',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_621_action_queue_sync_59_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_59_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_59_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_621_action_queue_sync_60',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_621_action_queue_sync_60_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_60_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_60_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [3, 22, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_60_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_60_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_621_remember_last_object_61',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_621_freeze_camera_62',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_621_pause_63',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_621_play_sound_64',
        "command": 'play_sound',
        "args": [Sounds._004_JUMP, 6]
    },
    {
        "identifier": 'EVENT_621_set_action_script_async_65',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 636]
    },
    {
        "identifier": 'EVENT_621_action_queue_sync_66',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_621_action_queue_sync_66_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_66_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_66_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_66_SUBSCRIPT_face_south_3',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_621_action_queue_sync_67',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_621_action_queue_sync_67_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_67_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_621_remember_last_object_68',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_621_play_sound_69',
        "command": 'play_sound',
        "args": [Sounds._004_JUMP, 6]
    },
    {
        "identifier": 'EVENT_621_set_action_script_async_70',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 636]
    },
    {
        "identifier": 'EVENT_621_play_sound_71',
        "command": 'play_sound',
        "args": [Sounds._004_JUMP, 6]
    },
    {
        "identifier": 'EVENT_621_set_action_script_async_72',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 636]
    },
    {
        "identifier": 'EVENT_621_action_queue_sync_73',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_621_action_queue_sync_73_SUBSCRIPT_walk_1_step_southeast_0',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_73_SUBSCRIPT_shift_east_steps_1',
                "command": 'shift_east_steps',
                "args": [7]
            }
        ]
    },
    {
        "identifier": 'EVENT_621_action_queue_sync_74',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_621_action_queue_sync_74_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_621_action_queue_sync_74_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_621_remember_last_object_75',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_621_pause_76',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_621_play_sound_77',
        "command": 'play_sound',
        "args": [Sounds._004_JUMP, 6]
    },
    {
        "identifier": 'EVENT_621_pause_78',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_621_action_queue_async_79',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_621_action_queue_async_79_SUBSCRIPT_shift_west_steps_0',
                "command": 'shift_west_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_621_action_queue_async_79_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_621_action_queue_async_79_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_621_action_queue_async_79_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_621_action_queue_async_79_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_621_set_action_script_async_80',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_621_pause_81',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_621_action_queue_async_82',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_621_action_queue_async_82_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_621_set_bit_83',
        "command": 'set_bit',
        "args": [0x704c, 1]
    },
    {
        "identifier": 'EVENT_621_unfreeze_camera_84',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_621_ret_85',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_621_jmp_if_bit_set_86',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'EVENT_621_run_dialog_107']
    },
    {
        "identifier": 'EVENT_621_set_bit_87',
        "command": 'set_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'EVENT_621_jmp_if_random_above_128_88',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_621_run_dialog_107']
    },
    {
        "identifier": 'EVENT_621_run_dialog_89',
        "command": 'run_dialog',
        "args": [1012, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_621_run_dialog_90',
        "command": 'run_dialog',
        "args": [1013, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_621_jmp_if_random_above_66_91',
        "command": 'jmp_if_random_above_66',
        "args": [0x7a1b, 0x7a27]
    },
    {
        "identifier": 'EVENT_621_add_coins_92',
        "command": 'add_coins',
        "args": [30]
    },
    {
        "identifier": 'EVENT_621_play_sound_93',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6]
    },
    {
        "identifier": 'EVENT_621_set_94',
        "command": 'set',
        "args": [0x7000, 30]
    },
    {
        "identifier": 'EVENT_621_run_dialog_95',
        "command": 'run_dialog',
        "args": [515, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_621_ret_96',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_621_set_97',
        "command": 'set',
        "args": [0x70a7, 96]
    },
    {
        "identifier": 'EVENT_621_play_sound_98',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_621_run_dialog_99',
        "command": 'run_dialog',
        "args": [524, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_621_put_inventory_100',
        "command": 'put_inventory',
        "args": [items.Mushroom]
    },
    {
        "identifier": 'EVENT_621_ret_101',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_621_set_102',
        "command": 'set',
        "args": [0x70a7, 97]
    },
    {
        "identifier": 'EVENT_621_play_sound_103',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_621_run_dialog_104',
        "command": 'run_dialog',
        "args": [524, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_621_put_inventory_105',
        "command": 'put_inventory',
        "args": [items.MidMushroom]
    },
    {
        "identifier": 'EVENT_621_ret_106',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_621_run_dialog_107',
        "command": 'run_dialog',
        "args": [1016, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_621_ret_108',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_621_jmp_if_bit_set_109',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 1, 'EVENT_621_run_dialog_122']
    },
    {
        "identifier": 'EVENT_621_set_bit_110',
        "command": 'set_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'EVENT_621_set_random_111',
        "command": 'set_random',
        "args": [0x7000, 101]
    },
    {
        "identifier": 'EVENT_621_mem_compare_val_112',
        "command": 'mem_compare_val',
        "args": [80]
    },
    {
        "identifier": 'EVENT_621_jmp_if_comparison_result_is_lesser_113',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_621_run_dialog_122']
    },
    {
        "identifier": 'EVENT_621_jmp_if_bit_set_114',
        "command": 'jmp_if_bit_set',
        "args": [0x7063, 0, 'EVENT_621_run_dialog_122']
    },
    {
        "identifier": 'EVENT_621_set_bit_115',
        "command": 'set_bit',
        "args": [0x7063, 0]
    },
    {
        "identifier": 'EVENT_621_run_dialog_116',
        "command": 'run_dialog',
        "args": [2049, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_621_play_sound_117',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_621_set_118',
        "command": 'set',
        "args": [0x70a7, 117]
    },
    {
        "identifier": 'EVENT_621_run_dialog_119',
        "command": 'run_dialog',
        "args": [524, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_621_put_inventory_120',
        "command": 'put_inventory',
        "args": [items.FlowerBox]
    },
    {
        "identifier": 'EVENT_621_ret_121',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_621_run_dialog_122',
        "command": 'run_dialog',
        "args": [2048, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_621_ret_123',
        "command": 'ret'
    }
]
