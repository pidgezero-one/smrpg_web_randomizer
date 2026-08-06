from randomizer.data.items.items import (RockCandyItem, SleepyBombItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class JAWFULEnemy(Enemy):
    """JAWFUL enemy class"""
    _monster_id: int = 35
    _name: str = "JAWFUL"

    _hp: int = 278
    _fp: int = 100
    _attack: int = 130
    _defense: int = 110
    _magic_attack: int = 8
    _magic_defense: int = 12
    _speed: int = 200
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.FEAR]
    _xp: int = 27
    _coins: int = 0
    _yoshi_cookie_item = RockCandyItem
    _rare_item_drop = SleepyBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 30
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 3
    _cursor_y: int = 4
    _psychopath_message: str = " Huh?[await]"


__all__ = ["JAWFULEnemy"]
