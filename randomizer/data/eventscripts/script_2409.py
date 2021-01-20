from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2409_jmp_if_var_equals_byte_0',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c0, 237, 'EVENT_2409_jmp_if_bit_clear_24'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2409_action_queue_sync_1_SUBSCRIPT_shift_south_pixels_0',
                "command": 'shift_south_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2409_action_queue_sync_1_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [5]
            },
        ]
    },
    {
        "identifier": 'EVENT_2409_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2409_action_queue_sync_2_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [12]
            },
        ]
    },
    {
        "identifier": 'EVENT_2409_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x708f, 5, 'EVENT_2409_set_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 690],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_5',
        "command": 'set',
        "args": [0x70c0, 239],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_6',
        "command": 'set',
        "args": [0x70c1, 24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_7',
        "command": 'set',
        "args": [0x70c2, 16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7045, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_freeze_camera_9',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2409_action_queue_sync_10_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [25, 44]
            },
            {
                "identifier": 'EVENT_2409_action_queue_sync_10_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2409_action_queue_sync_10_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [19]
            },
        ]
    },
    {
        "identifier": 'EVENT_2409_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2409_action_queue_sync_11_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [25, 43]
            },
            {
                "identifier": 'EVENT_2409_action_queue_sync_11_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [11]
            },
            {
                "identifier": 'EVENT_2409_action_queue_sync_11_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [19]
            },
        ]
    },
    {
        "identifier": 'EVENT_2409_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2409_action_queue_sync_12_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [27, 39]
            },
            {
                "identifier": 'EVENT_2409_action_queue_sync_12_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2409_action_queue_sync_12_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [19]
            },
        ]
    },
    {
        "identifier": 'EVENT_2409_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2409_action_queue_sync_13_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [28, 38]
            },
            {
                "identifier": 'EVENT_2409_action_queue_sync_13_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [11]
            },
            {
                "identifier": 'EVENT_2409_action_queue_sync_13_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [19]
            },
        ]
    },
    {
        "identifier": 'EVENT_2409_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2409_action_queue_async_14_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2409_action_queue_async_14_SUBSCRIPT_overwrite_solidity_1',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2409_action_queue_async_14_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [32, 43, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_2409_fade_in_from_black_async_15',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_action_script_async_16',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 414],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_action_script_async_17',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 399],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_action_script_async_18',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_run_background_event_19',
        "command": 'run_background_event',
        "args": [2592, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_unfreeze_camera_20',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_run_background_event_21',
        "command": 'run_background_event',
        "args": [2592, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_ret_22',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_ret_23',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_jmp_if_bit_clear_24',
        "command": 'jmp_if_bit_clear',
        "args": [0x708f, 5, 'EVENT_2409_set_26'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_action_script_sync_25',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 690],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_26',
        "command": 'set',
        "args": [0x70c0, 239],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_27',
        "command": 'set',
        "args": [0x70c1, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_28',
        "command": 'set',
        "args": [0x70c2, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_clear_bit_29',
        "command": 'clear_bit',
        "args": [0x7045, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2409_action_queue_sync_30_SUBSCRIPT_shift_z_down_pixels_0',
                "command": 'shift_z_down_pixels',
                "args": [19]
            },
        ]
    },
    {
        "identifier": 'EVENT_2409_action_queue_sync_31',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2409_action_queue_sync_31_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2409_action_queue_sync_31_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [19]
            },
        ]
    },
    {
        "identifier": 'EVENT_2409_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2409_action_queue_sync_32_SUBSCRIPT_shift_z_down_pixels_0',
                "command": 'shift_z_down_pixels',
                "args": [19]
            },
        ]
    },
    {
        "identifier": 'EVENT_2409_action_queue_async_33',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2409_action_queue_async_33_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2409_action_queue_async_33_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [19]
            },
        ]
    },
    {
        "identifier": 'EVENT_2409_run_background_event_34',
        "command": 'run_background_event',
        "args": [2592, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_fade_in_from_black_async_35',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_ret_36',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_jmp_if_bit_clear_37',
        "command": 'jmp_if_bit_clear',
        "args": [0x708f, 5, 'EVENT_2409_set_39'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_action_script_sync_38',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 690],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_39',
        "command": 'set',
        "args": [0x70c0, 239],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_40',
        "command": 'set',
        "args": [0x70c1, 24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_41',
        "command": 'set',
        "args": [0x70c2, 16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_clear_bit_42',
        "command": 'clear_bit',
        "args": [0x7045, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_freeze_camera_43',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_action_queue_sync_44',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2409_action_queue_sync_44_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [25, 44]
            },
            {
                "identifier": 'EVENT_2409_action_queue_sync_44_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2409_action_queue_sync_44_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [19]
            },
        ]
    },
    {
        "identifier": 'EVENT_2409_action_queue_sync_45',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2409_action_queue_sync_45_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [25, 43]
            },
            {
                "identifier": 'EVENT_2409_action_queue_sync_45_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [11]
            },
            {
                "identifier": 'EVENT_2409_action_queue_sync_45_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [19]
            },
        ]
    },
    {
        "identifier": 'EVENT_2409_action_queue_sync_46',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2409_action_queue_sync_46_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [27, 39]
            },
            {
                "identifier": 'EVENT_2409_action_queue_sync_46_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2409_action_queue_sync_46_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [19]
            },
        ]
    },
    {
        "identifier": 'EVENT_2409_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2409_action_queue_sync_47_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [28, 38]
            },
            {
                "identifier": 'EVENT_2409_action_queue_sync_47_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [11]
            },
            {
                "identifier": 'EVENT_2409_action_queue_sync_47_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [19]
            },
        ]
    },
    {
        "identifier": 'EVENT_2409_action_queue_async_48',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2409_action_queue_async_48_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2409_action_queue_async_48_SUBSCRIPT_overwrite_solidity_1',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2409_action_queue_async_48_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [27, 43, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_2409_fade_in_from_black_async_49',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_action_script_async_50',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 415],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_action_script_async_51',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 399],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_action_script_async_52',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_run_background_event_53',
        "command": 'run_background_event',
        "args": [2592, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_unfreeze_camera_54',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_run_background_event_55',
        "command": 'run_background_event',
        "args": [2592, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_ret_56',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_jmp_if_bit_clear_57',
        "command": 'jmp_if_bit_clear',
        "args": [0x708f, 5, 'EVENT_2409_set_59'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_action_script_sync_58',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 690],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_59',
        "command": 'set',
        "args": [0x70c0, 239],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_60',
        "command": 'set',
        "args": [0x70c1, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_61',
        "command": 'set',
        "args": [0x70c2, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_clear_bit_62',
        "command": 'clear_bit',
        "args": [0x7045, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_freeze_camera_63',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_action_queue_sync_64',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2409_action_queue_sync_64_SUBSCRIPT_shift_z_down_pixels_0',
                "command": 'shift_z_down_pixels',
                "args": [19]
            },
        ]
    },
    {
        "identifier": 'EVENT_2409_action_queue_sync_65',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2409_action_queue_sync_65_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2409_action_queue_sync_65_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [19]
            },
        ]
    },
    {
        "identifier": 'EVENT_2409_action_queue_sync_66',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2409_action_queue_sync_66_SUBSCRIPT_shift_z_down_pixels_0',
                "command": 'shift_z_down_pixels',
                "args": [19]
            },
        ]
    },
    {
        "identifier": 'EVENT_2409_action_queue_sync_67',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2409_action_queue_sync_67_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2409_action_queue_sync_67_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [19]
            },
        ]
    },
    {
        "identifier": 'EVENT_2409_action_queue_async_68',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2409_action_queue_async_68_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2409_action_queue_async_68_SUBSCRIPT_overwrite_solidity_1',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2409_action_queue_async_68_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [20, 60, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_2409_fade_in_from_black_async_69',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_action_script_async_70',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 860],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_action_script_async_71',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 399],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_set_action_script_async_72',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_run_background_event_73',
        "command": 'run_background_event',
        "args": [2592, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_unfreeze_camera_74',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2409_ret_75',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
