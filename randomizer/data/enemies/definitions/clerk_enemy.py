from randomizer.data.items.items import (MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)


class CLERKEnemy(Enemy):
    """CLERK enemy class"""
    _monster_id: int = 50
    _name: str = "CLERK"

    _hp: int = 500
    _fp: int = 100
    _attack: int = 160
    _defense: int = 100
    _magic_attack: int = 47
    _magic_defense: int = 60
    _speed: int = 15
    _evade: int = 0
    _magic_evade: int = 0
    _xp: int = 50
    _coins: int = 20
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 5
    _cursor_y: int = 6
    _ohko_immune: bool = True
    _psychopath_message: str = " 10 years I’ve been here![await]"


__all__ = ["CLERKEnemy"]
