from randomizer.data.items.items import (MushroomItem, RoyalSyrupItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class MACHINEMADEAxemRedEnemy(Enemy):
    """MACHINE MADE enemy class"""
    _monster_id: int = 168
    _name: str = "MACHINE MADE"

    _hp: int = 180
    _fp: int = 100
    _attack: int = 135
    _defense: int = 95
    _magic_attack: int = 24
    _magic_defense: int = 80
    _speed: int = 45
    _evade: int = 10
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 50
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = RoyalSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = " Gotta fight for evil![await]"


__all__ = ["MACHINEMADEAxemRedEnemy"]
