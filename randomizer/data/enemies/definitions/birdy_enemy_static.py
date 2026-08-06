from randomizer.data.items.items import (EnergizerItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class BIRDYEnemyStatic(Enemy):
    """BIRDY enemy class"""
    _monster_id: int = 13
    _name: str = "BIRDY"

    _hp: int = 150
    _fp: int = 100
    _attack: int = 110
    _defense: int = 75
    _magic_attack: int = 55
    _magic_defense: int = 13
    _speed: int = 23
    _evade: int = 18
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 16
    _coins: int = 3
    _yoshi_cookie_item = EnergizerItem
    _common_item_drop = EnergizerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.ZOOM_IN_FROM_RIGHT
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " I HATE Valentina.[await]"


__all__ = ["BIRDYEnemyStatic"]
