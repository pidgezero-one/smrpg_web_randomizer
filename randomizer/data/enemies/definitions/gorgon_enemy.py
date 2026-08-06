from randomizer.data.items.items import (MapleSyrupItem, MidMushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class GORGONEnemy(Enemy):
    """GORGON enemy class"""
    _monster_id: int = 100
    _name: str = "GORGON"

    _hp: int = 140
    _fp: int = 100
    _attack: int = 86
    _defense: int = 73
    _magic_attack: int = 24
    _magic_defense: int = 52
    _speed: int = 16
    _evade: int = 11
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 20
    _coins: int = 0
    _yoshi_cookie_item = MapleSyrupItem
    _rare_item_drop = MidMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 3
    _cursor_x: int = 2
    _cursor_y: int = 4
    _psychopath_message: str = " I just wanna go home.[await]"

    _remake_name = "ENIGMAX"


__all__ = ["GORGONEnemy"]
