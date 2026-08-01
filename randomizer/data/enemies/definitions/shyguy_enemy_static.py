from randomizer.data.items.items import (HoneySyrupItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)


class SHYGUYEnemyStatic(Enemy):
    """SHY GUY enemy class"""
    _monster_id: int = 90
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
    _psychopath_message: str = " Hold still, okay?![await]"


__all__ = ["SHYGUYEnemyStatic"]
