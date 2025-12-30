from __future__ import annotations
from typing import TYPE_CHECKING

from randomizer.data.overworld_scripts.event.scripts.script_3645 import NPC_2
from randomizer.data.variables.dialog_names import *
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (
    EventScript,
    UsableEventScriptCommand,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    Return,
    SetVarToConst,
    JmpToEvent,
    Inc,
    SetBit,
    CharacterJoinsParty,
    ClearBit,
    RunDialog,
    ApplySolidityModToLevel,
    ApplyTileModToLevel,
    RemoveObjectFromSpecificLevel,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import NPC_3
from ..data.variables.variable_names import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    MARIO,
    MALLOW,
    GENO,
    BOWSER,
    TOADSTOOL,
)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (
    FormationMember,
)
from ..data.items.items import (
    CrystalShardItem,
    ExtraShinyStoneItem,
    HammerItem,
    FroggieStickItem,
    NokNokShellItem,
    PunchGloveItem,
    FingerShotItem,
    CymbalsItem,
    ChompItem,
    MasherItem,
    ChompShellItem,
    StayVoucherItem,
    SuperHammerItem,
    HandGunItem,
    WhompGloveItem,
    SlapGloveItem,
    TroopaShellItem,
    ParasolItem,
    HurlyGlovesItem,
    DoublePunchItem,
    RibbitStickItem,
    SpikedLinkItem,
    MegaGloveItem,
    WarFanItem,
    HandCannonItem,
    StickyGloveItem,
    UltraHammerItem,
    SuperSlapItem,
    DrillClawItem,
    StarGunItem,
    SonicCymbalItem,
    LazyShellItem,
    FryingPanItem,
    LuckyHammerItem,
    ShirtItem,
    PantsItem,
    ThickShirtItem,
    ThickPantsItem,
    MegaShirtItem,
    MegaPantsItem,
    WorkPantsItem,
    MegaCapeItem,
    HappyShirtItem,
    HappyPantsItem,
    HappyCapeItem,
    HappyShellItem,
    PolkaDressItem,
    SailorShirtItem,
    SailorPantsItem,
    SailorCapeItem,
    NauticaDressItem,
    CourageShellItem,
    FuzzyShirtItem,
    FuzzyPantsItem,
    FuzzyCapeItem,
    FuzzyDressItem,
    FireShirtItem,
    FirePantsItem,
    FireCapeItem,
    FireShellItem,
    FireDressItem,
    HeroShirtItem,
    PrincePantsItem,
    StarCapeItem,
    HealShellItem,
    RoyalDressItem,
    SuperSuitItem,
    ZoomShoesItem,
    SafetyBadgeItem,
    JumpShoesItem,
    SafetyRingItem,
    AmuletItem,
    ScroogeRingItem,
    ExpBoosterItem,
    AttackScarfItem,
    RareScarfItem,
    BtubRingItem,
    AntidotePinItem,
    WakeUpPinItem,
    FearlessPinItem,
    TrueformPinItem,
    CoinTrickItem,
    GhostMedalItem,
    JinxBeltItem,
    FeatherItem,
    TroopaPinItem,
    SignalRingItem,
    QuartzCharmItem,
    MushroomItem,
    MidMushroomItem,
    MaxMushroomItem,
    HoneySyrupItem,
    MapleSyrupItem,
    RoyalSyrupItem,
    PickMeUpItem,
    AbleJuiceItem,
    BracerItem,
    EnergizerItem,
    YoshiAdeItem,
    RedEssenceItem,
    KerokeroColaItem,
    YoshiCookieItem,
    PureWaterItem,
    SleepyBombItem,
    BadMushroomItem,
    FireBombItem,
    IceBombItem,
    FlowerTabItem,
    FlowerJarItem,
    FlowerBoxItem,
    YoshiCandyItem,
    FroggieDrinkItem,
    MukuCookieItem,
    ElixirItem,
    MegalixirItem,
    SeeYaItem,
    TempleKeyItem,
    GoodieBagItem,
    EarlierTimesItem,
    FreshenUpItem,
    RareFrogCoinItem,
    WalletItem,
    CricketPieItem,
    RockCandyItem,
    CastleKey1Item,
    CastleKey2Item,
    BambinoBombItem,
    RoomKeyItem,
    ElderKeyItem,
    ShedKeyItem,
    FrightBombItem,
    BeetleBoxItem,
    LuckyJewelItem,
    CrystallineItem,
    PowerBlastItem,
    WiltShroomItem,
    RottenMushItem,
    MoldyMushItem,
    SeedItem,
    FertilizerItem,
    BigBooFlagItem,
    DryBonesFlagItem,
    GreaperFlagItem,
    CricketJamItem,
    FireworksItem,
    BrightCardItem,
    StarEggItem,
    ShoesItem,
    BroochItem,
    RingItem,
    CrownItem,
    LazyShellItem2,
    MushroomItem2,
    WonderChompItem,
    Stella023Item,
    SageStickItem,
    TeamworkBandItem,
    EnduringBroochItem,
)
from ..data.variables.variable_names import *
from ..data.variables.room_names import *
from ..data.variables.event_script_names import *
from ..data.variables.battlefield_names import *
from ..data.enemies.enemies import *
from ..data.variables.battle_event_names import *
from ..data.allies.allies import (
    MARIO_Ally,
    MALLOW_Ally,
    GENO_Ally,
    BOWSER_Ally,
    TOADSTOOL_Ally,
)
from ..types.prize import (
    FrogCoinQuantityPrize,
    EXPStarPrize,
    StandardPrize,
    CoinQuantityPrize,
    SlotsPrize,
    BossFightPrize,
    CharacterPrize,
    StarPiecePrize,
    ItemPrize,
    SpellPrize,
    MimicFightInitiatorPrize,
    TreasureHunterNickname,
    ProgressiveItemPrize,
    WeddingGearPrize,
    SpecialItemPrizeType,
    KeyPrize,
)
from ..data.spells.spells import (
    JumpSpell,
    FireOrbSpell,
    SuperJumpSpell,
    SuperFlameSpell,
    UltraJumpSpell,
    UltraFlameSpell,
    ThunderboltSpell,
    HPRainSpell,
    PsychopathSpell,
    ShockerSpell,
    SnowySpell,
    PsychBombSpell,
    GenoBeamSpell,
    GenoBoostSpell,
    GenoWhirlSpell,
    GenoBlastSpell,
    GenoFlashSpell,
    TerrorizeSpell,
    PoisonGasSpell,
    CrusherSpell,
    BowserCrushSpell,
    TherapySpell,
    GroupHugSpell,
    MuteSpell,
    SleepyTimeSpell,
    ComeBackSpell,
    StarRainSpell,
)
from ..data.variables.overworld_sfx_names import *
from ..data.physical_objects.items import *

# Note: Gating flags are imported lazily in _get_gating_flags() to avoid circular import
# (flags.py → prizelocations.py → prizes.py → flags.py)

_gating_flags_cache: dict | None = None


def _get_gating_flags():
    """Lazily import and cache gating flags to avoid circular import."""
    global _gating_flags_cache
    if _gating_flags_cache is None:
        from ..types.flags import (
            BanditsWayGating,
            BanditsWayGate,
            KeroSewersGate,
            KeroSewersGating,
            BoosterTowerGate,
            BoosterTowerGating,
            PipeVaultGate,
            PipeVaultGating,
            Moleville1Gate,
            Moleville1Gating,
            ForestMazeGate,
            ForestMazeGating,
            BoosterHillGate,
            BoosterHillGating,
            MarrymoreGate,
            MarrymoreGating,
            YaridovichGate,
            YaridovichGating,
            SeaGate,
            SeaGating,
            LandsEndGate,
            LandsEndGating,
            BelomeTempleGate,
            BelomeTempleGating,
            MonstroTownGate,
            MonstroTownGating,
            NimbusGate,
            NimbusGating,
            BarrelVolcanoGate,
            BarrelVolcanoGating,
            BowsersKeepGate,
            BowsersKeepGating,
            FactoryGate,
            FactoryGating,
        )

        _gating_flags_cache = {
            "BanditsWayGating": BanditsWayGating,
            "BanditsWayGate": BanditsWayGate,
            "KeroSewersGate": KeroSewersGate,
            "KeroSewersGating": KeroSewersGating,
            "BoosterTowerGate": BoosterTowerGate,
            "BoosterTowerGating": BoosterTowerGating,
            "PipeVaultGate": PipeVaultGate,
            "PipeVaultGating": PipeVaultGating,
            "Moleville1Gate": Moleville1Gate,
            "Moleville1Gating": Moleville1Gating,
            "ForestMazeGate": ForestMazeGate,
            "ForestMazeGating": ForestMazeGating,
            "BoosterHillGate": BoosterHillGate,
            "BoosterHillGating": BoosterHillGating,
            "MarrymoreGate": MarrymoreGate,
            "MarrymoreGating": MarrymoreGating,
            "YaridovichGate": YaridovichGate,
            "YaridovichGating": YaridovichGating,
            "SeaGate": SeaGate,
            "SeaGating": SeaGating,
            "LandsEndGate": LandsEndGate,
            "LandsEndGating": LandsEndGating,
            "BelomeTempleGate": BelomeTempleGate,
            "BelomeTempleGating": BelomeTempleGating,
            "MonstroTownGate": MonstroTownGate,
            "MonstroTownGating": MonstroTownGating,
            "NimbusGate": NimbusGate,
            "NimbusGating": NimbusGating,
            "BarrelVolcanoGate": BarrelVolcanoGate,
            "BarrelVolcanoGating": BarrelVolcanoGating,
            "BowsersKeepGate": BowsersKeepGate,
            "BowsersKeepGating": BowsersKeepGating,
            "FactoryGate": FactoryGate,
            "FactoryGating": FactoryGating,
        }
    return _gating_flags_cache


# Convenience function to get a specific flag
def _gf(name: str):
    """Get a gating flag by name."""
    return _get_gating_flags()[name]


if TYPE_CHECKING:
    from ..types.gameworld import GameWorld

### Real items ###


class HammerPrize(ItemPrize):
    item = HammerItem
    _nickname = TreasureHunterNickname(
        nickname="Hammer", description="I'm not sure if it does anything\n else."
    )
    _model = HammerObject


