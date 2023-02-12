# E1629_MA_MOLE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(OPTIONAL_MINECART_CLEARED, ["EVENT_1629_jmp_if_bit_set_3"]),
	RunDialog(dialog_id=DI1104_MA_MOLE_KIDS_HURRY_HOME, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI1117_MA_MOLE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1629_jmp_if_bit_set_3"),
	Return()
])
