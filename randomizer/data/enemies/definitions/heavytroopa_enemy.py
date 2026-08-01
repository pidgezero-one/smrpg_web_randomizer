from randomizer.data.items.items import (CrystallineItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class HEAVYTROOPAEnemy(Enemy):
    """HEAVY TROOPA enemy class"""
    _monster_id: int = 44
    _name: str = "HEAVY TROOPA"

    _hp: int = 250
    _fp: int = 100
    _attack: int = 160
    _defense: int = 100
    _magic_attack: int = 1
    _magic_defense: int = 50
    _speed: int = 3
    _evade: int = 2
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.JUMP]
    _xp: int = 32
    _coins: int = 4
    _yoshi_cookie_item = CrystallineItem
    _common_item_drop = CrystallineItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOVER_IN
    _elevate: int = 1
    _cursor_x: int = 3
    _cursor_y: int = 5
    _psychopath_message: str = " I’ll make ya beautiful![await]"

    _remake_name = "HEAVY TROOPA"


__all__ = ["HEAVYTROOPAEnemy"]
