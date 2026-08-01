from randomizer.data.items.items import (MaxMushroomItem, RoyalSyrupItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class AMEBOIDEnemy(Enemy):
    """AMEBOID enemy class"""
    _monster_id: int = 29
    _name: str = "AMEBOID"

    _hp: int = 220
    _fp: int = 100
    _attack: int = 130
    _defense: int = 1
    _magic_attack: int = 30
    _magic_defense: int = 120
    _speed: int = 1
    _evade: int = 0
    _magic_evade: int = 50
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 10
    _coins: int = 0
    _yoshi_cookie_item = MaxMushroomItem
    _common_item_drop = RoyalSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 30
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.SPREAD_FROM_MIDDLE
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Get outta my face.[await]"


__all__ = ["AMEBOIDEnemy"]
