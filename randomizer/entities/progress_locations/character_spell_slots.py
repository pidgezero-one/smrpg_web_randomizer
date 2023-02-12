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
from randomizer.types.progress_locations.classes import (
    BowserSpellSlot,
    GenoSpellSlot,
    LaterSpellSlot,
    MallowSpellSlot,
    MarioSpellSlot,
    ToadstoolSpellSlot,
)
from randomizer.types.spells.classes import Spell


class MarioSpellSlot1(MarioSpellSlot):
    _original_item: Type[Spell] = Jump


class MarioSpellSlot2(MarioSpellSlot, LaterSpellSlot):
    _original_item: Type[Spell] = FireOrb


class MarioSpellSlot3(MarioSpellSlot, LaterSpellSlot):
    _original_item: Type[Spell] = SuperJump


class MarioSpellSlot4(MarioSpellSlot, LaterSpellSlot):
    _original_item: Type[Spell] = SuperFlame


class MarioSpellSlot5(MarioSpellSlot, LaterSpellSlot):
    _original_item: Type[Spell] = UltraJump


class MarioSpellSlot6(MarioSpellSlot, LaterSpellSlot):
    _original_item: Type[Spell] = UltraFlame


class MallowSpellSlot1(MallowSpellSlot):
    _original_item: Type[Spell] = Thunderbolt


class MallowSpellSlot2(MallowSpellSlot, LaterSpellSlot):
    _original_item: Type[Spell] = HPRain


class MallowSpellSlot3(MallowSpellSlot, LaterSpellSlot):
    _original_item: Type[Spell] = Psychopath


class MallowSpellSlot4(MallowSpellSlot, LaterSpellSlot):
    _original_item: Type[Spell] = Shocker


class MallowSpellSlot5(MallowSpellSlot, LaterSpellSlot):
    _original_item: Type[Spell] = Snowy


class MallowSpellSlot6(MallowSpellSlot, LaterSpellSlot):
    _original_item: Type[Spell] = StarRain


class GenoSpellSlot1(GenoSpellSlot):
    _original_item: Type[Spell] = GenoBeam


class GenoSpellSlot2(GenoSpellSlot, LaterSpellSlot):
    _original_item: Type[Spell] = GenoBoost


class GenoSpellSlot3(GenoSpellSlot, LaterSpellSlot):
    _original_item: Type[Spell] = GenoWhirl


class GenoSpellSlot4(GenoSpellSlot, LaterSpellSlot):
    _original_item: Type[Spell] = GenoBlast


class GenoSpellSlot5(GenoSpellSlot, LaterSpellSlot):
    _original_item: Type[Spell] = GenoFlash


class GenoSpellSlot6(GenoSpellSlot, LaterSpellSlot):
    _original_item = None


class BowserSpellSlot1(BowserSpellSlot):
    _original_item: Type[Spell] = Terrorize


class BowserSpellSlot2(BowserSpellSlot, LaterSpellSlot):
    _original_item: Type[Spell] = PoisonGas


class BowserSpellSlot3(BowserSpellSlot, LaterSpellSlot):
    _original_item: Type[Spell] = Crusher


class BowserSpellSlot4(BowserSpellSlot, LaterSpellSlot):
    _original_item: Type[Spell] = BowserCrush


class BowserSpellSlot5(BowserSpellSlot, LaterSpellSlot):
    _original_item = None


class BowserSpellSlot6(BowserSpellSlot, LaterSpellSlot):
    _original_item = None


class ToadstoolSpellSlot1(ToadstoolSpellSlot):
    _original_item: Type[Spell] = Therapy


class ToadstoolSpellSlot2(ToadstoolSpellSlot, LaterSpellSlot):
    _original_item: Type[Spell] = GroupHug


class ToadstoolSpellSlot3(ToadstoolSpellSlot, LaterSpellSlot):
    _original_item: Type[Spell] = SleepyTime


class ToadstoolSpellSlot4(ToadstoolSpellSlot, LaterSpellSlot):
    _original_item: Type[Spell] = ComeBack


class ToadstoolSpellSlot5(ToadstoolSpellSlot, LaterSpellSlot):
    _original_item: Type[Spell] = Mute


class ToadstoolSpellSlot6(ToadstoolSpellSlot, LaterSpellSlot):
    _original_item: Type[Spell] = PsychBomb
