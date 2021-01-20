from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_577_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7061, 0, 'EVENT_577_set_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_577_jmp_if_object_in_level_1',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_4, Rooms._093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F, 'EVENT_577_set_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_577_set_2',
        "command": 'set',
        "args": [0x70a7, 32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_577_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_577_disable_trigger_in_level_4',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_1, Rooms._094_ROSE_TOWN_TREASURE_HOUSE_1F],
        "subscript": []
    },
    {
        "identifier": 'EVENT_577_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_577_set_6',
        "command": 'set',
        "args": [0x70a7, 136],
        "subscript": []
    },
    {
        "identifier": 'EVENT_577_run_event_as_subroutine_7',
        "command": 'run_event_as_subroutine',
        "args": [34],
        "subscript": []
    },
    {
        "identifier": 'EVENT_577_disable_trigger_in_level_8',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_1, Rooms._094_ROSE_TOWN_TREASURE_HOUSE_1F],
        "subscript": []
    },
    {
        "identifier": 'EVENT_577_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
