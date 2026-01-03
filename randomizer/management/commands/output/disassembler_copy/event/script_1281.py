
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1281_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR, RadialDirections.NORTHEAST, 4, 19, 0, []]
    },
    {
        "identifier": 'EVENT_1281_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1281_action_queue_sync_1_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_1281_action_queue_sync_1_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [7, 13, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1281_action_queue_sync_1_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1281_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1281_action_queue_sync_2_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1281_action_queue_sync_2_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1281_action_queue_sync_2_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1281_action_queue_sync_2_SUBSCRIPT_shift_west_pixels_3',
                "command": 'shift_west_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1281_action_queue_sync_2_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1281_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1281_action_queue_async_3_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [4, 20, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1281_action_queue_async_3_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1281_action_queue_async_3_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1281_action_queue_async_3_SUBSCRIPT_set_priority_3',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_1281_fade_in_from_black_async_4',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1281_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1281_action_queue_async_5_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_1281_pause_6',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1281_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1281_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, 1, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_1281_action_queue_async_7_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1281_action_queue_async_7_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1281_action_queue_async_7_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1281_action_queue_async_7_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1281_action_queue_async_7_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1281_pause_8',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1281_run_dialog_9',
        "command": 'run_dialog',
        "args": [2827, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1281_fade_out_music_to_volume_10',
        "command": 'fade_out_music_to_volume',
        "args": [1, 0]
    },
    {
        "identifier": 'EVENT_1281_pause_11',
        "command": 'pause',
        "args": [45]
    },
    {
        "identifier": 'EVENT_1281_freeze_camera_12',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_1281_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1281_action_queue_async_13_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1281_action_queue_async_13_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1281_action_queue_async_13_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1281_action_queue_async_13_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1281_action_queue_async_13_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._005_BLOCK_SWITCH, 4]
            },
            {
                "identifier": 'EVENT_1281_action_queue_async_13_SUBSCRIPT_shift_northeast_pixels_5',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1281_action_queue_async_13_SUBSCRIPT_shift_southwest_pixels_6',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1281_action_queue_async_13_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._005_BLOCK_SWITCH, 4]
            },
            {
                "identifier": 'EVENT_1281_action_queue_async_13_SUBSCRIPT_shift_northeast_pixels_8',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1281_action_queue_async_13_SUBSCRIPT_shift_southwest_pixels_9',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1281_action_queue_async_13_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._005_BLOCK_SWITCH, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1281_pause_14',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1281_run_dialog_15',
        "command": 'run_dialog',
        "args": [2828, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1281_pause_16',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1281_enter_area_17',
        "command": 'enter_area',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, RadialDirections.NORTHEAST, 3, 26, 0, []]
    },
    {
        "identifier": 'EVENT_1281_set_short_18',
        "command": 'set_short',
        "args": [0x7026, 0x0000]
    },
    {
        "identifier": 'EVENT_1281_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1281_action_queue_sync_19_SUBSCRIPT_shift_south_pixels_0',
                "command": 'shift_south_pixels',
                "args": [22]
            },
            {
                "identifier": 'EVENT_1281_action_queue_sync_19_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1281_action_queue_sync_19_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1281_action_queue_sync_19_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_1281_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1281_action_queue_sync_20_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1281_action_queue_sync_20_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1281_action_queue_sync_20_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1281_action_queue_sync_20_SUBSCRIPT_set_priority_3',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1281_action_queue_sync_20_SUBSCRIPT_shadow_on_4',
                "command": 'shadow_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1281_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.LAYER_1],
        "subscript": [
            {
                "identifier": 'EVENT_1281_action_queue_async_21_SUBSCRIPT_shift_east_pixels_0',
                "command": 'shift_east_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1281_action_queue_async_21_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_1281_apply_solidity_mod_22',
        "command": 'apply_solidity_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 2, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_1281_jmp_23',
        "command": 'jmp',
        "args": ['EVENT_1364_freeze_camera_6']
    }
]
