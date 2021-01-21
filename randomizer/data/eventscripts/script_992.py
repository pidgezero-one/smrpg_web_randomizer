from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_992_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._243_GAME_INTRO_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM, RadialDirections.NORTHEAST, 13, 35, 0, []]
    },
    {
        "identifier": 'EVENT_992_freeze_camera_1',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_992_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 790]
    },
    {
        "identifier": 'EVENT_992_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 790]
    },
    {
        "identifier": 'EVENT_992_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 791]
    },
    {
        "identifier": 'EVENT_992_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 791]
    },
    {
        "identifier": 'EVENT_992_set_action_script_sync_6',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 791]
    },
    {
        "identifier": 'EVENT_992_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 790]
    },
    {
        "identifier": 'EVENT_992_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.SCREEN_FOCUS, 792]
    },
    {
        "identifier": 'EVENT_992_pause_9',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_992_fade_in_from_black_sync_10',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_992_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_992_action_queue_sync_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_11_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_11_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_11_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_11_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_11_SUBSCRIPT_start_loop_n_times_5',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_11_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_11_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_11_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_11_SUBSCRIPT_end_loop_10',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_992_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_992_action_queue_sync_12_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_12_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_12_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_12_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [90]
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_12_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_12_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_12_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_992_remember_last_object_13',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_992_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_992_action_queue_sync_14_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_14_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_14_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_14_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_14_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_14_SUBSCRIPT_jmp_if_mario_in_air_5',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_992_action_queue_sync_14_SUBSCRIPT_pause_4']
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_14_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_14_SUBSCRIPT_shift_southwest_steps_7',
                "command": 'shift_southwest_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_14_SUBSCRIPT_clear_solidity_bits_8',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_14_SUBSCRIPT_shift_southwest_steps_9',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_992_action_queue_sync_14_SUBSCRIPT_visibility_off_10',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_992_pause_15',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'EVENT_992_fade_out_to_black_sync_duration_16',
        "command": 'fade_out_to_black_sync_duration',
        "args": [30]
    },
    {
        "identifier": 'EVENT_992_pause_script_until_effect_done_17',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_992_remember_last_object_18',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_992_jmp_to_event_19',
        "command": 'jmp_to_event',
        "args": [130]
    }
]
