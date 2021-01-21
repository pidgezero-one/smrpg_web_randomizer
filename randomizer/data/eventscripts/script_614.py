from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_614_run_dialog_0',
        "command": 'run_dialog',
        "args": [985, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_614_run_dialog_1',
        "command": 'run_dialog',
        "args": [986, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_614_jmp_if_dialog_option_b_2',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_614_pause_15']
    },
    {
        "identifier": 'EVENT_614_pause_3',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_614_set_short_4',
        "command": 'set_short',
        "args": [0x7024, 0x000a]
    },
    {
        "identifier": 'EVENT_614_run_event_as_subroutine_5',
        "command": 'run_event_as_subroutine',
        "args": [274]
    },
    {
        "identifier": 'EVENT_614_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 3, 'EVENT_614_run_dialog_14']
    },
    {
        "identifier": 'EVENT_614_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6]
    },
    {
        "identifier": 'EVENT_614_set_8',
        "command": 'set',
        "args": [0x7000, 10]
    },
    {
        "identifier": 'EVENT_614_dec_coins_9',
        "command": 'dec_coins'
    },
    {
        "identifier": 'EVENT_614_run_dialog_10',
        "command": 'run_dialog',
        "args": [988, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_614_jmp_if_bit_set_11',
        "command": 'jmp_if_bit_set',
        "args": [0x709f, 0, 'EVENT_614_pause_17']
    },
    {
        "identifier": 'EVENT_614_set_bit_12',
        "command": 'set_bit',
        "args": [0x7042, 7]
    },
    {
        "identifier": 'EVENT_614_jmp_13',
        "command": 'jmp',
        "args": ['EVENT_614_pause_17']
    },
    {
        "identifier": 'EVENT_614_run_dialog_14',
        "command": 'run_dialog',
        "args": [987, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_614_pause_15',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_614_run_dialog_16',
        "command": 'run_dialog',
        "args": [973, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_614_pause_17',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_614_jmp_if_bit_set_18',
        "command": 'jmp_if_bit_set',
        "args": [0x709f, 0, 'EVENT_614_action_queue_async_29']
    },
    {
        "identifier": 'EVENT_614_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_614_action_queue_async_19_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_614_action_queue_async_19_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_614_action_queue_async_19_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_614_action_queue_async_19_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_614_action_queue_async_19_SUBSCRIPT_clear_solidity_bits_4',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_614_pause_20',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_614_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_614_action_queue_async_21_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_614_clear_bit_22',
        "command": 'clear_bit',
        "args": [0x7042, 1]
    },
    {
        "identifier": 'EVENT_614_clear_bit_23',
        "command": 'clear_bit',
        "args": [0x7042, 2]
    },
    {
        "identifier": 'EVENT_614_clear_bit_24',
        "command": 'clear_bit',
        "args": [0x7042, 3]
    },
    {
        "identifier": 'EVENT_614_set_bit_25',
        "command": 'set_bit',
        "args": [0x7042, 4]
    },
    {
        "identifier": 'EVENT_614_clear_bit_26',
        "command": 'clear_bit',
        "args": [0x709f, 1]
    },
    {
        "identifier": 'EVENT_614_clear_bit_27',
        "command": 'clear_bit',
        "args": [0x709f, 0]
    },
    {
        "identifier": 'EVENT_614_ret_28',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_614_action_queue_async_29',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_614_action_queue_async_29_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_614_action_queue_async_29_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_614_action_queue_async_29_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_614_action_queue_async_29_SUBSCRIPT_walk_1_step_northwest_3',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_614_action_queue_async_29_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_614_action_queue_async_29_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_614_clear_bit_30',
        "command": 'clear_bit',
        "args": [0x7042, 1]
    },
    {
        "identifier": 'EVENT_614_clear_bit_31',
        "command": 'clear_bit',
        "args": [0x7042, 2]
    },
    {
        "identifier": 'EVENT_614_clear_bit_32',
        "command": 'clear_bit',
        "args": [0x7042, 3]
    },
    {
        "identifier": 'EVENT_614_clear_bit_33',
        "command": 'clear_bit',
        "args": [0x709f, 0]
    },
    {
        "identifier": 'EVENT_614_clear_bit_34',
        "command": 'clear_bit',
        "args": [0x709f, 1]
    },
    {
        "identifier": 'EVENT_614_ret_35',
        "command": 'ret'
    }
]
