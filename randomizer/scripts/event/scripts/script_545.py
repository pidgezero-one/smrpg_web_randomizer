# E0545_ROSE_TOWN_OCCUPIED_KID_3

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI0817_GRANDPA_PUMPING_WATER, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
