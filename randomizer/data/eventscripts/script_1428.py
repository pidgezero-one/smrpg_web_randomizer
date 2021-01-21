from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1428_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_1428_disable_trigger_1',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_1428_freeze_all_npcs_until_return_2',
        "command": 'freeze_all_npcs_until_return'
    },
    {
        "identifier": 'EVENT_1428_resume_action_script_3',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1428_start_battle_4',
        "command": 'start_battle',
        "args": [0x0006, 9]
    },
    {
        "identifier": 'EVENT_1428_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_1428_enable_trigger_21']
    },
    {
        "identifier": 'EVENT_1428_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_1428_reset_and_choose_game_27']
    },
    {
        "identifier": 'EVENT_1428_remove_from_level_7',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_9, Rooms._203_MUSHROOM_WAY_AREA_01]
    },
    {
        "identifier": 'EVENT_1428_remove_from_current_level_8',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_1428_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1428_action_queue_sync_9_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [10, 22, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1428_action_queue_sync_9_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1428_action_queue_sync_9_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1428_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1428_action_queue_async_10_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [10, 23, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1428_action_queue_async_10_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1428_set_bit_11',
        "command": 'set_bit',
        "args": [0x7052, 4]
    },
    {
        "identifier": 'EVENT_1428_fade_in_from_black_async_12',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1428_set_13',
        "command": 'set',
        "args": [0x70a7, 99]
    },
    {
        "identifier": 'EVENT_1428_set_14',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_1428_run_event_as_subroutine_15',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_1428_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1428_action_queue_async_16_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1428_action_queue_async_16_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1428_action_queue_async_16_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1428_action_queue_async_16_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1428_action_queue_async_16_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1428_remove_from_current_level_17',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_1428_remove_from_level_18',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_8, Rooms._203_MUSHROOM_WAY_AREA_01]
    },
    {
        "identifier": 'EVENT_1428_unfreeze_all_npcs_19',
        "command": 'unfreeze_all_npcs'
    },
    {
        "identifier": 'EVENT_1428_ret_20',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1428_enable_trigger_21',
        "command": 'enable_trigger',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_1428_enable_trigger_22',
        "command": 'enable_trigger',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_1428_set_temp_action_script_sync_23',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_8, 2]
    },
    {
        "identifier": 'EVENT_1428_set_temp_action_script_sync_24',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_9, 2]
    },
    {
        "identifier": 'EVENT_1428_fade_in_from_black_async_25',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1428_ret_26',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1428_reset_and_choose_game_27',
        "command": 'reset_and_choose_game'
    },
    {
        "identifier": 'EVENT_1428_ret_28',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1428_stop_sound_29',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1428_stop_sound_30',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1428_stop_sound_31',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1428_stop_sound_32',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1428_stop_sound_33',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1428_stop_sound_34',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1428_stop_sound_35',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1428_stop_sound_36',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1428_stop_sound_37',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1428_stop_sound_38',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1428_stop_sound_39',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1428_ret_40',
        "command": 'ret'
    }
]
