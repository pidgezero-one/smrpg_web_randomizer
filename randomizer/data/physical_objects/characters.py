from ...types.physical_objects import NPC
from ..rooms.npcs import (
    MARIO_CLONE_WALKING_DOWN_LEFT_NPC,
    MALLOW_CLONE_NPC,
    GENO_CLONE_NPC,
    BOWSER_CLONE_NPC,
    TOADSTOOL_NPC,
)


class MarioCharacterNPC(NPC):
    """Mario character NPC wrapper for recruitment prizes."""

    _base = MARIO_CLONE_WALKING_DOWN_LEFT_NPC


class MallowCharacterNPC(NPC):
    """Mallow character NPC wrapper for recruitment prizes."""

    _base = MALLOW_CLONE_NPC


class GenoCharacterNPC(NPC):
    """Geno character NPC wrapper for recruitment prizes."""

    _base = GENO_CLONE_NPC


class BowserCharacterNPC(NPC):
    """Bowser character NPC wrapper for recruitment prizes."""

    _base = BOWSER_CLONE_NPC


class ToadstoolCharacterNPC(NPC):
    """Toadstool character NPC wrapper for recruitment prizes."""

    _base = TOADSTOOL_NPC
