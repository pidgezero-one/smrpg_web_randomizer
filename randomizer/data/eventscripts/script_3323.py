from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3323_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 0, 'EVENT_3323_set_7000_to_current_level_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_jmp_to_subroutine_1',
        "command": 'jmp_to_subroutine',
        "args": [0x3e33],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_set_bit_2',
        "command": 'set_bit',
        "args": [0x7042, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_set_7000_to_current_level_3',
        "command": 'set_7000_to_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 354, 'EVENT_3333_set_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_run_event_as_subroutine_5',
        "command": 'run_event_as_subroutine',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_7',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._355_VOLCANO_AREA_03_SECRET_WTWO_FLOWERS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_8',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._355_VOLCANO_AREA_03_SECRET_WTWO_FLOWERS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_9',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._355_VOLCANO_AREA_03_SECRET_WTWO_FLOWERS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_10',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._356_VOLCANO_AREA_08],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_11',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._356_VOLCANO_AREA_08],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_12',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._356_VOLCANO_AREA_08],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_13',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._358_VOLCANO_AREA_11],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_14',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_7, Rooms._358_VOLCANO_AREA_11],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_15',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._359_VOLCANO_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_16',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._359_VOLCANO_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_17',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._360_VOLCANO_AREA_04_BUNCH_OF_STEPS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_18',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._360_VOLCANO_AREA_04_BUNCH_OF_STEPS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_19',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._361_VOLCANO_AREA_09],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_20',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._361_VOLCANO_AREA_09],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_21',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._361_VOLCANO_AREA_09],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_22',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._361_VOLCANO_AREA_09],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_23',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._361_VOLCANO_AREA_09],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_24',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._362_VOLCANO_AREA_07_STOMPING_CORKPEDITE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_remove_from_level_25',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._362_VOLCANO_AREA_07_STOMPING_CORKPEDITE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_remove_from_level_26',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._362_VOLCANO_AREA_07_STOMPING_CORKPEDITE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_remove_from_level_27',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._362_VOLCANO_AREA_07_STOMPING_CORKPEDITE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_remove_from_level_28',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._362_VOLCANO_AREA_07_STOMPING_CORKPEDITE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_29',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._363_VOLCANO_AREA_15_STOMPING_CORKPEDITE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_remove_from_level_30',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._363_VOLCANO_AREA_15_STOMPING_CORKPEDITE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_remove_from_level_31',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._363_VOLCANO_AREA_15_STOMPING_CORKPEDITE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_remove_from_level_32',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._363_VOLCANO_AREA_15_STOMPING_CORKPEDITE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_remove_from_level_33',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._363_VOLCANO_AREA_15_STOMPING_CORKPEDITE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_34',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._364_VOLCANO_AREA_14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_35',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._364_VOLCANO_AREA_14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_36',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._364_VOLCANO_AREA_14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_remove_from_level_37',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._364_VOLCANO_AREA_14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_remove_from_level_38',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._364_VOLCANO_AREA_14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_39',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._386_VOLCANO_AREA_12_ERUPTING_STUMPET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_40',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._386_VOLCANO_AREA_12_ERUPTING_STUMPET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_41',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._386_VOLCANO_AREA_12_ERUPTING_STUMPET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_42',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._386_VOLCANO_AREA_12_ERUPTING_STUMPET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_43',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._386_VOLCANO_AREA_12_ERUPTING_STUMPET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_44',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._386_VOLCANO_AREA_12_ERUPTING_STUMPET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_remove_from_level_45',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._386_VOLCANO_AREA_12_ERUPTING_STUMPET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_remove_from_level_46',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._386_VOLCANO_AREA_12_ERUPTING_STUMPET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_remove_from_level_47',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_8, Rooms._386_VOLCANO_AREA_12_ERUPTING_STUMPET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_remove_from_level_48',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_9, Rooms._386_VOLCANO_AREA_12_ERUPTING_STUMPET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_49',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_10, Rooms._386_VOLCANO_AREA_12_ERUPTING_STUMPET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_50',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_11, Rooms._386_VOLCANO_AREA_12_ERUPTING_STUMPET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_51',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._367_VOLCANO_AREA_17_LEADS_TO_HINOPIOS_SHOP],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_52',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._367_VOLCANO_AREA_17_LEADS_TO_HINOPIOS_SHOP],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_53',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._367_VOLCANO_AREA_17_LEADS_TO_HINOPIOS_SHOP],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_54',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._383_VOLCANO_AREA_10_JUMPING_PYROSPHERES],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_55',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._383_VOLCANO_AREA_10_JUMPING_PYROSPHERES],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_56',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._383_VOLCANO_AREA_10_JUMPING_PYROSPHERES],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_57',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._384_VOLCANO_AREA_05],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_58',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._384_VOLCANO_AREA_05],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_remove_from_level_59',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._384_VOLCANO_AREA_05],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_remove_from_level_60',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._384_VOLCANO_AREA_05],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_61',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._385_VOLCANO_AREA_06],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_remove_from_level_62',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._385_VOLCANO_AREA_06],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_remove_from_level_63',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._385_VOLCANO_AREA_06],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_remove_from_level_64',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._385_VOLCANO_AREA_06],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_65',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_8, Rooms._389_VOLCANO_AREA_20_JUMPING_PYROSPHERES],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_66',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_9, Rooms._389_VOLCANO_AREA_20_JUMPING_PYROSPHERES],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_67',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_10, Rooms._389_VOLCANO_AREA_20_JUMPING_PYROSPHERES],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_68',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_11, Rooms._389_VOLCANO_AREA_20_JUMPING_PYROSPHERES],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_69',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._390_VOLCANO_AREA_16_ERUPTING_STUMPET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_70',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._390_VOLCANO_AREA_16_ERUPTING_STUMPET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_71',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._390_VOLCANO_AREA_16_ERUPTING_STUMPET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_72',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._390_VOLCANO_AREA_16_ERUPTING_STUMPET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_73',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._390_VOLCANO_AREA_16_ERUPTING_STUMPET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_summon_to_level_74',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._390_VOLCANO_AREA_16_ERUPTING_STUMPET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_remove_from_level_75',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._390_VOLCANO_AREA_16_ERUPTING_STUMPET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_remove_from_level_76',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._390_VOLCANO_AREA_16_ERUPTING_STUMPET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_remove_from_level_77',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_8, Rooms._390_VOLCANO_AREA_16_ERUPTING_STUMPET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_remove_from_level_78',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_9, Rooms._390_VOLCANO_AREA_16_ERUPTING_STUMPET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_apply_tile_mod_79',
        "command": 'apply_tile_mod',
        "args": [Rooms._390_VOLCANO_AREA_16_ERUPTING_STUMPET, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_apply_tile_mod_80',
        "command": 'apply_tile_mod',
        "args": [Rooms._390_VOLCANO_AREA_16_ERUPTING_STUMPET, 1, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3323_ret_81',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
