# E2246_SETS_SEASIDE_ACCESSORY_SHOP_STATE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(SEASIDE_BOSS_SET, ["EVENT_2246_jmp_if_bit_set_0"]),
	EnterArea(room_id=R217_SEASIDE_TOWN_DURING_YARIDOVICH_ACCESSORY_SHOP_RIGHTMOST, face_direction=NORTHEAST, x=24, y=64, z=0, run_entrance_event=True),
	Return(),
	JmpIfBitSet(SEASIDE_SHED_EMPTIED, ["EVENT_2246_enter_area_3"], identifier="EVENT_2246_jmp_if_bit_set_0"),
	EnterArea(room_id=R313_SEASIDE_TOWN_ACCESSORY_SHOP, face_direction=NORTHEAST, x=24, y=64, z=0, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R313_SEASIDE_TOWN_ACCESSORY_SHOP, face_direction=NORTHEAST, x=24, y=64, z=0, show_banner=True, run_entrance_event=True, identifier="EVENT_2246_enter_area_3"),
	Return()
])
