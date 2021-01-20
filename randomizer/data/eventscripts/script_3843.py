from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3843_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 7, 'EVENT_3843_jmp_if_bit_set_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3843_jmp_if_var_equals_byte_1',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70de, 9, 'EVENT_3843_enter_area_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3843_enter_area_2',
        "command": 'enter_area',
        "args": [Rooms._191_MUSHROOM_KINGDOM_OUTSIDE, RadialDirections.NORTHWEST, 21, 122, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3843_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3843_enter_area_4',
        "command": 'enter_area',
        "args": [Rooms._191_MUSHROOM_KINGDOM_OUTSIDE, RadialDirections.NORTHEAST, 2, 102, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3843_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3843_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7082, 0, 'EVENT_3843_jmp_if_var_equals_byte_1'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3843_jmp_if_var_equals_byte_7',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70de, 9, 'EVENT_3843_enter_area_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3843_enter_area_8',
        "command": 'enter_area',
        "args": [Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, RadialDirections.NORTHWEST, 21, 122, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3843_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3843_enter_area_10',
        "command": 'enter_area',
        "args": [Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, RadialDirections.NORTHEAST, 2, 102, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3843_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3843_jmp_if_var_equals_byte_12',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70de, 9, 'EVENT_3843_enter_area_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3843_ret_13',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3843_ret_14',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3843_jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_3843_jmp_if_var_equals_byte_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3843_enter_area_16',
        "command": 'enter_area',
        "args": [Rooms._023_MUSHROOM_KINGDOM_BEFORE_CROCO_OUTSIDE, RadialDirections.NORTHWEST, 21, 122, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3843_enter_area_17',
        "command": 'enter_area',
        "args": [Rooms._023_MUSHROOM_KINGDOM_BEFORE_CROCO_OUTSIDE, RadialDirections.NORTHEAST, 2, 102, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    }
]
