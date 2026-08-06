from randomizer.data.items.items import (HoneySyrupItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class OCTOLOTEnemy(Enemy):
    """OCTOLOT enemy class"""
    _monster_id: int = 48
    _name: str = "OCTOLOT"

    _hp: int = 99
    _fp: int = 100
    _attack: int = 38
    _defense: int = 27
    _magic_attack: int = 25
    _magic_defense: int = 30
    _speed: int = 3
    _evade: int = 10
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 6
    _coins: int = 4
    _yoshi_cookie_item = HoneySyrupItem
    _rare_item_drop = HoneySyrupItem
    _common_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.DEEP_KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_LEFT
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 6
    _psychopath_message: str = " Check out my legs![await]"


__all__ = ["OCTOLOTEnemy"]
