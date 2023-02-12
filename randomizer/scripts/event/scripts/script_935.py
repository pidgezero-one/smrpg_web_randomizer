# E0935_MARRYMORE_INN_REGULAR_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfObjectNotInSpecificLevel(NPC_1, R009_MARRYMORE_INN_REGULAR_ROOM, ["EVENT_935_jmp_if_bit_set_4"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R009_MARRYMORE_INN_REGULAR_ROOM, mod_id=33),
	JmpIfBitSet(MARRYMORE_REGULAR_INN, ["EVENT_256_ret_0"], identifier="EVENT_935_jmp_if_bit_set_4"),
	FadeInFromBlack(sync=False),
	Return()
])
