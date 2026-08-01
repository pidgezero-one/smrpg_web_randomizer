from randomizer.data.items.items import (BracerItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class SPIKESTEREnemy(Enemy):
    """SPIKESTER enemy class"""
    _monster_id: int = 65
    _name: str = "SPIKESTER"

    _hp: int = 50
    _fp: int = 100
    _attack: int = 48
    _defense: int = 60
    _magic_attack: int = 12
    _magic_defense: int = 4
    _speed: int = 19
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 6
    _coins: int = 2
    _yoshi_cookie_item = BracerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 50
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Why, you’re AFRAID of me![await]"


__all__ = ["SPIKESTEREnemy"]
