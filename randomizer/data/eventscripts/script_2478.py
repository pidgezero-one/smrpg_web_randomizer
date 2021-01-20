from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2478_set_0',
        "command": 'set',
        "args": [0x70df, 39],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2478_summon_to_level_1',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2478_summon_to_level_2',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2478_summon_to_level_3',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2478_summon_to_level_4',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2478_summon_to_level_5',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2478_summon_to_level_6',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2478_summon_to_level_7',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_7, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2478_summon_to_level_8',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_9, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2478_summon_to_level_9',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_10, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2478_summon_to_level_10',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_11, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2478_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2478_action_queue_sync_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_11_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_11_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_11_SUBSCRIPT_shift_north_pixels_3',
                "command": 'shift_north_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_11_SUBSCRIPT_shift_west_pixels_4',
                "command": 'shift_west_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_11_SUBSCRIPT_jmp_if_bit_clear_5',
                "command": 'jmp_if_bit_clear',
                "args": [0x708c, 4, 'EVENT_2478_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_8']
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_11_SUBSCRIPT_ret_7',
                "command": 'ret',
                "args": []
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_11_SUBSCRIPT_visibility_off_9',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2478_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2478_action_queue_async_12_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2478_action_queue_async_12_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2478_action_queue_async_12_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_2478_action_queue_async_12_SUBSCRIPT_shift_east_pixels_3',
                "command": 'shift_east_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2478_action_queue_async_12_SUBSCRIPT_shift_north_pixels_4',
                "command": 'shift_north_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2478_action_queue_async_12_SUBSCRIPT_shift_west_pixels_5',
                "command": 'shift_west_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2478_action_queue_async_12_SUBSCRIPT_jmp_if_bit_clear_6',
                "command": 'jmp_if_bit_clear',
                "args": [0x708c, 4, 'EVENT_2478_action_queue_async_12_SUBSCRIPT_set_sprite_sequence_9']
            },
            {
                "identifier": 'EVENT_2478_action_queue_async_12_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2478_action_queue_async_12_SUBSCRIPT_ret_8',
                "command": 'ret',
                "args": []
            },
            {
                "identifier": 'EVENT_2478_action_queue_async_12_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2478_action_queue_async_12_SUBSCRIPT_visibility_off_10',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2478_jmp_if_bit_clear_13',
        "command": 'jmp_if_bit_clear',
        "args": [0x708c, 4, 'EVENT_2478_set_7000_to_object_coord_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2478_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2478_set_7000_to_object_coord_15',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Y, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2478_jmp_if_var_equals_short_16',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 27, 'EVENT_2478_freeze_camera_19'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2478_fade_in_from_black_async_17',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2478_ret_18',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2478_freeze_camera_19',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2478_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2478_action_queue_sync_20_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_20_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_20_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_20_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_20_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_20_SUBSCRIPT_overwrite_solidity_5',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_20_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_20_SUBSCRIPT_transfer_to_xyzf_7',
                "command": 'transfer_to_xyzf',
                "args": [27, 27, 24, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_20_SUBSCRIPT_shift_east_pixels_8',
                "command": 'shift_east_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_20_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2478_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2478_action_queue_async_21_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2478_action_queue_async_21_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [22, 5]
            },
            {
                "identifier": 'EVENT_2478_action_queue_async_21_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2478_fade_in_from_black_async_22',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2478_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2478_action_queue_async_23_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x01]
            },
            {
                "identifier": 'EVENT_2478_action_queue_async_23_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x24, 0xe3, 0xff, 0x00, 0x00]
            },
            {
                "identifier": 'EVENT_2478_action_queue_async_23_SUBSCRIPT_shift_z_down_steps_2',
                "command": 'shift_z_down_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2478_action_queue_async_23_SUBSCRIPT_bpl_26_27_28_3',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_2478_action_queue_async_23_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=6, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2478_action_queue_async_23_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [16]
            },
        ]
    },
    {
        "identifier": 'EVENT_2478_action_queue_sync_24',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2478_action_queue_sync_24_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_24_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_24_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 4]
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_24_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_24_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x24, 0x80, 0xfe, 0xb0, 0x00]
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_24_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_24_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [37]
            },
            {
                "identifier": 'EVENT_2478_action_queue_sync_24_SUBSCRIPT_bpl_26_27_28_7',
                "command": 'bpl_26_27_28',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2478_action_queue_async_25',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2478_action_queue_async_25_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2478_action_queue_async_25_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_2478_unfreeze_camera_26',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2478_set_action_script_async_27',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2478_ret_28',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