class FroggiestickPrize(ItemPrize):
    item = FroggieStickItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_2
    _nickname = TreasureHunterNickname(
        nickname="Caster's Staff", description="It looks pretty good at bonking."
    )
    _monstro_shuffle = True
    _model = StickObject


class NokNokShellPrize(ItemPrize):
    item = NokNokShellItem
    _nickname = TreasureHunterNickname(
        nickname="Green Shell", description="There's no turtle inside of it."
    )
    _model = GreenShellObject


class PunchGlovePrize(ItemPrize):
    item = PunchGloveItem
    _nickname = TreasureHunterNickname(
        nickname="Glove", description="You don't drink water out of it."
    )
    _model = GloveObject


class FingerShotPrize(ItemPrize):
    item = FingerShotItem
    _nickname = TreasureHunterNickname(
        nickname="Pellet Shooter", description="It was probably owned by a kid."
    )


class CymbalsPrize(ItemPrize):
    item = CymbalsItem
    _nickname = TreasureHunterNickname(
        nickname="Percussion Plate", description="I bet it could get pretty loud."
    )
    _model = MusicObject


class ChompPrize(ItemPrize):
    item = ChompItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_2
    _nickname = TreasureHunterNickname(
        nickname="Chain Chomp", description="It's hungry to stir up some trouble."
    )
    _monstro_shuffle = True
    _model = ChompObject


class MasherPrize(ItemPrize):
    item = MasherItem
    _nickname = TreasureHunterNickname(
        nickname="Hammer", description="I'm not sure if it does anything\n else."
    )
    _model = HammerObject


class ChompShellPrize(ItemPrize):
    item = ChompShellItem
    _nickname = TreasureHunterNickname(
        nickname="Chomp Exoskeleton",
        description="I didn't even know those things\n could shed their skin.",
    )
    _model = ChompObject


class SuperHammerPrize(ItemPrize):
    item = SuperHammerItem
    _nickname = TreasureHunterNickname(
        nickname="Hammer", description="I'm not sure if it does anything\n else."
    )
    _model = HammerObject


class HandGunPrize(ItemPrize):
    item = HandGunItem
    _nickname = TreasureHunterNickname(
        nickname="BB Gun", description="I'll throw in some ammo, too."
    )


class WhompGlovePrize(ItemPrize):
    item = WhompGloveItem
    _nickname = TreasureHunterNickname(
        nickname="Glove", description="You don't drink water out of it."
    )
    _model = GloveObject


class SlapGlovePrize(ItemPrize):
    item = SlapGloveItem
    _nickname = TreasureHunterNickname(
        nickname="Glove", description="You don't drink water out of it."
    )
    _model = GloveObject


class TroopaShellPrize(ItemPrize):
    item = TroopaShellItem
    _nickname = TreasureHunterNickname(
        nickname="Red Shell", description="There's no turtle inside of it."
    )
    _model = RedShellObject


class ParasolPrize(ItemPrize):
    item = ParasolItem
    _nickname = TreasureHunterNickname(
        nickname="Umbrella", description="There's no turtle inside of it."
    )
    _model = ParasolObject


class HurlyGlovesPrize(ItemPrize):
    item = HurlyGlovesItem
    _nickname = TreasureHunterNickname(
        nickname="Glove", description="You don't drink water out of it."
    )
    _model = GloveObject


class DoublePunchPrize(ItemPrize):
    item = DoublePunchItem
    _nickname = TreasureHunterNickname(
        nickname="Rocket Launcher",
        description="Be careful, it could take your\n hands clean off.",
    )
    _model = GloveObject


class RibbitStickPrize(ItemPrize):
    item = RibbitStickItem
    _nickname = TreasureHunterNickname(
        nickname="Caster's Staff", description="It looks pretty good at bonking."
    )
    _model = StickObject


class SpikedLinkPrize(ItemPrize):
    item = SpikedLinkItem
    _nickname = TreasureHunterNickname(
        nickname="Chain Chomp", description="This one's got thorns on it."
    )
    _model = ChompObject


class MegaGlovePrize(ItemPrize):
    item = MegaGloveItem
    _nickname = TreasureHunterNickname(
        nickname="Glove", description="You don't drink water out of it."
    )
    _model = GloveObject


class WarFanPrize(ItemPrize):
    item = WarFanItem
    _nickname = TreasureHunterNickname(
        nickname="Spiked Fan", description="Pretty, but deadly!"
    )
    _model = FanObject


class HandCannonPrize(ItemPrize):
    item = HandCannonItem
    _nickname = TreasureHunterNickname(
        nickname="Cannon Launcher", description="You need strong elbows for this!"
    )


class StickyGlovePrize(ItemPrize):
    item = StickyGloveItem
    _nickname = TreasureHunterNickname(
        nickname="Glove", description="You don't drink water out of it."
    )
    _model = GloveObject


class UltraHammerPrize(ItemPrize):
    item = UltraHammerItem
    _nickname = TreasureHunterNickname(
        nickname="Hammer", description="I'm not sure if it does anything\n else."
    )
    _model = HammerObject


class SuperSlapPrize(ItemPrize):
    item = SuperSlapItem
    _nickname = TreasureHunterNickname(
        nickname="Glove", description="You don't drink water out of it."
    )
    _model = GloveObject


class DrillClawPrize(ItemPrize):
    item = DrillClawItem
    _nickname = TreasureHunterNickname(
        nickname="Drilling Appendage",
        description="I bet you could do some real damage\n with this.",
    )
    _model = GloveObject


class StarGunPrize(ItemPrize):
    item = StarGunItem
    _nickname = TreasureHunterNickname(
        nickname="Celestial Launcher",
        description="I bet you could do some real damage\n with this.",
    )
    _model = TinyStarObject


class SonicCymbalPrize(ItemPrize):
    item = SonicCymbalItem
    _nickname = TreasureHunterNickname(
        nickname="Psych Percussion",
        description="This could catch monsters\n off-guard.",
    )
    _model = MusicObject


class LazyShellWeaponPrize(ItemPrize):
    item = LazyShellItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_2
    _nickname = TreasureHunterNickname(
        nickname="Red Shell", description="There's no turtle inside of it."
    )
    _monstro_shuffle = True
    _model = RedShellObject


class FryingPanPrize(ItemPrize):
    item = FryingPanItem
    _nickname = TreasureHunterNickname(
        nickname="Metal Plate", description="Don't know what it’s used for."
    )
    _model = FryingPanObject


class WonderChompPrize(ItemPrize):
    item = WonderChompItem
    _nickname = TreasureHunterNickname(
        nickname="Golden Chomp",
        description="It's hungry to stir up some BIG\n trouble.",
    )
    remake_only = True
    _monstro_shuffle = True
    _model = ChompObject


class Stella023Prize(ItemPrize):
    item = Stella023Item
    _nickname = TreasureHunterNickname(
        nickname="Cool Gun", description="Why does it remind me of a train?"
    )
    remake_only = True
    _monstro_shuffle = True
    _model = TinyStarObject


class SageStickPrize(ItemPrize):
    item = SageStickItem
    _nickname = TreasureHunterNickname(
        nickname="Caster's Staff", description="It looks pretty good at bonking."
    )
    remake_only = True
    _monstro_shuffle = True
    _model = StickObject


class LuckyHammerPrize(ItemPrize):
    item = LuckyHammerItem
    _nickname = TreasureHunterNickname(
        nickname="Hammer", description="I'm not sure if it does anything\n else."
    )
    _model = HammerObject


class ShirtPrize(ItemPrize):
    item = ShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Overalls", description="Don't go to work without 'em!"
    )


class PantsPrize(ItemPrize):
    item = PantsItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Pants", description="They're comfy and easy to wear."
    )


class ThickShirtPrize(ItemPrize):
    item = ThickShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Blue/Red Overalls", description="They look pretty sturdy."
    )


class ThickPantsPrize(ItemPrize):
    item = ThickPantsItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Pants", description="They're comfy and easy to wear."
    )


class MegaShirtPrize(ItemPrize):
    item = MegaShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Orange Overalls", description="You're sure to stand out in these!"
    )


class MegaPantsPrize(ItemPrize):
    item = MegaPantsItem
    _nickname = TreasureHunterNickname(
        nickname="Striped Red Pants",
        description="Made from only the finest threads\n in Mysidia.",
    )


class WorkPantsPrize(ItemPrize):
    item = WorkPantsItem
    _nickname = TreasureHunterNickname(
        nickname="Stained Pants", description="They look a bit worn out."
    )


class MegaCapePrize(ItemPrize):
    item = MegaCapeItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Cape", description="It looks pretty cool, right?"
    )


class HappyShirtPrize(ItemPrize):
    item = HappyShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Orange Overalls", description="You're sure to stand out in these!"
    )


class HappyPantsPrize(ItemPrize):
    item = HappyPantsItem
    _nickname = TreasureHunterNickname(
        nickname="Pink Pants", description="They're all the rage these days!"
    )


class HappyCapePrize(ItemPrize):
    item = HappyCapeItem
    _nickname = TreasureHunterNickname(
        nickname="Rainbow Cape", description="I'd be proud to wear this!"
    )


class HappyShellPrize(ItemPrize):
    item = HappyShellItem
    _nickname = TreasureHunterNickname(
        nickname="Green Shell", description="There's no turtle inside of it."
    )
    _model = GreenShellObject


class PolkaDressPrize(ItemPrize):
    item = PolkaDressItem
    _nickname = TreasureHunterNickname(
        nickname="Pink Dress", description="For serious fashionistas."
    )


class SailorShirtPrize(ItemPrize):
    item = SailorShirtItem
    _nickname = TreasureHunterNickname(
        nickname="White Overalls", description="Built for life on the sea."
    )


class SailorPantsPrize(ItemPrize):
    item = SailorPantsItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Pants", description="They're comfy and easy to wear."
    )


class SailorCapePrize(ItemPrize):
    item = SailorCapeItem
    _nickname = TreasureHunterNickname(
        nickname="White Cape", description="Built for life on the sea."
    )


class NauticaDressPrize(ItemPrize):
    item = NauticaDressItem
    _nickname = TreasureHunterNickname(
        nickname="School Uniform", description="The neckerchief is included."
    )


