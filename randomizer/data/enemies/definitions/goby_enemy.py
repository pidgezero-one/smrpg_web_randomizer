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


class GOBYEnemy(Enemy):
    """GOBY enemy class"""
    _monster_id: int = 9
    _name: str = "GOBY"

    _hp: int = 40
    _fp: int = 100
    _attack: int = 22
    _defense: int = 14
    _magic_attack: int = 2
    _magic_defense: int = 10
    _speed: int = 12
    _evade: int = 20
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 3
    _coins: int = 2
    _yoshi_cookie_item = MushroomItem
    _common_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 10
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_RIGHT
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Blub blub blub...[await]"

    _remake_name = "CHEEP CHEEP"


__all__ = ["GOBYEnemy"]
