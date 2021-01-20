from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1833_pause_0',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1833_jmp_if_mario_in_air_1',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1833_freeze_all_npcs_until_return_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1833_jmp_2',
        "command": 'jmp',
        "args": ['EVENT_1833_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1833_freeze_all_npcs_until_return_3',
        "command": 'freeze_all_npcs_until_return',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1833_pause_4',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1833_jmp_if_mario_in_air_5',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1833_freeze_all_npcs_until_return_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1833_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x704d, 1, 'EVENT_1833_freeze_all_npcs_until_return_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1833_unfreeze_all_npcs_7',
        "command": 'unfreeze_all_npcs',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1833_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_1833_pause_0'],
        "subscript": []
    }
]
