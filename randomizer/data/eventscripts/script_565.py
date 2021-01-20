from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_565_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'EVENT_565_run_dialog_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_565_jmp_to_subroutine_1',
        "command": 'jmp_to_subroutine',
        "args": [0x671c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_565_run_dialog_2',
        "command": 'run_dialog',
        "args": [865, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_565_jmp_to_subroutine_3',
        "command": 'jmp_to_subroutine',
        "args": [0x6723],
        "subscript": []
    },
    {
        "identifier": 'EVENT_565_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_565_run_dialog_5',
        "command": 'run_dialog',
        "args": [864, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_565_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
