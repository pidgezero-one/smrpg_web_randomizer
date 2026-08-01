from randomizer.data.items.items import (PureWaterItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class HOBGOBLINEnemy(Enemy):
    """HOBGOBLIN enemy class"""
    _monster_id: int = 40
    _name: str = "HOBGOBLIN"

    _hp: int = 50
    _fp: int = 8
    _attack: int = 22
    _defense: int = 22
    _magic_attack: int = 8
    _magic_defense: int = 12
    _speed: int = 5
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 4
    _coins: int = 3
    _yoshi_cookie_item = PureWaterItem
    _rare_item_drop = PureWaterItem
    _common_item_drop = PureWaterItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 60
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 2
    _cursor_y: int = 5
    _psychopath_message: str = " Havin’ a blast today![await]"


__all__ = ["HOBGOBLINEnemy"]
