from .types.prize import Prize, StandardPrize, CoinPrize, SlotsPrize, BossFightPrize, CharacterPrize, StarPiecePrize, ItemPrize, SpellPrize, TreasureHunterNickname, ProgressiveItemPrize, WeddingGearPrize, SpecialItemPrizeType
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import AddToInventory, JmpIfVarEqualsConst, RemoveOneOfItemFromInventory, Return, SetVarToConst, StoreItemAmountTo7000, ApplySolidityModToLevel, RemoveObjectFromSpecificLevel, JmpToEvent
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import NPC_2
from ..data.items.items import (
    HammerItem, FroggieStickItem, NokNokShellItem, PunchGloveItem,
    FingerShotItem, CymbalsItem, ChompItem, MasherItem, ChompShellItem,
    SuperHammerItem, HandGunItem, WhompGloveItem, SlapGloveItem,
    TroopaShellItem, ParasolItem, HurlyGlovesItem, DoublePunchItem,
    RibbitStickItem, SpikedLinkItem, MegaGloveItem, WarFanItem,
    HandCannonItem, StickyGloveItem, UltraHammerItem, SuperSlapItem,
    DrillClawItem, StarGunItem, SonicCymbalItem, LazyShellItem,
    FryingPanItem, LuckyHammerItem, ShirtItem, PantsItem, ThickShirtItem,
    ThickPantsItem, MegaShirtItem, MegaPantsItem, WorkPantsItem,
    MegaCapeItem, HappyShirtItem, HappyPantsItem, HappyCapeItem,
    HappyShellItem, PolkaDressItem, SailorShirtItem, SailorPantsItem,
    SailorCapeItem, NauticaDressItem, CourageShellItem, FuzzyShirtItem,
    FuzzyPantsItem, FuzzyCapeItem, FuzzyDressItem, FireShirtItem,
    FirePantsItem, FireCapeItem, FireShellItem, FireDressItem,
    HeroShirtItem, PrincePantsItem, StarCapeItem, HealShellItem,
    RoyalDressItem, SuperSuitItem, ZoomShoesItem, SafetyBadgeItem,
    JumpShoesItem, SafetyRingItem, AmuletItem, ScroogeRingItem,
    ExpBoosterItem, AttackScarfItem, RareScarfItem, BtubRingItem,
    AntidotePinItem, WakeUpPinItem, FearlessPinItem, TrueformPinItem,
    CoinTrickItem, GhostMedalItem, JinxBeltItem, FeatherItem,
    TroopaPinItem, SignalRingItem, QuartzCharmItem, MushroomItem,
    MidMushroomItem, MaxMushroomItem, HoneySyrupItem, MapleSyrupItem,
    RoyalSyrupItem, PickMeUpItem, AbleJuiceItem, BracerItem,
    EnergizerItem, YoshiAdeItem, RedEssenceItem, KerokeroColaItem,
    YoshiCookieItem, PureWaterItem, SleepyBombItem, BadMushroomItem,
    FireBombItem, IceBombItem, FlowerTabItem, FlowerJarItem,
    FlowerBoxItem, YoshiCandyItem, FroggieDrinkItem, MukuCookieItem,
    ElixirItem, MegalixirItem, SeeYaItem, TempleKeyItem, GoodieBagItem,
    EarlierTimesItem, FreshenUpItem, RareFrogCoinItem, WalletItem,
    CricketPieItem, RockCandyItem, CastleKey1Item, 
    CastleKey2Item, BambinoBombItem,
    RoomKeyItem, ElderKeyItem, ShedKeyItem,
    FrightBombItem, BeetleBoxItem,
    LuckyJewelItem, 
    CrystallineItem, PowerBlastItem, WiltShroomItem, RottenMushItem,
    MoldyMushItem, SeedItem, FertilizerItem,
    BigBooFlagItem, DryBonesFlagItem, GreaperFlagItem, CricketJamItem, FireworksItem,
    BrightCardItem, StarEggItem, ShoesItem, BroochItem, RingItem, CrownItem,
    LazyShellItem2, MushroomItem2, WonderChompItem, Stella023Item, SageStickItem,
    TeamworkBandItem, EnduringBroochItem
)
from ..data.variables.variable_names import *
from ..data.variables.room_names import *
from ..data.variables.event_script_names import *

### Real items ###

class HammerPrize(ItemPrize):
    item = HammerItem
    _nickname = TreasureHunterNickname(
        nickname="Hammer",
        description="I'm not sure if it does anything\n else."
    )


class FroggiestickPrize(ItemPrize):
    item = FroggieStickItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_2
    _nickname = TreasureHunterNickname(
        nickname="Caster's Staff",
        description="It looks pretty good at bonking."
    )


