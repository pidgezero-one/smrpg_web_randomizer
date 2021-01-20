from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3660_set_bit_0',
        "command": 'set_bit',
        "args": [0x705e, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_set_bit_1',
        "command": 'set_bit',
        "args": [0x705f, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_apply_solidity_mod_2',
        "command": 'apply_solidity_mod',
        "args": [Rooms._438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_pause_3',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_apply_solidity_mod_4',
        "command": 'apply_solidity_mod',
        "args": [Rooms._438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA, 1, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_apply_solidity_mod_5',
        "command": 'apply_solidity_mod',
        "args": [Rooms._497_NIMBUS_CASTLE_AREA_06_____DUMMY, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_6',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._009_MARRYMORE_INN_REGULAR_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_7',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._113_NIMBUS_CASTLE_AREA_16_SMALL_TWODOOR_ROOM_WTREASURE_FROM_AREA_15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_summon_to_level_8',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._113_NIMBUS_CASTLE_AREA_16_SMALL_TWODOOR_ROOM_WTREASURE_FROM_AREA_15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_9',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._116_NIMBUS_CASTLE_AREA_02_LEFT_OF_AREA_01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_10',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._116_NIMBUS_CASTLE_AREA_02_LEFT_OF_AREA_01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_11',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._116_NIMBUS_CASTLE_AREA_02_LEFT_OF_AREA_01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_summon_to_level_12',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._116_NIMBUS_CASTLE_AREA_02_LEFT_OF_AREA_01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_summon_to_level_13',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._116_NIMBUS_CASTLE_AREA_02_LEFT_OF_AREA_01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_14',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_15',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_16',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_17',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_summon_to_level_18',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_summon_to_level_19',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_20',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_21',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_22',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_23',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_summon_to_level_24',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_summon_to_level_25',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_summon_to_level_26',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_7, Rooms._119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_27',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM_],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_28',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM_],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_29',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM_],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_30',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM_],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_summon_to_level_31',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM_],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_summon_to_level_32',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM_],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_summon_to_level_33',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_7, Rooms._408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM_],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_34',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_35',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_36',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_summon_to_level_37',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_38',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._414_NIMBUS_CASTLE_AREA_08_FROM_AREA_07_GET_ROOM_KEY_1_HERE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_stop_sound_39',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_stop_sound_40',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_stop_sound_41',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_42',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._414_NIMBUS_CASTLE_AREA_08_FROM_AREA_07_GET_ROOM_KEY_1_HERE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_43',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._414_NIMBUS_CASTLE_AREA_08_FROM_AREA_07_GET_ROOM_KEY_1_HERE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_44',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._414_NIMBUS_CASTLE_AREA_08_FROM_AREA_07_GET_ROOM_KEY_1_HERE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_45',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._411_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_1ST],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_46',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._411_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_1ST],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_47',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._411_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_1ST],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_48',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._411_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_1ST],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_49',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._412_NIMBUS_CASTLE_AREA_11_LONG_HALLWAY_DOOR_TO_KINGS_CELLAR],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_50',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_8, Rooms._412_NIMBUS_CASTLE_AREA_11_LONG_HALLWAY_DOOR_TO_KINGS_CELLAR],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_51',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_9, Rooms._412_NIMBUS_CASTLE_AREA_11_LONG_HALLWAY_DOOR_TO_KINGS_CELLAR],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_52',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_summon_to_level_53',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_54',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_55',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_56',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_57',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_clear_bit_58',
        "command": 'clear_bit',
        "args": [0x7090, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_59',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_60',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_61',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_62',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_63',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_64',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_65',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_summon_to_level_66',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_summon_to_level_67',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_7, Rooms._341_NIMBUS_LAND_GARROS_HOUSE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_summon_to_level_68',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_9, Rooms._109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_summon_to_level_69',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_10, Rooms._109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_summon_to_level_70',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._368_NIMBUS_LAND_ROYAL_BUS_STATION],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_71',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_72',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_73',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_74',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_75',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._378_BEAN_VALLEY_BEANSTALKS_AREA_01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_76',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._378_BEAN_VALLEY_BEANSTALKS_AREA_01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_77',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._378_BEAN_VALLEY_BEANSTALKS_AREA_01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_78',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._379_BEAN_VALLEY_BEANSTALKS_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_79',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._379_BEAN_VALLEY_BEANSTALKS_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_80',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._379_BEAN_VALLEY_BEANSTALKS_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_summon_to_level_81',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._379_BEAN_VALLEY_BEANSTALKS_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_82',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_summon_to_level_83',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_84',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_85',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_86',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_remove_from_level_87',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_jmp_if_object_trigger_enabled_88',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_2, Rooms._111_NIMBUS_CASTLE_AREA_04_LEFT_OF_4WAY_PATH_RIGHTANGLE_RED_BRICK_PATH_W_TREASURE, 'EVENT_3660_jmp_if_object_trigger_enabled_90'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_disable_trigger_in_level_89',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_0, Rooms._500_NIMBUS_CASTLE_AREA_04_____DUMMY],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_jmp_if_object_trigger_enabled_90',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_0, Rooms._114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM, 'EVENT_3660_jmp_if_object_trigger_enabled_92'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_disable_trigger_in_level_91',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_0, Rooms._498_NIMBUS_CASTLE_AREA_10_____DUMMY],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_jmp_if_object_trigger_enabled_92',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_1, Rooms._114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM, 'EVENT_3660_ret_94'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_disable_trigger_in_level_93',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_1, Rooms._498_NIMBUS_CASTLE_AREA_10_____DUMMY],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3660_ret_94',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
