from randomizer.data.items.items import (MaxMushroomItem, MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class MACHINEMADEAxemBlackEnemy(Enemy):
    """MACHINE MADE enemy class"""
    _monster_id: int = 167
    _name: str = "MACHINE MADE"

    _hp: int = 120
    _fp: int = 100
    _attack: int = 120
    _defense: int = 110
    _magic_attack: int = 4
    _magic_defense: int = 40
    _speed: int = 55
    _evade: int = 30
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.FEAR]
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 20
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = MaxMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 30
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = " Will I make the team?[await]"


__all__ = ["MACHINEMADEAxemBlackEnemy"]
