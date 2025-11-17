from smrpgpatchbuilder.datatypes.spells.classes import CharacterSpell, EnemySpell, SpellCollection
from smrpgpatchbuilder.datatypes.spells.enums import SpellType, EffectType, Element, Status, InflictFunction, TempStatBuff
from smrpgpatchbuilder.datatypes.items.enums import ItemPrefix
from smrpgpatchbuilder.datatypes.spells.arguments.types.classes import TimingProperties, DamageModifiers
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import BUTTON_MASH, CHARGE_ONLY, MULTIPLE_BUTTON_PRESSES, ONE_PLUS_MORE_TARGETS_WITH_PRESSES, ONE_TIMING_FOR_125_DMG_ONLY, ONE_TIMING_FOR_125_OR_15X_DMG, ROTATE_1_TARGET_IF_TIMED_ALL, ROTATE_ONLY, TIMED_FOR_9999_SET_ENEMY_HP_0, TIMED_GIVES_TARGET_DEFENSE_UP_BUFF, TIMED_HEALS_ALL_HP_TO_FIRST_TARGET, TIMED_JUMPS, TIME_TO_ACTIVATE_HP_READ
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import NO_MODIFIERS, X00625_MODIFIER, X00625_MODIFIER_WITH_MULTI_TARGETING, X0125_MODIFIER_WITH_MULTI_TARGETING, X05_MODIFIER


class JumpSpell(CharacterSpell):
    _index = 0
    _title = 'Jump'
    _prefix = ItemPrefix.STAR
    _fp = 3
    _power = 25
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.JUMP
    _inflict = InflictFunction.INC_JUMP
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = ONE_TIMING_FOR_125_OR_15X_DMG
    _damage_modifiers = NO_MODIFIERS
    _description = ''


class FireOrbSpell(CharacterSpell):
    _index = 1
    _title = 'Fire Orb'
    _prefix = ItemPrefix.STAR
    _fp = 5
    _power = 20
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.FIRE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = MULTIPLE_BUTTON_PRESSES
    _damage_modifiers = X00625_MODIFIER
    _description = ' Fire orb!\n Push "Y"\n repeatedly!'


class SuperJumpSpell(CharacterSpell):
    _index = 2
    _title = 'Super Jump'
    _prefix = ItemPrefix.STAR
    _fp = 7
    _power = 45
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.JUMP
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = MULTIPLE_BUTTON_PRESSES
    _damage_modifiers = X05_MODIFIER
    _description = ' Push "Y"\n prior to hit\n for DAMAGE!'


class SuperFlameSpell(CharacterSpell):
    _index = 3
    _title = 'Super Flame'
    _prefix = ItemPrefix.STAR
    _fp = 9
    _power = 40
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.FIRE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = MULTIPLE_BUTTON_PRESSES
    _damage_modifiers = X00625_MODIFIER
    _description = ' Fire blast!\n Push "Y"\n repeatedly!'


class UltraJumpSpell(CharacterSpell):
    _index = 4
    _title = 'Ultra Jump'
    _prefix = ItemPrefix.STAR
    _fp = 11
    _power = 65
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.JUMP
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = ONE_PLUS_MORE_TARGETS_WITH_PRESSES
    _damage_modifiers = X0125_MODIFIER_WITH_MULTI_TARGETING
    _description = ' Push "Y"\n prior to hit\n for DAMAGE!'


class UltraFlameSpell(CharacterSpell):
    _index = 5
    _title = 'Ultra Flame'
    _prefix = ItemPrefix.STAR
    _fp = 14
    _power = 60
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.FIRE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = ONE_PLUS_MORE_TARGETS_WITH_PRESSES
    _damage_modifiers = X00625_MODIFIER_WITH_MULTI_TARGETING
    _description = ' Fire orbs!\n Push "Y"\n repeatedly!'


class TherapySpell(CharacterSpell):
    _index = 6
    _title = 'Therapy'
    _prefix = ItemPrefix.STAR
    _fp = 2
    _power = 40
    _hit_rate = 100
    _spell_type = SpellType.HEAL
    _effect_type = EffectType.NULLIFY
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = True
    _check_ohko = False
    _usable_outside_of_battle = True
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR, Status.BERSERK, Status.MUSHROOM, Status.SCARECROW]
    _timing_modifiers = ONE_TIMING_FOR_125_OR_15X_DMG
    _damage_modifiers = NO_MODIFIERS
    _description = ' Heal\n HP & status$'


