from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_468_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_468_action_queue_async_0_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_468_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70eb]
    },
    {
        "identifier": 'EVENT_468_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_468_pause_5']
    },
    {
        "identifier": 'EVENT_468_set_short_mem_3',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7000]
    },
    {
        "identifier": 'EVENT_468_run_dialog_4',
        "command": 'run_dialog',
        "args": [523, AreaObjects.NPC_14, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_468_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_468_set_7000_to_tapped_button_6',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_468_jmp_if_7000_any_bits_set_7',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[6], 'EVENT_468_jmp_if_bit_set_9']
    },
    {
        "identifier": 'EVENT_468_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_468_pause_5']
    },
    {
        "identifier": 'EVENT_468_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'EVENT_468_pause_5']
    },
    {
        "identifier": 'EVENT_468_jmp_if_var_equals_short_10',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 0, 'EVENT_468_pause_5']
    },
    {
        "identifier": 'EVENT_468_dec_short_11',
        "command": 'dec_short',
        "args": [0x7024]
    },
    {
        "identifier": 'EVENT_468_add_12',
        "command": 'add',
        "args": [0x70ee, 0x01]
    },
    {
        "identifier": 'EVENT_468_jmp_if_var_equals_short_13',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 0, 'EVENT_468_close_dialog_16']
    },
    {
        "identifier": 'EVENT_468_run_dialog_14',
        "command": 'run_dialog',
        "args": [523, AreaObjects.NPC_14, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_468_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_468_set_bit_17']
    },
    {
        "identifier": 'EVENT_468_close_dialog_16',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_468_set_bit_17',
        "command": 'set_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'EVENT_468_pause_action_script_18',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_468_pause_action_script_19',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_468_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_468_action_queue_async_20_SUBSCRIPT_transfer_to_object_xy_0',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.MARIO]
            },
            {
                "identifier": 'EVENT_468_action_queue_async_20_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 0, 16, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_468_action_queue_async_20_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_468_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_468_action_queue_sync_21_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [110]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_21_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_21_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_468_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [14]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [7, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [8, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [9, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [10, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [11, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [12, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [13, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_17',
                "command": 'set_sprite_sequence',
                "args": [14, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_19',
                "command": 'set_sprite_sequence',
                "args": [15, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_21',
                "command": 'set_sprite_sequence',
                "args": [16, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_23',
                "command": 'set_sprite_sequence',
                "args": [17, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_25',
                "command": 'set_sprite_sequence',
                "args": [18, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_pause_26',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_27',
                "command": 'set_sprite_sequence',
                "args": [19, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_pause_28',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_29',
                "command": 'set_sprite_sequence',
                "args": [20, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_pause_30',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_31',
                "command": 'set_sprite_sequence',
                "args": [21, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_pause_32',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_33',
                "command": 'set_sprite_sequence',
                "args": [22, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_pause_34',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_35',
                "command": 'set_sprite_sequence',
                "args": [21, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_pause_36',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_37',
                "command": 'set_sprite_sequence',
                "args": [23, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_pause_38',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_39',
                "command": 'set_sprite_sequence',
                "args": [24, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_pause_40',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_41',
                "command": 'set_sprite_sequence',
                "args": [25, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_pause_42',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_reset_properties_43',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_set_animation_speed_44',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_sequence_looping_on_45',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_468_action_queue_sync_22_SUBSCRIPT_pause_46',
                "command": 'pause',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_468_remember_last_object_23',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_468_set_action_script_sync_24',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 430]
    },
    {
        "identifier": 'EVENT_468_set_action_script_sync_25',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 503]
    },
    {
        "identifier": 'EVENT_468_jmp_26',
        "command": 'jmp',
        "args": ['EVENT_468_pause_5']
    }
]