class CourageShellPrize(ItemPrize):
    item = CourageShellItem
    _nickname = TreasureHunterNickname(
        nickname="Green Shell", description="There's no turtle inside of it."
    )
    _model = GreenShellObject


class FuzzyShirtPrize(ItemPrize):
    item = FuzzyShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Green Overalls", description="Made of the finest fleece."
    )


class FuzzyPantsPrize(ItemPrize):
    item = FuzzyPantsItem
    _nickname = TreasureHunterNickname(
        nickname="Striped Red Pants",
        description="Made from only the finest threads\n in Mysidia.",
    )


class FuzzyCapePrize(ItemPrize):
    item = FuzzyCapeItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Cape", description="Made of the finest fleece."
    )


class FuzzyDressPrize(ItemPrize):
    item = FuzzyDressItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Dress", description="Made of the finest fleece."
    )


class FireShirtPrize(ItemPrize):
    item = FireShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Orange Overalls", description="You're sure to stand out in these!"
    )


class FirePantsPrize(ItemPrize):
    item = FirePantsItem
    _nickname = TreasureHunterNickname(
        nickname="Red Pants", description="Stylish AND warm!"
    )


class FireCapePrize(ItemPrize):
    item = FireCapeItem
    _nickname = TreasureHunterNickname(
        nickname="Orange Cape", description="The pattern on it is pretty cool."
    )


class FireShellPrize(ItemPrize):
    item = FireShellItem
    _nickname = TreasureHunterNickname(
        nickname="Red Shell", description="There's no turtle inside of it."
    )
    _model = RedShellObject


class FireDressPrize(ItemPrize):
    item = FireDressItem
    _nickname = TreasureHunterNickname(
        nickname="Red Dress", description="The pattern on it is pretty cool."
    )


class HeroShirtPrize(ItemPrize):
    item = HeroShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Blue/Red Overalls", description="They look pretty sturdy."
    )


class PrincePantsPrize(ItemPrize):
    item = PrincePantsItem
    _nickname = TreasureHunterNickname(
        nickname="Flash Pants", description="You'll look like a superhero in\n these!"
    )
    _model = CrownObject


class StarCapePrize(ItemPrize):
    item = StarCapeItem
    _nickname = TreasureHunterNickname(
        nickname="Freedom Cape", description="It's red, white, and blue."
    )
    _model = TinyStarObject


class HealShellPrize(ItemPrize):
    item = HealShellItem
    _nickname = TreasureHunterNickname(
        nickname="Green Shell", description="There's no turtle inside of it."
    )
    _model = GreenShellObject


class RoyalDressPrize(ItemPrize):
    item = RoyalDressItem
    _nickname = TreasureHunterNickname(
        nickname="Fancy Dress", description="Check out the gold trim!"
    )
    _model = CrownObject


class SuperSuitPrize(ItemPrize):
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_1
    item = SuperSuitItem
    _nickname = TreasureHunterNickname(
        nickname="Jumpsuit", description="It looks pretty powerful, right?"
    )
    _monstro_shuffle = True


class LazyShellArmorPrize(ItemPrize):
    item = LazyShellItem2
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_2
    _nickname = TreasureHunterNickname(
        nickname="Red Shell", description="There's no turtle inside of it."
    )
    _monstro_shuffle = True
    _model = RedShellObject


class ZoomShoesPrize(ItemPrize):
    item = ZoomShoesItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_2
    _nickname = TreasureHunterNickname(
        nickname="Red Vans", description="I bet you can run really fast in\n these."
    )
    _monstro_shuffle = True
    _model = ShoesObject


class SafetyBadgePrize(ItemPrize):
    item = SafetyBadgeItem
    _nickname = TreasureHunterNickname(
        nickname="Rainbow Button",
        description="I don't really follow politics, but\n this button looks like it's against\n a lot of things.",
    )
    _model = BroochObject


class JumpShoesPrize(ItemPrize):
    item = JumpShoesItem
    _nickname = TreasureHunterNickname(
        nickname="Brown Clogs", description="Check out the thick soles!"
    )
    _model = ShoesObject


class SafetyRingPrize(ItemPrize):
    item = SafetyRingItem
    _nickname = TreasureHunterNickname(
        nickname="Protective Charm", description="Never go into battle without it."
    )
    _model = RingObject


class AmuletPrize(ItemPrize):
    item = AmuletItem
    _nickname = TreasureHunterNickname(
        nickname="Stinky Charm", description="It'll help you weather the elements."
    )
    _model = CardObject


class ScroogeRingPrize(ItemPrize):
    item = ScroogeRingItem
    _nickname = TreasureHunterNickname(
        nickname="Mage Totem", description="It might help with spellcasting."
    )
    _model = RingObject


class ExpBoosterPrize(ItemPrize):
    item = ExpBoosterItem
    _nickname = TreasureHunterNickname(
        nickname="Training Device", description="This'll make you strong in no time!"
    )


class AttackScarfPrize(ItemPrize):
    item = AttackScarfItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_1
    _nickname = TreasureHunterNickname(
        nickname="Starry Scarf", description="It could save your life!"
    )
    _monstro_shuffle = True


class RareScarfPrize(ItemPrize):
    item = RareScarfItem
    _nickname = TreasureHunterNickname(
        nickname="White Cloth", description="You don't see these around often."
    )


class BtubRingPrize(ItemPrize):
    item = BtubRingItem
    _nickname = TreasureHunterNickname(
        nickname="Wedding Ring", description="For that special someone!"
    )
    _model = RingObject


class AntidotePinPrize(ItemPrize):
    item = AntidotePinItem
    _nickname = TreasureHunterNickname(
        nickname="Green Button", description="Looks like an environmentalist\n thing."
    )
    _model = BroochObject


class WakeUpPinPrize(ItemPrize):
    item = WakeUpPinItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Button", description="Looks like an anti-fur thing."
    )
    _model = BroochObject


class FearlessPinPrize(ItemPrize):
    item = FearlessPinItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Button", description="Who you gonna call?\n GHOSTBUSTERS!"
    )
    _model = BroochObject


class TrueformPinPrize(ItemPrize):
    item = TrueformPinItem
    _nickname = TreasureHunterNickname(
        nickname="Orange Button",
        description="For someone who doesn't like\n scarecrows.",
    )
    _model = BroochObject


class CoinTrickPrize(ItemPrize):
    item = CoinTrickItem
    _nickname = TreasureHunterNickname(
        nickname="Fortune Charm", description="It's sure to make you very rich."
    )


class GhostMedalPrize(ItemPrize):
    item = GhostMedalItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_1
    _nickname = TreasureHunterNickname(
        nickname="Military Decoration", description="I wonder what powers it bestows?"
    )
    _monstro_shuffle = True


class JinxBeltPrize(ItemPrize):
    item = JinxBeltItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_1
    _nickname = TreasureHunterNickname(
        nickname="Black Sash", description="A true fighter would love this."
    )
    _monstro_shuffle = True


class FeatherPrize(ItemPrize):
    item = FeatherItem
    _nickname = TreasureHunterNickname(
        nickname="Fluttering Quill", description="It's pretty exotic, isn't it?"
    )
    _model = FeatherObject


class TroopaPinPrize(ItemPrize):
    item = TroopaPinItem
    _nickname = TreasureHunterNickname(
        nickname="Military Decoration", description="I wonder what powers it bestows?"
    )
    _model = BroochObject


class SignalRingPrize(ItemPrize):
    item = SignalRingItem
    _nickname = TreasureHunterNickname(
        nickname="Bell Charm", description="I wonder what it can help you find?"
    )
    _model = RingObject


class QuartzCharmPrize(ItemPrize):
    item = QuartzCharmItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_1
    _nickname = TreasureHunterNickname(
        nickname="Crystal",
        description="It might have special powers.\n Or it might not.",
    )
    _monstro_shuffle = True
    _model = CrystalObject


class TeamworkBandPrize(ItemPrize):
    item = TeamworkBandItem
    _nickname = TreasureHunterNickname(
        nickname="Friendship Bracelet",
        description="Maybe the real treasure is the\n friends we made along the way.",
    )
    remake_only = True
    _monstro_shuffle = True


class EnduringBroochPrize(ItemPrize):
    item = EnduringBroochItem
    _nickname = TreasureHunterNickname(
        nickname="Shiny Brooch", description="It looks pretty stylish."
    )
    remake_only = True
    _monstro_shuffle = True
    _model = BroochObject


class MushroomPrize(ItemPrize):
    item = MushroomItem
    _nickname = TreasureHunterNickname(
        nickname="Red Mushroom", description="It's just food, right?"
    )
    _model = RedMushroomObject


class MidMushroomPrize(ItemPrize):
    item = MidMushroomItem
    _nickname = TreasureHunterNickname(
        nickname="Green Mushroom", description="It's just food, right?"
    )
    _model = GreenMushroomObject


class MaxMushroomPrize(ItemPrize):
    item = MaxMushroomItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Mushroom", description="It's just food, right?"
    )
    _model = YellowMushroomObject


class HoneySyrupPrize(ItemPrize):
    item = HoneySyrupItem
    _nickname = TreasureHunterNickname(
        nickname="Red Drink", description="I wonder what flavor it is?"
    )
    _model = RedSyrupObject


class MapleSyrupPrize(ItemPrize):
    item = MapleSyrupItem
    _nickname = TreasureHunterNickname(
        nickname="Green Drink", description="I wonder what flavor it is?"
    )
    _model = GreenSyrupObject


class RoyalSyrupPrize(ItemPrize):
    item = RoyalSyrupItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Drink", description="I wonder what flavor it is?"
    )
    _model = YellowSyrupObject


class PickMeUpPrize(ItemPrize):
    item = PickMeUpItem
    _nickname = TreasureHunterNickname(
        nickname="Red Drink", description="I wonder what flavor it is?"
    )
    _model = StarDrinkObject


class AbleJuicePrize(ItemPrize):
    item = AbleJuiceItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Drink", description="I wonder what flavor it is?"
    )
    _model = RDrinkObject


class BracerPrize(ItemPrize):
    item = BracerItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Drink", description="I wonder what flavor it is?"
    )
    _model = DDrinkObject


class EnergizerPrize(ItemPrize):
    item = EnergizerItem
    _nickname = TreasureHunterNickname(
        nickname="Green Drink", description="I wonder what flavor it is?"
    )
    _model = PDrinkObject


