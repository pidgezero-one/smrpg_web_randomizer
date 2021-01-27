from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3350_fade_out_to_black_async_0',
        "command": 'fade_out_to_black_async'
    },
    {
        "identifier": 'EVENT_3350_enable_trigger_in_level_1',
        "command": 'enable_trigger_in_level',
        "args": [AreaObjects.NPC_0, Rooms._144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM]
    },
    {
        "identifier": 'EVENT_3350_enable_trigger_in_level_2',
        "command": 'enable_trigger_in_level',
        "args": [AreaObjects.NPC_0, Rooms._446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS]
    },
    {
        "identifier": 'EVENT_3350_set_7000_to_70A0_short_mem_3',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70b7]
    },
    {
        "identifier": 'EVENT_3350_mem_7000_and_const_4',
        "command": 'mem_7000_and_const',
        "args": [0x0070]
    },
    {
        "identifier": 'EVENT_3350_jmp_if_7000_equals_short_5',
        "command": 'jmp_if_7000_equals_short',
        "args": [32, 'EVENT_3350_set_7000_to_70A0_short_mem_14']
    },
    {
        "identifier": 'EVENT_3350_jmp_if_7000_equals_short_6',
        "command": 'jmp_if_7000_equals_short',
        "args": [48, 'EVENT_3350_set_7000_to_70A0_short_mem_18']
    },
    {
        "identifier": 'EVENT_3350_jmp_if_7000_equals_short_7',
        "command": 'jmp_if_7000_equals_short',
        "args": [64, 'EVENT_3350_set_7000_to_70A0_short_mem_22']
    },
    {
        "identifier": 'EVENT_3350_jmp_if_7000_equals_short_8',
        "command": 'jmp_if_7000_equals_short',
        "args": [80, 'EVENT_3350_set_7000_to_70A0_short_mem_26']
    },
    {
        "identifier": 'EVENT_3350_jmp_if_7000_equals_short_9',
        "command": 'jmp_if_7000_equals_short',
        "args": [96, 'EVENT_3350_set_7000_to_70A0_short_mem_30']
    },
    {
        "identifier": 'EVENT_3350_set_7000_to_70A0_short_mem_10',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70e7]
    },
    {
        "identifier": 'EVENT_3350_mem_7000_or_const_11',
        "command": 'mem_7000_or_const',
        "args": [0x0080]
    },
    {
        "identifier": 'EVENT_3350_set_70A0_short_mem_to_7000_12',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70e7]
    },
    {
        "identifier": 'EVENT_3350_jmp_13',
        "command": 'jmp',
        "args": ['EVENT_3350_set_7000_to_70A0_short_mem_33']
    },
    {
        "identifier": 'EVENT_3350_set_7000_to_70A0_short_mem_14',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70e7]
    },
    {
        "identifier": 'EVENT_3350_mem_7000_or_const_15',
        "command": 'mem_7000_or_const',
        "args": [0x0008]
    },
    {
        "identifier": 'EVENT_3350_set_70A0_short_mem_to_7000_16',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70e7]
    },
    {
        "identifier": 'EVENT_3350_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_3350_set_7000_to_70A0_short_mem_33']
    },
    {
        "identifier": 'EVENT_3350_set_7000_to_70A0_short_mem_18',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70e8]
    },
    {
        "identifier": 'EVENT_3350_mem_7000_or_const_19',
        "command": 'mem_7000_or_const',
        "args": [0x0080]
    },
    {
        "identifier": 'EVENT_3350_set_70A0_short_mem_to_7000_20',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70e8]
    },
    {
        "identifier": 'EVENT_3350_jmp_21',
        "command": 'jmp',
        "args": ['EVENT_3350_set_7000_to_70A0_short_mem_33']
    },
    {
        "identifier": 'EVENT_3350_set_7000_to_70A0_short_mem_22',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70e8]
    },
    {
        "identifier": 'EVENT_3350_mem_7000_or_const_23',
        "command": 'mem_7000_or_const',
        "args": [0x0008]
    },
    {
        "identifier": 'EVENT_3350_set_70A0_short_mem_to_7000_24',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70e8]
    },
    {
        "identifier": 'EVENT_3350_jmp_25',
        "command": 'jmp',
        "args": ['EVENT_3350_set_7000_to_70A0_short_mem_33']
    },
    {
        "identifier": 'EVENT_3350_set_7000_to_70A0_short_mem_26',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70e9]
    },
    {
        "identifier": 'EVENT_3350_mem_7000_or_const_27',
        "command": 'mem_7000_or_const',
        "args": [0x0080]
    },
    {
        "identifier": 'EVENT_3350_set_70A0_short_mem_to_7000_28',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70e9]
    },
    {
        "identifier": 'EVENT_3350_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_3350_set_7000_to_70A0_short_mem_33']
    },
    {
        "identifier": 'EVENT_3350_set_7000_to_70A0_short_mem_30',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70e9]
    },
    {
        "identifier": 'EVENT_3350_mem_7000_or_const_31',
        "command": 'mem_7000_or_const',
        "args": [0x0008]
    },
    {
        "identifier": 'EVENT_3350_set_70A0_short_mem_to_7000_32',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70e9]
    },
    {
        "identifier": 'EVENT_3350_set_7000_to_70A0_short_mem_33',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70b7]
    },
    {
        "identifier": 'EVENT_3350_mem_7000_and_const_34',
        "command": 'mem_7000_and_const',
        "args": [0x0007]
    },
    {
        "identifier": 'EVENT_3350_add_35',
        "command": 'add',
        "args": [0x7000, 512]
    },
    {
        "identifier": 'EVENT_3350_dec_36',
        "command": 'dec',
        "args": [0x7000]
    },
    {
        "identifier": 'EVENT_3350_jmp_if_mem_704x_at_7000_bit_clear_37',
        "command": 'jmp_if_mem_704x_at_7000_bit_clear',
        "args": ['EVENT_3350_inc_40']
    },
    {
        "identifier": 'EVENT_3350_disable_trigger_in_level_38',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_0, Rooms._144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM]
    },
    {
        "identifier": 'EVENT_3350_disable_trigger_in_level_39',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_0, Rooms._446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS]
    },
    {
        "identifier": 'EVENT_3350_inc_40',
        "command": 'inc',
        "args": [0x70b6]
    },
    {
        "identifier": 'EVENT_3350_jmp_if_var_equals_byte_41',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b6, 4, 'EVENT_3350_enter_area_44']
    },
    {
        "identifier": 'EVENT_3350_enter_area_42',
        "command": 'enter_area',
        "args": [Rooms._144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM, RadialDirections.NORTHEAST, 4, 79, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3350_ret_43',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3350_enter_area_44',
        "command": 'enter_area',
        "args": [Rooms._446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS, RadialDirections.NORTHEAST, 16, 79, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3350_ret_45',
        "command": 'ret'
    }
]
