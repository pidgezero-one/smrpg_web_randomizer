
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_5_set_var_to_random_1',
        "command": 'set_var_to_random',
        "args": [0x7000, 12]
    },
    {
        "identifier": 'EVENT_5_jmp_if_7000_equals_short_3',
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 1, 'EVENT_5_set_3']
    },
    {
        "identifier": 'EVENT_5_jmp_if_7000_equals_short_4',
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 2, 'EVENT_5_set_4']
    },
    {
        "identifier": 'EVENT_5_jmp_if_7000_equals_short_5',
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 3, 'EVENT_5_set_5']
    },
    {
        "identifier": 'EVENT_5_jmp_if_7000_equals_short_6',
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 4, 'EVENT_5_set_6']
    },
    {
        "identifier": 'EVENT_5_jmp_if_7000_equals_short_7',
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 5, 'EVENT_5_set_7']
    },
    {
        "identifier": 'EVENT_5_jmp_if_7000_equals_short_8',
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 6, 'EVENT_5_set_8']
    },
    {
        "identifier": 'EVENT_5_jmp_if_7000_equals_short_9',
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 7, 'EVENT_5_set_9']
    },
    {
        "identifier": 'EVENT_5_jmp_if_7000_equals_short_10',
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 8, 'EVENT_5_set_10']
    },
    {
        "identifier": 'EVENT_5_jmp_if_7000_equals_short_11',
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 9, 'EVENT_5_set_11']
    },
    {
        "identifier": 'EVENT_5_jmp_if_7000_equals_short_12',
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 10, 'EVENT_5_set_12']
    },
    {
        "identifier": 'EVENT_5_jmp_if_7000_equals_short_13',
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 11, 'EVENT_5_set_13']
    },
    {
        "identifier": 'EVENT_5_set_2',
        "command": "set_var_to_const",
        "args": [0x70A7, 96]
    },
    {
        "identifier": 'EVENT_5_ret_1',
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": 'EVENT_5_set_3',
        "command": "set_var_to_const",
        "args": [0x70A7, 99]
    },
    {
        "identifier": 'EVENT_5_ret_2',
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": 'EVENT_5_set_4',
        "command": "set_var_to_const",
        "args": [0x70A7, 102]
    },
    {
        "identifier": 'EVENT_5_ret_3',
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": 'EVENT_5_set_5',
        "command": "set_var_to_const",
        "args": [0x70A7, 103]
    },
    {
        "identifier": 'EVENT_5_ret_4',
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": 'EVENT_5_set_6',
        "command": "set_var_to_const",
        "args": [0x70A7, 109]
    },
    {
        "identifier": 'EVENT_5_ret_5',
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": 'EVENT_5_set_7',
        "command": "set_var_to_const",
        "args": [0x70A7, 110]
    },
    {
        "identifier": 'EVENT_5_ret_6',
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": 'EVENT_5_set_8',
        "command": "set_var_to_const",
        "args": [0x70A7, 111]
    },
    {
        "identifier": 'EVENT_5_ret_7',
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": 'EVENT_5_set_9',
        "command": "set_var_to_const",
        "args": [0x70A7, 119]
    },
    {
        "identifier": 'EVENT_5_ret_8',
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": 'EVENT_5_set_10',
        "command": "set_var_to_const",
        "args": [0x70A7, 155]
    },
    {
        "identifier": 'EVENT_5_ret_9',
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": 'EVENT_5_set_11',
        "command": "set_var_to_const",
        "args": [0x70A7, 156]
    },
    {
        "identifier": 'EVENT_5_ret_10',
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": 'EVENT_5_set_12',
        "command": "set_var_to_const",
        "args": [0x70A7, 157]
    },
    {
        "identifier": 'EVENT_5_ret_11',
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": 'EVENT_5_set_13',
        "command": "set_var_to_const",
        "args": [0x70A7, 175]
    },
    {
        "identifier": 'EVENT_5_ret_12',
        "command": 'jmp_to_event',
        "args": [160]
    },
]
