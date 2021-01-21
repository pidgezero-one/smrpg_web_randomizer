from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2108_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2108_action_queue_async_0_SUBSCRIPT_shift_south_pixels_0',
                "command": 'shift_south_pixels',
                "args": [7]
            }
        ]
    },
    {
        "identifier": 'EVENT_2108_palette_set_1',
        "command": 'palette_set',
        "args": [84, 1]
    },
    {
        "identifier": 'EVENT_2108_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7092, 7, 'EVENT_2108_action_queue_async_13']
    },
    {
        "identifier": 'EVENT_2108_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 4, 'EVENT_2108_play_music_default_volume_19']
    },
    {
        "identifier": 'EVENT_2108_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7090, 1, 'EVENT_2108_play_music_default_volume_7']
    },
    {
        "identifier": 'EVENT_2108_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7092, 6, 'EVENT_2108_play_music_default_volume_7']
    },
    {
        "identifier": 'EVENT_2108_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2108_action_queue_async_6_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2108_action_queue_async_6_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2108_action_queue_async_6_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2108_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2108_action_queue_async_6_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2108_play_music_default_volume_7',
        "command": 'play_music_default_volume',
        "args": [Music._61_VALENTINA]
    },
    {
        "identifier": 'EVENT_2108_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_2108_run_event_as_subroutine_17']
    },
    {
        "identifier": 'EVENT_2108_fade_in_from_black_async_9',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2108_ret_10',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2108_play_music_default_volume_11',
        "command": 'play_music_default_volume',
        "args": [Music._61_VALENTINA]
    },
    {
        "identifier": 'EVENT_2108_jmp_if_bit_set_12',
        "command": 'jmp_if_bit_set',
        "args": [0x7093, 1, 'EVENT_2108_jmp_if_bit_set_14']
    },
    {
        "identifier": 'EVENT_2108_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2108_action_queue_async_13_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [19, 16]
            },
            {
                "identifier": 'EVENT_2108_action_queue_async_13_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2108_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2108_action_queue_async_13_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2108_jmp_if_bit_set_14',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_2108_run_event_as_subroutine_17']
    },
    {
        "identifier": 'EVENT_2108_fade_in_from_black_async_15',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2108_ret_16',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2108_run_event_as_subroutine_17',
        "command": 'run_event_as_subroutine',
        "args": [81]
    },
    {
        "identifier": 'EVENT_2108_ret_18',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2108_play_music_default_volume_19',
        "command": 'play_music_default_volume',
        "args": [Music._50_NIMBUS_LAND]
    },
    {
        "identifier": 'EVENT_2108_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_2108_jmp_if_bit_set_14']
    },
    {
        "identifier": 'EVENT_2108_ret_21',
        "command": 'ret'
    }
]
