from randomizer.data.items.items import (BracerItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class MAGMUSEnemy(Enemy):
    """MAGMUS enemy class"""
    _monster_id: int = 81
    _name: str = "MAGMUS"

    _hp: int = 50
    _fp: int = 100
    _attack: int = 110
    _defense: int = 140
    _magic_attack: int = 3
    _magic_defense: int = 25
    _speed: int = 6
    _evade: int = 0
    _magic_evade: int = 10
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 18
    _coins: int = 3
    _yoshi_cookie_item = BracerItem
    _rare_item_drop = BracerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 100
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.SLIDE_IN
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " Clobber me for good life![await]"


__all__ = ["MAGMUSEnemy"]
