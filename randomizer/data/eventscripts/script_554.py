from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_554_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7085, 5, 'EVENT_554_jmp_if_bit_clear_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_554_set_bit_1',
        "command": 'set_bit',
        "args": [0x7085, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_554_run_dialog_2',
        "command": 'run_dialog',
        "args": [813, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_554_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_554_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7085, 0, 'EVENT_554_run_dialog_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_554_run_dialog_5',
        "command": 'run_dialog',
        "args": [820, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_554_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
