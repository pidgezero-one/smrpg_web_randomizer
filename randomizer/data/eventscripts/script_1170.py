from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1170_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7086, 7, 'EVENT_1170_run_dialog_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1170_run_dialog_1',
        "command": 'run_dialog',
        "args": [2900, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1170_open_shop_2',
        "command": 'open_shop',
        "args": [Shops._16_SEASIDE_HEALTH_FOODS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1170_set_bit_3',
        "command": 'set_bit',
        "args": [0x7086, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1170_fade_in_from_black_async_4',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1170_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1170_run_dialog_6',
        "command": 'run_dialog',
        "args": [2901, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1170_open_shop_7',
        "command": 'open_shop',
        "args": [Shops._16_SEASIDE_HEALTH_FOODS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1170_fade_in_from_black_async_8',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1170_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]