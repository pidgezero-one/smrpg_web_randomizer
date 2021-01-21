from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3503_set_0',
        "command": 'set',
        "args": [0x70ae, 3]
    },
    {
        "identifier": 'EVENT_3503_start_loop_n_times_1',
        "command": 'start_loop_n_times',
        "args": [6]
    },
    {
        "identifier": 'EVENT_3503_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 709]
    },
    {
        "identifier": 'EVENT_3503_pause_3',
        "command": 'pause',
        "args": [210]
    },
    {
        "identifier": 'EVENT_3503_end_loop_4',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_3503_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x704d, 7, 'EVENT_3503_pause_9']
    },
    {
        "identifier": 'EVENT_3503_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_3503_pause_9']
    },
    {
        "identifier": 'EVENT_3503_set_bit_7',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_3503_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 717]
    },
    {
        "identifier": 'EVENT_3503_pause_9',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3503_set_10',
        "command": 'set',
        "args": [0x70ae, 2]
    },
    {
        "identifier": 'EVENT_3503_start_loop_n_times_11',
        "command": 'start_loop_n_times',
        "args": [6]
    },
    {
        "identifier": 'EVENT_3503_jmp_if_random_above_66_12',
        "command": 'jmp_if_random_above_66',
        "args": ['EVENT_3503_set_action_script_sync_16']
    },
    {
        "identifier": 'EVENT_3503_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 708]
    },
    {
        "identifier": 'EVENT_3503_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 709]
    },
    {
        "identifier": 'EVENT_3503_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_3503_pause_21']
    },
    {
        "identifier": 'EVENT_3503_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 709]
    },
    {
        "identifier": 'EVENT_3503_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 710]
    },
    {
        "identifier": 'EVENT_3503_jmp_18',
        "command": 'jmp',
        "args": ['EVENT_3503_pause_21']
    },
    {
        "identifier": 'EVENT_3503_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 710]
    },
    {
        "identifier": 'EVENT_3503_set_action_script_sync_20',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 708]
    },
    {
        "identifier": 'EVENT_3503_pause_21',
        "command": 'pause',
        "args": [210]
    },
    {
        "identifier": 'EVENT_3503_end_loop_22',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_3503_pause_23',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3503_set_24',
        "command": 'set',
        "args": [0x70ae, 1]
    },
    {
        "identifier": 'EVENT_3503_start_loop_n_times_25',
        "command": 'start_loop_n_times',
        "args": [6]
    },
    {
        "identifier": 'EVENT_3503_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 708]
    },
    {
        "identifier": 'EVENT_3503_set_action_script_sync_27',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 709]
    },
    {
        "identifier": 'EVENT_3503_set_action_script_sync_28',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 710]
    },
    {
        "identifier": 'EVENT_3503_pause_29',
        "command": 'pause',
        "args": [210]
    },
    {
        "identifier": 'EVENT_3503_end_loop_30',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_3503_pause_31',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3503_set_32',
        "command": 'set',
        "args": [0x70ae, 0]
    },
    {
        "identifier": 'EVENT_3503_set_bit_33',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_3503_set_temp_action_script_async_34',
        "command": 'set_temp_action_script_async',
        "args": [AreaObjects.NPC_4, 712]
    },
    {
        "identifier": 'EVENT_3503_set_temp_action_script_async_35',
        "command": 'set_temp_action_script_async',
        "args": [AreaObjects.NPC_5, 712]
    },
    {
        "identifier": 'EVENT_3503_action_queue_async_36',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3503_action_queue_async_36_SUBSCRIPT_walk_1_step_northeast_0',
                "command": 'walk_1_step_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3503_set_temp_action_script_async_37',
        "command": 'set_temp_action_script_async',
        "args": [AreaObjects.NPC_3, 712]
    },
    {
        "identifier": 'EVENT_3503_ret_38',
        "command": 'ret'
    }
]
