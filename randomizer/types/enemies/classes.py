"""Base classes for enemies encountered in battle and their overworld representations."""

from copy import deepcopy
from typing import List, Optional, Type, Union
from randomizer.types.monster_scripts.commands import IfTargetedByItem

from randomizer.types.world.classes import GameWorld
from randomizer.types.world.flags.flags import NoOHKO

from randomizer.types.enemies.constants import (
    BASE_ENEMY_ADDRESS,
    BASE_PSYCHOPATH_DATA_ADDRESS,
    BASE_PSYCHOPATH_POINTER_ADDRESS,
    BASE_REWARD_ADDRESS,
    FLOWER_BONUS_BASE_ADDRESS,
    NAME_BASE_ADDRESS,
    PSYCHOPATH_DATA_POINTER_OFFSET,
    TOTAL_ENEMIES,
)
from randomizer.types.enemies.enums import ApproachSound, HitSound, FlowerBonusType

from randomizer.types.spells.enums import Status, Element
from randomizer.types.numbers.classes import BitMapSet, ByteField, UInt16, UInt8
from randomizer.types.items.classes import RegularItem
from randomizer.entities.items.items import BrightCard, Mushroom
from randomizer.types.patch.classes import Patch
from randomizer.utils.number import mutate_normal


class Enemy:
    """Class representing an enemy in the game."""

    _world: Optional[GameWorld]

    @property
    def world(self) -> GameWorld:
        """World instance reference"""
        assert self._world is not None
        return self._world

    # properties in lazy shell

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
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

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

    # properties not set in lazy shell

    # misc
    _boss: bool
    _palette: int
    _flying: bool
    _high_flying: bool
    # Flag if enemy is unique per battle (only 1 max per formation)
    _one_per_battle: bool

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

    # attribute methods

    @property
    def monster_id(self) -> UInt8:
        """Enemy's unique index."""
        return UInt8(self._monster_id)

    @property
    def hp(self) -> UInt16:
        """The enemy's HP at the start of the fight."""
        return UInt16(self._hp)

    def set_hp(self, hp: int) -> None:
        """Set how much HP the enemy will have at the start of the fight."""
        assert UInt16(hp)
        self._hp = hp

    @property
    def fp(self) -> UInt8:
        """The enemy's FP at the start of the fight."""
        return UInt8(self._fp)

    def set_fp(self, fp: int) -> None:
        """Set how much FP the enemy will have at the start of the fight."""
        assert UInt8(fp)
        self._fp = fp

    @property
    def attack(self) -> UInt8:
        """The enemy's base physical attack power."""
        return UInt8(self._attack)

    def set_attack(self, attack: int) -> None:
        """Set the enemy's base physical attack power."""
        assert UInt8(attack)
        self._attack = attack

    @property
    def defense(self) -> UInt8:
        """The enemy's base physical defense power."""
        return UInt8(self._defense)

    def set_defense(self, defense: int) -> None:
        """Set the enemy's base physical defense power."""
        assert UInt8(defense)
        self._defense = defense

    @property
    def magic_attack(self) -> UInt8:
        """The enemy's base magic attack power."""
        return UInt8(self._magic_attack)

    def set_magic_attack(self, magic_attack: int) -> None:
        """Set the enemy's base magic attack power."""
        assert UInt8(magic_attack)
        self._magic_attack = magic_attack

    @property
    def magic_defense(self) -> UInt8:
        """The enemy's base magic defense power."""
        return UInt8(self._magic_defense)

    def set_magic_defense(self, magic_defense: int) -> None:
        """Set the enemy's base magic defense power."""
        assert UInt8(magic_defense)
        self._magic_defense = magic_defense

    @property
    def speed(self) -> UInt8:
        """The enemy's speed."""
        return UInt8(self._speed)

    def set_speed(self, speed: int) -> None:
        """Set the enemy's speed."""
        assert UInt8(speed)
        self._speed = speed

    @property
    def evade(self) -> UInt8:
        """The enemy's percent likelihood of evading a physical attack."""
        return UInt8(self._evade)

    def set_evade(self, evade: int) -> None:
        """Set the enemy's percent likelihood of evading a physical attack."""
        assert 0 <= evade <= 100
        self._evade = evade

    @property
    def magic_evade(self) -> UInt8:
        """The enemy's percent likelihood of evading a magic attack."""
        return UInt8(self._magic_evade)

    def set_magic_evade(self, magic_evade: int) -> None:
        """Set the enemy's percent likelihood of evading a magic attack."""
        assert 0 <= magic_evade <= 100
        self._magic_evade = magic_evade

    @property
    def status_immunities(self) -> List[Status]:
        """The list of status effects that the enemy is unaffected by."""
        return deepcopy(self._status_immunities)

    def set_status_immunities(self, status_immunities: List[Status]) -> None:
        """Overwrite the list of status effects that the enemy is unaffected by."""
        self._status_immunities = deepcopy(status_immunities)

    def append_status_immunity(self, immunity: Status) -> None:
        """Add a status effect that the enemy should be unaffected by."""
        if immunity not in self._status_immunities:
            self._status_immunities.append(immunity)

    def remove_status_immunity(self, immunity: Status) -> None:
        """Remove a status effect from the list that the enemy should be unaffected by."""
        if immunity in self._status_immunities:
            self._status_immunities.remove(immunity)

    @property
    def weaknesses(self) -> List[Element]:
        """The list of elements that cause double damage to the enemy."""
        return deepcopy(self._weaknesses)

    def set_weaknesses(self, weaknesses: List[Element]) -> None:
        """Overwrite the list of elements that cause double damage to the enemy."""
        self._weaknesses = deepcopy(weaknesses)

    def append_weakness(self, element: Element) -> None:
        """Add an element that should cause double damage to the enemy."""
        if element not in self._weaknesses:
            self._weaknesses.append(element)

    def remove_weakness(self, element: Element) -> None:
        """Remove an element from the list that should cause double damage to the enemy."""
        if element in self._weaknesses:
            self._weaknesses.remove(element)

    @property
    def resistances(self) -> List[Element]:
        """The list of elements which will have their damage to the enemy reduced by 50%."""
        return deepcopy(self._resistances)

    def set_resistances(self, resistances: List[Element]) -> None:
        """Overwrite the list of elements which will have their damage to the enemy reduced
        by 50%."""
        self._resistances = deepcopy(resistances)

    def append_resistance(self, element: Element) -> None:
        """Add an element which will have their damage to the enemy reduced by 50%."""
        if element not in self._resistances:
            self._resistances.append(element)

    def remove_resistance(self, element: Element) -> None:
        """Remove an element from the list that will have their damage to the enemy
        reduced by 50%."""
        if element in self._resistances:
            self._resistances.remove(element)

    @property
    def xp(self) -> UInt16:
        """The amount of EXP awarded by the enemy. This number is divided by the number of
        active party members you have at the start of the battle."""
        return UInt16(self._xp)

    def set_xp(self, xp: int) -> None:
        """Set the amount of EXP awarded by the enemy. This number is divided by the number of
        active party members you have at the start of the battle."""
        assert 0 <= xp <= 9999
        self._xp = xp

    @property
    def coins(self) -> UInt8:
        """The amount of coins rewarded by the enemy."""
        return UInt8(self._coins)

    def set_coins(self, coins: int) -> None:
        """Set the amount of coins rewarded by the enemy."""
        assert UInt8(coins)
        self._coins = coins

    @property
    def rare_item_drop(self) -> Optional[Type[RegularItem]]:
        """A single item that the enemy has a very small chance of dropping."""
        return self._rare_item_drop

    def set_rare_item_drop(self, rare_item_drop: Optional[Type[RegularItem]]) -> None:
        """Set the single item that the enemy has a very small chance of dropping."""
        self._rare_item_drop = rare_item_drop

    @property
    def common_item_drop(self) -> Optional[Type[RegularItem]]:
        """A single item that the enemy has a high chance of dropping."""
        return self._common_item_drop

    def set_common_item_drop(self, common_item_drop: Type[RegularItem]) -> None:
        """Set the single item that the enemy has a high chance of dropping."""
        self._common_item_drop = common_item_drop

    @property
    def yoshi_cookie_item(self) -> Type[RegularItem]:
        """The item to be granted if a Yoshi Cookie on this enemy is successful."""
        return self._yoshi_cookie_item

    def set_yoshi_cookie_item(self, yoshi_cookie_item: Type[RegularItem]) -> None:
        """Set the item to be granted if a Yoshi Cookie on this enemy is successful."""
        self._yoshi_cookie_item = yoshi_cookie_item

    @property
    def flower_bonus_type(self) -> FlowerBonusType:
        """The bonus flower that is granted by defeating this enemy."""
        return self._flower_bonus_type

    def set_flower_bonus_type(self, flower_bonus_type: FlowerBonusType) -> None:
        """Set the bonus flower that is granted by defeating this enemy."""
        self._flower_bonus_type = flower_bonus_type

    @property
    def flower_bonus_chance(self) -> UInt8:
        """The percent likelihood of this enemy granting a bonus flower."""
        return UInt8(self._flower_bonus_chance)

    def set_flower_bonus_chance(self, flower_bonus_chance: int) -> None:
        """Set the percent likelihood of this enemy granting a bonus flower."""
        assert 0 <= flower_bonus_chance <= 100 and flower_bonus_chance % 10 == 0
        self._flower_bonus_chance = flower_bonus_chance

    @property
    def morph_chance(self) -> float:
        """The percent success rate that the enemy is affected by a Yoshi Cookie, Lamb's Lure,
        or Sheep Attack. Valid values are 0, 25, 75, or 100."""
        return self._morph_chance

    def set_morph_chance(self, morph_chance: float) -> None:
        """Set the percent success rate that the enemy is affected by a Yoshi Cookie, Lamb's Lure,
        or Sheep Attack. Valid values are 0, 25, 75, or 100."""
        assert morph_chance in [0, 25, 75, 100]
        self._morph_chance = morph_chance

    @property
    def sound_on_hit(self) -> HitSound:
        """The sound the enemy should make when it attacks you."""
        return self._sound_on_hit

    def set_sound_on_hit(self, sound_on_hit: HitSound) -> None:
        """Set the sound the enemy should make when it attacks you."""
        self._sound_on_hit = sound_on_hit

    @property
    def sound_on_approach(self) -> ApproachSound:
        """The sound the enemy should make when it approaches you."""
        return self._sound_on_approach

    def set_sound_on_approach(self, sound_on_approach: ApproachSound) -> None:
        """Set the sound the enemy should make when it approaches you."""
        self._sound_on_approach = sound_on_approach

    @property
    def invincible(self) -> bool:
        """If true, damage taken will not reduce the enemy's HP."""
        return self._invincible

    def set_invincible(self, invincible: bool) -> None:
        """If true, damage taken will not reduce the enemy's HP."""
        self._invincible = invincible

    @property
    def ohko_immune(self) -> bool:
        """If true, the enemy is immune to a timed Geno Whirl."""
        return self._ohko_immune

    def set_ohko_immune(self, ohko_immune: bool) -> None:
        """If true, the enemy is immune to a timed Geno Whirl."""
        self._ohko_immune = ohko_immune

    @property
    def boss(self) -> bool:
        """If true, this enemy is considered a boss."""
        return self._boss

    def set_boss(self, boss: bool) -> None:
        """If true, this enemy is considered a boss."""
        self._boss = boss

    @property
    def address(self):
        """The ROM address at which to begin writing properties to for this enemy."""
        return BASE_ENEMY_ADDRESS + self.monster_id * 16

    @property
    def reward_address(self):
        """The ROM address at which to begin writing reward/drop properties to for this enemy."""
        return BASE_REWARD_ADDRESS + self.monster_id * 6

    @property
    def palette(self) -> int:
        """The palette used by this enemy."""
        return self._palette

    def set_palette(self, palette: int) -> None:
        """Set the palette used by this enemy."""
        self._palette = palette

    @property
    def flying(self) -> bool:
        """If true, the enemy floats off the ground at a medium height and casts a shadow."""
        return self._flying

    def set_flying(self, flying: bool) -> None:
        """If true, the enemy floats off the ground at a medium height and casts a shadow."""
        self._flying = flying

    @property
    def high_flying(self) -> bool:
        """If true, the enemy floats off the ground at a high height and casts a shadow."""
        return self._high_flying

    def set_high_flying(self, high_flying: bool) -> None:
        """If true, the enemy floats off the ground at a high height and casts a shadow."""
        self._high_flying = high_flying

    @property
    def one_per_battle(self) -> bool:
        """If true, this enemy can only appear once in a formation."""
        return self._one_per_battle

    def set_one_per_battle(self, one_per_battle: bool) -> None:
        """If true, this enemy can only appear once in a formation."""
        self._one_per_battle = one_per_battle

    @property
    def anchor(self) -> bool:
        """(deprecated)"""
        return self._anchor

    def set_anchor(self, anchor: bool) -> None:
        """(deprecated)"""
        self._anchor = anchor

    @property
    def ratio_hp(self) -> float:
        """The percentage of a boss fight location's total HP stat that determines this
        enemy's HP."""
        return self._ratio_hp

    def set_ratio_hp(self, ratio_hp: float) -> None:
        """Set the percentage of a boss fight location's total HP stat that determines this
        enemy's HP."""
        self._ratio_hp = ratio_hp

    @property
    def ratio_fp(self) -> float:
        """(deprecated)"""
        return self._ratio_fp

    def set_ratio_fp(self, ratio_fp: float) -> None:
        """(deprecated)"""
        self._ratio_fp = ratio_fp

    @property
    def ratio_attack(self) -> float:
        """The percentage of a boss fight location's average attack stat that determines this
        enemy's HP."""
        return self._ratio_attack

    def set_ratio_attack(self, ratio_attack: float) -> None:
        """Set the percentage of a boss fight location's average attack stat that determines this
        enemy's HP."""
        self._ratio_attack = ratio_attack

    @property
    def ratio_defense(self) -> float:
        """The percentage of a boss fight location's average defense stat that determines this
        enemy's HP."""
        return self._ratio_defense

    def set_ratio_defense(self, ratio_defense: float) -> None:
        """Set the percentage of a boss fight location's average defense stat that determines this
        enemy's HP."""
        self._ratio_defense = ratio_defense

    @property
    def ratio_magic_attack(self) -> float:
        """The percentage of a boss fight location's average magic attack stat
        that determines this enemy's HP."""
        return self._ratio_magic_attack

    def set_ratio_magic_attack(self, ratio_magic_attack: float) -> None:
        """Set the percentage of a boss fight location's average magic attack stat
        that determines this enemy's HP."""
        self._ratio_magic_attack = ratio_magic_attack

    @property
    def ratio_magic_defense(self) -> float:
        """The percentage of a boss fight location's average magic defense stat
        that determines this enemy's HP."""
        return self._ratio_magic_defense

    def set_ratio_magic_defense(self, ratio_magic_defense: float) -> None:
        """Set the percentage of a boss fight location's average magic defense stat
        that determines this enemy's HP."""
        self._ratio_magic_defense = ratio_magic_defense

    @property
    def ratio_speed(self) -> float:
        """(deprecated)"""
        return self._ratio_speed

    def set_ratio_speed(self, ratio_speed: float) -> None:
        """(deprecated)"""
        self._ratio_speed = ratio_speed

    @property
    def ratio_evade(self) -> float:
        """(unknown)"""
        return self._ratio_evade

    def set_ratio_evade(self, ratio_evade: float) -> None:
        """(unknown)"""
        self._ratio_evade = ratio_evade

    @property
    def ratio_magic_evade(self) -> float:
        """(unknown)"""
        return self._ratio_magic_evade

    def set_ratio_magic_evade(self, ratio_magic_evade: float) -> None:
        """(unknown)"""
        self._ratio_magic_evade = ratio_magic_evade

    @property
    def name_override(self) -> str:
        """The name that will be displayed for this enemy in battle"""
        if self._name_override == "":
            return self.name
        return self._name_override

    def set_name_override(self, name_override: str) -> None:
        """Set the name that will be displayed for this enemy in battle, if it should
        be different from its default name."""
        if name_override == self.name:
            name_override = ""
        self._name_override = name_override

    @property
    def sprite(self) -> "Union[None, UInt16]":
        """(possibly deprecated)"""
        return UInt16(self._sprite)

    def set_sprite(self, sprite: "Union[None, int]") -> None:
        """(possibly deprecated)"""
        if sprite is not None:
            assert 0 <= sprite <= 1023
            assert UInt16(sprite)
        self._sprite = sprite

    def __init__(self, world: Optional[GameWorld] = None) -> None:
        self._world = world

    def __str__(self) -> str:
        return f"""<{self.name}
         hp: {self.hp} 
         attack: {self.attack}
         defense: {self.defense} 
         m.attack: {self.magic_attack} 
         m.defense: {self.magic_defense}>"""

    def __repr__(self) -> str:
        return str(self)

    @property
    def name(self) -> str:
        """Enemy's default name"""
        return self.__class__.__name__

    @staticmethod
    def round_for_battle_script(val: Union[float, int]) -> int:
        """Round a HP value for battle event data.
        This means round to an integer, and make sure it does have them values 0xfe or 0xff
        because these are special values that stop processing the battle script."""
        new_stat = int(round(val))
        modulus = new_stat % 256

        # 0xfe
        if modulus == 254:
            new_stat += 2
        # 0xff
        elif modulus == 255:
            new_stat += 1

        # If starting value was positive, final value must be at least 1
        # since zero is a death trigger that ends battle.
        if val > 0:
            return max(1, new_stat)
        else:
            return new_stat

    @classmethod
    def get_world_instance(cls, world: GameWorld) -> "Enemy":
        """Get the instance of this enemy in the seed being generated."""
        return next(
            iter(
                enemy for enemy in world.enemies if enemy.monster_id == cls().monster_id
            )
        )

    @property
    def rank(self) -> int:
        """Calculate rough difficulty ranking of enemy based on HP and attack stats."""
        hp = self.hp if self.hp >= 10 else 100
        return hp * max(self.attack, self.magic_attack, 1)

    @property
    def psychopath_text(self) -> str:
        """Make Psychopath text to show elemental weaknesses and immunities."""
        desc = ""

        elemental_immunities = ""
        elemental_weaknesses = ""
        status_vulnerabilities = ""

        # Elemental immunities.
        if len(self.resistances) > 0:
            elemental_immunities += "\x7C"
            elemental_immunities += "".join([e.dialog_char for e in self.resistances])

        # Elemental weaknesses.
        if len(self.weaknesses) > 0:
            elemental_weaknesses += "\x7B"
            elemental_immunities += "".join([e.dialog_char for e in self.weaknesses])

        # Status vulnerabilities.
        vulnerabilities = [
            i
            for i in [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
            if i not in self.status_immunities
        ]
        if vulnerabilities:
            status_vulnerabilities += "".join([e.dialog_char for e in vulnerabilities])

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

    def get_similar(self) -> "Enemy":
        """Get a similar enemy to this one for formation shuffling based on rank."""
        # If we're a boss enemy, treat as unique.
        if self.boss:
            return self

        # Get all non-boss candidates sorted by rank.
        candidates = [e for e in self.world.enemies if not e.boss]
        candidates = sorted(candidates, key=lambda e: (e.rank, e.monster_id))

        # If this is a special enemy, don't replace it.
        if self.rank < 0:
            return self
        if self not in candidates:
            return self

        # Sort by rank and mutate our position within the list to get a replacement enemy.
        index = candidates.index(self)
        index = mutate_normal(index, maximum=len(candidates) - 1)
        return candidates[index]

    def update_world_entities(self) -> None:
        """For some enemies, their stats being modified will have implications on
        certain thresholds in monster and animation scripts."""

    def get_patch(self) -> Patch:
        """Get patch for this enemy."""
        patch = Patch()

        # Main stats.
        data = bytearray()
        data += ByteField(self.hp).as_bytes()
        data += ByteField(self.speed).as_bytes()
        data += ByteField(self.attack).as_bytes()
        data += ByteField(self.defense).as_bytes()
        data += ByteField(self.magic_attack).as_bytes()
        data += ByteField(self.magic_defense).as_bytes()
        data += ByteField(self.fp).as_bytes()
        data += ByteField(self.evade).as_bytes()
        data += ByteField(self.magic_evade).as_bytes()
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
        data += BitMapSet(
            1, [resistance.stat_value for resistance in self.resistances]
        ).as_bytes()

        # Elemental weaknesses byte (top half), sound on approach is bottom half.
        weaknesses_approach = self.sound_on_approach
        for weakness in self.weaknesses:
            weaknesses_approach |= 1 << weakness.stat_value
        data.append(weaknesses_approach)

        # Status immunities.
        data += BitMapSet(
            1, [immunity.stat_value for immunity in self.status_immunities]
        ).as_bytes()

        patch.add_data(self.address + 11, data)

        # Flower bonus.
        bonus_addr = FLOWER_BONUS_BASE_ADDRESS + self.monster_id
        bonus = (self.flower_bonus_chance // 10) << 4
        bonus |= self.flower_bonus_type
        patch.add_data(bonus_addr, ByteField(bonus).as_bytes())

        yoshi_cookie_item = self.world.get_item_instance(self.yoshi_cookie_item).item_id
        common_item = 0xFF
        if self.common_item_drop is not None:
            common_item = self.world.get_item_instance(self.common_item_drop).item_id
        rare_item = 0xFF
        if self.rare_item_drop is not None:
            rare_item = self.world.get_item_instance(self.rare_item_drop).item_id

        # Build reward data patch.
        data = bytearray()
        data += ByteField(self.xp).as_bytes()
        data += ByteField(self.coins).as_bytes()
        data += ByteField(yoshi_cookie_item).as_bytes()
        data += ByteField(common_item).as_bytes()
        data += ByteField(rare_item).as_bytes()
        patch.add_data(self.reward_address, data)

        # If we have an override name, add to the patch data.
        if self.name_override:
            addr = NAME_BASE_ADDRESS + (self.monster_id * 13)
            patch.add_data(addr, self.name_override.upper().encode().ljust(13, b"\x20"))

        return patch

    @classmethod
    def build_psychopath_patch(cls, world: GameWorld) -> Patch:
        """Build patch data for Psychopath text.
        These use pointers, so we need to do them all together."""
        patch = Patch()

        # Begin text data with a single null byte to use for all empty text to save space.
        pointer_data = bytearray()
        text_data = bytearray()
        text_data.append(0x00)

        # Make list of blank text for all enemies, and get text for each valid enemy we have
        # based on index.
        descriptions = [""] * TOTAL_ENEMIES
        for enemy in world.enemies:
            descriptions[enemy.monster_id] = enemy.psychopath_text

        # Now build the actual pointer data.
        for desc in descriptions:
            # If the description is empty, just use the null byte at the very beginning.
            if not desc:
                pointer = BASE_PSYCHOPATH_DATA_ADDRESS - PSYCHOPATH_DATA_POINTER_OFFSET
                pointer_data += ByteField(pointer, num_bytes=2).as_bytes()
                continue

            # Compute pointer from base address and current data length.
            pointer = (
                BASE_PSYCHOPATH_DATA_ADDRESS
                + len(text_data)
                - PSYCHOPATH_DATA_POINTER_OFFSET
            )
            pointer_data += ByteField(pointer, num_bytes=2).as_bytes()

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
                f"Psychopath text too long (got {len(text_data)}, want <= {5235})"
            )

        # Add pointer data, then add text data.
        patch.add_data(BASE_PSYCHOPATH_POINTER_ADDRESS, pointer_data)
        patch.add_data(BASE_PSYCHOPATH_DATA_ADDRESS, text_data)

        return patch


class Henchman(Enemy):
    """A base class representing an overworld character who is related to the boss
    occupying a boss fight location."""


class AllyClone(Henchman):
    """A specialized base class representing an overworld character who is related to the boss
    occupying a boss fight location, when that boss is Belome 2."""

    def patch_script(self):
        """If no OHKO flag is set, make the Pure Water self-KO counter inaccessible"""

        if self.world.settings.is_boolean_flag_enabled(NoOHKO):
            battlescript = self.world.monster_scripts.scripts[self.monster_id]
            for command in battlescript.contents:
                if isinstance(command, IfTargetedByItem):
                    # Good luck using that in battle
                    command.set_commands([BrightCard])


class ShellySupport(Enemy):
    """A helper class that controls Shelly's behaviour whether attached to Birdetta or
    attached to the middle Nimbus boss"""

    _position: int = 0
    _vanilla: bool = False
    _summons: List[int] = []
    _summon_event: Union[int, None] = None
    _sprite_sub: bool = False
    _formation_id: Union[int, None] = 0

    @property
    def position(self) -> int:
        """Index of this entity within the battle formation"""
        return self._position

    def set_position(self, position: int) -> None:
        """Set the index of this entity within the battle formation"""
        self._position = position

    @property
    def vanilla(self) -> bool:
        """Should only be true if Birdetta is the middle boss of Nimbus Land"""
        return self._vanilla

    def set_vanilla(self, vanilla: bool) -> None:
        """Should only be true if Birdetta is the middle boss of Nimbus Land"""
        self._vanilla = vanilla

    @property
    def summons(self) -> List[int]:
        """A list of formation indexes corresponding to the enemies who should be summoned
        when Shelly hatches"""
        return self._summons

    def set_summons(self, summons: List[int]) -> None:
        """Set the list of formation indexes corresponding to the enemies who should be summoned
        when Shelly hatches"""
        self._summons = summons

    @property
    def summon_event(self) -> Union[int, None]:
        """Optional battle event to run after Shelly hatches"""
        return self._summon_event

    def set_summon_event(self, summon_event: Union[int, None]) -> None:
        """Set an optional battle event to run after Shelly hatches"""
        self._summon_event = summon_event

    @property
    def sprite_sub(self) -> bool:
        """(unknown)"""
        return self._sprite_sub

    def set_sprite_sub(self, sprite_sub: bool) -> None:
        """(unknown)"""
        self._sprite_sub = sprite_sub

    @property
    def formation_id(self) -> Union[UInt8, None]:
        """The formation containing Shelly"""
        if self._formation_id is not None:
            return UInt8(self._formation_id)
        return self._formation_id

    def set_formation_id(self, formation_id: Union[int, None]) -> None:
        """Set the formation containing Shelly"""
        if formation_id is not None:
            assert UInt8(formation_id)
        self._formation_id = formation_id
