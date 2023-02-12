# E0082_THREE_MUSTY_FEARS_GREAPER_DIALOG

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(INVISIBLE_ITEMS_ANYWHERE_EXPLAINED, ["EVENT_82_run_dialog_1"]),
	RunDialog(dialog_id=DI1105_MUSTY_FEARS_EXPLANATION, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(INVISIBLE_ITEMS_ANYWHERE_EXPLAINED),
	RunDialog(dialog_id=DI1106_INVISIBLE_ITEMS_CONFIRMED_PLACED, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_82_run_dialog_1"),
	Return()
])
