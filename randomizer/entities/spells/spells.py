from random import choice
from typing import Type
from randomizer.types.spells.classes import CharacterSpell, CloneSpell, EnemySpell
from randomizer.types.spells.constants.classes import DamageModifiers, TimingProperties
from randomizer.types.spells.constants.damage_modifiers import (
    NO_MODIFIERS,
    X00625_MODIFIER,
    X00625_MODIFIER_WITH_MULTI_TARGETING,
    X0125_MODIFIER_WITH_MULTI_TARGETING,
    X05_MODIFIER,
)
from randomizer.types.spells.constants.timing_properties import (
    BUTTON_MASH,
    CHARGE_ONLY,
    MULTIPLE_BUTTON_PRESSES,
    ONE_PLUS_MORE_TARGETS_WITH_PRESSES,
    ONE_TIMING_FOR_125_DMG_ONLY,
    ONE_TIMING_FOR_125_OR_15X_DMG,
    ROTATE_1_TARGET_IF_TIMED_ALL,
    ROTATE_ONLY,
    TIME_TO_ACTIVATE_HP_READ,
    TIMED_FOR_9999_SET_ENEMY_HP_0,
    TIMED_GIVES_TARGET_DEFENSE_UP_BUFF,
    TIMED_HEALS_ALL_HP_TO_FIRST_TARGET,
    TIMED_JUMPS,
)
from randomizer.types.spells.enums import (
    EffectType,
    InflictFunction,
    SpellBoosts,
    SpellElement,
    SpellStatusEffects,
    SpellType,
)

from randomizer.entities.spells.palettes import (
    FIRE_ORB_EARTH_BALL,
    FIRE_ORB_EARTH_FADE,
    FIRE_ORB_ICE_BALL,
    FIRE_ORB_ICE_FADE,
    FIRE_ORB_THUNDER_BALL,
    FIRE_ORB_THUNDER_FADE,
    SHOCKER_EARTH,
    SHOCKER_FIRE,
    SHOCKER_ICE,
    SNOWY_EARTH_LOWER,
    SNOWY_EARTH_UPPER,
    SNOWY_FIRE_LOWER,
    SNOWY_FIRE_UPPER,
    SNOWY_THUNDER_LOWER,
    SNOWY_THUNDER_UPPER,
    THUNDERBOLT_EARTH,
    THUNDERBOLT_FIRE,
    THUNDERBOLT_ICE,
)
from randomizer.types.world.flags.flags import CharacterSpellElements


class Jump(CharacterSpell):
    _index: int = 0
    _fp: int = 3
    _power: int = 25
    _hit_rate: int = 100

    _title: str = "Jump"

    _anim_ptr: int = 0x35C9CE
    _desc_ptr: int = 0x3A40A3

    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _inflict: InflictFunction = InflictFunction.IncJump
    _element: SpellElement = SpellElement.Jump

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _quad9s: bool = False
    _hideNum: bool = False

    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False

    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []

    _timing_modifiers: TimingProperties = ONE_TIMING_FOR_125_OR_15X_DMG
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 512


class IceJump(Jump):
    _title: str = "Ice Jump"
    _element: SpellElement = SpellElement.Ice


class ThunderJump(Jump):
    _title: str = "Thunder Jump"
    _element: SpellElement = SpellElement.Thunder


class FireJump(Jump):
    _title: str = "Fire Jump"
    _element: SpellElement = SpellElement.Fire


class FireOrb(CharacterSpell):
    _index: int = 1
    _fp: int = 5
    _power: int = 20
    _hit_rate: int = 100
    _title: str = "Fire Orb"
    _anim_ptr: int = 0x35C9D2
    _desc_ptr: int = 0x3A2BDF

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement = SpellElement.Fire
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False
    _timing_modifiers: TimingProperties = MULTIPLE_BUTTON_PRESSES
    _damage_modifiers: DamageModifiers = X00625_MODIFIER

    _item_id: int = 513


class IceOrb(FireOrb):
    _title: str = "Ice Orb"
    _element: SpellElement = SpellElement.Ice

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()

        patch.add_data(0x253000 + 30 * 408, FIRE_ORB_ICE_BALL.to_bytes())
        patch.add_data(0x253000 + 30 * 392, FIRE_ORB_ICE_FADE.to_bytes())

        return patch


class ThunderOrb(FireOrb):
    _title: str = "Thunder Orb"
    _element: SpellElement = SpellElement.Thunder

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()

        patch.add_data(0x253000 + 30 * 408, FIRE_ORB_THUNDER_BALL.to_bytes())
        patch.add_data(0x253000 + 30 * 392, FIRE_ORB_THUNDER_FADE.to_bytes())

        return patch


