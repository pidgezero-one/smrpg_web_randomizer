from randomizer.data.items.items import (PickMeUpItem, RoyalSyrupItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class SHOGUNEnemy(Enemy):
    """SHOGUN enemy class"""
    _monster_id: int = 42
    _name: str = "SHOGUN"

    _hp: int = 150
    _fp: int = 100
    _attack: int = 100
    _defense: int = 80
    _magic_attack: int = 1
    _magic_defense: int = 32
    _speed: int = 12
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 24
    _coins: int = 10
    _yoshi_cookie_item = RoyalSyrupItem
    _rare_item_drop = PickMeUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 3
    _cursor_y: int = 4
    _psychopath_message: str = " Do as you like.[await]"


__all__ = ["SHOGUNEnemy"]
