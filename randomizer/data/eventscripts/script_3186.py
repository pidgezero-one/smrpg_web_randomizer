from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3186_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7058, 3, 'EVENT_3186_jmp_if_bit_set_3']
    },
    {
        "identifier": 'EVENT_3186_run_dialog_1',
        "command": 'run_dialog',
        "args": [1631, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3186_ret_2',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3186_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 5, 'EVENT_3186_run_dialog_1']
    },
    {
        "identifier": 'EVENT_3186_run_dialog_4',
        "command": 'run_dialog',
        "args": [1653, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3186_ret_5',
        "command": 'ret'
    }
]
