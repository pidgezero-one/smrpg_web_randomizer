
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
        "identifier": "EVENT_3610_npc_",
        "command": "jmp_if_var_equals_const",
        "args": [0x70A8, 0x1D, "EVENT_3610_chest_2"],
    },
    {
        "identifier": "EVENT_3610_npc__",
        "command": "jmp_if_var_equals_const",
        "args": [0x70A8, 0x1E, "EVENT_3610_chest_3"],
    },
    {
        "identifier": "EVENT_3610_npc___",
        "command": "jmp_if_var_equals_const",
        "args": [0x70A8, 0x1F, "EVENT_3610_chest_4"],
    },
    {
        "identifier": "EVENT_3610_chest_1",
        "command": "jmp_to_event",
        "args": [1842],
    },
    {
        "identifier": "EVENT_3610_chest_2",
        "command": "jmp_to_event",
        "args": [1881],
    },
    {
        "identifier": "EVENT_3610_chest_3",
        "command": "jmp_to_event",
        "args": [1882],
    },
    {
        "identifier": "EVENT_3610_chest_4",
        "command": "jmp_to_event",
        "args": [1929],
    },
]
