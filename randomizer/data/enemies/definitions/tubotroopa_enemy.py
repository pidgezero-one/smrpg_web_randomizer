from randomizer.data.items.items import (ElixirItem, RockCandyItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class TUBOTROOPAEnemy(Enemy):
    """TUB-O-TROOPA enemy class"""
    _monster_id: int = 108
    _name: str = "TUB-O-TROOPA"

    _hp: int = 500
    _fp: int = 100
    _attack: int = 200
    _defense: int = 80
    _magic_attack: int = 7
    _magic_defense: int = 34
    _speed: int = 5
    _evade: int = 1
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 40
    _coins: int = 11
    _yoshi_cookie_item = ElixirItem
    _common_item_drop = RockCandyItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 60
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.HOVER_IN
    _elevate: int = 1
    _cursor_x: int = 3
    _cursor_y: int = 4
    _psychopath_message: str = " My shell’s shot![await]"

    _remake_name = "GRAND TROOPA"


__all__ = ["TUBOTROOPAEnemy"]
