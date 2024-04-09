"""Randomization logic for spells."""

from random import choice, choices
from typing import List, Type
from randomizer.entities.spells import (
    BowserCrush,
    Clone1,
    Clone2,
    Clone3,
    Crusher,
    EarthOrb,
    EarthPsychBomb,
    EarthShocker,
    EarthSnowy,
    EarthSuperFlame,
    EarthThunderbolt,
    EarthUltraFlame,
    FireBowserCrush,
    FireCrusher,
    FireJump,
    FireOrb,
    FireShocker,
    FireSnowy,
    FireSuperJump,
    FireThunderbolt,
    FireUltraJump,
    IceBowserCrush,
    IceCrusher,
    IceJump,
    IceOrb,
    IcePsychBomb,
    IceShocker,
    IceSuperFlame,
    IceSuperJump,
    IceThunderbolt,
    IceUltraFlame,
    IceUltraJump,
    Jump,
    PsychBomb,
    Shocker,
    Snowy,
    SuperFlame,
    SuperJump,
    ThunderBowserCrush,
    ThunderCrusher,
    ThunderJump,
    ThunderOrb,
    ThunderPsychBomb,
    ThunderSnowy,
    ThunderSuperFlame,
    ThunderSuperJump,
    ThunderUltraFlame,
    ThunderUltraJump,
    Thunderbolt,
    UltraFlame,
    UltraJump,
    EarthGenoBeam,
    EarthGenoFlash,
    FireGenoBeam,
    GenoBeam,
    GenoFlash,
    IceGenoFlash,
    ThunderGenoBeam,
    ThunderGenoFlash,
)
from randomizer.types.spells.classes import CharacterSpell, CloneSpell
from randomizer.types.spells.enums import Element
from randomizer.types.world import GameWorld
from randomizer.types.world.flags import CharacterSpellElements

ELEMENTAL_SPELL_POOLS = [
    [Jump, FireJump, IceJump, ThunderJump],
    [FireOrb, IceOrb, EarthOrb, ThunderOrb],
    [SuperJump, FireSuperJump, IceSuperJump, ThunderSuperJump],
    [SuperFlame, IceSuperFlame, ThunderSuperFlame, EarthSuperFlame],
    [UltraJump, IceUltraJump, FireUltraJump, ThunderUltraJump],
    [UltraFlame, IceUltraFlame, EarthUltraFlame, ThunderUltraFlame],
    [Thunderbolt, IceThunderbolt, FireThunderbolt, EarthThunderbolt],
    [Shocker, IceShocker, EarthShocker, FireShocker],
    [Snowy, FireSnowy, EarthSnowy, ThunderSnowy],
    [Crusher, IceCrusher, FireCrusher, ThunderCrusher],
    [BowserCrush, IceBowserCrush, FireBowserCrush, ThunderBowserCrush],
    [PsychBomb, IcePsychBomb, EarthPsychBomb, ThunderPsychBomb],
    [GenoBeam, FireGenoBeam, ThunderGenoBeam, EarthGenoBeam],
    [GenoFlash, IceGenoFlash, ThunderGenoFlash, EarthGenoFlash],
]


def initialize_clone_spells_and_elements(world: GameWorld) -> None:
    """There are 27 spells in the game, but all 5 characters
    can learn up to 6 spells each, for a total of 30.
    3 spells will be assigned to more than one character. We determine
    which spells this happens to here.
    This also determines spell elements, if applicable."""
    if world.settings.is_boolean_flag_enabled(CharacterSpellElements):
        randomizable_spells = [s for s in world.spells if s.element is not Element.NONE]
        for spell in randomizable_spells:
            index = world.spells.index(spell)
            group: List[Type[CharacterSpell]] = next(
                (g for g in ELEMENTAL_SPELL_POOLS if type(spell) in g)
            )
            world.spells[index] = choice(group)(world)
    clone_candidates = choices(world.spells, k=3)
    clone1 = world.get_spell_instance(Clone1)
    clone2 = world.get_spell_instance(Clone2)
    clone3 = world.get_spell_instance(Clone3)
    assert isinstance(clone_candidates[0], CharacterSpell)
    assert isinstance(clone_candidates[1], CharacterSpell)
    assert isinstance(clone_candidates[2], CharacterSpell)
    assert isinstance(clone1, CloneSpell)
    assert isinstance(clone2, CloneSpell)
    assert isinstance(clone3, CloneSpell)
    clone1.set_parent_spell(clone_candidates[0])
    clone2.set_parent_spell(clone_candidates[1])
    clone3.set_parent_spell(clone_candidates[2])
