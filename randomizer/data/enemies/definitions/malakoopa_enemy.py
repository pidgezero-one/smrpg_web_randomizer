from randomizer.data.items.items import (HoneySyrupItem, MapleSyrupItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class MALAKOOPAEnemy(Enemy):
    """MALAKOOPA enemy class"""
    _monster_id: int = 66
    _name: str = "MALAKOOPA"

    _hp: int = 95
    _fp: int = 100
    _attack: int = 130
    _defense: int = 120
    _magic_attack: int = 47
    _magic_defense: int = 98
    _speed: int = 35
    _evade: int = 20
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 23
    _coins: int = 3
    _yoshi_cookie_item = MapleSyrupItem
    _rare_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOVER_IN
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 2
    _psychopath_message: str = " Just call me “General!”[await]"


__all__ = ["MALAKOOPAEnemy"]
