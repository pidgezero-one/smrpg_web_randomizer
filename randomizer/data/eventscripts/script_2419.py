from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2419_jmp_if_present_in_current_level_0',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_1, 'EVENT_2419_jmp_if_present_in_current_level_10']
    },
    {
        "identifier": 'EVENT_2419_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 7, 'EVENT_2419_pause_action_script_31']
    },
    {
        "identifier": 'EVENT_2419_jmp_if_object_in_level_2',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_5, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS, 'EVENT_2419_action_queue_async_7']
    },
    {
        "identifier": 'EVENT_2419_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'EVENT_2419_jmp_if_present_in_current_level_10']
    },
    {
        "identifier": 'EVENT_2419_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 388]
    },
    {
        "identifier": 'EVENT_2419_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 388]
    },
    {
        "identifier": 'EVENT_2419_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_2419_jmp_if_present_in_current_level_10']
    },
    {
        "identifier": 'EVENT_2419_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2419_action_queue_async_7_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [14, 90, 16, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2419_action_queue_async_7_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2419_action_queue_async_7_SUBSCRIPT_shift_west_pixels_2',
                "command": 'shift_west_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2419_action_queue_async_7_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2419_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 388]
    },
    {
        "identifier": 'EVENT_2419_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 388]
    },
    {
        "identifier": 'EVENT_2419_jmp_if_present_in_current_level_10',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_3, 'EVENT_2419_jmp_if_present_in_current_level_20']
    },
    {
        "identifier": 'EVENT_2419_jmp_if_bit_clear_11',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 0, 'EVENT_2419_pause_action_script_37']
    },
    {
        "identifier": 'EVENT_2419_jmp_if_object_in_level_12',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_7, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS, 'EVENT_2419_action_queue_async_17']
    },
    {
        "identifier": 'EVENT_2419_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 4, 'EVENT_2419_jmp_if_present_in_current_level_20']
    },
    {
        "identifier": 'EVENT_2419_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 388]
    },
    {
        "identifier": 'EVENT_2419_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 388]
    },
    {
        "identifier": 'EVENT_2419_jmp_16',
        "command": 'jmp',
        "args": ['EVENT_2419_jmp_if_present_in_current_level_20']
    },
    {
        "identifier": 'EVENT_2419_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2419_action_queue_async_17_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [11, 82, 16, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2419_action_queue_async_17_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2419_action_queue_async_17_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2419_action_queue_async_17_SUBSCRIPT_shift_west_pixels_3',
                "command": 'shift_west_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2419_action_queue_async_17_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2419_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 388]
    },
    {
        "identifier": 'EVENT_2419_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 388]
    },
    {
        "identifier": 'EVENT_2419_jmp_if_present_in_current_level_20',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_2, 'EVENT_2419_ret_30']
    },
    {
        "identifier": 'EVENT_2419_jmp_if_bit_clear_21',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 1, 'EVENT_2419_pause_action_script_34']
    },
    {
        "identifier": 'EVENT_2419_jmp_if_object_in_level_22',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_6, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS, 'EVENT_2419_action_queue_async_27']
    },
    {
        "identifier": 'EVENT_2419_jmp_if_bit_set_23',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 3, 'EVENT_2419_ret_30']
    },
    {
        "identifier": 'EVENT_2419_set_action_script_sync_24',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 388]
    },
    {
        "identifier": 'EVENT_2419_set_action_script_sync_25',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 388]
    },
    {
        "identifier": 'EVENT_2419_jmp_26',
        "command": 'jmp',
        "args": ['EVENT_2419_ret_30']
    },
    {
        "identifier": 'EVENT_2419_action_queue_async_27',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2419_action_queue_async_27_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [13, 85, 18, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2419_action_queue_async_27_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2419_action_queue_async_27_SUBSCRIPT_shift_west_pixels_2',
                "command": 'shift_west_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2419_action_queue_async_27_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2419_set_action_script_sync_28',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 388]
    },
    {
        "identifier": 'EVENT_2419_set_action_script_sync_29',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 388]
    },
    {
        "identifier": 'EVENT_2419_ret_30',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2419_pause_action_script_31',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_2419_remove_from_current_level_32',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_2419_ret_33',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2419_pause_action_script_34',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_2419_remove_from_current_level_35',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_2419_ret_36',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2419_pause_action_script_37',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2419_remove_from_current_level_38',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2419_ret_39',
        "command": 'ret'
    }
]
