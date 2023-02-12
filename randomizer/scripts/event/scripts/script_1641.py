# E1641_TELLS_YOU_MINECART_PB

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Set7000ToMinecartTimer(),
	RunDialog(dialog_id=DI1137_MINECART_RECORD_STATEMENT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