class YoshiAdePrize(ItemPrize):
    item = YoshiAdeItem
    _nickname = TreasureHunterNickname(
        nickname="Green Drink", description="I wonder what flavor it is?"
    )
    _model = GreenJuiceObject


class RedEssencePrize(ItemPrize):
    item = RedEssenceItem
    _nickname = TreasureHunterNickname(
        nickname="Red Drink", description="I wonder what flavor it is?"
    )
    _model = RedJuiceObject


class KerokeroColaPrize(ItemPrize):
    item = KerokeroColaItem
    _nickname = TreasureHunterNickname(
        nickname="Green Drink", description="I wonder what flavor it is?"
    )
    _model = FrogDrinkObject


class YoshiCookiePrize(ItemPrize):
    item = YoshiCookieItem
    _nickname = TreasureHunterNickname(
        nickname="Baked Good", description="Looks tasty, doesn't it?"
    )
    _model = CookieObject


class PureWaterPrize(ItemPrize):
    item = PureWaterItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Drink", description="I wonder what flavor it is?"
    )
    _model = BlueSyrupObject


class SleepyBombPrize(ItemPrize):
    item = SleepyBombItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device", description="Don't try this at home!"
    )
    _model = YellowBombObject


class BadMushroomPrize(ItemPrize):
    item = BadMushroomItem
    _nickname = TreasureHunterNickname(
        nickname="Red Mushroom", description="It's just food, right?"
    )
    _model = RedMushroomObject


class FireBombPrize(ItemPrize):
    item = FireBombItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device", description="Don't try this at home!"
    )
    _model = RedBombObject


class IceBombPrize(ItemPrize):
    item = IceBombItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device", description="Don't try this at home!"
    )
    _model = BlueBombObject


class FlowerTabPrize(ItemPrize):
    item = FlowerTabItem
    _nickname = TreasureHunterNickname(
        nickname="Flower Capsule", description="You collect these, right?"
    )


class FlowerJarPrize(ItemPrize):
    item = FlowerJarItem
    _nickname = TreasureHunterNickname(
        nickname="Flower Set", description="You collect these, right?"
    )


class FlowerBoxPrize(ItemPrize):
    item = FlowerBoxItem
    _nickname = TreasureHunterNickname(
        nickname="Flower Gift", description="You collect these, right?"
    )


class YoshiCandyPrize(ItemPrize):
    item = YoshiCandyItem
    _nickname = TreasureHunterNickname(
        nickname="Candy Piece", description="I wonder what flavor it is?"
    )
    _model = GreenCandyObject


class FroggieDrinkPrize(ItemPrize):
    item = FroggieDrinkItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Drink", description="I wonder what flavor it is?"
    )
    _model = YellowMusicDrinkObject


class MukuCookiePrize(ItemPrize):
    item = MukuCookieItem
    _nickname = TreasureHunterNickname(
        nickname="Baked Good", description="Looks tasty, doesn't it?"
    )
    _model = CookieObject


class ElixirPrize(ItemPrize):
    item = ElixirItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Drink", description="I wonder what flavor it is?"
    )
    _model = BlueMusicDrinkObject


class MegalixirPrize(ItemPrize):
    item = MegalixirItem
    _nickname = TreasureHunterNickname(
        nickname="Red Drink", description="I wonder what flavor it is?"
    )
    _model = RedMusicDrinkObject


class SeeYaPrize(ItemPrize):
    item = SeeYaItem
    _nickname = TreasureHunterNickname(
        nickname="Eject Button", description="Seems useful in a pinch, doesn't\n it?"
    )


class TempleKeyPrize(ItemPrize, KeyPrize):
    item = TempleKeyItem
    _nickname = TreasureHunterNickname(
        nickname="Golden Key", description="I wonder what it opens?"
    )
    _model = KeyObject


class GoodieBagPrize(ItemPrize):
    item = GoodieBagItem
    _nickname = TreasureHunterNickname(
        nickname="Coin Sack", description="It could make you rich!"
    )



class EarlierTimesPrize(ItemPrize):
    item = EarlierTimesItem
    _nickname = TreasureHunterNickname(
        nickname="Reset Button", description="Sounds useful in a pinch, doesn't\n it?"
    )
    


class FreshenUpPrize(ItemPrize):
    item = FreshenUpItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Drink", description="I wonder what flavor it is?"
    )
    _model = RDrinkObject


class RareFrogCoinPrize(ItemPrize, KeyPrize):
    item = RareFrogCoinItem
    _nickname = TreasureHunterNickname(
        nickname="Green Coin", description="It looks different from most Frog \nCoins."
    )
    _model = SmallFrogCoinObject


class WalletPrize(ItemPrize, KeyPrize):
    item = WalletItem
    _nickname = TreasureHunterNickname(
        nickname="Coin Sack", description="It looks like it belongs to someone."
    )
    


class CricketPiePrize(ItemPrize, KeyPrize):
    item = CricketPieItem
    _nickname = TreasureHunterNickname(
        nickname="Baked Good", description="Looks tasty, doesn't it?"
    )
    _model = CookieObject


class RockCandyPrize(ItemPrize):
    item = RockCandyItem
    _nickname = TreasureHunterNickname(
        nickname="Candy Piece", description="I wonder what flavor it is?"
    )
    _model = BlueCandyObject


class CastleKey1Prize(ItemPrize, KeyPrize):
    item = CastleKey1Item
    _nickname = TreasureHunterNickname(
        nickname="Golden Key", description="I wonder what it opens?"
    )
    _model = KeyObject


class CastleKey2Prize(ItemPrize, KeyPrize):
    item = CastleKey2Item
    _nickname = TreasureHunterNickname(
        nickname="Golden Key", description="I wonder what it opens?"
    )
    _model = KeyObject


class BambinoBombPrize(ItemPrize, KeyPrize):
    item = BambinoBombItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device", description="Don't try this at home!"
    )
    _model = MicrobombObject


class ProgressiveCardPrize(ProgressiveItemPrize, KeyPrize):
    _nickname = TreasureHunterNickname(
        nickname="Membership Card",
        description="It's sure to bring you an air of\n prestige.",
    )
    _model = CardObject

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3086_JUICE_BAR_CARD_UPGRADE)])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3097_JUICE_BAR_CARD_NPC_GRANT)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3110_FREESTANDING_JUICE_BAR_CARD_GRANT)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3396_MIDAS_CAVE_PROGRESSIVE_CARD_GRANTER)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3115_HILL_PROGRESSIVE_CARD)])


class ProgressiveEggPrize(ProgressiveItemPrize):
    _nickname = TreasureHunterNickname(
        nickname="Mystery Egg",
        description="I have no idea what it does!\n It sort of grows on ya, huh?",
    )
    _model = EggObject

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3087_PROGRESSIVE_EGG_UPGRADE)])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3098_PROGRESSIVE_EGG_NPC_GRANT)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3111_FREESTANDING_PROGRESSIVE_EGG_GRANT)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3397_MIDAS_CAVE_PROGRESSIVE_EGG_GRANTER)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3114_HILL_PROGRESSIVE_EGG)])


class ExtraShinyStonePrize(ItemPrize, KeyPrize):
    item = ExtraShinyStoneItem
    _nickname = TreasureHunterNickname(
        nickname="Crystal",
        description="It might have special powers.\n Or it might not.",
    )
    remake_only = True
    _model = CrystalObject


class CrystalShardPrize(ItemPrize, KeyPrize):
    item = CrystalShardItem
    _nickname = TreasureHunterNickname(
        nickname="Crystal",
        description="It might have special powers.\n Or it might not.",
    )
    remake_only = True
    _model = CrystalObject


class RoomKeyPrize(ItemPrize, KeyPrize):
    item = RoomKeyItem
    _nickname = TreasureHunterNickname(
        nickname="Golden Key", description="I wonder what it opens?"
    )
    _model = KeyObject  


class ElderKeyPrize(ItemPrize, KeyPrize):
    item = ElderKeyItem
    _nickname = TreasureHunterNickname(
        nickname="Golden Key", description="I wonder what it opens?"
    )
    _model = KeyObject


class ShedKeyPrize(ItemPrize, KeyPrize):
    item = ShedKeyItem
    _nickname = TreasureHunterNickname(
        nickname="Golden Key", description="I wonder what it opens?"
    )
    _model = KeyObject


class FrightBombPrize(ItemPrize):
    item = FrightBombItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device", description="Don't try this at home!"
    )
    _model = GreenBombObject


class BeetleBoxPrize(ItemPrize):
    item = BeetleBoxItem
    _model = BeetleObject
    # TODO: Could not find dialog_replacements for BeetleBox


class LuckyJewelPrize(ItemPrize):
    item = LuckyJewelItem
    _nickname = TreasureHunterNickname(
        nickname="Lucky Jewel",
        description="It’s sure to bring you plenty of\n good luck.",
    )
    _model = CrystalObject


class CrystallinePrize(ItemPrize):
    item = CrystallineItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Drink", description="I wonder what flavor it is?"
    )
    _model = DDrinkObject


class PowerBlastPrize(ItemPrize):
    item = PowerBlastItem
    _nickname = TreasureHunterNickname(
        nickname="Green Drink", description="I wonder what flavor it is?"
    )
    _model = PDrinkObject


class WiltShroomPrize(ItemPrize):
    item = WiltShroomItem
    _nickname = TreasureHunterNickname(
        nickname="Red Mushroom", description="It's just food, right?"
    )
    _model = BananaObject


class RottenMushPrize(ItemPrize):
    item = RottenMushItem
    _nickname = TreasureHunterNickname(
        nickname="Red Mushroom", description="It's just food, right?"
    )
    _model = BananaObject


class MoldyMushPrize(ItemPrize):
    item = MoldyMushItem
    _nickname = TreasureHunterNickname(
        nickname="Red Mushroom", description="It's just food, right?"
    )
    _model = BananaObject


class SeedPrize(ItemPrize, KeyPrize):
    item = SeedItem
    _nickname = TreasureHunterNickname(
        nickname="Mysterious Seed", description="I wonder what will grow from it?"
    )
    _model = BerryObject


