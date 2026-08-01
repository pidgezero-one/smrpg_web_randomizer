from randomizer.data.items.items import (BadMushroomItem, MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class AMANITAEnemy(Enemy):
    """AMANITA enemy class"""
    _monster_id: int = 8
    _name: str = "AMANITA"

    _hp: int = 52
    _fp: int = 100
    _attack: int = 35
    _defense: int = 30
    _magic_attack: int = 31
    _magic_defense: int = 18
    _speed: int = 12
    _evade: int = 10
    _magic_evade: int = 10
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 3
    _coins: int = 0
    _yoshi_cookie_item = BadMushroomItem
    _rare_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.AMANITA_TERRAPIN
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Gotta work on my tan![await]"


__all__ = ["AMANITAEnemy"]
