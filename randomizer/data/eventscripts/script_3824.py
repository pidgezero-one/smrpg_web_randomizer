from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3824_set_0',
        "command": 'set',
        "args": [0x70ee, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_set_1',
        "command": 'set',
        "args": [0x70eb, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_set_2',
        "command": 'set',
        "args": [0x7100, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7061, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x705e, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x705e, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_set_temp_action_script_async_6',
        "command": 'set_temp_action_script_async',
        "args": [AreaObjects.NPC_1, 803],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_set_temp_action_script_async_7',
        "command": 'set_temp_action_script_async',
        "args": [AreaObjects.NPC_2, 803],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_set_temp_action_script_async_8',
        "command": 'set_temp_action_script_async',
        "args": [AreaObjects.NPC_5, 803],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_set_temp_action_script_async_9',
        "command": 'set_temp_action_script_async',
        "args": [AreaObjects.NPC_4, 803],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_3824_action_queue_async_10_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 252, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_3824_jmp_if_bit_clear_11',
        "command": 'jmp_if_bit_clear',
        "args": [0x708b, 5, 'EVENT_3824_jmp_if_bit_set_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_summon_to_current_level_12',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_summon_to_current_level_13',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_jmp_if_bit_set_16',
        "command": 'jmp_if_bit_set',
        "args": [0x7085, 3, 'EVENT_3824_pause_action_script_47'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_pause_action_script_17',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_pause_action_script_18',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_start_embedded_action_script_async_19',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3824_start_embedded_action_script_async_19_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [14, 86, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3824_start_embedded_action_script_async_19_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3824_start_embedded_action_script_async_20',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3824_start_embedded_action_script_async_20_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [21, 58, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3824_start_embedded_action_script_async_20_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3824_start_embedded_action_script_async_20_SUBSCRIPT_set_object_memory_bits_2',
                "command": 'set_object_memory_bits',
                "args": [0x0b, bits=[0, 1]]
            },
            {
                "identifier": 'EVENT_3824_start_embedded_action_script_async_20_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3824_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3824_action_queue_sync_21_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_3824_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3824_action_queue_sync_22_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_3824_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3824_action_queue_sync_23_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_3824_action_queue_sync_24',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3824_action_queue_sync_24_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3824_action_queue_sync_24_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3824_action_queue_sync_24_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3824_remember_last_object_25',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 21],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_set_action_script_sync_27',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 98],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_jmp_if_bit_set_28',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 7, 'EVENT_3824_jmp_if_bit_clear_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_jmp_if_bit_set_29',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_3824_jmp_if_bit_set_33'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_fade_in_from_black_async_30',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_ret_31',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_jmp_if_bit_clear_32',
        "command": 'jmp_if_bit_clear',
        "args": [0x704c, 6, 'EVENT_3824_clear_bit_41'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_jmp_if_bit_set_33',
        "command": 'jmp_if_bit_set',
        "args": [0x7084, 1, 'EVENT_3824_summon_to_current_level_43'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_summon_to_current_level_34',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_apply_tile_mod_35',
        "command": 'apply_tile_mod',
        "args": [Rooms._034_YOSTER_ISLE, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_apply_solidity_mod_36',
        "command": 'apply_solidity_mod',
        "args": [Rooms._034_YOSTER_ISLE, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_action_queue_async_37',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_3824_action_queue_async_37_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3824_action_queue_async_37_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3824_action_queue_async_37_SUBSCRIPT_floating_off_2',
                "command": 'floating_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3824_jmp_if_bit_set_38',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 7, 'EVENT_3824_clear_bit_41'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_fade_in_from_black_async_39',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_ret_40',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_clear_bit_41',
        "command": 'clear_bit',
        "args": [0x7049, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_ret_42',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_summon_to_current_level_43',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_11],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_remove_from_current_level_44',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_action_queue_async_45',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3824_action_queue_async_45_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3824_action_queue_async_45_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3824_action_queue_async_45_SUBSCRIPT_sequence_playback_on_2',
                "command": 'sequence_playback_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3824_jmp_46',
        "command": 'jmp',
        "args": ['EVENT_3824_jmp_if_bit_set_38'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_pause_action_script_47',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_start_embedded_action_script_async_48',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3824_start_embedded_action_script_async_48_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [11, 82, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3824_start_embedded_action_script_async_48_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3824_start_embedded_action_script_async_48_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3824_action_queue_sync_49',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3824_action_queue_sync_49_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [11, 83, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3824_action_queue_sync_49_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3824_action_queue_sync_49_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3824_action_queue_sync_50',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3824_action_queue_sync_50_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [9, 80, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3824_action_queue_sync_50_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3824_action_queue_sync_50_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3824_action_queue_sync_50_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3824_action_queue_sync_51',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3824_action_queue_sync_51_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [16, 64, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3824_action_queue_sync_51_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3824_action_queue_sync_51_SUBSCRIPT_set_object_memory_bits_2',
                "command": 'set_object_memory_bits',
                "args": [0x0b, bits=[1]]
            },
            {
                "identifier": 'EVENT_3824_action_queue_sync_51_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3824_action_queue_sync_52',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3824_action_queue_sync_52_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [19, 60, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3824_action_queue_sync_52_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3824_action_queue_sync_52_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3824_action_queue_async_53',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3824_action_queue_async_53_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3824_action_queue_async_53_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3824_action_queue_async_53_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3824_set_action_script_sync_54',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 677],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_set_action_script_sync_55',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 676],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3824_jmp_56',
        "command": 'jmp',
        "args": ['EVENT_3824_jmp_if_bit_set_28'],
        "subscript": []
    },
]
