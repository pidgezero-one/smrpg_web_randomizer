"""Randomization logic for grants."""

from copy import copy
from random import choice, choices, randint, random, shuffle
from typing import Dict, List, Optional, Type, Union
from scipy.stats import gamma
from randomizer.entities.characters import (
    Bowser,
    Geno,
    Mallow,
    Mario,
    Toadstool,
)
from randomizer.entities.items import (
    BanditsWayStar,
    Beetlemania,
    Brooch,
    Coins1,
    Coins10,
    Crown,
    EarlierTimes,
    Fireworks,
    Flower,
    FrogCoin,
    GoodieBag,
    InfiniteCoins,
    KeroSewersStar,
    LandsEndStar2,
    LandsEndStar3,
    LandsEndVolcanoStar,
    LuckyJewel,
    MimicFightInitiator1,
    MimicFightInitiator2,
    MimicFightInitiator3,
    MolevilleMinesStar,
    MultiFrogCoin,
    NimbusLandStar,
    ProgressiveEgg,
    ProgressiveFireworks,
    RecoveryMushroom,
    Ring,
    SeaStar,
    SeeYa,
    Shoes,
    SignalRing,
    SlotMachineChest,
    StarEgg,
    StarPiece1,
    StarPiece2,
    StarPiece3,
    StarPiece4,
    StarPiece5,
    StarPiece6,
    StarPiece7,
    Wallet,
    YouMissed,
)
from randomizer.entities.progress_locations import (
    BowserSpellSlot1,
    BowserSpellSlot2,
    BowserSpellSlot3,
    BowserSpellSlot4,
    BowserSpellSlot5,
    BowserSpellSlot6,
    GenoSpellSlot1,
    GenoSpellSlot2,
    GenoSpellSlot3,
    GenoSpellSlot4,
    GenoSpellSlot5,
    GenoSpellSlot6,
    MallowSpellSlot1,
    MallowSpellSlot2,
    MallowSpellSlot3,
    MallowSpellSlot4,
    MallowSpellSlot5,
    MallowSpellSlot6,
    MarioSpellSlot1,
    MarioSpellSlot2,
    MarioSpellSlot3,
    MarioSpellSlot4,
    MarioSpellSlot5,
    MarioSpellSlot6,
    ToadstoolSpellSlot1,
    ToadstoolSpellSlot2,
    ToadstoolSpellSlot3,
    ToadstoolSpellSlot4,
    ToadstoolSpellSlot5,
    ToadstoolSpellSlot6,
    StartingCharacter1,
    FireworksShopItem,
    KeepAfterObstaclesBossChest,
    MushroomKingdomInnPurchase,
)
from randomizer.entities.progress_locations.helpers.classes import (
    MarrymoreChapelLocation,
)
from randomizer.entities.spells import SuperJump
from randomizer.types.bosses import Boss
from randomizer.types.characters import Character
from randomizer.types.items import (
    Coins,
    Equipment,
    InvincibilityStar,
    Item,
    MimicFightChestAssignment,
    RecruitedCharacter,
    RegularItem,
    StarPiece,
    ItemUnique,
)
from randomizer.types.numbers.classes import UInt16
from randomizer.types.overworld_scripts.arguments.variables import PRIMARY_TEMP_7000
from randomizer.types.overworld_scripts.event_scripts.classes import EventScript
from randomizer.types.overworld_scripts.event_scripts.commands.commands import (
    Jmp,
    JmpIfVarEqualsConst,
    JmpToEvent,
    Set7000ToCurrentLevel,
)
from randomizer.types.overworld_scripts.event_scripts.commands.types.classes import (
    UsableEventScriptCommand,
)
from randomizer.types.progress_locations import (
    BossFightLocation,
    BossStarPiecePrize,
    CharacterRecruitLocation,
    CharacterSpellSlot,
    ChestLocation,
    FreestandingLocation,
    FrogDiscipleShopItem,
    GrantLocation,
    Inventory,
    ItemLocation,
    ProgressLocation,
    TreasureShopItem,
)
from randomizer.types.spells import CharacterSpell
from randomizer.types.world import GameWorld
from randomizer.types.world.classes import WorldBuildingException
from randomizer.types.world.flags import (
    BanditsWayGating,
    BoosterTowerGating,
    FireworksOptions,
    ForestMazeGating,
    ItemQualities,
    LearnableSpells,
    PlayableCharacters,
    SeaGating,
    ShuffleLocationSelector,
    WinConditions,
    AnnoyingChests,
    AvailableCharacters,
    AvailableSpells,
    BanditsWayGate,
    BiasItemShuffle,
    BoosterTowerGate,
    BossShuffle,
    CharacterLearnedSpells,
    EXPStarsAnywhere,
    EnabledBossChecks,
    EnabledRegularChecks,
    FireworksSetting,
    ForestMazeGate,
    ItemQuality,
    MaxCharacters,
    MimicsAnywhere,
    NoStarEgg,
    ReplaceItems,
    RestrictSpecialEquipsExclusive,
    SeaGate,
    ShuffleBeetlemania,
    ShuffleCharacters,
    ShuffleItems,
    ShuffleMagikoopaChest,
    ShuffleStarPieces,
    ShuffleWeddingGear,
    ShuffledBosses,
    SlotsAnywhere,
    StartingCharacter,
    TotalStarPieces,
    WinCondition,
)

