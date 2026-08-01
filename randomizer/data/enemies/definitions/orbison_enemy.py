from randomizer.data.items.items import (PureWaterItem, RoyalSyrupItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class ORBISONEnemy(Enemy):
    """ORBISON enemy class"""
    _monster_id: int = 107
    _name: str = "ORBISON"

    _hp: int = 30
    _fp: int = 100
    _attack: int = 113
    _defense: int = 140
    _magic_attack: int = 63
    _magic_defense: int = 65
    _speed: int = 25
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.JUMP]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE]
    _xp: int = 18
    _coins: int = 0
    _yoshi_cookie_item = RoyalSyrupItem
    _common_item_drop = PureWaterItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _cursor_x: int = 2
    _cursor_y: int = 4
    _psychopath_message: str = " Don’t jump on me![await]"


__all__ = ["ORBISONEnemy"]
