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


class FAUTSOEnemy(Enemy):
    """FAUTSO enemy class"""
    _monster_id: int = 103
    _name: str = "FAUTSO"

    _hp: int = 420
    _fp: int = 100
    _attack: int = 130
    _defense: int = 100
    _magic_attack: int = 60
    _magic_defense: int = 60
    _speed: int = 14
    _evade: int = 10
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE, Element.JUMP]
    _resistances: list[Element] = [Element.THUNDER, Element.FIRE]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SPREAD_OUT_FROM_BACK
    _cursor_x: int = 3
    _cursor_y: int = 6
    _disable_auto_death: bool = True
    _psychopath_message: str = " Thanks to you I’m free![await]"

    _remake_name = "JINNIE"


__all__ = ["FAUTSOEnemy"]
