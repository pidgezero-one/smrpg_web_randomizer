from randomizer.data.items.items import (CrystallineItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class STARCRUSTEREnemy(Enemy):
    """STAR CRUSTER enemy class"""
    _monster_id: int = 96
    _name: str = "STAR CRUSTER"

    _hp: int = 72
    _fp: int = 100
    _attack: int = 135
    _defense: int = 145
    _magic_attack: int = 16
    _magic_defense: int = 53
    _speed: int = 11
    _evade: int = 0
    _magic_evade: int = 10
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 36
    _coins: int = 30
    _yoshi_cookie_item = CrystallineItem
    _common_item_drop = CrystallineItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 4
    _cursor_y: int = 4
    _psychopath_message: str = " I’M NOT A CRAB!![await]"


__all__ = ["STARCRUSTEREnemy"]
