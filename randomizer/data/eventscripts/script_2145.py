from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2145_apply_tile_mod_0',
        "command": 'apply_tile_mod',
        "args": [Rooms._478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE, 32, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2145_apply_tile_mod_1',
        "command": 'apply_tile_mod',
        "args": [Rooms._478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE, 33, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2145_apply_tile_mod_2',
        "command": 'apply_tile_mod',
        "args": [Rooms._478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE, 34, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2145_apply_tile_mod_3',
        "command": 'apply_tile_mod',
        "args": [Rooms._478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE, 35, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2145_apply_tile_mod_4',
        "command": 'apply_tile_mod',
        "args": [Rooms._478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE, 36, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2145_apply_solidity_mod_5',
        "command": 'apply_solidity_mod',
        "args": [Rooms._478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2145_run_background_event_6',
        "command": 'run_background_event',
        "args": [3329, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2145_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2145_action_queue_sync_7_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2145_action_queue_sync_7_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
        ]
    },
    {
        "identifier": 'EVENT_2145_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2145_action_queue_sync_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2145_action_queue_sync_8_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_2145_action_queue_sync_8_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_2145_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2145_action_queue_sync_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2145_action_queue_sync_9_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_2145_action_queue_sync_9_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_2145_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2145_action_queue_async_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2145_action_queue_async_10_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_2145_action_queue_async_10_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_2145_set_7000_to_object_coord_11',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.X, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2145_jmp_if_var_not_equals_short_12',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 16, 'EVENT_2145_fade_in_from_black_async_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2145_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2145_action_queue_async_13_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [16, 42, 10, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2145_action_queue_async_13_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2145_action_queue_async_13_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
        ]
    },
    {
        "identifier": 'EVENT_2145_fade_in_from_black_async_14',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2145_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
