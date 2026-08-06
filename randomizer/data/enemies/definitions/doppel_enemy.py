from randomizer.data.items.items import (PickMeUpItem, PureWaterItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class DOPPELEnemy(Enemy):
    """DOPPEL enemy class"""
    _monster_id: int = 109
    _name: str = "DOPPEL"

    _hp: int = 333
    _fp: int = 100
    _attack: int = 140
    _defense: int = 60
    _magic_attack: int = 44
    _magic_defense: int = 50
    _speed: int = 40
    _evade: int = 19
    _magic_evade: int = 0
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 40
    _coins: int = 12
    _yoshi_cookie_item = PickMeUpItem
    _rare_item_drop = PureWaterItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_RIGHT
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 5
    _psychopath_message: str = " This’s been a bad year![await]"


__all__ = ["DOPPELEnemy"]
