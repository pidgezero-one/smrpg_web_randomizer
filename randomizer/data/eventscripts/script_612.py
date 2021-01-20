from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_612_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x709f, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_612_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 3, 'EVENT_612_clear_bit_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_612_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 0, 'EVENT_612_jmp_if_bit_set_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_612_fade_in_from_black_async_3',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_612_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_612_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 1, 'EVENT_257_fade_in_from_black_async_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_612_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 4, 'EVENT_257_fade_in_from_black_async_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_612_set_bit_7',
        "command": 'set_bit',
        "args": [0x7042, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_612_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_612_action_queue_async_8_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [14, 46, 4, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_612_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 300],
        "subscript": []
    },
    {
        "identifier": 'EVENT_612_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_612_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_612_clear_bit_12',
        "command": 'clear_bit',
        "args": [0x704c, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_612_jmp_13',
        "command": 'jmp',
        "args": ['EVENT_612_jmp_if_bit_set_2'],
        "subscript": []
    }
]
