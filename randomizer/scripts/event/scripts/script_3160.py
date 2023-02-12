# E3160_MINES_LONG_TRACK_ROOM_LOWER_BACKWARD_EXIT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	PauseScriptIfMenuOpen(),
	JmpIfObjectInSpecificLevel(NPC_0, R286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM, ["EVENT_3160_ret_3"]),
	EnterArea(room_id=R286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM, face_direction=SOUTHWEST, x=20, y=25, z=0, run_entrance_event=True),
	Return(identifier="EVENT_3160_ret_3")
])
