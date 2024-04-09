"""Base classes for item entities"""

from copy import deepcopy
import random
import math
from typing import Dict, List, Optional, Type, TypeVar, TYPE_CHECKING


from randomizer.types.overworld_scripts.arguments.types import (
    Flag,
    PartyCharacter,
)
from randomizer.types.overworld_scripts.event_scripts.ids import (
    E0242_CHEST_6_GRANT,
    E0243_CHEST_5_GRANT,
    E0244_CHEST_4_GRANT,
    E0245_CHEST_3_GRANT,
    E0246_CHEST_2_GRANT,
    E3074_COIN_CHEST_MULTI_HIT_1,
    E3401_COIN_CHEST_MULTI_HIT_2,
    E3402_COIN_CHEST_MULTI_HIT_3,
    E3403_COIN_CHEST_MULTI_HIT_4,
    E3404_COIN_CHEST_MULTI_HIT_5,
    E3405_COIN_CHEST_MULTI_HIT_6,
)
from randomizer.types.npcs.objects.types import ItemNPC
from randomizer.types.npcs.objects import BigCoin, ItemBag, SmallCoin, TinyStar
from randomizer.types.numbers import UInt16, UInt8, ByteField, BitMapSet
from randomizer.types.patch import Patch

# target .enums specifically to prevent cyclic import
from randomizer.types.spells.enums import Status, Element, TempStatBuff

from randomizer.utils.number import mutate_normal

from .enums import (
    EffectType,
    EquipStats,
    ItemShuffleType,
    ItemTypeValue,
    ItemUnique,
)
from .constants import (
    EQUIP_STATS,
    ITEMS_BASE_ADDRESS,
    ITEMS_BASE_DESC_DATA_ADDRESSES,
    ITEMS_BASE_DESC_POINTER_ADDRESS,
    ITEMS_BASE_PRICE_ADDRESS,
    ITEMS_DESC_DATA_POINTER_OFFSET,
    NUM_ITEMS,
)

if TYPE_CHECKING:
    from randomizer.types.world import GameWorld


class IllegalItemPropertyException(Exception):
    """Exception that has to do with illegal item property operations"""


