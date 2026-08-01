from randomizer.data.items.items import (MidMushroomItem, MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class TERRACOTTAEnemy(Enemy):
    """TERRA COTTA enemy class"""
    _monster_id: int = 64
    _name: str = "TERRA COTTA"

    _hp: int = 180
    _fp: int = 100
    _attack: int = 120
    _defense: int = 85
    _magic_attack: int = 36
    _magic_defense: int = 35
    _speed: int = 23
    _evade: int = 0
    _magic_evade: int = 0
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 25
    _coins: int = 0
    _yoshi_cookie_item = MidMushroomItem
    _rare_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Oh, Mr.Bowser~~[await]"


__all__ = ["TERRACOTTAEnemy"]
