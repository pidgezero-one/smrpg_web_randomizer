"""Item and prize shuffling logic."""

from __future__ import annotations
import random
from copy import copy
from typing import TYPE_CHECKING, cast

from randomizer.types.logic import Inventory
from smrpgpatchbuilder.datatypes.spells.enums import Status, Element

from data.items import (
    AbleJuiceItem,
    FroggieDrinkItem,
    HoneySyrupItem,
    MoldyMushItem,
    MushroomItem,
    MushroomItem2,
    PureWaterItem,
    RottenMushItem,
    WiltShroomItem,
    YoshiCookieItem,
)
from randomizer.types.prizelocation import StandingLocation, TreasureShopLocation
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    NPC_2,
    NPC_3,
    NPC_4,
    NPC_5,
    NPC_6,
    NPC_7,
)

from ...types.gameworld import CookiesPrize, MarioDollPrize
from ...data.rooms.npcs import EMPTY_NPC

from ..placement import PlacementException, place
from ...types.prize import (
    CharacterPrize,
    CoinQuantityPrize,
    ItemPrize,
    RandomPrizeSubstitute,
    CoinPrize,
    FPFlowerPrize,
    FrogCoinPrize,
)
from ...progression.prizes import (
    BanditsWayStarPrize,
    BowserRecruitmentPrize,
    FryingPanPrize,
    GenoRecruitmentPrize,
    MallowRecruitmentPrize,
    MarioRecruitmentPrize,
    RecoveryMushroomPrize,
    FrogCoin1Prize,
    KeroSewersStarPrize,
    MolevilleMinesStarPrize,
    SeaStarPrize,
    LandsEndVolcanoStarPrize,
    LandsEndVolcanoStarPrize,
    NimbusLandStarPrize,
    LandsEndStar2Prize,
    LandsEndStar3Prize,
    ToadstoolRecruitmentPrize,
)
from ...progression.prizelocations import (
    MushroomKingdomInnPurchaseLocation,
    ShipCoinSnakePuzzleLocation,
    MonstroFirstSuperJumpRewardLocation,
    MonstroSecondSuperJumpRewardLocation,
)
from ...types.flags import (
    ReplaceItems,
    ShuffleHillFlowers,
    ShuffleItems,
    ShuffleShops,
    Remake,
    RestrictSpecialEquips,
    SuperJump2Threshold,
    NoStarEgg,
    ItemQuality,
    ItemQualityOptions,
    FireworksSetting,
    FireworksOptions,
    ShuffleCharacters,
    StartingCharacters,
    AvailableCharacters,
    MaxCharacters,
    CharacterLearnedSpells,
    AvailableSpells,
    ShuffleStarPieces,
    TotalStarPieces,
    BossShuffle,
    ShuffledBosses,
    EnabledRegularChecks,
    EnabledBossChecks,
    EXPStarsAnywhere,
    MimicsAnywhere,
    SlotsAnywhere,
    ShuffleBeetlemania,
    ShuffleMagikoopaChest,
    ShuffleWeddingGear,
    ShuffleCoins,
    SpellsAnywhere,
    # Gating flags for character requirement validation
    BanditsWayGate,
    BanditsWayGating,
    KeroSewersGate,
    KeroSewersGating,
    ForestMazeGate,
    ForestMazeGating,
    PipeVaultGate,
    PipeVaultGating,
    Moleville1Gate,
    Moleville1Gating,
    BoosterTowerGate,
    BoosterTowerGating,
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
    BoosterHillGate,
    BoosterHillGating,
    MarrymoreGate,
    MarrymoreGating,
    YaridovichGate,
    YaridovichGating,
    StarPiecesRequired,
)
from ...types.prizelocation import (
    BoosterHillLocation,
    CharacterRecruitmentLocation,
    EventLocation,
    RiverLocation,
    StarPieceLocation,
    BossFightLocation,
    SpellSlotLocation,
    FrogDiscipleLocation,
    TreasureChestLocation,
)
from ...types.prize import (
    CharacterPrize,
    SpellPrize,
    StarPiecePrize,
    BossFightPrize,
)
from ...progression.prizelocations import (
    StartingCharacter1,
    StartingCharacter2,
    StartingCharacter3,
    StartingCharacter4,
    StartingCharacter5,
)
from ...progression.prizes import (
    # Key items
    RareFrogCoinPrize,
    WalletPrize,
    CricketPiePrize,
    BambinoBombPrize,
    CastleKey1Prize,
    CastleKey2Prize,
    ProgressiveCardPrize,
    GreaperFlagPrize,
    DryBonesFlagPrize,
    BigBooFlagPrize,
    ShedKeyPrize,
    ElderKeyPrize,
    CricketJamPrize,
    TempleKeyPrize,
    RoomKeyPrize,
    SeedPrize,
    FertilizerPrize,
    BrightCardPrize,
    YouMissed,
    ProgressiveEggPrize,
    LuckyJewelPrize,
    SignalRingPrize,
    GoodieBagPrize,
    CrystalShardPrize,
    ExtraShinyStonePrize,
    StayVoucherPrize,
    GoldPaintPrize,
    StarEggPrize,
    # Equipment
    FroggiestickPrize,
    ChompPrize,
    ZoomShoesPrize,
    LazyShellArmorPrize,
    LazyShellWeaponPrize,
    GhostMedalPrize,
    QuartzCharmPrize,
    JinxBeltPrize,
    AttackScarfPrize,
    WonderChompPrize,
    Stella023Prize,
    SageStickPrize,
    EnduringBroochPrize,
    TeamworkBandPrize,
    SuperSuitPrize,
    JumpShoesPrize,
    BtubRingPrize,
    # Fireworks
    RegularFireworksPrize,
    ProgressiveFireworksPrize,
    # Characters
    MarioRecruitmentPrize,
    MallowRecruitmentPrize,
    GenoRecruitmentPrize,
    BowserRecruitmentPrize,
    ToadstoolRecruitmentPrize,
    # Spells
    JumpSpellPrize,
    FireOrbSpellPrize,
    SuperJumpSpellPrize,
    SuperFlameSpellPrize,
    UltraJumpSpellPrize,
    UltraFlameSpellPrize,
    ThunderboltSpellPrize,
    HPRainSpellPrize,
    PsychopathSpellPrize,
    ShockerSpellPrize,
    SnowyPrize,
    StarRainSpellPrize,
    GenoBeamSpellPrize,
    GenoBoostSpellPrize,
    GenoWhirlSpellPrize,
    GenoBlastSpellPrize,
    GenoFlashSpellPrize,
    TerrorizeSpellPrize,
    PoisonGasSpellPrize,
    CrusherSpellPrize,
    BowserCrushSpellPrize,
    TherapySpellPrize,
    GroupHugSpellPrize,
    MuteSpellPrize,
    SleepyTimeSpellPrize,
    ComeBackSpellPrize,
    PsychBombSpellPrize,
    # Star pieces
    StarPiece1,
    StarPiece2,
    StarPiece3,
    StarPiece4,
    StarPiece5,
    StarPiece6,
    StarPiece7,
    # Special prizes
    EXPStarPrize,
    MimicFightInitiatorPrize,
    FirstMimicFightLauncher,
    SecondMimicFightLauncher,
    ThirdMimicFightLauncher,
    SlotsPrize,
    BeetlemaniaPrize,
    InfiniteCoinsPrize,
    WeddingGearPrize,
    # bosses
    SeeYaPrize,
    EarlierTimesPrize,
    CoinTrickPrize,
    ExpBoosterPrize,
    ScroogeRingPrize,
    # Boss fight prizes for gating
    BowyerBossFight,
    PunchinelloBossFight,
    BundtBossFight,
    YaridovichBossFight,
    Belome2BossFight,
    MegasmilaxBossFight,
    ValentinaBossFight,
    AxemRangersBossFight,
    KnifeGuyGrateGuyBossFight,
    JohnnyBossFight,
)
from ...data.spells.spells import (
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
    StarRainSpell,
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
    PsychBombSpell,
)
from randomizer.debug import load_debug_config, get_prize_class, get_location_class


if TYPE_CHECKING:
    from ...types.gameworld import GameWorld
    from ...types.prizelocation import PrizeLocation
    from ...types.prize import Prize


