from randomizer.data.items.items import (EnergizerItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class POUNDETTEEnemyHenchman(Enemy):
    """POUNDETTE henchman class to not interfere with overworld enemy in factory, etc"""
    _monster_id: int = 132
    _name: str = "POUNDETTE"

    _hp: int = 150
    _fp: int = 100
    _attack: int = 140
    _defense: int = 60
    _magic_attack: int = 66
    _magic_defense: int = 45
    _speed: int = 30
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 28
    _coins: int = 3
    _yoshi_cookie_item = EnergizerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = "[await]"


__all__ = ["POUNDETTEEnemyHenchman"]
