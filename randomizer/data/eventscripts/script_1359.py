from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1359_set_short_0',
        "command": 'set_short',
        "args": [0x7026, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1359_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1359_action_queue_sync_1_SUBSCRIPT_shift_south_pixels_0',
                "command": 'shift_south_pixels',
                "args": [22]
            },
            {
                "identifier": 'EVENT_1359_action_queue_sync_1_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1359_action_queue_sync_1_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1359_action_queue_sync_1_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
        ]
    },
    {
        "identifier": 'EVENT_1359_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1359_action_queue_sync_2_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1359_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1359_action_queue_sync_3_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1359_action_queue_sync_3_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1359_action_queue_sync_3_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1359_action_queue_sync_3_SUBSCRIPT_set_priority_3',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1359_action_queue_sync_3_SUBSCRIPT_shadow_off_4',
                "command": 'shadow_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1359_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.LAYER_1],
        "subscript": [
            {
                "identifier": 'EVENT_1359_action_queue_async_4_SUBSCRIPT_shift_east_pixels_0',
                "command": 'shift_east_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1359_action_queue_async_4_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_1359_apply_solidity_mod_5',
        "command": 'apply_solidity_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 2, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1359_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7053, 5, 'EVENT_1359_apply_tile_mod_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1359_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7053, 4, 'EVENT_1359_apply_solidity_mod_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1359_fade_in_from_black_async_8',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1359_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1359_apply_tile_mod_10',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 35, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1359_apply_tile_mod_11',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 39, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1359_apply_tile_mod_12',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 43, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1359_apply_tile_mod_13',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 47, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1359_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1359_action_queue_async_14_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [3, 21, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_1359_apply_solidity_mod_15',
        "command": 'apply_solidity_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 1, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1359_jmp_if_bit_clear_16',
        "command": 'jmp_if_bit_clear',
        "args": [0x7054, 4, 'EVENT_1359_fade_in_from_black_async_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1359_apply_tile_mod_17',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 33, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1359_fade_in_from_black_async_18',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1359_ret_19',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1359_apply_solidity_mod_20',
        "command": 'apply_solidity_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 2, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1359_fade_in_from_black_async_21',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1359_ret_22',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
