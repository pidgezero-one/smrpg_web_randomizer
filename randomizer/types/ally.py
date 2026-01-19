from smrpgpatchbuilder.datatypes.allies.ally import Ally as AllyBase, LevelUp, AllyCoordinate
from .room import ExtraSpriteActions


class Ally(AllyBase):
    """Extended Ally class with _sprites_primary support."""

    def __init__(
        self,
        *args,
        _sprites_primary: dict[ExtraSpriteActions, tuple[int, int, bool]] | None = None,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self._sprites_primary = _sprites_primary or {}