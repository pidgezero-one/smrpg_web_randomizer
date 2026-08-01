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


class GENOCLONESEnemy(Enemy):
    """GENO CLONE S enemy class"""
    _monster_id: int = 78
    _name: str = "GENO CLONE S"

    _hp: int = 500
    _fp: int = 100
    _attack: int = 220
    _defense: int = 170
    _magic_attack: int = 180
    _magic_defense: int = 60
    _speed: int = 30
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE, Element.FIRE]
    _resistances: list[Element] = [Element.ICE]
    _xp: int = 39
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SPREAD_OUT_FROM_BACK
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Truth is...[await]\nI don't care one bit about Star Pieces.[await]"


__all__ = ["GENOCLONESEnemy"]
