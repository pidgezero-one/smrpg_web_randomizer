# Data module for spell data.

from randomizer.logic import utils
from randomizer.logic.patch import Patch
from randomizer.data.utils import palette_to_bytes

import enum

STARTING_FP = 10

class SpellType(enum.Enum):
    Damage = 0
    Heal = 1

class EffectType(enum.Enum):
    Inflict = 2
    Nullify = 4

class SpellElement(enum.Enum):
    Ice = 0x10
    Thunder = 0x20
    Fire = 0x40
    Earth = 0x80

class InflictFunction(enum.Enum):
    Scan = 0
    Miss = 1
    NoDmg = 2
    Revive = 3
    IncJump = 4

class Spell:
    """Class representing a magic spell to be randomized."""
    BASE_ADDRESS = 0x3a20f1
    BASE_NAME_ADDRESS = 0x3A137F
    BASE_DESC_ADDRESS = 0x3a2b80

    # Default per-spell attributes.
    index = 0
    fp = 0
    power = 0
    hit_rate = 0
    instant_ko = False

    title = None

    anim_ptr = None # I'm not writing an assembler for this yet
    desc_ptr = None

    spell_type = SpellType.Damage
    effect_type = None
    inflict = None
    element = None

    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    quad9s = False
    hideNum = False

    targetOthers = False
    targetEnemies = False
    targetParty = False
    targetWounded = False
    targetOneParty = False
    targetNotSelf = False

    status_effects = []
    boosts = []



    def __init__(self, world):
        """

        Args:
            world (randomizer.logic.main.GameWorld):

        """
        self.world = world

    def __str__(self):
        return "<{}>".format(self.name)

    def __repr__(self):
        return str(self)

    @property
    def name(self):
        return self.__class__.__name__

    def get_patch(self):
        """Get patch for this spell.

        :return: Patch data.
        :rtype: randomizer.logic.patch.Patch
        """
        patch = Patch()

        # FP is byte 3, power is byte 6, hit rate is byte 7.  Each spell is 12 bytes.
        base_addr = self.BASE_ADDRESS + (self.index * 12)
        patch.add_data(base_addr, (self.checkStats * 0x01) + (self.ignoreDefense * 0x02) + (self.checkOHKO * 0x20) + (self.overworldUsable * 0x80))
        if self.spell_type is None:
            st = 0
        else:
            st = self.spell_type.value
        if self.effect_type is None:
            et = 0
        else:
            et = self.effect_type.value
        if self.element is None:
            el = 0
        else:
            el = self.element.value
        if self.inflict is None:
            iv = 0xFF
        else:
            iv = self.inflict.value
        patch.add_data(base_addr + 1, st + et + (self.quad9s * 0x08))
        patch.add_data(base_addr + 2, utils.ByteField(self.fp).as_bytes())
        patch.add_data(base_addr + 3, (self.targetOthers * 0x02) + (self.targetEnemies * 0x04) + (self.targetParty * 0x10) + (self.targetWounded * 0x20) + (self.targetOneParty * 0x40) + (self.targetNotSelf * 0x80))
        patch.add_data(base_addr + 4, el)
        data = utils.ByteField(self.power).as_bytes()
        data += utils.ByteField(self.hit_rate).as_bytes()
        patch.add_data(base_addr + 5, data)
        effects = 0
        for i in self.status_effects:
            effects += 2 ** i
        patch.add_data(base_addr + 7, effects)
        buffs = 0
        for i in self.boosts:
            buffs += 2 ** i
        patch.add_data(base_addr + 8, buffs)
        patch.add_data(base_addr + 10, iv)
        patch.add_data(base_addr + 11, (self.hideNum * 0x04))



        return patch


class CharacterSpell(Spell):
    """Grouping class for character-specific spells."""
    base_title = ""

    timingModifiers = 0
    damageModifiers = 0

    def get_patch(self):
        """Get patch for this spell.

        :return: Patch data.
        :rtype: randomizer.logic.patch.Patch
        """
        patch = super().get_patch()

        name_bytes = '\x40' + self.title
        name_bytes += " " * (15 - len(name_bytes))
        patch.add_data(self.BASE_NAME_ADDRESS + (self.index * 15), name_bytes)
        patch.add_data(0x02CACE + self.index * 2, bytearray([self.timingModifiers & 0xFF, (self.timingModifiers >> 8) & 0xFF]))
        patch.add_data(0x02D05B + self.index * 2, bytearray([self.damageModifiers & 0xFF, (self.damageModifiers >> 8) & 0xFF]))

        return patch

