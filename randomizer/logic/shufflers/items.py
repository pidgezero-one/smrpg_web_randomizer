"""Item and prize shuffling logic."""

from __future__ import annotations
import os
import random
from copy import copy
from datetime import datetime
from typing import TYPE_CHECKING, cast

from randomizer.types.item import Equipment
from smrpgpatchbuilder.datatypes.spells.enums import Status, Element

from ...data.items import (
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

from ..placement import PlacementException, place, collect_accessible_items
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
    InfuseSpellElements,
    ReplaceItems,
    SeeYa,
    ShopQualities,
    ShopQuality,
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
    InvisibleFlagLocation,
    PacketLocation,
    RiverLocation,
    StarPieceLocation,
    BossFightLocation,
    SpellSlotLocation,
    FrogDiscipleLocation,
    TreasureChestLocation,
    StartingCharacterLocation,
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
    HammerBrosFight,
    MackBossFight,
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

TIERS_CAN_OVERFLOW = [LOW_PRIORITY]

TIER_NAMES = {
    PROGRESSION_PRIZES: "PROGRESSION",
    RESTRICTED_PRIZES: "RESTRICTED",
    MANDATORY_INCLUSIONS: "MANDATORY_INCLUSIONS",
    LOW_PRIORITY: "LOW_PRIORITY",
}


def _dump_placement_failure(
    world: GameWorld,
    pool_before: dict[int, list[str]],
    unplaced_items: list[str],
    priority_classes: set[type[Prize]] | None = None,
) -> str:
    """Write a debug dump to a timestamped file when placement fails.

    Returns the path to the written file.
    """
    from ..placement import collect_accessible_items

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_dir = os.path.join(
        os.path.dirname(__file__), "..", "..", "debug", "placement_logs"
    )
    os.makedirs(log_dir, exist_ok=True)
    filepath = os.path.join(log_dir, f"placement_fail_{timestamp}.txt")

    player_has = collect_accessible_items(world)

    lines: list[str] = []
    lines.append(f"PLACEMENT FAILURE - {datetime.now().isoformat()}")
    lines.append("=" * 80)

    # 1) Pool contents before placement, by tier
    lines.append("")
    lines.append("POOL BEFORE PLACEMENT (by tier)")
    lines.append("-" * 40)
    for tier_id in sorted(pool_before.keys()):
        tier_name = TIER_NAMES.get(tier_id, f"TIER_{tier_id}")
        items = pool_before[tier_id]
        lines.append(f"  {tier_name} ({len(items)} items):")
        for item_name in sorted(items):
            lines.append(f"    - {item_name}")

    # 2) Priority classes used for placement
    lines.append("")
    lines.append("PRIORITY CLASSES (high-volume items)")
    lines.append("-" * 40)
    if priority_classes:
        for cls_name in sorted(cls.__name__ for cls in priority_classes):
            lines.append(f"  - {cls_name}")
    else:
        lines.append("  (none)")

    # 3) Unplaceable items
    lines.append("")
    lines.append(f"UNPLACEABLE ITEMS ({len(unplaced_items)})")
    lines.append("-" * 40)
    for name in sorted(unplaced_items):
        lines.append(f"  - {name}")

    # 3) Already placed items and their locations
    placed: list[tuple[str, str]] = []
    for loc in world.locations.values():
        if loc.has_item:
            placed.append((type(loc).__name__, type(loc.prize).__name__))
    placed.sort()

    lines.append("")
    lines.append(f"PLACED ITEMS ({len(placed)})")
    lines.append("-" * 40)
    for loc_name, prize_name in placed:
        lines.append(f"  {loc_name}: {prize_name}")

    # 4) Accessible locations with no item
    accessible_empty: list[str] = []
    for loc in world.locations.values():
        if loc.can_access(player_has, world) and not loc.has_item:
            accessible_empty.append(type(loc).__name__)
    accessible_empty.sort()

    lines.append("")
    lines.append(f"ACCESSIBLE EMPTY LOCATIONS ({len(accessible_empty)})")
    lines.append("-" * 40)
    for name in accessible_empty:
        lines.append(f"  - {name}")

    # 5) Inaccessible locations
    inaccessible: list[str] = []
    for loc in world.locations.values():
        if not loc.can_access(player_has, world):
            prize_info = type(loc.prize).__name__ if loc.has_item else "(empty)"
            inaccessible.append(f"{type(loc).__name__}: {prize_info}")
    inaccessible.sort()

    lines.append("")
    lines.append(f"INACCESSIBLE LOCATIONS ({len(inaccessible)})")
    lines.append("-" * 40)
    for entry in inaccessible:
        lines.append(f"  - {entry}")

    text = "\n".join(lines) + "\n"
    with open(filepath, "w") as f:
        f.write(text)

    print(f"[DEBUG] Placement failure dump written to: {filepath}")
    return filepath


def select_spells(world: GameWorld) -> list[type[Prize]]:
    # All 27 spell prize classes
    all_spell_prizes: list[type[Prize]] = [
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
    ]

    # Get excluded spell classes from AvailableSpells setting (for individual spell exclusions)
    available_spells_flag = world.settings.get_flag(AvailableSpells)
    excluded_spell_classes: set[type] = {
        m.value for m in available_spells_flag.disabled
    }

    # Map spell classes to their corresponding SpellPrize classes
    spell_to_prize: dict[type, type[Prize]] = {
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

    # Get excluded spell prize classes (from AvailableSpells setting)
    excluded_spell_prizes: set[type[Prize]] = {
        spell_to_prize[spell_cls]
        for spell_cls in excluded_spell_classes
        if spell_cls in spell_to_prize
    }

    # Build available spells list (all spells minus UI exclusions)
    available_spells: list[type[Prize]] = [
        sp for sp in all_spell_prizes if sp not in excluded_spell_prizes
    ]

    if not world.settings.isflag_enabled(CharacterLearnedSpells):
        # Characters learn their vanilla spells - return only those from
        # included characters' spell slots that aren't disabled
        return [
            loc.originally_held
            for loc in world.locations.values()
            if isinstance(loc, SpellSlotLocation)
            and loc.originally_held is not None
            and loc.originally_held not in excluded_spell_prizes
        ]

    selected_spells = []
    if SuperJumpSpellPrize in available_spells:
        selected_spells.append(SuperJumpSpellPrize)
    max_characters = world.settings.get_flag(MaxCharacters).value
    target_spell_count = min(27, 6 * max_characters) - len(selected_spells)
    remaining_spells = [a for a in available_spells if a not in selected_spells]
    # Select random spells up to target count (or all available if fewer)
    random.shuffle(remaining_spells)
    selected_spells.extend(remaining_spells[:target_spell_count])
    return selected_spells


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

    # Tier 4: Other prizes that don't unlock anything but are still mandatory to include
    # These can include unpurchase-able items, for example
    should_otherwise_include_rules: list[type[Prize]] = [
        ProgressiveEggPrize,
        CrystalShardPrize,
        ProgressiveCardPrize,
        EarlierTimesPrize,
        CoinTrickPrize,
        ExpBoosterPrize,
        ScroogeRingPrize,
        LuckyJewelPrize,
    ]
    if not world.settings.isflag_enabled(SeeYa):
        should_otherwise_include_rules.append(SeeYaPrize)

    # All boss fights are progress because they each unlock one star piece check at minimum.
    for prize_cls in BossFightPrize.__subclasses__():
        progress_rules.append(prize_cls)
    # Prizes that unlock progress depending on settings
    # Character recruitment prize handling
    # Map character names to their prize classes
    all_character_prizes: dict[str, type[CharacterPrize]] = {
        "Mario": MarioRecruitmentPrize,
        "Mallow": MallowRecruitmentPrize,
        "Geno": GenoRecruitmentPrize,
        "Bowser": BowserRecruitmentPrize,
        "Toadstool": ToadstoolRecruitmentPrize,
    }

    # Get excluded characters from AvailableCharacters setting
    available_chars_flag = world.settings.get_flag(AvailableCharacters)
    excluded_char_names: set[str] = {
        m.value.name for m in available_chars_flag.disabled
    }
    selected_spells = select_spells(world)

    non_elemental_spell_prizes: list[type[Prize]] = [
        prize
        for prize in [
            StarRainSpellPrize,
            GenoWhirlSpellPrize,
            GenoBlastSpellPrize,
            TerrorizeSpellPrize,
            PoisonGasSpellPrize,
        ]
        if prize in selected_spells
    ]
    if not world.settings.isflag_enabled(InfuseSpellElements):
        non_elemental_spell_prizes.extend(
            [
                prize
                for prize in [
                    GenoBeamSpellPrize,
                    GenoFlashSpellPrize,
                    CrusherSpellPrize,
                    BowserCrushSpellPrize,
                    PsychBombSpellPrize,
                ]
                if prize in selected_spells
            ]
        )
    if len(non_elemental_spell_prizes) == 0:
        raise ValueError(
            "No non-elemental spells are available to assign to progress rules. At least one non-elemental spell must be included in the seed for progression purposes."
        )

    # Place up to 3 non-elemental spells in progression tier to ensure
    # MokuraBossFight (and similar) can be placed (they require a non-elemental
    # spell to be accessible). Use fewer if not enough are available.
    random.shuffle(non_elemental_spell_prizes)
    progression_nonelementals = non_elemental_spell_prizes[
        : min(2, len(non_elemental_spell_prizes))
    ]

    # Characters required for spell progression (when spells are vanilla)
    spell_required_chars: set[type[CharacterPrize]] = set()
    if not world.settings.isflag_enabled(
        CharacterLearnedSpells
    ) and not world.settings.isflag_enabled(SpellsAnywhere):
        # Mario must be in progression (always has Jump for combat)
        spell_required_chars.add(MarioRecruitmentPrize)
        # Characters who learn the selected progression non-elemental spells
        spell_to_character: dict[type[Prize], type[CharacterPrize]] = {
            StarRainSpellPrize: MallowRecruitmentPrize,
            GenoWhirlSpellPrize: GenoRecruitmentPrize,
            GenoBlastSpellPrize: GenoRecruitmentPrize,
            TerrorizeSpellPrize: BowserRecruitmentPrize,
            PoisonGasSpellPrize: BowserRecruitmentPrize,
            GenoBeamSpellPrize: GenoRecruitmentPrize,
            GenoFlashSpellPrize: GenoRecruitmentPrize,
            CrusherSpellPrize: BowserRecruitmentPrize,
            BowserCrushSpellPrize: BowserRecruitmentPrize,
            PsychBombSpellPrize: ToadstoolRecruitmentPrize,
        }
        for spell in progression_nonelementals:
            char = spell_to_character.get(spell)
            if char is not None:
                spell_required_chars.add(char)

    # Assign selected spells to tiers
    for spell in selected_spells:
        if spell in progression_nonelementals or issubclass(spell, SuperJumpSpellPrize):
            progress_rules.append(spell)
        else:
            should_otherwise_include_rules.append(spell)

    # Get MaxCharacters setting
    max_characters = world.settings.get_flag(MaxCharacters).value

    # Determine which characters are required for progression
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

    # Collect characters required for progression
    progression_required_chars: set[type[CharacterPrize]] = set()
    for prize_cls, gating_info in conditional_progress.items():
        if not issubclass(prize_cls, CharacterPrize):
            continue  # Just a sanity check, all keys here should be CharacterPrize subclasses
        for gate, gating_flag in gating_info:
            if world.settings.is_flag_value(gate, gating_flag):
                progression_required_chars.add(prize_cls)
                break

    # Add characters required by spell progression (vanilla spells)
    progression_required_chars |= spell_required_chars

    # Map prize class to character name for validation
    prize_to_name: dict[type[CharacterPrize], str] = {
        v: k for k, v in all_character_prizes.items()
    }

    # Validation: Check if any progression-required character is excluded
    for prize_cls in progression_required_chars:
        char_name = prize_to_name.get(prize_cls)
        if char_name and char_name in excluded_char_names:
            raise ValueError(
                f"Character '{char_name}' is required for progression but has been excluded in settings."
            )

    # Validation: Check if MaxCharacters < number of progression-required characters
    if max_characters < len(progression_required_chars):
        raise ValueError(
            f"MaxCharacters ({max_characters}) is less than the number of characters "
            f"required for progression ({len(progression_required_chars)}). "
            f"Required characters: {[prize_to_name[c] for c in progression_required_chars]}"
        )

    # Calculate available (non-excluded) characters
    available_char_prizes: set[type[CharacterPrize]] = {
        prize_cls
        for name, prize_cls in all_character_prizes.items()
        if name not in excluded_char_names
    }

    # Validation: Check if MaxCharacters can be fulfilled with available characters
    if max_characters > len(available_char_prizes):
        raise ValueError(
            f"MaxCharacters ({max_characters}) cannot be fulfilled. "
            f"Only {len(available_char_prizes)} characters are available after exclusions."
        )

    # Add progression-required characters to progress_rules
    for prize_cls in progression_required_chars:
        progress_rules.append(prize_cls)

    # Determine how many additional characters we can add to should_otherwise_include_rules
    remaining_slots = max_characters - len(progression_required_chars)

    # Get non-progression, non-excluded characters
    non_progression_available: list[type[CharacterPrize]] = [
        prize_cls
        for prize_cls in available_char_prizes
        if prize_cls not in progression_required_chars
    ]

    # Randomly select characters to fill remaining slots
    if remaining_slots > 0 and non_progression_available:
        # Select up to remaining_slots characters randomly
        chars_to_include = random.sample(
            non_progression_available,
            min(remaining_slots, len(non_progression_available)),
        )
    else:
        chars_to_include = []

    # These will be added to should_otherwise_include_rules later

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
    if not world.settings.isflag_enabled(ShuffleShops):
        should_otherwise_include_rules.extend(
            [
                FryingPanPrize,
            ]
        )
    # Guarantee transformative equips
    if not world.settings.is_flag_value(ShopQuality, ShopQualities.ORIGINAL):
        should_otherwise_include_rules.extend(
            [
                JumpShoesPrize,
                BtubRingPrize,
            ]
        )
    # Add all spells except Super Jump and the chosen non-elemental
    if not world.settings.isflag_enabled(NoStarEgg):
        should_otherwise_include_rules.extend([StarEggPrize])

    # Add non-progression characters that were randomly selected to fill remaining slots
    should_otherwise_include_rules.extend(chars_to_include)
    if world.settings.isflag_enabled(ShuffleBeetlemania):
        should_otherwise_include_rules.append(BeetlemaniaPrize)
    should_otherwise_include_rules.extend(
        [SignalRingPrize, GoodieBagPrize, YouMissed]
    )

    if world.settings.isflag_enabled(RestrictSpecialEquips):
        should_otherwise_include_rules.extend(
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
                WonderChompPrize,
                Stella023Prize,
                SageStickPrize,
                EnduringBroochPrize,
                TeamworkBandPrize,
            ]
        )

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

    stars = [
        StarPiece1,
        StarPiece2,
        StarPiece3,
        StarPiece4,
        StarPiece5,
        StarPiece6,
        StarPiece7,
    ]
    for i in range(progress_stars):
        if i < progress_stars:
            progress_rules.append(stars[i])
        elif i < maxstars:
            should_otherwise_include_rules.append(stars[i])

    # Add spells to mandatory inclusions tier with characters

    return {
        PROGRESSION_PRIZES: copy(progress_rules),
        RESTRICTED_PRIZES: copy(post_progression_rules),
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
            PacketLocation,
            InvisibleFlagLocation,
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
        if issubclass(location.originally_held, CoinPrize) and isinstance(
            location, StandingLocation
        ):
            return False
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
        if issubclass(
            location.originally_held, WeddingGearPrize
        ) and not world.settings.isflag_enabled(ShuffleWeddingGear):
            return False
        if (
            issubclass(location.originally_held, SpellPrize)
            and not world.settings.isflag_enabled(CharacterLearnedSpells)
            and not world.settings.isflag_enabled(SpellsAnywhere)
        ):
            return False
        if issubclass(
            location.originally_held, RegularFireworksPrize
        ) and world.settings.is_flag_value(FireworksSetting, FireworksOptions.VANILLA):
            return False
    if not world.is_location_enabled(type(location)):
        return False
    if location.originally_held == SuperSuitPrize and world.settings.is_flag_value(
        SuperJump2Threshold, 100
    ):
        roll = random.randint(0, 1)
        if roll == 1:
            return False
    return True


def pull_prize(location: PrizeLocation, world: GameWorld) -> Prize | None:
    # empty locations don't return anything
    if location.originally_held is None:
        return None
    # special case
    if issubclass(location.originally_held, SpellPrize):
        return None
    if issubclass(
        location.originally_held, SeeYaPrize
    ) and world.settings.isflag_enabled(SeeYa):
        return None
    # always return the original prize if shuffling disabled so that it can receive its original prize during placement
    # this should happen regardless of item shuffler pool settings
    if not should_shuffle(location, world):
        return location.originally_held()
    inclusions = shuffle_rules(world)
    # Ignore excluded star pieces and characters
    if issubclass(location.originally_held, (StarPiecePrize, CharacterPrize)):
        for _, classes in inclusions.items():
            for cls in classes:
                if issubclass(location.originally_held, cls):
                    return cls()
        return None
    if issubclass(
        location.originally_held, RegularFireworksPrize
    ) and not world.settings.is_flag_value(FireworksSetting, FireworksOptions.VANILLA):
        return ProgressiveFireworksPrize()
    if issubclass(
        location.originally_held, StarEggPrize
    ) and world.settings.isflag_enabled(NoStarEgg):
        return None
    if issubclass(location.originally_held, (CharacterPrize, StarPiecePrize)):
        for tier in inclusions.values():
            for prize_cls in tier:
                if issubclass(location.originally_held, prize_cls):
                    return location.originally_held()
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
        for tier, prizes in inclusions.items():
            for prize_cls in prizes:
                if tier == LOW_PRIORITY and world.settings.is_flag_value(
                    ItemQuality, ItemQualityOptions.COMPLETELY_EMPTY
                ):
                    return None
                if issubclass(location.originally_held, prize_cls):
                    return location.originally_held()
        if world.settings.is_flag_value(
            ItemQuality, ItemQualityOptions.COMPLETELY_EMPTY
        ):
            return None

        if world.settings.is_flag_value(ItemQuality, ItemQualityOptions.ORIGINAL_POOL):
            prize = location.originally_held()
        else:
            prize = RandomPrizeSubstitute().generate(world, location)

        if world.settings.isflag_enabled(ReplaceItems) and issubclass(
            location.originally_held, ItemPrize
        ):
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
                and Status.INVINCIBLE
                not in world.get_item(MushroomItem2).status_immunities
            ):
                prize = CoinPrize(world.get_item(item).price)
        return prize

    return location.originally_held()


def remove_prize_from_pool(
    pool: dict[int, list[Prize]], prize_class: type[Prize], world: GameWorld
) -> None:
    """Remove the first instance of a prize class from the pool dict.

    Traverses all tiers in the pool dict and removes the first prize that is an
    instance of the specified class.

    Args:
        pool: The pool dict mapping tier IDs to lists of Prize instances.
        prize_class: The prize class to remove an instance of.

    Returns:
        True if an instance was found and removed, False otherwise.
    """
    for tier in pool:
        for i, prize in enumerate(pool[tier]):
            if isinstance(prize, prize_class):
                pool[tier].pop(i)
                return
    # certain force-included debug items that aren't normally found in a prize location are fine
    pr = prize_class()
    if isinstance(pr, ItemPrize) and world.get_item(pr.item).price > 0:
        return
    raise ValueError(
        f"Prize of class {prize_class} not found in pool when attempting to remove. Was it already set to a debug location?"
    )


def _build_priority_classes(world: GameWorld) -> set[type[Prize]]:
    """Build the set of high-unlock-volume prize types for priority placement.

    These items unlock many downstream checks, so they should be placed
    earlier and spread throughout the placement order rather than clumping
    at the end.
    """
    priority: set[type[Prize]] = {
        BambinoBombPrize,
        CastleKey1Prize,
        CastleKey2Prize,
        GoldPaintPrize,
        StayVoucherPrize,
        TempleKeyPrize,
    }

    # MarioDollPrize if Booster Tower completion gates downstream areas
    if world.settings.is_flag_value(
        BoosterHillGate, BoosterHillGating.TOWER
    ) or world.settings.is_flag_value(MarrymoreGate, MarrymoreGating.TOWER):
        priority.add(MarioDollPrize)

    # Star pieces if any area is star-gated
    if (
        world.settings.is_flag_value(SeaGate, SeaGating.STAR_4)
        or world.settings.is_flag_value(LandsEndGate, LandsEndGating.STAR_5)
        or world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.STAR_6)
        or world.settings.is_flag_value(FactoryGate, FactoryGating.STAR_6)
    ):
        priority.add(StarPiecePrize)

    # Boss fights that are required for gating in AreaAccessSubcategory flags
    boss_gating: list[tuple[type, object, type[Prize]]] = [
        (BanditsWayGate, BanditsWayGating.HAMMER_BRO, HammerBrosFight),
        (KeroSewersGate, KeroSewersGating.MACK, MackBossFight),
        (PipeVaultGate, PipeVaultGating.BOWYER, BowyerBossFight),
        (Moleville1Gate, Moleville1Gating.BOWYER, BowyerBossFight),
        (BoosterTowerGate, BoosterTowerGating.PUNCHINELLO, PunchinelloBossFight),
        (BoosterHillGate, BoosterHillGating.KGGG, KnifeGuyGrateGuyBossFight),
        (MarrymoreGate, MarrymoreGating.KGGG, KnifeGuyGrateGuyBossFight),
        (SeaGate, SeaGating.BUNDT, BundtBossFight),
        (YaridovichGate, YaridovichGating.JOHNNY, JohnnyBossFight),
        (LandsEndGate, LandsEndGating.YARIDOVICH, YaridovichBossFight),
        (MonstroTownGate, MonstroTownGating.BELOME_2, Belome2BossFight),
        (NimbusGate, NimbusGating.MEGASMILAX, MegasmilaxBossFight),
        (BarrelVolcanoGate, BarrelVolcanoGating.VALENTINA, ValentinaBossFight),
        (BowsersKeepGate, BowsersKeepGating.AXEM, AxemRangersBossFight),
    ]
    for gate, gating_value, boss_prize in boss_gating:
        if world.settings.is_flag_value(gate, gating_value):
            priority.add(boss_prize)

    # Conditional key items
    if world.settings.is_flag_value(LandsEndGate, LandsEndGating.ELDER):
        priority.add(ShedKeyPrize)

    if world.settings.is_flag_value(KeroSewersGate, KeroSewersGating.RFC):
        priority.add(RareFrogCoinPrize)

    if world.settings.is_flag_value(ForestMazeGate, ForestMazeGating.PIE):
        priority.add(CricketPiePrize)

    # Characters that are required by active gating settings (gate-critical)
    character_gating: list[tuple[type, object, type[Prize]]] = [
        (BanditsWayGate, BanditsWayGating.MALLOW, MallowRecruitmentPrize),
        (KeroSewersGate, KeroSewersGating.MALLOW, MallowRecruitmentPrize),
        (BoosterTowerGate, BoosterTowerGating.MALLOW, MallowRecruitmentPrize),
        (PipeVaultGate, PipeVaultGating.GENO, GenoRecruitmentPrize),
        (Moleville1Gate, Moleville1Gating.GENO, GenoRecruitmentPrize),
        (BoosterTowerGate, BoosterTowerGating.GENO, GenoRecruitmentPrize),
        (BoosterTowerGate, BoosterTowerGating.MARIO, MarioRecruitmentPrize),
        (BoosterTowerGate, BoosterTowerGating.TOADSTOOL, ToadstoolRecruitmentPrize),
        (SeaGate, SeaGating.TOADSTOOL, ToadstoolRecruitmentPrize),
        (BoosterTowerGate, BoosterTowerGating.BOWSER, BowserRecruitmentPrize),
    ]
    for gate, gating_value, char_prize in character_gating:
        if world.settings.is_flag_value(gate, gating_value):
            priority.add(char_prize)

    return priority


