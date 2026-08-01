from randomizer.data.items.items import (AbleJuiceItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class GUERRILLAEnemy(Enemy):
    """GUERRILLA enemy class"""
    _monster_id: int = 38
    _name: str = "GUERRILLA"

    _hp: int = 135
    _fp: int = 100
    _attack: int = 42
    _defense: int = 32
    _magic_attack: int = 1
    _magic_defense: int = 5
    _speed: int = 7
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.FIRE]
    _xp: int = 8
    _coins: int = 8
    _yoshi_cookie_item = AbleJuiceItem
    _rare_item_drop = AbleJuiceItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.GUERRILLA
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.LONG_JUMP
    _cursor_x: int = 4
    _cursor_y: int = 5
    _psychopath_message: str = " Don’t confuse me[await]\n with someone else![await]"


__all__ = ["GUERRILLAEnemy"]
