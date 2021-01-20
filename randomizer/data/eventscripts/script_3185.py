from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3185_set_0',
        "command": 'set',
        "args": [0x70a7, 135],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_store_7000_item_quantity_to_70A7_1',
        "command": 'store_7000_item_quantity_to_70A7',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_3185_set_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3185_action_queue_sync_4_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3185_action_queue_sync_4_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3185_action_queue_sync_4_SUBSCRIPT_face_mario_2',
                "command": 'face_mario',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3185_unsync_dialog_5',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_close_dialog_6',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_run_dialog_8',
        "command": 'run_dialog',
        "args": [1634, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_set_9',
        "command": 'set',
        "args": [0x70ae, 20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_set_action_script_async_10',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_jmp_11',
        "command": 'jmp',
        "args": ['EVENT_3185_pause_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_run_dialog_12',
        "command": 'run_dialog',
        "args": [1639, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_pause_13',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3185_action_queue_sync_14_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [72]
            }
        ]
    },
    {
        "identifier": 'EVENT_3185_jmp_if_bit_clear_15',
        "command": 'jmp_if_bit_clear',
        "args": [0x7058, 3, 'EVENT_3185_run_dialog_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_run_dialog_16',
        "command": 'run_dialog',
        "args": [1635, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3185_action_queue_sync_17_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3185_action_queue_sync_17_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3185_action_queue_sync_17_SUBSCRIPT_set_bit_2',
                "command": 'set_bit',
                "args": [0x7043, 4]
            },
            {
                "identifier": 'EVENT_3185_action_queue_sync_17_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3185_action_queue_sync_17_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3185_action_queue_sync_17_SUBSCRIPT_walk_1_step_southwest_5',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3185_action_queue_sync_17_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3185_action_queue_sync_17_SUBSCRIPT_shift_southwest_steps_7',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3185_action_queue_sync_17_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3185_action_queue_sync_17_SUBSCRIPT_fixed_f_coord_off_9',
                "command": 'fixed_f_coord_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3185_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3185_action_queue_sync_18_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3185_action_queue_sync_18_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3185_action_queue_sync_18_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3185_action_queue_sync_18_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [8, 20]
            },
            {
                "identifier": 'EVENT_3185_action_queue_sync_18_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3185_action_queue_sync_18_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3185_jmp_if_bit_clear_19',
        "command": 'jmp_if_bit_clear',
        "args": [0x7058, 3, 'EVENT_3185_run_dialog_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_run_dialog_20',
        "command": 'run_dialog',
        "args": [1636, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_pause_21',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_close_dialog_22',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_pause_23',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_store_02_to_0248_24',
        "command": 'store_02_to_0248',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_set_bit_25',
        "command": 'set_bit',
        "args": [0x707c, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_pause_26',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_apply_tile_mod_27',
        "command": 'apply_tile_mod',
        "args": [Rooms._272_MOLEVILLE_MINES_AREA_11_BOMBED_ROOM_WSINGING_MOLES, 32, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_apply_solidity_mod_28',
        "command": 'apply_solidity_mod',
        "args": [Rooms._272_MOLEVILLE_MINES_AREA_11_BOMBED_ROOM_WSINGING_MOLES, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_pause_29',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_clear_bit_30',
        "command": 'clear_bit',
        "args": [0x707c, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_store_00_to_0248_31',
        "command": 'store_00_to_0248',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_pause_32',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_jmp_if_bit_clear_33',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 5, 'EVENT_3185_action_queue_sync_41'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_jmp_34',
        "command": 'jmp',
        "args": ['EVENT_3185_action_queue_sync_41'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_pause_35',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3185_action_queue_sync_36_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3185_action_queue_sync_36_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3185_action_queue_sync_36_SUBSCRIPT_face_mario_2',
                "command": 'face_mario',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3185_run_dialog_37',
        "command": 'run_dialog',
        "args": [1637, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_action_queue_async_38',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3185_action_queue_async_38_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3185_action_queue_async_38_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3185_action_queue_async_38_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3185_action_queue_async_38_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3185_run_dialog_39',
        "command": 'run_dialog',
        "args": [1685, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_run_dialog_40',
        "command": 'run_dialog',
        "args": [1684, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_action_queue_sync_41',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3185_action_queue_sync_41_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3185_action_queue_sync_41_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3185_action_queue_sync_41_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3185_action_queue_sync_41_SUBSCRIPT_walk_1_step_northwest_3',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3185_action_queue_sync_41_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3185_action_queue_sync_41_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3185_set_42',
        "command": 'set',
        "args": [0x70ae, 20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_set_action_script_sync_43',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_set_action_script_sync_44',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_action_queue_async_45',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3185_action_queue_async_45_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3185_action_queue_async_45_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3185_action_queue_async_45_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3185_action_queue_async_45_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3185_action_queue_async_45_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [72]
            },
            {
                "identifier": 'EVENT_3185_action_queue_async_45_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3185_action_queue_async_45_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_3185_action_queue_async_45_SUBSCRIPT_walk_to_xy_coords_7',
                "command": 'walk_to_xy_coords',
                "args": [6, 24]
            },
            {
                "identifier": 'EVENT_3185_action_queue_async_45_SUBSCRIPT_walk_to_xy_coords_8',
                "command": 'walk_to_xy_coords',
                "args": [4, 20]
            },
            {
                "identifier": 'EVENT_3185_action_queue_async_45_SUBSCRIPT_shift_southwest_steps_9',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3185_action_queue_async_45_SUBSCRIPT_db_10',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_3185_action_queue_async_45_SUBSCRIPT_visibility_off_11',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3185_set_bit_46',
        "command": 'set_bit',
        "args": [0x7056, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_remove_one_from_inventory_47',
        "command": 'remove_one_from_inventory',
        "args": [items.BambinoBomb],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_ret_48',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_stop_sound_49',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_stop_sound_50',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_stop_sound_51',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_stop_sound_52',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_stop_sound_53',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_stop_sound_54',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_stop_sound_55',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_stop_sound_56',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_stop_sound_57',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3185_ret_58',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
