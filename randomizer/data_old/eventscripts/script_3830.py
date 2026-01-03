
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3830_jmp_if_bit_set_355__',
        "command": 'jmp_if_bit_set',
        "args": [0x7082, 0, 'EVENT_3830_run_dialog_14']
    },
    {
        "identifier": 'EVENT_3830_run_dialog_14_',
        "command": 'run_dialog',
        "args": [3747, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3830_ret_15_',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3830_run_dialog_14',
        "command": 'run_dialog',
        "args": [3746, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3830_ret_15',
        "command": 'ret'
    }
]