class GroupHugSpell(CharacterSpell):
    _index = 7
    _title = 'Group Hug'
    _prefix = ItemPrefix.STAR
    _fp = 4
    _power = 30
    _hit_rate = 100
    _spell_type = SpellType.HEAL
    _effect_type = EffectType.NULLIFY
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = True
    _check_ohko = False
    _usable_outside_of_battle = True
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR, Status.BERSERK, Status.MUSHROOM, Status.SCARECROW]
    _timing_modifiers = ONE_TIMING_FOR_125_DMG_ONLY
    _damage_modifiers = NO_MODIFIERS
    _description = ' Heal group!\n HP/status$'


class SleepyTimeSpell(CharacterSpell):
    _index = 8
    _title = 'Sleepy Time'
    _prefix = ItemPrefix.STAR
    _fp = 4
    _power = 0
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = True
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.SLEEP]
    _timing_modifiers = ROTATE_1_TARGET_IF_TIMED_ALL
    _damage_modifiers = NO_MODIFIERS
    _description = ' Zonk 1 or\n more foes!'


class ComeBackSpell(CharacterSpell):
    _index = 9
    _title = 'Come Back'
    _prefix = ItemPrefix.STAR
    _fp = 2
    _power = 0
    _hit_rate = 100
    _spell_type = SpellType.HEAL
    _element = Element.NONE
    _inflict = InflictFunction.REVIVE
    _check_stats = False
    _ignore_defense = True
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = False
    _target_party = False
    _target_wounded = True
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = TIMED_HEALS_ALL_HP_TO_FIRST_TARGET
    _damage_modifiers = NO_MODIFIERS
    _description = ' Revive one...\n or more pals!'


class MuteSpell(CharacterSpell):
    _index = 10
    _title = 'Mute'
    _prefix = ItemPrefix.STAR
    _fp = 3
    _power = 0
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = True
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.MUTE]
    _timing_modifiers = ROTATE_1_TARGET_IF_TIMED_ALL
    _damage_modifiers = NO_MODIFIERS
    _description = ' Halt magic\n attack(s)!'


class PsychBombSpell(CharacterSpell):
    _index = 11
    _title = 'Psych Bomb'
    _prefix = ItemPrefix.STAR
    _fp = 15
    _power = 60
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = BUTTON_MASH
    _damage_modifiers = X00625_MODIFIER
    _description = ' Make me mad\n and...BOOM!'


class TerrorizeSpell(CharacterSpell):
    _index = 12
    _title = 'Terrorize'
    _prefix = ItemPrefix.STAR
    _fp = 6
    _power = 10
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.FEAR]
    _timing_modifiers = ROTATE_ONLY
    _damage_modifiers = X00625_MODIFIER
    _description = "Scare 'em good!"


class PoisonGasSpell(CharacterSpell):
    _index = 13
    _title = 'Poison Gas'
    _prefix = ItemPrefix.STAR
    _fp = 10
    _power = 20
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.POISON]
    _timing_modifiers = ROTATE_ONLY
    _damage_modifiers = X00625_MODIFIER
    _description = ' Poison foes!'


class CrusherSpell(CharacterSpell):
    _index = 14
    _title = 'Crusher'
    _prefix = ItemPrefix.STAR
    _fp = 12
    _power = 60
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = ONE_TIMING_FOR_125_OR_15X_DMG
    _damage_modifiers = NO_MODIFIERS
    _description = ' Rock slide!\n Hit "Y" prior\n to contact!'


class BowserCrushSpell(CharacterSpell):
    _index = 15
    _title = 'Bowser Crush'
    _prefix = ItemPrefix.STAR
    _fp = 16
    _power = 58
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = BUTTON_MASH
    _damage_modifiers = X00625_MODIFIER
    _description = "Bowser's\nultimate weapon!"


class GenoBeamSpell(CharacterSpell):
    _index = 16
    _title = 'Geno Beam'
    _prefix = ItemPrefix.STAR
    _fp = 3
    _power = 40
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = CHARGE_ONLY
    _damage_modifiers = NO_MODIFIERS
    _description = ' Hold "Y" until\n just before\n discharge!'


