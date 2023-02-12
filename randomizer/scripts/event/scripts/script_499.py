# E0499_PIPE_VAULT_ENTRANCE_TRAMPOLINE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(DIRECTIONAL_7049_0, ["EVENT_499_run_event_as_subroutine_4"]),
	RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
	EnterArea(room_id=R055_PIPE_VAULT_ENTRANCE, face_direction=SOUTH, x=17, y=18, z=0),
	JmpToEvent(E0269_PIPE_UP_SUBROUTINE),
	RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE, identifier="EVENT_499_run_event_as_subroutine_4"),
	Return()
])
