from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_438_stop_all_background_events_0',
        "command": 'stop_all_background_events',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_438_start_battle_1',
        "command": 'start_battle',
        "args": [0x001f, 21],
        "subscript": []
    },
    {
        "identifier": 'EVENT_438_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [440],
        "subscript": []
    },
    {
        "identifier": 'EVENT_438_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_438_action_queue_async_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_438_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_287_reset_and_choose_game_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_438_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_438_action_queue_async_5_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [8, 13, 4, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_438_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_438_set_bit_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_438_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_438_action_queue_async_7_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [7, 16, 2, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_438_set_bit_8',
        "command": 'set_bit',
        "args": [0x7049, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_438_run_event_as_subroutine_9',
        "command": 'run_event_as_subroutine',
        "args": [276],
        "subscript": []
    },
    {
        "identifier": 'EVENT_438_jmp_if_bit_clear_10',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 1, 'EVENT_438_fade_in_from_black_async_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_438_set_temp_action_script_sync_11',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_438_fade_in_from_black_async_12',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_438_jmp_13',
        "command": 'jmp',
        "args": ['EVENT_436_action_queue_async_13'],
        "subscript": []
    },
]
