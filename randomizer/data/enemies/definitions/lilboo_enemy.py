from randomizer.data.items.items import (FreshenUpItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class LILBOOEnemy(Enemy):
    """LI’L BOO enemy class"""
    _monster_id: int = 82
    _name: str = "LI’L BOO"

    _hp: int = 66
    _fp: int = 100
    _attack: int = 120
    _defense: int = 20
    _magic_attack: int = 74
    _magic_defense: int = 120
    _speed: int = 27
    _evade: int = 50
    _magic_evade: int = 20
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 28
    _coins: int = 0
    _yoshi_cookie_item = FreshenUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.HOVER_IN
    _elevate: int = 1
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Beep pa doodle-dee!♪[await]"

    _remake_name = "HIGH BOO"


__all__ = ["LILBOOEnemy"]
