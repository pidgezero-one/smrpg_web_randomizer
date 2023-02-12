# E0605_MARRYMORE_INN_LOBBY_GUEST_1

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI2055_HOTEL_TIP_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
