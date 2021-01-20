from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3320_set_bit_0',
        "command": 'set_bit',
        "args": [0x7068, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3320_set_bit_1',
        "command": 'set_bit',
        "args": [0x7070, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3320_set_bit_2',
        "command": 'set_bit',
        "args": [0x7068, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3320_stop_all_background_events_3',
        "command": 'stop_all_background_events',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3320_db_4',
        "command": 'db',
        "args": [0xfd, 0x44],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3320_db_5',
        "command": 'db',
        "args": [0xfd, 0x45],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3320_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 1, 'EVENT_3320_jmp_to_event_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3320_set_bit_7',
        "command": 'set_bit',
        "args": [0x7042, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3320_remove_from_current_level_8',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3320_stop_music_9',
        "command": 'stop_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3320_run_event_as_subroutine_10',
        "command": 'run_event_as_subroutine',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3320_play_sound_11',
        "command": 'play_sound',
        "args": [Sounds._019_LONG_FALL, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3320_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3320_action_queue_sync_12_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3320_action_queue_sync_12_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3320_action_queue_sync_12_SUBSCRIPT_shift_south_steps_2',
                "command": 'shift_south_steps',
                "args": [17]
            },
        ]
    },
    {
        "identifier": 'EVENT_3320_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3320_action_queue_async_13_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3320_action_queue_async_13_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [9]
            },
        ]
    },
    {
        "identifier": 'EVENT_3320_pause_14',
        "command": 'pause',
        "args": [64],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3320_run_event_at_return_15',
        "command": 'run_event_at_return',
        "args": [3321],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3320_ret_16',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3320_jmp_to_event_17',
        "command": 'jmp_to_event',
        "args": [15],
        "subscript": []
    },
]
