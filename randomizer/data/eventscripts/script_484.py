from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_484_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'EVENT_484_run_event_as_subroutine_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_484_run_dialog_1',
        "command": 'run_dialog',
        "args": [2378, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_484_ret_2',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_484_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [456],
        "subscript": []
    },
    {
        "identifier": 'EVENT_484_run_dialog_4',
        "command": 'run_dialog',
        "args": [2378, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_484_run_background_event_5',
        "command": 'run_background_event',
        "args": [469, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_484_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