def shuffle_prizes(world: GameWorld) -> None:
    pool: dict[int, list[Prize]] = {
        PROGRESSION_PRIZES: [],
        RESTRICTED_PRIZES: [],
        MANDATORY_INCLUSIONS: [],
        LOW_PRIORITY: [],
    }
    # Always have 3 progressive eggs if item shuffle is enabled
    if world.settings.isflag_enabled(ShuffleItems):
        pool[MANDATORY_INCLUSIONS].extend(
            [ProgressiveEggPrize(), ProgressiveEggPrize()]
        )
        if not world.settings.is_flag_value(ShopQuality, ShopQualities.ORIGINAL):
            pool[MANDATORY_INCLUSIONS].extend(
                [
                    JumpShoesPrize(),
                    BtubRingPrize(),
                ]
            )

    # Reset spell assignments for SpellsAnywhere
    world._spell_assignments = None

    rules = shuffle_rules(world)

    # Empty every location and build the prize pool
    all_locations = list(world.locations.values())

    pre_seeded = sum(len(p) for p in pool.values())

    # Spells are a special case - added from rules, not pulled from locations
    spell_count = 0
    for tier, classes in rules.items():
        for cls in classes:
            if issubclass(cls, SpellPrize):
                pool[tier].append(cls())
                spell_count += 1

    pulled_count = 0
    for loc in all_locations:
        loc.set_prize(None)
        pool_item = pull_prize(loc, world)

        if pool_item is None:
            continue
        pulled_count += 1

        included = False
        for tier, classes in rules.items():
            if any(isinstance(pool_item, cls) for cls in classes):
                pool[tier].append(pool_item)
                included = True
                break
        if not included:
            if world.settings.is_flag_value(
                ItemQuality, ItemQualityOptions.ORIGINAL_POOL
            ):
                pool[MANDATORY_INCLUSIONS].append(pool_item)
            else:
                pool[LOW_PRIORITY].append(pool_item)

    pool_total = sum(len(p) for p in pool.values())
    if pool_total != pre_seeded + spell_count + pulled_count:
        # Dump full pool contents to find the extras
        pool_contents: dict[str, int] = {}
        for tier_prizes in pool.values():
            for p in tier_prizes:
                name = type(p).__name__
                pool_contents[name] = pool_contents.get(name, 0) + 1
        print(f"[DEBUG] Full pool contents: {dict(sorted(pool_contents.items()))}")
    # remove slot machine npcs from their original rooms
    room_334 = world.rooms._rooms[334]
    assert room_334 is not None, "Room 334 not found"
    for npc_target in [NPC_2, NPC_3, NPC_4, NPC_5, NPC_6]:
        npc = room_334.get_npc_by_target_id(npc_target)
        assert npc is not None, f"NPC {npc_target} not found in room 334"
        npc._npc = EMPTY_NPC
    room_348 = world.rooms._rooms[348]
    assert room_348 is not None, "Room 348 not found"
    for npc_target in [NPC_2, NPC_3, NPC_4, NPC_5, NPC_6]:
        npc = room_348.get_npc_by_target_id(npc_target)
        assert npc is not None, f"NPC {npc_target} not found in room 348"
        npc._npc = EMPTY_NPC
    room_349 = world.rooms._rooms[349]
    assert room_349 is not None, "Room 349 not found"
    for npc_target in [NPC_3, NPC_4, NPC_5, NPC_6, NPC_7]:
        npc = room_349.get_npc_by_target_id(npc_target)
        assert npc is not None, f"NPC {npc_target} not found in room 349"
        npc._npc = EMPTY_NPC

    # Build mapping of starting character locations to their index (0-4)
    starting_char_locations: dict[type, int] = {
        StartingCharacter1: 0,
        StartingCharacter2: 1,
        StartingCharacter3: 2,
        StartingCharacter4: 3,
        StartingCharacter5: 4,
    }

    # Map ally names to character prizes
    ally_name_to_prize: dict[str, type[CharacterPrize]] = {
        "Mario": MarioRecruitmentPrize,
        "Mallow": MallowRecruitmentPrize,
        "Geno": GenoRecruitmentPrize,
        "Bowser": BowserRecruitmentPrize,
        "Toadstool": ToadstoolRecruitmentPrize,
    }

    # Get starting characters from settings (resolved, so Random_X are actual allies)
    starting_chars_flag = world.settings.get_flag(StartingCharacters)
    resolved_starting_chars = starting_chars_flag.resolve_random_selections()

    # Fill statically set locations
    for loc in world.locations.values():
        # Handle starting character locations based on settings
        if isinstance(loc, StartingCharacterLocation):
            loc_idx = starting_char_locations.get(type(loc))
            if loc_idx is not None and loc_idx < len(resolved_starting_chars):
                ally = resolved_starting_chars[loc_idx]
                if ally and hasattr(ally, "name") and ally.name in ally_name_to_prize:
                    prize_cls = ally_name_to_prize[ally.name]
                    # Check if this character is in the pool (not excluded)
                    char_in_pool = any(
                        isinstance(p, prize_cls) for tier in pool.values() for p in tier
                    )
                    if char_in_pool:
                        loc.set_prize(prize_cls())
                        remove_prize_from_pool(pool, prize_cls, world)
                        continue
                    # else: character was excluded, skip this location
            # If no starting character assigned to this slot, leave it empty
            continue

        elif not should_shuffle(loc, world):
            if loc.originally_held is not None:
                # Check if this prize exists in the pool before trying to set/remove
                # Excluded characters/star pieces/spells won't be in the pool
                prize_exists_in_pool = any(
                    isinstance(p, loc.originally_held)
                    for tier in pool.values()
                    for p in tier
                )
                if prize_exists_in_pool:
                    loc.set_prize(loc.originally_held())
                    remove_prize_from_pool(pool, loc.originally_held, world)

    # Shuffle the prize pools
    for prizes in pool.values():
        random.shuffle(prizes)

    # Add some "noise" to the top tier to prevent progression items from ending up in too many same-y formations
    # non_progression_size = len(pool[RESTRICTED_PRIZES]) + len(pool[MANDATORY_INCLUSIONS]) + len(pool[LOW_PRIORITY])
    # progression_size = len(pool[PROGRESSION_PRIZES])
    # if non_progression_size > 0:
    #     addition_size = progression_size * 0.2
    #     rate = addition_size / non_progression_size
    # else:
    #     rate = 0
    # for tier, prizes in pool.items():
    #     if tier == PROGRESSION_PRIZES:
    #         continue
    #     for _ in range(len(prizes)):
    #         if random.random() < rate:
    #             pool[PROGRESSION_PRIZES].append(prizes.pop())

    # Shuffle the prize pools again
    for prizes in pool.values():
        random.shuffle(prizes)

    # Snapshot pool before placement (item names per tier, for debug dump)
    pool_before: dict[int, list[str]] = {
        tier: [type(p).__name__ for p in prizes] for tier, prizes in pool.items()
    }

    # Snapshot pool before placement for post-placement diff
    pool_snapshot: dict[str, int] = {}
    for tier_prizes in pool.values():
        for p in tier_prizes:
            name = type(p).__name__
            pool_snapshot[name] = pool_snapshot.get(name, 0) + 1
    # Also count items placed during static fills (debug/unshuffled)
    static_placed: dict[str, int] = {}
    for loc in world.locations.values():
        if loc.has_item:
            name = type(loc.prize).__name__
            static_placed[name] = static_placed.get(name, 0) + 1
    pool_plus_static: dict[str, int] = dict(pool_snapshot)
    for name, count in static_placed.items():
        pool_plus_static[name] = pool_plus_static.get(name, 0) + count

    # Only place items in locations that should be shuffled
    shuffle_filter = lambda loc: should_shuffle(loc, world)
    priority_classes = _build_priority_classes(world)

    try:
        place(
            world,
            pool[PROGRESSION_PRIZES],
            on_placed=lambda i, l: _on_item_placed(world, i, l),
            location_filter=shuffle_filter,
            priority_classes=priority_classes,
        )

        # Debug: check which locations are still inaccessible after progression placement
        player_has = collect_accessible_items(world)
        inaccessible = [
            loc
            for loc in world.locations.values()
            if should_shuffle(loc, world) and not loc.can_access(player_has, world)
        ]
        non_spell_inaccessible = [
            l for l in inaccessible if not isinstance(l, SpellSlotLocation)
        ]
        if non_spell_inaccessible:
            print(
                f"[DEBUG] After progression placement: {len(non_spell_inaccessible)} non-SpellSlot locations still inaccessible:"
            )
            for loc in non_spell_inaccessible:
                print(f"[DEBUG]   {type(loc).__name__}")
        else:
            print(
                f"[DEBUG] After progression placement: {len(inaccessible)} inaccessible locations, all SpellSlotLocations"
            )

        place(
            world,
            pool[RESTRICTED_PRIZES],
            on_placed=lambda i, l: _on_item_placed(world, i, l),
            location_filter=shuffle_filter,
        )
        place(
            world,
            pool[MANDATORY_INCLUSIONS],
            on_placed=lambda i, l: _on_item_placed(world, i, l),
            force_frog_disciple=True,
            location_filter=shuffle_filter,
        )
        place(
            world,
            pool[LOW_PRIORITY],
            can_overflow=True,
            on_placed=lambda i, l: _on_item_placed(world, i, l),
            location_filter=shuffle_filter,
        )
    except PlacementException as e:
        _dump_placement_failure(world, pool_before, e.unplaced_items, priority_classes)
        raise

    # Post-placement diff: collect all items from every location and compare to pool snapshot
    placed_items: dict[str, int] = {}
    for loc in world.locations.values():
        if loc.has_item:
            name = type(loc.prize).__name__
            placed_items[name] = placed_items.get(name, 0) + 1
    total_after = sum(placed_items.values())
    print(f"[DEBUG] Items in locations after placement: {total_after}")

    all_keys = sorted(set(pool_plus_static.keys()) | set(placed_items.keys()))
    diffs: list[str] = []
    for key in all_keys:
        before = pool_plus_static.get(key, 0)
        after = placed_items.get(key, 0)
        if before != after:
            diffs.append(
                f"  {key}: pool+static={before}, placed={after} (diff={after - before:+d})"
            )
    if diffs:
        print(f"[DEBUG] POOL vs PLACED DIFF ({len(diffs)} mismatches):")
        for d in diffs:
            print(f"[DEBUG] {d}")
    else:
        print(f"[DEBUG] Pool and placed items match perfectly.")


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
        spell_instance = world.get_spell(prize.spell)  # type: ignore

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


