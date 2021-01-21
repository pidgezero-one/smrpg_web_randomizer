from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3361_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._448_BOWSERS_KEEP_AREA_09_TALL_ROOM_WSAVE_POINT, RadialDirections.SOUTHEAST, 2, 42, 10, []]
    },
    {
        "identifier": 'EVENT_3361_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3361_action_queue_async_1_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_1_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_1_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3361_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [15]
    },
    {
        "identifier": 'EVENT_3361_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_jmp_if_bit_set_0',
                "command": 'jmp_if_bit_set',
                "args": [0x7055, 5, 'EVENT_3361_action_queue_async_3_SUBSCRIPT_set_solidity_bits_19']
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_start_loop_n_times_10',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_end_loop_14',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_face_northwest_17',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_reset_properties_18',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_set_solidity_bits_19',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_floating_on_20',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_jump_to_height_silent_21',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_play_sound_22',
                "command": 'play_sound',
                "args": [Sounds._019_LONG_FALL, 4]
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_pause_23',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_jmp_if_mario_in_air_24',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3361_action_queue_async_3_SUBSCRIPT_pause_23']
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_play_sound_25',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_set_bit_26',
                "command": 'set_bit',
                "args": [0x7055, 5]
            },
            {
                "identifier": 'EVENT_3361_action_queue_async_3_SUBSCRIPT_set_animation_speed_27',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3361_ret_4',
        "command": 'ret'
    }
]
