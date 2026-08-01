from randomizer.data.items.items import (MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)


class MANAGEREnemy(Enemy):
    """MANAGER enemy class"""
    _monster_id: int = 76
    _name: str = "MANAGER"

    _hp: int = 800
    _fp: int = 100
    _attack: int = 170
    _defense: int = 110
    _magic_attack: int = 60
    _magic_defense: int = 70
    _speed: int = 25
    _evade: int = 0
    _magic_evade: int = 0
    _xp: int = 60
    _coins: int = 40
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 2
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = " 25 years of working, sigh.[await]"


__all__ = ["MANAGEREnemy"]
