"""Progress location definitions for learnable spells."""

from typing import Type

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
    UltraJump,
)
from randomizer.types.progress_locations import (
    BowserSpellSlot,
    GenoSpellSlot,
    LaterSpellSlot,
    MallowSpellSlot,
    MarioSpellSlot,
    ToadstoolSpellSlot,
)
from randomizer.types.spells import Spell


class MarioSpellSlot1(MarioSpellSlot):
    """MarioSpellSlot1 progress location class"""

    _original_item: Type[Spell] = Jump


class MarioSpellSlot2(MarioSpellSlot, LaterSpellSlot):
    """MarioSpellSlot2 progress location class"""

    _original_item: Type[Spell] = FireOrb


class MarioSpellSlot3(MarioSpellSlot, LaterSpellSlot):
    """MarioSpellSlot3 progress location class"""

    _original_item: Type[Spell] = SuperJump


class MarioSpellSlot4(MarioSpellSlot, LaterSpellSlot):
    """MarioSpellSlot4 progress location class"""

    _original_item: Type[Spell] = SuperFlame


class MarioSpellSlot5(MarioSpellSlot, LaterSpellSlot):
    """MarioSpellSlot5 progress location class"""

    _original_item: Type[Spell] = UltraJump


class MarioSpellSlot6(MarioSpellSlot, LaterSpellSlot):
    """MarioSpellSlot6 progress location class"""

    _original_item: Type[Spell] = UltraFlame


class MallowSpellSlot1(MallowSpellSlot):
    """MallowSpellSlot1 progress location class"""

    _original_item: Type[Spell] = Thunderbolt


class MallowSpellSlot2(MallowSpellSlot, LaterSpellSlot):
    """MallowSpellSlot2 progress location class"""

    _original_item: Type[Spell] = HPRain


class MallowSpellSlot3(MallowSpellSlot, LaterSpellSlot):
    """MallowSpellSlot3 progress location class"""

    _original_item: Type[Spell] = Psychopath


class MallowSpellSlot4(MallowSpellSlot, LaterSpellSlot):
    """MallowSpellSlot4 progress location class"""

    _original_item: Type[Spell] = Shocker


class MallowSpellSlot5(MallowSpellSlot, LaterSpellSlot):
    """MallowSpellSlot5 progress location class"""

    _original_item: Type[Spell] = Snowy


class MallowSpellSlot6(MallowSpellSlot, LaterSpellSlot):
    """MallowSpellSlot6 progress location class"""

    _original_item: Type[Spell] = StarRain


class GenoSpellSlot1(GenoSpellSlot):
    """GenoSpellSlot1 progress location class"""

    _original_item: Type[Spell] = GenoBeam


class GenoSpellSlot2(GenoSpellSlot, LaterSpellSlot):
    """GenoSpellSlot2 progress location class"""

    _original_item: Type[Spell] = GenoBoost


class GenoSpellSlot3(GenoSpellSlot, LaterSpellSlot):
    """GenoSpellSlot3 progress location class"""

    _original_item: Type[Spell] = GenoWhirl


class GenoSpellSlot4(GenoSpellSlot, LaterSpellSlot):
    """GenoSpellSlot4 progress location class"""

    _original_item: Type[Spell] = GenoBlast


class GenoSpellSlot5(GenoSpellSlot, LaterSpellSlot):
    """GenoSpellSlot5 progress location class"""

    _original_item: Type[Spell] = GenoFlash


class GenoSpellSlot6(GenoSpellSlot, LaterSpellSlot):
    """GenoSpellSlot6 progress location class"""

    _original_item = None


class BowserSpellSlot1(BowserSpellSlot):
    """BowserSpellSlot1 progress location class"""

    _original_item: Type[Spell] = Terrorize


class BowserSpellSlot2(BowserSpellSlot, LaterSpellSlot):
    """BowserSpellSlot2 progress location class"""

    _original_item: Type[Spell] = PoisonGas


class BowserSpellSlot3(BowserSpellSlot, LaterSpellSlot):
    """BowserSpellSlot3 progress location class"""

    _original_item: Type[Spell] = Crusher


class BowserSpellSlot4(BowserSpellSlot, LaterSpellSlot):
    """BowserSpellSlot4 progress location class"""

    _original_item: Type[Spell] = BowserCrush


class BowserSpellSlot5(BowserSpellSlot, LaterSpellSlot):
    """BowserSpellSlot5 progress location class"""

    _original_item = None


class BowserSpellSlot6(BowserSpellSlot, LaterSpellSlot):
    """BowserSpellSlot6 progress location class"""

    _original_item = None


class ToadstoolSpellSlot1(ToadstoolSpellSlot):
    """ToadstoolSpellSlot1 progress location class"""

    _original_item: Type[Spell] = Therapy


class ToadstoolSpellSlot2(ToadstoolSpellSlot, LaterSpellSlot):
    """ToadstoolSpellSlot2 progress location class"""

    _original_item: Type[Spell] = GroupHug


class ToadstoolSpellSlot3(ToadstoolSpellSlot, LaterSpellSlot):
    """ToadstoolSpellSlot3 progress location class"""

    _original_item: Type[Spell] = SleepyTime


class ToadstoolSpellSlot4(ToadstoolSpellSlot, LaterSpellSlot):
    """ToadstoolSpellSlot4 progress location class"""

    _original_item: Type[Spell] = ComeBack


class ToadstoolSpellSlot5(ToadstoolSpellSlot, LaterSpellSlot):
    """ToadstoolSpellSlot5 progress location class"""

    _original_item: Type[Spell] = Mute


class ToadstoolSpellSlot6(ToadstoolSpellSlot, LaterSpellSlot):
    """ToadstoolSpellSlot6 progress location class"""

    _original_item: Type[Spell] = PsychBomb
