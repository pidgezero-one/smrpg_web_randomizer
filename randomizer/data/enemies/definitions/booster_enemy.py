from randomizer.data.items.items import (FlowerBoxItem, MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class BOOSTEREnemy(Enemy):
    """BOOSTER enemy class"""
    _monster_id: int = 246
    _name: str = "BOOSTER"

    _hp: int = 800
    _fp: int = 2
    _attack: int = 75
    _defense: int = 55
    _magic_attack: int = 1
    _magic_defense: int = 40
    _speed: int = 24
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.JUMP]
    _xp: int = 60
    _coins: int = 100
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = FlowerBoxItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.AMANITA_TERRAPIN
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 2
    _ohko_immune: bool = True
    _psychopath_message: str = " This is like realizing[await]\n you’re outside without[await]\n your clothes on![await]"


__all__ = ["BOOSTEREnemy"]
