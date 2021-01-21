from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1563_set_7016_to_object_xyz_0',
        "command": 'set_7016_to_object_xyz',
        "args": [0x94]
    },
    {
        "identifier": 'EVENT_1563_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._034_SQUIRM_WRITHE, 4]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._034_SQUIRM_WRITHE, 4]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._034_SQUIRM_WRITHE, 4]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_reset_properties_12',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_play_sound_14',
                "command": 'play_sound',
                "args": [Sounds._034_SQUIRM_WRITHE, 4]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_start_loop_n_times_15',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_turn_clockwise_45_degrees_n_times_16',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_end_loop_18',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_set_sprite_sequence_19',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_start_loop_n_times_20',
                "command": 'start_loop_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_play_sound_21',
                "command": 'play_sound',
                "args": [Sounds._043_POP_UP_FROM_WATER, 6]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_end_loop_23',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_set_animation_speed_24',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_set_sprite_sequence_25',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_play_sound_26',
                "command": 'play_sound',
                "args": [Sounds._024_TAPPING_FEET, 4]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_pause_27',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_set_animation_speed_28',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_reset_properties_29',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_jump_to_height_30',
                "command": 'jump_to_height',
                "args": [112]
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_run_away_shift_31',
                "command": 'run_away_shift'
            },
            {
                "identifier": 'EVENT_1563_action_queue_async_1_SUBSCRIPT_set_animation_speed_32',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1563_ret_2',
        "command": 'ret'
    }
]
