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


class BAHAMUTTEnemy2(Enemy):
    """BAHAMUTT enemy class"""
    _monster_id: int = 171
    _name: str = "BAHAMUTT"

    _hp: int = 500
    _fp: int = 100
    _attack: int = 170
    _defense: int = 100
    _magic_attack: int = 80
    _magic_defense: int = 20
    _speed: int = 8
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _cursor_x: int = 3
    _cursor_y: int = 8
    _disable_auto_death: bool = True
    _psychopath_message: str = "[await]"


__all__ = ["BAHAMUTTEnemy2"]
