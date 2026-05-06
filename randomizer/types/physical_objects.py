"""Various representations of an immutable object, like a mushroom, flower, shell, etc"""

from dataclasses import dataclass
from math import ceil
from smrpgpatchbuilder.datatypes.levels.classes import NPC as NPCBase
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import (
    SOUTHEAST,
    SOUTHWEST,
    NORTHEAST,
    NORTHWEST,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.direction import (
    Direction,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments.types.classes import (
    SequenceSpeed,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments.sequence_speeds import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.classes import (
    UsableActionScriptCommand,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.commands import (
    A_SetSpriteSequence as SetSpriteSequence,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (
    ActionSubcriptCommandPrototype,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.packet import Packet
from ..data.variables.event_script_names import *
from ..data.variables.packet_names import *
import re
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.graphics.classes import (
    AnimationSequence,
    Tile,
    CompleteSprite,
)
from ..data.sprites.sprites import sprites

if TYPE_CHECKING:
    from ..types.gameworld import GameWorld


class SpriteAnimation:
    """A container class for specific information that needs to be used in animating
    overworld bosses and henchmen who have been shuffled into new positions."""

    _sequence_id: int
    _contact_frame: int | None
    _total_duration: int
    _speed: SequenceSpeed
    _model: NPCBase

    @property
    def model(self) -> NPCBase:
        """The underlying NPC model whose sprite this animation is based on."""
        return self._model

    @property
    def sequence_id(self) -> int:
        """The ID of this sequence (from the sprite container definition)."""
        return self._sequence_id

    def set_sequence_id(self, sequence_id: int) -> None:
        """Set the ID of this sequence (from the sprite container definition)."""
        self._sequence_id = sequence_id

    @property
    def contact_frame(self) -> int | None:
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
        self._contact_frame = contact_frame

    @property
    def total_duration(self) -> int:
        """The total duration of the sequence."""
        return self._total_duration

    def set_total_duration(self, total_duration: int) -> None:
        """Set the total duration of the sequence."""
        self._total_duration = total_duration

    @property
    def speed(self) -> SequenceSpeed:
        """The speed at which the sequence should play."""
        return self._speed

    def set_speed(self, speed: SequenceSpeed) -> None:
        """Set the speed at which the sequence should play."""
        self._speed = speed

    def __init__(
        self,
        model: NPCBase,
        sequence_id: int,
        max_contact_frame: int | None = None,
        max_duration: int | None = None,
    ):
        self._model = model
        speed: SequenceSpeed = NORMAL
        sprite = sprites.sprites[model.sprite_id]
        assert sequence_id < len(sprite.animation.properties.sequences)
        sequence = sprite.animation.properties.sequences[sequence_id]
        if max_duration is not None and max_contact_frame is not None:
            speed_candidate_1 = sequence.target_speed_by_duration_limit(max_duration)
            speed_candidate_2 = sequence.target_speed_by_contact_frame_limit(
                max_contact_frame
            )
            if speed_candidate_1 == speed_candidate_2:
                speed = speed_candidate_1
            else:
                # solve conflict by seeing which of the two is valid for both
                candidate_1_valid = (
                    sequence.contact_duration(speed_candidate_1) <= max_contact_frame
                )
                candidate_2_valid = (
                    sequence.total_duration(speed_candidate_2) <= max_duration
                )
                if candidate_1_valid and candidate_2_valid:
                    speed = min(speed_candidate_1, speed_candidate_2)
                elif candidate_1_valid:
                    speed = speed_candidate_1
                elif candidate_2_valid:
                    speed = speed_candidate_2
                else:
                    raise ValueError(
                        f"Cannot set speed for sequence {sequence_id} with given max_contact_frame and max_duration, because neither speed_candidate_1 nor speed_candidate_2 is valid for both limits. "
                        f"(candidate_1_valid={candidate_1_valid}, candidate_2_valid={candidate_2_valid}, "
                        f"speed_candidate_1={speed_candidate_1}, speed_candidate_2={speed_candidate_2}, "
                        f"contact_duration at speed_candidate_1={sequence.contact_duration(speed_candidate_1)}, "
                        f"total_duration at speed_candidate_2={sequence.total_duration(speed_candidate_2)})"
                    )
        elif max_duration is not None:
            speed = sequence.target_speed_by_duration_limit(max_duration)
        elif max_contact_frame is not None:
            speed = sequence.target_speed_by_contact_frame_limit(max_contact_frame)
        self.set_sequence_id(sequence_id)
        self.set_contact_frame(sequence.contact_duration(speed))
        self.set_total_duration(sequence.total_duration(speed))
        self.set_speed(speed)


def statue_peck_animation(a: SpriteAnimation | None) -> SpriteAnimation | None:
    if a is None:
        return None
    return SpriteAnimation(a.model, a.sequence_id, max_contact_frame=20)


def factory_piece_animation(a: SpriteAnimation | None) -> SpriteAnimation | None:
    if a is None:
        return None
    return SpriteAnimation(a.model, a.sequence_id, max_duration=32)


def tower_bullet_animation(a: SpriteAnimation | None) -> SpriteAnimation | None:
    if a is None:
        return None
    return SpriteAnimation(a.model, a.sequence_id, max_contact_frame=56)


class SpriteAnimationCollection:
    """A collection that describes the animations an NPC should run
    under different circumstances in and in specific contexts."""

    _recoil: SpriteAnimation | None
    _tower_crying: SpriteAnimation | None
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
    _look_at_ceiling_mold_id: int | None
    _tpose_mold_id: int | None
    _tower_toss: SpriteAnimation | None
    _tpose: SpriteAnimation | None
    _look_at_ceiling: SpriteAnimation | None
    _look_at_camera: SpriteAnimation | None

    @property
    def tower_crying(self) -> SpriteAnimation | None:
        """Boss animation.
        A crying animation for this NPC to use in the tower henchman room where they cry.
        """
        return self._tower_crying

    def set_tower_crying(self, tower_crying: SpriteAnimation | None = None) -> None:
        """Boss animation.
        Set a crying animation for this NPC to use in the tower henchman room where they cry.
        """
        self._tower_crying = tower_crying

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
        self._tower_bullet = tower_bullet_animation(tower_bullet)

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

    def set_dojo_challenge(self, dojo_challenge: SpriteAnimation | None = None) -> None:
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
        self._statue_peck = statue_peck_animation(statue_peck)

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

    def set_keep_challenge(self, keep_challenge: SpriteAnimation | None = None) -> None:
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

    def set_factory_pierce(self, factory_pierce: SpriteAnimation | None = None) -> None:
        """Henchman animation.
        Set the animation performed by the NPC when it is working on the production line
        in the third boss rush room in the factory."""
        self._factory_pierce = factory_piece_animation(factory_pierce)

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

    @property
    def look_at_ceiling_mold_id(self) -> int | None:
        """The mold ID to use when the NPC is looking at the ceiling."""
        return self._look_at_ceiling_mold_id

    def set_look_at_ceiling_mold_id(self, mold_id: int | None = None) -> None:
        """Set the mold ID to use when the NPC is looking at the ceiling."""
        self._look_at_ceiling_mold_id = mold_id

    @property
    def tpose_mold_id(self) -> int | None:
        """The mold ID to use when the NPC is in a T-pose."""
        return self._tpose_mold_id

    def set_tpose_mold_id(self, mold_id: int | None = None) -> None:
        """Set the mold ID to use when the NPC is in a T-pose."""
        self._tpose_mold_id = mold_id

    @property
    def tower_toss(self) -> SpriteAnimation | None:
        """Henchman animation.
        The animation to use when tossing objects in the second tower henchman room.
        """
        return self._tower_toss

    def set_tower_toss(self, tower_toss: SpriteAnimation | None = None) -> None:
        """Henchman animation.
        Set the animation to use when tossing objects in the second tower henchman room.
        """
        self._tower_toss = tower_toss

    @property
    def tpose(self) -> SpriteAnimation | None:
        """The animation to use when the NPC is in a T-pose."""
        return self._tpose

    def set_tpose(self, tpose: SpriteAnimation | None = None) -> None:
        """Set the animation to use when the NPC is in a T-pose."""
        self._tpose = tpose

    @property
    def look_at_ceiling(self) -> SpriteAnimation | None:
        """The animation to use when the NPC is looking at the ceiling."""
        return self._look_at_ceiling

    def set_look_at_ceiling(
        self, look_at_ceiling: SpriteAnimation | None = None
    ) -> None:
        """Set the animation to use when the NPC is looking at the ceiling."""
        self._look_at_ceiling = look_at_ceiling

    @property
    def look_at_camera(self) -> SpriteAnimation | None:
        """The animation to use when the NPC is looking at the camera."""
        return self._look_at_camera

    def set_look_at_camera(self, look_at_camera: SpriteAnimation | None = None) -> None:
        """Set the animation to use when the NPC is looking at the camera."""
        self._look_at_camera = look_at_camera

    def __init__(
        self,
        recoil: SpriteAnimation | None = None,
        tower_crying: SpriteAnimation | None = None,
        bandits_way_distracted: SpriteAnimation | None = None,
        mines_punch: SpriteAnimation | None = None,
        tower_bullet: SpriteAnimation | None = None,
        tower_toss: SpriteAnimation | None = None,
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
        endgame_challenge: SpriteAnimation | None = None,
        look_at_ceiling_mold_id: int | None = None,
        tpose_mold_id: int | None = None,
        tpose: SpriteAnimation | None = None,
        look_at_ceiling: SpriteAnimation | None = None,
        look_at_camera: SpriteAnimation | None = None,
    ):
        self.set_recoil(recoil)
        self.set_tower_crying(tower_crying)
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
        self.set_look_at_ceiling_mold_id(look_at_ceiling_mold_id)
        self.set_tpose_mold_id(tpose_mold_id)
        self.set_tower_toss(tower_toss)
        self.set_tpose(tpose)
        self.set_look_at_ceiling(look_at_ceiling)
        self.set_look_at_camera(look_at_camera)


class NPC:
    _base: NPCBase

    _crown_height: int = 2
    _eye_height: int = 17
    _tower_entrance_horizontal_shift: int = 0

    @property
    def base(self) -> NPCBase:
        """The underlying NPC object from the patch builder."""
        return self._base

    @property
    def crown_height(self) -> int:
        """The height at which the crown should rise or lower relative to Booster's height to look like it is sitting on this NPC's head, in pixels."""
        return self._crown_height

    @property
    def eye_height(self) -> int:
        """The height at which the NPC should rise or lower to have their eyes match up with the window in the Booster Tower door."""
        return self._eye_height

    @property
    def tower_entrance_horizontal_shift(self) -> int:
        """The horizontal shift to apply to this NPC to complement the eye_height offset."""
        return self._tower_entrance_horizontal_shift

    @property
    def min_vram_size(self) -> int:
        """The minimum number (0 to 7) of VRAM chunks the NPC's sprite can be expected to require.\n
        Generally, this number is 0 for gridplane sprites. \n
        For non-gridplane sprites, this number is usually total tiles divided by 4,
        rounded down (where a tile is a group of four subtiles).\n
        This calculation should be based on the largest mold (in terms of tiles used)
        that you expect to see displayed from the sprite."""
        assert self.base._min_vram_size <= 7
        return self.base._min_vram_size

    def min_vram_from_mold(
        self, world: "GameWorld", mold_id: int, offset: int = 0
    ) -> int:
        """Get min vram size from a certain sprite mold ID"""
        sprite = world.get_sprite(self.base.sprite_id + offset)
        assert mold_id < len(sprite.animation.properties.molds), (
            f"Mold {mold_id} not found in sprite {self.base.sprite_id + offset} "
            f"(base={self.base.sprite_id}, offset={offset}, "
            f"num_molds={len(sprite.animation.properties.molds)})"
        )
        if sprite.animation.properties.molds[mold_id].gridplane:
            return 0
        tiles = sprite.animation.properties.molds[mold_id].tiles
        truthy_subtiles = 0
        for t in tiles:
            if isinstance(t, Tile):
                truthy_subtiles += len([s for s in t.subtile_bytes if s is not None])
        return ceil(max(0, truthy_subtiles - 16) / 16)

    def min_vram_from_sequence(
        self, world: "GameWorld", sequence_id: int, offset: int = 0
    ) -> int:
        """Get min vram size from a certain sprite sequence ID"""
        sprite = world.get_sprite(self.base.sprite_id + offset)
        assert sequence_id < len(sprite.animation.properties.sequences)
        min_vram = 0
        frames = sprite.animation.properties.sequences[sequence_id].frames
        for frame in frames:
            min_vram = max(
                min_vram, self.min_vram_from_mold(world, frame.mold_id, offset)
            )
        return min_vram

    def _min_vram_size_from_script(
        self, world: "GameWorld", script: list[UsableActionScriptCommand]
    ) -> int:
        min_vram = self.min_vram_from_mold(world, 0)
        for cmd in script:
            if isinstance(cmd, SetSpriteSequence):
                prop_id = cmd.index
                offset = cmd.sprite_offset
                if cmd.is_mold:
                    min_vram = max(
                        min_vram, self.min_vram_from_mold(world, prop_id, offset)
                    )
                else:
                    min_vram = max(
                        min_vram, self.min_vram_from_sequence(world, prop_id, offset)
                    )
        return min_vram

    def min_vram_from_action_script(self, world: "GameWorld", script_id: int) -> int:
        """Get min vram size from a given action script"""
        script = world.action_scripts.scripts[script_id]
        return self._min_vram_size_from_script(world, script.contents)

    def min_vram_from_event_script(
        self, world: "GameWorld", target: int, script_id: int
    ) -> int:
        """Get min vram size from subscripts in a given event script"""
        min_vram = self.min_vram_from_mold(world, 0)
        script = world.event_scripts.get_script_by_id(script_id)
        for cmd in script.contents:
            if isinstance(cmd, ActionSubcriptCommandPrototype) and cmd.target == target:
                min_vram = max(
                    min_vram,
                    self._min_vram_size_from_script(world, cmd.subscript.contents),
                )
        return min_vram

    def is_equal(self, npc: "NPC") -> bool:
        """True if this NPC's properties are all equal to another NPC's."""
        return (
            self.base.sprite_id == npc.base.sprite_id
            and self.base.show_shadow == npc.base.show_shadow
            and self.base.shadow_size == npc.base.shadow_size
            and self.base.acute_axis == npc.base.acute_axis
            and self.base.obtuse_axis == npc.base.obtuse_axis
            and self.base.height == npc.base.height
            and self.base.directions == npc.base.directions
            and self.base.min_vram_size == npc.base.min_vram_size
            and self.base.byte2_bit0 == npc.base.byte2_bit0
            and self.base.byte2_bit1 == npc.base.byte2_bit1
            and self.base.byte2_bit2 == npc.base.byte2_bit2
            and self.base.byte2_bit3 == npc.base.byte2_bit3
            and self.base.byte2_bit4 == npc.base.byte2_bit4
            and self.base.byte5_bit6 == npc.base.byte5_bit6
            and self.base.byte5_bit7 == npc.base.byte5_bit7
            and self.base.byte6_bit2 == npc.base.byte6_bit2
        )


@dataclass(frozen=True)
class PixelShift:
    """A signed pixel offset applied to a statue sprite when spawned.

    right: positive = shift right, negative = shift left (in pixels).
    down: positive = shift down, negative = shift up (in pixels).
    """

    right: int
    down: int


class SupplantableNPC(NPC):
    _recoil: int | None = None
    _tower_crying: int | None = None
    _bandits_way_distracted: int | None = None
    _mines_punch: int | None = None
    _tower_bullet: int | None = None
    _tower_toss: int | None = None
    _chapel_laugh: int | None = None
    _kitchen_prep: int | None = None
    _ship_beckon: int | None = None
    _ship_chair: int | None = None
    _dojo_challenge: int | None = None
    _statue_intro: int | None = None
    _statue_peck: int | None = None
    _statue_flustered: int | None = None
    _keep_challenge: int | None = None
    _keep_summon: int | None = None
    _chandelier_challenge: int | None = None
    _factory_pierce: int | None = None
    _endgame_challenge: int | None = None
    _look_at_ceiling_mold_id: int | None = None
    _tpose_mold_id: int | None = None
    _tpose: int | None = None
    _look_at_ceiling: int | None = None
    _look_at_camera: int | None = None

    @property
    def animations(self):
        return SpriteAnimationCollection(
            recoil=(
                SpriteAnimation(self.base, self._recoil)
                if self._recoil is not None
                else None
            ),
            tower_crying=(
                SpriteAnimation(self.base, self._tower_crying)
                if self._tower_crying is not None
                else None
            ),
            bandits_way_distracted=(
                SpriteAnimation(self.base, self._bandits_way_distracted)
                if self._bandits_way_distracted is not None
                else None
            ),
            mines_punch=(
                SpriteAnimation(self.base, self._mines_punch)
                if self._mines_punch is not None
                else None
            ),
            tower_bullet=(
                SpriteAnimation(self.base, self._tower_bullet)
                if self._tower_bullet is not None
                else None
            ),
            tower_toss=(
                SpriteAnimation(self.base, self._tower_toss)
                if self._tower_toss is not None
                else None
            ),
            chapel_laugh=(
                SpriteAnimation(self.base, self._chapel_laugh)
                if self._chapel_laugh is not None
                else None
            ),
            kitchen_prep=(
                SpriteAnimation(self.base, self._kitchen_prep)
                if self._kitchen_prep is not None
                else None
            ),
            ship_beckon=(
                SpriteAnimation(self.base, self._ship_beckon)
                if self._ship_beckon is not None
                else None
            ),
            ship_chair=(
                SpriteAnimation(self.base, self._ship_chair)
                if self._ship_chair is not None
                else None
            ),
            dojo_challenge=(
                SpriteAnimation(self.base, self._dojo_challenge)
                if self._dojo_challenge is not None
                else None
            ),
            statue_intro=(
                SpriteAnimation(self.base, self._statue_intro)
                if self._statue_intro is not None
                else None
            ),
            statue_peck=(
                SpriteAnimation(self.base, self._statue_peck)
                if self._statue_peck is not None
                else None
            ),
            statue_flustered=(
                SpriteAnimation(self.base, self._statue_flustered)
                if self._statue_flustered is not None
                else None
            ),
            keep_challenge=(
                SpriteAnimation(self.base, self._keep_challenge)
                if self._keep_challenge is not None
                else None
            ),
            keep_summon=(
                SpriteAnimation(self.base, self._keep_summon)
                if self._keep_summon is not None
                else None
            ),
            chandelier_challenge=(
                SpriteAnimation(self.base, self._chandelier_challenge)
                if self._chandelier_challenge is not None
                else None
            ),
            factory_pierce=(
                SpriteAnimation(self.base, self._factory_pierce)
                if self._factory_pierce is not None
                else None
            ),
            endgame_challenge=(
                SpriteAnimation(self.base, self._endgame_challenge)
                if self._endgame_challenge is not None
                else None
            ),
            look_at_ceiling_mold_id=self._look_at_ceiling_mold_id,
            tpose_mold_id=self._tpose_mold_id,
            tpose=(
                SpriteAnimation(self.base, self._tpose)
                if self._tpose is not None
                else None
            ),
            look_at_ceiling=(
                SpriteAnimation(self.base, self._look_at_ceiling)
                if self._look_at_ceiling is not None
                else None
            ),
            look_at_camera=(
                SpriteAnimation(self.base, self._look_at_camera)
                if self._look_at_camera is not None
                else None
            ),
        )

    @classmethod
    def get_vram_size(cls, world: "GameWorld") -> int:
        """Get the VRAM size for this BossNPC's sprite.

        Returns the sprite's animation.properties.vram_size value.
        Valid values are typically 2048, 4096, 6144, or 8192.
        """
        instance = cls()
        sprite_id = instance.base.sprite_id
        sprite = world.get_sprite(sprite_id)
        return sprite.animation.properties.vram_size

    @classmethod
    def get_min_vram_size(cls) -> int:
        """Get the min_vram_size for this BossNPC's NPC definition.

        Returns the NPC's min_vram_size value (0-7).
        """
        instance = cls()
        return instance.base.min_vram_size

    @classmethod
    def get_min_vram_from_sequence(cls, world: "GameWorld", sequence_id: int) -> int:
        """Get the min vram size from a certain sprite sequence ID for this BossNPC.

        Returns the maximum min_vram_from_mold across all frames in the sequence.
        """
        instance = cls()
        return instance.min_vram_from_sequence(world, sequence_id)


class StatueNPC(SupplantableNPC):
    _facing_shifts: dict[Direction, PixelShift] = {}

    @property
    def southwest_facing_shift(self) -> PixelShift | None:
        """Pixel shift applied when this statue is spawned facing southwest."""
        return self._facing_shifts.get(SOUTHWEST)

    @property
    def southeast_facing_shift(self) -> PixelShift | None:
        """Pixel shift applied when this statue is spawned facing southeast."""
        return self._facing_shifts.get(SOUTHEAST)

    @property
    def northwest_facing_shift(self) -> PixelShift | None:
        """Pixel shift applied when this statue is spawned facing northwest."""
        return self._facing_shifts.get(NORTHWEST)

    @property
    def northeast_facing_shift(self) -> PixelShift | None:
        """Pixel shift applied when this statue is spawned facing northeast."""
        return self._facing_shifts.get(NORTHEAST)


class BossNPC(SupplantableNPC):

    # Per-direction statue pixel shifts. Missing keys (or None) mean no shift
    # is applied for that direction. Keys: SOUTHWEST, SOUTHEAST, NORTHWEST, NORTHEAST.

    # Palette data (15 24-bit RGB colors) to use as this boss's "evil"
    # palette variant (e.g. for the Keep boss 1 pre-reformation scene).
    # None means no dedicated evil palette is defined; callers should
    # fall back to the sprite's default palette.
    _evil_palette: list[int] | None = None

    @property
    def evil_palette(self) -> list[int] | None:
        """The 15-color palette (as 24-bit hex RGB ints) to use as this
        boss's 'evil' palette variant. Returns None if this boss has no
        dedicated evil palette, in which case callers should fall back
        to the sprite's default palette (palette_id + palette_offset)."""
        return self._evil_palette


class HenchmanNPC(SupplantableNPC):
    pass


class ItemNPC(NPC):
    _chest_event_id: int = E0883_CHEST_ITEM_BAG_PACKET
    _chest_70a7_upper: int = 0
    _hover: bool = False