class Item:
    """Parent class representing an item."""

    _item_id: int = 0
    _type_value: ItemTypeValue = ItemTypeValue.ITEM
    _item_name: str = ""
    _description: str = ""
    _tier: int = 1
    _order: int = 0
    _consumable: bool = False
    _equip_chars: List[PartyCharacter] = []
    _speed: int = 0
    _attack: int = 0
    _defense: int = 0
    _magic_attack: int = 0
    _magic_defense: int = 0
    _variance: UInt8 = UInt8(0)
    _prevent_ko: bool = False
    _elemental_immunities: List[Element] = []
    _elemental_resistances: List[Element] = []
    _status_immunities: List[Status] = []
    _temp_buffs: List[TempStatBuff] = []
    _price: int = 0
    _frog_coin_item: bool = False
    _effect_type: Optional[EffectType] = None
    _original_effect_type: EffectType = EffectType.NORMAL
    _shuffle_as_key_item: bool = False
    _is_subitem: bool = False
    _shuffle_type: ItemShuffleType = ItemShuffleType.EXTRA
    _unique = ItemUnique.NEVER
    _rank_value: int = 0
    _rank_order: int = 0
    _rank_order_reverse: int = 0
    _arbitrary_value: int = 0
    _model: Type[ItemNPC] = ItemBag
    _chest_70a7_lower: int = 0
    _chest_70a7_upper: int = 0
    _chest_event: int = 0
    _quick_chest_event: int = 0
    _npc_event: int = 0
    _overworld_event: int = 0
    _overworld_midas_event: int = 0
    _dialog_replacements: Dict[int, str] = {}
    _room_service: str = ""
    # "special equip" refers to the 10 equips that can normally be obtained
    # from turning in key items or completing monsto town sidequests
    _special_equip: bool = False

    _world: Optional["GameWorld"] = None

    @property
    def item_id(self) -> int:
        """Unique identifier for this item"""
        return self._item_id

    @property
    def type_value(self) -> ItemTypeValue:
        """Armor, accessory, weapon, or other"""
        return self._type_value

    @property
    def description(self) -> str:
        """The description as it appears in the in-game menu"""
        return self._description

    def set_description(self, description: str) -> None:
        """Update the description as it appears in the in-game menu"""
        self._description = description

    @property
    def tier(self) -> int:
        """The relative desirability of the item, 4 (high) to 1 (low)"""
        return self._tier

    def set_tier(self, tier: int) -> None:
        """Set the relative desirability of the item, 4 (high) to 1 (low)"""
        assert 1 <= tier <= 5
        self._tier = tier

    @property
    def order(self) -> int:
        """An immutable sorting property"""
        return self._order

    @property
    def consumable(self) -> bool:
        """Consumable items are single-use, like mushrooms and syrups."""
        return self._consumable

    @property
    def equip_chars(self) -> List[PartyCharacter]:
        """A list of which characters can equip this item"""
        return self._equip_chars

    def set_equip_chars(self, equip_chars: List[PartyCharacter]) -> None:
        """Overwrites the list of which characters can equip this item"""
        self._equip_chars = equip_chars

    def append_equip_char(self, char: PartyCharacter) -> None:
        """Add a character who should be able to equip this item"""
        assert char < 5
        if char not in self._equip_chars:
            self._equip_chars.append(char)

    def remove_equip_char(self, char: PartyCharacter) -> None:
        """Remove a character from the list of characters who can equip this item"""
        assert char < 5
        if char in self._equip_chars:
            self._equip_chars.remove(char)

    @property
    def speed(self) -> int:
        """Base speed increase for this item."""
        return self._speed

    @property
    def attack(self) -> int:
        """Base physical attack increase for this item."""
        return self._attack

    @property
    def defense(self) -> int:
        """Base physical defense increase for this item."""
        return self._defense

    @property
    def magic_attack(self) -> int:
        """Base magic attack increase for this item."""
        return self._magic_attack

    @property
    def magic_defense(self) -> int:
        """Base magic defense increase for this item."""
        return self._magic_defense

    @property
    def variance(self) -> UInt8:
        """The range of randomness applied to weapon output."""
        return self._variance

    @property
    def prevent_ko(self) -> bool:
        """If true, OHKO moves like Shaker and Magnum have no effect on the wearer."""
        return self._prevent_ko

    @property
    def elemental_immunities(self) -> List[Element]:
        """The wearer takes 0 damage from spells infused with these elements."""
        return deepcopy(self._elemental_immunities)

    @property
    def elemental_resistances(self) -> List[Element]:
        """The wearer takes half damage from spells infused with these elements."""
        return deepcopy(self._elemental_resistances)

    @property
    def status_immunities(self) -> List[Status]:
        """The wearer is immune to these status effects."""
        return deepcopy(self._status_immunities)

    def set_status_immunities(self, status_immunities: List[Status]) -> None:
        """Overwrites the status effect immunities for this item."""
        self._status_immunities = deepcopy(status_immunities)

    def append_status_immunity(self, immunity: Status) -> None:
        """Adds a status effect to the immunities for this item."""
        if immunity not in self._status_immunities:
            self._status_immunities.append(immunity)

    def remove_status_immunity(self, immunity: Status) -> None:
        """Removes a status effect from the immunities for this item."""
        if immunity in self._status_immunities:
            self._status_immunities.remove(immunity)

    @property
    def temp_buffs(self) -> List[TempStatBuff]:
        """Boost multiplier effects applied to the wearer at the start of battle."""
        return deepcopy(self._temp_buffs)

    @property
    def price(self) -> int:
        """Purchase cost of the item, regardless of currency type."""
        return self._price

    def set_price(self, price: int) -> None:
        """Set item cost, regardless of currency type."""
        maximum: int = 999 if self.frog_coin_item else 9999
        self._price = min(maximum, price)

    @property
    def frog_coin_item(self) -> bool:
        """If true, item should only be purchasable in frog coin shops."""
        return self._frog_coin_item

    def _set_frog_coin_item(self, frog_coin_item: bool) -> None:
        self._frog_coin_item = frog_coin_item

    @property
    def original_effect_type(self) -> EffectType:
        """Indicator for special effects like EXP booster, coin trick, etc."""
        return self._original_effect_type

    def set_effect_type(self, effect_type: Optional[EffectType] = None) -> None:
        """Indicator for special effects like EXP booster, coin trick, etc."""
        self._effect_type = effect_type

    @property
    def effect_type(self) -> EffectType:
        """Indicator for special effects like EXP booster, coin trick, etc."""
        if self._effect_type is None:
            return self.original_effect_type
        return self._effect_type

    @property
    def shuffle_as_key_item(self) -> bool:
        """Can be shuffled into a key item location in flagsets that have a concept of this."""
        return self._shuffle_as_key_item

    def set_shuffle_as_key_item(self, shuffle_as_key_item: bool) -> None:
        """If true, item should qualify for the key item pool in flagsets that use that."""
        self._shuffle_as_key_item = shuffle_as_key_item

    @property
    def is_subitem(self) -> bool:
        """Subitems are items that need to have an in-game definition,
        and belong to progressive items like ProgressiveEgg or ProgressiveCard."""
        return self._is_subitem

    def set_subitem(self, is_subitem: bool) -> None:
        """Setting this to true implies that the item belongs
        to a Progressive item (i.e. ProgressiveCard)."""
        self._is_subitem = is_subitem

    @property
    def shuffle_type(self) -> ItemShuffleType:
        """REQUIRED items absolutely must be placed into the item pool.
        EXTRA items are optional."""
        return self._shuffle_type

    def set_shuffle_type(self, shuffle_type: ItemShuffleType) -> None:
        """REQUIRED items absolutely must be placed into the item pool.
        EXTRA items are optional, and not guaranteed to be in the pool."""
        self._shuffle_type = shuffle_type

    @property
    def unique(self) -> ItemUnique:
        """If true, can only be obtained once per seed."""
        return self._unique

    @property
    def rank_value(self) -> UInt16:
        """Used when recalculating item tiers from shuffled stats."""
        return UInt16(self._rank_value)

    def set_rank_value(self, rank_value: int) -> None:
        """Used when recalculating item tiers from shuffled stats."""
        self._rank_value = UInt16(rank_value)

    @property
    def rank_order(self) -> UInt16:
        """Used when recalculating item tiers from shuffled stats."""
        return UInt16(self._rank_order)

    def set_rank_order(self, rank_order: int) -> None:
        """Used when recalculating item tiers from shuffled stats."""
        self._rank_order = UInt16(rank_order)

    @property
    def rank_order_reverse(self) -> UInt16:
        """Used when recalculating item tiers from shuffled stats."""
        return UInt16(self._rank_order_reverse)

    def set_rank_order_reverse(self, rank_order_reverse: int) -> None:
        """Used when recalculating item tiers from shuffled stats."""
        self._rank_order_reverse = UInt16(rank_order_reverse)

    @property
    def arbitrary_value(self) -> UInt16:
        """Some unique accessory effects, like double EXP, are not shuffled onto any items.
        Therefore they are not directly factored into tier calculations.
        The arbitrary value is a value that is always added to inflate this item's value
        that is used when determining the tier cutoffs."""
        return UInt16(self._arbitrary_value)

    @property
    def model(self) -> Type[ItemNPC]:
        """Graphic object that should be used to represent this item in the overworld."""
        return self._model

    @property
    def chest_70a7_lower(self) -> int:
        """The lower 4 bits to be applied to a chest that contains this item."""
        return self._chest_70a7_lower

    def _set_chest_70a7_lower(self, chest_70a7_lower: int) -> None:
        """The lower 4 bits to be applied to a chest that contains this item. Must be 0 to 15"""
        assert 0 <= chest_70a7_lower <= 0x0F
        self._chest_70a7_lower = chest_70a7_lower

    @property
    def chest_70a7_upper(self) -> int:
        """The upper 4 bits to be applied to a chest that contains this item."""
        return self._chest_70a7_upper

    def _set_chest_70a7_upper(self, chest_70a7_upper: int) -> None:
        """The upper 4 bits to be applied to a chest that contains this item. Must be 0 to 15"""
        assert 0 <= chest_70a7_upper <= 0x0F
        self._chest_70a7_upper = chest_70a7_upper

    @property
    def chest_event(self) -> int:
        """The event ID that a chest containing this item should run when hit"""
        return self._chest_event

    @property
    def quick_chest_event(self) -> int:
        """The event ID that a chest containing this item should run when hit, if this item
        has a "quick" version (such as coins being granted in one hit instead of multiple).
        For most items, this will be the same as chest_event."""
        return self._quick_chest_event

    @property
    def npc_event(self) -> int:
        """The event ID that a NPC granting this item should run at the point of granting."""
        return self._npc_event

    @property
    def overworld_event(self) -> int:
        """The event ID that a freestanding object representing this item should run when
        collected."""
        return self._overworld_event

    @property
    def overworld_midas_event(self) -> int:
        """The event ID that a freestanding object representing this item specifically in
        the Midas River caves should run when collected."""
        return self._overworld_midas_event

    @property
    def dialog_replacements(self) -> Dict[int, str]:
        """A dict of dialog IDs, and the text that should overwrite the dialogs at thsoe IDs."""
        return self._dialog_replacements

    @property
    def room_service(self) -> str:
        """How this item should be displayed if it is sold on the Marrymore room service menu."""
        return self._room_service

    @property
    def special_equip(self) -> bool:
        """How this item should be displayed if it is sold on the Marrymore room service menu."""
        return self._special_equip

    @property
    def world(self) -> "GameWorld":
        """World instance reference"""
        assert self._world is not None
        return self._world

    def __init__(self, world: Optional["GameWorld"] = None):
        self._world = world
        self._rank = None
        if len(self.equip_chars) == 0:
            self.set_equip_chars([])
        if len(self.elemental_immunities) == 0:
            self._elemental_immunities = []
        if len(self.elemental_resistances) == 0:
            self._elemental_resistances = []
        if len(self.status_immunities) == 0:
            self._status_immunities = []
        if len(self.temp_buffs) == 0:
            self._temp_buffs = []
        if len(self.dialog_replacements) == 0:
            self._dialog_replacements = {}

    @property
    def name(self) -> str:
        """Human readable item name"""
        if self._item_name != "":
            return self._item_name
        return self.__class__.__name__

    def __str__(self):
        return f"<{self.name}: price {self.price}>"

    def __repr__(self):
        return str(self)

    def become_frog_coin_item(self) -> None:
        """Makes it so that item is only purchasable in frog coin shops,
        and sets price accordingly."""
        if self.frog_coin_item:
            return

        price: int = max(math.ceil(self.rank_value / 5), 1)

        self.set_price(price)
        self._set_frog_coin_item(True)

    def unbecome_frog_coin_item(self) -> None:
        """Makes it so that item is only purchasable in regular coin shops,
        and sets price accordingly."""
        if not self.frog_coin_item:
            return

        factor = float(random.randint(50, random.randint(50, 100)))
        price = int(round(self.price * factor))

        self.set_price(min(price, 9999))
        self._set_frog_coin_item(False)

    def get_similar(self, candidates: "List[Item]") -> "Item":
        """Get a random similar item from a list of potential candidates for this one."""
        # If this is a special item, don't replace it.
        if self.rank_value <= 0:
            return self
        if self not in candidates:
            return self

        # Sort by rank and mutate our position within the list to get a replacement item.
        cands: List[Item] = sorted(candidates, key=lambda c: c.rank_value)
        index: int = cands.index(self)
        index = mutate_normal(index, maximum=len(cands) - 1)
        return cands[index]

    def get_patch(self) -> Patch:
        """Get patch for this item."""
        patch = Patch()
        if self.price == 0:
            return patch
        base_addr = ITEMS_BASE_ADDRESS + (self.item_id * 18)

        # Stats and special properties.
        data = bytearray()
        data += BitMapSet(
            1, [i.stat_value for i in self.elemental_immunities]
        ).as_bytes()
        data += BitMapSet(
            1, [r.stat_value for r in self.elemental_resistances]
        ).as_bytes()
        data += BitMapSet(1, [i.stat_value for i in self.status_immunities]).as_bytes()
        data += BitMapSet(1, self.temp_buffs).as_bytes()
        data += ByteField(self.speed).as_bytes()
        data += ByteField(self.attack).as_bytes()
        data += ByteField(self.defense).as_bytes()
        data += ByteField(self.magic_attack).as_bytes()
        data += ByteField(self.magic_defense).as_bytes()
        data += ByteField(self.variance).as_bytes()
        patch.add_data(base_addr + 5, data)

        # Price
        price_addr = ITEMS_BASE_PRICE_ADDRESS + (self.item_id * 2)
        patch.add_data(price_addr, ByteField(self.price, num_bytes=2).as_bytes())

        return patch

    @classmethod
    def build_descriptions_patch(cls, world: "GameWorld") -> Patch:
        """Build patch data for item descriptions.
        These use pointers, so we need to do them all together."""
        patch = Patch()

        # Begin text data with a single null byte to use for all empty descriptions to save space.
        pointer_data = bytearray()
        text_data: List[bytearray] = []
        for _ in range(len(ITEMS_BASE_DESC_DATA_ADDRESSES)):
            text_data.append(bytearray())
        text_data[0].append(0x00)

        # Track current base address for the text.  We have multiple banks to split the text across.
        current_bank = 0

        # Make list of blank descriptions for all items, and get description
        # for each valid item we have based on index.
        descriptions = [""] * NUM_ITEMS
        for item in world.items:
            # If this isn't an equipment, use the vanilla description, if any.
            if isinstance(item, (Equipment, RegularItem)) and item.price != 0:
                desc = item.description
            else:
                continue
            descriptions[item.item_id] = desc

        # Now build the actual pointer data.
        for desc in descriptions:
            # If the description is empty, just use the null byte at the very beginning.
            if not desc:
                pointer = (
                    ITEMS_BASE_DESC_DATA_ADDRESSES[0][0]
                    - ITEMS_DESC_DATA_POINTER_OFFSET
                )
                pointer_data += ByteField(pointer, num_bytes=2).as_bytes()
                continue

            # Compute pointer from base address and current data length.
            # If we exceed the ending address of the current
            # data bank, move to the next one.
            # If we run out, it's an error.
            while True:
                pointer = ITEMS_BASE_DESC_DATA_ADDRESSES[current_bank][0] + len(
                    text_data[current_bank]
                )
                if (pointer + len(desc) + 1) > ITEMS_BASE_DESC_DATA_ADDRESSES[
                    current_bank
                ][1]:
                    current_bank += 1
                    if current_bank >= len(ITEMS_BASE_DESC_DATA_ADDRESSES):
                        raise ValueError("Text descriptions too long")
                    continue

                # Subtract base pointer offset from computed final address.
                pointer -= ITEMS_DESC_DATA_POINTER_OFFSET
                pointer_data += ByteField(pointer, num_bytes=2).as_bytes()
                break

            # Add null byte to terminate the text string.
            desc = desc.encode("latin1")
            desc += bytes([0x00])
            text_data[current_bank] += desc

        # Sanity check that pointer data has the correct number of items.
        if len(pointer_data) != NUM_ITEMS * 2:
            raise ValueError("Wrong length for pointer data, something went wrong...")

        # Sanity check that text data doesn't exceed size of each bank.
        for address, bank in enumerate(ITEMS_BASE_DESC_DATA_ADDRESSES):
            data_len = len(text_data[address])
            bank_len = bank[1] - bank[0] + 1
            if data_len > bank_len:
                raise ValueError(
                    f"Item description data bank {address} too long: {data_len} > max {bank_len}"
                )

        # Add item description data to the patch data.
        patch.add_data(ITEMS_BASE_DESC_POINTER_ADDRESS, pointer_data)
        for index, bank in enumerate(ITEMS_BASE_DESC_DATA_ADDRESSES):
            patch.add_data(bank[0], text_data[index])

        return patch


