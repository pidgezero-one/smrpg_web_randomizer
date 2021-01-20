from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2113_fade_in_from_black_sync_duration_0',
        "command": 'fade_in_from_black_sync_duration',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2113_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2113_action_queue_sync_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2113_action_queue_sync_1_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2113_action_queue_sync_1_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2113_action_queue_sync_1_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2113_action_queue_sync_1_SUBSCRIPT_end_loop_4',
                "command": 'end_loop',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2113_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2113_action_queue_async_2_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_2_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_2_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_2_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_2_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_2_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2113_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2113_action_queue_async_3_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_3_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_3_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_3_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_3_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_3_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_3_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_3_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_3_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_3_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [90]
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_3_SUBSCRIPT_fixed_f_coord_off_10',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_3_SUBSCRIPT_sequence_looping_off_11',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_3_SUBSCRIPT_reset_properties_12',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_3_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_3_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_3_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_3_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_3_SUBSCRIPT_set_sprite_sequence_17',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_3_SUBSCRIPT_shift_northwest_steps_18',
                "command": 'shift_northwest_steps',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2113_action_queue_async_3_SUBSCRIPT_visibility_off_19',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2113_pause_4',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2113_play_sound_5',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2113_pause_6',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2113_set_bit_7',
        "command": 'set_bit',
        "args": [0x7092, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2113_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
