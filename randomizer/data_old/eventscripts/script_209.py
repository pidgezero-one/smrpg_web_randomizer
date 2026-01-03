
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
        "identifier": "EVENT_209_set_7000_to_party_capacity_4",
        "command": "set_7000_to_party_capacity",
    },
    {
        "identifier": "EVENT_209_mem_compare_val_5",
        "command": "compare_var_to_const",
        "args": [0x7000, 4],
    },
    {
        "identifier": "EVENT_209_jmp_if_comparison_result_is_lesser_6",
        "command": "jmp_if_comparison_result_is_greater_or_equal",
        "args": ["EVENT_209_set_switch_menu"],
    },
    {"identifier": "EVENT_209_ret_16", "command": "ret"},
    {
        "identifier": "EVENT_209_set_switch_menu",
        "command": "set_bit",
        "args": [0x7062, 2],
    },
    {"identifier": "EVENT_209_ret_16_", "command": "ret"},
]
