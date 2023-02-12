# E3629_NIMBUS_EXTERIOR_BLUE_GUY_NEAR_SHOP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI2417_FERTILIZER_LOCATION_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
