from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1793_set_short_mem_0',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8]
    },
    {
        "identifier": 'EVENT_1793_mem_compare_1',
        "command": 'mem_compare',
        "args": [0x7000, 38]
    },
    {
        "identifier": 'EVENT_1793_jmp_if_loaded_memory_is_not_0_2',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['EVENT_1793_set_bit_6']
    },
    {
        "identifier": 'EVENT_1793_set_bit_3',
        "command": 'set_bit',
        "args": [0x7050, 0]
    },
    {
        "identifier": 'EVENT_1793_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x704f, 7]
    },
    {
        "identifier": 'EVENT_1793_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_1793_run_event_as_subroutine_8']
    },
    {
        "identifier": 'EVENT_1793_set_bit_6',
        "command": 'set_bit',
        "args": [0x7050, 2]
    },
    {
        "identifier": 'EVENT_1793_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7050, 1]
    },
    {
        "identifier": 'EVENT_1793_run_event_as_subroutine_8',
        "command": 'run_event_as_subroutine',
        "args": [32]
    },
    {
        "identifier": 'EVENT_1793_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1793_action_queue_sync_9_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1793_action_queue_sync_9_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1793_action_queue_sync_9_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1793_action_queue_sync_9_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1793_action_queue_sync_9_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1793_action_queue_sync_9_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1793_action_queue_sync_9_SUBSCRIPT_start_loop_n_times_6',
                "command": 'start_loop_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1793_action_queue_sync_9_SUBSCRIPT_visibility_on_7',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1793_action_queue_sync_9_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1793_action_queue_sync_9_SUBSCRIPT_visibility_off_9',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1793_action_queue_sync_9_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1793_action_queue_sync_9_SUBSCRIPT_end_loop_11',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1793_action_queue_sync_9_SUBSCRIPT_clear_solidity_bits_12',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1793_ret_10',
        "command": 'ret'
    }
]
