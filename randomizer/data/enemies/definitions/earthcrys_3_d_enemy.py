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


class EARTHCRYS3DEnemy(Enemy):
    """EARTH CRYS 3D enemy class"""
    _monster_id: int = 203
    _name: str = "EARTH CRYS 3D"

    _hp: int = 4200
    _fp: int = 250
    _attack: int = 1
    _defense: int = 100
    _magic_attack: int = 105
    _magic_defense: int = 53
    _speed: int = 5
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.THUNDER]
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 3
    _cursor_x: int = 2
    _cursor_y: int = 2
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _share_palette: bool = True
    _psychopath_message: str = "Personally, I'd never felt the need...[await]\n...to become three-dimensional.[await]"


__all__ = ["EARTHCRYS3DEnemy"]
