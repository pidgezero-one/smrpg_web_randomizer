from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_575_run_event_as_subroutine_0',
        "command": 'run_event_as_subroutine',
        "args": [281],
        "subscript": []
    },
    {
        "identifier": 'EVENT_575_jmp_if_object_in_level_1',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_4, Rooms._093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F, 'EVENT_575_summon_to_level_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_575_jmp_to_event_2',
        "command": 'jmp_to_event',
        "args": [261],
        "subscript": []
    },
    {
        "identifier": 'EVENT_575_summon_to_level_3',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._094_ROSE_TOWN_TREASURE_HOUSE_1F],
        "subscript": []
    },
    {
        "identifier": 'EVENT_575_summon_to_current_level_4',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_575_jmp_to_event_5',
        "command": 'jmp_to_event',
        "args": [261],
        "subscript": []
    }
]
