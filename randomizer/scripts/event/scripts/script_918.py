# E0918_CHEST_RED_MUSHROOM_PACKET

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
	CreatePacketAt7010(packet=P196_RED_MUSHROOM_CHEST, destinations=["EVENT_918_final_ret"]),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
	Return(identifier="EVENT_918_final_ret")
])
