from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1648_set_0',
        "command": 'set',
        "args": [0x70df, 24]
    },
    {
        "identifier": 'EVENT_1648_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'EVENT_1648_set_bit_15']
    },
    {
        "identifier": 'EVENT_1648_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_1648_fade_in_from_black_sync_9']
    },
    {
        "identifier": 'EVENT_1648_fade_in_from_black_async_3',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1648_start_loop_n_times_4',
        "command": 'start_loop_n_times',
        "args": [249]
    },
    {
        "identifier": 'EVENT_1648_play_sound_5',
        "command": 'play_sound',
        "args": [Sounds._001_MENU_SELECT, 6]
    },
    {
        "identifier": 'EVENT_1648_pause_6',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'EVENT_1648_end_loop_7',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1648_ret_8',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1648_fade_in_from_black_sync_9',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_1648_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1648_action_queue_async_10_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1648_action_queue_async_10_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [192]
            },
            {
                "identifier": 'EVENT_1648_action_queue_async_10_SUBSCRIPT_walk_1_step_south_2',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_1648_action_queue_async_10_SUBSCRIPT_floating_on_3',
                "command": 'floating_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1648_pause_11',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1648_jmp_if_mario_in_air_12',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1648_pause_11']
    },
    {
        "identifier": 'EVENT_1648_play_sound_13',
        "command": 'play_sound',
        "args": [Sounds._058_INSERT, 6]
    },
    {
        "identifier": 'EVENT_1648_ret_14',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1648_set_bit_15',
        "command": 'set_bit',
        "args": [0x707a, 6]
    },
    {
        "identifier": 'EVENT_1648_jmp_if_bit_set_16',
        "command": 'jmp_if_bit_set',
        "args": [0x707a, 5, 'EVENT_1648_clear_bit_18']
    },
    {
        "identifier": 'EVENT_1648_jmp_to_event_17',
        "command": 'jmp_to_event',
        "args": [1651]
    },
    {
        "identifier": 'EVENT_1648_clear_bit_18',
        "command": 'clear_bit',
        "args": [0x707a, 7]
    },
    {
        "identifier": 'EVENT_1648_enter_area_19',
        "command": 'enter_area',
        "args": [Rooms._108_MOLEVILLE_OUTSIDE, RadialDirections.SOUTHWEST, 28, 39, 4, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_1648_ret_20',
        "command": 'ret'
    }
]
