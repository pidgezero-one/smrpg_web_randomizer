# E3073_ITEM_CHEST

from randomizer.scripts.event.script_imports import *

script = EventScript([
	DisableObjectTrigger(MEM_70A8),
	PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
	DisableTriggerInLevel(),
	SetSyncActionScript(MEM_70A8, A0007_HIT_TREASURE_CHEST_CONTENTS_DEPLETED),
	Set70107015ToObjectXYZ(MEM_70A8),
	CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_7000),
	AddConstToVar(PRIMARY_TEMP_7000, 608),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Z_COORD_1),
	JmpIfBitSet(UNKNOWN_704A_3, ["EVENT_3073_clear_bit_10"]),
	PlaySound(sound=SO014_FLOWER, channel=6),
	ClearBit(UNKNOWN_704A_3, identifier="EVENT_3073_clear_bit_10"),
	Return()
])