class EarthOrb(FireOrb):
    _title: str = "Earth Orb"
    _element: SpellElement = SpellElement.Earth

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()

        patch.add_data(0x253000 + 30 * 408, FIRE_ORB_EARTH_BALL.to_bytes())
        patch.add_data(0x253000 + 30 * 392, FIRE_ORB_EARTH_FADE.to_bytes())

        return patch


class SuperJump(CharacterSpell):
    _index: int = 2
    _fp: int = 7
    _power: int = 45
    _hit_rate: int = 100
    _title: str = "Super Jump"
    _anim_ptr: int = 0x35C9D6
    _desc_ptr: int = 0x3A2C01

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement = SpellElement.Jump
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False
    _timing_modifiers: TimingProperties = MULTIPLE_BUTTON_PRESSES
    _damage_modifiers: DamageModifiers = X05_MODIFIER

    _item_id: int = 514


class IceSuperJump(SuperJump):
    _title: str = "Ice S.Jump"
    _element: SpellElement = SpellElement.Ice


class ThunderSuperJump(SuperJump):
    _title: str = "Thndr S.Jump"
    _element: SpellElement = SpellElement.Thunder


class FireSuperJump(SuperJump):
    _title: str = "Fire S.Jump"
    _element: SpellElement = SpellElement.Fire


class SuperFlame(CharacterSpell):
    _index: int = 3
    _fp: int = 9
    _power: int = 40
    _hit_rate: int = 100
    _title: str = "Super Flame"
    _anim_ptr: int = 0x35C9DA
    _desc_ptr: int = 0x3A2C26

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement = SpellElement.Fire
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False
    _timing_modifiers: TimingProperties = MULTIPLE_BUTTON_PRESSES
    _damage_modifiers: DamageModifiers = X00625_MODIFIER

    _item_id: int = 515


class IceSuperFlame(SuperFlame):
    _title: str = "Super Ice"
    _element: SpellElement = SpellElement.Ice

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()

        patch.add_data(0x253000 + 30 * 817, FIRE_ORB_ICE_BALL.to_bytes())
        patch.add_data(0x253000 + 30 * 815, FIRE_ORB_ICE_FADE.to_bytes())

        return patch


class ThunderSuperFlame(SuperFlame):
    _title: str = "SuperThunder"
    _element: SpellElement = SpellElement.Thunder

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()

        patch.add_data(0x253000 + 30 * 817, FIRE_ORB_THUNDER_BALL.to_bytes())
        patch.add_data(0x253000 + 30 * 815, FIRE_ORB_THUNDER_FADE.to_bytes())

        return patch


class EarthSuperFlame(SuperFlame):
    _title: str = "Super Earth"
    _element: SpellElement = SpellElement.Earth

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()

        patch.add_data(0x253000 + 30 * 817, FIRE_ORB_EARTH_BALL.to_bytes())
        patch.add_data(0x253000 + 30 * 815, FIRE_ORB_EARTH_FADE.to_bytes())

        return patch


class UltraJump(CharacterSpell):
    _index: int = 4
    _fp: int = 11
    _power: int = 65
    _hit_rate: int = 100
    _title: str = "Ultra Jump"
    _anim_ptr: int = 0x35C9E4
    _desc_ptr: int = 0x3A2C4A

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement = SpellElement.Jump
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False
    _timing_modifiers: TimingProperties = ONE_PLUS_MORE_TARGETS_WITH_PRESSES
    _damage_modifiers: DamageModifiers = X0125_MODIFIER_WITH_MULTI_TARGETING

    _item_id: int = 516


class IceUltraJump(UltraJump):
    _title: str = "Ice U.Jump"
    _element: SpellElement = SpellElement.Ice


class ThunderUltraJump(UltraJump):
    _title: str = "Thndr U.Jump"
    _element: SpellElement = SpellElement.Thunder


class FireUltraJump(UltraJump):
    _title: str = "Fire U.Jump"
    _element: SpellElement = SpellElement.Fire


class UltraFlame(CharacterSpell):
    _index: int = 5
    _fp: int = 14
    _power: int = 60
    _hit_rate: int = 100
    _title: str = "Ultra Flame"
    _anim_ptr: int = 0x35C9E8
    _desc_ptr: int = 0x3A2C6F

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement = SpellElement.Fire
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False
    _timing_modifiers: TimingProperties = ONE_PLUS_MORE_TARGETS_WITH_PRESSES
    _damage_modifiers: DamageModifiers = X00625_MODIFIER_WITH_MULTI_TARGETING

    _item_id: int = 517


