from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1358_remove_from_level_0',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._202_BOOSTER_TOWER_ENTRANCE]
    },
    {
        "identifier": 'EVENT_1358_remove_from_level_1',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM]
    },
    {
        "identifier": 'EVENT_1358_remove_from_level_2',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM]
    },
    {
        "identifier": 'EVENT_1358_remove_from_level_3',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_8, Rooms._037_BOOSTER_TOWER_4F_3LEVEL_ROOM_WJUMPING_SPOOKUMS]
    },
    {
        "identifier": 'EVENT_1358_remove_from_level_4',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM]
    },
    {
        "identifier": 'EVENT_1358_move_script_to_background_thread_2_5',
        "command": 'move_script_to_background_thread_2'
    },
    {
        "identifier": 'EVENT_1358_enable_controls_until_return_6',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1358_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_sync_7_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [9, 18, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_7_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_7_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_7_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_7_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_7_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_7_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_7_SUBSCRIPT_shift_southwest_steps_7',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_7_SUBSCRIPT_shift_northwest_steps_8',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_7_SUBSCRIPT_face_northeast_9',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_sync_8_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [70]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_8_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [9, 18, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_8_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_8_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_8_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_8_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_8_SUBSCRIPT_face_southwest_6',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_8_SUBSCRIPT_visibility_on_7',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_8_SUBSCRIPT_shift_southwest_steps_8',
                "command": 'shift_southwest_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_8_SUBSCRIPT_shift_northwest_steps_9',
                "command": 'shift_northwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_8_SUBSCRIPT_face_northeast_10',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_8_SUBSCRIPT_set_priority_11',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_sync_9_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [70]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_9_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_9_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [9, 18, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_9_SUBSCRIPT_set_priority_3',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_9_SUBSCRIPT_clear_solidity_bits_4',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_9_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_9_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_9_SUBSCRIPT_face_southwest_7',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_9_SUBSCRIPT_visibility_on_8',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_9_SUBSCRIPT_shift_southwest_steps_9',
                "command": 'shift_southwest_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_9_SUBSCRIPT_shift_northwest_steps_10',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_9_SUBSCRIPT_face_northeast_11',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_9_SUBSCRIPT_set_priority_12',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_async_10_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [70]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_10_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_10_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_10_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [9, 18, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_10_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_10_SUBSCRIPT_clear_solidity_bits_5',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_10_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_10_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_10_SUBSCRIPT_face_southwest_8',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_10_SUBSCRIPT_visibility_on_9',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_10_SUBSCRIPT_shift_southwest_steps_10',
                "command": 'shift_southwest_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_10_SUBSCRIPT_shift_northwest_steps_11',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_10_SUBSCRIPT_face_northeast_12',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_10_SUBSCRIPT_set_priority_13',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_jmp_11',
        "command": 'jmp',
        "args": ['EVENT_1358_action_queue_async_16']
    },
    {
        "identifier": 'EVENT_1358_pause_12',
        "command": 'pause',
        "args": [70]
    },
    {
        "identifier": 'EVENT_1358_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 573]
    },
    {
        "identifier": 'EVENT_1358_run_dialog_14',
        "command": 'run_dialog',
        "args": [2776, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1358_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 574]
    },
    {
        "identifier": 'EVENT_1358_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_async_16_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_16_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_16_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_16_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_16_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_16_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_16_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_16_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_16_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_16_SUBSCRIPT_reset_properties_9',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_1358_action_queue_sync_60']
    },
    {
        "identifier": 'EVENT_1358_run_dialog_18',
        "command": 'run_dialog',
        "args": [2772, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1358_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 573]
    },
    {
        "identifier": 'EVENT_1358_run_dialog_20',
        "command": 'run_dialog',
        "args": [2773, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1358_set_action_script_sync_21',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 574]
    },
    {
        "identifier": 'EVENT_1358_run_dialog_22',
        "command": 'run_dialog',
        "args": [2774, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1358_set_action_script_sync_23',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 573]
    },
    {
        "identifier": 'EVENT_1358_run_dialog_24',
        "command": 'run_dialog',
        "args": [2775, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1358_set_action_script_sync_25',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 574]
    },
    {
        "identifier": 'EVENT_1358_run_dialog_26',
        "command": 'run_dialog',
        "args": [2777, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1358_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_sync_27_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_27_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_27_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_27_SUBSCRIPT_fixed_f_coord_off_3',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_27_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_27_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_27_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_27_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_action_queue_sync_28',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_sync_28_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_28_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_28_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_28_SUBSCRIPT_fixed_f_coord_off_3',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_28_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_28_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_28_SUBSCRIPT_face_southwest_6',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_sync_29_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_29_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_29_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_29_SUBSCRIPT_fixed_f_coord_off_3',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_29_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_29_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_29_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_29_SUBSCRIPT_shift_northwest_steps_7',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_29_SUBSCRIPT_shift_southwest_steps_8',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_29_SUBSCRIPT_shift_southwest_pixels_9',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_29_SUBSCRIPT_face_southeast_10',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_sync_30_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_30_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_30_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_30_SUBSCRIPT_fixed_f_coord_off_3',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_30_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_30_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_30_SUBSCRIPT_shift_northwest_steps_6',
                "command": 'shift_northwest_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_async_31_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_31_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_31_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [7, 26, 3, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_31_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_31_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_31_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_31_SUBSCRIPT_shift_northwest_steps_6',
                "command": 'shift_northwest_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_pause_32',
        "command": 'pause',
        "args": [45]
    },
    {
        "identifier": 'EVENT_1358_action_queue_async_33',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_async_33_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_33_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_run_dialog_34',
        "command": 'run_dialog',
        "args": [2778, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1358_pause_35',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1358_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_sync_36_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_36_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_36_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_36_SUBSCRIPT_shift_northwest_pixels_3',
                "command": 'shift_northwest_pixels',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_sync_37_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_37_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_37_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_37_SUBSCRIPT_shift_northwest_pixels_3',
                "command": 'shift_northwest_pixels',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_action_queue_async_38',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_async_38_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_38_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_38_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_38_SUBSCRIPT_shift_northwest_pixels_3',
                "command": 'shift_northwest_pixels',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_run_dialog_39',
        "command": 'run_dialog',
        "args": [2779, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1358_action_queue_sync_40',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_sync_40_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_40_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_40_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_40_SUBSCRIPT_fixed_f_coord_off_3',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_40_SUBSCRIPT_shift_northwest_pixels_4',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_40_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_40_SUBSCRIPT_face_southwest_6',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_action_queue_sync_41',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_sync_41_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_41_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_41_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_41_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_41_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_41_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_41_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_41_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_41_SUBSCRIPT_shift_southeast_steps_8',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_41_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_41_SUBSCRIPT_shift_southwest_steps_10',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_41_SUBSCRIPT_shift_northwest_steps_11',
                "command": 'shift_northwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_41_SUBSCRIPT_shift_southwest_steps_12',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_41_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [35]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_41_SUBSCRIPT_shift_northeast_steps_14',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_41_SUBSCRIPT_sequence_looping_off_15',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_action_queue_sync_42',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_sync_42_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_42_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_42_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_42_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_42_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_42_SUBSCRIPT_shift_northeast_pixels_5',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_42_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_42_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_42_SUBSCRIPT_shift_southwest_steps_8',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_42_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [35]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_42_SUBSCRIPT_shift_southeast_steps_10',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_42_SUBSCRIPT_face_northeast_11',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_42_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_42_SUBSCRIPT_jump_to_height_13',
                "command": 'jump_to_height',
                "args": [48]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_42_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_42_SUBSCRIPT_shift_southwest_steps_15',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_42_SUBSCRIPT_face_northeast_16',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_42_SUBSCRIPT_sequence_looping_off_17',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_action_queue_sync_43',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_sync_43_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_43_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_43_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_43_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_43_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_43_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_43_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [35]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_43_SUBSCRIPT_shift_northwest_steps_7',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_43_SUBSCRIPT_face_northeast_8',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_43_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_43_SUBSCRIPT_shift_southwest_steps_10',
                "command": 'shift_southwest_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_43_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_43_SUBSCRIPT_shift_northeast_steps_12',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_43_SUBSCRIPT_shift_southeast_steps_13',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_43_SUBSCRIPT_face_northeast_14',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_43_SUBSCRIPT_sequence_looping_off_15',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_action_queue_async_44',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_async_44_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_44_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_44_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_44_SUBSCRIPT_fixed_f_coord_off_3',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_44_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_44_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_44_SUBSCRIPT_transfer_to_xyzf_6',
                "command": 'transfer_to_xyzf',
                "args": [6, 25, 1, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_44_SUBSCRIPT_shadow_off_7',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_44_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_44_SUBSCRIPT_set_vram_priority_9',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_pause_45',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1358_set_action_script_sync_46',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 573]
    },
    {
        "identifier": 'EVENT_1358_set_action_script_sync_47',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 573]
    },
    {
        "identifier": 'EVENT_1358_set_action_script_sync_48',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 573]
    },
    {
        "identifier": 'EVENT_1358_run_dialog_49',
        "command": 'run_dialog',
        "args": [2781, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1358_set_action_script_sync_50',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 574]
    },
    {
        "identifier": 'EVENT_1358_set_action_script_sync_51',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 574]
    },
    {
        "identifier": 'EVENT_1358_set_action_script_sync_52',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 574]
    },
    {
        "identifier": 'EVENT_1358_action_queue_async_53',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_async_53_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_53_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_53_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_run_dialog_54',
        "command": 'run_dialog',
        "args": [2782, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1358_action_queue_async_55',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_async_55_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_fade_out_music_to_volume_56',
        "command": 'fade_out_music_to_volume',
        "args": [5, 0]
    },
    {
        "identifier": 'EVENT_1358_pause_57',
        "command": 'pause',
        "args": [70]
    },
    {
        "identifier": 'EVENT_1358_action_queue_async_58',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_async_58_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_run_dialog_59',
        "command": 'run_dialog',
        "args": [2783, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1358_action_queue_sync_60',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_sync_60_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_60_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_jmp_61',
        "command": 'jmp',
        "args": ['EVENT_1358_jmp_66']
    },
    {
        "identifier": 'EVENT_1358_action_queue_sync_62',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_sync_62_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_62_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_action_queue_sync_63',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_sync_63_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1358_action_queue_sync_63_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_action_queue_async_64',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1358_action_queue_async_64_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1358_action_queue_async_64_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1358_pause_65',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1358_jmp_66',
        "command": 'jmp',
        "args": ['EVENT_1365_play_music_default_volume_0']
    }
]
