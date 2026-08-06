from randomizer.data.items.items import (AbleJuiceItem, HoneySyrupItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class WIGGLEREnemy(Enemy):
    """WIGGLER enemy class"""
    _monster_id: int = 31
    _name: str = "WIGGLER"

    _hp: int = 120
    _fp: int = 100
    _attack: int = 40
    _defense: int = 25
    _magic_attack: int = 18
    _magic_defense: int = 20
    _speed: int = 10
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 6
    _coins: int = 10
    _yoshi_cookie_item = AbleJuiceItem
    _rare_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 40
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 2
    _cursor_y: int = 3
    _psychopath_message: str = " I’m just a helpless wiggler...[await]"


__all__ = ["WIGGLEREnemy"]
