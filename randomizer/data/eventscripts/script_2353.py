from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2353_set_7000_to_object_coord_0',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.NPC_8, Coords.F]
    },
    {
        "identifier": 'EVENT_2353_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3, 'EVENT_2353_stop_all_background_events_4']
    },
    {
        "identifier": 'EVENT_2353_run_dialog_2',
        "command": 'run_dialog',
        "args": [3072, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2353_ret_3',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2353_stop_all_background_events_4',
        "command": 'stop_all_background_events'
    },
    {
        "identifier": 'EVENT_2353_run_dialog_5',
        "command": 'run_dialog',
        "args": [3073, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2353_start_battle_6',
        "command": 'start_battle',
        "args": [0x008e, 12]
    },
    {
        "identifier": 'EVENT_2353_jmp_if_bit_clear_7',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_2353_remove_from_current_level_9']
    },
    {
        "identifier": 'EVENT_2353_reset_and_choose_game_8',
        "command": 'reset_and_choose_game'
    },
    {
        "identifier": 'EVENT_2353_remove_from_current_level_9',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_2353_remove_from_current_level_10',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_2353_remove_from_current_level_11',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_2353_remove_from_current_level_12',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2353_remove_from_current_level_13',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_2353_remove_from_current_level_14',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_2353_remove_from_level_15',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_8, Rooms._037_BOOSTER_TOWER_4F_3LEVEL_ROOM_WJUMPING_SPOOKUMS]
    },
    {
        "identifier": 'EVENT_2353_pause_16',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_2353_fade_in_from_black_async_17',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2353_ret_18',
        "command": 'ret'
    }
]
