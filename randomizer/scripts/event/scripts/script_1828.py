# E1828_KEEP_MARIO_FALLS_IN_LAVA

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Pause(1, identifier="EVENT_1828_pause_0"),
	Set7000ToObjectCoord(object=MARIO, coord=COORD_Z, pixel=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1828_db_10"]),
	JmpIfMarioInAir(["EVENT_1828_pause_0"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703C),
	Set7000ToObjectCoord(object=MARIO, coord=COORD_X, pixel=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_7038),
	Set7000ToObjectCoord(object=MARIO, coord=COORD_Y, pixel=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703A),
	Jmp(["EVENT_1828_pause_0"]),
	Db(bytearray(b'\xfdD'), identifier="EVENT_1828_db_10"),
	Db(bytearray(b'\xfdG')),
	RunEventAtReturn(E1830_KEEP_HANDLE_ROOM_RELOAD_AFTER_LAVA_FALL),
	Return()
])
