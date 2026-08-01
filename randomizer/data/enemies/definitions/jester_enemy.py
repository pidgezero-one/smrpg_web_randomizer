from randomizer.data.items.items import (HoneySyrupItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class JESTEREnemy(Enemy):
    """JESTER enemy class"""
    _monster_id: int = 57
    _name: str = "JESTER"

    _hp: int = 151
    _fp: int = 12
    _attack: int = 48
    _defense: int = 35
    _magic_attack: int = 22
    _magic_defense: int = 35
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 80
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 10
    _coins: int = 10
    _yoshi_cookie_item = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 3
    _cursor_y: int = 4
    _psychopath_message: str = " I’ve failed my King...[await]"


__all__ = ["JESTEREnemy"]
