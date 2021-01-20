from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1766_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x704f, 0, 'EVENT_1766_action_queue_async_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1766_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1766_action_queue_async_1_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [20, 23, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1766_action_queue_async_1_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1766_action_queue_async_1_SUBSCRIPT_shift_east_pixels_2',
                "command": 'shift_east_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_1766_action_queue_async_1_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1766_fade_in_from_black_async_2',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1766_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1766_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1766_action_queue_async_4_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [20, 55, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1766_action_queue_async_4_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1766_action_queue_async_4_SUBSCRIPT_shift_east_pixels_2',
                "command": 'shift_east_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_1766_action_queue_async_4_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1766_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1766_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
