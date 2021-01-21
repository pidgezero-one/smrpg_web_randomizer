from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1720_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'EVENT_1720_ret_41']
    },
    {
        "identifier": 'EVENT_1720_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_1720_set_short_2',
        "command": 'set_short',
        "args": [0x7024, 0x0014]
    },
    {
        "identifier": 'EVENT_1720_set_short_mem_3',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8]
    },
    {
        "identifier": 'EVENT_1720_dec_short_mem_4',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_1720_mem_7000_and_const_5',
        "command": 'mem_7000_and_const',
        "args": [0x0004]
    },
    {
        "identifier": 'EVENT_1720_add_short_mem_6',
        "command": 'add_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_1720_set_short_mem_7',
        "command": 'set_short_mem',
        "args": [0x702e, 0x7000]
    },
    {
        "identifier": 'EVENT_1720_set_short_mem_8',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000]
    },
    {
        "identifier": 'EVENT_1720_set_7000_to_object_coord_9',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MEM_70AA, Coords.F]
    },
    {
        "identifier": 'EVENT_1720_set_short_mem_10',
        "command": 'set_short_mem',
        "args": [0x70ae, 0x7000]
    },
    {
        "identifier": 'EVENT_1720_start_loop_n_times_11',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1720_pause_action_script_12',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70AA]
    },
    {
        "identifier": 'EVENT_1720_add_13',
        "command": 'add',
        "args": [0x70aa, 0x01]
    },
    {
        "identifier": 'EVENT_1720_end_loop_14',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1720_set_short_mem_15',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ae]
    },
    {
        "identifier": 'EVENT_1720_set_short_mem_16',
        "command": 'set_short_mem',
        "args": [0x700c, 0x7000]
    },
    {
        "identifier": 'EVENT_1720_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1720_action_queue_sync_17_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1720_action_queue_sync_17_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [144]
            },
            {
                "identifier": 'EVENT_1720_action_queue_sync_17_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [20]
            }
        ]
    },
    {
        "identifier": 'EVENT_1720_add_18',
        "command": 'add',
        "args": [0x70af, 0x01]
    },
    {
        "identifier": 'EVENT_1720_jmp_if_var_not_equals_byte_19',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70af, 8, 'EVENT_1720_summon_to_current_level_at_marios_coords_22']
    },
    {
        "identifier": 'EVENT_1720_set_bit_20',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_1720_fade_out_to_black_sync_duration_21',
        "command": 'fade_out_to_black_sync_duration',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1720_summon_to_current_level_at_marios_coords_22',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.MEM_70AB]
    },
    {
        "identifier": 'EVENT_1720_start_embedded_action_script_async_23',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.MEM_70AB],
        "subscript": [
            {
                "identifier": 'EVENT_1720_start_embedded_action_script_async_23_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_1720_start_embedded_action_script_async_23_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_1720_start_embedded_action_script_async_23_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1720_start_embedded_action_script_async_23_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1720_start_embedded_action_script_async_23_SUBSCRIPT_set_700C_to_object_coord_4',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.MARIO, Coords.F]
            },
            {
                "identifier": 'EVENT_1720_start_embedded_action_script_async_23_SUBSCRIPT_add_5',
                "command": 'add',
                "args": [0x700c, 2]
            },
            {
                "identifier": 'EVENT_1720_start_embedded_action_script_async_23_SUBSCRIPT_mem_700C_and_const_6',
                "command": 'mem_700C_and_const',
                "args": [0x0004]
            },
            {
                "identifier": 'EVENT_1720_start_embedded_action_script_async_23_SUBSCRIPT_mem_700C_xor_const_7',
                "command": 'mem_700C_xor_const',
                "args": [0x0004]
            },
            {
                "identifier": 'EVENT_1720_start_embedded_action_script_async_23_SUBSCRIPT_face_east_8',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_1720_start_embedded_action_script_async_23_SUBSCRIPT_floating_off_9',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1720_start_embedded_action_script_async_23_SUBSCRIPT_db_10',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_1720_start_embedded_action_script_async_23_SUBSCRIPT_db_11',
                "command": 'db',
                "args": [0x25, 0x00, 0x08, 0xb0, 0xff]
            },
            {
                "identifier": 'EVENT_1720_start_embedded_action_script_async_23_SUBSCRIPT_walk_1_step_f_direction_12',
                "command": 'walk_1_step_f_direction'
            },
            {
                "identifier": 'EVENT_1720_start_embedded_action_script_async_23_SUBSCRIPT_visibility_off_13',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1720_start_embedded_action_script_async_23_SUBSCRIPT_bpl_26_27_28_14',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_1720_pause_24',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1720_set_short_mem_25',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702e]
    },
    {
        "identifier": 'EVENT_1720_set_short_mem_26',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000]
    },
    {
        "identifier": 'EVENT_1720_start_loop_n_times_27',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1720_action_queue_sync_28',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70AA],
        "subscript": [
            {
                "identifier": 'EVENT_1720_action_queue_sync_28_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1720_action_queue_sync_28_SUBSCRIPT_shift_z_up_pixels_1',
                "command": 'shift_z_up_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_1720_action_queue_sync_28_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [16]
            }
        ]
    },
    {
        "identifier": 'EVENT_1720_add_29',
        "command": 'add',
        "args": [0x70aa, 0x01]
    },
    {
        "identifier": 'EVENT_1720_pause_30',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1720_end_loop_31',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1720_dec_32',
        "command": 'dec',
        "args": [0x70aa]
    },
    {
        "identifier": 'EVENT_1720_stop_embedded_action_script_33',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.MEM_70AA]
    },
    {
        "identifier": 'EVENT_1720_set_short_mem_34',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702e]
    },
    {
        "identifier": 'EVENT_1720_set_short_mem_35',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000]
    },
    {
        "identifier": 'EVENT_1720_start_loop_n_times_36',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1720_resume_action_script_37',
        "command": 'resume_action_script',
        "args": [AreaObjects.MEM_70AA]
    },
    {
        "identifier": 'EVENT_1720_add_38',
        "command": 'add',
        "args": [0x70aa, 0x01]
    },
    {
        "identifier": 'EVENT_1720_end_loop_39',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1720_clear_bit_40',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_1720_ret_41',
        "command": 'ret'
    }
]
