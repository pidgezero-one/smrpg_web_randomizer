from randomizer.data.items.items import (ElixirItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class RIBBITEEnemy(Enemy):
    """RIBBITE enemy class"""
    _monster_id: int = 113
    _name: str = "RIBBITE"

    _hp: int = 250
    _fp: int = 100
    _attack: int = 115
    _defense: int = 20
    _magic_attack: int = 31
    _magic_defense: int = 29
    _speed: int = 15
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.POISON]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 22
    _coins: int = 8
    _yoshi_cookie_item = ElixirItem
    _common_item_drop = ElixirItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 40
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 3
    _cursor_y: int = 6
    _psychopath_message: str = " My dad says, “Hello.”[await]"


__all__ = ["RIBBITEEnemy"]
