# E0630_MARRYMORE_KITCHEN_CHEF_1

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI2061_HEAD_CHEF, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