def _on_item_placed(
    world: GameWorld, item: Prize, placed_location: PrizeLocation
) -> None:
    """Callback to handle placement events like Mimic world area updates and spell count tracking."""
    from ...progression.prizelocations import (
        Mimic1BossFight,
        Mimic1DropRewardLocation,
        Mimic1StarPiece,
        Mimic1ReloadRewardLocation,
        Mimic2BossFight,
        Mimic2DropRewardLocation,
        Mimic2StarPiece,
        Mimic2ReloadRewardLocation,
        Mimic3BossFight,
        Mimic3StarPiece,
    )
    from ...progression.prizes import (
        FirstMimicFightLauncher,
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
    )
    from ...types.flags import SpellsAnywhere
    from ...types.prize import SpellPrize

    # Update spell assignment count when a spell is actually placed
    # (the character was assigned in can_accept, but count is tracked here)
    if isinstance(item, SpellPrize) and world.settings.isflag_enabled(SpellsAnywhere):
        if item.character is not None:
            if world._spell_assignments is None:
                world._spell_assignments = {}
            char_type = item.character
            world._spell_assignments[char_type] = (
                world._spell_assignments.get(char_type, 0) + 1
            )

    # Update Mimic location world areas to match where the launcher was placed
    if isinstance(item, FirstMimicFightLauncher):
        world_area = placed_location._world_area
        world.locations[Mimic1BossFight]._world_area = world_area
        world.locations[Mimic1DropRewardLocation]._world_area = world_area
        world.locations[Mimic1StarPiece]._world_area = world_area
        world.locations[Mimic1ReloadRewardLocation]._world_area = world_area
    elif isinstance(item, SecondMimicFightLauncher):
        world_area = placed_location._world_area
        world.locations[Mimic2BossFight]._world_area = world_area
        world.locations[Mimic2DropRewardLocation]._world_area = world_area
        world.locations[Mimic2StarPiece]._world_area = world_area
        world.locations[Mimic2ReloadRewardLocation]._world_area = world_area
    elif isinstance(item, ThirdMimicFightLauncher):
        world_area = placed_location._world_area
        world.locations[Mimic3BossFight]._world_area = world_area
        world.locations[Mimic3StarPiece]._world_area = world_area


ally_name_to_prize: dict[str, type[CharacterPrize]] = {
    "Mario": MarioRecruitmentPrize,
    "Mallow": MallowRecruitmentPrize,
    "Geno": GenoRecruitmentPrize,
    "Bowser": BowserRecruitmentPrize,
    "Toadstool": ToadstoolRecruitmentPrize,
}

PROGRESSION_PRIZES = 0
RESTRICTED_PRIZES = 1
MANDATORY_INCLUSIONS = 2
LOW_PRIORITY = 3


def shuffle_rules(world: GameWorld) -> dict[int, list[type[Prize]]]:
    # Prize placement guidelines are divided into tiers.
    # The highest tier is prizes that gate other checks.
    progress_rules: list[type[Prize]] = [
        CastleKey1Prize,
        CastleKey2Prize,
        BambinoBombPrize,
        BrightCardPrize,
        ElderKeyPrize,
        RoomKeyPrize,
        WalletPrize,
        GreaperFlagPrize,
        DryBonesFlagPrize,
        BigBooFlagPrize,
        CricketJamPrize,
        SeedPrize,
        FertilizerPrize,
        RegularFireworksPrize,
        ProgressiveFireworksPrize,
        WeddingGearPrize,
        ExtraShinyStonePrize,
        StayVoucherPrize,
        CookiesPrize,
        MarioDollPrize,
        FirstMimicFightLauncher,
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
        CricketPiePrize,
        TempleKeyPrize,
        RareFrogCoinPrize,
        ShedKeyPrize,
        GoldPaintPrize,
    ]
    # All boss fights are progress because they each unlock one star piece check at minimum.
    for prize_cls in BossFightPrize.__subclasses__():
        progress_rules.append(prize_cls)
    # Prizes that unlock progress depending on settings
    conditional_progress: dict[type[Prize], list[tuple[type, object]]] = {
        MallowRecruitmentPrize: [
            (BanditsWayGate, BanditsWayGating.MALLOW),
            (KeroSewersGate, KeroSewersGating.MALLOW),
            (BoosterTowerGate, BoosterTowerGating.MALLOW),
        ],
        GenoRecruitmentPrize: [
            (PipeVaultGate, PipeVaultGating.GENO),
            (Moleville1Gate, Moleville1Gating.GENO),
            (BoosterTowerGate, BoosterTowerGating.GENO),
        ],
        MarioRecruitmentPrize: [
            (BoosterTowerGate, BoosterTowerGating.MARIO),
        ],
        ToadstoolRecruitmentPrize: [
            (BoosterTowerGate, BoosterTowerGating.TOADSTOOL),
            (SeaGate, SeaGating.TOADSTOOL),
        ],
        BowserRecruitmentPrize: [
            (BoosterTowerGate, BoosterTowerGating.BOWSER),
        ],
    }
    for prize_cls, gating_info in conditional_progress.items():
        for gate, gating_flag in gating_info:
            if world.settings.is_flag_value(gate, gating_flag):
                progress_rules.append(prize_cls)
                break

    # Add Super Jump to progress if either Super Jump reward location is enabled
    if (
        world.is_location_enabled(MonstroFirstSuperJumpRewardLocation)
        or world.is_location_enabled(MonstroSecondSuperJumpRewardLocation)
    ):
        progress_rules.append(SuperJumpSpellPrize)

    # All spell prizes (these will be split between progress and should_otherwise_include)
    all_spell_prizes: list[type[Prize]] = [
        JumpSpellPrize,
        FireOrbSpellPrize,
        SuperFlameSpellPrize,
        UltraJumpSpellPrize,
        UltraFlameSpellPrize,
        ThunderboltSpellPrize,
        HPRainSpellPrize,
        PsychopathSpellPrize,
        ShockerSpellPrize,
        SnowyPrize,
        StarRainSpellPrize,
        GenoBeamSpellPrize,
        GenoBoostSpellPrize,
        GenoWhirlSpellPrize,
        GenoBlastSpellPrize,
        GenoFlashSpellPrize,
        TerrorizeSpellPrize,
        PoisonGasSpellPrize,
        CrusherSpellPrize,
        BowserCrushSpellPrize,
        TherapySpellPrize,
        GroupHugSpellPrize,
        MuteSpellPrize,
        SleepyTimeSpellPrize,
        ComeBackSpellPrize,
        PsychBombSpellPrize,
    ]
    # SuperJumpSpellPrize is handled separately above based on location availability

    # Non-elemental spell prizes (Element.NONE) - excluding Super Jump (it's JUMP element)
    non_elemental_spell_prizes: list[type[Prize]] = [
        HPRainSpellPrize,
        PsychopathSpellPrize,
        StarRainSpellPrize,
        GenoBeamSpellPrize,
        GenoBoostSpellPrize,
        GenoWhirlSpellPrize,
        GenoBlastSpellPrize,
        GenoFlashSpellPrize,
        TerrorizeSpellPrize,
        PoisonGasSpellPrize,
        CrusherSpellPrize,
        BowserCrushSpellPrize,
        TherapySpellPrize,
        GroupHugSpellPrize,
        MuteSpellPrize,
        SleepyTimeSpellPrize,
        ComeBackSpellPrize,
        PsychBombSpellPrize,
    ]

    # Choose one random non-elemental spell for progress_rules
    chosen_nonelemental = random.choice(non_elemental_spell_prizes)
    progress_rules.append(chosen_nonelemental)

    # All other spells go to should_otherwise_include_rules
    spells_for_inclusion = [
        sp for sp in all_spell_prizes
        if sp != SuperJumpSpellPrize and sp != chosen_nonelemental
    ]

    # Tier 3: Prizes that don't unlock anything but that are extremely limited in terms of where they can be placed, so they need to be placed next
    post_progression_rules: list[type[Prize]] = [
        SlotsPrize,
        BanditsWayStarPrize,
        KeroSewersStarPrize,
        MolevilleMinesStarPrize,
        SeaStarPrize,
        LandsEndVolcanoStarPrize,
        NimbusLandStarPrize,
        LandsEndStar2Prize,
        LandsEndStar3Prize,
    ]

    # Tier 4: Other prizes that don't unlock anything but are still mandatory to include
    # These can include unpurchase-able items, for example
    should_otherwise_include_rules: list[type[Prize]] = [
        ProgressiveEggPrize,
        CrystalShardPrize,
        ProgressiveCardPrize,
        SeeYaPrize,
        EarlierTimesPrize,
        CoinTrickPrize,
        ExpBoosterPrize,
        ScroogeRingPrize,
        LuckyJewelPrize,
        FryingPanPrize,
    ]
    # Add all spells except Super Jump and the chosen non-elemental
    should_otherwise_include_rules.extend(spells_for_inclusion)
    if not world.settings.isflag_enabled(NoStarEgg):
        should_otherwise_include_rules.extend([StarEggPrize])
    return {
        PROGRESSION_PRIZES: progress_rules,
        RESTRICTED_PRIZES: post_progression_rules,
        MANDATORY_INCLUSIONS: should_otherwise_include_rules,
        LOW_PRIORITY: [FrogCoin1Prize, RecoveryMushroomPrize, FPFlowerPrize, CoinPrize],
    }


