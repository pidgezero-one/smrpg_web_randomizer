from randomizer.data.items.items import (CrystallineItem, MidMushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class MASTADOOMEnemy(Enemy):
    """MASTADOOM enemy class"""
    _monster_id: int = 62
    _name: str = "MASTADOOM"

    _hp: int = 180
    _fp: int = 100
    _attack: int = 90
    _defense: int = 65
    _magic_attack: int = 30
    _magic_defense: int = 50
    _speed: int = 3
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 20
    _coins: int = 0
    _yoshi_cookie_item = CrystallineItem
    _rare_item_drop = MidMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 100
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 4
    _cursor_y: int = 4
    _psychopath_message: str = " Phew, I’m FREEZING..[await]"


__all__ = ["MASTADOOMEnemy"]
