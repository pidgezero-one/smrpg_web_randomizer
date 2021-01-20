from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1132_run_dialog_0',
        "command": 'run_dialog',
        "args": [2832, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1132_jmp_if_dialog_option_b_1',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1132_run_dialog_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1132_run_dialog_2',
        "command": 'run_dialog',
        "args": [2833, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1132_set_bit_3',
        "command": 'set_bit',
        "args": [0x7062, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1132_jmp_4',
        "command": 'jmp',
        "args": ['EVENT_273_fade_out_music_to_volume_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1132_run_dialog_5',
        "command": 'run_dialog',
        "args": [2833, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1132_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
