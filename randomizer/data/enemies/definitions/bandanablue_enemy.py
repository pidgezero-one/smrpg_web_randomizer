from randomizer.data.items.items import (MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class BANDANABLUEEnemy(Enemy):
    """BANDANA BLUE enemy class"""
    _monster_id: int = 75
    _name: str = "BANDANA BLUE"

    _hp: int = 150
    _fp: int = 100
    _attack: int = 80
    _defense: int = 60
    _magic_attack: int = 20
    _magic_defense: int = 30
    _speed: int = 30
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER, Element.FIRE]
    _xp: int = 20
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Color me Blue, mates!![await]"


__all__ = ["BANDANABLUEEnemy"]
