# E3398_MIDAS_CAVE_SINGLE_FIREWORK_GRANTER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToConst(FIREWORKS_COUNTER, 5),
	SetVarToConst(ITEM_ID, Fireworks),
	JmpToEvent(E2820_ASYNC_NO_ANIMATION_ITEM)
])
