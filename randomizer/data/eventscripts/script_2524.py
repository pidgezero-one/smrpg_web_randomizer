from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2524_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_2524_action_queue_sync_0_SUBSCRIPT_shift_east_pixels_0',
                "command": 'shift_east_pixels',
                "args": [7]
            }
        ]
    },
    {
        "identifier": 'EVENT_2524_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_17],
        "subscript": [
            {
                "identifier": 'EVENT_2524_action_queue_sync_1_SUBSCRIPT_shift_east_pixels_0',
                "command": 'shift_east_pixels',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_2524_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_18],
        "subscript": [
            {
                "identifier": 'EVENT_2524_action_queue_sync_2_SUBSCRIPT_shift_west_pixels_0',
                "command": 'shift_west_pixels',
                "args": [9]
            }
        ]
    },
    {
        "identifier": 'EVENT_2524_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_19],
        "subscript": [
            {
                "identifier": 'EVENT_2524_action_queue_sync_3_SUBSCRIPT_shift_west_pixels_0',
                "command": 'shift_west_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2524_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_20],
        "subscript": [
            {
                "identifier": 'EVENT_2524_action_queue_sync_4_SUBSCRIPT_shift_west_pixels_0',
                "command": 'shift_west_pixels',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_2524_freeze_camera_5',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2524_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2524_action_queue_async_6_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [14, 22]
            },
            {
                "identifier": 'EVENT_2524_action_queue_async_6_SUBSCRIPT_overwrite_solidity_1',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2524_action_queue_async_6_SUBSCRIPT_floating_off_2',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2524_action_queue_async_6_SUBSCRIPT_shadow_off_3',
                "command": 'shadow_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2524_fade_in_from_black_async_7',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2524_pause_8',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2524_db_9',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2524_apply_tile_mod_10',
        "command": 'apply_tile_mod',
        "args": [Rooms._157_STAR_HILL_AREA_03, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2524_play_sound_11',
        "command": 'play_sound',
        "args": [Sounds._126_EMERGE_DEEP_WATER, 6]
    },
    {
        "identifier": 'EVENT_2524_pause_12',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2524_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2524_action_queue_async_13_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2524_action_queue_async_13_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_2524_pause_14',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2524_db_15',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2524_apply_tile_mod_16',
        "command": 'apply_tile_mod',
        "args": [Rooms._157_STAR_HILL_AREA_03, 13, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2524_play_sound_17',
        "command": 'play_sound',
        "args": [Sounds._125_ENTER_DEEP_WATER, 6]
    },
    {
        "identifier": 'EVENT_2524_set_action_script_async_18',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2524_unfreeze_camera_19',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2524_ret_20',
        "command": 'ret'
    }
]
