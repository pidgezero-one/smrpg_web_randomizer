from randomizer.data.items.items import (MaxMushroomItem, RoyalSyrupItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)


class SACKITEnemy(Enemy):
    """SACKIT enemy class"""
    _monster_id: int = 69
    _name: str = "SACKIT"

    _hp: int = 152
    _fp: int = 100
    _attack: int = 70
    _defense: int = 53
    _magic_attack: int = 13
    _magic_defense: int = 20
    _speed: int = 26
    _evade: int = 20
    _magic_evade: int = 0
    _xp: int = 20
    _coins: int = 30
    _yoshi_cookie_item = MaxMushroomItem
    _rare_item_drop = MaxMushroomItem
    _common_item_drop = RoyalSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " This is just how I am.[await]"


__all__ = ["SACKITEnemy"]
