# E1336_PORTRAIT_GAME_5

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_1, ["EVENT_1336_ret_17"]),
	JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 1, ["EVENT_1336_apply_tile_mod_10"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=51),
	Pause(5),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=53),
	PlaySound(sound=SO088_WRONG_SIGNAL, channel=6),
	Pause(30),
	StartBattleAtBattlefield(46, BF12_BOOSTER_TOWER),
	FadeInFromBlack(sync=False),
	Jmp(["EVENT_1338_pause_0"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=51, identifier="EVENT_1336_apply_tile_mod_10"),
	Pause(5),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=52),
	PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6),
	Pause(10),
	Inc(SECONDARY_TEMP_7024),
	SetBit(TEMP_7043_1),
	Return(identifier="EVENT_1336_ret_17")
])