class GenoBoostSpell(CharacterSpell):
    _index = 17
    _title = 'Geno Boost'
    _prefix = ItemPrefix.STAR
    _fp = 4
    _power = 0
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = True
    _target_others = True
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _boosts = [TempStatBuff(3), TempStatBuff(4)]
    _timing_modifiers = TIMED_GIVES_TARGET_DEFENSE_UP_BUFF
    _damage_modifiers = NO_MODIFIERS
    _description = ' Attack up!\n Push "Y" just\n before end!'


class GenoWhirlSpell(CharacterSpell):
    _index = 18
    _title = 'Geno Whirl'
    _prefix = ItemPrefix.STAR
    _fp = 8
    _power = 45
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = TIMED_FOR_9999_SET_ENEMY_HP_0
    _damage_modifiers = NO_MODIFIERS
    _description = 'Press "Y" prior\nto contact for\ncritical hit!'


class GenoBlastSpell(CharacterSpell):
    _index = 19
    _title = 'Geno Blast'
    _prefix = ItemPrefix.STAR
    _fp = 12
    _power = 50
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = CHARGE_ONLY
    _damage_modifiers = NO_MODIFIERS
    _description = ' Beam hits\n all foes!\n Energize!'


class GenoFlashSpell(CharacterSpell):
    _index = 20
    _title = 'Geno Flash'
    _prefix = ItemPrefix.STAR
    _fp = 16
    _power = 60
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = CHARGE_ONLY
    _damage_modifiers = NO_MODIFIERS
    _description = ' Build power!\n Beam hits\n all foes!'


class ThunderboltSpell(CharacterSpell):
    _index = 21
    _title = 'Thunderbolt'
    _prefix = ItemPrefix.STAR
    _fp = 2
    _power = 15
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.THUNDER
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = ONE_TIMING_FOR_125_DMG_ONLY
    _damage_modifiers = NO_MODIFIERS
    _description = ' Hit "Y" just\n before bolt\n ends!'


class HPRainSpell(CharacterSpell):
    _index = 22
    _title = 'HP Rain'
    _prefix = ItemPrefix.STAR
    _fp = 2
    _power = 10
    _hit_rate = 100
    _spell_type = SpellType.HEAL
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = True
    _check_ohko = False
    _usable_outside_of_battle = True
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = ONE_TIMING_FOR_125_OR_15X_DMG
    _damage_modifiers = NO_MODIFIERS
    _description = ' HP renewal!\n Hit "Y" just\n before shower\n ends! '


class PsychopathSpell(CharacterSpell):
    _index = 23
    _title = 'Psychopath'
    _prefix = ItemPrefix.STAR
    _fp = 1
    _power = 0
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _inflict = InflictFunction.SCAN
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = True
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = TIME_TO_ACTIVATE_HP_READ
    _damage_modifiers = NO_MODIFIERS
    _description = " See foe's HP\n and...secrets!"


class ShockerSpell(CharacterSpell):
    _index = 24
    _title = 'Shocker'
    _prefix = ItemPrefix.STAR
    _fp = 8
    _power = 60
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.THUNDER
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = ONE_TIMING_FOR_125_OR_15X_DMG
    _damage_modifiers = NO_MODIFIERS
    _description = ' Hit "Y" just\n before bolt\n ends!'


class SnowySpell(CharacterSpell):
    _index = 25
    _title = 'Snowy'
    _prefix = ItemPrefix.STAR
    _fp = 12
    _power = 40
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.ICE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = ROTATE_ONLY
    _damage_modifiers = X00625_MODIFIER
    _description = ' Snowman\n fells foes!'


class StarRainSpell(CharacterSpell):
    _index = 26
    _title = 'Star Rain'
    _prefix = ItemPrefix.STAR
    _fp = 14
    _power = 55
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = TIMED_JUMPS
    _damage_modifiers = X00625_MODIFIER
    _description = ' Star showers!\n Hit "Y" just\n upon contact!'


class DummySpell1(EnemySpell):
    _index = 27
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell2(EnemySpell):
    _index = 28
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 0
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.NULLIFY
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = True
    _target_others = False
    _target_enemies = False
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.INVINCIBLE]
    _boosts = [TempStatBuff(3), TempStatBuff(4), TempStatBuff(5), TempStatBuff(6)]


