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


class GLUMREAPEREnemy(Enemy):
    """GLUM REAPER enemy class"""
    _monster_id: int = 84
    _name: str = "GLUM REAPER"

    _hp: int = 180
    _fp: int = 100
    _attack: int = 120
    _defense: int = 55
    _magic_attack: int = 60
    _magic_defense: int = 80
    _speed: int = 35
    _evade: int = 20
    _magic_evade: int = 10
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 35
    _coins: int = 3
    _yoshi_cookie_item = PureWaterItem
    _common_item_drop = PureWaterItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_RIGHT
    _elevate: int = 1
    _cursor_x: int = 2
    _cursor_y: int = 2
    _psychopath_message: str = " Comin’ through...[await]"


__all__ = ["GLUMREAPEREnemy"]
