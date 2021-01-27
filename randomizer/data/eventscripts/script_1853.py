from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1853_set_7000_to_70A0_short_mem_0',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70a8]
    },
    {
        "identifier": 'EVENT_1853_set_70A0_short_mem_to_7000_1',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70ae]
    },
    {
        "identifier": 'EVENT_1853_jmp_fork_mario_on_object_2',
        "command": 'jmp_fork_mario_on_object',
        "args": ['EVENT_1853_stop_all_background_events_5', 'EVENT_1853_run_dialog_3']
    },
    {
        "identifier": 'EVENT_1853_run_dialog_3',
        "command": 'run_dialog',
        "args": [1313, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1853_ret_4',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1853_stop_all_background_events_5',
        "command": 'stop_all_background_events'
    },
    {
        "identifier": 'EVENT_1853_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_1853_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'EVENT_1853_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_1853_set_bit_9',
        "command": 'set_bit',
        "args": [0x7094, 3]
    },
    {
        "identifier": 'EVENT_1853_set_bit_10',
        "command": 'set_bit',
        "args": [0x707b, 7]
    },
    {
        "identifier": 'EVENT_1853_set_short_11',
        "command": 'set_short',
        "args": [0x702e, 0x0030]
    },
    {
        "identifier": 'EVENT_1853_set_short_12',
        "command": 'set_short',
        "args": [0x702c, 0x0046]
    },
    {
        "identifier": 'EVENT_1853_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_17],
        "subscript": [
            {
                "identifier": 'EVENT_1853_action_queue_sync_13_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [20, 104, 18, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_1853_set_7016_to_object_xyz_14',
        "command": 'set_7016_to_object_xyz',
        "args": [0x90]
    },
    {
        "identifier": 'EVENT_1853_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1853_action_queue_async_15_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1853_action_queue_async_15_SUBSCRIPT_run_away_shift_1',
                "command": 'run_away_shift'
            },
            {
                "identifier": 'EVENT_1853_action_queue_async_15_SUBSCRIPT_floating_on_2',
                "command": 'floating_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1853_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1853_action_queue_async_16_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1853_action_queue_async_16_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1853_action_queue_async_16_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1853_action_queue_async_16_SUBSCRIPT_shift_north_steps_3',
                "command": 'shift_north_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1853_action_queue_async_16_SUBSCRIPT_clear_solidity_bits_4',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1853_action_queue_async_16_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._161_GHOST, 4]
            },
            {
                "identifier": 'EVENT_1853_action_queue_async_16_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [128]
            },
            {
                "identifier": 'EVENT_1853_action_queue_async_16_SUBSCRIPT_start_loop_n_times_7',
                "command": 'start_loop_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1853_action_queue_async_16_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1853_action_queue_async_16_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1853_action_queue_async_16_SUBSCRIPT_visibility_on_10',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1853_action_queue_async_16_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1853_action_queue_async_16_SUBSCRIPT_end_loop_12',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1853_action_queue_async_16_SUBSCRIPT_set_solidity_bits_13',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_1853_action_queue_async_16_SUBSCRIPT_transfer_to_xyzf_14',
                "command": 'transfer_to_xyzf',
                "args": [20, 112, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1853_action_queue_async_16_SUBSCRIPT_face_southwest_15',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1853_ret_17',
        "command": 'ret'
    }
]
