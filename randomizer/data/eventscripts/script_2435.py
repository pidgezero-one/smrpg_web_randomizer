from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2435_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 0, 'EVENT_2435_clear_bit_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 1, 'EVENT_2435_clear_bit_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 2, 'EVENT_2435_clear_bit_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 3, 'EVENT_2435_clear_bit_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 4, 'EVENT_2435_clear_bit_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 6, 'EVENT_2435_set_bit_19'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 7, 'EVENT_2435_set_bit_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7046, 0, 'EVENT_2435_clear_bit_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7045, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7045, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7045, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_clear_bit_11',
        "command": 'clear_bit',
        "args": [0x7045, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_clear_bit_12',
        "command": 'clear_bit',
        "args": [0x7045, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_clear_bit_13',
        "command": 'clear_bit',
        "args": [0x7045, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_clear_bit_14',
        "command": 'clear_bit',
        "args": [0x7045, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_clear_bit_15',
        "command": 'clear_bit',
        "args": [0x7046, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_clear_bit_16',
        "command": 'clear_bit',
        "args": [0x7046, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_enter_area_17',
        "command": 'enter_area',
        "args": [Rooms._227_FOREST_MAZE_AREA_09_LEADS_TO_4PATH_MAZE, RadialDirections.SOUTHWEST, 16, 18, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_ret_18',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_set_bit_19',
        "command": 'set_bit',
        "args": [0x7045, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_clear_bit_20',
        "command": 'clear_bit',
        "args": [0x7045, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_enter_area_21',
        "command": 'enter_area',
        "args": [Rooms._230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09, RadialDirections.SOUTHWEST, 9, 46, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_ret_22',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_set_bit_23',
        "command": 'set_bit',
        "args": [0x7046, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_clear_bit_24',
        "command": 'clear_bit',
        "args": [0x7045, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_enter_area_25',
        "command": 'enter_area',
        "args": [Rooms._230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09, RadialDirections.SOUTHWEST, 8, 47, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2435_ret_26',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
