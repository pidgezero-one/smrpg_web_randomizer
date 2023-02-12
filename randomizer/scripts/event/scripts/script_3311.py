# E3311_SHIP_SHOP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E1603_EXP_STAR_SUBROUTINE_CANCEL_TILE_EVENT),
	JmpIfBitSet(TEMP_7042_2, ["EVENT_3311_jmp_if_bit_set_3"]),
	Jmp(["EVENT_3311_open_shop_12"]),
	JmpIfBitSet(TEMP_7042_6, ["EVENT_3311_run_dialog_11"], identifier="EVENT_3311_jmp_if_bit_set_3"),
	CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_3311_run_dialog_9"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_3311_run_dialog_11"]),
	RunDialog(dialog_id=DI1691_SHAMAN_PASSWORD_PROGRESS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_3311_open_shop_12"]),
	RunDialog(dialog_id=DI1686_SHAMAN_PASSWORD_WRONG, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3311_run_dialog_9"),
	Jmp(["EVENT_3311_open_shop_12"]),
	RunDialog(dialog_id=DI1687_SHAMAN_PASSWORD_RIGHT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3311_run_dialog_11"),
	RunEventAsSubroutine(E3297_SEA_SHOP, identifier="EVENT_3311_open_shop_12"),
	JmpIfBitSet(TEMP_7042_6, ["EVENT_3311_ret_16"]),
	RunDialog(dialog_id=DI1690_SEA_SHOPKEEPER_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(identifier="EVENT_3311_ret_16")
])
