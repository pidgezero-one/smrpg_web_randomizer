from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_525_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7083, 6, 'EVENT_525_run_dialog_5']
    },
    {
        "identifier": 'EVENT_525_run_dialog_1',
        "command": 'run_dialog',
        "args": [810, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_525_open_shop_2',
        "command": 'open_shop',
        "args": [Shops._01_ROSE_TOWN_ITEMS]
    },
    {
        "identifier": 'EVENT_525_fade_in_from_black_async_3',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_525_ret_4',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_525_run_dialog_5',
        "command": 'run_dialog',
        "args": [868, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_525_open_shop_6',
        "command": 'open_shop',
        "args": [Shops._01_ROSE_TOWN_ITEMS]
    },
    {
        "identifier": 'EVENT_525_fade_in_from_black_async_7',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_525_ret_8',
        "command": 'ret'
    }
]
