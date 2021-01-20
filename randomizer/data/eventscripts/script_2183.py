from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2183_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_2183_ret_26'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2183_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2183_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2183_action_queue_sync_2_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [16, 38, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2183_action_queue_sync_2_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2183_action_queue_sync_2_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2183_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2183_action_queue_async_3_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [14, 41, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2183_action_queue_async_3_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2183_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7093, 6, 'EVENT_2183_create_packet_at_object_coords_jmp_if_null_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2183_set_action_script_async_5',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_0, 1004],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2183_pause_6',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2183_create_packet_at_object_coords_jmp_if_null_7',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._034_GREY_EXPLOSION_SFX, AreaObjects.NPC_3, 'EVENT_2183_create_packet_at_object_coords_jmp_if_null_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2183_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 1005],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2183_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2183_action_queue_sync_9_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2183_action_queue_sync_9_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2183_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2183_action_queue_async_10_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2183_action_queue_async_10_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2183_action_queue_async_10_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_2183_action_queue_async_10_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2183_action_queue_async_10_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2183_action_queue_async_10_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [70]
            }
        ]
    },
    {
        "identifier": 'EVENT_2183_start_battle_11',
        "command": 'start_battle',
        "args": [0x00f2, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2183_jmp_if_bit_clear_12',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_2183_action_queue_sync_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2183_restore_all_hp_13',
        "command": 'restore_all_hp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2183_restore_all_fp_14',
        "command": 'restore_all_fp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2183_jmp_to_event_15',
        "command": 'jmp_to_event',
        "args": [3356],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2183_ret_16',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2183_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2183_action_queue_sync_17_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [13, 39, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2183_action_queue_sync_17_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2183_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2183_action_queue_async_18_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [15, 43, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2183_action_queue_async_18_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2183_apply_tile_mod_19',
        "command": 'apply_tile_mod',
        "args": [Rooms._376_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2B_1ST_FIGHT_CHEWY, 36, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2183_apply_solidity_mod_20',
        "command": 'apply_solidity_mod',
        "args": [Rooms._376_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2B_1ST_FIGHT_CHEWY, 4, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2183_apply_tile_mod_21',
        "command": 'apply_tile_mod',
        "args": [Rooms._376_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2B_1ST_FIGHT_CHEWY, 37, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2183_apply_solidity_mod_22',
        "command": 'apply_solidity_mod',
        "args": [Rooms._376_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2B_1ST_FIGHT_CHEWY, 5, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2183_fade_in_from_black_async_23',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2183_create_packet_at_object_coords_jmp_if_null_24',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._034_GREY_EXPLOSION_SFX, AreaObjects.NPC_0, 'EVENT_2183_create_packet_at_object_coords_jmp_if_null_24'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2183_create_packet_at_object_coords_jmp_if_null_25',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._034_GREY_EXPLOSION_SFX, AreaObjects.NPC_3, 'EVENT_2183_create_packet_at_object_coords_jmp_if_null_24'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2183_ret_26',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
