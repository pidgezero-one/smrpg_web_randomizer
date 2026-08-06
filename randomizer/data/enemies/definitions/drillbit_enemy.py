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


class DRILLBITEnemy(Enemy):
    """DRILL BIT enemy class"""
    _monster_id: int = 227
    _name: str = "DRILL BIT"

    _hp: int = 80
    _fp: int = 100
    _attack: int = 85
    _defense: int = 70
    _magic_attack: int = 40
    _magic_defense: int = 56
    _speed: int = 15
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 11
    _coins: int = 1
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " This is for Yaridovich![await]"


__all__ = ["DRILLBITEnemy"]
