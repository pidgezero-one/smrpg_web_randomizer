
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
        "identifier": "EVENT_3207_check_star",
        "command": "run_event_as_subroutine",
        "args": [1603],
    },
    {
        "identifier": "EVENT_3207_jmp_if_bit_set_129_",
        "command": "clear_bit",
        "args": [0x707E, 2],
    },
    {
        "identifier": "EVENT_3207_run_event_as_subroutine_0",
        "command": "run_event_as_subroutine",
        "args": [65],
    },
    {
        "identifier": "EVENT_3207_open_location_5",
        "command": "open_location",
        "args": [Locations._034_SUNKEN_SHIP, [6, 7]],
    },
    {"identifier": "EVENT_3207_ret_6", "command": "ret"},
]
