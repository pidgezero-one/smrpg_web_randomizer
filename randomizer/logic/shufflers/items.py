"""Item and prize shuffling logic."""

from __future__ import annotations
import random
from copy import copy
from typing import TYPE_CHECKING

from randomizer.types.prizelocation import StandingLocation

from ..placement import collect, place, fill_remaining
from ...types.prize import RandomPrizeSubstitute, CoinPrize
from ..utils import debug_time

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
    print("starting shuffle_prizes at", debug_time())
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
        EXPStarsAnywhere,
        MimicsAnywhere,
        SlotsAnywhere,
        ShuffleBeetlemania,
        ShuffleMagikoopaChest,
        ShuffleWeddingGear,
        ShuffleCoins,
    )
    from ...types.prizelocation import (
        CharacterRecruitmentLocation,
        StarPieceLocation,
        BossFightLocation,
        SpellSlotLocation,
        FrogDiscipleLocation,
    )
    from ...types.prize import CharacterPrize, SpellPrize
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
        CoinTrickPrize,
        ScroogeRingPrize,
        ExpBoosterPrize,
        SeeYaPrize,
        EarlierTimesPrize,
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
    from ...types.gameworld import WorldBuildingException

    print("imports done", debug_time())

    # Start off emptying every location of every type
    for loc in world.locations.values():
        loc.set_prize(None)
    print("set all to none", debug_time())

    must_include: list[Prize] = []
    less_important: list[Prize] = []

    # Init population of must_include
    if world.settings.isflag_enabled(ShuffleItems):
        must_include.extend(
            [
                RareFrogCoinPrize(),
                WalletPrize(),
                CricketPiePrize(),
                BambinoBombPrize(),
                CastleKey1Prize(),
                CastleKey2Prize(),
                ProgressiveCardPrize(),
                ProgressiveCardPrize(),
                ProgressiveCardPrize(),
                GreaperFlagPrize(),
                DryBonesFlagPrize(),
                BigBooFlagPrize(),
                ShedKeyPrize(),
                ElderKeyPrize(),
                CricketJamPrize(),
                TempleKeyPrize(),
                RoomKeyPrize(),
                SeedPrize(),
                FertilizerPrize(),
                BrightCardPrize(),
                YouMissed(),
                ProgressiveEggPrize(),
                ProgressiveEggPrize(),
                ProgressiveEggPrize(),
                LuckyJewelPrize(),
                SignalRingPrize(),
                GoodieBagPrize(),
            ]
        )
        if world.settings.isflag_enabled(ShuffleShops):
            must_include.extend(
                [
                    CoinTrickPrize(),
                    ScroogeRingPrize(),
                    ExpBoosterPrize(),
                    SeeYaPrize(),
                    EarlierTimesPrize(),
                ]
            )
        if world.settings.isflag_enabled(Remake):
            must_include.extend(
                [
                    CrystalShardPrize(),
                    ExtraShinyStonePrize(),
                    StayVoucherPrize(),
                ]
            )
        if world.settings.isflag_enabled(RestrictSpecialEquips):
            must_include.extend(
                [
                    FroggiestickPrize(),
                    ChompPrize(),
                    ZoomShoesPrize(),
                    LazyShellArmorPrize(),
                    LazyShellWeaponPrize(),
                    GhostMedalPrize(),
                    QuartzCharmPrize(),
                    JinxBeltPrize(),
                    AttackScarfPrize(),
                ]
            )
            if world.settings.isflag_enabled(Remake):
                must_include.extend(
                    [
                        WonderChompPrize(),
                        Stella023Prize(),
                        SageStickPrize(),
                        EnduringBroochPrize(),
                        TeamworkBandPrize(),
                    ]
                )
            if world.settings.is_flag_value(SuperJump2Threshold, 100):
                coinflip = random.randint(0, 1)
                if coinflip == 0:
                    must_include.append(SuperSuitPrize())
                else:
                    # 50% likely that you will get the super suit in the normal spot
                    # if you're good enough at the game to do 100
                    world.get_location(MonstroSecondSuperJumpRewardLocation).set_prize(
                        SuperSuitPrize()
                    )
        if world.settings.is_flag_value(NimbusGate, NimbusGating.PAINT):
            must_include.append(GoldPaintPrize())
        if not world.settings.isflag_enabled(NoStarEgg):
            must_include.append(StarEggPrize())
        # If not using original item pool, ensure that items with specific
        # non-randomizable changes are included at least once
        if not world.settings.is_flag_value(
            ItemQuality, ItemQualityOptions.ORIGINAL_POOL
        ):
            must_include.extend(
                [
                    JumpShoesPrize(),
                    BtubRingPrize(),
                ]
            )
            if world.settings.isflag_enabled(Remake):
                must_include.extend(
                    [
                        EnduringBroochPrize(),
                        StayVoucherPrize(),
                    ]
                )

        if world.settings.is_flag_value(FireworksSetting, FireworksOptions.SHUFFLE_ONE):
            must_include.append(RegularFireworksPrize())
        if world.settings.is_flag_value(FireworksSetting, FireworksOptions.PROGRESSIVE):
            must_include.append(ProgressiveFireworksPrize())
            must_include.append(ProgressiveFireworksPrize())
            must_include.append(ProgressiveFireworksPrize())
    print("must_include items filled", debug_time())

    if world.settings.isflag_enabled(ShuffleCharacters):
        # Place starting characters based on StartingCharacters flag
        ally_name_to_prize: dict[str, type[CharacterPrize]] = {
            "Mario": MarioRecruitmentPrize,
            "Mallow": MallowRecruitmentPrize,
            "Geno": GenoRecruitmentPrize,
            "Bowser": BowserRecruitmentPrize,
            "Toadstool": ToadstoolRecruitmentPrize,
        }

        # Starting character locations in order
        starting_locations = [
            StartingCharacter1,
            StartingCharacter2,
            StartingCharacter3,
            StartingCharacter4,
            StartingCharacter5,
        ]

        starting_chars_flag = world.settings.get_flag(StartingCharacters)
        available_chars_flag = world.settings.get_flag(AvailableCharacters)
        disabled_char_names = {m.value.name for m in available_chars_flag.disabled}
        max_char_count = world.settings.get_flag(MaxCharacters).value

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

        # Add unplaced characters to must_include (unless disabled in AvailableCharacters)
        all_recruitment_prizes: dict[str, type[CharacterPrize]] = {
            "Mario": MarioRecruitmentPrize,
            "Mallow": MallowRecruitmentPrize,
            "Geno": GenoRecruitmentPrize,
            "Bowser": BowserRecruitmentPrize,
            "Toadstool": ToadstoolRecruitmentPrize,
        }
        for ally_name, prize_class in all_recruitment_prizes.items():
            if (
                prize_class not in placed_characters
                and ally_name not in disabled_char_names
                and len(placed_characters) < max_char_count
            ):
                must_include.append(prize_class())
                placed_characters.add(prize_class)
    print("must_include characters filled", debug_time())

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
        must_include.append(
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
            must_include.append(SuperJumpSpellPrize())
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
                    (5 - charcount) * 6 - spell_count,
                ),
            )
        )

    print("must_include spells filled", debug_time())

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
        must_include.extend(
            [sp() for sp in sp_prizes[: world.settings.get_flag(TotalStarPieces).value]]
        )
    print("must_include stars filled", debug_time())

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
                must_include.append(loc.originally_held())  # type: ignore

    if not world.settings.isflag_enabled(ShuffleCoins):
        # Add all shuffled coins to must_include
        coin_locations = [
            l
            for l in world.locations.values()
            if isinstance(l, StandingLocation)
            and l.originally_held is not None
            and isinstance(l.originally_held(), CoinPrize)
        ]
        for loc in coin_locations:
            loc.set_prize(loc.originally_held())  # type: ignore
    print("must_include bosses filled", debug_time())

    # Check-by-check set for disabled flags and pulling items into inclusion array
    for loc in world.locations.values():
        if loc.originally_held is None:
            continue
        if isinstance(loc, CharacterRecruitmentLocation):
            if not world.settings.isflag_enabled(ShuffleCharacters):
                loc.set_prize(loc.originally_held())

        elif isinstance(loc, StarPieceLocation):
            if not world.settings.isflag_enabled(ShuffleStarPieces):
                loc.set_prize(loc.originally_held())

        elif isinstance(loc, BossFightLocation):
            if not world.settings.isflag_enabled(BossShuffle):
                loc.set_prize(loc.originally_held())

        elif isinstance(loc, SpellSlotLocation):
            if not world.settings.isflag_enabled(CharacterLearnedSpells):
                loc.set_prize(loc.originally_held())

        elif isinstance(loc, FrogDiscipleLocation):
            if not world.settings.isflag_enabled(ShuffleShops):
                loc.set_prize(loc.originally_held())

        else:
            if not world.settings.isflag_enabled(ShuffleItems):
                loc.set_prize(loc.originally_held())
            else:
                if isinstance(loc.originally_held(), EXPStarPrize):
                    if world.settings.isflag_enabled(EXPStarsAnywhere):
                        must_include.append(loc.originally_held())
                    else:
                        loc.set_prize(loc.originally_held())
                if isinstance(loc.originally_held(), MimicFightInitiatorPrize):
                    if world.settings.isflag_enabled(MimicsAnywhere):
                        must_include.append(loc.originally_held())
                    else:
                        loc.set_prize(loc.originally_held())
                if isinstance(loc.originally_held(), SlotsPrize):
                    if world.settings.isflag_enabled(SlotsAnywhere):
                        must_include.append(loc.originally_held())
                    else:
                        loc.set_prize(loc.originally_held())
                if isinstance(loc.originally_held(), BeetlemaniaPrize):
                    if world.settings.isflag_enabled(ShuffleBeetlemania):
                        must_include.append(loc.originally_held())
                    else:
                        loc.set_prize(loc.originally_held())
                if isinstance(loc.originally_held(), InfiniteCoinsPrize):
                    if world.settings.isflag_enabled(ShuffleMagikoopaChest):
                        must_include.append(loc.originally_held())
                    else:
                        loc.set_prize(loc.originally_held())
                if isinstance(loc.originally_held(), WeddingGearPrize):
                    if world.settings.isflag_enabled(ShuffleWeddingGear):
                        must_include.append(loc.originally_held())
                    else:
                        loc.set_prize(loc.originally_held())
                if isinstance(loc.originally_held(), RegularFireworksPrize):
                    if world.settings.is_flag_value(
                        FireworksSetting, FireworksOptions.VANILLA
                    ):
                        loc.set_prize(loc.originally_held())
                # For every location whose prize isn't already in must_include,
                # create a generic prize that could theoretically go in it
                elif (
                    len([p for p in must_include if isinstance(p, loc.originally_held)])
                    == 0
                ):
                    if world.settings.is_flag_value(
                        ItemQuality, ItemQualityOptions.ORIGINAL_POOL
                    ):
                        less_important.append(loc.originally_held())
                    else:
                        less_important.append(
                            RandomPrizeSubstitute().generate(world, loc)
                        )
    print("set unshuffled locations", debug_time())

    # Shuffle!
    to_fill = copy(list(world.locations.values()))

    random.shuffle(must_include)
    random.shuffle(to_fill)
    # Critical items use assumed-reachability to ensure game is completable
    place(
        world,
        must_include,
        to_fill,
        on_placed=lambda i, l: _on_item_placed(world, i, l),
    )

    to_fill = [l for l in to_fill if not l.has_item]

    random.shuffle(less_important)
    to_fill.reverse()
    place(
        world,
        less_important,
        to_fill,
        True,
        on_placed=lambda i, l: _on_item_placed(world, i, l),
    )

    collected = set(collect(world))

    # Verify all must_include prizes were placed
    missing_prizes = [p for p in must_include if p not in collected]
    if missing_prizes:
        missing_names = [type(p).__name__ for p in missing_prizes]
        raise WorldBuildingException(
            f"Failed to place required prizes: {', '.join(missing_names)}"
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
