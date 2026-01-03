
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1428_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7052, 4, 'EVENT_1428_ret_24']
    },
    {
        "identifier": 'EVENT_1428_disable_trigger_1',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_1428_disable_trigger_2',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_1428_freeze_all_npcs_until_return_3',
        "command": 'freeze_all_npcs_until_return'
    },
    {
        "identifier": 'EVENT_1428_resume_action_script_4',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1428_start_battle_5',
        "command": 'start_battle',
        "args": [0x0006, 9]
    },
    {
        "identifier": 'EVENT_1428_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_1428_enable_trigger_25']
    },
    {
        "identifier": 'EVENT_1428_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_1428_reset_and_choose_game_31']
    },
    {
        "identifier": 'EVENT_1428_remove_from_level_8',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_9, Rooms._203_MUSHROOM_WAY_AREA_01]
    },
    {
        "identifier": 'EVENT_1428_remove_from_current_level_9',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_1428_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1428_action_queue_sync_10_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [10, 22, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1428_action_queue_sync_10_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1428_action_queue_sync_10_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1428_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1428_action_queue_async_11_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [10, 23, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1428_action_queue_async_11_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1428_set_bit_12',
        "command": 'set_bit',
        "args": [0x7052, 4]
    },
    {
        "identifier": 'EVENT_1428_fade_in_from_black_async_13',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1428_pause_14',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1428_run_dialog_15',
        "command": 'run_dialog',
        "args": [2746, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1428_set_16',
        "command": 'set',
        "args": [0x70a7, 99]
    },
    {
        "identifier": 'EVENT_1428_set_17',
        "command": 'set',
        "args": [0x7000, 2736]
    },
    {
        "identifier": 'EVENT_1428_run_event_as_subroutine_18',
        "command": 'run_event_as_subroutine',
        "args": [3827]
    },
    {
        "identifier": 'EVENT_1428_pause_19',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1428_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1428_action_queue_async_20_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1428_action_queue_async_20_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1428_action_queue_async_20_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1428_action_queue_async_20_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1428_action_queue_async_20_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1428_remove_from_current_level_21',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_1428_remove_from_level_22',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_8, Rooms._203_MUSHROOM_WAY_AREA_01]
    },
    {
        "identifier": 'EVENT_1428_unfreeze_all_npcs_23',
        "command": 'unfreeze_all_npcs'
    },
    {
        "identifier": 'EVENT_1428_ret_24',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1428_enable_trigger_25',
        "command": 'enable_trigger',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_1428_enable_trigger_26',
        "command": 'enable_trigger',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_1428_set_temp_action_script_sync_27',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_8, 2]
    },
    {
        "identifier": 'EVENT_1428_set_temp_action_script_sync_28',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_9, 2]
    },
    {
        "identifier": 'EVENT_1428_fade_in_from_black_async_29',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1428_ret_30',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1428_reset_and_choose_game_31',
        "command": 'reset_and_choose_game'
    },
    {
        "identifier": 'EVENT_1428_ret_32',
        "command": 'ret'
    }
]
