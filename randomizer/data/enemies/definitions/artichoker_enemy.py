from randomizer.data.items.items import (FrightBombItem, MidMushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class ARTICHOKEREnemy(Enemy):
    """ARTICHOKER enemy class"""
    _monster_id: int = 58
    _name: str = "ARTICHOKER"

    _hp: int = 200
    _fp: int = 100
    _attack: int = 50
    _defense: int = 54
    _magic_attack: int = 27
    _magic_defense: int = 24
    _speed: int = 7
    _evade: int = 0
    _magic_evade: int = 20
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _resistances: list[Element] = [Element.THUNDER]
    _xp: int = 12
    _coins: int = 10
    _yoshi_cookie_item = MidMushroomItem
    _rare_item_drop = FrightBombItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 40
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 3
    _cursor_y: int = 5
    _psychopath_message: str = " Relax a little, okay?[await]"


__all__ = ["ARTICHOKEREnemy"]
