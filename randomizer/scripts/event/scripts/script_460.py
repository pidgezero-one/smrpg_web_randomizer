# E0460_COOKIE_STORAGE_YOSHI

from randomizer.scripts.event.script_imports import *

script = EventScript([
	PlaySound(sound=SO063_YOSHI_TALK, channel=6),
	JmpIfBitClear(TEMP_7044_5, ["EVENT_460_enable_controls_until_return_7"]),
	RunEventAsSubroutine(E0456_YOSHI_TALKS_TO_OTHER_YOSHI),
	JmpIfBitSet(COMPLETED_MUSHROOM_DERBY, ["EVENT_460_run_event_as_subroutine_10"]),
	RunDialog(dialog_id=DI0902_COOKIE_MANAGER_BEFORE_BEATING_BOSHI, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RunBackgroundEvent(event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, bit_7=True),
	Return(),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B], identifier="EVENT_460_enable_controls_until_return_7"),
	Pause(32),
	Return(),
	RunEventAsSubroutine(E0456_YOSHI_TALKS_TO_OTHER_YOSHI, identifier="EVENT_460_run_event_as_subroutine_10"),
	JmpToEvent(E0930_YOSHI_COOKIE_STORAGE_BUSINESS_LOGIC)
])
