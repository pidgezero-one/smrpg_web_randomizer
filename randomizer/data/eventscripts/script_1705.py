from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1705_pause_0',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1705_jmp_if_mario_in_air_1',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1705_clear_bit_3']
    },
    {
        "identifier": 'EVENT_1705_jmp_2',
        "command": 'jmp',
        "args": ['EVENT_1705_pause_0']
    },
    {
        "identifier": 'EVENT_1705_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_1705_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_1705_pause_13']
    },
    {
        "identifier": 'EVENT_1705_set_bit_5',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1705_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_1705_set_7',
        "command": 'set',
        "args": [0x70ab, 20]
    },
    {
        "identifier": 'EVENT_1705_start_loop_n_times_8',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1705_jmp_if_present_in_current_level_9',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.MEM_70AB, 'EVENT_1705_add_11']
    },
    {
        "identifier": 'EVENT_1705_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70AB, 474]
    },
    {
        "identifier": 'EVENT_1705_add_11',
        "command": 'add',
        "args": [0x70ab, 0x01]
    },
    {
        "identifier": 'EVENT_1705_end_loop_12',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1705_pause_13',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1705_jmp_if_mario_in_air_14',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1705_pause_13']
    },
    {
        "identifier": 'EVENT_1705_set_7000_to_object_coord_15',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_1705_jmp_if_var_not_equals_short_16',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 0, 'EVENT_1705_pause_0']
    },
    {
        "identifier": 'EVENT_1705_jmp_if_bit_set_17',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_1705_pause_0']
    },
    {
        "identifier": 'EVENT_1705_set_bit_18',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_1705_clear_bit_19',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1705_set_20',
        "command": 'set',
        "args": [0x70ab, 20]
    },
    {
        "identifier": 'EVENT_1705_start_loop_n_times_21',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1705_jmp_if_present_in_current_level_22',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.MEM_70AB, 'EVENT_1705_add_24']
    },
    {
        "identifier": 'EVENT_1705_set_action_script_sync_23',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70AB, 475]
    },
    {
        "identifier": 'EVENT_1705_add_24',
        "command": 'add',
        "args": [0x70ab, 0x01]
    },
    {
        "identifier": 'EVENT_1705_end_loop_25',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1705_jmp_26',
        "command": 'jmp',
        "args": ['EVENT_1705_pause_0']
    }
]
