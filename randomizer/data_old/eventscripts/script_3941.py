
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
        "identifier": "EVENT_3941_run_dialog_5",
        "command": "run_dialog",
        "args": [2097, AreaObjects.BOWSER, [_0x60Flags.ASYNC]],
    },
    {"identifier": "EVENT_3941_inc_7", "command": "inc", "args": [0x70B2]},
    {
        "identifier": "EVENT_3941_put_inventory_22",
        "command": "put_inventory",
        "args": [232],
    },
    {"identifier": "EVENT_3941_ret", "command": "ret"},
]
