"""Exceptions raised while building a world.

Kept in a leaf module so pipeline code (logic/build_world.py, logic/solvability.py)
can import them without importing types/gameworld.py, which imports the pipeline
back. gameworld re-exports both names, so existing imports keep working.
"""

from __future__ import annotations


class RandomizerSettingsException(Exception):
    pass


class WorldBuildingException(Exception):
    pass


__all__ = ["RandomizerSettingsException", "WorldBuildingException"]
