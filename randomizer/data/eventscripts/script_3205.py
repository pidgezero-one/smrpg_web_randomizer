from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3205_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7056, 4, 'EVENT_3205_ret_27'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3205_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7057, 3, 'EVENT_3205_ret_27'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3205_enter_area_2',
        "command": 'enter_area',
        "args": [Rooms._281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM, RadialDirections.SOUTHWEST, 27, 86, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3205_remove_from_current_level_3',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3205_jmp_if_object_not_in_level_4',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_6, Rooms._281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM, 'EVENT_3205_run_event_as_subroutine_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3205_pause_action_script_5',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3205_remove_from_current_level_6',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3205_run_event_as_subroutine_7',
        "command": 'run_event_as_subroutine',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3205_set_7010_to_object_xyz_8',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3205_start_loop_n_times_9',
        "command": 'start_loop_n_times',
        "args": [7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3205_create_packet_at_7010_coords_jmp_if_null_10',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._024_BOMB_EXPLOSION_SFX, 'EVENT_3205_pause_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3205_add_short_11',
        "command": 'add_short',
        "args": [0x7014, 0x0020],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3205_pause_12',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3205_pause_13',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3205_end_loop_14',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3205_apply_tile_mod_15',
        "command": 'apply_tile_mod',
        "args": [Rooms._281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM, 32, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3205_apply_solidity_mod_16',
        "command": 'apply_solidity_mod',
        "args": [Rooms._281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3205_set_bit_17',
        "command": 'set_bit',
        "args": [0x7057, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3205_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3205_action_queue_sync_18_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_18_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_18_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [26, 87, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_18_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_18_SUBSCRIPT_sequence_playback_on_4',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_18_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_18_SUBSCRIPT_walk_to_xy_coords_6',
                "command": 'walk_to_xy_coords',
                "args": [24, 96]
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_18_SUBSCRIPT_walk_to_xy_coords_7',
                "command": 'walk_to_xy_coords',
                "args": [22, 100]
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_18_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3205_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3205_action_queue_sync_19_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_19_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_19_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [26, 87, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_19_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_19_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_19_SUBSCRIPT_sequence_playback_on_5',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_19_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_19_SUBSCRIPT_walk_to_xy_coords_7',
                "command": 'walk_to_xy_coords',
                "args": [24, 96]
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_19_SUBSCRIPT_walk_to_xy_coords_8',
                "command": 'walk_to_xy_coords',
                "args": [22, 100]
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_19_SUBSCRIPT_visibility_off_9',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3205_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3205_action_queue_sync_20_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_20_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_20_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [26, 87, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_20_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [70]
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_20_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_20_SUBSCRIPT_sequence_playback_on_5',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_20_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_20_SUBSCRIPT_walk_to_xy_coords_7',
                "command": 'walk_to_xy_coords',
                "args": [24, 96]
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_20_SUBSCRIPT_walk_to_xy_coords_8',
                "command": 'walk_to_xy_coords',
                "args": [22, 100]
            },
            {
                "identifier": 'EVENT_3205_action_queue_sync_20_SUBSCRIPT_visibility_off_9',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3205_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3205_action_queue_async_21_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3205_action_queue_async_21_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3205_action_queue_async_21_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [26, 87, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3205_action_queue_async_21_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [90]
            },
            {
                "identifier": 'EVENT_3205_action_queue_async_21_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3205_action_queue_async_21_SUBSCRIPT_sequence_playback_on_5',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3205_action_queue_async_21_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_3205_action_queue_async_21_SUBSCRIPT_walk_to_xy_coords_7',
                "command": 'walk_to_xy_coords',
                "args": [24, 96]
            },
            {
                "identifier": 'EVENT_3205_action_queue_async_21_SUBSCRIPT_walk_to_xy_coords_8',
                "command": 'walk_to_xy_coords',
                "args": [22, 100]
            },
            {
                "identifier": 'EVENT_3205_action_queue_async_21_SUBSCRIPT_visibility_off_9',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3205_summon_to_current_level_22',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3205_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3205_action_queue_async_23_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3205_action_queue_async_23_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3205_action_queue_async_23_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3205_set_24',
        "command": 'set',
        "args": [0x70b5, 19],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3205_jmp_if_object_not_in_level_25',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_6, Rooms._281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM, 'EVENT_3205_ret_27'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3205_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 726],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3205_ret_27',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
