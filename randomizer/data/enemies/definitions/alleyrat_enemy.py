from randomizer.data.items.items import (AbleJuiceItem, MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)


class ALLEYRATEnemy(Enemy):
    """ALLEY RAT enemy class"""
    _monster_id: int = 79
    _name: str = "ALLEY RAT"

    _hp: int = 105
    _fp: int = 100
    _attack: int = 70
    _defense: int = 55
    _magic_attack: int = 13
    _magic_defense: int = 12
    _speed: int = 21
    _evade: int = 15
    _magic_evade: int = 0
    _xp: int = 9
    _coins: int = 3
    _yoshi_cookie_item = AbleJuiceItem
    _rare_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Don’t pity me, Mario![await]"


__all__ = ["ALLEYRATEnemy"]
