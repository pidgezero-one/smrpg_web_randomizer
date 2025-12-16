from typing import cast
from .flags import *

B64_TABLE: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def _get_flag_string_from_flag_collection(categories: list[type[FlagCategoryT]]) -> str:
    """Converts a series of settings into a copy-pastable string."""
    flag_strings: list[str] = []
    for category in categories:
        for subcategory in category().subcategories:
            flagstring_parts = []
            for f in subcategory().flags:
                flag = f()
                if isinstance(flag, BooleanFlag):
                    if flag.enabled:
                        flagstring_parts.append(flag.id)
                elif isinstance(flag, SelectOneFlag):
                    flagstring_parts.append(f"{flag.id}:{flag.selected}")
                elif isinstance(flag, RangeFlag):
                    flagstring_parts.append(f"{flag.id}:{flag.value}")
                elif isinstance(flag, CategorizationFlag):
                    ctr = 0
                    choice_rep = 0
                    choice_rep_string = ""
                    for f in flag.options:
                        if f in flag.enabled:
                            choice_rep += 1 << ctr
                        ctr += 1
                        if ctr == 6:
                            choice_rep_string += B64_TABLE[choice_rep]
                            ctr = 0
                            choice_rep = 0
                    if ctr > 0:
                        choice_rep_string += B64_TABLE[choice_rep]
                    flagstring_parts.append("{flag.id}:{choice_rep_string}")
            if len(flagstring_parts) != 0:
                flag_strings.append(f"{subcategory.id}.{flagstring_parts}")

    flag_string = "     ".join(flag_strings)

    return flag_string.strip()


FlagT = TypeVar("FlagT", bound=Flag)

