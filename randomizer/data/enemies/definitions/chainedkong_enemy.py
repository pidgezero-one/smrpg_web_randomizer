from randomizer.data.items.items import (MaxMushroomItem, PickMeUpItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class CHAINEDKONGEnemy(Enemy):
    """CHAINED KONG enemy class"""
    _monster_id: int = 102
    _name: str = "CHAINED KONG"

    _hp: int = 355
    _fp: int = 100
    _attack: int = 150
    _defense: int = 80
    _magic_attack: int = 22
    _magic_defense: int = 50
    _speed: int = 17
    _evade: int = 10
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 35
    _coins: int = 8
    _yoshi_cookie_item = PickMeUpItem
    _rare_item_drop = MaxMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.GUERRILLA
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 4
    _cursor_y: int = 6
    _psychopath_message: str = " A tad warm, isn’t it?![await]"


__all__ = ["CHAINEDKONGEnemy"]
