from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1370_jmp_if_var_equals_short_0',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 2, 'EVENT_1369_pause_0']
    },
    {
        "identifier": 'EVENT_1370_pause_1',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1370_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1370_action_queue_async_2_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_1370_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._090_CURTAIN, 6]
    },
    {
        "identifier": 'EVENT_1370_apply_tile_mod_4',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1370_apply_tile_mod_5',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 36, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1370_apply_tile_mod_6',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 40, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1370_apply_tile_mod_7',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 44, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1370_move_script_to_background_thread_2_8',
        "command": 'move_script_to_background_thread_2'
    },
    {
        "identifier": 'EVENT_1370_enable_controls_until_return_9',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1370_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1370_action_queue_sync_10_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1370_action_queue_sync_10_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1370_action_queue_sync_10_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1370_action_queue_sync_10_SUBSCRIPT_bounce_to_xy_with_height_3',
                "command": 'bounce_to_xy_with_height',
                "args": [5, 19, 0]
            },
            {
                "identifier": 'EVENT_1370_action_queue_sync_10_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1370_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1370_action_queue_sync_11_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1370_action_queue_sync_11_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1370_action_queue_sync_11_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1370_action_queue_sync_11_SUBSCRIPT_bounce_to_xy_with_height_3',
                "command": 'bounce_to_xy_with_height',
                "args": [3, 20, 0]
            },
            {
                "identifier": 'EVENT_1370_action_queue_sync_11_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1370_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1370_action_queue_sync_12_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1370_action_queue_sync_12_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1370_action_queue_sync_12_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1370_action_queue_sync_12_SUBSCRIPT_bounce_to_xy_with_height_3',
                "command": 'bounce_to_xy_with_height',
                "args": [4, 22, 0]
            },
            {
                "identifier": 'EVENT_1370_action_queue_sync_12_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1370_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1370_action_queue_async_13_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1370_action_queue_async_13_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1370_action_queue_async_13_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1370_action_queue_async_13_SUBSCRIPT_bounce_to_xy_with_height_3',
                "command": 'bounce_to_xy_with_height',
                "args": [5, 24, 0]
            },
            {
                "identifier": 'EVENT_1370_action_queue_async_13_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1370_pause_14',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1370_jmp_if_var_equals_short_15',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 1, 'EVENT_1370_add_short_26']
    },
    {
        "identifier": 'EVENT_1370_add_short_16',
        "command": 'add_short',
        "args": [0x7026, 0x01]
    },
    {
        "identifier": 'EVENT_1370_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_1358_jmp_66']
    },
    {
        "identifier": 'EVENT_1370_stop_sound_18',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1370_stop_sound_19',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1370_stop_sound_20',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1370_stop_sound_21',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1370_stop_sound_22',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1370_stop_sound_23',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1370_stop_sound_24',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1370_stop_sound_25',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1370_add_short_26',
        "command": 'add_short',
        "args": [0x7026, 0x01]
    },
    {
        "identifier": 'EVENT_1370_jmp_27',
        "command": 'jmp',
        "args": ['EVENT_1358_jmp_66']
    }
]
