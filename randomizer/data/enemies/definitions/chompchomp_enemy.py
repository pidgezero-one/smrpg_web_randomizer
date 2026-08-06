from randomizer.data.items.items import (CrystallineItem, MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class CHOMPCHOMPEnemy(Enemy):
    """CHOMP CHOMP enemy class"""
    _monster_id: int = 86
    _name: str = "CHOMP CHOMP"

    _hp: int = 150
    _fp: int = 100
    _attack: int = 100
    _defense: int = 92
    _magic_attack: int = 14
    _magic_defense: int = 30
    _speed: int = 10
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 12
    _coins: int = 5
    _yoshi_cookie_item = MushroomItem
    _common_item_drop = CrystallineItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 3
    _psychopath_message: str = " Hey, let’s PLAY![await]"


__all__ = ["CHOMPCHOMPEnemy"]
