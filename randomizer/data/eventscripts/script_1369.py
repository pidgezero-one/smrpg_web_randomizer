from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1369_pause_0',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_enable_controls_until_return_1',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_start_battle_2',
        "command": 'start_battle',
        "args": [0x00a1, 12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_1369_action_queue_sync_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_reset_and_choose_game_4',
        "command": 'reset_and_choose_game',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1369_action_queue_sync_5_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1369_action_queue_sync_5_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1369_action_queue_sync_5_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1369_action_queue_sync_5_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [3, 23, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1369_action_queue_sync_5_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1369_action_queue_sync_5_SUBSCRIPT_face_northeast_5',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1369_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1369_action_queue_sync_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1369_action_queue_sync_6_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [4, 21, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1369_action_queue_sync_6_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1369_action_queue_sync_6_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1369_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1369_action_queue_sync_7_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1369_action_queue_sync_7_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1369_action_queue_sync_7_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1369_action_queue_sync_7_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [5, 20, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1369_action_queue_sync_7_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1369_action_queue_sync_7_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1369_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1369_action_queue_sync_8_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1369_action_queue_sync_8_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1369_action_queue_sync_8_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1369_action_queue_sync_8_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [5, 19, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1369_action_queue_sync_8_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1369_action_queue_sync_8_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1369_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1369_action_queue_async_9_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1369_action_queue_async_9_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1369_action_queue_async_9_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1369_action_queue_async_9_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [6, 18, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1369_action_queue_async_9_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1369_action_queue_async_9_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1369_unfreeze_camera_10',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_apply_solidity_mod_11',
        "command": 'apply_solidity_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 2, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_set_bit_12',
        "command": 'set_bit',
        "args": [0x7053, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_fade_in_from_black_async_13',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1369_action_queue_sync_14_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_1369_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1369_action_queue_sync_15_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_1369_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1369_action_queue_sync_16_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_1369_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1369_action_queue_sync_17_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_1369_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1369_action_queue_async_18_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1369_action_queue_async_18_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1369_action_queue_async_18_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1369_action_queue_async_18_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1369_action_queue_async_18_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1369_action_queue_async_18_SUBSCRIPT_set_priority_5',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1369_action_queue_async_18_SUBSCRIPT_set_vram_priority_6',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_1369_action_queue_async_18_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1369_action_queue_async_18_SUBSCRIPT_fixed_f_coord_off_8',
                "command": 'fixed_f_coord_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1369_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1369_action_queue_sync_19_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1369_action_queue_sync_19_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1369_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1369_action_queue_sync_20_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1369_action_queue_sync_20_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1369_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1369_action_queue_sync_21_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1369_action_queue_sync_21_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1369_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1369_action_queue_async_22_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1369_action_queue_async_22_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1369_remove_from_current_level_23',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_remove_from_current_level_24',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_remove_from_current_level_25',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_remove_from_current_level_26',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_pause_27',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_enable_controls_until_return_28',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_set_action_script_async_29',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_restore_all_hp_30',
        "command": 'restore_all_hp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_restore_all_fp_31',
        "command": 'restore_all_fp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_set_short_32',
        "command": 'set_short',
        "args": [0x700a, 0x00cf],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_jmp_to_event_33',
        "command": 'jmp_to_event',
        "args": [720],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_stop_sound_34',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_stop_sound_35',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_stop_sound_36',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_stop_sound_37',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_stop_sound_38',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_stop_sound_39',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_stop_sound_40',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_stop_sound_41',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_stop_sound_42',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_stop_sound_43',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_stop_sound_44',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1369_ret_45',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