ItemT = TypeVar("ItemT", bound=Item)


class Equipment(Item):
    """Base class for weapons, armor, and accessories."""

    def _build_equipment_description(self) -> None:
        """Generate shop/menu description text for the equip based on shuffled stats."""

        desc: str = ""

        # Elemental immunities and resistances.
        if self.elemental_immunities:
            desc += "\x96\x98"
            desc += "".join([e.stat_char for e in self.elemental_immunities])
        else:
            desc += "\x99" * 4
        desc += "\x99"

        if self.elemental_resistances:
            desc += "\x97\x98"
            desc += "".join([e.stat_char for e in self.elemental_resistances])
        else:
            desc += "\x99" * 4
        desc += "\x01"

        # Speed
        desc += ["\x93", "\x94"][self.speed < 0]
        desc += str(abs(self.speed)).ljust(3, "\x99") + "\x99"

        # Status immunities
        desc += "".join([e.stat_char for e in self.status_immunities])
        if self.prevent_ko:
            desc += "\x89"
        desc += "\x01"

        # Physical attack/defense
        desc += ["\x8B", "\x8C"][self.attack < 0]
        desc += ["\x20", "\x95"][TempStatBuff.ATTACK in self.temp_buffs]
        desc += str(abs(self.attack)).ljust(3, "\x99")
        desc += "\x99"
        desc += ["\x8F", "\x90"][self.defense < 0]
        desc += ["\x20", "\x95"][TempStatBuff.DEFENSE in self.temp_buffs]
        desc += str(abs(self.defense)).ljust(3, "\x99")
        desc += "\x01"

        # Magic attack/defense
        desc += ["\x8D", "\x8E"][self.magic_attack < 0]
        desc += ["\x20", "\x95"][TempStatBuff.MAGIC_ATTACK in self.temp_buffs]
        desc += str(abs(self.magic_attack)).ljust(3, "\x99")
        desc += "\x99"
        desc += ["\x91", "\x92"][self.magic_defense < 0]
        desc += ["\x20", "\x95"][TempStatBuff.MAGIC_DEFENSE in self.temp_buffs]
        desc += str(abs(self.magic_defense)).ljust(3, "\x99")

        self.set_description(desc)

    def set_speed(self, speed: int) -> None:
        """Modify the base speed increase for this equip."""
        assert -128 <= speed <= 127
        self._speed = speed
        self._build_equipment_description()

    def set_attack(self, attack: int) -> None:
        """Modify the base attack increase for this equip."""
        assert -128 <= attack <= 127
        self._attack = attack
        self._build_equipment_description()

    def set_defense(self, defense: int) -> None:
        """Modify the base defense increase for this equip."""
        assert -128 <= defense <= 127
        self._defense = defense
        self._build_equipment_description()

    def set_magic_attack(self, magic_attack: int) -> None:
        """Modify the base magic attack increase for this equip."""
        assert -128 <= magic_attack <= 127
        self._magic_attack = magic_attack
        self._build_equipment_description()

    def set_magic_defense(self, magic_defense: int) -> None:
        """Modify the base magic defense increase for this equip."""
        assert -128 <= magic_defense <= 127
        self._magic_defense = magic_defense
        self._build_equipment_description()

    def set_prevent_ko(self, prevent_ko: bool) -> None:
        """Modify the OHKO protection flag for this equip."""
        self._prevent_ko = prevent_ko
        self._build_equipment_description()

    def set_elemental_immunities(self, elemental_immunities: List[Element]) -> None:
        """Overwrite the elemental immunities for this equip."""
        self._elemental_immunities = deepcopy(elemental_immunities)
        self._build_equipment_description()

    def append_elemental_immunity(self, element: Element) -> None:
        """Add an elemental immunity to this equip."""
        if element not in self._elemental_immunities:
            self._elemental_immunities.append(element)
            self._build_equipment_description()

    def remove_elemental_immunity(self, element: Element) -> None:
        """Remove an elemental immunity from this equip."""
        if element in self._elemental_immunities:
            self._elemental_immunities.remove(element)
            self._build_equipment_description()

    def set_elemental_resistances(self, elemental_resistances: List[Element]) -> None:
        """Overwrite the elemental resistances for this equip."""
        self._elemental_resistances = deepcopy(elemental_resistances)
        self._build_equipment_description()

    def append_elemental_resistance(self, element: Element) -> None:
        """Add an elemental resistance to this equip."""
        if element not in self._elemental_resistances:
            self._elemental_resistances.append(element)
            self._build_equipment_description()

    def remove_elemental_resistance(self, element: Element) -> None:
        """Remove an elemental resistance from this equip."""
        if element in self._elemental_resistances:
            self._elemental_resistances.remove(element)
            self._build_equipment_description()

    def set_temp_buffs(self, temp_buffs: List[TempStatBuff]) -> None:
        """Overwrite the buff multipliers for this equip."""
        self._temp_buffs = deepcopy(temp_buffs)
        self._build_equipment_description()

    def append_temp_buff(self, buff: TempStatBuff) -> None:
        """Add a buff multiplier to this equip."""
        if buff not in self._temp_buffs:
            self._temp_buffs.append(buff)
            self._build_equipment_description()

    def remove_temp_buff(self, buff: TempStatBuff) -> None:
        """Remove a buff multiplier from this equip."""
        if buff in self._temp_buffs:
            self._temp_buffs.remove(buff)
            self._build_equipment_description()

    def set_shuffle_as_key_item(self, shuffle_as_key_item: bool) -> None:
        """Equips should never do this."""
        raise IllegalItemPropertyException("equipment cannot be a key item")

    @property
    def primary_stats(self) -> List[EquipStats]:
        """Primary stats of this item, depending on the type."""
        return EQUIP_STATS

    @property
    def stat_point_value(self) -> int:
        """Overall stat point score for rough item power during shuffle."""
        score = 0
        for attr in EQUIP_STATS:
            value = getattr(self, attr)
            # Subtract any negative value from overall score.
            if value < 0:
                score += value
            # For primary stat, add the raw value.
            elif attr in self.primary_stats:
                score += value
            # If item has positive stat outside of primary stats,
            # consider that double points for the score.
            else:
                score += 2 * value
        return score

    def get_patch(self) -> Patch:
        """Get patch for this item."""
        patch = Patch()
        base_addr = ITEMS_BASE_ADDRESS + (self.item_id * 18)

        data = bytearray()

        # Only include initial item type and inflict/protect flags for equipment.

        # Item type and instant KO protection.
        val = self.type_value
        if self.prevent_ko:
            val |= 1 << 7
        data += ByteField(val).as_bytes()

        # Inflict/protect flags for status ailments/buffs.
        val = 0
        if self.status_immunities:
            val += 1 << 0
        if self.temp_buffs:
            val += 1 << 1
        data += ByteField(val).as_bytes()

        # Which characters can equip
        data += BitMapSet(1, self.equip_chars).as_bytes()

        patch.add_data(base_addr, data)

        patch += super().get_patch()

        return patch

    def __init__(self, world: Optional["GameWorld"] = None):
        super().__init__(world)
        self._set_chest_70a7_lower(self.item_id)


