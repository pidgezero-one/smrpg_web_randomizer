# E1818_LANDS_END_DESERT_MOUSE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfMarioOnAnObjectOrNot(['EVENT_1818_play_sound_13', 'EVENT_1818_run_dialog_8']),
	RunDialog(dialog_id=DI1274_WHIRLPOOL_INSTRUCTIONS, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_1818_run_dialog_8"),
	Return(),
	PlaySound(sound=SO030_SURPRISED_MONSTER, channel=6, identifier="EVENT_1818_play_sound_13"),
	RunDialog(dialog_id=DI1275_JUMP_ON_LANDS_END_MOUSE, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	Return()
])
