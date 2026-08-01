from randomizer.data.items.items import (MidMushroomItem, SleepyBombItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class APPRENTICEEnemyStatic(Enemy):
    """APPRENTICE enemy class"""
    _monster_id: int = 128
    _name: str = "APPRENTICE"

    _hp: int = 120
    _fp: int = 32
    _attack: int = 50
    _defense: int = 50
    _magic_attack: int = 20
    _magic_defense: int = 20
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 1
    _coins: int = 4
    _yoshi_cookie_item = SleepyBombItem
    _common_item_drop = MidMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.PUNCH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " I’ve had ENOUGH.[await]"


__all__ = ["APPRENTICEEnemyStatic"]
