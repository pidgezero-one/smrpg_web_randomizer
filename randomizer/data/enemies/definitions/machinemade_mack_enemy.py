from randomizer.data.items.items import (FireBombItem, MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class MACHINEMADEMackEnemy(Enemy):
    """MACHINE MADE enemy class"""
    _monster_id: int = 163
    _name: str = "MACHINE MADE"

    _hp: int = 300
    _fp: int = 250
    _attack: int = 160
    _defense: int = 120
    _magic_attack: int = 95
    _magic_defense: int = 40
    _speed: int = 10
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 120
    _coins: int = 30
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = FireBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _cursor_x: int = 3
    _cursor_y: int = 8
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Mario! I’m BAAAAAAAACK![await]"


__all__ = ["MACHINEMADEMackEnemy"]