class NokNokShellPrize(ItemPrize):
    item = NokNokShellItem
    _nickname = TreasureHunterNickname(
        nickname="Green Shell",
        description="There's no turtle inside of it."
    )


class PunchGlovePrize(ItemPrize):
    item = PunchGloveItem
    _nickname = TreasureHunterNickname(
        nickname="Glove",
        description="You don't drink water out of it."
    )


class FingerShotPrize(ItemPrize):
    item = FingerShotItem
    _nickname = TreasureHunterNickname(
        nickname="Pellet Shooter",
        description="It was probably owned by a kid."
    )


class CymbalsPrize(ItemPrize):
    item = CymbalsItem
    _nickname = TreasureHunterNickname(
        nickname="Percussion Plate",
        description="I bet it could get pretty loud."
    )


class ChompPrize(ItemPrize):
    item = ChompItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_2
    _nickname = TreasureHunterNickname(
        nickname="Chain Chomp",
        description="It's hungry to stir up some trouble."
    )


class MasherPrize(ItemPrize):
    item = MasherItem
    _nickname = TreasureHunterNickname(
        nickname="Hammer",
        description="I'm not sure if it does anything\n else."
    )


class ChompShellPrize(ItemPrize):
    item = ChompShellItem
    _nickname = TreasureHunterNickname(
        nickname="Chomp Exoskeleton",
        description="I didn't even know those things\n could shed their skin."
    )


class SuperHammerPrize(ItemPrize):
    item = SuperHammerItem
    _nickname = TreasureHunterNickname(
        nickname="Hammer",
        description="I'm not sure if it does anything\n else."
    )


class HandGunPrize(ItemPrize):
    item = HandGunItem
    _nickname = TreasureHunterNickname(
        nickname="BB Gun",
        description="I'll throw in some ammo, too."
    )


class WhompGlovePrize(ItemPrize):
    item = WhompGloveItem
    _nickname = TreasureHunterNickname(
        nickname="Glove",
        description="You don't drink water out of it."
    )


class SlapGlovePrize(ItemPrize):
    item = SlapGloveItem
    _nickname = TreasureHunterNickname(
        nickname="Glove",
        description="You don't drink water out of it."
    )


class TroopaShellPrize(ItemPrize):
    item = TroopaShellItem
    _nickname = TreasureHunterNickname(
        nickname="Red Shell",
        description="There's no turtle inside of it."
    )


class ParasolPrize(ItemPrize):
    item = ParasolItem
    _nickname = TreasureHunterNickname(
        nickname="Umbrella",
        description="There's no turtle inside of it."
    )


class HurlyGlovesPrize(ItemPrize):
    item = HurlyGlovesItem
    _nickname = TreasureHunterNickname(
        nickname="Glove",
        description="You don't drink water out of it."
    )


class DoublePunchPrize(ItemPrize):
    item = DoublePunchItem
    _nickname = TreasureHunterNickname(
        nickname="Rocket Launcher",
        description="Be careful, it could take your\n hands clean off."
    )


class RibbitStickPrize(ItemPrize):
    item = RibbitStickItem
    _nickname = TreasureHunterNickname(
        nickname="Caster's Staff",
        description="It looks pretty good at bonking."
    )


class SpikedLinkPrize(ItemPrize):
    item = SpikedLinkItem
    _nickname = TreasureHunterNickname(
        nickname="Chain Chomp",
        description="This one's got thorns on it."
    )


class MegaGlovePrize(ItemPrize):
    item = MegaGloveItem
    _nickname = TreasureHunterNickname(
        nickname="Glove",
        description="You don't drink water out of it."
    )


class WarFanPrize(ItemPrize):
    item = WarFanItem
    _nickname = TreasureHunterNickname(
        nickname="Spiked Fan",
        description="Pretty, but deadly!"
    )


class HandCannonPrize(ItemPrize):
    item = HandCannonItem
    _nickname = TreasureHunterNickname(
        nickname="Cannon Launcher",
        description="You need strong elbows for this!"
    )


class StickyGlovePrize(ItemPrize):
    item = StickyGloveItem
    _nickname = TreasureHunterNickname(
        nickname="Glove",
        description="You don't drink water out of it."
    )


class UltraHammerPrize(ItemPrize):
    item = UltraHammerItem
    _nickname = TreasureHunterNickname(
        nickname="Hammer",
        description="I'm not sure if it does anything\n else."
    )


class SuperSlapPrize(ItemPrize):
    item = SuperSlapItem
    _nickname = TreasureHunterNickname(
        nickname="Glove",
        description="You don't drink water out of it."
    )


class DrillClawPrize(ItemPrize):
    item = DrillClawItem
    _nickname = TreasureHunterNickname(
        nickname="Drilling Appendage",
        description="I bet you could do some real damage\n with this."
    )


