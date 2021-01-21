from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3283_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7058, 4, 'EVENT_3283_ret_43']
    },
    {
        "identifier": 'EVENT_3283_set_bit_1',
        "command": 'set_bit',
        "args": [0x7058, 4]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_2_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [10, 111, 14, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_2_SUBSCRIPT_floating_on_1',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_2_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_2_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_2_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_2_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_2_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_2_SUBSCRIPT_shift_southwest_steps_7',
                "command": 'shift_southwest_steps',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_2_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_2_SUBSCRIPT_walk_1_step_west_9',
                "command": 'walk_1_step_west'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_2_SUBSCRIPT_start_loop_n_times_10',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_2_SUBSCRIPT_face_northwest_11',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_2_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_2_SUBSCRIPT_face_southwest_13',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_2_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_2_SUBSCRIPT_end_loop_15',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_3_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [11, 112, 14, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_3_SUBSCRIPT_floating_on_1',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_3_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_3_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_3_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_3_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_3_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_3_SUBSCRIPT_shift_southwest_steps_7',
                "command": 'shift_southwest_steps',
                "args": [11]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_3_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_3_SUBSCRIPT_start_loop_n_times_9',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_3_SUBSCRIPT_face_southeast_10',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_3_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_3_SUBSCRIPT_face_southwest_12',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_3_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_3_SUBSCRIPT_end_loop_14',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_4_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [10, 111, 14, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_4_SUBSCRIPT_floating_on_1',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_4_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_4_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_4_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_4_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_4_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_4_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_4_SUBSCRIPT_shift_southwest_steps_8',
                "command": 'shift_southwest_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_4_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_4_SUBSCRIPT_start_loop_n_times_10',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_4_SUBSCRIPT_face_northwest_11',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_4_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_4_SUBSCRIPT_face_southeast_13',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_4_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_4_SUBSCRIPT_end_loop_15',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_4_SUBSCRIPT_walk_1_step_northwest_16',
                "command": 'walk_1_step_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_5_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [11, 112, 14, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_5_SUBSCRIPT_floating_on_1',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_5_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_5_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_5_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_5_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_5_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_5_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_5_SUBSCRIPT_shift_southwest_steps_8',
                "command": 'shift_southwest_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_5_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_5_SUBSCRIPT_start_loop_n_times_10',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_5_SUBSCRIPT_face_northwest_11',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_5_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_5_SUBSCRIPT_face_southwest_13',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_5_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_5_SUBSCRIPT_face_southeast_15',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_5_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_5_SUBSCRIPT_end_loop_17',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_run_dialog_6',
        "command": 'run_dialog',
        "args": [1788, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3283_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_async_7_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_7_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_7_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_7_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [3, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_7_SUBSCRIPT_set_vram_priority_5',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_7_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_7_SUBSCRIPT_shift_southwest_steps_7',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [8, 2, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_pause_8',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3283_close_dialog_9',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_3283_pause_10',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_11_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [48]
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_run_dialog_12',
        "command": 'run_dialog',
        "args": [1789, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_13_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [48]
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_run_dialog_14',
        "command": 'run_dialog',
        "args": [1790, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3283_set_15',
        "command": 'set',
        "args": [0x70ae, 20]
    },
    {
        "identifier": 'EVENT_3283_set_action_script_async_16',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_17_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_17_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [48]
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_run_dialog_18',
        "command": 'run_dialog',
        "args": [1791, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_19_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_20_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_21_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_22_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_22_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_22_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_22_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_22_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_22_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_22_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_22_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_23_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_23_SUBSCRIPT_set_object_memory_bits_1',
                "command": 'set_object_memory_bits',
                "args": [0x0b, []]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_23_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_23_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_23_SUBSCRIPT_walk_1_step_east_4',
                "command": 'walk_1_step_east'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_23_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_24',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_24_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_24_SUBSCRIPT_set_object_memory_bits_1',
                "command": 'set_object_memory_bits',
                "args": [0x0b, []]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_24_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_24_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_24_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_25_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_25_SUBSCRIPT_set_object_memory_bits_1',
                "command": 'set_object_memory_bits',
                "args": [0x0b, []]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_25_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_25_SUBSCRIPT_walk_1_step_southeast_3',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_25_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_async_26_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_26_SUBSCRIPT_set_object_memory_bits_1',
                "command": 'set_object_memory_bits',
                "args": [0x0b, []]
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_26_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_26_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_26_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_27_SUBSCRIPT_floating_on_0',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_27_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_27_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_27_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_27_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [48]
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_28',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_28_SUBSCRIPT_floating_on_0',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_28_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_28_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_28_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_28_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_28_SUBSCRIPT_jump_to_height_silent_5',
                "command": 'jump_to_height_silent',
                "args": [48]
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_run_dialog_29',
        "command": 'run_dialog',
        "args": [1774, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_30_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_30_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_30_SUBSCRIPT_play_sound_balance_2',
                "command": 'play_sound_balance',
                "args": [Sounds._109_BIG_SHELL_HIT, 128]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_30_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_30_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_30_SUBSCRIPT_shift_north_pixels_5',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_30_SUBSCRIPT_end_loop_6',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_30_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_30_SUBSCRIPT_play_sound_balance_8',
                "command": 'play_sound_balance',
                "args": [Sounds._109_BIG_SHELL_HIT, 64]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_30_SUBSCRIPT_start_loop_n_times_9',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_30_SUBSCRIPT_shift_south_pixels_10',
                "command": 'shift_south_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_30_SUBSCRIPT_shift_north_pixels_11',
                "command": 'shift_north_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_30_SUBSCRIPT_end_loop_12',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_30_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_30_SUBSCRIPT_play_sound_balance_14',
                "command": 'play_sound_balance',
                "args": [Sounds._109_BIG_SHELL_HIT, 32]
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_31',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_31_SUBSCRIPT_shift_xy_pixels_0',
                "command": 'shift_xy_pixels',
                "args": [8, 4]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_31_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_31_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_31_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_31_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_31_SUBSCRIPT_shift_southwest_pixels_5',
                "command": 'shift_southwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_31_SUBSCRIPT_jump_to_height_silent_6',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_31_SUBSCRIPT_floating_on_7',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_31_SUBSCRIPT_walk_1_step_southwest_8',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_31_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_31_SUBSCRIPT_shift_southwest_steps_10',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_31_SUBSCRIPT_jump_to_height_silent_11',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_31_SUBSCRIPT_shift_southwest_steps_12',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_31_SUBSCRIPT_jump_to_height_silent_13',
                "command": 'jump_to_height_silent',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_31_SUBSCRIPT_shift_southwest_steps_14',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_31_SUBSCRIPT_jump_to_height_silent_15',
                "command": 'jump_to_height_silent',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_31_SUBSCRIPT_shift_southwest_steps_16',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_31_SUBSCRIPT_visibility_off_17',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_31_SUBSCRIPT_db_18',
                "command": 'db',
                "args": [0xfd, 0xf2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_32_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [16, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_33',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_33_SUBSCRIPT_jmp_0',
                "command": 'jmp',
                "args": ['EVENT_3283_action_queue_sync_34_SUBSCRIPT_pause_0']
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_34',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_34_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [65]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_34_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_34_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_34_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_34_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_34_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_34_SUBSCRIPT_db_6',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_34_SUBSCRIPT_clear_solidity_bits_7',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_34_SUBSCRIPT_ret_8',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_35',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_35_SUBSCRIPT_jmp_0',
                "command": 'jmp',
                "args": ['EVENT_3283_action_queue_async_36_SUBSCRIPT_pause_0']
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_action_queue_async_36',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_async_36_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [55]
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_36_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_36_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_36_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_36_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_36_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_36_SUBSCRIPT_db_6',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_36_SUBSCRIPT_clear_solidity_bits_7',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_36_SUBSCRIPT_ret_8',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_37_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_37_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_37_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_37_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_action_queue_async_38',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_async_38_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_38_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_38_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_38_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [48]
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_run_dialog_39',
        "command": 'run_dialog',
        "args": [1775, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_40',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_40_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_40_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_40_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_40_SUBSCRIPT_walk_1_step_northeast_3',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_40_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_40_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0xfd, 0xf2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_action_queue_sync_41',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_sync_41_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_41_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_41_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_41_SUBSCRIPT_walk_1_step_northeast_3',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_41_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3283_action_queue_sync_41_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0xfd, 0xf2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_action_queue_async_42',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3283_action_queue_async_42_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3283_action_queue_async_42_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3283_ret_43',
        "command": 'ret'
    }
]
