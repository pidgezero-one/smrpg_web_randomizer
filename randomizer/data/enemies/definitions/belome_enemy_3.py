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


class BELOMEEnemy3(Enemy):
    """BELOME enemy class"""
    _monster_id: int = 201
    _name: str = "BELOME 3"

    _hp: int = 4600
    _fp: int = 250
    _attack: int = 210
    _defense: int = 0
    _magic_attack: int = 140
    _magic_defense: int = 0
    _speed: int = 4
    _evade: int = 0
    _magic_evade: int = 25
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 84
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.FLOPPING
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 5
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = "My throat's all scratchy.[await]\n Life would be better if it wasn't.[await]"


__all__ = ["BELOMEEnemy3"]
