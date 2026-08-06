from randomizer.data.items.items import (MapleSyrupItem, MidMushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class LAKITUEnemy(Enemy):
    """LAKITU enemy class"""
    _monster_id: int = 12
    _name: str = "LAKITU"

    _hp: int = 124
    _fp: int = 100
    _attack: int = 45
    _defense: int = 43
    _magic_attack: int = 35
    _magic_defense: int = 40
    _speed: int = 28
    _evade: int = 13
    _magic_evade: int = 0
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 10
    _coins: int = 3
    _yoshi_cookie_item = MapleSyrupItem
    _rare_item_drop = MidMushroomItem
    _common_item_drop = MapleSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.DEEP_KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOVER_IN
    _elevate: int = 3
    _cursor_x: int = 2
    _cursor_y: int = 3
    _psychopath_message: str = " Why do people hate me?[await]"


__all__ = ["LAKITUEnemy"]
