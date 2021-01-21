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
        "args": [AreaObjects.NPC_9, Rooms._100_BOOSTER_PASS_AREA_01, 'EVENT_2308_jmp_if_bit_clear_15']
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
        "identifier": 'EVENT_2308_stop_sound_6',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2308_stop_sound_7',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2308_stop_sound_8',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2308_stop_sound_9',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2308_stop_sound_10',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2308_stop_sound_11',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2308_stop_sound_12',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2308_stop_sound_13',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2308_stop_sound_14',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2308_jmp_if_bit_clear_15',
        "command": 'jmp_if_bit_clear',
        "args": [0x708d, 1, 'EVENT_2308_fade_in_from_black_async_26']
    },
    {
        "identifier": 'EVENT_2308_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2308_action_queue_async_16_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2308_remove_from_current_level_17',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_2308_fade_in_from_black_async_18',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2308_set_action_script_async_19',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 397]
    },
    {
        "identifier": 'EVENT_2308_pause_20',
        "command": 'pause',
        "args": [64]
    },
    {
        "identifier": 'EVENT_2308_set_action_script_async_21',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 384]
    },
    {
        "identifier": 'EVENT_2308_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2308_action_queue_async_22_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2308_set_action_script_async_23',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2308_clear_bit_24',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_2308_ret_25',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2308_fade_in_from_black_async_26',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2308_run_event_as_subroutine_27',
        "command": 'run_event_as_subroutine',
        "args": [3588]
    },
    {
        "identifier": 'EVENT_2308_jmp_if_bit_clear_28',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_2308_clear_bit_37']
    },
    {
        "identifier": 'EVENT_2308_jmp_if_bit_set_29',
        "command": 'jmp_if_bit_set',
        "args": [0x7059, 2, 'EVENT_2308_jmp_if_bit_set_33']
    },
    {
        "identifier": 'EVENT_2308_clear_bit_30',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_2308_play_sound_31',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6]
    },
    {
        "identifier": 'EVENT_2308_ret_32',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2308_jmp_if_bit_set_33',
        "command": 'jmp_if_bit_set',
        "args": [0x7059, 3, 'EVENT_2308_clear_bit_37']
    },
    {
        "identifier": 'EVENT_2308_clear_bit_34',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_2308_play_sound_35',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6]
    },
    {
        "identifier": 'EVENT_2308_ret_36',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2308_clear_bit_37',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_2308_ret_38',
        "command": 'ret'
    }
]
