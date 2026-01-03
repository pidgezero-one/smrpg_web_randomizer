
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_9_set_var_to_random_1',
        "command": 'set_var_to_random',
        "args": [0x7000, 46]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_0",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 0, "EVENT_9_set_0"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_1",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 1, "EVENT_9_set_1"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_2",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 2, "EVENT_9_set_2"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_3",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 3, "EVENT_9_set_3"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_4",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 4, "EVENT_9_set_4"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_5",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 5, "EVENT_9_set_5"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_6",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 6, "EVENT_9_set_6"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_7",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 7, "EVENT_9_set_7"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_8",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 8, "EVENT_9_set_8"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_9",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 9, "EVENT_9_set_9"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_10",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 10, "EVENT_9_set_10"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_11",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 11, "EVENT_9_set_11"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_12",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 12, "EVENT_9_set_12"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_13",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 13, "EVENT_9_set_13"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_14",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 14, "EVENT_9_set_14"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_15",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 15, "EVENT_9_set_15"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_16",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 16, "EVENT_9_set_16"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_17",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 17, "EVENT_9_set_17"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_18",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 18, "EVENT_9_set_18"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_19",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 19, "EVENT_9_set_19"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_20",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 20, "EVENT_9_set_20"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_21",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 21, "EVENT_9_set_21"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_22",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 22, "EVENT_9_set_22"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_23",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 23, "EVENT_9_set_23"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_24",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 24, "EVENT_9_set_24"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_25",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 25, "EVENT_9_set_25"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_26",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 26, "EVENT_9_set_26"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_27",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 27, "EVENT_9_set_27"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_28",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 28, "EVENT_9_set_28"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_29",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 29, "EVENT_9_set_29"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_30",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 30, "EVENT_9_set_30"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_31",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 31, "EVENT_9_set_31"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_32",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 32, "EVENT_9_set_32"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_33",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 33, "EVENT_9_set_33"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_34",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 34, "EVENT_9_set_34"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_35",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 35, "EVENT_9_set_35"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_36",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 36, "EVENT_9_set_36"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_37",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 37, "EVENT_9_set_37"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_38",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 38, "EVENT_9_set_38"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_39",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 39, "EVENT_9_set_39"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_40",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 40, "EVENT_9_set_40"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_41",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 41, "EVENT_9_set_41"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_42",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 42, "EVENT_9_set_42"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_43",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 43, "EVENT_9_set_43"]
    },
    {
        "identifier": "EVENT_9_jmp_if_7000_equals_short_44",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 44, "EVENT_9_set_44"]
    },
    {
        "identifier": "EVENT_9_set_45",
        "command": "set_var_to_const",
        "args": [0x70A7, 38]
    },
    {
        "identifier": "EVENT_9_ret_45",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_0",
        "command": "set_var_to_const",
        "args": [0x70A7, 61]
    },
    {
        "identifier": "EVENT_9_ret_0",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_1",
        "command": "set_var_to_const",
        "args": [0x70A7, 53]
    },
    {
        "identifier": "EVENT_9_ret_1",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_2",
        "command": "set_var_to_const",
        "args": [0x70A7, 51]
    },
    {
        "identifier": "EVENT_9_ret_2",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_3",
        "command": "set_var_to_const",
        "args": [0x70A7, 50]
    },
    {
        "identifier": "EVENT_9_ret_3",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_4",
        "command": "set_var_to_const",
        "args": [0x70A7, 23]
    },
    {
        "identifier": "EVENT_9_ret_4",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_5",
        "command": "set_var_to_const",
        "args": [0x70A7, 23]
    },
    {
        "identifier": "EVENT_9_ret_5",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_6",
        "command": "set_var_to_const",
        "args": [0x70A7, 76]
    },
    {
        "identifier": "EVENT_9_ret_6",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_7",
        "command": "set_var_to_const",
        "args": [0x70A7, 10]
    },
    {
        "identifier": "EVENT_9_ret_7",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_8",
        "command": "set_var_to_const",
        "args": [0x70A7, 8]
    },
    {
        "identifier": "EVENT_9_ret_8",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_9",
        "command": "set_var_to_const",
        "args": [0x70A7, 57]
    },
    {
        "identifier": "EVENT_9_ret_9",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_10",
        "command": "set_var_to_const",
        "args": [0x70A7, 46]
    },
    {
        "identifier": "EVENT_9_ret_10",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_11",
        "command": "set_var_to_const",
        "args": [0x70A7, 45]
    },
    {
        "identifier": "EVENT_9_ret_11",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_12",
        "command": "set_var_to_const",
        "args": [0x70A7, 67]
    },
    {
        "identifier": "EVENT_9_ret_12",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_13",
        "command": "set_var_to_const",
        "args": [0x70A7, 49]
    },
    {
        "identifier": "EVENT_9_ret_13",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_14",
        "command": "set_var_to_const",
        "args": [0x70A7, 15]
    },
    {
        "identifier": "EVENT_9_ret_14",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_15",
        "command": "set_var_to_const",
        "args": [0x70A7, 20]
    },
    {
        "identifier": "EVENT_9_ret_15",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_16",
        "command": "set_var_to_const",
        "args": [0x70A7, 83]
    },
    {
        "identifier": "EVENT_9_ret_16",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_17",
        "command": "set_var_to_const",
        "args": [0x70A7, 82]
    },
    {
        "identifier": "EVENT_9_ret_17",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_18",
        "command": "set_var_to_const",
        "args": [0x70A7, 79]
    },
    {
        "identifier": "EVENT_9_ret_18",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_19",
        "command": "set_var_to_const",
        "args": [0x70A7, 41]
    },
    {
        "identifier": "EVENT_9_ret_19",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_20",
        "command": "set_var_to_const",
        "args": [0x70A7, 87]
    },
    {
        "identifier": "EVENT_9_ret_20",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_21",
        "command": "set_var_to_const",
        "args": [0x70A7, 62]
    },
    {
        "identifier": "EVENT_9_ret_21",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_22",
        "command": "set_var_to_const",
        "args": [0x70A7, 42]
    },
    {
        "identifier": "EVENT_9_ret_22",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_23",
        "command": "set_var_to_const",
        "args": [0x70A7, 52]
    },
    {
        "identifier": "EVENT_9_ret_23",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_24",
        "command": "set_var_to_const",
        "args": [0x70A7, 6]
    },
    {
        "identifier": "EVENT_9_ret_24",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_25",
        "command": "set_var_to_const",
        "args": [0x70A7, 7]
    },
    {
        "identifier": "EVENT_9_ret_25",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_26",
        "command": "set_var_to_const",
        "args": [0x70A7, 11]
    },
    {
        "identifier": "EVENT_9_ret_26",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_27",
        "command": "set_var_to_const",
        "args": [0x70A7, 88]
    },
    {
        "identifier": "EVENT_9_ret_27",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_28",
        "command": "set_var_to_const",
        "args": [0x70A7, 86]
    },
    {
        "identifier": "EVENT_9_ret_28",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_29",
        "command": "set_var_to_const",
        "args": [0x70A7, 91]
    },
    {
        "identifier": "EVENT_9_ret_29",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_30",
        "command": "set_var_to_const",
        "args": [0x70A7, 9]
    },
    {
        "identifier": "EVENT_9_ret_30",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_31",
        "command": "set_var_to_const",
        "args": [0x70A7, 39]
    },
    {
        "identifier": "EVENT_9_ret_31",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_32",
        "command": "set_var_to_const",
        "args": [0x70A7, 13]
    },
    {
        "identifier": "EVENT_9_ret_32",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_33",
        "command": "set_var_to_const",
        "args": [0x70A7, 54]
    },
    {
        "identifier": "EVENT_9_ret_33",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_34",
        "command": "set_var_to_const",
        "args": [0x70A7, 47]
    },
    {
        "identifier": "EVENT_9_ret_34",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_35",
        "command": "set_var_to_const",
        "args": [0x70A7, 40]
    },
    {
        "identifier": "EVENT_9_ret_35",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_36",
        "command": "set_var_to_const",
        "args": [0x70A7, 85]
    },
    {
        "identifier": "EVENT_9_ret_36",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_37",
        "command": "set_var_to_const",
        "args": [0x70A7, 93]
    },
    {
        "identifier": "EVENT_9_ret_37",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_38",
        "command": "set_var_to_const",
        "args": [0x70A7, 74]
    },
    {
        "identifier": "EVENT_9_ret_38",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_39",
        "command": "set_var_to_const",
        "args": [0x70A7, 84]
    },
    {
        "identifier": "EVENT_9_ret_39",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_40",
        "command": "set_var_to_const",
        "args": [0x70A7, 5]
    },
    {
        "identifier": "EVENT_9_ret_40",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_41",
        "command": "set_var_to_const",
        "args": [0x70A7, 37]
    },
    {
        "identifier": "EVENT_9_ret_41",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_42",
        "command": "set_var_to_const",
        "args": [0x70A7, 35]
    },
    {
        "identifier": "EVENT_9_ret_42",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_43",
        "command": "set_var_to_const",
        "args": [0x70A7, 48]
    },
    {
        "identifier": "EVENT_9_ret_43",
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": "EVENT_9_set_44",
        "command": "set_var_to_const",
        "args": [0x70A7, 44]
    },
    {
        "identifier": "EVENT_9_ret_44",
        "command": 'jmp_to_event',
        "args": [160]
    }
]
