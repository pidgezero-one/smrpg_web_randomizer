from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3375_set_0',
        "command": 'set',
        "args": [0x70df, 4]
    },
    {
        "identifier": 'EVENT_3375_set_1',
        "command": 'set',
        "args": [0x70b6, 0]
    },
    {
        "identifier": 'EVENT_3375_set_2',
        "command": 'set',
        "args": [0x70b7, 0]
    },
    {
        "identifier": 'EVENT_3375_set_3',
        "command": 'set',
        "args": [0x70e7, 0]
    },
    {
        "identifier": 'EVENT_3375_set_4',
        "command": 'set',
        "args": [0x70e8, 0]
    },
    {
        "identifier": 'EVENT_3375_set_5',
        "command": 'set',
        "args": [0x70e9, 0]
    },
    {
        "identifier": 'EVENT_3375_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_3375_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_3375_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_3375_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_3375_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'EVENT_3375_clear_bit_11',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_3375_set_short_12',
        "command": 'set_short',
        "args": [0x703c, 0x0001]
    },
    {
        "identifier": 'EVENT_3375_set_random_13',
        "command": 'set_random',
        "args": [0x7000, 6]
    },
    {
        "identifier": 'EVENT_3375_add_14',
        "command": 'add',
        "args": [0x7000, 24]
    },
    {
        "identifier": 'EVENT_3375_jmp_if_mem_704x_at_7000_bit_set_15',
        "command": 'jmp_if_mem_704x_at_7000_bit_set',
        "args": ['EVENT_3375_set_random_13']
    },
    {
        "identifier": 'EVENT_3375_set_mem_704x_at_7000_bit_16',
        "command": 'set_mem_704x_at_7000_bit'
    },
    {
        "identifier": 'EVENT_3375_jmp_if_7000_equals_short_17',
        "command": 'jmp_if_7000_equals_short',
        "args": [25, 'EVENT_3375_set_short_mem_28']
    },
    {
        "identifier": 'EVENT_3375_jmp_if_7000_equals_short_18',
        "command": 'jmp_if_7000_equals_short',
        "args": [26, 'EVENT_3375_set_short_mem_33']
    },
    {
        "identifier": 'EVENT_3375_jmp_if_7000_equals_short_19',
        "command": 'jmp_if_7000_equals_short',
        "args": [27, 'EVENT_3375_set_short_mem_39']
    },
    {
        "identifier": 'EVENT_3375_jmp_if_7000_equals_short_20',
        "command": 'jmp_if_7000_equals_short',
        "args": [28, 'EVENT_3375_set_short_mem_44']
    },
    {
        "identifier": 'EVENT_3375_jmp_if_7000_equals_short_21',
        "command": 'jmp_if_7000_equals_short',
        "args": [29, 'EVENT_3375_set_short_mem_50']
    },
    {
        "identifier": 'EVENT_3375_set_short_mem_22',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70e7]
    },
    {
        "identifier": 'EVENT_3375_set_short_mem_23',
        "command": 'set_short_mem',
        "args": [0x703c, 0x703e]
    },
    {
        "identifier": 'EVENT_3375_mem_7000_shift_left_24',
        "command": 'mem_7000_shift_left',
        "args": [0x703e, 252]
    },
    {
        "identifier": 'EVENT_3375_mem_7000_or_var_25',
        "command": 'mem_7000_or_var',
        "args": [0x703e]
    },
    {
        "identifier": 'EVENT_3375_set_short_mem_26',
        "command": 'set_short_mem',
        "args": [0x70e7, 0x7000]
    },
    {
        "identifier": 'EVENT_3375_jmp_27',
        "command": 'jmp',
        "args": ['EVENT_3375_inc_short_54']
    },
    {
        "identifier": 'EVENT_3375_set_short_mem_28',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70e7]
    },
    {
        "identifier": 'EVENT_3375_set_short_mem_29',
        "command": 'set_short_mem',
        "args": [0x703c, 0x703e]
    },
    {
        "identifier": 'EVENT_3375_mem_7000_or_var_30',
        "command": 'mem_7000_or_var',
        "args": [0x703e]
    },
    {
        "identifier": 'EVENT_3375_set_short_mem_31',
        "command": 'set_short_mem',
        "args": [0x70e7, 0x7000]
    },
    {
        "identifier": 'EVENT_3375_jmp_32',
        "command": 'jmp',
        "args": ['EVENT_3375_inc_short_54']
    },
    {
        "identifier": 'EVENT_3375_set_short_mem_33',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70e8]
    },
    {
        "identifier": 'EVENT_3375_set_short_mem_34',
        "command": 'set_short_mem',
        "args": [0x703c, 0x703e]
    },
    {
        "identifier": 'EVENT_3375_mem_7000_shift_left_35',
        "command": 'mem_7000_shift_left',
        "args": [0x703e, 252]
    },
    {
        "identifier": 'EVENT_3375_mem_7000_or_var_36',
        "command": 'mem_7000_or_var',
        "args": [0x703e]
    },
    {
        "identifier": 'EVENT_3375_set_short_mem_37',
        "command": 'set_short_mem',
        "args": [0x70e8, 0x7000]
    },
    {
        "identifier": 'EVENT_3375_jmp_38',
        "command": 'jmp',
        "args": ['EVENT_3375_inc_short_54']
    },
    {
        "identifier": 'EVENT_3375_set_short_mem_39',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70e8]
    },
    {
        "identifier": 'EVENT_3375_set_short_mem_40',
        "command": 'set_short_mem',
        "args": [0x703c, 0x703e]
    },
    {
        "identifier": 'EVENT_3375_mem_7000_or_var_41',
        "command": 'mem_7000_or_var',
        "args": [0x703e]
    },
    {
        "identifier": 'EVENT_3375_set_short_mem_42',
        "command": 'set_short_mem',
        "args": [0x70e8, 0x7000]
    },
    {
        "identifier": 'EVENT_3375_jmp_43',
        "command": 'jmp',
        "args": ['EVENT_3375_inc_short_54']
    },
    {
        "identifier": 'EVENT_3375_set_short_mem_44',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70e9]
    },
    {
        "identifier": 'EVENT_3375_set_short_mem_45',
        "command": 'set_short_mem',
        "args": [0x703c, 0x703e]
    },
    {
        "identifier": 'EVENT_3375_mem_7000_shift_left_46',
        "command": 'mem_7000_shift_left',
        "args": [0x703e, 252]
    },
    {
        "identifier": 'EVENT_3375_mem_7000_or_var_47',
        "command": 'mem_7000_or_var',
        "args": [0x703e]
    },
    {
        "identifier": 'EVENT_3375_set_short_mem_48',
        "command": 'set_short_mem',
        "args": [0x70e9, 0x7000]
    },
    {
        "identifier": 'EVENT_3375_jmp_49',
        "command": 'jmp',
        "args": ['EVENT_3375_inc_short_54']
    },
    {
        "identifier": 'EVENT_3375_set_short_mem_50',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70e9]
    },
    {
        "identifier": 'EVENT_3375_set_short_mem_51',
        "command": 'set_short_mem',
        "args": [0x703c, 0x703e]
    },
    {
        "identifier": 'EVENT_3375_mem_7000_or_var_52',
        "command": 'mem_7000_or_var',
        "args": [0x703e]
    },
    {
        "identifier": 'EVENT_3375_set_short_mem_53',
        "command": 'set_short_mem',
        "args": [0x70e9, 0x7000]
    },
    {
        "identifier": 'EVENT_3375_inc_short_54',
        "command": 'inc_short',
        "args": [0x703c]
    },
    {
        "identifier": 'EVENT_3375_mem_compare_55',
        "command": 'mem_compare',
        "args": [0x703c, 7]
    },
    {
        "identifier": 'EVENT_3375_jmp_if_loaded_memory_is_above_or_equal_0_56',
        "command": 'jmp_if_loaded_memory_is_above_or_equal_0',
        "args": ['EVENT_3375_set_random_13']
    },
    {
        "identifier": 'EVENT_3375_ret_57',
        "command": 'ret'
    }
]
