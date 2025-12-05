"""Base classes for shops."""

from typing import Optional, List, Type, Generic, TYPE_CHECKING

from randomizer.types.items import (
    Accessory,
    Armor,
    Item,
    ItemT,
    RegularItem,
    Weapon,
)
from randomizer.types.numbers import UInt16, UInt8, ByteField
from randomizer.types.patch import Patch

from .constants import BASE_SHOP_ADDRESS


if TYPE_CHECKING:
    from randomizer.types.world import GameWorld


class Shop(Generic[ItemT]):
    """Base class representing any shop."""

    _original_items: List[Type[Item]] = []
    _items: List[ItemT] = []
    _retain_size: bool = False
    _container_event: Optional[int] = 0
    _world: Optional["GameWorld"] = None
    _minimum_size: int = 0

    @property
    def original_items(self) -> List[Type[Item]]:
        """The list of item classes that were in this shop before shuffling."""
        return self.original_items

    @property
    def items(self) -> List[ItemT]:
        """The current contents of the shop."""
        return self._items

    def set_items(self, items: List[ItemT]) -> None:
        """Overwrite the current contents of the shop."""
        assert len(items) <= 15
        self._items = items

    def append_item(self, item: ItemT) -> None:
        """Add an item to the shop."""
        assert len(self._items) <= 14
        self._items.append(item)

    @property
    def retain_size(self) -> bool:
        """If true, this shop needs to have the same items after randomization
        as it did before randomization."""
        return self._retain_size

    @property
    def container_event(self) -> Optional[UInt16]:
        """The ID of the event script that launches this shop."""
        if self._container_event is None:
            return None
        return UInt16(self._container_event)

    @property
    def world(self) -> "GameWorld":
        """The game world instance for this seed."""
        assert self._world is not None
        return self._world

    @property
    def minimum_size(self) -> int:
        """The minimum number of items this shop should contain."""
        return self._minimum_size

    @property
    def name(self):
        """A name used to identify this shop within this codebase."""
        return self.__class__.__name__

    def __str__(self):
        return f"<{self.name}: items {self.items}>"

    def can_accept(self, item: Item):
        """Gatekeeps if an item is allowed to be in this shop or not."""
        if self.retain_size and len(self.items) >= len(self.original_items):
            return False
        if len(self.items) >= 15:
            return False
        if (
            isinstance(item, RegularItem)
            and len([i for i in self.original_items if i.consumable]) == 0
        ):
            return False
        if (
            isinstance(item, Armor)
            and len([i for i in self.original_items if issubclass(i, Armor)]) == 0
        ):
            return False
        if (
            isinstance(item, Weapon)
            and len([i for i in self.original_items if issubclass(i, Weapon)]) == 0
        ):
            return False
        if (
            isinstance(item, Accessory)
            and len([i for i in self.original_items if issubclass(i, Accessory)]) == 0
        ):
            return False
        if not (isinstance(item, (Armor, Weapon, Accessory)) or item.consumable):
            return False
        return True

    def __init__(self, world: "GameWorld") -> None:
        self._world = world


class NormalShop(Shop):
    """Base class representing a shop that opens into its own window."""

    _shop_id: int = 0
    _is_frog_coin_shop: bool = False

    @property
    def shop_id(self) -> UInt8:
        """The ID of this shop as known to SMRPG internally."""
        return UInt8(self._shop_id)

    @property
    def is_frog_coin_shop(self) -> bool:
        """If true, items in this shop must be purchased with Frog Coins."""
        return self._is_frog_coin_shop

    def get_patch(self) -> Patch:
        """Returns this shop as a patch that can be applied to a ROM."""
        patch = Patch()
        base_addr = BASE_SHOP_ADDRESS + (self.shop_id * 16)

        data = bytearray()
        for item in self.items:
            data += ByteField(item.item_id).as_bytes()

        # Fill out extra shop fields with no item value.
        while len(data) < 15:
            data += ByteField(255).as_bytes()

        # First byte is shop flags, don't change those.  Put items one byte later.
        patch.add_data(base_addr + 1, data)

        return patch


class NonFrogCoinShop(NormalShop):
    """Base class for shops not requiring frog coins."""

    def can_accept(self, item: Item):
        return super().can_accept(item) and not item.frog_coin_item


class FrogCoinShop(NormalShop, Generic[ItemT]):
    """Base class for shops requiring frog coins."""

    _is_frog_coin_shop: bool = True

    def append_item(self, item: ItemT) -> None:
        """Add an item to the shop."""
        assert len(self._items) <= 14
        item.become_frog_coin_item()
        self._items.append(item)

    def set_items(self, items: List[ItemT]) -> None:
        """Overwrite the current contents of the shop."""
        assert len(items) <= 15
        super().set_items([])
        for item in items:
            self.append_item(item)

    def can_accept(self, item: Item):
        # Don't allow an item in a frog coin shop that's already been
        # placed in another non frog coin shop.
        other_shops = [s for s in self.world.shops if isinstance(s, NonFrogCoinShop)]
        for shop in other_shops:
            for item_class in shop.items:
                if isinstance(item, item_class):
                    return False
        return super().can_accept(item)


class PartialJuiceBarShop(NormalShop):
    """Base class for the first three iterations of the Juice Bar,
    which should each contain a progressively larger partial list
    of the `FullJuiceBarShop`."""


class FullJuiceBarShop(NormalShop):
    """The Juice Bar as it would appear to someone who has collected
    the Soprano Card."""

    _minimum_size: int = 4


class EventShop(Shop):
    """Base class for a shop that operates entirely as an event script,
    such as the Marrymore suite room service menu."""

    _retain_size: bool = True