class FertilizerPrize(ItemPrize, KeyPrize):
    item = FertilizerItem
    _nickname = TreasureHunterNickname(
        nickname="Bag of Dirt",
        description="It seems different from the soil\n I dug it out of.",
    )


class BigBooFlagPrize(ItemPrize, KeyPrize):
    item = BigBooFlagItem
    _nickname = TreasureHunterNickname(
        nickname="Invisible Flag",
        description="I wonder if someone is looking for\n this?",
    )
    _model = CardObject


class DryBonesFlagPrize(ItemPrize, KeyPrize):
    item = DryBonesFlagItem
    _nickname = TreasureHunterNickname(
        nickname="Invisible Flag",
        description="I wonder if someone is looking fon\n this?",
    )
    _model = CardObject


class GreaperFlagPrize(ItemPrize, KeyPrize):
    item = GreaperFlagItem
    _nickname = TreasureHunterNickname(
        nickname="Invisible Flag",
        description="I wonder if someone is looking for\n this?",
    )
    _model = CardObject


class CricketJamPrize(ItemPrize, KeyPrize):
    item = CricketJamItem
    _nickname = TreasureHunterNickname(
        nickname="Green Jelly", description="I wonder what flavor it is?"
    )
    _model = GreenJuiceObject


class RegularFireworksPrize(ItemPrize):
    item = FireworksItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device", description="Don't try this at home!"
    )


class ProgressiveFireworksPrize(ProgressiveItemPrize, KeyPrize):
    item = FireworksItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device", description="Don't try this at home!"
    )
    _model = ProgressiveFireworksObject

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3100_PROGRESSIVE_FIREWORKS_CHEST_GRANT)])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E0185_NPC_QUEST_GRANT_PROGRESSIVE_FIREWORKS)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3113_FREESTANDING_PROGRESSIVE_FIREWORKS_GRANT)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3399_MIDAS_CAVE_PROGRESSIVE_FIREWORK_GRANTER)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E0217_HILL_FIREWORKS)])


class StayVoucherPrize(ItemPrize):
    item = StayVoucherItem
    _nickname = TreasureHunterNickname(
        nickname="Special Ticket",
        description="You can probably redeem it at a\n fancy hotel.",
    )
    remake_only = True
    _model = CardObject


class BrightCardPrize(ItemPrize, KeyPrize):
    item = BrightCardItem
    _nickname = TreasureHunterNickname(
        nickname="Membership Card",
        description="It's sure to bring you an air of\n prestige.",
    )
    _model = CardObject


class PoisonMushroomPrize(ItemPrize):
    item = MushroomItem2
    _nickname = TreasureHunterNickname(
        nickname="Red Mushroom", description="It's just food, right?"
    )
    _model = RedMushroomObject


class StarEggPrize(ItemPrize):
    item = StarEggItem
    _nickname = TreasureHunterNickname(
        nickname="Mystery Egg",
        description="I have no idea what it does!\n It sort of grows on ya, huh?",
    )
    _model = EggObject


### Other kinds of prizes ###


class BeetlemaniaPrize(StandardPrize):
    _nickname = TreasureHunterNickname(
        nickname="Video Game",
        description="It's pretty addictive.",
    )
    _model = BeetleObject

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E0162_CHEST_GRANT_BEETLEMANIA)])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E0161_NPC_QUEST_GRANT_BEETLEMANIA)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3109_FREESTANDING_BEETLEMANIA_GRANT)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3395_MIDAS_CAVE_BEETLEMANIA_GRANTER)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E0218_HILL_BEETLEMANIA)])


class ShoesPrize(WeddingGearPrize, KeyPrize):
    item = ShoesItem
    _nickname = TreasureHunterNickname(
        nickname="Ruby Slippers", description="Do you think they'll take you\n home?"
    )
    _model = ShoesObject

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3943_SHOES_CHEST)])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3931_GET_SHOES)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3935_FREESTANDING_SHOES)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3939_RIVER_SHOES)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript(
            [
                Inc(WEDDING_GEAR_COUNTER),
                SetVarToConst(ITEM_ID, ShoesItem),
                JmpToEvent(E0215_HILL_ITEM),
            ]
        )


class BroochPrize(WeddingGearPrize, KeyPrize):
    item = BroochItem
    _nickname = TreasureHunterNickname(
        nickname="Shiny Brooch", description="It looks pretty stylish."
    )
    _model = BroochObject

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3944_BROOCH_CHEST)])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3932_GET_BROOCH)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3936_FREESTANDING_BROOCH)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3940_RIVER_BROOCH)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript(
            [
                Inc(WEDDING_GEAR_COUNTER),
                SetVarToConst(ITEM_ID, BroochItem),
                JmpToEvent(E0215_HILL_ITEM),
            ]
        )


class RingPrize(WeddingGearPrize, KeyPrize):
    item = RingItem
    _nickname = TreasureHunterNickname(
        nickname="Wedding Ring", description="For that special someone!"
    )
    _model = RingObject

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3945_RING_CHEST)])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3933_GET_RING)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3937_FREESTANDING_RING)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3941_RIVER_RING)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript(
            [
                Inc(WEDDING_GEAR_COUNTER),
                SetVarToConst(ITEM_ID, RingItem),
                JmpToEvent(E0215_HILL_ITEM),
            ]
        )


class CrownPrize(WeddingGearPrize, KeyPrize):
    item = CrownItem
    _nickname = TreasureHunterNickname(
        nickname="Gold Crown", description="It looks pretty important!"
    )
    _model = CrownObject

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3946_CROWN_CHEST)])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3934_GET_CROWN)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3938_FREESTANDING_CROWN)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3942_RIVER_CROWN)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript(
            [
                Inc(WEDDING_GEAR_COUNTER),
                SetVarToConst(ITEM_ID, CrownItem),
                JmpToEvent(E0215_HILL_ITEM),
            ]
        )


class GoldPaintPrize(ItemPrize, KeyPrize):
    item = GoldPaintItem
    _nickname = TreasureHunterNickname(
        nickname="Chrome Coat", description="It'll make you look shiny!"
    )
    _model = YellowJuiceObject


class RecoveryMushroomPrize(StandardPrize):
    _model = RecoveryMushroomObject
    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, 0),
                JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST),
            ]
        )

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E0397_HEAL_IN_TOADSTOOLS_ROOM)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E2822_ASYNC_NO_ANIMATION_MUSHROOM)])


class YouMissed(StandardPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3081_YOU_MISSED)])


class Nothing(YouMissed):
    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E0256_RETURN)])


class InfiniteCoinsPrize(StandardPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [SetVarToConst(ITEM_ID, 240), JmpToEvent(E3074_COIN_CHEST_MULTI_HIT_1)]
        )


class Coins1Prize(CoinQuantityPrize):
    _amount: int = 1

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E1293_COLLECT_FREESTANDING_SMALL_COIN)])


class Coins5Prize(CoinQuantityPrize):
    _amount = 5


class Coins8Prize(CoinQuantityPrize):
    _amount = 8


class Coins10Prize(CoinQuantityPrize):
    _amount: int = 10

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3146_FREESTANDING_BIG_COIN)])


class Coins20Prize(CoinQuantityPrize):
    _amount = 20


class Coins50Prize(CoinQuantityPrize):
    _amount = 50


class Coins100Prize(CoinQuantityPrize):
    _amount = 100


class Coins150Prize(CoinQuantityPrize):
    _amount = 150


class FirstMimicFightLauncher(MimicFightInitiatorPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3124_MIMIC_1_CHEST)])


class SecondMimicFightLauncher(MimicFightInitiatorPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3126_MIMIC_2_CHEST)])


class ThirdMimicFightLauncher(MimicFightInitiatorPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E2493_MIMIC_3)])


class FrogCoin1Prize(FrogCoinQuantityPrize):
    _amount = 1

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3238_FREESTANDING_FROG_COIN)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E2816_ASYNC_NO_ANIMATION_FROG_COIN)])


class FrogCoin2Prize(FrogCoinQuantityPrize):
    _amount = 2


class FrogCoin3Prize(FrogCoinQuantityPrize):
    _amount = 3


class FrogCoin10Prize(FrogCoinQuantityPrize):
    _amount = 10


class FrogCoin20Prize(FrogCoinQuantityPrize):
    _amount = 20


class BanditsWayStarPrize(EXPStarPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, 16),
                JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST),
            ]
        )


class KeroSewersStarPrize(EXPStarPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, 16 + 1),
                JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST),
            ]
        )


class MolevilleMinesStarPrize(EXPStarPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, 16 + 2),
                JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST),
            ]
        )


class SeaStarPrize(EXPStarPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, 16 + 3),
                JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST),
            ]
        )


class LandsEndVolcanoStarPrize(EXPStarPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, 16 + 5),
                JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST),
            ]
        )


class NimbusLandStarPrize(EXPStarPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, 16 + 7),
                JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST),
            ]
        )


class LandsEndStar2Prize(EXPStarPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, 16 + 8),
                JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST),
            ]
        )


class LandsEndStar3Prize(EXPStarPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, 16 + 9),
                JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST),
            ]
        )


# Star pieces


class StarPiece1(StarPiecePrize):
    _hint = SIGNAL_RING_STAR_PIECE_1


class StarPiece2(StarPiecePrize):
    _hint = SIGNAL_RING_STAR_PIECE_2


class StarPiece3(StarPiecePrize):
    _hint = SIGNAL_RING_STAR_PIECE_3


class StarPiece4(StarPiecePrize):
    _hint = SIGNAL_RING_STAR_PIECE_4


class StarPiece5(StarPiecePrize):
    _hint = SIGNAL_RING_STAR_PIECE_5


class StarPiece6(StarPiecePrize):
    _hint = SIGNAL_RING_STAR_PIECE_6


class StarPiece7(StarPiecePrize):
    _hint = SIGNAL_RING_STAR_PIECE_7


# Spells


class JumpSpellPrize(SpellPrize):
    _spell = JumpSpell


class FireOrbSpellPrize(SpellPrize):
    _spell = FireOrbSpell


class SuperJumpSpellPrize(SpellPrize):
    _spell = SuperJumpSpell


class SuperFlameSpellPrize(SpellPrize):
    _spell = SuperFlameSpell


class UltraJumpSpellPrize(SpellPrize):
    _spell = UltraJumpSpell


