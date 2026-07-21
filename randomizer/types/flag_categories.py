from __future__ import annotations
from typing import TypeVar
from .flags import *  # noqa: F401,F403  (all flag classes + FlagError + bases)
from .check_flags import *  # noqa: F401,F403  (EnabledRegularChecks, EnabledBossChecks, ShuffledBosses)


class FlagCategory:
    """Base class for a collection of settings."""

    _id: str = ""
    _name: str = ""
    _subcategories: "list[type[FlagCategory]]" = []
    _flags: list[type[Flag]] = []
    _size: int = 3

    @property
    def id(self) -> str:
        """An identifier for this collection to use internally."""
        return self._id

    @property
    def name(self) -> str:
        """An identifier for this collection to appear in the frontend."""
        return self._name

    @property
    def subcategories(self) -> "list[type[FlagCategory]]":
        """Subcategories for this collection."""
        return self._subcategories

    @property
    def flags(self) -> list[type[Flag]]:
        """Individual settings that belong in this collection."""
        return self._flags

    @property
    def size(self) -> int:
        """Something to do with the frontend that I don't remember"""
        return self._size


class CharacterRecruitmentSubcategory(FlagCategory):
    """Collection of settings related to character recruitment."""

    _name: str = "Character Recruitment"
    _flags: list[type[Flag]] = [
        ShuffleCharacters,
        MaxCharacters,
        AllowAllySwitching,
        AvailableCharacters,
        StartingCharacters,
    ]
    _size: int = 4
    _id: str = "P"


class CharacterEquipmentSubcategory(FlagCategory):
    """Collection of settings related to equipment properties."""

    _name: str = "Character Equipment"
    _flags: list[type[Flag]] = [
        EquipmentCharacters,
        EquipmentProperties,
        IgnoreNamesakeProperties,
        StarPieceHints,
    ]
    _size: int = 4
    _id: str = "Q"


class CharacterStatsSpellsSubcategory(FlagCategory):
    """Collection of settings related to learnable spells."""

    _name: str = "Character Stats & Spells"
    _flags: list[type[Flag]] = [
        EXPMultiplier,
        CharacterStats,
        CharacterLearnedSpells,
        CharacterSpellStats,
        InfuseSpellElements,
        CharacterSpellElements,
        UncapSuperJumps,
        UncapMaxFP,
        AvailableSpells,
    ]
    _size: int = 4
    _id = "C"


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
        ProgressionLogicDifficulty,
        DisperseStarPieces,
    ]
    _size: int = 3
    _id: str = "X"


class ItemShuffleSubcategory(FlagCategory):
    """Collection of settings related to item distribution."""

    _name: str = "Item Shuffle"
    _flags: list[type[Flag]] = [
        ShuffleItems,
        ItemQuality,
        AnnoyingChests,
        BiasItemShuffle,
        NoStarEgg,
        RestrictSpecialEquips,
        EXPStarsAnywhere,
        ShuffleHillFlowers,
        MimicsAnywhere,
        SlotsAnywhere,
        ShuffleBeetlemania,
        ShuffleMagikoopaChest,
        ShuffleWeddingGear,
        ShuffleMarioDoll,
        ShuffleCookies,
        FireworksSetting,
    ]
    _id: str = "T"


class ItemLocationSubcategory(FlagCategory):
    """Collection of settings related to item availability."""

    _name: str = "Item Locations"
    _flags: list[type[Flag]] = [
        KeyItemsAnywhere,
        StarPieceAvailability,
        SpellsAnywhere,
        InvisibleFlagsSetting,
        Remake,
        EnabledRegularChecks,
    ]
    _id: str = "L"


