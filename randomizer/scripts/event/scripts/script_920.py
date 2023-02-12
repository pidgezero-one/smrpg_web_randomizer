# E0920_CHEST_YELLOW_MUSHROOM_PACKET

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
	CreatePacketAt7010(packet=P202_YELLOW_MUSHROOM_CHEST, destinations=["EVENT_920_final_ret"]),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
	Return(identifier="EVENT_920_final_ret")
])
