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


class SMILAXEnemy(Enemy):
    """SMILAX enemy class"""
    _monster_id: int = 202
    _name: str = "SMILAX"

    _hp: int = 200
    _fp: int = 100
    _attack: int = 100
    _defense: int = 80
    _magic_attack: int = 70
    _magic_defense: int = 50
    _speed: int = 5
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.FADE_IN
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 2
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Turn your eyes![await]"


__all__ = ["SMILAXEnemy"]
