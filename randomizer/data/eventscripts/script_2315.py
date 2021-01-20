from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2315_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 0, 'EVENT_2315_jmp_if_bit_set_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2315_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2315_action_queue_sync_1_SUBSCRIPT_shift_z_up_steps_0',
                "command": 'shift_z_up_steps',
                "args": [15]
            },
        ]
    },
    {
        "identifier": 'EVENT_2315_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2315_action_queue_sync_2_SUBSCRIPT_shift_z_up_steps_0',
                "command": 'shift_z_up_steps',
                "args": [11]
            },
            {
                "identifier": 'EVENT_2315_action_queue_sync_2_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_2315_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2315_action_queue_sync_3_SUBSCRIPT_shift_z_up_steps_0',
                "command": 'shift_z_up_steps',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_2315_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2315_action_queue_sync_4_SUBSCRIPT_shift_z_up_steps_0',
                "command": 'shift_z_up_steps',
                "args": [15]
            },
        ]
    },
    {
        "identifier": 'EVENT_2315_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2315_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2315_action_queue_sync_5_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2315_action_queue_sync_5_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [15]
            },
        ]
    },
    {
        "identifier": 'EVENT_2315_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2315_action_queue_sync_6_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2315_action_queue_sync_6_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2315_action_queue_sync_6_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2315_action_queue_sync_6_SUBSCRIPT_shift_z_up_steps_3',
                "command": 'shift_z_up_steps',
                "args": [11]
            },
        ]
    },
    {
        "identifier": 'EVENT_2315_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2315_action_queue_sync_7_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2315_action_queue_sync_7_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2315_action_queue_sync_7_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [7]
            },
        ]
    },
    {
        "identifier": 'EVENT_2315_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2315_action_queue_async_8_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2315_action_queue_async_8_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2315_action_queue_async_8_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [15]
            },
        ]
    },
    {
        "identifier": 'EVENT_2315_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 0, 'EVENT_2315_freeze_camera_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2315_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2315_jmp_11',
        "command": 'jmp',
        "args": ['EVENT_2315_run_event_as_subroutine_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2315_freeze_camera_12',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2315_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2315_action_queue_async_13_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2315_action_queue_async_13_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2315_action_queue_async_13_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2315_fade_in_from_black_async_14',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2315_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2315_action_queue_sync_15_SUBSCRIPT_shift_south_steps_0',
                "command": 'shift_south_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2315_action_queue_sync_15_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2315_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2315_action_queue_sync_16_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2315_action_queue_sync_16_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2315_action_queue_sync_16_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_2315_action_queue_sync_16_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0xc0, 0x00, 0x60, 0x00]
            },
            {
                "identifier": 'EVENT_2315_action_queue_sync_16_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x25, 0x00, 0x0a, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2315_action_queue_sync_16_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_2315_action_queue_sync_16_SUBSCRIPT_bpl_26_27_28_6',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_2315_action_queue_sync_16_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            },
        ]
    },
    {
        "identifier": 'EVENT_2315_stop_embedded_action_script_17',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2315_set_action_script_async_18',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2315_stop_embedded_action_script_19',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2315_run_event_as_subroutine_20',
        "command": 'run_event_as_subroutine',
        "args": [3588],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2315_jmp_if_bit_clear_21',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_2315_unfreeze_camera_27'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2315_jmp_if_bit_set_22',
        "command": 'jmp_if_bit_set',
        "args": [0x708d, 4, 'EVENT_2315_unfreeze_camera_27'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2315_jmp_if_bit_clear_23',
        "command": 'jmp_if_bit_clear',
        "args": [0x7045, 0, 'EVENT_2315_clear_bit_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2315_pause_24',
        "command": 'pause',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2315_clear_bit_25',
        "command": 'clear_bit',
        "args": [0x7099, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2315_play_sound_26',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2315_unfreeze_camera_27',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2315_enable_controls_28',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2315_clear_bit_29',
        "command": 'clear_bit',
        "args": [0x7099, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2315_clear_bit_30',
        "command": 'clear_bit',
        "args": [0x7045, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2315_ret_31',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
