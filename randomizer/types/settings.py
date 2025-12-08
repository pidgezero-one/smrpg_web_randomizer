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


class Settings:
    _debug_mode: bool = False
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

    # ******** Party
    @property
    def shuffle_characters(self) -> bool:
        return ShuffleCharacters().enabled

    @property
    def max_characters(self) -> int:
        return MaxCharacters().value

    @property
    def starting_characters(self) -> list[StartingCharacterEnum]:
        return StartingCharacters().enabled

    @property
    def play_as_starter(self) -> bool:
        return PlayAsStarter().enabled

    # ******** Equipment
    @property
    def equipment_characters(self) -> EquipmentCharactersOptions:
        return EquipmentCharacters().selected

    @property
    def equipment_properties(self) -> EquipmentPropertiesOptions:
        return EquipmentProperties().selected

    @property
    def ignore_namesake_properties(self) -> bool:
        return IgnoreNamesakeProperties().enabled

    @property
    def star_piece_hints(self) -> bool:
        return StarPieceHints().enabled

    # ******** Stats & Spells
    @property
    def exp_multiplier(self) -> EXPMultiplierOptions:
        return EXPMultiplier().selected

    @property
    def character_stats(self) -> bool:
        return CharacterStats().enabled

    @property
    def character_learned_spells(self) -> bool:
        return CharacterLearnedSpells().enabled

    @property
    def character_spell_stats(self) -> bool:
        return CharacterSpellStats().enabled

    @property
    def infuse_spell_elements(self) -> bool:
        return InfuseSpellElements().enabled

    @property
    def character_spell_elements(self) -> bool:
        return CharacterSpellElements().enabled

    @property
    def uncap_super_jumps(self) -> bool:
        return UncapSuperJumps().enabled

    @property
    def available_spells(self) -> list[LearnableSpellEnum]:
        return AvailableSpells().enabled

    # ******** Star Pieces
    @property
    def shuffle_star_pieces(self) -> bool:
        return ShuffleStarPieces().enabled

    @property
    def total_star_pieces(self) -> int:
        return TotalStarPieces().value

    @property
    def enabled_boss_checks(self) -> list:
        return EnabledBossChecks().enabled

    @property
    def disperse_star_pieces(self) -> bool:
        return DisperseStarPieces().enabled

    # ******** Item shuffle
    @property
    def shuffle_items(self) -> bool:
        return ShuffleItems().enabled

    @property
    def item_quality(self) -> ItemQualityOptions:
        return ItemQuality().selected

    @property
    def bias_item_shuffle(self) -> bool:
        return BiasItemShuffle().enabled

    @property
    def no_star_egg(self) -> bool:
        return NoStarEgg().enabled

    @property
    def restrict_special_equips(self) -> bool:
        return RestrictSpecialEquips().enabled

    @property
    def exp_stars_anywhere(self) -> bool:
        return EXPStarsAnywhere().enabled

    @property
    def mimics_anywhere(self) -> bool:
        return MimicsAnywhere().enabled

    @property
    def slots_anywhere(self) -> bool:
        return SlotsAnywhere().enabled

    @property
    def shuffle_beetlemania(self) -> bool:
        return ShuffleBeetlemania().enabled

    @property
    def shuffle_magikoopa_chest(self) -> bool:
        return ShuffleMagikoopaChest().enabled

    @property
    def shuffle_wedding_gear(self) -> bool:
        return ShuffleWeddingGear().enabled

    @property
    def annoying_chests(self) -> bool:
        return AnnoyingChests().enabled

    @property
    def fireworks_setting(self) -> FireworksOptions:
        return FireworksSetting().selected

    # ******** Progression availability
    @property
    def key_items_anywhere(self) -> bool:
        return KeyItemsAnywhere().enabled

    @property
    def star_piece_availability(self) -> bool:
        return StarPieceAvailability().enabled

    @property
    def invisible_flags_setting(self) -> bool:
        return InvisibleFlagsSetting().enabled

    @property
    def remake(self) -> bool:
        return Remake().enabled

    @property
    def enabled_regular_checks(self) -> list[ShuffleLocationSelector]:
        return EnabledRegularChecks().enabled

    @property
    def replace_items(self) -> bool:
        return ReplaceItems().enabled

    @property
    def poison_mushroom(self) -> bool:
        return PoisonMushroom().enabled

    @property
    def exp_challenge(self) -> EXPChallengeOptions:
        return EXPChallenge().selected

    @property
    def grate_guy_prize_threshold(self) -> int:
        return GrateGuyPrizeThreshold().value

    @property
    def knife_guy_prize_threshold(self) -> int:
        return KnifeGuyPrizeThreshold().value

    @property
    def suite_prize_1_threshold(self) -> int:
        return SuitePrize1Threshold().value

    @property
    def suite_prize_2_threshold(self) -> int:
        return SuitePrize2Threshold().value

    @property
    def suite_prize_3_threshold(self) -> int:
        return SuitePrize3Threshold().value

    @property
    def suite_prize_4_threshold(self) -> int:
        return SuitePrize4Threshold().value

    @property
    def suite_prize_5_threshold(self) -> int:
        return SuitePrize5Threshold().value

    @property
    def suite_prize_6_threshold(self) -> int:
        return SuitePrize6Threshold().value

    @property
    def super_jump_1_threshold(self) -> int:
        return SuperJump1Threshold().value

    @property
    def super_jump_2_threshold(self) -> int:
        return SuperJump2Threshold().value

    # ******** Progression Gating
    @property
    def bandits_way_gate(self) -> BanditsWayGating:
        return BanditsWayGate().selected

    @property
    def kero_sewers_gate(self) -> KeroSewersGating:
        return KeroSewersGate().selected

    @property
    def forest_maze_gate(self) -> ForestMazeGating:
        return ForestMazeGate().selected

    @property
    def pipe_vault_gate(self) -> PipeVaultGating:
        return PipeVaultGate().selected

    @property
    def moleville_1_gate(self) -> Moleville1Gating:
        return Moleville1Gate().selected

    @property
    def booster_tower_gate(self) -> BoosterTowerGating:
        return BoosterTowerGate().selected

    @property
    def booster_hill_gate(self) -> BoosterHillGating:
        return BoosterHillGate().selected

    @property
    def marrymore_gate(self) -> MarrymoreGating:
        return MarrymoreGate().selected

    @property
    def yaridovich_gate(self) -> YaridovichGating:
        return YaridovichGate().selected

    @property
    def sea_gate(self) -> SeaGating:
        return SeaGate().selected

    @property
    def lands_end_gate(self) -> LandsEndGating:
        return LandsEndGate().selected

    @property
    def belome_temple_gate(self) -> BelomeTempleGating:
        return BelomeTempleGate().selected

    @property
    def monstro_town_gate(self) -> MonstroTownGating:
        return MonstroTownGate().selected

    @property
    def skip_musty_fears_sequence(self) -> bool:
        return SkipMustyFearsSequence().enabled

    @property
    def nimbus_gate(self) -> NimbusGating:
        return NimbusGate().selected

    @property
    def barrel_volcano_gate(self) -> BarrelVolcanoGating:
        return BarrelVolcanoGate().selected

    @property
    def bowsers_keep_gate(self) -> BowsersKeepGating:
        return BowsersKeepGate().selected

    @property
    def factory_gate(self) -> FactoryGating:
        return FactoryGate().selected

    @property
    def bowser_door_requirements(self) -> int:
        return BowserDoorRequirements().value

    @property
    def star_pieces_required(self) -> int:
        return StarPiecesRequired().value

    @property
    def casino_warp(self) -> bool:
        return CasinoWarp().enabled

    @property
    def bucket_warp(self) -> bool:
        return BucketWarp().enabled

    @property
    def fast_travel(self) -> bool:
        return FastTravel().enabled

    @property
    def win_condition(self) -> WinConditions:
        return WinCondition().selected

    # ******** Puzzles
    @property
    def ball_solitaire_shuffle(self) -> bool:
        return BallSolitaireShuffle().enabled

    @property
    def magic_button_shuffle(self) -> bool:
        return MagicButtonShuffle().enabled

    @property
    def quiz_shuffle(self) -> bool:
        return QuizShuffle().enabled

    @property
    def random_tadpole_pond_song(self) -> bool:
        return RandomTadpolePondSong().enabled

    @property
    def random_sunken_ship_password(self) -> bool:
        return RandomSunkenShipPassword().enabled

    @property
    def bowser_door_shuffle(self) -> bool:
        return BowserDoorShuffle().enabled

    @property
    def skip_minecart(self) -> bool:
        return SkipMinecart().enabled

    @property
    def better_tips(self) -> bool:
        return BetterTips().enabled

    # ******** Shops
    @property
    def shuffle_shops(self) -> bool:
        return ShuffleShops().enabled

    @property
    def shop_quality(self) -> ShopQualities:
        return ShopQuality().selected

    @property
    def bias_shop_shuffle(self) -> bool:
        return BiasShopShuffle().enabled

    @property
    def no_pick_me_ups(self) -> bool:
        return NoPickMeUps().enabled

    @property
    def show_equips(self) -> bool:
        return ShowEquips().enabled

    @property
    def free_shops(self) -> bool:
        return FreeShops().enabled

    # ******** Enemies & Bosses
    @property
    def boss_shuffle(self) -> bool:
        return BossShuffle().enabled

    @property
    def boss_shuffle_scale_stats(self) -> BossScaleOptions:
        return BossShuffleScaleStats().selected

    @property
    def boss_replace_minigame_sprites(self) -> bool:
        return BossReplaceMinigameSprites().enabled

    @property
    def differentiate_repeated_bosses(self) -> bool:
        return DifferentiateRepeatedBosses().enabled

    @property
    def include_henchmen(self) -> bool:
        return IncludeHenchmen().enabled

    @property
    def shuffled_bosses(self) -> list[ShuffledBossEnum]:
        return ShuffledBosses().enabled

    @property
    def enemy_stats(self) -> EnemyStatsShuffleOptions:
        return EnemyStats().selected

    @property
    def enemy_drops(self) -> bool:
        return EnemyDrops().enabled

    @property
    def enemy_formations(self) -> bool:
        return EnemyFormations().enabled

    @property
    def enemy_attacks(self) -> bool:
        return EnemyAttacks().enabled

    @property
    def enemy_spells(self) -> bool:
        return EnemySpells().enabled

    @property
    def experience_no_regular(self) -> bool:
        return ExperienceNoRegular().enabled

    @property
    def experience_no_bosses(self) -> bool:
        return ExperienceNoBosses().enabled

    @property
    def skip_boss_fights(self) -> bool:
        return SkipBossFights().enabled

    @property
    def no_geno_whirl_exor(self) -> bool:
        return NoGenoWhirlExor().enabled

    @property
    def fix_magikoopa(self) -> bool:
        return FixMagikoopa().enabled

    @property
    def no_ohko(self) -> bool:
        return NoOHKO().enabled

    # ******** Cosmetics and Accessibility
    @property
    def palette_swaps(self) -> bool:
        return PaletteSwaps().enabled

    @property
    def change_names(self) -> bool:
        return ChangeNames().enabled

    @property
    def remake_names(self) -> bool:
        return RemakeNames().enabled

    @property
    def canon_names(self) -> bool:
        return CanonNames().enabled

    @property
    def peach(self) -> bool:
        return Peach().enabled

    @property
    def japanese_abxy(self) -> bool:
        return JapaneseABXY().enabled

    @property
    def boss_shuffle_music(self) -> bool:
        return BossShuffleMusic().enabled

    @property
    def shuffled_music(self) -> list:
        return ShuffledMusic().enabled

    @property
    def remove_flashes(self) -> bool:
        return RemoveFlashes().enabled

    @property
    def hold_b(self) -> bool:
        return HoldB().enabled


# To consider when shuffling locations
# Inclusions:
# - Exclude remake_only when remake is unchecked
# 