from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3511_set_0',
        "command": 'set',
        "args": [0x70ae, 3]
    },
    {
        "identifier": 'EVENT_3511_start_loop_n_times_1',
        "command": 'start_loop_n_times',
        "args": [6]
    },
    {
        "identifier": 'EVENT_3511_jmp_if_random_above_66_2',
        "command": 'jmp_if_random_above_66',
        "args": ['EVENT_3511_set_action_script_sync_5']
    },
    {
        "identifier": 'EVENT_3511_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 708]
    },
    {
        "identifier": 'EVENT_3511_jmp_4',
        "command": 'jmp',
        "args": ['EVENT_3511_pause_8']
    },
    {
        "identifier": 'EVENT_3511_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 709]
    },
    {
        "identifier": 'EVENT_3511_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_3511_pause_8']
    },
    {
        "identifier": 'EVENT_3511_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 710]
    },
    {
        "identifier": 'EVENT_3511_pause_8',
        "command": 'pause',
        "args": [210]
    },
    {
        "identifier": 'EVENT_3511_end_loop_9',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_3511_pause_10',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3511_start_loop_n_times_11',
        "command": 'start_loop_n_times',
        "args": [6]
    },
    {
        "identifier": 'EVENT_3511_jmp_if_random_above_66_12',
        "command": 'jmp_if_random_above_66',
        "args": ['EVENT_3511_set_action_script_sync_16']
    },
    {
        "identifier": 'EVENT_3511_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 708]
    },
    {
        "identifier": 'EVENT_3511_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 709]
    },
    {
        "identifier": 'EVENT_3511_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_3511_pause_21']
    },
    {
        "identifier": 'EVENT_3511_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 709]
    },
    {
        "identifier": 'EVENT_3511_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 710]
    },
    {
        "identifier": 'EVENT_3511_jmp_18',
        "command": 'jmp',
        "args": ['EVENT_3511_pause_21']
    },
    {
        "identifier": 'EVENT_3511_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 710]
    },
    {
        "identifier": 'EVENT_3511_set_action_script_sync_20',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 708]
    },
    {
        "identifier": 'EVENT_3511_pause_21',
        "command": 'pause',
        "args": [210]
    },
    {
        "identifier": 'EVENT_3511_end_loop_22',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_3511_pause_23',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3511_start_loop_n_times_24',
        "command": 'start_loop_n_times',
        "args": [6]
    },
    {
        "identifier": 'EVENT_3511_set_action_script_sync_25',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 708]
    },
    {
        "identifier": 'EVENT_3511_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 709]
    },
    {
        "identifier": 'EVENT_3511_set_action_script_sync_27',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 710]
    },
    {
        "identifier": 'EVENT_3511_pause_28',
        "command": 'pause',
        "args": [210]
    },
    {
        "identifier": 'EVENT_3511_end_loop_29',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_3511_pause_30',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3511_pause_31',
        "command": 'pause',
        "args": [210]
    },
    {
        "identifier": 'EVENT_3511_pause_32',
        "command": 'pause',
        "args": [210]
    },
    {
        "identifier": 'EVENT_3511_start_loop_n_times_33',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3511_pause_34',
        "command": 'pause',
        "args": [210]
    },
    {
        "identifier": 'EVENT_3511_pause_35',
        "command": 'pause',
        "args": [210]
    },
    {
        "identifier": 'EVENT_3511_set_short_mem_36',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b1]
    },
    {
        "identifier": 'EVENT_3511_mem_compare_37',
        "command": 'mem_compare',
        "args": [0x7000, 8]
    },
    {
        "identifier": 'EVENT_3511_jmp_if_comparison_result_is_greater_or_equal_38',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_3511_end_loop_41']
    },
    {
        "identifier": 'EVENT_3511_play_sound_balance_39',
        "command": 'play_sound_balance',
        "args": [Sounds._014_FLOWER, 40]
    },
    {
        "identifier": 'EVENT_3511_set_action_script_sync_40',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 364]
    },
    {
        "identifier": 'EVENT_3511_end_loop_41',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_3511_ret_42',
        "command": 'ret'
    }
]
