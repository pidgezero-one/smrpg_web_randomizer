from randomizer.data.items.items import (MapleSyrupItem, MukuCookieItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class MUKUMUKUEnemy(Enemy):
    """MUKUMUKU enemy class"""
    _monster_id: int = 177
    _name: str = "MUKUMUKU"

    _hp: int = 108
    _fp: int = 100
    _attack: int = 60
    _defense: int = 47
    _magic_attack: int = 22
    _magic_defense: int = 30
    _speed: int = 11
    _evade: int = 0
    _magic_evade: int = 80
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 8
    _coins: int = 1
    _yoshi_cookie_item = MukuCookieItem
    _rare_item_drop = MapleSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.READY_TO_ATTACK
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Ya trying to bug me?![await]"

    _remake_name = "THROPHER"


__all__ = ["MUKUMUKUEnemy"]
