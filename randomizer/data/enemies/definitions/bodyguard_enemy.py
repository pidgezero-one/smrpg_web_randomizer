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


class BODYGUARDEnemy(Enemy):
    """BODYGUARD enemy class"""
    _monster_id: int = 225
    _name: str = "BODYGUARD"

    _hp: int = 30
    _fp: int = 3
    _attack: int = 20
    _defense: int = 22
    _magic_attack: int = 19
    _magic_defense: int = 12
    _speed: int = 15
    _evade: int = 10
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 30
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Boing, boing, boing.[await]"


__all__ = ["BODYGUARDEnemy"]
