
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1368_stop_music_FDA2_0',
        "command": 'stop_music_FDA2'
    },
    {
        "identifier": 'EVENT_1368_enable_controls_until_return_1',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1368_pause_action_script_2',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1368_pause_action_script_3',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1368_pause_action_script_4',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_1368_run_dialog_5',
        "command": 'run_dialog',
        "args": [2789, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_6_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_6_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_6_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_6_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_7_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_7_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_7_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_8_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_8_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_8_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_run_dialog_9',
        "command": 'run_dialog',
        "args": [2790, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_10_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_10_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_11_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_11_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_12_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_12_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_13_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_13_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_13_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_13_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_13_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_13_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_13_SUBSCRIPT_shift_northwest_pixels_6',
                "command": 'shift_northwest_pixels',
                "args": [13]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_13_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_13_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_play_music_default_volume_14',
        "command": 'play_music_default_volume',
        "args": [Music._32_AND_MY_NAMES_BOOSTER]
    },
    {
        "identifier": 'EVENT_1368_apply_tile_mod_15',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 41, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1368_pause_16',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1368_play_sound_17',
        "command": 'play_sound',
        "args": [Sounds._090_CURTAIN, 6]
    },
    {
        "identifier": 'EVENT_1368_apply_tile_mod_18',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 42, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1368_pause_19',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1368_apply_tile_mod_20',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 43, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1368_pause_21',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [16, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_23_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_23_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_23_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_23_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_23_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_23_SUBSCRIPT_sequence_looping_on_5',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_23_SUBSCRIPT_fixed_f_coord_on_6',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_23_SUBSCRIPT_jump_to_height_7',
                "command": 'jump_to_height',
                "args": [112]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_23_SUBSCRIPT_shift_southeast_steps_8',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_23_SUBSCRIPT_sequence_looping_on_9',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_24',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_24_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_25_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_26_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_run_dialog_27',
        "command": 'run_dialog',
        "args": [2791, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_28',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_28_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_28_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_28_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_28_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_28_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_28_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_29_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_29_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_29_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_29_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_29_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_29_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_30',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_30_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_30_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_30_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_30_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_30_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_pause_31',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_32_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_32_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_pause_33',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_34',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_34_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_34_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_35',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_35_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_35_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_36',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_36_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_36_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_pause_37',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_38',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_38_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_38_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_38_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_38_SUBSCRIPT_bounce_to_xy_with_height_3',
                "command": 'bounce_to_xy_with_height',
                "args": [3, 20, 0]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_38_SUBSCRIPT_face_north_4',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_38_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_38_SUBSCRIPT_face_east_6',
                "command": 'face_east'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_39',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_39_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_39_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_39_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_run_dialog_40',
        "command": 'run_dialog',
        "args": [2792, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_41',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_41_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_41_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_run_dialog_42',
        "command": 'run_dialog',
        "args": [2793, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_43',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_43_SUBSCRIPT_shift_northwest_steps_0',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_43_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_43_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_43_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_43_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_43_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_43_SUBSCRIPT_sequence_looping_off_6',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_43_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_43_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_44',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_44_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_44_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_44_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_44_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_44_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_45',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_45_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_45_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_45_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_pause_46',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'EVENT_1368_run_dialog_47',
        "command": 'run_dialog',
        "args": [2794, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_48',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_48_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_48_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_48_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [13, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_set_action_script_sync_49',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 579]
    },
    {
        "identifier": 'EVENT_1368_set_action_script_sync_50',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 580]
    },
    {
        "identifier": 'EVENT_1368_set_action_script_sync_51',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 578]
    },
    {
        "identifier": 'EVENT_1368_pause_52',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_53',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_53_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_53_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_53_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_53_SUBSCRIPT_bounce_to_xy_with_height_3',
                "command": 'bounce_to_xy_with_height',
                "args": [3, 16, 0]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_53_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_53_SUBSCRIPT_face_southeast_5',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_pause_54',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1368_set_7000_to_tapped_button_55',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_1368_pause_56',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1368_mem_7000_and_const_57',
        "command": 'mem_7000_and_const',
        "args": [0x0080]
    },
    {
        "identifier": 'EVENT_1368_jmp_if_7000_equals_short_58',
        "command": 'jmp_if_7000_equals_short',
        "args": [128, 'EVENT_1368_action_queue_sync_60']
    },
    {
        "identifier": 'EVENT_1368_jmp_59',
        "command": 'jmp',
        "args": ['EVENT_1368_set_7000_to_tapped_button_55']
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_60',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_60_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [112]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_60_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_60_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_60_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_60_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_61',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_61_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_61_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_61_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_61_SUBSCRIPT_floating_on_3',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_61_SUBSCRIPT_shadow_off_4',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_61_SUBSCRIPT_jump_to_height_silent_5',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_61_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_62',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_62_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_62_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_62_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._034_SQUIRM_WRITHE, 6]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_62_SUBSCRIPT_shift_north_pixels_3',
                "command": 'shift_north_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_62_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_62_SUBSCRIPT_shift_north_pixels_5',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_62_SUBSCRIPT_shift_south_pixels_6',
                "command": 'shift_south_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_pause_63',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1368_pause_action_script_64',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1368_pause_action_script_65',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1368_pause_action_script_66',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_67',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_67_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_67_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_67_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_67_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_67_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_68',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_68_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_68_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_68_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_69',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_69_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_69_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_69_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_70',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_70_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_70_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_70_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_run_dialog_71',
        "command": 'run_dialog',
        "args": [2795, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_72',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_72_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_72_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_72_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._024_TAPPING_FEET, 6]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_72_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_73',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_73_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_73_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_73_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_73_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [32]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_73_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._025_HEEL_CLICK, 6]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_73_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_pause_74',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1368_run_dialog_75',
        "command": 'run_dialog',
        "args": [2796, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1368_play_sound_76',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_1368_run_dialog_77',
        "command": 'run_dialog',
        "args": [2797, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1368_pause_78',
        "command": 'pause',
        "args": [45]
    },
    {
        "identifier": 'EVENT_1368_run_dialog_79',
        "command": 'run_dialog',
        "args": [2798, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_80',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_80_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_run_dialog_81',
        "command": 'run_dialog',
        "args": [2799, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_82',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_82_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_82_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_82_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_82_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_pause_83',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_84',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_84_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_84_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_84_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_84_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_85',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_85_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_85_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_85_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_85_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_86',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_86_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_86_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_86_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_86_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_pause_87',
        "command": 'pause',
        "args": [45]
    },
    {
        "identifier": 'EVENT_1368_run_dialog_88',
        "command": 'run_dialog',
        "args": [2800, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1368_play_sound_89',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_1368_pause_90',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_91',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_91_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_91_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_91_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_91_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_92',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_92_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_92_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_92_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_92_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_93',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_93_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_93_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_93_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_93_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_94',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_94_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_94_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_94_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_94_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_94_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_94_SUBSCRIPT_shift_northeast_pixels_5',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_94_SUBSCRIPT_shift_northwest_steps_6',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_94_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_94_SUBSCRIPT_face_southwest_8',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_94_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_94_SUBSCRIPT_face_northwest_10',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_94_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_94_SUBSCRIPT_shift_southeast_steps_12',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_94_SUBSCRIPT_shift_southwest_steps_13',
                "command": 'shift_southwest_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_94_SUBSCRIPT_shift_southwest_pixels_14',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_94_SUBSCRIPT_visibility_off_15',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1368_remove_from_current_level_95',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1368_remove_from_current_level_96',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1368_remove_from_current_level_97',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1368_remove_from_current_level_98',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_1368_apply_solidity_mod_99',
        "command": 'apply_solidity_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 1, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_1368_set_bit_100',
        "command": 'set_bit',
        "args": [0x7053, 5]
    },
    {
        "identifier": 'EVENT_1368_set_action_script_async_101',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_1368_put_inventory_102',
        "command": 'put_inventory',
        "args": [items.Amulet]
    },
    {
        "identifier": 'EVENT_1368_unfreeze_camera_103',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_1368_ret_104',
        "command": 'ret'
    }
]
