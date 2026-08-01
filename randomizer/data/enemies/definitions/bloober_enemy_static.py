from randomizer.data.items.items import (ElixirItem, HoneySyrupItem, MaxMushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class BLOOBEREnemyStatic(Enemy):
    """BLOOBER enemy class"""
    _monster_id: int = 10
    _name: str = "BLOOBER"

    _hp: int = 130
    _fp: int = 100
    _attack: int = 80
    _defense: int = 36
    _magic_attack: int = 21
    _magic_defense: int = 16
    _speed: int = 23
    _evade: int = 20
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER, Element.FIRE]
    _xp: int = 12
    _coins: int = 0
    _yoshi_cookie_item = ElixirItem
    _rare_item_drop = HoneySyrupItem
    _common_item_drop = MaxMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 100
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PUNCH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.HOVER_IN
    _elevate: int = 2
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " I love floating around.[await]"

    _remake_name = "BLOOPER"


__all__ = ["BLOOBEREnemyStatic"]