class StarGunPrize(ItemPrize):
    item = StarGunItem
    _nickname = TreasureHunterNickname(
        nickname="Celestial Launcher",
        description="I bet you could do some real damage\n with this."
    )


class SonicCymbalPrize(ItemPrize):
    item = SonicCymbalItem
    _nickname = TreasureHunterNickname(
        nickname="Psych Percussion",
        description="This could catch monsters\n off-guard."
    )


class LazyShellWeaponPrize(ItemPrize):
    item = LazyShellItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_2
    _nickname = TreasureHunterNickname(
        nickname="Red Shell",
        description="There's no turtle inside of it."
    )


class FryingPanPrize(ItemPrize):
    item = FryingPanItem
    _nickname = TreasureHunterNickname(
        nickname="Metal Plate",
        description="Don't know what it’s used for."
    )


class WonderChompPrize(ItemPrize):
    item = WonderChompItem
    _nickname = TreasureHunterNickname(
        nickname="Golden Chomp",
        description="It's hungry to stir up some BIG\n trouble."
    )
    remake_only = True


class Stella023Prize(ItemPrize):
    item = Stella023Item
    _nickname = TreasureHunterNickname(
        nickname="Cool Gun",
        description="Why does it remind me of a train?"
    )
    remake_only = True


class SageStickPrize(ItemPrize):
    item = SageStickItem
    _nickname = TreasureHunterNickname(
        nickname="Caster's Staff",
        description="It looks pretty good at bonking."
    )
    remake_only = True


class LuckyHammerPrize(ItemPrize):
    item = LuckyHammerItem
    _nickname = TreasureHunterNickname(
        nickname="Hammer",
        description="I'm not sure if it does anything\n else."
    )


class ShirtPrize(ItemPrize):
    item = ShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Overalls",
        description="Don't go to work without 'em!"
    )


class PantsPrize(ItemPrize):
    item = PantsItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Pants",
        description="They're comfy and easy to wear."
    )


class ThickShirtPrize(ItemPrize):
    item = ThickShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Blue/Red Overalls",
        description="They look pretty sturdy."
    )


class ThickPantsPrize(ItemPrize):
    item = ThickPantsItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Pants",
        description="They're comfy and easy to wear."
    )


class MegaShirtPrize(ItemPrize):
    item = MegaShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Orange Overalls",
        description="You're sure to stand out in these!"
    )


class MegaPantsPrize(ItemPrize):
    item = MegaPantsItem
    _nickname = TreasureHunterNickname(
        nickname="Striped Red Pants",
        description="Made from only the finest threads\n in Mysidia."
    )



class WorkPantsPrize(ItemPrize):
    item = WorkPantsItem
    _nickname = TreasureHunterNickname(
        nickname="Stained Pants",
        description="They look a bit worn out."
    )


class MegaCapePrize(ItemPrize):
    item = MegaCapeItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Cape",
        description="It looks pretty cool, right?"
    )


class HappyShirtPrize(ItemPrize):
    item = HappyShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Orange Overalls",
        description="You're sure to stand out in these!"
    )


class HappyPantsPrize(ItemPrize):
    item = HappyPantsItem
    _nickname = TreasureHunterNickname(
        nickname="Pink Pants",
        description="They're all the rage these days!"
    )


class HappyCapePrize(ItemPrize):
    item = HappyCapeItem
    _nickname = TreasureHunterNickname(
        nickname="Rainbow Cape",
        description="I'd be proud to wear this!"
    )


class HappyShellPrize(ItemPrize):
    item = HappyShellItem
    _nickname = TreasureHunterNickname(
        nickname="Green Shell",
        description="There's no turtle inside of it."
    )


class PolkaDressPrize(ItemPrize):
    item = PolkaDressItem
    _nickname = TreasureHunterNickname(
        nickname="Pink Dress",
        description="For serious fashionistas."
    )


class SailorShirtPrize(ItemPrize):
    item = SailorShirtItem
    _nickname = TreasureHunterNickname(
        nickname="White Overalls",
        description="Built for life on the sea."
    )


class SailorPantsPrize(ItemPrize):
    item = SailorPantsItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Pants",
        description="They're comfy and easy to wear."
    )


class SailorCapePrize(ItemPrize):
    item = SailorCapeItem
    _nickname = TreasureHunterNickname(
        nickname="White Cape",
        description="Built for life on the sea."
    )


class NauticaDressPrize(ItemPrize):
    item = NauticaDressItem
    _nickname = TreasureHunterNickname(
        nickname="School Uniform",
        description="The neckerchief is included."
    )


class CourageShellPrize(ItemPrize):
    item = CourageShellItem
    _nickname = TreasureHunterNickname(
        nickname="Green Shell",
        description="There's no turtle inside of it."
    )


class FuzzyShirtPrize(ItemPrize):
    item = FuzzyShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Green Overalls",
        description="Made of the finest fleece."
    )


