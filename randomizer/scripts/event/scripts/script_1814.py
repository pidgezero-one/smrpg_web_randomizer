# E1814_START_TROOPA_CLIFF_TIMER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7044_7, ["EVENT_1814_ret_10"]),
	JmpIfBitClear(TEMPLE_BOSS_DEFEATED, ["EVENT_1814_ret_10"]),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_1814_ret_10"]),
	SetBit(TEMP_7043_0),
	ClearBit(TEMP_7044_2),
	FadeOutMusicToVolume(duration=2, volume=0),
	PlaySound(sound=SO147_CLICK, channel=4),
	SetVarToConst(SECONDARY_TEMP_7024, 0),
	SetVarToConst(TEMP_7026, 0),
	RunBackgroundEvent(event_id=E1815_TROOPA_CLIFF_TIMER, return_on_level_exit=True),
	Return(identifier="EVENT_1814_ret_10")
])
