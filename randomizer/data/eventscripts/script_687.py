from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_687_pause_0',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_run_dialog_1',
        "command": 'run_dialog',
        "args": [2155, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_pause_action_script_2',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_pause_action_script_3',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_pause_action_script_4',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_pause_action_script_5',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_pause_action_script_6',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_pause_action_script_7',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_sync_8_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_687_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_sync_9_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_687_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_sync_10_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_10_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_687_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_sync_11_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_687_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_sync_12_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_687_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_sync_13_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_687_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_sync_14_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_687_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_sync_15_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_15_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [13, 41, 0]
            },
        ]
    },
    {
        "identifier": 'EVENT_687_remember_last_object_16',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_pause_17',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_play_sound_18',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_apply_tile_mod_19',
        "command": 'apply_tile_mod',
        "args": [Rooms._005_MARRYMORE_OUTSIDE_DURING_BOOSTER, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_sync_20_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_20_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [18, 63, 12, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_20_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_20_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_687_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_sync_21_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_21_SUBSCRIPT_sequence_looping_off_1',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_21_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [19, 64, 12, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_21_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_21_SUBSCRIPT_set_object_memory_bits_4',
                "command": 'set_object_memory_bits',
                "args": [0x0e, bits=[0]]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_21_SUBSCRIPT_clear_solidity_bits_5',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
        ]
    },
    {
        "identifier": 'EVENT_687_remember_last_object_22',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_pause_23',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_action_queue_sync_24',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_sync_24_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_24_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_24_SUBSCRIPT_floating_on_2',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_24_SUBSCRIPT_sequence_looping_off_3',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_24_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_24_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_24_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_24_SUBSCRIPT_set_priority_7',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_24_SUBSCRIPT_shift_southwest_steps_8',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_24_SUBSCRIPT_set_solidity_bits_9',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_24_SUBSCRIPT_floating_on_10',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_24_SUBSCRIPT_shift_southwest_steps_11',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_24_SUBSCRIPT_play_sound_12',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_24_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_24_SUBSCRIPT_jump_to_height_silent_14',
                "command": 'jump_to_height_silent',
                "args": [80]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_24_SUBSCRIPT_walk_1_step_southwest_15',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_24_SUBSCRIPT_set_solidity_bits_16',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            },
        ]
    },
    {
        "identifier": 'EVENT_687_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_sync_25_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_25_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_687_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_sync_26_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_26_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_26_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [18, 63, 12, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_26_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 4, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_26_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_26_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_26_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_26_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_26_SUBSCRIPT_shift_southwest_pixels_8',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_687_pause_27',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_action_queue_sync_28',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_sync_28_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_687_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_sync_29_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_687_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_sync_30_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_30_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_30_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_687_action_queue_sync_31',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_sync_31_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_31_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_31_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_31_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_31_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_31_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_31_SUBSCRIPT_set_solidity_bits_6',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_31_SUBSCRIPT_floating_on_7',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_31_SUBSCRIPT_shift_southeast_steps_8',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_31_SUBSCRIPT_shift_southwest_steps_9',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_687_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_sync_32_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_32_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_32_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_32_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_32_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_32_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_32_SUBSCRIPT_set_solidity_bits_6',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_32_SUBSCRIPT_floating_on_7',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_32_SUBSCRIPT_shift_northwest_steps_8',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_32_SUBSCRIPT_shift_southwest_steps_9',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_687_action_queue_sync_33',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_sync_33_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [16, 72]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_33_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_687_action_queue_sync_34',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_sync_34_SUBSCRIPT_walk_1_step_northeast_0',
                "command": 'walk_1_step_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_687_remember_last_object_35',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_sync_36_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0e, bits=[]]
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_36_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            },
        ]
    },
    {
        "identifier": 'EVENT_687_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_sync_37_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_687_action_queue_async_38',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_async_38_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_687_pause_39',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_set_action_script_sync_40',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 628],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_set_action_script_sync_41',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 628],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_set_action_script_sync_42',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 628],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_set_action_script_sync_43',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 628],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_set_action_script_sync_44',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 628],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_set_action_script_sync_45',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 628],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_pause_46',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_run_dialog_47',
        "command": 'run_dialog',
        "args": [2122, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_pause_48',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_action_queue_sync_49',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_687_action_queue_sync_49_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_687_action_queue_sync_49_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_687_pause_50',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_play_sound_51',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_apply_tile_mod_52',
        "command": 'apply_tile_mod',
        "args": [Rooms._005_MARRYMORE_OUTSIDE_DURING_BOOSTER, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_pause_53',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_run_event_as_subroutine_54',
        "command": 'run_event_as_subroutine',
        "args": [276],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_set_action_script_async_55',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_7, 625],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_set_action_script_async_56',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_8, 625],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_set_action_script_async_57',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_0, 626],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_set_action_script_async_58',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_1, 626],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_set_action_script_async_59',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_2, 627],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_set_action_script_sync_60',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_set_action_script_sync_61',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 113],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_set_action_script_sync_62',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_set_action_script_sync_63',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_set_action_script_sync_64',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_set_action_script_sync_65',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 376],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_set_action_script_sync_66',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 376],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_remove_from_level_67',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_11, Rooms._005_MARRYMORE_OUTSIDE_DURING_BOOSTER],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_set_bit_68',
        "command": 'set_bit',
        "args": [0x704c, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_687_ret_69',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
