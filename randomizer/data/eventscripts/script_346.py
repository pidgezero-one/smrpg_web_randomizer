from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_346_remove_from_current_level_0',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_346_remove_from_level_1',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._020_MUSHROOM_KINGDOM_CASTLE_TOADSTOOLS_ROOM]
    },
    {
        "identifier": 'EVENT_346_set_2',
        "command": 'set',
        "args": [0x70a7, 96]
    },
    {
        "identifier": 'EVENT_346_set_3',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_346_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_346_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_346_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_346_jmp_if_bit_set_24']
    },
    {
        "identifier": 'EVENT_346_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7084, 4, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_346_set_bit_8',
        "command": 'set_bit',
        "args": [0x7084, 4]
    },
    {
        "identifier": 'EVENT_346_run_dialog_9',
        "command": 'run_dialog',
        "args": [716, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_346_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_346_run_dialog_35']
    },
    {
        "identifier": 'EVENT_346_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_346_action_queue_sync_11_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_11_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [80]
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_11_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_11_SUBSCRIPT_jmp_if_mario_in_air_4',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_346_action_queue_sync_11_SUBSCRIPT_pause_3']
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_11_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_11_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_11_SUBSCRIPT_face_southwest_9',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_11_SUBSCRIPT_reset_properties_10',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_346_run_dialog_12',
        "command": 'run_dialog',
        "args": [717, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_346_remember_last_object_13',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_346_pause_action_script_14',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_346_start_embedded_action_script_async_15',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_346_start_embedded_action_script_async_15_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0b, [0, 1]]
            },
            {
                "identifier": 'EVENT_346_start_embedded_action_script_async_15_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_0]]
            },
            {
                "identifier": 'EVENT_346_start_embedded_action_script_async_15_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_346_run_dialog_16',
        "command": 'run_dialog',
        "args": [721, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_346_set_17',
        "command": 'set',
        "args": [0x70a7, 96]
    },
    {
        "identifier": 'EVENT_346_play_sound_18',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_346_run_dialog_19',
        "command": 'run_dialog',
        "args": [524, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_346_put_inventory_20',
        "command": 'put_inventory',
        "args": [items.Mushroom]
    },
    {
        "identifier": 'EVENT_346_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_346_action_queue_async_21_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_0]]
            }
        ]
    },
    {
        "identifier": 'EVENT_346_set_action_script_sync_22',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 128]
    },
    {
        "identifier": 'EVENT_346_ret_23',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_346_jmp_if_bit_set_24',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 5, 'EVENT_346_run_dialog_27']
    },
    {
        "identifier": 'EVENT_346_jmp_if_bit_clear_25',
        "command": 'jmp_if_bit_clear',
        "args": [0x705d, 1, 'EVENT_346_run_dialog_27']
    },
    {
        "identifier": 'EVENT_346_jmp_26',
        "command": 'jmp',
        "args": ['EVENT_346_jmp_if_bit_set_7']
    },
    {
        "identifier": 'EVENT_346_run_dialog_27',
        "command": 'run_dialog',
        "args": [2321, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_346_action_queue_async_28',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_346_action_queue_async_28_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_346_action_queue_async_28_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_28_SUBSCRIPT_bounce_to_xy_with_height_2',
                "command": 'bounce_to_xy_with_height',
                "args": [8, 60, 2]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_28_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_346_action_queue_async_29',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_346_action_queue_async_29_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_346_action_queue_async_29_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [8, 60, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_29_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_29_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_29_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_29_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_346_action_queue_async_29_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_346_run_dialog_30',
        "command": 'run_dialog',
        "args": [2322, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_346_action_queue_sync_31',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_346_action_queue_sync_31_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_31_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_346_action_queue_sync_31_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_346_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_346_action_queue_async_32_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_32_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_346_action_queue_async_32_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_32_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_32_SUBSCRIPT_transfer_to_xyzf_4',
                "command": 'transfer_to_xyzf',
                "args": [16, 66, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_346_set_action_script_sync_33',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_346_ret_34',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_346_run_dialog_35',
        "command": 'run_dialog',
        "args": [2381, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_346_action_queue_async_36',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_346_action_queue_async_36_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_36_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_36_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [80]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_36_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_36_SUBSCRIPT_jmp_if_mario_in_air_4',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_346_action_queue_async_36_SUBSCRIPT_pause_3']
            },
            {
                "identifier": 'EVENT_346_action_queue_async_36_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_36_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_36_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_36_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_346_action_queue_async_36_SUBSCRIPT_face_southwest_9',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_346_action_queue_async_36_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_346_run_dialog_37',
        "command": 'run_dialog',
        "args": [2382, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_346_set_action_script_sync_38',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_346_ret_39',
        "command": 'ret'
    }
]
