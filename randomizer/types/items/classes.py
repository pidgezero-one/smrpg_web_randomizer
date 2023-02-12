from copy import deepcopy
import random
import math
from randomizer.types.items.enums import (
    EffectType,
    EquipElement,
    EquipStats,
    ItemShuffleType,
    ItemStatusEffect,
    ItemTempBuff,
    ItemTypeValue,
    ItemUnique,
)
from randomizer.types.items.constants import (
    EQUIP_STATS,
    ITEMS_BASE_ADDRESS,
    ITEMS_BASE_DESC_DATA_ADDRESSES,
    ITEMS_BASE_DESC_POINTER_ADDRESS,
    ITEMS_BASE_PRICE_ADDRESS,
    ITEMS_DESC_DATA_POINTER_OFFSET,
    NUM_ITEMS,
)

from randomizer.types.overworld_scripts.variables.classes import Flag

from randomizer.logic import utils
from randomizer.types.patch.classes import Patch
from randomizer.data import npcs

from randomizer.types.overworld_scripts.constants.area_objects import PartyCharacter
from randomizer.types.numbers.classes import UInt16, UInt8

from typing import Dict, List, Optional, Type, TypeVar

from randomizer.types.world.classes import GameWorld


class Item:
    """Parent class representing an item."""

    _item_id: int = 0
    _type_value: ItemTypeValue = ItemTypeValue.Item
    _item_name: str = ""
    _description: str = ""
    _tier: int = 5
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
    _elemental_immunities: List[EquipElement] = []
    _elemental_resistances: List[EquipElement] = []
    _status_immunities: List[ItemStatusEffect] = []
    _temp_buffs: List[ItemTempBuff] = []
    _price: int = 0
    _frog_coin_item: bool = False
    _original_effect_type: EffectType = EffectType.Normal
    _shuffle_as_key_item: bool = False
    _is_subitem: bool = False
    _shuffle_type: ItemShuffleType = ItemShuffleType.Extra
    _unique = ItemUnique.Never
    _rank_value: int = 0
    _rank_order: int = 0
    _rank_order_reverse: int = 0
    _arbitrary_value: int = 0
    _model: Type[npcs.ItemNPC] = npcs.ItemBag
    _chest_70A7_lower: int = 0
    _chest_70A7_upper: int = 0
    _packet: int = 0
    _chest_event: int = 0
    _quick_chest_event: int = 0
    _npc_event: int = 0
    _overworld_event: int = 0
    _overworld_midas_event: int = 0
    _dialog_replacements: Dict[int, str] = {}
    _room_service: str = ""
    # "special equip" refers to the 10 equips that can normally be obtained from turning in key items or completing monsto town sidequests
    _special_equip: bool = False
    # Flag to override whether we include the item stats in the patch data.  By default, we only include equipment but
    # a small handful of consumable items have their effects shuffled as well.
    _include_stats_in_patch: bool = False

    _world: Optional[GameWorld] = None

    @property
    def item_id(self) -> int:
        return self._item_id

    @property
    def type_value(self) -> ItemTypeValue:
        return self._type_value

    @property
    def description(self) -> str:
        return self._description

    def set_description(self, description: str) -> None:
        self._description = description

    @property
    def tier(self) -> int:
        return self._tier

    def set_tier(self, tier: int) -> None:
        assert 1 <= tier <= 5
        self._tier = tier

    @property
    def order(self) -> int:
        return self._order

    @property
    def consumable(self) -> bool:
        return self._consumable

    @property
    def equip_chars(self) -> List[PartyCharacter]:
        return self._equip_chars

    def set_equip_chars(self, equip_chars: List[PartyCharacter]) -> None:
        self._equip_chars = equip_chars

    def append_equip_char(self, char: PartyCharacter) -> None:
        assert char < 5
        if char not in self._equip_chars:
            self._equip_chars.append(char)

    def remove_equip_char(self, char: PartyCharacter) -> None:
        assert char < 5
        if char in self._equip_chars:
            self._equip_chars.remove(char)

    @property
    def speed(self) -> int:
        return self._speed

    @property
    def attack(self) -> int:
        return self._attack

    @property
    def defense(self) -> int:
        return self._defense

    @property
    def magic_attack(self) -> int:
        return self._magic_attack

    @property
    def magic_defense(self) -> int:
        return self._magic_defense

    @property
    def variance(self) -> UInt8:
        return self._variance

    @property
    def prevent_ko(self) -> bool:
        return self._prevent_ko

    @property
    def elemental_immunities(self) -> List[EquipElement]:
        return deepcopy(self._elemental_immunities)

    @property
    def elemental_resistances(self) -> List[EquipElement]:
        return deepcopy(self._elemental_resistances)

    @property
    def status_immunities(self) -> List[ItemStatusEffect]:
        return deepcopy(self._status_immunities)

    def set_status_immunities(self, status_immunities: List[ItemStatusEffect]) -> None:
        self._status_immunities = deepcopy(status_immunities)

    def append_status_immunity(self, immunity: ItemStatusEffect) -> None:
        if immunity not in self._status_immunities:
            self._status_immunities.append(immunity)

    def remove_status_immunity(self, immunity: ItemStatusEffect) -> None:
        if immunity in self._status_immunities:
            self._status_immunities.remove(immunity)

    @property
    def temp_buffs(self) -> List[ItemTempBuff]:
        return deepcopy(self._temp_buffs)

    @property
    def price(self) -> int:
        return self._price

    def set_price(self, price: int) -> None:
        max: int = 999 if self.frog_coin_item else 9999
        self._price = min(max, price)

    @property
    def frog_coin_item(self) -> bool:
        return self._frog_coin_item

    def _set_frog_coin_item(self, frog_coin_item: bool) -> None:
        self._frog_coin_item = frog_coin_item

    @property
    def original_effect_type(self) -> EffectType:
        return self._original_effect_type

    @property
    def shuffle_as_key_item(self) -> bool:
        return self._shuffle_as_key_item

    def set_shuffle_as_key_item(self, shuffle_as_key_item: bool) -> None:
        self._shuffle_as_key_item = shuffle_as_key_item

    @property
    def is_subitem(self) -> bool:
        return self._is_subitem

    def set_subitem(self, is_subitem: bool) -> None:
        self._is_subitem = is_subitem

    @property
    def shuffle_type(self) -> ItemShuffleType:
        return self._shuffle_type

    def set_shuffle_type(self, shuffle_type: ItemShuffleType) -> None:
        self._shuffle_type = shuffle_type

    @property
    def unique(self) -> ItemUnique:
        return self._unique

    @property
    def rank_value(self) -> UInt16:
        return UInt16(self._rank_value)

    def set_rank_value(self, rank_value: int) -> None:
        self._rank_value = UInt16(rank_value)

    @property
    def rank_order(self) -> UInt16:
        return UInt16(self._rank_order)

    def set_rank_order(self, rank_order: int) -> None:
        self._rank_order = UInt16(rank_order)

    @property
    def rank_order_reverse(self) -> UInt16:
        return UInt16(self._rank_order_reverse)

    def set_rank_order_reverse(self, rank_order_reverse: int) -> None:
        self._rank_order_reverse = UInt16(rank_order_reverse)

    @property
    def arbitrary_value(self) -> UInt16:
        return UInt16(self._arbitrary_value)

    @property
    def model(self) -> Type[npcs.ItemNPC]:
        return self._model

    @property
    def chest_70A7_lower(self) -> int:
        return self._chest_70A7_lower

    def _set_chest_70A7_lower(self, chest_70A7_lower: int) -> None:
        assert 0 <= chest_70A7_lower <= 0x0F
        self._chest_70A7_lower = chest_70A7_lower

    @property
    def chest_70A7_upper(self) -> int:
        return self._chest_70A7_upper

    def _set_chest_70A7_upper(self, chest_70A7_upper: int) -> None:
        assert 0 <= chest_70A7_upper <= 0x0F
        self._chest_70A7_upper = chest_70A7_upper

    @property
    def packet(self) -> int:
        return self._packet

    @property
    def chest_event(self) -> int:
        return self._chest_event

    @property
    def quick_chest_event(self) -> int:
        return self._quick_chest_event

    @property
    def npc_event(self) -> int:
        return self._npc_event

    @property
    def overworld_event(self) -> int:
        return self._overworld_event

    @property
    def overworld_midas_event(self) -> int:
        return self._overworld_midas_event

    @property
    def dialog_replacements(self) -> Dict[int, str]:
        return self._dialog_replacements

    @property
    def room_service(self) -> str:
        return self._room_service

    @property
    def special_equip(self) -> bool:
        return self._special_equip

    @property
    def include_stats_in_patch(self) -> bool:
        return self._include_stats_in_patch

    @property
    def world(self) -> GameWorld:
        assert self._world is not None
        return self._world

    def __init__(self, world: Optional[GameWorld] = None):
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

    def __str__(self):
        return "<{}: price {}>".format(self.name, self.price)

    def __repr__(self):
        return str(self)

    @property
    def name(self) -> str:
        if self._item_name != "":
            return self._item_name
        return self.__class__.__name__

    def become_frog_coin_item(self) -> bool:
        if self.frog_coin_item:
            return False

        price: int = max(math.ceil(self.rank_value / 5), 1)

        self.set_price(price)
        self._set_frog_coin_item(True)
        return True

    def unbecome_frog_coin_item(self) -> bool:
        if not self.frog_coin_item:
            return False

        factor = float(random.randint(50, random.randint(50, 100)))
        price = int(round(self.price * factor))

        self.set_price(min(price, 9999))
        self._set_frog_coin_item(False)
        return True

    def get_similar(self, candidates: "List[Item]") -> "Item":
        """Get a random similar item from a list of potential candidates for this one."""
        # If this is a special item, don't replace it.
        if self.rank_value <= 0:
            return self
        elif self not in candidates:
            return self

        # Sort by rank and mutate our position within the list to get a replacement item.
        cands: List[Item] = sorted(candidates, key=lambda c: c.rank_value)
        index: int = cands.index(self)
        index = utils.mutate_normal(index, maximum=len(cands) - 1)
        return cands[index]

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
        data += utils.ByteField(val).as_bytes()

        # Inflict/protect flags for status ailments/buffs.
        val = 0
        if self.status_immunities:
            val += 1 << 0
        if self.temp_buffs:
            val += 1 << 1
        data += utils.ByteField(val).as_bytes()

        # Which characters can equip
        data += utils.BitMapSet(1, self.equip_chars).as_bytes()

        patch.add_data(base_addr, data)

        # Stats and special properties.
        data = bytearray()
        data += utils.BitMapSet(1, self.elemental_immunities).as_bytes()
        data += utils.BitMapSet(1, self.elemental_resistances).as_bytes()
        data += utils.BitMapSet(1, self.status_immunities).as_bytes()
        data += utils.BitMapSet(1, self.temp_buffs).as_bytes()
        data += utils.ByteField(self.speed).as_bytes()
        data += utils.ByteField(self.attack).as_bytes()
        data += utils.ByteField(self.defense).as_bytes()
        data += utils.ByteField(self.magic_attack).as_bytes()
        data += utils.ByteField(self.magic_defense).as_bytes()
        data += utils.ByteField(self.variance).as_bytes()
        patch.add_data(base_addr + 5, data)

        # Price
        price_addr = ITEMS_BASE_PRICE_ADDRESS + (self.item_id * 2)
        patch.add_data(price_addr, utils.ByteField(self.price, num_bytes=2).as_bytes())

        return patch

    @classmethod
    def build_descriptions_patch(cls, world) -> Patch:
        """Build patch data for item descriptions.  These use pointers, so we need to do them all together.

        :type world: randomizer.logic.main.GameWorld
        :return: Patch data.
        :rtype: randomizer.logic.patch.Patch
        """
        patch = Patch()

        # Begin text data with a single null byte to use for all empty descriptions to save space.
        pointer_data = bytearray()
        text_data = []
        for i in range(len(ITEMS_BASE_DESC_DATA_ADDRESSES)):
            text_data.append(bytearray())
        text_data[0].append(0x00)

        # Track current base address for the text.  We have multiple banks to split the text across.
        current_bank = 0

        # Make list of blank descriptions for all items, and get description for each valid item we have based on index.
        descriptions = [""] * NUM_ITEMS
        for item in world.items:
            # If this isn't an equipment, use the vanilla description, if any.
            if (
                isinstance(item, Equipment) or isinstance(item, RegularItem)
            ) and item.price != 0:
                desc = item.description
            else:
                continue
            descriptions[item.item_id] = desc

        # Now build the actual pointer data.
        for _, desc in enumerate(descriptions):
            # If the description is empty, just use the null byte at the very beginning.
            if not desc:
                pointer = (
                    ITEMS_BASE_DESC_DATA_ADDRESSES[0][0]
                    - ITEMS_DESC_DATA_POINTER_OFFSET
                )
                pointer_data += utils.ByteField(pointer, num_bytes=2).as_bytes()
                continue

            # Compute pointer from base address and current data length.  If we exceed the ending address of the current
            # data bank, move to the next one.  If we run out, it's an error.
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
                pointer_data += utils.ByteField(pointer, num_bytes=2).as_bytes()
                break

            # Add null byte to terminate the text string.
            desc = desc.encode("latin1")
            desc += bytes([0x00])
            text_data[current_bank] += desc

        # Sanity check that pointer data has the correct number of items.
        if len(pointer_data) != NUM_ITEMS * 2:
            raise ValueError("Wrong length for pointer data, something went wrong...")

        # Sanity check that text data doesn't exceed size of each bank.
        for i, bank in enumerate(ITEMS_BASE_DESC_DATA_ADDRESSES):
            data_len = len(text_data[i])
            bank_len = bank[1] - bank[0] + 1
            if data_len > bank_len:
                raise ValueError(
                    "Item description data bank {} too long: {} > max {}".format(
                        i, data_len, bank_len
                    )
                )

        # Add item description data to the patch data.
        patch.add_data(ITEMS_BASE_DESC_POINTER_ADDRESS, pointer_data)
        for i, bank in enumerate(ITEMS_BASE_DESC_DATA_ADDRESSES):
            patch.add_data(bank[0], text_data[i])

        return patch