class FuzzyPantsPrize(ItemPrize):
    item = FuzzyPantsItem
    _nickname = TreasureHunterNickname(
        nickname="Striped Red Pants",
        description="Made from only the finest threads\n in Mysidia."
    )


class FuzzyCapePrize(ItemPrize):
    item = FuzzyCapeItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Cape",
        description="Made of the finest fleece."
    )


class FuzzyDressPrize(ItemPrize):
    item = FuzzyDressItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Dress",
        description="Made of the finest fleece."
    )


class FireShirtPrize(ItemPrize):
    item = FireShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Orange Overalls",
        description="You're sure to stand out in these!"
    )


class FirePantsPrize(ItemPrize):
    item = FirePantsItem
    _nickname = TreasureHunterNickname(
        nickname="Red Pants",
        description="Stylish AND warm!"
    )


class FireCapePrize(ItemPrize):
    item = FireCapeItem
    _nickname = TreasureHunterNickname(
        nickname="Orange Cape",
        description="The pattern on it is pretty cool."
    )


class FireShellPrize(ItemPrize):
    item = FireShellItem
    _nickname = TreasureHunterNickname(
        nickname="Red Shell",
        description="There's no turtle inside of it."
    )


class FireDressPrize(ItemPrize):
    item = FireDressItem
    _nickname = TreasureHunterNickname(
        nickname="Red Dress",
        description="The pattern on it is pretty cool."
    )


class HeroShirtPrize(ItemPrize):
    item = HeroShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Blue/Red Overalls",
        description="They look pretty sturdy."
    )


class PrincePantsPrize(ItemPrize):
    item = PrincePantsItem
    _nickname = TreasureHunterNickname(
        nickname="Flash Pants",
        description="You'll look like a superhero in\n these!"
    )


class StarCapePrize(ItemPrize):
    item = StarCapeItem
    _nickname = TreasureHunterNickname(
        nickname="Freedom Cape",
        description="It's red, white, and blue."
    )


class HealShellPrize(ItemPrize):
    item = HealShellItem
    _nickname = TreasureHunterNickname(
        nickname="Green Shell",
        description="There's no turtle inside of it."
    )


class RoyalDressPrize(ItemPrize):
    item = RoyalDressItem
    _nickname = TreasureHunterNickname(
        nickname="Fancy Dress",
        description="Check out the gold trim!"
    )


class SuperSuitPrize(ItemPrize):
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_1
    item = SuperSuitItem
    _nickname = TreasureHunterNickname(
        nickname="Jumpsuit",
        description="It looks pretty powerful, right?"
    )


class LazyShellArmorPrize(ItemPrize):
    item = LazyShellItem2
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_2
    _nickname = TreasureHunterNickname(
        nickname="Red Shell",
        description="There's no turtle inside of it."
    )


class ZoomShoesPrize(ItemPrize):
    item = ZoomShoesItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_2
    _nickname = TreasureHunterNickname(
        nickname="Red Vans",
        description="I bet you can run really fast in\n these."
    )


class SafetyBadgePrize(ItemPrize):
    item = SafetyBadgeItem
    _nickname = TreasureHunterNickname(
        nickname="Rainbow Button",
        description="I don't really follow politics, but\n this button looks like it's against\n a lot of things."
    )


class JumpShoesPrize(ItemPrize):
    item = JumpShoesItem
    _nickname = TreasureHunterNickname(
        nickname="Brown Clogs",
        description="Check out the thick soles!"
    )


class SafetyRingPrize(ItemPrize):
    item = SafetyRingItem
    _nickname = TreasureHunterNickname(
        nickname="Protective Charm",
        description="Never go into battle without it."
    )


class AmuletPrize(ItemPrize):
    item = AmuletItem
    _nickname = TreasureHunterNickname(
        nickname="Stinky Charm",
        description="It'll help you weather the elements."
    )


class ScroogeRingPrize(ItemPrize):
    item = ScroogeRingItem
    _nickname = TreasureHunterNickname(
        nickname="Mage Totem",
        description="It might help with spellcasting."
    )


class ExpBoosterPrize(ItemPrize):
    item = ExpBoosterItem
    _nickname = TreasureHunterNickname(
        nickname="Training Device",
        description="This'll make you strong in no time!"
    )


class AttackScarfPrize(ItemPrize):
    item = AttackScarfItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_1
    _nickname = TreasureHunterNickname(
        nickname="Starry Scarf",
        description="It could save your life!"
    )


class RareScarfPrize(ItemPrize):
    item = RareScarfItem
    _nickname = TreasureHunterNickname(
        nickname="White Cloth",
        description="You don't see these around often."
    )


class BtubRingPrize(ItemPrize):
    item = BtubRingItem
    _nickname = TreasureHunterNickname(
        nickname="Wedding Ring",
        description="For that special someone!"
    )


