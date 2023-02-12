from typing import Optional
from randomizer.types.numbers.classes import UInt4, UInt8
from randomizer.types.overworld_scripts.action_scripts.constants.classes import (
    SequenceSpeed,
)
from randomizer.types.overworld_scripts.action_scripts.constants.sequence_speeds import (
    NORMAL,
)


class SpriteAnimation:
    _sequence_id: UInt4
    _contact_frame: Optional[UInt8]
    _total_duration: Optional[UInt8]
    _new_sprite_id: Optional[UInt8]
    _speed: SequenceSpeed

    @property
    def sequence_id(self) -> UInt4:
        return self._sequence_id

    def set_sequence_id(self, sequence_id: int) -> None:
        self._sequence_id = UInt4(sequence_id)

    @property
    def contact_frame(self) -> Optional[UInt8]:
        return self._contact_frame

    def set_contact_frame(self, contact_frame: Optional[int]) -> None:
        if contact_frame is not None:
            self._contact_frame = UInt8(contact_frame)
        else:
            self._contact_frame = None

    @property
    def total_duration(self) -> Optional[UInt8]:
        return self._total_duration

    def set_total_duration(self, total_duration: Optional[int]) -> None:
        if total_duration is not None:
            self._total_duration = UInt8(total_duration)
        else:
            self._total_duration = None

    @property
    def new_sprite_id(self) -> Optional[UInt8]:
        return self._new_sprite_id

    def set_new_sprite_id(self, new_sprite_id: Optional[int]) -> None:
        if new_sprite_id is not None:
            self._new_sprite_id = UInt8(new_sprite_id)
        else:
            self._new_sprite_id = None

    @property
    def speed(self) -> SequenceSpeed:
        return self._speed

    def set_speed(self, speed: SequenceSpeed) -> None:
        self._speed = speed

    def __init__(
        self,
        sequence_id=0,
        contact_frame=None,
        total_duration=None,
        new_sprite_id=None,
        speed=NORMAL,
    ):
        self.set_sequence_id(sequence_id)
        self.set_contact_frame(contact_frame)
        self.set_total_duration(total_duration)
        self.set_new_sprite_id(new_sprite_id)
        self.set_speed(speed)


