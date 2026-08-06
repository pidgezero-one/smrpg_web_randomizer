from randomizer.data.items.items import (PickMeUpItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class CLUSTEREnemy(Enemy):
    """CLUSTER enemy class"""
    _monster_id: int = 46
    _name: str = "CLUSTER"

    _hp: int = 60
    _fp: int = 100
    _attack: int = 50
    _defense: int = 50
    _magic_attack: int = 21
    _magic_defense: int = 10
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 8
    _coins: int = 8
    _yoshi_cookie_item = PickMeUpItem
    _rare_item_drop = PickMeUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 40
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.PULSAR
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 4
    _psychopath_message: str = " I’ll psyche you out![await]"


__all__ = ["CLUSTEREnemy"]
