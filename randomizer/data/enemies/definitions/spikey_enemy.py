from randomizer.data.items.items import (BracerItem, HoneySyrupItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class SPIKEYEnemy(Enemy):
    """SPIKEY enemy class"""
    _monster_id: int = 1
    _name: str = "SPIKEY"

    _hp: int = 20
    _fp: int = 100
    _attack: int = 6
    _defense: int = 11
    _magic_attack: int = 4
    _magic_defense: int = 2
    _speed: int = 14
    _evade: int = 0
    _magic_evade: int = 0
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 1
    _coins: int = 2
    _yoshi_cookie_item = BracerItem
    _common_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 10
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Just try and jump on me![await]"


__all__ = ["SPIKEYEnemy"]
