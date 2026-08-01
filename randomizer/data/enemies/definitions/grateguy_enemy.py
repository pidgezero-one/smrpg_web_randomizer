from randomizer.data.items.items import (FlowerJarItem, MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class GRATEGUYEnemy(Enemy):
    """GRATE GUY enemy class"""
    _monster_id: int = 193
    _name: str = "GRATE GUY"

    _hp: int = 900
    _fp: int = 50
    _attack: int = 60
    _defense: int = 40
    _magic_attack: int = 25
    _magic_defense: int = 40
    _speed: int = 14
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.THUNDER]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 50
    _coins: int = 10
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = FlowerJarItem
    _common_item_drop = FlowerJarItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 6
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Peace is just a dream.[await]"


__all__ = ["GRATEGUYEnemy"]
