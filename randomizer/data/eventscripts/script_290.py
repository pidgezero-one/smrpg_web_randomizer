from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_290_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7089, 6, 'EVENT_290_set_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_set_bit_1',
        "command": 'set_bit',
        "args": [0x7089, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_set_2',
        "command": 'set',
        "args": [0x70a7, 102],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_set_3',
        "command": 'set',
        "args": [0x7000, 524],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [3828],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_set_6',
        "command": 'set',
        "args": [0x70a7, 128],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_store_7000_item_quantity_to_70A7_7',
        "command": 'store_7000_item_quantity_to_70A7',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_290_set_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_open_shop_9',
        "command": 'open_shop',
        "args": [Shops._00_MUSHROOM_KINGDOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_set_12',
        "command": 'set',
        "args": [0x70a7, 130],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_set_13',
        "command": 'set',
        "args": [0x7000, 524],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_run_event_as_subroutine_14',
        "command": 'run_event_as_subroutine',
        "args": [3828],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_remove_one_from_inventory_15',
        "command": 'remove_one_from_inventory',
        "args": [items.RareFrogCoin],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_ret_16',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_17',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x10c7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_18',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xfb97],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_19',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xe660],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_20',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xd122],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_21',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xbbdd],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_22',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xa691],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_23',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x913e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_24',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x7be4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_25',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x6683],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_26',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x511b],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_27',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x3bac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_28',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x2636],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_29',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x10b9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_30',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xfb35],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_31',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xe5aa],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_32',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xd018],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_33',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xba7f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_34',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xa4df],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_35',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x8f38],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_36',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x798a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_37',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x63d5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_38',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x4e19],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_39',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x3856],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_40',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x228c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_41',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x0cbb],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_42',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xf6e3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_43',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xe104],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_44',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xcb1e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_45',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xb531],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_46',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x9f3d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_47',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x8942],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_48',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x7340],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_49',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x5d37],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_50',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x4727],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_51',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x3110],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_52',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x1af2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_53',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x04cd],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_54',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xeea1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_55',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xd86e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_56',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xc234],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_57',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xabf3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_58',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x95ab],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_59',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x7f5c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_60',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x6906],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_61',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x52a9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_62',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x3c45],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_63',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x25da],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_64',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x0f68],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_65',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xf8ef],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_66',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xe26f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_67',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xcbe8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_68',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xb55a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_69',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x9ec5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_70',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x8829],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_71',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x7186],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_72',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x5adc],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_stop_sound_73',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_stop_sound_74',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_stop_sound_75',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_stop_sound_76',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_stop_sound_77',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_stop_sound_78',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_stop_sound_79',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_290_ret_80',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
