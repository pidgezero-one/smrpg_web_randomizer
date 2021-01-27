from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1775_set_7000_to_70A0_short_mem_0',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70a8]
    },
    {
        "identifier": 'EVENT_1775_jmp_if_7000_equals_short_1',
        "command": 'jmp_if_7000_equals_short',
        "args": [23, 'EVENT_1775_jmp_if_bit_set_15']
    },
    {
        "identifier": 'EVENT_1775_jmp_if_7000_equals_short_2',
        "command": 'jmp_if_7000_equals_short',
        "args": [24, 'EVENT_1775_jmp_if_bit_set_21']
    },
    {
        "identifier": 'EVENT_1775_jmp_if_7000_equals_short_3',
        "command": 'jmp_if_7000_equals_short',
        "args": [25, 'EVENT_1775_jmp_if_bit_set_27']
    },
    {
        "identifier": 'EVENT_1775_jmp_if_7000_equals_short_4',
        "command": 'jmp_if_7000_equals_short',
        "args": [26, 'EVENT_1775_jmp_if_bit_set_33']
    },
    {
        "identifier": 'EVENT_1775_jmp_if_7000_equals_short_5',
        "command": 'jmp_if_7000_equals_short',
        "args": [27, 'EVENT_1775_jmp_if_bit_set_39']
    },
    {
        "identifier": 'EVENT_1775_jmp_if_7000_equals_short_6',
        "command": 'jmp_if_7000_equals_short',
        "args": [28, 'EVENT_1775_jmp_if_bit_set_45']
    },
    {
        "identifier": 'EVENT_1775_jmp_if_7000_equals_short_7',
        "command": 'jmp_if_7000_equals_short',
        "args": [29, 'EVENT_1775_jmp_if_bit_set_51']
    },
    {
        "identifier": 'EVENT_1775_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_1775_load_600f_13']
    },
    {
        "identifier": 'EVENT_1775_set_bit_9',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1775_set_bit_10',
        "command": 'set_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'EVENT_1775_jmp_to_subroutine_11',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1775_jmp_if_bit_set_57']
    },
    {
        "identifier": 'EVENT_1775_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1775_action_queue_sync_12_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_12_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_12_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_12_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_12_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_12_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_12_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_12_SUBSCRIPT_shift_z_down_steps_7',
                "command": 'shift_z_down_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_12_SUBSCRIPT_shift_northwest_steps_8',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_12_SUBSCRIPT_clear_bit_9',
                "command": 'clear_bit',
                "args": [0x7043, 1]
            }
        ]
    },
    {
        "identifier": 'EVENT_1775_load_600f_13',
        "command": 'load_600f'
    },
    {
        "identifier": 'EVENT_1775_ret_14',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1775_jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_1775_load_600f_19']
    },
    {
        "identifier": 'EVENT_1775_set_bit_16',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_1775_jmp_to_subroutine_17',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1775_jmp_if_bit_set_57']
    },
    {
        "identifier": 'EVENT_1775_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1775_action_queue_sync_18_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_18_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_18_SUBSCRIPT_add_z_coord_1_step_2',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_18_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_18_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_18_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_18_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_18_SUBSCRIPT_dec_z_coord_1_step_7',
                "command": 'dec_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_18_SUBSCRIPT_shift_northwest_steps_8',
                "command": 'shift_northwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_18_SUBSCRIPT_clear_bit_9',
                "command": 'clear_bit',
                "args": [0x7043, 2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1775_load_600f_19',
        "command": 'load_600f'
    },
    {
        "identifier": 'EVENT_1775_ret_20',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1775_jmp_if_bit_set_21',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_1775_load_600f_25']
    },
    {
        "identifier": 'EVENT_1775_set_bit_22',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_1775_jmp_to_subroutine_23',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1775_jmp_if_bit_set_57']
    },
    {
        "identifier": 'EVENT_1775_action_queue_sync_24',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1775_action_queue_sync_24_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_24_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_24_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_24_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_24_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_24_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_24_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_24_SUBSCRIPT_shift_southeast_steps_7',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_24_SUBSCRIPT_shift_z_down_steps_8',
                "command": 'shift_z_down_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_24_SUBSCRIPT_clear_bit_9',
                "command": 'clear_bit',
                "args": [0x7043, 3]
            }
        ]
    },
    {
        "identifier": 'EVENT_1775_load_600f_25',
        "command": 'load_600f'
    },
    {
        "identifier": 'EVENT_1775_ret_26',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1775_jmp_if_bit_set_27',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'EVENT_1775_load_600f_31']
    },
    {
        "identifier": 'EVENT_1775_set_bit_28',
        "command": 'set_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'EVENT_1775_jmp_to_subroutine_29',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1775_jmp_if_bit_set_57']
    },
    {
        "identifier": 'EVENT_1775_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1775_action_queue_sync_30_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_30_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_30_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_30_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_30_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_30_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_30_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_30_SUBSCRIPT_clear_bit_7',
                "command": 'clear_bit',
                "args": [0x7043, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1775_load_600f_31',
        "command": 'load_600f'
    },
    {
        "identifier": 'EVENT_1775_ret_32',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1775_jmp_if_bit_set_33',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'EVENT_1775_load_600f_37']
    },
    {
        "identifier": 'EVENT_1775_set_bit_34',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_1775_jmp_to_subroutine_35',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1775_jmp_if_bit_set_57']
    },
    {
        "identifier": 'EVENT_1775_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1775_action_queue_sync_36_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_36_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_36_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_36_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_36_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_36_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_36_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_36_SUBSCRIPT_shift_southeast_steps_7',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_36_SUBSCRIPT_shift_z_down_steps_8',
                "command": 'shift_z_down_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_36_SUBSCRIPT_walk_1_step_northwest_9',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_36_SUBSCRIPT_clear_bit_10',
                "command": 'clear_bit',
                "args": [0x7043, 5]
            }
        ]
    },
    {
        "identifier": 'EVENT_1775_load_600f_37',
        "command": 'load_600f'
    },
    {
        "identifier": 'EVENT_1775_ret_38',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1775_jmp_if_bit_set_39',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'EVENT_1775_load_600f_43']
    },
    {
        "identifier": 'EVENT_1775_set_bit_40',
        "command": 'set_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'EVENT_1775_jmp_to_subroutine_41',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1775_jmp_if_bit_set_57']
    },
    {
        "identifier": 'EVENT_1775_action_queue_sync_42',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1775_action_queue_sync_42_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_42_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_42_SUBSCRIPT_walk_1_step_southeast_2',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_42_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_42_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_42_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_42_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_42_SUBSCRIPT_walk_1_step_northwest_7',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_42_SUBSCRIPT_shift_z_down_steps_8',
                "command": 'shift_z_down_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_42_SUBSCRIPT_clear_bit_9',
                "command": 'clear_bit',
                "args": [0x7043, 6]
            }
        ]
    },
    {
        "identifier": 'EVENT_1775_load_600f_43',
        "command": 'load_600f'
    },
    {
        "identifier": 'EVENT_1775_ret_44',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1775_jmp_if_bit_set_45',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_1775_load_600f_49']
    },
    {
        "identifier": 'EVENT_1775_set_bit_46',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_1775_jmp_to_subroutine_47',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1775_jmp_if_bit_set_57']
    },
    {
        "identifier": 'EVENT_1775_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1775_action_queue_sync_48_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_48_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_48_SUBSCRIPT_shift_z_down_steps_2',
                "command": 'shift_z_down_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_48_SUBSCRIPT_walk_1_step_southeast_3',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_48_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_48_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_48_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_48_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_48_SUBSCRIPT_walk_1_step_northwest_8',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_48_SUBSCRIPT_shift_z_up_steps_9',
                "command": 'shift_z_up_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_48_SUBSCRIPT_shift_northwest_steps_10',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_48_SUBSCRIPT_clear_bit_11',
                "command": 'clear_bit',
                "args": [0x7043, 7]
            }
        ]
    },
    {
        "identifier": 'EVENT_1775_load_600f_49',
        "command": 'load_600f'
    },
    {
        "identifier": 'EVENT_1775_ret_50',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1775_jmp_if_bit_set_51',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'EVENT_1775_load_600f_55']
    },
    {
        "identifier": 'EVENT_1775_set_bit_52',
        "command": 'set_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'EVENT_1775_jmp_to_subroutine_53',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1775_jmp_if_bit_set_57']
    },
    {
        "identifier": 'EVENT_1775_action_queue_sync_54',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_1775_action_queue_sync_54_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_54_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_54_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_54_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_54_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_54_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_54_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_54_SUBSCRIPT_shift_z_down_steps_7',
                "command": 'shift_z_down_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_54_SUBSCRIPT_shift_northwest_steps_8',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1775_action_queue_sync_54_SUBSCRIPT_clear_bit_9',
                "command": 'clear_bit',
                "args": [0x7044, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_1775_load_600f_55',
        "command": 'load_600f'
    },
    {
        "identifier": 'EVENT_1775_ret_56',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1775_jmp_if_bit_set_57',
        "command": 'jmp_if_bit_set',
        "args": [0x707c, 0, 'EVENT_1775_clear_bit_60']
    },
    {
        "identifier": 'EVENT_1775_set_7016_to_object_xyz_58',
        "command": 'set_7016_to_object_xyz',
        "args": [0x90]
    },
    {
        "identifier": 'EVENT_1775_action_queue_async_59',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1775_action_queue_async_59_SUBSCRIPT_set_700C_to_object_coord_0',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.MARIO, Coords.F, []]
            },
            {
                "identifier": 'EVENT_1775_action_queue_async_59_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1775_action_queue_async_59_SUBSCRIPT_floating_off_2',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1775_action_queue_async_59_SUBSCRIPT_run_away_shift_3',
                "command": 'run_away_shift'
            },
            {
                "identifier": 'EVENT_1775_action_queue_async_59_SUBSCRIPT_floating_on_4',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1775_action_queue_async_59_SUBSCRIPT_fixed_f_coord_off_5',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1775_action_queue_async_59_SUBSCRIPT_face_east_7C_6',
                "command": 'face_east_7C'
            }
        ]
    },
    {
        "identifier": 'EVENT_1775_clear_bit_60',
        "command": 'clear_bit',
        "args": [0x707c, 0]
    },
    {
        "identifier": 'EVENT_1775_ret_61',
        "command": 'ret'
    }
]
