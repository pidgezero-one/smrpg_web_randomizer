from copy import deepcopy
from typing import List, Optional, Type, Union
from randomizer.types.monster_scripts.commands import IfHPBelow, IfTargetedByItem

from randomizer.types.world.classes import GameWorld
from randomizer.types.world.flags.flags import NoOHKO

from .constants import (
    BASE_ENEMY_ADDRESS,
    BASE_PSYCHOPATH_DATA_ADDRESS,
    BASE_PSYCHOPATH_POINTER_ADDRESS,
    BASE_REWARD_ADDRESS,
    FLOWER_BONUS_BASE_ADDRESS,
    NAME_BASE_ADDRESS,
    PSYCHOPATH_DATA_POINTER_OFFSET,
    TOTAL_ENEMIES,
)
from .enums import ApproachSound, HitSound, FlowerBonusType

from randomizer.types.items.enums import ItemStatusEffect, EquipElement
from randomizer.types.numbers.classes import UInt16, UInt8
from randomizer.types.items.classes import RegularItem
from randomizer.entities.items.items import BrightCard, Mushroom
from randomizer.logic import flags, utils
from randomizer.types.patch.classes import Patch


class Enemy:
    """Class representing an enemy in the game."""

    _world: Optional[GameWorld]

    @property
    def world(self) -> GameWorld:
        assert self._world is not None
        return self._world

    ### properties in lazy shell

    _monster_id: int = 0

    # vital status
    _hp: int = 0
    _fp: int = 0
    _attack: int = 0
    _defense: int = 0
    _magic_attack: int = 0
    _magic_defense: int = 0
    _speed: int = 0
    _evade: int = 0
    _magic_evade: int = 0

    # effect nullification
    _status_immunities: List[ItemStatusEffect] = []

    # element weaknesses
    _weaknesses: List[EquipElement] = []

    # element resistances
    _resistances: List[EquipElement] = []

    # rewards
    _xp: int = 0
    _coins: int = 0
    _rare_item_drop: Optional[Type[RegularItem]] = None
    _common_item_drop: Optional[Type[RegularItem]] = None
    _yoshi_cookie_item: Type[RegularItem] = Mushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.NONE
    _flower_bonus_chance: int = 0

    # other properties
    _morph_chance: float = 0
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE

    # special status
    _invincible: bool = False
    _ohko_immune: bool = False

    ### properties not set in lazy shell

    # misc
    _boss: bool
    _palette: int
    _flying: bool
    _high_flying: bool
    _one_per_battle: bool  # Flag if enemy is unique per battle (only 1 max per formation)

    # boss shuffle attributes
    _anchor: bool
    _ratio_hp: float = 1.0
    _ratio_fp: float = 1.0
    _ratio_attack: float = 1.0
    _ratio_defense: float = 1.0
    _ratio_magic_attack: float = 1.0
    _ratio_magic_defense: float = 1.0
    _ratio_speed: float = 1.0
    _ratio_evade: float = 1.0
    _ratio_magic_evade: float = 1.0
    _name_override: str

    # overworld subs
    _sprite: Union[None, int] = None

    ### attribute methods

    @property
    def monster_id(self) -> UInt8:
        return UInt8(self._monster_id)

    @property
    def hp(self) -> UInt16:
        return UInt16(self._hp)

    def set_hp(self, hp: int) -> None:
        assert UInt16(hp)
        self._hp = hp

    @property
    def fp(self) -> UInt8:
        return UInt8(self._fp)

    def set_fp(self, fp: int) -> None:
        assert UInt8(fp)
        self._fp = fp

    @property
    def attack(self) -> UInt8:
        return UInt8(self._attack)

    def set_attack(self, attack: int) -> None:
        assert UInt8(attack)
        self._attack = attack

    @property
    def defense(self) -> UInt8:
        return UInt8(self._defense)

    def set_defense(self, defense: int) -> None:
        assert UInt8(defense)
        self._defense = defense

    @property
    def magic_attack(self) -> UInt8:
        return UInt8(self._magic_attack)

    def set_magic_attack(self, magic_attack: int) -> None:
        assert UInt8(magic_attack)
        self._magic_attack = magic_attack

    @property
    def magic_defense(self) -> UInt8:
        return UInt8(self._magic_defense)

    def set_magic_defense(self, magic_defense: int) -> None:
        assert UInt8(magic_defense)
        self._magic_defense = magic_defense

    @property
    def speed(self) -> UInt8:
        return UInt8(self._speed)

    def set_speed(self, speed: int) -> None:
        assert UInt8(speed)
        self._speed = speed

    @property
    def evade(self) -> UInt8:
        return UInt8(self._evade)

    def set_evade(self, evade: int) -> None:
        assert 0 <= evade <= 100
        self._evade = evade

    @property
    def magic_evade(self) -> UInt8:
        return UInt8(self._magic_evade)

    def set_magic_evade(self, magic_evade: int) -> None:
        assert 0 <= magic_evade <= 100
        self._magic_evade = magic_evade

    @property
    def status_immunities(self) -> List[ItemStatusEffect]:
        return deepcopy(self._status_immunities)

    def set_status_immunities(self, status_immunities: List[ItemStatusEffect]) -> None:
        self._status_immunities = deepcopy(status_immunities)

    def append_status_immunity(self, immunity: ItemStatusEffect) -> None:
        if immunity not in self._status_immunities:
            self._status_immunities.append(immunity)

    def remove_status_immunity(self, immunity: ItemStatusEffect) -> None:
        if immunity in self._status_immunities:
            self._status_immunities.remove(immunity)

    @property
    def weaknesses(self) -> List[EquipElement]:
        return deepcopy(self._weaknesses)

    def set_weaknesses(self, weaknesses: List[EquipElement]) -> None:
        self._weaknesses = deepcopy(weaknesses)

    def append_weakness(self, element: EquipElement) -> None:
        if element not in self._weaknesses:
            self._weaknesses.append(element)

    def remove_weakness(self, element: EquipElement) -> None:
        if element in self._weaknesses:
            self._weaknesses.remove(element)

    @property
    def resistances(self) -> List[EquipElement]:
        return deepcopy(self._resistances)

    def set_resistances(self, resistances: List[EquipElement]) -> None:
        self._resistances = deepcopy(resistances)

    def append_resistance(self, element: EquipElement) -> None:
        if element not in self._resistances:
            self._resistances.append(element)

    def remove_resistance(self, element: EquipElement) -> None:
        if element in self._resistances:
            self._resistances.remove(element)

    @property
    def xp(self) -> UInt16:
        return UInt16(self._xp)

    def set_xp(self, xp: int) -> None:
        assert 0 <= xp <= 9999
        self._xp = xp

    @property
    def coins(self) -> UInt8:
        return UInt8(self._coins)

    def set_coins(self, coins: int) -> None:
        assert UInt8(coins)
        self._coins = coins

    @property
    def rare_item_drop(self) -> Optional[Type[RegularItem]]:
        return self._rare_item_drop

    def set_rare_item_drop(self, rare_item_drop: Optional[Type[RegularItem]]) -> None:
        self._rare_item_drop = rare_item_drop

    @property
    def common_item_drop(self) -> Optional[Type[RegularItem]]:
        return self._common_item_drop

    def set_common_item_drop(self, common_item_drop: Type[RegularItem]) -> None:
        self._common_item_drop = common_item_drop

    @property
    def yoshi_cookie_item(self) -> Type[RegularItem]:
        return self._yoshi_cookie_item

    def set_yoshi_cookie_item(self, yoshi_cookie_item: Type[RegularItem]) -> None:
        self._yoshi_cookie_item = yoshi_cookie_item

    @property
    def flower_bonus_type(self) -> FlowerBonusType:
        return self._flower_bonus_type

    def set_flower_bonus_type(self, flower_bonus_type: FlowerBonusType) -> None:
        self._flower_bonus_type = flower_bonus_type

    @property
    def flower_bonus_chance(self) -> UInt8:
        return UInt8(self._flower_bonus_chance)

    def set_flower_bonus_chance(self, flower_bonus_chance: int) -> None:
        assert 0 <= flower_bonus_chance <= 100 and flower_bonus_chance % 10 == 0
        self._flower_bonus_chance = flower_bonus_chance

    @property
    def morph_chance(self) -> float:
        return self._morph_chance

    def set_morph_chance(self, morph_chance: float) -> None:
        self._morph_chance = morph_chance

    @property
    def sound_on_hit(self) -> HitSound:
        return self._sound_on_hit

    def set_sound_on_hit(self, sound_on_hit: HitSound) -> None:
        self._sound_on_hit = sound_on_hit

    @property
    def sound_on_approach(self) -> ApproachSound:
        return self._sound_on_approach

    def set_sound_on_approach(self, sound_on_approach: ApproachSound) -> None:
        self._sound_on_approach = sound_on_approach

    @property
    def invincible(self) -> bool:
        return self._invincible

    def set_invincible(self, invincible: bool) -> None:
        self._invincible = invincible

    @property
    def ohko_immune(self) -> bool:
        return self._ohko_immune

    def set_ohko_immune(self, ohko_immune: bool) -> None:
        self._ohko_immune = ohko_immune

    @property
    def boss(self) -> bool:
        return self._boss

    def set_boss(self, boss: bool) -> None:
        self._boss = boss

    @property
    def address(self):
        return BASE_ENEMY_ADDRESS + self.monster_id * 16

    @property
    def reward_address(self):
        return BASE_REWARD_ADDRESS + self.monster_id * 6

    @property
    def palette(self) -> int:
        return self._palette

    def set_palette(self, palette: int) -> None:
        self._palette = palette

    @property
    def flying(self) -> bool:
        return self._flying

    def set_flying(self, flying: bool) -> None:
        self._flying = flying

    @property
    def high_flying(self) -> bool:
        return self._high_flying

    def set_high_flying(self, high_flying: bool) -> None:
        self._high_flying = high_flying

    @property
    def one_per_battle(self) -> bool:
        return self._one_per_battle

    def set_one_per_battle(self, one_per_battle: bool) -> None:
        self._one_per_battle = one_per_battle

    @property
    def anchor(self) -> bool:
        return self._anchor

    def set_anchor(self, anchor: bool) -> None:
        self._anchor = anchor

    @property
    def ratio_hp(self) -> float:
        return self._ratio_hp

    def set_ratio_hp(self, ratio_hp: float) -> None:
        self._ratio_hp = ratio_hp

    @property
    def ratio_fp(self) -> float:
        return self._ratio_fp

    def set_ratio_fp(self, ratio_fp: float) -> None:
        self._ratio_fp = ratio_fp

    @property
    def ratio_attack(self) -> float:
        return self._ratio_attack

    def set_ratio_attack(self, ratio_attack: float) -> None:
        self._ratio_attack = ratio_attack

    @property
    def ratio_defense(self) -> float:
        return self._ratio_defense

    def set_ratio_defense(self, ratio_defense: float) -> None:
        self._ratio_defense = ratio_defense

    @property
    def ratio_magic_attack(self) -> float:
        return self._ratio_magic_attack

    def set_ratio_magic_attack(self, ratio_magic_attack: float) -> None:
        self._ratio_magic_attack = ratio_magic_attack

    @property
    def ratio_magic_defense(self) -> float:
        return self._ratio_magic_defense

    def set_ratio_magic_defense(self, ratio_magic_defense: float) -> None:
        self._ratio_magic_defense = ratio_magic_defense

    @property
    def ratio_speed(self) -> float:
        return self._ratio_speed

    def set_ratio_speed(self, ratio_speed: float) -> None:
        self._ratio_speed = ratio_speed

    @property
    def ratio_evade(self) -> float:
        return self._ratio_evade

    def set_ratio_evade(self, ratio_evade: float) -> None:
        self._ratio_evade = ratio_evade

    @property
    def ratio_magic_evade(self) -> float:
        return self._ratio_magic_evade

    def set_ratio_magic_evade(self, ratio_magic_evade: float) -> None:
        self._ratio_magic_evade = ratio_magic_evade

    @property
    def name_override(self) -> str:
        if self._name_override == "":
            return self.name
        return self._name_override

    def set_name_override(self, name_override: str) -> None:
        self._name_override = name_override

    @property
    def sprite(self) -> "Union[None, UInt16]":
        return UInt16(self._sprite)

    def set_sprite(self, sprite: "Union[None, int]") -> None:
        if sprite is not None:
            assert 0 <= sprite <= 1023
            assert UInt16(sprite)
        self._sprite = sprite

    def __init__(self, world: Optional[GameWorld] = None):
        self._world = world

    def __str__(self):
        return "<{} hp: {} attack: {} defense: {} m.attack: {} m.defense: {}>".format(
            self.name,
            self.hp,
            self.attack,
            self.defense,
            self.magic_attack,
            self.magic_defense,
        )

    def __repr__(self):
        return str(self)

    @property
    def name(self):
        return self.__class__.__name__

    @staticmethod
    def round_for_battle_script(val):
        """Round a HP value for battle event data.  This means round to an integer, and make sure it does have the
        values 0xfe or 0xff because these are special values that stop processing the battle script.

        Args:
            val (float|int): Base value to confirm.

        Returns:
            int: Rounded HP value.

        """
        ret = int(round(val))
        m = ret % 256

        # 0xfe
        if m == 254:
            ret += 2
        # 0xff
        elif m == 255:
            ret += 1

        # If starting value was positive, final value must be at least 1 since zero is a death trigger that ends battle.
        if val > 0:
            return max(1, ret)
        else:
            return ret

    @classmethod
    def get_world_instance(cls, world):
        """

        Args:
            world (randomizer.logic.main.GameWorld): World to get instance of this enemy class for.

        Returns:
            Enemy: Instance of the enemy for this world.

        """
        return world.enemies_dict[cls.monster_id]

    @property
    def rank(self):
        """Calculate rough difficulty ranking of enemy based on HP and attack stats.

        :rtype: int
        """
        hp = self.hp if self.hp >= 10 else 100
        return hp * max(self.attack, self.magic_attack, 1)

    @property
    def psychopath_text(self):
        """Make Psychopath text to show elemental weaknesses and immunities.

        :rtype: str
        """
        desc = ""

        elemental_immunities = ""
        elemental_weaknesses = ""
        status_vulnerabilities = ""

        # Elemental immunities.
        if self.resistances:
            elemental_immunities += "\x7C"
            elemental_immunities += utils.add_desc_fields(
                (
                    ("\x7E", 6, self.resistances),
                    ("\x7D", 4, self.resistances),
                    ("\x7F", 5, self.resistances),
                    ("\x85", 7, self.resistances),
                )
            )

        # Elemental weaknesses.
        if self.weaknesses:
            elemental_weaknesses += "\x7B"
            elemental_weaknesses += utils.add_desc_fields(
                (
                    ("\x7E", 6, self.weaknesses),
                    ("\x7D", 4, self.weaknesses),
                    ("\x7F", 5, self.weaknesses),
                    ("\x85", 7, self.weaknesses),
                )
            )

        # Status vulnerabilities.
        vulnerabilities = [i for i in range(4) if i not in self.status_immunities]
        if vulnerabilities:
            status_vulnerabilities += utils.add_desc_fields(
                (
                    ("\x82", 0, vulnerabilities),
                    ("\x80", 1, vulnerabilities),
                    ("\x83", 2, vulnerabilities),
                    ("\x81", 3, vulnerabilities),
                    ("\x84\x84", True, not self.ohko_immune),
                )
            )

        eligible = [
            s
            for s in [
                status_vulnerabilities,
                elemental_weaknesses,
                elemental_immunities,
            ]
            if s != ""
        ]
        if len(eligible) == 0:
            desc = "No weaknesses or resistances.\x02"
        else:
            desc = "  \x2A  ".join(eligible) + "\x02"

        return desc

    def get_similar(self):
        """Get a similar enemy to this one for formation shuffling based on rank.

        :rtype: Enemy
        """
        # If we're a boss enemy, treat as unique.
        if self.boss:
            return self

        # Get all non-boss candidates sorted by rank.
        candidates = [e for e in self.world.enemies if not e.boss]
        candidates = sorted(candidates, key=lambda e: (e.rank, e.monster_id))

        # If this is a special enemy, don't replace it.
        if self.rank < 0:
            return self
        elif self not in candidates:
            return self

        # Sort by rank and mutate our position within the list to get a replacement enemy.
        index = candidates.index(self)
        index = utils.mutate_normal(index, maximum=len(candidates) - 1)
        return candidates[index]

    def update_world_entities(self):
        pass

    def get_patch(self):
        """Get patch for this enemy.

        Returns:
            randomizer.logic.patch.Patch: Patch data

        """
        patch = Patch()

        # Main stats.
        data = bytearray()
        data += utils.ByteField(self.hp, num_bytes=2).as_bytes()
        data += utils.ByteField(self.speed).as_bytes()
        data += utils.ByteField(self.attack).as_bytes()
        data += utils.ByteField(self.defense).as_bytes()
        data += utils.ByteField(self.magic_attack).as_bytes()
        data += utils.ByteField(self.magic_defense).as_bytes()
        data += utils.ByteField(self.fp).as_bytes()
        data += utils.ByteField(self.evade).as_bytes()
        data += utils.ByteField(self.magic_evade).as_bytes()
        patch.add_data(self.address, data)

        # Special defense bits, sound on hit is top half.
        data = bytearray()
        hit_special_defense = 1 if self.invincible else 0
        hit_special_defense |= (1 if self.ohko_immune else 0) << 1
        morph_chance: int = 0
        if self.morph_chance == 0.25:
            morph_chance = 1
        elif self.morph_chance == 0.75:
            morph_chance = 2
        if self.morph_chance == 1.0:
            morph_chance = 3
        hit_special_defense |= morph_chance << 2
        hit_special_defense |= self.sound_on_hit << 4
        data.append(hit_special_defense)

        # Elemental resistances.
        data += utils.BitMapSet(1, self.resistances).as_bytes()

        # Elemental weaknesses byte (top half), sound on approach is bottom half.
        weaknesses_approach = self.sound_on_approach
        for weakness in self.weaknesses:
            weaknesses_approach |= 1 << weakness
        data.append(weaknesses_approach)

        # Status immunities.
        data += utils.BitMapSet(1, self.status_immunities).as_bytes()

        patch.add_data(self.address + 11, data)

        # Flower bonus.
        bonus_addr = FLOWER_BONUS_BASE_ADDRESS + self.monster_id
        bonus = (self.flower_bonus_chance // 10) << 4
        bonus |= self.flower_bonus_type
        patch.add_data(bonus_addr, utils.ByteField(bonus).as_bytes())

        yoshi_cookie_item = self.world.get_item_instance(self.yoshi_cookie_item).item_id
        common_item = 0xFF
        if self.common_item_drop is not None:
            common_item = self.world.get_item_instance(self.common_item_drop).item_id
        rare_item = 0xFF
        if self.rare_item_drop is not None:
            rare_item = self.world.get_item_instance(self.rare_item_drop).item_id

        # Build reward data patch.
        data = bytearray()
        data += utils.ByteField(self.xp, num_bytes=2).as_bytes()
        data += utils.ByteField(self.coins).as_bytes()
        data += utils.ByteField(yoshi_cookie_item).as_bytes()
        data += utils.ByteField(common_item).as_bytes()
        data += utils.ByteField(rare_item).as_bytes()
        patch.add_data(self.reward_address, data)

        # If we have an override name, add to the patch data.
        if self.name_override:
            addr = NAME_BASE_ADDRESS + (self.monster_id * 13)
            patch.add_data(addr, self.name_override.upper().encode().ljust(13, b"\x20"))

        return patch

    @classmethod
    def build_psychopath_patch(cls, world):
        """Build patch data for Psychopath text.  These use pointers, so we need to do them all together.

        :type world: randomizer.logic.main.GameWorld
        :return: Patch data.
        :rtype: randomizer.logic.patch.Patch
        """
        patch = Patch()

        # Begin text data with a single null byte to use for all empty text to save space.
        pointer_data = bytearray()
        text_data = bytearray()
        text_data.append(0x00)

        # Make list of blank text for all enemies, and get text for each valid enemy we have based on index.
        descriptions = [""] * TOTAL_ENEMIES
        for enemy in world.enemies:
            descriptions[enemy.monster_id] = enemy.psychopath_text

        # Now build the actual pointer data.
        for desc in descriptions:
            # If the description is empty, just use the null byte at the very beginning.
            if not desc:
                pointer = BASE_PSYCHOPATH_DATA_ADDRESS - PSYCHOPATH_DATA_POINTER_OFFSET
                pointer_data += utils.ByteField(pointer, num_bytes=2).as_bytes()
                continue

            # Compute pointer from base address and current data length.
            pointer = (
                BASE_PSYCHOPATH_DATA_ADDRESS
                + len(text_data)
                - PSYCHOPATH_DATA_POINTER_OFFSET
            )
            pointer_data += utils.ByteField(pointer, num_bytes=2).as_bytes()

            # Add null byte to terminate the text string.
            desc = desc.encode("latin1")
            desc += bytes([0x00])
            text_data += desc

        # Sanity check that pointer data has the correct number of items.
        if len(pointer_data) != TOTAL_ENEMIES * 2:
            raise ValueError("Wrong length for pointer data, something went wrong...")
        # Sanity check that data doesn't overflow into battlefield tilesets.
        if len(text_data) > 5235:
            raise ValueError(
                "Psychopath text too long (got %i, want <= %i)" % (len(text_data), 5235)
            )

        # Add pointer data, then add text data.
        patch.add_data(BASE_PSYCHOPATH_POINTER_ADDRESS, pointer_data)
        patch.add_data(BASE_PSYCHOPATH_DATA_ADDRESS, text_data)

        return patch


class Henchman(Enemy):
    pass


class AllyClone(Henchman):
    def patch_script(self):

        if self.world.settings.is_boolean_flag_enabled(NoOHKO):
            battlescript = self.world.monster_scripts.scripts[self.monster_id]
            for command in battlescript.contents:
                if isinstance(command, IfTargetedByItem):
                    # Good luck using that in battle
                    command.set_commands([BrightCard])


class ShellySupport(Enemy):
    _position: int = 0
    _vanilla: bool = False
    _summons: List[int] = []
    _summon_event: Union[int, None] = None
    _sprite_sub: bool = False
    _formation_id: Union[int, None] = 0

    @property
    def position(self) -> int:
        return self._position

    def set_position(self, position: int) -> None:
        self._position = position

    @property
    def vanilla(self) -> bool:
        return self._vanilla

    def set_vanilla(self, vanilla: bool) -> None:
        self._vanilla = vanilla

    @property
    def summons(self) -> List[int]:
        return self._summons

    def set_summons(self, summons: List[int]) -> None:
        self._summons = summons

    @property
    def summon_event(self) -> Union[int, None]:
        return self._summon_event

    def set_summon_event(self, summon_event: Union[int, None]) -> None:
        self._summon_event = summon_event

    @property
    def sprite_sub(self) -> bool:
        return self._sprite_sub

    def set_sprite_sub(self, sprite_sub: bool) -> None:
        self._sprite_sub = sprite_sub

    @property
    def formation_id(self) -> Union[UInt8, None]:
        if self._formation_id is not None:
            return UInt8(self._formation_id)
        return self._formation_id

    def set_formation_id(self, formation_id: Union[int, None]) -> None:
        if formation_id is not None:
            assert UInt8(formation_id)
        self._formation_id = formation_id
