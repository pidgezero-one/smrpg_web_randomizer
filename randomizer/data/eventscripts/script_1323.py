from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1323_run_dialog_0',
        "command": 'run_dialog',
        "args": [2560, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1323_pause_1',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1323_start_battle_2',
        "command": 'start_battle',
        "args": [0x008e, 12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1323_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_1323_remove_from_current_level_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1323_reset_and_choose_game_4',
        "command": 'reset_and_choose_game',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1323_remove_from_current_level_5',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1323_remove_from_level_6',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1323_fade_in_from_black_async_7',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1323_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
