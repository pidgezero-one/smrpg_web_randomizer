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


class ZOMBONEEnemy(Enemy):
    """ZOMBONE enemy class"""
    _monster_id: int = 219
    _name: str = "ZOMBONE"

    _hp: int = 1800
    _fp: int = 100
    _attack: int = 190
    _defense: int = 60
    _magic_attack: int = 80
    _magic_defense: int = 100
    _speed: int = 6
    _evade: int = 0
    _magic_evade: int = 10
    _status_immunities: list[Status] = [Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.THUNDER, Element.JUMP]
    _resistances: list[Element] = [Element.ICE, Element.FIRE]
    _xp: int = 50
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.WAIT_THEN_APPEAR
    _elevate: int = 2
    _cursor_x: int = 6
    _cursor_y: int = 6
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Hey! We’re not done yet![await]"


__all__ = ["ZOMBONEEnemy"]
