
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
        "identifier": "EVENT_576_set_7000_to_70A0_short_mem_2",
        "command": "copy_var_to_var",
        "args": [0x70A7, 0x7000]
    },
    {
        "identifier": "EVENT_576_room_9_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 240, "EVENT_576_grant"]
    },
    {
        "identifier": "EVENT_576_DISABLE_CHEST_ROOM_1",
        "command": "disable_trigger_in_level",
        "args": [
            AreaObjects.NPC_0,
            Rooms._093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F,
        ],
    },
    {
        "identifier": "EVENT_576_DISABLE_CHEST_ROOM_2",
        "command": "disable_trigger_in_level",
        "args": [AreaObjects.NPC_0, Rooms._094_ROSE_TOWN_TREASURE_HOUSE_1F],
    },
    {"identifier": "EVENT_576_grant", "command": "jmp_to_event", "args": [172]},
]
