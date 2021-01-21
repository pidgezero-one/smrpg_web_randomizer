from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2456_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7046, 7, 'EVENT_2456_ret_23']
    },
    {
        "identifier": 'EVENT_2456_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7047, 3, 'EVENT_2456_ret_23']
    },
    {
        "identifier": 'EVENT_2456_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7046, 7]
    },
    {
        "identifier": 'EVENT_2456_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7046, 5]
    },
    {
        "identifier": 'EVENT_2456_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7046, 6]
    },
    {
        "identifier": 'EVENT_2456_set_bit_5',
        "command": 'set_bit',
        "args": [0x7047, 3]
    },
    {
        "identifier": 'EVENT_2456_set_bit_6',
        "command": 'set_bit',
        "args": [0x7047, 0]
    },
    {
        "identifier": 'EVENT_2456_set_bit_7',
        "command": 'set_bit',
        "args": [0x7047, 4]
    },
    {
        "identifier": 'EVENT_2456_freeze_camera_8',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2456_remove_from_current_level_9',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_13]
    },
    {
        "identifier": 'EVENT_2456_remove_from_level_10',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_13, Rooms._242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS]
    },
    {
        "identifier": 'EVENT_2456_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2456_action_queue_async_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_11_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [0, 59]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_11_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2456_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 485]
    },
    {
        "identifier": 'EVENT_2456_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.SCREEN_FOCUS, 392]
    },
    {
        "identifier": 'EVENT_2456_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_shift_southeast_pixels_0',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [24, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._021_RUMBLING, 6]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [25, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_shift_north_pixels_7',
                "command": 'shift_north_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._021_RUMBLING, 6]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_end_loop_10',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [26, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_play_sound_12',
                "command": 'play_sound',
                "args": [Sounds._021_RUMBLING, 6]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [27, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_set_bit_15',
                "command": 'set_bit',
                "args": [0x7043, 0]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_play_sound_16',
                "command": 'play_sound',
                "args": [Sounds._021_RUMBLING, 6]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [29, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_play_sound_19',
                "command": 'play_sound',
                "args": [Sounds._021_RUMBLING, 6]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_shift_northwest_pixels_21',
                "command": 'shift_northwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_22',
                "command": 'set_sprite_sequence',
                "args": [30, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_play_sound_23',
                "command": 'play_sound',
                "args": [Sounds._021_RUMBLING, 6]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_25',
                "command": 'set_sprite_sequence',
                "args": [31, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2456_action_queue_async_14_SUBSCRIPT_play_sound_26',
                "command": 'play_sound',
                "args": [Sounds._021_RUMBLING, 6]
            }
        ]
    },
    {
        "identifier": 'EVENT_2456_pause_15',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_2456_fade_out_to_black_async_duration_16',
        "command": 'fade_out_to_black_async_duration',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2456_remove_from_level_17',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS]
    },
    {
        "identifier": 'EVENT_2456_apply_solidity_mod_18',
        "command": 'apply_solidity_mod',
        "args": [Rooms._225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_2456_apply_tile_mod_19',
        "command": 'apply_tile_mod',
        "args": [Rooms._225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2456_apply_solidity_mod_20',
        "command": 'apply_solidity_mod',
        "args": [Rooms._234_FOREST_MAZE_SECRET, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_2456_apply_solidity_mod_21',
        "command": 'apply_solidity_mod',
        "args": [Rooms._242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_2456_enter_area_22',
        "command": 'enter_area',
        "args": [Rooms._225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA, RadialDirections.SOUTH, 4, 74, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2456_ret_23',
        "command": 'ret'
    }
]
