from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2209_pause_0',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_fade_out_music_to_volume_1',
        "command": 'fade_out_music_to_volume',
        "args": [7, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2209_action_queue_async_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_2_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_2209_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2209_action_queue_async_3_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [25, 101]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_3_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_3_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._044_GHOST_FLOAT, 4]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_3_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_3_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_3_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_3_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_3_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_3_SUBSCRIPT_end_loop_8',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_3_SUBSCRIPT_start_loop_n_times_9',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_3_SUBSCRIPT_visibility_on_10',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_3_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_3_SUBSCRIPT_visibility_off_12',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_3_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_3_SUBSCRIPT_end_loop_14',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_3_SUBSCRIPT_start_loop_n_times_15',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_3_SUBSCRIPT_visibility_on_16',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_3_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_3_SUBSCRIPT_visibility_off_18',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_3_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_3_SUBSCRIPT_end_loop_20',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_3_SUBSCRIPT_visibility_on_21',
                "command": 'visibility_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2209_pause_4',
        "command": 'pause',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2209_action_queue_async_5_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2209_pause_6',
        "command": 'pause',
        "args": [80],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_start_battle_7',
        "command": 'start_battle',
        "args": [0x00d1, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_jmp_if_bit_clear_8',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_2209_fade_in_from_black_async_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_jmp_to_event_9',
        "command": 'jmp_to_event',
        "args": [3819],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_play_music_default_volume_11',
        "command": 'play_music_default_volume',
        "args": [Music._51_MONSTRO_TOWN],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_palette_set_morphs_12',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 12, 138, 11],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2209_action_queue_async_13_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_13_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_13_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_13_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_13_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_13_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_13_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [11, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_13_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_13_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [15]
            },
        ]
    },
    {
        "identifier": 'EVENT_2209_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2209_action_queue_async_14_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_14_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_14_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_14_SUBSCRIPT_start_loop_n_times_5',
                "command": 'start_loop_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_14_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [16, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_14_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [17, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_14_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_14_SUBSCRIPT_end_loop_12',
                "command": 'end_loop',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2209_palette_set_15',
        "command": 'palette_set',
        "args": [139, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2209_action_queue_async_17_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._055_LOSE_COINS_COIN_FOUNTAIN, 6]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_17_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_17_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_17_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_17_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_17_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_17_SUBSCRIPT_end_loop_6',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_17_SUBSCRIPT_start_loop_n_times_7',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_17_SUBSCRIPT_visibility_on_8',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_17_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_17_SUBSCRIPT_visibility_off_10',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_17_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_17_SUBSCRIPT_end_loop_12',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_17_SUBSCRIPT_start_loop_n_times_13',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_17_SUBSCRIPT_visibility_on_14',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_17_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_17_SUBSCRIPT_visibility_off_16',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_17_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_17_SUBSCRIPT_end_loop_18',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_17_SUBSCRIPT_visibility_on_19',
                "command": 'visibility_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2209_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2209_action_queue_async_18_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_18_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_18_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2209_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2209_action_queue_async_19_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_19_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_19_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_19_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_19_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2209_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2209_action_queue_async_20_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_20_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_20_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2209_action_queue_async_20_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2209_set_bit_21',
        "command": 'set_bit',
        "args": [0x7093, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_restore_all_hp_22',
        "command": 'restore_all_hp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_restore_all_fp_23',
        "command": 'restore_all_fp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_set_short_24',
        "command": 'set_short',
        "args": [0x700a, 0x00e3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_jmp_to_event_25',
        "command": 'jmp_to_event',
        "args": [720],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_ret_26',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_27',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_28',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_29',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_30',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_31',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_32',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_33',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_34',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_35',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_36',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_37',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_38',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_39',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_40',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_41',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_42',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_43',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_44',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_45',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_46',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_47',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_48',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_49',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_50',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_51',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_52',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_53',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_54',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_55',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_56',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_57',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_58',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_59',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_60',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_61',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_62',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_63',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_64',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_65',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_66',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_67',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_68',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_69',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_70',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_71',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_72',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_73',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_74',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_75',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_76',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_77',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_78',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_79',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_80',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_81',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_82',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_83',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_84',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_85',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_86',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_87',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_88',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_89',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_90',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_91',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_92',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_93',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_94',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_95',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_96',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_97',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_stop_sound_98',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2209_ret_99',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
