from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2795_run_dialog_0',
        "command": 'run_dialog',
        "args": [3324, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2795_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7091, 7, 'EVENT_2795_ret_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2795_set_bit_2',
        "command": 'set_bit',
        "args": [0x7091, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2795_run_dialog_3',
        "command": 'run_dialog',
        "args": [3322, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2795_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
