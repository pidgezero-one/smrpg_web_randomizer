# E3714_NIMBUS_CASTLE_ANGLED_PLANT_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfObjectNotInSpecificLevel(NPC_4, R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, ["EVENT_3714_jmp_if_object_not_in_level_6"]),
	JmpIfObjectNotInSpecificLevel(NPC_2, R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, ["EVENT_3714_jmp_if_object_not_in_level_12"]),
	RunBackgroundEvent(event_id=E3713_NIMBUS_CASTLE_ANGLED_PLANT_ROOM_NPC_ANIMATIONS, return_on_level_exit=True),
	RunBackgroundEvent(event_id=E3716_NIMBUS_CASTLE_ANGLED_PLANT_ROOM_RIGHT_FAN_GUST, return_on_level_exit=True, bit_6=True),
	FadeInFromBlack(sync=False),
	Return(),
	JmpIfObjectNotInSpecificLevel(NPC_2, R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, ["EVENT_3585_fade_in_from_black_async_0"], identifier="EVENT_3714_jmp_if_object_not_in_level_6"),
	JmpIfObjectNotInSpecificLevel(NPC_3, R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, ["EVENT_3714_set_action_script_sync_9"]),
	RunBackgroundEvent(event_id=E3716_NIMBUS_CASTLE_ANGLED_PLANT_ROOM_RIGHT_FAN_GUST, return_on_level_exit=True, bit_6=True),
	SetSyncActionScript(NPC_2, A0257_NIMBUS_PINWHEEL_LEFT, identifier="EVENT_3714_set_action_script_sync_9"),
	FadeInFromBlack(sync=False),
	Return(),
	JmpIfObjectNotInSpecificLevel(NPC_3, R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, ["EVENT_3714_jmp_if_object_not_in_level_14"], identifier="EVENT_3714_jmp_if_object_not_in_level_12"),
	RunBackgroundEvent(event_id=E3716_NIMBUS_CASTLE_ANGLED_PLANT_ROOM_RIGHT_FAN_GUST, return_on_level_exit=True, bit_6=True),
	JmpIfObjectNotInSpecificLevel(NPC_4, R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, ["EVENT_3714_fade_in_from_black_async_16"], identifier="EVENT_3714_jmp_if_object_not_in_level_14"),
	SetSyncActionScript(NPC_4, A0881_NIMBUS_SHAMAN),
	FadeInFromBlack(sync=False, identifier="EVENT_3714_fade_in_from_black_async_16"),
	Return()
])
