# E3386_SHIP_3D_MAZE_SPAWN_PRIZE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	CreatePacketAt7010WithEvent(packet=P037_ITEM_BAG_FALL, event_id=E3290_SHIP_COLLECT_3D_MAZE_PRIZE, destinations=["EVENT_3221_pause_8"]),
	Return()
])
