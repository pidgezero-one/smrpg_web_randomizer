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


class JINX2Enemy(Enemy):
    """JINX 2 enemy class"""
    _monster_id: int = 196
    _name: str = "JINX 2"

    _hp: int = 800
    _fp: int = 100
    _attack: int = 160
    _defense: int = 120
    _magic_attack: int = 0
    _magic_defense: int = 90
    _speed: int = 32
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
    _psychopath_message: str = " Sympathy!? Not from me![await]"


__all__ = ["JINX2Enemy"]