def should_shuffle(location: PrizeLocation, world: GameWorld) -> bool:
    if isinstance(
        location,
        (
            TreasureChestLocation,
            StandingLocation,
            EventLocation,
            RiverLocation,
            BoosterHillLocation,
        ),
    ) and not world.settings.isflag_enabled(ShuffleItems):
        return False
    if isinstance(
        location, (TreasureShopLocation, FrogDiscipleLocation)
    ) and not world.settings.isflag_enabled(ShuffleShops):
        return False
    if isinstance(location, BoosterHillLocation) and not world.settings.isflag_enabled(
        ShuffleHillFlowers
    ):
        return False
    if isinstance(
        location, CharacterRecruitmentLocation
    ) and not world.settings.isflag_enabled(ShuffleCharacters):
        return False
    if isinstance(location, StarPieceLocation) and not world.settings.isflag_enabled(
        ShuffleStarPieces
    ):
        return False
    if isinstance(location, BossFightLocation) and not world.settings.isflag_enabled(
        BossShuffle
    ):
        return False
    if isinstance(
        location, MushroomKingdomInnPurchaseLocation
    ) and not world.settings.isflag_enabled(ShuffleBeetlemania):
        return False
    if location.originally_held is not None:
        if issubclass(
            location.originally_held, SlotsPrize
        ) and not world.settings.isflag_enabled(SlotsAnywhere):
            return False
        if issubclass(
            location.originally_held, EXPStarPrize
        ) and not world.settings.isflag_enabled(EXPStarsAnywhere):
            return False
        if issubclass(
            location.originally_held, MimicFightInitiatorPrize
        ) and not world.settings.isflag_enabled(MimicsAnywhere):
            return False
        if issubclass(
            location.originally_held, InfiniteCoinsPrize
        ) and not world.settings.isflag_enabled(ShuffleMagikoopaChest):
            return False
    if not world.is_location_enabled(type(location)):
        return False
    return True


def pull_prize(location: PrizeLocation, world: GameWorld) -> Prize | None:
    if location.originally_held is None:
        return None
    inclusions = shuffle_rules(world)
    if issubclass(
        location.originally_held, RegularFireworksPrize
    ) and not world.settings.is_flag_value(FireworksSetting, FireworksOptions.VANILLA):
        return ProgressiveFireworksPrize()
    if issubclass(
        location.originally_held, StarEggPrize
    ) and world.settings.isflag_enabled(NoStarEgg):
        return None
    if isinstance(
        location,
        (
            TreasureChestLocation,
            StandingLocation,
            EventLocation,
            RiverLocation,
            BoosterHillLocation,
        ),
    ):
        for tier in inclusions.values():
            for prize_cls in tier:
                if tier == LOW_PRIORITY and world.settings.is_flag_value(ItemQuality, ItemQualityOptions.COMPLETELY_EMPTY):
                    return None
                if issubclass(location.originally_held, prize_cls):
                    return prize_cls()
        if world.settings.is_flag_value(ItemQuality, ItemQualityOptions.COMPLETELY_EMPTY):
            return None
        
        if world.settings.is_flag_value(ItemQuality, ItemQualityOptions.ORIGINAL_POOL):
            prize = location.originally_held()
        else:
            prize = RandomPrizeSubstitute().generate(world, location)

        if world.settings.isflag_enabled(ReplaceItems) and issubclass(location.originally_held, ItemPrize):
            item = location.originally_held().item
            if issubclass(
                item,
                (
                    MushroomItem,
                    HoneySyrupItem,
                    AbleJuiceItem,
                    YoshiCookieItem,
                    PureWaterItem,
                    FroggieDrinkItem,
                    WiltShroomItem,
                    RottenMushItem,
                    MoldyMushItem,
                ),
            ) or (
                issubclass(item, MushroomItem2)
                and Status.INVINCIBLE not in world.get_item(MushroomItem2).status_immunities
            ):
                prize = CoinPrize(world.get_item(item).price)
        return prize
            
    return location.originally_held()


def shuffle(world: GameWorld) -> None:
    pool: dict[int, list[Prize]] = {
        PROGRESSION_PRIZES: [],
        RESTRICTED_PRIZES: [],
        MANDATORY_INCLUSIONS: [],
        LOW_PRIORITY: [],
    }
    # Always have 3 progressive eggs if item shuffle is enabled
    if world.settings.isflag_enabled(ShuffleItems):
        pool[MANDATORY_INCLUSIONS].extend([ProgressiveEggPrize(), ProgressiveEggPrize()])

    # Reset spell assignments for SpellsAnywhere
    world._spell_assignments = None
    stars = [
        StarPiece1,
        StarPiece2,
        StarPiece3,
        StarPiece4,
        StarPiece5,
        StarPiece6,
        StarPiece7,
    ]
    progress_stars = 0
    if world.settings.is_flag_value(SeaGate, SeaGating.STAR_4):
        progress_stars = 4
    elif world.settings.is_flag_value(LandsEndGate, LandsEndGating.STAR_5):
        progress_stars = 4
    elif world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.STAR_6):
        progress_stars = 6
    elif world.settings.is_flag_value(FactoryGate, FactoryGating.STAR_6):
        progress_stars = 6
    mxstars = world.settings.get_flag(StarPiecesRequired).value
    if mxstars > progress_stars:
        progress_stars = mxstars
    maxstars = world.settings.get_flag(TotalStarPieces).value

    rules = shuffle_rules(world)
    config = {}
    if world.settings.debug_mode:
        config = load_debug_config()
    overrides = config.get("items", {}).get("override", {})

    # Empty every location and build the prize pool
    for loc in world.locations.values():
        # TODO: Need to manage deficit for debug items
        # TODO: Need to account for excluded characters and starting characters
        # TODO: Need to account for reduced star piece counts
        is_debug = False
        if world.settings.debug_mode:
            for location_name, prize_name in overrides.items():
                location_cls = get_location_class(location_name)
                if location_cls is None:
                    raise ValueError(f"Invalid location name in debug config: '{location_name}'")
                if isinstance(loc, location_cls):
                    prize_cls = get_prize_class(prize_name)
                    if prize_cls is None or not loc.can_accept(prize_cls(), Inventory(), world):
                        if not loc.can_be_empty(world):
                            raise ValueError(
                                f"Invalid prize assigned to debug location '{location_name}' when it cannot be empty"
                            )
                        else:
                            loc.set_prize(None)
                    else:
                        loc.set_prize(prize_cls())
                    if loc.originally_held is not None:
                        # displace prize
                        for tier, classes in rules.items():
                            if any(isinstance(loc.originally_held(), cls) for cls in classes):
                                pool[tier].append(loc.originally_held())
                                break
                    is_debug = True
                    break
        if is_debug:
            continue
        if should_shuffle(loc, world):
            loc.set_prize(None)
            pool_item = pull_prize(loc, world)
            if pool_item is None:
                continue
            for tier, classes in rules.items():
                if any(isinstance(pool_item, cls) for cls in classes):
                    pool[tier].append(pool_item)
                    break
            if world.settings.is_flag_value(
                ItemQuality, ItemQualityOptions.ORIGINAL_POOL
            ):
                pool[MANDATORY_INCLUSIONS].append(pool_item)
            else:
                pool[LOW_PRIORITY].append(pool_item)
        else:
            if loc.originally_held is not None:
                loc.set_prize(loc.originally_held())


