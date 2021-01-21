from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_721_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7063, 4, 'EVENT_721_run_dialog_33']
    },
    {
        "identifier": 'EVENT_721_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x709c, 2, 'EVENT_721_jmp_if_bit_clear_6']
    },
    {
        "identifier": 'EVENT_721_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_721_action_queue_async_2_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_721_action_queue_async_2_SUBSCRIPT_face_mario_1',
                "command": 'face_mario'
            }
        ]
    },
    {
        "identifier": 'EVENT_721_run_dialog_3',
        "command": 'run_dialog',
        "args": [732, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_721_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_721_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_721_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_721_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x705d, 5, 'EVENT_721_action_queue_sync_35']
    },
    {
        "identifier": 'EVENT_721_set_bit_7',
        "command": 'set_bit',
        "args": [0x7063, 4]
    },
    {
        "identifier": 'EVENT_721_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_721_action_queue_async_8_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_721_action_queue_async_8_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_721_action_queue_async_8_SUBSCRIPT_floating_off_2',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_721_action_queue_async_8_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [4, 59]
            },
            {
                "identifier": 'EVENT_721_action_queue_async_8_SUBSCRIPT_face_north_4',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_721_action_queue_async_8_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_721_action_queue_async_8_SUBSCRIPT_set_solidity_bits_6',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_721_action_queue_async_8_SUBSCRIPT_floating_on_7',
                "command": 'floating_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_721_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_721_action_queue_async_9_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_721_action_queue_async_9_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [4, 59, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_721_action_queue_async_9_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 252, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_721_action_queue_async_9_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_721_action_queue_async_9_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_721_action_queue_async_9_SUBSCRIPT_shift_northwest_pixels_5',
                "command": 'shift_northwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_721_action_queue_async_9_SUBSCRIPT_face_northeast_6',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_721_pause_10',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_721_run_dialog_11',
        "command": 'run_dialog',
        "args": [733, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_721_pause_12',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_721_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_721_action_queue_sync_13_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_721_action_queue_sync_13_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_721_action_queue_sync_13_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_721_action_queue_sync_13_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_721_action_queue_sync_13_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_721_action_queue_sync_13_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_721_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_721_action_queue_sync_14_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_721_action_queue_sync_14_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_721_action_queue_sync_14_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [4, 57, 2, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_721_remember_last_object_15',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_721_pause_16',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_721_run_dialog_17',
        "command": 'run_dialog',
        "args": [2304, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_721_pause_18',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_721_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_721_action_queue_async_19_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_721_action_queue_async_19_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_721_action_queue_async_19_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_721_action_queue_async_19_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_721_action_queue_async_19_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_721_action_queue_async_19_SUBSCRIPT_face_southeast_5',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_721_run_dialog_20',
        "command": 'run_dialog',
        "args": [734, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_721_pause_21',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_721_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_721_action_queue_async_22_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_721_pause_23',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_721_run_dialog_24',
        "command": 'run_dialog',
        "args": [888, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_721_pause_25',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_721_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_721_action_queue_async_26_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_721_action_queue_async_26_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_721_action_queue_async_26_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_721_action_queue_async_26_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_721_action_queue_async_26_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_721_action_queue_async_26_SUBSCRIPT_transfer_to_xyzf_5',
                "command": 'transfer_to_xyzf',
                "args": [16, 66, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_721_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_721_action_queue_sync_27_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_721_action_queue_sync_27_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_721_action_queue_sync_27_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [16, 66, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_721_action_queue_sync_28',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_721_action_queue_sync_28_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_721_action_queue_sync_28_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_721_action_queue_sync_28_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_721_action_queue_sync_28_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [18, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_721_remember_last_object_29',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_721_pause_30',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_721_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_721_action_queue_async_31_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_721_action_queue_async_31_SUBSCRIPT_face_south_1',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_721_ret_32',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_721_run_dialog_33',
        "command": 'run_dialog',
        "args": [735, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_721_ret_34',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_721_action_queue_sync_35',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_721_action_queue_sync_35_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_721_action_queue_sync_35_SUBSCRIPT_object_memory_set_bit_1',
                "command": 'object_memory_set_bit',
                "args": [0x08, [4]]
            },
            {
                "identifier": 'EVENT_721_action_queue_sync_35_SUBSCRIPT_face_mario_2',
                "command": 'face_mario'
            },
            {
                "identifier": 'EVENT_721_action_queue_sync_35_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_721_action_queue_sync_35_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_721_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_721_action_queue_sync_36_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_721_action_queue_sync_36_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [4, 57, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_721_action_queue_sync_36_SUBSCRIPT_face_mario_2',
                "command": 'face_mario'
            }
        ]
    },
    {
        "identifier": 'EVENT_721_remember_last_object_37',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_721_run_dialog_38',
        "command": 'run_dialog',
        "args": [2305, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_721_action_queue_sync_39',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_721_action_queue_sync_39_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_721_action_queue_sync_39_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_721_action_queue_sync_39_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [12, 85, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_721_action_queue_sync_40',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_721_action_queue_sync_40_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_721_action_queue_sync_40_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_721_action_queue_sync_40_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_721_remember_last_object_41',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_721_ret_42',
        "command": 'ret'
    }
]
