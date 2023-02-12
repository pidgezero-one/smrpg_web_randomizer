# E2063_SUPER_JUMP_PRIZE_GRANT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Set7000To7FMemVar(),
	JmpIfBitSet(SUPER_JUMP_PRIZE_2_GRANTED, ["EVENT_2063_run_dialog_43"]),
	JmpIfBitSet(SUPER_JUMP_PRIZE_1_GRANTED, ["EVENT_2063_run_dialog_33"]),
	RunDialog(dialog_id=DI2627_SUPERJUMP_RECORD, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	RunEventAsSubroutine(E3393_SUPER_JUMP_COMPARE_FOR_1ST_PRIZE),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2063_run_dialog_24"]),
	RunDialog(dialog_id=DI2628_SUPERJUMP_CHALLENGE, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Return(),
	RunDialog(dialog_id=DI2629_SUPER_JUMP_PRIZE_1, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2063_run_dialog_24"),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	SetBit(SUPER_JUMP_PRIZE_1_GRANTED),
	Set7000To7FMemVar(),
	RunEventAsSubroutine(E3394_SUPER_JUMP_COMPARE_FOR_2ND_PRIZE),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2063_run_dialog_37"]),
	Return(),
	RunDialog(dialog_id=DI2627_SUPERJUMP_RECORD, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2063_run_dialog_33"),
	RunEventAsSubroutine(E3394_SUPER_JUMP_COMPARE_FOR_2ND_PRIZE),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2063_run_dialog_37"]),
	Return(),
	RunDialog(dialog_id=DI2631_SUPER_JUMP_PRIZE_2, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2063_run_dialog_37"),
	RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
	SetBit(SUPER_JUMP_PRIZE_2_GRANTED),
	Return(),
	RunDialog(dialog_id=DI2632_DOG_OUT_OF_PRIZES, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2063_run_dialog_43"),
	Return()
])