class IceUltraFlame(UltraFlame):
    _title: str = "Ultra Ice"
    _element: SpellElement = SpellElement.Ice

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()

        patch.add_data(0x253000 + 30 * 818, FIRE_ORB_ICE_BALL.to_bytes())
        patch.add_data(0x253000 + 30 * 816, FIRE_ORB_ICE_FADE.to_bytes())

        return patch


class ThunderUltraFlame(UltraFlame):
    _title: str = "UltraThunder"
    _element: SpellElement = SpellElement.Thunder

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()

        patch.add_data(0x253000 + 30 * 818, FIRE_ORB_THUNDER_BALL.to_bytes())
        patch.add_data(0x253000 + 30 * 816, FIRE_ORB_THUNDER_FADE.to_bytes())

        return patch


class EarthUltraFlame(UltraFlame):
    _title: str = "Ultra Earth"
    _element: SpellElement = SpellElement.Earth

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()

        patch.add_data(0x253000 + 30 * 818, FIRE_ORB_EARTH_BALL.to_bytes())
        patch.add_data(0x253000 + 30 * 816, FIRE_ORB_EARTH_FADE.to_bytes())

        return patch


class Therapy(CharacterSpell):
    _index: int = 6
    _fp: int = 2
    _power: int = 40
    _hit_rate: int = 100
    _title: str = "Therapy"
    _anim_ptr: int = 0x35C9F2
    _desc_ptr: int = 0x3A2C92

    _checkStats: bool = False
    _ignoreDefense: bool = True
    _checkOHKO: bool = False
    _overworldUsable: bool = True
    _spell_type: SpellType = SpellType.Heal
    _effect_type: EffectType = EffectType.Nullify
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = False
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = [
        SpellStatusEffects.Mute,
        SpellStatusEffects.Sleep,
        SpellStatusEffects.Poison,
        SpellStatusEffects.Fear,
        SpellStatusEffects.Berserk,
        SpellStatusEffects.Mushroom,
        SpellStatusEffects.Scarecrow,
    ]
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False
    _timing_modifiers: TimingProperties = ONE_TIMING_FOR_125_OR_15X_DMG
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 518


class GroupHug(CharacterSpell):
    _index: int = 7
    _fp: int = 4
    _power: int = 30
    _hit_rate: int = 100
    _title: str = "Group Hug"
    _anim_ptr: int = 0x35C9FC
    _desc_ptr: int = 0x3A2CA6

    _checkStats: bool = False
    _ignoreDefense: bool = True
    _checkOHKO: bool = False
    _overworldUsable: bool = True
    _spell_type: SpellType = SpellType.Heal
    _effect_type: EffectType = EffectType.Nullify
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = False
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = [
        SpellStatusEffects.Mute,
        SpellStatusEffects.Sleep,
        SpellStatusEffects.Poison,
        SpellStatusEffects.Fear,
        SpellStatusEffects.Berserk,
        SpellStatusEffects.Mushroom,
        SpellStatusEffects.Scarecrow,
    ]
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False
    _timing_modifiers: TimingProperties = ONE_TIMING_FOR_125_DMG_ONLY
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 519


class SleepyTime(CharacterSpell):
    _index: int = 8
    _fp: int = 4
    _hit_rate: int = 99
    _title: str = "Sleepy Time"
    _anim_ptr: int = 0x35CA00
    _desc_ptr: int = 0x3A2CBF

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType = EffectType.Inflict
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = [SpellStatusEffects.Sleep]
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = True
    _timing_modifiers: TimingProperties = ROTATE_1_TARGET_IF_TIMED_ALL
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 520


class ComeBack(CharacterSpell):
    _index: int = 9
    _fp: int = 2
    _hit_rate: int = 100
    _title: str = "Come Back"
    _anim_ptr: int = 0x35CA07
    _desc_ptr: int = 0x3A2CD6

    _checkStats: bool = False
    _ignoreDefense: bool = True
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Heal
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = False
    _targetParty: bool = False
    _targetWounded: bool = True
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction = InflictFunction.Revive
    _hideNum: bool = False
    _timing_modifiers: TimingProperties = TIMED_HEALS_ALL_HP_TO_FIRST_TARGET
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 521


