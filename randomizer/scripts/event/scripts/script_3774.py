# E3774_HOT_SPRINGS_RESET_EJECTION_TIMER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	ClearBit(TEMP_7043_1),
	StopBackgroundEvent(TIMER_701C),
	Return()
])
