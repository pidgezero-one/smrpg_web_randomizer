# E3945_RING_CHEST

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
	CreatePacketAt7010(packet=P091_RING_CHEST, destinations=["EVENT_3945_ret_259"]),
	PlaySound(sound=SO014_FLOWER, channel=6),
	RunDialog(dialog_id=DI2097_GOT_RING, above_object=MARIO, closable=False, sync=True, multiline=False, use_background=False, bit_6=True),
	Inc(UNUSED_70B2),
	AddToInventory(Ring),
	Return(identifier="EVENT_3945_ret_259")
])
