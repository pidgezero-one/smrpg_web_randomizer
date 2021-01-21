from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2642_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7059, 5, 'EVENT_2642_ret_67']
    },
    {
        "identifier": 'EVENT_2642_db_1',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2642_run_dialog_2',
        "command": 'run_dialog',
        "args": [2514, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2642_set_bit_3',
        "command": 'set_bit',
        "args": [0x7059, 5]
    },
    {
        "identifier": 'EVENT_2642_summon_to_level_4',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_9, Rooms._406_FACTORY_GROUNDS_AREA_01_WITH_TOAD]
    },
    {
        "identifier": 'EVENT_2642_summon_to_current_level_5',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_2642_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2642_action_queue_sync_6_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2642_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2642_action_queue_sync_7_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_7_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_7_SUBSCRIPT_overwrite_solidity_2',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_7_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [15, 59, 10, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_7_SUBSCRIPT_shift_north_pixels_4',
                "command": 'shift_north_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_7_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2642_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2642_action_queue_async_8_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2642_action_queue_async_8_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2642_action_queue_async_8_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [10, 29]
            }
        ]
    },
    {
        "identifier": 'EVENT_2642_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2642_action_queue_sync_9_SUBSCRIPT_overwrite_solidity_0',
                "command": 'overwrite_solidity',
                "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_9_SUBSCRIPT_shadow_on_1',
                "command": 'shadow_on'
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_9_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_9_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_9_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_9_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_9_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_9_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_9_SUBSCRIPT_shift_northwest_steps_8',
                "command": 'shift_northwest_steps',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_2642_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2642_action_queue_sync_10_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_10_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_10_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_10_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [9, 45]
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_10_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2642_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2642_action_queue_async_11_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [96]
            },
            {
                "identifier": 'EVENT_2642_action_queue_async_11_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2642_action_queue_async_11_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2642_db_12',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2642_run_dialog_13',
        "command": 'run_dialog',
        "args": [2515, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2642_db_14',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2642_run_dialog_15',
        "command": 'run_dialog',
        "args": [2516, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2642_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2642_action_queue_async_16_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2642_action_queue_async_16_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_2642_action_queue_async_16_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2642_action_queue_async_16_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [24]
            }
        ]
    },
    {
        "identifier": 'EVENT_2642_unsync_dialog_17',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_2642_pause_18',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2642_summon_to_current_level_at_marios_coords_19',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_2642_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_2642_action_queue_async_20_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2642_action_queue_async_20_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_2642_action_queue_async_20_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_2642_pause_21',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'EVENT_2642_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2642_action_queue_async_22_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2642_action_queue_async_22_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2642_action_queue_async_22_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2642_action_queue_async_22_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2642_action_queue_async_22_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2642_db_23',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2642_run_dialog_24',
        "command": 'run_dialog',
        "args": [2517, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2642_pause_25',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2642_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_2642_action_queue_sync_26_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_26_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_26_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2642_db_27',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2642_run_dialog_28',
        "command": 'run_dialog',
        "args": [2518, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2642_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_2642_action_queue_sync_29_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2642_db_30',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2642_run_dialog_31',
        "command": 'run_dialog',
        "args": [2519, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2642_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2642_action_queue_sync_32_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_32_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_32_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_32_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [96]
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_32_SUBSCRIPT_walk_1_step_northwest_4',
                "command": 'walk_1_step_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2642_pause_33',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'EVENT_2642_db_34',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2642_run_dialog_35',
        "command": 'run_dialog',
        "args": [2520, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2642_stop_embedded_action_script_36',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_2642_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2642_action_queue_sync_37_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [72]
            }
        ]
    },
    {
        "identifier": 'EVENT_2642_db_38',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2642_run_dialog_39',
        "command": 'run_dialog',
        "args": [2521, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2642_action_queue_async_40',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_2642_action_queue_async_40_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, 2, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2642_db_41',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2642_run_dialog_42',
        "command": 'run_dialog',
        "args": [2522, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2642_action_queue_sync_43',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_2642_action_queue_sync_43_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2642_action_queue_sync_44',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2642_action_queue_sync_44_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [64]
            }
        ]
    },
    {
        "identifier": 'EVENT_2642_db_45',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2642_run_dialog_46',
        "command": 'run_dialog',
        "args": [2523, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2642_open_shop_47',
        "command": 'open_shop',
        "args": [Shops._24_TOADS_SHOP]
    },
    {
        "identifier": 'EVENT_2642_fade_in_from_black_async_48',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2642_action_queue_sync_49',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2642_action_queue_sync_49_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [64]
            }
        ]
    },
    {
        "identifier": 'EVENT_2642_db_50',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2642_run_dialog_51',
        "command": 'run_dialog',
        "args": [3311, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2642_db_52',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2642_run_dialog_53',
        "command": 'run_dialog',
        "args": [3079, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2642_play_sound_54',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_2642_put_inventory_55',
        "command": 'put_inventory',
        "args": [items.RockCandy]
    },
    {
        "identifier": 'EVENT_2642_action_queue_async_56',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_2642_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2642_action_queue_async_56_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2642_action_queue_async_56_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2642_action_queue_sync_57',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2642_action_queue_sync_57_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_57_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_57_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2642_action_queue_sync_57_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2642_db_58',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2642_run_dialog_59',
        "command": 'run_dialog',
        "args": [2524, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2642_pause_60',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2642_db_61',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2642_run_dialog_62',
        "command": 'run_dialog',
        "args": [2525, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2642_stop_embedded_action_script_63',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_2642_pause_64',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2642_action_queue_async_65',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_2642_action_queue_async_65_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [9, 45]
            },
            {
                "identifier": 'EVENT_2642_action_queue_async_65_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2642_set_action_script_async_66',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2642_ret_67',
        "command": 'ret'
    }
]
