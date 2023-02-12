# E2089_SKY_TROOPAS_AD

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI2957_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
