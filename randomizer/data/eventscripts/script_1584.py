from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1584_set_0',
        "command": 'set',
        "args": [0x70df, 37],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x708c, 4, 'EVENT_1584_jmp_if_bit_clear_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_set_2',
        "command": 'set',
        "args": [0x70df, 43],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7050, 3, 'EVENT_1584_jmp_if_bit_set_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_4',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_16, Rooms._262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'EVENT_1584_set_bit_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_set_bit_8',
        "command": 'set_bit',
        "args": [0x704f, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7050, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7094, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_clear_bit_11',
        "command": 'clear_bit',
        "args": [0x7050, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_set_12',
        "command": 'set',
        "args": [0x70ac, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_clear_bit_13',
        "command": 'clear_bit',
        "args": [0x7094, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_clear_bit_14',
        "command": 'clear_bit',
        "args": [0x707b, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_clear_bit_15',
        "command": 'clear_bit',
        "args": [0x7094, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_set_16',
        "command": 'set',
        "args": [0x70ad, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_remove_from_current_level_17',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_set_bit_18',
        "command": 'set_bit',
        "args": [0x704f, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_19',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._263_LANDS_END_UNDERGROUND_AREA_01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_20',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._263_LANDS_END_UNDERGROUND_AREA_01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_21',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._263_LANDS_END_UNDERGROUND_AREA_01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_22',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._264_LANDS_END_UNDERGROUND_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_23',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._264_LANDS_END_UNDERGROUND_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_24',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._264_LANDS_END_UNDERGROUND_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_25',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._265_LANDS_END_UNDERGROUND_AREA_03],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_26',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._265_LANDS_END_UNDERGROUND_AREA_03],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_27',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._265_LANDS_END_UNDERGROUND_AREA_03],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_28',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_29',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_30',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_31',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_32',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_33',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_34',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_35',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_7, Rooms._262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_36',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_8, Rooms._262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_37',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_9, Rooms._262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_38',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_10, Rooms._262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_39',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_11, Rooms._262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_40',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_12, Rooms._262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_41',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_13, Rooms._262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_42',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_14, Rooms._262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_summon_to_level_43',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_15, Rooms._262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_fade_in_from_black_sync_44',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_set_action_script_async_45',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1584_ret_46',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
