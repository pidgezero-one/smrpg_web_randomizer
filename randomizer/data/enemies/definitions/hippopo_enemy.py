from randomizer.data.items.items import (MegalixirItem, RockCandyItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class HIPPOPOEnemy(Enemy):
    """HIPPOPO enemy class"""
    _monster_id: int = 61
    _name: str = "HIPPOPO"

    _hp: int = 400
    _fp: int = 100
    _attack: int = 150
    _defense: int = 110
    _magic_attack: int = 85
    _magic_defense: int = 53
    _speed: int = 6
    _evade: int = 0
    _magic_evade: int = 15
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 80
    _coins: int = 50
    _yoshi_cookie_item = MegalixirItem
    _common_item_drop = RockCandyItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 100
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 5
    _cursor_y: int = 4
    _psychopath_message: str = " This is a drag...[await]"


__all__ = ["HIPPOPOEnemy"]
