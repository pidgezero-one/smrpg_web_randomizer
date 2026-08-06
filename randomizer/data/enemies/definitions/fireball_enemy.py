from randomizer.data.items.items import (FireBombItem, PickMeUpItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class FIREBALLEnemy(Enemy):
    """FIREBALL enemy class"""
    _monster_id: int = 72
    _name: str = "FIREBALL"

    _hp: int = 10
    _fp: int = 100
    _attack: int = 55
    _defense: int = 16
    _magic_attack: int = 30
    _magic_defense: int = 16
    _speed: int = 42
    _evade: int = 50
    _magic_evade: int = 30
    _weaknesses: list[Element] = [Element.ICE, Element.JUMP]
    _resistances: list[Element] = [Element.FIRE]
    _xp: int = 8
    _coins: int = 0
    _yoshi_cookie_item = FireBombItem
    _common_item_drop = PickMeUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 50
    _morph_chance: float = 25
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 3
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Blurb blurb blurb...[await]"

    _remake_name = "LAVA BLUBBLE"


__all__ = ["FIREBALLEnemy"]
