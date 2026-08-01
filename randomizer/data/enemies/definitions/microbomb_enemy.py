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


class MICROBOMBEnemy(Enemy):
    """MICROBOMB enemy class"""
    _monster_id: int = 184
    _name: str = "MICROBOMB"

    _hp: int = 30
    _fp: int = 100
    _attack: int = 42
    _defense: int = 30
    _magic_attack: int = 6
    _magic_defense: int = 10
    _speed: int = 15
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SPREAD_OUT_FROM_BACK
    _cursor_x: int = 1
    _cursor_y: int = 1
    _disable_auto_death: bool = True
    _psychopath_message: str = " Small is as small does.[await]"


__all__ = ["MICROBOMBEnemy"]
