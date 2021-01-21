from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2186_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_2186_ret_26']
    },
    {
        "identifier": 'EVENT_2186_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_2186_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2186_action_queue_sync_2_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [8, 54, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2186_action_queue_sync_2_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2186_action_queue_sync_2_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2186_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2186_action_queue_async_3_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 57, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2186_action_queue_async_3_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2186_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7093, 6, 'EVENT_2186_create_packet_at_object_coords_jmp_if_null_7']
    },
    {
        "identifier": 'EVENT_2186_set_action_script_async_5',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_0, 1004]
    },
    {
        "identifier": 'EVENT_2186_pause_6',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_2186_create_packet_at_object_coords_jmp_if_null_7',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._034_GREY_EXPLOSION_SFX, AreaObjects.NPC_1, 'EVENT_2186_create_packet_at_object_coords_jmp_if_null_7']
    },
    {
        "identifier": 'EVENT_2186_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 1005]
    },
    {
        "identifier": 'EVENT_2186_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2186_action_queue_sync_9_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2186_action_queue_sync_9_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2186_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2186_action_queue_async_10_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2186_action_queue_async_10_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2186_action_queue_async_10_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2186_action_queue_async_10_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2186_action_queue_async_10_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2186_action_queue_async_10_SUBSCRIPT_shift_north_steps_5',
                "command": 'shift_north_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2186_action_queue_async_10_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2186_action_queue_async_10_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_2186_start_battle_11',
        "command": 'start_battle',
        "args": [0x00f4, 7]
    },
    {
        "identifier": 'EVENT_2186_jmp_if_bit_clear_12',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_2186_action_queue_sync_17']
    },
    {
        "identifier": 'EVENT_2186_restore_all_hp_13',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_2186_restore_all_fp_14',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_2186_jmp_to_event_15',
        "command": 'jmp_to_event',
        "args": [3356]
    },
    {
        "identifier": 'EVENT_2186_ret_16',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2186_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2186_action_queue_sync_17_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 55, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2186_action_queue_sync_17_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2186_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2186_action_queue_async_18_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [7, 59, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2186_action_queue_async_18_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2186_apply_tile_mod_19',
        "command": 'apply_tile_mod',
        "args": [Rooms._377_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2C_1ST_FIGHT_SPARKY, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2186_apply_solidity_mod_20',
        "command": 'apply_solidity_mod',
        "args": [Rooms._377_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2C_1ST_FIGHT_SPARKY, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_2186_apply_tile_mod_21',
        "command": 'apply_tile_mod',
        "args": [Rooms._377_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2C_1ST_FIGHT_SPARKY, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2186_apply_solidity_mod_22',
        "command": 'apply_solidity_mod',
        "args": [Rooms._377_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2C_1ST_FIGHT_SPARKY, 1, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_2186_fade_in_from_black_async_23',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2186_create_packet_at_object_coords_jmp_if_null_24',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._034_GREY_EXPLOSION_SFX, AreaObjects.NPC_0, 'EVENT_2186_create_packet_at_object_coords_jmp_if_null_24']
    },
    {
        "identifier": 'EVENT_2186_create_packet_at_object_coords_jmp_if_null_25',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._034_GREY_EXPLOSION_SFX, AreaObjects.NPC_1, 'EVENT_2186_create_packet_at_object_coords_jmp_if_null_24']
    },
    {
        "identifier": 'EVENT_2186_ret_26',
        "command": 'ret'
    }
]
