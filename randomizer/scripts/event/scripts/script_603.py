# E0603_MARRYMORE_BELLHOP_LOBBY_WHILE_GUEST

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_704C_0, ["EVENT_603_run_dialog_42"]),
	JmpIfBitSet(TEMP_7042_5, ["EVENT_603_run_dialog_6"]),
	JmpIfBitSet(TEMP_7042_4, ["EVENT_603_run_dialog_44"]),
	JmpIfBitSet(TEMP_7042_0, ["EVENT_321_inc_0"]),
	RunDialog(dialog_id=DI0979_INACTIVE_BELLHOP, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI0992_GOOD_MORNING_FROM_BELLHOP, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True, identifier="EVENT_603_run_dialog_6"),
	RunDialog(dialog_id=DI0995_BELLHOP_GIFT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	RunEventAsSubroutine(E0635_MARRYMORE_INN_ELDERLY_GUEST_TIP_SUNROUTINE_3),
	SetBit(TEMP_7043_1),
	SetSyncActionScript(NPC_5, A0322_MARRYMORE_INNKEEPER_OVERSTAY_MAKES_YOU_WORK),
	Return(),
	RunDialog(dialog_id=DI1006_BELLHOP_WHILE_PLAYER_EMPLOYED, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_603_run_dialog_42"),
	Return(),
	RunDialog(dialog_id=DI0969_MAKE_YOURSELF_AT_HOME, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_603_run_dialog_44"),
	Return()
])
