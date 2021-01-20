from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_341_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 5, 'EVENT_341_summon_to_current_level_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_341_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_257_fade_in_from_black_async_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_341_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 0, 'EVENT_257_fade_in_from_black_async_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_341_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7083, 5, 'EVENT_341_jmp_if_bit_clear_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_341_set_bit_4',
        "command": 'set_bit',
        "args": [0x7083, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_341_run_background_event_5',
        "command": 'run_background_event',
        "args": [342, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_341_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_341_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_341_jmp_if_bit_clear_8',
        "command": 'jmp_if_bit_clear',
        "args": [0x7081, 5, 'EVENT_341_jmp_if_bit_set_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_341_summon_to_current_level_9',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_341_summon_to_current_level_10',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_341_fade_in_from_black_async_11',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_341_ret_12',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_341_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 6, 'EVENT_341_summon_to_current_level_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_341_jmp_14',
        "command": 'jmp',
        "args": ['EVENT_257_fade_in_from_black_async_0'],
        "subscript": []
    },
]
