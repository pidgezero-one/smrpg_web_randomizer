# E1133_SEASIDE_OCCUPIED_ACCESSORY_SHOP_OCCUPANT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
