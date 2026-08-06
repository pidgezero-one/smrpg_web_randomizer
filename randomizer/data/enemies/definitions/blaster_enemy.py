from randomizer.data.items.items import (FrightBombItem, PickMeUpItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class BLASTEREnemy(Enemy):
    """BLASTER enemy class"""
    _monster_id: int = 37
    _name: str = "BLASTER"

    _hp: int = 120
    _fp: int = 100
    _attack: int = 70
    _defense: int = 70
    _magic_attack: int = 0
    _magic_defense: int = 10
    _speed: int = 1
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 12
    _coins: int = 0
    _yoshi_cookie_item = FrightBombItem
    _rare_item_drop = PickMeUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 60
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 3
    _psychopath_message: str = " Wanna join me?[await]"


__all__ = ["BLASTEREnemy"]