class AntidotePinPrize(ItemPrize):
    item = AntidotePinItem
    _nickname = TreasureHunterNickname(
        nickname="Green Button",
        description="Looks like an environmentalist\n thing."
    )


class WakeUpPinPrize(ItemPrize):
    item = WakeUpPinItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Button",
        description="Looks like an anti-fur thing."
    )


class FearlessPinPrize(ItemPrize):
    item = FearlessPinItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Button",
        description="Who you gonna call?\n GHOSTBUSTERS!"
    )


class TrueformPinPrize(ItemPrize):
    item = TrueformPinItem
    _nickname = TreasureHunterNickname(
        nickname="Orange Button",
        description="For someone who doesn't like\n scarecrows."
    )


class CoinTrickPrize(ItemPrize):
    item = CoinTrickItem
    _nickname = TreasureHunterNickname(
        nickname="Fortune Charm",
        description="It's sure to make you very rich."
    )


class GhostMedalPrize(ItemPrize):
    item = GhostMedalItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_1
    _nickname = TreasureHunterNickname(
        nickname="Military Decoration",
        description="I wonder what powers it bestows?"
    )


class JinxBeltPrize(ItemPrize):
    item = JinxBeltItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_1
    _nickname = TreasureHunterNickname(
        nickname="Black Sash",
        description="A true fighter would love this."
    )


class FeatherPrize(ItemPrize):
    item = FeatherItem
    _nickname = TreasureHunterNickname(
        nickname="Fluttering Quill",
        description="It's pretty exotic, isn't it?"
    )


class TroopaPinPrize(ItemPrize):
    item = TroopaPinItem
    _nickname = TreasureHunterNickname(
        nickname="Military Decoration",
        description="I wonder what powers it bestows?"
    )


class SignalRingPrize(ItemPrize):
    item = SignalRingItem
    _nickname = TreasureHunterNickname(
        nickname="Bell Charm",
        description="I wonder what it can help you find?"
    )


class QuartzCharmPrize(ItemPrize):
    item = QuartzCharmItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_1
    _nickname = TreasureHunterNickname(
        nickname="Crystal",
        description="It might have special powers.\n Or it might not."
    )


class TeamworkBandPrize(ItemPrize):
    item = TeamworkBandItem
    _nickname = TreasureHunterNickname(
        nickname="Friendship Bracelet",
        description="Maybe the real treasure is the\n friends we made along the way."
    )
    remake_only = True

class EnduringBroochPrize(ItemPrize):
    item = EnduringBroochItem
    _nickname = TreasureHunterNickname(
        nickname="Shiny Brooch",
        description="It looks pretty stylish."
    )
    remake_only = True

class MushroomPrize(ItemPrize):
    item = MushroomItem
    _nickname = TreasureHunterNickname(
        nickname="Red Mushroom",
        description="It's just food, right?"
    )


class MidMushroomPrize(ItemPrize):
    item = MidMushroomItem
    _nickname = TreasureHunterNickname(
        nickname="Green Mushroom",
        description="It's just food, right?"
    )


class MaxMushroomPrize(ItemPrize):
    item = MaxMushroomItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Mushroom",
        description="It's just food, right?"
    )


class HoneySyrupPrize(ItemPrize):
    item = HoneySyrupItem
    _nickname = TreasureHunterNickname(
        nickname="Red Drink",
        description="I wonder what flavor it is?"
    )


class MapleSyrupPrize(ItemPrize):
    item = MapleSyrupItem
    _nickname = TreasureHunterNickname(
        nickname="Green Drink",
        description="I wonder what flavor it is?"
    )


class RoyalSyrupPrize(ItemPrize):
    item = RoyalSyrupItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Drink",
        description="I wonder what flavor it is?"
    )


class PickMeUpPrize(ItemPrize):
    item = PickMeUpItem
    _nickname = TreasureHunterNickname(
        nickname="Red Drink",
        description="I wonder what flavor it is?"
    )


class AbleJuicePrize(ItemPrize):
    item = AbleJuiceItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Drink",
        description="I wonder what flavor it is?"
    )


class BracerPrize(ItemPrize):
    item = BracerItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Drink",
        description="I wonder what flavor it is?"
    )


class EnergizerPrize(ItemPrize):
    item = EnergizerItem
    _nickname = TreasureHunterNickname(
        nickname="Green Drink",
        description="I wonder what flavor it is?"
    )


class YoshiAdePrize(ItemPrize):
    item = YoshiAdeItem
    _nickname = TreasureHunterNickname(
        nickname="Green Drink",
        description="I wonder what flavor it is?"
    )


class RedEssencePrize(ItemPrize):
    item = RedEssenceItem
    _nickname = TreasureHunterNickname(
        nickname="Red Drink",
        description="I wonder what flavor it is?"
    )


