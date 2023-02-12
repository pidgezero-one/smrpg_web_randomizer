# E3384_SHIP_TROOPA_PRIZE_PACKET_GRANT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	CreatePacketAt7010WithEvent(packet=P036_MUSHROOM_FALL, event_id=E3288_SHIP_SPAWN_PRIZE_IN_TROOPA_PUZZLE_ROOM, destinations=["EVENT_3223_pause_9"]),
	Jmp(["EVENT_3223_ret_11"])
])
