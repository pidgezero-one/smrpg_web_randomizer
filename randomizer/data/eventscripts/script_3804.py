from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3804_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3804_action_queue_sync_0_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_1',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_2, 803]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_2',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_3, 807]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_3',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_7, 804]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_4',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_9, 803]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_5',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_5, 807]
    },
    {
        "identifier": 'EVENT_3804_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3804_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3804_star_mask_expand_from_screen_center_7',
        "command": 'star_mask_expand_from_screen_center'
    },
    {
        "identifier": 'EVENT_3804_pause_8',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_9',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_8, 238]
    },
    {
        "identifier": 'EVENT_3804_pause_10',
        "command": 'pause',
        "args": [18]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_11',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_1, 238]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_12',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_3, 238]
    },
    {
        "identifier": 'EVENT_3804_pause_13',
        "command": 'pause',
        "args": [18]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_14',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_11, 238]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_15',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_9, 238]
    },
    {
        "identifier": 'EVENT_3804_pause_16',
        "command": 'pause',
        "args": [18]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_17',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_2, 238]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_18',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_7, 238]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_19',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_5, 238]
    },
    {
        "identifier": 'EVENT_3804_pause_20',
        "command": 'pause',
        "args": [18]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_21',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_10, 238]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_22',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_6, 238]
    },
    {
        "identifier": 'EVENT_3804_pause_23',
        "command": 'pause',
        "args": [18]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_24',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_4, 238]
    },
    {
        "identifier": 'EVENT_3804_pause_25',
        "command": 'pause',
        "args": [28]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_26',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_4, 238]
    },
    {
        "identifier": 'EVENT_3804_pause_27',
        "command": 'pause',
        "args": [18]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_28',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_10, 238]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_29',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_6, 238]
    },
    {
        "identifier": 'EVENT_3804_pause_30',
        "command": 'pause',
        "args": [18]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_31',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_2, 238]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_32',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_7, 238]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_33',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_5, 238]
    },
    {
        "identifier": 'EVENT_3804_pause_34',
        "command": 'pause',
        "args": [18]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_35',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_11, 238]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_36',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_9, 238]
    },
    {
        "identifier": 'EVENT_3804_pause_37',
        "command": 'pause',
        "args": [18]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_38',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_1, 238]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_39',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_3, 238]
    },
    {
        "identifier": 'EVENT_3804_pause_40',
        "command": 'pause',
        "args": [18]
    },
    {
        "identifier": 'EVENT_3804_set_temp_action_script_sync_41',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_8, 238]
    },
    {
        "identifier": 'EVENT_3804_pause_42',
        "command": 'pause',
        "args": [65]
    },
    {
        "identifier": 'EVENT_3804_action_queue_async_43',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3804_action_queue_async_43_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3804_action_queue_async_43_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3804_action_queue_async_43_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3804_action_queue_async_43_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3804_action_queue_async_43_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [16, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3804_action_queue_async_43_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3804_action_queue_async_43_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3804_action_queue_async_43_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3804_action_queue_async_43_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [17, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3804_pause_44',
        "command": 'pause',
        "args": [95]
    },
    {
        "identifier": 'EVENT_3804_action_queue_sync_45',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3804_action_queue_sync_45_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3804_action_queue_sync_46',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3804_action_queue_sync_46_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3804_action_queue_sync_46_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3804_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3804_action_queue_sync_47_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3804_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3804_action_queue_sync_48_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3804_action_queue_sync_48_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3804_action_queue_sync_49',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3804_action_queue_sync_49_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3804_action_queue_sync_50',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3804_action_queue_sync_50_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3804_action_queue_sync_51',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3804_action_queue_sync_51_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [18]
            },
            {
                "identifier": 'EVENT_3804_action_queue_sync_51_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3804_action_queue_sync_52',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3804_action_queue_sync_52_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3804_action_queue_sync_53',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3804_action_queue_sync_53_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3804_action_queue_sync_54',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3804_action_queue_sync_54_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [18]
            },
            {
                "identifier": 'EVENT_3804_action_queue_sync_54_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3804_action_queue_sync_55',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3804_action_queue_sync_55_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [18]
            },
            {
                "identifier": 'EVENT_3804_action_queue_sync_55_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3804_action_queue_sync_56',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_3804_action_queue_sync_56_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3804_action_queue_sync_56_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3804_action_queue_sync_56_SUBSCRIPT_embedded_animation_routine_2',
                "command": 'embedded_animation_routine',
                "args": [0x28]
            },
            {
                "identifier": 'EVENT_3804_action_queue_sync_56_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3804_action_queue_sync_56_SUBSCRIPT_bpl_26_27_28_4',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3804_action_queue_sync_56_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3804_action_queue_sync_56_SUBSCRIPT_floating_on_6',
                "command": 'floating_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3804_action_queue_sync_57',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_14],
        "subscript": [
            {
                "identifier": 'EVENT_3804_action_queue_sync_57_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3804_action_queue_sync_57_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3804_action_queue_sync_57_SUBSCRIPT_embedded_animation_routine_2',
                "command": 'embedded_animation_routine',
                "args": [0x28]
            },
            {
                "identifier": 'EVENT_3804_action_queue_sync_57_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3804_action_queue_sync_57_SUBSCRIPT_bpl_26_27_28_4',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_3804_pause_58',
        "command": 'pause',
        "args": [45]
    },
    {
        "identifier": 'EVENT_3804_action_queue_sync_59',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3804_action_queue_sync_59_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3804_action_queue_sync_59_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3804_action_queue_sync_59_SUBSCRIPT_embedded_animation_routine_2',
                "command": 'embedded_animation_routine',
                "args": [0x28]
            },
            {
                "identifier": 'EVENT_3804_action_queue_sync_59_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_3804_pause_60',
        "command": 'pause',
        "args": [160]
    },
    {
        "identifier": 'EVENT_3804_star_mask_shrink_to_screen_center_61',
        "command": 'star_mask_shrink_to_screen_center'
    },
    {
        "identifier": 'EVENT_3804_pause_script_until_effect_done_62',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3804_jmp_to_event_63',
        "command": 'jmp_to_event',
        "args": [3803]
    }
]
