from randomizer.data.items.items import (MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class BUZZEREnemy(Enemy):
    """BUZZER enemy class"""
    _monster_id: int = 28
    _name: str = "BUZZER"

    _hp: int = 43
    _fp: int = 100
    _attack: int = 37
    _defense: int = 15
    _magic_attack: int = 4
    _magic_defense: int = 1
    _speed: int = 25
    _evade: int = 30
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER, Element.JUMP]
    _xp: int = 4
    _coins: int = 1
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_LEFT
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Buzzzzz...[await]"


__all__ = ["BUZZEREnemy"]
