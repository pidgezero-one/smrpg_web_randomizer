from randomizer.data.items.items import (CrystallineItem, MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class DOMINOEnemy2(Enemy):
    """DOMINO enemy class"""
    _monster_id: int = 253
    _name: str = "DOMINO"

    _hp: int = 900
    _fp: int = 250
    _attack: int = 65
    _defense: int = 80
    _magic_attack: int = 120
    _magic_defense: int = 150
    _speed: int = 25
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _xp: int = 260
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = CrystallineItem
    _common_item_drop = CrystallineItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _elevate: int = 2
    _cursor_x: int = 2
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Sh...sho...shocked![await]"


__all__ = ["DOMINOEnemy2"]
