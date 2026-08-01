from randomizer.data.items.items import (KerokeroColaItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class SHYRANGEREnemy(Enemy):
    """SHY RANGER enemy class"""
    _monster_id: int = 24
    _name: str = "SHY RANGER"

    _hp: int = 300
    _fp: int = 100
    _attack: int = 100
    _defense: int = 80
    _magic_attack: int = 4
    _magic_defense: int = 10
    _speed: int = 43
    _evade: int = 50
    _magic_evade: int = 0
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE, Element.JUMP]
    _xp: int = 60
    _coins: int = 1
    _yoshi_cookie_item = KerokeroColaItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 50
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = " Transmitting information.[await]\n Over and out.[await]"


__all__ = ["SHYRANGEREnemy"]
