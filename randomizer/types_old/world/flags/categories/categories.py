"""Categories of randomizer settings."""

from typing import TypeVar

from randomizer.types.world.flags.categories.types import FlagCategory
from randomizer.types.world.flags.types import Flag
from randomizer.types.world.flags import (
    AnnoyingChests,
    AvailableCharacters,
    AvailableSpells,
    BallSolitaireShuffle,
    BanditsWayGate,
    BarrelVolcanoGate,
    BelomeTempleGate,
    BetterTips,
    BiasItemShuffle,
    BiasShopShuffle,
    BoosterTowerGate,
    BossReplaceMinigameSprites,
    BossShuffle,
    BossShuffleMusic,
    BossShuffleScaleStats,
    BowserDoorRequirements,
    BowserDoorShuffle,
    BowsersKeepGate,
    BucketWarp,
    CasinoWarp,
    ChangeNames,
    CharacterLearnedSpells,
    CharacterSpellElements,
    CharacterSpellExtraElements,
    CharacterSpellStats,
    CharacterStats,
    DifferentiateRepeatedBosses,
    EXPChallenge,
    EXPMultiplier,
    EXPStarsAnywhere,
    EnabledBossChecks,
    EnabledRegularChecks,
    EnemyAttacks,
    EnemyDrops,
    EnemyFormations,
    EnemyNoSafetyChecks,
    EnemySpells,
    EnemyStats,
    EquipmentCharacters,
    EquipmentNoSafety,
    EquipmentProperties,
    ExperienceNoBosses,
    ExperienceNoRegular,
    FactoryGate,
    FastTravel,
    FireworksSetting,
    FixMagikoopa,
    ForestMazeGate,
    FreeShops,
    GrateGuyPrizeThreshold,
    IncludeRemakeBosses,
    InvisibleFlagsSetting,
    ItemQuality,
    JapaneseABXY,
    KeyItemsAnywhere,
    KnifeGuyPrizeThreshold,
    MagicButtonShuffle,
    MarrymoreGate,
    MaxCharacters,
    MimicsAnywhere,
    Moleville1Gate,
    MonstroTownGate,
    NoGenoWhirlExor,
    NoOHKO,
    NoPickMeUps,
    NoStarEgg,
    PaletteSwaps,
    PipeVaultGate,
    PlayAsStarter,
    PoisonMushroom,
    QuickHitCoins,
    QuizShuffle,
    RandomSunkenShipPassword,
    RandomTadpolePondSong,
    RemakeNames,
    RemoveFlashes,
    ReplaceItems,
    RequireBossFights,
    RestrictSpecialEquips,
    RestrictSpecialEquipsExclusive,
    SafeLogicProgression,
    SeaGate,
    ShopQuality,
    ShowEquips,
    ShuffleBeetlemania,
    ShuffleCharacters,
    ShuffleItems,
    ShuffleMagikoopaChest,
    ShuffleShops,
    ShuffleStarPieces,
    ShuffleWeddingGear,
    ShuffledBosses,
    ShuffledMusic,
    SkipMinecart,
    SkipMustyFearsSequence,
    SlotsAnywhere,
    StarPieceAvailability,
    StarPieceHints,
    StarPiecesRequired,
    StarPiecesRestrictedByArea,
    StartingCharacter,
    StartingCharacters,
    SuitePrize1Threshold,
    SuitePrize2Threshold,
    SuitePrize3Threshold,
    SuitePrize4Threshold,
    SuitePrize5Threshold,
    SuitePrize6Threshold,
    SuperJump1Threshold,
    SuperJump2Threshold,
    TotalStarPieces,
    UncapSuperJumps,
    WinCondition,
    YaridovichGate)


class CharacterRecruitmentSubcategory(FlagCategory):
    """Collection of settings related to character recruitment."""

    _flags: list[type[Flag]] = [
        ShuffleCharacters,
        StartingCharacter,
        PlayAsStarter,
        StartingCharacters,
        MaxCharacters,
        AvailableCharacters,
    ]
    _size: int = 4
    _id: str = "P"


class CharacterEquipmentSubcategory(FlagCategory):
    """Collection of settings related to equipment properties."""

    _flags: list[type[Flag]] = [
        EquipmentCharacters,
        EquipmentProperties,
        EquipmentNoSafety,
        StarPieceHints,
    ]
    _size: int = 4
    _id: str = "Q"


