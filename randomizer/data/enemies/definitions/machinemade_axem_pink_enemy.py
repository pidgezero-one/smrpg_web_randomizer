from randomizer.data.items.items import (MapleSyrupItem, MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class MACHINEMADEAxemPinkEnemy(Enemy):
    """MACHINE MADE enemy class"""
    _monster_id: int = 166
    _name: str = "MACHINE MADE"

    _hp: int = 100
    _fp: int = 200
    _attack: int = 95
    _defense: int = 90
    _magic_attack: int = 40
    _magic_defense: int = 100
    _speed: int = 35
    _evade: int = 25
    _magic_evade: int = 10
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP]
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.ICE]
    _xp: int = 30
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = MapleSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = " Oh! My makeup![await]"


__all__ = ["MACHINEMADEAxemPinkEnemy"]