def apply_debug_overrides(world: GameWorld) -> None:
    """Apply debug item overrides and diagnostics after shuffling.

    This runs after the shuffler so that debug mode doesn't affect the shuffle
    outcome. Overrides simply replace whatever the shuffler placed at the
    configured locations.
    """
    from ..placement import diagnose_empty_locations
    from randomizer.debug import load_debug_config, get_prize_class, get_location_class
    from ...types.logic import Inventory

    if not world.settings.debug_mode:
        return

    config = load_debug_config()
    overrides = config.get("items", {}).get("override", {})
    debug_locations: set[type[PrizeLocation]] = set()

    for location_name, prize_name in overrides.items():
        location_cls = get_location_class(location_name)
        if location_cls is None:
            raise ValueError(
                f"Invalid location name in debug config: '{location_name}'"
            )
        for loc in world.locations.values():
            if isinstance(loc, location_cls):
                debug_locations.add(type(loc))
                prize_cls = get_prize_class(prize_name)
                if prize_cls is None or not loc.can_accept(
                    prize_cls(), Inventory(), world
                ):
                    if not loc.can_be_empty(world):
                        raise ValueError(
                            f"Invalid prize assigned to debug location '{location_name}' when it cannot be empty"
                        )
                    else:
                        loc.set_prize(None)
                else:
                    loc.set_prize(prize_cls())
                break

    world._debug_locations = debug_locations
    diagnose_empty_locations(world)


def post_shuffle_cleanup(world: GameWorld) -> None:
    """Handle empty chests and replace low-value items with coins.

    This function:
    1. Applies debug overrides (if debug mode enabled)
    2. Assigns spell prize models based on finalized elements
    3. Fills or disables empty treasure chests based on settings
    4. Replaces low-impact items with coin prizes at half their price
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

    # Apply debug overrides (replaces shuffled prizes at configured locations)
    apply_debug_overrides(world)

    # Assign spell prize models based on their finalized elements
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
