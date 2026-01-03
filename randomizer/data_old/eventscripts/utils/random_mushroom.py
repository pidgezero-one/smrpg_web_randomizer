
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_21_set_var_to_random_1',
        "command": 'set_var_to_random',
        "args": [0x7000, 21]
    },
    {
        "identifier": "EVENT_21_jmp_if_7000_equals_short_0",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 0, "EVENT_21_set_0"]
    },
    {
        "identifier": "EVENT_21_jmp_if_7000_equals_short_1",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 1, "EVENT_21_set_0"]
    },
    {
        "identifier": "EVENT_21_jmp_if_7000_equals_short_2",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 2, "EVENT_21_set_0"]
    },
    {
        "identifier": "EVENT_21_jmp_if_7000_equals_short_3",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 3, "EVENT_21_set_0"]
    },
    {
        "identifier": "EVENT_21_jmp_if_7000_equals_short_4",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 4, "EVENT_21_set_1"]
    },
    {
        "identifier": "EVENT_21_jmp_if_7000_equals_short_5",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 5, "EVENT_21_set_1"]
    },
    {
        "identifier": "EVENT_21_jmp_if_7000_equals_short_6",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 6, "EVENT_21_set_1"]
    },
    {
        "identifier": "EVENT_21_jmp_if_7000_equals_short_7",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 7, "EVENT_21_set_1"]
    },
    {
        "identifier": "EVENT_21_jmp_if_7000_equals_short_8",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 8, "EVENT_21_set_2"]
    },
    {
        "identifier": "EVENT_21_jmp_if_7000_equals_short_9",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 9, "EVENT_21_set_2"]
    },
    {
        "identifier": "EVENT_21_jmp_if_7000_equals_short_10",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 10, "EVENT_21_set_2"]
    },
    {
        "identifier": "EVENT_21_jmp_if_7000_equals_short_11",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 11, "EVENT_21_set_2"]
    },
    {
        "identifier": "EVENT_21_jmp_if_7000_equals_short_12",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 12, "EVENT_21_set_3"]
    },
    {
        "identifier": "EVENT_21_jmp_if_7000_equals_short_13",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 13, "EVENT_21_set_3"]
    },
    {
        "identifier": "EVENT_21_jmp_if_7000_equals_short_14",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 14, "EVENT_21_set_3"]
    },
    {
        "identifier": "EVENT_21_jmp_if_7000_equals_short_15",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 15, "EVENT_21_set_4"]
    },
    {
        "identifier": "EVENT_21_jmp_if_7000_equals_short_16",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 16, "EVENT_21_set_4"]
    },
    {
        "identifier": "EVENT_21_jmp_if_7000_equals_short_17",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 17, "EVENT_21_set_4"]
    },
    {
        "identifier": "EVENT_21_jmp_if_7000_equals_short_18",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 18, "EVENT_21_set_5"]
    },
    {
        "identifier": "EVENT_21_jmp_if_7000_equals_short_19",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 19, "EVENT_21_set_6"]
    },
    {
        "identifier": "EVENT_21_set_7",
        "command": "set_var_to_const",
        "args": [0x70a7, 155]
    },
    {
        "identifier": "EVENT_21_ret_9",
        "command": "ret"
    },
    {
        "identifier": "EVENT_21_set_0",
        "command": "set_var_to_const",
        "args": [0x70a7, 96]
    },
    {
        "identifier": "EVENT_21_ret_0",
        "command": "ret"
    },
    {
        "identifier": "EVENT_21_set_1",
        "command": "set_var_to_const",
        "args": [0x70a7, 97]
    },
    {
        "identifier": "EVENT_21_ret_1",
        "command": "ret"
    },
    {
        "identifier": "EVENT_21_set_2",
        "command": "set_var_to_const",
        "args": [0x70a7, 98]
    },
    {
        "identifier": "EVENT_21_ret_2",
        "command": "ret"
    },
    {
        "identifier": "EVENT_21_set_3",
        "command": "set_var_to_const",
        "args": [0x70a7, 112]
    },
    {
        "identifier": "EVENT_21_ret_3",
        "command": "ret"
    },
    {
        "identifier": "EVENT_21_set_4",
        "command": "set_var_to_const",
        "args": [0x70a7, 175]
    },
    {
        "identifier": "EVENT_21_ret_4",
        "command": "ret"
    },
    {
        "identifier": "EVENT_21_set_5",
        "command": "set_var_to_const",
        "args": [0x70a7, 156]
    },
    {
        "identifier": "EVENT_21_ret_5",
        "command": "ret"
    },
    {
        "identifier": "EVENT_21_set_6",
        "command": "set_var_to_const",
        "args": [0x70a7, 157]
    },
    {
        "identifier": "EVENT_21_ret_6",
        "command": "ret"
    }
]