def shuffle_prizes(world: GameWorld) -> None:
    """Shuffle all prizes across available locations.

    This function:
    1. Empties all locations
    2. Builds must_include and less_important prize lists based on settings
    3. Places prizes using assumed-reachability algorithm
    4. Verifies all required prizes were placed
    """
    from ...types.flags import (
        ShuffleItems,
        ShuffleShops,
        Remake,
        RestrictSpecialEquips,
        SuperJump2Threshold,
        NoStarEgg,
        ItemQuality,
        ItemQualityOptions,
        FireworksSetting,
        FireworksOptions,
        ShuffleCharacters,
        StartingCharacters,
        AvailableCharacters,
        MaxCharacters,
        CharacterLearnedSpells,
        AvailableSpells,
        ShuffleStarPieces,
        TotalStarPieces,
        BossShuffle,
        ShuffledBosses,
        EnabledBossChecks,
        EXPStarsAnywhere,
        MimicsAnywhere,
        SlotsAnywhere,
        ShuffleBeetlemania,
        ShuffleMagikoopaChest,
        ShuffleWeddingGear,
        ShuffleCoins,
        SpellsAnywhere,
        # Gating flags for character requirement validation
        BanditsWayGate,
        BanditsWayGating,
        KeroSewersGate,
        KeroSewersGating,
        ForestMazeGate,
        ForestMazeGating,
        PipeVaultGate,
        PipeVaultGating,
        Moleville1Gate,
        Moleville1Gating,
        BoosterTowerGate,
        BoosterTowerGating,
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
        BoosterHillGate,
        BoosterHillGating,
        MarrymoreGate,
        MarrymoreGating,
        YaridovichGate,
        YaridovichGating,
        StarPiecesRequired,
    )
    from ...types.prizelocation import (
        CharacterRecruitmentLocation,
        StarPieceLocation,
        BossFightLocation,
        SpellSlotLocation,
        FrogDiscipleLocation,
    )
    from ...types.prize import (
        CharacterPrize,
        SpellPrize,
        StarPiecePrize,
        BossFightPrize,
    )
    from ...progression.prizelocations import (
        StartingCharacter1,
        StartingCharacter2,
        StartingCharacter3,
        StartingCharacter4,
        StartingCharacter5,
    )
    from ...progression.prizes import (
        # Key items
        RareFrogCoinPrize,
        WalletPrize,
        CricketPiePrize,
        BambinoBombPrize,
        CastleKey1Prize,
        CastleKey2Prize,
        ProgressiveCardPrize,
        GreaperFlagPrize,
        DryBonesFlagPrize,
        BigBooFlagPrize,
        ShedKeyPrize,
        ElderKeyPrize,
        CricketJamPrize,
        TempleKeyPrize,
        RoomKeyPrize,
        SeedPrize,
        FertilizerPrize,
        BrightCardPrize,
        YouMissed,
        ProgressiveEggPrize,
        LuckyJewelPrize,
        SignalRingPrize,
        GoodieBagPrize,
        CrystalShardPrize,
        ExtraShinyStonePrize,
        StayVoucherPrize,
        GoldPaintPrize,
        StarEggPrize,
        # Equipment
        FroggiestickPrize,
        ChompPrize,
        ZoomShoesPrize,
        LazyShellArmorPrize,
        LazyShellWeaponPrize,
        GhostMedalPrize,
        QuartzCharmPrize,
        JinxBeltPrize,
        AttackScarfPrize,
        WonderChompPrize,
        Stella023Prize,
        SageStickPrize,
        EnduringBroochPrize,
        TeamworkBandPrize,
        SuperSuitPrize,
        JumpShoesPrize,
        BtubRingPrize,
        # Fireworks
        RegularFireworksPrize,
        ProgressiveFireworksPrize,
        # Characters
        MarioRecruitmentPrize,
        MallowRecruitmentPrize,
        GenoRecruitmentPrize,
        BowserRecruitmentPrize,
        ToadstoolRecruitmentPrize,
        # Spells
        JumpSpellPrize,
        FireOrbSpellPrize,
        SuperJumpSpellPrize,
        SuperFlameSpellPrize,
        UltraJumpSpellPrize,
        UltraFlameSpellPrize,
        ThunderboltSpellPrize,
        HPRainSpellPrize,
        PsychopathSpellPrize,
        ShockerSpellPrize,
        SnowyPrize,
        StarRainSpellPrize,
        GenoBeamSpellPrize,
        GenoBoostSpellPrize,
        GenoWhirlSpellPrize,
        GenoBlastSpellPrize,
        GenoFlashSpellPrize,
        TerrorizeSpellPrize,
        PoisonGasSpellPrize,
        CrusherSpellPrize,
        BowserCrushSpellPrize,
        TherapySpellPrize,
        GroupHugSpellPrize,
        MuteSpellPrize,
        SleepyTimeSpellPrize,
        ComeBackSpellPrize,
        PsychBombSpellPrize,
        # Star pieces
        StarPiece1,
        StarPiece2,
        StarPiece3,
        StarPiece4,
        StarPiece5,
        StarPiece6,
        StarPiece7,
        # Special prizes
        EXPStarPrize,
        MimicFightInitiatorPrize,
        FirstMimicFightLauncher,
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
        SlotsPrize,
        BeetlemaniaPrize,
        InfiniteCoinsPrize,
        WeddingGearPrize,
        # bosses
        SeeYaPrize,
        EarlierTimesPrize,
        CoinTrickPrize,
        ExpBoosterPrize,
        ScroogeRingPrize,
        # Boss fight prizes for gating
        BowyerBossFight,
        PunchinelloBossFight,
        BundtBossFight,
        YaridovichBossFight,
        Belome2BossFight,
        MegasmilaxBossFight,
        ValentinaBossFight,
        AxemRangersBossFight,
        KnifeGuyGrateGuyBossFight,
        JohnnyBossFight,
    )
    from ...data.spells.spells import (
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
        StarRainSpell,
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
        PsychBombSpell,
    )

    # Start off emptying every location of every type
    for loc in world.locations.values():
        loc.set_prize(None)

    # Reset spell assignments for SpellsAnywhere mode (handles retry scenarios)
    world._spell_assignments = None

    # Apply debug overrides first (hard-set locations before shuffle)
    # Track which prize TYPES were placed via override (to avoid double-placing characters/spells/etc.)
    # Note: We don't remove these from the item pool - the overridden location's originally_held
    # item naturally won't be collected (because has_item will be True), so the pool already
    # accounts for one item being "replaced" by the override.
    debug_placed_prize_types: set[type] = set()
    displaced_prizes: list[type] = []
    if world.settings.debug_mode:
        from randomizer.debug import (
            load_debug_config,
            get_prize_class,
            get_location_class,
        )

        config = load_debug_config()
        overrides = config.get("items", {}).get("override", {})

        for location_name, prize_name in overrides.items():
            location_cls = get_location_class(location_name)
            prize_cls = get_prize_class(prize_name)

            if location_cls is None or prize_cls is None:
                continue
            if location_cls not in world.locations:
                print(f"Warning: Location '{location_name}' not in world.locations")
                continue

            location = world.locations[location_cls]

            # Warn if trying to override a BossFightLocation with a non-boss prize
            if isinstance(location, BossFightLocation) and not issubclass(
                prize_cls, BossFightPrize
            ):
                print(
                    f"WARNING: Cannot override BossFightLocation '{location_name}' with non-boss prize '{prize_name}'"
                )
                print(
                    f"  This will cause boss placement to fail! Skipping this override."
                )
                continue

            if location.originally_held is not None:
                displaced_prizes.append(location.originally_held)

            location.set_prize(prize_cls())
            debug_placed_prize_types.add(prize_cls)

    # Helper to check if a prize type was already placed via debug override
    def is_debug_placed(prize_cls: type) -> bool:
        return prize_cls in debug_placed_prize_types

    # Define which items unlock HIGH-VOLUME areas (many checks)
    # These are always considered high-volume regardless of settings
    always_high_volume_key_items: list[type[Prize]] = [
        CastleKey1Prize,  # Bowser's Keep
        CastleKey2Prize,  # Bowser's Keep
        BambinoBombPrize,  # Moleville Mines
    ]

    # Conditionally high-volume items (depend on gating settings)
    conditionally_high_volume: dict[type[Prize], list[tuple[type, object]]] = {
        # Key items
        CricketPiePrize: [(ForestMazeGate, ForestMazeGating.PIE)],
        TempleKeyPrize: [(BelomeTempleGate, BelomeTempleGating.KEY)],
        RareFrogCoinPrize: [],  # High-vol if any gating requires it (checked below)
        ShedKeyPrize: [(LandsEndGate, LandsEndGating.ELDER)],  # Needed to release elder
        GoldPaintPrize: [
            (NimbusGate, NimbusGating.PAINT)
        ],  # Needed to enter Nimbus Castle
        # Boss fights that unlock high-volume areas
        BowyerBossFight: [
            (PipeVaultGate, PipeVaultGating.BOWYER),
            (Moleville1Gate, Moleville1Gating.BOWYER),
        ],
        PunchinelloBossFight: [(BoosterTowerGate, BoosterTowerGating.PUNCHINELLO)],
        BundtBossFight: [(SeaGate, SeaGating.BUNDT)],
        YaridovichBossFight: [(LandsEndGate, LandsEndGating.YARIDOVICH)],
        Belome2BossFight: [(MonstroTownGate, MonstroTownGating.BELOME_2)],
        MegasmilaxBossFight: [(NimbusGate, NimbusGating.MEGASMILAX)],
        ValentinaBossFight: [(BarrelVolcanoGate, BarrelVolcanoGating.VALENTINA)],
        AxemRangersBossFight: [(BowsersKeepGate, BowsersKeepGating.AXEM)],
    }

    # Conditionally low-volume boss fights (unlock fewer checks)
    conditionally_low_volume_bosses: dict[type[Prize], list[tuple[type, object]]] = {
        KnifeGuyGrateGuyBossFight: [
            (BoosterHillGate, BoosterHillGating.KGGG),
            (MarrymoreGate, MarrymoreGating.KGGG),
        ],
        JohnnyBossFight: [(YaridovichGate, YaridovichGating.JOHNNY)],
    }

    # Define which items unlock LOW-VOLUME areas (fewer checks)
    low_volume_key_items: list[type[Prize]] = [
        BrightCardPrize,  # Grate Guy's Casino
        ElderKeyPrize,  # Tadpole Pond area
        RoomKeyPrize,  # Single room
        WalletPrize,  # Frog coin trade
        GreaperFlagPrize,  # Monstro Town flags
        DryBonesFlagPrize,  # Monstro Town flags
        BigBooFlagPrize,  # Monstro Town flags
        CricketJamPrize,  # Frog sage reward
        SeedPrize,  # Lazy shell
        FertilizerPrize,  # Lazy shell
        RegularFireworksPrize,  # Marrymore
        ProgressiveFireworksPrize,  # Marrymore
        WeddingGearPrize,  # Marrymore
        ExtraShinyStonePrize,  # Extra Shiny Stone (Remake)
        StayVoucherPrize,  # Stay Voucher (Marrymore item, Remake)
        CookiesPrize,
        MarioDollPrize,
    ]

    # Add mimic launchers to shuffle pool when MimicsAnywhere is enabled
    if world.settings.isflag_enabled(MimicsAnywhere):
        low_volume_key_items.extend(
            [
                FirstMimicFightLauncher,
                SecondMimicFightLauncher,
                ThirdMimicFightLauncher,
            ]
        )

    # Build high-volume list based on current settings
    high_volume_key_items: list[type[Prize]] = list(always_high_volume_key_items)

    # Check conditionally high-volume items
    for item_prize, gating_checks in conditionally_high_volume.items():
        # Skip if already in high-volume (from always_high_volume_key_items)
        if item_prize in high_volume_key_items:
            continue
        is_high_vol = False
        for gating_check in gating_checks:
            if world.settings.is_flag_value(gating_check[0], gating_check[1]):
                is_high_vol = True
                break
        if is_high_vol:
            high_volume_key_items.append(item_prize)
        else:
            # Add to low-volume if not high-volume (and not already there)
            if item_prize not in low_volume_key_items:
                low_volume_key_items.append(item_prize)

    # Check conditionally low-volume boss fights
    for boss_prize, gating_checks in conditionally_low_volume_bosses.items():
        is_low_vol = False
        for gating_check in gating_checks:
            if world.settings.is_flag_value(gating_check[0], gating_check[1]):
                is_low_vol = True
                break
        if is_low_vol:
            # Only add to low-volume if the gating is active AND not already in high-volume
            # (high-volume takes priority if same prize unlocks both types of areas)
            if (
                boss_prize not in low_volume_key_items
                and boss_prize not in high_volume_key_items
            ):
                low_volume_key_items.append(boss_prize)

    # Items that absolutely must be included, but aren't important for progress, can be second priority
    should_otherwise_include = copy(displaced_prizes)
    # Items that go to post_progression_priority (after progression, before must_include)
    # Order: slots/exp stars > progressive cards/crystal shard/leftover stars
    post_progression_include: list[type[Prize]] = [
        SlotsPrize,  # Slot machines (placed after progression, needs room with 5 NPCs)
        ProgressiveCardPrize,  # Progressive cards
    ]

    progress_stars = 0
    if world.settings.isflag_enabled(Remake):
        # ExtraShinyStonePrize and StayVoucherPrize are in low_volume_key_items
        post_progression_include.append(
            CrystalShardPrize
        )  # Crystal shard goes to post_progression
    # Note: Fireworks and GoldPaint are handled via conditionally_high_volume or low_volume_key_items
    if world.settings.is_flag_value(SeaGate, SeaGating.STAR_4):
        progress_stars = 4
    elif world.settings.is_flag_value(LandsEndGate, LandsEndGating.STAR_5):
        progress_stars = 4
    elif world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.STAR_6):
        progress_stars = 6
    elif world.settings.is_flag_value(FactoryGate, FactoryGating.STAR_6):
        progress_stars = 6
    if world.settings.isflag_enabled(ShuffleShops):
        should_otherwise_include.extend(
            [
                SeeYaPrize,
                EarlierTimesPrize,
                CoinTrickPrize,
                ExpBoosterPrize,
                ScroogeRingPrize,
                LuckyJewelPrize,
                ProgressiveEggPrize,
                FryingPanPrize,
            ]
        )
    mxstars = world.settings.get_flag(StarPiecesRequired).value
    if mxstars > progress_stars:
        progress_stars = mxstars
    if not world.settings.is_flag_value(ItemQuality, ItemQualityOptions.ORIGINAL_POOL):
        should_otherwise_include.extend(
            [
                JumpShoesPrize,
                BtubRingPrize,
            ]
        )
    if world.settings.isflag_enabled(RestrictSpecialEquips):
        should_otherwise_include.extend(
            [
                FroggiestickPrize,
                ChompPrize,
                ZoomShoesPrize,
                LazyShellArmorPrize,
                LazyShellWeaponPrize,
                GhostMedalPrize,
                QuartzCharmPrize,
                JinxBeltPrize,
                AttackScarfPrize,
                SuperSuitPrize,
            ]
        )
        # EXP stars go to post_progression_priority (placed after progression, before must_include)
        post_progression_include.append(EXPStarPrize)
        if world.settings.isflag_enabled(Remake):
            should_otherwise_include.extend(
                [
                    WonderChompPrize,
                    Stella023Prize,
                    SageStickPrize,
                    EnduringBroochPrize,
                    TeamworkBandPrize,
                ]
            )

    # Prize pools with high-vol/low-vol distinction
    # Characters and items that unlock high-volume areas (many checks)
    high_vol_character_prizes: list[Prize] = []
    high_vol_other_prizes: list[Prize] = []
    # Characters and items that unlock low-volume areas (fewer checks)
    low_vol_character_prizes: list[Prize] = []
    low_vol_other_prizes: list[Prize] = []

    progression_prizes: list[Prize] = []
    must_include: list[Prize] = []
    if world.settings.isflag_enabled(ShuffleItems):
        must_include.extend([ProgressiveEggPrize(), ProgressiveEggPrize()])
    not_important: list[Prize] = []
    # Items with very restricted placement options (e.g., SlotsPrize which can only go
    # in chest locations with enough room for 5 extra NPCs) - placed first
    restricted_prizes: list[Prize] = []
    # Items that go after progression but before must_include
    post_progression_priority: list[Prize] = []

    if world.settings.isflag_enabled(ShuffleCharacters):
        # Place starting characters based on StartingCharacters flag
        ally_name_to_prize: dict[str, type[CharacterPrize]] = {
            "Mario": MarioRecruitmentPrize,
            "Mallow": MallowRecruitmentPrize,
            "Geno": GenoRecruitmentPrize,
            "Bowser": BowserRecruitmentPrize,
            "Toadstool": ToadstoolRecruitmentPrize,
        }

        # Collect characters required by gating settings AND determine if they're high-vol
        # High-volume areas: Bandit's Way, Kero Sewers, Pipe Vault, Moleville, Booster Tower, Sea
        gating_required_characters: set[str] = set()
        high_vol_gating_characters: set[str] = (
            set()
        )  # Characters that unlock high-vol areas
        char_gating_checks: list[tuple[type, object, str]] = [
            # All of these areas are considered HIGH-VOLUME
            (BanditsWayGate, BanditsWayGating.MALLOW, "Mallow"),
            (KeroSewersGate, KeroSewersGating.MALLOW, "Mallow"),
            (PipeVaultGate, PipeVaultGating.GENO, "Geno"),
            (Moleville1Gate, Moleville1Gating.GENO, "Geno"),
            (BoosterTowerGate, BoosterTowerGating.MARIO, "Mario"),
            (BoosterTowerGate, BoosterTowerGating.MALLOW, "Mallow"),
            (BoosterTowerGate, BoosterTowerGating.GENO, "Geno"),
            (BoosterTowerGate, BoosterTowerGating.BOWSER, "Bowser"),
            (BoosterTowerGate, BoosterTowerGating.TOADSTOOL, "Toadstool"),
            (SeaGate, SeaGating.TOADSTOOL, "Toadstool"),
        ]
        for flag_class, gating_value, char_name in char_gating_checks:
            if world.settings.is_flag_value(flag_class, gating_value):
                gating_required_characters.add(char_name)
                high_vol_gating_characters.add(
                    char_name
                )  # All gating areas are high-vol

        # Collect explicitly set starting characters (non-random)
        starting_chars_flag = world.settings.get_flag(StartingCharacters)
        explicitly_set_starting_chars: set[str] = set()
        for option in starting_chars_flag.enabled:
            value = option.value
            # Check if this is a "Random_X" string value - skip, those aren't explicit
            if isinstance(value, str):
                continue
            # This is an actual ally instance
            ally_name = value.name
            if ally_name:
                explicitly_set_starting_chars.add(ally_name)

        # Validate requirements against available characters and max count
        available_chars_flag = world.settings.get_flag(AvailableCharacters)
        disabled_char_names = {m.value.name for m in available_chars_flag.disabled}
        max_char_count = world.settings.get_flag(MaxCharacters).value

        # Note: Character/gating validation is now done earlier in validate_settings()
        # The variables collected above (gating_required_characters, disabled_char_names,
        # max_char_count) are still needed for the actual placement logic below.

        # Starting character locations in order
        starting_locations = [
            StartingCharacter1,
            StartingCharacter2,
            StartingCharacter3,
            StartingCharacter4,
            StartingCharacter5,
        ]

        # Track which characters have been explicitly placed
        placed_characters: set[type[CharacterPrize]] = set()

        # Place characters based on their ordinance position
        for idx, option in enumerate(starting_chars_flag.enabled):
            if idx >= len(starting_locations) or idx >= max_char_count:
                break

            value = option.value
            # Check if this is a "Random_X" string value - skip, shuffler will handle it
            if isinstance(value, str):
                continue

            # This is an actual ally instance - place it using its name
            ally_name = value.name
            if ally_name and ally_name in ally_name_to_prize:
                prize_class = ally_name_to_prize[ally_name]
                loc = world.locations.get(starting_locations[idx])
                if loc is not None:
                    loc.set_prize(prize_class())
                    placed_characters.add(prize_class)

        # Add unplaced characters to progression_prizes (unless disabled in AvailableCharacters)
        all_recruitment_prizes: dict[str, type[CharacterPrize]] = {
            "Mario": MarioRecruitmentPrize,
            "Mallow": MallowRecruitmentPrize,
            "Geno": GenoRecruitmentPrize,
            "Bowser": BowserRecruitmentPrize,
            "Toadstool": ToadstoolRecruitmentPrize,
        }

        # First, add gating-required characters that haven't been placed yet
        # Sort to ensure deterministic order (sets have non-deterministic iteration due to hash randomization)
        for char_name in sorted(gating_required_characters):
            prize_class = all_recruitment_prizes[char_name]
            if prize_class not in placed_characters:
                # Skip if already placed via debug override
                if is_debug_placed(prize_class):
                    placed_characters.add(prize_class)
                    continue
                # All gating-required characters go to high-vol (they unlock major areas)
                high_vol_character_prizes.append(prize_class())
                placed_characters.add(prize_class)

        # Then add random unplaced characters up to max count
        remaining_chars = [
            (name, cls)
            for name, cls in all_recruitment_prizes.items()
            if cls not in placed_characters and name not in disabled_char_names
        ]
        random.shuffle(remaining_chars)
        for ally_name, prize_class in remaining_chars:
            if len(placed_characters) >= max_char_count:
                break
            # Skip if already placed via debug override
            if is_debug_placed(prize_class):
                placed_characters.add(prize_class)
                continue
            # Non-gating characters go to low-vol (they don't unlock major areas)
            low_vol_character_prizes.append(prize_class())
            placed_characters.add(prize_class)

    if world.settings.isflag_enabled(CharacterLearnedSpells):
        # Build mapping from spell class -> spell prize class
        spell_to_prize: dict[type, type[SpellPrize]] = {
            JumpSpell: JumpSpellPrize,
            FireOrbSpell: FireOrbSpellPrize,
            SuperJumpSpell: SuperJumpSpellPrize,
            SuperFlameSpell: SuperFlameSpellPrize,
            UltraJumpSpell: UltraJumpSpellPrize,
            UltraFlameSpell: UltraFlameSpellPrize,
            ThunderboltSpell: ThunderboltSpellPrize,
            HPRainSpell: HPRainSpellPrize,
            PsychopathSpell: PsychopathSpellPrize,
            ShockerSpell: ShockerSpellPrize,
            SnowySpell: SnowyPrize,
            StarRainSpell: StarRainSpellPrize,
            GenoBeamSpell: GenoBeamSpellPrize,
            GenoBoostSpell: GenoBoostSpellPrize,
            GenoWhirlSpell: GenoWhirlSpellPrize,
            GenoBlastSpell: GenoBlastSpellPrize,
            GenoFlashSpell: GenoFlashSpellPrize,
            TerrorizeSpell: TerrorizeSpellPrize,
            PoisonGasSpell: PoisonGasSpellPrize,
            CrusherSpell: CrusherSpellPrize,
            BowserCrushSpell: BowserCrushSpellPrize,
            TherapySpell: TherapySpellPrize,
            GroupHugSpell: GroupHugSpellPrize,
            MuteSpell: MuteSpellPrize,
            SleepyTimeSpell: SleepyTimeSpellPrize,
            ComeBackSpell: ComeBackSpellPrize,
            PsychBombSpell: PsychBombSpellPrize,
        }

        # Get disabled spell classes from AvailableSpells flag
        available_spells_flag = world.settings.get_flag(AvailableSpells)
        disabled_spell_classes = {m.value for m in available_spells_flag.disabled}

        # Get all enabled spell prize classes
        enabled_spell_prizes: list[type[SpellPrize]] = [
            prize_class
            for spell_class, prize_class in spell_to_prize.items()
            if spell_class not in disabled_spell_classes
        ]

        # Calculate how many characters are available (for spell slot count)
        available_chars_flag = world.settings.get_flag(AvailableCharacters)
        charcount = min(
            len(available_chars_flag.enabled),
            world.settings.get_flag(MaxCharacters).value,
        )

        # Add all enabled spells to the pool
        # One Mokura-compliant spell goes to low-vol (required for Mokura fight)
        mokura_spell_options = [
            p
            for p in [
                StarRainSpellPrize,
                GenoWhirlSpellPrize,
                TerrorizeSpellPrize,
                PoisonGasSpellPrize,
            ]
            if p in enabled_spell_prizes and not is_debug_placed(p)
        ]
        spell_count = 0
        if mokura_spell_options:
            # Mokura spell goes to low-vol (unlocks one check)
            low_vol_other_prizes.append(random.choice(mokura_spell_options)())
            spell_count = 1

        if SuperJumpSpell not in disabled_spell_classes:
            if not is_debug_placed(SuperJumpSpellPrize):
                # Super Jump goes to low-vol (unlocks few checks)
                low_vol_other_prizes.append(SuperJumpSpellPrize())
                spell_count += 1

        remaining_spell_pool = [
            p()
            for p in enabled_spell_prizes
            if p not in [type(q) for q in must_include] and not is_debug_placed(p)
        ]

        # Add all other spells to the "optional" array so that shuffler doesn't
        # throw an error if some of them can't be placed
        # ie 4 or less characters available
        must_include.extend(
            random.sample(
                remaining_spell_pool,
                min(
                    len(remaining_spell_pool),
                    (charcount) * 6 - spell_count,
                ),
            )
        )

    if world.settings.isflag_enabled(ShuffleStarPieces):
        sp_prizes = [
            StarPiece1,
            StarPiece2,
            StarPiece3,
            StarPiece4,
            StarPiece5,
            StarPiece6,
            StarPiece7,
        ]
        progression_prizes.extend(
            [sp() for sp in sp_prizes[:progress_stars] if not is_debug_placed(sp)]
        )
        # Leftover star pieces go to post_progression_priority (after progressive cards/crystal shard)
        post_progression_priority.extend(
            [
                sp()
                for sp in sp_prizes[
                    progress_stars : world.settings.get_flag(TotalStarPieces).value
                ]
                if not is_debug_placed(sp)
            ]
        )

    if world.settings.isflag_enabled(BossShuffle):
        # Place disabled bosses (those not enabled in ShuffledBosses)
        shuffled_bosses_flag = world.settings.get_flag(ShuffledBosses)
        disabled_boss_types = {m.value for m in shuffled_bosses_flag.disabled}

        boss_locations = [
            l
            for l in world.locations.values()
            if isinstance(l, BossFightLocation) and l.originally_held is not None
        ]

        for loc in boss_locations:
            if loc.originally_held in disabled_boss_types:
                loc.set_prize(loc.originally_held())  # type: ignore
            elif not is_debug_placed(loc.originally_held):
                progression_prizes.append(loc.originally_held())  # type: ignore

    # Always exclude freestanding coin locations (not frog coins) from shuffling
    # except coin snake
    freestanding_coin_locations = [
        l
        for l in world.locations.values()
        if isinstance(l, StandingLocation)
        and not isinstance(l, ShipCoinSnakePuzzleLocation)
        and l.originally_held is not None
        and isinstance(l.originally_held(), CoinPrize)
        and not isinstance(l.originally_held(), FrogCoinPrize)
    ]
    for loc in freestanding_coin_locations:
        loc.set_prize(loc.originally_held())  # type: ignore

    if not world.settings.isflag_enabled(ShuffleCoins):
        coin_locations = [
            l
            for l in world.locations.values()
            if isinstance(l, StandingLocation)
            and l.originally_held is not None
            and isinstance(l.originally_held(), CoinPrize)
        ]
        for loc in coin_locations:
            loc.set_prize(loc.originally_held())  # type: ignore

    # Collect item pool, or set excluded items
    for loc in world.locations.values():
        if loc.originally_held is None:
            continue
        if loc.has_item:
            continue
        # all of these are already in the pool
        if isinstance(loc, CharacterRecruitmentLocation):
            if not world.settings.isflag_enabled(ShuffleCharacters):
                loc.set_prize(loc.originally_held())
            continue  # Characters handled here or in ShuffleCharacters block above
        elif isinstance(loc, StarPieceLocation):
            if not world.settings.isflag_enabled(ShuffleStarPieces):
                loc.set_prize(loc.originally_held())
            continue  # Star pieces handled here or in ShuffleStarPieces block above
        elif isinstance(loc, BossFightLocation):
            if not world.settings.isflag_enabled(BossShuffle):
                loc.set_prize(loc.originally_held())
            else:
                # Check if this location's boss is disabled in ShuffledBosses
                shuffled_bosses_flag = world.settings.get_flag(ShuffledBosses)
                disabled_boss_types = {m.value for m in shuffled_bosses_flag.disabled}
                if loc.originally_held in disabled_boss_types:
                    loc.set_prize(loc.originally_held())
            continue  # Bosses handled here or in BossShuffle block above
        elif isinstance(loc, SpellSlotLocation):
            if not world.settings.isflag_enabled(CharacterLearnedSpells):
                # Place original spell unless it's disabled in AvailableSpells
                spell_prize = loc.originally_held()
                if spell_prize is not None:
                    available_spells_flag = world.settings.get_flag(AvailableSpells)
                    disabled_spell_classes = {
                        m.value for m in available_spells_flag.disabled
                    }
                    # Check if this spell's class is disabled
                    if (
                        cast(SpellPrize, spell_prize).spell
                        not in disabled_spell_classes
                    ):
                        loc.set_prize(spell_prize)
                    # else: leave location empty (spell is excluded)
            continue  # Always continue - spells handled here or in CharacterLearnedSpells block above
        # special exclusions
        elif isinstance(loc, FrogDiscipleLocation):
            # nowhere to put it if shuffle shops is on but item shuffle is off
            if not world.settings.isflag_enabled(
                ShuffleShops
            ) or not world.settings.isflag_enabled(ShuffleItems):
                loc.set_prize(loc.originally_held())
                continue
        elif isinstance(loc, TreasureShopLocation):
            # nowhere to put it if shuffle shops is on but item shuffle is off
            if not world.settings.isflag_enabled(
                ShuffleShops
            ) or not world.settings.isflag_enabled(ShuffleItems):
                loc.set_prize(loc.originally_held())
                continue
        # made it this far? start setting
        elif not world.settings.isflag_enabled(ShuffleItems):
            loc.set_prize(loc.originally_held())
            continue
        elif isinstance(loc.originally_held(), StarEggPrize):
            if world.settings.isflag_enabled(NoStarEgg):
                continue
        elif isinstance(loc.originally_held(), EXPStarPrize):
            if not world.settings.isflag_enabled(EXPStarsAnywhere):
                loc.set_prize(loc.originally_held())
                continue
        elif isinstance(loc.originally_held(), MimicFightInitiatorPrize):
            if not world.settings.isflag_enabled(MimicsAnywhere):
                loc.set_prize(loc.originally_held())
                continue
        elif isinstance(loc.originally_held(), SlotsPrize):
            if not world.settings.isflag_enabled(SlotsAnywhere):
                loc.set_prize(loc.originally_held())
                continue
            else:
                # SlotsPrize goes to post_progression_priority (placed after progression)
                # Note: Has restricted placement (needs room with space for 5 NPCs)
                post_progression_priority.append(loc.originally_held())

                # Clear the vanilla slot machine NPCs from their original rooms
                # Room 334: NPCs 2-6
                room_334 = world.rooms._rooms[334]
                assert room_334 is not None, "Room 334 not found"
                for npc_target in [NPC_2, NPC_3, NPC_4, NPC_5, NPC_6]:
                    npc = room_334.get_npc_by_target_id(npc_target)
                    assert npc is not None, f"NPC {npc_target} not found in room 334"
                    npc._npc = EMPTY_NPC

                # Room 348: NPCs 2-6
                room_348 = world.rooms._rooms[348]
                assert room_348 is not None, "Room 348 not found"
                for npc_target in [NPC_2, NPC_3, NPC_4, NPC_5, NPC_6]:
                    npc = room_348.get_npc_by_target_id(npc_target)
                    assert npc is not None, f"NPC {npc_target} not found in room 348"
                    npc._npc = EMPTY_NPC

                # Room 349: NPCs 3-7
                room_349 = world.rooms._rooms[349]
                assert room_349 is not None, "Room 349 not found"
                for npc_target in [NPC_3, NPC_4, NPC_5, NPC_6, NPC_7]:
                    npc = room_349.get_npc_by_target_id(npc_target)
                    assert npc is not None, f"NPC {npc_target} not found in room 349"
                    npc._npc = EMPTY_NPC

                continue
        elif isinstance(loc.originally_held(), BeetlemaniaPrize):
            if not world.settings.isflag_enabled(ShuffleBeetlemania):
                loc.set_prize(loc.originally_held())
                continue
        elif isinstance(loc.originally_held(), InfiniteCoinsPrize):
            if not world.settings.isflag_enabled(ShuffleMagikoopaChest):
                loc.set_prize(loc.originally_held())
                continue
        elif isinstance(loc.originally_held(), WeddingGearPrize):
            if not world.settings.isflag_enabled(ShuffleWeddingGear):
                loc.set_prize(loc.originally_held())
                continue
        elif isinstance(
            loc.originally_held(), SuperSuitPrize
        ) and world.settings.isflag_enabled(RestrictSpecialEquips):
            # 50% chance of keeping super suit in its original location if threshold is 100
            if world.settings.is_flag_value(SuperJump2Threshold, 100):
                roll = random.randint(0, 1)
                if roll:
                    loc.set_prize(loc.originally_held())
                    continue
        elif isinstance(loc.originally_held(), RegularFireworksPrize):
            if world.settings.is_flag_value(FireworksSetting, FireworksOptions.VANILLA):
                loc.set_prize(loc.originally_held())
                continue
        # Check if item unlocks high-volume areas
        is_high_vol_item = [
            p for p in high_volume_key_items if isinstance(loc.originally_held(), p)
        ]
        if len(is_high_vol_item) > 0:
            high_vol_other_prizes.append(loc.originally_held())
            continue
        # Check if item unlocks low-volume areas
        is_low_vol_item = [
            p for p in low_volume_key_items if isinstance(loc.originally_held(), p)
        ]
        if len(is_low_vol_item) > 0:
            low_vol_other_prizes.append(loc.originally_held())
            continue
        # Check if item goes to post_progression_priority (progressive cards, crystal shard, exp stars)
        is_post_prog_item = [
            p for p in post_progression_include if isinstance(loc.originally_held(), p)
        ]
        if len(is_post_prog_item) > 0:
            post_progression_priority.append(loc.originally_held())
            continue
        is_important_item = [
            p for p in should_otherwise_include if isinstance(loc.originally_held(), p)
        ]
        if len(is_important_item) > 0:
            must_include.append(loc.originally_held())
            continue
        elif world.settings.is_flag_value(
            ItemQuality, ItemQualityOptions.ORIGINAL_POOL
        ):
            if isinstance(
                loc.originally_held(),
                (RecoveryMushroomPrize, FrogCoin1Prize),
            ):
                not_important.append(loc.originally_held())
            else:
                must_include.append(loc.originally_held())
            continue
        if world.settings.is_flag_value(ItemQuality, ItemQualityOptions.ORIGINAL_POOL):
            not_important.append(loc.originally_held())
        else:
            not_important.append(RandomPrizeSubstitute().generate(world, loc))

    # Safety net: ensure these prize types end up in the pool if not already placed or queued
    for prize_class in [
        YouMissed,
        LuckyJewelPrize,
        SignalRingPrize,
        GoodieBagPrize,
        StarEggPrize,
    ]:
        # Check if already assigned to a location
        if any(
            loc.has_item and isinstance(loc.prize, prize_class)
            for loc in world.locations.values()
        ):
            continue
        # Check if already in must_include
        if any(isinstance(p, prize_class) for p in must_include):
            continue
        # Check if already in should_otherwise_include
        if prize_class in should_otherwise_include:
            continue
        # Not found anywhere — add an instance to must_include so it gets placed
        must_include.append(prize_class())

    # Build progression_prizes with 80% bias toward high-volume items
    # Priority order: high-vol chars > high-vol other > low-vol chars > low-vol other
    # Within each tier, 80% chance to pick from that tier before moving to next
    random.shuffle(high_vol_character_prizes)
    random.shuffle(high_vol_other_prizes)
    random.shuffle(low_vol_character_prizes)
    random.shuffle(low_vol_other_prizes)

    # Build progression prizes with bias: 80% chance to exhaust current tier before moving on
    prize_tiers = [
        high_vol_character_prizes,
        high_vol_other_prizes,
        low_vol_character_prizes,
        low_vol_other_prizes,
    ]

    for tier in prize_tiers:
        while tier:
            # 80% chance to take from current tier, 20% chance to defer to next tier
            if random.random() < 0.8:
                progression_prizes.append(tier.pop(0))
            else:
                break

    # Add any remaining items from all tiers
    for tier in prize_tiers:
        progression_prizes.extend(tier)

    # Debug: log pool sizes before placement
    _debug = world.settings.debug_mode
    if _debug:
        empty_locs = sum(1 for l in world.locations.values() if not l.has_item)
        total_pool = (
            len(restricted_prizes)
            + len(progression_prizes)
            + len(post_progression_priority)
            + len(must_include)
            + len(not_important)
        )
        print(
            f"\n[DEBUG] Pool sizes: restricted={len(restricted_prizes)}, progression={len(progression_prizes)}, "
            f"post_prog={len(post_progression_priority)}, must_include={len(must_include)}, "
            f"not_important={len(not_important)} | total={total_pool} items, {empty_locs} empty locations"
        )
        if total_pool < empty_locs:
            print(
                f"[DEBUG] WARNING: {empty_locs - total_pool} locations will remain empty (fewer items than locations)"
            )

    # Shuffle!
    # Place items with restricted placement options first (e.g., SlotsPrize)
    # These must be placed before other items fill up their limited eligible locations
    if restricted_prizes:
        random.shuffle(restricted_prizes)
        place(
            world,
            restricted_prizes,
            on_placed=lambda i, l: _on_item_placed(world, i, l),
            debug_label="restricted" if _debug else None,
        )

    # Place critical/progress items (with high-vol bias applied)
    place(
        world,
        progression_prizes,
        on_placed=lambda i, l: _on_item_placed(world, i, l),
        debug_label="progression" if _debug else None,
    )

    # Place post-progression priority items (slots/exp stars, progressive cards, crystal shard)
    if post_progression_priority:
        random.shuffle(post_progression_priority)
        place(
            world,
            post_progression_priority,
            on_placed=lambda i, l: _on_item_placed(world, i, l),
            debug_label="post_progression" if _debug else None,
        )

    random.shuffle(must_include)
    place(
        world,
        must_include,
        on_placed=lambda i, l: _on_item_placed(world, i, l),
        force_frog_disciple=True,
        debug_label="must_include" if _debug else None,
    )

    random.shuffle(not_important)
    place(
        world,
        not_important,
        True,
        on_placed=lambda i, l: _on_item_placed(world, i, l),
        force_frog_disciple=True,
        debug_label="not_important" if _debug else None,
    )

    # Debug: post-placement diagnostic
    if _debug:
        from ..placement import diagnose_empty_locations

        diagnose_empty_locations(world)


