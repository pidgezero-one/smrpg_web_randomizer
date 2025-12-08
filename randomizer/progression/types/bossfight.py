from smrpgpatchbuilder.datatypes.enemies.classes import (
    Enemy)
from smrpgpatchbuilder.datatypes.monster_scripts import MonsterScript
from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite

class CROOKDouble(Enemy):
    """Crook henchman class to not interfere with overworld enemy in Rose Way encounters, etc"""
    _name: str = "CROOK"

    _hp: int = 38
    _fp: int = 100
    _attack: int = 35
    _defense: int = 32
    _magic_attack: int = 12
    _magic_defense: int = 25
    _speed: int = 22
    _evade: int = 40
    _magic_evade: int = 40
    _xp: int = 10
    _coins: int = 10
    _yoshi_cookie_item = MidMushroomItem
    _rare_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = "[await]"


class APPRENTICEEnemyDouble(Enemy):
    """APPRENTICE henchman class to not interfere with overworld enemy in Booster Pass, etc"""
    _name: str = "APPRENTICE"

    _hp: int = 120
    _fp: int = 32
    _attack: int = 50
    _defense: int = 50
    _magic_attack: int = 20
    _magic_defense: int = 20
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 1
    _coins: int = 4
    _yoshi_cookie_item = SleepyBombItem
    _common_item_drop = MidMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.PUNCH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = "[await]"


class BANDANAREDEnemyDouble(Enemy):
    """BANDANA RED henchman class to not interfere with overworld enemy in sunken ship scheduled fights, etc"""
    _name: str = "BANDANA RED"

    _hp: int = 120
    _fp: int = 100
    _attack: int = 78
    _defense: int = 60
    _magic_attack: int = 25
    _magic_defense: int = 25
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER, Element.FIRE]
    _xp: int = 18
    _coins: int = 10
    _yoshi_cookie_item = EnergizerItem
    _rare_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 30
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = "[await]"


class PIRANHAPLANTEnemyDouble(Enemy):
    """PIRANHA PLANT henchman class to not interfere with overworld enemy in pipe vault, etc"""
    _name: str = "PIRANHA PLANT"

    _hp: int = 168
    _fp: int = 4
    _attack: int = 45
    _defense: int = 14
    _magic_attack: int = 20
    _magic_defense: int = 22
    _speed: int = 6
    _evade: int = 0
    _magic_evade: int = 0
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 5
    _coins: int = 5
    _yoshi_cookie_item = SleepyBombItem
    _common_item_drop = MapleSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = "[await]"


class BLUEBIRDEnemyDouble(Enemy):
    """BLUEBIRD henchman class to not interfere with overworld enemy in nimbus castle, etc"""
    _name: str = "BLUEBIRD"

    _hp: int = 200
    _fp: int = 100
    _attack: int = 95
    _defense: int = 50
    _magic_attack: int = 80
    _magic_defense: int = 94
    _speed: int = 29
    _evade: int = 8
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.ICE]
    _xp: int = 14
    _coins: int = 6
    _yoshi_cookie_item = BracerItem
    _common_item_drop = BracerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_RIGHT
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " ••••••[await]"


class BIRDYEnemyDouble(Enemy):
    """BIRDY henchman class to not interfere with overworld enemy in nimbus castle, etc"""
    _name: str = "BIRDY"

    _hp: int = 150
    _fp: int = 100
    _attack: int = 110
    _defense: int = 75
    _magic_attack: int = 55
    _magic_defense: int = 13
    _speed: int = 23
    _evade: int = 18
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 16
    _coins: int = 3
    _yoshi_cookie_item = EnergizerItem
    _common_item_drop = EnergizerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_RIGHT
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = "[await]"



class BLOOBEREnemyDouble(Enemy):
    """BLOOBER enemy class to not interfere with overworld enemy in ship, etc"""
    _name: str = "BLOOBER"

    _hp: int = 130
    _fp: int = 100
    _attack: int = 80
    _defense: int = 36
    _magic_attack: int = 21
    _magic_defense: int = 16
    _speed: int = 23
    _evade: int = 20
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER, Element.FIRE]
    _xp: int = 12
    _coins: int = 0
    _yoshi_cookie_item = ElixirItem
    _rare_item_drop = HoneySyrupItem
    _common_item_drop = MaxMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 100
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PUNCH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.HOVER_IN
    _elevate: int = 2
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = "[await]"




class MACHINEMADEAxemBlackDouble(Enemy):
    """MACHINE MADE enemy class to not interfere with overworld enemy in factory, etc"""
    _name: str = "MACHINE MADE"

    _hp: int = 120
    _fp: int = 100
    _attack: int = 120
    _defense: int = 110
    _magic_attack: int = 4
    _magic_defense: int = 40
    _speed: int = 55
    _evade: int = 30
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.FEAR]
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 20
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = MaxMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 30
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = "[await]"


