from randomizer.data.items.items import (AbleJuiceItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)


class STINGEREnemy(Enemy):
    """STINGER enemy class"""
    _monster_id: int = 92
    _name: str = "STINGER"

    _hp: int = 65
    _fp: int = 100
    _attack: int = 78
    _defense: int = 80
    _magic_attack: int = 23
    _magic_defense: int = 10
    _speed: int = 33
    _evade: int = 25
    _magic_evade: int = 0
    _xp: int = 13
    _coins: int = 1
    _yoshi_cookie_item = AbleJuiceItem
    _rare_item_drop = AbleJuiceItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 40
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_LEFT
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Strike the pose![await]"


__all__ = ["STINGEREnemy"]
