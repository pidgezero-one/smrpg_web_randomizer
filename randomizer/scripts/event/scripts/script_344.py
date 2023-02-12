# E0344_MUSHROOM_KINGDOM_RAZ_RAINI_HOUSE_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(NOTE_DIRECTION),
	SetSyncActionScript(NPC_0, A0977_NOTE_WITHOUT_KNIFE),
	JmpToEvent(E0261_FADE_MUSIC_ROOM_LOADER)
])
