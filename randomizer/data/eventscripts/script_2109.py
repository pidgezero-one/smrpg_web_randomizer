from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2109_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7092, 5, 'EVENT_2109_ret_38'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7092, 6, 'EVENT_2109_ret_38'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_fade_out_music_to_volume_2',
        "command": 'fade_out_music_to_volume',
        "args": [0, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2109_action_queue_async_3_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_3_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_3_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_3_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_3_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_3_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_3_SUBSCRIPT_walk_to_xy_coords_6',
                "command": 'walk_to_xy_coords',
                "args": [17, 15]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_3_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_3_SUBSCRIPT_face_southeast_8',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2109_pause_4',
        "command": 'pause',
        "args": [40],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_pause_5',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2109_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2109_pause_7',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_pause_8',
        "command": 'pause',
        "args": [80],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2109_action_queue_async_9_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_9_SUBSCRIPT_sequence_looping_off_1',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_9_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_9_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_9_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_9_SUBSCRIPT_shift_southwest_pixels_5',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_9_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [15]
            },
        ]
    },
    {
        "identifier": 'EVENT_2109_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2109_action_queue_async_10_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_10_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_10_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_10_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_10_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_10_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_10_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_10_SUBSCRIPT_shift_southeast_steps_7',
                "command": 'shift_southeast_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_10_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_10_SUBSCRIPT_set_solidity_bits_9',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_10_SUBSCRIPT_visibility_off_10',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2109_stop_sound_11',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_stop_sound_12',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_stop_sound_13',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_stop_sound_14',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_stop_sound_15',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_stop_sound_16',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_stop_sound_17',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_stop_sound_18',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_stop_sound_19',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_stop_sound_20',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_stop_sound_21',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_stop_sound_22',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_stop_sound_23',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_stop_sound_24',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_stop_sound_25',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_stop_sound_26',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_enter_area_27',
        "command": 'enter_area',
        "args": [Rooms._110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM, RadialDirections.SOUTHEAST, 2, 56, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_action_queue_async_28',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2109_action_queue_async_28_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_28_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [1, 49]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_28_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_28_SUBSCRIPT_shift_east_pixels_3',
                "command": 'shift_east_pixels',
                "args": [13]
            },
        ]
    },
    {
        "identifier": 'EVENT_2109_palette_set_29',
        "command": 'palette_set',
        "args": [111, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2109_action_queue_sync_30_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2109_action_queue_sync_30_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2109_action_queue_sync_30_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2109_action_queue_sync_31',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2109_action_queue_sync_31_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2109_action_queue_sync_31_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2109_action_queue_sync_31_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2109_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2109_action_queue_async_32_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_32_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_32_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2109_fade_in_from_black_async_33',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_freeze_camera_34',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_action_queue_async_35',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2109_action_queue_async_35_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_35_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_35_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_35_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_35_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2109_action_queue_async_35_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2109_pause_36',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_jmp_37',
        "command": 'jmp',
        "args": ['EVENT_2114_fade_out_music_to_volume_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2109_ret_38',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
