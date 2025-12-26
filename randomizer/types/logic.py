from .prize import Prize


class Inventory(list[Prize]):
    """A list of items, boss fights, spells, and characters the player is assumed
    to have collected."""

    def has_item_count(self, item_type: type[Prize], value=1):
        """The amount of a given item class collected."""
        count = [item for item in self if isinstance(item, item_type)]
        return len(count) >= value

    def has_item(self, item_type: type[Prize]):
        """Returns true if at least one of the given class is collected."""
        presence = next((item for item in self if isinstance(item, item_type)), None)
        return presence is not None

    def has_one_of(self, item_types: list[type[Prize]]):
        """Returns true of at least one of any of the given classes is collected."""
        found = False
        for held_item in self:
            for item_type in item_types:
                if isinstance(held_item, item_type):
                    found = True
                    break
        return found
    
    def get_items_of_type(self, item_type: type[Prize]) -> list[Prize]:
        """Returns a list of all items of the given type in the inventory."""
        return [item for item in self if isinstance(item, item_type)]
    
    def get_item(self, item_type: type[Prize]) -> Prize | None:
        """Returns the first item of the given type in the inventory, or None if not found."""
        return next((item for item in self.get_items_of_type(item_type)), None)