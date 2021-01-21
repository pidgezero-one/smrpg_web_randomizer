from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2050_add_0',
        "command": 'add',
        "args": [0x70bd, 0x01]
    },
    {
        "identifier": 'EVENT_2050_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2050_action_queue_async_1_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2050_action_queue_async_1_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2050_action_queue_async_1_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2050_action_queue_async_1_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2050_action_queue_async_1_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2050_action_queue_async_1_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2050_action_queue_async_1_SUBSCRIPT_shift_z_up_steps_6',
                "command": 'shift_z_up_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2050_action_queue_async_1_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2050_action_queue_async_1_SUBSCRIPT_shift_z_up_steps_8',
                "command": 'shift_z_up_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2050_action_queue_async_1_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2050_action_queue_async_1_SUBSCRIPT_shift_z_up_steps_10',
                "command": 'shift_z_up_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2050_action_queue_async_1_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2050_action_queue_async_1_SUBSCRIPT_shift_z_down_steps_12',
                "command": 'shift_z_down_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2050_action_queue_async_1_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2050_action_queue_async_1_SUBSCRIPT_shift_z_down_steps_14',
                "command": 'shift_z_down_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_2050_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2050_action_queue_sync_2_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [108]
            }
        ]
    },
    {
        "identifier": 'EVENT_2050_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2050_action_queue_sync_3_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [108]
            }
        ]
    },
    {
        "identifier": 'EVENT_2050_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2050_action_queue_sync_4_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [108]
            }
        ]
    },
    {
        "identifier": 'EVENT_2050_play_sound_5',
        "command": 'play_sound',
        "args": [Sounds._073_THWOMP_STOMP, 6]
    },
    {
        "identifier": 'EVENT_2050_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2050_action_queue_async_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2050_action_queue_async_6_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [22]
            },
            {
                "identifier": 'EVENT_2050_action_queue_async_6_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [22]
            },
            {
                "identifier": 'EVENT_2050_action_queue_async_6_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_2050_action_queue_async_6_SUBSCRIPT_shift_north_pixels_4',
                "command": 'shift_north_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_2050_action_queue_async_6_SUBSCRIPT_shift_south_pixels_5',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2050_action_queue_async_6_SUBSCRIPT_shift_north_pixels_6',
                "command": 'shift_north_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2050_jmp_if_var_equals_byte_7',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70bd, 7, 'EVENT_2050_run_dialog_20']
    },
    {
        "identifier": 'EVENT_2050_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_2050_ret_22']
    },
    {
        "identifier": 'EVENT_2050_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2050_action_queue_async_9_SUBSCRIPT_stop_sound_0',
                "command": 'stop_sound'
            },
            {
                "identifier": 'EVENT_2050_action_queue_async_9_SUBSCRIPT_stop_sound_1',
                "command": 'stop_sound'
            },
            {
                "identifier": 'EVENT_2050_action_queue_async_9_SUBSCRIPT_stop_sound_2',
                "command": 'stop_sound'
            }
        ]
    },
    {
        "identifier": 'EVENT_2050_jmp_if_bit_clear_10',
        "command": 'jmp_if_bit_clear',
        "args": [0x704f, 3, 'EVENT_1771_fade_in_from_black_async_7']
    },
    {
        "identifier": 'EVENT_2050_jmp_11',
        "command": 'jmp',
        "args": ['EVENT_1771_apply_solidity_mod_3']
    },
    {
        "identifier": 'EVENT_2050_run_dialog_12',
        "command": 'run_dialog',
        "args": [2963, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2050_ret_13',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2050_run_dialog_14',
        "command": 'run_dialog',
        "args": [2960, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2050_ret_15',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2050_run_dialog_16',
        "command": 'run_dialog',
        "args": [2961, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2050_ret_17',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2050_run_dialog_18',
        "command": 'run_dialog',
        "args": [2962, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2050_ret_19',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2050_run_dialog_20',
        "command": 'run_dialog',
        "args": [2963, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2050_set_bit_21',
        "command": 'set_bit',
        "args": [0x7088, 6]
    },
    {
        "identifier": 'EVENT_2050_ret_22',
        "command": 'ret'
    }
]
