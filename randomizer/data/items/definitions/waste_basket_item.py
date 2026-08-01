from randomizer.types.item import (RegularItem)


class WasteBasketItem(RegularItem):
    """>Waste Basket item class"""
    _item_name: str = ">Waste Basket"

    _item_id: int = 160
    _description: str = " You can throw\n away unwanted\n items"
    _price: int = 65535
    _inflict_type = None
    _usable_overworld: bool = True


__all__ = ["WasteBasketItem"]