class Mute(CharacterSpell):
    _index: int = 10
    _fp: int = 3
    _hit_rate: int = 99
    _title: str = "Mute"
    _anim_ptr: int = 0x35CA11
    _desc_ptr: int = 0x3A2CF4

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType = EffectType.Inflict
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = [SpellStatusEffects.Mute]
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = True
    _timing_modifiers: TimingProperties = ROTATE_1_TARGET_IF_TIMED_ALL
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 522


class PsychBomb(CharacterSpell):
    _index: int = 11
    _fp: int = 15
    _power: int = 60
    _hit_rate: int = 100
    _title: str = "Psych Bomb"
    _anim_ptr: int = 0x35CA1B
    _desc_ptr: int = 0x3A2D0C

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False
    _timing_modifiers: TimingProperties = BUTTON_MASH
    _damage_modifiers: DamageModifiers = X00625_MODIFIER

    _item_id: int = 523


class Terrorize(CharacterSpell):
    _index: int = 12
    _fp: int = 6
    _power: int = 10
    _hit_rate: int = 90
    _title: str = "Terrorize"
    _anim_ptr: int = 0x35CA22
    _desc_ptr: int = 0x3A2D26

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType = EffectType.Inflict
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = [SpellStatusEffects.Fear]
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False
    _timing_modifiers: TimingProperties = ROTATE_ONLY
    _damage_modifiers: DamageModifiers = X00625_MODIFIER

    _item_id: int = 524


class PoisonGas(CharacterSpell):
    _index: int = 13
    _fp: int = 10
    _power: int = 20
    _hit_rate: int = 90
    _title: str = "Poison Gas"
    _anim_ptr: int = 0x35CA2C
    _desc_ptr: int = 0x3A2D36

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType = EffectType.Inflict
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = [SpellStatusEffects.Poison]
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False
    _timing_modifiers: TimingProperties = ROTATE_ONLY
    _damage_modifiers: DamageModifiers = X00625_MODIFIER

    _item_id: int = 525


class Crusher(CharacterSpell):
    _index: int = 14
    _fp: int = 12
    _power: int = 60
    _hit_rate: int = 100
    _title: str = "Crusher"
    _anim_ptr: int = 0x35CA36
    _desc_ptr: int = 0x3A2D44

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False
    _timing_modifiers: TimingProperties = ONE_TIMING_FOR_125_OR_15X_DMG
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 526


class BowserCrush(CharacterSpell):
    _index: int = 15
    _fp: int = 16
    _power: int = 58
    _hit_rate: int = 100
    _title: str = "Bowser Crush"
    _anim_ptr: int = 0x35CA40
    _desc_ptr: int = 0x3A2D6D

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False
    _timing_modifiers: TimingProperties = BUTTON_MASH
    _damage_modifiers: DamageModifiers = X00625_MODIFIER

    _item_id: int = 527


class GenoBeam(CharacterSpell):
    _index: int = 16
    _fp: int = 3
    _power: int = 40
    _hit_rate: int = 100
    _title: str = "Geno Beam"
    _anim_ptr: int = 0x35CA47
    _desc_ptr: int = 0x3A2D87

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False
    _timing_modifiers: TimingProperties = CHARGE_ONLY
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 528


class GenoBoost(CharacterSpell):
    _index: int = 17
    _fp: int = 4
    _hit_rate: int = 100
    _title: str = "Geno Boost"
    _anim_ptr: int = 0x35CA4E
    _desc_ptr: int = 0x3A2DB0

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType = EffectType.Inflict
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = False
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = [SpellBoosts.MagicAttack, SpellBoosts.Attack]
    _inflict: InflictFunction
    _hideNum: bool = True
    _timing_modifiers: TimingProperties = TIMED_GIVES_TARGET_DEFENSE_UP_BUFF
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 529


class GenoWhirl(CharacterSpell):
    _index: int = 18
    _fp: int = 8
    _power: int = 45
    _hit_rate: int = 100
    _title: str = "Geno Whirl"
    _anim_ptr: int = 0x35CA58
    _desc_ptr: int = 0x3A2DD8

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False
    _timing_modifiers: TimingProperties = TIMED_FOR_9999_SET_ENEMY_HP_0
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 530


class GenoBlast(CharacterSpell):
    _index: int = 19
    _fp: int = 12
    _power: int = 50
    _hit_rate: int = 100
    _title: str = "Geno Blast"
    _anim_ptr: int = 0x35CA62
    _desc_ptr: int = 0x3A2E05

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False
    _timing_modifiers: TimingProperties = CHARGE_ONLY
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 531


