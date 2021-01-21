from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2482_jmp_if_random_above_128_0',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2482_start_battle_3']
    },
    {
        "identifier": 'EVENT_2482_start_battle_1',
        "command": 'start_battle',
        "args": [0x0058, 41]
    },
    {
        "identifier": 'EVENT_2482_jmp_2',
        "command": 'jmp',
        "args": ['EVENT_2482_jmp_if_bit_set_4']
    },
    {
        "identifier": 'EVENT_2482_start_battle_3',
        "command": 'start_battle',
        "args": [0x0059, 41]
    },
    {
        "identifier": 'EVENT_2482_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_2482_set_temp_action_script_sync_12']
    },
    {
        "identifier": 'EVENT_2482_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_2482_reset_and_choose_game_15']
    },
    {
        "identifier": 'EVENT_2482_remove_from_level_6',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA]
    },
    {
        "identifier": 'EVENT_2482_remove_from_level_7',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_10, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA]
    },
    {
        "identifier": 'EVENT_2482_remove_from_current_level_8',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_2482_remove_from_current_level_9',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_2482_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2482_ret_11',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2482_set_temp_action_script_sync_12',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_10, 2]
    },
    {
        "identifier": 'EVENT_2482_fade_in_from_black_async_13',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2482_ret_14',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2482_reset_and_choose_game_15',
        "command": 'reset_and_choose_game'
    },
    {
        "identifier": 'EVENT_2482_ret_16',
        "command": 'ret'
    }
]
