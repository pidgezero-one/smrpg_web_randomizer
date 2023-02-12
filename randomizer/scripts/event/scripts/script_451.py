# E0451_GOOMBA_THUMPIN_GOOMBA_4

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_4, ["EVENT_256_ret_0"]),
	SetBit(TEMP_7043_4),
	PlaySound(sound=SO066_KICK_BALL_SHELL, channel=6),
	SetSyncActionScript(MARIO, A0210_GOOMBA_THUMPIN),
	SetSyncActionScript(NPC_4, A0423_GOOMBA_THUMPIN_BONK),
	Inc(SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
	RunDialog(dialog_id=DI0835_DUPLICATE, above_object=MARIO, closable=False, sync=True, multiline=True, use_background=False),
	Return()
])