class UltraFlameSpellPrize(SpellPrize):
    _spell = UltraFlameSpell


class ThunderboltSpellPrize(SpellPrize):
    _spell = ThunderboltSpell


class HPRainSpellPrize(SpellPrize):
    _spell = HPRainSpell


class PsychopathSpellPrize(SpellPrize):
    _spell = PsychopathSpell


class ShockerSpellPrize(SpellPrize):
    _spell = ShockerSpell


class SnowyPrize(SpellPrize):
    _spell = SnowySpell


class StarRainSpellPrize(SpellPrize):
    _spell = StarRainSpell


class GenoBeamSpellPrize(SpellPrize):
    _spell = GenoBeamSpell


class GenoBoostSpellPrize(SpellPrize):
    _spell = GenoBoostSpell


class GenoWhirlSpellPrize(SpellPrize):
    _spell = GenoWhirlSpell


class GenoBlastSpellPrize(SpellPrize):
    _spell = GenoBlastSpell


class GenoFlashSpellPrize(SpellPrize):
    _spell = GenoFlashSpell


class TerrorizeSpellPrize(SpellPrize):
    _spell = TerrorizeSpell


class PoisonGasSpellPrize(SpellPrize):
    _spell = PoisonGasSpell


class CrusherSpellPrize(SpellPrize):
    _spell = CrusherSpell


class BowserCrushSpellPrize(SpellPrize):
    _spell = BowserCrushSpell


class TherapySpellPrize(SpellPrize):
    _spell = TherapySpell


class GroupHugSpellPrize(SpellPrize):
    _spell = GroupHugSpell


class MuteSpellPrize(SpellPrize):
    _spell = MuteSpell


class SleepyTimeSpellPrize(SpellPrize):
    _spell = SleepyTimeSpell


class ComeBackSpellPrize(SpellPrize):
    _spell = ComeBackSpell


class PsychBombSpellPrize(SpellPrize):
    _spell = PsychBombSpell


# Characters
class MarioRecruitmentPrize(CharacterPrize):
    _ally = MARIO_Ally

    def recruit(self, world: GameWorld, show_dialog: bool = False) -> EventScript:
        output: list[UsableEventScriptCommand] = [CharacterJoinsParty(MARIO)]
        if show_dialog:
            output.append(
                RunDialog(
                    dialog_id=DI1179_MARIO_JOINS,
                    above_object=BOWSER,
                    closable=True,
                    sync=False,
                    multiline=False,
                    use_background=False,
                )
            )
        if world.settings.is_flag_value(
            _gf("BoosterTowerGate"), _gf("BoosterTowerGating").MARIO
        ):
            output.append(SetBit(TOWER_CHARACTER_RECRUITED))
            # TODO: generate tower door animation
        output.append(Return())
        return EventScript(output)


class MallowRecruitmentPrize(CharacterPrize):
    _ally = MALLOW_Ally

    def recruit(self, world: GameWorld, show_dialog: bool = False) -> EventScript:
        output: list[UsableEventScriptCommand] = [CharacterJoinsParty(MALLOW)]
        if world.settings.is_flag_value(
            _gf("BanditsWayGate"), _gf("BanditsWayGating").MALLOW
        ):
            output.extend(
                [
                    SetBit(MAP_BANDITS_WAY),
                    SetBit(MAP_DIRECTIONAL_MUSHROOM_KINGDOM_BANDITS_WAY),
                ]
            )
        if world.settings.is_flag_value(
            _gf("KeroSewersGate"), _gf("KeroSewersGating").MALLOW
        ):
            output.extend(
                [
                    ClearBit(SEWERS_CLOSED),
                ]
            )
        if show_dialog:
            output.append(
                RunDialog(
                    dialog_id=DI1180_MALLOW_JOINS,
                    above_object=BOWSER,
                    closable=True,
                    sync=False,
                    multiline=False,
                    use_background=False,
                )
            )
        if world.settings.is_flag_value(
            _gf("BoosterTowerGate"), _gf("BoosterTowerGating").MALLOW
        ):
            output.append(SetBit(TOWER_CHARACTER_RECRUITED))
        output.append(Return())
        return EventScript(output)


class GenoRecruitmentPrize(CharacterPrize):
    _ally = GENO_Ally

    def recruit(self, world: GameWorld, show_dialog: bool = False) -> EventScript:
        output: list[UsableEventScriptCommand] = [CharacterJoinsParty(GENO)]
        if world.settings.is_flag_value(
            _gf("PipeVaultGate"), _gf("PipeVaultGating").GENO
        ):
            output.extend(
                [
                    ClearBit(PIPE_VAULT_GATED),
                ]
            )
        if world.settings.is_flag_value(
            _gf("Moleville1Gate"), _gf("Moleville1Gating").GENO
        ):
            output.extend(
                [
                    ClearBit(MOLEVILLE_MINES_ENTRANCE_GATING),
                ]
            )
        if show_dialog:
            output.append(
                RunDialog(
                    dialog_id=DI1181_GENO_JOINS,
                    above_object=BOWSER,
                    closable=True,
                    sync=False,
                    multiline=False,
                    use_background=False,
                )
            )
        if world.settings.is_flag_value(
            _gf("BoosterTowerGate"), _gf("BoosterTowerGating").GENO
        ):
            output.append(SetBit(TOWER_CHARACTER_RECRUITED))
        output.append(Return())
        return EventScript(output)


class BowserRecruitmentPrize(CharacterPrize):
    _ally = BOWSER_Ally

    def recruit(self, world: GameWorld, show_dialog: bool = False) -> EventScript:
        output: list[UsableEventScriptCommand] = [CharacterJoinsParty(BOWSER)]
        if show_dialog:
            output.append(
                RunDialog(
                    dialog_id=DI1182_BOWSER_JOINS,
                    above_object=BOWSER,
                    closable=True,
                    sync=False,
                    multiline=False,
                    use_background=False,
                )
            )
        if world.settings.is_flag_value(
            _gf("BoosterTowerGate"), _gf("BoosterTowerGating").BOWSER
        ):
            output.append(SetBit(TOWER_CHARACTER_RECRUITED))
        output.append(Return())
        return EventScript(output)


class ToadstoolRecruitmentPrize(CharacterPrize):
    _ally = TOADSTOOL_Ally

    def recruit(self, world: GameWorld, show_dialog: bool = False) -> EventScript:
        output: list[UsableEventScriptCommand] = [CharacterJoinsParty(TOADSTOOL)]
        if world.settings.is_flag_value(_gf("SeaGate"), _gf("SeaGating").TOADSTOOL):
            output.extend(
                [
                    SetBit(MAP_SEA),
                    SetBit(MAP_DIRECTIONAL_SEASIDE_DOWN_SEA),
                ]
            )
        if show_dialog:
            output.append(
                RunDialog(
                    dialog_id=DI1183_TOADSTOOL_JOINS,
                    above_object=BOWSER,
                    closable=True,
                    sync=False,
                    multiline=False,
                    use_background=False,
                )
            )
        if world.settings.is_flag_value(
            _gf("BoosterTowerGate"), _gf("BoosterTowerGating").TOADSTOOL
        ):
            output.append(SetBit(TOWER_CHARACTER_RECRUITED))
        output.append(Return())
        return EventScript(output)


# Boss fights


class HammerBrosFight(BossFightPrize):
    _text = "Hammer Bros."
    _members = [
        FormationMember(HAMMERBROEnemy, 135, 127),
        FormationMember(HAMMERBROEnemy, 199, 143),
    ]

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            _gf("BanditsWayGate"), _gf("BanditsWayGating").HAMMER_BRO
        ):
            output.extend(
                [
                    SetBit(MAP_BANDITS_WAY),
                    SetBit(MAP_DIRECTIONAL_MUSHROOM_KINGDOM_BANDITS_WAY),
                ]
            )
        return EventScript(output)


class Croco1BossFight(BossFightPrize):
    _text = "Croco 1"
    _members = [
        FormationMember(CROCO1Enemy, 183, 127),
    ]


class MackBossFight(BossFightPrize):
    _text = "Mack"
    _members = [
        FormationMember(MACKEnemy, 183, 127),
    ]

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            _gf("KeroSewersGate"), _gf("KeroSewersGating").MACK
        ):
            output.extend([ClearBit(SEWERS_CLOSED)])
        return EventScript(output)


class PandoriteBossFight(BossFightPrize):
    _text = "Pandorite"
    _members = [
        FormationMember(PANDORITEEnemy, 183, 127),
    ]


class Belome1BossFight(BossFightPrize):
    _text = "Belome 1"
    _members = [
        FormationMember(BELOME1Enemy, 183, 127),
    ]


class BowyerBossFight(BossFightPrize):
    _text = "Bowyer"
    _members = [
        FormationMember(BOWYEREnemy, 183, 127),
    ]
    _force_start_event = BE0014_SET_7EE00A_TO_PARTY_SIZE_AT_START_OF_FIGHT

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            _gf("PipeVaultGate"), _gf("PipeVaultGating").BOWYER
        ):
            output.extend(
                [
                    ClearBit(PIPE_VAULT_GATED),
                ]
            )
        if world.settings.is_flag_value(
            _gf("Moleville1Gate"), _gf("Moleville1Gating").BOWYER
        ):
            output.extend(
                [
                    ClearBit(MOLEVILLE_MINES_ENTRANCE_GATING),
                ]
            )
        return EventScript(output)


class Croco2BossFight(BossFightPrize):
    _text = "Croco 2"
    _members = [
        FormationMember(CROCO2Enemy, 183, 127),
    ]


class PunchinelloBossFight(BossFightPrize):
    _text = "Punchinello 1"
    _members = [
        FormationMember(PUNCHINELLOEnemy, 199, 119),
        FormationMember(MICROBOMBEnemy, 135, 119, hidden_at_start=True),
        FormationMember(MICROBOMBEnemy, 151, 135, hidden_at_start=True),
        FormationMember(MICROBOMBEnemy, 183, 151, hidden_at_start=True),
        FormationMember(MICROBOMBEnemy, 215, 159, hidden_at_start=True),
    ]

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            _gf("BoosterTowerGate"), _gf("BoosterTowerGating").PUNCHINELLO
        ):
            output.extend(
                [
                    ApplySolidityModToLevel(
                        permanent=True, room_id=R202_BOOSTER_TOWER_ENTRANCE, mod_id=0
                    ),
                    ApplyTileModToLevel(
                        use_alternate=True,
                        room_id=R202_BOOSTER_TOWER_ENTRANCE,
                        mod_id=32,
                    ),
                    SetBit(TOWER_OPENED),
                ]
            )
        return EventScript(output)


