
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_346_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_346_jmp_if_bit_set_18']
    },
    {
        "identifier": 'EVENT_346_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7084, 4, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_346_set_bit_2',
        "command": 'set_bit',
        "args": [0x7084, 4]
    },
    {
        "identifier": 'EVENT_346_run_dialog_3',
        "command": 'run_dialog',
        "args": [716, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_346_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_346_run_dialog_29']
    },
    {
        "identifier": 'EVENT_346_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_346_action_queue_sync_5_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_5_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [80]
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_5_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_5_SUBSCRIPT_jmp_if_mario_in_air_4',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_346_action_queue_sync_5_SUBSCRIPT_pause_3']
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_5_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_5_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_5_SUBSCRIPT_face_southwest_9',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_5_SUBSCRIPT_reset_properties_10',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_346_run_dialog_6',
        "command": 'run_dialog',
        "args": [717, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_346_remember_last_object_7',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_346_pause_action_script_8',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_346_start_embedded_action_script_async_F1_9',
        "command": 'start_embedded_action_script_async_F1',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_346_start_embedded_action_script_async_F1_9_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0b, [0, 1]]
            },
            {
                "identifier": 'EVENT_346_start_embedded_action_script_async_F1_9_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_346_start_embedded_action_script_async_F1_9_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_346_start_embedded_action_script_async_F1_9_SUBSCRIPT_bounce_to_xy_with_height_3',
                "command": 'bounce_to_xy_with_height',
                "args": [5, 65, 0]
            },
            {
                "identifier": 'EVENT_346_start_embedded_action_script_async_F1_9_SUBSCRIPT_floating_on_4',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_346_start_embedded_action_script_async_F1_9_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_346_start_embedded_action_script_async_F1_9_SUBSCRIPT_clear_solidity_bits_6',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_0]]
            },
            {
                "identifier": 'EVENT_346_start_embedded_action_script_async_F1_9_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_346_start_embedded_action_script_async_F1_9_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_346_run_dialog_10',
        "command": 'run_dialog',
        "args": [721, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_346_set_11',
        "command": 'set',
        "args": [0x70a7, 96]
    },
    {
        "identifier": 'EVENT_346_play_sound_12',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_346_run_dialog_13',
        "command": 'run_dialog',
        "args": [524, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_346_put_inventory_14',
        "command": 'put_inventory',
        "args": [items.Mushroom]
    },
    {
        "identifier": 'EVENT_346_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_346_action_queue_async_15_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_0]]
            }
        ]
    },
    {
        "identifier": 'EVENT_346_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 128]
    },
    {
        "identifier": 'EVENT_346_ret_17',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_346_jmp_if_bit_set_18',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 5, 'EVENT_346_run_dialog_21']
    },
    {
        "identifier": 'EVENT_346_jmp_if_bit_clear_19',
        "command": 'jmp_if_bit_clear',
        "args": [0x705d, 1, 'EVENT_346_run_dialog_21']
    },
    {
        "identifier": 'EVENT_346_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_346_jmp_if_bit_set_1']
    },
    {
        "identifier": 'EVENT_346_run_dialog_21',
        "command": 'run_dialog',
        "args": [2321, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_346_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_346_action_queue_async_22_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_346_action_queue_async_22_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_22_SUBSCRIPT_bounce_to_xy_with_height_2',
                "command": 'bounce_to_xy_with_height',
                "args": [8, 60, 2]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_22_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_346_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_346_action_queue_async_23_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_346_action_queue_async_23_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [8, 60, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_23_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_23_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_23_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_346_action_queue_async_23_SUBSCRIPT_shift_northeast_pixels_5',
                "command": 'shift_northeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_23_SUBSCRIPT_face_southwest_6',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_346_action_queue_async_23_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_346_run_dialog_24',
        "command": 'run_dialog',
        "args": [2322, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_346_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_346_action_queue_sync_25_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_25_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_25_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_346_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_346_action_queue_async_26_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_26_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_346_action_queue_async_26_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_26_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_26_SUBSCRIPT_transfer_to_xyzf_4',
                "command": 'transfer_to_xyzf',
                "args": [16, 66, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_346_set_action_script_sync_27',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_346_ret_28',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_346_run_dialog_29',
        "command": 'run_dialog',
        "args": [2381, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_346_action_queue_async_30',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_346_action_queue_async_30_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_30_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_30_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [80]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_30_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_30_SUBSCRIPT_jmp_if_mario_in_air_4',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_346_action_queue_async_30_SUBSCRIPT_pause_3']
            },
            {
                "identifier": 'EVENT_346_action_queue_async_30_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_30_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_30_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_30_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_30_SUBSCRIPT_face_southwest_9',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_346_action_queue_async_30_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_346_run_dialog_31',
        "command": 'run_dialog',
        "args": [2382, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_346_set_action_script_sync_32',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_346_ret_33',
        "command": 'ret'
    }
]