_dummy_allpurpose_item = RegularItem(None)
_dummy_allpurpose_item.set_price(1)

_REWARD_TABLE = [
    (2, SlotMachineChest),
    (5, InvincibilityStar),
    (5, RecoveryMushroom),
    (7, Flower),
    (6, FrogCoin),
    (6, Coins),
    (69, _dummy_allpurpose_item),
]


def _get_max_tier(world: GameWorld) -> int:
    item_setting = world.settings.get_flag(ItemQuality)
    if item_setting == ItemQualities.TIER_3:
        return 3
    elif item_setting == ItemQualities.TIER_2:
        return 2
    elif item_setting == ItemQualities.TIER_1:
        return 1
    return 4


def _generate_nonrequired_item(
    world: GameWorld, location: ProgressLocation
) -> Optional[Item]:
    max_tier: int = _get_max_tier(world)
    rewards = copy(_REWARD_TABLE)
    if not world.settings.is_boolean_flag_enabled(SlotsAnywhere):
        rewards = [r for r in rewards if r[1] != SlotMachineChest]
    if not world.settings.is_boolean_flag_enabled(EXPStarsAnywhere):
        rewards = [r for r in rewards if r[1] != InvincibilityStar]
    table = [r for r in rewards if location.can_accept(r[1])]

    weights, possible_options = list(zip(*table))
    result = choices(possible_options, weights=weights, k=1)[0]
    item: Optional[Item] = None
    if result == InvincibilityStar:
        all_choices = [
            world.get_item_instance(i)
            for i in [
                BanditsWayStar,
                KeroSewersStar,
                MolevilleMinesStar,
                SeaStar,
                LandsEndVolcanoStar,
                LandsEndVolcanoStar,
                NimbusLandStar,
                LandsEndStar2,
                LandsEndStar3,
            ]
        ]
        item = choice(all_choices)
    elif result == Coins:
        if isinstance(location, FreestandingLocation):
            if randint(1, 10) > 3:
                item = world.get_item_instance(Coins10)
            else:
                item = world.get_item_instance(Coins1)
        else:
            value = gamma.rvs(loc=80, size=1) // 1
            item = Coins(value, world)
    elif result == FrogCoin:
        if isinstance(location, FreestandingLocation):
            item = world.get_item_instance(FrogCoin)
        else:
            if randint(1, 10) > 1:
                item = world.get_item_instance(FrogCoin)
            else:
                possibilities = [2, 3, 4, 5, 6, 7, 8, 9, 10]
                value = choices(
                    possibilities, weights=(10, 9, 8, 7, 6, 5, 4, 3, 2), k=1
                )[0]
                item = MultiFrogCoin(world, value)
    elif isinstance(result, RegularItem):
        all_choices = [
            i
            for i in world.items
            if (
                i.unique == ItemUnique.NEVER
                or (
                    i.unique == ItemUnique.BALANCED_ONLY
                    and not world.settings.is_flag_value(
                        ItemQuality, ItemQualities.ORIGINAL
                    )
                )
            )
            and i.tier <= max_tier
            and location.can_accept(i)
        ]
        all_choices = []
        if isinstance(location, TreasureShopItem):
            all_choices = [
                i for i in all_choices if i.unique == ItemUnique.BALANCED_ONLY
            ]
        else:
            all_equips = [i for i in all_choices if isinstance(i, Equipment)]
            all_nonequips = [i for i in all_choices if not isinstance(i, Equipment)]
            if world.settings.is_boolean_flag_enabled(RestrictSpecialEquipsExclusive):
                all_equips = [e for e in all_equips if not e.special_equip]
            if len(all_equips) == 0:
                all_choices = all_nonequips
            elif len(all_nonequips) == 0:
                all_choices = all_equips
            else:
                if randint(0, 2) == 0:
                    all_choices = all_equips
                else:
                    all_choices = all_nonequips
        if len(all_choices) == 0:
            raise ValueError(f"could not fill {location}")
        possibilities = [1, 2, 3, 4]
        if world.settings.is_boolean_flag_enabled(BiasItemShuffle):
            if location.tier == 2:
                weights = [25, 40, 25, 10]
            else:
                weights = [10, 25, 40, 25]
        else:
            weights = [15, 25, 40, 20]
        possibilities = possibilities[0:max_tier]
        weights = tuple(weights[0:max_tier])
        choicelist = []
        value = choices(possibilities, weights, k=1)[0]
        while len(choicelist) == 0:
            choicelist = [i for i in all_choices if i.tier == value]
            # if empty, keep trying worse tiers
            p_index = possibilities.index(value)
            if p_index == 0:
                break
            value = possibilities[p_index - 1]
        if len(choicelist) == 0:
            raise ValueError(f"could not fill {location}")
        item = choice(choicelist)
        if (
            not item.shuffle_as_key_item
            and not (isinstance(item, Equipment) and item.special_equip)
            and item.tier == 1
            and world.settings.is_boolean_flag_enabled(ReplaceItems)
        ):
            item_tmp = Coins(item.price // 2, world)
            if location.can_accept(item_tmp):
                item = item_tmp
    else:
        item = world.get_item_instance(result)
    return item


def _included_characters(world: GameWorld) -> List[Character]:
    """Returns the list of character instances who will be recruitable in the seed."""
    max_chars: int = world.settings.get_flag(MaxCharacters).value
    excluded = world.settings.get_flag(AvailableCharacters).disabled
    allowed = world.settings.get_flag(AvailableCharacters).enabled

    required = []

    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.MARIO):
        required.append(PlayableCharacters.MARIO)
    if world.settings.is_flag_value(
        BoosterTowerGate, BoosterTowerGating.MALLOW
    ) or world.settings.is_flag_value(BanditsWayGate, BanditsWayGating.MALLOW):
        required.append(PlayableCharacters.MALLOW)
    if world.settings.is_flag_value(
        BoosterTowerGate, BoosterTowerGating.GENO
    ) or world.settings.is_flag_value(ForestMazeGate, ForestMazeGating.GENO):
        required.append(PlayableCharacters.GENO)
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.BOWSER):
        required.append(PlayableCharacters.BOWSER)
    if world.settings.is_flag_value(
        BoosterTowerGate, BoosterTowerGating.TOADSTOOL
    ) or world.settings.is_flag_value(SeaGate, SeaGating.TOADSTOOL):
        required.append(PlayableCharacters.TOADSTOOL)

    starter = world.settings.get_flag(StartingCharacter).value
    if starter not in required and starter != PlayableCharacters.RANDOM:
        required.append(starter)

    errcheck = [c for c in required if c in excluded]
    if len(errcheck) > 0:
        raise ValueError(f"excluded character is required: {errcheck}")

    if max_chars > len(required):
        remaining = max_chars - len(required)
        required.extend(choices([c for c in allowed if c not in required], k=remaining))

    included_characters = [c for c in world.characters if c.original_name in required]
    if world.get_character_instance(Mario) not in included_characters:
        world.remove_locations(
            [
                MarioSpellSlot1,
                MarioSpellSlot2,
                MarioSpellSlot3,
                MarioSpellSlot4,
                MarioSpellSlot5,
                MarioSpellSlot6,
            ]
        )
    if world.get_character_instance(Mallow) not in included_characters:
        world.remove_locations(
            [
                MallowSpellSlot1,
                MallowSpellSlot2,
                MallowSpellSlot3,
                MallowSpellSlot4,
                MallowSpellSlot5,
                MallowSpellSlot6,
            ]
        )
    if world.get_character_instance(Geno) not in included_characters:
        world.remove_locations(
            [
                GenoSpellSlot1,
                GenoSpellSlot2,
                GenoSpellSlot3,
                GenoSpellSlot4,
                GenoSpellSlot5,
                GenoSpellSlot6,
            ]
        )
    if world.get_character_instance(Bowser) not in included_characters:
        world.remove_locations(
            [
                BowserSpellSlot1,
                BowserSpellSlot2,
                BowserSpellSlot3,
                BowserSpellSlot4,
                BowserSpellSlot5,
                BowserSpellSlot6,
            ]
        )
    if world.get_character_instance(Toadstool) not in included_characters:
        world.remove_locations(
            [
                ToadstoolSpellSlot1,
                ToadstoolSpellSlot2,
                ToadstoolSpellSlot3,
                ToadstoolSpellSlot4,
                ToadstoolSpellSlot5,
                ToadstoolSpellSlot6,
            ]
        )

    return included_characters