def assign_spell_prize_models(world: GameWorld) -> None:
    """Assign spell prize models and packet data based on their element.

    This sets the visual appearance (colored orb) for spell prizes when they
    appear as freestanding items in the overworld:
    - Thunder spells → Yellow orb (SPR0218_YELLOW_BALL)
    - Fire spells → Red orb (SPR0214_RED_BALL)
    - Ice spells → Blue orb (SPR0215_BLUE_BALL)
    - Jump/Earth spells → Green orb (SPR0217_GREEN_BALL)
    - No element spells → Gray orb (SPR0224_GRAY_BALL)

    Also sets packet_data to (sprite_id, 0) for each spell prize based on element.

    Must run after spell elements are finalized and after prizes are shuffled into locations.
    """
    from ...types.prize import SpellPrize
    from ...data.physical_objects.items import (
        YellowSpellObject,
        FireSpellObject,
        BlueSpellObject,
        GreenSpellObject,
        GraySpellObject,
    )
    from ...data.variables.sprite_names import (
        SPR0214_RED_BALL,
        SPR0215_BLUE_BALL,
        SPR0217_GREEN_BALL,
        SPR0218_YELLOW_BALL,
        SPR0224_GRAY_BALL,
    )
    from smrpgpatchbuilder.datatypes.spells.enums import Element

    # Iterate through all locations to find spell prizes
    for location in world.locations.values():
        if not location.has_item:
            continue

        prize = location.prize
        if not isinstance(prize, SpellPrize):
            continue

        # Get the actual spell instance from world with its finalized element
        spell_instance = world.get_spell(prize.spell)

        # Map element to orb model and packet sprite
        if spell_instance.element == Element.THUNDER:
            prize.set_model(YellowSpellObject)
            prize._packet_data = (SPR0218_YELLOW_BALL, 0)
        elif spell_instance.element == Element.FIRE:
            prize.set_model(FireSpellObject)
            prize._packet_data = (SPR0214_RED_BALL, 0)
        elif spell_instance.element == Element.ICE:
            prize.set_model(BlueSpellObject)
            prize._packet_data = (SPR0215_BLUE_BALL, 0)
        elif spell_instance.element == Element.JUMP:
            prize.set_model(GreenSpellObject)
            prize._packet_data = (SPR0217_GREEN_BALL, 0)
        else:  # Element.NONE
            prize.set_model(GraySpellObject)
            prize._packet_data = (SPR0224_GRAY_BALL, 0)


