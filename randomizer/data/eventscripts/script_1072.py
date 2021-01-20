from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1072_play_music_default_volume_0',
        "command": 'play_music_default_volume',
        "args": [Music._17_TADPOLE_POND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_deactivate_sound_channels_1',
        "command": 'deactivate_sound_channels',
        "args": [[0, 1, 2, 3]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7054, 6, 'EVENT_1072_action_queue_async_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1072_action_queue_async_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1072_action_queue_async_3_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1072_action_queue_async_3_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1072_action_queue_async_3_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1072_action_queue_async_3_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_1072_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7051, 4, 'EVENT_1072_clear_bit_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x7057, 4, 'EVENT_1072_set_bit_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x7054, 5, 'EVENT_1072_clear_bit_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_jmp_if_bit_clear_7',
        "command": 'jmp_if_bit_clear',
        "args": [0x7089, 0, 'EVENT_1072_set_bit_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_1072_clear_bit_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_set_bit_9',
        "command": 'set_bit',
        "args": [0x7052, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_remove_from_current_level_10',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_jmp_if_bit_set_11',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_1072_clear_bit_24'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_fade_in_from_black_async_12',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_ret_13',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_clear_bit_14',
        "command": 'clear_bit',
        "args": [0x7052, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_1072_clear_bit_24'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_fade_in_from_black_async_16',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_ret_17',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1072_action_queue_async_18_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [15, 27]
            },
            {
                "identifier": 'EVENT_1072_action_queue_async_18_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1072_action_queue_async_18_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1072_action_queue_async_18_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1072_action_queue_async_18_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1072_action_queue_async_18_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1072_clear_bit_19',
        "command": 'clear_bit',
        "args": [0x7052, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_deactivate_sound_channels_20',
        "command": 'deactivate_sound_channels',
        "args": [[0, 1, 2, 3]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_jmp_if_bit_set_21',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_1072_clear_bit_24'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_fade_in_from_black_async_22',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_ret_23',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_clear_bit_24',
        "command": 'clear_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_clear_bit_25',
        "command": 'clear_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_clear_bit_26',
        "command": 'clear_bit',
        "args": [0x7043, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_clear_bit_27',
        "command": 'clear_bit',
        "args": [0x7043, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_clear_bit_28',
        "command": 'clear_bit',
        "args": [0x7043, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_clear_bit_29',
        "command": 'clear_bit',
        "args": [0x7043, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_clear_bit_30',
        "command": 'clear_bit',
        "args": [0x7043, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_clear_bit_31',
        "command": 'clear_bit',
        "args": [0x7043, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_run_event_as_subroutine_32',
        "command": 'run_event_as_subroutine',
        "args": [81],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1072_ret_33',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
