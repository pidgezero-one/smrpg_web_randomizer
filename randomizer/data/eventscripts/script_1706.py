from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1706_pause_0',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7076, 0, 'EVENT_1706_pause_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_ret_2',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_pause_3',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7076, 0, 'EVENT_1706_pause_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_set_5',
        "command": 'set',
        "args": [0x70ab, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_start_loop_n_times_6',
        "command": 'start_loop_n_times',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_jmp_if_present_in_current_level_7',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.MEM_70AB, 'EVENT_1706_pause_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_1706_add_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_pause_9',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_summon_to_level_10',
        "command": 'summon_to_level',
        "args": [AreaObjects.MEM_70AB, Rooms._078_BANDITS_WAY_AREA_04],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_set_action_script_sync_11',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70AB, 471],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_add_12',
        "command": 'add',
        "args": [0x70ab, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_end_loop_13',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_pause_14',
        "command": 'pause',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_1706_pause_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_pause_16',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_set_17',
        "command": 'set',
        "args": [0x70ab, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_start_loop_n_times_18',
        "command": 'start_loop_n_times',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_jmp_if_object_not_in_level_19',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.MEM_70AB, Rooms._078_BANDITS_WAY_AREA_04, 'EVENT_1706_add_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_pause_action_script_20',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70AB],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_reset_coords_21',
        "command": 'reset_coords',
        "args": [AreaObjects.MEM_70AB],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_set_action_script_sync_22',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70AB, 474],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_add_23',
        "command": 'add',
        "args": [0x70ab, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_end_loop_24',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1706_ret_25',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
