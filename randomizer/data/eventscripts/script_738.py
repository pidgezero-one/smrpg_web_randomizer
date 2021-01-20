from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_738_set_action_script_sync_0',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.LAYER_3, 808],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_set_temp_action_script_sync_1',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_0, 803],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_set_temp_action_script_sync_2',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_2, 807],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_set_temp_action_script_sync_3',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_6, 803],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_4_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_4_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_4_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [6]
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_async_5_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [11, 59, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_5_SUBSCRIPT_floating_off_1',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_async_5_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_async_5_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_fade_in_from_black_sync_duration_6',
        "command": 'fade_in_from_black_sync_duration',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_7_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_7_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [5]
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_8_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_8_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_8_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_8_SUBSCRIPT_walk_1_step_northeast_4',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_8_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_8_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_8_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_8_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_8_SUBSCRIPT_shift_northeast_pixels_9',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_9_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_9_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_9_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_9_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_9_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_9_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_9_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_9_SUBSCRIPT_fixed_f_coord_off_7',
                "command": 'fixed_f_coord_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_async_10_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_10_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_pause_11',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_remember_last_object_12',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_13_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_13_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_13_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_13_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_13_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_13_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_13_SUBSCRIPT_face_northeast_6',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_13_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_14_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_14_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_14_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_14_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_14_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_14_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_15_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_15_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_15_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_15_SUBSCRIPT_walk_1_step_southeast_3',
                "command": 'walk_1_step_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_16_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_16_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_16_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_16_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_16_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_17_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_17_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_17_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_17_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_738_remember_last_object_18',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_19',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_set_action_script_sync_20',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 880],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_21',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_action_script_22',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_async_23_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_async_23_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_23_SUBSCRIPT_floating_on_2',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_async_23_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_23_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x07, 0x62]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_23_SUBSCRIPT_floating_off_5',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_async_23_SUBSCRIPT_clear_solidity_bits_6',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
        ]
    },
    {
        "identifier": 'EVENT_738_pause_24',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_25_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_25_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 880],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_27',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_28',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_action_script_29',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_action_queue_async_30',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_async_30_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_async_30_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_30_SUBSCRIPT_floating_on_2',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_async_30_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_30_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x07, 0x85]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_30_SUBSCRIPT_floating_off_5',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_async_30_SUBSCRIPT_clear_solidity_bits_6',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
        ]
    },
    {
        "identifier": 'EVENT_738_pause_31',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_32_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_32_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_set_action_script_sync_33',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 880],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_34',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_35',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_action_script_36',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_action_queue_async_37',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_async_37_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_async_37_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_37_SUBSCRIPT_floating_on_2',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_async_37_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_37_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x07, 0xa8]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_37_SUBSCRIPT_floating_off_5',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_async_37_SUBSCRIPT_clear_solidity_bits_6',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
        ]
    },
    {
        "identifier": 'EVENT_738_pause_38',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_39',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_face_northeast_5',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_face_southeast_7',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_face_northwest_9',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_face_northeast_11',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_face_southwest_13',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_face_northeast_15',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_face_southeast_17',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_face_northwest_19',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_face_northeast_21',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_face_southwest_23',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_face_northwest_25',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_pause_26',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_face_northeast_27',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_pause_28',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_face_southwest_29',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_pause_30',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_face_southeast_31',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_pause_32',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_face_northeast_33',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_set_animation_speed_34',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_fixed_f_coord_on_35',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_shift_northeast_pixels_36',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_start_loop_n_times_37',
                "command": 'start_loop_n_times',
                "args": [9]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_shift_southwest_pixels_38',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_shift_northeast_pixels_39',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_39_SUBSCRIPT_end_loop_40',
                "command": 'end_loop',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_set_action_script_sync_40',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 880],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_41',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_42',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_close_dialog_43',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_set_action_script_sync_44',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 880],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_45',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_46',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_close_dialog_47',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_set_action_script_sync_48',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 880],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_49',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_set_action_script_sync_50',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 880],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_51',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_set_action_script_sync_52',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 880],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_53',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_54',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_close_dialog_55',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_56',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_57',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_close_dialog_58',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_remember_last_object_59',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_action_queue_async_60',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_async_60_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_async_60_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_60_SUBSCRIPT_sequence_playback_off_2',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_async_60_SUBSCRIPT_add_z_coord_1_step_3',
                "command": 'add_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_async_60_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_60_SUBSCRIPT_shift_z_up_pixels_5',
                "command": 'shift_z_up_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_60_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_60_SUBSCRIPT_shift_z_up_pixels_7',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_60_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_60_SUBSCRIPT_dec_z_coord_1_step_9',
                "command": 'dec_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_async_60_SUBSCRIPT_shift_z_down_pixels_10',
                "command": 'shift_z_down_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_60_SUBSCRIPT_play_sound_11',
                "command": 'play_sound',
                "args": [Sounds._020_LIGHTING_BOLT, 4]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_60_SUBSCRIPT_sequence_playback_on_12',
                "command": 'sequence_playback_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_pause_action_script_61',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_action_script_62',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_action_script_63',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_action_script_64',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_action_script_65',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_66',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_66_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_66_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_66_SUBSCRIPT_floating_on_2',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_66_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [112]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_66_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_66_SUBSCRIPT_sequence_looping_off_5',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_66_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_66_SUBSCRIPT_shift_northeast_pixels_7',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_67',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_67_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_67_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_67_SUBSCRIPT_floating_on_2',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_67_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [112]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_67_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_67_SUBSCRIPT_sequence_looping_off_5',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_67_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_67_SUBSCRIPT_shift_southwest_pixels_7',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_68',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_68_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_68_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_68_SUBSCRIPT_floating_on_2',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_68_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [112]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_68_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_68_SUBSCRIPT_sequence_looping_off_5',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_68_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_68_SUBSCRIPT_shift_southeast_pixels_7',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_69',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_69_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_69_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_69_SUBSCRIPT_floating_on_2',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_69_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [112]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_69_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_69_SUBSCRIPT_sequence_looping_off_5',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_69_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_69_SUBSCRIPT_shift_south_steps_7',
                "command": 'shift_south_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_69_SUBSCRIPT_shift_south_pixels_8',
                "command": 'shift_south_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_70',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_70_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_70_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_70_SUBSCRIPT_floating_on_2',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_70_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [112]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_70_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_70_SUBSCRIPT_sequence_looping_off_5',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_70_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_70_SUBSCRIPT_shift_northwest_steps_7',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_70_SUBSCRIPT_shift_northwest_pixels_8',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_738_remember_last_object_71',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_72',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_action_queue_async_73',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_async_73_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_async_73_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_73_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_async_73_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_73_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_async_73_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_73_SUBSCRIPT_face_northeast_6',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_pause_74',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_75',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_freeze_camera_76',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_77',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_77_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_77_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_77_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_77_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_77_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_77_SUBSCRIPT_sequence_looping_on_5',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_77_SUBSCRIPT_shift_south_pixels_6',
                "command": 'shift_south_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_77_SUBSCRIPT_sequence_looping_off_7',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_77_SUBSCRIPT_fixed_f_coord_off_8',
                "command": 'fixed_f_coord_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_78',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_78_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_78_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_79',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_79_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_79_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_79_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_80',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_80_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_80_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_80_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_81',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_81_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_81_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_81_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_82',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_82_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_82_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_82_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_83',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_83_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_83_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_83_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [160]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_83_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_83_SUBSCRIPT_floating_on_4',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_83_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_83_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [11]
            },
        ]
    },
    {
        "identifier": 'EVENT_738_remember_last_object_84',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_action_queue_async_85',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_async_85_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_85_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_85_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_85_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_85_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_85_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_85_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_pause_86',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_87',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_87_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_87_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_87_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_88',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_88_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_88_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_88_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_88_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_89',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_89_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_89_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_90',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_90_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_90_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_90_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_90_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_91',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_91_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_91_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_pause_92',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_action_queue_async_93',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_async_93_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_async_93_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_93_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_pause_94',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_action_queue_async_95',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_async_95_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_async_95_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_95_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_pause_96',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_pause_97',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_action_queue_async_98',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_async_98_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_async_98_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_738_action_queue_async_98_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_pause_99',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_100',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_100_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_100_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_100_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [252, 254, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_100_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_100_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=4, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_100_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_100_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [11, inc_sprite=4, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_100_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_100_SUBSCRIPT_end_loop_8',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_100_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=4, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_101',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_101_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_101_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_101_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_102',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_102_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_102_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_action_queue_sync_103',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_sync_103_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_103_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_738_action_queue_sync_103_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_remember_last_object_104',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_action_queue_async_105',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_738_action_queue_async_105_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_738_action_queue_async_105_SUBSCRIPT_sequence_playback_off_1',
                "command": 'sequence_playback_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_738_clear_bit_106',
        "command": 'clear_bit',
        "args": [0x7090, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_start_battle_107',
        "command": 'start_battle',
        "args": [0x00ab, 24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_set_108',
        "command": 'set',
        "args": [0x70a9, 29],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_set_bit_109',
        "command": 'set_bit',
        "args": [0x704a, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_run_event_as_subroutine_110',
        "command": 'run_event_as_subroutine',
        "args": [1010],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_restore_all_hp_111',
        "command": 'restore_all_hp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_restore_all_fp_112',
        "command": 'restore_all_fp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_run_event_as_subroutine_113',
        "command": 'run_event_as_subroutine',
        "args": [3660],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_jmp_if_bit_set_114',
        "command": 'jmp_if_bit_set',
        "args": [0x7092, 7, 'EVENT_738_summon_to_level_117'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_jmp_to_event_115',
        "command": 'jmp_to_event',
        "args": [3658],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_ret_116',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_summon_to_level_117',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_jmp_118',
        "command": 'jmp',
        "args": ['EVENT_738_jmp_to_event_115'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_119',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_120',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_121',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_122',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_123',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_124',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_125',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_126',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_127',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_128',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_129',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_130',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_131',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_132',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_133',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_134',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_135',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_136',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_137',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_138',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_139',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_140',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_141',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_142',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_143',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_144',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_145',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_146',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_147',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_148',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_149',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_150',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_151',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_152',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_153',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_154',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_155',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_156',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_157',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_158',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_159',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_160',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_161',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_162',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_163',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_164',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_165',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_166',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_167',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_168',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_169',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_170',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_171',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_172',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_173',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_174',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_175',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_176',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_738_stop_sound_177',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
]
