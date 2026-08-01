from randomizer.data.items.items import (MaxMushroomItem, MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class MACHINEMADEAxemYellowEnemy(Enemy):
    """MACHINE MADE enemy class"""
    _monster_id: int = 169
    _name: str = "MACHINE MADE"

    _hp: int = 200
    _fp: int = 100
    _attack: int = 140
    _defense: int = 130
    _magic_attack: int = 16
    _magic_defense: int = 20
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.POISON]
    _weaknesses: list[Element] = [Element.JUMP]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 25
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = MaxMushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 80
    _sound_on_hit: HitSound = HitSound.JAB
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _ohko_immune: bool = True
    _psychopath_message: str = " I’m STARVED![await]"


__all__ = ["MACHINEMADEAxemYellowEnemy"]
