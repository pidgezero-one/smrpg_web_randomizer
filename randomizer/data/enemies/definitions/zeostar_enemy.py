from randomizer.data.items.items import (MushroomItem, SleepyBombItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class ZEOSTAREnemy(Enemy):
    """ZEOSTAR enemy class"""
    _monster_id: int = 178
    _name: str = "ZEOSTAR"

    _hp: int = 90
    _fp: int = 4
    _attack: int = 75
    _defense: int = 60
    _magic_attack: int = 28
    _magic_defense: int = 20
    _speed: int = 10
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER, Element.FIRE]
    _xp: int = 10
    _coins: int = 3
    _yoshi_cookie_item = SleepyBombItem
    _rare_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 30
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _elevate: int = 1
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Oh, I can’t stand him![await]"


__all__ = ["ZEOSTAREnemy"]
