from randomizer.data.items.items import (MushroomItem, RockCandyItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class MACHINEMADEYaridovichEnemy(Enemy):
    """MACHINE MADE enemy class"""
    _monster_id: int = 165
    _name: str = "MACHINE MADE"

    _hp: int = 800
    _fp: int = 250
    _attack: int = 180
    _defense: int = 130
    _magic_attack: int = 90
    _magic_defense: int = 50
    _speed: int = 18
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 180
    _coins: int = 50
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = RockCandyItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 8
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " My promotion’s at stake![await]"


__all__ = ["MACHINEMADEYaridovichEnemy"]
