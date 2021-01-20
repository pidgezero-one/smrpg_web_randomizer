from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1392_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1392_action_queue_sync_0_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1392_action_queue_sync_0_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_1392_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1392_action_queue_async_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1392_action_queue_async_1_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_1392_palette_set_2',
        "command": 'palette_set',
        "args": [33, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1392_play_music_default_volume_3',
        "command": 'play_music_default_volume',
        "args": [Music._14_MARIOS_PAD],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1392_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7053, 2, 'EVENT_1392_fade_in_from_black_async_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1392_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7053, 1, 'EVENT_1392_action_queue_async_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1392_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1392_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1392_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1392_action_queue_async_8_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [2, 11]
            },
            {
                "identifier": 'EVENT_1392_action_queue_async_8_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1392_action_queue_async_8_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1392_action_queue_async_8_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1392_action_queue_async_8_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1392_action_queue_async_8_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1392_action_queue_async_8_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1392_action_queue_async_8_SUBSCRIPT_sequence_looping_on_7',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1392_fade_in_from_black_async_9',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1392_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
