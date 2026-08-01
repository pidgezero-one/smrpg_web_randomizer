from randomizer.data.items.items import (MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)


class TERRAPINEnemy(Enemy):
    """TERRAPIN enemy class"""
    _monster_id: int = 0
    _name: str = "TERRAPIN"

    _hp: int = 10
    _fp: int = 100
    _attack: int = 1
    _defense: int = 8
    _magic_attack: int = 0
    _magic_defense: int = 1
    _speed: int = 10
    _evade: int = 0
    _magic_evade: int = 0
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Yo! What’s going on?[await]"


__all__ = ["TERRAPINEnemy"]
