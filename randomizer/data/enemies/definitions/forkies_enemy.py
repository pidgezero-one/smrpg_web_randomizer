from randomizer.data.items.items import (RoyalSyrupItem, SleepyBombItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)


class FORKIESEnemy(Enemy):
    """FORKIES enemy class"""
    _monster_id: int = 99
    _name: str = "FORKIES"

    _hp: int = 350
    _fp: int = 100
    _attack: int = 170
    _defense: int = 120
    _magic_attack: int = 45
    _magic_defense: int = 128
    _speed: int = 200
    _evade: int = 0
    _magic_evade: int = 0
    _xp: int = 32
    _coins: int = 7
    _yoshi_cookie_item = RoyalSyrupItem
    _rare_item_drop = SleepyBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 4
    _psychopath_message: str = " Shikashikashika~~![await]"

    _remake_name = "FORKIE"


__all__ = ["FORKIESEnemy"]
