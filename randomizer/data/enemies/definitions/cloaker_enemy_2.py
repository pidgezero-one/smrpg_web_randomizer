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


class CLOAKEREnemy2(Enemy):
    """CLOAKER enemy class"""
    _monster_id: int = 252
    _name: str = "CLOAKER"

    _hp: int = 1200
    _fp: int = 100
    _attack: int = 180
    _defense: int = 130
    _magic_attack: int = 12
    _magic_defense: int = 20
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 260
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = PowerBlastItem
    _common_item_drop = PowerBlastItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I can’t think straight![await]"


__all__ = ["CLOAKEREnemy2"]
