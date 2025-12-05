"""Base classes for enemy attack data."""

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from randomizer.types.world import GameWorld


class EnemyAttack(TODOImportAttack):
    """Class representing an enemy attack."""

    _world: Optional["GameWorld"]

    @property
    def world(self) -> "GameWorld":
        """World instance reference"""
        assert self._world is not None
        return self._world
    
    def __init__(self, world: Optional["GameWorld"] = None) -> None:
        self._world = world