from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3605_set_bit_0',
        "command": 'set_bit',
        "args": [0x7044, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3605_set_short_1',
        "command": 'set_short',
        "args": [0x7016, 0x0007],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3605_set_short_2',
        "command": 'set_short',
        "args": [0x7018, 0x0032],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3605_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [66],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3605_enter_area_4',
        "command": 'enter_area',
        "args": [Rooms._125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES, RadialDirections.NORTHEAST, 0, 79, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3605_enable_controls_until_return_5',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3605_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3605_action_queue_async_6_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xc8, 0x00]
            },
            {
                "identifier": 'EVENT_3605_action_queue_async_6_SUBSCRIPT_add_short_1',
                "command": 'add_short',
                "args": [0x701a, 0x0900]
            },
            {
                "identifier": 'EVENT_3605_action_queue_async_6_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x99]
            },
            {
                "identifier": 'EVENT_3605_action_queue_async_6_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_3605_fade_in_from_black_async_7',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3605_pause_8',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3605_jmp_if_mario_in_air_9',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3605_pause_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3605_run_event_as_subroutine_10',
        "command": 'run_event_as_subroutine',
        "args": [3588],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3605_jmp_if_bit_clear_11',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3605_jmp_if_object_trigger_enabled_12',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_9, Rooms._125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES, 'EVENT_3605_clear_bit_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3605_jmp_if_object_trigger_enabled_13',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_10, Rooms._125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES, 'EVENT_3605_clear_bit_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3605_jmp_14',
        "command": 'jmp',
        "args": ['EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3605_clear_bit_15',
        "command": 'clear_bit',
        "args": [0x7099, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3605_play_sound_16',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3605_ret_17',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