class BoosterBossFight(BossFightPrize):
    _text = "Booster 1"
    _force_start_event = BE0012_DIALOGUE_FROM_BOOSTER_FIGHT
    _members = [
        FormationMember(BOOSTEREnemy, 183, 127),
        FormationMember(SNIFITEnemyHenchman, 135, 119),
        FormationMember(SNIFITEnemyHenchman, 151, 143),
        FormationMember(SNIFITEnemyHenchman, 199, 151),
    ]


class KnifeGuyGrateGuyBossFight(BossFightPrize):
    _text = "Knife Guy & Grate Guy"
    _members = [
        FormationMember(KNIFEGUYEnemy, 151, 119),
        FormationMember(GRATEGUYEnemy, 199, 143),
    ]

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            _gf("BoosterHillGate"), _gf("BoosterHillGating").KGGG
        ):
            output.extend([ClearBit(BOOSTER_HILL_CLOSED)])
        if world.settings.is_flag_value(
            _gf("MarrymoreGate"), _gf("MarrymoreGating").KGGG
        ):
            output.extend([SetBit(MARRYMORE_BACKDOOR_OPEN)])
        return EventScript(output)


class BundtBossFight(BossFightPrize):
    _text = "Bundt 1"
    _members = [
        FormationMember(BUNDTEnemy, 199, 127),
        FormationMember(RASPBERRYEnemy, 199, 119),
        FormationMember(TORTEEnemy, 199, 151),
        FormationMember(TORTEEnemy, 135, 119),
    ]

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(_gf("SeaGate"), _gf("SeaGating").BUNDT):
            output.extend(
                [
                    SetBit(MAP_SEA),
                    SetBit(MAP_DIRECTIONAL_SEASIDE_DOWN_SEA),
                ]
            )
        return EventScript(output)


class KingCalamariBossFight(BossFightPrize):
    _text = "King Calamari"
    _members = [
        FormationMember(KINGCALAMARIEnemy, 222, 94, hidden_at_start=True),
        FormationMember(TENTACLESEnemy2, 136, 115, hidden_at_start=True),
        FormationMember(TENTACLESEnemy2, 112, 127, hidden_at_start=True),
        FormationMember(TENTACLESEnemy, 193, 143, hidden_at_start=True),
        FormationMember(TENTACLESEnemy, 168, 156, hidden_at_start=True),
        FormationMember(TENTACLESEnemy, 135, 143, hidden_at_start=True),
    ]
    _force_start_event = BE0026_INTRO_SCENE_TENTACLES_RISE_FROM_HOLES
    _force_battlefield = BF03_SUNKEN_SHIP_KING_CALAMARIS_CELLAR


class HidonBossFight(BossFightPrize):
    _text = "Hidon"
    _members = [
        FormationMember(HIDONEnemy, 167, 119),
        FormationMember(GOOMBETTEEnemy, 135, 111, hidden_at_start=True),
        FormationMember(GOOMBETTEEnemy, 135, 135, hidden_at_start=True),
        FormationMember(GOOMBETTEEnemy, 167, 151, hidden_at_start=True),
        FormationMember(GOOMBETTEEnemy, 215, 151, hidden_at_start=True),
    ]


class JohnnyBossFight(BossFightPrize):
    _text = "Johnny 1"
    _members = [
        FormationMember(JOHNNYEnemy, 183, 127),
        FormationMember(BANDANABLUEEnemy, 135, 111),
        FormationMember(BANDANABLUEEnemy, 135, 135),
        FormationMember(BANDANABLUEEnemy, 183, 159),
        FormationMember(BANDANABLUEEnemy, 215, 151),
        FormationMember(WATERCRYSTALEnemy, 0, 0, hidden_at_start=True),
        FormationMember(WATERCRYSTALEnemy, 0, 0, hidden_at_start=True),
    ]

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            _gf("YaridovichGate"), _gf("YaridovichGating").JOHNNY
        ):
            output.extend([SetBit(SEASIDE_BOSS_AVAILABLE)])
        return EventScript(output)


class YaridovichBossFight(BossFightPrize):
    _text = "Yaridovich"
    _members = [
        FormationMember(YARIDOVICHEnemy, 183, 127),
        FormationMember(YARIDOVICHMirageEnemy, 183, 127, hidden_at_start=True),
    ]

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            _gf("LandsEndGate"), _gf("LandsEndGating").YARIDOVICH
        ):
            output.extend([ClearBit(LANDS_END_GATED)])
        return EventScript(output)


class MokuraBossFight(BossFightPrize):
    _text = "Mokura"
    _members = [
        FormationMember(FORMLESSEnemy, 167, 135),
        FormationMember(MOKURAEnemy, 167, 135, hidden_at_start=True),
    ]


class Belome2BossFight(BossFightPrize):
    _text = "Belome 2"
    _members = [
        FormationMember(BELOME2Enemy, 183, 127),
        FormationMember(MARIOCLONEEnemy, 135, 119, hidden_at_start=True),
        FormationMember(TOADSTOOL2Enemy, 215, 159, hidden_at_start=True),
    ]

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            _gf("MonstroTownGate"), _gf("MonstroTownGating").BELOME_2
        ):
            output.extend(
                [
                    RemoveObjectFromSpecificLevel(
                        NPC_3, R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN
                    ),
                    SetBit(MAP_DIRECTIONAL_LANDS_END_MONSTRO_TOWN),
                    SetBit(MAP_MONSTRO_TOWN),
                ]
            )
        return EventScript(output)


class JaggerBossFight(BossFightPrize):
    _text = "Jagger"
    _members = [
        FormationMember(JAGGEREnemy, 183, 127),
    ]


class Jinx1BossFight(BossFightPrize):
    _text = "Jinx 1"
    _members = [
        FormationMember(JINX1Enemy, 183, 127),
    ]
    _force_start_event = BE0071_JINX_USES_TRIPLE_KICK


class Jinx2BossFight(BossFightPrize):
    _text = "Jinx 2"
    _members = [
        FormationMember(JINX2Enemy, 183, 127),
    ]
    _force_start_event = BE0072_JINX_USES_QUICKSILVER


class Jinx3BossFight(BossFightPrize):
    _text = "Jinx 3"
    _members = [
        FormationMember(JINX3Enemy, 183, 127),
    ]
    _force_start_event = BE0073_JINX_USES_BOMBS_AWAY


class CulexBossFight(BossFightPrize):
    _text = "Culex 1"
    _members = [
        FormationMember(CULEXEnemy, 183, 103),
        FormationMember(FIRECRYSTALEnemy, 135, 103, hidden_at_start=True),
        FormationMember(WATERCRYSTALEnemy, 151, 119, hidden_at_start=True),
        FormationMember(EARTHCRYSTALEnemy, 183, 135, hidden_at_start=True),
        FormationMember(WINDCRYSTALEnemy, 215, 143, hidden_at_start=True),
    ]


class BoxBoyBossFight(BossFightPrize):
    _text = "Box Boy"
    _members = [
        FormationMember(BOXBOYEnemy, 183, 127),
        FormationMember(FAUTSOEnemy, 151, 111, hidden_at_start=True),
    ]


class MegasmilaxBossFight(BossFightPrize):
    _text = "Megasmilax"
    _members = [
        FormationMember(SMILAXEnemy, 180, 157),
        FormationMember(SMILAXEnemy, 164, 175, hidden_at_start=True),
        FormationMember(SMILAXEnemy, 143, 119, hidden_at_start=True),
        FormationMember(SMILAXEnemy, 207, 151, hidden_at_start=True),
        FormationMember(SMILAXEnemy, 191, 127, hidden_at_start=True),
        FormationMember(MEGASMILAXEnemy, 175, 111, hidden_at_start=True),
    ]
    _force_start_event = BE0058_THRAX_IS_THERE

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            _gf("NimbusGate"), _gf("NimbusGating").MEGASMILAX
        ):
            output.extend(
                [
                    SetBit(NIMBUS_MAINLAND_UNLOCKED),
                    RemoveObjectFromSpecificLevel(
                        NPC_2, R369_NIMBUS_LAND_ENTRANCE_WWARP_TRAMPOLINE
                    ),
                ]
            )
        return EventScript(output)


class DodoBossFight(BossFightPrize):
    _text = "Dodo"
    _members = [
        FormationMember(DODOEnemySolo, 183, 127),
    ]


class BirdettaBossFight(BossFightPrize):
    _text = "Birdo"
    _members = [
        FormationMember(BIRDETTAEnemy, 167, 118, hidden_at_start=True),
        FormationMember(SHELLYEnemy, 171, 103),
        FormationMember(EGGBERTEnemy, 135, 119, hidden_at_start=True),
        FormationMember(EGGBERTEnemy, 135, 135, hidden_at_start=True),
        FormationMember(EGGBERTEnemy, 167, 151, hidden_at_start=True),
        FormationMember(EGGBERTEnemy, 199, 151, hidden_at_start=True),
    ]
    _force_battlefield = BF23_NIMBUS_CASTLE_BIRDOS_ROOM


class ValentinaBossFight(BossFightPrize):
    _text = "Valentina"
    _members = [
        FormationMember(VALENTINAEnemy, 183, 127),
        FormationMember(DODOEnemy, 199, 151, hidden_at_start=True),
    ]

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            _gf("BarrelVolcanoGate"), _gf("BarrelVolcanoGating").VALENTINA
        ):
            output.extend(
                [
                    SetBit(MAP_DIRECTIONAL_NIMBUS_LAND_BARREL_VOLCANO),
                    SetBit(MAP_BARREL_VOLCANO),
                ]
            )
        return EventScript(output)


class CzarDragonBossFight(BossFightPrize):
    _text = "Czar Dragon"
    _members = [
        FormationMember(CZARDRAGONEnemy, 183, 143),
        FormationMember(ZOMBONEEnemy, 183, 143, hidden_at_start=True),
        FormationMember(HELIOEnemy, 167, 119, hidden_at_start=True),
        FormationMember(HELIOEnemy, 135, 135, hidden_at_start=True),
        FormationMember(HELIOEnemy, 199, 167, hidden_at_start=True),
        FormationMember(HELIOEnemy, 231, 151, hidden_at_start=True),
    ]