class GenoFlash(CharacterSpell):
    _index: int = 20
    _fp: int = 16
    _power: int = 60
    _hit_rate: int = 100
    _title: str = "Geno Flash"
    _anim_ptr: int = 0x35CA69
    _desc_ptr: int = 0x3A2E26

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False
    _timing_modifiers: TimingProperties = CHARGE_ONLY
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 532


class Thunderbolt(CharacterSpell):
    _index: int = 21
    _fp: int = 2
    _power: int = 15
    _hit_rate: int = 100
    _title: str = "Thunderbolt"
    _anim_ptr: int = 0x35CA73
    _desc_ptr: int = 0x3A2E4A

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement = SpellElement.Thunder
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False
    _timing_modifiers: TimingProperties = ONE_TIMING_FOR_125_DMG_ONLY
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 533


class IceThunderbolt(Thunderbolt):
    _title: str = "Icebolt"
    _element: SpellElement = SpellElement.Ice

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()

        patch.add_data(0x33CB1F, THUNDERBOLT_ICE.to_bytes())

        return patch


class FireThunderbolt(Thunderbolt):
    _title: str = "Firebolt"
    _element: SpellElement = SpellElement.Fire

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()

        patch.add_data(0x33CB1F, THUNDERBOLT_FIRE.to_bytes())

        return patch


class EarthThunderbolt(Thunderbolt):
    _title: str = "Earthbolt"
    _element: SpellElement = SpellElement.Earth

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()

        patch.add_data(0x33CB1F, THUNDERBOLT_EARTH.to_bytes())

        return patch


class HPRain(CharacterSpell):
    _index: int = 22
    _fp: int = 2
    _power: int = 10
    _hit_rate: int = 100
    _title: str = "HP Rain"
    _anim_ptr: int = 0x35CA7D
    _desc_ptr: int = 0x3A2E6C

    _checkStats: bool = False
    _ignoreDefense: bool = True
    _checkOHKO: bool = False
    _overworldUsable: bool = True
    _spell_type: SpellType = SpellType.Heal
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = False
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False
    _timing_modifiers: TimingProperties = ONE_TIMING_FOR_125_OR_15X_DMG
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 534


class Psychopath(CharacterSpell):
    _index: int = 23
    _fp: int = 1
    _hit_rate: int = 100
    _title: str = "Psychopath"
    _anim_ptr: int = 0x35CA84
    _desc_ptr: int = 0x3A2E9E

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction = InflictFunction.Scan
    _hideNum: bool = True
    _timing_modifiers: TimingProperties = TIME_TO_ACTIVATE_HP_READ
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 535


class Shocker(CharacterSpell):
    _index: int = 24
    _fp: int = 8
    _power: int = 60
    _hit_rate: int = 100
    _title: str = "Shocker"
    _anim_ptr: int = 0x35CA8E
    _desc_ptr: int = 0x3A2EBC

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement = SpellElement.Thunder
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False
    _timing_modifiers: TimingProperties = ONE_TIMING_FOR_125_OR_15X_DMG
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 536


class IceShocker(Shocker):
    _title: str = "Ice Shocker"
    _element: SpellElement = SpellElement.Ice

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()
        patch.add_data(0x330BB8, SHOCKER_ICE.to_bytes())
        return patch


class FireShocker(Shocker):
    _title: str = "Fire Shocker"
    _element: SpellElement = SpellElement.Fire

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()
        patch.add_data(0x330BB8, SHOCKER_FIRE.to_bytes())
        return patch


class EarthShocker(Shocker):
    _title: str = "EarthShocker"
    _element: SpellElement = SpellElement.Fire

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()
        patch.add_data(0x330BB8, SHOCKER_EARTH.to_bytes())
        return patch


class Snowy(CharacterSpell):
    _index: int = 25
    _fp: int = 12
    _power: int = 40
    _hit_rate: int = 100
    _title: str = "Snowy"
    _anim_ptr: int = 0x35CA98
    _desc_ptr: int = 0x3A2EDE

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement = SpellElement.Ice
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False
    _timing_modifiers: TimingProperties = ROTATE_ONLY
    _damage_modifiers: DamageModifiers = X00625_MODIFIER

    _item_id: int = 537

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()
        if self.element == SpellElement.Thunder:
            patch.add_data(0x33C141, SNOWY_THUNDER_UPPER.to_bytes())
            patch.add_data(0x33C400, SNOWY_THUNDER_LOWER.to_bytes())
        elif self.element == SpellElement.Fire:
            patch.add_data(0x33C141, SNOWY_FIRE_UPPER.to_bytes())
            patch.add_data(0x33C400, SNOWY_FIRE_LOWER.to_bytes())
        elif self.element == SpellElement.Jump:
            patch.add_data(0x33C141, SNOWY_EARTH_UPPER.to_bytes())
            patch.add_data(0x33C400, SNOWY_EARTH_LOWER.to_bytes())
        return patch


