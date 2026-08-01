from randomizer.data.items.items import (HoneySyrupItem, PickMeUpItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class SHADOWEnemy(Enemy):
    """SHADOW enemy class"""
    _monster_id: int = 45
    _name: str = "SHADOW"

    _hp: int = 85
    _fp: int = 14
    _attack: int = 24
    _defense: int = 5
    _magic_attack: int = 20
    _magic_defense: int = 20
    _speed: int = 18
    _evade: int = 10
    _magic_evade: int = 0
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 3
    _coins: int = 2
    _yoshi_cookie_item = HoneySyrupItem
    _common_item_drop = PickMeUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_RIGHT
    _elevate: int = 2
    _cursor_x: int = 3
    _cursor_y: int = 4
    _psychopath_message: str = " You’re a model, right?[await]"


__all__ = ["SHADOWEnemy"]
