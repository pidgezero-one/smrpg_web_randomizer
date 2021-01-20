from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_331_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7082, 1, 'EVENT_331_action_queue_async_136'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_pause_action_script_1',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_sync_2_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_331_action_queue_sync_2_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [12, 98]
            },
            {
                "identifier": 'EVENT_331_action_queue_sync_2_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_331_freeze_camera_3',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_async_4_SUBSCRIPT_bounce_to_xy_with_height_0',
                "command": 'bounce_to_xy_with_height',
                "args": [9, 86, 13]
            }
        ]
    },
    {
        "identifier": 'EVENT_331_start_embedded_action_script_async_5',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_set_action_script_sync_6',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 97],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_7_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [21, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_7_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_7_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [21, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_7_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_331_run_dialog_8',
        "command": 'run_dialog',
        "args": [570, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_pause_9',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_async_10_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_331_set_action_script_async_11',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_pause_12',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_fade_out_sound_to_volume_13',
        "command": 'fade_out_sound_to_volume',
        "args": [2, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_set_bit_7_offset_14',
        "command": 'set_bit_7_offset',
        "args": [0x015a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_palette_set_morphs_15',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 41, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_palette_set_morphs_16',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 42, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_palette_set_morphs_17',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 43, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_palette_set_morphs_18',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 44, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_palette_set_morphs_19',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 45, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_palette_set_morphs_20',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 46, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_palette_set_morphs_21',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 47, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_331_pause_23',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_run_dialog_24',
        "command": 'run_dialog',
        "args": [571, AreaObjects.NPC_10, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_action_queue_async_25',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_async_25_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_331_run_dialog_26',
        "command": 'run_dialog',
        "args": [593, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_pause_27',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_action_queue_async_28',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_async_28_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_28_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=2, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_28_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_28_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=2, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_28_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 6]
            }
        ]
    },
    {
        "identifier": 'EVENT_331_action_queue_async_29',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_async_29_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_29_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_331_set_action_script_sync_30',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_10, 96],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_pause_31',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_run_dialog_32',
        "command": 'run_dialog',
        "args": [574, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_pause_33',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_clear_bit_7_offset_34',
        "command": 'clear_bit_7_offset',
        "args": [0x015a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_pause_action_script_35',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_sync_36_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_331_action_queue_sync_36_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_331_action_queue_sync_36_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_331_action_queue_sync_36_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x1e, 0xb4]
            },
            {
                "identifier": 'EVENT_331_action_queue_sync_36_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_331_action_queue_sync_36_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_331_action_queue_sync_36_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_331_run_dialog_37',
        "command": 'run_dialog',
        "args": [575, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_remember_last_object_38',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_unsync_action_script_39',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_action_queue_async_40',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_async_40_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_40_SUBSCRIPT_add_z_coord_1_step_1',
                "command": 'add_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_331_action_queue_async_40_SUBSCRIPT_dec_z_coord_1_step_2',
                "command": 'dec_z_coord_1_step',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_331_action_queue_sync_41',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_sync_41_SUBSCRIPT_face_west_0',
                "command": 'face_west',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_331_action_queue_async_42',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_async_42_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [17, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_331_run_dialog_43',
        "command": 'run_dialog',
        "args": [576, AreaObjects.NPC_10, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_action_queue_sync_44',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_sync_44_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_331_action_queue_sync_44_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_331_run_event_as_subroutine_45',
        "command": 'run_event_as_subroutine',
        "args": [286],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_action_queue_async_46',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_async_46_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            }
        ]
    },
    {
        "identifier": 'EVENT_331_pause_47',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_jmp_if_mario_in_air_48',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_331_pause_47'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_action_queue_sync_49',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_sync_49_SUBSCRIPT_add_z_coord_1_step_0',
                "command": 'add_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_331_action_queue_sync_49_SUBSCRIPT_dec_z_coord_1_step_1',
                "command": 'dec_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_331_action_queue_sync_49_SUBSCRIPT_add_z_coord_1_step_2',
                "command": 'add_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_331_action_queue_sync_49_SUBSCRIPT_dec_z_coord_1_step_3',
                "command": 'dec_z_coord_1_step',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_331_run_dialog_50',
        "command": 'run_dialog',
        "args": [577, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_action_queue_async_51',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_async_51_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_51_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_51_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_51_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_51_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x1e, 0x03]
            }
        ]
    },
    {
        "identifier": 'EVENT_331_unsync_dialog_52',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_action_queue_async_53',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_async_53_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_331_pause_54',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_action_queue_sync_55',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_sync_55_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_331_run_dialog_56',
        "command": 'run_dialog',
        "args": [581, AreaObjects.NPC_10, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_action_queue_async_57',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_async_57_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_57_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_57_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_331_run_dialog_58',
        "command": 'run_dialog',
        "args": [582, AreaObjects.NPC_10, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_action_queue_sync_59',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_sync_59_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_331_action_queue_sync_59_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_331_action_queue_sync_59_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_331_run_dialog_60',
        "command": 'run_dialog',
        "args": [583, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_jmp_if_dialog_option_b_61',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_331_fade_out_sound_to_volume_95'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_close_dialog_62',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_pause_63',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_remember_last_object_64',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_set_action_script_async_65',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_action_queue_async_66',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_async_66_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_66_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_66_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_66_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_66_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_66_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_66_SUBSCRIPT_shift_z_up_pixels_6',
                "command": 'shift_z_up_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_66_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_66_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_66_SUBSCRIPT_shift_z_up_pixels_9',
                "command": 'shift_z_up_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_66_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_66_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [25, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_66_SUBSCRIPT_dec_z_coord_1_step_12',
                "command": 'dec_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_331_action_queue_async_66_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_66_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_66_SUBSCRIPT_face_southwest_15',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_331_action_queue_async_66_SUBSCRIPT_reset_properties_16',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_331_action_queue_async_66_SUBSCRIPT_shift_southwest_pixels_17',
                "command": 'shift_southwest_pixels',
                "args": [18]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_66_SUBSCRIPT_visibility_off_18',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_331_action_queue_async_67',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_async_67_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_67_SUBSCRIPT_face_south_1',
                "command": 'face_south',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_331_remove_from_current_level_68',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_join_party_69',
        "command": 'join_party',
        "args": [AreaObjects.MALLOW],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_run_dialog_70',
        "command": 'run_dialog',
        "args": [584, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_fade_out_music_to_volume_71',
        "command": 'fade_out_music_to_volume',
        "args": [2, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_pause_72',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_play_music_default_volume_73',
        "command": 'play_music_default_volume',
        "args": [Music._40_NEW_PARTNER],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_pause_74',
        "command": 'pause',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_action_queue_async_75',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_async_75_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [6]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_75_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_75_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_75_SUBSCRIPT_end_loop_3',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_331_set_action_script_async_76',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 510],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_play_music_default_volume_77',
        "command": 'play_music_default_volume',
        "args": [Music._02_MUSHROOM_KINGDOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_pause_78',
        "command": 'pause',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_clear_bit_79',
        "command": 'clear_bit',
        "args": [0x7081, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_set_bit_80',
        "command": 'set_bit',
        "args": [0x7081, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_clear_bit_81',
        "command": 'clear_bit',
        "args": [0x7082, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_summon_to_current_level_82',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_summon_to_current_level_83',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_summon_to_current_level_84',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_set_action_script_sync_85',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 128],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_set_action_script_sync_86',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_set_action_script_sync_87',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 64],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_set_action_script_sync_88',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_pause_action_script_89',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_set_action_script_sync_90',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 100],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_clear_bit_91',
        "command": 'clear_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_unfreeze_camera_92',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_clear_bit_7_offset_93',
        "command": 'clear_bit_7_offset',
        "args": [0x015a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_ret_94',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_fade_out_sound_to_volume_95',
        "command": 'fade_out_sound_to_volume',
        "args": [1, 111],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_set_action_script_async_96',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_remember_last_object_97',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_pause_98',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_action_queue_async_99',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_async_99_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_331_pause_100',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_run_dialog_101',
        "command": 'run_dialog',
        "args": [585, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_jmp_if_dialog_option_b_102',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_331_set_action_script_async_104'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_jmp_103',
        "command": 'jmp',
        "args": ['EVENT_331_close_dialog_62'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_set_action_script_async_104',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_remember_last_object_105',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_pause_action_script_106',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_set_action_script_sync_107',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_10, 76],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_run_dialog_108',
        "command": 'run_dialog',
        "args": [586, AreaObjects.NPC_10, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_jmp_if_dialog_option_b_109',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_331_fade_out_sound_to_volume_111'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_jmp_110',
        "command": 'jmp',
        "args": ['EVENT_331_close_dialog_62'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_fade_out_sound_to_volume_111',
        "command": 'fade_out_sound_to_volume',
        "args": [1, 111],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_set_action_script_async_112',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_remember_last_object_113',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_run_dialog_114',
        "command": 'run_dialog',
        "args": [587, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_pause_action_script_115',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_action_queue_async_116',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_async_116_SUBSCRIPT_floating_on_0',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_331_action_queue_async_116_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_116_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_116_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x1e, 0x03]
            }
        ]
    },
    {
        "identifier": 'EVENT_331_pause_117',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_pause_action_script_118',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_set_action_script_sync_119',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_10, 77],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_set_bit_7_offset_120',
        "command": 'set_bit_7_offset',
        "args": [0x015a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_palette_set_morphs_121',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 17, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_palette_set_morphs_122',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 18, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_palette_set_morphs_123',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 19, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_palette_set_morphs_124',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 20, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_palette_set_morphs_125',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 21, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_palette_set_morphs_126',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 22, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_palette_set_morphs_127',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 23, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_play_sound_128',
        "command": 'play_sound',
        "args": [Sounds._006_RUNNING_WATER, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_set_bit_129',
        "command": 'set_bit',
        "args": [0x7081, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_set_bit_130',
        "command": 'set_bit',
        "args": [0x7082, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_set_action_script_sync_131',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_unfreeze_camera_132',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_pause_script_until_effect_done_133',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_clear_bit_7_offset_134',
        "command": 'clear_bit_7_offset',
        "args": [0x015a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_ret_135',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_action_queue_async_136',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_async_136_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_136_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [12, 98]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_136_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_331_action_queue_async_137',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_331_action_queue_async_137_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_137_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_137_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [21, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_137_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_137_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_137_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_137_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [21, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_137_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_331_action_queue_async_137_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_331_fade_out_sound_to_volume_138',
        "command": 'fade_out_sound_to_volume',
        "args": [2, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_set_bit_7_offset_139',
        "command": 'set_bit_7_offset',
        "args": [0x015a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_palette_set_morphs_140',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 41, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_palette_set_morphs_141',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 42, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_palette_set_morphs_142',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 43, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_palette_set_morphs_143',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 44, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_palette_set_morphs_144',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 45, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_palette_set_morphs_145',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 46, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_palette_set_morphs_146',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 47, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_run_dialog_147',
        "command": 'run_dialog',
        "args": [589, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_jmp_if_dialog_option_b_148',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_331_fade_out_sound_to_volume_111'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_331_jmp_149',
        "command": 'jmp',
        "args": ['EVENT_331_close_dialog_62'],
        "subscript": []
    }
]
