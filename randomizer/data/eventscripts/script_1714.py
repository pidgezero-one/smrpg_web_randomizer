from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1714_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1714_action_queue_sync_0_SUBSCRIPT_shift_west_pixels_0',
                "command": 'shift_west_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_1714_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7077, 0, 'EVENT_1714_set_bit_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1714_jmp_to_event_2',
        "command": 'jmp_to_event',
        "args": [14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1714_set_bit_3',
        "command": 'set_bit',
        "args": [0x7077, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1714_fade_in_from_black_sync_4',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1714_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1714_action_queue_async_5_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_5_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_5_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1714_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_1714_action_queue_sync_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1714_summon_to_current_level_at_marios_coords_7',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1714_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1714_action_queue_async_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_8_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_8_SUBSCRIPT_walk_1_step_southeast_2',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_8_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_8_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_8_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_8_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_8_SUBSCRIPT_reset_properties_7',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_8_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_8_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_8_SUBSCRIPT_reset_properties_10',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_8_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_8_SUBSCRIPT_walk_1_step_northeast_12',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_8_SUBSCRIPT_face_northwest_13',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_8_SUBSCRIPT_sequence_looping_on_14',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1714_run_dialog_9',
        "command": 'run_dialog',
        "args": [1064, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1714_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1714_action_queue_sync_10_SUBSCRIPT_walk_1_step_southwest_0',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1714_action_queue_sync_10_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1714_action_queue_sync_10_SUBSCRIPT_sequence_looping_off_2',
                "command": 'sequence_looping_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1714_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1714_action_queue_async_11_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_11_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_11_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_11_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_11_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_11_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_11_SUBSCRIPT_sequence_looping_on_6',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1714_run_dialog_12',
        "command": 'run_dialog',
        "args": [1056, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1714_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1714_action_queue_sync_13_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1714_action_queue_sync_13_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1714_action_queue_sync_13_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1714_action_queue_sync_13_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_1714_action_queue_sync_13_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1714_action_queue_sync_13_SUBSCRIPT_shift_south_steps_5',
                "command": 'shift_south_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1714_action_queue_sync_13_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_1714_action_queue_sync_13_SUBSCRIPT_jump_to_height_7',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1714_action_queue_sync_13_SUBSCRIPT_shift_southeast_steps_8',
                "command": 'shift_southeast_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1714_action_queue_sync_13_SUBSCRIPT_object_memory_modify_bits_9',
                "command": 'object_memory_modify_bits',
                "args": [0x09, [5], [4, 6]]
            },
            {
                "identifier": 'EVENT_1714_action_queue_sync_13_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1714_action_queue_sync_13_SUBSCRIPT_shift_east_steps_11',
                "command": 'shift_east_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1714_action_queue_sync_13_SUBSCRIPT_visibility_off_12',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1714_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1714_action_queue_async_14_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_14_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_14_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_14_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_14_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_14_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_14_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_14_SUBSCRIPT_shift_north_steps_7',
                "command": 'shift_north_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_14_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1714_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_1714_ret_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1714_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1714_action_queue_async_16_SUBSCRIPT_walk_1_step_northwest_0',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_16_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1714_action_queue_async_16_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1714_ret_17',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
