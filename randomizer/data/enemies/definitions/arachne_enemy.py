from randomizer.data.items.items import (AbleJuiceItem, EnergizerItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class ARACHNEEnemy(Enemy):
    """ARACHNE enemy class"""
    _monster_id: int = 59
    _name: str = "ARACHNE"

    _hp: int = 82
    _fp: int = 100
    _attack: int = 35
    _defense: int = 35
    _magic_attack: int = 6
    _magic_defense: int = 0
    _speed: int = 14
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 6
    _coins: int = 6
    _yoshi_cookie_item = EnergizerItem
    _common_item_drop = AbleJuiceItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 3
    _cursor_y: int = 4
    _psychopath_message: str = " ♪Day-o...[await]"


__all__ = ["ARACHNEEnemy"]
