from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1367_pause_action_script_0',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1367_pause_action_script_1',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1367_pause_action_script_2',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_1367_pause_3',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1367_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_sync_4_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x6b]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_4_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_sync_5_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_async_6_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_6_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_6_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_6_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_6_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_6_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_6_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_6_SUBSCRIPT_shift_northwest_steps_7',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_6_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_sync_7_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_7_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_sync_8_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_8_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_async_9_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_9_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_pause_10',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_11',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 576]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 576]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 576]
    },
    {
        "identifier": 'EVENT_1367_play_sound_14',
        "command": 'play_sound',
        "args": [Sounds._090_CURTAIN, 4]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_15',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_16',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_17',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 41, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_18',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_19',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 34, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_20',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_21',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 42, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_22',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_23',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 35, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_24',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 39, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_25',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 43, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_start_loop_n_times_26',
        "command": 'start_loop_n_times',
        "args": [49]
    },
    {
        "identifier": 'EVENT_1367_jmp_if_bit_set_27',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_1367_stop_music_273']
    },
    {
        "identifier": 'EVENT_1367_jmp_if_bit_set_28',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_1367_stop_music_273']
    },
    {
        "identifier": 'EVENT_1367_jmp_if_bit_set_29',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_1367_stop_music_273']
    },
    {
        "identifier": 'EVENT_1367_pause_30',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1367_end_loop_31',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_32',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 577]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_33',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 577]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_34',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 577]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_35',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 34, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_36',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_37',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 42, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_38',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_39',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_40',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_41',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 41, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_42',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_43',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_44',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 36, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_45',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 40, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_46',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_pause_action_script_47',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1367_pause_action_script_48',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1367_pause_action_script_49',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_1367_action_queue_sync_50',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_sync_50_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x6b]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_50_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_50_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_50_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_50_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_50_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_50_SUBSCRIPT_face_northwest_6',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_50_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_50_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_sync_51',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_sync_51_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_51_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_51_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_51_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_51_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_51_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_51_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_51_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_async_52',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_async_52_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_52_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_52_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_52_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_52_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_52_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_52_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_52_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_pause_53',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_54',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 576]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_55',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 576]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_56',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 576]
    },
    {
        "identifier": 'EVENT_1367_play_sound_57',
        "command": 'play_sound',
        "args": [Sounds._090_CURTAIN, 4]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_58',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 45, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_59',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_60',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 41, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_61',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_62',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 46, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_63',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_64',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 42, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_65',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_66',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 47, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_67',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 39, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_68',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 43, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_start_loop_n_times_69',
        "command": 'start_loop_n_times',
        "args": [39]
    },
    {
        "identifier": 'EVENT_1367_jmp_if_bit_set_70',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_1367_stop_music_273']
    },
    {
        "identifier": 'EVENT_1367_jmp_if_bit_set_71',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_1367_stop_music_273']
    },
    {
        "identifier": 'EVENT_1367_jmp_if_bit_set_72',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_1367_stop_music_273']
    },
    {
        "identifier": 'EVENT_1367_pause_73',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1367_end_loop_74',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_75',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 577]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_76',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 577]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_77',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 577]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_78',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 46, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_79',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_80',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 42, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_81',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_82',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 45, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_83',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_84',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 41, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_85',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_86',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 44, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_87',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 36, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_88',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 40, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_89',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_pause_action_script_90',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1367_pause_action_script_91',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1367_pause_action_script_92',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_1367_action_queue_sync_93',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_sync_93_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x6b]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_93_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_93_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_93_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_93_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_93_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_93_SUBSCRIPT_face_northwest_6',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_93_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [20]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_sync_94',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_sync_94_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_94_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_94_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_async_95',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_async_95_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_95_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_95_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_sync_96',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_sync_96_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_sync_97',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_sync_97_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_async_98',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_async_98_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_pause_99',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_100',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 576]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_101',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 576]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_102',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 576]
    },
    {
        "identifier": 'EVENT_1367_play_sound_103',
        "command": 'play_sound',
        "args": [Sounds._090_CURTAIN, 4]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_104',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 45, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_105',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_106',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 41, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_107',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_108',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 46, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_109',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 34, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_110',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 42, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_111',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_112',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 47, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_113',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 35, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_114',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 43, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_start_loop_n_times_115',
        "command": 'start_loop_n_times',
        "args": [29]
    },
    {
        "identifier": 'EVENT_1367_jmp_if_bit_set_116',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_1367_stop_music_273']
    },
    {
        "identifier": 'EVENT_1367_jmp_if_bit_set_117',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_1367_stop_music_273']
    },
    {
        "identifier": 'EVENT_1367_jmp_if_bit_set_118',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_1367_stop_music_273']
    },
    {
        "identifier": 'EVENT_1367_pause_119',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1367_end_loop_120',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_121',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 577]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_122',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 577]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_123',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 577]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_124',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 46, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_125',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 34, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_126',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 42, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_127',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_128',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 45, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_129',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_130',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 41, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_131',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_132',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 44, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_133',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_134',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 40, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_135',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_pause_action_script_136',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1367_pause_action_script_137',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1367_pause_action_script_138',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_1367_action_queue_sync_139',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_sync_139_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x6b]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_139_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_139_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_139_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_139_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_139_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_139_SUBSCRIPT_face_northwest_6',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_139_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [20]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_sync_140',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_sync_140_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_140_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_140_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_async_141',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_async_141_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_141_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_141_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_sync_142',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_sync_142_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_sync_143',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_sync_143_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_async_144',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_async_144_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_pause_145',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_146',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 576]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_147',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 576]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_148',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 576]
    },
    {
        "identifier": 'EVENT_1367_play_sound_149',
        "command": 'play_sound',
        "args": [Sounds._090_CURTAIN, 4]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_150',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 45, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_151',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_152',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_153',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_154',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 46, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_155',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 34, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_156',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_157',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_158',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 47, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_159',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 35, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_160',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 39, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_start_loop_n_times_161',
        "command": 'start_loop_n_times',
        "args": [29]
    },
    {
        "identifier": 'EVENT_1367_jmp_if_bit_set_162',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_1367_stop_music_273']
    },
    {
        "identifier": 'EVENT_1367_jmp_if_bit_set_163',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_1367_stop_music_273']
    },
    {
        "identifier": 'EVENT_1367_jmp_if_bit_set_164',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_1367_stop_music_273']
    },
    {
        "identifier": 'EVENT_1367_pause_165',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1367_end_loop_166',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_167',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 577]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_168',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 577]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_169',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 577]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_170',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 46, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_171',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 34, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_172',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_173',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_174',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 45, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_175',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_176',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_177',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_178',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 44, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_179',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_180',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 36, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_181',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_pause_action_script_182',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1367_pause_action_script_183',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1367_pause_action_script_184',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_1367_action_queue_sync_185',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_sync_185_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x6b]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_185_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_185_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_185_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_185_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_185_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_185_SUBSCRIPT_face_northwest_6',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_185_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [20]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_sync_186',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_sync_186_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_186_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_186_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_async_187',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_async_187_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_187_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_187_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_sync_188',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_sync_188_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_188_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_188_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_188_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_188_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_188_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x6b]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_188_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_188_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_188_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_sync_189',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_sync_189_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_189_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_189_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_189_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_189_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_189_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_189_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_189_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_async_190',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_async_190_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_190_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_190_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_190_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_190_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_190_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_190_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_190_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_pause_191',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_192',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 576]
    },
    {
        "identifier": 'EVENT_1367_play_sound_193',
        "command": 'play_sound',
        "args": [Sounds._090_CURTAIN, 4]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_194',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 45, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_195',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_196',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 46, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_197',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_198',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 47, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_start_loop_n_times_199',
        "command": 'start_loop_n_times',
        "args": [9]
    },
    {
        "identifier": 'EVENT_1367_jmp_if_bit_set_200',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_1367_stop_music_273']
    },
    {
        "identifier": 'EVENT_1367_pause_201',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1367_end_loop_202',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_203',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 576]
    },
    {
        "identifier": 'EVENT_1367_play_sound_204',
        "command": 'play_sound',
        "args": [Sounds._090_CURTAIN, 4]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_205',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 41, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_206',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_207',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 42, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_208',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_209',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 43, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_start_loop_n_times_210',
        "command": 'start_loop_n_times',
        "args": [9]
    },
    {
        "identifier": 'EVENT_1367_jmp_if_bit_set_211',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_1367_stop_music_273']
    },
    {
        "identifier": 'EVENT_1367_jmp_if_bit_set_212',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_1367_stop_music_273']
    },
    {
        "identifier": 'EVENT_1367_pause_213',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1367_end_loop_214',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_215',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 576]
    },
    {
        "identifier": 'EVENT_1367_play_sound_216',
        "command": 'play_sound',
        "args": [Sounds._090_CURTAIN, 4]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_217',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_218',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_219',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_220',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_221',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 39, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_start_loop_n_times_222',
        "command": 'start_loop_n_times',
        "args": [29]
    },
    {
        "identifier": 'EVENT_1367_jmp_if_bit_set_223',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_1367_stop_music_273']
    },
    {
        "identifier": 'EVENT_1367_jmp_if_bit_set_224',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_1367_stop_music_273']
    },
    {
        "identifier": 'EVENT_1367_jmp_if_bit_set_225',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_1367_stop_music_273']
    },
    {
        "identifier": 'EVENT_1367_pause_226',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1367_end_loop_227',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_228',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 577]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_229',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 577]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_230',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 577]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_231',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 46, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_232',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_233',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 42, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_234',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_235',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 45, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_236',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_237',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 41, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_238',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_239',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 44, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_240',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 36, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_241',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 40, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_242',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_pause_action_script_243',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1367_pause_action_script_244',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1367_pause_action_script_245',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_1367_action_queue_sync_246',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_sync_246_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x6b]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_246_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_246_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_246_SUBSCRIPT_fixed_f_coord_off_3',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_246_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_246_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_246_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_246_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_246_SUBSCRIPT_shift_northwest_steps_8',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_246_SUBSCRIPT_shift_southwest_steps_9',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_246_SUBSCRIPT_shift_northwest_steps_10',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_246_SUBSCRIPT_face_northwest_11',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_246_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_246_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_sync_247',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_sync_247_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_247_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_247_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_247_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_247_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_247_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_247_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_247_SUBSCRIPT_shift_southeast_steps_7',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_247_SUBSCRIPT_shift_northeast_steps_8',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_247_SUBSCRIPT_shift_northwest_steps_9',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_247_SUBSCRIPT_fixed_f_coord_on_10',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_247_SUBSCRIPT_shift_northeast_steps_11',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_247_SUBSCRIPT_face_northwest_12',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_247_SUBSCRIPT_fixed_f_coord_off_13',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_247_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_247_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_async_248',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_async_248_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_248_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_248_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_248_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_248_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_248_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_248_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [112]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_248_SUBSCRIPT_shift_southwest_steps_7',
                "command": 'shift_southwest_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_248_SUBSCRIPT_shift_northwest_steps_8',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_248_SUBSCRIPT_face_northwest_9',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_248_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_248_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_pause_249',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_250',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 576]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_251',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 576]
    },
    {
        "identifier": 'EVENT_1367_set_action_script_sync_252',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 576]
    },
    {
        "identifier": 'EVENT_1367_play_sound_253',
        "command": 'play_sound',
        "args": [Sounds._090_CURTAIN, 4]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_254',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 45, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_255',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_256',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_257',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_258',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 46, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_259',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_260',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 34, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_pause_261',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_262',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 47, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_263',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 39, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_apply_tile_mod_264',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 35, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1367_start_loop_n_times_265',
        "command": 'start_loop_n_times',
        "args": [39]
    },
    {
        "identifier": 'EVENT_1367_jmp_if_bit_set_266',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_1367_stop_music_273']
    },
    {
        "identifier": 'EVENT_1367_jmp_if_bit_set_267',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_1367_stop_music_273']
    },
    {
        "identifier": 'EVENT_1367_jmp_if_bit_set_268',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_1367_stop_music_273']
    },
    {
        "identifier": 'EVENT_1367_pause_269',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1367_end_loop_270',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1367_enable_controls_until_return_271',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1367_jmp_272',
        "command": 'jmp',
        "args": ['EVENT_1368_stop_music_0']
    },
    {
        "identifier": 'EVENT_1367_stop_music_273',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1367_move_script_to_main_thread_274',
        "command": 'move_script_to_main_thread'
    },
    {
        "identifier": 'EVENT_1367_enable_controls_until_return_275',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1367_action_queue_sync_276',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_sync_276_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_276_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_sync_277',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_sync_277_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_277_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_277_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_sync_278',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_sync_278_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_278_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_sync_278_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_action_queue_async_279',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_async_279_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_279_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_279_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_pause_280',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1367_action_queue_async_281',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1367_action_queue_async_281_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_281_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_281_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1367_action_queue_async_281_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [50]
            }
        ]
    },
    {
        "identifier": 'EVENT_1367_jmp_282',
        "command": 'jmp',
        "args": ['EVENT_1370_jmp_if_var_equals_short_0']
    }
]
