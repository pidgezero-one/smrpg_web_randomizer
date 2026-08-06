from randomizer.data.items.items import (FlowerJarItem, MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class HAMMERBROEnemy(Enemy):
    """HAMMER BRO enemy class"""
    _monster_id: int = 27
    _name: str = "HAMMER BRO"

    _hp: int = 50
    _fp: int = 1
    _attack: int = 6
    _defense: int = 13
    _magic_attack: int = 6
    _magic_defense: int = 8
    _speed: int = 10
    _evade: int = 10
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _xp: int = 3
    _coins: int = 10
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = FlowerJarItem
    _common_item_drop = FlowerJarItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 5
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I love my hammer![await]"


__all__ = ["HAMMERBROEnemy"]
