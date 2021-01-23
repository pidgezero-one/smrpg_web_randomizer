from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1804_store_item_amount_7000_0',
        "command": 'store_item_amount_7000',
        "args": [items.TempleKey]
    },
    {
        "identifier": 'EVENT_1804_jmp_if_7000_not_equals_short_1',
        "command": 'jmp_if_7000_not_equals_short',
        "args": [0, 'EVENT_1804_run_dialog_4']
    },
    {
        "identifier": 'EVENT_1804_run_dialog_2',
        "command": 'run_dialog',
        "args": [1235, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1804_ret_3',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1804_run_dialog_4',
        "command": 'run_dialog',
        "args": [1236, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1804_jmp_if_dialog_option_b_5',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1804_ret_24']
    },
    {
        "identifier": 'EVENT_1804_summon_to_current_level_at_marios_coords_6',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.NPC_12]
    },
    {
        "identifier": 'EVENT_1804_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_1804_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_7_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_7_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_7_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_7_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [112]
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_7_SUBSCRIPT_walk_to_xy_coords_5',
                "command": 'walk_to_xy_coords',
                "args": [1, 118]
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_7_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_7_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x20, 0xf8, 0x4f]
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_7_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_7_SUBSCRIPT_shift_z_up_pixels_9',
                "command": 'shift_z_up_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_7_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_7_SUBSCRIPT_shift_z_up_pixels_11',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_7_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_7_SUBSCRIPT_shift_z_up_pixels_13',
                "command": 'shift_z_up_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1804_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_1804_action_queue_async_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_8_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_8_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_8_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_8_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_8_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.LOOPING_OFF]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1804_remove_from_current_level_9',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_12]
    },
    {
        "identifier": 'EVENT_1804_pause_10',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1804_play_sound_11',
        "command": 'play_sound',
        "args": [Sounds._021_RUMBLING, 6]
    },
    {
        "identifier": 'EVENT_1804_set_short_12',
        "command": 'set_short',
        "args": [0x7034, 0x0001]
    },
    {
        "identifier": 'EVENT_1804_set_7010_to_object_xyz_13',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.NPC_16]
    },
    {
        "identifier": 'EVENT_1804_start_loop_n_times_14',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1804_pause_15',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1804_create_packet_at_7010_coords_jmp_if_null_16',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._032_BLUE_CLOUD, 'EVENT_1804_pause_15']
    },
    {
        "identifier": 'EVENT_1804_pause_17',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'EVENT_1804_add_short_18',
        "command": 'add_short',
        "args": [0x7034, 0x0003]
    },
    {
        "identifier": 'EVENT_1804_end_loop_19',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1804_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_1804_action_queue_async_20_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [128]
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_20_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_20_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_20_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_20_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_20_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_20_SUBSCRIPT_end_loop_6',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1804_action_queue_async_20_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0xfd, 0xf2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1804_remove_one_from_inventory_21',
        "command": 'remove_one_from_inventory',
        "args": [items.TempleKey]
    },
    {
        "identifier": 'EVENT_1804_apply_solidity_mod_22',
        "command": 'apply_solidity_mod',
        "args": [Rooms._422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_1804_set_bit_23',
        "command": 'set_bit',
        "args": [0x7094, 6]
    },
    {
        "identifier": 'EVENT_1804_ret_24',
        "command": 'ret'
    }
]
