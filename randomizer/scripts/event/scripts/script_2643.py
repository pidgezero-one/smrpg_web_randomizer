# E2643_TOAD_SHOP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TOAD_SHOP_FREEBIE_RECEIVED, ["EVENT_2643_open_shop_6"]),
	SetBit(TOAD_SHOP_FREEBIE_RECEIVED),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	Return(),
	JmpToEvent(E1185_TOAD_SHOP, identifier="EVENT_2643_open_shop_6")
])
