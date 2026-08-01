from randomizer.data.items.items import (BracerItem, HoneySyrupItem, RoyalSyrupItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class CRUSTYEnemy(Enemy):
    """CRUSTY enemy class"""
    _monster_id: int = 32
    _name: str = "CRUSTY"

    _hp: int = 80
    _fp: int = 100
    _attack: int = 100
    _defense: int = 100
    _magic_attack: int = 12
    _magic_defense: int = 35
    _speed: int = 6
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER, Element.FIRE]
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 25
    _coins: int = 7
    _yoshi_cookie_item = BracerItem
    _rare_item_drop = HoneySyrupItem
    _common_item_drop = RoyalSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 4
    _cursor_y: int = 4
    _psychopath_message: str = " Look at THIS![await]"


__all__ = ["CRUSTYEnemy"]
