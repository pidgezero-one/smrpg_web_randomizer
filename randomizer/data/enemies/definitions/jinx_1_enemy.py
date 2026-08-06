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


class JINX1Enemy(Enemy):
    """JINX 1 enemy class"""
    _monster_id: int = 195
    _name: str = "JINX 1"

    _hp: int = 600
    _fp: int = 100
    _attack: int = 140
    _defense: int = 100
    _magic_attack: int = 0
    _magic_defense: int = 80
    _speed: int = 30
    _evade: int = 30
    _magic_evade: int = 25
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
    _cursor_x: int = 1
    _cursor_y: int = 1
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " You’re just a beginner![await]"


__all__ = ["JINX1Enemy"]
