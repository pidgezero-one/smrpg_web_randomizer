from randomizer.data.items.items import (MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class VALENTINAEnemy(Enemy):
    """VALENTINA enemy class"""
    _monster_id: int = 251
    _name: str = "VALENTINA"

    _hp: int = 2000
    _fp: int = 250
    _attack: int = 120
    _defense: int = 80
    _magic_attack: int = 80
    _magic_defense: int = 60
    _speed: int = 200
    _evade: int = 10
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.ICE]
    _xp: int = 120
    _coins: int = 200
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SLOW_DROP_FROM_ABOVE
    _elevate: int = 2
    _cursor_x: int = 3
    _cursor_y: int = 6
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I tell ya, he’s NOTHING![await]"


__all__ = ["VALENTINAEnemy"]
