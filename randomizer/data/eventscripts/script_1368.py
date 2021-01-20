from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1368_stop_music_0',
        "command": 'stop_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_enable_controls_until_return_1',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_pause_action_script_2',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_pause_action_script_3',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_pause_action_script_4',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_5_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_5_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_5_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_6_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_6_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_6_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_7_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_7_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_7_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_8_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_8_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_9_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_9_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_10_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_10_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_11_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_11_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_11_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_11_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_11_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_11_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_11_SUBSCRIPT_shift_northwest_pixels_6',
                "command": 'shift_northwest_pixels',
                "args": [13]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_11_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_11_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_play_music_default_volume_12',
        "command": 'play_music_default_volume',
        "args": [Music._32_AND_MY_NAMES_BOOSTER],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_apply_tile_mod_13',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 41, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_pause_14',
        "command": 'pause',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_play_sound_15',
        "command": 'play_sound',
        "args": [Sounds._090_CURTAIN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_apply_tile_mod_16',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 42, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_pause_17',
        "command": 'pause',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_apply_tile_mod_18',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 43, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_pause_19',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_20_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [16, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_21_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_21_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_21_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_21_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_21_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_21_SUBSCRIPT_sequence_looping_on_5',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_21_SUBSCRIPT_fixed_f_coord_on_6',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_21_SUBSCRIPT_jump_to_height_7',
                "command": 'jump_to_height',
                "args": [112]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_21_SUBSCRIPT_shift_southeast_steps_8',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_21_SUBSCRIPT_sequence_looping_on_9',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_22_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_23_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_24_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_25_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_25_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_25_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_25_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_25_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_25_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_26_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_26_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_26_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_26_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_26_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_26_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_27',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_27_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_27_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_27_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_27_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_27_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_pause_28',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_29',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_29_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_29_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_pause_30',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_31',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_31_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_31_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_32_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_32_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_33',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_33_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_33_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_pause_34',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_35',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_35_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_35_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_35_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_35_SUBSCRIPT_bounce_to_xy_with_height_3',
                "command": 'bounce_to_xy_with_height',
                "args": [3, 20, 0]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_35_SUBSCRIPT_face_north_4',
                "command": 'face_north',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_35_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_35_SUBSCRIPT_face_east_6',
                "command": 'face_east',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_36',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_36_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_36_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_36_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_37',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_37_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_37_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_38',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_38_SUBSCRIPT_shift_northwest_steps_0',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_38_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_38_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_38_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_38_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_38_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_38_SUBSCRIPT_sequence_looping_off_6',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_38_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_38_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_39',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_39_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_39_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_39_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_39_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_39_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_40',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_40_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_40_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_40_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_pause_41',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_42',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_42_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_42_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_42_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_set_action_script_sync_43',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 579],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_set_action_script_sync_44',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 580],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_set_action_script_sync_45',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 578],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_pause_46',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_47',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_47_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_47_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_47_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_47_SUBSCRIPT_bounce_to_xy_with_height_3',
                "command": 'bounce_to_xy_with_height',
                "args": [3, 16, 0]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_47_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_47_SUBSCRIPT_face_southeast_5',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_pause_48',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_set_7000_to_tapped_button_49',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_pause_50',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_mem_7000_and_const_51',
        "command": 'mem_7000_and_const',
        "args": [0x0080],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_jmp_if_var_equals_short_52',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 128, 'EVENT_1368_action_queue_sync_54'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_jmp_53',
        "command": 'jmp',
        "args": ['EVENT_1368_set_7000_to_tapped_button_49'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_54',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_54_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [112]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_54_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_54_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_54_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_54_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_55',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_55_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_55_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_55_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_55_SUBSCRIPT_floating_on_3',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_55_SUBSCRIPT_shadow_on_4',
                "command": 'shadow_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_55_SUBSCRIPT_jump_to_height_silent_5',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_55_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_56',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_56_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_56_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_56_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._034_SQUIRM_WRITHE, 6]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_56_SUBSCRIPT_shift_north_pixels_3',
                "command": 'shift_north_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_56_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_56_SUBSCRIPT_shift_north_pixels_5',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_56_SUBSCRIPT_shift_south_pixels_6',
                "command": 'shift_south_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_pause_action_script_57',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_pause_action_script_58',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_pause_action_script_59',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_60',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_60_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_60_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_60_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_60_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_60_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_61',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_61_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_61_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_61_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_62',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_62_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_62_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_62_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_63',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_63_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_63_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_63_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_64',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_64_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_64_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_64_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._024_TAPPING_FEET, 6]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_64_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_65',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_65_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_65_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_65_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_65_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [32]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_65_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._025_HEEL_CLICK, 6]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_65_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_pause_66',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_play_sound_67',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_pause_68',
        "command": 'pause',
        "args": [45],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_69',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_69_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_70',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_70_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_70_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_70_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_70_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [6]
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_pause_71',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_72',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_72_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_72_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_72_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_72_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_73',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_73_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_73_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_73_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_73_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_74',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_74_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_74_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_74_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_74_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_pause_75',
        "command": 'pause',
        "args": [45],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_play_sound_76',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_pause_77',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_78',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_78_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_78_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_78_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_78_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_79',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_79_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_79_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_79_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_79_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_sync_80',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_sync_80_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_80_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_80_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1368_action_queue_sync_80_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_81',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_81_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_81_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_81_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_81_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_81_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [45]
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_remove_from_current_level_82',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_remove_from_current_level_83',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_remove_from_current_level_84',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_remove_from_current_level_85',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_apply_solidity_mod_86',
        "command": 'apply_solidity_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 1, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_set_bit_87',
        "command": 'set_bit',
        "args": [0x7053, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_set_action_script_async_88',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_set_89',
        "command": 'set',
        "args": [0x70a7, 78],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_set_90',
        "command": 'set',
        "args": [0x7000, 524],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_run_event_as_subroutine_91',
        "command": 'run_event_as_subroutine',
        "args": [3828],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_92',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_93',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_94',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_95',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_96',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_97',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_98',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_99',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_100',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_101',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_102',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_103',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_104',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_105',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_106',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_107',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_108',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_109',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_110',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_111',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_112',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_113',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_114',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_115',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_116',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_117',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_118',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_119',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_120',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_121',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_122',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_123',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_124',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_125',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_126',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_127',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_128',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_129',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_130',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_131',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_132',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_133',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_134',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_135',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_136',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_137',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_138',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_139',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_140',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_141',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_142',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_143',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_stop_sound_144',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_summon_to_level_145',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_7, Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_action_queue_async_146',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1368_action_queue_async_146_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_146_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1368_action_queue_async_146_SUBSCRIPT_shirt_to_xy_coords_2',
                "command": 'shirt_to_xy_coords',
                "args": [5, 29]
            },
        ]
    },
    {
        "identifier": 'EVENT_1368_unfreeze_camera_147',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1368_ret_148',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
