# E3597_YOSTER_EMPTY_MAILBOX

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7044_5, ["EVENT_3597_run_event_as_subroutine_7"]),
	RunDialog(dialog_id=DI2338_CHECK_MAILBOX, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=True),
	ClearBit(TEMP_7043_0),
	Return(),
	RunEventAsSubroutine(E0456_YOSHI_TALKS_TO_OTHER_YOSHI, identifier="EVENT_3597_run_event_as_subroutine_7"),
	RunDialog(dialog_id=DI2337_YOSHI_CHECKING_MAILBOX, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=True),
	ClearBit(TEMP_7043_0),
	RunBackgroundEvent(event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, bit_7=True),
	Return()
])