class DummySpell3(EnemySpell):
    _index = 29
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell4(EnemySpell):
    _index = 30
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell5(EnemySpell):
    _index = 31
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell6(EnemySpell):
    _index = 32
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell7(EnemySpell):
    _index = 33
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 15
    _power = 60
    _hit_rate = 80
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell8(EnemySpell):
    _index = 34
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell9(EnemySpell):
    _index = 35
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell10(EnemySpell):
    _index = 36
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell11(EnemySpell):
    _index = 37
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell12(EnemySpell):
    _index = 38
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell13(EnemySpell):
    _index = 39
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell14(EnemySpell):
    _index = 40
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell15(EnemySpell):
    _index = 41
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell16(EnemySpell):
    _index = 42
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell17(EnemySpell):
    _index = 43
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell18(EnemySpell):
    _index = 44
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell19(EnemySpell):
    _index = 45
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell20(EnemySpell):
    _index = 46
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell21(EnemySpell):
    _index = 47
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell22(EnemySpell):
    _index = 48
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell23(EnemySpell):
    _index = 49
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell24(EnemySpell):
    _index = 50
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell25(EnemySpell):
    _index = 51
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell26(EnemySpell):
    _index = 52
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell27(EnemySpell):
    _index = 53
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell28(EnemySpell):
    _index = 54
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell29(EnemySpell):
    _index = 55
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell30(EnemySpell):
    _index = 56
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell31(EnemySpell):
    _index = 57
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell32(EnemySpell):
    _index = 58
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell33(EnemySpell):
    _index = 59
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell34(EnemySpell):
    _index = 60
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell35(EnemySpell):
    _index = 61
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell36(EnemySpell):
    _index = 62
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DummySpell37(EnemySpell):
    _index = 63
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 0
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = False
    _target_not_self = False


class DrainSpell(EnemySpell):
    _index = 64
    _title = ' Drain'
    _fp = 1
    _power = 4
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.FIRE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class LightningOrbSpell(EnemySpell):
    _index = 65
    _title = ' Lightning Orb'
    _fp = 2
    _power = 8
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.THUNDER
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class FlameSpell(EnemySpell):
    _index = 66
    _title = ' Flame'
    _fp = 3
    _power = 12
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.FIRE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class BoltSpell(EnemySpell):
    _index = 67
    _title = ' Bolt'
    _fp = 4
    _power = 20
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.THUNDER
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class CrystalSpell(EnemySpell):
    _index = 68
    _title = ' Crystal'
    _fp = 5
    _power = 25
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.ICE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class FlameStoneSpell(EnemySpell):
    _index = 69
    _title = ' Flame Stone'
    _fp = 6
    _power = 32
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.FIRE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class MegaDrainSpell(EnemySpell):
    _index = 70
    _title = ' Mega Drain'
    _fp = 7
    _power = 40
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.FIRE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class WillyWispSpell(EnemySpell):
    _index = 71
    _title = ' Willy Wisp'
    _fp = 8
    _power = 48
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DiamondSawSpell(EnemySpell):
    _index = 72
    _title = ' Diamond Saw'
    _fp = 9
    _power = 60
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class ElectroshockSpell(EnemySpell):
    _index = 73
    _title = ' Electroshock'
    _fp = 10
    _power = 72
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.THUNDER
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class BlastSpell(EnemySpell):
    _index = 74
    _title = ' Blast'
    _fp = 11
    _power = 89
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class StormSpell(EnemySpell):
    _index = 75
    _title = ' Storm'
    _fp = 12
    _power = 108
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class IceRockSpell(EnemySpell):
    _index = 76
    _title = ' Ice Rock'
    _fp = 13
    _power = 130
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.ICE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class EscapeSpell(EnemySpell):
    _index = 77
    _title = ' Escape'
    _fp = 0
    _power = 0
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _inflict = InflictFunction.NO_DMG
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DarkStarSpell(EnemySpell):
    _index = 78
    _title = ' Dark Star'
    _fp = 20
    _power = 160
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class RecoverSpell(EnemySpell):
    _index = 79
    _title = ' Recover'
    _fp = 3
    _power = 50
    _hit_rate = 100
    _spell_type = SpellType.HEAL
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = True
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class MegaRecoverSpell(EnemySpell):
    _index = 80
    _title = ' Mega Recover'
    _fp = 9
    _power = 200
    _hit_rate = 100
    _spell_type = SpellType.HEAL
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = True
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class FlameWallSpell(EnemySpell):
    _index = 81
    _title = ' Flame Wall'
    _fp = 2
    _power = 8
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.FIRE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class StaticESpell(EnemySpell):
    _index = 82
    _title = ' Static E!'
    _fp = 4
    _power = 12
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.THUNDER
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class SandStormSpell(EnemySpell):
    _index = 83
    _title = ' Sand Storm'
    _fp = 6
    _power = 16
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.FEAR]