def post_shuffle_cleanup(world: GameWorld) -> None:
    """Handle empty chests and replace low-value items with coins.

    This function:
    1. Assigns spell prize models based on finalized elements
    2. Fills or disables empty treasure chests based on settings
    3. Replaces low-impact items with coin prizes at half their price
    """
    from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
        DisableObjectTriggerInSpecificLevel,
        JmpIfBitClear,
    )
    from ...types.flags import (
        AnnoyingChests,
        EquipmentProperties,
        EquipmentPropertiesOptions,
        StarPieceHints,
    )
    from ...types.prizelocation import (
        TreasureChestLocation,
        StandardPrizeLocation,
        RiverLocation,
        StandingLocation,
        SIGNAL_RING_EVENT_DICT,
    )
    from ...types.prize import ItemPrize, CoinPrize, StarPiecePrize
    from ...progression.prizes import YouMissed, Coins10Prize
    from ...data.items.items import (
        MushroomItem,
        HoneySyrupItem,
        AbleJuiceItem,
        YoshiCookieItem,
        PureWaterItem,
        FroggieDrinkItem,
        WiltShroomItem,
        RottenMushItem,
        MoldyMushItem,
        MushroomItem2,
    )

    # First, assign spell prize models based on their finalized elements
    assign_spell_prize_models(world)

    # Replace as necessary
    for loc in [
        s for s in world.locations.values() if isinstance(s, TreasureChestLocation)
    ]:
        if not loc.has_item:
            if world.settings.isflag_enabled(AnnoyingChests):
                loc.set_prize(YouMissed())
            else:
                disable = zip(loc._rooms, loc._npc_ids)
                for room, npc in disable:
                    world.event_2496_startup.append(
                        DisableObjectTriggerInSpecificLevel(npc, room)
                    )

    # Verify that all locations that need prizes are filled
    for loc in world.locations.values():
        if loc.has_item:
            continue
        if loc.can_be_empty(world):
            continue  # Location is allowed to be empty
        print(f"Error: Location {loc} is empty but cannot be empty based on settings")
        raise PlacementException(0, [])

    for loc in [
        s
        for s in world.locations.values()
        if s.has_item
        and isinstance(s, StandardPrizeLocation)
        and not isinstance(s, RiverLocation)
    ]:
        if isinstance(loc.prize, ItemPrize) and (
            isinstance(
                loc.prize,
                (
                    MushroomItem,
                    HoneySyrupItem,
                    AbleJuiceItem,
                    YoshiCookieItem,
                    PureWaterItem,
                    FroggieDrinkItem,
                    WiltShroomItem,
                    RottenMushItem,
                    MoldyMushItem,
                    MushroomItem2,
                ),
            )
            or (
                not world.settings.is_flag_value(
                    EquipmentProperties, EquipmentPropertiesOptions.SOME
                )
                and type(loc.prize) in world.low_impact_equip
            )
        ):
            if isinstance(loc, StandingLocation):
                loc.set_prize(Coins10Prize())
            else:
                loc.set_prize(CoinPrize(world.get_item(loc.prize.item).price // 2))

    if world.settings.isflag_enabled(StarPieceHints):
        for l in world.locations.values():
            if not isinstance(l.prize, StarPiecePrize):
                continue
            event = SIGNAL_RING_EVENT_DICT[l.world_area]
            script = world.event_scripts.get_script_by_id(event)
            assert (
                script is not None
            ), f"Event script {event} not found for StarPieceHints"
            script.insert_before_nth_command(
                0, JmpIfBitClear(l.prize._hint, [f"EVENT_{event}_play_sound"])
            )
