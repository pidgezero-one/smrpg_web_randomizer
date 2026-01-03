
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_46_set_var_to_random_1',
        "command": 'set_var_to_random',
        "args": [0x7000, 3]
    },
    {
        "identifier": "EVENT_46_jmp_if_7000_equals_short_0",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 0, "EVENT_46__2"]
    },
    {
        "identifier": "EVENT_46_jmp_if_7000_equals_short__0",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 1, "EVENT_46___2"]
    },
    {
        "identifier": "EVENT_46_2",
        "command": 'jmp_to_event',
        "args": [10]
    },
    {
        "identifier": "EVENT_46__2",
        "command": 'jmp_to_event',
        "args": [11]
    },
    {
        "identifier": "EVENT_46___2",
        "command": 'jmp_to_event',
        "args": [12]
    }
]
