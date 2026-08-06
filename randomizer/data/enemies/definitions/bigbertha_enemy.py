from randomizer.data.items.items import (PickMeUpItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class BIGBERTHAEnemy(Enemy):
    """BIG BERTHA enemy class"""
    _monster_id: int = 101
    _name: str = "BIG BERTHA"

    _hp: int = 350
    _fp: int = 100
    _attack: int = 170
    _defense: int = 130
    _magic_attack: int = 0
    _magic_defense: int = 0
    _speed: int = 1
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 35
    _coins: int = 7
    _yoshi_cookie_item = PickMeUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 3
    _psychopath_message: str = " Adabing, ADABANG![await]"

    _remake_name = "BIG BLASTER"


__all__ = ["BIGBERTHAEnemy"]
