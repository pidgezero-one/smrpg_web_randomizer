from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1645_set_short_mem_0',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8]
    },
    {
        "identifier": 'EVENT_1645_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x70ae, 0x7000]
    },
    {
        "identifier": 'EVENT_1645_store_item_amount_7000_2',
        "command": 'store_item_amount_7000',
        "args": [items.CarboCookie]
    },
    {
        "identifier": 'EVENT_1645_jmp_if_var_not_equals_short_3',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 0, 'EVENT_1645_run_dialog_6']
    },
    {
        "identifier": 'EVENT_1645_run_dialog_4',
        "command": 'run_dialog',
        "args": [1146, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1645_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1645_run_dialog_6',
        "command": 'run_dialog',
        "args": [1147, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1645_jmp_if_dialog_option_b_7',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1645_pause_27']
    },
    {
        "identifier": 'EVENT_1645_pause_8',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1645_set_action_script_async_9',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_1645_remove_one_from_inventory_10',
        "command": 'remove_one_from_inventory',
        "args": [items.CarboCookie]
    },
    {
        "identifier": 'EVENT_1645_jmp_if_bit_set_11',
        "command": 'jmp_if_bit_set',
        "args": [0x704d, 2, 'EVENT_1645_run_dialog_21']
    },
    {
        "identifier": 'EVENT_1645_run_dialog_12',
        "command": 'run_dialog',
        "args": [1149, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1645_set_bit_13',
        "command": 'set_bit',
        "args": [0x704d, 2]
    },
    {
        "identifier": 'EVENT_1645_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1645_action_queue_async_14_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 4]
            },
            {
                "identifier": 'EVENT_1645_action_queue_async_14_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1645_action_queue_async_14_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1645_action_queue_async_14_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1645_action_queue_async_14_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1645_action_queue_async_14_SUBSCRIPT_fixed_f_coord_on_5',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1645_action_queue_async_14_SUBSCRIPT_shift_south_steps_6',
                "command": 'shift_south_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1645_action_queue_async_14_SUBSCRIPT_jmp_if_bit_set_7',
                "command": 'jmp_if_bit_set',
                "args": [0x7096, 7, 'EVENT_1645_jmp_if_bit_set_15']
            },
            {
                "identifier": 'EVENT_1645_action_queue_async_14_SUBSCRIPT_fixed_f_coord_off_8',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1645_action_queue_async_14_SUBSCRIPT_face_mario_9',
                "command": 'face_mario'
            },
            {
                "identifier": 'EVENT_1645_action_queue_async_14_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_1645_jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x7096, 7, 'EVENT_1645_action_queue_async_18']
    },
    {
        "identifier": 'EVENT_1645_run_dialog_16',
        "command": 'run_dialog',
        "args": [1232, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1645_set_bit_17',
        "command": 'set_bit',
        "args": [0x7096, 7]
    },
    {
        "identifier": 'EVENT_1645_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1645_action_queue_async_18_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1645_action_queue_async_18_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_1645_action_queue_async_18_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1645_set_bit_19',
        "command": 'set_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_1645_ret_20',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1645_run_dialog_21',
        "command": 'run_dialog',
        "args": [1150, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1645_play_sound_22',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_1645_add_frog_coins_23',
        "command": 'add_frog_coins',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1645_run_dialog_24',
        "command": 'run_dialog',
        "args": [1176, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1645_clear_bit_25',
        "command": 'clear_bit',
        "args": [0x704d, 2]
    },
    {
        "identifier": 'EVENT_1645_ret_26',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1645_pause_27',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1645_set_action_script_async_28',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_1645_run_dialog_29',
        "command": 'run_dialog',
        "args": [1148, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1645_ret_30',
        "command": 'ret'
    }
]