class ThunderSnowy(Snowy):
    _title: str = "Thundery"
    _element: SpellElement = SpellElement.Thunder

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()
        patch.add_data(0x33C141, SNOWY_THUNDER_UPPER.to_bytes())
        patch.add_data(0x33C400, SNOWY_THUNDER_LOWER.to_bytes())
        return patch


class FireSnowy(Snowy):
    _title: str = "Firey"
    _element: SpellElement = SpellElement.Fire

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()
        patch.add_data(0x33C141, SNOWY_FIRE_UPPER.to_bytes())
        patch.add_data(0x33C400, SNOWY_FIRE_LOWER.to_bytes())
        return patch


class EarthSnowy(Snowy):
    _title: str = "Earthy"
    _element: SpellElement = SpellElement.Earth

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()
        patch.add_data(0x33C141, SNOWY_EARTH_UPPER.to_bytes())
        patch.add_data(0x33C400, SNOWY_EARTH_LOWER.to_bytes())
        return patch


class StarRain(CharacterSpell):
    _index: int = 26
    _fp: int = 14
    _power: int = 55
    _hit_rate: int = 100
    _title: str = "Star Rain"
    _anim_ptr: int = 0x35CAA2
    _desc_ptr: int = 0x3A2EF4

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False
    _timing_modifiers: TimingProperties = TIMED_JUMPS
    _damage_modifiers: DamageModifiers = X00625_MODIFIER

    _item_id: int = 538


class Clone1(CloneSpell):
    _index: int = 27


class Clone2(CloneSpell):
    _index: int = 28


class Clone3(CloneSpell):
    _index: int = 29


class Drain(EnemySpell):
    _index: int = 64
    _fp: int = 1
    _power: int = 4
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement = SpellElement.Fire
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class LightningOrb(EnemySpell):
    _index: int = 65
    _fp: int = 2
    _power: int = 8
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement = SpellElement.Thunder
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class Flame(EnemySpell):
    _index: int = 66
    _fp: int = 3
    _power: int = 12
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement = SpellElement.Fire
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class Bolt(EnemySpell):
    _index: int = 67
    _fp: int = 4
    _power: int = 20
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement = SpellElement.Thunder
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class Crystal(EnemySpell):
    _index: int = 68
    _fp: int = 5
    _power: int = 25
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement = SpellElement.Ice
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class FlameStone(EnemySpell):
    _index: int = 69
    _fp: int = 6
    _power: int = 32
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement = SpellElement.Fire
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class MegaDrain(EnemySpell):
    _index: int = 70
    _fp: int = 7
    _power: int = 40
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement = SpellElement.Fire
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class WillyWisp(EnemySpell):
    _index: int = 71
    _fp: int = 8
    _power: int = 48
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class DiamondSaw(EnemySpell):
    _index: int = 72
    _fp: int = 9
    _power: int = 60
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class Electroshock(EnemySpell):
    _index: int = 73
    _fp: int = 10
    _power: int = 72
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement = SpellElement.Thunder
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class Blast(EnemySpell):
    _index: int = 74
    _fp: int = 11
    _power: int = 89
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class Storm(EnemySpell):
    _index: int = 75
    _fp: int = 12
    _power: int = 108
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class IceRock(EnemySpell):
    _index: int = 76
    _fp: int = 13
    _power: int = 130
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement = SpellElement.Ice
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class Escape(EnemySpell):
    _index: int = 77
    _hit_rate: int = 100

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = False
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction = InflictFunction.NoDmg
    _hideNum: bool = False


