from randomizer.data.items.items import (FroggieDrinkItem, MaxMushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)


class GUGOOMBAEnemy(Enemy):
    """GU GOOMBA enemy class"""
    _monster_id: int = 70
    _name: str = "GU GOOMBA"

    _hp: int = 132
    _fp: int = 100
    _attack: int = 115
    _defense: int = 66
    _magic_attack: int = 13
    _magic_defense: int = 66
    _speed: int = 14
    _evade: int = 0
    _magic_evade: int = 50
    _xp: int = 15
    _coins: int = 1
    _yoshi_cookie_item = FroggieDrinkItem
    _rare_item_drop = MaxMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Hey, maybe I CAN win![await]"

    _remake_name = "PRO GOOMBA"


__all__ = ["GUGOOMBAEnemy"]
