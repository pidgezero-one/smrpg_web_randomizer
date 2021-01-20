from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3627_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7042, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_1',
        "command": 'set',
        "args": [0x70df, 49],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_apply_solidity_mod_2',
        "command": 'apply_solidity_mod',
        "args": [Rooms._438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_apply_solidity_mod_3',
        "command": 'apply_solidity_mod',
        "args": [Rooms._438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA, 1, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_apply_solidity_mod_4',
        "command": 'apply_solidity_mod',
        "args": [Rooms._061_NIMBUS_LAND_OUTSIDE_DURING_VALENTINA_RIGHT_BEFORE_FIGHT, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 803],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_6',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 805],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 804],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_async_8',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_5, 806],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 376],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 376],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_11',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 376],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 376],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_14_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_14_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_14_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_sync_15_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_15_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_15_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [140]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_15_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_15_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [12]
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_fade_in_from_black_sync_16',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_script_until_effect_done_17',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_18_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [10]
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_19',
        "command": 'pause',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_run_dialog_20',
        "command": 'run_dialog',
        "args": [2384, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_21',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_sync_22_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_22_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_sync_23_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_23_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_23_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_23_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_23_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_23_SUBSCRIPT_fixed_f_coord_off_5',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_23_SUBSCRIPT_face_southwest_6',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_action_queue_sync_24',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_sync_24_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_24_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_24_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_24_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_24_SUBSCRIPT_walk_1_step_southeast_4',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_24_SUBSCRIPT_shadow_off_5',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_24_SUBSCRIPT_walk_1_step_southeast_6',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_24_SUBSCRIPT_fixed_f_coord_off_7',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_24_SUBSCRIPT_face_southwest_8',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_sync_25_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [90]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_25_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_25_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [20, 36, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_25_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_25_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_25_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_remember_last_object_26',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_27',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_run_dialog_28',
        "command": 'run_dialog',
        "args": [2385, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_action_script_29',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_action_script_30',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_action_script_31',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_action_script_32',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_33',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_34',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 628],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_async_35',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_2, 628],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_36',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_37',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_38',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_39',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 628],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_40',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_async_41',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_3, 628],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_42',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_43',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_44',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_async_45',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_4, 628],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_46',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_47',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_10, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_sync_48_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_48_SUBSCRIPT_walk_1_step_northwest_1',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_48_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_action_queue_sync_49',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_sync_49_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_49_SUBSCRIPT_walk_1_step_northwest_1',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_49_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_remember_last_object_50',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_51',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_run_dialog_52',
        "command": 'run_dialog',
        "args": [2386, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_53',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_54',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 376],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_55',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 626],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_56',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 376],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_57',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 376],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_58',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 376],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_59',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_action_script_60',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_action_script_61',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_action_script_62',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_action_script_63',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_64',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_65',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 628],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_66',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 628],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_67',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 628],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_68',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 628],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_async_69',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_5, 628],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_run_dialog_70',
        "command": 'run_dialog',
        "args": [2387, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_71',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_72',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_72_SUBSCRIPT_walk_1_step_southwest_0',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_72_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_72_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_73',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_run_dialog_74',
        "command": 'run_dialog',
        "args": [2388, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_75',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_76',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_76_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_77',
        "command": 'pause',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_78',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_78_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_79',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_run_dialog_80',
        "command": 'run_dialog',
        "args": [2389, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_81',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_82',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 376],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_83',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 626],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_84',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 376],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_85',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 376],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_86',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 376],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_87',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_action_script_88',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_action_script_89',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_action_script_90',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_action_script_91',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_92',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_93',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 628],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_94',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 628],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_95',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 628],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_96',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 628],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_async_97',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_4, 628],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_98',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_98_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_99',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_run_dialog_100',
        "command": 'run_dialog',
        "args": [2390, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_101',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_102',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_102_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_102_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_102_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_102_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_102_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_102_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_102_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_102_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_103',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_run_dialog_104',
        "command": 'run_dialog',
        "args": [2391, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_105',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_run_dialog_106',
        "command": 'run_dialog',
        "args": [2392, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_107',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_sync_108',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [24, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [20, 36, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_shadow_off_2',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_walk_1_step_southwest_4',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_shift_southwest_pixels_7',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_shift_southwest_pixels_9',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_shift_southwest_pixels_12',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_shift_southwest_pixels_14',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_shift_southwest_pixels_17',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_shift_southwest_pixels_19',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_set_sprite_sequence_20',
                "command": 'set_sprite_sequence',
                "args": [16, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_shift_southwest_pixels_21',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_set_sprite_sequence_22',
                "command": 'set_sprite_sequence',
                "args": [17, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_shift_southwest_pixels_23',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_set_sprite_sequence_24',
                "command": 'set_sprite_sequence',
                "args": [18, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_shift_southwest_pixels_25',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_set_sprite_sequence_26',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_shift_southwest_pixels_27',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_set_animation_speed_28',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_start_loop_n_times_29',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_set_sprite_sequence_30',
                "command": 'set_sprite_sequence',
                "args": [20, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_shift_southwest_pixels_31',
                "command": 'shift_southwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_set_sprite_sequence_32',
                "command": 'set_sprite_sequence',
                "args": [21, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_shift_southwest_pixels_33',
                "command": 'shift_southwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_end_loop_34',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_start_loop_n_times_35',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_set_sprite_sequence_36',
                "command": 'set_sprite_sequence',
                "args": [22, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_pause_37',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_set_sprite_sequence_38',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_pause_39',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_set_sprite_sequence_40',
                "command": 'set_sprite_sequence',
                "args": [24, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_pause_41',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_end_loop_42',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_pause_43',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_set_sprite_sequence_44',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_108_SUBSCRIPT_shadow_off_45',
                "command": 'shadow_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_action_queue_sync_109',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_sync_109_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [180]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_109_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_109_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_109_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_remember_last_object_110',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_111',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_run_dialog_112',
        "command": 'run_dialog',
        "args": [2406, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_113',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_114',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_114_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_114_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_115',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_run_dialog_116',
        "command": 'run_dialog',
        "args": [2393, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_117',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_118',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_118_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_118_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_118_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_119',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_120',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_120_SUBSCRIPT_walk_1_step_northeast_0',
                "command": 'walk_1_step_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_121',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_run_dialog_122',
        "command": 'run_dialog',
        "args": [2394, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_123',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_124',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_124_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_124_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_124_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_125',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_126',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_126_SUBSCRIPT_walk_1_step_northeast_0',
                "command": 'walk_1_step_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_127',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_run_dialog_128',
        "command": 'run_dialog',
        "args": [2395, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_129',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_130',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_130_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_130_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_130_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_131',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_132',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_132_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [25, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_133',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_134',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_134_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_134_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_135',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_run_dialog_136',
        "command": 'run_dialog',
        "args": [2396, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_137',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_138',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_138_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_138_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_138_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_138_SUBSCRIPT_shift_northwest_pixels_3',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_139',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_140',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_140_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_140_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_140_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_140_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [25, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_140_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_140_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_140_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_141',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_142',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_142_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_142_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_142_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_142_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_142_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_142_SUBSCRIPT_shift_southeast_pixels_5',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_143',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_run_dialog_144',
        "command": 'run_dialog',
        "args": [2397, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_145',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_146',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_146_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_146_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_146_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_146_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_147',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_run_dialog_148',
        "command": 'run_dialog',
        "args": [2398, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_149',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_150',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_150_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_151',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_run_dialog_152',
        "command": 'run_dialog',
        "args": [2399, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_153',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_153_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_153_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_153_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_154',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_run_dialog_155',
        "command": 'run_dialog',
        "args": [2400, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_156',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_157',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_157_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_157_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_run_dialog_158',
        "command": 'run_dialog',
        "args": [2401, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_159',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_160',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_160_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_run_dialog_161',
        "command": 'run_dialog',
        "args": [2402, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_162',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_163',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_163_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_163_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_163_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_163_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_164',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_run_dialog_165',
        "command": 'run_dialog',
        "args": [2403, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_sync_166',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_sync_166_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_166_SUBSCRIPT_add_z_coord_1_step_1',
                "command": 'add_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_166_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_166_SUBSCRIPT_shift_z_down_pixels_3',
                "command": 'shift_z_down_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_166_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_166_SUBSCRIPT_shift_z_down_pixels_5',
                "command": 'shift_z_down_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_166_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_166_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_166_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_166_SUBSCRIPT_shift_northwest_steps_9',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_166_SUBSCRIPT_shift_northeast_steps_10',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_166_SUBSCRIPT_visibility_off_11',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_action_queue_sync_167',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [22, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [24, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_start_loop_n_times_7',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [22, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [24, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_end_loop_14',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_reset_properties_15',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_set_animation_speed_16',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_set_animation_speed_17',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_walk_1_step_northeast_19',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_set_sprite_sequence_20',
                "command": 'set_sprite_sequence',
                "args": [29, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_shift_northeast_pixels_21',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_set_sprite_sequence_23',
                "command": 'set_sprite_sequence',
                "args": [30, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_shift_northeast_pixels_24',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_pause_25',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_set_sprite_sequence_26',
                "command": 'set_sprite_sequence',
                "args": [31, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_set_animation_speed_27',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_shift_northeast_pixels_28',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_set_animation_speed_29',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_set_sprite_sequence_30',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_walk_1_step_northeast_31',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_167_SUBSCRIPT_visibility_off_32',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_168',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_169',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 810],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_170',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 813],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_171',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_172',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 811],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_sync_173',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_sync_173_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_173_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_173_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_173_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_173_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_174',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_175',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 812],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_176',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 815],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_177',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 626],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_178',
        "command": 'pause',
        "args": [40],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_sync_179',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_sync_179_SUBSCRIPT_shift_southeast_steps_0',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_179_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_179_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_action_queue_sync_180',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_sync_180_SUBSCRIPT_shadow_on_0',
                "command": 'shadow_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_180_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_180_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_sync_180_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_181',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_181_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_181_SUBSCRIPT_shift_west_pixels_1',
                "command": 'shift_west_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_181_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_action_queue_sync_182',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_sync_182_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_183',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_183_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_183_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [13, 55, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_183_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_183_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_183_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_183_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_183_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_183_SUBSCRIPT_walk_1_step_northwest_7',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_183_SUBSCRIPT_face_southeast_8',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_run_dialog_184',
        "command": 'run_dialog',
        "args": [2404, AreaObjects.NPC_11, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_pause_185',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_186',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_186_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_186_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_186_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [24, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_186_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_186_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_186_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_186_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_187',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_run_dialog_188',
        "command": 'run_dialog',
        "args": [2405, AreaObjects.NPC_11, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_189',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_189_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_189_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_189_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_189_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_189_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_189_SUBSCRIPT_shift_southeast_pixels_5',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_189_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_pause_190',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_action_queue_async_191',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3627_action_queue_async_191_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_191_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3627_action_queue_async_191_SUBSCRIPT_face_south_2',
                "command": 'face_south',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3627_set_action_script_sync_192',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_bit_193',
        "command": 'set_bit',
        "args": [0x705e, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_set_bit_194',
        "command": 'set_bit',
        "args": [0x7070, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3627_ret_195',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
