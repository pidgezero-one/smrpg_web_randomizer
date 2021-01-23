from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2310_inc_0',
        "command": 'inc',
        "args": [0x70c8]
    },
    {
        "identifier": 'EVENT_2310_set_bit_1',
        "command": 'set_bit',
        "args": [0x7091, 5]
    },
    {
        "identifier": 'EVENT_2310_remove_from_level_2',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_8, Rooms._199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT]
    },
    {
        "identifier": 'EVENT_2310_summon_to_level_3',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_9, Rooms._199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT]
    },
    {
        "identifier": 'EVENT_2310_jmp_to_event_4',
        "command": 'jmp_to_event',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2310_ret_5',
        "command": 'ret'
    }
]
