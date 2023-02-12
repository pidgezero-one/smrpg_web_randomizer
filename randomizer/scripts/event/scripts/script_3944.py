# E3944_BROOCH_CHEST

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
	CreatePacketAt7010(packet=P096_BROOCH_CHEST, destinations=["EVENT_3944_ret_259"]),
	AddToInventory(Brooch),
	PlaySound(sound=SO014_FLOWER, channel=6),
	RunDialog(dialog_id=DI2095_GOT_BROOCH, above_object=MARIO, closable=False, sync=True, multiline=False, use_background=False, bit_6=True),
	Inc(UNUSED_70B2),
	Return(identifier="EVENT_3944_ret_259")
])
