from randomizer.data.items.items import (PickMeUpItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class ROBOMBEnemy(Enemy):
    """ROB-OMB enemy class"""
    _monster_id: int = 89
    _name: str = "ROB-OMB"

    _hp: int = 42
    _fp: int = 100
    _attack: int = 54
    _defense: int = 63
    _magic_attack: int = 1
    _magic_defense: int = 20
    _speed: int = 2
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 6
    _coins: int = 1
    _yoshi_cookie_item = PickMeUpItem
    _common_item_drop = PickMeUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Disappear? Maybe later![await]"


__all__ = ["ROBOMBEnemy"]
