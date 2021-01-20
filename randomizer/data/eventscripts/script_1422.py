from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1422_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_pause_action_script_1',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_pause_action_script_2',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_start_battle_3',
        "command": 'start_battle',
        "args": [0x0004, 9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_1422_set_action_script_async_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_1422_reset_and_choose_game_37'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_1422_freeze_all_npcs_until_return_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_set_action_script_async_7',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_7, 15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_set_action_script_async_8',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_8, 15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1422_action_queue_sync_9_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_1422_action_queue_sync_9_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [13, 28, 12, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1422_action_queue_sync_9_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1422_action_queue_sync_9_SUBSCRIPT_ret_3',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1422_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1422_action_queue_sync_10_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_1422_action_queue_sync_10_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [13, 28, 14, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1422_action_queue_sync_10_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1422_action_queue_sync_10_SUBSCRIPT_ret_3',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1422_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1422_action_queue_async_11_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [14, 28, 6, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1422_action_queue_async_11_SUBSCRIPT_face_south_1',
                "command": 'face_south',
                "args": []
            },
            {
                "identifier": 'EVENT_1422_action_queue_async_11_SUBSCRIPT_ret_2',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1422_run_background_event_12',
        "command": 'run_background_event',
        "args": [1432, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_fade_in_from_black_async_13',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_ret_14',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_freeze_all_npcs_until_return_15',
        "command": 'freeze_all_npcs_until_return',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1422_action_queue_sync_16_SUBSCRIPT_floating_on_0',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1422_action_queue_sync_16_SUBSCRIPT_bpl_26_27_28_1',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_1422_action_queue_sync_16_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1422_action_queue_sync_16_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_1422_action_queue_sync_16_SUBSCRIPT_transfer_to_xyzf_4',
                "command": 'transfer_to_xyzf',
                "args": [14, 28, 6, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1422_action_queue_sync_16_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1422_action_queue_sync_16_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1422_action_queue_sync_16_SUBSCRIPT_sequence_looping_on_7',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1422_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1422_action_queue_async_17_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [13, 29, 6, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1422_action_queue_async_17_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1422_remove_from_current_level_18',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_remove_from_level_19',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_8, Rooms._204_MUSHROOM_WAY_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_fade_in_from_black_async_20',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_pause_21',
        "command": 'pause',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_set_22',
        "command": 'set',
        "args": [0x70a7, 115],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_set_23',
        "command": 'set',
        "args": [0x7000, 524],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_run_event_as_subroutine_24',
        "command": 'run_event_as_subroutine',
        "args": [3828],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_pause_25',
        "command": 'pause',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1422_action_queue_async_26_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1422_action_queue_async_26_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1422_action_queue_async_26_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [112]
            },
            {
                "identifier": 'EVENT_1422_action_queue_async_26_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [11]
            },
            {
                "identifier": 'EVENT_1422_action_queue_async_26_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1422_remove_from_current_level_27',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_remove_from_level_28',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._204_MUSHROOM_WAY_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_summon_to_level_29',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._205_MUSHROOM_WAY_AREA_03],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_set_bit_30',
        "command": 'set_bit',
        "args": [0x7052, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_unfreeze_all_npcs_31',
        "command": 'unfreeze_all_npcs',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_stop_sound_32',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_stop_sound_33',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_stop_sound_34',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_stop_sound_35',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_ret_36',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_reset_and_choose_game_37',
        "command": 'reset_and_choose_game',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1422_ret_38',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
