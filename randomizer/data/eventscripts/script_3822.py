from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3822_set_0',
        "command": 'set',
        "args": [0x70a7, 163]
    },
    {
        "identifier": 'EVENT_3822_set_short_1',
        "command": 'set_short',
        "args": [0x7000, 0x020c]
    },
    {
        "identifier": 'EVENT_3822_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_3822_remove_from_level_3',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_12, Rooms._084_ROSE_TOWN_OUTSIDE]
    },
    {
        "identifier": 'EVENT_3822_remove_from_level_4',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE]
    },
    {
        "identifier": 'EVENT_3822_remove_from_current_level_5',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_3822_remove_from_current_level_6',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_12]
    },
    {
        "identifier": 'EVENT_3822_ret_7',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3822_ret_8',
        "command": 'ret'
    }
]
