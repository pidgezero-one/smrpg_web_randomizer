from randomizer.data.items.items import (MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class KAMEKEnemy(Enemy):
    """KAMEK enemy class"""
    _monster_id: int = 33
    _name: str = "MAGIKOOPA"

    _hp: int = 1600
    _fp: int = 250
    _attack: int = 100
    _defense: int = 60
    _magic_attack: int = 120
    _magic_defense: int = 100
    _speed: int = 12
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON]
    _xp: int = 30
    _coins: int = 10
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 4
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " That’s...my child?[await]"

    _remake_name = "WIZAKOOPA"


__all__ = ["KAMEKEnemy"]
