from randomizer.data.items.items import (FrightBombItem, HoneySyrupItem, PureWaterItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class THEBIGBOOEnemy(Enemy):
    """THE BIG BOO enemy class"""
    _monster_id: int = 18
    _name: str = "THE BIG BOO"

    _hp: int = 43
    _fp: int = 12
    _attack: int = 18
    _defense: int = 0
    _magic_attack: int = 18
    _magic_defense: int = 24
    _speed: int = 17
    _evade: int = 40
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.FEAR]
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 2
    _coins: int = 0
    _yoshi_cookie_item = FrightBombItem
    _rare_item_drop = PureWaterItem
    _common_item_drop = HoneySyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 30
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.HOVER_IN
    _elevate: int = 1
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Stop staring at me![await]"

    _remake_name = "BOO"


__all__ = ["THEBIGBOOEnemy"]