class Weapon(Equipment):
    """Base class for all weapons.
    Also provides the weapon ID for unarmed attack animations."""

    _item_id: int = 0
    _type_value: ItemTypeValue = ItemTypeValue.WEAPON

    def set_variance(self, variance: int) -> None:
        """Sets the variance range on this weapon's damage RNG."""
        self._variance = UInt8(variance)

    @property
    def primary_stats(self) -> List[EquipStats]:
        """Primary stats of this item, depending on the type."""
        if self.attack >= self.magic_attack:
            return [EquipStats.ATTACK]
        return [EquipStats.MAGIC_ATTACK]


class Armor(Equipment):
    """Base class for all armor."""

    _item_id: int = 1
    _type_value: ItemTypeValue = ItemTypeValue.ARMOR

    @property
    def primary_stats(self) -> List[EquipStats]:
        """Primary stats of this item, depending on the type."""
        return [EquipStats.DEFENSE, EquipStats.MAGIC_DEFENSE]


class Accessory(Equipment):
    """Base class for all accessories."""

    _item_id: int = 2
    _type_value: ItemTypeValue = ItemTypeValue.ACCESSORY

    @property
    def primary_stats(self) -> List[EquipStats]:
        """Primary stats of this item, depending on the type."""
        # include Rare Scarf
        if self.item_id == 82:
            return [EquipStats.DEFENSE, EquipStats.MAGIC_DEFENSE]
        # Speed items are the Zoom Shoes and Feather
        if self.item_id in [74, 91]:
            return [EquipStats.SPEED]
        return super().primary_stats


