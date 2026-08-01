from randomizer.data.items.items import (MushroomItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class JOHNNYEnemy2(Enemy):
    """JOHNNY 2 enemy class"""
    _monster_id: int = 175
    _name: str = "JOHNNY 2"

    _hp: int = 2000
    _fp: int = 200
    _attack: int = 170
    _defense: int = 50
    _magic_attack: int = 135
    _magic_defense: int = 180
    _speed: int = 255
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP]
    _resistances: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 90
    _coins: int = 50
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 3
    _cursor_y: int = 6
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Mario sure is amazing.  I'm a lucky[await]\n guy to get a rematch with him.[await]"


__all__ = ["JOHNNYEnemy2"]
