from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1339_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_1339_action_queue_sync_0_SUBSCRIPT_shift_southeast_pixels_0',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_0_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_0_SUBSCRIPT_shadow_off_2',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_0_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_0_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_1339_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_14],
        "subscript": [
            {
                "identifier": 'EVENT_1339_action_queue_sync_1_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_1_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1339_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1339_action_queue_sync_2_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_2_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_2_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_2_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_2_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_2_SUBSCRIPT_sequence_looping_on_5',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1339_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1339_action_queue_sync_3_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_3_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_3_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_3_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_3_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_3_SUBSCRIPT_sequence_looping_on_5',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1339_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1339_action_queue_sync_4_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_4_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_4_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_4_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_4_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_4_SUBSCRIPT_sequence_looping_on_5',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1339_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1339_action_queue_sync_5_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_5_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_5_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_5_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_5_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_5_SUBSCRIPT_sequence_looping_on_5',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1339_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1339_action_queue_sync_6_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_6_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_6_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_6_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_6_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1339_action_queue_sync_6_SUBSCRIPT_sequence_looping_on_5',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1339_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1339_action_queue_async_7_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1339_action_queue_async_7_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1339_action_queue_async_7_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1339_action_queue_async_7_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_1339_action_queue_async_7_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1339_action_queue_async_7_SUBSCRIPT_sequence_looping_on_5',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1339_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7054, 0, 'EVENT_1339_set_bit_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1339_set_short_9',
        "command": 'set_short',
        "args": [0x7024, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1339_apply_tile_mod_10',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 34, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1339_apply_tile_mod_11',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1339_apply_tile_mod_12',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 42, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1339_apply_tile_mod_13',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 46, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1339_apply_tile_mod_14',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 50, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1339_apply_tile_mod_15',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 54, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1339_fade_in_from_black_async_16',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1339_ret_17',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1339_set_bit_18',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1339_set_bit_19',
        "command": 'set_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1339_set_bit_20',
        "command": 'set_bit',
        "args": [0x7043, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1339_set_bit_21',
        "command": 'set_bit',
        "args": [0x7043, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1339_set_bit_22',
        "command": 'set_bit',
        "args": [0x7043, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1339_set_bit_23',
        "command": 'set_bit',
        "args": [0x7043, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1339_apply_tile_mod_24',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 36, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1339_apply_tile_mod_25',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 40, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1339_apply_tile_mod_26',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 44, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1339_apply_tile_mod_27',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 48, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1339_apply_tile_mod_28',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 52, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1339_apply_tile_mod_29',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 56, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1339_fade_in_from_black_async_30',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1339_ret_31',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
