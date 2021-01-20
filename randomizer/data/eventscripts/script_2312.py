from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2312_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7047, 6, 'EVENT_2312_ret_78'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_disable_trigger_1',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_set_bit_2',
        "command": 'set_bit',
        "args": [0x7047, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_remove_from_level_3',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._101_BOOSTER_PASS_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_remove_from_level_4',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._101_BOOSTER_PASS_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_remove_from_level_5',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._101_BOOSTER_PASS_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_remove_from_level_6',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._101_BOOSTER_PASS_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_store_01_to_0248_7',
        "command": 'store_01_to_0248',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._009_GREEN_SWITCH, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2312_action_queue_async_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2312_action_queue_async_9_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [3, 94]
            },
        ]
    },
    {
        "identifier": 'EVENT_2312_pause_10',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_jmp_if_present_in_current_level_11',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_0, 'EVENT_2312_apply_tile_mod_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_pause_12',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_2312_pause_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_set_bit_14',
        "command": 'set_bit',
        "args": [0x7042, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_remove_from_current_level_15',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_add_coins_16',
        "command": 'add_coins',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2312_action_queue_sync_17_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_17_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [7, 115, 8, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_17_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_17_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._013_COIN, 6]
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_17_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_17_SUBSCRIPT_jump_to_height_5',
                "command": 'jump_to_height',
                "args": [128]
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_17_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_17_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_17_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2312_apply_tile_mod_18',
        "command": 'apply_tile_mod',
        "args": [Rooms._101_BOOSTER_PASS_AREA_02, 4, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_jmp_if_bit_set_19',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 0, 'EVENT_2312_set_action_script_sync_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_play_sound_20',
        "command": 'play_sound',
        "args": [Sounds._021_RUMBLING, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_set_action_script_sync_21',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.SCREEN_FOCUS, 391],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_pause_22',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_apply_tile_mod_23',
        "command": 'apply_tile_mod',
        "args": [Rooms._101_BOOSTER_PASS_AREA_02, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_pause_24',
        "command": 'pause',
        "args": [48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_action_queue_async_25',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2312_action_queue_async_25_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2312_action_queue_async_25_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [4, 85]
            },
        ]
    },
    {
        "identifier": 'EVENT_2312_pause_26',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_jmp_if_present_in_current_level_27',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_1, 'EVENT_2312_apply_tile_mod_34'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_pause_28',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_jmp_if_bit_set_29',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_2312_pause_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_set_bit_30',
        "command": 'set_bit',
        "args": [0x7042, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_remove_from_current_level_31',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_add_coins_32',
        "command": 'add_coins',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_action_queue_sync_33',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2312_action_queue_sync_33_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_33_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [8, 109, 8, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_33_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_33_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._013_COIN, 6]
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_33_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [128]
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_33_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_33_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_33_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2312_apply_tile_mod_34',
        "command": 'apply_tile_mod',
        "args": [Rooms._101_BOOSTER_PASS_AREA_02, 5, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_jmp_if_bit_set_35',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 1, 'EVENT_2312_set_action_script_sync_37'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_play_sound_36',
        "command": 'play_sound',
        "args": [Sounds._021_RUMBLING, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_set_action_script_sync_37',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.SCREEN_FOCUS, 391],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_pause_38',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_apply_tile_mod_39',
        "command": 'apply_tile_mod',
        "args": [Rooms._101_BOOSTER_PASS_AREA_02, 1, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_pause_40',
        "command": 'pause',
        "args": [48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_action_queue_async_41',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2312_action_queue_async_41_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2312_action_queue_async_41_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [8, 85]
            },
        ]
    },
    {
        "identifier": 'EVENT_2312_pause_42',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_jmp_if_present_in_current_level_43',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_2, 'EVENT_2312_apply_tile_mod_50'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_pause_44',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_jmp_if_bit_set_45',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_2312_pause_44'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_set_bit_46',
        "command": 'set_bit',
        "args": [0x7042, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_remove_from_current_level_47',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_add_coins_48',
        "command": 'add_coins',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_action_queue_sync_49',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2312_action_queue_sync_49_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_49_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [12, 109, 8, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_49_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_49_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._013_COIN, 6]
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_49_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [128]
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_49_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_49_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_49_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2312_apply_tile_mod_50',
        "command": 'apply_tile_mod',
        "args": [Rooms._101_BOOSTER_PASS_AREA_02, 6, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_jmp_if_bit_set_51',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 2, 'EVENT_2312_set_action_script_sync_53'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_play_sound_52',
        "command": 'play_sound',
        "args": [Sounds._021_RUMBLING, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_set_action_script_sync_53',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.SCREEN_FOCUS, 391],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_pause_54',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_apply_tile_mod_55',
        "command": 'apply_tile_mod',
        "args": [Rooms._101_BOOSTER_PASS_AREA_02, 2, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_pause_56',
        "command": 'pause',
        "args": [48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_action_queue_async_57',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2312_action_queue_async_57_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2312_action_queue_async_57_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [8, 73]
            },
        ]
    },
    {
        "identifier": 'EVENT_2312_pause_58',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_jmp_if_present_in_current_level_59',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_3, 'EVENT_2312_apply_tile_mod_65'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_pause_60',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_jmp_if_bit_set_61',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_2312_pause_60'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_remove_from_current_level_62',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_add_coins_63',
        "command": 'add_coins',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_action_queue_sync_64',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2312_action_queue_sync_64_SUBSCRIPT_set_bit_0',
                "command": 'set_bit',
                "args": [0x7042, 3]
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_64_SUBSCRIPT_floating_off_1',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_64_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [11, 97, 12, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_64_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_64_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._013_COIN, 6]
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_64_SUBSCRIPT_jump_to_height_5',
                "command": 'jump_to_height',
                "args": [128]
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_64_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_64_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2312_action_queue_sync_64_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2312_apply_tile_mod_65',
        "command": 'apply_tile_mod',
        "args": [Rooms._101_BOOSTER_PASS_AREA_02, 7, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_jmp_if_bit_set_66',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 3, 'EVENT_2312_set_action_script_sync_68'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_play_sound_67',
        "command": 'play_sound',
        "args": [Sounds._021_RUMBLING, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_set_action_script_sync_68',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.SCREEN_FOCUS, 391],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_pause_69',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_apply_tile_mod_70',
        "command": 'apply_tile_mod',
        "args": [Rooms._101_BOOSTER_PASS_AREA_02, 3, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_pause_71',
        "command": 'pause',
        "args": [48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_apply_solidity_mod_72',
        "command": 'apply_solidity_mod',
        "args": [Rooms._101_BOOSTER_PASS_AREA_02, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_apply_solidity_mod_73',
        "command": 'apply_solidity_mod',
        "args": [Rooms._101_BOOSTER_PASS_AREA_02, 1, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_apply_solidity_mod_74',
        "command": 'apply_solidity_mod',
        "args": [Rooms._101_BOOSTER_PASS_AREA_02, 2, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_apply_solidity_mod_75',
        "command": 'apply_solidity_mod',
        "args": [Rooms._101_BOOSTER_PASS_AREA_02, 3, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_store_00_to_0248_76',
        "command": 'store_00_to_0248',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2312_action_queue_async_77',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2312_action_queue_async_77_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2312_action_queue_async_77_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [6, 95]
            },
        ]
    },
    {
        "identifier": 'EVENT_2312_ret_78',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
