"""Base classes for frequently used sprite animations that need to be
inserted into overworld scripts depending on boss shuffling."""

import re
from randomizer.types.numbers import UInt4, UInt8
from randomizer.types.overworld_scripts.action_scripts.arguments.types import (
    SequenceSpeed)
from randomizer.types.overworld_scripts.action_scripts.arguments import (
    NORMAL)


class SpriteAnimation:
    """A container class for specific information that needs to be used in animating
    overworld bosses and henchmen who have been shuffled into new positions."""

    _sequence_id: UInt4
    _contact_frame: UInt8 | None
    _total_duration: UInt8 | None
    _new_sprite_id: UInt8 | None
    _speed: SequenceSpeed

    @property
    def sequence_id(self) -> UInt4:
        """The ID of this sequence (from the sprite container definition)."""
        return self._sequence_id

    def set_sequence_id(self, sequence_id: int) -> None:
        """Set the ID of this sequence (from the sprite container definition)."""
        self._sequence_id = UInt4(sequence_id)

    @property
    def contact_frame(self) -> UInt8 | None:
        """The specific frame in the sequence where it looks like the sprite would be
        attacking the player.
        For example, if the sprite is punching, this would be the exact frame at which
        the punch looks like it would land.
        This matters especially for calibrating each sprite to replace Dodo in the
        statue minigame, or replace Punchinello shoving you backward in the mines."""
        return self._contact_frame

    def set_contact_frame(self, contact_frame: int | None) -> None:
        """Set the specific frame in the sequence where it looks like the sprite would be
        attacking the player.
        For example, if the sprite is punching, this would be the exact frame at which
        the punch looks like it would land.
        This matters especially for calibrating each sprite to replace Dodo in the
        statue minigame, or replace Punchinello shoving you backward in the mines."""
        if contact_frame is not None:
            self._contact_frame = UInt8(contact_frame)
        else:
            self._contact_frame = None

    @property
    def total_duration(self) -> UInt8 | None:
        """The total duration of the sequence."""
        return self._total_duration

    def set_total_duration(self, total_duration: int | None) -> None:
        """Set the total duration of the sequence."""
        if total_duration is not None:
            self._total_duration = UInt8(total_duration)
        else:
            self._total_duration = None

    @property
    def new_sprite_id(self) -> UInt8 | None:
        """If the desired animation doesn't belong to the sprite that would normally
        be used for this NPC, this specifies a different sprite ID to draw."""
        return self._new_sprite_id

    def set_new_sprite_id(self, new_sprite_id: int | None) -> None:
        """If the desired animation doesn't belong to the sprite that would normally
        be used for this NPC, this specifies a different sprite ID to draw."""
        if new_sprite_id is not None:
            self._new_sprite_id = UInt8(new_sprite_id)
        else:
            self._new_sprite_id = None

    @property
    def speed(self) -> SequenceSpeed:
        """The speed at which the sequence should play."""
        return self._speed

    def set_speed(self, speed: SequenceSpeed) -> None:
        """Set the speed at which the sequence should play."""
        self._speed = speed

    def __init__(
        self,
        sequence_id=0,
        contact_frame=None,
        total_duration=None,
        new_sprite_id=None,
        speed=NORMAL):
        self.set_sequence_id(sequence_id)
        self.set_contact_frame(contact_frame)
        self.set_total_duration(total_duration)
        self.set_new_sprite_id(new_sprite_id)
        self.set_speed(speed)


