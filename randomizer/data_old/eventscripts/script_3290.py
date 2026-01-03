
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
        "identifier": "EVENT_3290_jmp_if_bit_set_0",
        "command": "jmp_if_bit_set",
        "args": [0x707D, 2, "EVENT_3290_ret_10"],
    },
    {"identifier": "EVENT_3290_set_bit_1", "command": "set_bit", "args": [0x707D, 2]},
    {
        "identifier": "EVENT_3290_stop_all_background_events_4",
        "command": "stop_all_background_events",
    },
    {
        "identifier": "EVENT_3290_grant",
        "command": "run_event_as_subroutine",
        "args": [241],
    },
    {"identifier": "EVENT_3290_pause", "command": "pause", "args": [120]},
    {
        "identifier": "EVENT_3290_run_background_event_8",
        "command": "run_background_event",
        "args": [3212, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
    },
    {
        "identifier": "EVENT_3290_run_dialog_9",
        "command": "run_dialog",
        "args": [1657, AreaObjects.BOWSER, []],
    },
    {"identifier": "EVENT_3290_ret_10", "command": "ret"},
]
