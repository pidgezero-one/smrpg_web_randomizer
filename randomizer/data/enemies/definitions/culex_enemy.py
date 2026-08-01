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


class CULEXEnemy(Enemy):
    """CULEX enemy class"""
    _monster_id: int = 255
    _name: str = "CULEX"

    _hp: int = 4096
    _fp: int = 200
    _attack: int = 250
    _defense: int = 100
    _magic_attack: int = 100
    _magic_defense: int = 80
    _speed: int = 50
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 600
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.FADE_IN
    _elevate: int = 1
    _cursor_x: int = 6
    _cursor_y: int = 7
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " A little off, eh?[await]"


__all__ = ["CULEXEnemy"]
