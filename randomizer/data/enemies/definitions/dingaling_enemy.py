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


class DINGALINGEnemy(Enemy):
    """DING-A-LING enemy class"""
    _monster_id: int = 198
    _name: str = "DING-A-LING"

    _hp: int = 1200
    _fp: int = 100
    _attack: int = 180
    _defense: int = 120
    _magic_attack: int = 20
    _magic_defense: int = 50
    _speed: int = 10
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 30
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 2
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = " Wake up sleepy heads![await]"

    _remake_name = "RING-A-DING"


__all__ = ["DINGALINGEnemy"]
