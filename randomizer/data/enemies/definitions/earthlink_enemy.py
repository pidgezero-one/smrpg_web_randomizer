from randomizer.data.items.items import (MushroomItem, PowerBlastItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class EARTHLINKEnemy(Enemy):
    """EARTH LINK enemy class"""
    _monster_id: int = 243
    _name: str = "EARTH LINK"

    _hp: int = 2500
    _fp: int = 100
    _attack: int = 220
    _defense: int = 120
    _magic_attack: int = 5
    _magic_defense: int = 10
    _speed: int = 16
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 200
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = PowerBlastItem
    _common_item_drop = PowerBlastItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 10
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " What a royal pain![await]"

    _remake_name = "BAD ADDER"


__all__ = ["EARTHLINKEnemy"]
