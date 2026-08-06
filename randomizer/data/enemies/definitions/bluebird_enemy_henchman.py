from randomizer.data.items.items import (BracerItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class BLUEBIRDEnemyHenchman(Enemy):
    """BLUEBIRD enemy class"""
    _monster_id: int = 105
    _name: str = "BLUEBIRD"

    _hp: int = 200
    _fp: int = 100
    _attack: int = 95
    _defense: int = 50
    _magic_attack: int = 80
    _magic_defense: int = 94
    _speed: int = 29
    _evade: int = 8
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.ICE]
    _xp: int = 14
    _coins: int = 6
    _yoshi_cookie_item = BracerItem
    _common_item_drop = BracerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_RIGHT
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " You are... magnificent[await]"


__all__ = ["BLUEBIRDEnemyHenchman"]
