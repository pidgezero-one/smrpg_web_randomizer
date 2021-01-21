from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2433_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 0, 'EVENT_2433_clear_bit_11']
    },
    {
        "identifier": 'EVENT_2433_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 1, 'EVENT_2433_clear_bit_11']
    },
    {
        "identifier": 'EVENT_2433_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 2, 'EVENT_2433_clear_bit_11']
    },
    {
        "identifier": 'EVENT_2433_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 3, 'EVENT_2433_clear_bit_11']
    },
    {
        "identifier": 'EVENT_2433_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 4, 'EVENT_2433_clear_bit_23']
    },
    {
        "identifier": 'EVENT_2433_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 6, 'EVENT_2433_clear_bit_11']
    },
    {
        "identifier": 'EVENT_2433_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 7, 'EVENT_2433_clear_bit_11']
    },
    {
        "identifier": 'EVENT_2433_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7046, 0, 'EVENT_2433_clear_bit_26']
    },
    {
        "identifier": 'EVENT_2433_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7046, 1, 'EVENT_2433_set_bit_9']
    },
    {
        "identifier": 'EVENT_2433_set_bit_9',
        "command": 'set_bit',
        "args": [0x7045, 6]
    },
    {
        "identifier": 'EVENT_2433_jmp_10',
        "command": 'jmp',
        "args": ['EVENT_2433_clear_bit_12']
    },
    {
        "identifier": 'EVENT_2433_clear_bit_11',
        "command": 'clear_bit',
        "args": [0x7045, 6]
    },
    {
        "identifier": 'EVENT_2433_clear_bit_12',
        "command": 'clear_bit',
        "args": [0x7045, 0]
    },
    {
        "identifier": 'EVENT_2433_clear_bit_13',
        "command": 'clear_bit',
        "args": [0x7045, 1]
    },
    {
        "identifier": 'EVENT_2433_clear_bit_14',
        "command": 'clear_bit',
        "args": [0x7045, 2]
    },
    {
        "identifier": 'EVENT_2433_clear_bit_15',
        "command": 'clear_bit',
        "args": [0x7045, 3]
    },
    {
        "identifier": 'EVENT_2433_clear_bit_16',
        "command": 'clear_bit',
        "args": [0x7045, 4]
    },
    {
        "identifier": 'EVENT_2433_set_bit_17',
        "command": 'set_bit',
        "args": [0x7045, 5]
    },
    {
        "identifier": 'EVENT_2433_clear_bit_18',
        "command": 'clear_bit',
        "args": [0x7045, 7]
    },
    {
        "identifier": 'EVENT_2433_clear_bit_19',
        "command": 'clear_bit',
        "args": [0x7046, 0]
    },
    {
        "identifier": 'EVENT_2433_clear_bit_20',
        "command": 'clear_bit',
        "args": [0x7046, 1]
    },
    {
        "identifier": 'EVENT_2433_enter_area_21',
        "command": 'enter_area',
        "args": [Rooms._230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09, RadialDirections.NORTHWEST, 8, 61, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2433_ret_22',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2433_clear_bit_23',
        "command": 'clear_bit',
        "args": [0x7045, 4]
    },
    {
        "identifier": 'EVENT_2433_enter_area_24',
        "command": 'enter_area',
        "args": [Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD, RadialDirections.NORTHWEST, 16, 40, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2433_ret_25',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2433_clear_bit_26',
        "command": 'clear_bit',
        "args": [0x7046, 0]
    },
    {
        "identifier": 'EVENT_2433_enter_area_27',
        "command": 'enter_area',
        "args": [Rooms._231_FOREST_MAZE_SECRET_ENTRANCE, RadialDirections.NORTHWEST, 21, 76, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2433_ret_28',
        "command": 'ret'
    }
]
