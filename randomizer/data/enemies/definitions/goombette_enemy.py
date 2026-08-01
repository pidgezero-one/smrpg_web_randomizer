from randomizer.data.items.items import (MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class GOOMBETTEEnemy(Enemy):
    """GOOMBETTE enemy class"""
    _monster_id: int = 93
    _name: str = "GOOMBETTE"

    _hp: int = 100
    _fp: int = 100
    _attack: int = 90
    _defense: int = 80
    _magic_attack: int = 30
    _magic_defense: int = 30
    _speed: int = 16
    _evade: int = 20
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SPREAD_OUT_FROM_BACK
    _cursor_x: int = 1
    _cursor_y: int = 1
    _psychopath_message: str = " Me speak soft, BIG STICK![await]"

    _remake_name = "MINI GOOMBA"


__all__ = ["GOOMBETTEEnemy"]
