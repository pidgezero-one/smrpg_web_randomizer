from randomizer.data.items.items import (FireBombItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class SPARKYEnemy(Enemy):
    """SPARKY enemy class"""
    _monster_id: int = 21
    _name: str = "SPARKY"

    _hp: int = 120
    _fp: int = 12
    _attack: int = 40
    _defense: int = 1
    _magic_attack: int = 38
    _magic_defense: int = 50
    _speed: int = 19
    _evade: int = 6
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 4
    _coins: int = 1
    _yoshi_cookie_item = FireBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Fire EVERYWHERE![await]"

    _remake_name = "LAVA BUBBLE"


__all__ = ["SPARKYEnemy"]
