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


class CROCO2Enemy(Enemy):
    """CROCO 2 enemy class"""
    _monster_id: int = 241
    _name: str = "CROCO 2"

    _hp: int = 750
    _fp: int = 12
    _attack: int = 52
    _defense: int = 50
    _magic_attack: int = 27
    _magic_defense: int = 50
    _speed: int = 20
    _evade: int = 20
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.MUSHROOM, Status.SCARECROW]
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 30
    _coins: int = 50
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = FlowerBoxItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 2
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Ooh! I’m good![await]"


__all__ = ["CROCO2Enemy"]
