from randomizer.data.items.items import (MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class GOOMBAEnemy(Enemy):
    """GOOMBA enemy class"""
    _monster_id: int = 6
    _name: str = "GOOMBA"

    _hp: int = 16
    _fp: int = 100
    _attack: int = 3
    _defense: int = 3
    _magic_attack: int = 1
    _magic_defense: int = 1
    _speed: int = 13
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 1
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Goomba gumba...phew![await]"


__all__ = ["GOOMBAEnemy"]
