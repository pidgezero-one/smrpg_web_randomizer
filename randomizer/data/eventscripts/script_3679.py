from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3679_jmp_if_object_not_in_level_0',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_0, Rooms._409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, 'EVENT_3679_jmp_if_object_not_in_level_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3679_action_queue_async_1_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3679_jmp_if_object_not_in_level_2',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_6, Rooms._409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, 'EVENT_3679_jmp_if_object_not_in_level_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_apply_solidity_mod_3',
        "command": 'apply_solidity_mod',
        "args": [Rooms._409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_jmp_if_object_not_in_level_4',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, 'EVENT_3585_fade_in_from_black_async_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3679_action_queue_sync_5_SUBSCRIPT_jmp_if_bit_set_0',
                "command": 'jmp_if_bit_set',
                "args": [0x709c, 5, 'EVENT_3679_action_queue_sync_5_SUBSCRIPT_transfer_to_xyzf_3']
            },
            {
                "identifier": 'EVENT_3679_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3679_action_queue_sync_5_SUBSCRIPT_jmp_2',
                "command": 'jmp',
                "args": ['EVENT_3679_remember_last_object_6']
            },
            {
                "identifier": 'EVENT_3679_action_queue_sync_5_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [20, 49, 10, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3679_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3679_remember_last_object_6',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_jmp_if_bit_clear_7',
        "command": 'jmp_if_bit_clear',
        "args": [0x709c, 5, 'EVENT_3679_jmp_if_bit_clear_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 978],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_jmp_if_bit_clear_9',
        "command": 'jmp_if_bit_clear',
        "args": [0x705f, 5, 'EVENT_3679_fade_in_from_black_async_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_jmp_if_object_not_in_level_10',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_0, Rooms._409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, 'EVENT_3679_fade_in_from_black_async_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3679_action_queue_async_11_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [17, 56, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3679_fade_in_from_black_async_12',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x709c, 5, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3679_action_queue_sync_14_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3679_action_queue_sync_14_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3679_pause_15',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_run_dialog_16',
        "command": 'run_dialog',
        "args": [3601, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_pause_17',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3679_action_queue_async_18_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3679_action_queue_async_18_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3679_pause_19',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_run_dialog_20',
        "command": 'run_dialog',
        "args": [3602, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3679_action_queue_async_21_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3679_action_queue_async_21_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3679_action_queue_async_21_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3679_action_queue_async_21_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3679_action_queue_async_21_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3679_action_queue_async_21_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_3679_action_queue_async_21_SUBSCRIPT_db_6',
                "command": 'db',
                "args": [0x24, 0x80, 0x00, 0xc0, 0xff]
            },
            {
                "identifier": 'EVENT_3679_action_queue_async_21_SUBSCRIPT_shift_z_down_steps_7',
                "command": 'shift_z_down_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3679_action_queue_async_21_SUBSCRIPT_bpl_26_27_28_8',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_3679_action_queue_async_21_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3679_action_queue_async_21_SUBSCRIPT_fixed_f_coord_on_10',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3679_action_queue_async_21_SUBSCRIPT_start_loop_n_times_11',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3679_action_queue_async_21_SUBSCRIPT_shift_southwest_pixels_12',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3679_action_queue_async_21_SUBSCRIPT_play_sound_13',
                "command": 'play_sound',
                "args": [Sounds._005_BLOCK_SWITCH, 4]
            },
            {
                "identifier": 'EVENT_3679_action_queue_async_21_SUBSCRIPT_shift_northeast_pixels_14',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3679_action_queue_async_21_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3679_action_queue_async_21_SUBSCRIPT_end_loop_16',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3679_action_queue_async_21_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3679_action_queue_async_21_SUBSCRIPT_fixed_f_coord_off_18',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3679_action_queue_async_21_SUBSCRIPT_face_southwest_19',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3679_action_queue_async_21_SUBSCRIPT_set_sprite_sequence_20',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3679_run_dialog_22',
        "command": 'run_dialog',
        "args": [3603, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3679_action_queue_sync_23_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3679_action_queue_sync_23_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3679_action_queue_sync_24',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3679_action_queue_sync_24_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3679_pause_25',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_run_dialog_26',
        "command": 'run_dialog',
        "args": [3604, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_remember_last_object_27',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_set_action_script_sync_28',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 978],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_set_bit_29',
        "command": 'set_bit',
        "args": [0x709c, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_set_bit_30',
        "command": 'set_bit',
        "args": [0x7049, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_run_event_as_subroutine_31',
        "command": 'run_event_as_subroutine',
        "args": [276],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3679_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3679_action_queue_async_32_SUBSCRIPT_face_south_0',
                "command": 'face_south',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3679_ret_33',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
