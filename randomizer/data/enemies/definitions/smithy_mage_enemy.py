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


class SMITHYMageEnemy(Enemy):
    """SMITHY enemy class"""
    _monster_id: int = 238
    _name: str = "SMITHY"

    _hp: int = 8000
    _fp: int = 250
    _attack: int = 135
    _defense: int = 50
    _magic_attack: int = 130
    _magic_defense: int = 150
    _speed: int = 35
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 3
    _cursor_x: int = 3
    _cursor_y: int = 4
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Good magic, bad defense.[await]"


__all__ = ["SMITHYMageEnemy"]
