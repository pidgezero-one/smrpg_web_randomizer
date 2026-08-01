from randomizer.data.items.items import (MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)


class FACTORYCHIEFEnemy(Enemy):
    """FACTORY CHIEF enemy class"""
    _monster_id: int = 74
    _name: str = "FACTORY CHIEF"

    _hp: int = 1000
    _fp: int = 100
    _attack: int = 200
    _defense: int = 120
    _magic_attack: int = 70
    _magic_defense: int = 90
    _speed: int = 45
    _evade: int = 0
    _magic_evade: int = 0
    _xp: int = 80
    _coins: int = 90
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = " Who DARES to fight ME?![await]"


__all__ = ["FACTORYCHIEFEnemy"]