class KerokeroColaPrize(ItemPrize):
    item = KerokeroColaItem
    _nickname = TreasureHunterNickname(
        nickname="Green Drink",
        description="I wonder what flavor it is?"
    )


class YoshiCookiePrize(ItemPrize):
    item = YoshiCookieItem
    _nickname = TreasureHunterNickname(
        nickname="Baked Good",
        description="Looks tasty, doesn't it?"
    )


class PureWaterPrize(ItemPrize):
    item = PureWaterItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Drink",
        description="I wonder what flavor it is?"
    )


class SleepyBombPrize(ItemPrize):
    item = SleepyBombItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device",
        description="Don't try this at home!"
    )


class BadMushroomPrize(ItemPrize):
    item = BadMushroomItem
    _nickname = TreasureHunterNickname(
        nickname="Red Mushroom",
        description="It's just food, right?"
    )


class FireBombPrize(ItemPrize):
    item = FireBombItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device",
        description="Don't try this at home!"
    )


class IceBombPrize(ItemPrize):
    item = IceBombItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device",
        description="Don't try this at home!"
    )


class FlowerTabPrize(ItemPrize):
    item = FlowerTabItem
    _nickname = TreasureHunterNickname(
        nickname="Flower Capsule",
        description="You collect these, right?"
    )


class FlowerJarPrize(ItemPrize):
    item = FlowerJarItem
    _nickname = TreasureHunterNickname(
        nickname="Flower Set",
        description="You collect these, right?"
    )


class FlowerBoxPrize(ItemPrize):
    item = FlowerBoxItem
    _nickname = TreasureHunterNickname(
        nickname="Flower Gift",
        description="You collect these, right?"
    )


class YoshiCandyPrize(ItemPrize):
    item = YoshiCandyItem
    _nickname = TreasureHunterNickname(
        nickname="Candy Piece",
        description="I wonder what flavor it is?"
    )


class FroggieDrinkPrize(ItemPrize):
    item = FroggieDrinkItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Drink",
        description="I wonder what flavor it is?"
    )


class MukuCookiePrize(ItemPrize):
    item = MukuCookieItem
    _nickname = TreasureHunterNickname(
        nickname="Baked Good",
        description="Looks tasty, doesn't it?"
    )


class ElixirPrize(ItemPrize):
    item = ElixirItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Drink",
        description="I wonder what flavor it is?"
    )


class MegalixirPrize(ItemPrize):
    item = MegalixirItem
    _nickname = TreasureHunterNickname(
        nickname="Red Drink",
        description="I wonder what flavor it is?"
    )


class SeeYaPrize(ItemPrize):
    item = SeeYaItem
    _nickname = TreasureHunterNickname(
        nickname="Eject Button",
        description="Seems useful in a pinch, doesn't\n it?"
    )


class TempleKeyPrize(ItemPrize):
    item = TempleKeyItem
    _nickname = TreasureHunterNickname(
        nickname="Golden Key",
        description="I wonder what it opens?"
    )


class GoodieBagPrize(ItemPrize):
    item = GoodieBagItem
    _nickname = TreasureHunterNickname(
        nickname="Coin Sack",
        description="It could make you rich!"
    )


class EarlierTimesPrize(ItemPrize):
    item = EarlierTimesItem
    _nickname = TreasureHunterNickname(
        nickname="Reset Button",
        description="Sounds useful in a pinch, doesn't\n it?"
    )


class FreshenUpPrize(ItemPrize):
    item = FreshenUpItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Drink",
        description="I wonder what flavor it is?"
    )


class RareFrogCoinPrize(ItemPrize):
    item = RareFrogCoinItem
    _nickname = TreasureHunterNickname(
        nickname="Green Coin",
        description="It looks different from most Frog \nCoins."
    )


class WalletPrize(ItemPrize):
    item = WalletItem
    _nickname = TreasureHunterNickname(
        nickname="Coin Sack",
        description="It looks like it belongs to someone."
    )


class CricketPiePrize(ItemPrize):
    item = CricketPieItem
    _nickname = TreasureHunterNickname(
        nickname="Baked Good",
        description="Looks tasty, doesn't it?"
    )


class RockCandyPrize(ItemPrize):
    item = RockCandyItem
    _nickname = TreasureHunterNickname(
        nickname="Candy Piece",
        description="I wonder what flavor it is?"
    )


class CastleKey1Prize(ItemPrize):
    item = CastleKey1Item
    _nickname = TreasureHunterNickname(
        nickname="Golden Key",
        description="I wonder what it opens?"
    )


class CastleKey2Prize(ItemPrize):
    item = CastleKey2Item
    _nickname = TreasureHunterNickname(
        nickname="Golden Key",
        description="I wonder what it opens?"
    )


