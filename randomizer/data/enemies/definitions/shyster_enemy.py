from randomizer.data.items.items import (HoneySyrupItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)


class SHYSTEREnemy(Enemy):
    """SHYSTER enemy class"""
    _monster_id: int = 158
    _name: str = "SHYSTER"

    _hp: int = 30
    _fp: int = 2
    _attack: int = 20
    _defense: int = 26
    _magic_attack: int = 18
    _magic_defense: int = 10
    _speed: int = 18
    _evade: int = 10
    _magic_evade: int = 0
    _xp: int = 3
    _coins: int = 2
    _yoshi_cookie_item = HoneySyrupItem
    _common_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Boing, boing, boing.[await]"

    _remake_name = "SHYMORE"


__all__ = ["SHYSTEREnemy"]
