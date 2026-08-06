from randomizer.data.items.items import (EnergizerItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)


class K9Enemy(Enemy):
    """K-9 enemy class"""
    _monster_id: int = 16
    _name: str = "K-9"

    _hp: int = 30
    _fp: int = 100
    _attack: int = 13
    _defense: int = 13
    _magic_attack: int = 1
    _magic_defense: int = 10
    _speed: int = 19
    _evade: int = 0
    _magic_evade: int = 0
    _xp: int = 2
    _coins: int = 0
    _yoshi_cookie_item = EnergizerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 30
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " May I take a BITE?[await]"


__all__ = ["K9Enemy"]
