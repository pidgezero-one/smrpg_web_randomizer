# E1141_SEASIDE_OCCUPIED_BOMB_SHOP_CUSTOMER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
