
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2122_remove_from_level_0',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_9, Rooms._159_STAR_HILL_AREA_04]
    },
    {
        "identifier": 'EVENT_2122_remove_from_current_level_1',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_2122_jmp_to_event_3',
        "command": 'jmp_to_event',
        "args": [168]
    }
]
