from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1895_run_event_as_subroutine_0',
        "command": 'run_event_as_subroutine',
        "args": [65],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1895_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7095, 7, 'EVENT_1895_set_bit_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1895_enter_area_2',
        "command": 'enter_area',
        "args": [Rooms._239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER, RadialDirections.SOUTH, 29, 37, 10, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1895_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1895_set_bit_4',
        "command": 'set_bit',
        "args": [0x7096, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1895_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 5, 'EVENT_1895_enter_area_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1895_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 4, 'EVENT_1895_enter_area_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1895_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 3, 'EVENT_1895_enter_area_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1895_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 2, 'EVENT_1895_enter_area_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1895_enter_area_9',
        "command": 'enter_area',
        "args": [Rooms._475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS, RadialDirections.SOUTH, 22, 116, 10, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1895_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1895_enter_area_11',
        "command": 'enter_area',
        "args": [Rooms._475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS, RadialDirections.SOUTH, 27, 86, 9, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1895_ret_12',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1895_enter_area_13',
        "command": 'enter_area',
        "args": [Rooms._475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS, RadialDirections.SOUTH, 19, 82, 12, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1895_ret_14',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1895_enter_area_15',
        "command": 'enter_area',
        "args": [Rooms._475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS, RadialDirections.SOUTH, 25, 72, 12, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1895_ret_16',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1895_enter_area_17',
        "command": 'enter_area',
        "args": [Rooms._475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS, RadialDirections.SOUTH, 28, 106, 9, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1895_ret_18',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
