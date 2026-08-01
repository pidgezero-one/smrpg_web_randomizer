from randomizer.data.items.items import (MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class BELOME2Enemy(Enemy):
    """BELOME 2 enemy class"""
    _monster_id: int = 200
    _name: str = "BELOME 2"

    _hp: int = 1200
    _fp: int = 250
    _attack: int = 120
    _defense: int = 80
    _magic_attack: int = 20
    _magic_defense: int = 40
    _speed: int = 4
    _evade: int = 0
    _magic_evade: int = 25
    _status_immunities: list[Status] = [Status.SLEEP]
    _xp: int = 80
    _coins: int = 20
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.FLOPPING
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 5
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Gotta yummy in my tummy![await]"


__all__ = ["BELOME2Enemy"]
