from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_997_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._429_GAME_INTRO_NIMBUS_LAND_OUTSIDE_WITH_PATROLLING_BIRDIES, RadialDirections.NORTHEAST, 12, 56, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_997_freeze_camera_1',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_997_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_997_action_queue_async_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_997_action_queue_async_2_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_997_action_queue_async_2_SUBSCRIPT_shift_north_steps_2',
                "command": 'shift_north_steps',
                "args": [1]
            },
        ]
    },
    {
        "identifier": 'EVENT_997_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_997_action_queue_sync_3_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_3_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_3_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [140]
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_3_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_3_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_3_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [90]
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_3_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_3_SUBSCRIPT_jump_to_height_silent_7',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_3_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_3_SUBSCRIPT_shift_north_steps_9',
                "command": 'shift_north_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_3_SUBSCRIPT_shift_northeast_steps_10',
                "command": 'shift_northeast_steps',
                "args": [12]
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_3_SUBSCRIPT_visibility_off_11',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_997_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_997_action_queue_sync_4_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_4_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [20]
            },
        ]
    },
    {
        "identifier": 'EVENT_997_fade_in_from_black_sync_duration_5',
        "command": 'fade_in_from_black_sync_duration',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_997_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_997_action_queue_sync_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_6_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_6_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [5]
            },
        ]
    },
    {
        "identifier": 'EVENT_997_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_997_action_queue_sync_7_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_7_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_7_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [9]
            },
        ]
    },
    {
        "identifier": 'EVENT_997_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_997_action_queue_sync_8_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_8_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_8_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_997_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_997_action_queue_sync_9_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [150]
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_9_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_9_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_9_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_9_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_9_SUBSCRIPT_walk_1_step_northwest_5',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_9_SUBSCRIPT_fixed_f_coord_off_6',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_9_SUBSCRIPT_face_southwest_7',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_997_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_997_action_queue_sync_10_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [150]
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_10_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_10_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_10_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_10_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_10_SUBSCRIPT_walk_1_step_southeast_5',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_10_SUBSCRIPT_fixed_f_coord_off_6',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_997_action_queue_sync_10_SUBSCRIPT_face_southwest_7',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_997_pause_short_11',
        "command": 'pause_short',
        "args": [270],
        "subscript": []
    },
    {
        "identifier": 'EVENT_997_fade_out_to_black_sync_duration_12',
        "command": 'fade_out_to_black_sync_duration',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_997_pause_script_until_effect_done_13',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_997_jmp_to_event_14',
        "command": 'jmp_to_event',
        "args": [146],
        "subscript": []
    },
]
