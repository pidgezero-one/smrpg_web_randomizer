from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2121_stop_music_0',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_2121_enable_controls_until_return_1',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_2121_freeze_camera_2',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2121_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2121_action_queue_sync_3_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2121_action_queue_sync_3_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 6]
            },
            {
                "identifier": 'EVENT_2121_action_queue_sync_3_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2121_action_queue_sync_3_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2121_action_queue_sync_3_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2121_action_queue_sync_3_SUBSCRIPT_shift_southwest_pixels_5',
                "command": 'shift_southwest_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_2121_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2121_action_queue_sync_4_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_2121_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2121_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2121_action_queue_async_5_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_2121_action_queue_async_5_SUBSCRIPT_sequence_playback_on_1',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_2121_action_queue_async_5_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2121_action_queue_async_5_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2121_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2121_action_queue_async_5_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2121_action_queue_async_5_SUBSCRIPT_sequence_playback_off_6',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_2121_action_queue_async_5_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2121_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=2, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2121_action_queue_async_5_SUBSCRIPT_shift_southwest_steps_9',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2121_action_queue_async_5_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_2121_action_queue_async_5_SUBSCRIPT_sequence_playback_on_11',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_2121_action_queue_async_5_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2121_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2121_action_queue_async_5_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2121_action_queue_async_5_SUBSCRIPT_reset_properties_15',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2121_action_queue_async_5_SUBSCRIPT_sequence_looping_off_16',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_2121_action_queue_async_5_SUBSCRIPT_set_animation_speed_17',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2121_action_queue_async_5_SUBSCRIPT_set_animation_speed_18',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2121_action_queue_async_5_SUBSCRIPT_jump_to_height_19',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2121_action_queue_async_5_SUBSCRIPT_shift_northeast_steps_20',
                "command": 'shift_northeast_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_2121_pause_6',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'EVENT_2121_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2121_action_queue_async_7_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2121_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2121_action_queue_async_7_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [60]
            }
        ]
    },
    {
        "identifier": 'EVENT_2121_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2121_action_queue_sync_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2121_action_queue_sync_8_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2121_action_queue_sync_8_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [11]
            },
            {
                "identifier": 'EVENT_2121_action_queue_sync_8_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2121_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2121_action_queue_async_9_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_2121_action_queue_async_9_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2121_pause_10',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_2121_play_sound_11',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_2121_pause_12',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_2121_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'EVENT_2130_run_dialog_0']
    },
    {
        "identifier": 'EVENT_2121_run_dialog_14',
        "command": 'run_dialog',
        "args": [3349, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2121_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2121_action_queue_async_15_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2121_clear_bit_16',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_2121_clear_bit_17',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_2121_set_bit_18',
        "command": 'set_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'EVENT_2121_pause_19',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_2121_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_2131_pause_0']
    },
    {
        "identifier": 'EVENT_2121_ret_21',
        "command": 'ret'
    }
]
