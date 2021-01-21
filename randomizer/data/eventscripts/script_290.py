from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_290_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7089, 6, 'EVENT_290_set_6']
    },
    {
        "identifier": 'EVENT_290_set_bit_1',
        "command": 'set_bit',
        "args": [0x7089, 6]
    },
    {
        "identifier": 'EVENT_290_set_2',
        "command": 'set',
        "args": [0x70a7, 102]
    },
    {
        "identifier": 'EVENT_290_set_3',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_290_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_290_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_290_set_6',
        "command": 'set',
        "args": [0x70a7, 128]
    },
    {
        "identifier": 'EVENT_290_store_7000_item_quantity_to_70A7_7',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_290_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_290_set_12']
    },
    {
        "identifier": 'EVENT_290_open_shop_9',
        "command": 'open_shop',
        "args": [Shops._00_MUSHROOM_KINGDOM]
    },
    {
        "identifier": 'EVENT_290_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_290_ret_11',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_290_set_12',
        "command": 'set',
        "args": [0x70a7, 130]
    },
    {
        "identifier": 'EVENT_290_set_13',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_290_run_event_as_subroutine_14',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_290_remove_one_from_inventory_15',
        "command": 'remove_one_from_inventory',
        "args": [items.RareFrogCoin]
    },
    {
        "identifier": 'EVENT_290_ret_16',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_17',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x10c7]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_18',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xfb97]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_19',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xe660]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_20',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xd122]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_21',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xbbdd]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_22',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xa691]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_23',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x913e]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_24',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x7be4]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_25',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x6683]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_26',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x511b]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_27',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x3bac]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_28',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x2636]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_29',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x10b9]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_30',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xfb35]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_31',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xe5aa]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_32',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xd018]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_33',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xba7f]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_34',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xa4df]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_35',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x8f38]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_36',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x798a]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_37',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x63d5]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_38',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x4e19]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_39',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x3856]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_40',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x228c]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_41',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x0cbb]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_42',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xf6e3]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_43',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xe104]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_44',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xcb1e]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_45',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xb531]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_46',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x9f3d]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_47',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x8942]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_48',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x7340]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_49',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x5d37]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_50',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x4727]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_51',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x3110]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_52',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x1af2]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_53',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x04cd]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_54',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xeea1]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_55',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xd86e]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_56',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xc234]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_57',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xabf3]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_58',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x95ab]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_59',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x7f5c]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_60',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x6906]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_61',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x52a9]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_62',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x3c45]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_63',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x25da]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_64',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x0f68]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_65',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xf8ef]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_66',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xe26f]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_67',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xcbe8]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_68',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xb55a]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_69',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x9ec5]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_70',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x8829]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_71',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x7186]
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_72',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x5adc]
    },
    {
        "identifier": 'EVENT_290_stop_sound_73',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_290_stop_sound_74',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_290_stop_sound_75',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_290_stop_sound_76',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_290_stop_sound_77',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_290_stop_sound_78',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_290_stop_sound_79',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_290_ret_80',
        "command": 'ret'
    }
]
