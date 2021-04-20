# Data module for enemy data.

from randomizer.logic import flags, utils
from randomizer.logic.battleassembler import BattleScript
from randomizer.logic.patch import Patch
from . import attacks
from . import battlescripts
from . import items
from . import spells
from .utils import palette_to_bytes
from .battletables import Monsters, Targets
from randomizer.data.npcmodels import models
from randomizer.data.npcmodeltables import SpriteName, VramStore, ShadowSize

# Number of enemies
NUM_ENEMIES = 256
NO_SHADOW = 0
SMALL_SHADOW = 1
MED_SHADOW = 2
LARGE_SHADOW = 3
BLOCK_SHADOW = 4


class Enemy:
    """Class representing an enemy in the game."""
    FLOWER_BONUS_BASE_ADDRESS = 0x39bb44
    BASE_PSYCHOPATH_POINTER_ADDRESS = 0x399fd1
    PSYCHOPATH_DATA_POINTER_OFFSET = 0x390000
    BASE_PSYCHOPATH_DATA_ADDRESS = 0x39a1d1
    NAME_BASE_ADDRESS = 0x3992d1

    # Default instance attributes.
    index = 0
    address = 0x000000
    boss = False
    hp = 0
    speed = 0
    attack = 0
    defense = 0
    magic_attack = 0
    magic_defense = 0
    fp = 0
    evade = 0
    magic_evade = 0
    invincible = False
    death_immune = False
    morph_chance = 0
    sound_on_hit = 0
    sound_on_approach = 0
    resistances = []
    weaknesses = []
    status_immunities = []
    palette = 0
    flower_bonus_type = 0
    flower_bonus_chance = 0
    flying = False
    high_flying = False
    # Flag if enemy is unique per battle (only 1 max per formation)
    one_per_battle = False
    hp_counter_ratios = []

    # Reward attributes.
    reward_address = 0x000000
    xp = 0
    coins = 0
    yoshi_cookie_item = None
    normal_item = None
    rare_item = None

    # Boss shuffle attributes.
    anchor = False
    ratio_hp = 1.0
    ratio_fp = 1.0
    ratio_attack = 1.0
    ratio_defense = 1.0
    ratio_magic_attack = 1.0
    ratio_magic_defense = 1.0
    ratio_speed = 1.0
    ratio_evade = 1.0
    ratio_magic_evade = 1.0
    name_override = ''
    dialog_replacements = []
    optional_dialog_replacements = []

    # shuffled overworld sprites
    sidekicks = []
    sprite_width = 32
    sprite_height = 32
    model_small = None
    model_large = None

    def __init__(self, world):
        """

        Args:
            world (randomizer.logic.main.GameWorld):

        """
        self.world = world

        # Set instance normal and rare item rewards to the actual item instances for this world.
        if self.normal_item is not None:
            self.normal_item = self.world.get_item_instance(self.normal_item)
        if self.rare_item is not None:
            self.rare_item = self.world.get_item_instance(self.rare_item)
        # Check world type....
        self.script = list(battlescripts.scripts[self.index])

    def __str__(self):
        return "<{}>".format(self.name)

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
        return world.enemies_dict[cls.index]

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
        desc = ''

        # Elemental immunities.
        if self.resistances:
            desc += '\x7C'
            desc += utils.add_desc_fields((
                ('\x7E', 6, self.resistances),
                ('\x7D', 4, self.resistances),
                ('\x7F', 5, self.resistances),
                ('\x85', 7, self.resistances),
            ))
        else:
            desc += '\x20' * 5

        desc += '\x20'

        # Elemental weaknesses.
        if self.weaknesses:
            desc += '\x7B'
            desc += utils.add_desc_fields((
                ('\x7E', 6, self.weaknesses),
                ('\x7D', 4, self.weaknesses),
                ('\x7F', 5, self.weaknesses),
                ('\x85', 7, self.weaknesses),
            ))
        else:
            desc += '\x20' * 5

        desc += '\x20\x20'

        # Status vulnerabilities.
        vulnerabilities = [i for i in range(
            4) if i not in self.status_immunities]
        if vulnerabilities:
            desc += utils.add_desc_fields((
                ('\x82', 0, vulnerabilities),
                ('\x80', 1, vulnerabilities),
                ('\x83', 2, vulnerabilities),
                ('\x81', 3, vulnerabilities),
                ('\x84\x84', True, not self.death_immune),
            ))
        else:
            desc += '\x20' * 6

        desc += '\x02'

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
        candidates = sorted(candidates, key=lambda e: (e.rank, e.index))

        # If this is a special enemy, don't replace it.
        if self.rank < 0:
            return self
        elif self not in candidates:
            return self

        # Sort by rank and mutate our position within the list to get a replacement enemy.
        index = candidates.index(self)
        index = utils.mutate_normal(index, maximum=len(candidates) - 1)
        return candidates[index]

    def fix_hp_counters(self):
        """Fixes up battlescripts that rely on countering when their HP goes down.

        Returns: None

        """
        dex = 0
        script = self.script
        hps = self.hp_counter_ratios
        for i in range(len(script)):
            (name, val) = script[i]
            # Skip any HP checks for 0 because these are death checks that end the fight.
            if name == 'if_hp' and val[0] > 0:
                hp = self.round_for_battle_script(self.hp * hps[dex])
                script[i] = ('if_hp', [hp])
                dex += 1
                if dex == len(hps):
                    break
        else:
            raise Exception('More HP values than counters')

    def get_model(self, battle=False):
        if battle and self.model_large is not None:
            return self.model_large
        elif self.model_small is not None:
            return self.model_small
        else:
            raise 'No model for %s' % self.name

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
        hit_special_defense |= (1 if self.death_immune else 0) << 1
        hit_special_defense |= self.morph_chance << 2
        hit_special_defense |= self.sound_on_hit
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
        bonus_addr = self.FLOWER_BONUS_BASE_ADDRESS + self.index
        bonus = self.flower_bonus_chance << 4
        bonus |= self.flower_bonus_type
        patch.add_data(bonus_addr, utils.ByteField(bonus).as_bytes())

        # Build reward data patch.
        data = bytearray()
        data += utils.ByteField(self.xp, num_bytes=2).as_bytes()
        data += utils.ByteField(self.coins).as_bytes()
        data += utils.ByteField(
            self.yoshi_cookie_item.index if self.yoshi_cookie_item else 0xff).as_bytes()
        data += utils.ByteField(
            self.normal_item.index if self.normal_item else 0xff).as_bytes()
        data += utils.ByteField(
            self.rare_item.index if self.rare_item else 0xff).as_bytes()
        patch.add_data(self.reward_address, data)

        # If we have an override name, add to the patch data.
        if self.name_override:
            addr = self.NAME_BASE_ADDRESS + (self.index * 13)
            patch.add_data(
                addr, self.name_override.upper().encode().ljust(13, b'\x20'))

        return patch

    def patch_script(self):
        if self.world.open_mode and self.hp_counter_ratios:
            self.fix_hp_counters()

        if self.world.settings.is_flag_enabled(flags.NoOHKO) and type(self) in (
                MarioClone, MallowClone, GenoClone, BowserClone, PeachClone):
            for i in range(len(self.script)):
                name, args = self.script[i]
                if name == 'if_item':
                    # Good luck using that in battle
                    self.script[i] = ('if_item', [items.BrightCard])

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
        descriptions = [''] * NUM_ENEMIES
        for enemy in world.enemies:
            descriptions[enemy.index] = enemy.psychopath_text

        # Now build the actual pointer data.
        for desc in descriptions:
            # If the description is empty, just use the null byte at the very beginning.
            if not desc:
                pointer = cls.BASE_PSYCHOPATH_DATA_ADDRESS - cls.PSYCHOPATH_DATA_POINTER_OFFSET
                pointer_data += utils.ByteField(pointer,
                                                num_bytes=2).as_bytes()
                continue

            # Compute pointer from base address and current data length.
            pointer = cls.BASE_PSYCHOPATH_DATA_ADDRESS + \
                len(text_data) - cls.PSYCHOPATH_DATA_POINTER_OFFSET
            pointer_data += utils.ByteField(pointer, num_bytes=2).as_bytes()

            # Add null byte to terminate the text string.
            desc = desc.encode('latin1')
            desc += bytes([0x00])
            text_data += desc

        # Sanity check that pointer data has the correct number of items.
        if len(pointer_data) != NUM_ENEMIES * 2:
            raise ValueError(
                "Wrong length for pointer data, something went wrong...")

        # Add pointer data, then add text data.
        patch.add_data(cls.BASE_PSYCHOPATH_POINTER_ADDRESS, pointer_data)
        patch.add_data(cls.BASE_PSYCHOPATH_DATA_ADDRESS, text_data)

        return patch


# ********************* Actual data classes

class Terrapin(Enemy):
    index = 0
    address = 0x390226
    hp = 10
    speed = 10
    attack = 1
    defense = 8
    magic_defense = 1
    fp = 100
    morph_chance = 3
    sound_on_hit = 80
    palette = 16
    flower_bonus_type = 3

    # Reward attributes
    reward_address = 0x39162a
    yoshi_cookie_item = items.Mushroom


class Spikey(Enemy):
    index = 1
    address = 0x390236
    hp = 20
    speed = 14
    attack = 6
    defense = 11
    magic_attack = 4
    magic_defense = 2
    fp = 100
    morph_chance = 2
    sound_on_approach = 1
    resistances = [7]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 1

    # Reward attributes
    reward_address = 0x391630
    xp = 1
    coins = 2
    yoshi_cookie_item = items.Bracer
    normal_item = items.HoneySyrup


class Skytroopa(Enemy):
    index = 2
    address = 0x390246
    hp = 10
    speed = 18
    attack = 4
    defense = 16
    magic_attack = 6
    magic_defense = 4
    fp = 100
    evade = 8
    morph_chance = 3
    sound_on_hit = 80
    sound_on_approach = 1
    weaknesses = [7]
    palette = 8
    flower_bonus_type = 5
    flower_bonus_chance = 3
    flying = True

    # Reward attributes
    reward_address = 0x391636
    xp = 1
    coins = 1
    yoshi_cookie_item = items.Mushroom
    rare_item = items.Mushroom


class MadMallet(Enemy):
    index = 3
    address = 0x390866
    boss = True
    hp = 200
    speed = 20
    attack = 120
    defense = 80
    magic_attack = 34
    magic_defense = 85
    fp = 100
    morph_chance = 3
    sound_on_hit = 80
    weaknesses = [5]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391888
    xp = 20
    coins = 1
    yoshi_cookie_item = items.Energizer

    # Boss shuffle attributes.
    ratio_hp = 0.2222
    ratio_fp = 0.3333
    ratio_attack = 0.75
    ratio_defense = 0.8
    ratio_magic_attack = 0.7234
    ratio_magic_defense = 1.4167
    ratio_speed = 1.3333
    ratio_evade = 0.0
    ratio_magic_evade = 0.0

    model_small = {**models[259]}


class Shaman(Enemy):
    index = 4
    address = 0x390706
    hp = 150
    speed = 9
    attack = 92
    defense = 50
    magic_attack = 80
    magic_defense = 90
    fp = 100
    morph_chance = 3
    sound_on_hit = 80
    palette = 8
    flower_bonus_type = 5
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x3917fe
    xp = 17
    coins = 4
    yoshi_cookie_item = items.RoyalSyrup
    normal_item = items.RoyalSyrup
    rare_item = items.MapleSyrup


class Crook(Enemy):
    index = 5
    address = 0x3902e6
    hp = 38
    speed = 22
    attack = 35
    defense = 32
    magic_attack = 12
    magic_defense = 25
    fp = 100
    evade = 40
    magic_evade = 40
    morph_chance = 3
    palette = 8
    flower_bonus_type = 4
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391672
    xp = 10
    coins = 10
    yoshi_cookie_item = items.MidMushroom
    rare_item = items.HoneySyrup

    model_small = {
        **models[261],
        "is_wide": True
    }


class Goomba(Enemy):
    index = 6
    address = 0x390256
    hp = 16
    speed = 13
    attack = 3
    defense = 3
    magic_attack = 1
    magic_defense = 1
    fp = 100
    morph_chance = 3
    sound_on_approach = 2
    weaknesses = [6]
    palette = 8
    flower_bonus_type = 3
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x39163c
    xp = 1
    yoshi_cookie_item = items.Mushroom


class PiranhaPlant(Enemy):
    index = 7
    address = 0x390396
    hp = 168
    speed = 6
    attack = 45
    defense = 14
    magic_attack = 20
    magic_defense = 22
    fp = 4
    morph_chance = 2
    sound_on_hit = 16
    sound_on_approach = 2
    resistances = [7]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3916b4
    xp = 5
    coins = 5
    yoshi_cookie_item = items.SleepyBomb
    normal_item = items.MapleSyrup
    
    model_small = {
        **models[263],
        "extra_props": {
            "is_skinny": True
        }
    }


class Amanita(Enemy):
    index = 8
    address = 0x390346
    hp = 52
    speed = 12
    attack = 35
    defense = 30
    magic_attack = 31
    magic_defense = 18
    fp = 100
    evade = 10
    magic_evade = 10
    morph_chance = 3
    sound_on_hit = 80
    sound_on_approach = 3
    weaknesses = [6]
    palette = 8
    flower_bonus_type = 3
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391696
    xp = 3
    yoshi_cookie_item = items.BadMushroom
    rare_item = items.Mushroom


class Goby(Enemy):
    index = 9
    address = 0x3902b6
    hp = 40
    speed = 12
    attack = 22
    defense = 14
    magic_attack = 2
    magic_defense = 10
    fp = 100
    evade = 20
    morph_chance = 3
    sound_on_hit = 80
    sound_on_approach = 1
    weaknesses = [5]
    palette = 8
    flower_bonus_type = 4
    flower_bonus_chance = 1
    flying = True
    high_flying = True

    # Reward attributes
    reward_address = 0x391660
    xp = 3
    coins = 2
    yoshi_cookie_item = items.Mushroom
    normal_item = items.Mushroom


class Bloober(Enemy):
    index = 10
    address = 0x390536
    hp = 130
    speed = 23
    attack = 80
    defense = 36
    magic_attack = 21
    magic_defense = 16
    fp = 100
    evade = 20
    morph_chance = 3
    sound_on_hit = 128
    weaknesses = [5, 6]
    palette = 8
    flower_bonus_type = 5
    flower_bonus_chance = 10
    flying = True

    # Reward attributes
    reward_address = 0x391756
    xp = 12
    yoshi_cookie_item = items.Elixir
    normal_item = items.MaxMushroom
    rare_item = items.HoneySyrup


class BandanaRed(Enemy):
    index = 11
    address = 0x390576
    hp = 120
    speed = 20
    attack = 78
    defense = 60
    magic_attack = 25
    magic_defense = 25
    fp = 100
    morph_chance = 2
    sound_on_hit = 16
    weaknesses = [5, 6]
    palette = 8
    flower_bonus_type = 4
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x39176e
    xp = 18
    coins = 10
    yoshi_cookie_item = items.Energizer
    rare_item = items.Mushroom


class Lakitu(Enemy):
    index = 12
    address = 0x3903f6
    hp = 124
    speed = 28
    attack = 45
    defense = 43
    magic_attack = 35
    magic_defense = 40
    fp = 100
    evade = 13
    morph_chance = 3
    sound_on_hit = 112
    resistances = [5]
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2
    flying = True

    # Reward attributes
    reward_address = 0x3916d8
    xp = 10
    coins = 3
    yoshi_cookie_item = items.MapleSyrup
    normal_item = items.MapleSyrup
    rare_item = items.MidMushroom


class Birdy(Enemy):
    index = 13
    address = 0x3906d6
    hp = 150
    speed = 23
    attack = 110
    defense = 75
    magic_attack = 55
    magic_defense = 13
    fp = 100
    evade = 18
    morph_chance = 3
    sound_on_hit = 16
    sound_on_approach = 2
    resistances = [6]
    weaknesses = [4]
    status_immunities = [1]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2
    flying = True

    # Reward attributes
    reward_address = 0x3917ec
    xp = 16
    coins = 3
    yoshi_cookie_item = items.Energizer
    normal_item = items.Energizer

    model_small = {
        **models[279],
        "extra_props": {
            "is_wide": True
        }
    }


class Pinwheel(Enemy):
    index = 14
    address = 0x3906f6
    hp = 99
    speed = 32
    attack = 120
    defense = 90
    magic_attack = 70
    magic_defense = 66
    fp = 100
    evade = 35
    morph_chance = 3
    sound_on_hit = 48
    resistances = [5]
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 4
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x3917f8
    xp = 23
    yoshi_cookie_item = items.PickMeUp
    rare_item = items.PickMeUp


class Ratfunk(Enemy):
    index = 15
    address = 0x390296
    hp = 32
    speed = 21
    attack = 20
    defense = 14
    magic_defense = 6
    fp = 100
    evade = 30
    morph_chance = 3
    weaknesses = [6]
    palette = 8
    flower_bonus_type = 4
    flower_bonus_chance = 4

    # Reward attributes
    reward_address = 0x391654
    xp = 2
    coins = 6
    yoshi_cookie_item = items.Mushroom
    normal_item = items.AbleJuice


class K9(Enemy):
    index = 16
    address = 0x390266
    hp = 30
    speed = 19
    attack = 13
    defense = 13
    magic_attack = 1
    magic_defense = 10
    fp = 100
    morph_chance = 2
    palette = 8
    flower_bonus_type = 4
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x391642
    xp = 2
    yoshi_cookie_item = items.Energizer


class Magmite(Enemy):
    index = 17
    address = 0x3903c6
    hp = 26
    speed = 2
    attack = 45
    defense = 70
    magic_attack = 3
    magic_defense = 1
    fp = 100
    morph_chance = 2
    sound_on_hit = 80
    resistances = [7]
    weaknesses = [4]
    palette = 8
    flower_bonus_type = 5
    flower_bonus_chance = 10

    # Reward attributes
    reward_address = 0x3916c6
    xp = 5
    coins = 1
    yoshi_cookie_item = items.Bracer


class TheBigBoo(Enemy):
    index = 18
    address = 0x3902a6
    hp = 43
    speed = 17
    attack = 18
    magic_attack = 18
    magic_defense = 24
    fp = 12
    evade = 40
    morph_chance = 2
    resistances = [7]
    status_immunities = [3]
    palette = 8
    flower_bonus_type = 2
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x39165a
    xp = 2
    yoshi_cookie_item = items.FrightBomb
    normal_item = items.HoneySyrup
    rare_item = items.PureWater


class DryBones(Enemy):
    index = 19
    address = 0x390596
    boss = True
    speed = 9
    attack = 74
    magic_attack = 7
    fp = 100
    morph_chance = 3
    sound_on_hit = 144
    sound_on_approach = 6
    weaknesses = [5]
    palette = 8
    flower_bonus_type = 2
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x39177a
    xp = 12
    coins = 5
    yoshi_cookie_item = items.Mushroom
    normal_item = items.MaxMushroom
    rare_item = items.PureWater


class Greaper(Enemy):
    index = 20
    address = 0x3905b6
    hp = 148
    speed = 30
    attack = 72
    defense = 50
    magic_attack = 40
    magic_defense = 20
    fp = 100
    evade = 30
    magic_evade = 30
    morph_chance = 3
    sound_on_hit = 16
    resistances = [7]
    weaknesses = [5]
    palette = 8
    flower_bonus_type = 5
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x391786
    xp = 13
    yoshi_cookie_item = items.HoneySyrup
    normal_item = items.HoneySyrup
    rare_item = items.PureWater


class Sparky(Enemy):
    index = 21
    address = 0x390386
    hp = 120
    speed = 19
    attack = 40
    defense = 1
    magic_attack = 38
    magic_defense = 50
    fp = 12
    evade = 6
    morph_chance = 1
    sound_on_approach = 2
    resistances = [6]
    weaknesses = [4]
    palette = 8
    flower_bonus_type = 2
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3916ae
    xp = 4
    coins = 1
    yoshi_cookie_item = items.FireBomb

    model_small = {
        **models[277]
    }


class Chomp(Enemy):
    index = 22
    address = 0x390456
    hp = 100
    speed = 10
    attack = 60
    defense = 65
    magic_attack = 5
    magic_defense = 31
    fp = 100
    morph_chance = 2
    sound_on_hit = 32
    weaknesses = [5]
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3916fc
    xp = 10
    yoshi_cookie_item = items.Bracer
    normal_item = items.Mushroom


