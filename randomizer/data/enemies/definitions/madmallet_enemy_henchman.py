from randomizer.data.items.items import (EnergizerItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class MADMALLETEnemyHenchman(Enemy):
    """MAD MALLET henchman class to not interfere with overworld enemy in factory, etc"""
    _monster_id: int = 133
    _name: str = "MAD MALLET"

    _hp: int = 200
    _fp: int = 100
    _attack: int = 120
    _defense: int = 80
    _magic_attack: int = 34
    _magic_defense: int = 85
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.THUNDER]
    _xp: int = 20
    _coins: int = 1
    _yoshi_cookie_item = EnergizerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.SMALL
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 3
    _psychopath_message: str = "[await]"


__all__ = ["MADMALLETEnemyHenchman"]
