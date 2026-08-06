from randomizer.data.items.items import (AbleJuiceItem, HoneySyrupItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class CARROBOSCISEnemy(Enemy):
    """CARROBOSCIS enemy class"""
    _monster_id: int = 60
    _name: str = "CARROBOSCIS"

    _hp: int = 90
    _fp: int = 100
    _attack: int = 55
    _defense: int = 44
    _magic_attack: int = 28
    _magic_defense: int = 22
    _speed: int = 30
    _evade: int = 13
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 10
    _coins: int = 4
    _yoshi_cookie_item = HoneySyrupItem
    _rare_item_drop = AbleJuiceItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 6
    _psychopath_message: str = " I ALWAYS eat my vegetables![await]"


__all__ = ["CARROBOSCISEnemy"]