class BehaviourSubcategory(FlagCategory):
    """Collection of settings related to item and minigame behaviour."""

    _name: str = "Behaviour & Minigames"
    _flags: list[type[Flag]] = [
        ReplaceItems,
        PoisonMushroom,
        EXPChallenge,
        GrateGuyPrizeThreshold,
        KnifeGuyPrizeThreshold,
        FixKnifeGuy,
        KnifeGuyFixedPrizeThreshold,
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

    _name: str = "Area Access"
    _flags: list[type[Flag]] = [
        BanditsWayGate,
        KeroSewersGate,
        ForestMazeGate,
        PipeVaultGate,
        Moleville1Gate,
        BoosterTowerGate,
        BoosterHillGate,
        MarrymoreGate,
        SeaGate,
        LandsEndGate,
        BelomeTempleGate,
        MonstroTownGate,
        NimbusGate,
        BarrelVolcanoGate,
        BowsersKeepGate,
        FactoryGate,
    ]
    _size: int = 3
    _id: str = "A"


class OtherAccessSubcategory(FlagCategory):
    """Collection of settings related to event gating logic."""

    _name: str = "Other Access & Win Condition"
    _flags: list[type[Flag]] = [
        YaridovichGate,
        WinCondition,
        StarPiecesRequired,
        BowserDoorRequirements,
        CasinoWarp,
        BucketWarp,
        FastTravel,
        SkipMinecart,
        SkipAnts,
        SkipMustyFearsSequence,
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
        QuizIncludeNonSmrpg,
        RandomTadpolePondSong,
        RandomSunkenShipPassword,
        RandomMinecartTrack,
        RedBarrels,
        BowserDoorShuffle,
        BetterTips,
    ]
    _size: int = 3
    _id: str = "G"


class ShopsCategory(FlagCategory):
    """Collection of settings related to shops."""

    _name: str = "Shops"
    _flags: list[type[Flag]] = [
        ShuffleShops,
        ShopQuality,
        BiasShopShuffle,
        NoPickMeUps,
        ShowEquips,
        FreeShops,
        ProtectSpecialItems,
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

    _name: str = "Boss Position"
    _flags: list[type[Flag]] = [
        BossShuffle,
        BossShuffleScaleStats,
        DontAutoheal,
        KeepMinigameSpritesIntact,
        DifferentiateRepeatedBosses,
        ShuffledBosses,
    ]
    _size: int = 4
    _id: str = "B"


class BossStatSubcategory(FlagCategory):
    """Collection of settings related to enemy stats."""

    _name: str = "Enemy Stats"
    _flags: list[type[Flag]] = [
        EnemyStats,
        EnemyDrops,
        EnemyFormations,
        EnemyAttacks,
        EnemySpells,
        ExperienceNoRegular,
        ExperienceNoBosses,
    ]
    _size: int = 4
    _id: str = "E"


class BossCheeseSubcategory(FlagCategory):
    """Collection of settings related to boss exploits."""

    _name: str = "Boss Exploits"
    _flags: list[type[Flag]] = [
        SkipBossFights,
        NoGenoWhirlExor,
        FixMagikoopa,
        NoOHKO,
        Punchinello2BobombDifficulty,
        FixInvincibility,
        SeeYa,
    ]
    _size: int = 4
    _id: str = "F"


class BossCategory(FlagCategory):
    """Pan-collection of settings related to bosses."""

    _name: str = "Battles & Boss Fights"
    _subcategories: list[type[FlagCategory]] = [
        BossPositionSubcategory,
        BossStatSubcategory,
        BossCheeseSubcategory,
    ]
    _id: str = "BossCategory"


class AccessibilitySubcategory(FlagCategory):
    """Collection of settings related to accessibility."""

    _name: str = "Accessibility"
    _flags: list[type[Flag]] = [RemoveFlashes, HoldB]
    _size: int = 3
    _id: str = "R"


class MusicSubcategory(FlagCategory):
    """Collection of settings related to music cosmetics."""

    _name: str = "Music"
    _flags: list[type[Flag]] = [BossShuffleMusic, ShuffledMusic]
    _size: int = 3
    _id: str = "R"


class PaletteSubcategory(FlagCategory):
    """Collection of settings related to visual cosmetics."""

    _name: str = "Visual Cosmetics"
    _flags: list[type[Flag]] = [
        JapaneseABXY,
        MarioPaletteChoice,
        MallowPaletteChoice,
        GenoPaletteChoice,
        BowserPaletteChoice,
        ToadstoolPaletteChoice,
    ]
    _size: int = 3
    _id: str = "R"


class NamesCategory(FlagCategory):

    _name: str = "Names"
    _flags: list[type[Flag]] = [
        PlayAsStarter,
        ChangeNames,
        RemakeNames,
        CanonNames,
        Peach,
    ]
    _size: int = 3
    _id: str = "R"


class CosmeticCategory(FlagCategory):
    """Pan-collection of settings related to things that don't affect logic."""

    _name: str = "Player Experience"
    _subcategories: list[type[FlagCategory]] = [
        AccessibilitySubcategory,
        MusicSubcategory,
        PaletteSubcategory,
        NamesCategory,
    ]


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
    NamesCategory,
    CosmeticCategory,
    FlagCategory,
)

CATEGORIES = (
    PartyCategory,
    ItemsCategory,
    AccessCategory,
    BossCategory,
    CosmeticCategory,
)

#############

"""Base classes for settings presets."""


class Preset:
    """A pre-created settings string"""

    _name: str = ""
    _description: str = ""
    _flags: str = ""

    @property
    def name(self) -> str:
        """The name of this preset as it appears on the site"""
        return self._name

    @property
    def description(self) -> str:
        """A brief description of who this preset is meant for and what it does"""
        return self._description

    @property
    def flags(self) -> str:
        """The string that corresponds to the desired settings"""
        return self._flags

    @classmethod
    def id(cls):
        """An identifier for this preset to use internally."""
        return cls.__name__


class ReturningVeteran(Preset):
    _name: str = '"I haven\'t played in a while..."'
    _description: str = (
        "For people who played SMRPG growing up and may do an occasional playthrough nowadays but don't necessarily know all of its obscure secrets inside out."
    )
    _flags: str = (
        "P(rchars)     Q(perms:random_accessories_all)     C(exp:triple)     X(rstars|bosses:/39b8v//)     T(ritems|itemqual:completely_random)     L(keys_anywhere|postgame|chests://P9/3/B//HAA0/Xt4BgAAA89BZOPKhAwi/N+c///7V+xP0N4+//vP7+/C)     A(bw:mushroom_way|fm:open|bh:tower|mm:tower|sea:open)     O(doorcount:1|fasttravel)     S(rshops|shopqual:completely_random|showperms)     B(rboss|pool:f79v3N/P)     E(drops|formations)     F(skips|seeya)"
    )


class VeteranPreset(Preset):

    _name: str = '"I know everything about SMRPG"'
    _description: str = (
        "For people who know the original game (and its remake) upside down and inside out. Everything is shuffled and no checks are disabled. Your knowledge of equipment properties and monster behaviours will come in handy."
    )
    _flags: str = (
        "P(rchars)     Q(perms:vanilla_accessories_all|hints)     C(exp:double|uncap)     X(rstars|disperse)     T(ritems|biasitems|restrict_monstro|xpstars|hill|mimics|slots|beetle|kamek|marry|doll|cookies|fireworks:progressive)     L(keys_anywhere|stars_anywhere|moveflags|postgame)     I(fake|xpstar:bosses|fix_kg)     A(fm:open|bh:tower|bk:star_6)     O(doorcount:1|fasttravel|skipcart)     G(rng)     S(rshops|biasshops|showperms)     B(rboss)     E(drops)     F(skips)"
    )


class RandomizerPreset(Preset):

    _name: str = '"I ♥ randomizer logic"'
    _description: str = (
        "A highly access-restrictive preset for people who enjoy solving the puzzle of randomized progression."
    )
    _flags: str = (
        "P(rchars)     Q(perms:random_accessories_all|props:random|hints)     C(exp:double|charspells|infuse|uncap)     X(rstars)     T(ritems|itemqual:completely_random|biasitems|restrict_monstro|xpstars|hill|mimics|slots|beetle|kamek|marry|doll|cookies|fireworks:progressive)     L(keys_anywhere|stars_anywhere|spells_anywhere|moveflags|postgame)     I(replace|fake|xpstar:bosses|fix_kg)     A(ks:rfc|pv:geno|me:bowyer|bh:kggg|land:elder|tmpl:key|mt:belome_2|nl:paint|bv:valentina|bk:axem|wf:exor)     O(seaside:johnny|doorcount:1|cwarp|bwarp|fasttravel|skipcart|skipant)     G(ball|button|quiz|melody|pwd|rng)     S(rshops|shopqual:mostly_random|biasshops|showperms)     B(rboss)     E(drops)     F(skips)"
    )


class GodPreset(Preset):

    _name: str = '"The world\'s my oyster"'
    _description: str = "A preset where your order of operations is wide open."
    _flags: str = (
        "P(rchars|starters:4:5:6:7:8)     Q(perms:random_accessories_all|props:random|unsafe|hints)     C(stats|charspells)     X(rstars|total_sp:7)     T(ritems|itemqual:completely_random|xpstars|hill|mimics|slots|beetle|kamek|marry|doll|cookies|fireworks:progressive)     L(keys_anywhere|stars_anywhere|spells_anywhere|moveflags|postgame)     I(replace|fake|xpstar:none|fix_kg|sj1:10|sj2:20)     A(bw:open|fm:open|bt:open|mm:open|sea:open|mt:open|bv:open|bk:open|wf:open)     O(seaside:open|objective:stars|endgame:7|doorcount:1|cwarp|bwarp|fasttravel|skipcart|skipant|skip_musty)     G(ball|button|quiz|quizext|melody|pwd|doorshuffle|rng)     S(rshops|shopqual:completely_random|showperms)     B(rboss|bossscale:godmode)     E(enemystats:full_random|drops|formations|attacks|enemyspells|noregexp|nobossexp)     F(skips|nowhirl|nobigbang|noko|seeya)"
    )


class Speedrunner(Preset):
    _name: str = '"I just speedrun this game"'
    _description: str = (
        "For any% speedrunners who don't remember much about casual playthroughs or MOTS speedruns (but might have done Low Level once or twice)."
    )
    _flags: str = "Q(hints)     C(exp:double|uncap)     X(rstars|bosses:fz9v3t/f)     T(ritems|hill|marry)     L(keys_anywhere|stars_anywhere|chests://P//3/D//XA/9/f9+9/b4/99/5//d9gzi/d+f//n71/9/8P7////v7+vf)     I(replace|fake)     A(bw:mushroom_way|fm:open|bh:tower|mm:tower|sea:open)     O(doorcount:1|fasttravel|skipcart)     G(rng)     S(showperms)     B(rboss|allsprites|pool://9////f)     F(skips|seeya)"


class LegacyQuick(Preset):
    _name: str = "Legacy Quick Preset"
    _description: str = (
        "A preset that approximates the settings of the old 'Quick' preset from 8.x.x."
    )
    _flags: str = (
        "P(rchars|starters:4:5:6)     Q(perms:random|props:random)     C(exp:triple|stats|charspells)     X(rstars|bosses:fzFu3Nfe)     T(ritems|itemqual:completely_random|restrict_monstro)     I(replace)     A(bw:open|fm:open|bt:open|mm:open|sea:open|mt:open|bv:open|bk:open|wf:star_6)     O(seaside:open|doorcount:1|cwarp|bwarp|fasttravel|skipcart|skipant|skip_musty)     S(rshops|shopqual:all|showperms|free)     B(rboss|pool:fz9v3N/P)     E(drops)"
    )


class LegacyCasual(Preset):
    _name: str = "Legacy Casual Preset"
    _description: str = (
        "A preset that approximates the settings of the old 'Casual' preset from 8.x.x."
    )
    _flags: str = (
        "P(rchars|starters:4:5:6)     Q(perms:random)     C(exp:double|stats)     X(rstars|bosses:f7/v3N/f)     T(ritems|itemqual:completely_random|restrict_monstro)     I(replace|xpstar:bosses)     A(bw:open|fm:open|bt:open|mm:open|sea:open|mt:open|bv:open|bk:star_6)     O(doorcount:1|cwarp)     G(ball|button|quiz|doorshuffle)     S(rshops|shopqual:all|showperms)     B(rboss|pool:fz9v3N/P)     E(drops|formations)"
    )


class LegacyIntermediate(Preset):
    _name: str = "Legacy Intermediate Preset"
    _description: str = (
        "A preset that approximates the settings of the old 'Intermediate' preset from 8.x.x."
    )
    _flags: str = (
        "P(rchars|starters:4:6:5)     Q(perms:random|props:random)     C(exp:double|stats|charspells|spellstats)     X(rstars|total_sp:7|bosses:/HE+//f+)     T(ritems|itemqual:completely_random|restrict_monstro)     I(replace)     A(bw:open|fm:open|bt:open|mm:open|sea:open|mt:open|bv:open|bk:open|wf:open)     O(seaside:open|endgame:7|doorcount:2|cwarp)     G(ball|button|quiz|doorshuffle)     S(rshops|shopqual:all|showperms)     B(rboss|pool:fz9v3N/P)     E(drops|formations)"
    )


class LegacyAdvanced(Preset):
    _name: str = "Legacy Advanced Preset"
    _description: str = (
        "A preset that approximates the settings of the old 'Advanced' preset from 8.x.x."
    )
    _flags: str = (
        "P(rchars|starters:4)     Q(perms:random|props:random)     C(exp:double|stats|charspells|spellstats)     X(rstars|total_sp:7|bosses://F+//f+)     T(ritems|itemqual:mostly_random|restrict_monstro)     L(keys_anywhere|chests:////////////////////////////////////f8////////////////////)     I(replace|xpstar:stars)     A(bw:open|fm:open|bt:open|mm:open|sea:open|mt:open|bv:open|bk:open)     O(seaside:open|endgame:7)     G(ball|button|quiz|doorshuffle)     S(rshops|shopqual:mostly_random|showperms)     B(rboss|pool:fz9v3t/P)     E(enemystats:full_random|drops|formations|attacks)"
    )


class LegacyExpert(Preset):
    _name: str = "Legacy Expert Preset"
    _description: str = (
        "A preset that approximates the settings of the old 'Expert' preset from 8.x.x."
    )
    _flags: str = (
        "P(rchars|starters:4)     Q(perms:random|props:random|unsafe)     C(exp:double|stats|charspells|spellstats)     X(rstars|total_sp:7|bosses://F+//f+)     T(ritems|itemqual:mostly_random|restrict_monstro)     L(keys_anywhere)     I(replace|fake|xpstar:stars)     A(bw:open|fm:open|bt:open|mm:open|sea:open|mt:open|bv:open|bk:open|wf:open)     O(seaside:open|endgame:7)     G(ball|button|quiz|doorshuffle)     S(rshops|showperms)     B(rboss|bossscale:vanilla|pool:f79v3t/P)     E(enemystats:full_random|drops|formations|attacks|enemyspells)     F(nowhirl|nobigbang|noko)"
    )


class LegacyAsyncTournament(Preset):
    _name: str = "Legacy 2021 Fall Async Tournament Preset"
    _description: str = (
        "A preset that approximates the settings of the old '2021 Fall Async Tournament' preset from 8.x.x."
    )
    _flags: str = (
        "P(rchars|starters:4)     Q(perms:random|props:random)     C(exp:double|stats|charspells|spellstats)     X(rstars|total_sp:7|bosses:f7Fu3Nfe)     T(ritems|itemqual:completely_random|restrict_monstro)     I(replace|fake)     A(bw:open|fm:open|bt:open|mm:open|sea:open|mt:open|bv:open|bk:open)     O(endgame:7|doorcount:2|cwarp)     G(button|doorshuffle)     S(rshops|shopqual:all|showperms)     B(rboss|pool:/39////f)     E(enemystats:full_random|drops|formations|attacks)"
    )


class LegacyBingo(Preset):
    _name: str = "Legacy Standard Bingo Flags Preset"
    _description: str = (
        "A preset that approximates the settings of the old 'Standard Bingo Flags' preset from 8.x.x."
    )
    _flags: str = (
        "P(rchars|starters:4)     Q(perms:random|props:random)     C(exp:triple|stats|charspells|spellstats)     X(rstars|total_sp:7)     T(ritems|itemqual:completely_random|restrict_monstro)     L(keys_anywhere|chests:////////////////////////////////////f8//////////////v/////)     I(fake)     A(bw:open|fm:open|bt:open|mm:open|sea:open|mt:open|bv:open|bk:open)     O(seaside:open|endgame:7|doorcount:2|cwarp)     G(button|doorshuffle)     S(rshops|shopqual:all)     B(rboss|pool:f79v3t/P)     E(enemystats:full_random|drops|formations|attacks)"
    )


class Pidge(Preset):

    _name: str = "Pidge loves this preset"
    _description: str = "She likes testing with this, so it's here for convenience."
    _flags: str = (
        "P(rchars|starters:4)     Q(perms:vanilla_accessories_all|props:some|hints)     C(exp:double|charspells|infuse|uncap)     X(rstars)     T(ritems|xpstars|hill|mimics|slots|beetle|kamek|marry|doll|cookies|fireworks:progressive)     L(keys_anywhere|stars_anywhere|spells_anywhere|moveflags|postgame)     I(replace|fake|xpstar:bosses|fix_kg)     A(ks:rfc|pv:geno|me:geno|bh:kggg|mm:tower|land:elder|tmpl:key|nl:paint|bv:valentina|bk:axem|wf:open)     O(doorcount:1|cwarp|bwarp|fasttravel|skipcart|skipant)     G(quiz|melody|pwd|rng)     S(rshops|showperms)     B(rboss|pool://9////f)     E(drops)     F(skips|seeya)"
    )


PRESETS = [
    ReturningVeteran,
    VeteranPreset,
    RandomizerPreset,
    GodPreset,
    Speedrunner,
    LegacyQuick,
    LegacyCasual,
    LegacyIntermediate,
    LegacyAdvanced,
    LegacyExpert,
    LegacyAsyncTournament,
    LegacyBingo,
    Pidge,
]