class AxemRangersBossFight(BossFightPrize):
    _text = "Axem Rangers"
    _members = [
        FormationMember(AXEMRANGERSEnemy, 201, 79),
        FormationMember(AXEMREDEnemy, 135, 111, hidden_at_start=True),
        FormationMember(AXEMBLACKEnemy, 135, 127, hidden_at_start=True),
        FormationMember(AXEMPINKEnemy, 151, 143, hidden_at_start=True),
        FormationMember(AXEMGREENEnemy, 183, 151, hidden_at_start=True),
        FormationMember(AXEMYELLOWEnemy, 215, 151, hidden_at_start=True),
    ]
    _force_start_event = BE0061_ONLY_MARIO_IS_THERE
    _force_battlefield = BF39_BLADE_AXEM_RANGERS

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            _gf("BowsersKeepGate"), _gf("BowsersKeepGating").AXEM
        ):
            output.extend(
                [
                    SetBit(MAP_VISTA_HILL),
                    ClearBit(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL),
                ]
            )
            if world.settings.is_flag_value(
                _gf("FactoryGate"), _gf("FactoryGating").OPEN
            ):
                output.extend(
                    [
                        SetBit(MAP_GATE),
                        SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE),
                    ]
                )
        return EventScript(output)


class ChesterBossFight(BossFightPrize):
    _text = "Chester"
    _members = [
        FormationMember(CHESTEREnemy, 183, 127),
        FormationMember(BAHAMUTTEnemy, 135, 119, hidden_at_start=True),
    ]


class KamekBossFight(BossFightPrize):
    _text = "Magikoopa"
    _members = [
        FormationMember(KAMEKEnemy, 215, 111),
        FormationMember(TERRAPINEnemy, 167, 135, hidden_at_start=True),
    ]
    _force_start_event = BE0101_MAGIKOOPA_IS_THERE


class BoomerBossFight(BossFightPrize):
    _text = "Boomer"
    _members = [
        FormationMember(BOOMEREnemy, 215, 143),
        FormationMember(HANGINSHYEnemy, 66, 115),
        FormationMember(HANGINSHYEnemy, 186, 74),
    ]
    _force_battlefield = BF29_BOWSERS_KEEP_CHANDELIERS


class ExorBossFight(BossFightPrize):
    _text = "Exor"
    _members = [
        FormationMember(EXOREnemy, 193, 64),
        FormationMember(NEOSQUIDEnemy, 187, 136),
        FormationMember(RIGHTEYEEnemy, 174, 145, hidden_at_start=True),
        FormationMember(LEFTEYEEnemy, 203, 157, hidden_at_start=True),
    ]
    _force_start_event = BE0080_EXOR_FIGHT_BEGINS
    _force_battlefield = BF16_BOWSERS_KEEP_TURRET_EXOR

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(_gf("FactoryGate"), _gf("FactoryGating").EXOR):
            output.extend(
                [
                    SetBit(MAP_GATE),
                    SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE),
                ]
            )

        return EventScript(output)


class CountdownBossFight(BossFightPrize):
    _text = "Count Down"
    _members = [
        FormationMember(COUNTDOWNEnemy, 150, 93),
        FormationMember(DINGALINGEnemy, 158, 52),
        FormationMember(DINGALINGEnemy, 194, 67),
    ]
    _force_battlefield = BF18_SMITHY_FACTORY_COUNT_DOWNS_PAD


class CloakerDominoBossFight(BossFightPrize):
    _text = "Cloaker & Domino"
    _members = [
        FormationMember(CLOAKEREnemy, 151, 111),
        FormationMember(DOMINOEnemy, 215, 159),
        FormationMember(MADADDEREnemy, 167, 135, hidden_at_start=True),
    ]
    _force_battlefield = BF40_SMITHY_FACTORY_DOMINO_CLOAKERS_PAD
    _force_start_event = BE0052_INTRO_SCENE_DOMINO_CLOAKER_S_INTRODUCTION


class ClerkBossFight(BossFightPrize):
    _text = "Clerk"
    _members = [
        FormationMember(CLERKEnemy, 199, 119),
        FormationMember(MADMALLETEnemyHenchman, 135, 119),
        FormationMember(MADMALLETEnemyHenchman, 199, 151),
    ]


class ManagerBossFight(BossFightPrize):
    _text = "Manager"
    _members = [
        FormationMember(MANAGEREnemy, 199, 119),
        FormationMember(POUNDEREnemyHenchman, 151, 111),
        FormationMember(POUNDEREnemyHenchman, 167, 135),
        FormationMember(POUNDEREnemyHenchman, 215, 143),
    ]


class DirectorBossFight(BossFightPrize):
    _text = "Director"
    _members = [
        FormationMember(DIRECTOREnemy, 183, 127),
        FormationMember(POUNDETTEEnemyHenchman, 135, 119),
        FormationMember(POUNDETTEEnemyHenchman, 167, 103),
        FormationMember(POUNDETTEEnemyHenchman, 199, 151),
        FormationMember(POUNDETTEEnemyHenchman, 231, 135),
    ]


class GunyolkBossFight(BossFightPrize):
    _text = "Gunyolk"
    _members = [
        FormationMember(GUNYOLKEnemy, 199, 103),
        FormationMember(FACTORYCHIEFEnemy, 231, 151),
    ]


class SmithyBossFight(BossFightPrize):
    _text = "Smithy"
    _members = [
        FormationMember(SMITHY1Enemy, 199, 127),
        FormationMember(SMELTEREnemy, 87, 87),
        FormationMember(MACHINEMADEBodyguardEnemy, 135, 127, hidden_at_start=True),
        FormationMember(MACHINEMADEBodyguardEnemy, 199, 159, hidden_at_start=True),
    ]


class Punchinello2BossFight(BossFightPrize):
    _text = "Punchinello 2"
    _members = [
        FormationMember(PUNCHINELLO2Enemy, 188, 116),
        FormationMember(STRONGBOBOMB3Enemy, 145, 103, hidden_at_start=True),
        FormationMember(STRONGBOBOMB1Enemy, 150, 129, hidden_at_start=True),
        FormationMember(STRONGBOBOMB4Enemy, 182, 142, hidden_at_start=True),
        FormationMember(STRONGBOBOMB2Enemy, 223, 142, hidden_at_start=True),
    ]


class Booster2BossFight(BossFightPrize):
    _text = "Booster 2"
    _members = [
        FormationMember(BOOSTEREnemy2, 184, 116),
        FormationMember(SNIFIT2Enemy, 156, 132),
        FormationMember(SNIFIT2Enemy, 143, 104),
        FormationMember(SNIFIT2Enemy, 212, 138),
        FormationMember(BOOSTERDUMMY, 0, 0),
    ]


class Bundt2BossFight(BossFightPrize):
    _text = "Bundt 2"
    _members = [
        FormationMember(BUNDT2Enemy, 199, 127),
        FormationMember(RASPBERRY2Enemy, 199, 119),
        FormationMember(TORTE2Enemy, 199, 151),
        FormationMember(TORTE2Enemy, 135, 119),
        FormationMember(CANDLEEnemy, 0, 0),
    ]
    _force_start_event = BE0017_BEGIN_BUNDT_POSTGAME


class Johnny2Fight(BossFightPrize):
    _text = "Johnny 2"
    _members = [
        FormationMember(JOHNNYEnemy2, 165, 121),
    ]


class Belome3Dight(BossFightPrize):
    _text = "Belome 3"
    _members = [
        FormationMember(BELOMEEnemy3, 183, 127),
        FormationMember(MARIOCLONESEnemy, 135, 119, hidden_at_start=True),
        FormationMember(TOADSTOOL3Enemy, 215, 159, hidden_at_start=True),
    ]


class Jinx4BossFight(BossFightPrize):
    _text = "Jinx 4"
    _members = [
        FormationMember(JINXEnemy4, 181, 122),
        FormationMember(TeamGaugeEnemy, 36, 200),
    ]


class Culex3DBossFight(BossFightPrize):
    _text = "Culex 2"
    _members = [
        FormationMember(CULEX3DEnemy, 183, 103),
        FormationMember(FIRECRYS3DEnemy, 135, 103, hidden_at_start=True),
        FormationMember(FIRECRYS3DEnemy, 151, 119, hidden_at_start=True),
        FormationMember(FIRECRYS3DEnemy, 183, 135, hidden_at_start=True),
        FormationMember(FIRECRYS3DEnemy, 215, 143, hidden_at_start=True),
    ]
    _force_start_event = BE0077_CULEX_3D


# Collection of all BossFightPrize subclasses for the ShuffledBosses flag
ALL_BOSS_FIGHTS: list[type[BossFightPrize]] = [
    # Standard bosses
    HammerBrosFight,
    Croco1BossFight,
    MackBossFight,
    PandoriteBossFight,
    Belome1BossFight,
    BowyerBossFight,
    Croco2BossFight,
    PunchinelloBossFight,
    BoosterBossFight,
    KnifeGuyGrateGuyBossFight,
    BundtBossFight,
    KingCalamariBossFight,
    HidonBossFight,
    JohnnyBossFight,
    YaridovichBossFight,
    Belome2BossFight,
    JaggerBossFight,
    Jinx1BossFight,
    Jinx2BossFight,
    Jinx3BossFight,
    CulexBossFight,
    BoxBoyBossFight,
    MegasmilaxBossFight,
    DodoBossFight,
    BirdettaBossFight,
    ValentinaBossFight,
    CzarDragonBossFight,
    AxemRangersBossFight,
    ChesterBossFight,
    KamekBossFight,
    BoomerBossFight,
    ExorBossFight,
    CountdownBossFight,
    CloakerDominoBossFight,
    ClerkBossFight,
    ManagerBossFight,
    DirectorBossFight,
    GunyolkBossFight,
    SmithyBossFight,
    # Remake bosses
    Punchinello2BossFight,
    Booster2BossFight,
    Bundt2BossFight,
    Johnny2Fight,
    Belome3Dight,
    Jinx4BossFight,
    Culex3DBossFight,
]
