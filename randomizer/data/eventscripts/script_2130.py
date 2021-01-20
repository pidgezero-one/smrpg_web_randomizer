from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2130_run_dialog_0',
        "command": 'run_dialog',
        "args": [3350, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2130_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2130_action_queue_async_1_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2130_enable_controls_until_return_2',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2130_pause_3',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2130_fade_out_music_to_volume_4',
        "command": 'fade_out_music_to_volume',
        "args": [5, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2130_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2130_action_queue_async_5_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [2, 56]
            },
            {
                "identifier": 'EVENT_2130_action_queue_async_5_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2130_action_queue_async_5_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2130_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2130_action_queue_async_5_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2130_action_queue_async_5_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2130_action_queue_async_5_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2130_action_queue_async_5_SUBSCRIPT_shift_southeast_steps_7',
                "command": 'shift_southeast_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_2130_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2130_action_queue_async_5_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2130_action_queue_async_5_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2130_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2130_action_queue_async_5_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [120]
            },
        ]
    },
    {
        "identifier": 'EVENT_2130_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2130_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2130_action_queue_sync_6_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_2130_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2130_action_queue_sync_6_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_2130_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [11, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2130_action_queue_sync_6_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_2130_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2130_action_queue_sync_6_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [40]
            },
        ]
    },
    {
        "identifier": 'EVENT_2130_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2130_action_queue_async_7_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_2130_action_queue_async_7_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_2130_action_queue_async_7_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2130_action_queue_async_7_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2130_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2130_action_queue_async_7_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [50]
            },
        ]
    },
    {
        "identifier": 'EVENT_2130_start_battle_8',
        "command": 'start_battle',
        "args": [0x00d0, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2130_jmp_if_bit_clear_9',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_2130_unfreeze_camera_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2130_reset_and_choose_game_10',
        "command": 'reset_and_choose_game',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2130_unfreeze_camera_11',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2130_palette_set_12',
        "command": 'palette_set',
        "args": [84, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2130_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2130_action_queue_sync_13_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2130_action_queue_sync_13_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2130_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2130_action_queue_async_14_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2130_action_queue_async_14_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2130_fade_in_from_black_async_15',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2130_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2130_action_queue_async_16_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_2130_action_queue_async_16_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2130_action_queue_async_16_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2130_action_queue_async_16_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2130_action_queue_async_16_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [11]
            },
            {
                "identifier": 'EVENT_2130_action_queue_async_16_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2130_pause_17',
        "command": 'pause',
        "args": [35],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2130_play_sound_18',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2130_pause_19',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2130_set_bit_20',
        "command": 'set_bit',
        "args": [0x7092, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2130_remove_from_level_21',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2130_set_action_script_async_22',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2130_enable_controls_until_return_23',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2130_restore_all_hp_24',
        "command": 'restore_all_hp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2130_restore_all_fp_25',
        "command": 'restore_all_fp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2130_play_music_default_volume_26',
        "command": 'play_music_default_volume',
        "args": [Music._61_VALENTINA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2130_ret_27',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
