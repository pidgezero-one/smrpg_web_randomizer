from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1116_set_0',
        "command": 'set',
        "args": [0x70a7, 150],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_store_7000_item_quantity_to_70A7_1',
        "command": 'store_7000_item_quantity_to_70A7',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_1116_open_shop_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_set_3',
        "command": 'set',
        "args": [0x70a7, 152],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_store_7000_item_quantity_to_70A7_4',
        "command": 'store_7000_item_quantity_to_70A7',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_1116_open_shop_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_set_6',
        "command": 'set',
        "args": [0x70a7, 151],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_store_7000_item_quantity_to_70A7_7',
        "command": 'store_7000_item_quantity_to_70A7',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_1116_open_shop_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_open_shop_9',
        "command": 'open_shop',
        "args": [Shops._09_JUICE_BAR_NO_CARD],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_open_shop_12',
        "command": 'open_shop',
        "args": [Shops._12_JUICE_BAR_SOPRANO_CARD],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_fade_in_from_black_async_13',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_ret_14',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_open_shop_15',
        "command": 'open_shop',
        "args": [Shops._11_JUICE_BAR_TENOR_CARD],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_fade_in_from_black_async_16',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_ret_17',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_open_shop_18',
        "command": 'open_shop',
        "args": [Shops._10_JUICE_BAR_ALTO_CARD],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_fade_in_from_black_async_19',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_ret_20',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_21',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_22',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_23',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_24',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_25',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_26',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_27',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_28',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_29',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_30',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_31',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_32',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_33',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_34',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_35',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_36',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_37',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_38',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_39',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_40',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_41',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_42',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_43',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_44',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_45',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_46',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_47',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_48',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_49',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_50',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_51',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_52',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_53',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_54',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_55',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_56',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_57',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_stop_sound_58',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1116_ret_59',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
