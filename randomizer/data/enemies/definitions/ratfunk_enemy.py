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


class RATFUNKEnemy(Enemy):
    """RAT FUNK enemy class"""
    _monster_id: int = 15
    _name: str = "RAT FUNK"

    _hp: int = 32
    _fp: int = 100
    _attack: int = 20
    _defense: int = 14
    _magic_attack: int = 0
    _magic_defense: int = 6
    _speed: int = 21
    _evade: int = 30
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 2
    _coins: int = 6
    _yoshi_cookie_item = MushroomItem
    _common_item_drop = AbleJuiceItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 40
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Squeek, squeek...[await]"


__all__ = ["RATFUNKEnemy"]
