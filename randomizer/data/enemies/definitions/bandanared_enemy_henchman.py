from randomizer.data.items.items import (EnergizerItem, MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class BANDANAREDEnemyHenchman(Enemy):
    """BANDANA RED enemy class"""
    _monster_id: int = 124
    _name: str = "BANDANA RED"

    _hp: int = 124
    _fp: int = 100
    _attack: int = 78
    _defense: int = 60
    _magic_attack: int = 25
    _magic_defense: int = 25
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER, Element.FIRE]
    _xp: int = 18
    _coins: int = 10
    _yoshi_cookie_item = EnergizerItem
    _rare_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 30
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " I love the color RED![await]"


__all__ = ["BANDANAREDEnemyHenchman"]
