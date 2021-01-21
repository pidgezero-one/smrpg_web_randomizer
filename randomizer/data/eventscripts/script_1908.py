from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1908_set_short_0',
        "command": 'set_short',
        "args": [0x700e, 0x00d6]
    },
    {
        "identifier": 'EVENT_1908_start_battle_700E_1',
        "command": 'start_battle_700E'
    },
    {
        "identifier": 'EVENT_1908_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_1904_fade_in_from_black_sync_15']
    },
    {
        "identifier": 'EVENT_1908_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_1695_reset_and_choose_game_12']
    },
    {
        "identifier": 'EVENT_1908_remove_from_current_level_4',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_1908_disable_trigger_5',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_1908_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1908_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 826]
    },
    {
        "identifier": 'EVENT_1908_ret_8',
        "command": 'ret'
    }
]
