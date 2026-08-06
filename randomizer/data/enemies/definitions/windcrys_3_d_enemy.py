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


class WINDCRYS3DEnemy(Enemy):
    """WIND CRYS 3D enemy class"""
    _monster_id: int = 242
    _name: str = "WIND CRYS 3D"

    _hp: int = 1800
    _fp: int = 250
    _attack: int = 0
    _defense: int = 150
    _magic_attack: int = 90
    _magic_defense: int = 108
    _speed: int = 30
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.JUMP]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 2
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _share_palette: bool = True
    _psychopath_message: str = " Whooooosh...  Swoooooosh...[await]"


__all__ = ["WINDCRYS3DEnemy"]
