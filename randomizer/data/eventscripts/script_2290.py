from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2290_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._250_GAME_INTRO_BOOSTER_TOWER_BALCONY_WITH_TOADSTOOL_CRYING, RadialDirections.NORTHEAST, 4, 17, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2290_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2290_action_queue_sync_1_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2290_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2290_action_queue_sync_2_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2290_action_queue_sync_2_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2290_action_queue_sync_2_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2290_action_queue_sync_2_SUBSCRIPT_shift_west_pixels_3',
                "command": 'shift_west_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2290_action_queue_sync_2_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2290_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2290_action_queue_sync_3_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2290_action_queue_sync_3_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2290_action_queue_sync_3_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2290_action_queue_sync_3_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2290_action_queue_sync_3_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2290_action_queue_sync_3_SUBSCRIPT_sequence_looping_on_5',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2290_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2290_action_queue_async_4_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 16, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2290_action_queue_async_4_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2290_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2290_action_queue_async_4_SUBSCRIPT_set_priority_3',
                "command": 'set_priority',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_2290_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2290_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2290_action_queue_async_6_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_2290_action_queue_async_6_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2290_action_queue_async_6_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2290_action_queue_async_6_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2290_action_queue_async_6_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2290_action_queue_async_6_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2290_action_queue_async_6_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2290_action_queue_async_6_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2290_action_queue_async_6_SUBSCRIPT_shift_southwest_pixels_8',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2290_action_queue_async_6_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_2290_action_queue_async_6_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2290_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2290_action_queue_async_6_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [50]
            },
        ]
    },
    {
        "identifier": 'EVENT_2290_circle_mask_nonstatic_7',
        "command": 'circle_mask_nonstatic',
        "args": [AreaObjects.NPC_0, 30, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2290_pause_8',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2290_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2290_action_queue_async_9_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [22, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2290_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2290_action_queue_async_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2290_action_queue_async_10_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_2290_display_intro_title_11',
        "command": 'display_intro_title',
        "args": [17, IntroTitles.PRINCESS_TOADSTOOL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2290_pause_12',
        "command": 'pause',
        "args": [150],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2290_fade_out_to_black_async_duration_13',
        "command": 'fade_out_to_black_async_duration',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2290_jmp_to_event_14',
        "command": 'jmp_to_event',
        "args": [141],
        "subscript": []
    },
]
