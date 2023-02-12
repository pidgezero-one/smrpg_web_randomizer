# E3946_CROWN_CHEST

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
	CreatePacketAt7010(packet=P103_CROWN_CHEST, destinations=["EVENT_3946_ret_259"]),
	PlaySound(sound=SO014_FLOWER, channel=6),
	RunDialog(dialog_id=DI2098_GOT_CROWN, above_object=MARIO, closable=False, sync=True, multiline=False, use_background=False, bit_6=True),
	Inc(UNUSED_70B2),
	AddToInventory(Crown),
	Return(identifier="EVENT_3946_ret_259")
])
