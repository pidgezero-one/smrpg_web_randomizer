from randomizer.data.items.items import (ElixirItem, EnergizerItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)


class SPRINGEREnemy(Enemy):
    """SPRINGER enemy class"""
    _monster_id: int = 120
    _name: str = "SPRINGER"

    _hp: int = 122
    _fp: int = 100
    _attack: int = 155
    _defense: int = 110
    _magic_attack: int = 100
    _magic_defense: int = 79
    _speed: int = 16
    _evade: int = 30
    _magic_evade: int = 0
    _xp: int = 29
    _coins: int = 2
    _yoshi_cookie_item = ElixirItem
    _rare_item_drop = EnergizerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 40
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " What’s going on here?[await]"


__all__ = ["SPRINGEREnemy"]