class SpecialEquip(Equipment):
    """Base class for the ten special equips (granted in the original game
    either by key items or by Monstro Town sidequests)."""


class RegularEquip(Equipment):
    """Base class for all equips excluding special equips."""


class RegularItem(Item):
    """Base class for most obtainable, non-equippable, non-key items."""

    _chest_event = 3089
    _npc_event = 160
    _overworld_event = 165
    _overworld_midas_event = 2820

    def __init__(self, world: Optional["GameWorld"] = None):
        super().__init__(world)
        self._set_chest_70a7_lower(self.item_id)


class KeyItem(Item):
    """Base class for items that go in the Special pocket."""

    _chest_event = 3089
    _npc_event = 160
    _overworld_event = 165
    _overworld_midas_event = 2820

    def __init__(self, world: Optional["GameWorld"] = None):
        super().__init__(world)
        self._set_chest_70a7_lower(self.item_id)


class MiscReward(Item):
    """Base class for grants which don't represent collectible items,
    such as FP flowers, recovery mushrooms, slot machines, etc."""


class ProgressiveItem(MiscReward):
    """Base class for grants that control progressive item granting,
    such as progressive Mystery Egg or Alto/Tenor/Soprano cards."""


class MimicFightChestAssignment(MiscReward):
    """Grant class that launches fight inside a treasure chest."""


