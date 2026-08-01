from randomizer.data.items.items import (FlowerJarItem, MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class PANDORITEEnemy(Enemy):
    """PANDORITE enemy class"""
    _monster_id: int = 23
    _name: str = "PANDORITE"

    _hp: int = 300
    _fp: int = 50
    _attack: int = 30
    _defense: int = 20
    _magic_attack: int = 20
    _magic_defense: int = 20
    _speed: int = 1
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.JUMP]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE]
    _xp: int = 20
    _coins: int = 30
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = FlowerJarItem
    _common_item_drop = FlowerJarItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 4
    _ohko_immune: bool = True
    _psychopath_message: str = " I’m trying to sleep, OK?[await]"

    _remake_name = "HUHWHAT"


__all__ = ["PANDORITEEnemy"]
