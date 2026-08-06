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


class CHESTEREnemy(Enemy):
    """CHESTER enemy class"""
    _monster_id: int = 139
    _name: str = "CHESTER"

    _hp: int = 1200
    _fp: int = 100
    _attack: int = 220
    _defense: int = 120
    _magic_attack: int = 120
    _magic_defense: int = 80
    _speed: int = 1
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.JUMP]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE]
    _xp: int = 150
    _coins: int = 200
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 4
    _ohko_immune: bool = True
    _psychopath_message: str = " I love my job!♥[await]"

    _remake_name = "COMEON"


__all__ = ["CHESTEREnemy"]
