from typing import List, Type, TypeVar

from randomizer.types.world.flags.categories.classes import FlagCategory
from randomizer.types.world.flags.classes import Flag
from randomizer.types.world.flags.flags import (
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
    YaridovichGate,
)


class CharacterRecruitmentSubcategory(FlagCategory):
    _flags: List[Type[Flag]] = [
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
    _flags: List[Type[Flag]] = [
        EquipmentCharacters,
        EquipmentProperties,
        EquipmentNoSafety,
        StarPieceHints,
    ]
    _size: int = 4
    _id: str = "Q"


class CharacterStatsSpellsSubcategory(FlagCategory):
    _flags: List[Type[Flag]] = [
        EXPMultiplier,
        CharacterStats,
        CharacterLearnedSpells,
        CharacterSpellStats,
        CharacterSpellElements,
        UncapSuperJumps,
        AvailableSpells,
    ]
    _size: int = 4
    _id: str = "C"


class PartyCategory(FlagCategory):
    _name: str = "Party & Equipment"
    _subcategories: List[Type[FlagCategory]] = [
        CharacterRecruitmentSubcategory,
        CharacterEquipmentSubcategory,
        CharacterStatsSpellsSubcategory,
    ]
    _id: str = "PartyCategory"


class StarPiecesCategory(FlagCategory):
    _flags: List[Type[Flag]] = [
        ShuffleStarPieces,
        TotalStarPieces,
        EnabledBossChecks,
        StarPiecesRestrictedByArea,
    ]
    _size: int = 3
    _id: str = "X"


class ItemShuffleSubcategory(FlagCategory):
    _flags: List[Type[Flag]] = [
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
    _flags: List[Type[Flag]] = [
        InvisibleFlagsSetting,
        KeyItemsAnywhere,
        StarPieceAvailability,
        EnabledRegularChecks,
    ]
    _id: str = "L"


class BehaviourSubcategory(FlagCategory):
    _flags: List[Type[Flag]] = [
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
    _name: str = "Items & Star Pieces"
    _subcategories: List[Type[FlagCategory]] = [
        StarPiecesCategory,
        ItemShuffleSubcategory,
        ItemLocationSubcategory,
        BehaviourSubcategory,
    ]
    _id: str = "ItemsCategory"


class AreaAccessSubcategory(FlagCategory):
    _flags: List[Type[Flag]] = [
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
    _flags: List[Type[Flag]] = [
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
    _name: str = "Puzzles & Minigames"
    _flags: List[Type[Flag]] = [
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
    _flags: List[Type[Flag]] = [
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
    _name: str = "Progression & Shops"
    _subcategories: List[Type[FlagCategory]] = [
        AreaAccessSubcategory,
        OtherAccessSubcategory,
        PuzzleCategory,
        ShopsCategory,
    ]
    _id: str = "AccessCategory"


class BossPositionSubcategory(FlagCategory):
    _flags: List[Type[Flag]] = [
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
    _flags: List[Type[Flag]] = [
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
    _flags: List[Type[Flag]] = [
        RequireBossFights,
        NoGenoWhirlExor,
        FixMagikoopa,
        NoOHKO,
    ]
    _size: int = 4
    _id: str = "F"


class BossCategory(FlagCategory):
    _name: str = "Enemies & Boss Fights"
    _subcategories: List[Type[FlagCategory]] = [
        BossPositionSubcategory,
        BossStatSubcategory,
        BossCheeseSubcategory,
    ]
    _id: str = "BossCategory"


class AccessibilitySubcategory(FlagCategory):
    _flags: List[Type[Flag]] = [RemoveFlashes]
    _size: int = 4
    _id: str = "R"


class MusicSubcategory(FlagCategory):
    _flags: List[Type[Flag]] = [
        BossShuffleMusic,
        ShuffledMusic,
    ]
    _size: int = 4
    _id: str = "R"


class PaletteSubcategory(FlagCategory):
    _flags: List[Type[Flag]] = [PaletteSwaps, ChangeNames, JapaneseABXY]
    _size: int = 4
    _id: str = "R"


class CosmeticCategory(FlagCategory):
    _name: str = "Cosmetics"
    _subcategories: List[Type[FlagCategory]] = [
        PaletteSubcategory,
        MusicSubcategory,
        AccessibilitySubcategory,
    ]
    _id: str = "CosmeticCategory"


TFlagCategory = TypeVar(
    "TFlagCategory",
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
    FlagCategory,
)
