from randomizer.data.items.items import (BadMushroomItem, SleepyBombItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class CHEWYEnemy(Enemy):
    """CHEWY enemy class"""
    _monster_id: int = 71
    _name: str = "CHEWY"

    _hp: int = 90
    _fp: int = 100
    _attack: int = 110
    _defense: int = 82
    _magic_attack: int = 70
    _magic_defense: int = 52
    _speed: int = 6
    _evade: int = 0
    _magic_evade: int = 50
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 14
    _coins: int = 0
    _yoshi_cookie_item = BadMushroomItem
    _common_item_drop = SleepyBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " I’m just a fresh flower.[await]"


__all__ = ["CHEWYEnemy"]
