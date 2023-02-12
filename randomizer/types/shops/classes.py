from typing import Optional, Sequence, Type, cast
from randomizer.types.patch.classes import Patch
from randomizer.types.shops.constants import BASE_SHOP_ADDRESS
from randomizer.types.numbers.classes import UInt16, UInt8
from randomizer.types.items.classes import Accessory, Armor, Item, RegularItem, Weapon
from randomizer.types.world.classes import GameWorld
from randomizer.types.numbers.classes import ByteField


class Shop:
    _original_items: Sequence[Type[Item]] = []
    _items: Sequence[Item] = []
    _retain_size: bool = False
    _container_event: Optional[int] = 0
    _world: Optional[GameWorld] = None
    _minimum_size: int = 0

    @property
    def original_items(self) -> Sequence[Type[Item]]:
        return self.original_items

    @property
    def items(self) -> Sequence[Item]:
        return self._items

    def set_items(self, items: Sequence[Item]) -> None:
        self._items = items

    def append_item(self, item: Item) -> None:
        items = cast(list[Item], self._items)
        if item not in items:
            items.append(item)
        self._items = cast(Sequence[Item], items)

    @property
    def retain_size(self) -> bool:
        return self._retain_size

    @property
    def container_event(self) -> Optional[UInt16]:
        if self._container_event is None:
            return None
        return UInt16(self._container_event)

    @property
    def world(self) -> GameWorld:
        assert self._world is not None
        return self._world

    @property
    def minimum_size(self) -> int:
        return self._minimum_size

    @property
    def name(self):
        return self.__class__.__name__

    def __str__(self):
        return "<{}: items {}>".format(self.name, self.items)

    def can_accept(self, item: Item):
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
        if not (
            isinstance(item, Armor)
            or isinstance(item, Weapon)
            or isinstance(item, Accessory)
            or item.consumable
        ):
            return False
        return True

    def __init__(self, world: GameWorld) -> None:
        self._world = world


class NormalShop(Shop):
    _shop_id: int = 0
    _is_frog_coin_shop: bool = False

    @property
    def shop_id(self) -> UInt8:
        return UInt8(self._shop_id)

    @property
    def is_frog_coin_shop(self) -> bool:
        return self._is_frog_coin_shop

    def get_patch(self) -> Patch:
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


class FrogCoinShop(NormalShop):
    _is_frog_coin_shop: bool = True


class PartialJuiceBarShop(NormalShop):
    pass


class FullJuiceBarShop(NormalShop):
    _minimum_size: int = 4


class EventShop(Shop):
    _retain_size: bool = True