class Pandorite(Enemy):
    index = 23
    address = 0x390936
    boss = True
    hp = 300
    speed = 1
    attack = 30
    defense = 20
    magic_attack = 20
    magic_defense = 20
    fp = 50
    death_immune = True
    sound_on_hit = 32
    resistances = [4, 5, 6]
    weaknesses = [7]
    status_immunities = [0, 1, 2, 3]
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3918fa
    xp = 20
    coins = 30
    yoshi_cookie_item = items.Mushroom
    normal_item = items.FlowerJar
    rare_item = items.FlowerJar

    # shuffled overworld sprites
    sprite_width = 37
    sprite_height = 40

    model_small = {
        **models[199],
        "extra_props": {
            "is_empty": True,
            "sequence": 4,
            "freeze": True
        }
    }
    model_large = {
        **models[343],
        "sprite": SpriteName._279_PANDORITE,
    }
    dialog_replacements = [
        (49,'''PANDORITE: That thing was making\n me sick...[await]'''),
        (1660, ''' So, you cracked the code. I'm\n warning you though, I hate being\n woken up.[await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Pandorite's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped \nPANDORITE!![await]'''),
        (1778, '''PANDORITE: Whatever... Leave me\n alone so I can go back to sleep.[await]'''),
        (1780, '''PANDORITE: I think I like this place\n more than the sewers. It smells\n marginally better.[await]'''),
        (1781, '''PANDORITE: I can't tell if this is\n better or worse without the\n protection of my box.[await]'''),
        (1784, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1792, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1793, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (2061, '''CHEF TORTE: Zees cake, ve make\n it look like mimic! It is...\n masterpiece![await]'''),
        (2504, '''PANDORITE: Sorry, you can't skip\n getting the last [0x7024] item(s).[await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Pandorite's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Pandorite.[await]'''),
        (2831, '''PANDORITE: There's not much to do\n around here.[await]'''),
        (2832, ''' Yo! You look tired.[delay] How 'bout a\n night on the house?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]'''),
        (2838, ''' You will find Pandorite...\n in his house. He is...the most\n respected person here.[await]'''),
        (3044, '''PANDORITE: Now this should be\n interesting. Can you beat THE\n master, Mario?[await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Treasure-this and Ghost-that.[await]'''),
        (3352, '''PANDORITE: ...I'm not sure how\n I'm accomplishing this.[await]'''),
        (3353, '''PANDORITE: ...I'm not sure how\n I'm accomplishing this.[await]'''),
    ]


class ShyRanger(Enemy):
    index = 24
    address = 0x3903a6
    hp = 300
    speed = 43
    attack = 100
    defense = 80
    magic_attack = 4
    magic_defense = 10
    fp = 100
    evade = 50
    death_immune = True
    morph_chance = 1
    resistances = [4, 5, 6, 7]
    palette = 8
    flower_bonus_type = 5
    flower_bonus_chance = 5

    # Reward attributes
    reward_address = 0x3916ba
    xp = 60
    coins = 1
    yoshi_cookie_item = items.KerokeroCola


class Bobomb(Enemy):
    index = 25
    address = 0x3903b6
    boss = True
    hp = 90
    speed = 1
    attack = 50
    defense = 38
    magic_attack = 1
    magic_defense = 10
    fp = 100
    sound_on_hit = 80
    weaknesses = [6, 7]
    palette = 8
    flower_bonus_type = 2
    flower_bonus_chance = 4

    # Reward attributes
    reward_address = 0x3916c0
    xp = 4
    yoshi_cookie_item = items.Mushroom
    normal_item = items.PickMeUp

    # Boss shuffle attributes.
    ratio_hp = 0.075
    ratio_fp = 10.0
    ratio_attack = 0.83
    ratio_defense = 0.9
    ratio_magic_attack = 0.05
    ratio_magic_defense = 0.25
    ratio_speed = 0.07
    ratio_evade = 0.0
    ratio_magic_evade = 0.0

    model_small = {
        **models[145],
        "extra_props": {
            "is_skinny": True
        }
    }

class Spookum(Enemy):
    index = 26
    address = 0x390436
    hp = 98
    speed = 18
    attack = 50
    defense = 45
    magic_attack = 32
    magic_defense = 5
    fp = 100
    morph_chance = 2
    sound_on_hit = 128
    weaknesses = [4]
    palette = 8
    flower_bonus_type = 4
    flower_bonus_chance = 1

    # Reward attributes
    reward_address = 0x3916f0
    xp = 8
    coins = 4
    yoshi_cookie_item = items.SleepyBomb
    normal_item = items.MidMushroom


class HammerBro(Enemy):
    index = 27
    address = 0x390c26
    boss = True
    hp = 50
    speed = 10
    attack = 6
    defense = 13
    magic_attack = 6
    magic_defense = 8
    fp = 1
    evade = 10
    death_immune = True
    sound_on_hit = 80
    status_immunities = [1]
    palette = 16
    flower_bonus_type = 2
    flower_bonus_chance = 4

    # Reward attributes
    reward_address = 0x391a9e
    xp = 3
    coins = 10
    yoshi_cookie_item = items.Mushroom
    normal_item = items.FlowerJar
    rare_item = items.FlowerJar

    # Boss shuffle attributes.
    ratio_hp = 0.5
    ratio_fp = 0.5

    # shuffled overworld sprites
    sprite_width = 40
    sprite_height = 45
    model_large = {
        **models[283],
        "extra_props": {
            "is_tall": True,
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 40
        }
    }
    model_small = {
        "sprite": SpriteName._545_THROWN_HAMMER,
        "shadow": ShadowSize._00_OVAL_SMALL,
        "y_pixel_shift": 1,
        "acute_axis": 2,
        "obtuse_axis": 2,
        "height": 6,
        "vram_store": VramStore._02_SWSE,
        "extra_props": {
            "is_empty": True,
            "sequence": 4,
            "freeze": True
        }
    }
    dialog_replacements = [
        (49,'''HAMMER BRO: Alright already,\n you won, now go away![await]'''),
        (1660, ''' So, you figured it out... But you\n gotta get past my hammer to get\n through![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n the Hammer Bros' place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped\n the HAMMER BROS!![await]'''),
        (1778, '''HAMMER BRO: ...grumble...\n My hammer's embarrassed about\n losing...[await]'''),
        (1780, '''HAMMER BRO: What're YOU lookin' at?[await]'''),
        (1781, '''HAMMER BRO: Look buddy, you\n already won, you can get off of my\n hammer now.[await]'''),
        (1784, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1792, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1793, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (2061, '''CHEF TORTE: Zees cake, ve make\n it look like big hammer! It is...\n masterpiece![await]'''),
        (2504, '''HAMMER BRO: You better find [0x7024]\n more of `MARRYMORE_CHARACTER`'s things,\n or my hammer'll be angry![await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n The Hammer Bros are busy right\n now, so they can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering the Hammer Bros.[await]'''),
        (2831, '''HAMMER BRO: What're YOU lookin'\n at?[await]'''),
        (2838, ''' You will find the Hammer Bro...\n in his house. He is...the most\n respected person here.[await]'''),
        (3044, '''HAMMER BRO: The dojo master\n takes on 3 different forms.\n Me, though? I'm just a hammer.[await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Hammer-this and Hammer-that.[await]'''),
        (3352, '''HAMMER BRO: I guess you were\n tougher than I thought![await]'''),
        (3353, '''HAMMER BRO: I guess you were\n tougher than I thought![await]'''),
   ]


class Buzzer(Enemy):
    index = 28
    address = 0x390356
    hp = 43
    speed = 25
    attack = 37
    defense = 15
    magic_attack = 4
    magic_defense = 1
    fp = 100
    evade = 30
    morph_chance = 3
    sound_on_hit = 16
    sound_on_approach = 1
    weaknesses = [5, 7]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2
    flying = True

    # Reward attributes
    reward_address = 0x39169c
    xp = 4
    coins = 1
    yoshi_cookie_item = items.Mushroom


class Ameboid(Enemy):
    index = 29
    address = 0x3908c6
    hp = 220
    speed = 1
    attack = 130
    defense = 1
    magic_attack = 30
    magic_defense = 120
    fp = 100
    magic_evade = 50
    morph_chance = 3
    sound_on_approach = 1
    resistances = [7]
    weaknesses = [6]
    palette = 8
    flower_bonus_type = 3
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x3918ca
    xp = 10
    yoshi_cookie_item = items.MaxMushroom
    normal_item = items.RoyalSyrup


class Gecko(Enemy):
    index = 30
    address = 0x3904f6
    hp = 92
    speed = 22
    attack = 68
    defense = 46
    magic_attack = 9
    magic_defense = 32
    fp = 100
    evade = 14
    morph_chance = 3
    sound_on_hit = 128
    resistances = [5]
    weaknesses = [6]
    palette = 8
    flower_bonus_type = 3
    flower_bonus_chance = 4

    # Reward attributes
    reward_address = 0x39173e
    xp = 10
    yoshi_cookie_item = items.FroggieDrink


class Wiggler(Enemy):
    index = 31
    address = 0x390336
    hp = 120
    speed = 10
    attack = 40
    defense = 25
    magic_attack = 18
    magic_defense = 20
    fp = 100
    morph_chance = 3
    sound_on_hit = 96
    weaknesses = [6]
    palette = 16
    flower_bonus_type = 5
    flower_bonus_chance = 4

    # Reward attributes
    reward_address = 0x391690
    xp = 6
    coins = 10
    yoshi_cookie_item = items.AbleJuice
    rare_item = items.HoneySyrup


class Crusty(Enemy):
    index = 32
    address = 0x390556
    hp = 80
    speed = 6
    attack = 100
    defense = 100
    magic_attack = 12
    magic_defense = 35
    fp = 100
    morph_chance = 2
    sound_on_hit = 32
    resistances = [7]
    weaknesses = [5, 6]
    palette = 24
    flower_bonus_type = 1
    flower_bonus_chance = 8

    # Reward attributes
    reward_address = 0x391762
    xp = 25
    coins = 7
    yoshi_cookie_item = items.Bracer
    normal_item = items.RoyalSyrup
    rare_item = items.HoneySyrup


class Magikoopa(Enemy):
    index = 33
    address = 0x391186
    boss = True
    hp = 1600
    speed = 12
    attack = 100
    defense = 60
    magic_attack = 120
    magic_defense = 100
    fp = 250
    death_immune = True
    sound_on_hit = 16
    status_immunities = [0, 1, 2]
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391876
    xp = 30
    coins = 10
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 1.0
    ratio_fp = 1.0

    # overworld sprites
    sprite_height = 42
    sprite_width = 45
    model_small = {
        **models[190],
        "extra_props": {
            "extra_sequence": 10,
            "moleville_animation_sequence": 10,
            "moleville_animation_duration": 52,
            "is_skinny": True,
            "statue_east_shift": 2,
            "opposite_statue_west_shift": 4,
            "opposite_statue_south_shift": 1
        }
    }
    model_large = {
        **models[289],
        "sprite": SpriteName._353_MERLIN,
        "extra_props": {
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 48
        }
    }
    dialog_replacements = [
        (49,'''MAGIKOOPA: Normally,[delay] when I\n summon an egg,[delay] it doesn't\n encapsulate me...[await]'''),
        (1660, ''' This..is..my ship!\n Come in..if you dare![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Magikoopa's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped\n MAGIKOOPA!![await]'''),
        (1778, '''\n  MAGIKOOPA: Huh? ...Where am I?[await]'''),
        (1780, '''MAGIKOOPA: Hello! How have you\n been?[await]'''),
        (1781, '''MAGIKOOPA: Uh, what are you\n doing?[await]'''),
        (1784, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1792, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1793, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (2061, '''CHEF TORTE: Zees cake, ve make\n it look like big wizard! It is...\n masterpiece![await]'''),
        (2504, '''MAGIKOOPA: You••need••[0x7024] more\n item(s)![await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Magikoopa's busy right now, so\n he can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Magikoopa.[await]'''),
        (2831, '''MAGIKOOPA: There's nothing••to\n see••here![await]'''),
        (2838, ''' You will find Magikoopa...\n in his house. He is...the most\n respected person here.[await]'''),
        (3044, '''MAGIKOOPA: Now this should be\n interesting. Can you beat THE\n master, Mario?[await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Yoshi-this and Bowser-that.[await]'''),
        (3352, '''MAGIKOOPA: This is more fun than I\n expected![await]'''),
        (3353, '''MAGIKOOPA: This is more fun than I\n expected![await]'''),
    ]


class Leuko(Enemy):
    index = 34
    address = 0x390566
    hp = 220
    speed = 3
    attack = 65
    defense = 50
    magic_attack = 42
    magic_defense = 60
    fp = 100
    magic_evade = 30
    morph_chance = 1
    sound_on_hit = 64
    resistances = [5]
    weaknesses = [6]
    palette = 16
    flower_bonus_type = 3
    flower_bonus_chance = 6

    # Reward attributes
    reward_address = 0x391768
    xp = 20
    coins = 3
    yoshi_cookie_item = items.Megalixir
    normal_item = items.HoneySyrup
    rare_item = items.MidMushroom


class Jawful(Enemy):
    index = 35
    address = 0x390726
    hp = 278
    speed = 200
    attack = 130
    defense = 110
    magic_attack = 8
    magic_defense = 12
    fp = 100
    morph_chance = 1
    sound_on_hit = 32
    status_immunities = [3]
    palette = 16
    flower_bonus_type = 3
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x39180a
    xp = 27
    yoshi_cookie_item = items.RockCandy
    rare_item = items.SleepyBomb


class Enigma(Enemy):
    index = 36
    address = 0x3903d6
    hp = 150
    speed = 25
    attack = 55
    defense = 40
    magic_attack = 30
    magic_defense = 35
    fp = 100
    evade = 20
    morph_chance = 2
    sound_on_hit = 96
    sound_on_approach = 1
    weaknesses = [7]
    palette = 16
    flower_bonus_type = 3
    flower_bonus_chance = 5

    # Reward attributes
    reward_address = 0x3916cc
    xp = 10
    coins = 5
    yoshi_cookie_item = items.Energizer
    normal_item = items.MapleSyrup


class Blaster(Enemy):
    index = 37
    address = 0x390466
    hp = 120
    speed = 1
    attack = 70
    defense = 70
    magic_defense = 10
    fp = 100
    morph_chance = 2
    weaknesses = [5]
    palette = 24
    flower_bonus_type = 2
    flower_bonus_chance = 6

    # Reward attributes
    reward_address = 0x391702
    xp = 12
    yoshi_cookie_item = items.FrightBomb
    rare_item = items.PickMeUp


class Guerrilla(Enemy):
    index = 38
    address = 0x390366
    hp = 135
    speed = 7
    attack = 42
    defense = 32
    magic_attack = 1
    magic_defense = 5
    fp = 100
    morph_chance = 3
    sound_on_hit = 96
    sound_on_approach = 4
    weaknesses = [6]
    palette = 24
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3916a2
    xp = 8
    coins = 8
    yoshi_cookie_item = items.AbleJuice
    rare_item = items.AbleJuice


class Babayaga(Enemy):
    index = 39
    address = 0x3909a6
    hp = 10
    fp = 100
    morph_chance = 3
    sound_on_hit = 96
    palette = 32
    flower_bonus_type = 2
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391924
    yoshi_cookie_item = items.Mushroom


class Hobgoblin(Enemy):
    index = 40
    address = 0x3902c6
    hp = 50
    speed = 5
    attack = 22
    defense = 22
    magic_attack = 8
    magic_defense = 12
    fp = 8
    morph_chance = 3
    sound_on_hit = 16
    weaknesses = [6]
    palette = 16
    flower_bonus_type = 3
    flower_bonus_chance = 6

    # Reward attributes
    reward_address = 0x391666
    xp = 4
    coins = 3
    yoshi_cookie_item = items.PureWater
    normal_item = items.PureWater
    rare_item = items.PureWater


class Reacher(Enemy):
    index = 41
    address = 0x3905c6
    hp = 184
    speed = 3
    attack = 95
    defense = 75
    magic_attack = 8
    fp = 100
    morph_chance = 3
    sound_on_hit = 32
    weaknesses = [5]
    palette = 24
    flower_bonus_type = 2
    flower_bonus_chance = 6

    # Reward attributes
    reward_address = 0x39178c
    xp = 30
    coins = 8
    yoshi_cookie_item = items.PickMeUp
    normal_item = items.RoyalSyrup
    rare_item = items.PickMeUp


class Shogun(Enemy):
    index = 42
    address = 0x390626
    hp = 150
    speed = 12
    attack = 100
    defense = 80
    magic_attack = 1
    magic_defense = 32
    fp = 100
    morph_chance = 3
    sound_on_hit = 48
    weaknesses = [4]
    status_immunities = [1, 3]
    palette = 16
    flower_bonus_type = 2
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x3917b6
    xp = 24
    coins = 10
    yoshi_cookie_item = items.RoyalSyrup
    rare_item = items.PickMeUp


class Orbuser(Enemy):
    index = 43
    address = 0x390496
    hp = 8
    speed = 15
    attack = 42
    defense = 80
    magic_attack = 28
    magic_defense = 40
    fp = 20
    morph_chance = 3
    sound_on_hit = 80
    resistances = [4, 5, 6]
    palette = 16
    flower_bonus_type = 3
    flower_bonus_chance = 4

    # Reward attributes
    reward_address = 0x391714
    xp = 5
    coins = 2
    yoshi_cookie_item = items.MapleSyrup
    rare_item = items.HoneySyrup


class HeavyTroopa(Enemy):
    index = 44
    address = 0x390736
    hp = 250
    speed = 3
    attack = 160
    defense = 100
    magic_attack = 1
    magic_defense = 50
    fp = 100
    evade = 2
    morph_chance = 1
    sound_on_hit = 96
    sound_on_approach = 1
    weaknesses = [7]
    palette = 16
    flower_bonus_type = 2
    flower_bonus_chance = 8
    flying = True

    # Reward attributes
    reward_address = 0x391810
    xp = 32
    coins = 4
    yoshi_cookie_item = items.Crystalline
    normal_item = items.Crystalline


class Shadow(Enemy):
    index = 45
    address = 0x3902d6
    hp = 85
    speed = 18
    attack = 24
    defense = 5
    magic_attack = 20
    magic_defense = 20
    fp = 14
    evade = 10
    morph_chance = 3
    sound_on_hit = 96
    resistances = [7]
    palette = 16
    flower_bonus_type = 5
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x39166c
    xp = 3
    coins = 2
    yoshi_cookie_item = items.HoneySyrup
    normal_item = items.PickMeUp


class Cluster(Enemy):
    index = 46
    address = 0x3903e6
    hp = 60
    speed = 20
    attack = 50
    defense = 50
    magic_attack = 21
    magic_defense = 10
    fp = 100
    morph_chance = 3
    sound_on_hit = 32
    sound_on_approach = 5
    resistances = [7]
    palette = 16
    flower_bonus_type = 2
    flower_bonus_chance = 4

    # Reward attributes
    reward_address = 0x3916d2
    xp = 8
    coins = 8
    yoshi_cookie_item = items.PickMeUp
    rare_item = items.PickMeUp


class Bahamutt(Enemy):
    index = 47
    address = 0x390996
    boss = True
    hp = 500
    speed = 8
    attack = 170
    defense = 100
    magic_attack = 80
    magic_defense = 20
    fp = 100
    sound_on_hit = 32
    resistances = [6]
    weaknesses = [4]
    status_immunities = [1, 3]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x39191e
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.3125
    ratio_fp = 0.4
    ratio_attack = 1.7
    ratio_defense = 1.6667
    ratio_magic_attack = 0.6667
    ratio_magic_defense = 0.2
    ratio_speed = 0.6667
    ratio_evade = 0.0
    ratio_magic_evade = 0.0


class Octolot(Enemy):
    index = 48
    address = 0x390376
    hp = 99
    speed = 3
    attack = 38
    defense = 27
    magic_attack = 25
    magic_defense = 30
    fp = 100
    evade = 10
    morph_chance = 3
    sound_on_hit = 112
    weaknesses = [6, 7]
    palette = 24
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3916a8
    xp = 6
    coins = 4
    yoshi_cookie_item = items.HoneySyrup
    normal_item = items.HoneySyrup
    rare_item = items.HoneySyrup


class Frogog(Enemy):
    index = 49
    address = 0x390276
    hp = 80
    speed = 8
    attack = 15
    defense = 8
    magic_defense = 8
    fp = 100
    morph_chance = 3
    sound_on_hit = 16
    weaknesses = [5, 6]
    palette = 24
    flower_bonus_type = 3
    flower_bonus_chance = 6

    # Reward attributes
    reward_address = 0x391648
    xp = 3
    coins = 4
    yoshi_cookie_item = items.AbleJuice
    rare_item = items.Mushroom


class Clerk(Enemy):
    index = 50
    address = 0x3911d6
    boss = True
    hp = 500
    speed = 15
    attack = 160
    defense = 100
    magic_attack = 47
    magic_defense = 60
    fp = 100
    death_immune = True
    sound_on_hit = 48
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3918a0
    xp = 50
    coins = 20
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    anchor = True
    ratio_hp = 0.5556
    ratio_fp = 0.3333

    # shuffled overworld sprites
    sprite_width = 60
    sprite_height = 58
    sidekicks = [3, 3]
    model_small = {
        **models[489],
        "extra_props": {
            "dont_reverse_northeast": True,
            "extra_sequence": 2,
            "statue_west_shift": 3,
            "opposite_statue_west_shift": 5,
        }
    }
    model_large = {
        **models[306],
        "sprite": SpriteName._353_MERLIN,
        "extra_props": {
            "is_wide": True,
            "is_tall": True,
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 32
        }
    }
    dialog_replacements = [
        (49,'''CLERK: I'm going to sleep for 10\n years.[await]'''),
        (1660, ''' Sorry, you may have figured out the\n password, but I can't allow you\n through without a fight.[await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n the Clerk's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped\n the CLERK!![await]'''),
        (1778, '''CLERK: I don't get paid nearly\n enough to get whooped that\n badly...[await]'''),
        (1780, '''CLERK: So, you've come back! I\n hope your journey is staying on\n schedule![await]'''),
        (1781, '''CLERK: What do you think you're\n doing?![await]'''),
        (1784, '''MAD MALLET: To be honest, I hate\n fighting alone. I'll run away if I'm\n the last one left in a battle.[await]\n  It sounds cowardly, but this is\n just the way I am.[await]'''),
        (1785, '''MAD MALLET: Hop on the\n trampoline in the next room. It'll\n take you outside.[await]'''),
        (1792, '''MAD MALLET: To be honest, I hate\n fighting alone. I'll run away if I'm\n the last one left in a battle.[await]\n  It sounds cowardly, but this is\n just the way I am.[await]'''),
        (1793, '''MAD MALLET: To be honest, I hate\n fighting alone. I'll run away if I'm\n the last one left in a battle.[await]\n  It sounds cowardly, but this is\n just the way I am.[await]'''),
        (2061, '''MAD MALLET: We're making a cake\n to look just like the Clerk![await]'''),
        (2062, '''MAD MALLET: We've gotten REAL\n good with fondant![await]'''),
        (2504, '''CLERK: Whatcha got? [0x7000] item(s)?\n At this rate, you should find the\n last [0x7024] in no time![await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n The Clerk is busy right now, so\n he can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering the Clerk.[await]'''),
        (2831, '''CLERK: Not much happens in this\n quiet and completely unsuspicious\n town.[await]'''),
        (2832, ''' Welcome.[delay] Would you like to stay\n here for free?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]'''),
        (2834, ''' The two guys in the left building\n have been acting suspicious.[await]'''),
        (2836, ''' If you haven't been to the Sunken\n Ship yet, you can get there through\n the whirlpools in the sea.[await]'''),
        (2837, ''' If you haven't been to the Sunken\n Ship yet, you can get there after\n you crash the wedding over in\n Marrymore.[await]'''),
        (2838, ''' Have you been to the Clerk's\n house up on the hill yet?[await]'''),
        (2839, '''\nDon't go snooping around our town![await]'''),
        (2841, ''' Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]'''),
        (2842, ''' Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]'''),
        (2843, ''' Once you get through the Sunken\n Ship, you can... er...[await]'''),
        (2844, ''' You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]'''),
        (2845, '''\n        I'm just shopping here![await]'''),
        (2847, '''\n                 Get lost![await]'''),
        (2848, ''' Hey buddy, why don't you go snoop\n around some other houses instead?[await]'''),
        (3044, '''CLERK: Now this should be\n interesting. Can you beat THE\n master, Mario?[await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Hammer-this and Puffball-that.[await]'''),
        (3352, '''CLERK: If anyone asks, I'm on\n break![await]'''),
        (3353, '''CLERK: If anyone asks, I'm on\n break![await]'''),
    ]
    optional_dialog_replacements = [
        (1694, '''MAD MALLET: You trashed us!\n Go on to the Clerk's place.[await]'''),
        (1695, '''MAD MALLET: Whoa... No one's\n beaten the Clerk in 10 years![await]'''),
        (2560, '''MAD MALLET: Welcome.[await][pause] It's the\n Clerk's day off, so he's not taking\n visitors today.[await][page]\n ...But if you insist, I'll have to\n keep you out myself![await]'''),
        (2572, '''MAD MALLET: Listen, the Clerk\n doesn't get paid enough to deal\n with you.[await][page]\n  I certainly don't either, but I'm\n having a bad day![await]'''),
        (3072, '''MAD MALLET: Wow! I can see\n Nimbus Land from here![await]'''),
        (3073, '''MAD MALLET: I'm gonna THRASH\n ya![await]'''),
    ]


class Gunyolk(Enemy):
    index = 51
    address = 0x391216
    boss = True
    hp = 1500
    speed = 25
    attack = 200
    defense = 130
    magic_attack = 120
    magic_defense = 80
    fp = 100
    death_immune = True
    sound_on_hit = 96
    resistances = [6]
    weaknesses = [4, 5]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2
    sprite_width = 71
    sprite_height = 63

    # Reward attributes
    reward_address = 0x3918b8
    xp = 100
    coins = 10
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.6
    ratio_fp = 0.5
    ratio_attack = 1.0
    ratio_defense = 1.04
    ratio_magic_attack = 1.2632
    ratio_magic_defense = 0.9412
    ratio_speed = 0.7143

    # shuffled overworld sprites
    model_small = {
        **models[484],
        "extra_props": {
            "extra_sequence": 10,
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 30,
            "statue_west_shift": 1
        }
    }
    model_large = {
        **models[307],
        "extra_props": {
            "is_wide": True,
            "is_tall": True,
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 52
        }
    }
    dialog_replacements = [
        (49,'''FACTORY CHIEF: Grrr... Leave me\n alone![await]'''),
        (1660, ''' So, you solved it?[delay_30]\n Too bad, this is the end of the line\n for you! I won't let you through![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n the Gunyolk's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped\n the GUNYOLK!![await]'''),
        (1778, '''FACTORY CHIEF: Harrumph! Get out\n of here before I invent something\n even stronger![await]'''),
        (1780, '''FACTORY CHIEF: I'm surprised to\n see you back here! I don't have any\n new inventions to show yet.[await]'''),
        (1781, '''FACTORY CHIEF: Harrumph! I should\n invent myself a spiky hat![await]'''),
        (1784, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1792, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1793, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (2061, '''CHEF TORTE: Zees cake, ve make\n it look like big ninja! It is...\n masterpiece![await]'''),
        (2504, '''FACTORY CHIEF: Harrumph! You're\n still missing [0x7024] more item(s)![await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n The Gunyolk is busy right now, so\n it can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering the Gunyolk.[await]'''),
        (2831, '''FACTORY CHIEF: Harrumph! What're\n you doing here?[await]'''),
        (2838, ''' You will find the Factory Chief...\n in his house. He is...the most\n respected person here.[await]'''),
        (3044, '''FACTORY CHIEF: Harrumph! Just\n because you beat me, doesn't mean\n you can beat the dojo master![await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Ninja-this and Invention-that.[await]'''),
        (3352, '''FACTORY CHIEF: I'll out-jump you\n if it's the last thing I do![await]'''),
        (3353, '''FACTORY CHIEF: I'll out-jump you\n if it's the last thing I do![await]'''),
    ]


class Boomer(Enemy):
    index = 52
    address = 0x3911b6
    boss = True
    hp = 2000
    speed = 18
    attack = 200
    defense = 140
    magic_attack = 35
    magic_defense = 26
    fp = 200
    death_immune = True
    sound_on_hit = 48
    status_immunities = [0, 1, 2, 3]
    palette = 24
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3918dc
    xp = 55
    coins = 9
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 1.0
    ratio_fp = 1.0

    # shuffled overworld sprites
    sprite_width = 52
    sprite_width = 49
    sidekicks = [90, 90]

    model_small = {
        **models[159],
        "extra_props": {
            "extra_sequence": 5,
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 40,
            "is_skinny": True,
            "statue_east_shift": 2,
            "opposite_statue_west_shift": 2
        }
    }
    model_large = {
        **models[482],
        "sprite": SpriteName._353_MERLIN,
        "extra_props": {
            "is_tall": True
        }
    }
    dialog_replacements = [
        (49,'''BOOMER: I lost fair and square.[await]\n Now it is time for me to sleep.[await]'''),
        (1660, ''' Ahhhhh... So, it's YOU who solved\n my riddle![delay_30] Now, you've got to deal\n with ME![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Boomer's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped BOOMER!![await]'''),
        (1778, '''BOOMER: I don't need your\n sympathy! Go on...[await]'''),
        (1780, '''BOOMER: A true soldier knows\n when to accept defeat. You earned\n your victory.[await]'''),
        (1781, '''BOOMER: This is absurd! Get off\n of my head.[await]'''),
        (1784, '''CHANDELI-HO: There's nowhere for\n Boomer to crash down onto in here!\n Thank goodness![await]'''),
        (1785, '''CHANDELI-HO: Hop on the\n trampoline in the next room. It'll\n take you outside.[await]'''),
        (1792, '''CHANDELI-HO: There's nowhere for\n Boomer to crash down onto in here!\n Thank goodness![await]'''),
        (1793, '''CHANDELI-HO: There's nowhere for\n Boomer to crash down onto in here!\n Thank goodness![await]'''),
        (2061, '''CHANDELI-HO: We're making a cake\n to look just like Boomer![await]'''),
        (2062, '''CHANDELI-HO: We've gotten REAL\n good with fondant![await]'''),
        (2504, '''BOOMER: Ha ha ha![delay_30] So, you found\n [0x7000] item(s) already. Impressive.[await][pause] But\n now you've got to find [0x7024] more![await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Boomer's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Boomer.[await]'''),
        (2831, '''BOOMER: Ha ha ha![await]\n So, you've\n found our village![await]'''),
        (2832, ''' Hi! Are you tired? You can rest\n up here, and you don't have to\n pay me anything.[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]'''),
        (2834, ''' The two guys in the left building\n have been acting suspicious.[await]'''),
        (2836, ''' If you haven't been to the Sunken\n Ship yet, you can get there through\n the whirlpools in the sea.[await]'''),
        (2837, ''' If you haven't been to the Sunken\n Ship yet, you can get there after\n you crash the wedding over in\n Marrymore.[await]'''),
        (2838, ''' Have you been to Boomer's house\n up on the hill yet?[await]'''),
        (2839, ''' ...Stay away from the shed, OK?\n It's scary![await]'''),
        (2841, ''' Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]'''),
        (2842, ''' Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]'''),
        (2843, ''' Once you get through the Sunken\n Ship, you can... er...[await]'''),
        (2844, ''' You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]'''),
        (2845, ''' I'm upset. There's no candles on\n sale here.[await]'''),
        (2847, '''\n      Sorry, we can't let you in![await]'''),
        (2848, ''' This is Boomer's top-secret shed![await]\n ...Oh no, was I supposed to tell\n you it's top secret?[await]'''),
        (3044, '''BOOMER: Ha ha ha! A match\n against the dojo master?!\n This ought to be fun![await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Soldier-this and Honor-that.[await]'''),
        (3352, '''BOOMER: You won fair and square!\n But I won't make it so easy for you\n next time![await]'''),
        (3353, '''BOOMER: You won fair and square!\n But I won't make it so easy for you\n next time![await]'''),
    ]
    optional_dialog_replacements = [
        (1694, '''CHANDELI-HO: Oh, no, I lost!\n Good luck, Boomer![await]'''),
        (1695, '''CHANDELI-HO: I hope you didn't\n hurt Boomer too bad![await]'''),
        (2560, '''CHANDELI-HO: Welcome! Have you\n come to install the chandelier?[await][page]\n ...No?[delay] Well, you'd better leave\n Boomer alone![await]'''),
        (2572, '''CHANDELI-HO: I won't let you\n bother Boomer![await]'''),
        (3072, '''CHANDELI-HO: Whew... It's weird\n for me to say, but I think I might\n be afraid of heights.[await]'''),
        (3073, '''CHANDELI-HO: I won't let anything\n bad happen to Boomer![await]'''),
    ]

    def get_patch(self):
        """Update battle events for switching between blue and red states for Boomer with shuffled stat changes.

        Returns:
            randomizer.logic.patch.Patch: Patch data

        """
        patch = super().get_patch()

        # TODO: Get addresses for linear mode.
        if self.world.open_mode:
            # Change to blue state.  Scale shuffled stats based on vanilla ratios.
            patch.add_data(0x353629, utils.ByteField(
                int(round(min(self.attack * 0.6, 255)))).as_bytes())
            patch.add_data(0x35362d, utils.ByteField(
                int(round(min(self.defense * 0.6429, 255)))).as_bytes())
            patch.add_data(0x353631, utils.ByteField(
                int(round(min(self.magic_attack * 2.8571, 255)))).as_bytes())
            patch.add_data(0x353635, utils.ByteField(
                int(round(min(self.magic_defense * 3.4615, 255)))).as_bytes())

            # Change back to red state (use starting stats).
            patch.add_data(0x3535e2, utils.ByteField(self.attack).as_bytes())
            patch.add_data(0x3535e6, utils.ByteField(self.defense).as_bytes())
            patch.add_data(0x3535ea, utils.ByteField(
                self.magic_attack).as_bytes())
            patch.add_data(0x3535ee, utils.ByteField(
                self.magic_defense).as_bytes())

        return patch


class Remocon(Enemy):
    index = 53
    address = 0x390476
    hp = 88
    speed = 5
    attack = 56
    defense = 52
    magic_attack = 25
    magic_defense = 10
    fp = 100
    morph_chance = 3
    sound_on_hit = 80
    resistances = [4, 5]
    weaknesses = [6]
    palette = 16
    flower_bonus_type = 5
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391708
    xp = 8
    coins = 7
    yoshi_cookie_item = items.PickMeUp
    normal_item = items.HoneySyrup


class Snapdragon(Enemy):
    index = 54
    address = 0x390316
    hp = 90
    speed = 4
    attack = 28
    defense = 25
    magic_attack = 31
    magic_defense = 25
    fp = 100
    morph_chance = 2
    sound_on_hit = 64
    weaknesses = [6]
    palette = 16
    flower_bonus_type = 3
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391684
    xp = 4
    coins = 3
    yoshi_cookie_item = items.SleepyBomb
    rare_item = items.Mushroom


class Stumpet(Enemy):
    index = 55
    address = 0x3907a6
    hp = 500
    speed = 1
    attack = 200
    defense = 120
    magic_attack = 6
    magic_defense = 60
    fp = 100
    morph_chance = 3
    sound_on_hit = 96
    resistances = [6]
    weaknesses = [4]
    status_immunities = [0, 1, 2, 3]
    palette = 32
    flower_bonus_type = 2
    flower_bonus_chance = 10

    # Reward attributes
    reward_address = 0x39183a
    xp = 70
    coins = 15
    yoshi_cookie_item = items.RoyalSyrup
    normal_item = items.FireBomb
    rare_item = items.FrightBomb


class Dodo(Enemy):
    index = 56
    address = 0x391116
    boss = True
    hp = 1000
    speed = 10
    attack = 140
    defense = 100
    magic_attack = 9
    magic_defense = 60
    fp = 100
    death_immune = True
    sound_on_hit = 16
    weaknesses = [6]
    status_immunities = [0, 1]
    palette = 24
    flower_bonus_type = 1
    flower_bonus_chance = 2
    hp_counter_ratios = [0.6]

    # Reward attributes
    reward_address = 0x391c12
    xp = 40
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.4167
    ratio_fp = 0.2857
    ratio_attack = 1.1667
    ratio_defense = 1.25
    ratio_magic_attack = 0.1125
    ratio_magic_defense = 1.0
    ratio_speed = 0.05
    ratio_evade = 0.0
    ratio_magic_evade = 1.0

    def get_patch(self):
        """For Dodo solo boss, also update the battle event trigger so he runs away from the solo fight at 60% of his
        shuffled HP, not always 600 HP like the vanilla game.

        Returns:
            randomizer.logic.patch.Patch: Patch data

        """
        patch = super().get_patch()

        # Open mode event address is the same as vanilla, but standard mode patch is in a different spot.
        if not self.world.open_mode:
            run_away = self.round_for_battle_script(self.hp * 0.6)
            patch.add_data(0x393818, utils.ByteField(
                run_away, num_bytes=2).as_bytes())

        return patch


class Jester(Enemy):
    index = 57
    address = 0x390486
    boss = True
    hp = 151
    speed = 20
    attack = 48
    defense = 35
    magic_attack = 22
    magic_defense = 35
    fp = 12
    magic_evade = 80
    morph_chance = 3
    sound_on_hit = 16
    weaknesses = [4]
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x39170e
    xp = 10
    coins = 10
    yoshi_cookie_item = items.HoneySyrup


class Artichoker(Enemy):
    index = 58
    address = 0x390416
    hp = 200
    speed = 7
    attack = 50
    defense = 54
    magic_attack = 27
    magic_defense = 24
    fp = 100
    magic_evade = 20
    morph_chance = 3
    sound_on_hit = 32
    sound_on_approach = 2
    resistances = [5]
    weaknesses = [6, 7]
    palette = 24
    flower_bonus_type = 2
    flower_bonus_chance = 4

    # Reward attributes
    reward_address = 0x3916e4
    xp = 12
    coins = 10
    yoshi_cookie_item = items.MidMushroom
    rare_item = items.FrightBomb


class Arachne(Enemy):
    index = 59
    address = 0x390326
    hp = 82
    speed = 14
    attack = 35
    defense = 35
    magic_attack = 6
    fp = 100
    morph_chance = 2
    sound_on_hit = 32
    weaknesses = [4]
    palette = 24
    flower_bonus_type = 2
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x39168a
    xp = 6
    coins = 6
    yoshi_cookie_item = items.Energizer
    normal_item = items.AbleJuice


class Carriboscis(Enemy):
    index = 60
    address = 0x390426
    hp = 90
    speed = 30
    attack = 55
    defense = 44
    magic_attack = 28
    magic_defense = 22
    fp = 100
    evade = 13
    morph_chance = 3
    sound_on_hit = 16
    weaknesses = [6, 7]
    palette = 24
    flower_bonus_type = 3
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x3916ea
    xp = 10
    coins = 4
    yoshi_cookie_item = items.HoneySyrup
    rare_item = items.AbleJuice


class Hippopo(Enemy):
    index = 61
    address = 0x390926
    hp = 400
    speed = 6
    attack = 150
    defense = 110
    magic_attack = 85
    magic_defense = 53
    fp = 100
    magic_evade = 15
    morph_chance = 1
    sound_on_hit = 96
    weaknesses = [5]
    status_immunities = [0, 1, 2, 3]
    palette = 32
    flower_bonus_type = 5
    flower_bonus_chance = 10
    one_per_battle = True

    # Reward attributes
    reward_address = 0x3918f4
    xp = 80
    coins = 50
    yoshi_cookie_item = items.Megalixir
    normal_item = items.RockCandy


class Mastadoom(Enemy):
    index = 62
    address = 0x390506
    hp = 180
    speed = 3
    attack = 90
    defense = 65
    magic_attack = 30
    magic_defense = 50
    fp = 100
    morph_chance = 1
    sound_on_hit = 96
    resistances = [5]
    weaknesses = [6]
    palette = 32
    flower_bonus_type = 3
    flower_bonus_chance = 10

    # Reward attributes
    reward_address = 0x391744
    xp = 20
    yoshi_cookie_item = items.Crystalline
    rare_item = items.MidMushroom


class Corkpedite(Enemy):
    index = 63
    address = 0x3907d6
    hp = 200
    speed = 5
    attack = 130
    defense = 110
    magic_attack = 80
    magic_defense = 20
    fp = 100
    morph_chance = 1
    sound_on_hit = 96
    resistances = [6]
    weaknesses = [4]
    status_immunities = [0, 1, 2, 3]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 6

    # Reward attributes
    reward_address = 0x39184c
    xp = 50
    coins = 10
    yoshi_cookie_item = items.Crystalline
    rare_item = items.FrightBomb


class Terracotta(Enemy):
    index = 64
    address = 0x3907f6
    hp = 180
    speed = 23
    attack = 120
    defense = 85
    magic_attack = 36
    magic_defense = 35
    fp = 100
    morph_chance = 3
    resistances = [6]
    palette = 16
    flower_bonus_type = 4
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x391858
    xp = 25
    yoshi_cookie_item = items.MidMushroom
    rare_item = items.Mushroom


class Spikester(Enemy):
    index = 65
    address = 0x390406
    hp = 50
    speed = 19
    attack = 48
    defense = 60
    magic_attack = 12
    magic_defense = 4
    fp = 100
    morph_chance = 2
    sound_on_approach = 1
    resistances = [7]
    weaknesses = [4]
    palette = 8
    flower_bonus_type = 4
    flower_bonus_chance = 5

    # Reward attributes
    reward_address = 0x3916de
    xp = 6
    coins = 2
    yoshi_cookie_item = items.Bracer


class Malakoopa(Enemy):
    index = 66
    address = 0x390806
    hp = 95
    speed = 35
    attack = 130
    defense = 120
    magic_attack = 47
    magic_defense = 98
    fp = 100
    evade = 20
    morph_chance = 3
    sound_on_hit = 80
    sound_on_approach = 1
    weaknesses = [5]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 3
    flying = True

    # Reward attributes
    reward_address = 0x39185e
    xp = 23
    coins = 3
    yoshi_cookie_item = items.MapleSyrup
    rare_item = items.HoneySyrup


class Pounder(Enemy):
    index = 67
    address = 0x390876
    boss = True
    hp = 180
    speed = 25
    attack = 130
    defense = 70
    magic_attack = 45
    magic_defense = 60
    fp = 100
    morph_chance = 3
    sound_on_hit = 80
    weaknesses = [5]
    palette = 8
    flower_bonus_type = 2
    flower_bonus_chance = 4

    # Reward attributes
    reward_address = 0x39188e
    xp = 24
    coins = 2
    yoshi_cookie_item = items.Energizer

    # Boss shuffle attributes.
    ratio_hp = 0.1343
    ratio_fp = 0.25
    ratio_attack = 1.0
    ratio_defense = 0.6364
    ratio_magic_attack = 0.75
    ratio_magic_defense = 0.8571
    ratio_speed = 1.0
    ratio_evade = 0.0
    ratio_magic_evade = 0.0

    model_small = {**models[323]}


class Poundette(Enemy):
    index = 68
    address = 0x390886
    boss = True
    hp = 150
    speed = 30
    attack = 140
    defense = 60
    magic_attack = 66
    magic_defense = 45
    fp = 100
    morph_chance = 3
    sound_on_hit = 80
    weaknesses = [5]
    palette = 8
    flower_bonus_type = 4
    flower_bonus_chance = 5

    # Reward attributes
    reward_address = 0x391894
    xp = 28
    coins = 3
    yoshi_cookie_item = items.Energizer

    # Boss shuffle attributes.
    ratio_hp = 0.0938
    ratio_fp = 0.2
    ratio_attack = 0.7368
    ratio_defense = 0.5
    ratio_magic_attack = 1.1579
    ratio_magic_defense = 0.5625
    ratio_speed = 0.8571
    ratio_evade = 0.0
    ratio_magic_evade = 0.0

    model_small = {**models[324]}


class Sackit(Enemy):
    index = 69
    address = 0x3904e6
    hp = 152
    speed = 26
    attack = 70
    defense = 53
    magic_attack = 13
    magic_defense = 20
    fp = 100
    evade = 20
    morph_chance = 3
    palette = 8
    flower_bonus_type = 4
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x391738
    xp = 20
    coins = 30
    yoshi_cookie_item = items.MaxMushroom
    normal_item = items.RoyalSyrup
    rare_item = items.MaxMushroom


class GuGoomba(Enemy):
    index = 70
    address = 0x390816
    hp = 132
    speed = 14
    attack = 115
    defense = 66
    magic_attack = 13
    magic_defense = 66
    fp = 100
    magic_evade = 50
    morph_chance = 3
    sound_on_approach = 2
    palette = 8
    flower_bonus_type = 3
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391864
    xp = 15
    coins = 1
    yoshi_cookie_item = items.FroggieDrink
    rare_item = items.MaxMushroom


class Chewy(Enemy):
    index = 71
    address = 0x390686
    hp = 90
    speed = 6
    attack = 110
    defense = 82
    magic_attack = 70
    magic_defense = 52
    fp = 100
    magic_evade = 50
    morph_chance = 3
    sound_on_hit = 16
    sound_on_approach = 2
    resistances = [7]
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 5

    # Reward attributes
    reward_address = 0x3917ce
    xp = 14
    yoshi_cookie_item = items.BadMushroom
    normal_item = items.SleepyBomb


class Fireball(Enemy):
    index = 72
    address = 0x3904b6
    hp = 10
    speed = 42
    attack = 55
    defense = 16
    magic_attack = 30
    magic_defense = 16
    fp = 100
    evade = 50
    magic_evade = 30
    morph_chance = 1
    sound_on_approach = 2
    resistances = [6]
    weaknesses = [4, 7]
    palette = 8
    flower_bonus_type = 5
    flower_bonus_chance = 5

    # Reward attributes
    reward_address = 0x391720
    xp = 8
    yoshi_cookie_item = items.FireBomb
    normal_item = items.PickMeUp


class MrKipper(Enemy):
    index = 73
    address = 0x390546
    hp = 133
    speed = 23
    attack = 75
    defense = 45
    magic_attack = 14
    magic_defense = 10
    fp = 100
    evade = 13
    morph_chance = 3
    sound_on_hit = 80
    sound_on_approach = 1
    weaknesses = [5, 6]
    palette = 8
    flower_bonus_type = 2
    flower_bonus_chance = 5
    flying = True
    high_flying = True

    # Reward attributes
    reward_address = 0x39175c
    xp = 8
    coins = 2
    yoshi_cookie_item = items.Mushroom
    normal_item = items.AbleJuice


class FactoryChief(Enemy):
    index = 74
    address = 0x391206
    boss = True
    hp = 1000
    speed = 45
    attack = 200
    defense = 120
    magic_attack = 70
    magic_defense = 90
    fp = 100
    death_immune = True
    sound_on_hit = 16
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3918b2
    xp = 80
    coins = 90
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.4
    ratio_fp = 0.5
    ratio_attack = 1.0
    ratio_defense = 0.96
    ratio_magic_attack = 0.7368
    ratio_magic_defense = 1.0588
    ratio_speed = 1.2857


class BandanaBlue(Enemy):
    index = 75
    address = 0x390586
    boss = True
    hp = 150
    speed = 30
    attack = 80
    defense = 60
    magic_attack = 20
    magic_defense = 30
    fp = 100
    morph_chance = 3
    sound_on_hit = 16
    weaknesses = [5, 6]
    palette = 8
    flower_bonus_type = 5
    flower_bonus_chance = 5

    # Reward attributes
    reward_address = 0x391774
    xp = 20
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.1829
    ratio_fp = 1.0
    ratio_attack = 0.9412
    ratio_defense = 0.75
    ratio_magic_attack = 0.8
    ratio_magic_defense = 0.5
    ratio_speed = 2.3077

    model_small = {
        **models[331]
    }    


class Manager(Enemy):
    index = 76
    address = 0x3911e6
    boss = True
    hp = 800
    speed = 25
    attack = 170
    defense = 110
    magic_attack = 60
    magic_defense = 70
    fp = 100
    death_immune = True
    sound_on_hit = 48
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3918a6
    xp = 60
    coins = 40
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    anchor = True
    ratio_hp = 0.597
    ratio_fp = 0.25
    ratio_attack = 1.3077
    ratio_defense = 1.0
    ratio_magic_attack = 1.0
    ratio_magic_defense = 1.0
    ratio_speed = 1.0

    # shuffled overworld sprites
    sprite_width = 60
    sprite_height = 58
    sidekicks = [67, 67, 67]
    model_small = {
        **models[493],
        "extra_props": {
            "dont_reverse_northeast": True,
            "extra_sequence": 2,
            "statue_west_shift": 3,
            "opposite_statue_west_shift": 5,
        }
    }
    model_large = {
        **models[306],
        "sprite": SpriteName._332_MANAGER,
        "extra_props": {
            "is_wide": True,
            "is_tall": True,
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 32
        }
    }
    dialog_replacements = [
        (49,'''MANAGER: I'm going to sleep for 25\n years.[await]'''),
        (1660, ''' Who gave you the password?!\n You're gonna pay for this![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n the Manager's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped\n the MANAGER!![await]'''),
        (1778, '''MANAGER: Why don't you just jump\n on out of here?![await]'''),
        (1780, '''MANAGER: Oh, you've returned.\n Good work so far.[await]'''),
        (1781, '''MANAGER: Get off of my head\n before I make you take the longestn jump of your life![await]'''),
        (1784, '''POUNDER: This is way more fun\n than working in the factory was.[await]'''),
        (1785, '''POUNDER: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]'''),
        (1792, '''POUNDER: This is way more fun\n than working in the factory was.[await]'''),
        (1793, '''POUNDER: This is way more fun\n than working in the factory was.[await]'''),
        (2061, '''POUNDER: We're making a cake\n to look just like the Manager![await]'''),
        (2062, '''POUNDER: We've gotten REAL\n good with fondant![await]'''),
        (2504, '''MANAGER: Heh heh heh.[delay] Good work.[await]\n You just need [0x7024] more item(s).[await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n The Manager is busy right now, so\n he can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering the Manager.[await]'''),
        (2831, '''MANAGER: Come to invade our\n town, have you?[await][pause] No need, there's\n nothing of interest here, I swear![await]'''),
        (2832, ''' Good day.[delay] We're offering free\n reservations today. Would you like\n to stay?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]'''),
        (2834, ''' The two guys in the left building\n have been acting suspicious.[await]'''),
        (2836, ''' If you haven't been to the Sunken\n Ship yet, you can get there through\n the whirlpools in the sea.[await]'''),
        (2837, ''' If you haven't been to the Sunken\n Ship yet, you can get there after\n you crash the wedding over in\n Marrymore.[await]'''),
        (2838, ''' Have you been to the Manager's\n house up on the hill yet?[await]'''),
        (2839, ''' If you're gonna snoop around,\n [delay]just don't do it near the shed![await]'''),
        (2841, ''' Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]'''),
        (2842, ''' Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]'''),
        (2843, ''' Once you get through the Sunken\n Ship, you can... er...[await]'''),
        (2844, ''' You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]'''),
        (2845, ''' Hey buddy, I'm just trying to shop\n here. Why don't you mind your own\n business?[await]'''),
        (2847, '''\n             Don't bother us![await]'''),
        (2848, '''\n      Can't you see we're busy?[await]'''),
        (3044, '''MANAGER: You think you can beat\n the dojo master?![await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Hammer-this and Schedule-that.[await]'''),
        (3352, '''MANAGER: Don't interrupt me while\n I'm training![await]'''),
        (3353, '''MANAGER: Don't interrupt me while\n I'm training![await]'''),
    ]
    optional_dialog_replacements = [
        (1694, '''POUNDER: We lost, but we made\n the Manager proud![await]'''),
        (1695, '''POUNDER: Wow! The Manager's\n been here 25 years, and you just\n dethroned him![await]'''),
        (2560, '''POUNDER: Good day.[await][pause] The Manager\n is busy today and will not be\n seeing any guests.[await][pause]\n If you try to force your way in,\n I'll have to deal with you![await]'''),
        (2572, '''POUNDER: Stay outta our hair![await]\n [delay]...Huh? [delay]“You don't have hair”?[await][pause]\n That's it, you're asking for it![await]'''),
        (3072, '''POUNDER: Man, I need a break. This\n job is tiring.[await]'''),
        (3073, '''POUNDER: Bullet Bill production is\n on schedule! Don't get in my way![await]'''),
    ]


class Bluebird(Enemy):
    index = 77
    address = 0x3906e6
    hp = 200
    speed = 29
    attack = 95
    defense = 50
    magic_attack = 80
    magic_defense = 94
    fp = 100
    evade = 8
    morph_chance = 3
    sound_on_hit = 16
    sound_on_approach = 2
    resistances = [4]
    weaknesses = [6]
    status_immunities = [1]
    palette = 8
    flower_bonus_type = 2
    flower_bonus_chance = 2
    flying = True

    # Reward attributes
    reward_address = 0x3917f2
    xp = 14
    coins = 6
    yoshi_cookie_item = items.Bracer
    normal_item = items.Bracer

    model_small = {
        **models[333],
        "extra_props": {
            "is_wide": True
        }
    }


class AlleyRat(Enemy):
    index = 79
    address = 0x3905a6
    hp = 105
    speed = 21
    attack = 70
    defense = 55
    magic_attack = 13
    magic_defense = 12
    fp = 100
    evade = 15
    morph_chance = 3
    palette = 8
    flower_bonus_type = 4
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x391780
    xp = 9
    coins = 3
    yoshi_cookie_item = items.AbleJuice
    rare_item = items.Mushroom


class Chow(Enemy):
    index = 80
    address = 0x390606
    hp = 80
    speed = 27
    attack = 82
    defense = 77
    magic_attack = 8
    magic_defense = 28
    fp = 100
    morph_chance = 3
    status_immunities = [1, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 5

    # Reward attributes
    reward_address = 0x3917aa
    xp = 15
    coins = 3
    yoshi_cookie_item = items.FrightBomb


class Magmus(Enemy):
    index = 81
    address = 0x390766
    hp = 50
    speed = 6
    attack = 110
    defense = 140
    magic_attack = 3
    magic_defense = 25
    fp = 100
    magic_evade = 10
    morph_chance = 3
    sound_on_hit = 80
    resistances = [6, 7]
    weaknesses = [4]
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 5
    flower_bonus_chance = 10

    # Reward attributes
    reward_address = 0x391822
    xp = 18
    coins = 3
    yoshi_cookie_item = items.Bracer
    rare_item = items.Bracer


class LilBoo(Enemy):
    index = 82
    address = 0x3908e6
    hp = 66
    speed = 27
    attack = 120
    defense = 20
    magic_attack = 74
    magic_defense = 120
    fp = 100
    evade = 50
    magic_evade = 20
    morph_chance = 3
    resistances = [7]
    palette = 8
    flower_bonus_type = 2
    flower_bonus_chance = 5

    # Reward attributes
    reward_address = 0x3918d6
    xp = 28
    yoshi_cookie_item = items.FreshenUp


class Vomer(Enemy):
    index = 83
    address = 0x390796
    boss = True
    speed = 10
    attack = 110
    magic_attack = 9
    fp = 100
    magic_evade = 5
    morph_chance = 3
    sound_on_hit = 144
    sound_on_approach = 6
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391834
    xp = 19
    yoshi_cookie_item = items.PureWater
    rare_item = items.PureWater


class GlumReaper(Enemy):
    index = 84
    address = 0x3908d6
    hp = 180
    speed = 35
    attack = 120
    defense = 55
    magic_attack = 60
    magic_defense = 80
    fp = 100
    evade = 20
    magic_evade = 10
    morph_chance = 3
    sound_on_hit = 16
    resistances = [7]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 5

    # Reward attributes
    reward_address = 0x3918d0
    xp = 35
    coins = 3
    yoshi_cookie_item = items.PureWater
    normal_item = items.PureWater


class Pyrosphere(Enemy):
    index = 85
    address = 0x390786
    hp = 167
    speed = 24
    attack = 105
    defense = 66
    magic_attack = 100
    magic_defense = 48
    fp = 100
    evade = 7
    morph_chance = 1
    sound_on_approach = 2
    resistances = [6]
    weaknesses = [4]
    status_immunities = [2]
    palette = 8
    flower_bonus_type = 4
    flower_bonus_chance = 4

    # Reward attributes
    reward_address = 0x39182e
    xp = 17
    coins = 2
    yoshi_cookie_item = items.FireBomb


class ChompChomp(Enemy):
    index = 86
    address = 0x390666
    hp = 150
    speed = 10
    attack = 100
    defense = 92
    magic_attack = 14
    magic_defense = 30
    fp = 100
    morph_chance = 3
    sound_on_hit = 32
    weaknesses = [5]
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3917c2
    xp = 12
    coins = 5
    yoshi_cookie_item = items.Mushroom
    normal_item = items.Crystalline


class Hidon(Enemy):
    index = 87
    address = 0x390946
    boss = True
    hp = 600
    speed = 1
    attack = 110
    defense = 90
    magic_attack = 60
    magic_defense = 30
    fp = 100
    death_immune = True
    sound_on_hit = 32
    resistances = [4, 5, 6]
    weaknesses = [7]
    status_immunities = [0, 1, 2, 3]
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391900
    xp = 50
    coins = 100
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 1.0
    ratio_fp = 1.0
    other_sprites = [349, 349, 349, 349]

    # shuffled overworld sprites
    sprite_width = 37
    sprite_height = 40
    sidekicks = [93, 93, 93, 93]

    model_small = {
        **models[199],
        "extra_props": {
            "is_empty": True,
            "sequence": 4,
            "freeze": True
        }
    }
    model_large = {
        **models[343]
    }
    dialog_replacements = [
        (49,'''HIDON: No, I'm not gonna puke up\n another item for you! Go away![await]'''),
        (1660, ''' Ugh... What a rude awakening!\n I'm going to make it a hassle for\n you to pass through here![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Hidon's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped HIDON!![await]'''),
        (1778, '''HIDON: Guess I'll have to train the\n Goombettes harder.[await]'''),
        (1780, '''HIDON: This is definitely an upgrade\n from my old post.[await]'''),
        (1781, '''HIDON: Oh come on, you know I'm\n weak to jumps![await]'''),
        (1784, '''GOOMBETTE: Besides when he\n haphazardly throws us at enemies,\n Hidon is very good to us.[await]'''),
        (1785, '''GOOMBETTE: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]'''),
        (1792, '''GOOMBETTE: Besides when he\n haphazardly throws us at enemies,\n Hidon is very good to us.[await]'''),
        (1793, '''GOOMBETTE: Besides when he\n haphazardly throws us at enemies,\n Hidon is very good to us.[await]'''),
        (2061, '''GOOMBETTE: Doesn't this cake\n look just like Hidon?[await]'''),
        (2062, '''GOOMBETTE: We've gotten REAL\n good with fondant![await]'''),
        (2504, '''HIDON: ...I don't know where the\n last [0x7024] item(s) are. Ask the\n Goombettes.[await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Hidon's busy right now, so\n he can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Hidon.[await]'''),
        (2831, '''\n          HIDON: Oh, it's you.[await]'''),
        (2832, ''' Hey! Why don't you crash here for\n the night? It's free! FREE![await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]'''),
        (2834, ''' The two guys in the left building\n have been acting suspicious.[await]'''),
        (2836, ''' If you haven't been to the Sunken\n Ship yet, you can get there through\n the whirlpools in the sea.[await]'''),
        (2837, ''' If you haven't been to the Sunken\n Ship yet, you can get there after\n you crash the wedding over in\n Marrymore.[await]'''),
        (2838, ''' Have you been to Hidon's\n house up on the hill yet?[await]'''),
        (2839, ''' Hey! What are you doing in our\n town? Don't go snooping around![await]'''),
        (2841, ''' Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]'''),
        (2842, ''' Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]'''),
        (2843, ''' Once you get through the Sunken\n Ship, you can... er...[await]'''),
        (2844, ''' You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]'''),
        (2845, ''' Why don'tcha mind your own\n beeswax?![await]'''),
        (2847, ''' Don't even THINK about going\n inside this house![await]'''),
        (2848, ''' Hey, buster![delay] You think you're some\n kinda tough guy, tryin' to step\n over us guards?![await]'''),
        (3044, '''HIDON: The dojo master's pretty\n tough.[await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Treasure-this and Piranha-that.[await]'''),
        (3352, '''HIDON: I bet this would be even\n harder to do in my box.[await]'''),
        (3353, '''HIDON: I bet this would be even\n harder to do in my box.[await]'''),
    ]
    optional_dialog_replacements = [
        (1694, '''GOOMBETTE: You mighta' won\n against us, but Hidon's gonna\n beat you up![await]'''),
        (1695, '''GOOMBETTE: You beat Hidon?![await]\n Oh, man...[await]'''),
        (2560, '''GOOMBETTE: I need a pen, but I\n can't reach the top drawer of this\n desk. Can you help me out?[await][page]\n [delay]...What?[delay] “How are you going to\n use a pen when you don't have any\n arms”?[await][pause] You makin' fun of me?!\n [delay]That's IT, buddy! Get down here![await]'''),
        (2572, '''GOOMBETTE: Hey! Hidon's trying to\n stay in hidin' over here![delay] Get lost![await]'''),
        (3072, '''GOOMBETTE: (I'm too short to see\n out this window.)[await]'''),
        (3073, '''GOOMBETTE: Put up your dukes,\n big man![await]'''),
    ]


class SlingShy(Enemy):
    index = 88
    address = 0x390716
    hp = 120
    speed = 16
    attack = 108
    defense = 80
    magic_attack = 42
    magic_defense = 21
    fp = 100
    morph_chance = 3
    palette = 8
    flower_bonus_type = 5
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x391804
    xp = 3
    coins = 20
    yoshi_cookie_item = items.MapleSyrup
    rare_item = items.HoneySyrup


class Robomb(Enemy):
    index = 89
    address = 0x390446
    hp = 42
    speed = 2
    attack = 54
    defense = 63
    magic_attack = 1
    magic_defense = 20
    fp = 100
    morph_chance = 3
    sound_on_hit = 80
    weaknesses = [6, 7]
    palette = 8
    flower_bonus_type = 2
    flower_bonus_chance = 5

    # Reward attributes
    reward_address = 0x3916f6
    xp = 6
    coins = 1
    yoshi_cookie_item = items.PickMeUp
    normal_item = items.PickMeUp


class ShyGuy(Enemy):
    index = 90
    address = 0x3902f6
    hp = 78
    speed = 14
    attack = 29
    defense = 30
    magic_attack = 20
    magic_defense = 6
    fp = 100
    evade = 10
    morph_chance = 3
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391678
    xp = 2
    coins = 1
    yoshi_cookie_item = items.HoneySyrup

    model_small = {**models[159]}


class Ninja(Enemy):
    index = 91
    address = 0x3908a6
    boss = True
    hp = 235
    speed = 28
    attack = 130
    defense = 76
    magic_attack = 51
    magic_defense = 67
    fp = 100
    evade = 30
    morph_chance = 1
    sound_on_hit = 16
    resistances = [4, 5, 6]
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 5
    flower_bonus_chance = 7

    # Reward attributes
    reward_address = 0x3918be
    xp = 32
    coins = 6
    yoshi_cookie_item = items.PowerBlast
    normal_item = items.MapleSyrup


class Stinger(Enemy):
    index = 92
    address = 0x3905f6
    hp = 65
    speed = 33
    attack = 78
    defense = 80
    magic_attack = 23
    magic_defense = 10
    fp = 100
    evade = 25
    morph_chance = 3
    sound_on_hit = 16
    sound_on_approach = 1
    palette = 8
    flower_bonus_type = 4
    flower_bonus_chance = 4
    flying = True

    # Reward attributes
    reward_address = 0x3917a4
    xp = 13
    coins = 1
    yoshi_cookie_item = items.AbleJuice
    rare_item = items.AbleJuice


class Goombette(Enemy):
    index = 93
    address = 0x390976
    boss = True
    hp = 100
    speed = 16
    attack = 90
    defense = 80
    magic_attack = 30
    magic_defense = 30
    fp = 100
    evade = 20
    sound_on_approach = 2
    weaknesses = [6]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391912
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.1667
    ratio_fp = 1.0
    ratio_attack = 0.8182
    ratio_defense = 0.8889
    ratio_magic_attack = 0.5
    ratio_magic_defense = 1.0
    ratio_speed = 16.0
    ratio_evade = 1.0
    ratio_magic_evade = 0.0

    model_small = {**models[199]}


class Geckit(Enemy):
    index = 94
    address = 0x390696
    hp = 100
    speed = 25
    attack = 84
    defense = 63
    magic_attack = 20
    magic_defense = 8
    fp = 100
    evade = 14
    morph_chance = 3
    sound_on_hit = 128
    resistances = [6]
    weaknesses = [4]
    palette = 8
    flower_bonus_type = 4
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3917d4
    xp = 18
    yoshi_cookie_item = items.Energizer
    rare_item = items.AbleJuice


class Jabit(Enemy):
    index = 95
    address = 0x390896
    hp = 150
    speed = 13
    attack = 120
    defense = 95
    magic_attack = 27
    magic_defense = 34
    fp = 100
    morph_chance = 3
    weaknesses = [5]
    palette = 8
    flower_bonus_type = 2
    flower_bonus_chance = 1

    # Reward attributes
    reward_address = 0x39189a
    xp = 18
    yoshi_cookie_item = items.Bracer
    normal_item = items.PickMeUp


class Starcruster(Enemy):
    index = 96
    address = 0x390846
    hp = 72
    speed = 11
    attack = 135
    defense = 145
    magic_attack = 16
    magic_defense = 53
    fp = 100
    magic_evade = 10
    morph_chance = 1
    sound_on_hit = 32
    resistances = [7]
    weaknesses = [4]
    palette = 24
    flower_bonus_type = 1
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x39187c
    xp = 36
    coins = 30
    yoshi_cookie_item = items.Crystalline
    normal_item = items.Crystalline


class Merlin(Enemy):
    index = 97
    address = 0x3908f6
    boss = True
    hp = 169
    speed = 20
    attack = 124
    defense = 63
    magic_attack = 90
    magic_defense = 130
    fp = 100
    morph_chance = 3
    sound_on_hit = 16
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3918e2
    xp = 50
    coins = 20
    yoshi_cookie_item = items.Mushroom


class Muckle(Enemy):
    index = 98
    address = 0x390746
    boss = True
    hp = 320
    speed = 2
    attack = 90
    defense = 44
    magic_attack = 90
    magic_defense = 44
    fp = 100
    evade = 1
    morph_chance = 1
    sound_on_hit = 64
    resistances = [4]
    weaknesses = [6]
    status_immunities = [0, 1, 2, 3]
    palette = 16
    flower_bonus_type = 3
    flower_bonus_chance = 6

    # Reward attributes
    reward_address = 0x391816
    xp = 6
    coins = 3
    yoshi_cookie_item = items.IceBomb
    normal_item = items.IceBomb


class Forkies(Enemy):
    index = 99
    address = 0x390856
    hp = 350
    speed = 200
    attack = 170
    defense = 120
    magic_attack = 45
    magic_defense = 128
    fp = 100
    morph_chance = 3
    sound_on_hit = 32
    palette = 16
    flower_bonus_type = 3
    flower_bonus_chance = 5

    # Reward attributes
    reward_address = 0x391882
    xp = 32
    coins = 7
    yoshi_cookie_item = items.RoyalSyrup
    rare_item = items.SleepyBomb


class Gorgon(Enemy):
    index = 100
    address = 0x3905d6
    hp = 140
    speed = 16
    attack = 86
    defense = 73
    magic_attack = 24
    magic_defense = 52
    fp = 100
    evade = 11
    morph_chance = 3
    sound_on_hit = 96
    sound_on_approach = 1
    weaknesses = [5]
    palette = 16
    flower_bonus_type = 3
    flower_bonus_chance = 5

    # Reward attributes
    reward_address = 0x391792
    xp = 20
    yoshi_cookie_item = items.MapleSyrup
    rare_item = items.MidMushroom


class BigBertha(Enemy):
    index = 101
    address = 0x390826
    hp = 350
    speed = 1
    attack = 170
    defense = 130
    fp = 100
    morph_chance = 3
    weaknesses = [5]
    palette = 24
    flower_bonus_type = 2
    flower_bonus_chance = 5

    # Reward attributes
    reward_address = 0x39186a
    xp = 35
    coins = 7
    yoshi_cookie_item = items.PickMeUp


class ChainedKong(Enemy):
    index = 102
    address = 0x3907b6
    hp = 355
    speed = 17
    attack = 150
    defense = 80
    magic_attack = 22
    magic_defense = 50
    fp = 100
    evade = 10
    morph_chance = 3
    sound_on_hit = 96
    sound_on_approach = 4
    resistances = [6]
    weaknesses = [4]
    palette = 24
    flower_bonus_type = 3
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x391840
    xp = 35
    coins = 8
    yoshi_cookie_item = items.PickMeUp
    rare_item = items.MaxMushroom


class Fautso(Enemy):
    index = 103
    address = 0x390986
    boss = True
    hp = 420
    speed = 14
    attack = 130
    defense = 100
    magic_attack = 60
    magic_defense = 60
    fp = 100
    evade = 10
    sound_on_hit = 96
    resistances = [5, 6]
    weaknesses = [4, 7]
    status_immunities = [0, 2, 3]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391918
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.4667
    ratio_fp = 1.0
    ratio_attack = 0.7222
    ratio_defense = 0.9091
    ratio_magic_attack = 0.75
    ratio_magic_defense = 1.5
    ratio_speed = 14.0
    ratio_evade = 1.0
    ratio_magic_evade = 0.0


class Strawhead(Enemy):
    index = 104
    address = 0x3905e6
    hp = 131
    speed = 9
    attack = 80
    defense = 63
    magic_attack = 18
    magic_defense = 12
    fp = 100
    morph_chance = 3
    sound_on_hit = 16
    weaknesses = [5]
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x391798
    xp = 17
    coins = 12
    yoshi_cookie_item = items.PureWater
    normal_item = items.PureWater
    rare_item = items.PureWater


class Juju(Enemy):
    index = 105
    address = 0x3909c6
    hp = 10
    fp = 100
    morph_chance = 3
    sound_on_hit = 32
    palette = 24
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391930
    yoshi_cookie_item = items.Mushroom


class ArmoredAnt(Enemy):
    index = 106
    address = 0x3907c6
    hp = 230
    speed = 12
    attack = 130
    defense = 120
    magic_attack = 24
    magic_defense = 80
    fp = 100
    morph_chance = 1
    sound_on_hit = 48
    resistances = [6]
    weaknesses = [4]
    palette = 16
    flower_bonus_type = 2
    flower_bonus_chance = 5

    # Reward attributes
    reward_address = 0x391846
    xp = 30
    coins = 5
    yoshi_cookie_item = items.PowerBlast
    normal_item = items.PowerBlast


class Orbison(Enemy):
    index = 107
    address = 0x390756
    hp = 30
    speed = 25
    attack = 113
    defense = 140
    magic_attack = 63
    magic_defense = 65
    fp = 100
    morph_chance = 3
    sound_on_hit = 80
    resistances = [4, 5, 6]
    weaknesses = [7]
    palette = 16
    flower_bonus_type = 2
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x39181c
    xp = 18
    yoshi_cookie_item = items.RoyalSyrup
    normal_item = items.PureWater


class TuboTroopa(Enemy):
    index = 108
    address = 0x390836
    hp = 500
    speed = 5
    attack = 200
    defense = 80
    magic_attack = 7
    magic_defense = 34
    fp = 100
    evade = 1
    morph_chance = 3
    sound_on_hit = 96
    weaknesses = [5]
    palette = 16
    flower_bonus_type = 5
    flower_bonus_chance = 6
    flying = True

    # Reward attributes
    reward_address = 0x391870
    xp = 40
    coins = 11
    yoshi_cookie_item = items.Elixir
    normal_item = items.RockCandy


class Doppel(Enemy):
    index = 109
    address = 0x390916
    hp = 333
    speed = 40
    attack = 140
    defense = 60
    magic_attack = 44
    magic_defense = 50
    fp = 100
    evade = 19
    morph_chance = 3
    sound_on_hit = 96
    resistances = [7]
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3918ee
    xp = 40
    coins = 12
    yoshi_cookie_item = items.PickMeUp
    rare_item = items.PureWater


class Pulsar(Enemy):
    index = 110
    address = 0x390516
    hp = 69
    speed = 8
    attack = 75
    defense = 90
    magic_attack = 33
    magic_defense = 35
    fp = 100
    evade = 10
    morph_chance = 3
    sound_on_hit = 32
    sound_on_approach = 5
    resistances = [7]
    weaknesses = [6]
    palette = 16
    flower_bonus_type = 5
    flower_bonus_chance = 9

    # Reward attributes
    reward_address = 0x39174a
    xp = 15
    coins = 12
    yoshi_cookie_item = items.PickMeUp
    rare_item = items.PickMeUp


class Octovader(Enemy):
    index = 112
    address = 0x390636
    hp = 250
    speed = 5
    attack = 90
    defense = 50
    magic_attack = 63
    magic_defense = 50
    fp = 100
    evade = 9
    magic_evade = 8
    morph_chance = 3
    sound_on_hit = 112
    resistances = [5]
    weaknesses = [6]
    palette = 24
    flower_bonus_type = 3
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3917bc
    xp = 30
    coins = 8
    yoshi_cookie_item = items.FroggieDrink
    normal_item = items.PowerBlast


class Ribbite(Enemy):
    index = 113
    address = 0x3906a6
    hp = 250
    speed = 15
    attack = 115
    defense = 20
    magic_attack = 31
    magic_defense = 29
    fp = 100
    morph_chance = 3
    resistances = [6]
    weaknesses = [4]
    status_immunities = [2]
    palette = 24
    flower_bonus_type = 3
    flower_bonus_chance = 4

    # Reward attributes
    reward_address = 0x3917da
    xp = 22
    coins = 8
    yoshi_cookie_item = items.Elixir
    normal_item = items.Elixir


class Director(Enemy):
    index = 114
    address = 0x3911f6
    boss = True
    hp = 1000
    speed = 35
    attack = 190
    defense = 120
    magic_attack = 57
    magic_defense = 80
    fp = 100
    death_immune = True
    sound_on_hit = 48
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3918ac
    xp = 70
    coins = 80
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    anchor = True
    ratio_hp = 0.625
    ratio_fp = 0.2

    # shuffled overworld sprites
    sprite_width = 60
    sprite_height = 58
    sidekicks = [68, 68, 68, 68]

    model_small = {
        **models[497],
        "extra_props": {
            "dont_reverse_northeast": True,
            "extra_sequence": 2,
            "statue_west_shift": 3,
            "opposite_statue_west_shift": 5
        }
    }
    model_large = {
        **models[370],
        "extra_props": {
            "is_wide": True,
            "is_tall": True,
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 32
        }
    }
    dialog_replacements = [
        (49,'''DIRECTOR: (Could this day get any\n worse?)[await]'''),
        (1660, ''' Figured out the password, did you?[delay_30]\n Don't get too cocky![delay_30]\n Intruders will be eliminated![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n the Director's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped\n the DIRECTOR!![await]'''),
        (1778, '''DIRECTOR: I'm afraid I have more\n pressing matters to attend to.\n Depart at once.[await]'''),
        (1780, '''DIRECTOR: Do not waste too much\n time here. Your quest must\n continue.[await]'''),
        (1781, '''DIRECTOR: Any tomfoolery will be\n dealt with by immediate meltdown.\n Get off of my head.[await]'''),
        (1784, '''POUNDETTE: I don't feel like I'm\n being used to my full potentia\n down here, but I don't mind\n having a break.[await]'''),
        (1785, '''POUNDETTE: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]'''),
        (1792, '''POUNDETTE: I don't feel like I'm\n being used to my full potentia\n down here, but I don't mind\n having a break.[await]'''),
        (1793, '''POUNDETTE: I don't feel like I'm\n being used to my full potentia\n down here, but I don't mind\n having a break.[await]'''),
        (2061, '''POUNDETTE: We're making a cake\n to look just like the Director![await]'''),
        (2062, '''POUNDETTE: We've gotten REAL\n good with fondant![await]'''),
        (2504, '''DIRECTOR: I'm afraid you must\n continue searching.[delay] There are\n [0x7024] item(s) remaining.[await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n The Director is busy right now, so\n he can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering the Director.[await]'''),
        (2831, '''DIRECTOR: I'm afraid there is\n nothing of concern to you in\n this town.[await]'''),
        (2832, ''' Salutations. How would you like to\n stay in our inn for free today?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]'''),
        (2834, ''' The two guys in the left building\n have been acting suspicious.[await]'''),
        (2836, ''' If you haven't been to the Sunken\n Ship yet, you can get there through\n the whirlpools in the sea.[await]'''),
        (2837, ''' If you haven't been to the Sunken\n Ship yet, you can get there after\n you crash the wedding over in\n Marrymore.[await]'''),
        (2838, ''' Have you been to the Director's\n house up on the hill yet?[await]'''),
        (2839, ''' There's nothing suspicious going on\n in our town! [delay]Now go on, go to the\n next town![await]'''),
        (2841, ''' Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]'''),
        (2842, ''' Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]'''),
        (2843, ''' Once you get through the Sunken\n Ship, you can... er...[await]'''),
        (2844, ''' You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]'''),
        (2845, ''' No, you can't see what I'm buying!\n [delay]How rude![await]'''),
        (2847, '''\n                   Scram![await]'''),
        (2848, ''' There's some important business\n happening in this shed, so get lost\n and quit trying to interrupt us![await]'''),
        (3044, '''DIRECTOR: I'm afraid the dojo\n master will be quite a challenge for\n you to beat.[await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Hammer-this and Meltdown-that.[await]'''),
        (3352, '''DIRECTOR: This is quite the\n difficult regimen for a white-collar\n fellow like me.[await]'''),
        (3353, '''DIRECTOR: This is quite the\n difficult regimen for a white-collar\n fellow like me.[await]'''),
    ]
    optional_dialog_replacements = [
        (1694, '''POUNDETTE: Well, we lost.\n Time for a break.[await]'''),
        (1695, '''POUNDETTE: You beat the Director!\n Impressive![await]'''),
        (2560, '''POUNDETTE: Salutations.[await][pause] Would you\n like to book an appointment with\n the Director?[await][pause]\n ...You want to just barge right\n in?![delay] No way![await]\n Time to teach you some manners![await]'''),
        (2572, '''POUNDETTE: The Director doesn't\n want anyone coming back here,\n so I'm going to have to ask you\n to leave.[await]'''),
        (3072, '''POUNDETTE: Finally, some time to\n rest![await]'''),
        (3073, '''\nPOUNDETTE: Let's see whatcha got![await]'''),
    ]


class Puppox(Enemy):
    index = 117
    address = 0x390906
    hp = 300
    speed = 9
    attack = 145
    defense = 110
    magic_attack = 20
    magic_defense = 32
    fp = 100
    morph_chance = 1
    sound_on_hit = 80
    resistances = [5]
    weaknesses = [6]
    palette = 16
    flower_bonus_type = 2
    flower_bonus_chance = 1

    # Reward attributes
    reward_address = 0x3918e8
    xp = 30
    coins = 10
    yoshi_cookie_item = items.RockCandy
    rare_item = items.FreshenUp


class FinkFlower(Enemy):
    index = 118
    address = 0x390616
    hp = 200
    speed = 4
    attack = 95
    defense = 32
    magic_attack = 63
    magic_defense = 90
    fp = 100
    magic_evade = 12
    morph_chance = 3
    sound_on_hit = 64
    weaknesses = [6]
    status_immunities = [0, 1, 2, 3]
    palette = 16
    flower_bonus_type = 3
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x3917b0
    xp = 20
    coins = 2
    yoshi_cookie_item = items.MaxMushroom
    rare_item = items.MidMushroom


class Lumbler(Enemy):
    index = 119
    address = 0x390a06
    boss = True
    hp = 10
    fp = 100
    morph_chance = 3
    sound_on_hit = 96
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391948
    yoshi_cookie_item = items.Mushroom


class Springer(Enemy):
    index = 120
    address = 0x3908b6
    hp = 122
    speed = 16
    attack = 155
    defense = 110
    magic_attack = 100
    magic_defense = 79
    fp = 100
    evade = 30
    morph_chance = 3
    sound_on_hit = 80
    palette = 8
    flower_bonus_type = 4
    flower_bonus_chance = 4

    # Reward attributes
    reward_address = 0x3918c4
    xp = 29
    coins = 2
    yoshi_cookie_item = items.Elixir
    rare_item = items.Energizer


class Harlequin(Enemy):
    index = 121
    address = 0x390a16
    hp = 10
    fp = 100
    morph_chance = 3
    sound_on_hit = 16
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x39194e
    yoshi_cookie_item = items.Mushroom


class Kriffid(Enemy):
    index = 122
    address = 0x3906b6
    hp = 320
    speed = 8
    attack = 95
    defense = 100
    magic_attack = 50
    magic_defense = 40
    fp = 100
    morph_chance = 1
    sound_on_hit = 32
    sound_on_approach = 2
    resistances = [6]
    weaknesses = [4]
    status_immunities = [2]
    palette = 24
    flower_bonus_type = 2
    flower_bonus_chance = 5

    # Reward attributes
    reward_address = 0x3917e0
    xp = 35
    coins = 6
    yoshi_cookie_item = items.Crystalline
    normal_item = items.BadMushroom


class Spinthra(Enemy):
    index = 123
    address = 0x3906c6
    hp = 230
    speed = 19
    attack = 110
    defense = 70
    magic_attack = 4
    magic_defense = 32
    fp = 100
    morph_chance = 1
    sound_on_hit = 32
    weaknesses = [4]
    status_immunities = [2]
    palette = 24
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3917e6
    xp = 30
    coins = 4
    yoshi_cookie_item = items.PowerBlast
    rare_item = items.Bracer


class Radish(Enemy):
    index = 124
    address = 0x390a26
    hp = 10
    fp = 100
    morph_chance = 3
    sound_on_hit = 16
    palette = 24
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391954
    yoshi_cookie_item = items.Mushroom


class Crippo(Enemy):
    index = 125
    address = 0x390a36
    hp = 10
    fp = 100
    morph_chance = 3
    sound_on_hit = 96
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x39195a
    yoshi_cookie_item = items.Mushroom


class MastaBlasta(Enemy):
    index = 126
    address = 0x390a46
    hp = 10
    fp = 100
    morph_chance = 3
    sound_on_hit = 96
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391960
    yoshi_cookie_item = items.Mushroom


class Piledriver(Enemy):
    index = 127
    address = 0x390a56
    hp = 10
    fp = 100
    morph_chance = 3
    sound_on_hit = 96
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391966
    yoshi_cookie_item = items.Mushroom


class Apprentice(Enemy):
    index = 128
    address = 0x3904c6
    boss = True
    hp = 120
    speed = 20
    attack = 50
    defense = 50
    magic_attack = 20
    magic_defense = 20
    fp = 32
    sound_on_hit = 128
    weaknesses = [4]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391726
    xp = 1
    coins = 4
    yoshi_cookie_item = items.SleepyBomb
    normal_item = items.MidMushroom


class BoxBoy(Enemy):
    index = 134
    address = 0x390956
    boss = True
    hp = 900
    speed = 1
    attack = 180
    defense = 110
    magic_attack = 80
    magic_defense = 40
    fp = 100
    death_immune = True
    sound_on_hit = 32
    resistances = [4, 5, 6]
    weaknesses = [7]
    status_immunities = [0, 1, 2, 3]
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391906
    xp = 100
    coins = 150
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 1.0
    ratio_fp = 1.0

    # shuffled overworld sprites
    sprite_width = 37
    sprite_height = 40

    model_small = {
        **models[199],
        "extra_props": {
            "is_empty": True,
            "sequence": 4,
            "freeze": True
        }
    }
    model_large = {
        **models[390]
    }
    dialog_replacements = [
        (49,'''BOX BOY: How many times are you\n gonna wake me up? Get lost![await]'''),
        (1660, ''' Oh, you're gonna PAY for waking\n me up like this![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Box Boy's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped BOX BOY!![await]'''),
        (1778, '''\n    BOX BOY: You just got lucky![await]'''),
        (1780, '''\n   BOX BOY: This place is boring.[await]'''),
        (1781, '''BOX BOY: You sure you wanna jump\n on me? I counter special attacks.[await]'''),
        (1784, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1792, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1793, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (2061, '''CHEF TORTE: Zees cake, ve make\n it look like mimic! It is...\n masterpiece![await]'''),
        (2504, '''BOX BOY: Still missing [0x7024] item(s)?\n Pathetic![await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Box Boy's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Box Boy.[await]'''),
        (2831, '''BOX BOY: What'd you come here\n for?[await]'''),
        (2838, ''' You will find Box Boy...\n in his house. He is...the most\n respected person here.[await]'''),
        (3044, '''BOX BOY: The dojo master's gonna\n kick your butt![await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Treasure-this and Ghost-that.[await]'''),
        (3352, '''BOX BOY: Ahh, you're not so\n tough![await]'''),
        (3353, '''BOX BOY: Ahh, you're not so\n tough![await]'''),
    ]


class Shelly(Enemy):
    index = 135
    address = 0x390e06
    boss = True
    hp = 10
    defense = 80
    fp = 100
    death_immune = True
    status_immunities = [0, 1, 2, 3]
    palette = 24
    flower_bonus_type = 1
    flower_bonus_chance = 2
    hp_counter_ratios = [0.8, 0.6, 0.4, 0.2]

    # Reward attributes
    reward_address = 0x39198a
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.0129
    ratio_fp = 0.0
    ratio_attack = 0.0
    ratio_defense = 0.6154
    ratio_magic_attack = 0.0
    ratio_magic_defense = 0.0
    ratio_speed = 0.0
    ratio_evade = 0.0
    ratio_magic_evade = 0.0


class Superspike(Enemy):
    index = 136
    address = 0x390ab6
    boss = True
    hp = 10
    fp = 100
    morph_chance = 3
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391990
    yoshi_cookie_item = items.Mushroom


class DodoSolo(Enemy):
    index = 137
    address = 0x391126
    boss = True
    hp = 800
    speed = 10
    attack = 140
    defense = 100
    magic_attack = 9
    magic_defense = 60
    fp = 100
    death_immune = True
    sound_on_hit = 16
    weaknesses = [6]
    status_immunities = [0, 1]
    palette = 24
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391c18
    xp = 70
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 1.0
    ratio_fp = 1.0

    # shuffled overworld sprites
    sprite_height = 56
    sprite_width = 46
    
    model_small = {
        **models[131],
        "acute_axis": 2,
        "obtuse_axis": 2,
        "height": 5,
        "shadow": ShadowSize._00_OVAL_SMALL,
        "extra_props": {
            "is_empty": True,
            "sequence": 2,
            "freeze": True,
            "statue_south_shift": 3
        }
    }
    model_large = {
        **models[21],
        "extra_props": {
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 16
        }
    }
    dialog_replacements = [
        # actually, don't use dialogs for dodo, just play sfx... how to handle this?
        (49,'''[delay_60][end]'''), #time this according to how long the feather sound effect is
        (1660, '''[delay_60][end]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Dodo's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped DODO!![await]'''),
        (1778, '''[delay_60][end]'''),
        (1780, '''[delay_60][end]'''),
        (1781, '''[delay_60][end]'''),
        (1784, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1792, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1793, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (2061, '''CHEF TORTE: Zees cake, ve make\n it look like big bird! It is...\n masterpiece![await]'''),
        (2504, '''    Dodo is a bird of few words.[await]\n    You still have [0x7024] item(s) left\n                 to find.[await]'''), # use async for this one too
        (2560, '''SNIFIT 1: Hello there.[await]\n Dodo's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2571, '''[delay_60][end]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Dodo.[await]'''),
        (2831, '''[delay_60][end]'''),
        (2838, ''' You will find Dodo...\n in his house. He is...the most\n respected person here.[await]'''),
        (3044, '''[delay_60][end]'''),
        (3338, ''' It's really weird.\n I never hear the guy next door.[await]\n Maybe he can't talk.[await]'''),
        (3352, '''[delay_60][end]'''),
        (3353, '''[delay_60][end]'''),
    ]


class Oerlikon(Enemy):
    index = 138
    address = 0x390776
    hp = 85
    speed = 20
    attack = 120
    defense = 125
    magic_attack = 17
    magic_defense = 50
    fp = 100
    morph_chance = 3
    sound_on_approach = 1
    resistances = [6, 7]
    weaknesses = [4]
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 5

    # Reward attributes
    reward_address = 0x391828
    xp = 22
    yoshi_cookie_item = items.Energizer
    rare_item = items.Energizer


class Chester(Enemy):
    index = 139
    address = 0x390966
    boss = True
    hp = 1200
    speed = 1
    attack = 220
    defense = 120
    magic_attack = 120
    magic_defense = 80
    fp = 100
    death_immune = True
    sound_on_hit = 32
    resistances = [4, 5, 6]
    weaknesses = [7]
    status_immunities = [0, 1, 2, 3]
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x39190c
    xp = 150
    coins = 200
    yoshi_cookie_item = items.Mushroom


class CorkpediteBody(Enemy):
    index = 140
    address = 0x3907e6
    hp = 300
    speed = 5
    attack = 100
    defense = 99
    magic_attack = 6
    magic_defense = 1
    fp = 100
    morph_chance = 3
    resistances = [6]
    weaknesses = [4]
    status_immunities = [0, 1, 2, 3]
    palette = 16
    flower_bonus_type = 2
    flower_bonus_chance = 8

    # Reward attributes
    reward_address = 0x391852
    xp = 30
    yoshi_cookie_item = items.Mushroom


class Torte(Enemy):
    index = 142
    address = 0x390cc6
    boss = True
    hp = 100
    speed = 99
    attack = 60
    defense = 50
    magic_attack = 8
    magic_defense = 27
    fp = 100
    death_immune = True
    sound_on_hit = 80
    sound_on_approach = 7
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x39172c
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.0667
    ratio_fp = 0.5
    ratio_attack = 0.8824
    ratio_defense = 3.3333
    ratio_magic_attack = 0.2857
    ratio_magic_defense = 0.675
    ratio_speed = 6.1875
    ratio_evade = 1.0
    ratio_magic_evade = 1.0

    model_small = {
        **models[398]
    }


class Shyaway(Enemy):
    index = 143
    address = 0x390676
    hp = 140
    speed = 25
    attack = 90
    defense = 50
    magic_attack = 39
    magic_defense = 73
    fp = 100
    evade = 40
    morph_chance = 3
    sound_on_approach = 2
    weaknesses = [4]
    palette = 8
    flower_bonus_type = 5
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x3917c8
    xp = 1
    coins = 30
    yoshi_cookie_item = items.MapleSyrup
    rare_item = items.HoneySyrup


class JinxClone(Enemy):
    index = 144
    address = 0x3911a6
    boss = True
    hp = 320
    speed = 22
    attack = 180
    defense = 120
    magic_defense = 35
    evade = 30
    death_immune = True
    sound_on_hit = 96
    status_immunities = [1, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x39199c
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.2
    ratio_fp = 0.0
    ratio_attack = 1.8
    ratio_defense = 2.0
    ratio_magic_attack = 0.0
    ratio_magic_defense = 0.35
    ratio_speed = 1.8333
    ratio_evade = 1.0
    ratio_magic_evade = 0.0


class MachineMadeShyster(Enemy):
    index = 145
    address = 0x390b06
    hp = 100
    speed = 36
    attack = 135
    defense = 95
    magic_attack = 90
    magic_defense = 65
    fp = 250
    evade = 10
    morph_chance = 3
    sound_on_hit = 80
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3919a2
    yoshi_cookie_item = items.Mushroom


class MachineMadeDrillBit(Enemy):
    index = 146
    address = 0x390b36
    boss = True
    hp = 180
    speed = 24
    attack = 130
    defense = 82
    magic_attack = 31
    magic_defense = 69
    fp = 100
    morph_chance = 3
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3919a8
    yoshi_cookie_item = items.Mushroom


class Formless(Enemy):
    index = 147
    address = 0x390646
    boss = True
    hp = 10
    speed = 2
    magic_attack = 50
    fp = 100
    evade = 100
    death_immune = True
    sound_on_hit = 32
    resistances = [5, 7]
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3919ae
    yoshi_cookie_item = items.Mushroom


class Mokura(Enemy):
    index = 148
    address = 0x390656
    boss = True
    hp = 620
    speed = 25
    attack = 120
    defense = 75
    magic_attack = 80
    magic_defense = 90
    fp = 100
    evade = 20
    magic_evade = 10
    death_immune = True
    sound_on_hit = 32
    resistances = [5, 7]
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3919b4
    xp = 90
    yoshi_cookie_item = items.Mushroom
    normal_item = items.KerokeroCola
    rare_item = items.RoyalSyrup

    model_small = {
        **models[201]
    }
    model_large = {
        "sprite": SpriteName._573_MOKURA,
        "priority_0": True,
        "priority_1": True,
        "priority_2": False,
        "show_shadow": False,
        "shadow": ShadowSize._02_OVAL_BIG,
        "y_pixel_shift": 2,
        "acute_axis": 10,
        "obtuse_axis": 10,
        "height": 8,
        "vram_store": VramStore._00_SWSE_NWNE,
        "vram_size": 0,
        "cannot_clone": False,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False,
        "extra_props": {
            "is_empty": True
        }
    }
    dialog_replacements = [
        (49,'''\n     MOKURA: Uhh... Go away![await]'''),
        (1660, '''\n             Duh, huh, huh...[await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Mokura's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped MOKURA!![await]'''),
        (1778, '''\n            MOKURA: Hmm...[await]'''),
        (1780, '''MOKURA: What're you doing in my\n secret lair?[await]'''),
        (1781, '''MOKURA: I oughtta go back to\n being invisible...[await]'''),
        (1784, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1792, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1793, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (2061, '''CHEF TORTE: Zees cake, ve make\n it look like big cloud! It is...\n masterpiece![await]'''),
        (2504, '''MOKURA: Uhh... You need [0x7024] more\n items...[await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Mokura's busy right now, so he[1] can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Mokura.[await]'''),
        (2831, '''\n       MOKURA: Mwa, ha, ha![await]'''),
        (2838, ''' You will find Mokura...\n in his house. He is...the most\n respected person here.[await]'''),
        (3044, '''MOKURA: Uhh... Are you... gonna\n beat the Dojo Master?[await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Secret-this and Gas-that.[await]'''),
        (3352, '''\n    MOKURA: A cloud can jump...[await]'''),
        (3353, '''\n    MOKURA: A cloud can jump...[await]'''),
    ]


class FireCrystal(Enemy):
    index = 149
    address = 0x391146
    boss = True
    hp = 2500
    speed = 10
    defense = 100
    magic_attack = 130
    magic_defense = 60
    fp = 250
    evade = 10
    death_immune = True
    resistances = [6]
    weaknesses = [4]
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3919ba
    xp = 40
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.6104
    ratio_fp = 1.25
    ratio_attack = 0.0
    ratio_defense = 1.0
    ratio_magic_attack = 1.3
    ratio_magic_defense = 0.75
    ratio_speed = 0.2
    ratio_evade = 1.0
    ratio_magic_evade = 0.0
    
    model_small = {
        **models[405],
        "sprite": 786,
        "extra_props": {
            "sequence": 1,
            "freeze": True,
            "mold": 0
        }
    }


class WaterCrystal(Enemy):
    index = 150
    address = 0x391156
    boss = True
    hp = 1800
    speed = 12
    defense = 130
    magic_attack = 120
    magic_defense = 50
    fp = 250
    evade = 20
    death_immune = True
    resistances = [4]
    weaknesses = [6]
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3919c0
    xp = 30
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.4395
    ratio_fp = 1.25
    ratio_attack = 0.0
    ratio_defense = 1.3
    ratio_magic_attack = 1.2
    ratio_magic_defense = 0.625
    ratio_speed = 0.24
    ratio_evade = 1.0
    ratio_magic_evade = 0.0

    model_small = {
        **models[406],
        "sprite": 789,
        "extra_props": {
            "freeze": True,
            "mold": 0
        }
    }


class EarthCrystal(Enemy):
    index = 151
    address = 0x391166
    boss = True
    hp = 3200
    speed = 1
    defense = 70
    magic_attack = 80
    magic_defense = 33
    fp = 250
    evade = 5
    death_immune = True
    resistances = [7]
    weaknesses = [5]
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3919c6
    xp = 50
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.7813
    ratio_fp = 1.25
    ratio_attack = 0.0
    ratio_defense = 0.7
    ratio_magic_attack = 0.8
    ratio_magic_defense = 0.4125
    ratio_speed = 0.02
    ratio_evade = 1.0
    ratio_magic_evade = 0.0

    model_small = {
        **models[407],
        "sprite": 789,
        "extra_props": {
            "sequence": 1,
            "freeze": True,
            "mold": 0
        }
    }

class WindCrystal(Enemy):
    index = 152
    address = 0x391176
    boss = True
    hp = 800
    speed = 30
    defense = 200
    magic_attack = 60
    magic_defense = 88
    fp = 250
    evade = 30
    death_immune = True
    resistances = [5]
    weaknesses = [7]
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3919cc
    xp = 10
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.1953
    ratio_fp = 1.25
    ratio_attack = 0.0
    ratio_defense = 0.2
    ratio_magic_attack = 0.6
    ratio_magic_defense = 1.1
    ratio_speed = 0.6
    ratio_evade = 1.0
    ratio_magic_evade = 0.0

    model_small = {
        **models[408],
        "sprite": 786,
        "extra_props": {
            "freeze": True,
            "mold": 0
        }
    }

class MarioClone(Enemy):
    index = 153
    address = 0x390d66
    boss = True
    hp = 200
    speed = 20
    attack = 100
    defense = 90
    magic_attack = 33
    magic_defense = 50
    fp = 25
    death_immune = True
    sound_on_hit = 80
    resistances = [6, 7]
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3919d2
    xp = 10
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.1667
    ratio_fp = 0.1
    ratio_attack = 0.8333
    ratio_defense = 1.125
    ratio_magic_attack = 1.65
    ratio_magic_defense = 1.25
    ratio_speed = 5.0
    ratio_evade = 0.0
    ratio_magic_evade = 0.0


class PeachClone(Enemy):
    index = 154
    address = 0x390d76
    boss = True
    hp = 120
    speed = 20
    attack = 90
    defense = 60
    magic_attack = 62
    magic_defense = 70
    fp = 180
    death_immune = True
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3919d8
    xp = 1
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.1
    ratio_fp = 0.72
    ratio_attack = 0.75
    ratio_defense = 0.75
    ratio_magic_attack = 3.1
    ratio_magic_defense = 1.75
    ratio_speed = 5.0
    ratio_evade = 0.0
    ratio_magic_evade = 0.0


class BowserClone(Enemy):
    index = 155
    address = 0x390d86
    boss = True
    hp = 300
    speed = 12
    attack = 130
    defense = 100
    magic_attack = 12
    fp = 1
    death_immune = True
    sound_on_hit = 32
    resistances = [6, 7]
    weaknesses = [4]
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3919de
    xp = 100
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.25
    ratio_fp = 0.004
    ratio_attack = 1.0833
    ratio_defense = 1.25
    ratio_magic_attack = 0.6
    ratio_magic_defense = 0.0
    ratio_speed = 3.0
    ratio_evade = 0.0
    ratio_magic_evade = 0.0


class GenoClone(Enemy):
    index = 156
    address = 0x390d96
    boss = True
    hp = 250
    speed = 30
    attack = 120
    defense = 80
    magic_attack = 60
    magic_defense = 30
    fp = 40
    death_immune = True
    sound_on_hit = 16
    resistances = [4]
    weaknesses = [6]
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3919e4
    xp = 40
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.2083
    ratio_fp = 0.16
    ratio_attack = 1.0
    ratio_defense = 1.0
    ratio_magic_attack = 3.0
    ratio_magic_defense = 0.75
    ratio_speed = 7.5
    ratio_evade = 0.0
    ratio_magic_evade = 0.0


class MallowClone(Enemy):
    index = 157
    address = 0x390da6
    boss = True
    hp = 150
    speed = 14
    attack = 80
    defense = 65
    magic_attack = 70
    magic_defense = 80
    fp = 80
    death_immune = True
    sound_on_hit = 80
    resistances = [4, 5]
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3919ea
    xp = 60
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.125
    ratio_fp = 0.32
    ratio_attack = 0.6667
    ratio_defense = 0.8125
    ratio_magic_attack = 3.5
    ratio_magic_defense = 2.0
    ratio_speed = 3.5
    ratio_evade = 0.0
    ratio_magic_evade = 0.0


class Shyster(Enemy):
    index = 158
    address = 0x390286
    hp = 30
    speed = 18
    attack = 20
    defense = 26
    magic_attack = 18
    magic_defense = 10
    fp = 2
    evade = 10
    morph_chance = 3
    sound_on_hit = 80
    palette = 8
    flower_bonus_type = 3
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x39164e
    xp = 3
    coins = 2
    yoshi_cookie_item = items.HoneySyrup
    normal_item = items.HoneySyrup

    model_small = {
        **models[414]
    }


class Kinklink(Enemy):
    index = 159
    address = 0x390ad6
    boss = True
    hp = 60
    speed = 99
    defense = 10
    fp = 100
    morph_chance = 3
    palette = 16
    flower_bonus_type = 1

    # Reward attributes
    reward_address = 0x3919f0
    yoshi_cookie_item = items.Mushroom


class HanginShy(Enemy):
    index = 161
    address = 0x3911c6
    boss = True
    hp = 10
    speed = 200
    fp = 100
    death_immune = True
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x3919fc
    yoshi_cookie_item = items.Mushroom


class Smelter(Enemy):
    index = 162
    address = 0x390fc6
    boss = True
    hp = 1500
    defense = 120
    magic_defense = 100
    fp = 100
    death_immune = True
    resistances = [6]
    weaknesses = [5]
    status_immunities = [0, 1, 2, 3]
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391a02
    yoshi_cookie_item = items.Mushroom


class MachineMadeMack(Enemy):
    index = 163
    address = 0x390af6
    boss = True
    hp = 300
    speed = 10
    attack = 160
    defense = 120
    magic_attack = 95
    magic_defense = 40
    fp = 250
    death_immune = True
    sound_on_hit = 48
    weaknesses = [5]
    status_immunities = [0, 1, 2, 3]
    palette = 24
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391a08
    xp = 120
    coins = 30
    yoshi_cookie_item = items.Mushroom
    rare_item = items.FireBomb


class MachineMadeBowyer(Enemy):
    index = 164
    address = 0x390b16
    boss = True
    hp = 1000
    speed = 200
    attack = 150
    defense = 120
    magic_attack = 90
    magic_defense = 80
    fp = 250
    death_immune = True
    sound_on_hit = 16
    status_immunities = [0, 1, 2, 3]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391a0e
    xp = 150
    coins = 40
    yoshi_cookie_item = items.Mushroom
    rare_item = items.IceBomb


class MachineMadeYaridovich(Enemy):
    index = 165
    address = 0x390b26
    boss = True
    hp = 800
    speed = 18
    attack = 180
    defense = 130
    magic_attack = 90
    magic_defense = 50
    fp = 250
    death_immune = True
    sound_on_hit = 32
    status_immunities = [0, 1, 2, 3]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391a14
    xp = 180
    coins = 50
    yoshi_cookie_item = items.Mushroom
    rare_item = items.RockCandy


class MachineMadeAxemPink(Enemy):
    index = 166
    address = 0x390b46
    hp = 100
    speed = 35
    attack = 95
    defense = 90
    magic_attack = 40
    magic_defense = 100
    fp = 200
    evade = 25
    magic_evade = 10
    death_immune = True
    sound_on_hit = 48
    resistances = [4]
    weaknesses = [6]
    status_immunities = [0, 1]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 4

    # Reward attributes
    reward_address = 0x391a1a
    xp = 30
    yoshi_cookie_item = items.Mushroom
    rare_item = items.MapleSyrup


class MachineMadeAxemBlack(Enemy):
    index = 167
    address = 0x390b56
    hp = 120
    speed = 55
    attack = 120
    defense = 110
    magic_attack = 4
    magic_defense = 40
    fp = 100
    evade = 30
    death_immune = True
    sound_on_hit = 48
    weaknesses = [5]
    status_immunities = [1, 3]
    palette = 8
    flower_bonus_type = 4
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x391a20
    xp = 20
    yoshi_cookie_item = items.Mushroom
    rare_item = items.MaxMushroom


class MachineMadeAxemRed(Enemy):
    index = 168
    address = 0x390b66
    hp = 180
    speed = 45
    attack = 135
    defense = 95
    magic_attack = 24
    magic_defense = 80
    fp = 100
    evade = 10
    death_immune = True
    sound_on_hit = 48
    resistances = [6]
    weaknesses = [4]
    status_immunities = [1, 3]
    palette = 8
    flower_bonus_type = 5
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391a26
    xp = 50
    yoshi_cookie_item = items.Mushroom
    rare_item = items.RoyalSyrup


class MachineMadeAxemYellow(Enemy):
    index = 169
    address = 0x390b76
    hp = 200
    speed = 20
    attack = 140
    defense = 130
    magic_attack = 16
    magic_defense = 20
    fp = 100
    death_immune = True
    sound_on_hit = 48
    resistances = [5]
    weaknesses = [7]
    status_immunities = [1, 2]
    palette = 8
    flower_bonus_type = 3
    flower_bonus_chance = 8

    # Reward attributes
    reward_address = 0x391a2c
    xp = 25
    yoshi_cookie_item = items.Mushroom
    rare_item = items.MaxMushroom


class MachineMadeAxemGreen(Enemy):
    index = 170
    address = 0x390b86
    hp = 80
    speed = 40
    attack = 105
    defense = 80
    magic_attack = 80
    magic_defense = 120
    fp = 250
    magic_evade = 20
    death_immune = True
    sound_on_hit = 48
    weaknesses = [4]
    status_immunities = [0, 1]
    palette = 8
    flower_bonus_type = 2
    flower_bonus_chance = 4

    # Reward attributes
    reward_address = 0x391a32
    xp = 10
    yoshi_cookie_item = items.Mushroom
    rare_item = items.RoyalSyrup


class Starslap(Enemy):
    index = 176
    address = 0x390306
    boss = True
    hp = 62
    speed = 9
    attack = 25
    defense = 24
    magic_attack = 4
    magic_defense = 10
    fp = 100
    morph_chance = 3
    sound_on_hit = 80
    sound_on_approach = 1
    weaknesses = [5, 6]
    palette = 8
    flower_bonus_type = 4
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x39167e
    xp = 2
    coins = 2
    yoshi_cookie_item = items.Mushroom


class Mukumuku(Enemy):
    index = 177
    address = 0x3904d6
    hp = 108
    speed = 11
    attack = 60
    defense = 47
    magic_attack = 22
    magic_defense = 30
    fp = 100
    magic_evade = 80
    morph_chance = 3
    sound_on_hit = 80
    resistances = [5]
    weaknesses = [6]
    palette = 8
    flower_bonus_type = 5
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391732
    xp = 8
    coins = 1
    yoshi_cookie_item = items.MukuCookie
    rare_item = items.MapleSyrup


class Zeostar(Enemy):
    index = 178
    address = 0x390526
    hp = 90
    speed = 10
    attack = 75
    defense = 60
    magic_attack = 28
    magic_defense = 20
    fp = 4
    morph_chance = 2
    sound_on_hit = 80
    sound_on_approach = 1
    weaknesses = [5, 6]
    palette = 8
    flower_bonus_type = 4
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x391750
    xp = 10
    coins = 3
    yoshi_cookie_item = items.SleepyBomb
    rare_item = items.Mushroom


class Jagger(Enemy):
    index = 179
    address = 0x390d06
    boss = True
    hp = 600
    speed = 30
    attack = 120
    defense = 80
    magic_defense = 50
    fp = 100
    evade = 10
    death_immune = True
    sound_on_hit = 80
    resistances = [6, 7]
    status_immunities = [2]
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391ad4
    xp = 50
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 1.0
    ratio_fp = 1.0

    # shuffled overworld sprites
    overworld_sprite = 237
    overworld_npc = 237
    battle_sprite = 237
    battle_npc = 237
    overworld_extra_sequence = 8
    battle_extra_sequence = 8
    overworld_push_sequence = 4
    battle_push_sequence = 4
    battle_push_length = 48
    overworld_is_skinny = True
    shadow = MED_SHADOW
    overworld_solidity = [4, 4, 11]
    battle_solidity = [4, 4, 11]
    overworld_y_shift = 1
    battle_y_shift = 1
    model_small = {
        **models[156],
        "extra_props": {
            "moleville_animation_sequence": 4,
            "moleville_animation_duration": 38,
            "is_skinny": True,
        }
    }
    dialog_replacements = [
        (49,'''JAGGER: It'd be fun to fight\n again, but I need a nap.[await]'''),
        (1660, ''' Wow, you figured out the\n password! Come on in and let's\n have a spar![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Jagger's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped JAGGER!![await]'''),
        (1778, '''JAGGER: Wow, what a fight! I\n better think about what I'm gonna\n do to win next time...[await]'''),
        (1780, '''JAGGER: Welcome back! I've been\n training hard for our next fight,\n whenever that may be![await]'''),
        (1781, '''JAGGER: Mario, I can't jump as\n high as you. Is this really\n necessary?[await]'''),
        (1784, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1792, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1793, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (2061, '''CHEF TORTE: Zees cake, ve make\n it look like big turtle! It is...\n masterpiece![await]'''),
        (2504, '''JAGGER: Oh, wow, you've already\n found [0x7000] item(s)![await][pause] I bet you'll find\n the last [0x7024] in no time.[await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Jagger's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Jagger.[await]'''),
        (2831, '''\n         JAGGER: Hi, Mario![await]'''),
        (2838, ''' You will find Jagger...\n in his house. He is...the most\n respected person here.[await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Dojo-this and Sensei-that.[await]'''),
        (3353, '''JAGGER: Mario Sensei, the new\n regimen will strengthen us, right?[await]'''),
    ]


class Chompweed(Enemy):
    index = 180
    address = 0x390be6
    boss = True
    hp = 10
    fp = 100
    morph_chance = 3
    sound_on_hit = 16
    sound_on_approach = 2
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391a56
    yoshi_cookie_item = items.Mushroom


class Smithy2TankHead(Enemy):
    index = 181
    address = 0x390ff6
    boss = True
    hp = 8000
    speed = 50
    attack = 250
    defense = 130
    magic_attack = 10
    magic_defense = 50
    fp = 30
    death_immune = True
    sound_on_hit = 80
    weaknesses = [5]
    status_immunities = [0, 1, 2, 3]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391a5c
    yoshi_cookie_item = items.Mushroom


class Smithy2SafeHead(Enemy):
    index = 182
    address = 0x391006
    boss = True
    hp = 8000
    attack = 40
    defense = 150
    magic_attack = 70
    magic_defense = 100
    fp = 120
    death_immune = True
    resistances = [5, 6, 7]
    weaknesses = [4]
    status_immunities = [0, 1, 2, 3]
    palette = 24
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391a62
    yoshi_cookie_item = items.Mushroom


class Microbomb(Enemy):
    index = 184
    address = 0x390c36
    boss = True
    hp = 30
    speed = 15
    attack = 42
    defense = 30
    magic_attack = 6
    magic_defense = 10
    fp = 100
    sound_on_hit = 80
    weaknesses = [6, 7]
    status_immunities = [1]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 4

    # Reward attributes
    reward_address = 0x391a86
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.025
    ratio_fp = 10.0
    ratio_attack = 0.7
    ratio_defense = 0.71
    ratio_magic_attack = 0.27
    ratio_magic_defense = 0.25
    ratio_speed = 1.0
    ratio_evade = 0.0
    ratio_magic_evade = 0.0


class Grit(Enemy):
    index = 186
    address = 0x390c16
    boss = True
    hp = 10
    fp = 100
    morph_chance = 3
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391a74
    yoshi_cookie_item = items.Mushroom


class Neosquid(Enemy):
    index = 187
    address = 0x390f76
    boss = True
    hp = 800
    speed = 20
    attack = 180
    defense = 80
    magic_attack = 86
    magic_defense = 50
    fp = 200
    death_immune = True
    sound_on_hit = 32
    status_immunities = [1]
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391bb2
    xp = 40
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.3636
    ratio_fp = 0.3333
    ratio_attack = 1.5652
    ratio_defense = 0.7407
    ratio_magic_attack = 1.5926
    ratio_magic_defense = 0.8065
    ratio_speed = 0.3077


class YaridovichMirage(Enemy):
    index = 188
    address = 0x390f16
    boss = True
    hp = 500
    speed = 16
    attack = 100
    defense = 40
    magic_attack = 60
    magic_defense = 10
    fp = 100
    sound_on_hit = 32
    weaknesses = [5]
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391a7a
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.3333
    ratio_fp = 1.0
    ratio_attack = 0.8
    ratio_defense = 0.4706
    ratio_magic_attack = 0.8571
    ratio_magic_defense = 0.1333
    ratio_speed = 0.8


class Helio(Enemy):
    index = 189
    address = 0x390e76
    boss = True
    hp = 10
    attack = 140
    fp = 100
    resistances = [6]
    weaknesses = [4]
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391a80
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.0031
    ratio_fp = 0.5
    ratio_attack = 0.8
    ratio_defense = 0.0
    ratio_magic_attack = 0.0
    ratio_magic_defense = 0.0
    ratio_speed = 0.0
    ratio_evade = 0.0
    ratio_magic_evade = 0.0


class RightEye(Enemy):
    index = 190
    address = 0x390f86
    boss = True
    hp = 500
    speed = 17
    attack = 128
    defense = 100
    magic_attack = 82
    magic_defense = 36
    fp = 200
    death_immune = True
    resistances = [5]
    weaknesses = [6, 7]
    status_immunities = [1]
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391ba6
    xp = 30
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.2273
    ratio_fp = 0.3333
    ratio_attack = 1.113
    ratio_defense = 0.9259
    ratio_magic_attack = 1.5185
    ratio_magic_defense = 0.5806
    ratio_speed = 0.2615

    def get_patch(self):
        """Update battle event triggers based on HP to use shuffled HP value instead.

        Returns:
            randomizer.logic.patch.Patch: Patch data

        """
        patch = super().get_patch()

        # TODO: Get addresses for linear mode.
        if self.world.open_mode:
            # Vanilla game gives a 20% bonus when the eye comes back...h*ck it, let's keep it!
            reset_hp = self.round_for_battle_script(self.hp * 1.2)
            patch.add_data(0x35366e, utils.ByteField(
                reset_hp, num_bytes=2).as_bytes())

        return patch

    def patch_script(self):
        script = BattleScript()
        script.if_bits_set(0x7ee002, 0x01)
        script.if_greater_or_equal(0x7ee004, 0x03)
        script.set_targetable(Monsters.SELF)
        script.zero(0x7ee004)
        script.zero(0x7ee002)
        script.animate(0x0d)
        script.wait_return()

        script.if_bits_set(0x7ee002, 0x01)
        script.inc(0x7ee004)
        script.wait_return()

        script.zero(0x7ee005)
        script.rand(0x07)
        script.if_less_than(0x7ee005, 0x04)
        script.cast_spell(spells.Bolt, spells.DiamondSaw, spells.MegaDrain)
        script.wait_return()

        script.cast_spell(spells.FlameStone, spells.DarkStar, spells.Blast)
        script.start_counter()

        script.if_hp(0x0000)
        script.if_bits_clear(0x7ee008, 0x01)
        script.set(0x7ee002, 0x01)
        script.set(0x7ee000, 0x01)
        script.clear(0x7ee000, 0x04)
        script.set_untargetable(Monsters.SELF)

        if self.world.settings.is_flag_enabled(flags.NoGenoWhirlExor):
            script.set_targetable(Monsters.MONSTER_1)
        else:
            script.uninvuln(Targets.MONSTER_1)

        script.animate(0x0b)
        script.battle_dialog(0xdb)
        script.wait_return()

        self.script = script.fin()


class LeftEye(Enemy):
    index = 191
    address = 0x390f96
    boss = True
    hp = 300
    speed = 21
    attack = 153
    defense = 130
    magic_attack = 47
    magic_defense = 80
    fp = 200
    death_immune = True
    resistances = [5]
    weaknesses = [6, 7]
    status_immunities = [1]
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391bac
    xp = 30
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.1364
    ratio_fp = 0.3333
    ratio_attack = 1.3304
    ratio_defense = 1.2037
    ratio_magic_attack = 0.8704
    ratio_magic_defense = 1.2903
    ratio_speed = 0.3231

    def get_patch(self):
        """Update battle event triggers based on HP to use shuffled HP value instead.

        Returns:
            randomizer.logic.patch.Patch: Patch data

        """
        patch = super().get_patch()

        # TODO: Get addresses for linear mode.
        if self.world.open_mode:
            patch.add_data(0x35368e, utils.ByteField(
                self.hp, num_bytes=2).as_bytes())

        return patch

    def patch_script(self):
        script = BattleScript()
        script.if_bits_set(0x7ee003, 0x01)
        script.if_greater_or_equal(0x7ee004, 0x02)
        script.set_targetable(Monsters.SELF)
        script.zero(0x7ee004)
        script.zero(0x7ee003)
        script.animate(0x0d)
        script.wait_return()

        script.if_bits_set(0x7ee003, 0x01)
        script.inc(0x7ee004)
        script.wait_return()

        script.zero(0x7ee005)
        script.rand(0x07)
        script.if_less_than(0x7ee005, 0x04)
        script.set(0x7ee00f, 0x01)
        script.attack(attacks.PhysicalAttack0,
                      attacks.GunkBall, attacks.PhysicalAttack0)
        script.clear(0x7ee00f, 0x01)
        script.wait_return()

        script.set(0x7ee00f, 0x01)
        script.attack(attacks.PhysicalAttack0,
                      attacks.VenomDrool, attacks.ScrowBell)
        script.clear(0x7ee00f, 0x01)
        script.start_counter()

        script.if_hp(0x0000)
        script.if_bits_clear(0x7ee008, 0x01)
        script.set(0x7ee003, 0x01)
        script.set(0x7ee000, 0x02)
        script.clear(0x7ee000, 0x04)
        script.set_untargetable(Monsters.SELF)

        if self.world.settings.is_flag_enabled(flags.NoGenoWhirlExor):
            script.set_targetable(Monsters.MONSTER_1)
        else:
            script.uninvuln(Targets.MONSTER_1)

        script.animate(0x0c)
        script.battle_dialog(0xdb)
        script.wait_return()

        self.script = script.fin()


class KnifeGuy(Enemy):
    index = 192
    address = 0x390c66
    boss = True
    hp = 700
    speed = 25
    attack = 70
    defense = 55
    magic_attack = 20
    magic_defense = 10
    fp = 35
    death_immune = True
    sound_on_hit = 32
    resistances = [5]
    weaknesses = [6]
    status_immunities = [1]
    palette = 24
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391aa4
    xp = 40
    coins = 15
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.44
    ratio_fp = 0.41
    ratio_attack = 1.08
    ratio_defense = 1.15
    ratio_magic_attack = 0.87
    ratio_magic_defense = 0.4
    ratio_speed = 1.25

    model_small = {
        **models[134],
        "extra_props": {
            "is_wide": True
        }
    }
    model_large = {**models[448]}


class GrateGuy(Enemy):
    index = 193
    address = 0x390c76
    boss = True
    hp = 900
    speed = 14
    attack = 60
    defense = 40
    magic_attack = 25
    magic_defense = 40
    fp = 50
    death_immune = True
    sound_on_hit = 96
    resistances = [6]
    weaknesses = [5]
    status_immunities = [1]
    palette = 24
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391aaa
    xp = 50
    coins = 10
    yoshi_cookie_item = items.Mushroom
    normal_item = items.FlowerJar
    rare_item = items.FlowerJar

    # Boss shuffle attributes.
    ratio_hp = 0.56
    ratio_fp = 0.59
    ratio_attack = 0.92
    ratio_defense = 0.83
    ratio_magic_attack = 1.09
    ratio_magic_defense = 1.6
    ratio_speed = 0.7

    # shuffled overworld sprites
    sprite_width = 41
    sprite_height = 57
    sidekicks = [192]

    model_small = {
        **models[452],
        "extra_props": {
            "statue_west_shift": 3,
            "opposite_statue_west_shift": 2
        }
    }
    model_large = {
        **models[449],
        "extra_props": {
            "is_tall": True,
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 44
        }
    }
    dialog_replacements = [
        (49,'''GRATE GUY: Get lost, buddy, I'm\n busy![await]'''),
        (1660, ''' Oh, a patron![delay_30] Come on in and let's\n get this show on the road![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Knife Guy and Grate Guy's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped KNIFE GUY\n and GRATE GUY!![await]'''),
        (1778, '''GRATE GUY: Yikes, you're pretty\n tough! I need some time to recover.[await]'''),
        (1780, '''GRATE GUY: It's so boring\n around here... Hey Mario, wanna\n play "Look the other way" with me?[await][page]\n Just kidding![await]'''),
        (1781, '''GRATE GUY: Sorry, Mario, but\n jumping on my head isn't going to\n teach you Blizzard.[await]'''),
        (1784, '''KNIFE GUY: No, I'm not giving you the Bright Card down here![await]'''),
        (2061, '''CHEF TORTE: Zees cake, ve make\n it look like big clown! It is...\n masterpiece![await]'''),
        (2504, '''GRATE GUY: Hm?[await][pause] Well, you took all\n the trouble to find [0x7000] item(s),\n so... keep looking for the other [0x7024]![await]\n I can stick around all day.[await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Knife Guy and Grate Guy are busy\n right now, so they can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Knife Guy and\n Grate Guy.[await]'''),
        (2831, '''GRATE GUY: Gee, it sure is boring\n around here![await]'''),
        (2838, ''' You will find Grate Guy...\n in his house. He is...the most\n respected person here.[await]'''),
        (3044, '''GRATE GUY: The dojo master's\n much tougher than I am. Think you\n can win?[await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the people\n next door.[await][page]\n They're always mumbling about\n Knife-this and Casino-that.[await]'''),
        (3352, '''GRATE GUY: Look, Mario! I've been\n training so hard, that my ball\n jumps with me![await]'''),
        (3353, '''GRATE GUY: Look, Mario! I've been\n training so hard, that my ball\n jumps with me![await]'''),
    ]

class Bundt(Enemy):
    index = 194
    address = 0x390c86
    boss = True
    hp = 900
    speed = 16
    attack = 65
    defense = 10
    magic_attack = 25
    magic_defense = 50
    fp = 100
    death_immune = True
    sound_on_hit = 16
    resistances = [4, 5, 6]
    weaknesses = [7]
    status_immunities = [1, 2, 3]
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391ab0
    xp = 25
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.6
    ratio_fp = 0.5
    ratio_attack = 0.9559
    ratio_defense = 0.6667
    ratio_magic_attack = 0.8929
    ratio_magic_defense = 1.25
    ratio_speed = 1.0

    # shuffled overworld sprites
    sprite_height = 56
    sprite_width = 35
    
    sidekicks = [142, 142]

    model_small = {
        **models[470],
        "shadow": ShadowSize._02_OVAL_BIG,
        "extra_props": {
            "sequence": 8,
            "freeze": True,
            "statue_west_shift": 3
        }
    }
    model_large = {
        **models[450]
    }
    dialog_replacements = [
        (49,'''\n        (There's no response.)[await]'''),
        (1660, '''\n    (The cake beckons you forth.)[await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Bundt's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped BUNDT!![await]'''),
        # Find some way to do an animation instead of posting dialogue
        (1784, '''CHEF TORTE: Ze apprentice, he\n inseests he saw ze cake MOVE!\n Vhy must he still talk of zees?![await]'''),
        (1785, '''APPRENTICE: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]'''),
        (1792, '''APPRENTICE: You saw it too,\n right? I know I wasn't just\n imagining it![await]'''),
        (1785, '''APPRENTICE: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]'''),
        (2504, '''Wait... Did that cake just move?[await]\n Let's worry about it after finding\n the last [0x7024] item(s).[await]'''), # do this one with no background
        (2560, '''SNIFIT 1: Hello there.[await]\n Bundt's busy right now, so it\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2571, '''[delay_60][end]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Bundt.[await]'''),
        (2831, '''[delay_60][end]'''),
        (2832, ''' Welcome. Our inn services are free\n tonight.[await][pause] We've unfortunately run\n out of complimentary cake, but\n would you like to stay anyway?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]'''),
        (2834, ''' The two guys in the left building\n have been acting suspicious.[await]'''),
        (2836, ''' If you haven't been to the Sunken\n Ship yet, you can get there through\n the whirlpools in the sea.[await]'''),
        (2837, ''' If you haven't been to the Sunken\n Ship yet, you can get there after\n you crash the wedding over in\n Marrymore.[await]'''),
        (2838, ''' Have you been to Bundt's\n house up on the hill yet?[await]'''),
        (2839, ''' Don't disturb the guards at the\n shed. They're uh... guarding a\n very important bake-off![await]'''),
        (2841, ''' Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]'''),
        (2842, ''' Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]'''),
        (2843, ''' Once you get through the Sunken\n Ship, you can... er...[await]'''),
        (2844, ''' You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]'''),
        (2845, ''' I'm just here for kitchen supplies.\n Please leave me alone.[await]'''),
        (2847, ''' You can't just barge in here while\n I'm standing guard.[await]'''),
        (2848, ''' Why's the door locked? [delay]Uh... [delay]We're\n uh... [delay]baking a very important\n cake! [delay]Do not disturb! [delay_30](I'm so sly!)[await]'''),
        (3044, '''[delay_60][end]'''),
        (3338, ''' It's really weird.\n I never hear the next door\n neighbour.[await][pause] Maybe they don't move\n around much.[await]'''),
        (3352, '''[delay_60][end]'''),
        (3353, '''[delay_60][end]'''),
    ]
    optional_dialog_replacements = [
        (1694, '''APPRENTICE: All right, we'll let\n you through. But don't mess our\n cake up, we spent all day on it.[await]'''),
        (1695, '''APPRENTICE: I thought we asked\n you not to mess our cake up![await]'''),
        (2560, '''APPRENTICE: Welcome to our\n world-class culinary school.[await]\n Please come back later to try some\n of our famous Bundt Cake.[await][page]\n [delay]...You want it NOW?\n [delay]How impatient! [delay]I oughtta teach you a lesson![await]'''),
        (2572, '''CHEF TORTE: Ve are busy preparing\n ze batter at ze moment...[await]\n No, you can't have any right zees\n second! [delay]How rude![await]'''),
        (3072, '''APPRENTICE: (Please let this cake\n not be evil... please let this cake\n not be evil...)[await]'''),
        (3073, '''APPRENTICE: You again?! Leave\n our cake alone![await]'''),
    ]

    def get_patch(self):
        """Update battle event triggers based on HP to use shuffled HP value instead.

        Returns:
            randomizer.logic.patch.Patch: Patch data

        """
        patch = super().get_patch()

        if self.world.chocolate_cake:
            data = palette_to_bytes(["A88878", "906858", "906858", "684838", "504028", "382018", "382010", "382818", "201800",
                                     "484020", "483020", "805848", "483020", "806050", "181818"])
            patch.add_data(0x2547AC, data)
        return patch


class Jinx1(Enemy):
    index = 195
    address = 0x390cd6
    boss = True
    hp = 600
    speed = 30
    attack = 140
    defense = 100
    magic_defense = 80
    fp = 100
    evade = 30
    magic_evade = 25
    death_immune = True
    sound_on_hit = 96
    resistances = [4, 5, 6]
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2
    hp_counter_ratios = [0.5]

    # Reward attributes
    reward_address = 0x391ac2
    xp = 75
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 1.0
    ratio_fp = 1.0
    name_override = 'JINX 1'

    # shuffled overworld sprites
    model_small = {
        **models[207],
        "extra_props": {
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 10,
            "is_empty": True,
        }
    }
    dialog_replacements = [
        (49,'''JINX: Please do not disturb me.\n I am training in here.[await]'''),
        (1660, ''' So, you've figured out the\n password. But, I'm not letting you\n through just yet![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Jinx's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped JINX!![await]'''),
        (1778, '''\n   JINX: I was going easy on you![await]'''),
        (1780, '''JINX: I must accept that I have been\n bested. Good work![await]'''),
        (1781, '''JINX: Yes, I am short! Show a little\n respect![await]'''),
        (1784, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1792, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1793, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (2061, '''CHEF TORTE: Zees cake, ve make\n it look like tiny monk! It is...\n masterpiece![await]'''),
        (2504, '''JINX: Hmm.[delay] [0x7000] item(s). Not bad.[await]\n But don't let it get to your head,\n you still have [0x7024] left to find![await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Jinx is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Jinx.[await]'''),
        (2831, '''\n               JINX: Hmm...[await]'''),
        (2838, ''' You will find Jinx...\n in his house. He is...the most\n respected person here.[await]'''),
        (3044, '''JINX: The dojo master is quite\n disciplined. Good luck on your\n challenge.[await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Dojo-this and Ki-that.[await]'''),
        (3352, '''JINX: Master!\n Share your wisdom with us![await]'''),
    ]


class Jinx2(Enemy):
    index = 196
    address = 0x390ce6
    boss = True
    hp = 800
    speed = 32
    attack = 160
    defense = 120
    magic_defense = 90
    fp = 100
    evade = 30
    magic_evade = 25
    death_immune = True
    sound_on_hit = 96
    resistances = [4, 5, 6]
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2
    hp_counter_ratios = [0.5]

    # Reward attributes
    reward_address = 0x391ac8
    xp = 100
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 1.0
    ratio_fp = 1.0
    name_override = 'JINX 2'

    # shuffled overworld sprites
    model_small = {
        **models[415],
        "extra_props": {
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 10,
            "is_empty": True,
        }
    }
    dialog_replacements = [
        (49,'''JINX: Please do not disturb me.\n I am training in here.[await]'''),
        (1660, ''' So, you've figured out the\n password. But, I'm not letting you\n through just yet![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Jinx's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped JINX!![await]'''),
        (1778, '''\n   JINX: I was going easy on you![await]'''),
        (1780, '''JINX: I must accept that I have been\n bested. Good work![await]'''),
        (1781, '''JINX: Yes, I am short! Show a little\n respect![await]'''),
        (1784, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1792, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1793, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (2061, '''CHEF TORTE: Zees cake, ve make\n it look like tiny monk! It is...\n masterpiece![await]'''),
        (2504, '''JINX: Hmm.[delay] [0x7000] item(s). Not bad.[await]\n But don't let it get to your head,\n you still have [0x7024] left to find![await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Jinx is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Jinx.[await]'''),
        (2831, '''\n               JINX: Hmm...[await]'''),
        (2838, ''' You will find Jinx...\n in his house. He is...the most\n respected person here.[await]'''),
        (3044, '''JINX: The dojo master is quite\n disciplined. Good luck on your\n challenge.[await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Dojo-this and Ki-that.[await]'''),
        (3352, '''JINX: Master!\n Share your wisdom with us![await]'''),
    ]


class CountDown(Enemy):
    index = 197
    address = 0x390d26
    boss = True
    hp = 2400
    speed = 5
    defense = 80
    magic_attack = 120
    magic_defense = 80
    fp = 100
    death_immune = True
    weaknesses = [5, 7]
    status_immunities = [0, 1, 2, 3]
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391ada
    xp = 140
    coins = 100
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.5
    ratio_fp = 0.3333
    ratio_attack = 0.0
    ratio_defense = 0.7477
    ratio_magic_attack = 2.2642
    ratio_magic_defense = 1.3333
    ratio_speed = 0.625

    # shuffled overworld sprites
    model_small = {
        **models[454],
        "shadow": ShadowSize._02_OVAL_BIG,
        "extra_props": {
            "freeze": True,
            "is_empty": True,
        }
    }
    dialog_replacements = [
        (49,'''COUNT DOWN: Sometimes, even an\n alarm clock needs to sleep.[await]'''),
        (1660, ''' This is not good![delay_30]\n He figured out the password![delay_30]\n ...We better do something![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Count Down's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped\n COUNT DOWN!![await]'''),
        (1778, '''COUNT DOWN: ...What time is it?\n Time for you to leave![await]'''),
        (1780, '''COUNT DOWN: What are you still\n doing around here? Taking a break,\n huh?[await]'''),
        (1781, '''\n   COUNT DOWN: This is not good![await]'''),
        (1784, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1792, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1793, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (2061, '''CHEF TORTE: Zees cake, ve make\n it look like big bell! It is...\n masterpiece![await]'''),
        (2504, '''COUNT DOWN: You've only got\n [0x7000] item(s)! You're missing [0x7024]![await]\n You better do something![await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Count Down's busy right now, so\n he can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Count Down.[await]'''),
        (2831, '''COUNT DOWN: There's nothing to\n do here![await]'''),
        (2838, ''' You will find Count Down...\n in his house. He is...the most\n respected person here.[await]'''),
        (3044, '''COUNT DOWN: The dojo master will\n be tough to beat![await]'''),
        (3338, ''' It's really weird.\n The guy next door never seems\n to shut his alarm clock off.[await]'''),
        (3352, '''COUNT DOWN: This is a weird\n training regimen for an alarm\n clock![await]'''),
        (3353, '''COUNT DOWN: This is a weird\n training regimen for an alarm\n clock![await]'''),
    ]
    # unsure if this makes sense to do with countdown. dingalings are kinda terrible to vram
    optional_dialog_replacements = [
        (1694, '''DING-A-LING: We failed to stop\n you. Go ahead into Count Down's\n room![await]'''),
        (1695, '''DING-A-LING: You beat Count Down!\n We didn't see that coming![await]'''),
        # come up with something for booster's other replacement dialogs if it's feasible to have 4 bells in curtain room
    ]


class DingALing(Enemy):
    index = 198
    address = 0x390d36
    boss = True
    hp = 1200
    speed = 10
    attack = 180
    defense = 120
    magic_attack = 20
    magic_defense = 50
    fp = 100
    death_immune = True
    weaknesses = [5]
    status_immunities = [0, 1, 2, 3]
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391ae0
    xp = 30
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.25
    ratio_fp = 0.3333
    ratio_attack = 1.5
    ratio_defense = 1.1215
    ratio_magic_attack = 0.3774
    ratio_magic_defense = 0.8333
    ratio_speed = 1.25


class Belome1(Enemy):
    index = 199
    address = 0x390d46
    boss = True
    hp = 500
    speed = 4
    attack = 30
    defense = 25
    magic_attack = 15
    magic_defense = 20
    fp = 30
    magic_evade = 10
    death_immune = True
    sound_on_hit = 160
    weaknesses = [5]
    status_immunities = [1]
    palette = 24
    flower_bonus_type = 1
    flower_bonus_chance = 2
    hp_counter_ratios = [300 / 500]

    # Reward attributes
    reward_address = 0x391ae6
    xp = 30
    coins = 40
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 1.0
    ratio_fp = 1.0
    name_override = 'BELOME 1'

    # shuffled overworld sprites
    sprite_height = 54
    sprite_width = 49

    model_small = {
        "sprite": SpriteName._39_RED_SCARECROW,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": False,
        "shadow": ShadowSize._00_OVAL_SMALL,
        "y_pixel_shift": 0,
        "acute_axis": 8,
        "obtuse_axis": 3,
        "height": 10,
        "vram_store": VramStore._00_SWSE_NWNE,
        "vram_size": 0,
        "cannot_clone": False,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False,
        "extra_props": {
            "is_empty": True,
            "invert_se_sw": True,
        }
    }
    model_large = {
        **models[371],
        "extra_props": {
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 38
        }
    }
    dialog_replacements = [
        (49,'''\n        BELOME: Good night~![await]'''),
        (1660, ''' Oh, is it dinner time already?\n Come on in...[delay_60] if you dare~![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Belome's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped BELOME!![await]'''),
        (1778, '''BELOME: You look tasty! If you\n stick around any longer, I might\n just have a snack![await]'''),
        (1780, '''BELOME: Oh, you're back![await]\n Did you bring any food?[await]'''),
        (1781, '''BELOME: Say, it's past my bedtime.\n Can you get off of my head?[await]'''),
        (1784, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1792, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1793, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (2061, '''CHEF TORTE: Zees cake, ve make\n it look like big dog! It is...\n masterpiece![await]'''),
        (2504, '''BELOME: Oh, no, you're still\n missing [0x7024] item(s).[await][pause] I can't wait any\n longer to see what today's cake\n will be.[await][pause] I'm STARVING![await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Belome's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Belome.[await]'''),
        (2831, '''BELOME: It's dreadfully boring\n around here~![await]'''),
        (2838, ''' You will find Belome...\n in his house. He is...the most\n respected person here.[await]'''),
        (3044, '''BELOME: Ooh, how exciting~!\n [delay]The dojo master has challenged\n you![await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Scarecrow-this and Hungry-that.[await]'''),
        (3352, '''BELOME: This training regimen is\n giving me quite the appetite![await]'''),
        (3353, '''BELOME: This training regimen is\n giving me quite the appetite![await]'''),
    ]


class Belome2(Enemy):
    index = 200
    address = 0x390d56
    boss = True
    hp = 1200
    speed = 4
    attack = 120
    defense = 80
    magic_attack = 20
    magic_defense = 40
    fp = 250
    magic_evade = 25
    death_immune = True
    sound_on_hit = 160
    status_immunities = [1]
    palette = 24
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391aec
    xp = 80
    coins = 20
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 1.0
    ratio_fp = 1.0
    name_override = 'BELOME 2'

    # shuffled overworld sprites
    sprite_height = 54
    sprite_width = 49

    model_small = {
        "sprite": SpriteName._39_RED_SCARECROW,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": False,
        "shadow": ShadowSize._00_OVAL_SMALL,
        "y_pixel_shift": 0,
        "acute_axis": 8,
        "obtuse_axis": 3,
        "height": 10,
        "vram_store": VramStore._00_SWSE_NWNE,
        "vram_size": 0,
        "cannot_clone": False,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False,
        "extra_props": {
            "is_empty": True,
            "invert_se_sw": True,
        }
    }
    model_large = {
        **models[371],
        "extra_props": {
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 38
        }
    }
    dialog_replacements = [
        (49,'''\n        BELOME: Good night~![await]'''),
        (1660, ''' Oh, is it dinner time already?\n Come on in...[delay_60] if you dare~![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Belome's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped BELOME!![await]'''),
        (1778, '''BELOME: You look tasty! If you\n stick around any longer, I might\n just have a snack![await]'''),
        (1780, '''BELOME: Oh, you're back![await]\n Did you bring any food?[await]'''),
        (1781, '''BELOME: Say, it's past my bedtime.\n Can you get off of my head?[await]'''),
        (1784, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1792, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1793, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (2061, '''CHEF TORTE: Zees cake, ve make\n it look like big dog! It is...\n masterpiece![await]'''),
        (2504, '''BELOME: Oh, no, you're still\n missing [0x7024] item(s).[await][pause] I can't wait any\n longer to see what today's cake\n will be.[await][pause] I'm STARVING![await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Belome's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Belome.[await]'''),
        (2831, '''BELOME: It's dreadfully boring\n around here~![await]'''),
        (2838, ''' You will find Belome...\n in his house. He is...the most\n respected person here.[await]'''),
        (3044, '''BELOME: Ooh, how exciting~!\n [delay]The dojo master has challenged\n you![await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Scarecrow-this and Hungry-that.[await]'''),
        (3352, '''BELOME: This training regimen is\n giving me quite the appetite![await]'''),
        (3353, '''BELOME: This training regimen is\n giving me quite the appetite![await]'''),
    ]


class Smilax(Enemy):
    index = 202
    address = 0x390dc6
    boss = True
    hp = 200
    speed = 5
    attack = 100
    defense = 80
    magic_attack = 70
    magic_defense = 50
    fp = 100
    death_immune = True
    sound_on_hit = 16
    weaknesses = [4]
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391af8
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.0769
    ratio_fp = 0.1111
    ratio_attack = 0.71
    ratio_defense = 1.0
    ratio_magic_attack = 1.0
    ratio_magic_defense = 0.63
    ratio_speed = 2.50

    model_small = {**models[458]}

class Thrax(Enemy):
    index = 203
    address = 0x390dd6
    boss = True
    hp = 10
    speed = 200
    fp = 100
    death_immune = True
    status_immunities = [1]
    palette = 24
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391afe
    yoshi_cookie_item = items.Mushroom


class Megasmilax(Enemy):
    index = 204
    address = 0x390de6
    boss = True
    hp = 1000
    speed = 2
    attack = 140
    defense = 80
    magic_attack = 70
    magic_defense = 80
    fp = 100
    death_immune = True
    sound_on_hit = 32
    weaknesses = [4]
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391b04
    xp = 120
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes
    anchor = True
    ratio_hp = 0.3846
    ratio_fp = 0.1111

    # shuffled overworld sprites
    sprite_width = 37
    sprite_height = 37
    sidekicks = [7, 7, 7, 7]
    czar = 202
    	
    model_small = {
        **models[263],
        "extra_props": {
            "is_skinny": True,
            "statue_west_shift": 1,
            "statue_south_shift": 4,
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 22
        }
    }
    model_large = {
        **models[460],
        "extra_props": {
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 20
        }
    }
    dialog_replacements = [
        (49,'''MEGASMILAX: I'm thirsty.[await][pause] Can you\n ask Shy Away to come back here,[delay]\n please?[await]'''),
        (1660, ''' Hm?[delay_30] Not often we get visitors\n down here.[delay_30] Come in...[delay_60]\n at your own risk, that is![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Megasmilax's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped\n MEGASMILAX!![await]'''),
        (1778, '''\n      MEGASMILAX: I'm thirsty.[await]'''),
        (1780, '''MEGASMILAX: You'd think it\n wouldn't be so difficult to get\n watered around here, when we're\n literally underwater.[await]'''),
        (1781, '''MEGASMILAX: Careful. I have sharp\n teeth.[await]'''),
        (1784, '''SMILAX: I guess salt water\n wouldn't be very good for us.[await]'''),
        (1785, '''SMILAX: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]'''),
        (1792, '''SMILAX: I guess salt water\n wouldn't be very good for us.[await]'''),
        (1793, '''SMILAX: I guess salt water\n wouldn't be very good for us.[await]'''),
        (2061, '''SMILAX: We're making this cake\n in honour of Megasmilax.[await]'''),
        (2062, '''SMILAX: I hope the wedding party\n likes it. If they don't... well,\n they DID hire plants to bake a cake.[await]'''),
        (2504, '''MEGASMILAX: Hm?[await]\n [0x7024] more item(s)?[await]\n Don't ask me.[delay] I'm just a plant.[await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Megasmilax is busy right now, so\n he can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Megasmilax.[await]'''),
        (2831, '''\n         MEGASMILAX: Hmm...[await]'''),
        (2832, ''' Hello there. Are you tired?\n We don't charge any fees here,\n if you'd like to stay.[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]'''),
        (2834, ''' The two guys in the left building\n have been acting suspicious.[await]'''),
        (2836, ''' If you haven't been to the Sunken\n Ship yet, you can get there through\n the whirlpools in the sea.[await]'''),
        (2837, ''' If you haven't been to the Sunken\n Ship yet, you can get there after\n you crash the wedding over in\n Marrymore.[await]'''),
        (2838, ''' Have you been to Megasmilax's\n house up on the hill yet?[await]'''),
        (2839, ''' Welcome to our humble little town.\n You're welcome to stick around,\n but keep away from the shed, OK?[await]'''),
        (2841, ''' Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]'''),
        (2842, ''' Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]'''),
        (2843, ''' Once you get through the Sunken\n Ship, you can... er...[await]'''),
        (2844, ''' You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]'''),
        (2845, ''' I'm shopping for some fertilizer.[await]\n [delay]...Don't give me that look!\n [delay]I'm just a plant![await]'''),
        (2847, ''' There's nothing suspicious going on\n in here.[await]'''),
        (2848, ''' We're just two plants growing in\n front of an abandoned door. ...But\n we're not letting you in.[await]'''),
        (3044, '''MEGASMILAX: I would love to\n watch your match with the dojo\n master.[await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Water-this and Fertilizer-that.[await]\n ...[delay]Actually, [delay]that doesn't sound\n so bad![await]'''),
        (3352, '''MEGASMILAX: This is harder than it\n looks. I'm a plant.[await]'''),
        (3353, '''MEGASMILAX: This is harder than it\n looks. I'm a plant.[await]'''),
    ]
    optional_dialog_replacements = [
        (1694, '''SMILAX: Go on ahead to visit\n Megasmilax. But be warned, it's\n pretty tough when it's hydrated.[await]'''),
        (1695, '''SMILAX: Wow, you won![await][pause] Shy Away\n must have watered you more than\n he watered Megasmilax.[await]'''),
        (2560, '''SMILAX: Hello there. Are you the\n gardener?[await][page]\n No?[await][pause] Well, [delay]we didn't call for a\n plumber today... [delay]I better get you\n outta here![await]'''),
        (2572, '''SMILAX: If you didn't come back\n here to water us, you'd better get\n outta here.[await]'''),
        (3072, '''\n          SMILAX: I'm thirsty.[await]'''),
        (3073, '''\n       SMILAX: Careful, I bite.[await]'''),
    ]



class Birdo(Enemy):
    index = 205
    address = 0x390df6
    boss = True
    hp = 777
    speed = 10
    attack = 160
    defense = 130
    magic_attack = 6
    magic_defense = 100
    fp = 100
    death_immune = True
    resistances = [6]
    status_immunities = [0, 1, 2, 3]
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391b0a
    xp = 60
    coins = 30
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes
    ratio_hp = 1.0
    ratio_fp = 1.0

    # shuffled overworld sprites
    sprite_height = 57
    sprite_width = 38
    empty_sidekicks = True
    name_override = 'BIRDETTA'

    sidekicks = [206, 206, 206, 206]

    model_small = {
        **models[462],
        "acute_axis": 2,
        "obtuse_axis": 2,
        "height": 5,
        "y_pixel_shift": 0,
        "extra_props": {
            "is_empty": True
        }
    }
    model_large = {
        **models[461],
        "acute_axis": 11,
        "obtuse_axis": 11,
        "height": 13,
        "extra_props": {
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 42,
            "is_tall": True
        }
    }
    dialog_replacements = [
        (1660, ''' Oh, yay, you've come to play!\n Come on in~![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Birdetta's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped\n BIRDETTA!![await]'''),
        (1778, '''BIRDETTA: Tee hee! Let's play\n again sometime♥![await]'''),
        (1780, '''BIRDETTA: Oh, you didn't forget\n about me! You're so sweet♥![await]'''),
        (1781, '''BIRDETTA: This isn't what I had in\n mind when I said I wanted to play![await]'''),
        (1784, '''EGGBERT: You visiting us has\n really made Birdetta happy.\n Thank you![await]'''),
        (1785, '''EGGBERT: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]'''),
        (1792, '''EGGBERT: You visiting us has\n really made Birdetta happy.\n Thank you![await]'''),
        (1793, '''EGGBERT: You visiting us has\n really made Birdetta happy.\n Thank you![await]'''),
        (2061, '''EGGBERT: We're making this cake\n look just like Birdetta![await]'''),
        (2062, '''EGGBERT: No eggs were harmed\n in the making of this cake.[await]'''),
        (2504, '''BIRDETTA: Hello♥![await]\n ...Oh, no, you're still missing\n [0x7024] items![await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Birdetta's busy right now, so she\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Birdetta.[await]'''),
        (2831, '''\n          BIRDETTA: Hello♥![await]'''),
        (2832, ''' Hello! You've been chosen to stay\n here in our lovely inn for FREE!\n Aren't you lucky?[await]\n Will you stay with us?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]'''),
        (2834, ''' The two guys in the left building\n have been acting suspicious.[await]'''),
        (2836, ''' If you haven't been to the Sunken\n Ship yet, you can get there through\n the whirlpools in the sea.[await]'''),
        (2837, ''' If you haven't been to the Sunken\n Ship yet, you can get there after\n you crash the wedding over in\n Marrymore.[await]'''),
        (2838, ''' Have you been to Birdetta's\n house up on the hill yet?[await]'''),
        (2839, ''' Hi![delay] Welcome to our town![delay]\n Stay away from our shed, OK~?[await]'''),
        (2841, ''' Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]'''),
        (2842, ''' Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]'''),
        (2843, ''' Once you get through the Sunken\n Ship, you can... er...[await]'''),
        (2844, ''' You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]'''),
        (2845, ''' Do you think they sell frying pans\n here?[await]'''),
        (2847, ''' It's perfectly normal for two eggs\n to stand outside a locked house![await]'''),
        (2848, ''' There's nothing weird going on\n here![await]'''),
        (3044, '''BIRDETTA: Ooh, are you gonna play\n with the dojo master?![await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the lady next door.[await][page]\n She's always mumbling about\n Egg-this and Playtime-that.[await]'''),
        (3352, '''BIRDETTA: Thanks for playing with\n me~![await]'''),
        (3353, '''BIRDETTA: Thanks for playing with\n me~![await]'''),
    ]
    optional_dialog_replacements = [
        (1694, '''EGGBERT: Wow, you sure showed\n us! Don't disappoint Birdetta![await]'''),
        (1695, '''EGGBERT: Thanks for playing\n with us today![await]'''),
        (2560, '''EGGBERT: Birdetta's feeling lonely\n today, so feel free to pay her a\n visit upstairs.[await][pause] I'm sure she'd love\n the company.[await][page]\n Just, let me make sure you'll be\n nice, first![await]'''),
        (2572, '''EGGBERT: Pardon me, Birdetta's\n not back here. Please refrain from\n snooping around.[await]'''),
        (3072, '''EGGBERT: What did Birdetta want\n me to do here, again? I'm just an\n egg![await]'''),
        (3073, '''EGGBERT: You're making me so\n mad, I could explode![await]'''),
    ]


class Eggbert(Enemy):
    index = 206
    address = 0x390e16
    boss = True
    hp = 10
    attack = 210
    fp = 100
    death_immune = True
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391b10
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.01
    ratio_fp = 1.0
    ratio_attack = 1.31
    ratio_defense = 0.0
    ratio_magic_attack = 0.0
    ratio_magic_defense = 0.0
    ratio_speed = 0.0
    ratio_evade = 0.0
    ratio_magic_evade = 0.0

    model_small = {
        **models[462],
        "acute_axis": 2,
        "obtuse_axis": 2,
        "height": 5,
        "y_pixel_shift": 0,
        "extra_props": {
            "is_empty": True
        }
    }

class AxemYellow(Enemy):
    index = 207
    address = 0x391086
    boss = True
    hp = 600
    speed = 3
    attack = 170
    defense = 130
    magic_attack = 6
    magic_defense = 60
    fp = 100
    death_immune = True
    sound_on_hit = 48
    resistances = [5]
    weaknesses = [7]
    status_immunities = [1, 2]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391b1c
    xp = 30
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.1579
    ratio_fp = 0.125
    ratio_attack = 1.4783
    ratio_defense = 1.3265
    ratio_magic_attack = 0.1538
    ratio_magic_defense = 0.7229
    ratio_speed = 0.0577
    ratio_evade = 0.0
    ratio_magic_evade = 0.0

    model_small = {
        **models[211],
        "extra_props": {
            "is_wide": True
        }
    }


class Punchinello(Enemy):
    index = 208
    address = 0x390c56
    boss = True
    hp = 1200
    speed = 15
    attack = 60
    defense = 42
    magic_attack = 22
    magic_defense = 40
    fp = 10
    death_immune = True
    sound_on_hit = 32
    resistances = [7]
    status_immunities = [0, 1, 2, 3]
    palette = 16
    flower_bonus_type = 1
    battle_sesw_only = True
    hp_counter_ratios = [2/3, 2/3, 1/3, 1/3]

    # Reward attributes
    reward_address = 0x391a98
    xp = 70
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 1.0
    ratio_fp = 1.0

    # shuffled overworld sprites
    sprite_width = 45
    sprite_height = 45

    sidekicks = [25, 25, 25]

    model_small = {
        **models[145],
        "extra_props": {
            "is_skinny": True
        }
    }
    model_large = {
        **models[464],
        "extra_props": {
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 26
        }
    }
    dialog_replacements = [
        (49,'''PUNCHINELLO: Grrr... Leave me\n alone![await]'''),
        (1660, ''' So... You figured out my\n password.[await]\n If you're not here for an\n autograph, I'll have to test you\n once more to let you through![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Punchinello's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped\n CROCO!![await]'''),
        (1778, '''PUNCHINELLO: Grrr... I'll never get famous\n at this rate![await]'''),
        (1780, '''PUNCHINELLO: You've come back to\n visit? I truly must be famous![await]'''),
        (1781, '''PUNCHINELLO: They say I'm a hot\n head, so it's a bad idea to stand\n on my head.[await]'''),
        (1784, '''\n      BOB-OMB: I need a break.[await]'''),
        (1785, '''BOB-OMB: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]'''),
        (1792, '''\n      BOB-OMB: I need a break.[await]'''),
        (1793, '''\n      BOB-OMB: I need a break.[await]'''),
        (2061, '''BOB-OMB: Doesn't this cake\n look just like Punchinello?[await]'''),
        (2062, '''BOB-OMB: We've gotten quite\n good with fondant.[await]'''),
        (2504, '''PUNCHINELLO: Huh?[delay_30] What the hay?[await]\n Where are the other [0x7024] item(s)?[await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Punchinello's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Punchinello.[await]'''),
        (2831, '''PUNCHINELLO: Hmmm... [delay]Huh?\n [delay]A visitor? [delay]Well, there's not much\n to do around here.[await]'''),
        (2832, ''' Hello there.[await][pause] Today, we've got an\n explosively good deal for you![delay] All\n inn expenses are free of charge.[await]\n Would you like to stay?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]'''),
        (2834, ''' The two guys in the left building\n have been acting suspicious.[await]'''),
        (2836, ''' If you haven't been to the Sunken\n Ship yet, you can get there through\n the whirlpools in the sea.[await]'''),
        (2837, ''' If you haven't been to the Sunken\n Ship yet, you can get there after\n you crash the wedding over in\n Marrymore.[await]'''),
        (2838, ''' Have you been to Punchinello's\n house up on the hill yet?[await]'''),
        (2839, ''' Hello there.[delay] Welcome to our humble\n town. We have the least suspicious\n shed in all the land.[await]'''),
        (2841, ''' Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]'''),
        (2842, ''' Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]'''),
        (2843, ''' Once you get through the Sunken\n Ship, you can... er...[await]'''),
        (2844, ''' You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]'''),
        (2845, ''' I know how this must look, but I'm\n just here to browse the perfectly\n legal goods they're selling.[await]'''),
        (2847, ''' Hello there.[delay] Sorry, but I can't let\n you through this door today.[await]'''),
        (2848, ''' You wouldn't wanna enter this\n house, oh no.[delay] We'll make sure you\n don't enter by accident.[await]'''),
        (3044, '''PUNCHINELLO: A challenge from\n the dojo master, eh? Let's see\n where this goes.[await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Bomb-this and Famous-that.[await]'''),
        (3352, '''PUNCHINELLO: Will this training\n montage be my ticket to stardom?[await]'''),
        (3353, '''PUNCHINELLO: Will this training\n montage be my ticket to stardom?[await]'''),
    ]
    optional_dialog_replacements = [
        (1694, '''BOB-OMB: I guess I was a little\n hot-headed, thinking I could win.\n Go on in to Punchinello's room.[await]'''),
        (1695, '''BOB-OMB: Wow, you beat\n Punchinello! He's not very happy\n about that.[await]'''),
        (2560, '''BOB-OMB: Hello there.[await][pause] If you've\n come for Punchinello's autograph,\n please allow me to buzz you up...[await][page]\n [delay]...You're not here for that?[await]\n [delay]Uh oh, he'll be pretty mad!\n [delay]I'd better do something![await]'''),
        (2572, '''BOB-OMB: There's nothing to see\n back here...[await][pause] I mean that.[await]\n You don't believe me?[await]'''),
        (3072, '''BOB-OMB: I don't look like the\n other bob-ombs here. [delay]That's weird.[await]'''),
        (3073, '''BOB-OMB: You don't think it makes\n sense for a bob-omb to be shooting\n bullets?[await][pause] ...Fight me about it![await]'''),
    ]



class TentaclesRight(Enemy):
    index = 209
    address = 0x390e46
    boss = True
    hp = 260
    speed = 21
    attack = 82
    defense = 50
    magic_attack = 35
    magic_defense = 40
    fp = 100
    sound_on_hit = 64
    weaknesses = [6]
    status_immunities = [0, 1]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391b3a
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.0985
    ratio_fp = 0.1111
    ratio_attack = 0.82
    ratio_defense = 0.625
    ratio_magic_attack = 1.1667
    ratio_magic_defense = 1.0
    ratio_speed = 2.625


class AxemRed(Enemy):
    index = 210
    address = 0x391096
    boss = True
    hp = 800
    speed = 30
    attack = 150
    defense = 100
    magic_attack = 24
    magic_defense = 80
    fp = 100
    evade = 10
    death_immune = True
    sound_on_hit = 48
    resistances = [6]
    weaknesses = [4]
    status_immunities = [1, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391b22
    xp = 40
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.2106
    ratio_fp = 0.125
    ratio_attack = 1.3043
    ratio_defense = 1.0204
    ratio_magic_attack = 0.6154
    ratio_magic_defense = 0.9639
    ratio_speed = 0.5769
    ratio_evade = 0.9091
    ratio_magic_evade = 0.0

class AxemGreen(Enemy):
    index = 211
    address = 0x3910a6
    boss = True
    hp = 450
    speed = 20
    attack = 110
    defense = 60
    magic_attack = 90
    magic_defense = 120
    fp = 200
    magic_evade = 20
    death_immune = True
    sound_on_hit = 48
    weaknesses = [4]
    status_immunities = [0, 1]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391b28
    xp = 20
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.1185
    ratio_fp = 0.25
    ratio_attack = 0.9565
    ratio_defense = 0.6122
    ratio_magic_attack = 0.0
    ratio_magic_defense = 1.4458
    ratio_speed = 0.3846
    ratio_evade = 0.0
    ratio_magic_evade = 4.0

    model_small = {
        **models[212],
        "extra_props": {
            "is_wide": True
        }
    }

class KingBomb(Enemy):
    index = 212
    address = 0x391196
    boss = True
    hp = 500
    defense = 130
    magic_attack = 80
    fp = 100
    death_immune = True
    sound_on_hit = 96
    weaknesses = [6, 7]
    status_immunities = [0, 1, 2, 3]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391a8c
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.3125
    ratio_fp = 0.4
    ratio_attack = 0.0
    ratio_defense = 2.1667
    ratio_magic_attack = 0.6667
    ratio_magic_defense = 0.0
    ratio_speed = 0.0
    ratio_evade = 0.0
    ratio_magic_evade = 0.0

    def patch_script(self):
        script = BattleScript()

        script.if_phase(0x03)
        if self.world.settings.is_flag_enabled(flags.FixMagikoopa):
            script.zero(0x7ee000)
        script.set_targetable(Monsters.MONSTER_1)
        script.cast_spell(spells.BigBang)
        script.remove(0x1b)
        script.wait_return()

        script.start_counter()

        script.if_hp(0x0000)
        script.zero(0x7ee000)
        script.set_targetable(Monsters.MONSTER_1)
        script.animate(0x03)
        script.remove(0x1b)
        script.wait_return()

        self.script = script.fin()

        super().patch_script()


class MezzoBomb(Enemy):
    index = 213
    address = 0x390c46
    boss = True
    hp = 150
    speed = 1
    attack = 70
    defense = 40
    magic_defense = 10
    fp = 100
    sound_on_hit = 96
    weaknesses = [6, 7]
    status_immunities = [1]
    palette = 16
    flower_bonus_type = 3
    flower_bonus_chance = 8

    # Reward attributes
    reward_address = 0x391a92
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.125
    ratio_fp = 10.0
    ratio_attack = 1.17
    ratio_defense = 0.95
    ratio_magic_attack = 0.0
    ratio_magic_defense = 0.25
    ratio_speed = 0.07
    ratio_evade = 0.0
    ratio_magic_evade = 0.0


class Raspberry(Enemy):
    index = 215
    address = 0x390c96
    boss = True
    hp = 600
    speed = 16
    attack = 70
    defense = 20
    magic_attack = 30
    magic_defense = 30
    fp = 100
    death_immune = True
    sound_on_hit = 32
    resistances = [4, 5, 6]
    weaknesses = [7]
    status_immunities = [1, 2, 3]
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391abc
    xp = 50
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.4
    ratio_fp = 0.5
    ratio_attack = 1.0294
    ratio_defense = 1.3333
    ratio_magic_attack = 1.0714
    ratio_magic_defense = 0.75
    ratio_speed = 1.0

    def get_patch(self):
        """Update battle event triggers based on HP to use shuffled HP value instead.

        Returns:
            randomizer.logic.patch.Patch: Patch data

        """
        patch = super().get_patch()

        if self.world.chocolate_cake:
            data = palette_to_bytes(["A88878", "806858", "704838", "685040", "604838", "503828", "685040", "684028", "482820",
                                     "584028", "684838", "382820", "402010", "583828", "281808"])
            patch.add_data(0x254770, data)
        return patch


class KingCalamari(Enemy):
    index = 216
    address = 0x390e26
    boss = True
    hp = 800
    speed = 8
    attack = 100
    defense = 80
    magic_attack = 30
    magic_defense = 40
    fp = 100
    death_immune = True
    sound_on_hit = 176
    weaknesses = [6]
    status_immunities = [0, 1, 2, 3]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391b40
    xp = 100
    coins = 100
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes
    anchor = True
    ratio_hp = 0.303
    ratio_fp = 0.1111

    # shuffled overworld sprites
    sprite_width = 34
    sprite_height = 52

    model_small = {
        **models[266],
        "extra_props": {
            "is_skinny": True,
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 34
        }
    }
    model_large = {
        **models[465],
        "extra_props": {
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 35
        }
    }
    dialog_replacements = [
        (49,'''KING CALAMARI: My species\n doesn't normally hatch from eggs\n quite this large.[await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n King Calamari's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped\n KING CALAMARI!![await]'''),
        (1778, '''KING CALAMARI: I can't believe I\n was defeated in the ship I sunk\n myself...[await]'''),
        (1780, '''KING CALAMARI: Win or lose, I'm\n still king of this ship.[await]'''),
        (1781, '''KING CALAMARI: I'm pretty slimy,\n so this seems like a bad idea.[await]'''),
        (1784, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1792, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1793, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (2061, '''CHEF TORTE: Zees cake, ve make\n it look like big squid! It is...\n masterpiece![await]'''),
        (2504, '''KING CALAMARI: Sorry, I don't\n have any hint memos for where you\n can find the last [0x7024] item(s).[await]'''), # do this one with no background
        (2560, '''SNIFIT 1: Hello there.[await]\n King Calamari's busy right now, so\n he can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering King Calamari.[await]'''),
        (2831, '''KING CALAMARI: It's not so weird\n for a squid to run a rown.[await]'''),
        (2838, ''' You will find King Calamari...\n in his house. He is...the most\n respected person here.[await]'''),
        (3044, '''KING CALAMARI: Think you can beat\n the dojo master?[await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Ship-this and Tentacle-that.[await]'''),
        (3352, '''KING CALAMARI: My tentacles\n shouldn't be able to do this.[await]'''),
        (3353, '''KING CALAMARI: My tentacles\n shouldn't be able to do this.[await]'''),
    ]


class TentaclesLeft(Enemy):
    index = 217
    address = 0x390e36
    boss = True
    hp = 200
    speed = 21
    attack = 87
    defense = 70
    magic_attack = 35
    magic_defense = 23
    fp = 100
    death_immune = True
    sound_on_hit = 64
    weaknesses = [6]
    status_immunities = [0, 1]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391b46
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.0758
    ratio_fp = 0.1111
    ratio_attack = 0.87
    ratio_defense = 1.0
    ratio_magic_attack = 1.1667
    ratio_magic_defense = 0.575
    ratio_speed = 2.625


class Jinx3(Enemy):
    index = 218
    address = 0x390cf6
    boss = True
    hp = 1000
    speed = 35
    attack = 180
    defense = 140
    magic_defense = 100
    fp = 100
    evade = 30
    magic_evade = 25
    death_immune = True
    sound_on_hit = 96
    resistances = [4, 5, 6]
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2
    hp_counter_ratios = [0.6, 0.3]

    # Reward attributes
    reward_address = 0x391ace
    xp = 150
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 1.0
    ratio_fp = 1.0
    name_override = 'JINX 3'

    # shuffled overworld sprites
    model_small = {
        **models[416],
        "extra_props": {
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 10,
            "is_empty": True,
        }
    }
    dialog_replacements = [
        (49,'''JINX: Please do not disturb me.\n I am training in here.[await]'''),
        (1660, ''' So, you've figured out the\n password. But, I'm not letting you\n through just yet![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Jinx's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped JINX!![await]'''),
        (1778, '''\n   JINX: I was going easy on you![await]'''),
        (1780, '''JINX: I must accept that I have been\n bested. Good work![await]'''),
        (1781, '''JINX: Yes, I am short! Show a little\n respect![await]'''),
        (1784, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1792, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1793, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (2061, '''CHEF TORTE: Zees cake, ve make\n it look like tiny monk! It is...\n masterpiece![await]'''),
        (2504, '''JINX: Hmm.[delay] [0x7000] item(s). Not bad.[await]\n But don't let it get to your head,\n you still have [0x7024] left to find![await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Jinx is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Jinx.[await]'''),
        (2831, '''\n               JINX: Hmm...[await]'''),
        (2838, ''' You will find Jinx...\n in his house. He is...the most\n respected person here.[await]'''),
        (3044, '''JINX: The dojo master is quite\n disciplined. Good luck on your\n challenge.[await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Dojo-this and Ki-that.[await]'''),
        (3352, '''JINX: Master!\n Share your wisdom with us![await]'''),
    ]


class Zombone(Enemy):
    index = 219
    address = 0x390e56
    boss = True
    hp = 1800
    speed = 6
    attack = 190
    defense = 60
    magic_attack = 80
    magic_defense = 100
    fp = 100
    magic_evade = 10
    death_immune = True
    sound_on_hit = 32
    resistances = [4, 6]
    weaknesses = [5, 7]
    status_immunities = [1, 2, 3]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391b4c
    xp = 50
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.5625
    ratio_fp = 0.5
    ratio_attack = 1.0857
    ratio_defense = 0.75
    ratio_magic_attack = 0.8
    ratio_magic_defense = 1.1765
    ratio_speed = 0.4615
    ratio_evade = 0.0
    ratio_magic_evade = 2.0


class CzarDragon(Enemy):
    index = 220
    address = 0x390e66
    boss = True
    hp = 1400
    speed = 20
    attack = 160
    defense = 100
    magic_attack = 120
    magic_defense = 70
    fp = 100
    evade = 20
    death_immune = True
    sound_on_hit = 32
    resistances = [6]
    weaknesses = [4]
    status_immunities = [1]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391b52
    xp = 100
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.4375
    ratio_fp = 0.5
    ratio_attack = 0.9143
    ratio_defense = 1.25
    ratio_magic_attack = 1.2
    ratio_magic_defense = 0.8235
    ratio_speed = 1.5385
    ratio_evade = 2.0
    ratio_magic_evade = 0.0

    # shuffled overworld sprites
    sidekicks = [21, 21, 21, 21]
    sprite_width = 59
    sprite_height = 54
    model_small = {
        **models[277],
        "extra_props": {
            "is_skinny": True,
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 30
        }
    }
    model_large = {
        **models[216],
        "extra_props": {
            "is_wide": True
        }
    }
    dialog_replacements = [
        (49,'''\n    CZAR DRAGON: BLARRGGGG[await]'''),
        (1660, ''' BLARRGGGG[await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n the Czar Dragon's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped\n the CZAR DRAGON!![await]'''),
        (1778, '''\n    CZAR DRAGON: BLARRGGGG[await]'''),
        (1780, '''\n    CZAR DRAGON: BLARRGGGG[await]'''),
        (1781, '''\n    CZAR DRAGON: BLARRGGGG[await]'''),
        (1784, '''[delay_60][end]'''),
        (1785, '''[delay_60][end]'''),
        (1792, '''[delay_60][end]'''),
        (1793, '''[delay_60][end]'''),
        (2061, '''[delay_60][end]'''),
        (2062, '''[delay_60][end]'''),
        (2504, '''CZAR DRAGON: BLARRGGGG[await]'''), # can we make him say BLARG as many times as you have items remaining?
        (2560, '''SNIFIT 1: Hello there.[await]\n The Czar Dragon's busy right now,\n so it can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2571, '''BLARRGGGG?[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering the Czar Dragon.[await]'''),
        (2831, '''\n  CZAR DRAGON: BLAAARRRGGGG[await]'''),
        (2832, ''' (Stay in the inn for free?)[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]'''),
        (2834, '''[delay_60][end]'''),
        (2836, '''[delay_60][end]'''),
        (2837, '''[delay_60][end]'''),
        (2838, '''[delay_60][end]'''),
        (2839, '''[delay_60][end]'''),
        (2841, '''[delay_60][end]'''),
        (2842, '''[delay_60][end]'''),
        (2843, '''[delay_60][end]'''),
        (2844, '''[delay_60][end]'''),
        (2845, '''[delay_60][end]'''),
        (2847, '''[delay_60][end]'''),
        (2848, '''[delay_60][end]'''),
        (3044, '''\n  CZAR DRAGON: BLAAARRRGGGG[await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always yelling about\n BLARRRRG-this and\n BLAHGAHRGGH-that.[await]'''),
        (3352, '''\n  CZAR DRAGON: BLAAARRRGGGG[await]'''),
        (3353, '''\n  CZAR DRAGON: BLAAARRRGGGG[await]'''),
    ]
    optional_dialog_replacements = [
        (1694, '''[delay_60][end]'''),
        (1695, '''[delay_60][end]'''),
        (2560, '''[delay_60][end]'''),
        (2572, '''[delay_60][end]'''),
        (3072, '''[delay_60][end]'''),
        (3073, '''[delay_60][end]'''),
    ]

class Cloaker(Enemy):
    index = 221
    address = 0x390e86
    boss = True
    hp = 1200
    speed = 20
    attack = 170
    defense = 130
    magic_attack = 12
    magic_defense = 20
    fp = 100
    death_immune = True
    sound_on_hit = 48
    status_immunities = [0, 1, 2, 3]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391b58
    xp = 60
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.3934
    ratio_fp = 0.1429
    ratio_attack = 1.1688
    ratio_defense = 1.3
    ratio_magic_attack = 0.2105
    ratio_magic_defense = 0.2222
    ratio_speed = 1.1111

    # shuffled overworld sprites
    sprite_width = 50
    sprite_height = 62

    model_small = {
        **models[249],
        "shadow": ShadowSize._03_BLOCK,
        "acute_axis": 7,
        "obtuse_axis": 7,
        "height": 7,
        "extra_props": {
            "freeze": True,
            "statue_west_shift": 4,
            "statue_south_shift": 3
        }
    }
    #may have to adjust these props
    model_large = {
        **models[371],
        "extra_props": {
            "is_tall": True,
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 42
        }
    }
    dialog_replacements = [
        (49,'''CLOAKER: I'm busy wallowing in\n misery at my defeat here.[await][pause] Get lost![await]'''),
        (1660, ''' Uh oh, you cracked the code...\n I don't like where this is going...[await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Cloaker and Domino's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped\n CLOAKER and DOMINO!![await]'''),
        (1778, '''CLOAKER: Guess you're tougher\n than I thought...[await]'''),
        (1780, '''\n CLOAKER: So, you've returned...![await]'''),
        (1781, '''CLOAKER: I don't like where this is\n going...[await]'''),
        (1784, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1792, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1793, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (2061, '''CHEF TORTE: Zees cake, ve make\n it look like big brick! It is...\n masterpiece![await]'''),
        (2504, '''CLOAKER: Hee hee hee... You still\n need to find [0x7024] more item(s)![await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Cloaker and Domino are busy right\n now, so they can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Cloaker and Domino.[await]'''),
        (2831, '''CLOAKER: Hee hee hee... So you've\n found our little town! Boring,\n isn't it?[await]'''),
        (2838, ''' You will find Cloaker...\n in his house. He is...the most\n respected person here.[await]'''),
        (3044, '''CLOAKER: Hee hee hee... So you're\n challenging the dojo master?[await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the people\n next door.[await][page]\n They're always mumbling about\n Weaklings-this and Snake-that.[await]'''),
        (3352, '''CLOAKER: This is exactly the kind\n of training I needed.[await][pause] Fusing myself\n with a snake just hasn't been\n getting me the results I wanted.[await]'''),
        (3353, '''CLOAKER: This is exactly the kind\n of training I needed.[await][pause] Fusing myself\n with a snake just hasn't been\n getting me the results I wanted.[await]'''),
    ]



class Domino(Enemy):
    index = 222
    address = 0x390eb6
    boss = True
    hp = 900
    speed = 25
    attack = 65
    defense = 80
    magic_attack = 120
    magic_defense = 150
    fp = 250
    death_immune = True
    sound_on_hit = 16
    status_immunities = [0, 1, 2, 3]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391b5e
    xp = 60
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.2951
    ratio_fp = 0.3571
    ratio_attack = 0.4221
    ratio_defense = 0.8
    ratio_magic_attack = 2.1053
    ratio_magic_defense = 1.6667
    ratio_speed = 1.3889


class MadAdder(Enemy):
    index = 223
    address = 0x390ed6
    boss = True
    hp = 1500
    speed = 10
    attack = 150
    defense = 70
    magic_attack = 90
    magic_defense = 180
    fp = 250
    death_immune = True
    sound_on_hit = 32
    status_immunities = [0, 1, 2, 3]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391b64
    xp = 200
    yoshi_cookie_item = items.Mushroom
    normal_item = items.Crystalline
    rare_item = items.Crystalline

    # Boss shuffle attributes.
    ratio_hp = 0.4918
    ratio_fp = 0.3571
    ratio_attack = 0.974
    ratio_defense = 0.7
    ratio_magic_attack = 1.5789
    ratio_magic_defense = 2.0
    ratio_speed = 0.5556


class Mack(Enemy):
    index = 224
    address = 0x390ee6
    boss = True
    hp = 480
    speed = 8
    attack = 22
    defense = 25
    magic_attack = 15
    magic_defense = 20
    fp = 28
    death_immune = True
    sound_on_hit = 48
    weaknesses = [5]
    status_immunities = [0, 1, 2, 3]
    palette = 24
    flower_bonus_type = 1

    # Reward attributes
    reward_address = 0x391b7c
    xp = 24
    coins = 20
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes
    anchor = True
    ratio_hp = 0.8

    # shuffled overworld sprites
    sprite_height = 57
    sprite_width = 43
    sidekicks = [158, 158, 158, 158]

    model_small = {
        **models[414],
        "extra_props": {
            "moleville_animation_sequence": 4,
            "moleville_animation_duration": 54,
            "is_skinny": True
        }
    }
    model_large = {
        **models[480],
        "extra_props": {
            "sequence": 7,
            "is_tall": True
        }
    }
    dialog_replacements = [
        (49,'''MACK: Party's over. I'm going to\n sleep.[await]'''),
        (1660, ''' Listen, bub![await]\n You may have figured out my\n password, but you still gotta get\n past me if you want through![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Mack's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped MACK!![await]'''),
        (1778, '''\n   MACK: Guess the party's over.[await]'''),
        (1780, '''MACK: Hey Mario! Come back to\n crash our party?[await]'''),
        (1781, '''MACK: OK, I get it, you can bounce\n too.[await]'''),
        (1784, '''BODYGUARD: There's no hard\n feelings. We're all just trying to\n have a good time.[await]'''),
        (1785, '''BODYGUARD: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]'''),
        (1792, '''BODYGUARD: There's no hard\n feelings. We're all just trying to\n have a good time.[await]'''),
        (1793, '''BODYGUARD: There's no hard\n feelings. We're all just trying to\n have a good time.[await]'''),
        (2061, '''BODYGUARD: Doesn't this cake\n look just like Mack?[await]'''),
        (2062, '''BODYGUARD: We've gotten REAL\n good with fondant![await]'''),
        (2504, '''MACK: I'm not happy to delay the\n party, but we can't get started\n until you find [0x7024] more item(s)![await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Mack's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Mack.[await]'''),
        (2831, '''\n   MACK: What are you doing here?[await]'''),
        (2832, ''' Yo! You look tired.[delay] How 'bout a\n night on the house?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]'''),
        (2834, ''' The two guys in the left building\n have been acting suspicious.[await]'''),
        (2836, ''' If you haven't been to the Sunken\n Ship yet, you can get there through\n the whirlpools in the sea.[await]'''),
        (2837, ''' If you haven't been to the Sunken\n Ship yet, you can get there after\n you crash the wedding over in\n Marrymore.[await]'''),
        (2838, ''' Have you been to Mack's house\n up on the hill yet?[await]'''),
        (2839, ''' Yo! It's fine if you hang out in\n town, but... [delay]stay away from the\n shed![await]'''),
        (2841, ''' Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]'''),
        (2842, ''' Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]'''),
        (2843, ''' Once you get through the Sunken\n Ship, you can... er...[await]'''),
        (2844, ''' You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]'''),
        (2845, ''' You trying to snoop on what I'm\n buying here?[await]'''),
        (2847, '''\n       What're YOU lookin' at?[await]'''),
        (2848, '''\n               Beat it, bub![await]'''),
        (3044, '''MACK: Think you're gonna beat the\n dojo master today?[await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Bouncing-this and Party-that.[await]'''),
        (3352, '''MACK: I guess you CAN bounce\n after all.[await]'''),
        (3353, '''MACK: I guess you CAN bounce\n after all.[await]'''),
    ]
    optional_dialog_replacements = [
        (1694, '''BODYGUARD: Think you're tough,\n pal?[await][delay] March that ugly mustache into\n Mack's room, and see what\n happens![await]'''),
        (1695, '''BODYGUARD: You beat Mack?[await]\n This is not good![delay_30]\n I guess you can bounce after all.[await]'''),
        (2560, '''BODYGUARD: Welcome![await][pause] Our party is invitation-only, so\n please come back another time.[await][page]\n[delay] ...You're here to crash it anyway?[delay]\n Alright, wise guy, let's go![await]'''),
        (2572, '''\n   BODYGUARD: Oh, no you don't![0][await]'''),
        (3072, '''BODYGUARD: I almost feel bad\n for all those fools out there,\n who can't even bounce...[await]'''),
        (3073, '''BODYGUARD: How 'bout a fat lip to\n go with that ugly moustache?[await]'''),
    ]


class Bodyguard(Enemy):
    index = 225
    address = 0x390ef6
    boss = True
    hp = 30
    speed = 15
    attack = 20
    defense = 22
    magic_attack = 19
    magic_defense = 12
    fp = 3
    evade = 10
    sound_on_hit = 80
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 3
    flower_bonus_chance = 3

    # Reward attributes
    reward_address = 0x391b82
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes
    ratio_hp = 0.05
    ratio_fp = 0.1071
    ratio_attack = 0.91
    ratio_defense = 0.88
    ratio_magic_attack = 1.27
    ratio_magic_defense = 0.6
    ratio_speed = 1.88
    ratio_evade = 0.1
    ratio_magic_evade = 0.0


class Yaridovich(Enemy):
    index = 226
    address = 0x390f06
    boss = True
    hp = 1500
    speed = 20
    attack = 125
    defense = 85
    magic_attack = 70
    magic_defense = 75
    fp = 100
    death_immune = True
    sound_on_hit = 32
    weaknesses = [5]
    status_immunities = [0, 1, 2, 3]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391b88
    xp = 120
    coins = 50
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 1.0
    ratio_fp = 1.0
    battle_push_length = 78

    # shuffled overworld sprites
    sprite_width = 56
    sprite_height = 84

    sidekick_models = [39, 39, 39, 39]

    model_small = {
        **models[40],
        "extra_props": {
            "is_skinny": True
        }
    }
    model_large = {
        **models[421],
        "sprite": SpriteName._482_YARIDOVICH,
        "shadow": ShadowSize._02_OVAL_BIG,
        "extra_props": {
            "is_tall": True,
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 78
        }
    }
    dialog_replacements = [
        (49,'''YARIDOVICH: How could I lose to\n those... Huh? Hey, get lost![await]'''),
        (1660, ''' Eee hee hee! So, you've cracked the\n code... Now, it's time for the\n REAL test![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Yaridovich's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped\n YARIDOVICH!![await]'''),
        (1778, '''YARIDOVICH: Ridiculous! How could a\n genius like me lose to them...?[await]'''),
        (1780, '''YARIDOVICH: I'm thinking it might\n be time for me to switch careers.[await][page]\n Say, do you happen to know anyone\n who's looking to hire a\n hydrodemolitions expert?[await]'''),
        (1781, '''YARIDOVICH: This is just adding\n insult to injury![await]'''),
        (1784, '''TOWNSPERSON: We must.. be\n careful. We could rust.. down here.[await]'''),
        (1785, '''TOWNSPERSON: Hop on... then trampoline... in the next room.\n It'll take you... outside.[await]'''),
        (1792, '''TOWNSPERSON: We must.. be\n careful. We could rust.. down here.[await]'''),
        (1793, '''TOWNSPERSON: We must.. be\n careful. We could rust.. down here.[await]'''),
        (2061, '''TOWNSPERSON: We must... make\n this cake... look exactly...\n like Yaridovich.[await]'''),
        (2062, '''TOWNSPERSON: We need... more\n fondant.[await]'''),
        (2504, '''YARIDOVICH: Eee hee...! You're\n still missing [0x7024] item(s)! Isn't that\n a shame?[await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Yaridovich is busy right now, so\n he can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Yaridovich.[await]'''),
        (3044, '''YARIDOVICH: A challenge from the\n dojo master? [delay]Eee hee hee, this\n ought to be interesting![await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Brownie-this and Tickle-that.[await]'''),
        (3352, '''YARIDOVICH: I guess I wasn't as\n strong as I thought...[await]'''),
        (3353, '''YARIDOVICH: I guess I wasn't as\n strong as I thought...[await]'''),
    ]
    optional_dialog_replacements = [
        (1694, '''TOWNSPERSON: Well done...\n You may go on... to Yaridovich.[await]'''),
        (1695, '''TOWNSPERSON: You won...\n Well done...[await]'''),
        (2560, '''TOWNSPERSON: I'm just... a\n secretary. Don't bother...\n Yaridovich.[await]'''),
        (2572, '''TOWNSPERSON: This is...not...\n the right...way.[await]'''),
        (3072, '''TOWNSPERSON: It's nice...\n outside.[await]'''),
        (3073, '''TOWNSPERSON: You want...to\n fight?[await]'''),
    ]


class DrillBit(Enemy):
    index = 227
    address = 0x390f26
    boss = True
    hp = 80
    speed = 15
    attack = 85
    defense = 70
    magic_attack = 40
    magic_defense = 56
    fp = 100
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x39179e
    xp = 11
    coins = 1
    yoshi_cookie_item = items.Mushroom


class AxemPink(Enemy):
    index = 228
    address = 0x3910b6
    boss = True
    hp = 400
    speed = 25
    attack = 120
    defense = 80
    magic_attack = 80
    magic_defense = 100
    fp = 200
    evade = 25
    magic_evade = 10
    death_immune = True
    sound_on_hit = 48
    resistances = [4]
    weaknesses = [6]
    status_immunities = [0, 1]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391b2e
    xp = 10
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.1053
    ratio_fp = 0.25
    ratio_attack = 1.0435
    ratio_defense = 0.8163
    ratio_magic_attack = 2.0513
    ratio_magic_defense = 1.2048
    ratio_speed = 0.4808
    ratio_evade = 2.2727
    ratio_magic_evade = 2.0

    model_small = {**models[210]}

class AxemBlack(Enemy):
    index = 229
    address = 0x3910c6
    boss = True
    hp = 550
    speed = 35
    attack = 140
    defense = 120
    magic_attack = 4
    magic_defense = 40
    fp = 100
    evade = 30
    death_immune = True
    sound_on_hit = 48
    weaknesses = [5]
    status_immunities = [1, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391b34
    xp = 40
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.1448
    ratio_fp = 0.125
    ratio_attack = 1.2174
    ratio_defense = 1.2245
    ratio_magic_attack = 0.1026
    ratio_magic_defense = 0.4819
    ratio_speed = 0.6731
    ratio_evade = 2.7273
    ratio_magic_evade = 0.0

    model_small = {
        **models[209],
        "extra_props": {
            "is_wide": True
        }
    }

class Bowyer(Enemy):
    index = 230
    address = 0x390f36
    boss = True
    hp = 720
    speed = 10
    attack = 50
    defense = 40
    magic_attack = 30
    magic_defense = 35
    fp = 250
    death_immune = True
    sound_on_hit = 16
    status_immunities = [0, 1, 2, 3]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391b8e
    xp = 60
    coins = 50
    yoshi_cookie_item = items.Mushroom
    normal_item = items.FlowerBox
    rare_item = items.FlowerBox

    # shuffled overworld sprites
    sprite_width = 47
    sprite_height = 52
    sidekicks = [231, 231, 231, 231]

    	
    model_small = {
        **models[487],
        "extra_props": {
            "statue_mold": 3,
            "sequence": 1,
            "freeze": True,
            "is_skinny": True,
        }
    }
    model_large = {
        **models[241],
        "acute_axis": 6,
        "obtuse_axis": 8,
        "height": 16,
        "y_pixel_shift": 1,
        "shadow": ShadowSize._01_OVAL_MED,
        "extra_props": {
            "is_tall": True,
        }
    }
    dialog_replacements = [
        (49,'''BOWYER: Disturb me you must not,\n nya!'''),
        (1660, ''' Nya, NYA?![delay_30] Cracked the code, you\n did! But fight you, I will, nya![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Bowyer's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped BOWYER!![await]'''),
        (1778, '''BOWYER: That was nyat fair!\n Scram you must, nya![await]'''),
        (1780, '''BOWYER: Back again, you are,\n nya? I'm nyat as mad as before.[await]'''),
        (1781, '''BOWYER: Nya, NYA?! Stop this,\n you must![await]'''),
        (1784, '''FLUNKIE: Bowyer is easily\n distracted from his missions. But\n we're off the hook today.[await]'''),
        (1785, '''FLUNKIE: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]'''),
        (1792, '''FLUNKIE: Bowyer is easily\n distracted from his missions. But\n we're off the hook today.[await]'''),
        (1793, '''FLUNKIE: Bowyer is easily\n distracted from his missions. But\n we're off the hook today.[await]'''),
        (2061, '''FLUNKIE: Doesn't this cake\n look just like Bowyer?[await]'''),
        (2062, '''FLUNKIE: We've gotten REAL\n good with fondant![await]'''),
        (2504, '''BOWYER: Nya, NYA!?[await][pause] Disturb me\n you must not, until [0x7024] more item(s)\n you find, nya![await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Bowyer's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Bowyer.[await]'''),
        (2831, '''\nBOWYER: Nya! Boring here, it is...[await]'''),
        (2832, ''' Since I'm having a good day, you\n can stay here free of charge.\n [delay]How's that sound?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]'''),
        (2834, ''' The two guys in the left building\n have been acting suspicious.[await]'''),
        (2836, ''' If you haven't been to the Sunken\n Ship yet, you can get there through\n the whirlpools in the sea.[await]'''),
        (2837, ''' If you haven't been to the Sunken\n Ship yet, you can get there after\n you crash the wedding over in\n Marrymore.[await]'''),
        (2838, ''' Have you been to Bowyer's house\n up on the hill yet?[await]'''),
        (2839, ''' Don't cause any trouble in our\n town! Stay away from the shed![await]'''),
        (2841, ''' Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]'''),
        (2842, ''' Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]'''),
        (2843, ''' Once you get through the Sunken\n Ship, you can... er...[await]'''),
        (2844, ''' You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]'''),
        (2845, ''' I'm just a customer![delay] Let me shop\n in peace![await]'''),
        (2847, ''' There's a very uh... [delay]important\n meeting happening inside.\n [delay]You may not enter.[await]'''),
        (2848, ''' What's going on in here?[await][pause] None of\n your business, that's what![await]'''),
        (3044, '''\n BOWYER: Interesting, this will be![await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Arrow-this and Target-that.[await]'''),
        (3352, '''BOWYER: 1000 jumps I must do,\n nya![await]'''),
        (3353, '''BOWYER: 1000 jumps I must do,\n nya![await]'''),
    ]
    optional_dialog_replacements = [
        (1694, '''FLUNKIE: Whoa! You sure showed\n us! Go on ahead to Bowyer's\n place![await]'''),
        (1695, '''FLUNKIE: Come back and visit\n us sometime. Bowyer won't stay\n mad forever![await]'''),
        (2560, '''FLUNKIE: Hello.[await][pause] Bowyer is busy\n now, and he really hates to be\n interrupted.[await][page]\n[delay] ...If you're not going to leave,\n I'll have to kick you out myself![await]'''),
        (2572, '''FLUNKIE: I'm gonna have to ask you\n not to interrupt Bowyer's target\n practice.[await]'''),
        (3072, '''FLUNKIE: ...sigh... [delay]Bowyer scolded\n me for interrupting his shooting\n practice.[await][pause] I was just trying to warn\n him that Mario is here![await]'''),
        (3073, '''FLUNKIE: You look like you'd make\n for a good statue![await]'''),
    ]


class Aero(Enemy):
    index = 231
    address = 0x390f46
    boss = True
    hp = 10
    fp = 100
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391b94
    yoshi_cookie_item = items.Mushroom

    model_small = {
        **models[487],
        "extra_props": {
            "statue_mold": 3,
            "sequence": 1,
            "freeze": True,
            "is_skinny": True,
        }
    }

class Exor(Enemy):
    index = 233
    address = 0x390f66
    boss = True
    hp = 1800
    speed = 200
    defense = 120
    magic_defense = 80
    death_immune = True
    resistances = [5]
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391ba0
    xp = 100
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.8182
    ratio_fp = 0.0
    ratio_attack = 0.0
    ratio_defense = 1.1111
    ratio_magic_attack = 0.0
    ratio_magic_defense = 1.2903
    ratio_speed = 3.0769

    # shuffled overworld sprites
    	
    model_small = {
        **models[0],
        "sprite": SpriteName._03_MARIO_SURPRISE_LEFT,
        "vram_store": VramStore._02_SWSE,
        "extra_props": {
            "sprite_plus": 3, # use this if Sprite property has to be reverted,
            "sequence": 10,
            "is_empty": True,
            "freeze": True,
            "statue_mold": 22
        }
    }
    dialog_replacements = [
        (49,'''  EXOR: What do you want? Get\n lost![await]'''),
        (1660, ''' Halt! This ship belongs to ME!\n If you want to get through...\n bring it on![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Exor's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped EXOR!![await]'''),
        (1778, '''EXOR: If it weren't for nosey\n characters like you, I could live in\n this ship undisturbed![await]'''),
        (1780, '''EXOR: Halt! Don't even THINK\n about leaving until you've had\n some of this juice![await]'''),
        (1781, '''EXOR: Look, if you really want to\n humiliate me, why not use\n Geno Whirl too, while you're at it?[await]'''),
        (1784, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1792, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1793, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (2061, '''CHEF TORTE: Zees cake, ve make\n it look like big sword man! It is...\n masterpiece![await]'''),
        (2504, '''EXOR: Halt![await][pause] What do you have\n here?[delay] [0x7000] item(s)?[await]\n No, this won't do.[await][pause] Find [0x7024] more,\n[delay] or I won't let you through![await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Exor's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Exor.[await]'''),
        (2831, '''EXOR: There isn't much to see in\n this town. Especially not in\n the shed.[await]'''),
        (2838, ''' You will find Exor...\n in his house. He is...the most\n respected person here.[await]'''),
        (3044, '''EXOR: Think you're gonna beat the\n dojo master? Now this I GOTTA\n see![await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Nosey-this and Trespasser-that.[await]'''),
        (3352, '''\n        EXOR: How humiliating![await]'''),
        (3353, '''\n        EXOR: How humiliating![await]'''),
    ]

    def patch_script(self):
        script = BattleScript()
        script.if_bits_clear(0x7ee000, 0x07)
        script.if_target_alive(Targets.MONSTER_3)
        script.if_target_alive(Targets.MONSTER_4)
        script.set(0x7ee000, 0x04)
        script.battle_dialog(0xda)

        if self.world.settings.is_flag_enabled(flags.NoGenoWhirlExor):
            script.set_untargetable(Monsters.MONSTER_1)
        else:
            script.invuln(Targets.MONSTER_1)

        script.wait_return()

        script.start_counter()

        script.if_hp(0x0000)
        script.set(0x7ee008, 0x01)
        script.set_untargetable(Monsters.MONSTER_2)
        script.set_untargetable(Monsters.MONSTER_3)
        script.set_untargetable(Monsters.MONSTER_4)
        script.remove(0x1b)
        script.wait_return()

        self.script = script.fin()


class Smithy1(Enemy):
    index = 234
    address = 0x390fa6
    boss = True
    hp = 2000
    speed = 30
    attack = 230
    defense = 130
    magic_attack = 100
    magic_defense = 100
    fp = 250
    death_immune = True
    sound_on_hit = 96
    status_immunities = [0, 1, 2, 3]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391bb8
    yoshi_cookie_item = items.Mushroom

    model_small = {
        **models[351],
        "extra_props": {
            "is_skinny": True
        }
    }
    # may need to adjust these properties
    model_large = {
        **models[371],
        "sprite": SpriteName._490_SMITHY_1ST_FORM
    }
    # dialog_replacements = [
    #     (49,'''SMITHY: How utterly annoying!\n Leave me alone![await]'''),
    #     (1660, ''' Gufaw, haw, haw![delay_30] You really think\n I'm going to let you through with\n just a password?![await]'''),
    #     (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Smithy's place.[await]'''),
    #     (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped\n SMITHY!![await]'''),
    #     (1778, '''SMITHY: How utterly annoying!\n Get out of here before I crush\n you all![await]'''),
    #     (1780, '''SMITHY: Gufaw, haw, haw...\n Not quite as impressive as my\n factory, eh?[await]'''),
    #     (1781, '''SMITHY: Never have I been so\n wronged![await]'''),
    #     (1784, '''MACHINE MADE: The foundation in\n this old haunted ship looks pretty\n weak, so we try not to make Smithy\n too mad.[await]'''),
    #     (1785, '''MACHINE MADE: Hop on the\n trampoline in the next room. It'll\n take you outside.[await]'''),
    #     (1792, '''MACHINE MADE: The foundation in\n this old haunted ship looks pretty\n weak, so we try not to make Smithy\n too mad.[await]'''),
    #     (1793, '''MACHINE MADE: The foundation in\n this old haunted ship looks pretty\n weak, so we try not to make Smithy\n too mad.[await]'''),
    #     (2061, '''MACHINE MADE: We're making a cake\n to look just like Smithy![await]'''),
    #     (2062, '''MACHINE MADE: We've gotten REAL\n good with fondant![await]'''),
    #     (2504, '''SMITHY: How utterly annoying![await]\n Give me [28][1] more item(s)![await]'''),
    #     (2560, '''SNIFIT 1: Hello there.[await]\n Smithy's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
    #     (2572, '''SNIFIT 2: Please refrain\n from bothering Smithy.[await]'''),
    #     (2831, '''SMITHY: So, it's YOU![await]\n Unfortunately for you, there's\n nothing evil in this town that\n demands your attention.[await]'''),
    #     (2832, ''' Yo. This inn doesn't charge\n anything for our services.\n Wanna stay?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]'''),
    #     (2834, ''' The two guys in the left building\n have been acting suspicious.[await]'''),
    #     (2836, ''' If you haven't been to the Sunken\n Ship yet, you can get there through\n the whirlpools in the sea.[await]'''),
    #     (2837, ''' If you haven't been to the Sunken\n Ship yet, you can get there after\n you crash the wedding over in\n Marrymore.[await]'''),
    #     (2838, ''' Have you been to Smithy's house\n up on the hill yet?[await]'''),
    #     (2839, ''' The shed...?[delay] No, there's nothing in\n there! Take my word for it.[await]'''),
    #     (2841, ''' Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]'''),
    #     (2842, ''' Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]'''),
    #     (2843, ''' Once you get through the Sunken\n Ship, you can... er...[await]'''),
    #     (2844, ''' You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]'''),
    #     (2845, ''' What am I doing with this stuff?\n ...None of your business![await]'''),
    #     (2847, '''\n             Get out of here![await]'''),
    #     (2848, ''' No visitors allowed in the shed!\n Scram![await]'''),
    #     (3044, '''\n   SMITHY: Grr... Leave me alone![await]'''),
    #     (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Factory-this and Weapon-that.[await]'''),
    # ]
    # optional_dialog_replacements = [
    #     (1694, '''DRILL BIT: You're pretty tough,\n but are you ready to fight Smithy?[await]'''),
    #     (1695, '''DRILL BIT: Oh, wow, you did it!\n No wonder we lost to you...[await]'''),
    #     (2560, '''MACHINE MADE: Yo![await][pause] Smithy's busy,\n so come back another time! [await][page]\n [delay]...You sure you wanna just barge\n in like that?[await][pause] Alright buddy, don't\n say I didn't warn you![await]'''),
    #     (2572, '''MACHINE MADE: Man, what's your\n deal?[await][pause] Quit snooping around!\n Smithy'll have a fit![await]'''),
    #     (3072, '''MACHINE MADE: It's pretty drafty\n in here![await]'''),
    #     (3073, '''\n MACHINE MADE: Oh, no you don't![await]'''),
    #     (3352, '''SMITHY: Grr... [delay]You're stronger\n than I thought...[await]'''),
    #     (3353, '''SMITHY: Grr... [delay]You're stronger\n than I thought...[await]'''),
    # ]

class Shyper(Enemy):
    index = 235
    address = 0x390fb6
    boss = True
    hp = 400
    speed = 42
    attack = 170
    defense = 80
    magic_attack = 70
    magic_defense = 50
    fp = 30
    evade = 20
    death_immune = True
    sound_on_hit = 80
    status_immunities = [0, 1, 2, 3]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391bbe
    yoshi_cookie_item = items.Mushroom


class Smithy2Body(Enemy):
    index = 236
    address = 0x390fd6
    boss = True
    hp = 1000
    speed = 30
    attack = 180
    defense = 80
    magic_attack = 20
    magic_defense = 60
    fp = 50
    death_immune = True
    sound_on_hit = 96
    status_immunities = [0, 1, 2, 3]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391bc4
    yoshi_cookie_item = items.Mushroom


class Smithy2Head(Enemy):
    index = 237
    address = 0x390fe6
    boss = True
    hp = 8000
    speed = 40
    attack = 180
    defense = 80
    magic_attack = 60
    magic_defense = 50
    fp = 50
    death_immune = True
    sound_on_hit = 96
    status_immunities = [0, 1, 2, 3]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391bca
    yoshi_cookie_item = items.Mushroom


class Smithy2MageHead(Enemy):
    index = 238
    address = 0x391016
    boss = True
    hp = 8000
    speed = 35
    attack = 135
    defense = 50
    magic_attack = 130
    magic_defense = 150
    fp = 250
    death_immune = True
    sound_on_hit = 96
    resistances = [4, 5, 6]
    status_immunities = [0, 1, 2, 3]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391bd0
    yoshi_cookie_item = items.Mushroom


class Smithy2ChestHead(Enemy):
    index = 239
    address = 0x391026
    boss = True
    hp = 8000
    speed = 18
    attack = 150
    defense = 120
    magic_attack = 78
    magic_defense = 80
    fp = 250
    death_immune = True
    sound_on_hit = 96
    resistances = [5]
    weaknesses = [6]
    status_immunities = [0, 1, 2, 3]
    palette = 24
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391bd6
    yoshi_cookie_item = items.Mushroom


class Croco1(Enemy):
    index = 240
    address = 0x391036
    boss = True
    hp = 320
    speed = 16
    attack = 25
    defense = 25
    magic_attack = 30
    magic_defense = 18
    fp = 12
    evade = 20
    death_immune = True
    sound_on_hit = 16
    weaknesses = [6]
    status_immunities = [1, 5, 6]
    palette = 8
    flower_bonus_type = 1
    hp_counter_ratios = [100 / 320]

    # Reward attributes
    reward_address = 0x391bdc
    xp = 16
    coins = 10
    yoshi_cookie_item = items.Mushroom
    normal_item = items.FlowerTab
    rare_item = items.FlowerTab

    # Boss shuffle attributes.
    ratio_hp = 1.0
    ratio_fp = 1.0
    name_override = 'CROCO 1'

    # shuffled overworld sprites
    sidekicks = [5, 5, 5]

    model_small = {
        **models[48],
        "extra_props": {
            "extra_sequence": 5,
            "statue_west_shift": 3
        }
    }
    dialog_replacements = [
        (49,'''\n CROCO: Get the heck outta here![await]'''),
        (1660, ''' Alright, alright, so ya figured out\n my password! But I ain't goin'\n down without a fight![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Croco's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped CROCO!![await]'''),
        (1778, '''CROCO: Enough already, get outta\n here![await]'''),
        (1780, '''CROCO: Back already? How 'bout a\n drink?[await]'''),
        (1781, '''\n    CROCO: 'Dis some kinda joke?[await]'''),
        (1784, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1792, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (1793, ''' Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]'''),
        (2061, '''CHEF TORTE: Zees cake, ve make\n it look like big reptile! It is...\n masterpiece![await]'''),
        (2504, '''CROCO: What's dis?[await][pause] You fools're\n gonna take another 100 years to\n find the last [0x7024] item(s)![await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Croco's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Croco.[await]'''),
        (2831, '''CROCO: Whaddya doin' hangin\n 'round here?[await]'''),
        (2838, ''' You will find Croco...\n in his house. He is...the most\n respected person here.[await]'''),
        (3044, '''CROCO: Think ya can beat the dojo\n master, chump? I'd like to see ya\n try![await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Wallet-this and Coin-that.[await]'''),
        (3352, '''CROCO: I hate to say it, but...\n I kinda like this![await]'''),
        (3353, '''CROCO: I hate to say it, but...\n I kinda like this![await]'''),
    ]



class Croco2(Enemy):
    index = 241
    address = 0x391046
    boss = True
    hp = 750
    speed = 20
    attack = 52
    defense = 50
    magic_attack = 27
    magic_defense = 50
    fp = 12
    evade = 20
    death_immune = True
    sound_on_hit = 16
    weaknesses = [6]
    status_immunities = [1, 5, 6]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2
    hp_counter_ratios = [400 / 750]

    # Reward attributes
    reward_address = 0x391be2
    xp = 30
    coins = 50
    yoshi_cookie_item = items.Mushroom
    rare_item = items.FlowerBox

    # Boss shuffle attributes.
    ratio_hp = 1.0
    ratio_fp = 1.0
    name_override = 'CROCO 2'

    # shuffled overworld sprites
    sidekicks = [5, 5, 5]

    model_small = {
        **models[361],
        "extra_props": {
            "extra_sequence": 5,
            "statue_west_shift": 3
        }
    }
    dialog_replacements = [
        (49,'''\n CROCO: Get the heck outta here![await]'''),
        (1660, ''' Alright, alright, so ya figured out\n my password! But I ain't goin'\n down without a fight![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Croco's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped CROCO!![await]'''),
        (1778, '''CROCO: Enough already, get outta\n here![await]'''),
        (1780, '''CROCO: Back already? How 'bout a\n drink?[await]'''),
        (1781, '''\n    CROCO: 'Dis some kinda joke?[await]'''),
        (1784, '''FLUNKIE: To be honest, Croco's not\n really a bad guy.[await][pause] I guess that's why\n we follow him.[await]'''),
        (1785, '''FLUNKIE: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]'''),
        (1792, '''FLUNKIE: To be honest, Croco's not\n really a bad guy.[await][pause] I guess that's why\n we follow him.[await]'''),
        (1793, '''FLUNKIE: To be honest, Croco's not\n really a bad guy.[await][pause] I guess that's why\n we follow him.[await]'''),
        (2061, '''FLUNKIE: Doesn't this cake\n look just like Croco?[await]'''),
        (2062, '''FLUNKIE: We've gotten REAL\n good with fondant![await]'''),
        (2504, '''CROCO: What's dis?[await][pause] You fools're\n gonna take another 100 years to\n find the last [0x7024] item(s)![await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Croco's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Croco.[await]'''),
        (2831, '''CROCO: Whaddya doin' hangin\n 'round here?[await]'''),
        (2832, ''' You tired? You can stay here\n for free.[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]'''),
        (2834, ''' The two guys in the left building\n have been acting suspicious.[await]'''),
        (2836, ''' If you haven't been to the Sunken\n Ship yet, you can get there through\n the whirlpools in the sea.[await]'''),
        (2837, ''' If you haven't been to the Sunken\n Ship yet, you can get there after\n you crash the wedding over in\n Marrymore.[await]'''),
        (2838, ''' Have you been to Croco's house\n up on the hill yet?[await]'''),
        (2839, ''' You better not be snooping around\n the shed![await]'''),
        (2841, ''' Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]'''),
        (2842, ''' Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]'''),
        (2843, ''' Once you get through the Sunken\n Ship, you can... er...[await]'''),
        (2844, ''' You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]'''),
        (2845, ''' Huh?[delay] What am I doing here?[delay] None\n of your business, that's what![await]'''),
        (2847, '''\n           Nothin' to see here.[await]'''),
        (2848, ''' Nope, nothing suspicious going on\n in this house![await]'''),
        (3044, '''CROCO: Think ya can beat the dojo\n master, chump? I'd like to see ya\n try![await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Wallet-this and Coin-that.[await]'''),
        (3352, '''CROCO: I hate to say it, but...\n I kinda like this![await]'''),
        (3353, '''CROCO: I hate to say it, but...\n I kinda like this![await]'''),
    ]
    optional_dialog_replacements = [
        (1694, '''FLUNKIE: (Sob, sob...)[delay_30]\n You're pretty tough. I guess I'll let\n you through to Croco's place.[await]'''),
        (1695, '''FLUNKIE: You beat Croco!?[delay_30]\n We'll getcha for this![await][page]\n Maybe not today, maybe not\n tomorrow, but someday...[await]'''),
        (2560, '''FLUNKIE: Croco's busy! Scram![await][page]\n  ...Not leaving, huh?\n[delay] Alright buddy, you asked for it![await]'''),
        (2572, '''FLUNKIE: Where d'ya think YOU'RE\n going?![await]'''),
        (3072, '''\n  FLUNKIE: I could use a stepstool.[await]'''),
        (3073, '''\n      FLUNKIE: A tough guy, eh?[await]'''),
    ]


class Earthlink(Enemy):
    index = 243
    address = 0x390ea6
    boss = True
    hp = 2500
    speed = 16
    attack = 220
    defense = 120
    magic_attack = 5
    magic_defense = 10
    fp = 100
    death_immune = True
    sound_on_hit = 32
    status_immunities = [0, 1, 2, 3]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391b6a
    xp = 200
    yoshi_cookie_item = items.Mushroom
    normal_item = items.PowerBlast
    rare_item = items.PowerBlast

    # Boss shuffle attributes.
    ratio_hp = 0.8197
    ratio_fp = 0.1429
    ratio_attack = 1.4286
    ratio_defense = 1.2
    ratio_magic_attack = 0.0877
    ratio_magic_defense = 0.1111
    ratio_speed = 0.8889


class Bowser(Enemy):
    index = 244
    address = 0x391066
    boss = True
    hp = 320
    speed = 15
    attack = 1
    defense = 12
    fp = 100
    death_immune = True
    sound_on_hit = 32
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391bee
    yoshi_cookie_item = items.Mushroom


class AxemRangers(Enemy):
    index = 245
    address = 0x391076
    boss = True
    hp = 999
    speed = 200
    defense = 100
    magic_attack = 120
    magic_defense = 100
    fp = 100
    death_immune = True
    sound_on_hit = 96
    weaknesses = [5]
    status_immunities = [0, 1, 2, 3]
    palette = 24
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391b16
    xp = 50
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.263
    ratio_fp = 0.125
    ratio_attack = 0.0
    ratio_defense = 1.0204
    ratio_magic_attack = 3.0769
    ratio_magic_defense = 1.2048
    ratio_speed = 3.8462
    ratio_evade = 0.0
    ratio_magic_evade = 0.0

    sidekicks = [229, 207, 228, 211]

    # shuffled overworld sprites
    battle_push_sequence = 3
    battle_push_length = 24

    model_small = {
        **models[208],
        "extra_props": {
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 24,
            "statue_west_shift": 6
        }
    }
    dialog_replacements = [
        (49,'''AXEM RED: We're busy playing Uno\n in here. Go bother someone else![await]'''),
        (1660, ''' Listen up, nerd![delay_30] You may have\n figured out our password, but\n we're not going down without\n a fight![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n the Axem Rangers' place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped\n the AXEM RANGERS!![await]'''),
        (1778, '''AXEM RED: How could this happen\n to the Axem Rangers?![await]'''),
        (1780, '''AXEM RED: Yo! Quit wasting yourn time around here, you've got a\n world to save![await]'''),
        (1781, '''AXEM RED: Yo, Mario! This isn't\n cool! Get off of my head.[await]'''),
        (1784, '''AXEM BLACK: Red can be kind of\n a chump when he loses.[await]'''),
        (1785, '''AXEM YELLOW: Say, do you have\n anything to eat?[await]'''),
        (1792, '''AXEM PINK: I hate it down here!\n The water makes my makeup run![await]'''),
        (1793, '''AXEM GREEN: The four of them may\n be hot heads, but I truly enjoy\n causing mischief with them.[await]'''),
        (2061, '''AXEM YELLOW: Why the heck do\n I have to bake a cake that I'm\n not going to get to eat?![await]'''),
        (2062, '''AXEM GREEN: Not EVERYTHING\n we do is evil. Today we're baking a\n cake that looks like Axem Red.[await]'''),
        (2504, '''AXEM RED: Listen! You're not\n going anywhere until you find [0x7024]\n more of `MARRYMORE_CHARACTER`'s item(s)![await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n The Axem Rangers are busy right\n now, so they can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering the Axem Rangers.[await]'''),
        (2831, '''AXEM RED: Listen up![await]\n Quit snooping around town![await]'''),
        (2832, '''AXEM PINK: Hi~![delay] Are you sleepy?\n I'm feeling nice today, so you can\n stay for free.[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]'''),
        (2834, ''' The two guys in the left building\n have been acting suspicious.[await]'''),
        (2836, ''' If you haven't been to the Sunken\n Ship yet, you can get there through\n the whirlpools in the sea.[await]'''),
        (2837, ''' If you haven't been to the Sunken\n Ship yet, you can get there after\n you crash the wedding over in\n Marrymore.[await]'''),
        (2838, ''' Have you been to Axem Red's\n house up on the hill yet?[await]'''),
        (2839, ''' They won't give me a better job\n in this town! I wanted to be one\n of the shed guards![await]\n ...What are they guarding?\n [delay]N-nothing![await]'''),
        (2841, ''' Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]'''),
        (2842, ''' Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]'''),
        (2843, ''' Once you get through the Sunken\n Ship, you can... er...[await]'''),
        (2844, ''' You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]'''),
        (2845, ''' Why does HE get to be the\n shopkeeper?[await]'''),
        (2847, '''\n     AXEM BLACK: Beat it, clod![await]'''),
        (2848, '''AXEM YELLOW: Get lost, mustache!\n [delay]This shed belongs to the Axem\n Rangers![await]'''),
        (3044, '''AXEM RED: Yo! It won't be enough\n to win just once. The dojo master\n has three forms.[await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the people\n next door.[await][page]\n They're always mumbling about\n Shades-this and Makeup-that.[await]'''),
        (3352, '''\n  AXEM RED: I'm way outta shape![await]'''),
        (3353, '''\n  AXEM RED: I'm way outta shape![await]'''),
    ]
    optional_dialog_replacements = [
    # probably not going to do many optional sidekicks with axems as a donor
        (2560, '''AXEM YELLOW: Green hasn't showed\n up to cover me for lunch yet! I'm\n so HUNGRY![await][page]\n ...I need a distraction![await]'''),
        (2572, '''AXEM BLACK: Where do you clods\n think you're going?![await]'''),
        (3072, '''AXEM PINK: It's so nice outside!\n Why does Red want us cooped up\n in here, anyway?![await]'''),
        (3073, '''AXEM PINK: What the heck do you\n want?![await]'''),
    ]


class Booster(Enemy):
    index = 246
    address = 0x3910d6
    boss = True
    hp = 800
    speed = 24
    attack = 75
    defense = 55
    magic_attack = 1
    magic_defense = 40
    fp = 2
    death_immune = True
    sound_on_hit = 96
    sound_on_approach = 3
    weaknesses = [7]
    status_immunities = [1]
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2
    hp_counter_ratios = [500 / 800]

    # Reward attributes
    reward_address = 0x391bf4
    xp = 60
    coins = 100
    yoshi_cookie_item = items.Mushroom
    rare_item = items.FlowerBox

    # Boss shuffle attributes
    anchor = True
    ratio_hp = 0.57
    ratio_fp = 0.02

    # shuffled overworld sprites

    model_small = {
        **models[50],
        "extra_props": {
            "extra_sequence": 2,
            "moleville_animation_sequence": 2,
            "moleville_animation_duration": 72,
            "is_skinny": True,
        }
    }
    dialog_replacements = [
        (49,'''BOOSTER: It's pretty cozy in here.[await][pause]\n No, you can't come in![await]'''),
        (1660, ''' Eh?[delay_30] THAT was my password?![delay_30]\n I'd better fight you, just to be\n sure.[await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Booster's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped BOOSTER!![await]'''),
        (1778, '''BOOSTER: I'd love to entertain\n you, but I'm busy watching the\n fish. Come back later.[await]'''),
        (1780, '''BOOSTER: Eh...? My! It's you\n again![await][page]\n  We're having a heated debate over\n what a “party” is, so you can stay\n if you'd like to contribute.[await]'''),
        (1781, '''BOOSTER: Hm? How's the view up there?[await]'''),
        (1784, '''SNIFIT 1: There's a 70%% chance the\n drink on the table is actually\n punch.[await]'''),
        (1792, '''SNIFIT 2: Booster can't find any\n beetles underwater, but he still\n enjoys watching the fish.[await]'''),
        (1793, '''SNIFIT 3: Uh... Do you know where\n we could get some cake down here?[await]'''),
        (2061, '''SNIFIT 2: Doesn't this cake\n look just like Booster?[await]'''),
        (2062, '''SNIFIT 3: Uh... I think we should\n have made his mustache bigger.[await]'''),
        (2831, '''\n   BOOSTER: Found our town, eh?[await]'''),
        (2832, '''SNIFIT 1: Welcome![delay] How would you\n like to stay in our fabulous inn\n for free today?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]'''),
        (2834, ''' The two guys in the left building\n have been acting suspicious.[await]'''),
        (2836, ''' If you haven't been to the Sunken\n Ship yet, you can get there through\n the whirlpools in the sea.[await]'''),
        (2837, ''' If you haven't been to the Sunken\n Ship yet, you can get there after\n you crash the wedding over in\n Marrymore.[await]'''),
        (2838, ''' Have you been to Booster's\n house up on the hill yet?[await]'''),
        (2839, '''\n You'd better not go near our shed![await]'''),
        (2841, ''' Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]'''),
        (2842, ''' Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]'''),
        (2843, ''' Once you get through the Sunken\n Ship, you can... er...[await]'''),
        (2844, ''' You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]'''),
        (2845, ''' I'm facing a promotion. Do they sell\n anything here that'll make me look\n more professional?[await]'''),
        (2847, '''SNIFIT 3: Uh... Don't look in the\n window. [delay]Pretty please.[await]'''),
        (2848, '''SNIFIT 2: There is nothing of\n interest to you in here.[await]'''),
        (3044, '''BOOSTER: I wonder if the dojo\n master can shape-shift into a\n Mario doll.[await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Beetle-this and Train-that.[await]'''),
        (3352, '''BOOSTER: Eh?[await][pause] ...Training? [delay]What training?[await]'''),
        (3353, '''BOOSTER: Eh?[await][pause] ...Training? [delay]What training?[await]'''),
    ]
    optional_dialog_replacements = [
        (1694, '''SNIFIT: Oh, dear! We've failed to\n keep the intruder away from\n Booster![await]'''),
        (1695, '''SNIFIT: Booster's not happy about\n losing. Please do not jump on\n his head.[await]'''),
    ]


class Booster2(Enemy):
    index = 247
    address = 0x3910e6
    boss = True
    hp = 10
    fp = 100
    death_immune = True
    sound_on_hit = 96
    palette = 16
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391bfa
    yoshi_cookie_item = items.Mushroom


class Snifit(Enemy):
    index = 248
    address = 0x3904a6
    boss = True
    hp = 200
    speed = 26
    attack = 60
    defense = 60
    magic_attack = 20
    magic_defense = 20
    fp = 32
    sound_on_hit = 128
    weaknesses = [4]
    palette = 8
    flower_bonus_type = 5
    flower_bonus_chance = 8

    # Reward attributes
    reward_address = 0x39171a
    xp = 2
    coins = 15
    yoshi_cookie_item = items.Mushroom
    rare_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.14
    ratio_fp = 0.33
    ratio_attack = 0.80
    ratio_defense = 1.09
    ratio_magic_attack = 1.0
    ratio_magic_defense = 0.5
    ratio_speed = 1.08
    ratio_evade = 0.0
    ratio_magic_evade = 0.0

    model_small = {
        **models[504]
    }


class Johnny(Enemy):
    index = 249
    address = 0x3910f6
    boss = True
    hp = 820
    speed = 13
    attack = 85
    defense = 80
    magic_attack = 25
    magic_defense = 60
    fp = 100
    death_immune = True
    sound_on_hit = 32
    status_immunities = [1]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2
    hp_counter_ratios = [400 / 820]

    # Reward attributes
    reward_address = 0x391c00
    xp = 90
    coins = 50
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 1.0
    ratio_fp = 1.0

    sidekicks = [75, 75, 75, 75]

    # shuffled overworld sprites
    sprite_height = 55
    sprite_width = 64

    model_small = {
        **models[55],
        "extra_props": {
            "extra_sequence": 10
        }
    }
    # may need to adjust these properties
    model_large = {
        **models[371],
        "sprite": SpriteName._505_JOHNNY,
        "extra_props": {
            "is_wide": True,
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 38
        }
    }
    dialog_replacements = [
        (49,'''JOHNNY: Matey, it'd be mighty fun\n to spar again, but I'm tryin' to\n sleep now.[await]'''),
        (1660, ''' Good job, matey... But ye gotta\n fight me first if ye wanna be let\n through![await]'''),
        (2061, '''PIRATE: Y'arr, don't ye think\n this cake here be lookin' just like\n Johnny?[await]'''),
        (2062, '''PIRATE: Us pirates are pretty\n good with food, arr harr![await]'''),
        (2504, '''JOHNNY: Found [0x7000] item(s), eh? Arr,\n harr, harr...! You gotta find [0x7024]\n more, matey![await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Johnny's busy right now, so\n he can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Johnny.[await]'''),
        (2831, '''\n        JOHNNY: Ahoy, matey![await]'''),
        (2832, ''' Welcome, matey! How'd ya like to\n stay here tonight, on the house?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]'''),
        (2834, ''' The two fellas o'er in the left\n building have been actin' weird.[await]'''),
        (2836, ''' Y'arr, so ye want to visit the ship,\n do ye? Ya gotta go through the\n whirlpools, matey![await]'''),
        (2837, ''' Y'arr, so ye want to visit the ship,\n do ye? Ya gotta crash a wedding a\n few towns over first, matey![await]'''),
        (2838, ''' Have ye been to visit Johnny up\n on the hill yet, matey?[await]'''),
        (2839, ''' Arr, what ye be doin' in our town?\n Just stay away from the shed,\n ya hear?[await]'''),
        (2841, ''' Out in yonder Sunken Ship, there\n be a... er...[await]'''),
        (2842, ''' A treasure chest, behind a big\n stack o' boxes! Don't forget about\n it, matey![await]'''),
        (2843, ''' If ye can tough it out through the\n ship, you can come back here for\n some... er...[await]'''),
        (2844, ''' Come back here for some FUN,\n arr harr! Ya got that, matey?![await]'''),
        (2845, '''\n       I just be shoppin', matey.[await]'''),
        (2847, ''' Read my lips... WE AIN'T LETTIN'\n YA THROUGH![await]'''),
        (2848, '''\n You ain't gettin in here! It's ours![await]'''),
        (3044, '''JOHNNY: Good luck, matey. The dojo\n master's mighty tough.[await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Arr-this and Matey-that.[await]'''),
        (3352, '''JOHNNY: Matey, I've got lots o'\n training to do![await]'''),
        (3353, '''JOHNNY: Matey, I've got lots o'\n training to do![await]'''),
    ]
    optional_dialog_replacements = [
        (2560, '''PIRATE: Welcome, matey![await][pause] Here to\n spar with Johnny, are ye?[await][page]\n Arr, good fun! Let's have a\n warm-up round![await]'''),
        (2572, '''PIRATE: This ain't the corner you\n want, matey![await][pause] But while you're here,\n let's have a spar, arr harr![await]'''),
        (3072, '''PIRATE: I know there be some fine\n loot in this tower, but it's too far\n 'bove sea level for my liking![await]'''),
        (3073, '''PIRATE: I'll make ya see stars,\n arr harr![await]'''),
    ]


class JohnnySolo(Enemy):
    index = 250
    address = 0x390d16
    boss = True
    hp = 400
    speed = 30
    attack = 90
    defense = 100
    magic_defense = 32
    fp = 100
    evade = 10
    death_immune = True
    sound_on_hit = 32
    resistances = [6, 7]
    status_immunities = [2]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391c06
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.4878
    ratio_fp = 1.0
    ratio_attack = 1.0588
    ratio_defense = 1.25
    ratio_magic_attack = 0.0
    ratio_magic_defense = 0.5333
    ratio_speed = 2.3077
    ratio_evade = 1.0
    ratio_magic_evade = 1.0


class Valentina(Enemy):
    index = 251
    address = 0x391106
    boss = True
    hp = 2000
    speed = 200
    attack = 120
    defense = 80
    magic_attack = 80
    magic_defense = 60
    fp = 250
    evade = 10
    death_immune = True
    sound_on_hit = 32
    resistances = [4]
    status_immunities = [0, 1, 2, 3]
    palette = 24
    flower_bonus_type = 1
    flower_bonus_chance = 2
    hp_counter_ratios = [0.6]

    # Reward attributes
    reward_address = 0x391c0c
    xp = 120
    coins = 200
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes
    anchor = True
    ratio_hp = 0.8333
    ratio_fp = 0.7143

    # shuffled overworld sprites
    sprite_height = 82
    sprite_width = 51
    overworld_extra_sequence = 2
    battle_push_sequence = 3
    battle_push_length = 18
    battle_sesw_only = True
    overworld_is_skinny = True
    shadow = SMALL_SHADOW

    other_sprites = [77, 13, 77, 13]

    model_small = {
        **models[56],
        "extra_props": {
            "extra_sequence": 2,
            "statue_west_shift": 3,
            "statue_south_shift": 1,
            "opposite_statue_west_shift": 2
        }
    }
    # may need to edit these
    model_large = {
        **models[507],
        "extra_props": {
            "is_tall": True,
            "moleville_animation_sequence": 3,
            "moleville_animation_duration": 18
        }
    }
    dialog_replacements = [
        (49,'''VALENTINA: ...What? You're STILL\n here?! Go AWAY!!![await]'''),
        (1660, ''' ALRIGHT, already![delay_30] If you're going\n to annoy me like this, get in here\n and finish the job![await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Valentina's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped\n VALENTINA!![await]'''),
        (1778, '''VALENTINA: If you don't stop\n bothering me, I'm going to turn\n your mustache into a\n vegetable scrubber![await]'''),
        (1780, '''VALENTINA: YOU again?! You better\n have brought some margaritas![await]'''),
        (1781, '''VALENTINA: Get OFF of my head\n before I take your shoes and throw\n them in the ocean!!![await]'''),
        (1784, '''BLUEBIRD: Valentina's grumpy.\n Booster got her a gold beetle for\n their anniversary.[await][pause] She wanted a\n ladybug.[await][page]\n Married life sounds truly weird.[await]'''),
        (1785, '''BLUEBIRD: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]'''),
        (1792, '''BLUEBIRD: Valentina's grumpy.\n Booster got her a gold beetle for\n their anniversary.[await][pause] She wanted a\n ladybug.[await][page]\n Married life sounds truly weird.[await]'''),
        (1793, '''BLUEBIRD: Valentina's grumpy.\n Booster got her a gold beetle for\n their anniversary.[await][pause] She wanted a\n ladybug.[await][page]\n Married life sounds truly weird.[await]'''),
        (2061, '''BLUEBIRD: Why are we making\n a cake that looks like Valentina,\n again?[await]'''),
        (2062, '''BLUEBIRD: We're making a cake\n that looks like Valentina.[await]\n What else are we gonna do\n on our day off?[await]'''),
        (2504, '''VALENTINA: STOP BOTHERING ME![await]\n If you need something to do, go\n look for [0x7024] more item(s)![await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Valentina's busy right now, so she\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Valentina.[await]'''),
        (2831, '''\n   VALENTINA: I'm SO frustrated![await]'''),
        (2832, ''' Welcome![delay] I'll let you stay here for\n free, but don't tell Valentina.[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]'''),
        (2834, ''' The two guys in the left building\n have been acting suspicious.[await]'''),
        (2836, ''' If you haven't been to the Sunken\n Ship yet, you can get there through\n the whirlpools in the sea.[await]'''),
        (2837, ''' If you haven't been to the Sunken\n Ship yet, you can get there after\n you crash the wedding over in\n Marrymore.[await]'''),
        (2838, ''' Have you been to Valentina's\n house up on the hill yet?[await]'''),
        (2839, ''' Hmm...[delay] What're you loitering\n around here for?[delay] Uh...[delay] Stay away\n from the shed, OK?[await]'''),
        (2841, ''' Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]'''),
        (2842, ''' Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]'''),
        (2843, ''' Once you get through the Sunken\n Ship, you can... er...[await]'''),
        (2844, ''' You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]'''),
        (2845, ''' ...I'm on my break. [delay]Just let me\n shop in peace, OK?[await]'''),
        (2847, '''\n     You can't just barge in here![await]'''),
        (2848, '''\n         Hey! Who're YOU?!...[await]'''),
        (3044, '''VALENTINA: You? Fighting the dojo\n master? Good luck, chump![await]'''),
        (3338, ''' It's really weird.\n Sometimes I hear the lady next door.[await][page]\n She's always mumbling about\n Queen-this and Dodo-that.[await]'''),
        (3352, '''VALENTINA: Is this REALLY going to\n make me powerful enough to take\n ov...[delay_30] I mean...[delay_30] pay a cordial visit\n to Nimbus Land?![await]'''),
        (3353, '''VALENTINA: Is this REALLY going to\n make me powerful enough to take\n ov...[delay_30] I mean...[delay_30] pay a cordial visit\n to Nimbus Land?![await]'''),
    ]
    optional_dialog_replacements = [
        (1694, '''BLUEBIRD: Whatever, go on and\n fight Valentina. She doesn't pay\n us enough to keep you out.[await]'''),
        (1695, '''BLUEBIRD: Oh, you won?[await]\n [delay_30](...[delay_30]It's about time!)[await]'''),
        (2560, '''BLUEBIRD: I hate being a secretary!\n And... [delay_30]I'm going to make this\n your problem![await]'''),
        (2572, '''BLUEBIRD: Whaddya want?[await][pause] You\n better not be trying to bother\n Valentina, [delay]or I'll be in trouble![await]'''),
        (3072, '''BLUEBIRD: Valentina only gives us\n the most boring jobs to do...[await]'''),
        (3073, '''\nBLUEBIRD: I'm bored. Entertain me![await]'''),
    ]

class Cloaker2(Enemy):
    index = 252
    address = 0x390e96
    boss = True
    hp = 1200
    speed = 20
    attack = 180
    defense = 130
    magic_attack = 12
    magic_defense = 20
    fp = 100
    death_immune = True
    sound_on_hit = 48
    status_immunities = [0, 1, 2, 3]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391b70
    xp = 60
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.3934
    ratio_fp = 0.1429
    ratio_attack = 1.1688
    ratio_defense = 1.3
    ratio_magic_attack = 0.2105
    ratio_magic_defense = 0.2222
    ratio_speed = 1.1111


class Domino2(Enemy):
    index = 253
    address = 0x390ec6
    boss = True
    hp = 900
    speed = 25
    attack = 65
    defense = 80
    magic_attack = 120
    magic_defense = 150
    fp = 250
    death_immune = True
    sound_on_hit = 16
    status_immunities = [0, 1, 2, 3]
    palette = 32
    flower_bonus_type = 1

    # Reward attributes
    reward_address = 0x391b76
    xp = 60
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 0.2951
    ratio_fp = 0.3571
    ratio_attack = 0.4221
    ratio_defense = 0.8
    ratio_magic_attack = 2.1053
    ratio_magic_defense = 1.6667
    ratio_speed = 1.3889


class Candle(Enemy):
    index = 254
    address = 0x390cb6
    boss = True
    hp = 10
    fp = 100
    status_immunities = [0, 1, 2, 3]
    palette = 8
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391c1e
    yoshi_cookie_item = items.Mushroom


class Culex(Enemy):
    index = 255
    address = 0x391136
    boss = True
    hp = 4096
    speed = 50
    attack = 250
    defense = 100
    magic_attack = 100
    magic_defense = 80
    fp = 200
    death_immune = True
    sound_on_hit = 32
    status_immunities = [0, 1, 2, 3]
    palette = 32
    flower_bonus_type = 1
    flower_bonus_chance = 2

    # Reward attributes
    reward_address = 0x391c24
    xp = 600
    yoshi_cookie_item = items.Mushroom

    # Boss shuffle attributes.
    ratio_hp = 1.0
    ratio_fp = 1.0

    # shuffled overworld sprites
    sprite_height = 143
    sprite_width = 90
    
    #other_sprites = [786, 789, 789, 786]
    #other_sprites_sequences = [1, 0, 1, 0]

    sidekicks = [149, 150, 151, 152]

    model_small = {
        **models[511],
        "extra_props": {
            "sequence": 8,
            "is_empty": True,
            "freeze": True,
            "statue_mold": 3
        }
    }
    model_large = {
        **models[511]
    }
    dialog_replacements = [
        (49,'''CULEX: Please do not attempt to\n crack this egg again.[await][page]\n It will not give you thousands of\n experience points.[await]'''),
        (1660, ''' You have passed the first test.\n But you're not finished yet!\n Please enter.[await]'''),
        (1694, '''PIRATE: You're pretty tough, mate.\n All right. I'll let you through to\n Culex's place.[await]'''),
        (1695, '''PIRATE: That's AMAZING!\n No one's EVER whipped CULEX!![await]'''),
        (1778, '''CULEX: This world truly is\n uninhabitable for me and my kind...[await]'''),
        (1780, '''CULEX: Greetings. It is good to\n make your acquaintance once\n again.[await]'''),
        (1781, '''CULEX: This is not the encounter In expected when I came to visit this\n world.[await]'''),
        (1784, '''WATER CRYSTAL: I guess this is as\n close as I'll get to being returned\n to Mysidia.[await]'''),
        (1785, '''EARTH CRYSTAL: I thought the\n Dark Elf was a bit strange, until\n we came to this world.[await]\n You truly have some characters\n here![await]'''),
        (1792, '''FIRE CRYSTAL: Of course I'm\n miserable! We're UNDERWATER![await]'''),
        (1793, '''WIND CRYSTAL: Culex is nice and\n all, but I miss Yang sometimes.[await]'''),
        (2061, '''FIRE CRYSTAL: We needed a lot of\n heat to bake a cake of this size.[await]'''),
        (2062, '''WATER CRYSTAL: We must shape\n this confection to resemble Culex.[await]'''),
        (2504, '''CULEX: You must retrieve [0x7024] more\n item(s) before we may proceed.[await]\n Godspeed, champion knight![await]'''),
        (2560, '''SNIFIT 1: Hello there.[await]\n Culex is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]'''),
        (2572, '''SNIFIT 2: Please refrain\n from bothering Culex.[await]'''),
        (2831, '''\n           CULEX: Good day.[await]'''),
        (2832, '''WIND CRYSTAL: Welcome to our inn.[await][pause] To compete\n with our price-hiking rivals in the\n Feymarch Inn,[delay] we are offering free\n stays here in Seaside.[await]\n Will you be staying tonight?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]'''),
        (2834, ''' The two guys in the left building\n have been acting suspicious.[await]'''),
        (2836, ''' If you haven't been to the Sunken\n Ship yet, you can get there through\n the whirlpools in the sea.[await]'''),
        (2837, ''' If you haven't been to the Sunken\n Ship yet, you can get there after\n you crash the wedding over in\n Marrymore.[await]'''),
        (2838, ''' Have you been to Culex's\n house up on the hill yet?[await]'''),
        (2841, ''' Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]'''),
        (2842, ''' Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]'''),
        (2843, ''' Once you get through the Sunken\n Ship, you can... er...[await]'''),
        (2844, ''' You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]'''),
        (2847, '''FIRE CRYSTAL: This area is\n off-limits.[await]'''),
        (2848, '''WATER CRYSTAL: This door is a...\n uh... portal to another dimension!\n We can't let you fall into it.[await]'''),
        (3044, '''CULEX: It will be quite difficult to\n claim victory over the dojo master.\n I wish you luck.[await]'''),
        (3352, '''CULEX: Well met! Thank you for\n the excellent battle.[await]'''),
        (3353, '''CULEX: Well met! Thank you for\n the excellent battle.[await]'''),
    ]
    # Not sure if optional sidekicks really works with Culex as a donor, the 4 crystals are kinda distinct
    optional_dialog_replacements = [
    #    (1694, '''CRYSTAL: Proceed forth. Culex\n awaits you.[await]'''),
    #    (1695, '''CRYSTAL: Well met! You have\n satisfied Culex's hunger for a\n true challenge.[await]'''),
        (2560, '''EARTH CRYSTAL: Greetings.[await][pause] Culex\n is making preparations to head\n back to his home world, so he's\n busy right now.[await][page]\n Please come back later...\n [delay]unless you want to get hurt![await]'''),
        (2572, '''FIRE CRYSTAL: You are not going\n to find what you're seeking back\n here.[delay] Stay out.[await]'''),
        (3072, '''WATER CRYSTAL: Wind Crystal\n really should have been the one\n standing guard all the way up here.[await]'''),
        (3073, '''WATER CRYSTAL: Stand back!\n I might know Water Blast![await]'''),
    ]

# ********************* Default lists for the world.


def get_default_enemies(world):
    """

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        list[Enemy]: Default list of objects for the world.

    """
    return [
        Terrapin(world),
        Spikey(world),
        Skytroopa(world),
        MadMallet(world),
        Shaman(world),
        Crook(world),
        Goomba(world),
        PiranhaPlant(world),
        Amanita(world),
        Goby(world),
        Bloober(world),
        BandanaRed(world),
        Lakitu(world),
        Birdy(world),
        Pinwheel(world),
        Ratfunk(world),
        K9(world),
        Magmite(world),
        TheBigBoo(world),
        DryBones(world),
        Greaper(world),
        Sparky(world),
        Chomp(world),
        Pandorite(world),
        ShyRanger(world),
        Bobomb(world),
        Spookum(world),
        HammerBro(world),
        Buzzer(world),
        Ameboid(world),
        Gecko(world),
        Wiggler(world),
        Crusty(world),
        Magikoopa(world),
        Leuko(world),
        Jawful(world),
        Enigma(world),
        Blaster(world),
        Guerrilla(world),
        Babayaga(world),
        Hobgoblin(world),
        Reacher(world),
        Shogun(world),
        Orbuser(world),
        HeavyTroopa(world),
        Shadow(world),
        Cluster(world),
        Bahamutt(world),
        Octolot(world),
        Frogog(world),
        Clerk(world),
        Gunyolk(world),
        Boomer(world),
        Remocon(world),
        Snapdragon(world),
        Stumpet(world),
        Dodo(world),
        Jester(world),
        Artichoker(world),
        Arachne(world),
        Carriboscis(world),
        Hippopo(world),
        Mastadoom(world),
        Corkpedite(world),
        Terracotta(world),
        Spikester(world),
        Malakoopa(world),
        Pounder(world),
        Poundette(world),
        Sackit(world),
        GuGoomba(world),
        Chewy(world),
        Fireball(world),
        MrKipper(world),
        FactoryChief(world),
        BandanaBlue(world),
        Manager(world),
        Bluebird(world),
        AlleyRat(world),
        Chow(world),
        Magmus(world),
        LilBoo(world),
        Vomer(world),
        GlumReaper(world),
        Pyrosphere(world),
        ChompChomp(world),
        Hidon(world),
        SlingShy(world),
        Robomb(world),
        ShyGuy(world),
        Ninja(world),
        Stinger(world),
        Goombette(world),
        Geckit(world),
        Jabit(world),
        Starcruster(world),
        Merlin(world),
        Muckle(world),
        Forkies(world),
        Gorgon(world),
        BigBertha(world),
        ChainedKong(world),
        Fautso(world),
        Strawhead(world),
        Juju(world),
        ArmoredAnt(world),
        Orbison(world),
        TuboTroopa(world),
        Doppel(world),
        Pulsar(world),
        Octovader(world),
        Ribbite(world),
        Director(world),
        Puppox(world),
        FinkFlower(world),
        Lumbler(world),
        Springer(world),
        Harlequin(world),
        Kriffid(world),
        Spinthra(world),
        Radish(world),
        Crippo(world),
        MastaBlasta(world),
        Piledriver(world),
        Apprentice(world),
        BoxBoy(world),
        Shelly(world),
        Superspike(world),
        DodoSolo(world),
        Oerlikon(world),
        Chester(world),
        CorkpediteBody(world),
        Torte(world),
        Shyaway(world),
        JinxClone(world),
        MachineMadeShyster(world),
        MachineMadeDrillBit(world),
        Formless(world),
        Mokura(world),
        FireCrystal(world),
        WaterCrystal(world),
        EarthCrystal(world),
        WindCrystal(world),
        MarioClone(world),
        PeachClone(world),
        BowserClone(world),
        GenoClone(world),
        MallowClone(world),
        Shyster(world),
        Kinklink(world),
        HanginShy(world),
        Smelter(world),
        MachineMadeMack(world),
        MachineMadeBowyer(world),
        MachineMadeYaridovich(world),
        MachineMadeAxemPink(world),
        MachineMadeAxemBlack(world),
        MachineMadeAxemRed(world),
        MachineMadeAxemYellow(world),
        MachineMadeAxemGreen(world),
        Starslap(world),
        Mukumuku(world),
        Zeostar(world),
        Jagger(world),
        Chompweed(world),
        Smithy2TankHead(world),
        Smithy2SafeHead(world),
        Microbomb(world),
        Grit(world),
        Neosquid(world),
        YaridovichMirage(world),
        Helio(world),
        RightEye(world),
        LeftEye(world),
        KnifeGuy(world),
        GrateGuy(world),
        Bundt(world),
        Jinx1(world),
        Jinx2(world),
        CountDown(world),
        DingALing(world),
        Belome1(world),
        Belome2(world),
        Smilax(world),
        Thrax(world),
        Megasmilax(world),
        Birdo(world),
        Eggbert(world),
        AxemYellow(world),
        Punchinello(world),
        TentaclesRight(world),
        AxemRed(world),
        AxemGreen(world),
        KingBomb(world),
        MezzoBomb(world),
        Raspberry(world),
        KingCalamari(world),
        TentaclesLeft(world),
        Jinx3(world),
        Zombone(world),
        CzarDragon(world),
        Cloaker(world),
        Domino(world),
        MadAdder(world),
        Mack(world),
        Bodyguard(world),
        Yaridovich(world),
        DrillBit(world),
        AxemPink(world),
        AxemBlack(world),
        Bowyer(world),
        Aero(world),
        Exor(world),
        Smithy1(world),
        Shyper(world),
        Smithy2Body(world),
        Smithy2Head(world),
        Smithy2MageHead(world),
        Smithy2ChestHead(world),
        Croco1(world),
        Croco2(world),
        Earthlink(world),
        Bowser(world),
        AxemRangers(world),
        Booster(world),
        Booster2(world),
        Snifit(world),
        Johnny(world),
        JohnnySolo(world),
        Valentina(world),
        Cloaker2(world),
        Domino2(world),
        Candle(world),
        Culex(world),
    ]
