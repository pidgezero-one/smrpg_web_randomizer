# E0272_PAUSE_ACTIVE_UNTIL_A_PRESSED

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Pause(1, identifier="EVENT_272_pause_0"),
	Set7000ToTappedButton(),
	JmpIf7000AnyBitsSet(destinations=["EVENT_272_ret_4"]),
	Jmp(["EVENT_272_pause_0"]),
	Return(identifier="EVENT_272_ret_4")
])