class CharacterStatsSpellsSubcategory(FlagCategory):
    """Collection of settings related to learnable spells."""

    _flags: list[type[Flag]] = [
        EXPMultiplier,
        CharacterStats,
        CharacterLearnedSpells,
        CharacterSpellStats,
        CharacterSpellExtraElements,
        CharacterSpellElements,
        UncapSuperJumps,
        AvailableSpells,
    ]
    _size: int = 4
    _id: str = "C"


class PartyCategory(FlagCategory):
    """Pan-collection of settings related to party members and equips."""

    _name: str = "Party & Equipment"
    _subcategories: list[type[FlagCategory]] = [
        CharacterRecruitmentSubcategory,
        CharacterEquipmentSubcategory,
        CharacterStatsSpellsSubcategory,
    ]
    _id: str = "PartyCategory"


class StarPiecesCategory(FlagCategory):
    """Collection of settings related to star piece distribution."""

    _flags: list[type[Flag]] = [
        ShuffleStarPieces,
        TotalStarPieces,
        EnabledBossChecks,
        StarPiecesRestrictedByArea,
    ]
    _size: int = 3
    _id: str = "X"


class ItemShuffleSubcategory(FlagCategory):
    """Collection of settings related to item distribution."""

    _flags: list[type[Flag]] = [
        ShuffleItems,
        ItemQuality,
        BiasItemShuffle,
        RestrictSpecialEquips,
        RestrictSpecialEquipsExclusive,
        NoStarEgg,
        EXPStarsAnywhere,
        MimicsAnywhere,
        SlotsAnywhere,
        ShuffleBeetlemania,
        ShuffleMagikoopaChest,
        ShuffleWeddingGear,
        AnnoyingChests,
        FireworksSetting,
    ]
    _id: str = "T"


class ItemLocationSubcategory(FlagCategory):
    """Collection of settings related to item availability."""

    _flags: list[type[Flag]] = [
        InvisibleFlagsSetting,
        KeyItemsAnywhere,
        StarPieceAvailability,
        RemakePostgame,
        EnabledRegularChecks,
    ]
    _id: str = "L"


class BehaviourSubcategory(FlagCategory):
    """Collection of settings related to item and minigame behaviour."""

    _flags: list[type[Flag]] = [
        PoisonMushroom,
        ReplaceItems,
        QuickHitCoins,
        EXPChallenge,
        GrateGuyPrizeThreshold,
        KnifeGuyPrizeThreshold,
        SuitePrize1Threshold,
        SuitePrize2Threshold,
        SuitePrize3Threshold,
        SuitePrize4Threshold,
        SuitePrize5Threshold,
        SuitePrize6Threshold,
        SuperJump1Threshold,
        SuperJump2Threshold,
    ]
    _id: str = "I"


class ItemsCategory(FlagCategory):
    """Pan-collection of settings related to items."""

    _name: str = "Items & Star Pieces"
    _subcategories: list[type[FlagCategory]] = [
        StarPiecesCategory,
        ItemShuffleSubcategory,
        ItemLocationSubcategory,
        BehaviourSubcategory,
    ]
    _id: str = "ItemsCategory"


class AreaAccessSubcategory(FlagCategory):
    """Collection of settings related to area gating logic."""

    _flags: list[type[Flag]] = [
        BanditsWayGate,
        ForestMazeGate,
        Moleville1Gate,
        PipeVaultGate,
        BoosterTowerGate,
        MarrymoreGate,
        SeaGate,
        BelomeTempleGate,
        MonstroTownGate,
        BarrelVolcanoGate,
        BowsersKeepGate,
        FactoryGate,
    ]
    _size: int = 3
    _id: str = "A"


class OtherAccessSubcategory(FlagCategory):
    """Collection of settings related to event gating logic."""

    _flags: list[type[Flag]] = [
        YaridovichGate,
        SkipMustyFearsSequence,
        BowserDoorRequirements,
        StarPiecesRequired,
        CasinoWarp,
        BucketWarp,
        FastTravel,
        WinCondition,
    ]
    _size: int = 3
    _id: str = "O"


class PuzzleCategory(FlagCategory):
    """Collection of settings related to puzzles."""

    _name: str = "Puzzles & Minigames"
    _flags: list[type[Flag]] = [
        BallSolitaireShuffle,
        MagicButtonShuffle,
        QuizShuffle,
        RandomTadpolePondSong,
        RandomSunkenShipPassword,
        BowserDoorShuffle,
        SkipMinecart,
        BetterTips,
    ]
    _size: int = 3
    _id: str = "G"


