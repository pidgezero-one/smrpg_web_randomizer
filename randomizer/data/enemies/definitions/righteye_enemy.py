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


class RIGHTEYEEnemy(Enemy):
    """RIGHT EYE enemy class"""
    _monster_id: int = 190
    _name: str = "RIGHT EYE"

    _hp: int = 500
    _fp: int = 200
    _attack: int = 128
    _defense: int = 100
    _magic_attack: int = 82
    _magic_defense: int = 36
    _speed: int = 17
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 30
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 2
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I’ve got an astigmatism![await]"


__all__ = ["RIGHTEYEEnemy"]
