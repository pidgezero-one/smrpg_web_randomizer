from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1397_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1397_action_queue_async_0_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1397_pause_1',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1397_run_dialog_2',
        "command": 'run_dialog',
        "args": [2763, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1397_pause_3',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1397_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 146]
    },
    {
        "identifier": 'EVENT_1397_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_bounce_to_xy_with_height_3',
                "command": 'bounce_to_xy_with_height',
                "args": [3, 18, 0]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_jump_to_height_7',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_shift_southeast_steps_8',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_shift_southeast_pixels_9',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_face_northeast_11',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_floating_off_15',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_shift_northeast_steps_16',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_shift_northeast_pixels_17',
                "command": 'shift_northeast_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_19',
                "command": 'set_sprite_sequence',
                "args": [23, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_21',
                "command": 'set_sprite_sequence',
                "args": [24, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_23',
                "command": 'set_sprite_sequence',
                "args": [9, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_reset_properties_25',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_face_northeast_26',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_fixed_f_coord_on_27',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_jump_to_height_28',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_set_animation_speed_29',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_shift_southwest_steps_30',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_set_solidity_bits_31',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_floating_on_32',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_fixed_f_coord_off_33',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_set_animation_speed_34',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_pause_35',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_face_northwest_36',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_pause_37',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_set_animation_speed_38',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_39',
                "command": 'set_sprite_sequence',
                "args": [4, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_pause_40',
                "command": 'pause',
                "args": [70]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_reset_properties_41',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_5_SUBSCRIPT_set_animation_speed_42',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1397_pause_6',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1397_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1397_action_queue_async_7_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_7_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_7_SUBSCRIPT_sequence_looping_off_2',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1397_run_dialog_8',
        "command": 'run_dialog',
        "args": [2764, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1397_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1397_action_queue_async_9_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_9_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_9_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_9_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_9_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_9_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._016_OPEN_DOOR, 4]
            },
            {
                "identifier": 'EVENT_1397_action_queue_async_9_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1397_remove_from_current_level_10',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1397_set_bit_11',
        "command": 'set_bit',
        "args": [0x7053, 2]
    },
    {
        "identifier": 'EVENT_1397_ret_12',
        "command": 'ret'
    }
]
