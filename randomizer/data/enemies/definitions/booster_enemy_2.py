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


class BOOSTEREnemy2(Enemy):
    """BOOSTER enemy class"""
    _monster_id: int = 247
    _name: str = "BOOSTER 2"

    _hp: int = 3800
    _fp: int = 100
    _attack: int = 75
    _defense: int = 120
    _magic_attack: int = 1
    _magic_defense: int = 80
    _speed: int = 25
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.JUMP]
    _xp: int = 60
    _coins: int = 100
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.AMANITA_TERRAPIN
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 2
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I feel like I just knocked my prized[await]\n Impossible Grade model off the[await]\n shelf while cleaning it.[await]"


__all__ = ["BOOSTEREnemy2"]
