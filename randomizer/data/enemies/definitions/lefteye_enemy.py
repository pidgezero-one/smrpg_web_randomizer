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


class LEFTEYEEnemy(Enemy):
    """LEFT EYE enemy class"""
    _monster_id: int = 191
    _name: str = "LEFT EYE"

    _hp: int = 300
    _fp: int = 200
    _attack: int = 153
    _defense: int = 130
    _magic_attack: int = 47
    _magic_defense: int = 80
    _speed: int = 21
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
    _cursor_x: int = 1
    _cursor_y: int = 2
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " I can’t see a thing![await]"


__all__ = ["LEFTEYEEnemy"]
