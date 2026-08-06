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


class TENTACLESEnemy2(Enemy):
    """TENTACLES enemy class"""
    _monster_id: int = 217
    _name: str = "TENTACLES"

    _hp: int = 200
    _fp: int = 100
    _attack: int = 87
    _defense: int = 70
    _magic_attack: int = 35
    _magic_defense: int = 23
    _speed: int = 21
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP]
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.SLAP
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.READY_TO_ATTACK_2
    _cursor_x: int = 5
    _cursor_y: int = 5
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " You wouldn’t...EAT me?![await]"

    _remake_name = "TENTACLE"


__all__ = ["TENTACLESEnemy2"]
