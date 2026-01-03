
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_59_store_multiplier',
        "command": 'copy_var_to_var',
        'args': [0x7088, 0x7000]
    },
    {
        "identifier": 'EVENT_59_mem_7000_and_const_6',
        "command": 'mem_7000_and_const',
        "args": [0x0018]
    },
    {
        "identifier": "EVENT_59_tier4_jmp",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 0, "EVENT_59_tier4"]
    },
    {
        "identifier": "EVENT_59_tier3_jmp",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 8, "EVENT_59_tier3"]
    },
    {
        "identifier": "EVENT_59_tier2_jmp",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 16, "EVENT_59_tier2"]
    },
    {
        "identifier": "EVENT_59_tier1",
        "command": 'jmp_to_event',
        "args": [26]
    },
    {
        "identifier": "EVENT_59_tier2",
        "command": 'jmp_to_event',
        "args": [44]
    },
    {
        "identifier": "EVENT_59_tier3",
        "command": 'jmp_to_event',
        "args": [39]
    },
    {
        "identifier": "EVENT_59_tier4",
        "command": 'jmp_to_event',
        "args": [38]
    }
]
