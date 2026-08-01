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


class SNIFITEnemyStatic(Enemy):
    """SNIFIT enemy class to not interfere with overworld enemy in tower, etc"""
    _monster_id: int = 248
    _name: str = "SNIFIT"

    _hp: int = 200
    _fp: int = 32
    _attack: int = 60
    _defense: int = 60
    _magic_attack: int = 20
    _magic_defense: int = 20
    _speed: int = 26
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 2
    _coins: int = 15
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 80
    _sound_on_hit: HitSound = HitSound.PUNCH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Minimum wage for THIS?![await]"

    _remake_name = "SNIFSTER"


__all__ = ["SNIFITEnemyStatic"]
