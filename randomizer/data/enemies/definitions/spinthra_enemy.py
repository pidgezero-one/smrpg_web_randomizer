from randomizer.data.items.items import (BracerItem, PowerBlastItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class SPINTHRAEnemy(Enemy):
    """SPINTHRA enemy class"""
    _monster_id: int = 123
    _name: str = "SPINTHRA"

    _hp: int = 230
    _fp: int = 100
    _attack: int = 110
    _defense: int = 70
    _magic_attack: int = 4
    _magic_defense: int = 32
    _speed: int = 19
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.POISON]
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 30
    _coins: int = 4
    _yoshi_cookie_item = PowerBlastItem
    _rare_item_drop = BracerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 3
    _cursor_y: int = 4
    _psychopath_message: str = " Oh! I’m gonna poison ya![await]"


__all__ = ["SPINTHRAEnemy"]