class BlizzardSpell(EnemySpell):
    _index = 84
    _title = ' Blizzard'
    _fp = 8
    _power = 22
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.ICE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DrainBeamSpell(EnemySpell):
    _index = 85
    _title = ' Drain Beam'
    _fp = 10
    _power = 26
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class MeteorBlastSpell(EnemySpell):
    _index = 86
    _title = ' Meteor Blast'
    _fp = 12
    _power = 30
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class LightBeamSpell(EnemySpell):
    _index = 87
    _title = ' Light Beam'
    _fp = 13
    _power = 34
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.SLEEP]


class WaterBlastSpell(EnemySpell):
    _index = 88
    _title = ' Water Blast'
    _fp = 14
    _power = 39
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class SolidifySpell(EnemySpell):
    _index = 89
    _title = ' Solidify'
    _fp = 15
    _power = 47
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.ICE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class PetalBlastSpell(EnemySpell):
    _index = 90
    _title = ' Petal Blast'
    _fp = 16
    _power = 40
    _hit_rate = 85
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.MUSHROOM]


class AuroraFlashSpell(EnemySpell):
    _index = 91
    _title = ' Aurora Flash'
    _fp = 17
    _power = 50
    _hit_rate = 85
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.SLEEP]


class BoulderSpell(EnemySpell):
    _index = 92
    _title = ' Boulder'
    _fp = 18
    _power = 72
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class CoronaSpell(EnemySpell):
    _index = 93
    _title = ' Corona'
    _fp = 19
    _power = 88
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.FIRE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class MeteorSwarmSpell(EnemySpell):
    _index = 94
    _title = ' Meteor Swarm'
    _fp = 20
    _power = 100
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class KnockOutSpell(EnemySpell):
    _index = 95
    _title = ' Knock Out'
    _fp = 15
    _power = 1
    _hit_rate = 60
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = True
    _usable_outside_of_battle = False
    _quad9s = True
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class WeirdMushroomSpell(EnemySpell):
    _index = 96
    _title = ' Weird Mushroom'
    _fp = 0
    _power = 30
    _hit_rate = 100
    _spell_type = SpellType.HEAL
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = True
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class BreakerBeamSpell(EnemySpell):
    _index = 97
    _title = ' Breaker Beam'
    _fp = 15
    _power = 80
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class ShredderSpell(EnemySpell):
    _index = 98
    _title = ' Shredder'
    _fp = 8
    _power = 0
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.NULLIFY
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = True
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _boosts = [TempStatBuff(3), TempStatBuff(4), TempStatBuff(5), TempStatBuff(6)]


class SledgeSpell(EnemySpell):
    _index = 99
    _title = ' Sledge'
    _fp = 6
    _power = 50
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class SwordRainSpell(EnemySpell):
    _index = 100
    _title = ' Sword Rain'
    _fp = 8
    _power = 80
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class SpearRainSpell(EnemySpell):
    _index = 101
    _title = ' Spear Rain'
    _fp = 5
    _power = 60
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class ArrowRainSpell(EnemySpell):
    _index = 102
    _title = ' Arrow Rain'
    _fp = 2
    _power = 40
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class BigBangSpell(EnemySpell):
    _index = 103
    _title = ' Big Bang'
    _fp = 0
    _power = 100
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell38(EnemySpell):
    _index = 104
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 10
    _hit_rate = 85
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.SCARECROW]


class DummySpell39(EnemySpell):
    _index = 105
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 82
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = True
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.FEAR]


class DummySpell40(EnemySpell):
    _index = 106
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 85
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = True
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.MUTE]


class DummySpell41(EnemySpell):
    _index = 107
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 0
    _power = 0
    _hit_rate = 85
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = True
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.POISON]


