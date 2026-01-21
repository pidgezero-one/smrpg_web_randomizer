"""Item and prize shuffling logic."""

from __future__ import annotations
import random
from copy import copy
from typing import TYPE_CHECKING

from randomizer.types.prizelocation import StandingLocation, TreasureShopLocation

from ..placement import place
from ...types.prize import RandomPrizeSubstitute, CoinPrize, FPFlowerPrize, FrogCoinPrize
from ..utils import debug_time
from ...progression.prizes import FryingPanPrize, RecoveryMushroomPrize, FrogCoin1Prize
from ...progression.prizelocations import MushroomKingdomInnPurchaseLocation, ShipCoinSnakePuzzleLocation

if TYPE_CHECKING:
    from ...types.gameworld import GameWorld
    from ...types.prizelocation import PrizeLocation
    from ...types.prize import Prize


def _on_item_placed(
    world: GameWorld, item: Prize, placed_location: PrizeLocation
) -> None:
    """Callback to handle Mimic world area updates after placement."""
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
    #print(f"Placed {type(item).__name__} at {type(placed_location).__name__}")

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
        NimbusGate,
        NimbusGating,
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
        # Gating flags for character requirement validation
        BanditsWayGate,
        BanditsWayGating,
        KeroSewersGate,
        KeroSewersGating,
        PipeVaultGate,
        PipeVaultGating,
        Moleville1Gate,
        Moleville1Gating,
        BoosterTowerGate,
        BoosterTowerGating,
        SeaGate,
        SeaGating,
        BoosterHillGate,
        BoosterHillGating,
        MarrymoreGate,
        MarrymoreGating,
        YaridovichGate,
        YaridovichGating,
        LandsEndGate,
        LandsEndGating,
        MonstroTownGate,
        MonstroTownGating,
        BarrelVolcanoGate,
        BarrelVolcanoGating,
        BowsersKeepGate,
        BowsersKeepGating,
        FactoryGate,
        FactoryGating,
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
        MonstroSecondSuperJumpRewardLocation,
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

    # Apply debug overrides first (hard-set locations before shuffle)
    debug_prizes_to_remove: dict[type, int] = {}
    if world.settings.debug_mode:
        from randomizer.debug import load_debug_config, get_prize_class, get_location_class
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
            location.set_prize(prize_cls())

            # Track prize to remove from pool (one instance per override)
            debug_prizes_to_remove[prize_cls] = debug_prizes_to_remove.get(prize_cls, 0) + 1

    # Helper to check if prize should be skipped for debug override
    def should_skip_for_debug(prize_cls: type) -> bool:
        if prize_cls in debug_prizes_to_remove and debug_prizes_to_remove[prize_cls] > 0:
            debug_prizes_to_remove[prize_cls] -= 1
            print(f"Debug: Removed one {prize_cls.__name__} from pool")
            return True
        return False

    # Define which items should be considered highest priority to place
    unlocks_other_checks: list[type[Prize]] = [
        RareFrogCoinPrize,
        WalletPrize,
        CricketPiePrize,
        BambinoBombPrize,
        CastleKey1Prize,
        CastleKey2Prize,
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
        RegularFireworksPrize,
        ProgressiveFireworksPrize,
        WeddingGearPrize,
        MimicFightInitiatorPrize,
    ]
    # Items that absolutely must be included, but aren't important for progress, can be second priority
    should_otherwise_include = [
        ProgressiveCardPrize,
        YouMissed,
        LuckyJewelPrize,
        SignalRingPrize,
        GoodieBagPrize,
        StarEggPrize,
    ]
    # Items with very restricted placement options (can only go in certain chest locations
    # with additional room constraints) should be placed first to ensure they have valid spots
    restricted_placement_items: list[type[Prize]] = [SlotsPrize]

    progress_stars = 0
    if world.settings.isflag_enabled(Remake):
        unlocks_other_checks.extend([ExtraShinyStonePrize, StayVoucherPrize])
        should_otherwise_include.extend([CrystalShardPrize])
    if world.settings.is_flag_value(FireworksSetting, FireworksOptions.SHUFFLE_ONE):
        unlocks_other_checks.append(RegularFireworksPrize)
    elif world.settings.is_flag_value(FireworksSetting, FireworksOptions.PROGRESSIVE):
        unlocks_other_checks.append(ProgressiveFireworksPrize)
    if world.settings.is_flag_value(SeaGate, SeaGating.STAR_4):
        progress_stars = 4
    elif world.settings.is_flag_value(LandsEndGate, LandsEndGating.STAR_5):
        progress_stars = 4
    elif world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.STAR_6):
        progress_stars = 6
    elif world.settings.is_flag_value(FactoryGate, FactoryGating.STAR_6):
        progress_stars = 6
    if world.settings.is_flag_value(NimbusGate, NimbusGating.PAINT):
        unlocks_other_checks.append(GoldPaintPrize)
    if world.settings.isflag_enabled(ShuffleShops):
        should_otherwise_include.extend([
            SeeYaPrize,
            EarlierTimesPrize,
            CoinTrickPrize,
            ExpBoosterPrize,
            ScroogeRingPrize,
            LuckyJewelPrize,
            ProgressiveEggPrize,
            FryingPanPrize,
        ])
    mxstars = world.settings.get_flag(StarPiecesRequired).value
    if mxstars > progress_stars:
        progress_stars = mxstars
    if not world.settings.is_flag_value(
        ItemQuality, ItemQualityOptions.ORIGINAL_POOL
    ):
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
                EXPStarPrize,
            ]
        )
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

    progression_prizes: list[Prize] = []
    must_include: list[Prize] = [ProgressiveEggPrize(), ProgressiveEggPrize()]
    not_important: list[Prize] = []
    # Items with very restricted placement options (e.g., SlotsPrize which can only go
    # in chest locations with enough room for 5 extra NPCs) - placed first
    restricted_prizes: list[Prize] = []

    if world.settings.isflag_enabled(ShuffleCharacters):
        # Place starting characters based on StartingCharacters flag
        ally_name_to_prize: dict[str, type[CharacterPrize]] = {
            "Mario": MarioRecruitmentPrize,
            "Mallow": MallowRecruitmentPrize,
            "Geno": GenoRecruitmentPrize,
            "Bowser": BowserRecruitmentPrize,
            "Toadstool": ToadstoolRecruitmentPrize,
        }

        # Collect characters required by gating settings
        gating_required_characters: set[str] = set()
        gating_checks: list[tuple[type, object, str]] = [
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
        for flag_class, gating_value, char_name in gating_checks:
            if world.settings.is_flag_value(flag_class, gating_value):
                gating_required_characters.add(char_name)

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
                progression_prizes.append(prize_class())
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
            progression_prizes.append(prize_class())
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

        # Check if all 5 characters are available
        available_chars_flag = world.settings.get_flag(AvailableCharacters)
        charcount = min(
            len(available_chars_flag.enabled),
            world.settings.get_flag(MaxCharacters).value,
        )
        all_chars_available = charcount == 5
        extra_spells = []

        # If all 5 characters are present, double 3 random spells
        if all_chars_available and len(enabled_spell_prizes) >= 3:
            spells_to_double = random.sample(enabled_spell_prizes, 3)
            extra_spells = [c() for c in spells_to_double]

        # Add all enabled spells to the pool
        # absolutely must have a spell that can always damage mokura
        progression_prizes.append(
            random.choice(
                [
                    p()
                    for p in enabled_spell_prizes
                    if p
                    in [
                        StarRainSpellPrize,
                        GenoWhirlSpellPrize,
                        TerrorizeSpellPrize,
                        PoisonGasSpellPrize,
                    ]
                ]
            )
        )
        spell_count = 1
        if SuperJumpSpell not in disabled_spell_classes:
            progression_prizes.append(SuperJumpSpellPrize())
            spell_count += 1

        remaining_spell_pool = [
            p()
            for p in enabled_spell_prizes
            if p not in [type(q) for q in must_include] + extra_spells
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
        progression_prizes.extend([sp() for sp in sp_prizes[: progress_stars]])
        must_include.extend([sp() for sp in sp_prizes[progress_stars:world.settings.get_flag(TotalStarPieces).value]])

    if world.settings.isflag_enabled(BossShuffle):
        # Place disabled bosses (those not enabled in ShuffledBosses)
        shuffled_bosses_flag = world.settings.get_flag(ShuffledBosses)
        disabled_boss_types = {m.value for m in shuffled_bosses_flag.disabled}
        for loc in [
            l
            for l in world.locations.values()
            if isinstance(l, BossFightLocation) and l.originally_held is not None
        ]:
            if loc.originally_held in disabled_boss_types:
                loc.set_prize(loc.originally_held())  # type: ignore
            else:
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
            else:
                continue
        if isinstance(loc, StarPieceLocation):
            if not world.settings.isflag_enabled(ShuffleStarPieces):
                loc.set_prize(loc.originally_held())
            else:
                continue
        if isinstance(loc, BossFightLocation):
            if not world.settings.isflag_enabled(BossShuffle):
                loc.set_prize(loc.originally_held())
            else:
                # Check if this location's boss is disabled in ShuffledBosses
                shuffled_bosses_flag = world.settings.get_flag(ShuffledBosses)
                disabled_boss_types = {m.value for m in shuffled_bosses_flag.disabled}
                if loc.originally_held in disabled_boss_types:
                    loc.set_prize(loc.originally_held())
                else:
                    continue
        if isinstance(loc, SpellSlotLocation):
            if not world.settings.isflag_enabled(CharacterLearnedSpells):
                loc.set_prize(loc.originally_held())
            else:
                continue
        # special exclusions
        if isinstance(loc, FrogDiscipleLocation):
            # nowhere to put it if shuffle shops is on but item shuffle is off
            if not world.settings.isflag_enabled(ShuffleShops) or not world.settings.isflag_enabled(ShuffleItems):
                loc.set_prize(loc.originally_held())
                continue
        if isinstance(loc, TreasureShopLocation):
            # nowhere to put it if shuffle shops is on but item shuffle is off
            if not world.settings.isflag_enabled(ShuffleShops) or not world.settings.isflag_enabled(ShuffleItems):
                loc.set_prize(loc.originally_held())
                continue
        # made it this far? start setting
        if not world.settings.isflag_enabled(ShuffleItems):
            loc.set_prize(loc.originally_held())
            continue
        if isinstance(loc.originally_held(), StarEggPrize):
            if world.settings.isflag_enabled(NoStarEgg):
                continue
        if isinstance(loc.originally_held(), EXPStarPrize):
            if not world.settings.isflag_enabled(EXPStarsAnywhere):
                loc.set_prize(loc.originally_held())
                continue
        if isinstance(loc.originally_held(), MimicFightInitiatorPrize):
            if not world.settings.isflag_enabled(MimicsAnywhere):
                loc.set_prize(loc.originally_held())
                continue
        if isinstance(loc.originally_held(), SlotsPrize):
            if not world.settings.isflag_enabled(SlotsAnywhere):
                loc.set_prize(loc.originally_held())
                continue
            else:
                # SlotsPrize has restricted placement (needs room with space for 5 NPCs)
                # so it must be placed before other items fill up eligible locations
                restricted_prizes.append(loc.originally_held())
                continue
        if isinstance(loc.originally_held(), BeetlemaniaPrize):
            if not world.settings.isflag_enabled(ShuffleBeetlemania):
                loc.set_prize(loc.originally_held())
                continue
        if isinstance(loc.originally_held(), InfiniteCoinsPrize):
            if not world.settings.isflag_enabled(ShuffleMagikoopaChest):
                loc.set_prize(loc.originally_held())
                continue
        if isinstance(loc.originally_held(), WeddingGearPrize):
            if not world.settings.isflag_enabled(ShuffleWeddingGear):
                loc.set_prize(loc.originally_held())
                continue
        if isinstance(loc.originally_held(), SuperSuitPrize) and world.settings.isflag_enabled(RestrictSpecialEquips):
            # 50% chance of keeping super suit in its original location if threshold is 100
            if world.settings.is_flag_value(
                SuperJump2Threshold, 100
            ):
                roll = random.randint(0, 1)
                if roll:
                    loc.set_prize(loc.originally_held())
                    continue
        if isinstance(loc.originally_held(), RegularFireworksPrize):
            if world.settings.is_flag_value(
                FireworksSetting, FireworksOptions.VANILLA
            ):
                loc.set_prize(loc.originally_held())
                continue
        is_progress_item = [p for p in unlocks_other_checks if isinstance(loc.originally_held(), p)]
        if len(is_progress_item) > 0:
            if not should_skip_for_debug(type(loc.originally_held())):
                progression_prizes.append(loc.originally_held())
            continue
        is_important_item = [p for p in should_otherwise_include if isinstance(loc.originally_held(), p)]
        if len(is_important_item) > 0:
            if not should_skip_for_debug(type(loc.originally_held())):
                must_include.append(loc.originally_held())
            continue
        elif world.settings.is_flag_value(ItemQuality, ItemQualityOptions.ORIGINAL_POOL):
            if isinstance(
                loc.originally_held(),
                (RecoveryMushroomPrize, FPFlowerPrize, FrogCoin1Prize),
            ):
                if not should_skip_for_debug(type(loc.originally_held())):
                    not_important.append(loc.originally_held())
            else:
                if not should_skip_for_debug(type(loc.originally_held())):
                    must_include.append(loc.originally_held())
            continue
        if world.settings.is_flag_value(ItemQuality, ItemQualityOptions.ORIGINAL_POOL):
            if not should_skip_for_debug(type(loc.originally_held())):
                not_important.append(loc.originally_held())
        else:
            not_important.append(RandomPrizeSubstitute().generate(world, loc))
            
    """     print(f"Priority 1:")
    for p in progression_prizes:
        print(f"  {type(p).__name__}")
    print(f"Priority 2:")
    for p in must_include:
        print(f"  {type(p).__name__}")
    print(f"Priority 3:")
    for p in not_important:
        print(f"  {type(p).__name__}") """

    # Shuffle!
    # Place items with restricted placement options first (e.g., SlotsPrize)
    # These must be placed before other items fill up their limited eligible locations
    if restricted_prizes:
        print("placing restricted items (slots)")
        random.shuffle(restricted_prizes)
        place(
            world,
            restricted_prizes,
            on_placed=lambda i, l: _on_item_placed(world, i, l),
        )

    # Place critical/progress items first
    # or items that likely can't appear in shops and do something unique
    print("placing keys")
    random.shuffle(progression_prizes)
    place(
        world,
        progression_prizes,
        on_placed=lambda i, l: _on_item_placed(world, i, l),
    )
    print("placing important items")
    random.shuffle(must_include)
    place(
        world,
        must_include,
        on_placed=lambda i, l: _on_item_placed(world, i, l),
        force_frog_disciple=True
    )
    print("filling remaining")
    random.shuffle(not_important)
    place(
        world,
        not_important,
        True,
        on_placed=lambda i, l: _on_item_placed(world, i, l),
        force_frog_disciple=True
    )


def post_shuffle_cleanup(world: GameWorld) -> None:
    """Handle empty chests and replace low-value items with coins.

    This function:
    1. Fills or disables empty treasure chests based on settings
    2. Replaces low-impact items with coin prizes at half their price
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
            script.insert_before_nth_command(
                0, JmpIfBitClear(l.prize._hint, [f"EVENT_{event}_play_sound"])
                )
