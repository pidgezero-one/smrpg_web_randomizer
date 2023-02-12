# E0197_TOADSTOOL_JOINS_CONTAINER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI1183_TOADSTOOL_JOINS, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	JmpToEvent(E0191_TOADSTOOL_JOINS)
])
