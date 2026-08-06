from randomizer.data.items.items import (MushroomItem, SleepyBombItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class SNAPDRAGONEnemy(Enemy):
    """SNAPDRAGON enemy class"""
    _monster_id: int = 54
    _name: str = "SNAPDRAGON"

    _hp: int = 90
    _fp: int = 100
    _attack: int = 28
    _defense: int = 25
    _magic_attack: int = 31
    _magic_defense: int = 25
    _speed: int = 4
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 4
    _coins: int = 3
    _yoshi_cookie_item = SleepyBombItem
    _rare_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 20
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.SLAP
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 2
    _cursor_y: int = 4
    _psychopath_message: str = " I did a lot in my youth.[await]"


__all__ = ["SNAPDRAGONEnemy"]