class DarkStar(EnemySpell):
    _index: int = 78
    _fp: int = 20
    _power: int = 160
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = True
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class Recover(EnemySpell):
    _index: int = 79
    _fp: int = 3
    _power: int = 50
    _hit_rate: int = 100

    _checkStats: bool = False
    _ignoreDefense: bool = True
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Heal
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = False
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class MegaRecover(EnemySpell):
    _index: int = 80
    _fp: int = 9
    _power: int = 200
    _hit_rate: int = 100

    _checkStats: bool = False
    _ignoreDefense: bool = True
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Heal
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = False
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class FlameWall(EnemySpell):
    _index: int = 81
    _fp: int = 2
    _power: int = 8
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement = SpellElement.Fire
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class StaticE(EnemySpell):
    _index: int = 82
    _fp: int = 4
    _power: int = 12
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement = SpellElement.Thunder
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class SandStorm(EnemySpell):
    _index: int = 83
    _fp: int = 6
    _power: int = 16
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType = EffectType.Inflict
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = [SpellStatusEffects.Fear]
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class Blizzard(EnemySpell):
    _index: int = 84
    _fp: int = 8
    _power: int = 22
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement = SpellElement.Ice
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class DrainBeam(EnemySpell):
    _index: int = 85
    _fp: int = 10
    _power: int = 26
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class MeteorBlast(EnemySpell):
    _index: int = 86
    _fp: int = 12
    _power: int = 30
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class LightBeam(EnemySpell):
    _index: int = 87
    _fp: int = 13
    _power: int = 34
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType = EffectType.Inflict
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = [SpellStatusEffects.Sleep]
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class WaterBlast(EnemySpell):
    _index: int = 88
    _fp: int = 14
    _power: int = 39
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class Solidify(EnemySpell):
    _index: int = 89
    _fp: int = 15
    _power: int = 47
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement = SpellElement.Ice
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class PetalBlast(EnemySpell):
    _index: int = 90
    _fp: int = 16
    _power: int = 40
    _hit_rate: int = 85

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType = EffectType.Inflict
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = [SpellStatusEffects.Mushroom]
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class AuroraFlash(EnemySpell):
    _index: int = 91
    _fp: int = 17
    _power: int = 50
    _hit_rate: int = 85

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType = EffectType.Inflict
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = [SpellStatusEffects.Sleep]
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class Boulder(EnemySpell):
    _index: int = 92
    _fp: int = 18
    _power: int = 72
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class Corona(EnemySpell):
    _index: int = 93
    _fp: int = 19
    _power: int = 88
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement = SpellElement.Fire
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class MeteorSwarm(EnemySpell):
    _index: int = 94
    _fp: int = 20
    _power: int = 100
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class KnockOut(EnemySpell):
    _index: int = 95
    _fp: int = 15
    _power: int = 1
    _hit_rate: int = 60
    instant_ko = True

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = True
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = True
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class WeirdMushroom(EnemySpell):
    _index: int = 96
    _power: int = 30
    _hit_rate: int = 100

    _checkStats: bool = False
    _ignoreDefense: bool = True
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Heal
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = True
    _targetEnemies: bool = False
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class BreakerBeam(EnemySpell):
    _index: int = 97
    _fp: int = 15
    _power: int = 80
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class Shredder(EnemySpell):
    _index: int = 98
    _fp: int = 8
    _hit_rate: int = 100

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType = EffectType.Nullify
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = [
        SpellBoosts.MagicAttack,
        SpellBoosts.Attack,
        SpellBoosts.MagicDefense,
        SpellBoosts.Defense,
    ]
    _inflict: InflictFunction
    _hideNum: bool = True


class Sledge(EnemySpell):
    _index: int = 99
    _fp: int = 6
    _power: int = 50
    _hit_rate: int = 99

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class SwordRain(EnemySpell):
    _index: int = 100
    _fp: int = 8
    _power: int = 80
    _hit_rate: int = 99

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class SpearRain(EnemySpell):
    _index: int = 101
    _fp: int = 5
    _power: int = 60
    _hit_rate: int = 99

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class ArrowRain(EnemySpell):
    _index: int = 102
    _fp: int = 2
    _power: int = 40
    _hit_rate: int = 99

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class BigBang(EnemySpell):
    _index: int = 103
    _power: int = 100
    _hit_rate: int = 100

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class ChestScrow(EnemySpell):
    _index: int = 104
    _power: int = 10
    _hit_rate: int = 85

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType = EffectType.Inflict
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = [SpellStatusEffects.Scarecrow]
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class ChestFear(EnemySpell):
    _index: int = 105
    _power: int = 0
    _hit_rate: int = 82

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType = EffectType.Inflict
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = [SpellStatusEffects.Fear]
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = True


class ChestMute(EnemySpell):
    _index: int = 106
    _power: int = 0
    _hit_rate: int = 85

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType = EffectType.Inflict
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = [SpellStatusEffects.Mute]
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = True


class ChestPoison(EnemySpell):
    _index: int = 107
    _power: int = 0
    _hit_rate: int = 85

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType = EffectType.Inflict
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = [SpellStatusEffects.Poison]
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = True


