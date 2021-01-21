from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1910_freeze_all_npcs_until_return_0',
        "command": 'freeze_all_npcs_until_return'
    },
    {
        "identifier": 'EVENT_1910_jmp_if_random_above_128_1',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_1910_set_short_4']
    },
    {
        "identifier": 'EVENT_1910_set_short_2',
        "command": 'set_short',
        "args": [0x700e, 0x007a]
    },
    {
        "identifier": 'EVENT_1910_jmp_3',
        "command": 'jmp',
        "args": ['EVENT_1909_start_battle_700E_5']
    },
    {
        "identifier": 'EVENT_1910_set_short_4',
        "command": 'set_short',
        "args": [0x700e, 0x007b]
    },
    {
        "identifier": 'EVENT_1910_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_1909_start_battle_700E_5']
    }
]
