from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3794_set_action_script_sync_0',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 991],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_set_action_script_sync_1',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 240],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 990],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 241],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_set_bit_4',
        "command": 'set_bit',
        "args": [0x7044, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_run_background_event_5',
        "command": 'run_background_event',
        "args": [3793, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_6_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_6_SUBSCRIPT_floating_on_1',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_6_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_6_SUBSCRIPT_jmp_if_mario_in_air_3',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3794_action_queue_sync_6_SUBSCRIPT_pause_2']
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_6_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_6_SUBSCRIPT_set_vram_priority_6',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_6_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_6_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_7_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_7_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_7_SUBSCRIPT_walk_1_step_south_2',
                "command": 'walk_1_step_south',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_remember_last_object_8',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_pause_9',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_jmp_10',
        "command": 'jmp',
        "args": ['EVENT_3794_initiate_battle_mask_141'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_run_dialog_11',
        "command": 'run_dialog',
        "args": [3888, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_pause_12',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_13_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_13_SUBSCRIPT_face_east_1',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_13_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_13_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_async_14_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_14_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [3, 23, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_14_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 2, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_14_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_14_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_14_SUBSCRIPT_shift_southeast_pixels_5',
                "command": 'shift_southeast_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_14_SUBSCRIPT_face_northeast_6',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_14_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_pause_15',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_run_dialog_16',
        "command": 'run_dialog',
        "args": [3889, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_17_SUBSCRIPT_face_east_0',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_17_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_17_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_async_18_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_19',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_20',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_21',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_22',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_pause_23',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_jmp_if_bit_clear_24',
        "command": 'jmp_if_bit_clear',
        "args": [0x704c, 0, 'EVENT_3794_pause_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_clear_bit_25',
        "command": 'clear_bit',
        "args": [0x704c, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_stop_all_background_events_26',
        "command": 'stop_all_background_events',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_set_bit_27',
        "command": 'set_bit',
        "args": [0x7043, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_set_action_script_sync_28',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 989],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_set_action_script_sync_29',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 988],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_jmp_to_subroutine_30',
        "command": 'jmp_to_subroutine',
        "args": [0xc846],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_pause_31',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_run_dialog_32',
        "command": 'run_dialog',
        "args": [3890, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_jmp_to_subroutine_33',
        "command": 'jmp_to_subroutine',
        "args": [0xc851],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_set_bit_34',
        "command": 'set_bit',
        "args": [0x7043, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_set_bit_35',
        "command": 'set_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_run_background_event_36',
        "command": 'run_background_event',
        "args": [3793, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_pause_37',
        "command": 'pause',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_38',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_38_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_38_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_38_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_38_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_38_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_39',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_39_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_39_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_39_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_pause_40',
        "command": 'pause',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_run_dialog_41',
        "command": 'run_dialog',
        "args": [3891, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_pause_42',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_43',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_43_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_43_SUBSCRIPT_face_north_1',
                "command": 'face_north',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_43_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_43_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_44',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_44_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_44_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_async_45',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_async_45_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_45_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [3, 23, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_45_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [252, 254, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_45_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_45_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_45_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_45_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_45_SUBSCRIPT_shift_northwest_pixels_7',
                "command": 'shift_northwest_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_45_SUBSCRIPT_face_northeast_8',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_45_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_45_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_45_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_run_dialog_46',
        "command": 'run_dialog',
        "args": [3892, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_47_SUBSCRIPT_face_north_0',
                "command": 'face_north',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_47_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_47_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_48_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_async_49',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_async_49_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_49_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_pause_50',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_action_queue_async_51',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_async_51_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_51_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_51_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3794_action_queue_async_51_SUBSCRIPT_pause_1']
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_51_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_51_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_51_SUBSCRIPT_jmp_if_mario_in_air_5',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3794_action_queue_async_51_SUBSCRIPT_pause_4']
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_pause_52',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_53',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_54',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_55',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_56',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_pause_57',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_jmp_if_bit_clear_58',
        "command": 'jmp_if_bit_clear',
        "args": [0x704c, 0, 'EVENT_3794_pause_57'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_clear_bit_59',
        "command": 'clear_bit',
        "args": [0x704c, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_stop_all_background_events_60',
        "command": 'stop_all_background_events',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_clear_bit_61',
        "command": 'clear_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_clear_bit_62',
        "command": 'clear_bit',
        "args": [0x7043, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_set_action_script_sync_63',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 989],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_set_action_script_sync_64',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 988],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_jmp_to_subroutine_65',
        "command": 'jmp_to_subroutine',
        "args": [0xc846],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_pause_66',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_run_dialog_67',
        "command": 'run_dialog',
        "args": [3893, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_jmp_to_subroutine_68',
        "command": 'jmp_to_subroutine',
        "args": [0xc851],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_pause_69',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_play_sound_70',
        "command": 'play_sound',
        "args": [Sounds._026_LAUGHING_BOWSER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_pause_71',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_72',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_72_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_72_SUBSCRIPT_face_north_1',
                "command": 'face_north',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_72_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_72_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_72_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_72_SUBSCRIPT_face_west_5',
                "command": 'face_west',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_73',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_73_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_73_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_73_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_73_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_74',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_74_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_74_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_74_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_74_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_async_75',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_async_75_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_75_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [3, 23, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_75_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_75_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_75_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_75_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_75_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_75_SUBSCRIPT_shift_west_pixels_7',
                "command": 'shift_west_pixels',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_75_SUBSCRIPT_face_northwest_8',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_75_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_75_SUBSCRIPT_face_northeast_10',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_75_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_75_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_75_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_pause_76',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_run_dialog_77',
        "command": 'run_dialog',
        "args": [3894, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_78',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_78_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_78_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_78_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_78_SUBSCRIPT_end_loop_3',
                "command": 'end_loop',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_79',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_79_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_80',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_80_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_80_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_81',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_81_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_81_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_81_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_remember_last_object_82',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_pause_83',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_jmp_to_subroutine_84',
        "command": 'jmp_to_subroutine',
        "args": [0xc846],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_pause_85',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_run_dialog_86',
        "command": 'run_dialog',
        "args": [3895, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_jmp_to_subroutine_87',
        "command": 'jmp_to_subroutine',
        "args": [0xc851],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_pause_88',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_89',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_89_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_89_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [3, 23, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_89_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 2, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_89_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_89_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_89_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_89_SUBSCRIPT_shift_southeast_pixels_6',
                "command": 'shift_southeast_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_89_SUBSCRIPT_face_northeast_7',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_90',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_90_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_90_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_90_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_90_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_90_SUBSCRIPT_walk_1_step_southwest_4',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_90_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_90_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_90_SUBSCRIPT_face_northeast_7',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_91',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_91_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_91_SUBSCRIPT_face_east_1',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_91_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_91_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_92',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_92_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_92_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_93',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_93_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_remember_last_object_94',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_action_queue_async_95',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_async_95_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_95_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_pause_96',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_run_dialog_97',
        "command": 'run_dialog',
        "args": [3896, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_pause_98',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_99',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_99_SUBSCRIPT_face_east_0',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_99_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_99_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_100',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_100_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_101',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_101_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_102',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_102_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_jmp_to_subroutine_103',
        "command": 'jmp_to_subroutine',
        "args": [0xc846],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_pause_104',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_run_dialog_105',
        "command": 'run_dialog',
        "args": [3897, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_jmp_to_subroutine_106',
        "command": 'jmp_to_subroutine',
        "args": [0xc851],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_action_queue_async_107',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_async_107_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_107_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_107_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_107_SUBSCRIPT_end_loop_3',
                "command": 'end_loop',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_108',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_108_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_109',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_109_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [18, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_110',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_110_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_111',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_111_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_remember_last_object_112',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_pause_113',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_action_queue_async_114',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_async_114_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_114_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_114_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3794_action_queue_async_114_SUBSCRIPT_pause_1']
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_114_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_114_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_114_SUBSCRIPT_jmp_if_mario_in_air_5',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3794_action_queue_async_114_SUBSCRIPT_pause_4']
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_pause_115',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_116',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_116_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_116_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_116_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_116_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_116_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_116_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_116_SUBSCRIPT_shift_northwest_pixels_6',
                "command": 'shift_northwest_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_116_SUBSCRIPT_transfer_to_xyzf_7',
                "command": 'transfer_to_xyzf',
                "args": [7, 65, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_117',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_117_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_117_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_117_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_117_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_117_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_117_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_117_SUBSCRIPT_shift_southeast_pixels_6',
                "command": 'shift_southeast_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_117_SUBSCRIPT_transfer_to_xyzf_7',
                "command": 'transfer_to_xyzf',
                "args": [7, 69, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_118',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_118_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_118_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_118_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_118_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_118_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_118_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_118_SUBSCRIPT_shift_north_pixels_6',
                "command": 'shift_north_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_118_SUBSCRIPT_transfer_to_xyzf_7',
                "command": 'transfer_to_xyzf',
                "args": [7, 67, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_119',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_119_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_119_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_119_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_119_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_119_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_119_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_119_SUBSCRIPT_shift_east_pixels_6',
                "command": 'shift_east_pixels',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_119_SUBSCRIPT_transfer_to_xyzf_7',
                "command": 'transfer_to_xyzf',
                "args": [9, 69, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_remember_last_object_120',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_pause_121',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_action_queue_async_122',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_async_122_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_122_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_122_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_122_SUBSCRIPT_end_loop_3',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_122_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_jmp_to_subroutine_123',
        "command": 'jmp_to_subroutine',
        "args": [0xc846],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_pause_124',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_run_dialog_125',
        "command": 'run_dialog',
        "args": [3898, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_jmp_to_subroutine_126',
        "command": 'jmp_to_subroutine',
        "args": [0xc851],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_pause_127',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_unfreeze_camera_128',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_set_bit_129',
        "command": 'set_bit',
        "args": [0x7043, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_130',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_131',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_132',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_132_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_132_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_132_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_133',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_133_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_133_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_133_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_133_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_133_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [152]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_133_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_133_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_133_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_133_SUBSCRIPT_floating_off_8',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_133_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_pause_134',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_pause_action_script_135',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_136',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_136_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_136_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_136_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_136_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_136_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_137',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_137_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_137_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_137_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_137_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_138',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_138_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_138_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_138_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_138_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_138_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_138_SUBSCRIPT_shift_z_down_pixels_5',
                "command": 'shift_z_down_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_139',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_139_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_139_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_139_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_139_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_139_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_139_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_139_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_139_SUBSCRIPT_shift_north_pixels_7',
                "command": 'shift_north_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_139_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3794_pause_140',
        "command": 'pause',
        "args": [55],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_initiate_battle_mask_141',
        "command": 'initiate_battle_mask',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_enter_area_142',
        "command": 'enter_area',
        "args": [Rooms._496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE, RadialDirections.NORTHEAST, 4, 51, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_ret_143',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_set_bit_144',
        "command": 'set_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_145',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_clear_bit_146',
        "command": 'clear_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_set_action_script_sync_147',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 242],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_ret_148',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_set_bit_149',
        "command": 'set_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_clear_bit_150',
        "command": 'clear_bit',
        "args": [0x7043, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_151',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_clear_bit_152',
        "command": 'clear_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_set_action_script_sync_153',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 987],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3794_ret_154',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
