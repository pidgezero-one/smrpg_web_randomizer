from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3364_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3364_action_queue_async_0_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3364_action_queue_async_0_SUBSCRIPT_shift_xy_pixels_1',
                "command": 'shift_xy_pixels',
                "args": [250, 253]
            },
            {
                "identifier": 'EVENT_3364_action_queue_async_0_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3364_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [15]
    },
    {
        "identifier": 'EVENT_3364_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3364_action_queue_async_2_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_3364_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3364_action_queue_async_3_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3364_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_3364_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 59]
    },
    {
        "identifier": 'EVENT_3364_run_dialog_6',
        "command": 'run_dialog',
        "args": [1920, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3364_set_bit_7',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_3364_set_short_8',
        "command": 'set_short',
        "args": [0x7024, 0x0001]
    },
    {
        "identifier": 'EVENT_3364_set_short_9',
        "command": 'set_short',
        "args": [0x7026, 0x0002]
    },
    {
        "identifier": 'EVENT_3364_set_short_10',
        "command": 'set_short',
        "args": [0x7028, 0x0003]
    },
    {
        "identifier": 'EVENT_3364_set_short_11',
        "command": 'set_short',
        "args": [0x702a, 0x0004]
    },
    {
        "identifier": 'EVENT_3364_start_loop_n_times_12',
        "command": 'start_loop_n_times',
        "args": [18]
    },
    {
        "identifier": 'EVENT_3364_jmp_if_random_above_128_13',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_3364_jmp_if_random_above_66_21']
    },
    {
        "identifier": 'EVENT_3364_jmp_if_random_above_66_14',
        "command": 'jmp_if_random_above_66',
        "args": [0x574a, 0x5750]
    },
    {
        "identifier": 'EVENT_3364_swap_short_mem_15',
        "command": 'swap_short_mem',
        "args": [0x7024, 0x7026]
    },
    {
        "identifier": 'EVENT_3364_jmp_16',
        "command": 'jmp',
        "args": ['EVENT_3364_end_loop_27']
    },
    {
        "identifier": 'EVENT_3364_swap_short_mem_17',
        "command": 'swap_short_mem',
        "args": [0x7024, 0x7028]
    },
    {
        "identifier": 'EVENT_3364_jmp_18',
        "command": 'jmp',
        "args": ['EVENT_3364_end_loop_27']
    },
    {
        "identifier": 'EVENT_3364_swap_short_mem_19',
        "command": 'swap_short_mem',
        "args": [0x7024, 0x702a]
    },
    {
        "identifier": 'EVENT_3364_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_3364_end_loop_27']
    },
    {
        "identifier": 'EVENT_3364_jmp_if_random_above_66_21',
        "command": 'jmp_if_random_above_66',
        "args": [0x5761, 0x5767]
    },
    {
        "identifier": 'EVENT_3364_swap_short_mem_22',
        "command": 'swap_short_mem',
        "args": [0x7026, 0x7028]
    },
    {
        "identifier": 'EVENT_3364_jmp_23',
        "command": 'jmp',
        "args": ['EVENT_3364_end_loop_27']
    },
    {
        "identifier": 'EVENT_3364_swap_short_mem_24',
        "command": 'swap_short_mem',
        "args": [0x7026, 0x702a]
    },
    {
        "identifier": 'EVENT_3364_jmp_25',
        "command": 'jmp',
        "args": ['EVENT_3364_end_loop_27']
    },
    {
        "identifier": 'EVENT_3364_swap_short_mem_26',
        "command": 'swap_short_mem',
        "args": [0x7028, 0x702a]
    },
    {
        "identifier": 'EVENT_3364_end_loop_27',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_3364_play_music_default_volume_28',
        "command": 'play_music_default_volume',
        "args": [Music._36_EXPLANATION]
    },
    {
        "identifier": 'EVENT_3364_ret_29',
        "command": 'ret'
    }
]
