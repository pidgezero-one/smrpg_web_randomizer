from randomizer.data.items.items import (FroggieDrinkItem, PowerBlastItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class OCTOVADEREnemy(Enemy):
    """OCTOVADER enemy class"""
    _monster_id: int = 112
    _name: str = "OCTOVADER"

    _hp: int = 250
    _fp: int = 100
    _attack: int = 90
    _defense: int = 50
    _magic_attack: int = 63
    _magic_defense: int = 50
    _speed: int = 5
    _evade: int = 9
    _magic_evade: int = 8
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 30
    _coins: int = 8
    _yoshi_cookie_item = FroggieDrinkItem
    _common_item_drop = PowerBlastItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.DEEP_KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_LEFT
    _elevate: int = 2
    _cursor_x: int = 3
    _cursor_y: int = 6
    _psychopath_message: str = " I’m a part-time typist![await]"


__all__ = ["OCTOVADEREnemy"]
