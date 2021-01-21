from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1347_remove_from_current_level_0',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_1347_remove_from_level_1',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM]
    },
    {
        "identifier": 'EVENT_1347_set_2',
        "command": 'set',
        "args": [0x70a7, 115]
    },
    {
        "identifier": 'EVENT_1347_set_3',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_1347_jmp_to_event_4',
        "command": 'jmp_to_event',
        "args": [3828]
    }
]
