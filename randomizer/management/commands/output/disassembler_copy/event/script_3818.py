
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3818_jmp_if_object_trigger_disabled_0',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_0, Rooms._031_MUSHROOM_KINGDOM_CASTLE_VAULT, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3818_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_3818_jmp_to_subroutine_2',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3818_disable_trigger_21']
    },
    {
        "identifier": 'EVENT_3818_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3818_action_queue_async_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3818_action_queue_async_3_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3818_action_queue_async_3_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3818_action_queue_async_3_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3818_action_queue_async_3_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x99]
            }
        ]
    },
    {
        "identifier": 'EVENT_3818_pause_4',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3818_jmp_if_mario_in_air_5',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3818_pause_4']
    },
    {
        "identifier": 'EVENT_3818_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3818_action_queue_async_6_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3818_action_queue_async_6_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [2, 91]
            },
            {
                "identifier": 'EVENT_3818_action_queue_async_6_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3818_pause_action_script_7',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_3818_start_embedded_action_script_async_F1_8',
        "command": 'start_embedded_action_script_async_F1',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3818_start_embedded_action_script_async_F1_8_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3818_start_embedded_action_script_async_F1_8_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3818_start_embedded_action_script_async_F1_8_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3818_start_embedded_action_script_async_F1_8_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [3, 90]
            },
            {
                "identifier": 'EVENT_3818_start_embedded_action_script_async_F1_8_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3818_set_action_script_async_9',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_3, 636]
    },
    {
        "identifier": 'EVENT_3818_pause_10',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3818_run_dialog_11',
        "command": 'run_dialog',
        "args": [3755, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3818_pause_12',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3818_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3818_action_queue_sync_13_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._013_COIN, 4]
            },
            {
                "identifier": 'EVENT_3818_action_queue_sync_13_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3818_action_queue_sync_13_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3818_action_queue_sync_13_SUBSCRIPT_shift_z_up_steps_3',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3818_action_queue_sync_13_SUBSCRIPT_transfer_to_xyzf_4',
                "command": 'transfer_to_xyzf',
                "args": [13, 91, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3818_jmp_to_subroutine_14',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3818_action_queue_sync_34']
    },
    {
        "identifier": 'EVENT_3818_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3818_action_queue_sync_15_SUBSCRIPT_shift_southeast_steps_0',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3818_action_queue_sync_15_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3818_action_queue_sync_15_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3818_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3818_action_queue_async_16_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3818_action_queue_async_16_SUBSCRIPT_shift_z_down_steps_1',
                "command": 'shift_z_down_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3818_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 978]
    },
    {
        "identifier": 'EVENT_3818_add_coins_18',
        "command": 'add_coins',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3818_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_3818_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_3818_clear_bit_38']
    },
    {
        "identifier": 'EVENT_3818_disable_trigger_21',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3818_play_sound_22',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_3818_disable_event_trigger_for_object_at_70A8_23',
        "command": 'disable_event_trigger_for_object_at_70A8'
    },
    {
        "identifier": 'EVENT_3818_freeze_camera_24',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_3818_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3818_action_queue_sync_25_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3818_action_queue_sync_25_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3818_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3818_action_queue_async_26_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3818_action_queue_async_26_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3818_action_queue_async_26_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3818_action_queue_async_26_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3818_action_queue_async_26_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._014_FLOWER, 4]
            },
            {
                "identifier": 'EVENT_3818_action_queue_async_26_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3818_action_queue_async_26_SUBSCRIPT_db_6',
                "command": 'db',
                "args": [0x25, 0xc0, 0x03, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_3818_action_queue_async_26_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3818_action_queue_async_26_SUBSCRIPT_bpl_26_27_28_8',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3818_action_queue_async_26_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3818_set_7016_to_object_xyz_27',
        "command": 'set_7016_to_object_xyz',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3818_set_7000_to_7000_short_mem_28',
        "command": 'set_7000_to_7000_short_mem',
        "args": [0x701a]
    },
    {
        "identifier": 'EVENT_3818_jmp_if_bit_set_29',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3818_add_31']
    },
    {
        "identifier": 'EVENT_3818_add_30',
        "command": 'add',
        "args": [0x7000, 128]
    },
    {
        "identifier": 'EVENT_3818_add_31',
        "command": 'add',
        "args": [0x7000, 160]
    },
    {
        "identifier": 'EVENT_3818_set_7000_short_mem_to_7000_32',
        "command": 'set_7000_short_mem_to_7000',
        "args": [0x701a]
    },
    {
        "identifier": 'EVENT_3818_ret_33',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3818_action_queue_sync_34',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3818_action_queue_sync_34_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3818_action_queue_sync_34_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3818_action_queue_sync_34_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x25, 0x40, 0x00, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_3818_action_queue_sync_34_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3818_action_queue_sync_34_SUBSCRIPT_bpl_26_27_28_4',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3818_action_queue_sync_34_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3818_action_queue_sync_34_SUBSCRIPT_sequence_looping_off_6',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3818_action_queue_sync_34_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3818_action_queue_sync_34_SUBSCRIPT_object_memory_clear_bit_8',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3818_action_queue_sync_34_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3818_pause_action_script_35',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3818_unfreeze_camera_36',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_3818_ret_37',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3818_clear_bit_38',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_3818_jmp_if_object_trigger_enabled_39',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_1, Rooms._031_MUSHROOM_KINGDOM_CASTLE_VAULT, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3818_jmp_if_object_trigger_enabled_40',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_0, Rooms._031_MUSHROOM_KINGDOM_CASTLE_VAULT, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3818_jmp_if_object_trigger_enabled_41',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_2, Rooms._031_MUSHROOM_KINGDOM_CASTLE_VAULT, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3818_set_bit_42',
        "command": 'set_bit',
        "args": [0x7098, 7]
    },
    {
        "identifier": 'EVENT_3818_set_bit_43',
        "command": 'set_bit',
        "args": [0x7042, 7]
    },
    {
        "identifier": 'EVENT_3818_ret_44',
        "command": 'ret'
    }
]
