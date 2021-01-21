from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1335_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'EVENT_1335_ret_54']
    },
    {
        "identifier": 'EVENT_1335_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 5, 'EVENT_1335_remove_from_current_level_10']
    },
    {
        "identifier": 'EVENT_1335_apply_tile_mod_2',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 47, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1335_pause_3',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1335_apply_tile_mod_4',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 49, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1335_play_sound_5',
        "command": 'play_sound',
        "args": [Sounds._088_WRONG_SIGNAL, 6]
    },
    {
        "identifier": 'EVENT_1335_pause_6',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1335_start_battle_7',
        "command": 'start_battle',
        "args": [0x002e, 12]
    },
    {
        "identifier": 'EVENT_1335_fade_in_from_black_async_8',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1335_jmp_9',
        "command": 'jmp',
        "args": ['EVENT_1338_pause_0']
    },
    {
        "identifier": 'EVENT_1335_remove_from_current_level_10',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_1335_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1335_action_queue_async_11_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [18, 25]
            },
            {
                "identifier": 'EVENT_1335_action_queue_async_11_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1335_action_queue_async_11_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1335_action_queue_async_11_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1335_action_queue_async_11_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1335_action_queue_async_11_SUBSCRIPT_set_vram_priority_5',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_1335_apply_tile_mod_12',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 47, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1335_pause_13',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1335_apply_tile_mod_14',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 49, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1335_pause_15',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1335_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1335_action_queue_async_16_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1335_action_queue_async_16_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1335_action_queue_async_16_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1335_action_queue_async_16_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [17, 27]
            },
            {
                "identifier": 'EVENT_1335_action_queue_async_16_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1335_pause_17',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1335_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1335_action_queue_async_18_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1335_action_queue_async_18_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1335_action_queue_async_18_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1335_action_queue_async_18_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1335_pause_19',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1335_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1335_action_queue_async_20_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1335_action_queue_async_20_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1335_action_queue_async_20_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._078_CLICK, 6]
            },
            {
                "identifier": 'EVENT_1335_action_queue_async_20_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1335_action_queue_async_20_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [21]
            },
            {
                "identifier": 'EVENT_1335_action_queue_async_20_SUBSCRIPT_floating_on_5',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1335_action_queue_async_20_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_1335_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1335_action_queue_async_21_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_1335_pause_22',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1335_play_sound_23',
        "command": 'play_sound',
        "args": [Sounds._106_OFF_BALANCE, 6]
    },
    {
        "identifier": 'EVENT_1335_apply_tile_mod_24',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 47, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1335_pause_25',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1335_apply_tile_mod_26',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 48, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1335_pause_27',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1335_apply_tile_mod_28',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 47, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1335_pause_29',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1335_apply_tile_mod_30',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 48, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1335_pause_31',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1335_apply_tile_mod_32',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 47, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1335_pause_33',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1335_apply_tile_mod_34',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 48, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1335_pause_35',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1335_apply_tile_mod_36',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 47, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1335_pause_37',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1335_apply_tile_mod_38',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 48, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1335_pause_39',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1335_apply_tile_mod_40',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 47, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1335_pause_41',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1335_play_sound_42',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_1335_apply_tile_mod_43',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 48, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1335_pause_44',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1335_action_queue_sync_45',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1335_action_queue_sync_45_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1335_action_queue_sync_45_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1335_action_queue_sync_45_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1335_action_queue_sync_45_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [10, 2, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1335_action_queue_sync_45_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [45]
            }
        ]
    },
    {
        "identifier": 'EVENT_1335_action_queue_async_46',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1335_action_queue_async_46_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1335_action_queue_async_46_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1335_jmp_to_event_47',
        "command": 'jmp_to_event',
        "args": [560]
    },
    {
        "identifier": 'EVENT_1335_set_48',
        "command": 'set',
        "args": [0x70a7, 141]
    },
    {
        "identifier": 'EVENT_1335_set_49',
        "command": 'set',
        "args": [0x7000, 2567]
    },
    {
        "identifier": 'EVENT_1335_run_event_as_subroutine_50',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_1335_action_queue_async_51',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1335_action_queue_async_51_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_1335_set_bit_52',
        "command": 'set_bit',
        "args": [0x7054, 0]
    },
    {
        "identifier": 'EVENT_1335_ret_53',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1335_ret_54',
        "command": 'ret'
    }
]
