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


class RASPBERRYEnemy(Enemy):
    """RASPBERRY enemy class"""
    _monster_id: int = 215
    _name: str = "RASPBERRY"

    _hp: int = 600
    _fp: int = 100
    _attack: int = 70
    _defense: int = 20
    _magic_attack: int = 30
    _magic_defense: int = 30
    _speed: int = 16
    _evade: int = 0
    _magic_evade: int = 0
    _status_immunities: list[Status] = [Status.SLEEP, Status.POISON, Status.FEAR]
    _weaknesses: list[Element] = [Element.JUMP]
    _resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE]
    _xp: int = 50
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _cursor_x: int = 4
    _cursor_y: int = 5
    _ohko_immune: bool = True
    _disable_auto_death: bool = True
    _psychopath_message: str = " Congratulations![await]"


__all__ = ["RASPBERRYEnemy"]
