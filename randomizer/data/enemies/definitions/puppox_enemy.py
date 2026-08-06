from randomizer.data.items.items import (FreshenUpItem, RockCandyItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class PUPPOXEnemy(Enemy):
    """PUPPOX enemy class"""
    _monster_id: int = 117
    _name: str = "PUPPOX"

    _hp: int = 300
    _fp: int = 100
    _attack: int = 145
    _defense: int = 110
    _magic_attack: int = 20
    _magic_defense: int = 32
    _speed: int = 9
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 30
    _coins: int = 10
    _yoshi_cookie_item = RockCandyItem
    _rare_item_drop = FreshenUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 10
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 2
    _cursor_y: int = 5
    _psychopath_message: str = " What does it all MEAN?[await]"


__all__ = ["PUPPOXEnemy"]
