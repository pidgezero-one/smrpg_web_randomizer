from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2362_set_7000_to_object_coord_0',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.X, CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_2362_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 19, 'EVENT_2362_set_21']
    },
    {
        "identifier": 'EVENT_2362_set_2',
        "command": 'set',
        "args": [0x70c0, 222]
    },
    {
        "identifier": 'EVENT_2362_set_3',
        "command": 'set',
        "args": [0x70c1, 0]
    },
    {
        "identifier": 'EVENT_2362_set_4',
        "command": 'set',
        "args": [0x70c2, 0]
    },
    {
        "identifier": 'EVENT_2362_set_5',
        "command": 'set',
        "args": [0x70c3, 0]
    },
    {
        "identifier": 'EVENT_2362_set_6',
        "command": 'set',
        "args": [0x70c4, 0]
    },
    {
        "identifier": 'EVENT_2362_set_7',
        "command": 'set',
        "args": [0x70c5, 0]
    },
    {
        "identifier": 'EVENT_2362_run_background_event_8',
        "command": 'run_background_event',
        "args": [2385, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_9_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_9_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_10_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_10_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_11_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_11_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_12_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_12_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_13_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_13_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_14_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_14_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_15_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_15_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_15_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_16_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_16_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [13]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_16_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_17_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_17_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_17_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_async_18_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_async_18_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [13]
            },
            {
                "identifier": 'EVENT_2362_action_queue_async_18_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_fade_in_from_black_async_19',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2362_ret_20',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2362_set_21',
        "command": 'set',
        "args": [0x70c0, 222]
    },
    {
        "identifier": 'EVENT_2362_set_22',
        "command": 'set',
        "args": [0x70c1, 24]
    },
    {
        "identifier": 'EVENT_2362_set_23',
        "command": 'set',
        "args": [0x70c2, 30]
    },
    {
        "identifier": 'EVENT_2362_set_24',
        "command": 'set',
        "args": [0x70c3, 24]
    },
    {
        "identifier": 'EVENT_2362_set_25',
        "command": 'set',
        "args": [0x70c4, 16]
    },
    {
        "identifier": 'EVENT_2362_set_26',
        "command": 'set',
        "args": [0x70c5, 16]
    },
    {
        "identifier": 'EVENT_2362_run_background_event_27',
        "command": 'run_background_event',
        "args": [2385, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_28',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_28_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [7, 116]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_28_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_29_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [6, 117]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_29_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_29_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_30_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [13, 104]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_30_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_31',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_31_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [12, 105]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_31_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_31_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_32_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [18, 114]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_32_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_33',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_33_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [17, 115]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_33_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_33_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_34',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_34_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [11, 118]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_34_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_34_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_34_SUBSCRIPT_shift_z_down_pixels_3',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_35',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_35_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [11, 119]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_35_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_35_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_35_SUBSCRIPT_shift_z_down_pixels_3',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_36_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [17, 107]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_36_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_36_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_36_SUBSCRIPT_shift_z_down_pixels_3',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_async_37',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_async_37_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [17, 106]
            },
            {
                "identifier": 'EVENT_2362_action_queue_async_37_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_async_37_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2362_action_queue_async_37_SUBSCRIPT_shift_z_down_pixels_3',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_fade_in_from_black_async_38',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2362_ret_39',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2362_set_40',
        "command": 'set',
        "args": [0x70c0, 222]
    },
    {
        "identifier": 'EVENT_2362_set_41',
        "command": 'set',
        "args": [0x70c1, 0]
    },
    {
        "identifier": 'EVENT_2362_set_42',
        "command": 'set',
        "args": [0x70c2, 0]
    },
    {
        "identifier": 'EVENT_2362_set_43',
        "command": 'set',
        "args": [0x70c3, 0]
    },
    {
        "identifier": 'EVENT_2362_set_44',
        "command": 'set',
        "args": [0x70c4, 0]
    },
    {
        "identifier": 'EVENT_2362_set_45',
        "command": 'set',
        "args": [0x70c5, 0]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_46',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_46_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_46_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_47_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_47_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_48_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_48_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_49',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_49_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_49_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_50',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_50_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_50_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_51',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_51_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_51_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_52',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_52_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_52_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_52_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_53',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_53_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_53_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [13]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_53_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_54',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_54_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_54_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_54_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_55',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_55_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_55_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [13]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_55_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_async_56',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_async_56_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2362_action_queue_async_56_SUBSCRIPT_overwrite_solidity_1',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_async_56_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [7, 130, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_freeze_camera_57',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2362_fade_in_from_black_async_58',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2362_set_action_script_async_59',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 414]
    },
    {
        "identifier": 'EVENT_2362_set_action_script_async_60',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 399]
    },
    {
        "identifier": 'EVENT_2362_set_action_script_async_61',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2362_run_background_event_62',
        "command": 'run_background_event',
        "args": [2385, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_2362_unfreeze_camera_63',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2362_clear_bit_64',
        "command": 'clear_bit',
        "args": [0x7045, 7]
    },
    {
        "identifier": 'EVENT_2362_ret_65',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2362_set_66',
        "command": 'set',
        "args": [0x70c0, 222]
    },
    {
        "identifier": 'EVENT_2362_set_67',
        "command": 'set',
        "args": [0x70c1, 0]
    },
    {
        "identifier": 'EVENT_2362_set_68',
        "command": 'set',
        "args": [0x70c2, 30]
    },
    {
        "identifier": 'EVENT_2362_set_69',
        "command": 'set',
        "args": [0x70c3, 0]
    },
    {
        "identifier": 'EVENT_2362_set_70',
        "command": 'set',
        "args": [0x70c4, 0]
    },
    {
        "identifier": 'EVENT_2362_set_71',
        "command": 'set',
        "args": [0x70c5, 0]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_72',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_72_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [7, 116]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_72_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_73',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_73_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [6, 117]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_73_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_73_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_74',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_74_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_74_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_75',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_75_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_75_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_76',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_76_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_76_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_77',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_77_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_77_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_78',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_78_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_78_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_78_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_79',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_79_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_79_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [13]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_79_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_80',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_80_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_80_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_80_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_81',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_81_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_81_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [13]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_81_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_async_82',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_async_82_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2362_action_queue_async_82_SUBSCRIPT_overwrite_solidity_1',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_async_82_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [12, 118, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_freeze_camera_83',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2362_fade_in_from_black_async_84',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2362_set_action_script_async_85',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 414]
    },
    {
        "identifier": 'EVENT_2362_set_action_script_async_86',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 399]
    },
    {
        "identifier": 'EVENT_2362_set_action_script_async_87',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2362_run_background_event_88',
        "command": 'run_background_event',
        "args": [2385, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_2362_unfreeze_camera_89',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2362_clear_bit_90',
        "command": 'clear_bit',
        "args": [0x7045, 7]
    },
    {
        "identifier": 'EVENT_2362_ret_91',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2362_set_92',
        "command": 'set',
        "args": [0x70c0, 222]
    },
    {
        "identifier": 'EVENT_2362_set_93',
        "command": 'set',
        "args": [0x70c1, 0]
    },
    {
        "identifier": 'EVENT_2362_set_94',
        "command": 'set',
        "args": [0x70c2, 30]
    },
    {
        "identifier": 'EVENT_2362_set_95',
        "command": 'set',
        "args": [0x70c3, 0]
    },
    {
        "identifier": 'EVENT_2362_set_96',
        "command": 'set',
        "args": [0x70c4, 16]
    },
    {
        "identifier": 'EVENT_2362_set_97',
        "command": 'set',
        "args": [0x70c5, 0]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_98',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_98_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [7, 116]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_98_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_99',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_99_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [6, 117]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_99_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_99_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_100',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_100_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_100_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_101',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_101_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_101_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_102',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_102_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_102_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_103',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_103_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_103_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_104',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_104_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [11, 118]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_104_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_104_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_104_SUBSCRIPT_shift_z_down_pixels_3',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_105',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_105_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [11, 119]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_105_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_105_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_105_SUBSCRIPT_shift_z_down_pixels_3',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_106',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_106_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_106_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_106_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_107',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_107_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_107_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [13]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_107_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_async_108',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_async_108_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2362_action_queue_async_108_SUBSCRIPT_overwrite_solidity_1',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_async_108_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [16, 127, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_freeze_camera_109',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2362_fade_in_from_black_async_110',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2362_set_action_script_async_111',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 414]
    },
    {
        "identifier": 'EVENT_2362_set_action_script_async_112',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 399]
    },
    {
        "identifier": 'EVENT_2362_set_action_script_async_113',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2362_run_background_event_114',
        "command": 'run_background_event',
        "args": [2385, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_2362_unfreeze_camera_115',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2362_clear_bit_116',
        "command": 'clear_bit',
        "args": [0x7045, 7]
    },
    {
        "identifier": 'EVENT_2362_ret_117',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2362_set_118',
        "command": 'set',
        "args": [0x70c0, 222]
    },
    {
        "identifier": 'EVENT_2362_set_119',
        "command": 'set',
        "args": [0x70c1, 24]
    },
    {
        "identifier": 'EVENT_2362_set_120',
        "command": 'set',
        "args": [0x70c2, 30]
    },
    {
        "identifier": 'EVENT_2362_set_121',
        "command": 'set',
        "args": [0x70c3, 0]
    },
    {
        "identifier": 'EVENT_2362_set_122',
        "command": 'set',
        "args": [0x70c4, 0]
    },
    {
        "identifier": 'EVENT_2362_set_123',
        "command": 'set',
        "args": [0x70c5, 0]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_124',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_124_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [7, 116]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_124_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_125',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_125_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [6, 117]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_125_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_125_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_126',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_126_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [13, 104]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_126_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_127',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_127_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [12, 105]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_127_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_127_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_128',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_128_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_128_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_129',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_129_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_129_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_130',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_130_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_130_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_130_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_131',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_131_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_131_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [13]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_131_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_132',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_132_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_132_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_132_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_133',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_133_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_133_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [13]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_133_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_async_134',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_async_134_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2362_action_queue_async_134_SUBSCRIPT_overwrite_solidity_1',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_async_134_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [18, 106, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_freeze_camera_135',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2362_fade_in_from_black_async_136',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2362_set_action_script_async_137',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 414]
    },
    {
        "identifier": 'EVENT_2362_set_action_script_async_138',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 399]
    },
    {
        "identifier": 'EVENT_2362_set_action_script_async_139',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2362_run_background_event_140',
        "command": 'run_background_event',
        "args": [2385, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_2362_unfreeze_camera_141',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2362_clear_bit_142',
        "command": 'clear_bit',
        "args": [0x7045, 7]
    },
    {
        "identifier": 'EVENT_2362_ret_143',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2362_set_144',
        "command": 'set',
        "args": [0x70c0, 222]
    },
    {
        "identifier": 'EVENT_2362_set_145',
        "command": 'set',
        "args": [0x70c1, 24]
    },
    {
        "identifier": 'EVENT_2362_set_146',
        "command": 'set',
        "args": [0x70c2, 30]
    },
    {
        "identifier": 'EVENT_2362_set_147',
        "command": 'set',
        "args": [0x70c3, 24]
    },
    {
        "identifier": 'EVENT_2362_set_148',
        "command": 'set',
        "args": [0x70c4, 16]
    },
    {
        "identifier": 'EVENT_2362_set_149',
        "command": 'set',
        "args": [0x70c5, 16]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_150',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_150_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [7, 116]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_150_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_151',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_151_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [6, 117]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_151_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_151_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_152',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_152_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [13, 104]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_152_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_153',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_153_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [12, 105]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_153_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_153_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_154',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_154_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [18, 114]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_154_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_155',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_155_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [17, 115]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_155_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_155_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_156',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_156_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [11, 118]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_156_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_156_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_156_SUBSCRIPT_shift_z_down_pixels_3',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_157',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_157_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [11, 119]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_157_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_157_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_157_SUBSCRIPT_shift_z_down_pixels_3',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_158',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_158_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [17, 107]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_158_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_158_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_158_SUBSCRIPT_shift_z_down_pixels_3',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_sync_159',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_sync_159_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [17, 106]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_159_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_159_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2362_action_queue_sync_159_SUBSCRIPT_shift_z_down_pixels_3',
                "command": 'shift_z_down_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_action_queue_async_160',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2362_action_queue_async_160_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2362_action_queue_async_160_SUBSCRIPT_overwrite_solidity_1',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2362_action_queue_async_160_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [17, 117, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_2362_freeze_camera_161',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2362_fade_in_from_black_async_162',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2362_set_action_script_async_163',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 415]
    },
    {
        "identifier": 'EVENT_2362_set_action_script_async_164',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 399]
    },
    {
        "identifier": 'EVENT_2362_set_action_script_async_165',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2362_run_background_event_166',
        "command": 'run_background_event',
        "args": [2385, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_2362_unfreeze_camera_167',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2362_clear_bit_168',
        "command": 'clear_bit',
        "args": [0x7045, 7]
    },
    {
        "identifier": 'EVENT_2362_ret_169',
        "command": 'ret'
    }
]
