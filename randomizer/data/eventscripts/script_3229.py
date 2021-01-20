from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3229_stop_all_background_events_0',
        "command": 'stop_all_background_events',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3229_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3229_action_queue_async_1_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._044_GHOST_FLOAT, 4]
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_1_SUBSCRIPT_transfer_to_object_xy_1',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.NPC_0]
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_1_SUBSCRIPT_set_700C_to_object_coord_2',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.NPC_0, Coords.F]
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_1_SUBSCRIPT_face_east_3',
                "command": 'face_east',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3229_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3229_action_queue_sync_2_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3229_action_queue_sync_2_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3229_action_queue_sync_2_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3229_action_queue_sync_2_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3229_action_queue_sync_2_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3229_action_queue_sync_2_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3229_action_queue_sync_2_SUBSCRIPT_start_loop_n_times_6',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3229_action_queue_sync_2_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3229_action_queue_sync_2_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3229_action_queue_sync_2_SUBSCRIPT_visibility_on_9',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3229_action_queue_sync_2_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3229_action_queue_sync_2_SUBSCRIPT_end_loop_11',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3229_action_queue_sync_2_SUBSCRIPT_start_loop_n_times_12',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3229_action_queue_sync_2_SUBSCRIPT_visibility_off_13',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3229_action_queue_sync_2_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3229_action_queue_sync_2_SUBSCRIPT_visibility_on_15',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3229_action_queue_sync_2_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3229_action_queue_sync_2_SUBSCRIPT_end_loop_17',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3229_action_queue_sync_2_SUBSCRIPT_visibility_off_18',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3229_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3229_action_queue_async_3_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_3_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_3_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_3_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_3_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_3_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_3_SUBSCRIPT_start_loop_n_times_6',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_3_SUBSCRIPT_visibility_on_7',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_3_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_3_SUBSCRIPT_visibility_off_9',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_3_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_3_SUBSCRIPT_end_loop_11',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_3_SUBSCRIPT_start_loop_n_times_12',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_3_SUBSCRIPT_visibility_on_13',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_3_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_3_SUBSCRIPT_visibility_off_15',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_3_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_3_SUBSCRIPT_end_loop_17',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_3_SUBSCRIPT_visibility_on_18',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_3_SUBSCRIPT_face_mario_19',
                "command": 'face_mario',
                "args": []
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_3_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3229_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x707c, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3229_set_bit_5',
        "command": 'set_bit',
        "args": [0x707c, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3229_set_bit_6',
        "command": 'set_bit',
        "args": [0x707c, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3229_set_short_7',
        "command": 'set_short',
        "args": [0x700e, 0x004d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3229_run_event_as_subroutine_8',
        "command": 'run_event_as_subroutine',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3229_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3229_action_queue_sync_9_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3229_action_queue_sync_9_SUBSCRIPT_object_memory_set_bit_1',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3229_action_queue_sync_9_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_3229_action_queue_sync_9_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3229_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3229_action_queue_async_10_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_10_SUBSCRIPT_object_memory_set_bit_1',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_10_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_3229_action_queue_async_10_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3229_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
