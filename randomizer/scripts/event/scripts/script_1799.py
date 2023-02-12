# E1799_TEMPLE_FINAL_FORTUNE_SCROLL

from randomizer.scripts.event.script_imports import *

script = EventScript([
	PlaySound(sound=SO084_SMOKED, channel=6),
	SetVarToConst(TEMP_7034, 1),
	Set70107015ToObjectXYZ(MEM_70A8),
	StartLoopNTimes(2),
	Pause(1, identifier="EVENT_1799_pause_4"),
	CreatePacketAt7010(packet=P032_BLUE_CLOUD, destinations=["EVENT_1799_pause_4"]),
	Pause(4),
	AddConstToVar(TEMP_7034, 3),
	EndLoop(),
	RemoveObjectFromCurrentLevel(MEM_70A8),
	JmpIfBitSet(TEMPLE_BOSS_ACCESS_FORTUNE, ["EVENT_1799_run_dialog_13"]),
	RunDialog(dialog_id=DI1238_TEMPLE_TREASURY_FORTUNE, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	Return(),
	RunDialog(dialog_id=DI1230_TEMPLE_BOSS_FORTUNE, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_1799_run_dialog_13"),
	Return()
])