class BossFight(MiscReward):
    """Base class representing a boss fight, in order to treat it as
    an entity subject to shuffler logic."""


class SpellLearn(MiscReward):
    """Base class representing an ally's learned spell, in order to treat
    it as an entity subject to shuffler logic."""

    _damaging: bool = True
    _item_id: int = 192


class Coins(MiscReward):
    """Base class for coin rewards, excluding frog coins."""

    _tier: int = 1
    _amount: int = 0
    _multiplier: int = 0
    _chest_event: int = 3074
    _quick_chest_event: int = 3080
    _npc_event: int = 159

    @property
    def amount(self) -> UInt16:
        """The amount of coins included in this grant."""
        assert self.amount <= 9999
        return UInt16(self._amount)

    def _set_amount(self, amount: int) -> None:
        """Set the amount of coins included in this grant."""
        self._amount = UInt16(amount)

    @property
    def multiplier(self) -> UInt8:
        """Used in the calculation logic that determines the number of times
        you can hit a chest to fully deplete it at this grant's coin amount."""
        return UInt8(self._multiplier)

    def _set_multiplier(self, multiplier: int) -> None:
        """Set a multiplier that factors into chest calculation depletion."""
        self._multiplier = UInt8(multiplier)

    # coins and multi frog coins need 6 different events
    # because they run on per-chest counters (0x70DA-0x70DD and 0x70F8-0x70F9)
    def get_chest_event(self, parent) -> int:
        """Returns the specific coin chest event to run, depending on the
        central granter event used for this chest. This is necessary because
        multiple chests in the same room need to use a different bit to
        control whether or not they can be considered depleted, and up to
        six chests can be present in one room."""
        if parent == E0246_CHEST_2_GRANT:
            return E3401_COIN_CHEST_MULTI_HIT_2
        if parent == E0245_CHEST_3_GRANT:
            return E3402_COIN_CHEST_MULTI_HIT_3
        if parent == E0244_CHEST_4_GRANT:
            return E3403_COIN_CHEST_MULTI_HIT_4
        if parent == E0243_CHEST_5_GRANT:
            return E3404_COIN_CHEST_MULTI_HIT_5
        if parent == E0242_CHEST_6_GRANT:
            return E3405_COIN_CHEST_MULTI_HIT_6
        return E3074_COIN_CHEST_MULTI_HIT_1

    @property
    def chest_event(self):
        raise IllegalItemPropertyException("use get_chest_event for coins")

    def __init__(self, amount=0, world: Optional["GameWorld"] = None):
        super().__init__(world)
        if amount < 10:
            self._model: Type[ItemNPC] = SmallCoin
            self._set_chest_70a7_upper(8)
            self._set_chest_70a7_lower(amount)
        else:
            self._model: Type[ItemNPC] = BigCoin
            self._set_chest_70a7_upper(10)
            hits: int = amount // 10
            loops: int = hits // 16
            leftover: int = hits - 15 * loops
            self._set_multiplier(loops)
            self._set_chest_70a7_lower(leftover)
        self._set_amount(amount)


