from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2432_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 0, 'EVENT_2432_set_bit_14']
    },
    {
        "identifier": 'EVENT_2432_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 1, 'EVENT_2432_set_bit_18']
    },
    {
        "identifier": 'EVENT_2432_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 3, 'EVENT_2432_set_bit_22']
    },
    {
        "identifier": 'EVENT_2432_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7045, 0]
    },
    {
        "identifier": 'EVENT_2432_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7045, 1]
    },
    {
        "identifier": 'EVENT_2432_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7045, 2]
    },
    {
        "identifier": 'EVENT_2432_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x7045, 3]
    },
    {
        "identifier": 'EVENT_2432_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7045, 4]
    },
    {
        "identifier": 'EVENT_2432_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7045, 6]
    },
    {
        "identifier": 'EVENT_2432_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7045, 7]
    },
    {
        "identifier": 'EVENT_2432_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7046, 0]
    },
    {
        "identifier": 'EVENT_2432_clear_bit_11',
        "command": 'clear_bit',
        "args": [0x7046, 1]
    },
    {
        "identifier": 'EVENT_2432_enter_area_12',
        "command": 'enter_area',
        "args": [Rooms._230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09, RadialDirections.NORTHEAST, 3, 61, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2432_ret_13',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2432_set_bit_14',
        "command": 'set_bit',
        "args": [0x7045, 1]
    },
    {
        "identifier": 'EVENT_2432_clear_bit_15',
        "command": 'clear_bit',
        "args": [0x7045, 0]
    },
    {
        "identifier": 'EVENT_2432_enter_area_16',
        "command": 'enter_area',
        "args": [Rooms._230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09, RadialDirections.NORTHEAST, 3, 61, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2432_ret_17',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2432_set_bit_18',
        "command": 'set_bit',
        "args": [0x7045, 2]
    },
    {
        "identifier": 'EVENT_2432_clear_bit_19',
        "command": 'clear_bit',
        "args": [0x7045, 1]
    },
    {
        "identifier": 'EVENT_2432_enter_area_20',
        "command": 'enter_area',
        "args": [Rooms._230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09, RadialDirections.NORTHEAST, 3, 61, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2432_ret_21',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2432_set_bit_22',
        "command": 'set_bit',
        "args": [0x7045, 4]
    },
    {
        "identifier": 'EVENT_2432_clear_bit_23',
        "command": 'clear_bit',
        "args": [0x7045, 3]
    },
    {
        "identifier": 'EVENT_2432_enter_area_24',
        "command": 'enter_area',
        "args": [Rooms._230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09, RadialDirections.NORTHEAST, 3, 61, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2432_ret_25',
        "command": 'ret'
    }
]
