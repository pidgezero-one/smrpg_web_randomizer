from randomizer.data.items.items import (FlowerBoxItem, MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class BOWYEREnemy(Enemy):
    """BOWYER enemy class"""
    _monster_id: int = 230
    _name: str = "BOWYER"

    _hp: int = 720
    _fp: int = 250
    _attack: int = 50
    _defense: int = 40
    _magic_attack: int = 30
    _magic_defense: int = 35
    _speed: int = 10
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 60
    _coins: int = 50
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = FlowerBoxItem
    _common_item_drop = FlowerBoxItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 6
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " What’s with these folks?[await]"


__all__ = ["BOWYEREnemy"]
