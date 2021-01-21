from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_439_stop_all_background_events_0',
        "command": 'stop_all_background_events'
    },
    {
        "identifier": 'EVENT_439_start_battle_1',
        "command": 'start_battle',
        "args": [0x001e, 21]
    },
    {
        "identifier": 'EVENT_439_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [440]
    },
    {
        "identifier": 'EVENT_439_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_439_action_queue_async_7']
    },
    {
        "identifier": 'EVENT_439_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_287_reset_and_choose_game_0']
    },
    {
        "identifier": 'EVENT_439_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_439_action_queue_async_5_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [10, 10, 2, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_439_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_439_jmp_if_bit_clear_8']
    },
    {
        "identifier": 'EVENT_439_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_439_action_queue_async_7_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [8, 13, 4, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_439_jmp_if_bit_clear_8',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 1, 'EVENT_439_fade_in_from_black_async_10']
    },
    {
        "identifier": 'EVENT_439_set_temp_action_script_sync_9',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 2]
    },
    {
        "identifier": 'EVENT_439_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_439_jmp_11',
        "command": 'jmp',
        "args": ['EVENT_436_action_queue_async_13']
    }
]
