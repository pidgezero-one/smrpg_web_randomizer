# E2646_CASINO_GRATE_GUY_AWAIT_BUTTON

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Set7000ToPressedButton(identifier="EVENT_2646_set_7000_to_pressed_button_13"),
	Pause(1),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2646_set_7000_to_pressed_button_13"]),
	Return()
])
