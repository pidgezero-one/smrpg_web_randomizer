"""Per-section builders for the seed spoiler JSON.

Extracted from types/gameworld.py.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from randomizer.data.variables.shop_names import (
    SH00_MUSHROOM_KINGDOM,
    SH01_ROSE_TOWN_ITEM,
    SH02_ROSE_TOWN_ARMOR,
    SH03_FROG_DISCIPLE,
    SH04_MOLEVILLE,
    SH05_MARRYMORE,
    SH06_FROG_COIN_EMPORIUM,
    SH07_SEA_AND_SHIP_SHAMAN,
    SH08_SEASIDE_TOWN_MINION,
    SH09_JUICE_BAR_BASE,
    SH10_JUICE_BAR_ALTO,
    SH11_JUICE_BAR_TENOR,
    SH12_JUICE_BAR_SOPRANO,
    SH13_SEASIDE_WEAPON,
    SH14_SEASIDE_ARMOR,
    SH15_SEASIDE_ACCESSORY,
    SH16_SEASIDE_HEALTH_FOOD,
    SH17_MONSTRO,
    SH18_VOLCANO_ITEM,
    SH19_VOLCANO_ARMOR,
    SH20_GOOMBETTE,
    SH21_NIMBUS_LAND,
    SH22_KEEP_1,
    SH23_KEEP_2,
    SH24_FACTORY_TOAD,
)
from randomizer.types.flags import (
    BooleanFlag,
    CategorizationFlag,
    CategorizationFlagWithOrdinance,
    RangeFlag,
    SelectOneFlag,
)
from randomizer.types.prize import (SpellPrize)
from typing import (Any)

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld


def _get_locations_json(world: GameWorld) -> dict[str, str]:
    """Return a JSON-serializable dict of all locations and their prizes.

    Keys are location class names, values are prize class names or "None".
    For SpellPrize items, includes the character name in the format: "SpellName (CharacterName)"
    """
    result: dict[str, str] = dict()
    for loc_type, loc in world.locations.items():
        location_name = loc_type.__name__
        if loc.prize is None:
            prize_name = "None"
        else:
            prize_name = type(loc.prize).__name__
            # If it's a spell, include the character it's assigned to
            if isinstance(loc.prize, SpellPrize):
                character = loc.prize.character
                if character is not None:
                    character_name = character.__name__.replace(
                        "RecruitmentPrize", ""
                    )
                    prize_name = f"{prize_name} ({character_name})"
                else:
                    prize_name = f"{prize_name} (No Character)"
        result[location_name] = prize_name
    return result


def _get_spell_character_assignments_json(world: GameWorld) -> dict[str, str]:
    """Get JSON representation of all spell-to-character assignments.

    Returns a dictionary mapping spell names to their assigned character names.
    This works whether spells are in the general item pool or learned by level-up.
    """
    result: dict[str, str] = {}

    # Get all spell prizes from locations
    for loc in world.locations.values():
        if loc.prize and isinstance(loc.prize, SpellPrize):
            spell_name = type(loc.prize).__name__
            character = loc.prize.character
            if character is not None:
                character_name = character.__name__.replace("RecruitmentPrize", "")
                result[spell_name] = character_name
            else:
                result[spell_name] = "No Character"

    return result


def _get_palettes_json(world: GameWorld) -> dict[str, str]:
    """Get JSON representation of character palette names.

    Uses the palette's custom name if set, otherwise falls back to the class name.
    """

    def get_palette_name(palette: Any, original_name: str) -> str:
        # If palette has a custom name different from original, use it
        if hasattr(palette, "name") and palette.name != original_name:
            return palette.name
        # Otherwise use the class name
        return type(palette).__name__

    return {
        "Mario": get_palette_name(world.mario_palette, "Mario"),
        "Mallow": get_palette_name(world.mallow_palette, "Mallow"),
        "Geno": get_palette_name(world.geno_palette, "Geno"),
        "Bowser": get_palette_name(world.bowser_palette, "Bowser"),
        "Toadstool": get_palette_name(world.toadstool_palette, "Toadstool"),
    }


def _get_shops_json(world: GameWorld) -> dict[str, list[str]]:
    """Get JSON representation of all shops with their item names."""

    shop_names = {
        SH00_MUSHROOM_KINGDOM: "Mushroom Kingdom",
        SH01_ROSE_TOWN_ITEM: "Rose Town Item",
        SH02_ROSE_TOWN_ARMOR: "Rose Town Armor",
        SH03_FROG_DISCIPLE: "Frog Disciple",
        SH04_MOLEVILLE: "Moleville",
        SH05_MARRYMORE: "Marrymore",
        SH06_FROG_COIN_EMPORIUM: "Frog Coin Emporium",
        SH07_SEA_AND_SHIP_SHAMAN: "Sea/Ship Shaman",
        SH08_SEASIDE_TOWN_MINION: "Seaside Town (Minion)",
        SH09_JUICE_BAR_BASE: "Juice Bar (Base)",
        SH10_JUICE_BAR_ALTO: "Juice Bar (Alto)",
        SH11_JUICE_BAR_TENOR: "Juice Bar (Tenor)",
        SH12_JUICE_BAR_SOPRANO: "Juice Bar (Soprano)",
        SH13_SEASIDE_WEAPON: "Seaside Weapon",
        SH14_SEASIDE_ARMOR: "Seaside Armor",
        SH15_SEASIDE_ACCESSORY: "Seaside Accessory",
        SH16_SEASIDE_HEALTH_FOOD: "Seaside Health Food",
        SH17_MONSTRO: "Monstro Town",
        SH18_VOLCANO_ITEM: "Barrel Volcano Item",
        SH19_VOLCANO_ARMOR: "Barrel Volcano Armor",
        SH20_GOOMBETTE: "Goombette",
        SH21_NIMBUS_LAND: "Nimbus Land",
        SH22_KEEP_1: "Bowser's Keep 1",
        SH23_KEEP_2: "Bowser's Keep 2",
        SH24_FACTORY_TOAD: "Factory Toad",
    }

    result: dict[str, list[str]] = dict()
    for shop in world.shops.shops:
        if shop is None:
            continue
        shop_name = shop_names.get(shop.index, f"Shop {shop.index}")
        item_names = []
        for item in shop.items:
            if item is None:
                continue
            # item is a class type, get its _name attribute
            item_name = getattr(item, "_name", None)
            if item_name:
                item_names.append(item_name)
            else:
                item_names.append(item.__name__)
        result[shop_name] = item_names

    # Add text-based shops
    def get_item_name(item_type: type) -> str:
        name = getattr(item_type, "_name", None)
        if name:
            return name
        return item_type.__name__

    if world.room_service_items:
        result["Room Service (Marrymore)"] = [
            get_item_name(i) for i in world.room_service_items
        ]
    if world.bomb_shop_items:
        result["Swap Shop (Seaside)"] = [
            get_item_name(i) for i in world.bomb_shop_items
        ]

    return result


def _get_spell_learning_levels_json(world: GameWorld) -> dict[str, dict[str, int]]:
    """Get JSON representation of which spells are learned at which levels for each character."""
    result: dict[str, dict[str, int]] = {}

    for ally in world.allies._allies:
        character_name = ally.name
        spells_by_level: dict[str, int] = {}

        # Check starting spells (learned at level 1)
        for spell_type in ally.starting_magic:
            spell_name = spell_type.__name__
            spells_by_level[spell_name] = 1

        # Check level-up spells
        for level_up in ally.levels:
            if level_up.spell_learned:
                spell_name = level_up.spell_learned.__name__
                spells_by_level[spell_name] = level_up.level

        if spells_by_level:
            result[character_name] = spells_by_level

    return result


def _get_settings_json(world: GameWorld) -> dict[str, Any]:
    """Get JSON representation of all settings with their names and values."""

    def get_option_display_name(opt: Any) -> str:
        """Get a human-readable display name for an option."""
        if hasattr(opt, "value"):
            val = opt.value
            # Check if val is a string (e.g., "Random_1", "Random_2")
            if isinstance(val, str):
                return val
            # Check if val is a class type (for ClassCategorizationOption)
            if isinstance(val, type):
                # For class types, use _title (spell title) or __name__ (class name)
                if hasattr(val, "_title") and val._title:
                    return val._title
                elif hasattr(val, "_name") and val._name:
                    return val._name
                else:
                    return val.__name__
            elif hasattr(val, "name") and isinstance(val.name, str):
                return val.name
            elif hasattr(val, "_name") and isinstance(val._name, str):
                return val._name
            else:
                return str(val)
        elif hasattr(opt, "name"):
            return opt.name
        else:
            return str(opt)

    result: dict[str, Any] = dict()
    for flag_class, flag in world.settings._flags.items():
        flag_name = flag.name
        if isinstance(flag, BooleanFlag):
            result[flag_name] = flag.enabled
        elif isinstance(flag, RangeFlag):
            result[flag_name] = flag.value
        elif isinstance(flag, SelectOneFlag):
            # Get the selected option's display value
            selected = flag.selected
            if hasattr(selected, "value"):
                result[flag_name] = selected.value
            else:
                result[flag_name] = str(selected)
        elif isinstance(flag, CategorizationFlagWithOrdinance):
            # Get list of selected options sorted by their order
            selected_with_order = [
                (opt, order)
                for opt, order in flag.options.items()
                if order is not None
            ]
            # Sort by order value
            selected_with_order.sort(key=lambda x: x[1])
            # Get display names in order
            result[flag_name] = [
                get_option_display_name(opt) for opt, _ in selected_with_order
            ]
        elif isinstance(flag, CategorizationFlag):
            # Get list of enabled options
            result[flag_name] = [
                get_option_display_name(opt) for opt in flag.enabled
            ]
        else:
            result[flag_name] = str(flag)
    return result


__all__ = ['_get_locations_json', '_get_spell_character_assignments_json', '_get_palettes_json', '_get_shops_json', '_get_spell_learning_levels_json', '_get_settings_json']