class ChainSaw(EnemySpell):
    _index: int = 108
    _power: int = 50
    _hit_rate: int = 90

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _quad9s: bool = False
    _targetOthers: bool = False
    _targetEnemies: bool = True
    _targetParty: bool = True
    _targetWounded: bool = False
    _targetOneParty: bool = True
    _targetNotSelf: bool = False
    _element: SpellElement
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []
    _inflict: InflictFunction
    _hideNum: bool = False


class SpellDoNothing(EnemySpell):
    _index: int = 251
    _power: int = 0
    _hit_rate: int = 100


# ********************* Util functions to choose an elemental version of specific spells.


def _get_jump_spell(world) -> Type[Jump]:
    if world.settings.is_boolean_flag_enabled(CharacterSpellElements):
        return choice([Jump, FireJump, IceJump, ThunderJump])
    else:
        return Jump


def _get_fire_orb_spell(world) -> Type[FireOrb]:
    if world.settings.is_boolean_flag_enabled(CharacterSpellElements):
        return choice([FireOrb, IceOrb, ThunderOrb, EarthOrb])
    else:
        return FireOrb


def _get_super_jump_spell(world) -> Type[SuperJump]:
    if world.settings.is_boolean_flag_enabled(CharacterSpellElements):
        return choice([SuperJump, FireSuperJump, IceSuperJump, ThunderSuperJump])
    else:
        return SuperJump


def _get_super_flame_spell(world) -> Type[SuperFlame]:
    if world.settings.is_boolean_flag_enabled(CharacterSpellElements):
        return choice([SuperFlame, IceSuperFlame, ThunderSuperFlame, EarthSuperFlame])
    else:
        return SuperFlame


def _get_ultra_jump_spell(world) -> Type[UltraJump]:
    if world.settings.is_boolean_flag_enabled(CharacterSpellElements):
        return choice([UltraJump, FireUltraJump, IceUltraJump, ThunderUltraJump])
    else:
        return UltraJump


def _get_ultra_flame_spell(world) -> Type[UltraFlame]:
    if world.settings.is_boolean_flag_enabled(CharacterSpellElements):
        return choice([UltraFlame, IceUltraFlame, ThunderUltraFlame, EarthUltraFlame])
    else:
        return UltraFlame


def _get_thunderbolt_spell(world) -> Type[Thunderbolt]:
    if world.settings.is_boolean_flag_enabled(CharacterSpellElements):
        return choice([Thunderbolt, IceThunderbolt, FireThunderbolt, EarthThunderbolt])
    else:
        return Thunderbolt


def _get_shocker_spell(world) -> Type[Shocker]:
    if world.settings.is_boolean_flag_enabled(CharacterSpellElements):
        return choice([Shocker, IceShocker, FireShocker, EarthShocker])
    else:
        return Shocker


def _get_snowy_spell(world) -> Type[Snowy]:
    if world.settings.is_boolean_flag_enabled(CharacterSpellElements):
        return choice([Snowy, ThunderSnowy, FireSnowy, EarthSnowy])
    else:
        return Snowy


# ********************* Default lists for the world.


def get_default_spells(world):
    """Get default vanilla item list for the world.

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        list[Spell]: List of default spell objects.

    """
    return [
        _get_jump_spell(world)(world),
        _get_fire_orb_spell(world)(world),
        _get_super_jump_spell(world)(world),
        _get_super_flame_spell(world)(world),
        _get_ultra_jump_spell(world)(world),
        _get_ultra_flame_spell(world)(world),
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
        _get_thunderbolt_spell(world)(world),
        HPRain(world),
        Psychopath(world),
        _get_shocker_spell(world)(world),
        _get_snowy_spell(world)(world),
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
SingleTargets = [
    Drain,
    LightningOrb,
    Flame,
    Bolt,
    Crystal,
    FlameStone,
    MegaDrain,
    WillyWisp,
    DiamondSaw,
    Electroshock,
    Blast,
    Storm,
    IceRock,
    DarkStar,
]
Heals = [Recover, MegaRecover, WeirdMushroom]
MultiTargets = [
    FlameWall,
    StaticE,
    SandStorm,
    Blizzard,
    DrainBeam,
    MeteorBlast,
    LightBeam,
    WaterBlast,
    Solidify,
    PetalBlast,
    AuroraFlash,
    Boulder,
    Corona,
    MeteorSwarm,
    KnockOut,
    Shredder,
    Sledge,
    SwordRain,
    SpearRain,
    ArrowRain,
    ChestScrow,
    ChestFear,
    ChestMute,
    ChestPoison,
    ChainSaw,
]
DoNothing = [SpellDoNothing]
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
    SpellDoNothing.index: DoNothing,
    Escape.index: Run,
}
