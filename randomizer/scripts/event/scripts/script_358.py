# E0358_MUSHROOM_KINGDOM_NPC_BEHIND_HOUSE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(MAP_BANDITS_WAY, ["EVENT_358_run_dialog_12"]),
	RunDialog(dialog_id=DI1053_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI1050_I_WISH_YOU_LUCK_ON_YOUR_QUEST, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_358_run_dialog_12"),
	Return()
])
