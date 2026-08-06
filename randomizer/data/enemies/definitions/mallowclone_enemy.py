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


class MALLOWCLONEEnemy(Enemy):
    """MALLOW CLONE enemy class"""
    _monster_id: int = 157
    _name: str = "MALLOW CLONE"

    _hp: int = 150
    _fp: int = 80
    _attack: int = 80
    _defense: int = 65
    _magic_attack: int = 70
    _magic_defense: int = 80
    _speed: int = 14
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER]
    _xp: int = 60
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SPREAD_OUT_FROM_BACK
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Ma? Pa? Where are ya?[await]"


__all__ = ["MALLOWCLONEEnemy"]
