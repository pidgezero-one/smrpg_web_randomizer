from randomizer.data.items.items import (BracerItem, PickMeUpItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class JABITEnemy(Enemy):
    """JABIT enemy class"""
    _monster_id: int = 95
    _name: str = "JABIT"

    _hp: int = 150
    _fp: int = 100
    _attack: int = 120
    _defense: int = 95
    _magic_attack: int = 27
    _magic_defense: int = 34
    _speed: int = 13
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 18
    _coins: int = 0
    _yoshi_cookie_item = BracerItem
    _common_item_drop = PickMeUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 10
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " This is the pits![await]"


__all__ = ["JABITEnemy"]
