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


class MEZZOBOMBEnemy(Enemy):
    """MEZZO BOMB enemy class"""
    _monster_id: int = 213
    _name: str = "MEZZO BOMB"

    _hp: int = 150
    _fp: int = 100
    _attack: int = 70
    _defense: int = 40
    _magic_attack: int = 0
    _magic_defense: int = 10
    _speed: int = 1
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 80
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _cursor_x: int = 3
    _cursor_y: int = 5
    _disable_auto_death: bool = True
    _psychopath_message: str = " Look out![await]"


__all__ = ["MEZZOBOMBEnemy"]
