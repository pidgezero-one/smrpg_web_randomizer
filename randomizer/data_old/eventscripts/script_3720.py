
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3720_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 7, 'EVENT_3720_run_dialog_10']
    },
    {
        "identifier": 'EVENT_3720_set_bit_1',
        "command": 'set_bit',
        "args": [0x705f, 7]
    },
    {
        "identifier": 'EVENT_3720_run_event_as_subroutine_8',
        "command": 'run_event_as_subroutine',
        "args": [178]
    },
    {
        "identifier": 'EVENT_3720_ret_9',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3720_run_dialog_10',
        "command": 'run_dialog',
        "args": [3667, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3720_ret_11',
        "command": 'ret'
    }
]
