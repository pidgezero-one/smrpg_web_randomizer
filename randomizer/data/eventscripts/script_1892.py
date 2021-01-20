from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1892_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7096, 2, 'EVENT_1892_fade_in_from_black_async_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1892_set_bit_1',
        "command": 'set_bit',
        "args": [0x7049, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1892_enable_controls_2',
        "command": 'enable_controls',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1892_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1892_action_queue_async_3_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [14, 9, 18, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1892_action_queue_async_3_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
        ]
    },
    {
        "identifier": 'EVENT_1892_fade_in_from_black_sync_4',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1892_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1892_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1892_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7096, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1892_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
