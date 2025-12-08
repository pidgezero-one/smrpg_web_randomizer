# pylint: disable=C0301

"""E3660_NIMBUS_REPOPULATE_CASTLE_UPON_LIBERATION"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(NIMBUS_LAND_LIBERATED),
        ApplySolidityModToLevel(
            permanent=True, room_id=R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA, mod_id=0
        ),
        Pause(1),
        ApplySolidityModToLevel(
            permanent=True, room_id=R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA, mod_id=1
        ),
        ApplySolidityModToLevel(
            permanent=True, room_id=R497_NIMBUS_CASTLE_AREA_06_____DUMMY, mod_id=0
        ),
        RemoveObjectFromSpecificLevel(NPC_1, R009_MARRYMORE_INN_REGULAR_ROOM),
        RemoveObjectFromSpecificLevel(
            NPC_0, R113_NIMBUS_CASTLE_AREA_16_SMALL_TWODOOR_ROOM_WTREASURE_FROM_AREA_15
        ),
        SummonObjectToSpecificLevel(
            NPC_3, R113_NIMBUS_CASTLE_AREA_16_SMALL_TWODOOR_ROOM_WTREASURE_FROM_AREA_15
        ),
        RemoveObjectFromSpecificLevel(
            NPC_1, R116_NIMBUS_CASTLE_AREA_02_LEFT_OF_AREA_01
        ),
        RemoveObjectFromSpecificLevel(
            NPC_2, R116_NIMBUS_CASTLE_AREA_02_LEFT_OF_AREA_01
        ),
        RemoveObjectFromSpecificLevel(
            NPC_3, R116_NIMBUS_CASTLE_AREA_02_LEFT_OF_AREA_01
        ),
        SummonObjectToSpecificLevel(NPC_4, R116_NIMBUS_CASTLE_AREA_02_LEFT_OF_AREA_01),
        SummonObjectToSpecificLevel(NPC_5, R116_NIMBUS_CASTLE_AREA_02_LEFT_OF_AREA_01),
        RemoveObjectFromSpecificLevel(
            NPC_2,
            R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT),
        RemoveObjectFromSpecificLevel(
            NPC_3,
            R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT),
        RemoveObjectFromSpecificLevel(
            NPC_4,
            R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT),
        RemoveObjectFromSpecificLevel(
            NPC_5,
            R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT),
        SummonObjectToSpecificLevel(
            NPC_0,
            R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT),
        SummonObjectToSpecificLevel(
            NPC_1,
            R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT),
        RemoveObjectFromSpecificLevel(
            NPC_0, R119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05
        ),
        RemoveObjectFromSpecificLevel(
            NPC_1, R119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05
        ),
        RemoveObjectFromSpecificLevel(
            NPC_2, R119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05
        ),
        RemoveObjectFromSpecificLevel(
            NPC_3, R119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05
        ),
        SummonObjectToSpecificLevel(
            NPC_4, R119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05
        ),
        SummonObjectToSpecificLevel(
            NPC_6, R119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05
        ),
        SummonObjectToSpecificLevel(
            NPC_7, R119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05
        ),
        RemoveObjectFromSpecificLevel(
            NPC_0, R408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM_
        ),
        RemoveObjectFromSpecificLevel(
            NPC_1, R408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM_
        ),
        RemoveObjectFromSpecificLevel(
            NPC_2, R408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM_
        ),
        RemoveObjectFromSpecificLevel(
            NPC_3, R408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM_
        ),
        SummonObjectToSpecificLevel(
            NPC_4, R408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM_
        ),
        SummonObjectToSpecificLevel(
            NPC_6, R408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM_
        ),
        SummonObjectToSpecificLevel(
            NPC_7, R408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM_
        ),
        RemoveObjectFromSpecificLevel(
            NPC_2, R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE
        ),
        RemoveObjectFromSpecificLevel(
            NPC_3, R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE
        ),
        RemoveObjectFromSpecificLevel(
            NPC_5, R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE
        ),
        SummonObjectToSpecificLevel(
            NPC_4, R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE
        ),
        RemoveObjectFromSpecificLevel(
            NPC_2, R414_NIMBUS_CASTLE_AREA_08_FROM_AREA_07_GET_ROOM_KEY_1_HERE
        ),
        RemoveObjectFromSpecificLevel(
            NPC_3, R414_NIMBUS_CASTLE_AREA_08_FROM_AREA_07_GET_ROOM_KEY_1_HERE
        ),
        RemoveObjectFromSpecificLevel(
            NPC_4, R414_NIMBUS_CASTLE_AREA_08_FROM_AREA_07_GET_ROOM_KEY_1_HERE
        ),
        RemoveObjectFromSpecificLevel(
            NPC_0, R411_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_1ST
        ),
        RemoveObjectFromSpecificLevel(
            NPC_1, R411_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_1ST
        ),
        RemoveObjectFromSpecificLevel(
            NPC_2, R411_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_1ST
        ),
        RemoveObjectFromSpecificLevel(
            NPC_3, R411_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_1ST
        ),
        RemoveObjectFromSpecificLevel(
            NPC_2, R412_NIMBUS_CASTLE_AREA_11_LONG_HALLWAY_DOOR_TO_KINGS_CELLAR
        ),
        RemoveObjectFromSpecificLevel(
            NPC_3, R412_NIMBUS_CASTLE_AREA_11_LONG_HALLWAY_DOOR_TO_KINGS_CELLAR
        ),
        RemoveObjectFromSpecificLevel(
            NPC_4, R412_NIMBUS_CASTLE_AREA_11_LONG_HALLWAY_DOOR_TO_KINGS_CELLAR
        ),
        RemoveObjectFromSpecificLevel(
            NPC_0, R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND
        ),
        SummonObjectToSpecificLevel(
            NPC_1, R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND
        ),
        RemoveObjectFromSpecificLevel(
            NPC_2, R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND
        ),
        RemoveObjectFromSpecificLevel(
            NPC_3, R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND
        ),
        RemoveObjectFromSpecificLevel(
            NPC_4, R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND
        ),
        RemoveObjectFromSpecificLevel(
            NPC_5, R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND
        ),
        ClearBit(INNER_FACTORY_ROOM_2_COMPLETED),
        RemoveObjectFromSpecificLevel(
            NPC_0, R437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD
        ),
        RemoveObjectFromSpecificLevel(
            NPC_1, R437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD
        ),
        RemoveObjectFromSpecificLevel(
            NPC_2, R437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD
        ),
        RemoveObjectFromSpecificLevel(
            NPC_0, R345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING
        ),
        RemoveObjectFromSpecificLevel(
            NPC_1, R345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING
        ),
        RemoveObjectFromSpecificLevel(
            NPC_2, R345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING
        ),
        RemoveObjectFromSpecificLevel(
            NPC_3, R345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING
        ),
        SummonObjectToSpecificLevel(
            NPC_4, R345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING
        ),
        SummonObjectToSpecificLevel(NPC_7, R341_NIMBUS_LAND_GARROS_HOUSE),
        SummonObjectToSpecificLevel(NPC_6, R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL),
        SummonObjectToSpecificLevel(NPC_7, R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL),
        SummonObjectToSpecificLevel(NPC_1, R368_NIMBUS_LAND_ROYAL_BUS_STATION),
        RemoveObjectFromSpecificLevel(NPC_1, R378_BEAN_VALLEY_BEANSTALKS_AREA_01),
        RemoveObjectFromSpecificLevel(NPC_2, R378_BEAN_VALLEY_BEANSTALKS_AREA_01),
        RemoveObjectFromSpecificLevel(NPC_1, R379_BEAN_VALLEY_BEANSTALKS_AREA_02),
        RemoveObjectFromSpecificLevel(NPC_7, R379_BEAN_VALLEY_BEANSTALKS_AREA_02),
        SummonObjectToSpecificLevel(NPC_2, R379_BEAN_VALLEY_BEANSTALKS_AREA_02),
        RemoveObjectFromSpecificLevel(
            NPC_0, R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02
        ),
        SummonObjectToSpecificLevel(
            NPC_1, R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02
        ),
        RemoveObjectFromSpecificLevel(
            NPC_1, R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02
        ),
        RemoveObjectFromSpecificLevel(
            NPC_2, R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02
        ),
        RemoveObjectFromSpecificLevel(
            NPC_3, R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_2,
            R111_NIMBUS_CASTLE_AREA_04_LEFT_OF_4WAY_PATH_RIGHTANGLE_RED_BRICK_PATH_W_TREASURE,
            ["EVENT_3660_jmp_if_object_trigger_enabled_90"]),
        DisableObjectTriggerInSpecificLevel(
            NPC_0, R500_NIMBUS_CASTLE_AREA_04_____DUMMY
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0,
            R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
            ["EVENT_3660_jmp_if_object_trigger_enabled_92"],
            identifier="EVENT_3660_jmp_if_object_trigger_enabled_90"),
        DisableObjectTriggerInSpecificLevel(
            NPC_0, R498_NIMBUS_CASTLE_AREA_10_____DUMMY
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1,
            R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
            ["EVENT_3660_ret_94"],
            identifier="EVENT_3660_jmp_if_object_trigger_enabled_92"),
        DisableObjectTriggerInSpecificLevel(
            NPC_1, R498_NIMBUS_CASTLE_AREA_10_____DUMMY
        ),
        Return(identifier="EVENT_3660_ret_94"),
    ]
)
