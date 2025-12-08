"""Base classes for enemies encountered in battle and their overworld representations."""

from typing import TYPE_CHECKING

from randomizer.types.items import RegularItem
from randomizer.types.monster_scripts.commands import IfTargetedByItem
from randomizer.types.numbers import ByteField, UInt16, UInt8
from randomizer.types.patch import Patch
from randomizer.types.spells import Status

from randomizer.types.world.flags import NoOHKO

from randomizer.utils.number import mutate_normal

from randomizer.entities.items.items import BrightCard, Mushroom

from .constants import (
    BASE_PSYCHOPATH_DATA_ADDRESS,
    BASE_PSYCHOPATH_POINTER_ADDRESS,
    PSYCHOPATH_DATA_POINTER_OFFSET,
    TOTAL_ENEMIES)
from .enums import ApproachSound, HitSound, FlowerBonusType

if TYPE_CHECKING:
    from randomizer.types.world import GameWorld


class Enemy(TODOImportEnemy):
    """Class representing an enemy in the game."""

    _world: "GameWorld" | None

    @property
    def world(self) -> "GameWorld":
        """World instance reference"""
        assert self._world is not None
        return self._world

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
    _sprite: None | int = None

    # attribute methods

    @property
    def rare_item_drop(self) -> type[RegularItem] | None:
        """A single item that the enemy has a very small chance of dropping."""
        return self._rare_item_drop

    def set_rare_item_drop(self, rare_item_drop: type[RegularItem] | None) -> None:
        """Set the single item that the enemy has a very small chance of dropping."""
        self._rare_item_drop = rare_item_drop
        if rare_item_drop is not None:
            self.set_rare_item_drop_id(rare_item_drop.item_id)
        else:
            self.set_rare_item_drop_id(None)

    @property
    def common_item_drop(self) -> type[RegularItem] | None:
        """A single item that the enemy has a high chance of dropping."""
        return self._common_item_drop

    def set_common_item_drop(self, common_item_drop: type[RegularItem]) -> None:
        """Set the single item that the enemy has a high chance of dropping."""
        self._common_item_drop = common_item_drop
        if common_item_drop is not None:
            self.set_common_item_drop_id(rare_common_drop.item_id)
        else:
            self.set_common_item_drop_id(None)

    @property
    def boss(self) -> bool:
        """If true, this enemy is considered a boss."""
        return self._boss

    def set_boss(self, boss: bool) -> None:
        """If true, this enemy is considered a boss."""
        self._boss = boss

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
    def sprite(self) -> None | UInt16:
        """(possibly deprecated)"""
        if self._sprite is None:
            return self._sprite
        return UInt16(self._sprite)

    def set_sprite(self, sprite: "None | int") -> None:
        """(possibly deprecated)"""
        if sprite is not None:
            assert 0 <= sprite <= 1023
            assert UInt16(sprite)
        self._sprite = sprite

    def __init__(self, world: "GameWorld" | None = None) -> None:
        self._world = world

    @staticmethod
    def round_for_battle_script(val: float | int) -> int:
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
        return new_stat

    @classmethod
    def get_world_instance(cls, world: "GameWorld") -> "Enemy":
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

    @classmethod
    def build_psychopath_patch(cls, world: "GameWorld") -> Patch:
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
    _summons: list[int] = []
    _summon_event: int | None = None
    _sprite_sub: bool = False
    _formation_id: int | None = 0

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
    def summons(self) -> list[int]:
        """A list of formation indexes corresponding to the enemies who should be summoned
        when Shelly hatches"""
        return self._summons

    def set_summons(self, summons: list[int]) -> None:
        """Set the list of formation indexes corresponding to the enemies who should be summoned
        when Shelly hatches"""
        self._summons = summons

    @property
    def summon_event(self) -> int | None:
        """Optional battle event to run after Shelly hatches"""
        return self._summon_event

    def set_summon_event(self, summon_event: int | None) -> None:
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
    def formation_id(self) -> UInt8 | None:
        """The formation containing Shelly"""
        if self._formation_id is not None:
            return UInt8(self._formation_id)
        return self._formation_id

    def set_formation_id(self, formation_id: int | None) -> None:
        """Set the formation containing Shelly"""
        if formation_id is not None:
            assert UInt8(formation_id)
        self._formation_id = formation_id