class Settings:
    _debug_mode: bool = False
    _flags: dict[type[FlagT], Flag]
    _override: dict = {}

    @property
    def override(self) -> dict:
        """Override certain settings (developer mode)"""
        return self._override

    @property
    def flag_string(self) -> str:
        """Computed flag string for these settings."""

        non_cosmetic_categories = [
            category
            for category in CATEGORIES
            if not isinstance(category, CosmeticCategory)
        ]

        return _get_flag_string_from_flag_collection(non_cosmetic_categories)

    def __init__(self) -> None:
        # todo: get setting params in here
        self._flags = {
            ShuffleCharacters: ShuffleCharacters(),
            MaxCharacters: MaxCharacters(),
            StartingCharacters: StartingCharacters(),
            PlayAsStarter: PlayAsStarter(),
            EquipmentCharacters: EquipmentCharacters(),
            EquipmentProperties: EquipmentProperties(),
            IgnoreNamesakeProperties: IgnoreNamesakeProperties(),
            StarPieceHints: StarPieceHints(),
            EXPMultiplier: EXPMultiplier(),
            CharacterStats: CharacterStats(),
            CharacterLearnedSpells: CharacterLearnedSpells(),
            CharacterSpellStats: CharacterSpellStats(),
            InfuseSpellElements: InfuseSpellElements(),
            CharacterSpellElements: CharacterSpellElements(),
            UncapSuperJumps: UncapSuperJumps(),
            AvailableSpells: AvailableSpells(),
            ShuffleStarPieces: ShuffleStarPieces(),
            TotalStarPieces: TotalStarPieces(),
            EnabledBossChecks: EnabledBossChecks(),
            ProgressionLogicDifficulty: ProgressionLogicDifficulty(),
            DisperseStarPieces: DisperseStarPieces(),
            ShuffleItems: ShuffleItems(),
            ItemQuality: ItemQuality(),
            BiasItemShuffle: BiasItemShuffle(),
            NoStarEgg: NoStarEgg(),
            RestrictSpecialEquips: RestrictSpecialEquips(),
            EXPStarsAnywhere: EXPStarsAnywhere(),
            MimicsAnywhere: MimicsAnywhere(),
            SlotsAnywhere: SlotsAnywhere(),
            ShuffleBeetlemania: ShuffleBeetlemania(),
            ShuffleMagikoopaChest: ShuffleMagikoopaChest(),
            ShuffleWeddingGear: ShuffleWeddingGear(),
            AnnoyingChests: AnnoyingChests(),
            FireworksSetting: FireworksSetting(),
            KeyItemsAnywhere: KeyItemsAnywhere(),
            StarPieceAvailability: StarPieceAvailability(),
            InvisibleFlagsSetting: InvisibleFlagsSetting(),
            Remake: Remake(),
            EnabledRegularChecks: EnabledRegularChecks(),
            ReplaceItems: ReplaceItems(),
            PoisonMushroom: PoisonMushroom(),
            EXPChallenge: EXPChallenge(),
            GrateGuyPrizeThreshold: GrateGuyPrizeThreshold(),
            KnifeGuyPrizeThreshold: KnifeGuyPrizeThreshold(),
            SuitePrize1Threshold: SuitePrize1Threshold(),
            SuitePrize2Threshold: SuitePrize2Threshold(),
            SuitePrize3Threshold: SuitePrize3Threshold(),
            SuitePrize4Threshold: SuitePrize4Threshold(),
            SuitePrize5Threshold: SuitePrize5Threshold(),
            SuitePrize6Threshold: SuitePrize6Threshold(),
            SuperJump1Threshold: SuperJump1Threshold(),
            SuperJump2Threshold: SuperJump2Threshold(),
            BanditsWayGate: BanditsWayGate(),
            KeroSewersGate: KeroSewersGate(),
            ForestMazeGate: ForestMazeGate(),
            PipeVaultGate: PipeVaultGate(),
            Moleville1Gate: Moleville1Gate(),
            BoosterTowerGate: BoosterTowerGate(),
            BoosterHillGate: BoosterHillGate(),
            MarrymoreGate: MarrymoreGate(),
            YaridovichGate: YaridovichGate(),
            SeaGate: SeaGate(),
            LandsEndGate: LandsEndGate(),
            BelomeTempleGate: BelomeTempleGate(),
            MonstroTownGate: MonstroTownGate(),
            SkipMustyFearsSequence: SkipMustyFearsSequence(),
            NimbusGate: NimbusGate(),
            BarrelVolcanoGate: BarrelVolcanoGate(),
            BowsersKeepGate: BowsersKeepGate(),
            FactoryGate: FactoryGate(),
            BowserDoorRequirements: BowserDoorRequirements(),
            StarPiecesRequired: StarPiecesRequired(),
            CasinoWarp: CasinoWarp(),
            BucketWarp: BucketWarp(),
            FastTravel: FastTravel(),
            WinCondition: WinCondition(),
            BallSolitaireShuffle: BallSolitaireShuffle(),
            MagicButtonShuffle: MagicButtonShuffle(),
            QuizShuffle: QuizShuffle(),
            RandomTadpolePondSong: RandomTadpolePondSong(),
            RandomSunkenShipPassword: RandomSunkenShipPassword(),
            BowserDoorShuffle: BowserDoorShuffle(),
            SkipMinecart: SkipMinecart(),
            BetterTips: BetterTips(),
            ShuffleShops: ShuffleShops(),
            ShopQuality: ShopQuality(),
            BiasShopShuffle: BiasShopShuffle(),
            NoPickMeUps: NoPickMeUps(),
            ShowEquips: ShowEquips(),
            FreeShops: FreeShops(),
            BossShuffle: BossShuffle(),
            BossShuffleScaleStats: BossShuffleScaleStats(),
            BossReplaceMinigameSprites: BossReplaceMinigameSprites(),
            DifferentiateRepeatedBosses: DifferentiateRepeatedBosses(),
            IncludeHenchmen: IncludeHenchmen(),
            ShuffledBosses: ShuffledBosses(),
            EnemyStats: EnemyStats(),
            EnemyDrops: EnemyDrops(),
            EnemyFormations: EnemyFormations(),
            EnemyAttacks: EnemyAttacks(),
            EnemySpells: EnemySpells(),
            ExperienceNoRegular: ExperienceNoRegular(),
            ExperienceNoBosses: ExperienceNoBosses(),
            SkipBossFights: SkipBossFights(),
            NoGenoWhirlExor: NoGenoWhirlExor(),
            FixMagikoopa: FixMagikoopa(),
            NoOHKO: NoOHKO(),
            PaletteSwaps: PaletteSwaps(),
            ChangeNames: ChangeNames(),
            RemakeNames: RemakeNames(),
            CanonNames: CanonNames(),
            Peach: Peach(),
            JapaneseABXY: JapaneseABXY(),
            BossShuffleMusic: BossShuffleMusic(),
            ShuffledMusic: ShuffledMusic(),
            RemoveFlashes: RemoveFlashes(),
            HoldB: HoldB(),
        }

    @property
    def flags(self) -> dict[type[Flag], Flag]:
        """All settings flags."""
        return self._flags

    def get_flag(self, flag_type: type[FlagT]) -> FlagT:
        """Get a flag instance with proper typing."""
        return cast(FlagT, self._flags[flag_type])
    
    def is_flag_value(self, flag_class: type[FlagT], value: Any) -> bool:
        """Check if a setting is set to the given value."""
        flag = self.get_flag(flag_class)
        if isinstance(flag, (BooleanFlag, RangeFlag, SelectOneFlag)):
            return flag.value == value
        if isinstance(flag, CategorizationFlag):
            return value in flag.enabled
        raise RandomizerSettingsException(
            f"is_flag_value unknown flag type {type(flag)}"
        )
    
    def isflag_enabled(self, flag_class: type[BooleanFlag]) -> bool:
        """Check if a boolean flag is on or not."""
        return self.is_flag_value(flag_class, True)
