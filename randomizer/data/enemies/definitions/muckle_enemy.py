from randomizer.data.items.items import (IceBombItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class MUCKLEEnemy(Enemy):
    """MUCKLE enemy class"""
    _monster_id: int = 98
    _name: str = "MUCKLE"

    _hp: int = 320
    _fp: int = 100
    _attack: int = 90
    _defense: int = 44
    _magic_attack: int = 90
    _magic_defense: int = 44
    _speed: int = 2
    _evade: int = 1
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.ICE]
    _xp: int = 6
    _coins: int = 3
    _yoshi_cookie_item = IceBombItem
    _common_item_drop = IceBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 60
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.SLAP
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOVER_IN
    _elevate: int = 2
    _cursor_x: int = 3
    _cursor_y: int = 5
    _psychopath_message: str = " Gotta know your limits.[await]"


__all__ = ["MUCKLEEnemy"]
