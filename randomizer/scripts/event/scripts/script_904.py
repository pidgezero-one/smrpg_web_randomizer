# E0904_CHEST_YELLOW_M_DRINK_PACKET

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
	CreatePacketAt7010(packet=P151_YELLOW_MUSIC_DRINK_CHEST, destinations=["EVENT_904_final_ret"]),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
	Return(identifier="EVENT_904_final_ret")
])