def _collect_items(
    world: GameWorld, collected: Optional[Inventory] = None
) -> Inventory:
    my_items = Inventory()
    if collected is not None:
        my_items.extend(collected)

    all_locations = (
        world.boss_locations
        + world.boss_star_pieces
        + world.character_recruit_locations
        + world.character_spell_slots
        + world.character_spotted_locations
        + world.item_locations
    )
    available_locations = [l for l in all_locations if l.contents is not None]

    while True:
        search_locations = [l for l in available_locations if l.can_access(my_items)]
        available_locations = [
            l for l in available_locations if l not in search_locations
        ]
        found_items = Inventory(
            [
                world.get_item_instance(type(l.contents))
                for l in search_locations
                if l.contents is not None
            ]
        )
        if len(found_items) == 0:
            break
        my_items.extend(found_items)

    return my_items


def _place_items(
    world: GameWorld,
    items_to_place: Inventory,
    locations: List[
        Union[
            ChestLocation,
            GrantLocation,
            FreestandingLocation,
            CharacterSpellSlot,
            CharacterRecruitLocation,
            BossStarPiecePrize,
            BossFightLocation,
        ]
    ],
    base_inventory: Optional[Inventory] = None,
) -> Inventory:
    if base_inventory is None:
        base_inventory = Inventory()
    remaining_fill_items = copy(items_to_place)
    item_loop = copy(items_to_place)

    item: Item
    for item in item_loop:
        remaining_fill_items_without_this_item: Inventory = copy(remaining_fill_items)
        remaining_fill_items_without_this_item.remove(item)
        collection = copy(base_inventory)
        collection += remaining_fill_items_without_this_item
        assumed_items = _collect_items(world, collection)
        fillable_locations = [
            l
            for l in locations
            if l.contents is None and l.can_access(assumed_items) and l.can_accept(item)
        ]

        # bias worse items to worse locations when necessary and possible
        if world.settings.is_boolean_flag_enabled(BiasItemShuffle):
            if item.tier <= 2:
                filtered_locations = [l for l in fillable_locations if l.tier <= 2]
            else:
                filtered_locations = [l for l in fillable_locations if l.tier > 2]
            if len(filtered_locations) > 0 and random() < 0.75:
                fillable_locations = filtered_locations

        if len(fillable_locations) > 0:
            priority = [
                l
                for l in fillable_locations
                if isinstance(l, (TreasureShopItem, FrogDiscipleShopItem))
            ]
            if len(priority) > 0:
                fillable_locations = priority

            remaining_fill_items.remove(item)

            to_fill = fillable_locations[0]

            if (
                world.settings.is_boolean_flag_enabled(ReplaceItems)
                and not item.shuffle_as_key_item
                and not (isinstance(item, Equipment) and item.special_equip)
            ):
                coins = Coins(item.price // 2, world)
                if to_fill.can_accept(coins):
                    item = coins

            if isinstance(to_fill, BossFightLocation):
                assert isinstance(item, Boss)
                to_fill.set_contents(item)
            elif isinstance(to_fill, BossStarPiecePrize):
                assert isinstance(item, StarPiece)
                to_fill.set_contents(item)
            elif isinstance(to_fill, CharacterRecruitLocation):
                assert isinstance(item, Character)
                to_fill.set_contents(item)
            elif isinstance(to_fill, CharacterSpellSlot):
                assert isinstance(item, CharacterSpell)
                to_fill.set_contents(item)
            else:
                assert isinstance(item, Item)
                to_fill.set_contents(item)

    return remaining_fill_items


def _fill_locations(
    world: GameWorld,
    locations: List[
        Union[
            ChestLocation,
            GrantLocation,
            FreestandingLocation,
            CharacterSpellSlot,
            CharacterRecruitLocation,
            BossStarPiecePrize,
            BossFightLocation,
        ]
    ],
    required_items: Inventory,
    extra_items: Optional[Inventory] = None,
    existing_inventory: Optional[Inventory] = None,
) -> Inventory:
    if extra_items is None:
        extra_items = Inventory()
    if existing_inventory is None:
        existing_inventory = Inventory()

    locations_to_fill = [l for l in locations]

    shuffle(locations_to_fill)
    shuffle(required_items)
    shuffle(extra_items)

    allowed_for_required = [
        l
        for l in locations_to_fill
        if isinstance(l, (CharacterSpellSlot, CharacterRecruitLocation))
        or l.name_enum not in world.settings.get_flag(EnabledRegularChecks).disabled
    ]

    # first pass
    remainder: Inventory = Inventory()
    remainder = _place_items(
        world, required_items, allowed_for_required, existing_inventory
    )

    # second pass
    locations_to_fill = [l for l in locations_to_fill if l.contents is None]
    allowed_for_required = [
        l
        for l in locations_to_fill
        if isinstance(l, (CharacterSpellSlot, CharacterRecruitLocation))
        or l.name_enum not in world.settings.get_flag(EnabledRegularChecks).disabled
    ]
    remainder = _place_items(
        world, required_items, allowed_for_required, existing_inventory
    )

    # fail case forcing retry: unplaced characters
    unplaced_characters = [i for i in remainder if isinstance(i, RecruitedCharacter)]
    if len(unplaced_characters) > 0:
        return remainder

    # deprioritize flowers, mushrooms, and frog coins,
    # in case we end up with more items than locations
    regular_items = Inventory(
        [
            i
            for i in extra_items
            if not isinstance(i, (Flower, RecoveryMushroom, FrogCoin))
        ]
    )
    expendable_items = Inventory(
        [i for i in extra_items if isinstance(i, (Flower, RecoveryMushroom, FrogCoin))]
    )

    # Reverse remaining empty locations, then fill extra items.
    locations_to_fill = [l for l in locations_to_fill if l.contents is None]
    locations_to_fill.reverse()

    # Prioritize frog shop and treasure seller since those are highly restrictive
    priority = [
        l
        for l in locations_to_fill
        if isinstance(l, (FrogDiscipleShopItem, TreasureShopItem))
    ]
    locations_to_fill = [l for l in locations_to_fill if l not in priority]
    locations_to_fill = priority + locations_to_fill

    # third pass
    _place_items(world, regular_items, locations_to_fill, existing_inventory)
    # third pass, expendable itels
    _place_items(world, expendable_items, locations_to_fill, existing_inventory)

    # If we have items left over, return them
    collected_items = set(_collect_items(world))
    leftover = set(required_items + extra_items) - collected_items
    return Inventory(leftover)


def _place_everything(world: GameWorld) -> None:
    remainder = Inventory()
    required_item_pool = Inventory()
    extra_item_pool = Inventory()

    all_locations = (
        world.boss_locations
        + world.boss_star_pieces
        + world.character_recruit_locations
        + world.character_spell_slots
        + world.item_locations
    )

    characters = _included_characters(world)

    # First: For anything that is NOT shuffled, place it in its original location.
    preset_locations: List[
        Union[ItemLocation, BossStarPiecePrize, CharacterRecruitLocation]
    ] = []
    if not world.settings.is_boolean_flag_enabled(ShuffleItems):
        preset_locations += [l for l in world.item_locations if not l.key_item_location]

    preset_locations += [
        l
        for l in world.item_locations
        if l.keep_original_item_if_excluded
        and l.name_enum in world.settings.get_flag(EnabledRegularChecks).disabled
    ]

    if not world.settings.is_boolean_flag_enabled(ShuffleStarPieces):
        preset_locations += world.boss_star_pieces
    else:
        bosses_to_ignore = world.settings.get_flag(EnabledBossChecks).disabled
        if (
            world.settings.is_flag_value(WinCondition, WinConditions.SEALED)
            and ShuffleLocationSelector.CULEX_BOSS not in bosses_to_ignore
        ):
            bosses_to_ignore.append(ShuffleLocationSelector.CULEX_BOSS)
        elif (
            world.settings.is_flag_value(WinCondition, WinConditions.FACTORY)
            and ShuffleLocationSelector.INNER_FACTORY_BOSS_FINAL not in bosses_to_ignore
        ):
            bosses_to_ignore.append(ShuffleLocationSelector.INNER_FACTORY_BOSS_FINAL)
        preset_locations += [
            l for l in world.boss_star_pieces if l.name_enum in bosses_to_ignore
        ]

    if not world.settings.is_boolean_flag_enabled(CharacterLearnedSpells):
        preset_locations += [l for l in world.item_locations if not l.key_item_location]

    if not world.settings.is_boolean_flag_enabled(ShuffleWeddingGear):
        preset_locations += [
            l for l in world.item_locations if isinstance(l, MarrymoreChapelLocation)
        ]

    if not world.settings.is_boolean_flag_enabled(ShuffleMagikoopaChest):
        preset_locations.append(
            world.get_location_instance(KeepAfterObstaclesBossChest)
        )

    if not world.settings.is_boolean_flag_enabled(ShuffleBeetlemania):
        preset_locations.append(world.get_location_instance(MushroomKingdomInnPurchase))

    if not world.settings.is_boolean_flag_enabled(SlotsAnywhere):
        preset_locations.extend(
            [l for l in world.item_locations if not l.original_item == SlotMachineChest]
        )

    if not world.settings.is_boolean_flag_enabled(MimicsAnywhere):
        preset_locations.extend(
            [
                l
                for l in world.item_locations
                if l.original_item is not None
                and not issubclass(l.original_item, MimicFightChestAssignment)
            ]
        )

    if not world.settings.is_boolean_flag_enabled(EXPStarsAnywhere):
        preset_locations.extend(
            [
                l
                for l in world.item_locations
                if l.original_item is not None
                and not issubclass(l.original_item, InvincibilityStar)
            ]
        )

    fireworks = world.settings.get_flag(FireworksSetting).value
    if fireworks == FireworksOptions.VANILLA:
        preset_locations.append(world.get_location_instance(FireworksShopItem))

    if not world.settings.is_boolean_flag_enabled(ShuffleCharacters):
        preset_locations += [
            l
            for l in world.character_recruit_locations
            if l.original_item is not None
            and world.get_character_instance(l.original_item) in characters
        ]

    for location in preset_locations:
        if location.original_item is not None:
            location.set_contents(world.get_item_instance(location.original_item))

    # do the same for boss fights, but they're a little different

    preset_bosses: List[BossFightLocation] = []
    if not world.settings.is_boolean_flag_enabled(BossShuffle):
        preset_bosses += world.boss_locations
    else:
        boss_exclusions = world.settings.get_flag(ShuffledBosses).disabled
        preset_bosses += [
            l for l in world.boss_locations if l.name_enum in boss_exclusions
        ]

    for location in preset_bosses:
        if location.original_item is not None:
            location.set_contents(location.original_item(world))

    # starting character

    starter = world.settings.get_flag(StartingCharacter).value
    if starter == PlayableCharacters.MARIO:
        world.get_location_instance(StartingCharacter1).set_contents(
            world.get_character_instance(Mario)
        )
    if starter == PlayableCharacters.MALLOW:
        world.get_location_instance(StartingCharacter1).set_contents(
            world.get_character_instance(Mallow)
        )
    if starter == PlayableCharacters.GENO:
        world.get_location_instance(StartingCharacter1).set_contents(
            world.get_character_instance(Geno)
        )
    if starter == PlayableCharacters.BOWSER:
        world.get_location_instance(StartingCharacter1).set_contents(
            world.get_character_instance(Bowser)
        )
    if starter == PlayableCharacters.TOADSTOOL:
        world.get_location_instance(StartingCharacter1).set_contents(
            world.get_character_instance(Toadstool)
        )

    # pool items

    # items required to unlock another check

    presets = [l.contents for l in all_locations if l.contents is not None]

    # item locations

    if world.settings.get_flag(ItemQuality).value == ItemQualities.ORIGINAL:
        extra_item_pool.extend(
            [
                world.get_item_instance(l.original_item)
                for l in world.item_locations
                if l.original_item is not None and l.contents is None
            ]
        )
    else:
        # These items should be in every seed.
        other_important_item_classes: List[Type[Item]] = [
            Wallet,
            Fireworks,
            ProgressiveEgg,
            ProgressiveEgg,
            ProgressiveEgg,
            SignalRing,
            SeeYa,
            GoodieBag,
            EarlierTimes,
            LuckyJewel,
            StarEgg,
            MimicFightInitiator1,
            MimicFightInitiator2,
            MimicFightInitiator3,
            Beetlemania,
            InfiniteCoins,
            Shoes,
            Brooch,
            Ring,
            Crown,
            YouMissed,
        ]
        required_item_pool.extend([i for i in world.items if i.shuffle_as_key_item])
        required_item_pool.extend(
            [
                world.get_item_instance(i)
                for i in other_important_item_classes
                if world.get_item_instance(i) not in presets
            ]
        )
    if world.settings.is_boolean_flag_enabled(NoStarEgg):
        required_item_pool = Inventory(
            [r for r in required_item_pool if not isinstance(r, StarEgg)]
        )
        extra_item_pool = Inventory(
            [r for r in extra_item_pool if not isinstance(r, StarEgg)]
        )
    if fireworks == FireworksOptions.PROGRESSIVE:
        required_item_pool = [
            i for i in required_item_pool if not isinstance(i, Fireworks)
        ]
        required_item_pool.extend([world.get_item_instance(ProgressiveFireworks)] * 3)

    # characters

    required_item_pool.extend(characters)

    # spells

    if LearnableSpells.SUPER_JUMP in world.settings.get_flag(AvailableSpells).enabled:
        required_item_pool.append(world.get_spell_instance(SuperJump))
    extra_item_pool.extend(
        [
            s
            for s in world.spells
            if isinstance(s, CharacterSpell) and s not in required_item_pool
        ]
    )

    # boss fights

    required_item_pool.extend(
        [b.original_item(world) for b in world.boss_locations if b.contents is None]
    )

    # star pieces

    sp_definitions = [
        StarPiece1,
        StarPiece2,
        StarPiece3,
        StarPiece4,
        StarPiece5,
        StarPiece6,
        StarPiece7,
    ]
    total_stars = world.settings.get_flag(TotalStarPieces).value
    sp_definitions = sp_definitions[:total_stars]
    required_item_pool.extend([world.get_item_instance(s) for s in sp_definitions])

    required_item_pool = Inventory([i for i in required_item_pool if i not in presets])
    crosscheck = copy(required_item_pool)

    remainder = _fill_locations(
        world,
        all_locations,
        required_item_pool,
        extra_item_pool,
        Inventory(presets),
    )
    remainder_check = [i for i in remainder if i in crosscheck]
    if len(remainder_check) > 0:
        raise WorldBuildingException

    remaining_locations = [l for l in world.item_locations if l.contents is None]
    for loc in remaining_locations:
        if not world.settings.get_flag(ItemQuality).value == ItemQualities.EMPTY:
            loc.set_contents(_generate_nonrequired_item(world, loc))
    remaining_locations = [
        l
        for l in world.item_locations
        if isinstance(l, ChestLocation) and l.contents is None
    ]
    # populate empty chests with YouMissed if setting enabled
    if world.settings.is_boolean_flag_enabled(AnnoyingChests):
        for loc in remaining_locations:
            loc.set_contents(world.get_item_instance(YouMissed))


class _Grant:
    jumps: List[UsableEventScriptCommand]
    executions: List[UsableEventScriptCommand]

    def __init__(
        self,
        jumps: List[UsableEventScriptCommand],
        executions: Optional[List[UsableEventScriptCommand]] = None,
    ):
        self.jumps = jumps
        if executions is None:
            self.executions = []
        else:
            self.executions = executions


def shuffle_all(world: GameWorld) -> None:
    """Shuffles the placement of everything in logic
    (items, boss fights, star pieces, characters, spells)."""
    _place_everything(world)

    grant_builders: Dict[UInt16, _Grant] = {}

    # update granter scripts to match character placements
    for loc in world.character_recruit_locations:
        character = loc.contents
        assert isinstance(character, Character) or character is None
        if character is None:
            continue
        # character joins party
        for event_id in loc.event_builder_identifiers:
            grant_builders[event_id] = _Grant([Set7000ToCurrentLevel()])
            recruitment_jump_command = JmpToEvent(character.container_script)
            grant_builders[event_id].executions.append(
                JmpToEvent(character.container_script)
            )
            for room_id in loc.room_ids:
                grant_builders[event_id].jumps.append(
                    JmpIfVarEqualsConst(
                        PRIMARY_TEMP_7000,
                        room_id,
                        [recruitment_jump_command.identifier.name],
                    )
                )
        # gating
        if isinstance(character, Mario) and world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.MARIO):
            # this location's container event should unlock booster tower
            loc.container_event
            
