from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1076_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7052, 0, 'EVENT_1076_ret_5']
    },
    {
        "identifier": 'EVENT_1076_run_dialog_1',
        "command": 'run_dialog',
        "args": [2722, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1076_set_bit_2',
        "command": 'set_bit',
        "args": [0x7052, 0]
    },
    {
        "identifier": 'EVENT_1076_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7051, 1, 'EVENT_1076_ret_5']
    },
    {
        "identifier": 'EVENT_1076_run_dialog_4',
        "command": 'run_dialog',
        "args": [2733, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1076_ret_5',
        "command": 'ret'
    }
]
