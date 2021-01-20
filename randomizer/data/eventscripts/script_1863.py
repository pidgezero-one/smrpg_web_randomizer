from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1863_run_dialog_0',
        "command": 'run_dialog',
        "args": [1280, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1863_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7095, 2, 'EVENT_1863_open_shop_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1863_run_dialog_2',
        "command": 'run_dialog',
        "args": [1282, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1863_set_bit_3',
        "command": 'set_bit',
        "args": [0x7095, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1863_open_shop_4',
        "command": 'open_shop',
        "args": [Shops._23_CROCOS_SHOP_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1863_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1863_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
