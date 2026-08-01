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


class REMOCONEnemy(Enemy):
    """REMO CON enemy class"""
    _monster_id: int = 53
    _name: str = "REMO CON"

    _hp: int = 88
    _fp: int = 100
    _attack: int = 56
    _defense: int = 52
    _magic_attack: int = 25
    _magic_defense: int = 10
    _speed: int = 5
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER]
    _xp: int = 8
    _coins: int = 7
    _yoshi_cookie_item = PickMeUpItem
    _common_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 2
    _cursor_y: int = 5
    _psychopath_message: str = " The world is history.[await]"

    _remake_name = "DOLLOX"


__all__ = ["REMOCONEnemy"]
