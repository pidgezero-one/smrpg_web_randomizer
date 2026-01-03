
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
        "identifier": "EVENT_1800_run_dialog_duration_5",
        "command": "run_dialog_duration",
        "args": [1233, DialogDurations.SHORT, [_0x60Flags.ASYNC]],
    },
    {
        "identifier": "EVENT_1800_jmp_if_bit_set_2",
        "command": "jmp_if_bit_set",
        "args": [0x7067, 7, "EVENT_1800_ret_7"],
    },
    {
        "identifier": "EVENT_1800_run_dialog_duration_5_",
        "command": "run_dialog_duration",
        "args": [1166, DialogDurations.SHORT, [_0x60Flags.ASYNC]],
    },
    {"identifier": "EVENT_1800_ret_7", "command": "ret"},
]
