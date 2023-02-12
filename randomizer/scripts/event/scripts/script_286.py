# E0286_AWAIT_B_PRESS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	EnableControlsUntilReturn([]),
	Pause(1, identifier="EVENT_286_pause_1"),
	Set7000ToTappedButton(),
	JmpIf7000AnyBitsSet(destinations=["EVENT_256_ret_0"]),
	Jmp(["EVENT_286_pause_1"])
])
