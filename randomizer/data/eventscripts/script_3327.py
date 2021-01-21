from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3327_stop_all_background_events_0',
        "command": 'stop_all_background_events'
    },
    {
        "identifier": 'EVENT_3327_start_battle_1',
        "command": 'start_battle',
        "args": [0x0090, 20]
    },
    {
        "identifier": 'EVENT_3327_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_3327_set_temp_action_script_sync_13']
    },
    {
        "identifier": 'EVENT_3327_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_3327_reset_and_choose_game_22']
    },
    {
        "identifier": 'EVENT_3327_move_script_to_main_thread_4',
        "command": 'move_script_to_main_thread'
    },
    {
        "identifier": 'EVENT_3327_set_action_script_async_5',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_0, 1023]
    },
    {
        "identifier": 'EVENT_3327_set_action_script_async_6',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_1, 1023]
    },
    {
        "identifier": 'EVENT_3327_set_action_script_async_7',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_2, 1023]
    },
    {
        "identifier": 'EVENT_3327_set_action_script_async_8',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_3, 1023]
    },
    {
        "identifier": 'EVENT_3327_set_action_script_async_9',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_4, 1023]
    },
    {
        "identifier": 'EVENT_3327_set_action_script_async_10',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_5, 1023]
    },
    {
        "identifier": 'EVENT_3327_fade_in_from_black_async_11',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3327_ret_12',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3327_set_temp_action_script_sync_13',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_0, 2]
    },
    {
        "identifier": 'EVENT_3327_set_temp_action_script_sync_14',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_1, 2]
    },
    {
        "identifier": 'EVENT_3327_set_temp_action_script_sync_15',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_2, 2]
    },
    {
        "identifier": 'EVENT_3327_set_temp_action_script_sync_16',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_3, 2]
    },
    {
        "identifier": 'EVENT_3327_set_temp_action_script_sync_17',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_4, 2]
    },
    {
        "identifier": 'EVENT_3327_set_temp_action_script_sync_18',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_5, 2]
    },
    {
        "identifier": 'EVENT_3327_run_background_event_19',
        "command": 'run_background_event',
        "args": [3326, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_3327_fade_in_from_black_async_20',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3327_ret_21',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3327_reset_and_choose_game_22',
        "command": 'reset_and_choose_game'
    }
]
