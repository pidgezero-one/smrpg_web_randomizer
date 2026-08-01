from randomizer.data.items.items import (CrystallineItem, FrightBombItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class CORKPEDITEEnemy(Enemy):
    """CORKPEDITE enemy class"""
    _monster_id: int = 63
    _name: str = "CORKPEDITE"

    _hp: int = 200
    _fp: int = 100
    _attack: int = 130
    _defense: int = 110
    _magic_attack: int = 80
    _magic_defense: int = 20
    _speed: int = 5
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 50
    _coins: int = 10
    _yoshi_cookie_item = CrystallineItem
    _rare_item_drop = FrightBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 60
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 4
    _cursor_y: int = 5
    _psychopath_message: str = " Off! FORGET IT![await]"

    _remake_name = "STOMPILLAR"


__all__ = ["CORKPEDITEEnemy"]
