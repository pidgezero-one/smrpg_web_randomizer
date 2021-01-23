from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_368_set_bit_7_offset_0',
        "command": 'set_bit_7_offset',
        "args": [0x015c, []]
    },
    {
        "identifier": 'EVENT_368_set_bit_7_offset_1',
        "command": 'set_bit_7_offset',
        "args": [0x015e, []]
    },
    {
        "identifier": 'EVENT_368_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7082, 4]
    },
    {
        "identifier": 'EVENT_368_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_368_action_queue_sync_3_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_368_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_368_action_queue_sync_3_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_368_action_queue_sync_3_SUBSCRIPT_shift_north_pixels_3',
                "command": 'shift_north_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_368_action_queue_sync_3_SUBSCRIPT_shift_northwest_pixels_4',
                "command": 'shift_northwest_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_368_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_368_action_queue_sync_4_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_368_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_368_action_queue_sync_5_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_368_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_368_action_queue_sync_6_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_368_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_368_action_queue_sync_7_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_368_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_368_action_queue_sync_8_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_368_action_queue_sync_8_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_368_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_368_action_queue_sync_9_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_368_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_368_action_queue_async_10_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_368_action_queue_async_10_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_368_freeze_camera_11',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_368_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_368_action_queue_async_12_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_368_action_queue_async_12_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [10, 19, 6]
            },
            {
                "identifier": 'EVENT_368_action_queue_async_12_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 252, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_368_fade_in_from_black_async_13',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_368_jmp_14',
        "command": 'jmp',
        "args": ['EVENT_368_set_bit_52']
    },
    {
        "identifier": 'EVENT_368_pause_15',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'EVENT_368_set_bit_16',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_368_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 103]
    },
    {
        "identifier": 'EVENT_368_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 103]
    },
    {
        "identifier": 'EVENT_368_pause_19',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_368_set_action_script_sync_20',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 103]
    },
    {
        "identifier": 'EVENT_368_set_action_script_sync_21',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 103]
    },
    {
        "identifier": 'EVENT_368_pause_22',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_368_set_action_script_sync_23',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 103]
    },
    {
        "identifier": 'EVENT_368_set_action_script_sync_24',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 103]
    },
    {
        "identifier": 'EVENT_368_pause_25',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_368_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 103]
    },
    {
        "identifier": 'EVENT_368_set_action_script_sync_27',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 103]
    },
    {
        "identifier": 'EVENT_368_pause_28',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_368_set_action_script_sync_29',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 103]
    },
    {
        "identifier": 'EVENT_368_set_action_script_sync_30',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 103]
    },
    {
        "identifier": 'EVENT_368_pause_31',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_368_set_action_script_sync_32',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 103]
    },
    {
        "identifier": 'EVENT_368_set_action_script_sync_33',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 103]
    },
    {
        "identifier": 'EVENT_368_stop_sound_34',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_368_clear_bit_35',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_368_set_action_script_sync_36',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 103]
    },
    {
        "identifier": 'EVENT_368_run_dialog_37',
        "command": 'run_dialog',
        "args": [619, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_368_set_bit_38',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_368_pause_39',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_368_clear_bit_40',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_368_set_action_script_sync_41',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 103]
    },
    {
        "identifier": 'EVENT_368_run_dialog_42',
        "command": 'run_dialog',
        "args": [620, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_368_set_bit_43',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_368_clear_bit_44',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_368_set_action_script_sync_45',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 103]
    },
    {
        "identifier": 'EVENT_368_run_dialog_46',
        "command": 'run_dialog',
        "args": [621, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_368_set_bit_47',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_368_pause_48',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_368_clear_bit_49',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_368_set_action_script_sync_50',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 103]
    },
    {
        "identifier": 'EVENT_368_run_dialog_51',
        "command": 'run_dialog',
        "args": [622, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_368_set_bit_52',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_368_pause_53',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_368_clear_bit_54',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_368_action_queue_async_55',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_368_action_queue_async_55_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_368_action_queue_async_56',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_368_action_queue_async_56_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_368_set_bit_57',
        "command": 'set_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'EVENT_368_set_action_script_sync_58',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 101]
    },
    {
        "identifier": 'EVENT_368_set_action_script_sync_59',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 102]
    },
    {
        "identifier": 'EVENT_368_set_action_script_sync_60',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 101]
    },
    {
        "identifier": 'EVENT_368_set_action_script_sync_61',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 102]
    },
    {
        "identifier": 'EVENT_368_set_action_script_sync_62',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 101]
    },
    {
        "identifier": 'EVENT_368_set_action_script_sync_63',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 102]
    },
    {
        "identifier": 'EVENT_368_pause_64',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_368_set_bit_65',
        "command": 'set_bit',
        "args": [0x7049, 2]
    },
    {
        "identifier": 'EVENT_368_run_event_as_subroutine_66',
        "command": 'run_event_as_subroutine',
        "args": [276]
    },
    {
        "identifier": 'EVENT_368_unfreeze_camera_67',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_368_ret_68',
        "command": 'ret'
    }
]
