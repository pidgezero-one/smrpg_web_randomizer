from randomizer.data.items.items import (HoneySyrupItem, MapleSyrupItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class ORBUSEREnemy(Enemy):
    """ORB USER enemy class"""
    _monster_id: int = 43
    _name: str = "ORB USER"

    _hp: int = 8
    _fp: int = 20
    _attack: int = 42
    _defense: int = 80
    _magic_attack: int = 28
    _magic_defense: int = 40
    _speed: int = 15
    _evade: int = 0
    _magic_evade: int = 0
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE]
    _xp: int = 5
    _coins: int = 2
    _yoshi_cookie_item = MapleSyrupItem
    _rare_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 40
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _cursor_x: int = 2
    _cursor_y: int = 5
    _psychopath_message: str = " I hate Kinklinks![await]"


__all__ = ["ORBUSEREnemy"]
