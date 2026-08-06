from randomizer.data.items.items import (PickMeUpItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class PULSAREnemy(Enemy):
    """PULSAR enemy class"""
    _monster_id: int = 110
    _name: str = "PULSAR"

    _hp: int = 69
    _fp: int = 100
    _attack: int = 75
    _defense: int = 90
    _magic_attack: int = 33
    _magic_defense: int = 35
    _speed: int = 8
    _evade: int = 10
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 15
    _coins: int = 12
    _yoshi_cookie_item = PickMeUpItem
    _rare_item_drop = PickMeUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 90
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.PULSAR
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 4
    _psychopath_message: str = " I’m a mini-pulsar.[await]"


__all__ = ["PULSAREnemy"]
