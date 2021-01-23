from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3819_restore_all_hp_0',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_3819_restore_all_fp_1',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_3819_enter_area_2',
        "command": 'enter_area',
        "args": [Rooms._189_MARIOS_PIPEHOUSE, RadialDirections.SOUTHEAST, 3, 13, 0, []]
    },
    {
        "identifier": 'EVENT_3819_palette_set_3',
        "command": 'palette_set',
        "args": [33, 7, [0]]
    },
    {
        "identifier": 'EVENT_3819_stop_music_FDA2_4',
        "command": 'stop_music_FDA2'
    },
    {
        "identifier": 'EVENT_3819_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3819_action_queue_async_5_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_5_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [3, 9, 3, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_5_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_5_SUBSCRIPT_shift_z_up_pixels_3',
                "command": 'shift_z_up_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_5_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_5_SUBSCRIPT_shadow_off_6',
                "command": 'shadow_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3819_set_action_script_sync_6',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 95]
    },
    {
        "identifier": 'EVENT_3819_freeze_camera_7',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_3819_fade_in_from_black_async_8',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3819_play_music_default_volume_9',
        "command": 'play_music_default_volume',
        "args": [Music._14_MARIOS_PAD]
    },
    {
        "identifier": 'EVENT_3819_pause_10',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3819_set_7000_to_tapped_button_11',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_3819_pause_12',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3819_mem_7000_and_const_13',
        "command": 'mem_7000_and_const',
        "args": [0x0080]
    },
    {
        "identifier": 'EVENT_3819_jmp_if_7000_equals_short_14',
        "command": 'jmp_if_7000_equals_short',
        "args": [128, 'EVENT_3819_pause_action_script_16']
    },
    {
        "identifier": 'EVENT_3819_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_3819_set_7000_to_tapped_button_11']
    },
    {
        "identifier": 'EVENT_3819_pause_action_script_16',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_3819_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3819_action_queue_async_17_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_17_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_17_SUBSCRIPT_sequence_playback_on_2',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_17_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_17_SUBSCRIPT_shadow_on_4',
                "command": 'shadow_on'
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_17_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_17_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [69]
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_17_SUBSCRIPT_floating_on_7',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_17_SUBSCRIPT_shift_southeast_steps_8',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_17_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_17_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._056_SHAKE_HEAD, 6]
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_17_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_17_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_17_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_17_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_17_SUBSCRIPT_stop_sound_15',
                "command": 'stop_sound'
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_17_SUBSCRIPT_reset_properties_16',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_17_SUBSCRIPT_set_animation_speed_17',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3819_ret_18',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3819_ret_19',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3819_ret_20',
        "command": 'ret'
    }
]
