from randomizer.data.items.items import (MapleSyrupItem, RoyalSyrupItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)


class SHAMANEnemy(Enemy):
    """SHAMAN enemy class"""
    _monster_id: int = 4
    _name: str = "SHAMAN"

    _hp: int = 150
    _fp: int = 100
    _attack: int = 92
    _defense: int = 50
    _magic_attack: int = 80
    _magic_defense: int = 90
    _speed: int = 9
    _evade: int = 0
    _magic_evade: int = 0
    _xp: int = 17
    _coins: int = 4
    _yoshi_cookie_item = RoyalSyrupItem
    _rare_item_drop = MapleSyrupItem
    _common_item_drop = RoyalSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " I’m losing this fight![await]"


__all__ = ["SHAMANEnemy"]
