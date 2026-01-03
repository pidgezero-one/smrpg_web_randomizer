
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3843_clear_bit_0',
        "command": 'set_bit',
        "args": [0x7087, 0]
    },
    {
        "identifier": 'EVENT_3843_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 7, 'EVENT_3843_jmp_if_bit_set_6']
    },
    {
        "identifier": 'EVENT_3843_jmp_if_var_equals_const_1',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70de, 9, 'EVENT_3843_enter_area_4']
    },
    {
        "identifier": 'EVENT_3843_enter_area_2',
        "command": 'enter_area',
        "args": [Rooms._191_MUSHROOM_KINGDOM_OUTSIDE, RadialDirections.NORTHWEST, 21, 122, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3843_ret_3',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3843_enter_area_4',
        "command": 'enter_area',
        "args": [Rooms._191_MUSHROOM_KINGDOM_OUTSIDE, RadialDirections.NORTHEAST, 2, 102, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3843_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3843_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7082, 0, 'EVENT_3843_jmp_if_var_equals_const_1']
    },
    {
        "identifier": 'EVENT_3843_jmp_if_var_equals_const_7',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70de, 9, 'EVENT_3843_enter_area_10']
    },
    {
        "identifier": 'EVENT_3843_enter_area_8',
        "command": 'enter_area',
        "args": [Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, RadialDirections.NORTHWEST, 21, 122, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3843_ret_9',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3843_enter_area_10',
        "command": 'enter_area',
        "args": [Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, RadialDirections.NORTHEAST, 2, 102, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3843_ret_11',
        "command": 'ret'
    }
]
