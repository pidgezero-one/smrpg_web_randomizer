from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2430_run_event_as_subroutine_0',
        "command": 'run_event_as_subroutine',
        "args": [3588]
    },
    {
        "identifier": 'EVENT_2430_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x708c, 6, 'EVENT_2430_clear_bit_3']
    },
    {
        "identifier": 'EVENT_2430_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2430_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2430_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7045, 0]
    },
    {
        "identifier": 'EVENT_2430_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7045, 1]
    },
    {
        "identifier": 'EVENT_2430_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7045, 2]
    },
    {
        "identifier": 'EVENT_2430_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x7045, 3]
    },
    {
        "identifier": 'EVENT_2430_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7045, 4]
    },
    {
        "identifier": 'EVENT_2430_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7045, 5]
    },
    {
        "identifier": 'EVENT_2430_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7045, 6]
    },
    {
        "identifier": 'EVENT_2430_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7045, 7]
    },
    {
        "identifier": 'EVENT_2430_clear_bit_11',
        "command": 'clear_bit',
        "args": [0x7046, 0]
    },
    {
        "identifier": 'EVENT_2430_set_bit_12',
        "command": 'set_bit',
        "args": [0x7046, 1]
    },
    {
        "identifier": 'EVENT_2430_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2430_action_queue_async_13_SUBSCRIPT_shift_south_pixels_0',
                "command": 'shift_south_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2430_jmp_if_bit_clear_14',
        "command": 'jmp_if_bit_clear',
        "args": [0x7047, 0, 'EVENT_2430_jmp_if_bit_clear_27']
    },
    {
        "identifier": 'EVENT_2430_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2430_action_queue_async_15_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2430_freeze_all_npcs_until_return_16',
        "command": 'freeze_all_npcs_until_return'
    },
    {
        "identifier": 'EVENT_2430_fade_in_from_black_async_17',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2430_freeze_camera_18',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2430_set_action_script_async_19',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 482]
    },
    {
        "identifier": 'EVENT_2430_set_action_script_async_20',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2430_unfreeze_camera_21',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2430_unfreeze_all_npcs_22',
        "command": 'unfreeze_all_npcs'
    },
    {
        "identifier": 'EVENT_2430_jmp_if_bit_clear_23',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_2430_jmp_26']
    },
    {
        "identifier": 'EVENT_2430_jmp_if_bit_set_24',
        "command": 'jmp_if_bit_set',
        "args": [0x708c, 6, 'EVENT_2430_jmp_26']
    },
    {
        "identifier": 'EVENT_2430_pause_25',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2430_jmp_26',
        "command": 'jmp',
        "args": ['EVENT_2430_jmp_if_bit_clear_30']
    },
    {
        "identifier": 'EVENT_2430_jmp_if_bit_clear_27',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 7, 'EVENT_2430_fade_in_from_black_async_29']
    },
    {
        "identifier": 'EVENT_2430_jmp_to_event_28',
        "command": 'jmp_to_event',
        "args": [81]
    },
    {
        "identifier": 'EVENT_2430_fade_in_from_black_async_29',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2430_jmp_if_bit_clear_30',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_2430_clear_bit_34']
    },
    {
        "identifier": 'EVENT_2430_jmp_if_bit_set_31',
        "command": 'jmp_if_bit_set',
        "args": [0x708c, 6, 'EVENT_2430_clear_bit_34']
    },
    {
        "identifier": 'EVENT_2430_clear_bit_32',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_2430_play_sound_33',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6]
    },
    {
        "identifier": 'EVENT_2430_clear_bit_34',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_2430_ret_35',
        "command": 'ret'
    }
]
