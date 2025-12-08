from ..logic import Inventory
from ..settings import Settings
from collections.abc import Callable
from ...types.prizelocation import BossFightLocation


def can_defeat_some_of(
    inventory: Inventory,
    conditions: list[Callable[[Inventory], bool]],
    amount: int = 1,
) -> bool:
    """If true, the player is expected to be able to defeat at least some of
    the provided bosses."""
    bosses: list[bool] = [cond(inventory) for cond in conditions]
    completable: list[bool] = [cond for cond in bosses if cond]
    return len(completable) >= amount

def can_defeat_all_of(
    inventory: Inventory,
    conditions: list[Callable[[Inventory], bool]],
) -> bool:
    """If true, the player is expected to be able to defeat all of the provided
    bosses."""
    return can_defeat_some_of(inventory, conditions, len(conditions))

def can_defeat_boss(
    inventory: Inventory,
    location: BossFightLocation
) -> bool:
    if location.prize is None: # not assigned yet
        return False 
    return inventory.has_item(type(location.prize))

# TODO: can_defeat boss locations

def can_access_invaded_kingdom(
    inventory: Inventory,
    settings: Settings
) -> bool:
    #return can_defeat_boss(inventory, )
    return True

