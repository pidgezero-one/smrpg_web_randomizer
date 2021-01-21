from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1366_pause_action_script_0',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1366_pause_action_script_1',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1366_pause_2',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1366_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_sync_3_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x6b]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_3_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_3_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_3_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_3_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_3_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_3_SUBSCRIPT_face_northwest_6',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_async_4_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_4_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_4_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_4_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_4_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_4_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_4_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_pause_5',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_6',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 576]
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 576]
    },
    {
        "identifier": 'EVENT_1366_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._090_CURTAIN, 4]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_9',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_10',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 45, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_11',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_12',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_13',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 46, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_14',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_15',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 39, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_16',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 47, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_start_loop_n_times_17',
        "command": 'start_loop_n_times',
        "args": [79]
    },
    {
        "identifier": 'EVENT_1366_jmp_if_bit_set_18',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_1366_move_script_to_main_thread_243']
    },
    {
        "identifier": 'EVENT_1366_jmp_if_bit_set_19',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_1366_move_script_to_main_thread_243']
    },
    {
        "identifier": 'EVENT_1366_pause_20',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1366_end_loop_21',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_22',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 577]
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_23',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 577]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_24',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_25',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 46, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_26',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_27',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_28',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 45, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_29',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_30',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 36, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_31',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 44, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_32',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_pause_action_script_33',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1366_pause_action_script_34',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1366_action_queue_sync_35',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_sync_35_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x6b]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_35_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_35_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_35_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_35_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_35_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_35_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_35_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_action_queue_async_36',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_async_36_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_36_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_36_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_36_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_36_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_36_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_36_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_pause_37',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_38',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 576]
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_39',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 576]
    },
    {
        "identifier": 'EVENT_1366_play_sound_40',
        "command": 'play_sound',
        "args": [Sounds._090_CURTAIN, 4]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_41',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_42',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 41, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_43',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_44',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 34, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_45',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 42, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_46',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_47',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 35, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_48',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 43, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_start_loop_n_times_49',
        "command": 'start_loop_n_times',
        "args": [59]
    },
    {
        "identifier": 'EVENT_1366_jmp_if_bit_set_50',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_1366_move_script_to_main_thread_243']
    },
    {
        "identifier": 'EVENT_1366_jmp_if_bit_set_51',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_1366_move_script_to_main_thread_243']
    },
    {
        "identifier": 'EVENT_1366_pause_52',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1366_end_loop_53',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_54',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 577]
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_55',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 577]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_56',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 34, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_57',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 42, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_58',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_59',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_60',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 41, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_61',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_62',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_63',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 40, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_64',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_pause_action_script_65',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1366_pause_action_script_66',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1366_action_queue_sync_67',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_sync_67_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x6b]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_67_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_67_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_67_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_67_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_67_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_67_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [117]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_67_SUBSCRIPT_shift_southwest_steps_7',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_67_SUBSCRIPT_face_northwest_8',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_67_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_67_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_action_queue_async_68',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_async_68_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_68_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_68_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_68_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_68_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_68_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_68_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_68_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_pause_69',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_70',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 576]
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_71',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 576]
    },
    {
        "identifier": 'EVENT_1366_play_sound_72',
        "command": 'play_sound',
        "args": [Sounds._090_CURTAIN, 4]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_73',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_74',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 41, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_75',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_76',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_77',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 42, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_78',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_79',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 39, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_80',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 43, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_start_loop_n_times_81',
        "command": 'start_loop_n_times',
        "args": [39]
    },
    {
        "identifier": 'EVENT_1366_jmp_if_bit_set_82',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_1366_move_script_to_main_thread_243']
    },
    {
        "identifier": 'EVENT_1366_jmp_if_bit_set_83',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_1366_move_script_to_main_thread_243']
    },
    {
        "identifier": 'EVENT_1366_pause_84',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1366_end_loop_85',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_86',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 577]
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_87',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 577]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_88',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_89',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 42, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_90',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_91',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_92',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 41, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_93',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_94',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 36, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_95',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 40, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_96',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_pause_action_script_97',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1366_pause_action_script_98',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1366_pause_99',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1366_action_queue_sync_100',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_sync_100_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x6b]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_100_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_100_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_100_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_100_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_100_SUBSCRIPT_shift_southwest_pixels_5',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_100_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_100_SUBSCRIPT_fixed_f_coord_on_7',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_100_SUBSCRIPT_jump_to_height_8',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_100_SUBSCRIPT_shift_northeast_steps_9',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_100_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_100_SUBSCRIPT_fixed_f_coord_off_11',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_100_SUBSCRIPT_shift_northeast_steps_12',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_100_SUBSCRIPT_shift_northeast_pixels_13',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_100_SUBSCRIPT_face_northwest_14',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_100_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_100_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_action_queue_async_101',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_async_101_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_101_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_101_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_101_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_101_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_101_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_101_SUBSCRIPT_fixed_f_coord_on_6',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_101_SUBSCRIPT_jump_to_height_7',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_101_SUBSCRIPT_shift_southwest_steps_8',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_101_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_101_SUBSCRIPT_fixed_f_coord_off_10',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_101_SUBSCRIPT_shift_southwest_steps_11',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_101_SUBSCRIPT_shift_southwest_pixels_12',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_101_SUBSCRIPT_face_northwest_13',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_101_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_101_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_pause_102',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1366_play_sound_103',
        "command": 'play_sound',
        "args": [Sounds._107_DRUM_ROLL, 4]
    },
    {
        "identifier": 'EVENT_1366_action_queue_async_104',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_async_104_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_104_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_104_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_104_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_104_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_104_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_104_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_pause_105',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_106',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 576]
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_107',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 576]
    },
    {
        "identifier": 'EVENT_1366_play_sound_108',
        "command": 'play_sound',
        "args": [Sounds._090_CURTAIN, 4]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_109',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_110',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 45, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_111',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_112',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_113',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 46, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_114',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_115',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 39, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_116',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 47, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_start_loop_n_times_117',
        "command": 'start_loop_n_times',
        "args": [24]
    },
    {
        "identifier": 'EVENT_1366_jmp_if_bit_set_118',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_1366_move_script_to_main_thread_243']
    },
    {
        "identifier": 'EVENT_1366_jmp_if_bit_set_119',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_1366_move_script_to_main_thread_243']
    },
    {
        "identifier": 'EVENT_1366_pause_120',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1366_end_loop_121',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_122',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 577]
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_123',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 577]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_124',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_125',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 46, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_126',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_127',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_128',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 45, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_129',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_130',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 36, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_131',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 44, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_132',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_pause_action_script_133',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1366_pause_action_script_134',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1366_action_queue_sync_135',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_sync_135_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_135_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_135_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_135_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_action_queue_async_136',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_async_136_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_136_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_136_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_136_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_136_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_136_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_136_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_136_SUBSCRIPT_jump_to_height_7',
                "command": 'jump_to_height',
                "args": [53]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_136_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_136_SUBSCRIPT_jump_to_height_9',
                "command": 'jump_to_height',
                "args": [53]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_136_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_play_sound_137',
        "command": 'play_sound',
        "args": [Sounds._107_DRUM_ROLL, 4]
    },
    {
        "identifier": 'EVENT_1366_action_queue_async_138',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_async_138_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_138_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_138_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_138_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_138_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_138_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_138_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_138_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_138_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_138_SUBSCRIPT_face_northwest_9',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_action_queue_sync_139',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_sync_139_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_139_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_139_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_action_queue_async_140',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_async_140_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_140_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_140_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_pause_141',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_142',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 576]
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_143',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 576]
    },
    {
        "identifier": 'EVENT_1366_play_sound_144',
        "command": 'play_sound',
        "args": [Sounds._090_CURTAIN, 4]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_145',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 41, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_146',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 45, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_147',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_148',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 42, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_149',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 46, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_150',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_151',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 43, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_152',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 47, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_start_loop_n_times_153',
        "command": 'start_loop_n_times',
        "args": [14]
    },
    {
        "identifier": 'EVENT_1366_jmp_if_bit_set_154',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_1366_move_script_to_main_thread_243']
    },
    {
        "identifier": 'EVENT_1366_jmp_if_bit_set_155',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_1366_move_script_to_main_thread_243']
    },
    {
        "identifier": 'EVENT_1366_pause_156',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1366_end_loop_157',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_158',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 577]
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_159',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 577]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_160',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 42, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_161',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 46, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_162',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_163',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 41, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_164',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 45, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_165',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_166',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 40, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_167',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 44, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_168',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_pause_action_script_169',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1366_pause_action_script_170',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1366_action_queue_sync_171',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_sync_171_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x6b]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_171_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_171_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_171_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_171_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_171_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_171_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_171_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_171_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_171_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_action_queue_async_172',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_async_172_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_172_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_172_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_172_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_172_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_172_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_172_SUBSCRIPT_face_northwest_6',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_172_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_172_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_pause_173',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_174',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 576]
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_175',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 576]
    },
    {
        "identifier": 'EVENT_1366_play_sound_176',
        "command": 'play_sound',
        "args": [Sounds._090_CURTAIN, 4]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_177',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_178',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 41, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_179',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_180',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_181',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 42, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_182',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_183',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 39, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_184',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 43, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_start_loop_n_times_185',
        "command": 'start_loop_n_times',
        "args": [14]
    },
    {
        "identifier": 'EVENT_1366_jmp_if_bit_set_186',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_1366_move_script_to_main_thread_243']
    },
    {
        "identifier": 'EVENT_1366_jmp_if_bit_set_187',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_1366_move_script_to_main_thread_243']
    },
    {
        "identifier": 'EVENT_1366_pause_188',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1366_end_loop_189',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_190',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 577]
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_191',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 577]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_192',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_193',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 42, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_194',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_195',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_196',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 41, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_197',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_198',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 36, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_199',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 40, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_200',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_pause_action_script_201',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1366_pause_action_script_202',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1366_action_queue_sync_203',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_sync_203_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x6b]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_203_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_203_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_203_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_203_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_203_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_203_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_203_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_203_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_203_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_action_queue_async_204',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_async_204_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_204_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_204_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_204_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_204_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_204_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_204_SUBSCRIPT_face_northwest_6',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_204_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_204_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_pause_205',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_206',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 576]
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_207',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 576]
    },
    {
        "identifier": 'EVENT_1366_play_sound_208',
        "command": 'play_sound',
        "args": [Sounds._090_CURTAIN, 4]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_209',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_210',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_211',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_212',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 34, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_213',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_214',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_215',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 35, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_216',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 39, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_start_loop_n_times_217',
        "command": 'start_loop_n_times',
        "args": [29]
    },
    {
        "identifier": 'EVENT_1366_jmp_if_bit_set_218',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_1366_move_script_to_main_thread_243']
    },
    {
        "identifier": 'EVENT_1366_jmp_if_bit_set_219',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_1366_move_script_to_main_thread_243']
    },
    {
        "identifier": 'EVENT_1366_pause_220',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1366_end_loop_221',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_222',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 577]
    },
    {
        "identifier": 'EVENT_1366_set_action_script_sync_223',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 577]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_224',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 34, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_225',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_226',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_227',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_228',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_229',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_230',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_apply_tile_mod_231',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 36, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1366_pause_232',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1366_pause_action_script_233',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1366_pause_action_script_234',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1366_action_queue_sync_235',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_sync_235_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_235_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_235_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_235_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_235_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_235_SUBSCRIPT_face_southeast_5',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_action_queue_async_236',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_async_236_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_236_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_236_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_236_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_236_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_236_SUBSCRIPT_face_southeast_5',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_pause_237',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1366_jmp_238',
        "command": 'jmp',
        "args": ['EVENT_1366_jmp_242']
    },
    {
        "identifier": 'EVENT_1366_stop_sound_239',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1366_pause_240',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1366_run_dialog_241',
        "command": 'run_dialog',
        "args": [2787, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1366_jmp_242',
        "command": 'jmp',
        "args": ['EVENT_1367_pause_action_script_0']
    },
    {
        "identifier": 'EVENT_1366_move_script_to_main_thread_243',
        "command": 'move_script_to_main_thread'
    },
    {
        "identifier": 'EVENT_1366_enable_controls_until_return_244',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1366_stop_music_245',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1366_action_queue_sync_246',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_sync_246_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_246_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_action_queue_sync_247',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_sync_247_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_247_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_247_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_action_queue_async_248',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_async_248_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_248_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_248_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_pause_249',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1366_action_queue_sync_250',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_sync_250_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_250_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_250_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1366_action_queue_sync_250_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [50]
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_action_queue_async_251',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1366_action_queue_async_251_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_251_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_251_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1366_action_queue_async_251_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [50]
            }
        ]
    },
    {
        "identifier": 'EVENT_1366_jmp_252',
        "command": 'jmp',
        "args": ['EVENT_1370_jmp_if_var_equals_short_0']
    }
]
