# E0215_HILL_ITEM
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
    JmpIfVarEqualsConst(ITEM_ID, CymbalsItem, ["EVENT_215_no_article"]),
    JmpIfVarEqualsConst(ITEM_ID, HurlyGlovesItem, ["EVENT_215_no_article"]),
    JmpIfVarEqualsConst(ITEM_ID, PantsItem, ["EVENT_215_no_article"]),
    JmpIfVarEqualsConst(ITEM_ID, ThickPantsItem, ["EVENT_215_no_article"]),
    JmpIfVarEqualsConst(ITEM_ID, MegaPantsItem, ["EVENT_215_no_article"]),
    JmpIfVarEqualsConst(ITEM_ID, WorkPantsItem, ["EVENT_215_no_article"]),
    JmpIfVarEqualsConst(ITEM_ID, HappyPantsItem, ["EVENT_215_no_article"]),
    JmpIfVarEqualsConst(ITEM_ID, SailorPantsItem, ["EVENT_215_no_article"]),
    JmpIfVarEqualsConst(ITEM_ID, FuzzyPantsItem, ["EVENT_215_no_article"]),
    JmpIfVarEqualsConst(ITEM_ID, FirePantsItem, ["EVENT_215_no_article"]),
    JmpIfVarEqualsConst(ITEM_ID, PrincePantsItem, ["EVENT_215_no_article"]),
    JmpIfVarEqualsConst(ITEM_ID, ZoomShoesItem, ["EVENT_215_no_article"]),
    JmpIfVarEqualsConst(ITEM_ID, JumpShoesItem, ["EVENT_215_no_article"]),
    JmpIfVarEqualsConst(ITEM_ID, TempleKeyItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, RareFrogCoinItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, WalletItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, CricketPieItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, CricketJamItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, CastleKey1Item, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, CastleKey2Item, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, BambinoBombItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, AltoCardItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, TenorCardItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, SopranoCardItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, ExtraShinyStoneItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, CrystalShardItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, RoomKeyItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, ShedKeyItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, ElderKeyItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, SeedItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, FertilizerItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, DryBonesFlagItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, GreaperFlagItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, BigBooFlagItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, FireworksItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, ShinyStoneItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, CarboCookieItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, BrightCardItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, ShoesItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, BroochItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, RingItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, CrownItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, GoldPaintItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, CookiesItem, ["EVENT_215_the_article"]),
    JmpIfVarEqualsConst(ITEM_ID, MarioDollItem, ["EVENT_215_the_article"]),
	JmpIfVarEqualsConst(ITEM_ID, UltraHammerItem, ["EVENT_215_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, AmuletItem, ["EVENT_215_run_dialog_16"], identifier="EVENT_215_delete_vowel_1"),
	JmpIfVarEqualsConst(ITEM_ID, AttackScarfItem, ["EVENT_215_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, ExpBoosterItem, ["EVENT_215_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, AntidotePinItem, ["EVENT_215_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, AbleJuiceItem, ["EVENT_215_run_dialog_16"], identifier="EVENT_215_delete_vowel_2"),
	JmpIfVarEqualsConst(ITEM_ID, EnergizerItem, ["EVENT_215_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, IceBombItem, ["EVENT_215_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, ElixirItem, ["EVENT_215_run_dialog_16"], identifier="EVENT_215_delete_vowel_3"),
	JmpIfVarEqualsConst(ITEM_ID, EarlierTimesItem, ["EVENT_215_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, EnduringBroochItem, ["EVENT_215_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, LambsLureItem, ["EVENT_215_lambs_lure"]),
	JmpIfVarEqualsConst(ITEM_ID, BtubRingItem, ["EVENT_215_btub_ring"]),
	JmpIfVarEqualsConst(ITEM_ID, YoshiAdeItem, ["EVENT_215_yoshi_ade"]),
	RunDialog(dialog_id=DI0536_BOOSTER_HILL_ITEM, above_object=BOWSER, closable=False, sync=True, multiline=False, use_background=False, bit_6=True),
	AddToInventory(ITEM_ID),
	Jmp(["hill_choose_SOUND"]),
	RunDialog(dialog_id=DI0535_BOOSTER_HILL_ITEM_VOWEL, above_object=BOWSER, closable=False, sync=True, multiline=False, use_background=False, bit_6=True, identifier="EVENT_215_run_dialog_16"),
	AddToInventory(ITEM_ID),
    JmpIfVarEqualsConst(ITEM_ID, TempleKeyItem, ["hill_key_item_sound"], identifier="hill_choose_SOUND"),
    JmpIfVarEqualsConst(ITEM_ID, RareFrogCoinItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, WalletItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CricketPieItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CastleKey1Item, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CastleKey2Item, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BambinoBombItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, AltoCardItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, TenorCardItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, SopranoCardItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ExtraShinyStoneItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CrystalShardItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, RoomKeyItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ShedKeyItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ElderKeyItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, SeedItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, FertilizerItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, DryBonesFlagItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, GreaperFlagItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BigBooFlagItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, FireworksItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ShinyStoneItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CarboCookieItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BrightCardItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ShoesItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BroochItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, RingItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CrownItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, GoldPaintItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CookiesItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, MarioDollItem, ["hill_key_item_sound"]),
	PlaySound(sound=SO014_FLOWER, channel=6),
	Return(),
    PlaySound(sound=SO085_FLOWER, channel=6, identifier="hill_key_item_sound"),
	Return(),
	RunDialog(dialog_id=DI2020_HILL_GOT_70A7_AUTO_TERMINATE, above_object=BOWSER, closable=False, sync=True, multiline=False, use_background=False, bit_6=True, identifier="EVENT_215_no_article"),
	AddToInventory(ITEM_ID),
	Jmp(["hill_choose_SOUND"]),
	RunDialog(dialog_id=DI2021_HILL_GOT_THE_70A7_AUTO_TERMINATE, above_object=BOWSER, closable=False, sync=True, multiline=False, use_background=False, bit_6=True, identifier="EVENT_215_the_article"),
	AddToInventory(ITEM_ID),
	Jmp(["hill_choose_SOUND"]),
	RunDialog(dialog_id=DI2006_FOUND_A_LAMBS_LURE_AUTO_TERMINATE, above_object=BOWSER, closable=False, sync=True, multiline=False, use_background=False, bit_6=True, identifier="EVENT_215_lambs_lure"),
	AddToInventory(ITEM_ID),
	Jmp(["hill_choose_SOUND"]),
	RunDialog(dialog_id=DI2007_FOUND_A_BTUB_RING_AUTO_TERMINATE, above_object=BOWSER, closable=False, sync=True, multiline=False, use_background=False, bit_6=True, identifier="EVENT_215_btub_ring"),
	AddToInventory(ITEM_ID),
	Jmp(["hill_choose_SOUND"]),
	RunDialog(dialog_id=DI2013_GOT_A_YOSHI_ADE_AUTO_TERMINATE, above_object=BOWSER, closable=False, sync=True, multiline=False, use_background=False, bit_6=True, identifier="EVENT_215_yoshi_ade"),
	AddToInventory(ITEM_ID),
	Jmp(["hill_choose_SOUND"]),
])
