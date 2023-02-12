# E0564_ROSE_TOWN_LIBERATED_KID_OUTDOORS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7044_2, ["EVENT_564_run_dialog_5"]),
	JmpToSubroutine(["EVENT_562_pause_action_script_7"]),
	RunDialog(dialog_id=DI0867_ILL_CARRY_THAT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpToSubroutine(["EVENT_562_resume_action_script_11"]),
	Return(),
	RunDialog(dialog_id=DI0864_CAN_FINALLY_RELAX, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_564_run_dialog_5"),
	Return()
])
