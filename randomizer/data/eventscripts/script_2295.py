from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2295_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA, RadialDirections.NORTHEAST, 22, 74, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2295_freeze_camera_1',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2295_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2295_action_queue_sync_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_2_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [18, 55, 0]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_2_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_2295_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2295_action_queue_sync_3_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2295_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2295_action_queue_sync_4_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_4_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [1]
            },
        ]
    },
    {
        "identifier": 'EVENT_2295_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_2295_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_5_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [1]
            },
        ]
    },
    {
        "identifier": 'EVENT_2295_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2295_action_queue_async_6_SUBSCRIPT_shift_southeast_pixels_0',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2295_action_queue_async_6_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_async_6_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2295_star_mask_expand_from_screen_center_7',
        "command": 'star_mask_expand_from_screen_center',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2295_pause_8',
        "command": 'pause',
        "args": [95],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2295_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2295_action_queue_async_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2295_action_queue_async_9_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2295_action_queue_async_9_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_2295_pause_10',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2295_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_2295_action_queue_async_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2295_action_queue_async_11_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2295_action_queue_async_11_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_2295_pause_12',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2295_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2295_action_queue_async_13_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_async_13_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_async_13_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2295_action_queue_async_13_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_async_13_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_async_13_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_2295_action_queue_async_13_SUBSCRIPT_shift_southeast_pixels_6',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_2295_pause_14',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2295_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_2295_action_queue_sync_15_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_15_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_15_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_15_SUBSCRIPT_shift_southeast_pixels_3',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_15_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_15_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_15_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_15_SUBSCRIPT_shift_northwest_steps_7',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_15_SUBSCRIPT_shift_southwest_steps_8',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_15_SUBSCRIPT_shift_southeast_steps_9',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_15_SUBSCRIPT_shift_southeast_pixels_10',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_15_SUBSCRIPT_shift_southwest_steps_11',
                "command": 'shift_southwest_steps',
                "args": [10]
            },
        ]
    },
    {
        "identifier": 'EVENT_2295_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2295_action_queue_sync_16_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_16_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_16_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_16_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_16_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_16_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_16_SUBSCRIPT_shift_southeast_pixels_6',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_16_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_16_SUBSCRIPT_shift_northeast_steps_8',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_16_SUBSCRIPT_shift_northwest_steps_9',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_16_SUBSCRIPT_shift_southwest_steps_10',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_16_SUBSCRIPT_shift_southeast_steps_11',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_16_SUBSCRIPT_shift_southeast_pixels_12',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_16_SUBSCRIPT_shift_southwest_steps_13',
                "command": 'shift_southwest_steps',
                "args": [10]
            },
        ]
    },
    {
        "identifier": 'EVENT_2295_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2295_action_queue_sync_17_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [100]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_17_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_17_SUBSCRIPT_sequence_looping_off_2',
                "command": 'sequence_looping_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2295_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2295_action_queue_sync_18_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [85]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_18_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_18_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_18_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_18_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_18_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [65]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_18_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_18_SUBSCRIPT_shift_southeast_steps_7',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_18_SUBSCRIPT_shift_southwest_steps_8',
                "command": 'shift_southwest_steps',
                "args": [7]
            },
        ]
    },
    {
        "identifier": 'EVENT_2295_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2295_action_queue_sync_19_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [85]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_19_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_19_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_19_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_19_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_19_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [65]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_19_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_19_SUBSCRIPT_shift_southeast_steps_7',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_19_SUBSCRIPT_shift_southwest_steps_8',
                "command": 'shift_southwest_steps',
                "args": [7]
            },
        ]
    },
    {
        "identifier": 'EVENT_2295_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2295_action_queue_sync_20_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [85]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_20_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_20_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_20_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_20_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_20_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [65]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_20_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_20_SUBSCRIPT_shift_northwest_steps_7',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_20_SUBSCRIPT_shift_southwest_steps_8',
                "command": 'shift_southwest_steps',
                "args": [7]
            },
        ]
    },
    {
        "identifier": 'EVENT_2295_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2295_action_queue_sync_21_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [85]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_21_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_21_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_21_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_21_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_21_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [65]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_21_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_21_SUBSCRIPT_shift_northwest_steps_7',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_21_SUBSCRIPT_shift_southwest_steps_8',
                "command": 'shift_southwest_steps',
                "args": [7]
            },
        ]
    },
    {
        "identifier": 'EVENT_2295_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2295_action_queue_sync_22_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_22_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [85]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_22_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_22_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_22_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [65]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_22_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_22_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_22_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_22_SUBSCRIPT_shift_southeast_steps_8',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_22_SUBSCRIPT_shift_southwest_steps_9',
                "command": 'shift_southwest_steps',
                "args": [7]
            },
        ]
    },
    {
        "identifier": 'EVENT_2295_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2295_action_queue_sync_23_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_23_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [85]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_23_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_23_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_23_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_23_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [65]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_23_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_23_SUBSCRIPT_visibility_on_7',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_23_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_23_SUBSCRIPT_shift_southeast_steps_9',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_23_SUBSCRIPT_shift_southwest_steps_10',
                "command": 'shift_southwest_steps',
                "args": [7]
            },
        ]
    },
    {
        "identifier": 'EVENT_2295_action_queue_sync_24',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2295_action_queue_sync_24_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [85]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_24_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_24_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_24_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_24_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_24_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [65]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_24_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_24_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_24_SUBSCRIPT_shift_northwest_steps_8',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_24_SUBSCRIPT_shift_southwest_steps_9',
                "command": 'shift_southwest_steps',
                "args": [7]
            },
        ]
    },
    {
        "identifier": 'EVENT_2295_action_queue_async_25',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2295_action_queue_async_25_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [85]
            },
            {
                "identifier": 'EVENT_2295_action_queue_async_25_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_async_25_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2295_action_queue_async_25_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_2295_action_queue_async_25_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2295_action_queue_async_25_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [65]
            },
            {
                "identifier": 'EVENT_2295_action_queue_async_25_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_2295_action_queue_async_25_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2295_action_queue_async_25_SUBSCRIPT_shift_northwest_steps_8',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2295_action_queue_async_25_SUBSCRIPT_shift_southwest_steps_9',
                "command": 'shift_southwest_steps',
                "args": [7]
            },
        ]
    },
    {
        "identifier": 'EVENT_2295_pause_26',
        "command": 'pause',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2295_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2295_action_queue_sync_27_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2295_action_queue_sync_27_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [45]
            },
        ]
    },
    {
        "identifier": 'EVENT_2295_star_mask_shrink_to_screen_center_28',
        "command": 'star_mask_shrink_to_screen_center',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2295_pause_29',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2295_jmp_to_event_30',
        "command": 'jmp_to_event',
        "args": [3802],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2295_ret_31',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
