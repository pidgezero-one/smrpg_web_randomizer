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


class SKYTROOPAEnemy(Enemy):
    """SKY TROOPA enemy class"""
    _monster_id: int = 2
    _name: str = "SKY TROOPA"

    _hp: int = 10
    _fp: int = 100
    _attack: int = 4
    _defense: int = 16
    _magic_attack: int = 6
    _magic_defense: int = 4
    _speed: int = 18
    _evade: int = 8
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.JUMP]
    _xp: int = 1
    _coins: int = 1
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOVER_IN
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 2
    _psychopath_message: str = " What a gorgeous day![await]"

    _remake_name = "PARATROOPA"


__all__ = ["SKYTROOPAEnemy"]
