
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2308_remove_from_level_0',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._100_BOOSTER_PASS_AREA_01]
    },
    {
        "identifier": 'EVENT_2308_remove_from_level_1',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._100_BOOSTER_PASS_AREA_01]
    },
    {
        "identifier": 'EVENT_2308_remove_from_level_2',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._100_BOOSTER_PASS_AREA_01]
    },
    {
        "identifier": 'EVENT_2308_run_background_event_3',
        "command": 'run_background_event',
        "args": [2309, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_2308_jmp_if_object_not_in_level_4',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_9, Rooms._100_BOOSTER_PASS_AREA_01, 'EVENT_2308_action_queue_async_6']
    },
    {
        "identifier": 'EVENT_2308_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2308_action_queue_sync_5_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2308_action_queue_sync_5_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2308_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2308_action_queue_async_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2308_action_queue_async_6_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2308_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2308_jmp_if_bit_clear_7',
        "command": 'jmp_if_bit_clear',
        "args": [0x708d, 1, 'EVENT_2308_fade_in_from_black_async_18']
    },
    {
        "identifier": 'EVENT_2308_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2308_action_queue_async_8_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2308_remove_from_current_level_9',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_2308_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2308_set_action_script_async_11',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 397]
    },
    {
        "identifier": 'EVENT_2308_pause_12',
        "command": 'pause',
        "args": [64]
    },
    {
        "identifier": 'EVENT_2308_set_action_script_async_13',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 384]
    },
    {
        "identifier": 'EVENT_2308_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2308_action_queue_async_14_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2308_set_action_script_async_15',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2308_clear_bit_16',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_2308_ret_17',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2308_fade_in_from_black_async_18',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2308_run_event_as_subroutine_19',
        "command": 'run_event_as_subroutine',
        "args": [3588]
    },
    {
        "identifier": 'EVENT_2308_jmp_if_bit_clear_20',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_2308_clear_bit_29']
    },
    {
        "identifier": 'EVENT_2308_jmp_if_bit_set_21',
        "command": 'jmp_if_bit_set',
        "args": [0x7059, 2, 'EVENT_2308_jmp_if_bit_set_25']
    },
    {
        "identifier": 'EVENT_2308_clear_bit_22',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_2308_play_sound_23',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6]
    },
    {
        "identifier": 'EVENT_2308_ret_24',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2308_jmp_if_bit_set_25',
        "command": 'jmp_if_bit_set',
        "args": [0x7059, 3, 'EVENT_2308_clear_bit_29']
    },
    {
        "identifier": 'EVENT_2308_clear_bit_26',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_2308_play_sound_27',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6]
    },
    {
        "identifier": 'EVENT_2308_ret_28',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2308_clear_bit_29',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_2308_ret_30',
        "command": 'ret'
    }
]
