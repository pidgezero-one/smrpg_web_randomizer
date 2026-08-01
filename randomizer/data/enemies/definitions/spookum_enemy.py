from randomizer.data.items.items import (MidMushroomItem, SleepyBombItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class SPOOKUMEnemy(Enemy):
    """SPOOKUM enemy class"""
    _monster_id: int = 26
    _name: str = "SPOOKUM"

    _hp: int = 98
    _fp: int = 100
    _attack: int = 50
    _defense: int = 45
    _magic_attack: int = 32
    _magic_defense: int = 5
    _speed: int = 18
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 8
    _coins: int = 4
    _yoshi_cookie_item = SleepyBombItem
    _common_item_drop = MidMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 10
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.PUNCH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Que pasa?[await]"

    _remake_name = "SNIFIT"


__all__ = ["SPOOKUMEnemy"]
