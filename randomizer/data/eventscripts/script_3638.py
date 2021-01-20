from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3638_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 4, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_set_bit_2',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_3_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_3_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_3_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3638_action_queue_async_3_SUBSCRIPT_pause_1']
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_3_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [3, 17]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_3_SUBSCRIPT_face_east_4',
                "command": 'face_east',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_4_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_4_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_4_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_4_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [3, 17, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_4_SUBSCRIPT_transfer_xyzf_pixels_4',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 2, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_4_SUBSCRIPT_face_northeast_5',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_6',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_4_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_4_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_4_SUBSCRIPT_visibility_on_9',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_4_SUBSCRIPT_shift_east_pixels_10',
                "command": 'shift_east_pixels',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_4_SUBSCRIPT_sequence_looping_off_11',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_4_SUBSCRIPT_fixed_f_coord_off_12',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_4_SUBSCRIPT_reset_properties_13',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_4_SUBSCRIPT_face_northwest_14',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_pause_5',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_run_dialog_6',
        "command": 'run_dialog',
        "args": [2420, AreaObjects.NPC_9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_pause_7',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_8_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_8_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_8_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_8_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_9_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_9_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_run_dialog_10',
        "command": 'run_dialog',
        "args": [2421, AreaObjects.NPC_0, [_0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_remember_last_object_11',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_12_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_12_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_12_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_12_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_12_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_unsync_dialog_13',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_14_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_14_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_14_SUBSCRIPT_sequence_looping_off_2',
                "command": 'sequence_looping_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_run_dialog_15',
        "command": 'run_dialog',
        "args": [2432, AreaObjects.NPC_0, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_run_dialog_16',
        "command": 'run_dialog',
        "args": [2422, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_remember_last_object_17',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_pause_18',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_19_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_19_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_19_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_pause_20',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_run_dialog_21',
        "command": 'run_dialog',
        "args": [2433, AreaObjects.NPC_9, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_22_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_22_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [17, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_22_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_22_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_22_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_22_SUBSCRIPT_face_southeast_6',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_23_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_23_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_23_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_23_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_23_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_23_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_23_SUBSCRIPT_face_east_6',
                "command": 'face_east',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_pause_24',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_run_dialog_25',
        "command": 'run_dialog',
        "args": [2434, AreaObjects.NPC_9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_pause_26',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_run_dialog_27',
        "command": 'run_dialog',
        "args": [2423, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_pause_28',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_29_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_29_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [240]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_29_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._019_LONG_FALL, 4]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_29_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_29_SUBSCRIPT_floating_off_4',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_29_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_29_SUBSCRIPT_floating_on_6',
                "command": 'floating_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_30',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_30_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_30_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_30_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_30_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_30_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [90]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_30_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_pause_31',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_jmp_if_object_in_air_32',
        "command": 'jmp_if_object_in_air',
        "args": [AreaObjects.NPC_9, 'EVENT_3638_pause_31'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_stop_sound_33',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_34_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_34_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_34_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_run_dialog_35',
        "command": 'run_dialog',
        "args": [2424, AreaObjects.NPC_9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_pause_36',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_37',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_37_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_37_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_37_SUBSCRIPT_walk_1_step_southeast_2',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_37_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_pause_38',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_39',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_39_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_40',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_40_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [16, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_fade_out_music_to_volume_41',
        "command": 'fade_out_music_to_volume',
        "args": [2, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_pause_42',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_set_action_script_async_43',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_pause_44',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_freeze_camera_45',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_play_music_default_volume_46',
        "command": 'play_music_default_volume',
        "args": [Music._36_EXPLANATION],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_47_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_47_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_47_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_48',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_48_SUBSCRIPT_shift_west_pixels_0',
                "command": 'shift_west_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_48_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_48_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [240]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_48_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_48_SUBSCRIPT_floating_off_4',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_48_SUBSCRIPT_shadow_off_5',
                "command": 'shadow_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_49',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_49_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_49_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [4, 20, 20, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_49_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 252, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_49_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_49_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_49_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_49_SUBSCRIPT_floating_on_6',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_49_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_49_SUBSCRIPT_db_8',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x1f, 0xab]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_49_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [24, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_49_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_49_SUBSCRIPT_shift_z_up_pixels_11',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_set_action_script_sync_50',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_11, 880],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_pause_51',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_52',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_52_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_52_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_52_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_53',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_53_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_53_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_53_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_53_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [3, 19, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_53_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_53_SUBSCRIPT_transfer_xyzf_pixels_5',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 4, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_53_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_53_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_53_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_53_SUBSCRIPT_floating_on_9',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_53_SUBSCRIPT_face_west_10',
                "command": 'face_west',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_53_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_53_SUBSCRIPT_face_southwest_12',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_53_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_53_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_53_SUBSCRIPT_shift_southwest_pixels_15',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_54',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_54_SUBSCRIPT_face_west_0',
                "command": 'face_west',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_54_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_54_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_54_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_54_SUBSCRIPT_face_north_4',
                "command": 'face_north',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_54_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_54_SUBSCRIPT_face_northeast_6',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_54_SUBSCRIPT_jump_to_height_silent_7',
                "command": 'jump_to_height_silent',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_54_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_54_SUBSCRIPT_floating_off_9',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_54_SUBSCRIPT_visibility_off_10',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_55',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_55_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_55_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_55_SUBSCRIPT_sequence_playback_off_2',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_55_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [3, 20, 1, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_set_action_script_sync_56',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_pause_57',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_58',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_58_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_58_SUBSCRIPT_floating_on_1',
                "command": 'floating_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_start_embedded_action_script_async_59',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3638_start_embedded_action_script_async_59_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_start_embedded_action_script_async_59_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_remember_last_object_60',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_61',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_61_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_61_SUBSCRIPT_face_north_1',
                "command": 'face_north',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_61_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_61_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_61_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_61_SUBSCRIPT_face_west_5',
                "command": 'face_west',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_61_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_61_SUBSCRIPT_face_southwest_7',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_61_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_61_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_61_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_61_SUBSCRIPT_visibility_off_11',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_pause_action_script_62',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_11],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_start_embedded_action_script_async_63',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3638_start_embedded_action_script_async_63_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_start_embedded_action_script_async_63_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_start_embedded_action_script_async_63_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 248, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3638_start_embedded_action_script_async_63_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_start_embedded_action_script_async_63_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_start_embedded_action_script_async_63_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3638_start_embedded_action_script_async_63_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_64',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_64_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_64_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_64_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_64_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_65',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_65_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_65_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_65_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_65_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_66',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_66_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_66_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_66_SUBSCRIPT_walk_1_step_northwest_2',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_66_SUBSCRIPT_face_north_3',
                "command": 'face_north',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_66_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_66_SUBSCRIPT_face_northeast_5',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_66_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_66_SUBSCRIPT_face_east_7',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_66_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_66_SUBSCRIPT_face_southeast_9',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_66_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_66_SUBSCRIPT_jump_to_height_silent_11',
                "command": 'jump_to_height_silent',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_66_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_66_SUBSCRIPT_visibility_off_13',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_pause_action_script_67',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_start_embedded_action_script_async_68',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3638_start_embedded_action_script_async_68_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_start_embedded_action_script_async_68_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_start_embedded_action_script_async_68_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [3, 18, 1, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3638_start_embedded_action_script_async_68_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_start_embedded_action_script_async_68_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3638_start_embedded_action_script_async_68_SUBSCRIPT_sequence_playback_on_5',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_start_embedded_action_script_async_68_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_start_embedded_action_script_async_68_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [28]
            },
            {
                "identifier": 'EVENT_3638_start_embedded_action_script_async_68_SUBSCRIPT_visibility_on_8',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_start_embedded_action_script_async_68_SUBSCRIPT_shift_z_down_pixels_9',
                "command": 'shift_z_down_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3638_start_embedded_action_script_async_68_SUBSCRIPT_sequence_looping_off_10',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_start_embedded_action_script_async_68_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_start_embedded_action_script_async_68_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_69',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_69_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_69_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_69_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_70',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_70_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_70_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_70_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_70_SUBSCRIPT_face_south_3',
                "command": 'face_south',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_70_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_70_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_70_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_70_SUBSCRIPT_face_west_7',
                "command": 'face_west',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_70_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_70_SUBSCRIPT_face_northwest_9',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_70_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_70_SUBSCRIPT_visibility_off_11',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_71',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_71_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [67]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_71_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_71_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_71_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_71_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_72',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_72_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_72_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_72_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_72_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_72_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_72_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_72_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_73',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_73_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_73_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_73_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_73_SUBSCRIPT_face_north_3',
                "command": 'face_north',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_73_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_73_SUBSCRIPT_face_northeast_5',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_73_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_73_SUBSCRIPT_face_east_7',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_73_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_73_SUBSCRIPT_face_southeast_9',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_73_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_73_SUBSCRIPT_visibility_off_11',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_74',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_74_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [39]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_74_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_74_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_74_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_74_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_74_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_74_SUBSCRIPT_face_southwest_6',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_74_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_74_SUBSCRIPT_face_northwest_8',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_74_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_74_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_74_SUBSCRIPT_fixed_f_coord_on_11',
                "command": 'fixed_f_coord_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_75',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_75_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_75_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_75_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_75_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_75_SUBSCRIPT_end_loop_4',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_75_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_76',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_76_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_76_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_76_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_76_SUBSCRIPT_walk_1_step_southeast_3',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_76_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_76_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_77',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [68]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_face_southeast_10',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_reset_properties_11',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_face_southwest_13',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_face_northwest_15',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_start_loop_n_times_17',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_reset_properties_20',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_pause_21',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_end_loop_22',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_77_SUBSCRIPT_visibility_off_23',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_78',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_78_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_78_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_78_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_78_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [3, 19, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_78_SUBSCRIPT_floating_on_4',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_78_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_78_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_fade_out_music_to_volume_79',
        "command": 'fade_out_music_to_volume',
        "args": [2, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_80',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_80_SUBSCRIPT_shift_east_pixels_0',
                "command": 'shift_east_pixels',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_80_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_80_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_81',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_81_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_81_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_play_music_default_volume_82',
        "command": 'play_music_default_volume',
        "args": [Music._50_NIMBUS_LAND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_pause_83',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_set_action_script_async_84',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_pause_85',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_run_dialog_86',
        "command": 'run_dialog',
        "args": [2435, AreaObjects.NPC_9, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_pause_87',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_88',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_88_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_89',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_89_SUBSCRIPT_walk_1_step_northwest_0',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_89_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_pause_90',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_run_dialog_91',
        "command": 'run_dialog',
        "args": [2436, AreaObjects.NPC_9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_pause_92',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_93',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_93_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_93_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_93_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_93_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_93_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_93_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_93_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_pause_94',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_run_dialog_95',
        "command": 'run_dialog',
        "args": [2437, AreaObjects.NPC_9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_pause_96',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_97',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_97_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_97_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_97_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [31, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_97_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [50]
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_pause_98',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_99',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_99_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_99_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_99_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_99_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_99_SUBSCRIPT_face_east_4',
                "command": 'face_east',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_100',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_100_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_100_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_100_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_pause_101',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_run_dialog_102',
        "command": 'run_dialog',
        "args": [2425, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_pause_103',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_104',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_104_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_104_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_run_dialog_105',
        "command": 'run_dialog',
        "args": [2426, AreaObjects.NPC_9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_106',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_106_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_106_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_106_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_106_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_106_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_106_SUBSCRIPT_sequence_looping_on_5',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_106_SUBSCRIPT_walk_1_step_south_6',
                "command": 'walk_1_step_south',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_106_SUBSCRIPT_sequence_looping_off_7',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_106_SUBSCRIPT_fixed_f_coord_off_8',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_106_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_106_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [11, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_106_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_106_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_106_SUBSCRIPT_shift_southwest_steps_13',
                "command": 'shift_southwest_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_106_SUBSCRIPT_visibility_off_14',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_107',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_107_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_107_SUBSCRIPT_face_south_1',
                "command": 'face_south',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_107_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_107_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_108',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_108_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_108_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_remember_last_object_109',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_pause_110',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_run_dialog_111',
        "command": 'run_dialog',
        "args": [2419, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_pause_112',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_play_sound_113',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_pause_114',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_115',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_115_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_115_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_115_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_115_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_115_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_115_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_115_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_115_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_115_SUBSCRIPT_start_loop_n_times_8',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_115_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_115_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_115_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_115_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_115_SUBSCRIPT_end_loop_13',
                "command": 'end_loop',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_116',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_116_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [100]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_116_SUBSCRIPT_face_south_1',
                "command": 'face_south',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_116_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_116_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_116_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_116_SUBSCRIPT_face_east_5',
                "command": 'face_east',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_pause_117',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_118',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_118_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_118_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_118_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_118_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_118_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_118_SUBSCRIPT_face_southeast_5',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_118_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_118_SUBSCRIPT_face_southwest_7',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_119',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_119_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_run_dialog_120',
        "command": 'run_dialog',
        "args": [2427, AreaObjects.NPC_9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_pause_121',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_unfreeze_camera_122',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_123',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_123_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_123_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_123_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_123_SUBSCRIPT_walk_1_step_northeast_3',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_123_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_123_SUBSCRIPT_fixed_f_coord_off_5',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_123_SUBSCRIPT_face_southeast_6',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_pause_124',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_action_queue_sync_125',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_sync_125_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_125_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_125_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_125_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3638_action_queue_sync_125_SUBSCRIPT_face_south_4',
                "command": 'face_south',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_action_queue_async_126',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3638_action_queue_async_126_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_126_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_126_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3638_action_queue_async_126_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [28, 85, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_3638_set_action_script_sync_127',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_set_bit_128',
        "command": 'set_bit',
        "args": [0x705f, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_set_bit_129',
        "command": 'set_bit',
        "args": [0x705e, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3638_ret_130',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
