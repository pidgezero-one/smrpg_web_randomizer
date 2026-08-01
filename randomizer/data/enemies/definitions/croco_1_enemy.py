from randomizer.data.items.items import (FlowerTabItem, MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class CROCO1Enemy(Enemy):
    """CROCO 1 enemy class"""
    _monster_id: int = 240
    _name: str = "CROCO 1"

    _hp: int = 320
    _fp: int = 12
    _attack: int = 25
    _defense: int = 25
    _magic_attack: int = 30
    _magic_defense: int = 18
    _speed: int = 16
    _evade: int = 20
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.MUSHROOM, Status.SCARECROW]
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 16
    _coins: int = 10
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = FlowerTabItem
    _common_item_drop = FlowerTabItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 2
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Gosh, I’m good![await]"


__all__ = ["CROCO1Enemy"]
