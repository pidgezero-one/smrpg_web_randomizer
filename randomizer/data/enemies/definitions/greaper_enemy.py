from randomizer.data.items.items import (HoneySyrupItem, PureWaterItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class GREAPEREnemy(Enemy):
    """GREAPER enemy class"""
    _monster_id: int = 20
    _name: str = "GREAPER"

    _hp: int = 148
    _fp: int = 100
    _attack: int = 72
    _defense: int = 50
    _magic_attack: int = 40
    _magic_defense: int = 20
    _speed: int = 30
    _evade: int = 30
    _magic_evade: int = 30
    _weaknesses: list[Element] = [Element.THUNDER]
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 13
    _coins: int = 0
    _yoshi_cookie_item = HoneySyrupItem
    _rare_item_drop = PureWaterItem
    _common_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_RIGHT
    _elevate: int = 1
    _cursor_x: int = 2
    _cursor_y: int = 2
    _psychopath_message: str = " Any reaping to be done?[await]"


__all__ = ["GREAPEREnemy"]
