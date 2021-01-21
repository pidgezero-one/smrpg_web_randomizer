from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2500_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_2500_ret_41']
    },
    {
        "identifier": 'EVENT_2500_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_2500_remove_from_current_level_2',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_12]
    },
    {
        "identifier": 'EVENT_2500_remove_from_current_level_3',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_13]
    },
    {
        "identifier": 'EVENT_2500_remove_from_current_level_4',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_14]
    },
    {
        "identifier": 'EVENT_2500_remove_from_current_level_5',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_15]
    },
    {
        "identifier": 'EVENT_2500_remove_from_current_level_6',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_16]
    },
    {
        "identifier": 'EVENT_2500_pause_7',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'EVENT_2500_run_background_event_8',
        "command": 'run_background_event',
        "args": [2501, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_2500_summon_to_current_level_9',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_2500_summon_to_current_level_10',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_2500_summon_to_current_level_11',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_2500_summon_to_current_level_12',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2500_summon_to_current_level_13',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_2500_summon_to_current_level_14',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_2500_summon_to_current_level_15',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_2500_summon_to_current_level_16',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_2500_summon_to_current_level_17',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_2500_summon_to_current_level_18',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_2500_summon_to_current_level_19',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_2500_summon_to_current_level_20',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_11]
    },
    {
        "identifier": 'EVENT_2500_pause_21',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_2500_db_22',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2500_apply_tile_mod_23',
        "command": 'apply_tile_mod',
        "args": [Rooms._261_BOWSERS_KEEP_1ST_TIME_AREA_03_LAVA_ROOM_WBRIDGE, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2500_pause_24',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2500_db_25',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2500_apply_tile_mod_26',
        "command": 'apply_tile_mod',
        "args": [Rooms._261_BOWSERS_KEEP_1ST_TIME_AREA_03_LAVA_ROOM_WBRIDGE, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2500_pause_27',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2500_db_28',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2500_apply_tile_mod_29',
        "command": 'apply_tile_mod',
        "args": [Rooms._261_BOWSERS_KEEP_1ST_TIME_AREA_03_LAVA_ROOM_WBRIDGE, 2, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2500_pause_30',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2500_db_31',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2500_apply_tile_mod_32',
        "command": 'apply_tile_mod',
        "args": [Rooms._261_BOWSERS_KEEP_1ST_TIME_AREA_03_LAVA_ROOM_WBRIDGE, 3, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2500_pause_33',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2500_db_34',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2500_apply_tile_mod_35',
        "command": 'apply_tile_mod',
        "args": [Rooms._261_BOWSERS_KEEP_1ST_TIME_AREA_03_LAVA_ROOM_WBRIDGE, 4, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2500_pause_36',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2500_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2500_action_queue_sync_37_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2500_action_queue_sync_37_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2500_action_queue_sync_37_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2500_action_queue_sync_37_SUBSCRIPT_shift_north_pixels_3',
                "command": 'shift_north_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2500_action_queue_sync_37_SUBSCRIPT_jmp_if_bit_set_4',
                "command": 'jmp_if_bit_set',
                "args": [0x7043, 1, 'EVENT_2500_action_queue_sync_37_SUBSCRIPT_set_animation_speed_6']
            },
            {
                "identifier": 'EVENT_2500_action_queue_sync_37_SUBSCRIPT_jmp_5',
                "command": 'jmp',
                "args": ['EVENT_2500_action_queue_sync_37_SUBSCRIPT_set_animation_speed_0']
            },
            {
                "identifier": 'EVENT_2500_action_queue_sync_37_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2500_action_queue_async_38',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2500_action_queue_async_38_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2500_action_queue_async_38_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2500_action_queue_async_38_SUBSCRIPT_jmp_if_bit_set_2',
                "command": 'jmp_if_bit_set',
                "args": [0x7043, 1, 'EVENT_2500_action_queue_async_38_SUBSCRIPT_pause_4']
            },
            {
                "identifier": 'EVENT_2500_action_queue_async_38_SUBSCRIPT_jmp_3',
                "command": 'jmp',
                "args": ['EVENT_2500_action_queue_async_38_SUBSCRIPT_set_sprite_sequence_0']
            },
            {
                "identifier": 'EVENT_2500_action_queue_async_38_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [32]
            }
        ]
    },
    {
        "identifier": 'EVENT_2500_apply_solidity_mod_39',
        "command": 'apply_solidity_mod',
        "args": [Rooms._261_BOWSERS_KEEP_1ST_TIME_AREA_03_LAVA_ROOM_WBRIDGE, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_2500_set_action_script_async_40',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2500_ret_41',
        "command": 'ret'
    }
]
