from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2359_summon_to_level_0',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_10, Rooms._222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS]
    },
    {
        "identifier": 'EVENT_2359_summon_to_level_1',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_11, Rooms._222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS]
    },
    {
        "identifier": 'EVENT_2359_summon_to_level_2',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_12, Rooms._222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS]
    },
    {
        "identifier": 'EVENT_2359_summon_to_level_3',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_13, Rooms._222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS]
    },
    {
        "identifier": 'EVENT_2359_summon_to_level_4',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_14, Rooms._222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS]
    },
    {
        "identifier": 'EVENT_2359_summon_to_level_5',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_15, Rooms._222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS]
    },
    {
        "identifier": 'EVENT_2359_set_bit_6',
        "command": 'set_bit',
        "args": [0x708f, 3]
    },
    {
        "identifier": 'EVENT_2359_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_2359_set_9']
    },
    {
        "identifier": 'EVENT_2359_jmp_if_var_equals_byte_8',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c0, 219, 'EVENT_2359_set_13']
    },
    {
        "identifier": 'EVENT_2359_set_9',
        "command": 'set',
        "args": [0x70c1, 24]
    },
    {
        "identifier": 'EVENT_2359_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2359_action_queue_sync_10_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [8, 70]
            },
            {
                "identifier": 'EVENT_2359_action_queue_sync_10_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2359_action_queue_sync_10_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2359_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2359_action_queue_async_11_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [8, 69]
            },
            {
                "identifier": 'EVENT_2359_action_queue_async_11_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2359_jmp_12',
        "command": 'jmp',
        "args": ['EVENT_2359_set_16']
    },
    {
        "identifier": 'EVENT_2359_set_13',
        "command": 'set',
        "args": [0x70c1, 0]
    },
    {
        "identifier": 'EVENT_2359_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2359_action_queue_sync_14_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2359_action_queue_sync_14_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2359_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2359_action_queue_async_15_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2359_action_queue_async_15_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2359_set_16',
        "command": 'set',
        "args": [0x70c0, 220]
    },
    {
        "identifier": 'EVENT_2359_run_background_event_17',
        "command": 'run_background_event',
        "args": [2379, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_2359_jmp_if_bit_clear_18',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 7, 'EVENT_2359_fade_in_from_black_async_22']
    },
    {
        "identifier": 'EVENT_2359_run_event_as_subroutine_19',
        "command": 'run_event_as_subroutine',
        "args": [81]
    },
    {
        "identifier": 'EVENT_2359_clear_bit_20',
        "command": 'clear_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_2359_ret_21',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2359_fade_in_from_black_async_22',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2359_ret_23',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2359_set_24',
        "command": 'set',
        "args": [0x70c0, 220]
    },
    {
        "identifier": 'EVENT_2359_set_25',
        "command": 'set',
        "args": [0x70c1, 0]
    },
    {
        "identifier": 'EVENT_2359_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2359_action_queue_sync_26_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2359_action_queue_sync_26_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2359_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2359_action_queue_sync_27_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2359_action_queue_sync_27_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2359_action_queue_async_28',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2359_action_queue_async_28_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2359_action_queue_async_28_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [7, 81, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2359_action_queue_async_28_SUBSCRIPT_overwrite_solidity_2',
                "command": 'overwrite_solidity',
                "args": [[]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2359_freeze_camera_29',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2359_fade_in_from_black_async_30',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2359_set_action_script_async_31',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 414]
    },
    {
        "identifier": 'EVENT_2359_set_action_script_async_32',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 399]
    },
    {
        "identifier": 'EVENT_2359_set_action_script_async_33',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2359_run_background_event_34',
        "command": 'run_background_event',
        "args": [2379, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_2359_unfreeze_camera_35',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2359_ret_36',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2359_set_37',
        "command": 'set',
        "args": [0x70c0, 220]
    },
    {
        "identifier": 'EVENT_2359_set_38',
        "command": 'set',
        "args": [0x70c1, 24]
    },
    {
        "identifier": 'EVENT_2359_action_queue_sync_39',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2359_action_queue_sync_39_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [8, 70]
            },
            {
                "identifier": 'EVENT_2359_action_queue_sync_39_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2359_action_queue_sync_39_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2359_action_queue_async_40',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2359_action_queue_async_40_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [8, 69]
            },
            {
                "identifier": 'EVENT_2359_action_queue_async_40_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2359_action_queue_async_41',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2359_action_queue_async_41_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2359_action_queue_async_41_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [9, 74, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2359_action_queue_async_41_SUBSCRIPT_overwrite_solidity_2',
                "command": 'overwrite_solidity',
                "args": [[]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2359_freeze_camera_42',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2359_fade_in_from_black_async_43',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2359_set_action_script_async_44',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 415]
    },
    {
        "identifier": 'EVENT_2359_set_action_script_async_45',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 399]
    },
    {
        "identifier": 'EVENT_2359_set_action_script_async_46',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2359_run_background_event_47',
        "command": 'run_background_event',
        "args": [2379, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_2359_unfreeze_camera_48',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2359_ret_49',
        "command": 'ret'
    }
]
