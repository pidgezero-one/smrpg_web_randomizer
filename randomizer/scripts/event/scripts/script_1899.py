# E1899_ABYSS_AXEM_PIT_ROOM_FALL_

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Pause(1, identifier="EVENT_1899_pause_0"),
	Set7000ToObjectCoord(object=MARIO, coord=COORD_Z, pixel=True),
	CompareVarToConst(PRIMARY_TEMP_7000, 1024),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1899_pause_0"]),
	RemoveObjectFromCurrentLevel(MARIO),
	SetBit(DIRECTIONAL_7049_0),
	EnableControls([]),
	EnterArea(room_id=R445_SMITHY_FACTORY_AREA_10_FALL_FROM_AREA_09, face_direction=SOUTH, x=3, y=28, z=10, run_entrance_event=True),
	Return()
])
