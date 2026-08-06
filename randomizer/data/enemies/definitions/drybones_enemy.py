from randomizer.data.items.items import (MaxMushroomItem, MushroomItem, PureWaterItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class DRYBONESEnemy(Enemy):
    """DRY BONES enemy class"""
    _monster_id: int = 19
    _name: str = "DRY BONES"

    _hp: int = 0
    _fp: int = 100
    _attack: int = 74
    _defense: int = 0
    _magic_attack: int = 7
    _magic_defense: int = 0
    _speed: int = 9
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 12
    _coins: int = 5
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = PureWaterItem
    _common_item_drop = MaxMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BONK
    _sound_on_approach: ApproachSound = ApproachSound.DRY_BONES
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 1
    _cursor_y: int = 3
    _disable_auto_death: bool = True
    _psychopath_message: str = " I’m sick of gettin’ hit![await]"


__all__ = ["DRYBONESEnemy"]
