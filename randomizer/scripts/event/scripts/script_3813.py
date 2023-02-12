# E3813_NIMBUS_INN_GUEST

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI2105_SIGNAL_RING_STAR_PIECE_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
