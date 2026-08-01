from randomizer.data.items.items import (MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)


class DIRECTOREnemy(Enemy):
    """DIRECTOR enemy class"""
    _monster_id: int = 114
    _name: str = "DIRECTOR"

    _hp: int = 1000
    _fp: int = 100
    _attack: int = 190
    _defense: int = 120
    _magic_attack: int = 57
    _magic_defense: int = 80
    _speed: int = 35
    _evade: int = 0
    _magic_evade: int = 0
    _xp: int = 70
    _coins: int = 80
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 5
    _cursor_y: int = 6
    _ohko_immune: bool = True
    _psychopath_message: str = " I just lost EVERYTHING.[await]"


__all__ = ["DIRECTOREnemy"]
