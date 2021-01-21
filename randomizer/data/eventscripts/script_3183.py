from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3183_run_event_as_subroutine_0',
        "command": 'run_event_as_subroutine',
        "args": [65]
    },
    {
        "identifier": 'EVENT_3183_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._108_MOLEVILLE_OUTSIDE, RadialDirections.SOUTH, 20, 41, 10, []]
    },
    {
        "identifier": 'EVENT_3183_set_bit_2',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_3183_jmp_to_event_3',
        "command": 'jmp_to_event',
        "args": [1648]
    },
    {
        "identifier": 'EVENT_3183_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 3, 'EVENT_3183_remove_from_level_28']
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_5',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._278_MOLEVILLE_MINES_AREA_03_LEADS_BACK_TO_AREA_1]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_6',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._278_MOLEVILLE_MINES_AREA_03_LEADS_BACK_TO_AREA_1]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_7',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._278_MOLEVILLE_MINES_AREA_03_LEADS_BACK_TO_AREA_1]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_8',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._274_MOLEVILLE_MINES_AREA_02]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_9',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._274_MOLEVILLE_MINES_AREA_02]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_10',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_11',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_12',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._279_MOLEVILLE_MINES_AREA_08_CROCOS_BOMBED_ROOM]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_13',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._279_MOLEVILLE_MINES_AREA_08_CROCOS_BOMBED_ROOM]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_14',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._279_MOLEVILLE_MINES_AREA_08_CROCOS_BOMBED_ROOM]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_15',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_16',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_17',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_18',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._275_MOLEVILLE_MINES_AREA_06_SMALL_ROOM_LEADING_TO_AREA_06]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_19',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._275_MOLEVILLE_MINES_AREA_06_SMALL_ROOM_LEADING_TO_AREA_06]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_20',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._275_MOLEVILLE_MINES_AREA_06_SMALL_ROOM_LEADING_TO_AREA_06]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_21',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_22',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_23',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_24',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._282_MOLEVILLE_MINES_AREA_10_SMALL_ROOM_WMINECART_TRACKS]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_25',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._282_MOLEVILLE_MINES_AREA_10_SMALL_ROOM_WMINECART_TRACKS]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_26',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._282_MOLEVILLE_MINES_AREA_10_SMALL_ROOM_WMINECART_TRACKS]
    },
    {
        "identifier": 'EVENT_3183_jmp_27',
        "command": 'jmp',
        "args": ['EVENT_3183_remove_from_level_50']
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_28',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._278_MOLEVILLE_MINES_AREA_03_LEADS_BACK_TO_AREA_1]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_29',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._278_MOLEVILLE_MINES_AREA_03_LEADS_BACK_TO_AREA_1]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_30',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._278_MOLEVILLE_MINES_AREA_03_LEADS_BACK_TO_AREA_1]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_31',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._274_MOLEVILLE_MINES_AREA_02]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_32',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._274_MOLEVILLE_MINES_AREA_02]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_33',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_34',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_35',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._279_MOLEVILLE_MINES_AREA_08_CROCOS_BOMBED_ROOM]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_36',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._279_MOLEVILLE_MINES_AREA_08_CROCOS_BOMBED_ROOM]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_37',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._279_MOLEVILLE_MINES_AREA_08_CROCOS_BOMBED_ROOM]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_38',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_39',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_40',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_41',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._275_MOLEVILLE_MINES_AREA_06_SMALL_ROOM_LEADING_TO_AREA_06]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_42',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._275_MOLEVILLE_MINES_AREA_06_SMALL_ROOM_LEADING_TO_AREA_06]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_43',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._275_MOLEVILLE_MINES_AREA_06_SMALL_ROOM_LEADING_TO_AREA_06]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_44',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_45',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_46',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_47',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._282_MOLEVILLE_MINES_AREA_10_SMALL_ROOM_WMINECART_TRACKS]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_48',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._282_MOLEVILLE_MINES_AREA_10_SMALL_ROOM_WMINECART_TRACKS]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_49',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._282_MOLEVILLE_MINES_AREA_10_SMALL_ROOM_WMINECART_TRACKS]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_50',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._272_MOLEVILLE_MINES_AREA_11_BOMBED_ROOM_WSINGING_MOLES]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_51',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._272_MOLEVILLE_MINES_AREA_11_BOMBED_ROOM_WSINGING_MOLES]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_52',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._272_MOLEVILLE_MINES_AREA_11_BOMBED_ROOM_WSINGING_MOLES]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_53',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._272_MOLEVILLE_MINES_AREA_11_BOMBED_ROOM_WSINGING_MOLES]
    },
    {
        "identifier": 'EVENT_3183_jmp_if_bit_clear_54',
        "command": 'jmp_if_bit_clear',
        "args": [0x7057, 4, 'EVENT_3183_remove_from_level_62']
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_55',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._274_MOLEVILLE_MINES_AREA_02]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_56',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._272_MOLEVILLE_MINES_AREA_11_BOMBED_ROOM_WSINGING_MOLES]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_57',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._272_MOLEVILLE_MINES_AREA_11_BOMBED_ROOM_WSINGING_MOLES]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_58',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._272_MOLEVILLE_MINES_AREA_11_BOMBED_ROOM_WSINGING_MOLES]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_59',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._272_MOLEVILLE_MINES_AREA_11_BOMBED_ROOM_WSINGING_MOLES]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_60',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._272_MOLEVILLE_MINES_AREA_11_BOMBED_ROOM_WSINGING_MOLES]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_61',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._272_MOLEVILLE_MINES_AREA_11_BOMBED_ROOM_WSINGING_MOLES]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_62',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_63',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM]
    },
    {
        "identifier": 'EVENT_3183_remove_from_level_64',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_65',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_66',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_67',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_68',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_69',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_70',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._287_MOLEVILLE_MINES_AREA_14_2LEVEL_ROOM_FROM_LONG_MINECART_TRACKS_ROOM]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_71',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._287_MOLEVILLE_MINES_AREA_14_2LEVEL_ROOM_FROM_LONG_MINECART_TRACKS_ROOM]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_72',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._287_MOLEVILLE_MINES_AREA_14_2LEVEL_ROOM_FROM_LONG_MINECART_TRACKS_ROOM]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_73',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._287_MOLEVILLE_MINES_AREA_14_2LEVEL_ROOM_FROM_LONG_MINECART_TRACKS_ROOM]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_74',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._287_MOLEVILLE_MINES_AREA_14_2LEVEL_ROOM_FROM_LONG_MINECART_TRACKS_ROOM]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_75',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._280_MOLEVILLE_MINES_AREA_15_2LEVEL_ROOM_WSPARKY_AND_10COIN_TC]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_76',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._280_MOLEVILLE_MINES_AREA_15_2LEVEL_ROOM_WSPARKY_AND_10COIN_TC]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_77',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_78',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_79',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_80',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_81',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_82',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE]
    },
    {
        "identifier": 'EVENT_3183_summon_to_level_83',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_7, Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE]
    },
    {
        "identifier": 'EVENT_3183_ret_84',
        "command": 'ret'
    }
]