class StarPiece(MiscReward):
    """Base class for star piece grants."""

    _hint_bit: Flag
    _item_id: int = 230
    _tier: int = 4
    _unique: ItemUnique = ItemUnique.ALWAYS
    _chest_event: int = 163
    _npc_event: int = 164
    _overworld_event: int = 166
    _overworld_midas_event: int = 2821
    _model: Type[ItemNPC] = TinyStar
    _dialog_replacements = {
        2911: (
            """ Item #1: A “Shooting Star”!\n"""
            """ It's sure to make all your wishes\n"""
            """ come true.[await]\n"""
            """ I'll sell it to you for 100 coins.\n"""
            """  [select] (It's a deal)\n"""
            """  [select] (I'll pass)[await]"""
        ),
        2908: (
            """ Item #2: A “Shooting Star”.\n"""
            """ It's sure to make all your wishes\n"""
            """ come true.[await]\n"""
            """ It's yours for 200 coins.\n"""
            """  [select] (Okay)\n"""
            """  [select] (No thanks)[await]"""
        ),
        2914: (
            """ Item #3: A “Shooting Star”.\n"""
            """ It's sure to make all your wishes\n"""
            """ come true.[await]\n"""
            """ I'll sell it for 300 coins.\n"""
            """  [select] (I'll take it)\n"""
            """  [select] (No thanks)[await]"""
        ),
    }


