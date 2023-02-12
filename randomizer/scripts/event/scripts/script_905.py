# E0905_CHEST_BLUE_M_DRINK_PACKET

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
	CreatePacketAt7010(packet=P154_BLUE_MUSIC_DRINK_CHEST, destinations=["EVENT_905_final_ret"]),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
	Return(identifier="EVENT_905_final_ret")
])
