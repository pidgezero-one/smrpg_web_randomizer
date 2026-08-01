from randomizer.data.items.items import (MapleSyrupItem, PowerBlastItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class NINJAEnemy(Enemy):
    """NINJA enemy class"""
    _monster_id: int = 91
    _name: str = "NINJA"

    _hp: int = 235
    _fp: int = 100
    _attack: int = 130
    _defense: int = 76
    _magic_attack: int = 51
    _magic_defense: int = 67
    _speed: int = 28
    _evade: int = 30
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE]
    _xp: int = 32
    _coins: int = 6
    _yoshi_cookie_item = PowerBlastItem
    _common_item_drop = MapleSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 70
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 1
    _cursor_y: int = 3
    _disable_auto_death: bool = True
    _psychopath_message: str = " Wooo HOOO! I’m a FOO![await]"


__all__ = ["NINJAEnemy"]
