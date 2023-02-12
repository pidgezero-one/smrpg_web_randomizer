# E0596_MINES_BOSS_ROOM_BACKGROUND_EXPLOSIONS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Pause(1, identifier="EVENT_596_pause_0"),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_596_pause_31"]),
	JmpIfObjectInCurrentLevel(NPC_2, ["EVENT_596_pause_8"]),
	Jmp(["EVENT_596_pause_0"]),
	Pause(34, identifier="EVENT_596_pause_8"),
	SetSyncActionScript(NPC_1, A0299_MINES_FINAL_BOSS_ROOM_TINY_HENCHMAN_EXPLODE),
	Pause(1, identifier="EVENT_596_pause_10"),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_596_pause_34"]),
	JmpIfObjectInCurrentLevel(NPC_3, ["EVENT_596_pause_18"]),
	Jmp(["EVENT_596_pause_10"]),
	Pause(34, identifier="EVENT_596_pause_18"),
	SetSyncActionScript(NPC_2, A0299_MINES_FINAL_BOSS_ROOM_TINY_HENCHMAN_EXPLODE),
	Pause(1, identifier="EVENT_596_pause_20"),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_596_pause_37"]),
	JmpIfObjectInCurrentLevel(NPC_1, ["EVENT_596_pause_28"]),
	Jmp(["EVENT_596_pause_20"]),
	Pause(34, identifier="EVENT_596_pause_28"),
	SetSyncActionScript(NPC_3, A0299_MINES_FINAL_BOSS_ROOM_TINY_HENCHMAN_EXPLODE),
	Jmp(["EVENT_596_pause_0"]),
	Pause(2, identifier="EVENT_596_pause_31"),
	CreatePacketAtObjectCoords(packet=P033_BOMB_EXPLOSION, object=NPC_2, destinations=["EVENT_596_pause_31"]),
	Jmp(["EVENT_596_pause_10"]),
	Pause(2, identifier="EVENT_596_pause_34"),
	CreatePacketAtObjectCoords(packet=P033_BOMB_EXPLOSION, object=NPC_3, destinations=["EVENT_596_pause_34"]),
	Jmp(["EVENT_596_pause_20"]),
	Pause(2, identifier="EVENT_596_pause_37"),
	CreatePacketAtObjectCoords(packet=P033_BOMB_EXPLOSION, object=NPC_1, destinations=["EVENT_596_pause_37"]),
	Jmp(["EVENT_596_pause_0"])
])
