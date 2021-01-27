from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1682_set_7000_to_70A0_short_mem_0',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70a8]
    },
    {
        "identifier": 'EVENT_1682_set_70A0_short_mem_to_7000_1',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70ae]
    },
    {
        "identifier": 'EVENT_1682_store_coin_amount_7000_2',
        "command": 'store_coin_amount_7000'
    },
    {
        "identifier": 'EVENT_1682_mem_compare_val_3',
        "command": 'mem_compare_val',
        "args": [100]
    },
    {
        "identifier": 'EVENT_1682_jmp_if_comparison_result_is_lesser_4',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1682_action_queue_async_19']
    },
    {
        "identifier": 'EVENT_1682_run_dialog_5',
        "command": 'run_dialog',
        "args": [1228, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1682_jmp_if_dialog_option_b_6',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1682_pause_22']
    },
    {
        "identifier": 'EVENT_1682_pause_7',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1682_set_action_script_async_8',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_1682_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1682_action_queue_async_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1682_action_queue_async_9_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1682_action_queue_async_9_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1682_action_queue_async_9_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1682_set_10',
        "command": 'set',
        "args": [0x7000, 100]
    },
    {
        "identifier": 'EVENT_1682_dec_coins_11',
        "command": 'dec_coins'
    },
    {
        "identifier": 'EVENT_1682_play_sound_12',
        "command": 'play_sound',
        "args": [Sounds._055_LOSE_COINS_COIN_FOUNTAIN, 6]
    },
    {
        "identifier": 'EVENT_1682_pause_13',
        "command": 'pause',
        "args": [50]
    },
    {
        "identifier": 'EVENT_1682_set_14',
        "command": 'set',
        "args": [0x70aa, 20]
    },
    {
        "identifier": 'EVENT_1682_jmp_to_subroutine_15',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1794_action_queue_async_73']
    },
    {
        "identifier": 'EVENT_1682_remove_from_level_16',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._428_BELOME_TEMPLE_AREA_01_WWARP_TRAMPOLINE]
    },
    {
        "identifier": 'EVENT_1682_set_bit_17',
        "command": 'set_bit',
        "args": [0x704f, 1]
    },
    {
        "identifier": 'EVENT_1682_ret_18',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1682_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1682_action_queue_async_19_SUBSCRIPT_face_mario_0',
                "command": 'face_mario'
            }
        ]
    },
    {
        "identifier": 'EVENT_1682_run_dialog_20',
        "command": 'run_dialog',
        "args": [1229, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1682_ret_21',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1682_pause_22',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1682_set_action_script_async_23',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_1682_ret_24',
        "command": 'ret'
    }
]
