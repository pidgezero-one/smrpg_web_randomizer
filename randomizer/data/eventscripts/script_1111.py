from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1111_set_0',
        "command": 'set',
        "args": [0x70a7, 130],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_store_7000_item_quantity_to_70A7_1',
        "command": 'store_7000_item_quantity_to_70A7',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_1111_set_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_set_3',
        "command": 'set',
        "args": [0x70a7, 166],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_store_7000_item_quantity_to_70A7_4',
        "command": 'store_7000_item_quantity_to_70A7',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_1111_play_sound_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_set_7',
        "command": 'set',
        "args": [0x70a7, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_set_8',
        "command": 'set',
        "args": [0x7000, 524],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_run_event_as_subroutine_9',
        "command": 'run_event_as_subroutine',
        "args": [3828],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_remove_one_from_inventory_10',
        "command": 'remove_one_from_inventory',
        "args": [items.CricketPie],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_set_12',
        "command": 'set',
        "args": [0x70a7, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_set_13',
        "command": 'set',
        "args": [0x7000, 524],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_run_event_as_subroutine_14',
        "command": 'run_event_as_subroutine',
        "args": [3828],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_remove_one_from_inventory_15',
        "command": 'remove_one_from_inventory',
        "args": [items.CricketJam],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_ret_16',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_play_sound_17',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_set_short_18',
        "command": 'set_short',
        "args": [0x7000, 0x000a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_add_frog_coins_19',
        "command": 'add_frog_coins',
        "args": [0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_remove_one_from_inventory_20',
        "command": 'remove_one_from_inventory',
        "args": [items.CricketJam],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_ret_21',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_22',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x0d2c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_23',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x4397],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_24',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x79fb],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_25',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xb058],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_26',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xe6ae],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_27',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x1cfd],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_28',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x5345],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_29',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x8986],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_30',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xbfc0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_31',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xf5f3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_32',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x2c1f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_33',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x6244],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_34',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x9862],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_35',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xce79],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_36',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x0489],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_37',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x3a92],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_38',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x7094],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_39',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xa68f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_40',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xdc83],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_41',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x1270],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_42',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x4856],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_43',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x7e35],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_44',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xb40d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_45',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xe9de],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_46',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x1fa8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_47',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x556b],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_48',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x8b27],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_49',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xc0dc],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_50',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xf68a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_51',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x2c31],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_52',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x61d1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_53',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x976a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_54',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xccfc],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_55',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x0287],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_56',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x380b],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_57',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x6d88],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_58',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xa2fe],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_59',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xd86d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_60',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x0dd5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_61',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x4336],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_62',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x7890],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_63',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xade3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_64',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xe32f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_65',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x1874],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_66',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x4db2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_67',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x82e9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_68',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xb819],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_69',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xed42],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_70',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x2264],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_stop_sound_71',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_stop_sound_72',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_stop_sound_73',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_stop_sound_74',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1111_ret_75',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