class InvincibilityStar(MiscReward):
    """Base class for invincibility stars."""

    _tier: int = 0
    _chest_70a7_upper: int = 1
    _chest_event: int = 3072


class SpottedCharacter(Item):
    """Base class representing the event of discovering a character's
    location for the first time, regardless of whether that event
    also includes recruiting them. This is used for unlocking
    Forest Maze once you have seen Geno, even if you do not
    receuit Geno (i.e. he's being carried up Booster Hill)."""

    _starter_script = None
    _container_script = None


class RecruitedCharacter(Item):
    """Base class representing a character as understood by the item shuffler."""

    _starter_script: int = -1
    _container_script: int = -1
    _model: Type[ItemNPC]
    _sprites_primary: Dict[str, tuple[int, int, bool]] = {}
    _sprites_secondary: Dict[str, tuple[int, int, bool]] = {}
    _doll: Type[ItemNPC]
    _placeholder: str = "`NAME`"
    _gender: str = "man"
    _gender_casual: str = "guy"
    _honorific: str = "sir"
    _title: str = "mister"
    _title_short: str = "Mr"
    _mole_greeting: str = "mate"
    _mboy_greeting: str = ", man"

    _associated_spotted_class: Type[SpottedCharacter]

    @property
    def starter_script(self) -> int:
        """Get the script ID that initiates this character as your first character."""
        return self._starter_script

    @property
    def container_script(self) -> int:
        """Get the script ID that performs recruiting this character."""
        return self._container_script

    @property
    def model(self) -> Type[ItemNPC]:
        """Graphic object that should be used to represent this character in the overworld."""
        return self._model

    @property
    def sprites_primary(self) -> Dict[str, tuple[int, int, bool]]:
        """[Deprecated]"""
        return self._sprites_primary

    @property
    def sprites_secondary(self) -> Dict[str, tuple[int, int, bool]]:
        """[Deprecated]"""
        return self._sprites_secondary

    @property
    def doll(self) -> Type[ItemNPC]:
        """Graphic object that should be used to represent this character's
        corresponding doll in the overworld."""
        return self._doll

    @property
    def placeholder(self) -> str:
        """Replaces `MAIN_CHARACTER_NAME` in dialogs, if this character is your starter.
        This will then be replaced by the character's name, if default, or if changed
        by the palette shuffler."""
        return self._placeholder

    @property
    def gender(self) -> str:
        """Replaces `MAIN_CHARACTER_GENDER` in dialogs, if this character is your starter."""
        return self._gender

    @property
    def gender_casual(self) -> str:
        """Replaces `MAIN_CHARACTER_GENDER_CASUAL_CAP` in dialogs,
        if this character is your starter."""
        return self._gender_casual

    @property
    def honorific(self) -> str:
        """Replaces `MAIN_CHARACTER_HONORIFIC` in dialogs, if this character is your starter."""
        return self._honorific

    @property
    def title(self) -> str:
        """Replaces `MAIN_CHARACTER_TITLE` in dialogs, if this character is your starter."""
        return self._title

    @property
    def title_short(self) -> str:
        """Replaces `MAIN_CHARACTER_TITLE_SHORT` in dialogs, if this character is your starter."""
        return self._title_short

    @property
    def mole_greeting(self) -> str:
        """Replaces `MAIN_CHARACTER_MOLE_GREETING` in dialogs, if this character is your starter.
        This changes how the moles in Moleville greet you."""
        return self._mole_greeting

    @property
    def mboy_greeting(self) -> str:
        """Replaces `MAIN_CHARACTER_MBOY_GREETING` in dialogs, if this character is your starter.
        This changes how Mushroom Boy greets you."""
        return self._mboy_greeting

    @property
    def associated_spotted_class(self) -> Type[SpottedCharacter]:
        """The SpottedCharacter class definition that represents this character."""
        return self._associated_spotted_class


class MarrymoreGear(MiscReward):
    """Base class for collectible wedding chapel gear."""