class BambinoBombPrize(ItemPrize):
    item = BambinoBombItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device",
        description="Don't try this at home!"
    )


class ProgressiveCardPrize(ProgressiveItemPrize):
    _nickname = TreasureHunterNickname(
        nickname="Membership Card",
        description="It's sure to bring you an air of\n prestige."
    )
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3086_JUICE_BAR_CARD_UPGRADE)
        ])
    @property
    def npc_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3097_JUICE_BAR_CARD_NPC_GRANT)
        ])
    @property
    def standing_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3110_FREESTANDING_JUICE_BAR_CARD_GRANT)
        ])
    @property
    def river_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3396_MIDAS_CAVE_PROGRESSIVE_CARD_GRANTER)
        ])


class ProgressiveEggPrize(ProgressiveItemPrize):
    _nickname = TreasureHunterNickname(
        nickname="Mystery Egg",
        description="I have no idea what it does!\n It sort of grows on ya, huh?"
    )
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3087_PROGRESSIVE_EGG_UPGRADE)
        ])
    @property
    def npc_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3098_PROGRESSIVE_EGG_NPC_GRANT)
        ])
    @property
    def standing_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3111_FREESTANDING_PROGRESSIVE_EGG_GRANT)
        ])
    @property
    def river_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3397_MIDAS_CAVE_PROGRESSIVE_EGG_GRANTER)
        ])


class ExtraShinyStonePrize(ItemPrize):
    item = ExtraShinyStoneItem
    _nickname = TreasureHunterNickname(
        nickname="Crystal",
        description="It might have special powers.\n Or it might not."
    )
    remake_only = True


class CrystalShardPrize(ItemPrize):
    item = CrystalShardItem
    _nickname = TreasureHunterNickname(
        nickname="Crystal",
        description="It might have special powers.\n Or it might not."
    )
    remake_only = True


class RoomKeyPrize(ItemPrize):
    item = RoomKeyItem
    _nickname = TreasureHunterNickname(
        nickname="Golden Key",
        description="I wonder what it opens?"
    )


class ElderKeyPrize(ItemPrize):
    item = ElderKeyItem
    _nickname = TreasureHunterNickname(
        nickname="Golden Key",
        description="I wonder what it opens?"
    )


class ShedKeyPrize(ItemPrize):
    item = ShedKeyItem
    _nickname = TreasureHunterNickname(
        nickname="Golden Key",
        description="I wonder what it opens?"
    )


class FrightBombPrize(ItemPrize):
    item = FrightBombItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device",
        description="Don't try this at home!"
    )


class BeetleBoxPrize(ItemPrize):
    item = BeetleBoxItem
    # TODO: Could not find dialog_replacements for BeetleBox


class LuckyJewelPrize(ItemPrize):
    item = LuckyJewelItem
    _nickname = TreasureHunterNickname(
        nickname="Lucky Jewel",
        description="It’s sure to bring you plenty of\n good luck."
    )


class CrystallinePrize(ItemPrize):
    item = CrystallineItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Drink",
        description="I wonder what flavor it is?"
    )


class PowerBlastPrize(ItemPrize):
    item = PowerBlastItem
    _nickname = TreasureHunterNickname(
        nickname="Green Drink",
        description="I wonder what flavor it is?"
    )


class WiltShroomPrize(ItemPrize):
    item = WiltShroomItem
    _nickname = TreasureHunterNickname(
        nickname="Red Mushroom",
        description="It's just food, right?"
    )


class RottenMushPrize(ItemPrize):
    item = RottenMushItem
    _nickname = TreasureHunterNickname(
        nickname="Red Mushroom",
        description="It's just food, right?"
    )


class MoldyMushPrize(ItemPrize):
    item = MoldyMushItem
    _nickname = TreasureHunterNickname(
        nickname="Red Mushroom",
        description="It's just food, right?"
    )


class SeedPrize(ItemPrize):
    item = SeedItem
    _nickname = TreasureHunterNickname(
        nickname="Mysterious Seed",
        description="I wonder what will grow from it?"
    )


class FertilizerPrize(ItemPrize):
    item = FertilizerItem
    _nickname = TreasureHunterNickname(
        nickname="Bag of Dirt",
        description="It seems different from the soil\n I dug it out of."
    )


class BigBooFlagPrize(ItemPrize):
    item = BigBooFlagItem
    _nickname = TreasureHunterNickname(
        nickname="Invisible Flag",
        description="I wonder if someone is looking for\n this?"
    )


class DryBonesFlagPrize(ItemPrize):
    item = DryBonesFlagItem
    _nickname = TreasureHunterNickname(
        nickname="Invisible Flag",
        description="I wonder if someone is looking fon\n this?"
    )


