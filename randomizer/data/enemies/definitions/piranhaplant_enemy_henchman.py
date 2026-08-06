from randomizer.data.items.items import (MapleSyrupItem, SleepyBombItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class PIRANHAPLANTEnemyHenchman(Enemy):
    """PIRANHA PLANT enemy class"""
    _monster_id: int = 130
    _name: str = "PIRANHA PLANT"

    _hp: int = 168
    _fp: int = 4
    _attack: int = 45
    _defense: int = 14
    _magic_attack: int = 20
    _magic_defense: int = 22
    _speed: int = 6
    _evade: int = 0
    _magic_evade: int = 0
    _resistances: list[Element] = [Element.JUMP]
    _xp: int = 5
    _coins: int = 5
    _yoshi_cookie_item = SleepyBombItem
    _common_item_drop = MapleSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = " Pretty boring nowadays.[await]"


__all__ = ["PIRANHAPLANTEnemyHenchman"]