class ChainSawSpell(EnemySpell):
    _index = 108
    _title = ' Chain Saw'
    _fp = 0
    _power = 50
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell42(EnemySpell):
    _index = 109
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell43(EnemySpell):
    _index = 110
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell44(EnemySpell):
    _index = 111
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell45(EnemySpell):
    _index = 112
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell46(EnemySpell):
    _index = 113
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell47(EnemySpell):
    _index = 114
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell48(EnemySpell):
    _index = 115
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell49(EnemySpell):
    _index = 116
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell50(EnemySpell):
    _index = 117
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell51(EnemySpell):
    _index = 118
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell52(EnemySpell):
    _index = 119
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell53(EnemySpell):
    _index = 120
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell54(EnemySpell):
    _index = 121
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell55(EnemySpell):
    _index = 122
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell56(EnemySpell):
    _index = 123
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell57(EnemySpell):
    _index = 124
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell58(EnemySpell):
    _index = 125
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell59(EnemySpell):
    _index = 126
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


class DummySpell60(EnemySpell):
    _index = 127
    _title = 'Dummy'
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


ALL_SPELLS = SpellCollection([
    JumpSpell(),
    FireOrbSpell(),
    SuperJumpSpell(),
    SuperFlameSpell(),
    UltraJumpSpell(),
    UltraFlameSpell(),
    TherapySpell(),
    GroupHugSpell(),
    SleepyTimeSpell(),
    ComeBackSpell(),
    MuteSpell(),
    PsychBombSpell(),
    TerrorizeSpell(),
    PoisonGasSpell(),
    CrusherSpell(),
    BowserCrushSpell(),
    GenoBeamSpell(),
    GenoBoostSpell(),
    GenoWhirlSpell(),
    GenoBlastSpell(),
    GenoFlashSpell(),
    ThunderboltSpell(),
    HPRainSpell(),
    PsychopathSpell(),
    ShockerSpell(),
    SnowySpell(),
    StarRainSpell(),
    DummySpell1(),
    DummySpell2(),
    DummySpell3(),
    DummySpell4(),
    DummySpell5(),
    DummySpell6(),
    DummySpell7(),
    DummySpell8(),
    DummySpell9(),
    DummySpell10(),
    DummySpell11(),
    DummySpell12(),
    DummySpell13(),
    DummySpell14(),
    DummySpell15(),
    DummySpell16(),
    DummySpell17(),
    DummySpell18(),
    DummySpell19(),
    DummySpell20(),
    DummySpell21(),
    DummySpell22(),
    DummySpell23(),
    DummySpell24(),
    DummySpell25(),
    DummySpell26(),
    DummySpell27(),
    DummySpell28(),
    DummySpell29(),
    DummySpell30(),
    DummySpell31(),
    DummySpell32(),
    DummySpell33(),
    DummySpell34(),
    DummySpell35(),
    DummySpell36(),
    DummySpell37(),
    DrainSpell(),
    LightningOrbSpell(),
    FlameSpell(),
    BoltSpell(),
    CrystalSpell(),
    FlameStoneSpell(),
    MegaDrainSpell(),
    WillyWispSpell(),
    DiamondSawSpell(),
    ElectroshockSpell(),
    BlastSpell(),
    StormSpell(),
    IceRockSpell(),
    EscapeSpell(),
    DarkStarSpell(),
    RecoverSpell(),
    MegaRecoverSpell(),
    FlameWallSpell(),
    StaticESpell(),
    SandStormSpell(),
    BlizzardSpell(),
    DrainBeamSpell(),
    MeteorBlastSpell(),
    LightBeamSpell(),
    WaterBlastSpell(),
    SolidifySpell(),
    PetalBlastSpell(),
    AuroraFlashSpell(),
    BoulderSpell(),
    CoronaSpell(),
    MeteorSwarmSpell(),
    KnockOutSpell(),
    WeirdMushroomSpell(),
    BreakerBeamSpell(),
    ShredderSpell(),
    SledgeSpell(),
    SwordRainSpell(),
    SpearRainSpell(),
    ArrowRainSpell(),
    BigBangSpell(),
    DummySpell38(),
    DummySpell39(),
    DummySpell40(),
    DummySpell41(),
    ChainSawSpell(),
    DummySpell42(),
    DummySpell43(),
    DummySpell44(),
    DummySpell45(),
    DummySpell46(),
    DummySpell47(),
    DummySpell48(),
    DummySpell49(),
    DummySpell50(),
    DummySpell51(),
    DummySpell52(),
    DummySpell53(),
    DummySpell54(),
    DummySpell55(),
    DummySpell56(),
    DummySpell57(),
    DummySpell58(),
    DummySpell59(),
    DummySpell60(),
])
