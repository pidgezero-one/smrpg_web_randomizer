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


class KNIFEGUYEnemy(Enemy):
    """KNIFE GUY enemy class"""
    _monster_id: int = 192
    _name: str = "KNIFE GUY"

    _hp: int = 700
    _fp: int = 35
    _attack: int = 70
    _defense: int = 55
    _magic_attack: int = 20
    _magic_defense: int = 10
    _speed: int = 25
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 40
    _coins: int = 15
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 4
    _cursor_y: int = 5
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Happiness is hip![await]"


__all__ = ["KNIFEGUYEnemy"]
