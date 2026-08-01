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


class WINDCRYSTALEnemy(Enemy):
    """WIND CRYSTAL enemy class"""
    _monster_id: int = 152
    _name: str = "WIND CRYSTAL"

    _hp: int = 800
    _fp: int = 250
    _attack: int = 0
    _defense: int = 200
    _magic_attack: int = 60
    _magic_defense: int = 88
    _speed: int = 30
    _evade: int = 30
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.JUMP]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 10
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 2
    _ohko_immune: bool = True
    _share_palette: bool = True
    _psychopath_message: str = " Whhhhhhooooo...[await]"


__all__ = ["WINDCRYSTALEnemy"]
