from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3388_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7086, 0, 'EVENT_3388_ret_64']
    },
    {
        "identifier": 'EVENT_3388_jmp_1',
        "command": 'jmp',
        "args": ['EVENT_3388_set_short_mem_23']
    },
    {
        "identifier": 'EVENT_3388_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3388_set_7000_to_tapped_button_3',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_3388_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 32, 'EVENT_3388_play_sound_27']
    },
    {
        "identifier": 'EVENT_3388_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 128, 'EVENT_3388_play_sound_62']
    },
    {
        "identifier": 'EVENT_3388_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 16, 'EVENT_3388_play_sound_62']
    },
    {
        "identifier": 'EVENT_3388_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 64, 'EVENT_3388_play_sound_62']
    },
    {
        "identifier": 'EVENT_3388_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 2, 'EVENT_3388_play_sound_11']
    },
    {
        "identifier": 'EVENT_3388_jmp_if_var_equals_short_9',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_3388_play_sound_17']
    },
    {
        "identifier": 'EVENT_3388_jmp_10',
        "command": 'jmp',
        "args": ['EVENT_3388_pause_2']
    },
    {
        "identifier": 'EVENT_3388_play_sound_11',
        "command": 'play_sound',
        "args": [Sounds._003_MENU_SCROLL, 6]
    },
    {
        "identifier": 'EVENT_3388_jmp_if_var_equals_byte_12',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ad, 0, 'EVENT_3388_set_15']
    },
    {
        "identifier": 'EVENT_3388_dec_13',
        "command": 'dec',
        "args": [0x70ad]
    },
    {
        "identifier": 'EVENT_3388_jmp_14',
        "command": 'jmp',
        "args": ['EVENT_3388_set_short_mem_23']
    },
    {
        "identifier": 'EVENT_3388_set_15',
        "command": 'set',
        "args": [0x70ad, 6]
    },
    {
        "identifier": 'EVENT_3388_jmp_16',
        "command": 'jmp',
        "args": ['EVENT_3388_set_short_mem_23']
    },
    {
        "identifier": 'EVENT_3388_play_sound_17',
        "command": 'play_sound',
        "args": [Sounds._003_MENU_SCROLL, 6]
    },
    {
        "identifier": 'EVENT_3388_jmp_if_var_equals_byte_18',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ad, 6, 'EVENT_3388_set_21']
    },
    {
        "identifier": 'EVENT_3388_add_19',
        "command": 'add',
        "args": [0x70ad, 0x01]
    },
    {
        "identifier": 'EVENT_3388_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_3388_set_short_mem_23']
    },
    {
        "identifier": 'EVENT_3388_set_21',
        "command": 'set',
        "args": [0x70ad, 0]
    },
    {
        "identifier": 'EVENT_3388_jmp_22',
        "command": 'jmp',
        "args": ['EVENT_3388_set_short_mem_23']
    },
    {
        "identifier": 'EVENT_3388_set_short_mem_23',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ad]
    },
    {
        "identifier": 'EVENT_3388_add_24',
        "command": 'add',
        "args": [0x7000, 1952]
    },
    {
        "identifier": 'EVENT_3388_run_dialog_25',
        "command": 'run_dialog',
        "args": [0x7000, AreaObjects.MARIO, [_0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3388_jmp_26',
        "command": 'jmp',
        "args": ['EVENT_3388_pause_2']
    },
    {
        "identifier": 'EVENT_3388_play_sound_27',
        "command": 'play_sound',
        "args": [Sounds._001_MENU_SELECT, 6]
    },
    {
        "identifier": 'EVENT_3388_close_dialog_28',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_3388_jmp_if_var_equals_byte_29',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ad, 0, 'EVENT_3388_enter_area_36']
    },
    {
        "identifier": 'EVENT_3388_jmp_if_var_equals_byte_30',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ad, 1, 'EVENT_3388_enter_area_38']
    },
    {
        "identifier": 'EVENT_3388_jmp_if_var_equals_byte_31',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ad, 2, 'EVENT_3388_enter_area_40']
    },
    {
        "identifier": 'EVENT_3388_jmp_if_var_equals_byte_32',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ad, 3, 'EVENT_3388_enter_area_42']
    },
    {
        "identifier": 'EVENT_3388_jmp_if_var_equals_byte_33',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ad, 4, 'EVENT_3388_enter_area_44']
    },
    {
        "identifier": 'EVENT_3388_jmp_if_var_equals_byte_34',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ad, 5, 'EVENT_3388_enter_area_46']
    },
    {
        "identifier": 'EVENT_3388_jmp_if_var_equals_byte_35',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ad, 6, 'EVENT_3388_enter_area_48']
    },
    {
        "identifier": 'EVENT_3388_enter_area_36',
        "command": 'enter_area',
        "args": [Rooms._180_SUNKEN_SHIP_POSTKC_AREA_02_SMALL_2LEVEL_ROOM, RadialDirections.SOUTH, 27, 21, 4, []]
    },
    {
        "identifier": 'EVENT_3388_jmp_37',
        "command": 'jmp',
        "args": ['EVENT_3388_remove_from_current_level_50']
    },
    {
        "identifier": 'EVENT_3388_enter_area_38',
        "command": 'enter_area',
        "args": [Rooms._182_SUNKEN_SHIP_POSTKC_AREA_07_THREE_DRY_BONES, RadialDirections.SOUTH, 25, 95, 2, []]
    },
    {
        "identifier": 'EVENT_3388_jmp_39',
        "command": 'jmp',
        "args": ['EVENT_3388_remove_from_current_level_50']
    },
    {
        "identifier": 'EVENT_3388_enter_area_40',
        "command": 'enter_area',
        "args": [Rooms._187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS, RadialDirections.SOUTH, 3, 35, 0, []]
    },
    {
        "identifier": 'EVENT_3388_jmp_41',
        "command": 'jmp',
        "args": ['EVENT_3388_remove_from_current_level_50']
    },
    {
        "identifier": 'EVENT_3388_enter_area_42',
        "command": 'enter_area',
        "args": [Rooms._188_SUNKEN_SHIP_POSTKC_AREA_11_WATER_ROOM_WITH_WHIRLPOOL, RadialDirections.SOUTH, 2, 79, 5, []]
    },
    {
        "identifier": 'EVENT_3388_jmp_43',
        "command": 'jmp',
        "args": ['EVENT_3388_remove_from_current_level_50']
    },
    {
        "identifier": 'EVENT_3388_enter_area_44',
        "command": 'enter_area',
        "args": [Rooms._188_SUNKEN_SHIP_POSTKC_AREA_11_WATER_ROOM_WITH_WHIRLPOOL, RadialDirections.SOUTH, 10, 81, 0, []]
    },
    {
        "identifier": 'EVENT_3388_jmp_45',
        "command": 'jmp',
        "args": ['EVENT_3388_remove_from_current_level_50']
    },
    {
        "identifier": 'EVENT_3388_enter_area_46',
        "command": 'enter_area',
        "args": [Rooms._185_SUNKEN_SHIP_POSTKC_AREA_14_SECRET_SAFETY_RING, RadialDirections.SOUTH, 30, 49, 0, []]
    },
    {
        "identifier": 'EVENT_3388_jmp_47',
        "command": 'jmp',
        "args": ['EVENT_3388_remove_from_current_level_50']
    },
    {
        "identifier": 'EVENT_3388_enter_area_48',
        "command": 'enter_area',
        "args": [Rooms._024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL, RadialDirections.SOUTH, 5, 117, 0, []]
    },
    {
        "identifier": 'EVENT_3388_jmp_49',
        "command": 'jmp',
        "args": ['EVENT_3388_remove_from_current_level_50']
    },
    {
        "identifier": 'EVENT_3388_remove_from_current_level_50',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_3388_circle_mask_static_51',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 96, 8]
    },
    {
        "identifier": 'EVENT_3388_pause_52',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'EVENT_3388_pause_53',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3388_set_7000_to_pressed_button_54',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_3388_jmp_if_7000_all_bits_clear_55',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[0, 1, 2, 3, 4, 5, 6, 7], 'EVENT_3388_pause_53']
    },
    {
        "identifier": 'EVENT_3388_circle_mask_static_56',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 0, 8]
    },
    {
        "identifier": 'EVENT_3388_pause_57',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'EVENT_3388_enter_area_58',
        "command": 'enter_area',
        "args": [Rooms._028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM, RadialDirections.NORTHEAST, 24, 110, 0, []]
    },
    {
        "identifier": 'EVENT_3388_action_queue_async_59',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3388_action_queue_async_59_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3388_fade_in_from_black_async_60',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3388_jmp_61',
        "command": 'jmp',
        "args": ['EVENT_3388_jmp_if_bit_clear_0']
    },
    {
        "identifier": 'EVENT_3388_play_sound_62',
        "command": 'play_sound',
        "args": [Sounds._002_MENU_CANCEL, 6]
    },
    {
        "identifier": 'EVENT_3388_close_dialog_63',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_3388_ret_64',
        "command": 'ret'
    }
]
