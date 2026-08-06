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


class STARSLAPEnemy(Enemy):
    """STARSLAP enemy class"""
    _monster_id: int = 176
    _name: str = "STARSLAP"

    _hp: int = 62
    _fp: int = 100
    _attack: int = 25
    _defense: int = 24
    _magic_attack: int = 4
    _magic_defense: int = 10
    _speed: int = 9
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER, Element.FIRE]
    _xp: int = 2
    _coins: int = 2
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _elevate: int = 1
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " They think I’m goofy...[await]"


__all__ = ["STARSLAPEnemy"]
