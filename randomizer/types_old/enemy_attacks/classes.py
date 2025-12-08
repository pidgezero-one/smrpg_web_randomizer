"""Base classes for enemy attack data."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from randomizer.types.world import GameWorld


class EnemyAttack(TODOImportAttack):
    """Class representing an enemy attack."""

    _world: "GameWorld" | None

    @property
    def world(self) -> "GameWorld":
        """World instance reference"""
        assert self._world is not None
        return self._world
    
    def __init__(self, world: "GameWorld" | None = None) -> None:
        self._world = world