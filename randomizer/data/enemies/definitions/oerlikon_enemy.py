from randomizer.data.items.items import (EnergizerItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class OERLIKONEnemy(Enemy):
    """OERLIKON enemy class"""
    _monster_id: int = 138
    _name: str = "OERLIKON"

    _hp: int = 85
    _fp: int = 100
    _attack: int = 120
    _defense: int = 125
    _magic_attack: int = 17
    _magic_defense: int = 50
    _speed: int = 20
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.ICE]
    _resistances: list[Element] = [Element.FIRE, Element.JUMP]
    _xp: int = 22
    _coins: int = 0
    _yoshi_cookie_item = EnergizerItem
    _rare_item_drop = EnergizerItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 50
    _morph_chance: float = 100
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.HOP_3_TIMES
    _cursor_x: int = 1
    _cursor_y: int = 2
    _psychopath_message: str = " I live to eat.[await]"

    _remake_name = "URSPIKE"


__all__ = ["OERLIKONEnemy"]
