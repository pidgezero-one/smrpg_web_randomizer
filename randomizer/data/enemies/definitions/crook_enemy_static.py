from randomizer.data.items.items import (HoneySyrupItem, MidMushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)


class CROOKEnemyStatic(Enemy):
    """CROOK enemy class"""
    _monster_id: int = 5
    _name: str = "CROOK"

    _hp: int = 38
    _fp: int = 100
    _attack: int = 35
    _defense: int = 32
    _magic_attack: int = 12
    _magic_defense: int = 25
    _speed: int = 22
    _evade: int = 40
    _magic_evade: int = 40
    _xp: int = 10
    _coins: int = 10
    _yoshi_cookie_item = MidMushroomItem
    _rare_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " You can’t run away! Ha![await]"


__all__ = ["CROOKEnemyStatic"]
