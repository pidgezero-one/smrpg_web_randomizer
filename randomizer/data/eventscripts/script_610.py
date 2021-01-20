from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_610_set_0',
        "command": 'set',
        "args": [0x70df, 28],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_set_bit_7_offset_1',
        "command": 'set_bit_7_offset',
        "args": [0x0158],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_set_bit_2',
        "command": 'set_bit',
        "args": [0x7067, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7042, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7042, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7042, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x7042, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7042, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7042, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7042, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7042, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_set_11',
        "command": 'set',
        "args": [0x70ac, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_set_12',
        "command": 'set',
        "args": [0x70b8, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_clear_bit_13',
        "command": 'clear_bit',
        "args": [0x704c, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_clear_bit_14',
        "command": 'clear_bit',
        "args": [0x704c, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_clear_bit_15',
        "command": 'clear_bit',
        "args": [0x704c, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_clear_bit_16',
        "command": 'clear_bit',
        "args": [0x704c, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_clear_bit_17',
        "command": 'clear_bit',
        "args": [0x709f, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_clear_bit_18',
        "command": 'clear_bit',
        "args": [0x709f, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_fade_out_music_to_volume_19',
        "command": 'fade_out_music_to_volume',
        "args": [1, 127],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_jmp_if_bit_set_20',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 7, 'EVENT_610_action_queue_sync_33'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_set_action_script_sync_21',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 376],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_set_action_script_sync_22',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 113],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_set_action_script_sync_23',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 376],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_set_action_script_sync_24',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 376],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_set_action_script_sync_25',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 98],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 376],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_610_action_queue_sync_27_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [17, 112, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_610_action_queue_sync_27_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_610_action_queue_sync_28',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_610_action_queue_sync_28_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [16, 119, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_610_action_queue_sync_28_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_610_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_610_action_queue_sync_29_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [17, 113, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_610_action_queue_sync_29_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_610_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_610_action_queue_sync_30_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [18, 113, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_610_action_queue_sync_30_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_610_fade_in_from_black_async_31',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_ret_32',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_action_queue_sync_33',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_610_action_queue_sync_33_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [15, 72, 8, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_610_action_queue_sync_34',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_610_action_queue_sync_34_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [16, 68, 8, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_610_action_queue_sync_34_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_610_action_queue_sync_35',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_610_action_queue_sync_35_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [16, 69, 8, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_610_action_queue_sync_35_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_610_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_610_action_queue_sync_36_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [16, 72, 8, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_610_action_queue_sync_36_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_610_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_610_action_queue_sync_37_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_610_remember_last_object_38',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_set_action_script_sync_39',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 376],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_set_action_script_sync_40',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 376],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_set_action_script_sync_41',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 113],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_fade_in_from_black_async_42',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_ret_43',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_run_event_at_return_44',
        "command": 'run_event_at_return',
        "args": [1022],
        "subscript": []
    },
    {
        "identifier": 'EVENT_610_ret_45',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
