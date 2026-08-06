from randomizer.data.items.items import (BracerItem, MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class CHOMPEnemy(Enemy):
    """CHOMP enemy class"""
    _monster_id: int = 22
    _name: str = "CHOMP"

    _hp: int = 100
    _fp: int = 100
    _attack: int = 60
    _defense: int = 65
    _magic_attack: int = 5
    _magic_defense: int = 31
    _speed: int = 10
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 10
    _coins: int = 0
    _yoshi_cookie_item = BracerItem
    _common_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 3
    _psychopath_message: str = " Workin’ on a chain gang.[await]"

    _remake_name = "CHAIN CHOMP"


__all__ = ["CHOMPEnemy"]
