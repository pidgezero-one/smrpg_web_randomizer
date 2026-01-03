
from randomizer.helpers.eventtables import (
    ControllerDirections,
    RadialDirections,
    Rooms,
    Sounds,
    AreaObjects,
    NPCPackets,
    Locations,
    Shops,
    EventSequences,
    MenuTutorials,
    OverworldSequences,
    PlayableCharacters,
    EquipSlots,
    DialogDurations,
    IntroTitles,
    Colours,
    PaletteSetTypes,
    Music,
    MusicDirections,
    MusicPitch,
    Coords,
    CoordUnits,
    Tutorials,
    _0x40Flags,
    _0x60Flags,
    _0x62Flags,
    _0x63Flags,
    _0x68Flags,
    _0x6AFlags,
    _0x6BFlags,
    _0x81Flags,
    _0x84Flags)
from randomizer.helpers.objectsequencetables import (
    SequenceSpeeds,
    VramPriority,
    _0x08Flags,
    _0x0AFlags,
    _0x10Flags)
from randomizer.data import items

script = [
    {
        "identifier": "EVENT_359_npc",
        "command": "jmp_if_var_equals_const",
        "args": [0x70A8, 0x16, "EVENT_359_chest_2"],
    },
    {
        "identifier": "EVENT_359_npc2",
        "command": "jmp_if_var_equals_const",
        "args": [0x70A8, 0x17, "EVENT_359_chest_3"],
    },
    {
        "identifier": "EVENT_359_npc3",
        "command": "jmp_if_var_equals_const",
        "args": [0x70A8, 0x18, "EVENT_359_chest_4"],
    },
    {
        "identifier": "EVENT_359_npc4",
        "command": "jmp_if_var_equals_const",
        "args": [0x70A8, 0x19, "EVENT_359_chest_5"],
    },
    {
        "identifier": "EVENT_359_chest_1",
        "command": "jmp_to_event",
        "args": [172],
    },
    {
        "identifier": "EVENT_359_chest_2",
        "command": "jmp_to_event",
        "args": [173],
    },
    {
        "identifier": "EVENT_359_chest_3",
        "command": "jmp_to_event",
        "args": [174],
    },
    {
        "identifier": "EVENT_359_chest_4",
        "command": "jmp_to_event",
        "args": [175],
    },
    {
        "identifier": "EVENT_359_chest_5",
        "command": "jmp_to_event",
        "args": [176],
    },
]
