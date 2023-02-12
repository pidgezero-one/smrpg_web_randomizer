# E0926_CHEST_RED_SHELL_PACKET

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
	CreatePacketAt7010(packet=P220_RED_SHELL_CHEST, destinations=["EVENT_926_final_ret"]),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
	Return(identifier="EVENT_926_final_ret")
])