class CloneSpell(CharacterSpell):
    reference_spell = None
    ref_ptr = None
    """Spell class that allows an ally spell to be repeated with a different name."""
    def __init__(self, world, title, spell):
        super().__init__(world)
        self.title = title
        self.base_title = title
        self.fp = spell.fp
        self.power = spell.power
        self.hit_rate = spell.hit_rate
        self.reference_spell = spell.base_title
        self.ref_ptr = spell.anim_ptr
        self.desc_ptr = spell.desc_ptr
        self.checkStats = spell.checkStats
        self.ignoreDefense = spell.ignoreDefense
        self.checkOHKO = spell.checkOHKO
        self.overworldUsable = spell.overworldUsable
        self.spell_type = spell.spell_type
        self.effect_type = spell.effect_type
        self.quad9s = spell.quad9s
        self.targetOthers = spell.targetOthers
        self.targetEnemies = spell.targetEnemies
        self.targetParty = spell.targetParty
        self.targetWounded = spell.targetWounded
        self.targetOneParty = spell.targetOneParty
        self.targetNotSelf = spell.targetNotSelf
        self.element = spell.element
        self.status_effects = spell.status_effects
        self.boosts = spell.boosts
        self.inflict = spell.inflict
        self.hideNum = spell.hideNum
        self.timingModifiers = spell.timingModifiers
        self.damageModifiers = spell.damageModifiers


    def get_patch(self):
        """Get patch for this spell.

        :return: Patch data.
        :rtype: randomizer.logic.patch.Patch
        """
        patch = super().get_patch()

        patch.add_data(0x35C992 + self.index * 2, bytearray([self.ref_ptr & 0xFF, (self.ref_ptr >> 8) & 0xFF]))
        patch.add_data(0x3A2B80 + self.index * 2, bytearray([self.desc_ptr & 0xFF, (self.desc_ptr >> 8) & 0xFF]))

        return patch

class EnemySpell(Spell):
    """Grouping class for enemy-specific spells."""

    @property
    def title(self):
        return self.__class__.__name__

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()

        # Add status effects for enemy attacks, if any.
        base_addr = self.BASE_ADDRESS + (self.index * 12)
        data = utils.BitMapSet(1, self.status_effects).as_bytes()
        patch.add_data(base_addr + 7, data)

        return patch


# ********************* Actual data classes

class Jump(CharacterSpell):
    index = 0
    fp = 3
    power = 25
    hit_rate = 100
    title = "Jump"
    base_title = "Jump"
    anim_ptr = 0x35C9CE
    desc_ptr = 0x3A40A3
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = SpellElement.Earth
    status_effects = []
    boosts = []
    inflict = InflictFunction.IncJump
    hideNum = False
    timingModifiers = 0xcb0e
    damageModifiers = 0xd09b