class Equipment(Item):
    def _build_equipment_description(self) -> None:
        """Generate shop/menu description text for the item based on shuffled stats."""

        desc: str = ""

        # Elemental immunities and resistances.
        if self.elemental_immunities:
            desc += "\x96\x98"
            desc += utils.add_desc_fields(
                (
                    ("\x80\x98", EquipElement.Fire, self.elemental_immunities),
                    ("\x81", EquipElement.Ice, self.elemental_immunities),
                    ("\x82", EquipElement.Thunder, self.elemental_immunities),
                )
            )
        else:
            desc += "\x99" * 4
        desc += "\x99"

        if self.elemental_resistances:
            desc += "\x97\x98"
            desc += utils.add_desc_fields(
                (
                    ("\x80\x98", EquipElement.Fire, self.elemental_resistances),
                    ("\x81", EquipElement.Ice, self.elemental_resistances),
                    ("\x82", EquipElement.Thunder, self.elemental_resistances),
                )
            )
        else:
            desc += "\x99" * 4
        desc += "\x01"

        # Speed
        desc += ["\x93", "\x94"][self.speed < 0]
        desc += str(abs(self.speed)).ljust(3, "\x99") + "\x99"

        # Status immunities
        desc += utils.add_desc_fields(
            (
                ("\x83", ItemStatusEffect.Mute, self.status_immunities),
                ("\x84", ItemStatusEffect.Sleep, self.status_immunities),
                ("\x85", ItemStatusEffect.Poison, self.status_immunities),
                ("\x86", ItemStatusEffect.Fear, self.status_immunities),
                ("\x98\x87", ItemStatusEffect.Mushroom, self.status_immunities),
                ("\x88", ItemStatusEffect.Scarecrow, self.status_immunities),
                ("\x89", True, self.prevent_ko),
                ("\x8A", ItemStatusEffect.Berserk, self.status_immunities),
            )
        )
        desc += "\x01"

        # Physical attack/defense
        desc += ["\x8B", "\x8C"][self.attack < 0]
        desc += ["\x20", "\x95"][ItemTempBuff.Attack in self.temp_buffs]
        desc += str(abs(self.attack)).ljust(3, "\x99")
        desc += "\x99"
        desc += ["\x8F", "\x90"][self.defense < 0]
        desc += ["\x20", "\x95"][ItemTempBuff.Defense in self.temp_buffs]
        desc += str(abs(self.defense)).ljust(3, "\x99")
        desc += "\x01"

        # Magic attack/defense
        desc += ["\x8D", "\x8E"][self.magic_attack < 0]
        desc += ["\x20", "\x95"][ItemTempBuff.MagicAttack in self.temp_buffs]
        desc += str(abs(self.magic_attack)).ljust(3, "\x99")
        desc += "\x99"
        desc += ["\x91", "\x92"][self.magic_defense < 0]
        desc += ["\x20", "\x95"][ItemTempBuff.MagicDefense in self.temp_buffs]
        desc += str(abs(self.magic_defense)).ljust(3, "\x99")

        self.set_description(desc)

    def set_speed(self, speed: int) -> None:
        assert -128 <= speed <= 127
        self._speed = speed
        self._build_equipment_description()

    def set_attack(self, attack: int) -> None:
        assert -128 <= attack <= 127
        self._attack = attack
        self._build_equipment_description()

    def set_defense(self, defense: int) -> None:
        assert -128 <= defense <= 127
        self._defense = defense
        self._build_equipment_description()

    def set_magic_attack(self, magic_attack: int) -> None:
        assert -128 <= magic_attack <= 127
        self._magic_attack = magic_attack
        self._build_equipment_description()

    def set_magic_defense(self, magic_defense: int) -> None:
        assert -128 <= magic_defense <= 127
        self._magic_defense = magic_defense
        self._build_equipment_description()

    def set_prevent_ko(self, prevent_ko: bool) -> None:
        self._prevent_ko = prevent_ko
        self._build_equipment_description()

    def set_elemental_immunities(
        self, elemental_immunities: List[EquipElement]
    ) -> None:
        self._elemental_immunities = deepcopy(elemental_immunities)
        self._build_equipment_description()

    def append_elemental_immunity(self, element: EquipElement) -> None:
        if element not in self._elemental_immunities:
            self._elemental_immunities.append(element)
            self._build_equipment_description()

    def remove_elemental_immunity(self, element: EquipElement) -> None:
        if element in self._elemental_immunities:
            self._elemental_immunities.remove(element)
            self._build_equipment_description()

    def set_elemental_resistances(
        self, elemental_resistances: List[EquipElement]
    ) -> None:
        self._elemental_resistances = deepcopy(elemental_resistances)
        self._build_equipment_description()

    def append_elemental_resistance(self, element: EquipElement) -> None:
        if element not in self._elemental_resistances:
            self._elemental_resistances.append(element)
            self._build_equipment_description()

    def remove_elemental_resistance(self, element: EquipElement) -> None:
        if element in self._elemental_resistances:
            self._elemental_resistances.remove(element)
            self._build_equipment_description()

    def set_temp_buffs(self, temp_buffs: List[ItemTempBuff]) -> None:
        self._temp_buffs = deepcopy(temp_buffs)
        self._build_equipment_description()

    def append_temp_buff(self, buff: ItemTempBuff) -> None:
        if buff not in self._temp_buffs:
            self._temp_buffs.append(buff)
            self._build_equipment_description()

    def remove_temp_buff(self, buff: ItemTempBuff) -> None:
        if buff in self._temp_buffs:
            self._temp_buffs.remove(buff)
            self._build_equipment_description()

    def set_shuffle_as_key_item(self, shuffle_as_key_item: bool) -> None:
        raise Exception("equipment cannot be a key item")

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
            # If item has positive stat outside of primary stats, consider that double points for the score.
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
        data += utils.ByteField(val).as_bytes()

        # Inflict/protect flags for status ailments/buffs.
        val = 0
        if self.status_immunities:
            val += 1 << 0
        if self.temp_buffs:
            val += 1 << 1
        data += utils.ByteField(val).as_bytes()

        # Which characters can equip
        data += utils.BitMapSet(1, self.equip_chars).as_bytes()

        patch.add_data(base_addr, data)

        # Stats and special properties.
        data = bytearray()
        data += utils.BitMapSet(1, self.elemental_immunities).as_bytes()
        data += utils.BitMapSet(1, self.elemental_resistances).as_bytes()
        data += utils.BitMapSet(1, self.status_immunities).as_bytes()
        data += utils.BitMapSet(1, self.temp_buffs).as_bytes()
        data += utils.ByteField(self.speed).as_bytes()
        data += utils.ByteField(self.attack).as_bytes()
        data += utils.ByteField(self.defense).as_bytes()
        data += utils.ByteField(self.magic_attack).as_bytes()
        data += utils.ByteField(self.magic_defense).as_bytes()
        data += utils.ByteField(self.variance).as_bytes()
        patch.add_data(base_addr + 5, data)

        patch += super().get_patch

        return patch

    def __init__(self, world: Optional[GameWorld] = None):
        super().__init__(world)
        self._set_chest_70A7_lower(self.item_id)


