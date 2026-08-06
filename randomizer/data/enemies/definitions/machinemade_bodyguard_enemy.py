from randomizer.data.items.items import (MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)


class MACHINEMADEBodyguardEnemy(Enemy):
    """MACHINE MADE enemy class"""
    _monster_id: int = 145
    _name: str = "MACHINE MADE"

    _hp: int = 100
    _fp: int = 250
    _attack: int = 135
    _defense: int = 95
    _magic_attack: int = 90
    _magic_defense: int = 65
    _speed: int = 36
    _evade: int = 10
    _magic_evade: int = 0
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Boing, boing, boing.[await]"


__all__ = ["MACHINEMADEBodyguardEnemy"]
