from randomizer.data.items.items import (AbleJuiceItem, MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class MRKIPPEREnemy(Enemy):
    """MR.KIPPER enemy class"""
    _monster_id: int = 73
    _name: str = "MR.KIPPER"

    _hp: int = 133
    _fp: int = 100
    _attack: int = 75
    _defense: int = 45
    _magic_attack: int = 14
    _magic_defense: int = 10
    _speed: int = 23
    _evade: int = 13
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER, Element.FIRE]
    _xp: int = 8
    _coins: int = 2
    _yoshi_cookie_item = MushroomItem
    _common_item_drop = AbleJuiceItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_RIGHT
    _elevate: int = 3
    _cursor_x: int = 2
    _cursor_y: int = 2
    _psychopath_message: str = " I’m a fresh little fish.[await]"


__all__ = ["MRKIPPEREnemy"]
