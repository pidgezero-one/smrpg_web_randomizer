# Data module for enemy attack data.

from typing import List, Optional
from randomizer.types.enemy_attacks.constants import ENEMY_ATTACK_BASE_ADDRESS
from randomizer.types.spells.enums import SpellBoosts, SpellStatusEffects
from randomizer.logic import utils
from randomizer.types.patch.classes import Patch
from randomizer.types.numbers.classes import UInt4, UInt8
from randomizer.types.world.classes import GameWorld


class EnemyAttack:
    """Class representing an enemy attack."""

    # Default instance attributes.
    _index: int = 0
    _attack_level: int = 0
    _ohko: bool = False
    _damageless_flag_1: bool = False
    _hide_numbers: bool = False
    _damageless_flag_2: bool = False
    _hit_rate: int = 0
    _status_effects: List[SpellStatusEffects] = []
    _buffs: List[SpellBoosts] = []

    _world: Optional[GameWorld]

    @property
    def world(self) -> GameWorld:
        assert self._world is not None
        return self._world

    @property
    def index(self) -> UInt8:
        assert 0 <= self._index <= 128 or self._index == 251
        return UInt8(self._index)

    @property
    def attack_level(self) -> UInt4:
        return UInt4(self._attack_level)

    def set_attack_level(self, attack_level: int) -> None:
        assert 0 <= attack_level <= 7
        self._attack_level = attack_level

    @property
    def ohko(self) -> bool:
        return self._ohko

    def set_ohko(self, ohko: bool) -> None:
        self._ohko = ohko

    @property
    def damageless_flag_1(self) -> bool:
        return self._damageless_flag_1

    def set_damageless_flag_1(self, damageless_flag_1: bool) -> None:
        self._damageless_flag_1 = damageless_flag_1

    @property
    def hide_numbers(self) -> bool:
        return self._hide_numbers

    def set_hide_numbers(self, hide_numbers: bool) -> None:
        self._hide_numbers = hide_numbers

    @property
    def damageless_flag_2(self) -> bool:
        return self._damageless_flag_2

    def set_damageless_flag_2(self, damageless_flag_2: bool) -> None:
        self._damageless_flag_2 = damageless_flag_2

    @property
    def hit_rate(self) -> UInt8:
        return UInt8(self._hit_rate)

    def set_hit_rate(self, hit_rate: int) -> None:
        assert UInt8(hit_rate)
        self._hit_rate = hit_rate

    @property
    def status_effects(self) -> List[SpellStatusEffects]:
        return self._status_effects

    def set_status_effects(self, status_effects: List[SpellStatusEffects]) -> None:
        self._status_effects = status_effects

    @property
    def buffs(self) -> List[SpellBoosts]:
        return self._buffs

    def set_buffs(self, buffs: List[SpellBoosts]) -> None:
        self._buffs = buffs

    def __init__(self, world: Optional[GameWorld] = None):
        self._world = world

    def __str__(self):
        return "<{}>".format(self.name)

    def __repr__(self):
        return str(self)

    @property
    def name(self):
        return self.__class__.__name__

    def get_patch(self) -> Patch:
        """Get patch for this item.

        :return: Patch data.
        :rtype: randomizer.logic.patch.Patch
        """
        patch = Patch()
        base_addr = ENEMY_ATTACK_BASE_ADDRESS + (self.index * 4)

        data = bytearray()

        # First byte is attack level + damage type flags in a bitmap.
        attack_flags = [i for i in range(3) if self.attack_level & (1 << i)]
        if self.ohko:
            attack_flags.append(3)
        if self.damageless_flag_1:
            attack_flags.append(4)
        if self.hide_numbers:
            attack_flags.append(5)
        if self.damageless_flag_2:
            attack_flags.append(6)
        data += utils.BitMapSet(1, attack_flags).as_bytes()

        # Other bytes are hit rate, status effects, and buffs.
        data += utils.ByteField(self.hit_rate).as_bytes()
        data += utils.BitMapSet(1, self.status_effects).as_bytes()
        data += utils.BitMapSet(1, self.buffs).as_bytes()

        patch.add_data(base_addr, data)
        return patch
