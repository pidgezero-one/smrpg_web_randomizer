from randomizer.data.items.items import (MushroomItem, PickMeUpItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class BOBOMBEnemyStatic(Enemy):
    """BOB-OMB enemy class"""
    _monster_id: int = 25
    _name: str = "BOB-OMB"

    _hp: int = 90
    _fp: int = 100
    _attack: int = 50
    _defense: int = 38
    _magic_attack: int = 1
    _magic_defense: int = 10
    _speed: int = 1
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 4
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _common_item_drop = PickMeUpItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 40
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 1
    _cursor_y: int = 3
    _disable_auto_death: bool = True
    _psychopath_message: str = " Ouch. HEY! Watch it![await]"


__all__ = ["BOBOMBEnemyStatic"]
