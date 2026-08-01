from randomizer.data.items.items import (FroggieDrinkItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class GECKOEnemy(Enemy):
    """GECKO enemy class"""
    _monster_id: int = 30
    _name: str = "GECKO"

    _hp: int = 92
    _fp: int = 100
    _attack: int = 68
    _defense: int = 46
    _magic_attack: int = 9
    _magic_defense: int = 32
    _speed: int = 22
    _evade: int = 14
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 10
    _coins: int = 0
    _yoshi_cookie_item = FroggieDrinkItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 40
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PUNCH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 2
    _cursor_y: int = 2
    _psychopath_message: str = " Red? What about Green?[await]"


__all__ = ["GECKOEnemy"]
