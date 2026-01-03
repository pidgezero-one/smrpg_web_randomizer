
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3843_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_3843_jmp_if_var_equals_byte_13']
    },
    {
        "identifier": 'EVENT_3843_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 7, 'EVENT_3843_jmp_if_bit_set_7']
    },
    {
        "identifier": 'EVENT_3843_jmp_if_var_equals_byte_2',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70de, 9, 'EVENT_3843_enter_area_5']
    },
    {
        "identifier": 'EVENT_3843_enter_area_3',
        "command": 'enter_area',
        "args": [Rooms._023_MUSHROOM_KINGDOM_BEFORE_CROCO_OUTSIDE, RadialDirections.NORTHWEST, 21, 122, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3843_ret_4',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3843_enter_area_5',
        "command": 'enter_area',
        "args": [Rooms._023_MUSHROOM_KINGDOM_BEFORE_CROCO_OUTSIDE, RadialDirections.NORTHEAST, 2, 102, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3843_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3843_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7082, 0, 'EVENT_3843_jmp_if_var_equals_byte_2']
    },
    {
        "identifier": 'EVENT_3843_jmp_if_var_equals_byte_8',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70de, 9, 'EVENT_3843_enter_area_11']
    },
    {
        "identifier": 'EVENT_3843_enter_area_9',
        "command": 'enter_area',
        "args": [Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, RadialDirections.NORTHWEST, 21, 122, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3843_ret_10',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3843_enter_area_11',
        "command": 'enter_area',
        "args": [Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, RadialDirections.NORTHEAST, 2, 102, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3843_ret_12',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3843_jmp_if_var_equals_byte_13',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70de, 9, 'EVENT_3843_enter_area_16']
    },
    {
        "identifier": 'EVENT_3843_enter_area_14',
        "command": 'enter_area',
        "args": [Rooms._191_MUSHROOM_KINGDOM_OUTSIDE, RadialDirections.NORTHWEST, 21, 122, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3843_ret_15',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3843_enter_area_16',
        "command": 'enter_area',
        "args": [Rooms._191_MUSHROOM_KINGDOM_OUTSIDE, RadialDirections.NORTHEAST, 2, 102, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3843_ret_17',
        "command": 'ret'
    }
]
