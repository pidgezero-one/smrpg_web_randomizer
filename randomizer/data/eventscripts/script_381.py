from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_381_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_jmp_if_object_not_in_level_1',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_0, Rooms._332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_set_bit_2',
        "command": 'set_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_set_bit_3',
        "command": 'set_bit',
        "args": [0x7043, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_381_action_queue_sync_4_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_4_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [12, 95]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_4_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_4_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_4_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
        ]
    },
    {
        "identifier": 'EVENT_381_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_381_action_queue_sync_5_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_381_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_381_action_queue_sync_6_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_381_remember_last_object_7',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_pause_8',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7043, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 103],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_remember_last_object_11',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_set_bit_12',
        "command": 'set_bit',
        "args": [0x7043, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_pause_13',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_clear_bit_14',
        "command": 'clear_bit',
        "args": [0x7043, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 103],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_381_action_queue_async_16_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_381_action_queue_async_16_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_381_set_bit_17',
        "command": 'set_bit',
        "args": [0x7043, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_pause_18',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_remember_last_object_19',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_381_action_queue_sync_20_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_20_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4]]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_20_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_20_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_20_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_20_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x25, 0xc0, 0x06, 0x60, 0xff]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_20_SUBSCRIPT_shift_southeast_pixels_6',
                "command": 'shift_southeast_pixels',
                "args": [11]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_20_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_20_SUBSCRIPT_shift_southeast_pixels_8',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_20_SUBSCRIPT_bpl_26_27_28_9',
                "command": 'bpl_26_27_28',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_381_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_381_action_queue_sync_21_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_21_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4]]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_21_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_21_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_21_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_21_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x25, 0xc0, 0x06, 0x60, 0xff]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_21_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 6]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_21_SUBSCRIPT_shift_northwest_pixels_7',
                "command": 'shift_northwest_pixels',
                "args": [11]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_21_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_21_SUBSCRIPT_shift_northwest_pixels_9',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_21_SUBSCRIPT_bpl_26_27_28_10',
                "command": 'bpl_26_27_28',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_381_remember_last_object_22',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_start_battle_23',
        "command": 'start_battle',
        "args": [0x000b, 15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_set_bit_24',
        "command": 'set_bit',
        "args": [0x704a, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_run_event_as_subroutine_25',
        "command": 'run_event_as_subroutine',
        "args": [1011],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_remove_from_level_26',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_remove_from_level_27',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_remove_from_current_level_28',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_remove_from_current_level_29',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_jmp_if_object_not_in_level_30',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM, 'EVENT_381_jmp_if_object_in_level_45'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_fade_in_from_black_async_31',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_ret_32',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_ret_33',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_ret_34',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_ret_35',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_ret_36',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_ret_37',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_ret_38',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_ret_39',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_ret_40',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_ret_41',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_ret_42',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_ret_43',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_ret_44',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_jmp_if_object_in_level_45',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_4, Rooms._325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL, 'EVENT_257_fade_in_from_black_async_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_action_queue_sync_46',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_381_action_queue_sync_46_SUBSCRIPT_face_south_0',
                "command": 'face_south',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_381_action_queue_async_47',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_381_action_queue_async_47_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_381_action_queue_async_47_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_381_action_queue_async_47_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_381_fade_in_from_black_async_48',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_action_queue_async_49',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_381_action_queue_async_49_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_381_action_queue_async_49_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_381_apply_tile_mod_50',
        "command": 'apply_tile_mod',
        "args": [Rooms._332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_apply_solidity_mod_51',
        "command": 'apply_solidity_mod',
        "args": [Rooms._332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_play_sound_52',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_action_queue_sync_53',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_381_action_queue_sync_53_SUBSCRIPT_walk_1_step_northeast_0',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_53_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_53_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
        ]
    },
    {
        "identifier": 'EVENT_381_action_queue_sync_54',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_381_action_queue_sync_54_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_54_SUBSCRIPT_face_east_1',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_54_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_381_action_queue_sync_54_SUBSCRIPT_face_south_3',
                "command": 'face_south',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_381_remember_last_object_55',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_381_ret_56',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
