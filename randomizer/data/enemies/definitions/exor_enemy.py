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


class EXOREnemy(Enemy):
    """EXOR enemy class"""
    _monster_id: int = 233
    _name: str = "EXOR"

    _hp: int = 1800
    _fp: int = 0
    _attack: int = 0
    _defense: int = 120
    _magic_attack: int = 0
    _magic_defense: int = 80
    _speed: int = 200
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 100
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 3
    _cursor_x: int = 1
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Gotta mow the lawn soon.[await]"


__all__ = ["EXOREnemy"]
