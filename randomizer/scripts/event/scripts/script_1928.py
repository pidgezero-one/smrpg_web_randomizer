# E1928_BALCONY_IS_LOCKED

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI2811_ITS_LOCKED, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	Pause(30),
	RunDialog(dialog_id=DI2812_TOP_OF_TOWER_WITH_FAST_TRAVEL_DISABLED, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	Pause(30),
	RunDialog(dialog_id=DI2813_TOP_OF_TOWER_WITH_FAST_TRAVEL_DISABLED, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	Return()
])