class Weapon(Equipment):
    _item_id: int = 0
    _type_value: ItemTypeValue = ItemTypeValue.Weapon

    def set_variance(self, variance: int) -> None:
        self._variance = UInt8(variance)

    @property
    def primary_stats(self) -> List[EquipStats]:
        """Primary stats of this item, depending on the type."""
        if self.attack >= self.magic_attack:
            return [EquipStats.Attack]
        else:
            return [EquipStats.MagicAttack]


class Armor(Equipment):
    _item_id: int = 1
    _type_value: ItemTypeValue = ItemTypeValue.Armor

    @property
    def primary_stats(self) -> List[EquipStats]:
        """Primary stats of this item, depending on the type."""
        return [EquipStats.Defense, EquipStats.MagicDefense]


class Accessory(Equipment):
    _item_id: int = 2
    _type_value: ItemTypeValue = ItemTypeValue.Accessory

    @property
    def primary_stats(self) -> List[EquipStats]:
        """Primary stats of this item, depending on the type."""
        # include Rare Scarf
        if self.item_id == 82:
            return [EquipStats.Defense, EquipStats.MagicDefense]
        # Speed items are the Zoom Shoes and Feather
        elif self.item_id in [74, 91]:
            return [EquipStats.Speed]
        return super().primary_stats


