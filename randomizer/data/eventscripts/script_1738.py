from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1738_enable_controls_0',
        "command": 'enable_controls',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1738_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._150_GAME_INTRO_MOLEVILLE_OUTSIDE_DURING_BOWSERS_TROOP_SCENE, RadialDirections.SOUTH, 19, 31, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1738_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 771],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1738_fade_in_from_black_sync_3',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1738_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1738_action_queue_sync_4_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1738_action_queue_sync_4_SUBSCRIPT_walk_1_step_northwest_1',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1738_action_queue_sync_4_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1738_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_1738_action_queue_sync_4_SUBSCRIPT_walk_1_step_southwest_4',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1738_action_queue_sync_4_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1738_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1738_action_queue_sync_4_SUBSCRIPT_walk_1_step_southeast_7',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1738_action_queue_sync_4_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1738_action_queue_sync_4_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1738_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1738_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1738_action_queue_async_5_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1738_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1738_action_queue_async_5_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1738_action_queue_async_5_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1738_action_queue_async_5_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1738_action_queue_async_5_SUBSCRIPT_face_southeast_5',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1738_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1738_action_queue_async_5_SUBSCRIPT_set_solidity_bits_7',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1738_action_queue_async_5_SUBSCRIPT_jump_to_height_8',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1738_action_queue_async_5_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [24]
            },
        ]
    },
    {
        "identifier": 'EVENT_1738_freeze_all_npcs_until_return_6',
        "command": 'freeze_all_npcs_until_return',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1738_resume_action_script_7',
        "command": 'resume_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1738_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1738_action_queue_sync_8_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1738_action_queue_sync_8_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_1738_action_queue_sync_8_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1738_start_embedded_action_script_async_9',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_9_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_9_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_9_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [27, 42]
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_9_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_9_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1738_start_embedded_action_script_async_10',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_10_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_10_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_10_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_10_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [26, 44]
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_10_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_10_SUBSCRIPT_sequence_looping_off_5',
                "command": 'sequence_looping_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1738_start_embedded_action_script_async_11',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_11_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_11_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_11_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [27, 43]
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_11_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_11_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1738_start_embedded_action_script_async_12',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_12_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_12_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_12_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [26, 45]
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_12_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_12_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1738_start_embedded_action_script_async_13',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_13_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_13_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_13_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [28, 44]
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_13_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_13_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1738_start_embedded_action_script_async_14',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_14_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_14_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_14_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [27, 46]
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_14_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1738_start_embedded_action_script_async_14_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1738_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1738_action_queue_async_15_SUBSCRIPT_floating_on_0',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1738_action_queue_async_15_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1738_action_queue_async_15_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1738_action_queue_async_15_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x17, 0xbf]
            },
        ]
    },
    {
        "identifier": 'EVENT_1738_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1738_action_queue_async_16_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1738_action_queue_async_16_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1738_action_queue_async_16_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1738_action_queue_async_16_SUBSCRIPT_shift_north_pixels_3',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1738_action_queue_async_16_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1738_action_queue_async_16_SUBSCRIPT_shift_north_pixels_5',
                "command": 'shift_north_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_1738_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1738_action_queue_sync_17_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1738_action_queue_sync_17_SUBSCRIPT_walk_1_step_south_1',
                "command": 'walk_1_step_south',
                "args": []
            },
            {
                "identifier": 'EVENT_1738_action_queue_sync_17_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_1738_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1738_action_queue_async_18_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1738_action_queue_async_18_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1738_action_queue_async_18_SUBSCRIPT_shift_south_steps_2',
                "command": 'shift_south_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1738_action_queue_async_18_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1738_circle_mask_nonstatic_19',
        "command": 'circle_mask_nonstatic',
        "args": [AreaObjects.NPC_3, 30, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1738_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1738_action_queue_async_20_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1738_action_queue_async_20_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [80]
            },
        ]
    },
    {
        "identifier": 'EVENT_1738_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1738_action_queue_sync_21_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1738_action_queue_sync_21_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1738_action_queue_sync_21_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_1738_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1738_action_queue_async_22_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1738_action_queue_async_22_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [24]
            },
        ]
    },
    {
        "identifier": 'EVENT_1738_display_intro_title_23',
        "command": 'display_intro_title',
        "args": [6, IntroTitles.KING_BOWSER],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1738_pause_24',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1738_fade_out_to_black_async_duration_25',
        "command": 'fade_out_to_black_async_duration',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1738_jmp_to_event_26',
        "command": 'jmp_to_event',
        "args": [1730],
        "subscript": []
    },
]
