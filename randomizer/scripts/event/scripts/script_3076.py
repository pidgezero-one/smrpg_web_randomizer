# E3076_EXP_STAR_CHEST_BACKGROUND

from randomizer.scripts.event.script_imports import *

script = EventScript([
	MoveScriptToMainThread(),
	PlaySound(sound=SO102_TIME_RUNNING_OUT, channel=6),
	StopMusicFDA1(),
	SetBit(EXP_STAR_BIT_5),
	SetBit(EXP_STAR_BIT_6),
	SetVarToConst(TIMER_7022, 50),
	RunBackgroundEventWithPause(event_id=E3079_EXP_STAR_LEVELUP_SCREEN, timer_var=TIMER_7022),
	Return()
])
