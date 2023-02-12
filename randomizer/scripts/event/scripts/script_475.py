# E0475_MUSHROOM_DERBY_UNKNOWN

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Db(bytearray(b'\xfdD')),
	JmpToEvent(E0465_MUSHROOM_DERBY_BUSINESS_LOGIC),
	Return()
])
