# E1874_TEMPLE_ELEVATOR_ROOM_SHAMAN

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI1298_TEMPLE_FINAL_FORTUNE_INSTRUCTIONS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
