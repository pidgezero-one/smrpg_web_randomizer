from randomizer.data.items.items import (MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class STRONGBOBOMB1Enemy(Enemy):
    """BOB-OMB enemy class"""
    _monster_id: int = 141
    _name: str = "BOB-OMB S"

    _hp: int = 999
    _fp: int = 100
    _attack: int = 255
    _defense: int = 68
    _magic_attack: int = 1
    _magic_defense: int = 10
    _max_shuffled_attack: int = 155
    _max_shuffled_magic_attack: int = 155
    _speed: int = 2
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 0
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _disable_auto_death: bool = True
    _psychopath_message: str = " How many times do I need to say,[await]\n “Watch out.  I'm gonna explode.”[await]\n before you get it?[await]"


__all__ = ["STRONGBOBOMB1Enemy"]
