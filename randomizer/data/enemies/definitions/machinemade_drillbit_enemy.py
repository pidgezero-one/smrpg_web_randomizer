from randomizer.data.items.items import (MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)


class MACHINEMADEDrillbitEnemy(Enemy):
    """MACHINE MADE enemy class"""
    _monster_id: int = 146
    _name: str = "MACHINE MADE"

    _hp: int = 180
    _fp: int = 100
    _attack: int = 130
    _defense: int = 82
    _magic_attack: int = 31
    _magic_defense: int = 69
    _speed: int = 24
    _evade: int = 0
    _magic_evade: int = 0
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Look out, LOSERS![await]"


__all__ = ["MACHINEMADEDrillbitEnemy"]
