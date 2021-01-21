from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_436_stop_all_background_events_0',
        "command": 'stop_all_background_events'
    },
    {
        "identifier": 'EVENT_436_start_battle_1',
        "command": 'start_battle',
        "args": [0x001e, 21]
    },
    {
        "identifier": 'EVENT_436_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [440]
    },
    {
        "identifier": 'EVENT_436_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_436_action_queue_async_7']
    },
    {
        "identifier": 'EVENT_436_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_287_reset_and_choose_game_0']
    },
    {
        "identifier": 'EVENT_436_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_436_action_queue_async_5_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 19, 4, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_436_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_436_set_bit_8']
    },
    {
        "identifier": 'EVENT_436_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_436_action_queue_async_7_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [4, 22, 2, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_436_set_bit_8',
        "command": 'set_bit',
        "args": [0x7049, 6]
    },
    {
        "identifier": 'EVENT_436_run_event_as_subroutine_9',
        "command": 'run_event_as_subroutine',
        "args": [276]
    },
    {
        "identifier": 'EVENT_436_jmp_if_bit_clear_10',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 1, 'EVENT_436_fade_in_from_black_async_12']
    },
    {
        "identifier": 'EVENT_436_set_temp_action_script_sync_11',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 2]
    },
    {
        "identifier": 'EVENT_436_fade_in_from_black_async_12',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_436_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_436_action_queue_async_13_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_436_action_queue_async_13_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_436_action_queue_async_13_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_436_action_queue_async_13_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_436_action_queue_async_13_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_436_action_queue_async_13_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_436_action_queue_async_13_SUBSCRIPT_start_loop_n_times_6',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_436_action_queue_async_13_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_436_action_queue_async_13_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_436_action_queue_async_13_SUBSCRIPT_visibility_on_9',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_436_action_queue_async_13_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_436_action_queue_async_13_SUBSCRIPT_end_loop_11',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_436_action_queue_async_13_SUBSCRIPT_start_loop_n_times_12',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_436_action_queue_async_13_SUBSCRIPT_visibility_off_13',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_436_action_queue_async_13_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_436_action_queue_async_13_SUBSCRIPT_visibility_on_15',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_436_action_queue_async_13_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_436_action_queue_async_13_SUBSCRIPT_end_loop_17',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_436_run_background_event_14',
        "command": 'run_background_event',
        "args": [3329, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_436_ret_15',
        "command": 'ret'
    }
]
