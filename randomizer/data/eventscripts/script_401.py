from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_401_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 7, 'EVENT_401_remove_from_current_level_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_401_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7098, 7, 'EVENT_401_action_queue_async_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_401_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7099, 0, 'EVENT_401_remove_from_current_level_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_401_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_401_action_queue_async_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_401_action_queue_async_3_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_401_action_queue_async_3_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_401_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 7, 'EVENT_257_fade_in_from_black_async_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_401_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7086, 0, 'EVENT_401_summon_to_current_level_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_401_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_401_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_401_summon_to_current_level_8',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_401_fade_in_from_black_async_9',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_401_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_401_remove_from_current_level_11',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_401_fade_in_from_black_async_12',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_401_ret_13',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