class FireOrb(CharacterSpell):
    index = 1
    fp = 5
    power = 20
    hit_rate = 100
    title = "Fire Orb"
    base_title = "Fire Orb"
    anim_ptr = 0x35C9D2
    desc_ptr = 0x3A2BDF
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = SpellElement.Fire
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False
    timingModifiers = 0xcbd8
    damageModifiers = 0xd09c

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()

        if self.element == SpellElement.Ice:
            patch.add_data(0x253000 + 30 * 408, palette_to_bytes(["F8F8D0", "00F8F8", "00D0F8", "00A8F8", "0080F8", "0058F8", "0028F8", "0028F8", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0"]))
            patch.add_data(0x253000 + 30 * 392, palette_to_bytes(["F8F8F8", "A0F8F8", "40F8F8", "38D0F8", "30A8F8", "1850F8", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000"]))
        elif self.element == SpellElement.Thunder:
            patch.add_data(0x253000 + 30 * 408, palette_to_bytes(["F8F8F8", "B8F8F8", "F8F8F8", "B8F8F8", "F8F8F8", "B8F8F8", "F8F8F8", "B8F8F8", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0"]))
            patch.add_data(0x253000 + 30 * 392, palette_to_bytes(["F8F8F8", "B8F0F8", "B8E0F8", "B0E0F8", "A0D0F8", "80D0F8", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000"]))
        elif self.element == SpellElement.Earth:
            patch.add_data(0x253000 + 30 * 408, palette_to_bytes(["80F800", "78F800", "30D800", "38C800", "18B000", "008000", "78F800", "A8F800", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0"]))
            patch.add_data(0x253000 + 30 * 392, palette_to_bytes(["F8F8F8", "B8F800", "78F800", "30D800", "38C800", "18B000", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000"]))

        return patch
    


class SuperJump(CharacterSpell):
    index = 2
    fp = 7
    power = 45
    hit_rate = 100
    title = "Super Jump"
    base_title = "Super Jump"
    anim_ptr = 0x35C9D6
    desc_ptr = 0x3A2C01
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = SpellElement.Earth
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False
    timingModifiers = 0xcbd8
    damageModifiers = 0xd177


class SuperFlame(CharacterSpell):
    index = 3
    fp = 9
    power = 40
    hit_rate = 100
    title = "Super Flame"
    base_title = "Super Flame"
    anim_ptr = 0x35C9DA
    desc_ptr = 0x3A2C26
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = SpellElement.Fire
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False
    timingModifiers = 0xcbd8
    damageModifiers = 0xd09c

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()

        if self.element == SpellElement.Ice:
            patch.add_data(0x253000 + 30 * 817, palette_to_bytes(["F8F8D0", "00F8F8", "00D0F8", "00A8F8", "0080F8", "0058F8", "0028F8", "0028F8", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0"]))
            patch.add_data(0x253000 + 30 * 815, palette_to_bytes(["F8F8F8", "A0F8F8", "40F8F8", "38D0F8", "30A8F8", "1850F8", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000"]))
        elif self.element == SpellElement.Thunder:
            patch.add_data(0x253000 + 30 * 817, palette_to_bytes(["F8F8F8", "B8F8F8", "F8F8F8", "B8F8F8", "F8F8F8", "B8F8F8", "F8F8F8", "B8F8F8", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0"]))
            patch.add_data(0x253000 + 30 * 815, palette_to_bytes(["F8F8F8", "B8F0F8", "B8E0F8", "B0E0F8", "A0D0F8", "80D0F8", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000"]))
        elif self.element == SpellElement.Earth:
            patch.add_data(0x253000 + 30 * 817, palette_to_bytes(["80F800", "78F800", "30D800", "38C800", "18B000", "008000", "78F800", "A8F800", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0"]))
            patch.add_data(0x253000 + 30 * 815, palette_to_bytes(["F8F8F8", "B8F800", "78F800", "30D800", "38C800", "18B000", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000"]))

        return patch

class UltraJump(CharacterSpell):
    index = 4
    fp = 11
    power = 65
    hit_rate = 100
    title = "Ultra Jump"
    base_title = "Ultra Jump"
    anim_ptr = 0x35C9E4
    desc_ptr = 0x3A2C4A
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = SpellElement.Earth
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False
    timingModifiers = 0xcc44
    damageModifiers = 0xd0fb


class UltraFlame(CharacterSpell):
    index = 5
    fp = 14
    power = 60
    hit_rate = 100
    title = "Ultra Flame"
    base_title = "Ultra Flame"
    anim_ptr = 0x35C9E8
    desc_ptr = 0x3A2C6F
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = SpellElement.Fire
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False
    timingModifiers = 0xcc44
    damageModifiers = 0xd14f

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()

        if self.element == SpellElement.Ice:
            patch.add_data(0x253000 + 30 * 818, palette_to_bytes(["F8F8D0", "00F8F8", "00D0F8", "00A8F8", "0080F8", "0058F8", "0028F8", "0028F8", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0"]))
            patch.add_data(0x253000 + 30 * 816, palette_to_bytes(["F8F8F8", "A0F8F8", "40F8F8", "38D0F8", "30A8F8", "1850F8", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000"]))
        elif self.element == SpellElement.Thunder:
            patch.add_data(0x253000 + 30 * 818, palette_to_bytes(["F8F8F8", "B8F8F8", "F8F8F8", "B8F8F8", "F8F8F8", "B8F8F8", "F8F8F8", "B8F8F8", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0"]))
            patch.add_data(0x253000 + 30 * 816, palette_to_bytes(["F8F8F8", "B8F0F8", "B8E0F8", "B0E0F8", "A0D0F8", "80D0F8", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000"]))
        elif self.element == SpellElement.Earth:
            patch.add_data(0x253000 + 30 * 818, palette_to_bytes(["80F800", "78F800", "30D800", "38C800", "18B000", "008000", "78F800", "A8F800", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0", "0000D0"]))
            patch.add_data(0x253000 + 30 * 816, palette_to_bytes(["F8F8F8", "B8F800", "78F800", "30D800", "38C800", "18B000", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000"]))

        return patch

class Therapy(CharacterSpell):
    index = 6
    fp = 2
    power = 40
    hit_rate = 100
    title = "Therapy"
    base_title = "Therapy"
    anim_ptr = 0x35C9F2
    desc_ptr = 0x3A2C92
    
    checkStats = False
    ignoreDefense = True
    checkOHKO = False
    overworldUsable = True
    spell_type = SpellType.Heal
    effect_type = EffectType.Nullify
    quad9s = False
    targetOthers = True
    targetEnemies = False
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = [0, 1, 2, 3, 4, 5, 6]
    boosts = []
    inflict = None
    hideNum = False
    timingModifiers = 0xcb0e
    damageModifiers = 0xd09b


class GroupHug(CharacterSpell):
    index = 7
    fp = 4
    power = 30
    hit_rate = 100
    title = "Group Hug"
    base_title = "Group Hug"
    anim_ptr = 0x35C9FC
    desc_ptr = 0x3A2CA6
    
    checkStats = False
    ignoreDefense = True
    checkOHKO = False
    overworldUsable = True
    spell_type = SpellType.Heal
    effect_type = EffectType.Nullify
    quad9s = False
    targetOthers = False
    targetEnemies = False
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = [0, 1, 2, 3, 4, 5, 6]
    boosts = []
    inflict = None
    hideNum = False
    timingModifiers = 0xcd1e
    damageModifiers = 0xd09b


class SleepyTime(CharacterSpell):
    index = 8
    fp = 4
    hit_rate = 99
    title = "Sleepy Time"
    base_title = "Sleepy Time"
    anim_ptr = 0x35CA00
    desc_ptr = 0x3A2CBF
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = EffectType.Inflict
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = [1]
    boosts = []
    inflict = None
    hideNum = True
    timingModifiers = 0xcd3f
    damageModifiers = 0xd09b


class ComeBack(CharacterSpell):
    index = 9
    fp = 2
    hit_rate = 100
    title = "Come Back"
    base_title = "Come Back"
    anim_ptr = 0x35CA07
    desc_ptr = 0x3A2CD6
    
    checkStats = False
    ignoreDefense = True
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Heal
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = False
    targetParty = False
    targetWounded = True
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = InflictFunction.Revive
    hideNum = False
    timingModifiers = 0xcda2
    damageModifiers = 0xd09b


class Mute(CharacterSpell):
    index = 10
    fp = 3
    hit_rate = 99
    title = "Mute"
    base_title = "Mute"
    anim_ptr = 0x35CA11
    desc_ptr = 0x3A2CF4
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = EffectType.Inflict
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = [0]
    boosts = []
    inflict = None
    hideNum = True
    timingModifiers = 0xcd3f
    damageModifiers = 0xd09b


class PsychBomb(CharacterSpell):
    index = 11
    fp = 15
    power = 60
    hit_rate = 100
    title = "Psych Bomb"
    base_title = "Psych Bomb"
    anim_ptr = 0x35CA1B
    desc_ptr = 0x3A2D0C
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False
    timingModifiers = 0xcde1
    damageModifiers = 0xd09c


class Terrorize(CharacterSpell):
    index = 12
    fp = 6
    power = 10
    hit_rate = 90
    title = "Terrorize"
    base_title = "Terrorize"
    anim_ptr = 0x35CA22
    desc_ptr = 0x3A2D26
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = EffectType.Inflict
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = [3]
    boosts = []
    inflict = None
    hideNum = False
    timingModifiers = 0xce75
    damageModifiers = 0xd09c


class PoisonGas(CharacterSpell):
    index = 13
    fp = 10
    power = 20
    hit_rate = 90
    title = "Poison Gas"
    base_title = "Poison Gas"
    anim_ptr = 0x35CA2C
    desc_ptr = 0x3A2D36
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = EffectType.Inflict
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = [2]
    boosts = []
    inflict = None
    hideNum = False
    timingModifiers = 0xce75
    damageModifiers = 0xd09c


class Crusher(CharacterSpell):
    index = 14
    fp = 12
    power = 60
    hit_rate = 100
    title = "Crusher"
    base_title = "Crusher"
    anim_ptr = 0x35CA36
    desc_ptr = 0x3A2D44
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False
    timingModifiers = 0xcb0e
    damageModifiers = 0xd09b


class BowserCrush(CharacterSpell):
    index = 15
    fp = 16
    power = 58
    hit_rate = 100
    title = "Bowser Crush"
    base_title = "Bowser Crush"
    anim_ptr = 0x35CA40
    desc_ptr = 0x3A2D6D
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False
    timingModifiers = 0xcde1
    damageModifiers = 0xd09c


class GenoBeam(CharacterSpell):
    index = 16
    fp = 3
    power = 40
    hit_rate = 100
    title = "Geno Beam"
    base_title = "Geno Beam"
    anim_ptr = 0x35CA47
    desc_ptr = 0x3A2D87
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False
    timingModifiers = 0xce85
    damageModifiers = 0xd09b


class GenoBoost(CharacterSpell):
    index = 17
    fp = 4
    hit_rate = 100
    title = "Geno Boost"
    base_title = "Geno Boost"
    anim_ptr = 0x35CA4E
    desc_ptr = 0x3A2DB0
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = EffectType.Inflict
    quad9s = False
    targetOthers = True
    targetEnemies = False
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = [3, 4]
    inflict = None
    hideNum = True
    timingModifiers = 0xcf22
    damageModifiers = 0xd09b


class GenoWhirl(CharacterSpell):
    index = 18
    fp = 8
    power = 45
    hit_rate = 100
    title = "Geno Whirl"
    base_title = "Geno Whirl"
    anim_ptr = 0x35CA58
    desc_ptr = 0x3A2DD8
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False
    timingModifiers = 0xcf63
    damageModifiers = 0xd09b


class GenoBlast(CharacterSpell):
    index = 19
    fp = 12
    power = 50
    hit_rate = 100
    title = "Geno Blast"
    base_title = "Geno Blast"
    anim_ptr = 0x35CA62
    desc_ptr = 0x3A2E05
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False
    timingModifiers = 0xce85
    damageModifiers = 0xd09b


class GenoFlash(CharacterSpell):
    index = 20
    fp = 16
    power = 60
    hit_rate = 100
    title = "Geno Flash"
    base_title = "Geno Flash"
    anim_ptr = 0x35CA69
    desc_ptr = 0x3A2E26
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False
    timingModifiers = 0xce85
    damageModifiers = 0xd09b


class Thunderbolt(CharacterSpell):
    index = 21
    fp = 2
    power = 15
    hit_rate = 100
    title = "Thunderbolt"
    base_title = "Thunderbolt"
    anim_ptr = 0x35CA73
    desc_ptr = 0x3A2E4A
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = SpellElement.Thunder
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False
    timingModifiers = 0xcd1e
    damageModifiers = 0xd09b

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()

        if self.element == SpellElement.Ice:
            patch.add_data(0x33cb1f, bytearray([0x7E, 0x40, 0xC0, 0x51, 0x20, 0x67, 0xF3, 0x7F]))
        elif self.element == SpellElement.Fire:
            patch.add_data(0x33cb1f, bytearray([0x7E, 0x40, 0x11, 0x00, 0x99, 0x01, 0xFF, 0x03]))
        elif self.element == SpellElement.Earth:
            patch.add_data(0x33cb1f, bytearray([0x7E, 0x40, 0x00, 0x06, 0x20, 0x13, 0xF8, 0x03]))

        return patch


class HPRain(CharacterSpell):
    index = 22
    fp = 2
    power = 10
    hit_rate = 100
    title = "HP Rain"
    base_title = "HP Rain"
    anim_ptr = 0x35CA7D
    desc_ptr = 0x3A2E6C
    
    checkStats = False
    ignoreDefense = True
    checkOHKO = False
    overworldUsable = True
    spell_type = SpellType.Heal
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = False
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False
    timingModifiers = 0xcb0e
    damageModifiers = 0xd09b


class Psychopath(CharacterSpell):
    index = 23
    fp = 1
    hit_rate = 100
    title = "Psychopath"
    base_title = "Psychopath"
    anim_ptr = 0x35CA84
    desc_ptr = 0x3A2E9E
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = InflictFunction.Scan
    hideNum = True
    timingModifiers = 0xcfc2
    damageModifiers = 0xd09b


class Shocker(CharacterSpell):
    index = 24
    fp = 8
    power = 60
    hit_rate = 100
    title = "Shocker"
    base_title = "Shocker"
    anim_ptr = 0x35CA8E
    desc_ptr = 0x3A2EBC
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = SpellElement.Thunder
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False
    timingModifiers = 0xcb0e
    damageModifiers = 0xd09b

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()
        if self.element == SpellElement.Ice:
            patch.add_data(0x330bb8, bytearray([0x00, 0x00, 0x9F, 0x73, 0xF8, 0x7F, 0xF4, 0x7F, 0xF0, 0x7F, 0xEC, 0x7F, 0xE9, 0x7F, 0xC0, 0x5A, 0x00, 0x42, 0xE0, 0x3D, 0x00, 0x21, 0x20, 0x25, 0x80, 0x10, 0x40, 0x08]))
        elif self.element == SpellElement.Fire:
            patch.add_data(0x330bb8, bytearray([0x00, 0x00, 0x9F, 0x73, 0x1F, 0x63, 0x9F, 0x52, 0x1F, 0x42, 0x9F, 0x31, 0x3F, 0x25, 0x16, 0x00, 0x10, 0x00, 0x0F, 0x00, 0x08, 0x00, 0x09, 0x00, 0x04, 0x00, 0x02]))
        elif self.element == SpellElement.Earth:
            patch.add_data(0x330bb8, bytearray([0x00, 0x00, 0xF4, 0x53, 0xEA, 0x2B, 0xE0, 0x03, 0xE0, 0x03, 0xA0, 0x03, 0x20, 0x03, 0xA0, 0x02, 0x00, 0x02, 0xE0, 0x01, 0x00, 0x01, 0x20, 0x01, 0x80, 0x00, 0x40, 0x08]))
        return patch


class Snowy(CharacterSpell):
    index = 25
    fp = 12
    power = 40
    hit_rate = 100
    title = "Snowy"
    base_title = "Snowy"
    anim_ptr = 0x35CA98
    desc_ptr = 0x3A2EDE
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = SpellElement.Ice
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False
    timingModifiers = 0xce75
    damageModifiers = 0xd09c

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()
        if self.element == SpellElement.Thunder:
            patch.add_data(0x33c141, bytearray([0x85, 0x02, 0xFF, 0x7F, 0xF8, 0x7F, 0xED, 0x7F]))
            patch.add_data(0x33c400, bytearray([00, 0x00, 0xFF, 0x7F]))
        elif self.element == SpellElement.Fire:
            patch.add_data(0x33c141, bytearray([0x85, 0x02, 0xDB, 0x02, 0x97, 0x01, 0x13, 0x00]))
            patch.add_data(0x33c400, bytearray([00, 0x00, 0xDB, 0x02]))
        elif self.element == SpellElement.Earth:
            patch.add_data(0x33c141, bytearray([0x85, 0x02, 0x40, 0x03, 0xA0, 0x02, 0x00, 0x02]))
            patch.add_data(0x33c400, bytearray([00, 0x00, 0x40, 0x03]))
        return patch



class StarRain(CharacterSpell):
    index = 26
    fp = 14
    power = 55
    hit_rate = 100
    title = "Star Rain"
    base_title = "Star Rain"
    anim_ptr = 0x35CAA2
    desc_ptr = 0x3A2EF4
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False
    timingModifiers = 0xcfdf
    damageModifiers = 0xd09c


class Clone1(CloneSpell):
    index = 27


class Clone2(CloneSpell):
    index = 28


class Clone3(CloneSpell):
    index = 29


class Drain(EnemySpell):
    index = 64
    fp = 1
    power = 4
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = SpellElement.Fire
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class LightningOrb(EnemySpell):
    index = 65
    fp = 2
    power = 8
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = SpellElement.Thunder
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class Flame(EnemySpell):
    index = 66
    fp = 3
    power = 12
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = SpellElement.Fire
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class Bolt(EnemySpell):
    index = 67
    fp = 4
    power = 20
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = SpellElement.Thunder
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class Crystal(EnemySpell):
    index = 68
    fp = 5
    power = 25
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = SpellElement.Ice
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class FlameStone(EnemySpell):
    index = 69
    fp = 6
    power = 32
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = SpellElement.Fire
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class MegaDrain(EnemySpell):
    index = 70
    fp = 7
    power = 40
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = SpellElement.Fire
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class WillyWisp(EnemySpell):
    index = 71
    fp = 8
    power = 48
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class DiamondSaw(EnemySpell):
    index = 72
    fp = 9
    power = 60
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class Electroshock(EnemySpell):
    index = 73
    fp = 10
    power = 72
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = SpellElement.Thunder
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class Blast(EnemySpell):
    index = 74
    fp = 11
    power = 89
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class Storm(EnemySpell):
    index = 75
    fp = 12
    power = 108
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class IceRock(EnemySpell):
    index = 76
    fp = 13
    power = 130
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = SpellElement.Ice
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class Escape(EnemySpell):
    index = 77
    hit_rate = 100
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = False
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = InflictFunction.NoDmg
    hideNum = False


class DarkStar(EnemySpell):
    index = 78
    fp = 20
    power = 160
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = True
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class Recover(EnemySpell):
    index = 79
    fp = 3
    power = 50
    hit_rate = 100
    
    checkStats = False
    ignoreDefense = True
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Heal
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = False
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class MegaRecover(EnemySpell):
    index = 80
    fp = 9
    power = 200
    hit_rate = 100
    
    checkStats = False
    ignoreDefense = True
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Heal
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = False
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class FlameWall(EnemySpell):
    index = 81
    fp = 2
    power = 8
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = SpellElement.Fire
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class StaticE(EnemySpell):
    index = 82
    fp = 4
    power = 12
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = SpellElement.Thunder
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class SandStorm(EnemySpell):
    index = 83
    fp = 6
    power = 16
    hit_rate = 90
    status_effects = [3]
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = EffectType.Inflict
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = [3]
    boosts = []
    inflict = None
    hideNum = False


class Blizzard(EnemySpell):
    index = 84
    fp = 8
    power = 22
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = SpellElement.Ice
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class DrainBeam(EnemySpell):
    index = 85
    fp = 10
    power = 26
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class MeteorBlast(EnemySpell):
    index = 86
    fp = 12
    power = 30
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class LightBeam(EnemySpell):
    index = 87
    fp = 13
    power = 34
    hit_rate = 90
    status_effects = [1]
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = EffectType.Inflict
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = [1]
    boosts = []
    inflict = None
    hideNum = False


class WaterBlast(EnemySpell):
    index = 88
    fp = 14
    power = 39
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class Solidify(EnemySpell):
    index = 89
    fp = 15
    power = 47
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = SpellElement.Ice
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class PetalBlast(EnemySpell):
    index = 90
    fp = 16
    power = 40
    hit_rate = 85
    status_effects = [5]
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = EffectType.Inflict
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = [5]
    boosts = []
    inflict = None
    hideNum = False


class AuroraFlash(EnemySpell):
    index = 91
    fp = 17
    power = 50
    hit_rate = 85
    status_effects = [1]
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = EffectType.Inflict
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = [1]
    boosts = []
    inflict = None
    hideNum = False


class Boulder(EnemySpell):
    index = 92
    fp = 18
    power = 72
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class Corona(EnemySpell):
    index = 93
    fp = 19
    power = 88
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = SpellElement.Fire
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class MeteorSwarm(EnemySpell):
    index = 94
    fp = 20
    power = 100
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class KnockOut(EnemySpell):
    index = 95
    fp = 15
    power = 1
    hit_rate = 60
    instant_ko = True
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = True
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = True
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class WeirdMushroom(EnemySpell):
    index = 96
    power = 30
    hit_rate = 100
    
    checkStats = False
    ignoreDefense = True
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Heal
    effect_type = None
    quad9s = False
    targetOthers = True
    targetEnemies = False
    targetParty = False
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class BreakerBeam(EnemySpell):
    index = 97
    fp = 15
    power = 80
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class Shredder(EnemySpell):
    index = 98
    fp = 8
    hit_rate = 100
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = EffectType.Nullify
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = [3, 4, 5, 6]
    inflict = None
    hideNum = True


class Sledge(EnemySpell):
    index = 99
    fp = 6
    power = 50
    hit_rate = 99
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class SwordRain(EnemySpell):
    index = 100
    fp = 8
    power = 80
    hit_rate = 99
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class SpearRain(EnemySpell):
    index = 101
    fp = 5
    power = 60
    hit_rate = 99
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False


class ArrowRain(EnemySpell):
    index = 102
    fp = 2
    power = 40
    hit_rate = 99
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False

class BigBang(EnemySpell):
    index = 103
    power = 100
    hit_rate = 100
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False

class ChestScrow(EnemySpell):
    index = 104
    power = 10
    hit_rate = 85
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = EffectType.Inflict
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = [6]
    boosts = []
    inflict = None
    hideNum = False

class ChestFear(EnemySpell):
    index = 105
    power = 0
    hit_rate = 82
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = EffectType.Inflict
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = [3]
    boosts = []
    inflict = None
    hideNum = True

class ChestMute(EnemySpell):
    index = 106
    power = 0
    hit_rate = 85
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = EffectType.Inflict
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = [0]
    boosts = []
    inflict = None
    hideNum = True

class ChestPoison(EnemySpell):
    index = 107
    power = 0
    hit_rate = 85
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = EffectType.Inflict
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = [2]
    boosts = []
    inflict = None
    hideNum = True

class ChainSaw(EnemySpell):
    index = 108
    power = 50
    hit_rate = 90
    
    checkStats = False
    ignoreDefense = False
    checkOHKO = False
    overworldUsable = False
    spell_type = SpellType.Damage
    effect_type = None
    quad9s = False
    targetOthers = False
    targetEnemies = True
    targetParty = True
    targetWounded = False
    targetOneParty = True
    targetNotSelf = False
    element = None
    status_effects = []
    boosts = []
    inflict = None
    hideNum = False

class Nothing(EnemySpell):
    index = 251
    power = 0
    hit_rate = 100


# ********************* Default lists for the world.

def get_default_spells(world):
    """Get default vanilla item list for the world.

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        list[Spell]: List of default spell objects.

    """
    return [
        Jump(world),
        FireOrb(world),
        SuperJump(world),
        SuperFlame(world),
        UltraJump(world),
        UltraFlame(world),
        Therapy(world),
        GroupHug(world),
        SleepyTime(world),
        ComeBack(world),
        Mute(world),
        PsychBomb(world),
        Terrorize(world),
        PoisonGas(world),
        Crusher(world),
        BowserCrush(world),
        GenoBeam(world),
        GenoBoost(world),
        GenoWhirl(world),
        GenoBlast(world),
        GenoFlash(world),
        Thunderbolt(world),
        HPRain(world),
        Psychopath(world),
        Shocker(world),
        Snowy(world),
        StarRain(world),
        Drain(world),
        LightningOrb(world),
        Flame(world),
        Bolt(world),
        Crystal(world),
        FlameStone(world),
        MegaDrain(world),
        WillyWisp(world),
        DiamondSaw(world),
        Electroshock(world),
        Blast(world),
        Storm(world),
        IceRock(world),
        Escape(world),
        DarkStar(world),
        Recover(world),
        MegaRecover(world),
        FlameWall(world),
        StaticE(world),
        SandStorm(world),
        Blizzard(world),
        DrainBeam(world),
        MeteorBlast(world),
        LightBeam(world),
        WaterBlast(world),
        Solidify(world),
        PetalBlast(world),
        AuroraFlash(world),
        Boulder(world),
        Corona(world),
        MeteorSwarm(world),
        KnockOut(world),
        WeirdMushroom(world),
        BreakerBeam(world),
        Shredder(world),
        Sledge(world),
        SwordRain(world),
        SpearRain(world),
        ArrowRain(world),
        BigBang(world),
        # ChestScrow(world),
        # ChestFear(world),
        # ChestMute(world),
        # ChestPoison(world),
        ChainSaw(world),
        # Nothing(world),
    ]

# BigBang is not in any of these tables. It's just a bad idea.
SingleTargets = [Drain, LightningOrb, Flame, Bolt, Crystal, FlameStone, MegaDrain, WillyWisp, DiamondSaw, Electroshock, Blast, Storm, IceRock, DarkStar]
Heals = [Recover, MegaRecover, WeirdMushroom]
MultiTargets = [FlameWall, StaticE, SandStorm, Blizzard, DrainBeam, MeteorBlast, LightBeam, WaterBlast, Solidify, PetalBlast, AuroraFlash, Boulder, Corona, MeteorSwarm, KnockOut, Shredder, Sledge, SwordRain, SpearRain, ArrowRain, ChestScrow, ChestFear, ChestMute, ChestPoison, ChainSaw]
DoNothing = [Nothing]
Run = [Escape]

SpellsToTargets = {
    Drain.index: SingleTargets,
    LightningOrb.index: SingleTargets,
    Flame.index: SingleTargets,
    Bolt.index: SingleTargets,
    Crystal.index: SingleTargets,
    FlameStone.index: SingleTargets,
    MegaDrain.index: SingleTargets,
    WillyWisp.index: SingleTargets,
    DiamondSaw.index: SingleTargets,
    Electroshock.index: SingleTargets,
    Blast.index: SingleTargets,
    Storm.index: SingleTargets,
    IceRock.index: SingleTargets,
    DarkStar.index: SingleTargets,

    Recover.index: Heals,
    MegaRecover.index: Heals,
    WeirdMushroom.index: Heals,

    FlameWall.index: MultiTargets,
    StaticE.index: MultiTargets,
    SandStorm.index: MultiTargets,
    Blizzard.index: MultiTargets,
    DrainBeam.index: MultiTargets,
    MeteorBlast.index: MultiTargets,
    LightBeam.index: MultiTargets,
    WaterBlast.index: MultiTargets,
    Solidify.index: MultiTargets,
    PetalBlast.index: MultiTargets,
    AuroraFlash.index: MultiTargets,
    Boulder.index: MultiTargets,
    Corona.index: MultiTargets,
    MeteorSwarm.index: MultiTargets,
    KnockOut.index: MultiTargets,
    Shredder.index: MultiTargets,
    Sledge.index: MultiTargets,
    SwordRain.index: MultiTargets,
    SpearRain.index: MultiTargets,
    ArrowRain.index: MultiTargets,
    ChestScrow.index: MultiTargets,
    ChestFear.index: MultiTargets,
    ChestMute.index: MultiTargets,
    ChestPoison.index: MultiTargets,
    ChainSaw.index: MultiTargets,

    # These can really only be done by their specific casters
    BreakerBeam.index: [BreakerBeam] + MultiTargets,
    BigBang.index: [BigBang] + MultiTargets,

    Nothing.index: DoNothing,
    Escape.index: Run,
}
