from randomizer.data.items.items import (PickMeUpItem, RoyalSyrupItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class REACHEREnemy(Enemy):
    """REACHER enemy class"""
    _monster_id: int = 41
    _name: str = "REACHER"

    _hp: int = 184
    _fp: int = 100
    _attack: int = 95
    _defense: int = 75
    _magic_attack: int = 8
    _magic_defense: int = 0
    _speed: int = 3
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 30
    _coins: int = 8
    _yoshi_cookie_item = PickMeUpItem
    _rare_item_drop = PickMeUpItem
    _common_item_drop = RoyalSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 60
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 4
    _cursor_y: int = 6
    _psychopath_message: str = " Hope you’ll stay close.[await]"


__all__ = ["REACHEREnemy"]