class SpriteAnimationCollection:
    """A collection that describes the animations an NPC should run
    under different circumstances in and in specific contexts."""

    _recoil: SpriteAnimation | None
    _bandits_way_distracted: SpriteAnimation | None
    _mines_punch: SpriteAnimation | None
    _tower_bullet: SpriteAnimation | None
    _chapel_laugh: SpriteAnimation | None
    _kitchen_prep: SpriteAnimation | None
    _ship_beckon: SpriteAnimation | None
    _ship_chair: SpriteAnimation | None
    _dojo_challenge: SpriteAnimation | None
    _statue_intro: SpriteAnimation | None
    _statue_peck: SpriteAnimation | None
    _statue_flustered: SpriteAnimation | None
    _keep_challenge: SpriteAnimation | None
    _keep_summon: SpriteAnimation | None
    _chandelier_challenge: SpriteAnimation | None
    _factory_pierce: SpriteAnimation | None
    _endgame_challenge: SpriteAnimation | None

    @property
    def recoil(self) -> SpriteAnimation | None:
        """Boss animation.
        A recoil animation for this NPC to use in several cutscenes."""
        return self._recoil

    def set_recoil(self, recoil: SpriteAnimation | None = None) -> None:
        """Boss animation.
        Set a recoil animation for this NPC to use in several cutscenes."""
        self._recoil = recoil

    @property
    def bandits_way_distracted(self) -> SpriteAnimation | None:
        """Boss animation.
        An animation to be used when looking away from the player in most Bandit's Way rooms.
        """
        return self._bandits_way_distracted

    def set_bandits_way_distracted(
        self, bandits_way_distracted: SpriteAnimation | None = None
    ) -> None:
        """Boss animation.
        Set the animation to be used when looking away from the player in most Bandit's Way
        rooms."""
        self._bandits_way_distracted = bandits_way_distracted

    @property
    def mines_punch(self) -> SpriteAnimation | None:
        """Boss animation.
        The animation to use when shoving the player out of the Mines final boss room.
        """
        return self._mines_punch

    def set_mines_punch(self, mines_punch: SpriteAnimation | None = None) -> None:
        """Boss animation.
        Set the animation to use when shoving the player out of the Mines final boss room.
        """
        self._mines_punch = mines_punch

    @property
    def tower_bullet(self) -> SpriteAnimation | None:
        """Henchman animation.
        The animation to use when spawning Bullet Bills in the third tower henchman room.
        """
        return self._tower_bullet

    def set_tower_bullet(self, tower_bullet: SpriteAnimation | None = None) -> None:
        """Henchman animation.
        Set the animation to use when spawning Bullet Bills in the third tower henchman room.
        """
        self._tower_bullet = tower_bullet

    @property
    def chapel_laugh(self) -> SpriteAnimation | None:
        """Boss animation.
        The animation for the NPC to use while henchmen are collecting dropped gear
        in the chapel."""
        return self._chapel_laugh

    def set_chapel_laugh(self, chapel_laugh: SpriteAnimation | None = None) -> None:
        """Boss animation.
        Set the animation for the NPC to use while henchmen are collecting dropped gear
        in the chapel."""
        self._chapel_laugh = chapel_laugh

    @property
    def kitchen_prep(self) -> SpriteAnimation | None:
        """Henchman animation.
        The animation for the NPC to use while fussing with the cake in the kitchen."""
        return self._kitchen_prep

    def set_kitchen_prep(self, kitchen_prep: SpriteAnimation | None = None) -> None:
        """Henchman animation.
        Set the animation for the NPC to use while fussing with the cake in the kitchen.
        """
        self._kitchen_prep = kitchen_prep

    @property
    def ship_beckon(self) -> SpriteAnimation | None:
        """Boss animation.
        The animation performed by the NPC when it pops out of the ship password pipe.
        """
        return self._ship_beckon

    def set_ship_beckon(self, ship_beckon: SpriteAnimation | None = None) -> None:
        """Boss animation.
        Sethe animation performed by the NPC when it pops out of the ship password pipe.
        """
        self._ship_beckon = ship_beckon

    @property
    def ship_chair(self) -> SpriteAnimation | None:
        """Boss animation.
        The animation performed by the NPC when it is seated in the chair in the ship boss room.
        """
        return self._ship_chair

    def set_ship_chair(self, ship_chair: SpriteAnimation | None = None) -> None:
        """Boss animation.
        Set he animation performed by the NPC when it is seated in the chair in the
        ship boss room."""
        self._ship_chair = ship_chair

    @property
    def dojo_challenge(self) -> SpriteAnimation | None:
        """Boss animation.
        The animation performed by the NPC right before your battle begins in the dojo.
        """
        return self._dojo_challenge

    def set_dojo_challenge(
        self, dojo_challenge: SpriteAnimation | None = None
    ) -> None:
        """Boss animation.
        Set the animation performed by the NPC right before your battle begins in the dojo.
        """
        self._dojo_challenge = dojo_challenge

    @property
    def statue_intro(self) -> SpriteAnimation | None:
        """Boss animation.
        The animation performed by the NPC, when it is the statue polisher, upon first entering
        the satue minigame room."""
        return self._statue_intro

    def set_statue_intro(self, statue_intro: SpriteAnimation | None = None) -> None:
        """Boss animation.
        Set the animation performed by the NPC, when it is the statue polisher, upon first entering
        the satue minigame room."""
        self._statue_intro = statue_intro

    @property
    def statue_peck(self) -> SpriteAnimation | None:
        """Boss animation.
        The animation performed by the NPC, when it is the statue polisher, for it to hit
        the statue."""
        return self._statue_peck

    def set_statue_peck(self, statue_peck: SpriteAnimation | None = None) -> None:
        """Boss animation.
        Set the animation performed by the NPC, when it is the statue polisher, for it to hit
        the statue."""
        self._statue_peck = statue_peck

    @property
    def statue_flustered(self) -> SpriteAnimation | None:
        """Boss animation.
        The animation performed by the NPC, when it is the statue polisher, when it gets
        startled by the player failing to jump out of the way."""
        return self._statue_flustered

    def set_statue_flustered(
        self, statue_flustered: SpriteAnimation | None = None
    ) -> None:
        """Boss animation.
        Set the animation performed by the NPC, when it is the statue polisher, when it gets
        startled by the player failing to jump out of the way."""
        self._statue_flustered = statue_flustered

    @property
    def keep_challenge(self) -> SpriteAnimation | None:
        """Boss animation.
        The animation performed by the NPC, when it is the first Keep boss past the 6 doors,
        right before the battle starts."""
        return self._keep_challenge

    def set_keep_challenge(
        self, keep_challenge: SpriteAnimation | None = None
    ) -> None:
        """Boss animation.
        Set the animation performed by the NPC, when it is the first Keep boss past the 6 doors,
        right before the battle starts."""
        self._keep_challenge = keep_challenge

    @property
    def keep_summon(self) -> SpriteAnimation | None:
        """Boss animation.
        The animation performed by the NPC, when it is the first Keep boss past the 6 doors,
        when it is summoning an object into the room."""
        return self._keep_summon

    def set_keep_summon(self, keep_summon: SpriteAnimation | None = None) -> None:
        """Boss animation.
        Set the animation performed by the NPC, when it is the first Keep boss past the 6 doors,
        when it is summoning an object into the room."""
        self._keep_summon = keep_summon

    @property
    def chandelier_challenge(self) -> SpriteAnimation | None:
        """Boss animation.
        The animation performed by the NPC, when it is the chandelier boss,
        right before the battle starts."""
        return self._chandelier_challenge

    def set_chandelier_challenge(
        self, chandelier_challenge: SpriteAnimation | None = None
    ) -> None:
        """Boss animation.
        Set the animation performed by the NPC, when it is the chandelier boss,
        right before the battle starts."""
        self._chandelier_challenge = chandelier_challenge

    @property
    def factory_pierce(self) -> SpriteAnimation | None:
        """Henchman animation.
        The animation performed by the NPC when it is working on the production line
        in the third boss rush room in the factory."""
        return self._factory_pierce

    def set_factory_pierce(
        self, factory_pierce: SpriteAnimation | None = None
    ) -> None:
        """Henchman animation.
        Set the animation performed by the NPC when it is working on the production line
        in the third boss rush room in the factory."""
        self._factory_pierce = factory_pierce

    @property
    def endgame_challenge(self) -> SpriteAnimation | None:
        """Boss animation.
        The animation performed by the NPC, when it is the final boss,
        right before the battle starts."""
        return self._endgame_challenge

    def set_endgame_challenge(
        self, endgame_challenge: SpriteAnimation | None = None
    ) -> None:
        """Boss animation.
        Set the animation performed by the NPC, when it is the final boss,
        right before the battle starts."""
        self._endgame_challenge = endgame_challenge

    @property
    def animation_prop_names(self) -> list[str]:
        """Returns the property names of all animations as strings"""
        return [prop for prop in dir(self) if re.search("^_+", prop) is None]

    def __init__(
        self,
        recoil: SpriteAnimation | None = None,
        bandits_way_distracted: SpriteAnimation | None = None,
        mines_punch: SpriteAnimation | None = None,
        tower_bullet: SpriteAnimation | None = None,
        chapel_laugh: SpriteAnimation | None = None,
        kitchen_prep: SpriteAnimation | None = None,
        ship_beckon: SpriteAnimation | None = None,
        ship_chair: SpriteAnimation | None = None,
        dojo_challenge: SpriteAnimation | None = None,
        statue_intro: SpriteAnimation | None = None,
        statue_peck: SpriteAnimation | None = None,
        statue_flustered: SpriteAnimation | None = None,
        keep_challenge: SpriteAnimation | None = None,
        keep_summon: SpriteAnimation | None = None,
        chandelier_challenge: SpriteAnimation | None = None,
        factory_pierce: SpriteAnimation | None = None,
        endgame_challenge: SpriteAnimation | None = None):
        self.set_recoil(recoil)
        self.set_bandits_way_distracted(bandits_way_distracted)
        self.set_mines_punch(mines_punch)
        self.set_tower_bullet(tower_bullet)
        self.set_chapel_laugh(chapel_laugh)
        self.set_kitchen_prep(kitchen_prep)
        self.set_ship_beckon(ship_beckon)
        self.set_ship_chair(ship_chair)
        self.set_dojo_challenge(dojo_challenge)
        self.set_statue_intro(statue_intro)
        self.set_statue_peck(statue_peck)
        self.set_statue_flustered(statue_flustered)
        self.set_keep_challenge(keep_challenge)
        self.set_keep_summon(keep_summon)
        self.set_chandelier_challenge(chandelier_challenge)
        self.set_factory_pierce(factory_pierce)
        self.set_endgame_challenge(endgame_challenge)
