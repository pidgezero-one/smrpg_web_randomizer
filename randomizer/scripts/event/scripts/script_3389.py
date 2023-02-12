# E3389_SHIP_BARREL_PUZZLE_SPAWN_PRIZE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	CreatePacketAt7010WithEvent(packet=P038_MUSHROOM_FALL_DEFAULT_PRIORITY, event_id=E3295_SHIP_COLLECT_BARREL_PRIZE, destinations=["EVENT_3219_pause_13"]),
	Return()
])
