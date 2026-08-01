from randomizer.data.items.items import (BracerItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class MAGMITEEnemy(Enemy):
    """MAGMITE enemy class"""
    _monster_id: int = 17
    _name: str = "MAGMITE"

    _hp: int = 26
    _fp: int = 100
    _attack: int = 45
    _defense: int = 70
    _magic_attack: int = 3
    _magic_defense: int = 1
    _speed: int = 2
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 5
    _coins: int = 1
    _yoshi_cookie_item = BracerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 100
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Got a thorn in my foot.[await]"


__all__ = ["MAGMITEEnemy"]
