from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2405_summon_to_level_0',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._158_STAR_HILL_AREA_02]
    },
    {
        "identifier": 'EVENT_2405_summon_to_level_1',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._158_STAR_HILL_AREA_02]
    },
    {
        "identifier": 'EVENT_2405_summon_to_level_2',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_7, Rooms._158_STAR_HILL_AREA_02]
    },
    {
        "identifier": 'EVENT_2405_summon_to_level_3',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_8, Rooms._158_STAR_HILL_AREA_02]
    },
    {
        "identifier": 'EVENT_2405_summon_to_level_4',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._157_STAR_HILL_AREA_03]
    },
    {
        "identifier": 'EVENT_2405_summon_to_level_5',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_7, Rooms._157_STAR_HILL_AREA_03]
    },
    {
        "identifier": 'EVENT_2405_summon_to_level_6',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_8, Rooms._157_STAR_HILL_AREA_03]
    },
    {
        "identifier": 'EVENT_2405_summon_to_level_7',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_9, Rooms._157_STAR_HILL_AREA_03]
    },
    {
        "identifier": 'EVENT_2405_summon_to_level_8',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._159_STAR_HILL_AREA_04]
    },
    {
        "identifier": 'EVENT_2405_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2405_action_queue_sync_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2405_action_queue_sync_9_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_2405_action_queue_sync_9_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2405_action_queue_sync_9_SUBSCRIPT_shadow_off_3',
                "command": 'shadow_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2405_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_2405_action_queue_sync_10_SUBSCRIPT_shift_west_pixels_0',
                "command": 'shift_west_pixels',
                "args": [7]
            }
        ]
    },
    {
        "identifier": 'EVENT_2405_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2405_action_queue_sync_11_SUBSCRIPT_shift_east_pixels_0',
                "command": 'shift_east_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2405_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_14],
        "subscript": [
            {
                "identifier": 'EVENT_2405_action_queue_sync_12_SUBSCRIPT_shift_west_pixels_0',
                "command": 'shift_west_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2405_freeze_camera_13',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2405_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2405_action_queue_async_14_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [27, 108]
            },
            {
                "identifier": 'EVENT_2405_action_queue_async_14_SUBSCRIPT_overwrite_solidity_1',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2405_action_queue_async_14_SUBSCRIPT_floating_off_2',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2405_action_queue_async_14_SUBSCRIPT_shadow_off_3',
                "command": 'shadow_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2405_fade_in_from_black_async_15',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2405_pause_16',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2405_db_17',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2405_apply_tile_mod_18',
        "command": 'apply_tile_mod',
        "args": [Rooms._159_STAR_HILL_AREA_04, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2405_play_sound_19',
        "command": 'play_sound',
        "args": [Sounds._126_EMERGE_DEEP_WATER, 6]
    },
    {
        "identifier": 'EVENT_2405_pause_20',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2405_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2405_action_queue_async_21_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2405_action_queue_async_21_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_2405_pause_22',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2405_db_23',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2405_apply_tile_mod_24',
        "command": 'apply_tile_mod',
        "args": [Rooms._159_STAR_HILL_AREA_04, 13, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2405_play_sound_25',
        "command": 'play_sound',
        "args": [Sounds._125_ENTER_DEEP_WATER, 6]
    },
    {
        "identifier": 'EVENT_2405_set_action_script_async_26',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2405_unfreeze_camera_27',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2405_ret_28',
        "command": 'ret'
    }
]
