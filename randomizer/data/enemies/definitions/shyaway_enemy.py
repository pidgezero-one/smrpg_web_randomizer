from randomizer.data.items.items import (HoneySyrupItem, MapleSyrupItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class SHYAWAYEnemy(Enemy):
    """SHY AWAY enemy class"""
    _monster_id: int = 143
    _name: str = "SHY AWAY"

    _hp: int = 140
    _fp: int = 100
    _attack: int = 90
    _defense: int = 50
    _magic_attack: int = 39
    _magic_defense: int = 73
    _speed: int = 25
    _evade: int = 40
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 1
    _coins: int = 30
    _yoshi_cookie_item = MapleSyrupItem
    _rare_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_LEFT
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " La Dee Dah~ Ha Ha.[await]"

    _remake_name = "BEEZO"


__all__ = ["SHYAWAYEnemy"]
