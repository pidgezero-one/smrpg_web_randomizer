"""Progress location definitions for learnable spells."""

from randomizer.entities.spells.spells import (
    BowserCrush,
    ComeBack,
    Crusher,
    FireOrb,
    GenoBeam,
    GenoBlast,
    GenoBoost,
    GenoFlash,
    GenoWhirl,
    GroupHug,
    HPRain,
    Jump,
    Mute,
    PoisonGas,
    PsychBomb,
    Psychopath,
    Shocker,
    SleepyTime,
    Snowy,
    StarRain,
    SuperFlame,
    SuperJump,
    Terrorize,
    Therapy,
    Thunderbolt,
    UltraFlame,
    UltraJump)
from randomizer.types.progress_locations import (
    ToadstoolSpellSlot,
    GenoSpellSlot,
    LaterSpellSlot,
    MallowSpellSlot,
    MarioSpellSlot,
    BowserSpellSlot)
from randomizer.types.spells import Spell


class MarioSpellSlot1(MarioSpellSlot):
    """MarioSpellSlot1 progress location class"""

    _original_item: type[Spell] = Jump


class MarioSpellSlot2(MarioSpellSlot, LaterSpellSlot):
    """MarioSpellSlot2 progress location class"""

    _original_item: type[Spell] = FireOrb


class MarioSpellSlot3(MarioSpellSlot, LaterSpellSlot):
    """MarioSpellSlot3 progress location class"""

    _original_item: type[Spell] = SuperJump


class MarioSpellSlot4(MarioSpellSlot, LaterSpellSlot):
    """MarioSpellSlot4 progress location class"""

    _original_item: type[Spell] = SuperFlame


class MarioSpellSlot5(MarioSpellSlot, LaterSpellSlot):
    """MarioSpellSlot5 progress location class"""

    _original_item: type[Spell] = UltraJump


class MarioSpellSlot6(MarioSpellSlot, LaterSpellSlot):
    """MarioSpellSlot6 progress location class"""

    _original_item: type[Spell] = UltraFlame


class MallowSpellSlot1(MallowSpellSlot):
    """MallowSpellSlot1 progress location class"""

    _original_item: type[Spell] = Thunderbolt


class MallowSpellSlot2(MallowSpellSlot, LaterSpellSlot):
    """MallowSpellSlot2 progress location class"""

    _original_item: type[Spell] = HPRain


class MallowSpellSlot3(MallowSpellSlot, LaterSpellSlot):
    """MallowSpellSlot3 progress location class"""

    _original_item: type[Spell] = Psychopath


class MallowSpellSlot4(MallowSpellSlot, LaterSpellSlot):
    """MallowSpellSlot4 progress location class"""

    _original_item: type[Spell] = Shocker


class MallowSpellSlot5(MallowSpellSlot, LaterSpellSlot):
    """MallowSpellSlot5 progress location class"""

    _original_item: type[Spell] = Snowy


class MallowSpellSlot6(MallowSpellSlot, LaterSpellSlot):
    """MallowSpellSlot6 progress location class"""

    _original_item: type[Spell] = StarRain


class GenoSpellSlot1(GenoSpellSlot):
    """GenoSpellSlot1 progress location class"""

    _original_item: type[Spell] = GenoBeam


class GenoSpellSlot2(GenoSpellSlot, LaterSpellSlot):
    """GenoSpellSlot2 progress location class"""

    _original_item: type[Spell] = GenoBoost


class GenoSpellSlot3(GenoSpellSlot, LaterSpellSlot):
    """GenoSpellSlot3 progress location class"""

    _original_item: type[Spell] = GenoWhirl


class GenoSpellSlot4(GenoSpellSlot, LaterSpellSlot):
    """GenoSpellSlot4 progress location class"""

    _original_item: type[Spell] = GenoBlast


class GenoSpellSlot5(GenoSpellSlot, LaterSpellSlot):
    """GenoSpellSlot5 progress location class"""

    _original_item: type[Spell] = GenoFlash


class GenoSpellSlot6(GenoSpellSlot, LaterSpellSlot):
    """GenoSpellSlot6 progress location class"""

    _original_item = None


class BowserSpellSlot1(BowserSpellSlot):
    """BowserSpellSlot1 progress location class"""

    _original_item: type[Spell] = Terrorize


class BowserSpellSlot2(BowserSpellSlot, LaterSpellSlot):
    """BowserSpellSlot2 progress location class"""

    _original_item: type[Spell] = PoisonGas


class BowserSpellSlot3(BowserSpellSlot, LaterSpellSlot):
    """BowserSpellSlot3 progress location class"""

    _original_item: type[Spell] = Crusher


class BowserSpellSlot4(BowserSpellSlot, LaterSpellSlot):
    """BowserSpellSlot4 progress location class"""

    _original_item: type[Spell] = BowserCrush


class BowserSpellSlot5(BowserSpellSlot, LaterSpellSlot):
    """BowserSpellSlot5 progress location class"""

    _original_item = None


class BowserSpellSlot6(BowserSpellSlot, LaterSpellSlot):
    """BowserSpellSlot6 progress location class"""

    _original_item = None


class ToadstoolSpellSlot1(ToadstoolSpellSlot):
    """ToadstoolSpellSlot1 progress location class"""

    _original_item: type[Spell] = Therapy


class ToadstoolSpellSlot2(ToadstoolSpellSlot, LaterSpellSlot):
    """ToadstoolSpellSlot2 progress location class"""

    _original_item: type[Spell] = GroupHug


class ToadstoolSpellSlot3(ToadstoolSpellSlot, LaterSpellSlot):
    """ToadstoolSpellSlot3 progress location class"""

    _original_item: type[Spell] = SleepyTime


class ToadstoolSpellSlot4(ToadstoolSpellSlot, LaterSpellSlot):
    """ToadstoolSpellSlot4 progress location class"""

    _original_item: type[Spell] = ComeBack


class ToadstoolSpellSlot5(ToadstoolSpellSlot, LaterSpellSlot):
    """ToadstoolSpellSlot5 progress location class"""

    _original_item: type[Spell] = Mute


class ToadstoolSpellSlot6(ToadstoolSpellSlot, LaterSpellSlot):
    """ToadstoolSpellSlot6 progress location class"""

    _original_item: type[Spell] = PsychBomb
