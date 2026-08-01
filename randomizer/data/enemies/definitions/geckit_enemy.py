from randomizer.data.items.items import (AbleJuiceItem, EnergizerItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class GECKITEnemy(Enemy):
    """GECKIT enemy class"""
    _monster_id: int = 94
    _name: str = "GECKIT"

    _hp: int = 100
    _fp: int = 100
    _attack: int = 84
    _defense: int = 63
    _magic_attack: int = 20
    _magic_defense: int = 8
    _speed: int = 25
    _evade: int = 14
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 18
    _coins: int = 0
    _yoshi_cookie_item = EnergizerItem
    _rare_item_drop = AbleJuiceItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.PUNCH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 2
    _cursor_y: int = 2
    _psychopath_message: str = " Geck...Geck...GOCK?[await]"


__all__ = ["GECKITEnemy"]
