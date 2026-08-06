from randomizer.data.items.items import (HoneySyrupItem, MegalixirItem, MidMushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class LEUKOEnemy(Enemy):
    """LEUKO enemy class"""
    _monster_id: int = 34
    _name: str = "LEUKO"

    _hp: int = 220
    _fp: int = 100
    _attack: int = 65
    _defense: int = 50
    _magic_attack: int = 42
    _magic_defense: int = 60
    _speed: int = 3
    _evade: int = 0
    _magic_evade: int = 30
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 20
    _coins: int = 3
    _yoshi_cookie_item = MegalixirItem
    _rare_item_drop = MidMushroomItem
    _common_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 60
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.SLAP
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOVER_IN
    _elevate: int = 2
    _cursor_x: int = 3
    _cursor_y: int = 5
    _psychopath_message: str = " Floating’s a bad habit.[await]"


__all__ = ["LEUKOEnemy"]
