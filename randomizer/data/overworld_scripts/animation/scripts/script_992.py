#A0992_DEFAULT_SEQUENCE_IN_CHEST
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.event_script_names import *
from ....variables.overworld_sfx_names import *
from ....variables.room_names import *
from ....variables.variable_names import *
from ....packets import *
from ....items import *

# ITEM_ID_SHADOW - 70A7 is a scratch variable for background events, so it gets overwritten between chest execution and packet execution.
# Shadow to an otherwise unused var so the packet can recall it.
script = ActionScript([
	A_ShadowOn(),
	A_FloatingOff(),
	A_SetVRAMPriority(PRIORITY_3),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, HoneySyrupItem().item_id, ["A0992_syrup"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, MapleSyrupItem().item_id, ["A0992_syrup"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, RoyalSyrupItem().item_id, ["A0992_syrup"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, PureWaterItem().item_id, ["A0992_syrup"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, RedEssenceItem().item_id, ["A0992_juice"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, YoshiAdeItem().item_id, ["A0992_juice"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, CricketJamItem().item_id, ["A0992_juice"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, ShedKeyItem().item_id, ["A0992_juice"]), # sequence 2 also used for keys
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, RoomKeyItem().item_id, ["A0992_juice"]), 
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, ElderKeyItem().item_id, ["A0992_juice"]), 
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, TempleKeyItem().item_id, ["A0992_juice"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, CastleKey1Item().item_id, ["A0992_juice"]), 
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, CastleKey2Item().item_id, ["A0992_juice"]), 
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, GoldPaintItem().item_id, ["A0992_juice"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, EnergizerItem().item_id, ["A0992_p"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, PowerBlastItem().item_id, ["A0992_p"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, BracerItem().item_id, ["A0992_d"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, CrystallineItem().item_id, ["A0992_d"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, FroggieDrinkItem().item_id, ["A0992_music"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, ElixirItem().item_id, ["A0992_music"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, MegalixirItem().item_id, ["A0992_music"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, KerokeroColaItem().item_id, ["A0992_frog"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, FreshenUpItem().item_id, ["A0992_r"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, AbleJuiceItem().item_id, ["A0992_r"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, CymbalsItem().item_id, ["A0992_r"]), # sequence 7 also used for music notes
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, PickMeUpItem().item_id, ["A0992_star"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, YoshiCandyItem().item_id, ["A0992_candy"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, RockCandyItem().item_id, ["A0992_candy"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, SonicCymbalItem().item_id, ["A0992_candy"]), 
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, FrightBombItem().item_id, ["A0992_bomb"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, SleepyBombItem().item_id, ["A0992_bomb"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, IceBombItem().item_id, ["A0992_bomb"]),
    A_JmpIfVarEqualsConst(ITEM_ID_SHADOW, FireBombItem().item_id, ["A0992_bomb"]),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, identifier="A0992_default"),
    A_Jmp(["A0992_begin_animation"]),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True, identifier="A0992_syrup"),
    A_Jmp(["A0992_begin_animation"]),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=True, identifier="A0992_juice"),
    A_Jmp(["A0992_begin_animation"]),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True, identifier="A0992_p"),
    A_Jmp(["A0992_begin_animation"]),
	A_SetSpriteSequence(index=4, is_sequence=True, looping=True, identifier="A0992_d"),
    A_Jmp(["A0992_begin_animation"]),
	A_SetSpriteSequence(index=5, is_sequence=True, looping=True, identifier="A0992_music"),
    A_Jmp(["A0992_begin_animation"]),
	A_SetSpriteSequence(index=6, is_sequence=True, looping=True, identifier="A0992_frog"),
    A_Jmp(["A0992_begin_animation"]),
	A_SetSpriteSequence(index=7, is_sequence=True, looping=True, identifier="A0992_r"),
    A_Jmp(["A0992_begin_animation"]),
	A_SetSpriteSequence(index=8, is_sequence=True, looping=True, identifier="A0992_star"),
    A_Jmp(["A0992_begin_animation"]),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True, identifier="A0992_candy"),
    A_Jmp(["A0992_begin_animation"]),
	A_SetSpriteSequence(index=10, is_sequence=True, looping=True, identifier="A0992_bomb"),
	A_VisibilityOff(identifier="A0992_begin_animation"),
    A_SequenceLoopingOn(),
	A_Pause(6),
	A_VisibilityOn(),
	A_Pause(26),
	A_VisibilityOff(),
	A_ReturnQueue()
])