class SpecialEquip(Equipment):
    pass


class RegularEquip(Equipment):
    pass


class RegularItem(Item):
    _chest_event = 3089
    _npc_event = 160
    _overworld_event = 165
    _overworld_midas_event = 2820

    def __init__(self, world: Optional[GameWorld] = None):
        super().__init__(world)
        self._set_chest_70A7_lower(self.item_id)


class KeyItem(Item):
    _chest_event = 3089
    _npc_event = 160
    _overworld_event = 165
    _overworld_midas_event = 2820

    def __init__(self, world: Optional[GameWorld] = None):
        super().__init__(world)
        self._set_chest_70A7_lower(self.item_id)


class MiscReward(Item):
    """Base class for items requiring special logic."""

    pass


class ProgressiveItem(MiscReward):
    pass


class MimicFightChestAssignment(MiscReward):

    pass


class BossFight(MiscReward):
    pass


class SpellLearn(MiscReward):
    _damaging = True

    _item_id: int = 192


class Coins(MiscReward):
    _tier: int = 1
    _amount: int = 0
    _multiplier: int = 0
    _chest_event: int = 3074
    _quick_chest_event: int = 3080
    _npc_event: int = 159

    @property
    def amount(self) -> UInt16:
        assert self.amount <= 9999
        return UInt16(self._amount)

    def _set_amount(self, amount: int) -> None:
        self._amount = UInt16(amount)

    @property
    def multiplier(self) -> UInt8:
        return UInt8(self._multiplier)

    def _set_multiplier(self, multiplier: int) -> None:
        self._multiplier = UInt8(multiplier)

    # coins and multi frog coins need 6 different events
    # because they run on per-chest counters (0x70DA-0x70DD and 0x70F8-0x70F9)
    def get_chest_event(self, parent) -> int:
        if parent == 246:
            return 3401
        elif parent == 245:
            return 3402
        elif parent == 244:
            return 3403
        elif parent == 243:
            return 3404
        elif parent == 242:
            return 3405
        else:
            return 3074

    @property
    def chest_event(self):
        raise Exception("use get_chest_event for coins")

    def __init__(self, amount=0, world: Optional[GameWorld] = None):
        super().__init__(world)
        if amount < 10:
            self._model: Type[npcs.ItemNPC] = npcs.SmallCoin
            self._set_chest_70A7_upper(8)
            self._set_chest_70A7_lower(amount)
        else:
            self._model: Type[npcs.ItemNPC] = npcs.BigCoin
            self._set_chest_70A7_upper(10)
            hits: int = amount // 10
            loops: int = hits // 16
            leftover: int = hits - 15 * loops
            self._set_multiplier(loops)
            self._set_chest_70A7_lower(leftover)
        self._set_amount(amount)


