# E0562_ROSE_TOWN_LIBERATED_KIDS_INDOORS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7044_2, ["EVENT_562_run_dialog_5"]),
	JmpToSubroutine(["EVENT_562_pause_action_script_7"]),
	RunDialog(dialog_id=DI0864_CAN_FINALLY_RELAX, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpToSubroutine(["EVENT_562_resume_action_script_11"]),
	Return(),
	RunDialog(dialog_id=DI0864_CAN_FINALLY_RELAX, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_562_run_dialog_5"),
	Return(),
	PauseActionScript(NPC_2, identifier="EVENT_562_pause_action_script_7"),
	PauseActionScript(NPC_3),
	PauseActionScript(NPC_4),
	Return(),
	ResumeActionScript(NPC_2, identifier="EVENT_562_resume_action_script_11"),
	ResumeActionScript(NPC_3),
	ResumeActionScript(NPC_4),
	Return()
])
