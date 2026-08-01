from randomizer.data.items.items import (AbleJuiceItem, MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class FROGOGEnemy(Enemy):
    """FROGOG enemy class"""
    _monster_id: int = 49
    _name: str = "FROGOG"

    _hp: int = 80
    _fp: int = 100
    _attack: int = 15
    _defense: int = 8
    _magic_attack: int = 0
    _magic_defense: int = 8
    _speed: int = 8
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER, Element.FIRE]
    _xp: int = 3
    _coins: int = 4
    _yoshi_cookie_item = AbleJuiceItem
    _rare_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 60
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 2
    _cursor_y: int = 6
    _psychopath_message: str = " This bright sunlight[await]\n better not fry me![await]"


__all__ = ["FROGOGEnemy"]