class GreaperFlagPrize(ItemPrize):
    item = GreaperFlagItem
    _nickname = TreasureHunterNickname(
        nickname="Invisible Flag",
        description="I wonder if someone is looking for\n this?"
    )


class CricketJamPrize(ItemPrize):
    item = CricketJamItem
    _nickname = TreasureHunterNickname(
        nickname="Green Jelly",
        description="I wonder what flavor it is?"
    )


class RegularFireworksPrize(ItemPrize):
    item = FireworksItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device",
        description="Don't try this at home!"
    )


class ProgressiveFireworksPrize(ProgressiveItemPrize):
    item = FireworksItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device",
        description="Don't try this at home!"
    )
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3100_PROGRESSIVE_FIREWORKS_CHEST_GRANT)
        ])
    @property
    def npc_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E0185_NPC_QUEST_GRANT_PROGRESSIVE_FIREWORKS)
        ])
    @property
    def standing_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3113_FREESTANDING_PROGRESSIVE_FIREWORKS_GRANT)
        ])
    @property
    def river_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3399_MIDAS_CAVE_PROGRESSIVE_FIREWORK_GRANTER)
        ])


class StayVoucherPrize(ItemPrize):
    item = StayVoucherItem
    _nickname = TreasureHunterNickname(
        nickname="Special Ticket",
        description="You can probably redeem it at a\n fancy hotel."
    )
    remake_only = True


class BrightCardPrize(ItemPrize):
    item = BrightCardItem
    _nickname = TreasureHunterNickname(
        nickname="Membership Card",
        description="It's sure to bring you an air of\n prestige."
    )

class PoisonMushroomPrize(ItemPrize):
    item = MushroomItem2
    _nickname = TreasureHunterNickname(
        nickname="Red Mushroom",
        description="It's just food, right?"
    )


class StarEggPrize(ItemPrize):
    item = StarEggItem
    _nickname = TreasureHunterNickname(
        nickname="Mystery Egg",
        description="I have no idea what it does!\n It sort of grows on ya, huh?"
    )


### Other kinds of prizes ###


class BeetlemaniaPrize(StandardPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E0162_CHEST_GRANT_BEETLEMANIA)
        ])
    @property
    def npc_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E0161_NPC_QUEST_GRANT_BEETLEMANIA)
        ])
    @property
    def standing_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3109_FREESTANDING_BEETLEMANIA_GRANT)
        ])
    @property
    def river_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3395_MIDAS_CAVE_BEETLEMANIA_GRANTER)
        ])


class ShoesPrize(WeddingGearPrize):
    item = ShoesItem
    _nickname = TreasureHunterNickname(
        nickname="Ruby Slippers",
        description="Do you think they'll take you\n home?"
    )
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3943_SHOES_CHEST)
        ])
    @property
    def npc_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3931_GET_SHOES)
        ])
    @property
    def standing_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3935_FREESTANDING_SHOES)
        ])
    @property
    def river_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3939_RIVER_SHOES)
        ])


class BroochPrize(WeddingGearPrize):
    item = BroochItem
    _nickname = TreasureHunterNickname(
        nickname="Shiny Brooch",
        description="It looks pretty stylish."
    )
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3944_BROOCH_CHEST)
        ])
    @property
    def npc_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3932_GET_BROOCH)
        ])
    @property
    def standing_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3936_FREESTANDING_BROOCH)
        ])
    @property
    def river_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3940_RIVER_BROOCH)
        ])


class RingPrize(WeddingGearPrize):
    item = RingItem
    _nickname = TreasureHunterNickname(
        nickname="Wedding Ring",
        description="For that special someone!"
    )
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3945_RING_CHEST)
        ])
    @property
    def npc_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3933_GET_RING)
        ])
    @property
    def standing_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3937_FREESTANDING_RING)
        ])
    @property
    def river_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3941_RIVER_RING)
        ])


class CrownPrize(WeddingGearPrize):
    item = CrownItem
    _nickname = TreasureHunterNickname(
        nickname="Gold Crown",
        description="It looks pretty important!"
    )
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3946_CROWN_CHEST)
        ])
    @property
    def npc_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3934_GET_CROWN)
        ])
    @property
    def standing_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3938_FREESTANDING_CROWN)
        ])
    @property
    def river_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3942_RIVER_CROWN)
        ])

class RecoveryMushroomPrize(StandardPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([
            SetVarToConst(ITEM_ID, 48),
            JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST)
        ])
    @property
    def npc_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E0397_HEAL_IN_TOADSTOOLS_ROOM)
        ])
    @property
    def standing_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E2822_ASYNC_NO_ANIMATION_MUSHROOM)
        ])

class CoinPrize5(CoinPrize):
    amount = 5

    def __init__(self):
        super().__init__(self.amount)

class CoinPrize8(CoinPrize):
    amount = 8

    def __init__(self):
        super().__init__(self.amount)