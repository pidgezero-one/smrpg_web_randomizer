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


class POUNDEREnemyHenchman(Enemy):
    """Pounder henchman class to not interfere with overworld enemy in factory encounters, etc"""
    _monster_id: int = 116
    _name: str = "POUNDER"

    _hp: int = 180
    _fp: int = 100
    _attack: int = 130
    _defense: int = 70
    _magic_attack: int = 45
    _magic_defense: int = 60
    _speed: int = 25
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 24
    _coins: int = 2
    _yoshi_cookie_item = EnergizerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 40
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = "[await]"


__all__ = ["POUNDEREnemyHenchman"]
