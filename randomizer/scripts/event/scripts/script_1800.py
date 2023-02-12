# E1800_TEMPLE_MOUSE_MONSTRO_TOWN_ACCESS_HINT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialogForDuration(dialog_id=DI1233_MONSTRO_TADPOLE_POND_HINT, duration=1, sync=False),
	JmpIfBitSet(MAP_MONSTRO_TOWN, ["EVENT_1800_ret_7"]),
	RunDialogForDuration(dialog_id=DI1166_TEMPLE_BLOCKED_PIPE_HINT, duration=1, sync=False),
	Return(identifier="EVENT_1800_ret_7")
])
