
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3680_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 5, 'EVENT_3680_run_dialog_16']
    },
    {
        "identifier": 'EVENT_3680_run_dialog_1',
        "command": 'run_dialog',
        "args": [48, AreaObjects.MARIO, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3680_jmp_if_dialog_option_b_2',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3680_run_dialog_14']
    },
    {
        "identifier": 'EVENT_3680_run_dialog_3',
        "command": 'run_dialog',
        "args": [47, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3680_start_battle_4',
        "command": 'start_battle',
        "args": [0x00af, 23]
    },
    {
        "identifier": 'EVENT_3680_set_bit_5',
        "command": 'set_bit',
        "args": [0x704a, 2]
    },
    {
        "identifier": 'EVENT_3680_run_event_as_subroutine_6',
        "command": 'run_event_as_subroutine',
        "args": [1011]
    },
    {
        "identifier": 'EVENT_3680_set_bit_7',
        "command": 'set_bit',
        "args": [0x705f, 5]
    },
    {
        "identifier": 'EVENT_3680_restore_all_hp_8',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_3680_restore_all_fp_9',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_3680_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3680_pause_11',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3680_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3680_action_queue_async_12_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3680_action_queue_async_12_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [18, 53, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3680_action_queue_async_12_SUBSCRIPT_floating_on_2',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3680_action_queue_async_12_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3680_action_queue_async_12_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3680_action_queue_async_12_SUBSCRIPT_shift_southwest_pixels_5',
                "command": 'shift_southwest_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3680_ret_13',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3680_run_dialog_14',
        "command": 'run_dialog',
        "args": [50, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3680_ret_15',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3680_run_dialog_16',
        "command": 'run_dialog',
        "args": [49, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3680_ret_17',
        "command": 'ret'
    }
]
