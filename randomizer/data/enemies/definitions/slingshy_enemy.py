from randomizer.data.items.items import (HoneySyrupItem, MapleSyrupItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)


class SLINGSHYEnemy(Enemy):
    """SLING SHY enemy class"""
    _monster_id: int = 88
    _name: str = "SLING SHY"

    _hp: int = 120
    _fp: int = 100
    _attack: int = 108
    _defense: int = 80
    _magic_attack: int = 42
    _magic_defense: int = 21
    _speed: int = 16
    _evade: int = 0
    _magic_evade: int = 0
    _xp: int = 3
    _coins: int = 20
    _yoshi_cookie_item = MapleSyrupItem
    _rare_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Hear my song.[await]"


__all__ = ["SLINGSHYEnemy"]
