from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1862_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7095, 1, 'EVENT_1862_run_dialog_3']
    },
    {
        "identifier": 'EVENT_1862_run_dialog_1',
        "command": 'run_dialog',
        "args": [1278, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1862_set_bit_2',
        "command": 'set_bit',
        "args": [0x7095, 1]
    },
    {
        "identifier": 'EVENT_1862_run_dialog_3',
        "command": 'run_dialog',
        "args": [1279, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1862_open_shop_4',
        "command": 'open_shop',
        "args": [Shops._22_CROCOS_SHOP_1]
    },
    {
        "identifier": 'EVENT_1862_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1862_ret_6',
        "command": 'ret'
    }
]
