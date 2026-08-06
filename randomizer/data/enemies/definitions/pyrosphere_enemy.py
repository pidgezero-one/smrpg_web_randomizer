from randomizer.data.items.items import (FireBombItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class PYROSPHEREEnemy(Enemy):
    """PYROSPHERE enemy class"""
    _monster_id: int = 85
    _name: str = "PYROSPHERE"

    _hp: int = 167
    _fp: int = 100
    _attack: int = 105
    _defense: int = 66
    _magic_attack: int = 100
    _magic_defense: int = 48
    _speed: int = 24
    _evade: int = 7
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.POISON]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 17
    _coins: int = 2
    _yoshi_cookie_item = FireBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 40
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Vroom, VROOM!![await]"

    _remake_name = "LAVA BABBLE"


__all__ = ["PYROSPHEREEnemy"]
