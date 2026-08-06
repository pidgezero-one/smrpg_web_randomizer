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


class WATERCRYSTALEnemy(Enemy):
    """WATER CRYSTAL enemy class"""
    _monster_id: int = 150
    _name: str = "WATER CRYSTAL"

    _hp: int = 1800
    _fp: int = 250
    _attack: int = 0
    _defense: int = 130
    _magic_attack: int = 120
    _magic_defense: int = 50
    _speed: int = 12
    _evade: int = 20
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.ICE]
    _xp: int = 30
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
    _psychopath_message: str = " Get me back underground![await]"


__all__ = ["WATERCRYSTALEnemy"]