class MACHINEMADEAxemPinkDouble(Enemy):
    """MACHINE MADE enemy class to not interfere with overworld enemy in factory, etc"""
    _name: str = "MACHINE MADE"

    _hp: int = 100
    _fp: int = 200
    _attack: int = 95
    _defense: int = 90
    _magic_attack: int = 40
    _magic_defense: int = 100
    _speed: int = 35
    _evade: int = 25
    _magic_evade: int = 10
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP]
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.ICE]
    _xp: int = 30
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = MapleSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = "[await]"


class AEROEnemy(Enemy):
    """AERO enemy class"""
    # 175
    _name: str = "AERO"

    _hp: int = 10
    _fp: int = 100
    _attack: int = 0
    _defense: int = 0
    _magic_attack: int = 0
    _magic_defense: int = 0
    _speed: int = 0
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 4
    _psychopath_message: str = "[await]"


class PYROSPHEREEnemyDouble(Enemy):
    """PYROSPHERE enemy class to not interfere with overworld enemy in volcano, etc"""
    _name: str = "PYROSPHERE"

    _hp: int = 167
    _fp: int = 100
    _attack: int = 105
    _defense: int = 66
    _magic_attack: int = 100
    _magic_defense: int = 48
    _speed: int = 24
    _evade: int = 7
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.POISON]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 17
    _coins: int = 2
    _yoshi_cookie_item = FireBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 40
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = "[await]"


class SHYGUYEnemyDouble(Enemy):
    """SHY GUY enemy class to not interfere with overworld enemy in rose way, etc"""
    _name: str = "SHY GUY"

    _hp: int = 78
    _fp: int = 100
    _attack: int = 29
    _defense: int = 30
    _magic_attack: int = 20
    _magic_defense: int = 6
    _speed: int = 14
    _evade: int = 10
    _magic_evade: int = 0
    _xp: int = 2
    _coins: int = 1
    _yoshi_cookie_item = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = "[await]"


class MACHINEMADEAxemRedDouble(Enemy):
    """MACHINE MADE enemy class to not interfere with overworld enemy in factory, etc"""
    _name: str = "MACHINE MADE"

    _hp: int = 180
    _fp: int = 100
    _attack: int = 135
    _defense: int = 95
    _magic_attack: int = 24
    _magic_defense: int = 80
    _speed: int = 45
    _evade: int = 10
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 50
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = RoyalSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = "[await]"


class MACHINEMADEBodyguardEnemyDouble(Enemy):
    """MACHINE MADE enemy class to not interfere with overworld enemy in factory, etc"""
    _name: str = "MACHINE MADE"

    _hp: int = 100
    _fp: int = 250
    _attack: int = 135
    _defense: int = 95
    _magic_attack: int = 90
    _magic_defense: int = 65
    _speed: int = 36
    _evade: int = 10
    _magic_evade: int = 0
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = "[await]"




# unused? make sure whichever one we replace is not used in formations
class AEROEnemy2(Enemy):
    """AERO enemy class"""
    _monster_id: int = 231
    _name: str = "AERO"

    _hp: int = 10
    _fp: int = 100
    _attack: int = 0
    _defense: int = 0
    _magic_attack: int = 0
    _magic_defense: int = 0
    _speed: int = 0
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 4
    _psychopath_message: str = "[await]"


class MACHINEMADEAxemGreenDouble(Enemy):
    """MACHINE MADE enemy class to not interfere with overworld enemy in factory, etc"""
    _name: str = "MACHINE MADE"

    _hp: int = 80
    _fp: int = 250
    _attack: int = 105
    _defense: int = 80
    _magic_attack: int = 80
    _magic_defense: int = 120
    _speed: int = 40
    _evade: int = 0
    _magic_evade: int = 20
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP]
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 10
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = RoyalSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = "[await]"


class MACHINEMADEAxemYellowDouble(Enemy):
    """MACHINE MADE enemy class"""
    _name: str = "MACHINE MADE"

    _hp: int = 200
    _fp: int = 100
    _attack: int = 140
    _defense: int = 130
    _magic_attack: int = 16
    _magic_defense: int = 20
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.POISON]
    _weaknesses: list[Element] = [Element.JUMP]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 25
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = MaxMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 80
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = "[await]"


class DRILLBITEnemyDouble(Enemy):
    """DRILL BIT enemy class"""
    _monster_id: int = 244
    _name: str = "DRILL BIT"

    _hp: int = 80
    _fp: int = 100
    _attack: int = 85
    _defense: int = 70
    _magic_attack: int = 40
    _magic_defense: int = 56
    _speed: int = 15
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 11
    _coins: int = 1
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Mario! It’s time![await]"




class InterchangeableHenchman:
    _enemy: type[Enemy]
    _script: MonsterScript
    _sprite: CompleteSprite
    # model
    # todo: replace pointer set in anim scripts




# henchman areas
# mushroom kingdom
# forest
# croco 1
# punchinello
# tower
# kitchen
# ship
# seaside
# nimbus
# czar
# axems
# smithy