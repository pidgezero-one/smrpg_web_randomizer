from randomizer.data.items.items import (PowerBlastItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class ARMOREDANTEnemy(Enemy):
    """ARMORED ANT enemy class"""
    _monster_id: int = 106
    _name: str = "ARMORED ANT"

    _hp: int = 230
    _fp: int = 100
    _attack: int = 130
    _defense: int = 120
    _magic_attack: int = 24
    _magic_defense: int = 80
    _speed: int = 12
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 30
    _coins: int = 5
    _yoshi_cookie_item = PowerBlastItem
    _common_item_drop = PowerBlastItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 50
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 3
    _cursor_y: int = 3
    _psychopath_message: str = " Do one good turn a day![await]"


__all__ = ["ARMOREDANTEnemy"]
