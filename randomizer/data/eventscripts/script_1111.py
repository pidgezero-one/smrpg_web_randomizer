from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1111_set_0',
        "command": 'set',
        "args": [0x70a7, 130]
    },
    {
        "identifier": 'EVENT_1111_store_7000_item_quantity_to_70A7_1',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_1111_jmp_if_7000_equals_short_2',
        "command": 'jmp_if_7000_equals_short',
        "args": [1, 'EVENT_1111_set_7']
    },
    {
        "identifier": 'EVENT_1111_set_3',
        "command": 'set',
        "args": [0x70a7, 166]
    },
    {
        "identifier": 'EVENT_1111_store_7000_item_quantity_to_70A7_4',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_1111_jmp_if_7000_equals_short_5',
        "command": 'jmp_if_7000_equals_short',
        "args": [1, 'EVENT_1111_play_sound_17']
    },
    {
        "identifier": 'EVENT_1111_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1111_set_7',
        "command": 'set',
        "args": [0x70a7, 6]
    },
    {
        "identifier": 'EVENT_1111_set_8',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_1111_run_event_as_subroutine_9',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_1111_remove_one_from_inventory_10',
        "command": 'remove_one_from_inventory',
        "args": [items.CricketPie]
    },
    {
        "identifier": 'EVENT_1111_ret_11',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1111_set_12',
        "command": 'set',
        "args": [0x70a7, 6]
    },
    {
        "identifier": 'EVENT_1111_set_13',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_1111_run_event_as_subroutine_14',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_1111_remove_one_from_inventory_15',
        "command": 'remove_one_from_inventory',
        "args": [items.CricketJam]
    },
    {
        "identifier": 'EVENT_1111_ret_16',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1111_play_sound_17',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_1111_set_short_18',
        "command": 'set_short',
        "args": [0x7000, 0x000a]
    },
    {
        "identifier": 'EVENT_1111_add_frog_coins_19',
        "command": 'add_frog_coins',
        "args": [0x7000]
    },
    {
        "identifier": 'EVENT_1111_remove_one_from_inventory_20',
        "command": 'remove_one_from_inventory',
        "args": [items.CricketJam]
    },
    {
        "identifier": 'EVENT_1111_ret_21',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_22',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x0d2c]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_23',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x4397]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_24',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x79fb]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_25',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xb058]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_26',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xe6ae]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_27',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x1cfd]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_28',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x5345]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_29',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x8986]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_30',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xbfc0]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_31',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xf5f3]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_32',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x2c1f]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_33',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x6244]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_34',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x9862]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_35',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xce79]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_36',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x0489]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_37',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x3a92]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_38',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x7094]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_39',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xa68f]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_40',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xdc83]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_41',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x1270]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_42',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x4856]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_43',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x7e35]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_44',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xb40d]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_45',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xe9de]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_46',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x1fa8]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_47',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x556b]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_48',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x8b27]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_49',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xc0dc]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_50',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xf68a]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_51',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x2c31]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_52',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x61d1]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_53',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x976a]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_54',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xccfc]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_55',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x0287]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_56',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x380b]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_57',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x6d88]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_58',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xa2fe]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_59',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xd86d]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_60',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x0dd5]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_61',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x4336]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_62',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x7890]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_63',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xade3]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_64',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xe32f]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_65',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x1874]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_66',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x4db2]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_67',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x82e9]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_68',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xb819]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_69',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xed42]
    },
    {
        "identifier": 'EVENT_1111_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_70',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x2264]
    },
    {
        "identifier": 'EVENT_1111_stop_sound_71',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1111_stop_sound_72',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1111_stop_sound_73',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1111_stop_sound_74',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1111_ret_75',
        "command": 'ret'
    }
]
