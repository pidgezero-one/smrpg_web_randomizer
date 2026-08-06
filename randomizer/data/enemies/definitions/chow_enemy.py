from randomizer.data.items.items import (FrightBombItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class CHOWEnemy(Enemy):
    """CHOW enemy class"""
    _monster_id: int = 80
    _name: str = "CHOW"

    _hp: int = 80
    _fp: int = 100
    _attack: int = 82
    _defense: int = 77
    _magic_attack: int = 8
    _magic_defense: int = 28
    _speed: int = 27
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.FEAR]
    _xp: int = 15
    _coins: int = 3
    _yoshi_cookie_item = FrightBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Hey, I fought you already![await]"


__all__ = ["CHOWEnemy"]
