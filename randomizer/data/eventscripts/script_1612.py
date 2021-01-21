from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1612_remove_from_current_level_0',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_1612_remove_from_current_level_1',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_1612_remove_from_current_level_2',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_1612_remove_from_current_level_3',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_1612_remove_from_current_level_4',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_1612_remove_from_current_level_5',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_1612_remove_from_current_level_6',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_11]
    },
    {
        "identifier": 'EVENT_1612_remove_from_current_level_7',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_12]
    },
    {
        "identifier": 'EVENT_1612_pause_8',
        "command": 'pause',
        "args": [21]
    },
    {
        "identifier": 'EVENT_1612_set_9',
        "command": 'set',
        "args": [0x70ab, 25]
    },
    {
        "identifier": 'EVENT_1612_start_loop_n_times_10',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1612_jmp_if_object_not_in_level_11',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.MEM_70AB, Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL, 'EVENT_1612_add_13']
    },
    {
        "identifier": 'EVENT_1612_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70AB, 126]
    },
    {
        "identifier": 'EVENT_1612_add_13',
        "command": 'add',
        "args": [0x70ab, 0x01]
    },
    {
        "identifier": 'EVENT_1612_end_loop_14',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1612_pause_15',
        "command": 'pause',
        "args": [238]
    },
    {
        "identifier": 'EVENT_1612_set_16',
        "command": 'set',
        "args": [0x70ab, 29]
    },
    {
        "identifier": 'EVENT_1612_start_loop_n_times_17',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1612_jmp_if_object_not_in_level_18',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.MEM_70AB, Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL, 'EVENT_1612_add_20']
    },
    {
        "identifier": 'EVENT_1612_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70AB, 126]
    },
    {
        "identifier": 'EVENT_1612_add_20',
        "command": 'add',
        "args": [0x70ab, 0x01]
    },
    {
        "identifier": 'EVENT_1612_end_loop_21',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1612_ret_22',
        "command": 'ret'
    }
]
