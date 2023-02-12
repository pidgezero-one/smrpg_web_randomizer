# E3749_NIMBUS_MEZZANINE_TRAMPOLINE_TO_TOWN_SQUARE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(DIRECTIONAL_7049_0, ["EVENT_3749_run_event_as_subroutine_16"]),
	RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
	JmpIfBitSet(NIMBUS_BOSS_IN_TOWN_SQUARE, ["EVENT_3749_enter_area_14"]),
	JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3749_set_bit_11"]),
	SetBit(TEMP_7042_0),
	EnterArea(room_id=R416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA, face_direction=NORTHEAST, x=11, y=59, z=0, run_entrance_event=True),
	Return(),
	SetBit(TEMP_7042_0, identifier="EVENT_3749_set_bit_11"),
	EnterArea(room_id=R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA, face_direction=NORTHEAST, x=11, y=59, z=0, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R430_NIMBUS_LAND_OUTSIDE_DURING_VALENTINA, face_direction=NORTHEAST, x=11, y=59, z=0, run_entrance_event=True, identifier="EVENT_3749_enter_area_14"),
	Return(),
	RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE, identifier="EVENT_3749_run_event_as_subroutine_16"),
	Return()
])
