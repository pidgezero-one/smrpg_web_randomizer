from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3287_set_0',
        "command": 'set',
        "args": [0x7000, 1694]
    },
    {
        "identifier": 'EVENT_3287_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7058, 7, 'EVENT_3287_run_dialog_3']
    },
    {
        "identifier": 'EVENT_3287_inc_2',
        "command": 'inc',
        "args": [0x7000]
    },
    {
        "identifier": 'EVENT_3287_run_dialog_3',
        "command": 'run_dialog',
        "args": [0x7000, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3287_ret_4',
        "command": 'ret'
    }
]
