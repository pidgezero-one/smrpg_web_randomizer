from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2278_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2278_action_queue_sync_0_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_0_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [4, 23, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_0_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_0_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_0_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2278_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2278_action_queue_sync_1_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_1_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [5, 22, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_1_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_1_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2278_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2278_action_queue_sync_2_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_2_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [5, 21, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_2_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_2_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_2_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2278_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2278_action_queue_sync_3_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_3_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [5, 17, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_3_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_3_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_3_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2278_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2278_action_queue_async_4_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [4, 20]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_4_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_4_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_4_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2278_remove_from_current_level_5',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2278_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x709a, 1, 'EVENT_2278_action_queue_sync_33'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2278_fade_in_from_black_async_7',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2278_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2278_action_queue_async_8_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [12]
            },
        ]
    },
    {
        "identifier": 'EVENT_2278_pause_9',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2278_run_dialog_10',
        "command": 'run_dialog',
        "args": [3424, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2278_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2278_action_queue_async_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_11_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_11_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_11_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_11_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [75]
            },
        ]
    },
    {
        "identifier": 'EVENT_2278_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2278_action_queue_sync_12_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_12_SUBSCRIPT_sequence_looping_off_1',
                "command": 'sequence_looping_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2278_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2278_action_queue_async_13_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_13_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_13_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_13_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_13_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_13_SUBSCRIPT_fixed_f_coord_off_5',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_13_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_13_SUBSCRIPT_shift_northwest_steps_7',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_2278_pause_14',
        "command": 'pause',
        "args": [50],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2278_run_dialog_15',
        "command": 'run_dialog',
        "args": [3425, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2278_pause_16',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2278_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2278_action_queue_async_17_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_17_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_17_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_17_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_17_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_17_SUBSCRIPT_fixed_f_coord_on_5',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_17_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_17_SUBSCRIPT_shift_northeast_pixels_7',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_2278_pause_18',
        "command": 'pause',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2278_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2278_action_queue_sync_19_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_19_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_19_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_19_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_19_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2278_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2278_action_queue_sync_20_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_20_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_20_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_20_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_20_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2278_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2278_action_queue_sync_21_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_21_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_21_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_21_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_21_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2278_pause_22',
        "command": 'pause',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2278_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2278_action_queue_async_23_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_23_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_23_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_23_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [10]
            },
        ]
    },
    {
        "identifier": 'EVENT_2278_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2278_action_queue_async_24_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_24_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_24_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_24_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_24_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_24_SUBSCRIPT_fixed_f_coord_on_5',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_24_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_24_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_24_SUBSCRIPT_shift_northeast_pixels_8',
                "command": 'shift_northeast_pixels',
                "args": [10]
            },
        ]
    },
    {
        "identifier": 'EVENT_2278_pause_25',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2278_fade_out_to_black_async_duration_26',
        "command": 'fade_out_to_black_async_duration',
        "args": [70],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2278_enter_area_27',
        "command": 'enter_area',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, RadialDirections.SOUTHWEST, 3, 26, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2278_freeze_camera_28',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2278_action_queue_async_29',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2278_action_queue_async_29_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_29_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_29_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_29_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_29_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_29_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_29_SUBSCRIPT_fixed_f_coord_off_6',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_29_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2278_unfreeze_camera_30',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2278_set_bit_31',
        "command": 'set_bit',
        "args": [0x709a, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2278_ret_32',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2278_action_queue_sync_33',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2278_action_queue_sync_33_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_33_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_33_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2278_action_queue_sync_34',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2278_action_queue_sync_34_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_34_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_34_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2278_action_queue_sync_35',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2278_action_queue_sync_35_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_35_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_35_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2278_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2278_action_queue_sync_36_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [4, 16, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_36_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_sync_36_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2278_action_queue_async_37',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2278_action_queue_async_37_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [3, 17, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_37_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_37_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_37_SUBSCRIPT_sequence_looping_off_3',
                "command": 'sequence_looping_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2278_fade_in_from_black_async_38',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2278_action_queue_async_39',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2278_action_queue_async_39_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [12]
            },
        ]
    },
    {
        "identifier": 'EVENT_2278_pause_40',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2278_enter_area_41',
        "command": 'enter_area',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, RadialDirections.SOUTHWEST, 3, 26, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2278_freeze_camera_42',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2278_action_queue_async_43',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2278_action_queue_async_43_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_43_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_43_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_43_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_43_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_43_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_43_SUBSCRIPT_fixed_f_coord_off_6',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_43_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2278_unfreeze_camera_44',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2278_ret_45',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