class StarPiece(MiscReward):
    _hint_bit: Flag
    _item_id: int = 230
    _tier: int = 4
    _unique: ItemUnique = ItemUnique.Always
    _chest_event: int = 163
    _npc_event: int = 164
    _overworld_event: int = 166
    _overworld_midas_event: int = 2821
    _model: Type[npcs.ItemNPC] = npcs.TinyStar
    _dialog_replacements = {
        2911: """ Item #1: A “Shooting Star”!\n It's sure to make all your wishes\n come true.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Shooting Star”.\n It's sure to make all your wishes\n come true.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Shooting Star”.\n It's sure to make all your wishes\n come true.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class InvincibilityStar(MiscReward):
    """Base class for invincibility stars."""

    _tier: int = 0
    _chest_70A7_upper: int = 1
    _chest_event: int = 3072
    pass


class SpottedCharacter(Item):
    _starter_script = None
    _container_script = None


class RecruitedCharacter(Item):

    _starter_script: int = -1
    _container_script: int = -1
    _model: Type[npcs.ItemNPC]
    _sprites_primary: Dict[str, tuple[int, int, bool]] = {}
    _sprites_secondary: Dict[str, tuple[int, int, bool]] = {}
    _doll: Type[npcs.ItemNPC]
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
        return self._starter_script

    @property
    def container_script(self) -> int:
        return self._container_script

    @property
    def model(self) -> Type[npcs.ItemNPC]:
        return self._model

    @property
    def sprites_primary(self) -> Dict[str, tuple[int, int, bool]]:
        return self._sprites_primary

    @property
    def sprites_secondary(self) -> Dict[str, tuple[int, int, bool]]:
        return self._sprites_secondary

    @property
    def doll(self) -> Type[npcs.ItemNPC]:
        return self._doll

    @property
    def placeholder(self) -> str:
        return self._placeholder

    @property
    def gender(self) -> str:
        return self._gender

    @property
    def gender_casual(self) -> str:
        return self._gender_casual

    @property
    def honorific(self) -> str:
        return self._honorific

    @property
    def title(self) -> str:
        return self._title

    @property
    def title_short(self) -> str:
        return self._title_short

    @property
    def mole_greeting(self) -> str:
        return self._mole_greeting

    @property
    def mboy_greeting(self) -> str:
        return self._mboy_greeting

    @property
    def associated_spotted_class(self) -> Type[SpottedCharacter]:
        return self._associated_spotted_class


class MarrymoreGear(MiscReward):
    pass


TItem = TypeVar("TItem", bound="Item")
