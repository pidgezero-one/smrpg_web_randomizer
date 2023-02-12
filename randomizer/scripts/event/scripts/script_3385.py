# E3385_SHIP_UPPER_STAIRWAY_ITEM_PACKET_GRANT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	CreatePacketAt7010WithEvent(packet=P035_FLOWER_FALL, event_id=E3247__ITEM_BEHIND_SHIP_UPPER_STAIRS_GRANTER, destinations=["EVENT_3385_ret"]),
	Return(identifier="EVENT_3385_ret")
])
