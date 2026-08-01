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


class AXEMGREENEnemy(Enemy):
    """AXEM GREEN enemy class"""
    _monster_id: int = 211
    _name: str = "AXEM GREEN"

    _hp: int = 450
    _fp: int = 200
    _attack: int = 110
    _defense: int = 60
    _magic_attack: int = 90
    _magic_defense: int = 120
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 20
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP]
    _weaknesses: list[Element] = [Element.ICE]
    _xp: int = 20
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Are we done here?[await]"


__all__ = ["AXEMGREENEnemy"]
