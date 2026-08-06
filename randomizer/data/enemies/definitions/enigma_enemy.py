from randomizer.data.items.items import (EnergizerItem, MapleSyrupItem)
from randomizer.types.enemy import (Enemy)
from smrpgpatchbuilder.datatypes.enemies.enums import (
    ApproachSound,
    CoinSprite,
    EntranceStyle,
    FlowerBonusType,
    HitSound,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class ENIGMAEnemy(Enemy):
    """ENIGMA enemy class"""
    _monster_id: int = 36
    _name: str = "ENIGMA"

    _hp: int = 150
    _fp: int = 100
    _attack: int = 55
    _defense: int = 40
    _magic_attack: int = 30
    _magic_defense: int = 35
    _speed: int = 25
    _evade: int = 20
    _magic_evade: int = 0
    _weaknesses: list[Element] = [Element.JUMP]
    _xp: int = 10
    _coins: int = 5
    _yoshi_cookie_item = EnergizerItem
    _common_item_drop = MapleSyrupItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 50
    _morph_chance: float = 75
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _coin_sprite: CoinSprite = CoinSprite.BIG
    _entrance_style: EntranceStyle = EntranceStyle.DROP_FROM_ABOVE
    _elevate: int = 3
    _cursor_x: int = 2
    _cursor_y: int = 4
    _psychopath_message: str = " Gather around! Watch it![await]"


__all__ = ["ENIGMAEnemy"]
