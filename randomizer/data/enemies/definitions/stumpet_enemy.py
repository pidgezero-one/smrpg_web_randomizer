from randomizer.data.items.items import (FireBombItem, FrightBombItem, RoyalSyrupItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class STUMPETEnemy(Enemy):
    """STUMPET enemy class"""
    _monster_id: int = 55
    _name: str = "STUMPET"

    _hp: int = 500
    _fp: int = 100
    _attack: int = 200
    _defense: int = 120
    _magic_attack: int = 6
    _magic_defense: int = 60
    _speed: int = 1
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 70
    _coins: int = 15
    _yoshi_cookie_item = RoyalSyrupItem
    _rare_item_drop = FrightBombItem
    _common_item_drop = FireBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 100
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 4
    _cursor_y: int = 6
    _psychopath_message: str = " Express yourself![await]"


__all__ = ["STUMPETEnemy"]
