# E4077_PACKET_OF_E0165 (auto: E165 minus FD F2 presence-commit, jumps repointed)
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.colours import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.controller_inputs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.intro_title_text import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_types import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_rows import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.battlefield_names import *
from ....variables.dialog_names import *
from ....variables.event_script_names import *
from ....variables.music_names import *
from ....variables.overworld_area_names import *
from ....variables.overworld_sfx_names import *
from ....variables.pack_names import *
from ....variables.room_names import *
from ....variables.shop_names import *
from ....variables.variable_names import *
from ....items import *
from ....packets import *
from ....spells.spells import *
from ....variables.event_palette_names import *

script = EventScript([
	DisableObjectTrigger(MEM_70A8),
	# decide get-sound first: key items -> key queue, else fall through to normal
	JmpIfVarEqualsConst(ITEM_ID, TempleKeyItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, RareFrogCoinItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, WalletItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, CricketPieItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, CricketJamItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, CastleKey1Item, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, CastleKey2Item, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, BambinoBombItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, AltoCardItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, TenorCardItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, SopranoCardItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, ExtraShinyStoneItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, CrystalShardItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, RoomKeyItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, ShedKeyItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, ElderKeyItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, SeedItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, FertilizerItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, DryBonesFlagItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, GreaperFlagItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, BigBooFlagItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, FireworksItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, ShinyStoneItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, CarboCookieItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, BrightCardItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, ShoesItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, BroochItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, RingItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, CrownItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, GoldPaintItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, CookiesItem, ["EVENT_4077L_165_key_queue"]),
	JmpIfVarEqualsConst(ITEM_ID, MarioDollItem, ["EVENT_4077L_165_key_queue"]),
	# normal get-sound: hide sprite + flower jingle + set presence (runs concurrently)
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_VisibilityOff(),
		A_PlaySound(sound=SO014_FLOWER, channel=6),
	]),
	Jmp(["EVENT_4077L_165_after_queue"]),
	# key-item get-sound
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_VisibilityOff(),
		A_PlaySound(sound=SO085_FLOWER, channel=6),
	], identifier="EVENT_4077L_165_key_queue"),
	# article selection (get-sound already chosen + playing)
	JmpIfVarEqualsConst(ITEM_ID, CymbalsItem, ["EVENT_4077L_165_no_article"], identifier="EVENT_4077L_165_after_queue"),
	JmpIfVarEqualsConst(ITEM_ID, HurlyGlovesItem, ["EVENT_4077L_165_no_article"]),
	JmpIfVarEqualsConst(ITEM_ID, PantsItem, ["EVENT_4077L_165_no_article"]),
	JmpIfVarEqualsConst(ITEM_ID, ThickPantsItem, ["EVENT_4077L_165_no_article"]),
	JmpIfVarEqualsConst(ITEM_ID, MegaPantsItem, ["EVENT_4077L_165_no_article"]),
	JmpIfVarEqualsConst(ITEM_ID, WorkPantsItem, ["EVENT_4077L_165_no_article"]),
	JmpIfVarEqualsConst(ITEM_ID, HappyPantsItem, ["EVENT_4077L_165_no_article"]),
	JmpIfVarEqualsConst(ITEM_ID, SailorPantsItem, ["EVENT_4077L_165_no_article"]),
	JmpIfVarEqualsConst(ITEM_ID, FuzzyPantsItem, ["EVENT_4077L_165_no_article"]),
	JmpIfVarEqualsConst(ITEM_ID, FirePantsItem, ["EVENT_4077L_165_no_article"]),
	JmpIfVarEqualsConst(ITEM_ID, PrincePantsItem, ["EVENT_4077L_165_no_article"]),
	JmpIfVarEqualsConst(ITEM_ID, ZoomShoesItem, ["EVENT_4077L_165_no_article"]),
	JmpIfVarEqualsConst(ITEM_ID, JumpShoesItem, ["EVENT_4077L_165_no_article"]),
	JmpIfVarEqualsConst(ITEM_ID, TempleKeyItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, RareFrogCoinItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, WalletItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, CricketPieItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, CricketJamItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, CastleKey1Item, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, CastleKey2Item, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, BambinoBombItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, AltoCardItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, TenorCardItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, SopranoCardItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, ExtraShinyStoneItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, CrystalShardItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, RoomKeyItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, ShedKeyItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, ElderKeyItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, SeedItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, FertilizerItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, DryBonesFlagItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, GreaperFlagItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, BigBooFlagItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, FireworksItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, ShinyStoneItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, CarboCookieItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, BrightCardItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, ShoesItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, BroochItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, RingItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, CrownItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, GoldPaintItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, CookiesItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, MarioDollItem, ["EVENT_4077L_165_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, UltraHammerItem, ["EVENT_4077L_165_run_dialog_17"]),
	JmpIfVarEqualsConst(ITEM_ID, AmuletItem, ["EVENT_4077L_165_run_dialog_17"], identifier="EVENT_4077L_165_delete_vowel_1"),
	JmpIfVarEqualsConst(ITEM_ID, AttackScarfItem, ["EVENT_4077L_165_run_dialog_17"]),
	JmpIfVarEqualsConst(ITEM_ID, ExpBoosterItem, ["EVENT_4077L_165_run_dialog_17"]),
	JmpIfVarEqualsConst(ITEM_ID, AntidotePinItem, ["EVENT_4077L_165_run_dialog_17"]),
	JmpIfVarEqualsConst(ITEM_ID, AbleJuiceItem, ["EVENT_4077L_165_run_dialog_17"], identifier="EVENT_4077L_165_delete_vowel_2"),
	JmpIfVarEqualsConst(ITEM_ID, EnergizerItem, ["EVENT_4077L_165_run_dialog_17"]),
	JmpIfVarEqualsConst(ITEM_ID, IceBombItem, ["EVENT_4077L_165_run_dialog_17"]),
	JmpIfVarEqualsConst(ITEM_ID, ElixirItem, ["EVENT_4077L_165_run_dialog_17"], identifier="EVENT_4077L_165_delete_vowel_3"),
	JmpIfVarEqualsConst(ITEM_ID, EarlierTimesItem, ["EVENT_4077L_165_run_dialog_17"]),
	JmpIfVarEqualsConst(ITEM_ID, EnduringBroochItem, ["EVENT_4077L_165_run_dialog_17"]),
	JmpIfVarEqualsConst(ITEM_ID, LambsLureItem, ["EVENT_4077L_165_lambs_lure"]),
	JmpIfVarEqualsConst(ITEM_ID, BtubRingItem, ["EVENT_4077L_165_btub_ring"]),
	JmpIfVarEqualsConst(ITEM_ID, YoshiAdeItem, ["EVENT_4077L_165_yoshi_ade"]),
	# default 'a' article
	RunDialog(dialog_id=DI1177_FOUND_A_70A7_AUTO_TERMINATE, above_object=MARIO, closable=False, sync=True, multiline=False, use_background=False, bit_6=True),
	AddToInventory(ITEM_ID),
	Return(),
	# 'an' vowel article
	RunDialog(dialog_id=DI1178_FOUND_AN_70A7_AUTO_TERMINATE, above_object=MARIO, closable=False, sync=True, multiline=False, use_background=False, bit_6=True, identifier="EVENT_4077L_165_run_dialog_17"),
	AddToInventory(ITEM_ID),
	Return(),
	# no-article (plural) items
	RunDialog(dialog_id=DI2016_FOUND_70A7_AUTO_TERMINATE, above_object=MARIO, closable=False, sync=True, multiline=False, use_background=False, bit_6=True, identifier="EVENT_4077L_165_no_article"),
	AddToInventory(ITEM_ID),
	Return(),
	# 'the' (key items)
	RunDialog(dialog_id=DI2019_FOUND_THE_70A7_AUTO_TERMINATE, above_object=MARIO, closable=False, sync=True, multiline=False, use_background=False, bit_6=True, identifier="EVENT_4077L_165_the_article"),
	AddToInventory(ITEM_ID),
	Return(),
	# lambs lure
	RunDialog(dialog_id=DI2006_FOUND_A_LAMBS_LURE_AUTO_TERMINATE, above_object=MARIO, closable=False, sync=True, multiline=False, use_background=False, bit_6=True, identifier="EVENT_4077L_165_lambs_lure"),
	AddToInventory(ITEM_ID),
	Return(),
	# btub ring
	RunDialog(dialog_id=DI2007_FOUND_A_BTUB_RING_AUTO_TERMINATE, above_object=MARIO, closable=False, sync=True, multiline=False, use_background=False, bit_6=True, identifier="EVENT_4077L_165_btub_ring"),
	AddToInventory(ITEM_ID),
	Return(),
	# yoshi ade (sound already fired up top)
	RunDialog(dialog_id=DI2013_GOT_A_YOSHI_ADE_AUTO_TERMINATE, above_object=MARIO, closable=False, sync=True, multiline=False, use_background=False, identifier="EVENT_4077L_165_yoshi_ade"),
	AddToInventory(ITEM_ID),
	Return(),
])