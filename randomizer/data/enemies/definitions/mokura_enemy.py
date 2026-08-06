from randomizer.data.items.items import (KerokeroColaItem, MushroomItem, RoyalSyrupItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class MOKURAEnemy(Enemy):
    """MOKURA enemy class"""
    _monster_id: int = 148
    _name: str = "MOKURA"

    _hp: int = 620
    _fp: int = 100
    _attack: int = 120
    _defense: int = 75
    _magic_attack: int = 80
    _magic_defense: int = 90
    _speed: int = 25
    _evade: int = 20
    _magic_evade: int = 10
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: list[Element] = [Element.THUNDER, Element.JUMP]
    _xp: int = 90
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = RoyalSyrupItem
    _common_item_drop = KerokeroColaItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 2
    _ohko_immune: bool = True
    _psychopath_message: str = " Mwa ha ha...[await]"

    _remake_name = "GASSOX"


__all__ = ["MOKURAEnemy"]