class SpriteAnimationCollection:
    _recoil: Optional[SpriteAnimation]
    _bandits_way_distracted: Optional[SpriteAnimation]
    _mines_punch: Optional[SpriteAnimation]
    _tower_bullet: Optional[SpriteAnimation]
    _chapel_laugh: Optional[SpriteAnimation]
    _kitchen_prep: Optional[SpriteAnimation]
    _ship_beckon: Optional[SpriteAnimation]
    _ship_chair: Optional[SpriteAnimation]
    _dojo_challenge: Optional[SpriteAnimation]
    _statue_intro: Optional[SpriteAnimation]
    _statue_peck: Optional[SpriteAnimation]
    _statue_flustered: Optional[SpriteAnimation]
    _keep_challenge: Optional[SpriteAnimation]
    _keep_summon: Optional[SpriteAnimation]
    _chandelier_challenge: Optional[SpriteAnimation]
    _factory_pierce: Optional[SpriteAnimation]
    _endgame_challenge: Optional[SpriteAnimation]

    @property
    def recoil(self) -> Optional[SpriteAnimation]:
        return self._recoil

    def set_recoil(self, recoil: Optional[SpriteAnimation] = None) -> None:
        self._recoil = recoil

    @property
    def bandits_way_distracted(self) -> Optional[SpriteAnimation]:
        return self._bandits_way_distracted

    def set_bandits_way_distracted(
        self, bandits_way_distracted: Optional[SpriteAnimation] = None
    ) -> None:
        self._bandits_way_distracted = bandits_way_distracted

    @property
    def mines_punch(self) -> Optional[SpriteAnimation]:
        return self._mines_punch

    def set_mines_punch(self, mines_punch: Optional[SpriteAnimation] = None) -> None:
        self._mines_punch = mines_punch

    @property
    def tower_bullet(self) -> Optional[SpriteAnimation]:
        return self._tower_bullet

    def set_tower_bullet(self, tower_bullet: Optional[SpriteAnimation] = None) -> None:
        self._tower_bullet = tower_bullet

    @property
    def chapel_laugh(self) -> Optional[SpriteAnimation]:
        return self._chapel_laugh

    def set_chapel_laugh(self, chapel_laugh: Optional[SpriteAnimation] = None) -> None:
        self._chapel_laugh = chapel_laugh

    @property
    def kitchen_prep(self) -> Optional[SpriteAnimation]:
        return self._kitchen_prep

    def set_kitchen_prep(self, kitchen_prep: Optional[SpriteAnimation] = None) -> None:
        self._kitchen_prep = kitchen_prep

    @property
    def ship_beckon(self) -> Optional[SpriteAnimation]:
        return self._ship_beckon

    def set_ship_beckon(self, ship_beckon: Optional[SpriteAnimation] = None) -> None:
        self._ship_beckon = ship_beckon

    @property
    def ship_chair(self) -> Optional[SpriteAnimation]:
        return self._ship_chair

    def set_ship_chair(self, ship_chair: Optional[SpriteAnimation] = None) -> None:
        self._ship_chair = ship_chair

    @property
    def dojo_challenge(self) -> Optional[SpriteAnimation]:
        return self._dojo_challenge

    def set_dojo_challenge(
        self, dojo_challenge: Optional[SpriteAnimation] = None
    ) -> None:
        self._dojo_challenge = dojo_challenge

    @property
    def statue_intro(self) -> Optional[SpriteAnimation]:
        return self._statue_intro

    def set_statue_intro(self, statue_intro: Optional[SpriteAnimation] = None) -> None:
        self._statue_intro = statue_intro

    @property
    def statue_peck(self) -> Optional[SpriteAnimation]:
        return self._statue_peck

    def set_statue_peck(self, statue_peck: Optional[SpriteAnimation] = None) -> None:
        self._statue_peck = statue_peck

    @property
    def statue_flustered(self) -> Optional[SpriteAnimation]:
        return self._statue_flustered

    def set_statue_flustered(
        self, statue_flustered: Optional[SpriteAnimation] = None
    ) -> None:
        self._statue_flustered = statue_flustered

    @property
    def keep_challenge(self) -> Optional[SpriteAnimation]:
        return self._keep_challenge

    def set_keep_challenge(
        self, keep_challenge: Optional[SpriteAnimation] = None
    ) -> None:
        self._keep_challenge = keep_challenge

    @property
    def keep_summon(self) -> Optional[SpriteAnimation]:
        return self._keep_summon

    def set_keep_summon(self, keep_summon: Optional[SpriteAnimation] = None) -> None:
        self._keep_summon = keep_summon

    @property
    def chandelier_challenge(self) -> Optional[SpriteAnimation]:
        return self._chandelier_challenge

    def set_chandelier_challenge(
        self, chandelier_challenge: Optional[SpriteAnimation] = None
    ) -> None:
        self._chandelier_challenge = chandelier_challenge

    @property
    def factory_pierce(self) -> Optional[SpriteAnimation]:
        return self._factory_pierce

    def set_factory_pierce(
        self, factory_pierce: Optional[SpriteAnimation] = None
    ) -> None:
        self._factory_pierce = factory_pierce

    @property
    def endgame_challenge(self) -> Optional[SpriteAnimation]:
        return self._endgame_challenge

    def set_endgame_challenge(
        self, endgame_challenge: Optional[SpriteAnimation] = None
    ) -> None:
        self._endgame_challenge = endgame_challenge

    def __init__(
        self,
        recoil: Optional[SpriteAnimation] = None,
        bandits_way_distracted: Optional[SpriteAnimation] = None,
        mines_punch: Optional[SpriteAnimation] = None,
        tower_bullet: Optional[SpriteAnimation] = None,
        chapel_laugh: Optional[SpriteAnimation] = None,
        kitchen_prep: Optional[SpriteAnimation] = None,
        ship_beckon: Optional[SpriteAnimation] = None,
        ship_chair: Optional[SpriteAnimation] = None,
        dojo_challenge: Optional[SpriteAnimation] = None,
        statue_intro: Optional[SpriteAnimation] = None,
        statue_peck: Optional[SpriteAnimation] = None,
        statue_flustered: Optional[SpriteAnimation] = None,
        keep_challenge: Optional[SpriteAnimation] = None,
        keep_summon: Optional[SpriteAnimation] = None,
        chandelier_challenge: Optional[SpriteAnimation] = None,
        factory_pierce: Optional[SpriteAnimation] = None,
        endgame_challenge: Optional[SpriteAnimation] = None,
    ):
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