class ShopsCategory(FlagCategory):
    """Collection of settings related to shops."""

    _flags: list[type[Flag]] = [
        ShuffleShops,
        ShopQuality,
        NoPickMeUps,
        BiasShopShuffle,
        ShowEquips,
        FreeShops,
    ]
    _size: int = 3
    _id: str = "S"


class AccessCategory(FlagCategory):
    """Pan-collection of settings related to logical access and puzzles."""

    _name: str = "Progression & Shops"
    _subcategories: list[type[FlagCategory]] = [
        AreaAccessSubcategory,
        OtherAccessSubcategory,
        PuzzleCategory,
        ShopsCategory,
    ]
    _id: str = "AccessCategory"


class BossPositionSubcategory(FlagCategory):
    """Collection of settings related to boss placement."""

    _flags: list[type[Flag]] = [
        BossShuffle,
        BossShuffleScaleStats,
        SafeLogicProgression,
        BossReplaceMinigameSprites,
        DifferentiateRepeatedBosses,
        ShuffledBosses,
    ]
    _size: int = 4
    _id: str = "B"


class BossStatSubcategory(FlagCategory):
    """Collection of settings related to enemy stats."""

    _flags: list[type[Flag]] = [
        EnemyStats,
        EnemyDrops,
        EnemyFormations,
        EnemyAttacks,
        EnemyNoSafetyChecks,
        EnemySpells,
        ExperienceNoRegular,
        ExperienceNoBosses,
    ]
    _size: int = 4
    _id: str = "E"


class BossCheeseSubcategory(FlagCategory):
    """Collection of settings related to boss exploits."""

    _flags: list[type[Flag]] = [
        RequireBossFights,
        NoGenoWhirlExor,
        FixMagikoopa,
        NoOHKO,
    ]
    _size: int = 4
    _id: str = "F"


class BossCategory(FlagCategory):
    """Pan-collection of settings related to bosses."""

    _name: str = "Enemies & Boss Fights"
    _subcategories: list[type[FlagCategory]] = [
        BossPositionSubcategory,
        BossStatSubcategory,
        BossCheeseSubcategory,
    ]
    _id: str = "BossCategory"


class AccessibilitySubcategory(FlagCategory):
    """Collection of settings related to accessibility."""

    _flags: list[type[Flag]] = [RemoveFlashes]
    _size: int = 4
    _id: str = "R"


class MusicSubcategory(FlagCategory):
    """Collection of settings related to music cosmetics."""

    _flags: list[type[Flag]] = [
        BossShuffleMusic,
        ShuffledMusic,
    ]
    _size: int = 4
    _id: str = "R"


class PaletteSubcategory(FlagCategory):
    """Collection of settings related to visual cosmetics."""

    _flags: list[type[Flag]] = [PaletteSwaps, ChangeNames, JapaneseABXY]
    _size: int = 4
    _id: str = "R"


class CosmeticCategory(FlagCategory):
    """Pan-collection of settings related to things that don't affect logic."""

    _name: str = "Cosmetics"
    _subcategories: list[type[FlagCategory]] = [
        PaletteSubcategory,
        MusicSubcategory,
        AccessibilitySubcategory,
        RemakeNames,
    ]
    _id: str = "CosmeticCategory"


FlagCategoryT = TypeVar(
    "FlagCategoryT",
    CharacterRecruitmentSubcategory,
    CharacterEquipmentSubcategory,
    CharacterStatsSpellsSubcategory,
    PartyCategory,
    StarPiecesCategory,
    ItemShuffleSubcategory,
    ItemLocationSubcategory,
    BehaviourSubcategory,
    ItemsCategory,
    AreaAccessSubcategory,
    OtherAccessSubcategory,
    PuzzleCategory,
    ShopsCategory,
    AccessCategory,
    BossPositionSubcategory,
    BossStatSubcategory,
    BossCheeseSubcategory,
    BossCategory,
    AccessibilitySubcategory,
    MusicSubcategory,
    PaletteSubcategory,
    CosmeticCategory,
    FlagCategory)

CATEGORIES = (
    PartyCategory,
    ItemsCategory,
    AccessCategory,
    BossCategory,
    CosmeticCategory)
