# E0427_PIPE_VAULT_CHOMPWEED_ROOM_EXIT_PIPE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToConst(X_COORD_2, 26),
	SetVarToConst(Y_COORD_2, 56),
	RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
	SetBit(MAP_YOSTER_ISLE),
	SetBit(MAP_DIRECTIONAL_PIPE_VAULT_YOSTER_ISLE),
	EnterArea(room_id=R033_YOSTER_ISLE_ENTRANCE_FROM_PIPE_VAULT, face_direction=SOUTH, x=5, y=20, z=0, run_entrance_event=True),
	RunEventAsSubroutine(E0270_TRAMPOLINE_OR_PIPE_SUBROUTINE),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_427_ret_26"]),
	RunEventAsSubroutine(E3901_YOSTER_ISLE_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_427_ret_26")
])
