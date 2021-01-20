from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1768_summon_to_level_0',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._396_MONSTRO_TOWN_MONSTERMAMAS_HOUSE_2F],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1768_set_bit_1',
        "command": 'set_bit',
        "args": [0x7089, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1768_set_short_2',
        "command": 'set_short',
        "args": [0x700a, 0x00d7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1768_jmp_to_event_3',
        "command": 'jmp_to_event',
        "args": [720],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1768_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1768_action_queue_async_4_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1768_action_queue_async_4_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_1768_action_queue_async_4_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1768_action_queue_async_4_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1768_action_queue_async_4_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1768_action_queue_async_4_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 4]
            },
            {
                "identifier": 'EVENT_1768_action_queue_async_4_SUBSCRIPT_shadow_on_6',
                "command": 'shadow_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1768_action_queue_async_4_SUBSCRIPT_set_solidity_bits_7',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1768_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_8',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1768_action_queue_async_4_SUBSCRIPT_jump_to_height_9',
                "command": 'jump_to_height',
                "args": [112]
            },
            {
                "identifier": 'EVENT_1768_action_queue_async_4_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1768_action_queue_async_4_SUBSCRIPT_db_11',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x18, 0xcb]
            }
        ]
    },
    {
        "identifier": 'EVENT_1768_start_battle_5',
        "command": 'start_battle',
        "args": [0x00a9, 42],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1768_set_bit_6',
        "command": 'set_bit',
        "args": [0x707c, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1768_set_bit_7',
        "command": 'set_bit',
        "args": [0x707c, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1768_set_bit_8',
        "command": 'set_bit',
        "args": [0x707c, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1768_run_event_as_subroutine_9',
        "command": 'run_event_as_subroutine',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1768_remove_from_current_level_10',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1768_restore_all_hp_11',
        "command": 'restore_all_hp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1768_restore_all_fp_12',
        "command": 'restore_all_fp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1768_fade_in_from_black_async_13',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1768_play_sound_14',
        "command": 'play_sound',
        "args": [Sounds._021_RUMBLING, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1768_set_short_15',
        "command": 'set_short',
        "args": [0x7034, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1768_set_7010_to_object_xyz_16',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1768_start_loop_n_times_17',
        "command": 'start_loop_n_times',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1768_pause_18',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1768_create_packet_at_7010_coords_jmp_if_null_19',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._032_BLUE_CLOUD, 'EVENT_1768_pause_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1768_pause_20',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1768_add_short_21',
        "command": 'add_short',
        "args": [0x7034, 0x0003],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1768_end_loop_22',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1768_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1768_action_queue_sync_23_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1768_action_queue_sync_23_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1768_ret_24',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
