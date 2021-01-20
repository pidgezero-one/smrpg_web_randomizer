from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3335_stop_all_background_events_0',
        "command": 'stop_all_background_events',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3335_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7076, 0, 'EVENT_3335_start_battle_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3335_jmp_to_event_2',
        "command": 'jmp_to_event',
        "args": [255],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3335_start_battle_3',
        "command": 'start_battle',
        "args": [0x0091, 20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3335_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_3335_set_temp_action_script_sync_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3335_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_3335_reset_and_choose_game_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3335_set_action_script_async_6',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MEM_70A8, 1023],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3335_remove_from_current_level_7',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3335_disable_trigger_8',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3335_pause_9',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3335_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3335_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3335_set_temp_action_script_sync_12',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3335_run_background_event_13',
        "command": 'run_background_event',
        "args": [3337, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3335_fade_in_from_black_async_14',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3335_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3335_reset_and_choose_game_16',
        "command": 'reset_and_choose_game',
        "args": [],
        "subscript": []
    }
]
