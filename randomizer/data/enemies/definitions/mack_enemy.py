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


class MACKEnemy(Enemy):
    """MACK enemy class"""
    _monster_id: int = 224
    _name: str = "MACK"

    _hp: int = 480
    _fp: int = 28
    _attack: int = 22
    _defense: int = 25
    _magic_attack: int = 15
    _magic_defense: int = 20
    _speed: int = 8
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 24
    _coins: int = 20
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _cursor_x: int = 3
    _cursor_y: int = 8
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Boing, boing, boing.[await]"

    _remake_name = "CLAYMORTON"


__all__ = ["MACKEnemy"]
