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


class MACHINEMADEAxemGreenEnemy(Enemy):
    """MACHINE MADE enemy class"""
    _monster_id: int = 170
    _name: str = "MACHINE MADE"

    _hp: int = 80
    _fp: int = 250
    _attack: int = 105
    _defense: int = 80
    _magic_attack: int = 80
    _magic_defense: int = 120
    _speed: int = 40
    _evade: int = 0
    _magic_evade: int = 20
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP]
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 10
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = RoyalSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = " Whew! Vertigo![await]"


__all__ = ["MACHINEMADEAxemGreenEnemy"]
