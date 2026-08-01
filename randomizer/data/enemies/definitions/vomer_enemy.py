from randomizer.data.items.items import (PureWaterItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class VOMEREnemy(Enemy):
    """VOMER enemy class"""
    _monster_id: int = 83
    _name: str = "VOMER"

    _hp: int = 0
    _fp: int = 100
    _attack: int = 110
    _defense: int = 0
    _magic_attack: int = 9
    _magic_defense: int = 0
    _speed: int = 10
    _evade: int = 0
    _magic_evade: int = 5
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 19
    _coins: int = 0
    _yoshi_cookie_item = PureWaterItem
    _rare_item_drop = PureWaterItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BONK
    _sound_on_approach: ApproachSound = ApproachSound.DRY_BONES
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 1
    _cursor_y: int = 3
    _disable_auto_death: bool = True
    _psychopath_message: str = " Nobody, NOBODY likes me.[await]"


__all__ = ["VOMEREnemy"]
