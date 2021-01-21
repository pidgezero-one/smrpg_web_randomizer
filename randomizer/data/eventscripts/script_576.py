from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_576_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7061, 0, 'EVENT_576_set_6']
    },
    {
        "identifier": 'EVENT_576_jmp_if_object_in_level_1',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_4, Rooms._093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F, 'EVENT_576_set_6']
    },
    {
        "identifier": 'EVENT_576_set_2',
        "command": 'set',
        "args": [0x70a7, 32]
    },
    {
        "identifier": 'EVENT_576_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [32]
    },
    {
        "identifier": 'EVENT_576_disable_trigger_in_level_4',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_0, Rooms._094_ROSE_TOWN_TREASURE_HOUSE_1F]
    },
    {
        "identifier": 'EVENT_576_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_576_set_6',
        "command": 'set',
        "args": [0x70a7, 133]
    },
    {
        "identifier": 'EVENT_576_run_event_as_subroutine_7',
        "command": 'run_event_as_subroutine',
        "args": [34]
    },
    {
        "identifier": 'EVENT_576_disable_trigger_in_level_8',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_0, Rooms._094_ROSE_TOWN_TREASURE_HOUSE_1F]
    },
    {
        "identifier": 'EVENT_576_ret_9',
        "command": 'ret'
    }
]
