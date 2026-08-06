from randomizer.data.items.items import (MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class SNIFIT2Enemy(Enemy):
    """SNIFIT enemy class"""
    _monster_id: int = 250
    _name: str = "STRONG SNIFIT"

    _hp: int = 2200
    _fp: int = 100
    _attack: int = 220
    _defense: int = 100
    _magic_attack: int = 180
    _magic_defense: int = 60
    _speed: int = 26
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 2
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.PUNCH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " I don't get enough paid vacation.[await]\n I should get to cash it out[await]\n at the end of the year![await]"

    _remake_name = "SNIFSTER S"


__all__ = ["SNIFIT2Enemy"]
