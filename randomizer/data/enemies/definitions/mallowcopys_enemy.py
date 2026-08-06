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


class MALLOWCOPYSEnemy(Enemy):
    """MALLOW COPY S enemy class"""
    _monster_id: int = 172
    _name: str = "MALLOW COPY S"

    _hp: int = 300
    _fp: int = 80
    _attack: int = 180
    _defense: int = 160
    _magic_attack: int = 190
    _magic_defense: int = 110
    _speed: int = 14
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER]
    _xp: int = 60
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SPREAD_OUT_FROM_BACK
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = "I'm afraid to go[await]\n to the bathroom at night.[await]"


__all__ = ["MALLOWCOPYSEnemy"]
