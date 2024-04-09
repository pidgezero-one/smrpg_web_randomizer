"""Individual enemy class definitions."""

from typing import List, Optional, Type, Union, cast
from randomizer.types.battle_animation_scripts.ids import (
    BATTLE_EVENTS,
    BE0092_SHELLY_BREAKS,
    SUBROUTINES_0X353437,
)
from randomizer.types.battle_animation_scripts import AnimationScriptBank
from randomizer.types.battle_animation_scripts.commands import (
    SetAMEM16BitToConst,
)
from randomizer.types.enemies import (
    Enemy,
    AllyClone,
    Henchman,
    ShellySupport,
    ApproachSound,
    HitSound,
    FlowerBonusType,
)
from randomizer.types.items import RegularItem
from randomizer.types.monster_scripts import MonsterScript
from randomizer.types.monster_scripts.arguments import MONSTER_1_SET
from randomizer.types.monster_scripts.commands import (
    CallTarget,
    ClearVar,
    IfHPBelow,
    IfTurnCounterEquals,
    RunBattleEvent,
    SetTargetable,
    SetUntargetable,
)
from randomizer.types.patch import Patch
from randomizer.types.spells import Element, Status
from randomizer.types.world.flags import FixMagikoopa, NoGenoWhirlExor

from randomizer.entities.items.items import (
    AbleJuice,
    BadMushroom,
    Bracer,
    Crystalline,
    Elixir,
    Energizer,
    FireBomb,
    FlowerBox,
    FlowerJar,
    FlowerTab,
    FreshenUp,
    FrightBomb,
    FroggieDrink,
    HoneySyrup,
    IceBomb,
    KerokeroCola,
    MapleSyrup,
    MaxMushroom,
    Megalixir,
    MidMushroom,
    MukuCookie,
    Mushroom,
    PickMeUp,
    PowerBlast,
    PureWater,
    RockCandy,
    RoyalSyrup,
    SleepyBomb,
)
from randomizer.types.world.flags.flags import DifferentiateRepeatedBosses

from .palettes import CHOCOLATE_CAKE, CHOCOLATE_RASPBERRY


class Terrapin(Enemy):
    """Terrapin enemy class"""

    _monster_id: int = 0

    # vital status
    _hp: int = 10
    _fp: int = 100
    _attack: int = 1
    _defense: int = 8
    _magic_defense: int = 1
    _speed: int = 10

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # reward attributes
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK

    # misc
    _palette = 16


class Spikey(Enemy):
    """Spikey enemy class"""

    _monster_id: int = 1

    # vital status
    _hp: int = 20
    _fp: int = 100
    _attack: int = 6
    _defense: int = 11
    _magic_attack: int = 4
    _magic_defense: int = 2
    _speed: int = 14

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element nullification
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 1
    _coins: int = 2
    _common_item_drop: "Type[RegularItem]" = HoneySyrup
    _yoshi_cookie_item: "Type[RegularItem]" = Bracer

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # other properties
    _morph_chance: float = 0.75
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA

    # misc
    _palette: int = 8


class Skytroopa(Enemy):
    """Skytroopa enemy class"""

    _monster_id: int = 2

    # vital status
    _hp: int = 10
    _fp: int = 100
    _attack: int = 4
    _defense: int = 16
    _magic_attack: int = 6
    _magic_defense: int = 4
    _speed: int = 18
    _evade: int = 8

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.JUMP]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 1
    _coins: int = 1
    _rare_item_drop: "Type[RegularItem]" = Mushroom
    _yoshi_cookie_item: "Type[RegularItem]" = MidMushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 60

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA

    # misc
    _palette: int = 8
    _flying: bool = True


class MadMallet(Enemy):
    """MadMallet enemy class"""

    _monster_id: int = 3

    # vital status
    _hp: int = 200
    _fp: int = 100
    _attack: int = 120
    _defense: int = 80
    _magic_attack: int = 34
    _magic_defense: int = 85
    _speed: int = 20

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 20
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = Energizer

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK

    # misc
    _palette: int = 8


# address data may be mixed up with bandana red henchman
class MadMalletHenchman(MadMallet, Henchman):
    """MadMalletHenchman enemy class"""

    _monster_id: int = 133

    # misc
    _boss: bool = True

    # boss shuffle attributes
    _ratio_hp: float = 0.2222
    _ratio_fp: float = 0.3333
    _ratio_attack: float = 0.75
    _ratio_defense: float = 0.8
    _ratio_magic_attack: float = 0.7234
    _ratio_magic_defense: float = 1.4167
    _ratio_speed: float = 1.3333
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 0.0


class Shaman(Enemy):
    """Shaman enemy class"""

    _monster_id: int = 4

    # vital status
    _hp: int = 150
    _fp: int = 100
    _attack: int = 92
    _defense: int = 50
    _magic_attack: int = 80
    _magic_defense: int = 90
    _speed: int = 9

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 17
    _coins: int = 4
    _rare_item_drop: "Type[RegularItem]" = MapleSyrup
    _common_item_drop: "Type[RegularItem]" = RoyalSyrup
    _yoshi_cookie_item: "Type[RegularItem]" = RoyalSyrup

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 40

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK

    # misc
    _palette: int = 8


class Crook(Enemy):
    """Crook enemy class"""

    _monster_id: int = 5

    # vital status
    _hp: int = 38
    _fp: int = 100
    _attack: int = 35
    _defense: int = 32
    _magic_attack: int = 12
    _magic_defense: int = 25
    _speed: int = 22
    _evade: int = 40
    _magic_evade: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 10
    _coins: int = 10
    _rare_item_drop: "Type[RegularItem]" = HoneySyrup
    _yoshi_cookie_item: "Type[RegularItem]" = MidMushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 80

    # other properties
    _morph_chance: float = 1.0

    # misc
    _palette: int = 8


class CrookHenchman(Crook, Henchman):
    """CrookHenchman enemy class"""

    _monster_id: int = 78

    # boss shuffle attributes
    _ratio_hp: float = 38 / 750
    _ratio_fp: float = 100 / 12
    _ratio_attack: float = 35 / 52
    _ratio_defense: float = 0.64
    _ratio_magic_attack: float = 12 / 27
    _ratio_magic_defense: float = 0.5
    _ratio_speed: float = 1.1
    _ratio_evade: float = 2.0
    _ratio_magic_evade: float = 3.0


class Goomba(Enemy):
    """Goomba enemy class"""

    _monster_id: int = 6

    # vital status
    _hp: int = 16
    _fp: int = 100
    _attack: int = 3
    _defense: int = 3
    _magic_attack: int = 1
    _magic_defense: int = 1
    _speed: int = 13

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX

    # other properties
    _morph_chance: float = 1.0
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY

    # misc
    _palette: int = 8


class PiranhaPlant(Enemy):
    """PiranhaPlant enemy class"""

    _monster_id: int = 7

    # vital status
    _hp: int = 168
    _fp: int = 4
    _attack: int = 45
    _defense: int = 14
    _magic_attack: int = 20
    _magic_defense: int = 22
    _speed: int = 6

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 5
    _coins: int = 5
    _common_item_drop: "Type[RegularItem]" = MapleSyrup
    _yoshi_cookie_item: "Type[RegularItem]" = SleepyBomb

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # other properties
    _morph_chance: float = 0.75
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY

    # misc
    _palette: int = 8


class PiranhaPlantHenchman(PiranhaPlant, Henchman):
    """PiranhaPlantHenchman enemy class"""

    _monster_id: int = 131

    # boss shuffle attributes.
    # partially taken from Chewy to be closer to Megasmilax
    _ratio_hp: float = 168 / 2600
    _ratio_fp: float = 1 / 9
    _ratio_attack: float = 110 / 940
    _ratio_defense: float = 52 / 720
    _ratio_magic_attack: float = 1 / 9
    _ratio_magic_defense: float = 52 / 480
    _ratio_speed: float = 6 / 42


class Amanita(Enemy):
    """Amanita enemy class"""

    _monster_id: int = 8

    # vital status
    _hp: int = 52
    _fp: int = 100
    _attack: int = 35
    _defense: int = 30
    _magic_attack: int = 31
    _magic_defense: int = 18
    _speed: int = 12
    _evade: int = 10
    _magic_evade: int = 10

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 3
    _rare_item_drop: "Type[RegularItem]" = Mushroom
    _yoshi_cookie_item: "Type[RegularItem]" = BadMushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.AMANITA_TERRAPIN

    # misc
    _palette: int = 8


class Goby(Enemy):
    """Goby enemy class"""

    _monster_id: int = 9

    # vital status
    _hp: int = 40
    _fp: int = 100
    _attack: int = 22
    _defense: int = 14
    _magic_attack: int = 2
    _magic_defense: int = 10
    _speed: int = 12
    _evade: int = 20

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 3
    _coins: int = 2
    _common_item_drop: "Type[RegularItem]" = Mushroom
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 70

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA

    # misc
    _palette: int = 8
    _flying: bool = True
    _high_flying: bool = True


class Bloober(Enemy):
    """Bloober enemy class"""

    _monster_id: int = 10

    # vital status
    _hp: int = 130
    _fp: int = 100
    _attack: int = 80
    _defense: int = 36
    _magic_attack: int = 21
    _magic_defense: int = 16
    _speed: int = 23
    _evade: int = 20

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE, Element.THUNDER]

    # rewards
    _xp: int = 12
    _rare_item_drop: "Type[RegularItem]" = HoneySyrup
    _common_item_drop: "Type[RegularItem]" = MaxMushroom
    _yoshi_cookie_item: "Type[RegularItem]" = Elixir

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 20

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PUNCH

    # misc
    _palette: int = 8
    _flying: bool = True


class BlooberHenchman(Bloober, Henchman):
    """BlooberHenchman enemy class"""

    _monster_id: int = 172

    # boss shuffle attributes
    _ratio_hp: float = 130 / (800 + 260 + 200)
    _ratio_fp: float = 100 / (100 + 100 + 100)
    _ratio_attack: float = 80 / (100 + 82 + 87)
    _ratio_defense: float = 36 / (80 + 50 + 70)
    _ratio_magic_attack: float = 21 / (30 + 35 + 35)
    _ratio_magic_defense: float = 16 / (40 + 40 + 23)
    _ratio_speed: float = 23 / (8 + 21 + 21)


class BandanaRed(Enemy):
    """BandanaRed enemy class"""

    _monster_id: int = 11

    # vital status
    _hp: int = 120
    _fp: int = 100
    _attack: int = 78
    _defense: int = 60
    _magic_attack: int = 25
    _magic_defense: int = 25
    _speed: int = 20

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE, Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 18
    _coins: int = 10
    _rare_item_drop: "Type[RegularItem]" = Mushroom
    _yoshi_cookie_item: "Type[RegularItem]" = Energizer

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 80

    # other properties
    _morph_chance: float = 0.75
    _sound_on_hit: HitSound = HitSound.PIERCE

    # misc
    _palette: int = 8


class BandanaRedHenchman(BandanaRed, Henchman):
    """BandanaRedHenchman enemy class"""

    _monster_id: int = 130

    # boss shuffle attributes
    _ratio_hp: float = 120 / 820
    _ratio_fp: float = 1.0
    _ratio_attack: float = 78 / 85
    _ratio_defense: float = 0.75
    _ratio_magic_attack: float = 1.0
    _ratio_magic_defense: float = 25 / 60
    _ratio_speed: float = 20 / 13


class Lakitu(Enemy):
    """Lakitu enemy class"""

    _monster_id: int = 12

    # vital status
    _hp: int = 124
    _fp: int = 100
    _attack: int = 45
    _defense: int = 43
    _magic_attack: int = 35
    _magic_defense: int = 40
    _speed: int = 28
    _evade: int = 13

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [Element.THUNDER]

    # rewards
    _xp: int = 10
    _coins: int = 3
    _rare_item_drop: "Type[RegularItem]" = MidMushroom
    _common_item_drop: "Type[RegularItem]" = MapleSyrup
    _yoshi_cookie_item: "Type[RegularItem]" = MapleSyrup

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 70

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.DEEP_KNOCK

    # misc
    _palette: int = 16
    _flying: bool = True


class Birdy(Enemy):
    """Birdy enemy class"""

    _monster_id: int = 13

    # vital status
    _hp: int = 150
    _fp: int = 100
    _attack: int = 110
    _defense: int = 75
    _magic_attack: int = 55
    _magic_defense: int = 13
    _speed: int = 23
    _evade: int = 18

    # effect nullification
    _status_immunities: List[Status] = [Status.SLEEP]

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = [Element.FIRE]

    # rewards
    _xp: int = 16
    _coins: int = 3
    _common_item_drop: "Type[RegularItem]" = Energizer
    _yoshi_cookie_item: "Type[RegularItem]" = Energizer

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 70

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY

    # misc
    _palette: int = 8
    _flying: bool = True


class BirdyHenchman(Birdy, Henchman):
    """BirdyHenchman enemy class"""

    _monster_id: int = 160

    # boss shuffle attributes
    _anchor: bool = False
    _ratio_hp: float = 150 / 2400
    _ratio_fp: float = 100 / 350
    _ratio_attack: float = 110 / 260
    _ratio_defense: float = 75 / 180
    _ratio_magic_attack: float = 55 / 89
    _ratio_magic_defense: float = 13 / 120
    _ratio_evade: float = 1.8


class Pinwheel(Enemy):
    """Pinwheel enemy class"""

    _monster_id: int = 14

    # vital status
    _hp: int = 99
    _fp: int = 100
    _attack: int = 120
    _defense: int = 90
    _magic_attack: int = 70
    _magic_defense: int = 66
    _speed: int = 32
    _evade: int = 35

    # effect nullification
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [Element.THUNDER]

    # rewards
    _xp: int = 23
    _rare_item_drop: "Type[RegularItem]" = PickMeUp
    _yoshi_cookie_item: "Type[RegularItem]" = PickMeUp

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 30

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.JAB

    # misc
    _palette: int = 8


class Ratfunk(Enemy):
    """Ratfunk enemy class"""

    _monster_id: int = 15

    # vital status
    _hp: int = 32
    _fp: int = 100
    _attack: int = 20
    _defense: int = 14
    _magic_defense: int = 6
    _speed: int = 21
    _evade: int = 30

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 2
    _coins: int = 6
    _common_item_drop: "Type[RegularItem]" = AbleJuice
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 80

    # other properties
    _morph_chance: float = 1.0

    # misc
    _palette: int = 8


class K9(Enemy):
    """K9 enemy class"""

    _monster_id: int = 16

    # vital status
    _hp: int = 30
    _fp: int = 100
    _attack: int = 13
    _defense: int = 13
    _magic_attack: int = 1
    _magic_defense: int = 10
    _speed: int = 19

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = Energizer

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN

    # other properties
    _morph_chance: float = 0.75

    # misc
    _palette: int = 8


class Magmite(Enemy):
    """Magmite enemy class"""

    _monster_id: int = 17

    # vital status
    _hp: int = 26
    _fp: int = 100
    _attack: int = 45
    _defense: int = 70
    _magic_attack: int = 3
    _magic_defense: int = 1
    _speed: int = 2

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 5
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = Bracer

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 40

    # other properties
    _morph_chance: float = 0.75
    _sound_on_hit: HitSound = HitSound.KNOCK

    # misc
    _palette: int = 8


class TheBigBoo(Enemy):
    """TheBigBoo enemy class"""

    _monster_id: int = 18

    # vital status
    _hp: int = 43
    _fp: int = 12
    _attack: int = 18
    _magic_attack: int = 18
    _magic_defense: int = 24
    _speed: int = 17
    _evade: int = 40

    # effect nullification
    _status_immunities: List[Status] = [Status.FEAR]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = FrightBomb
    _common_item_drop: "Type[RegularItem]" = HoneySyrup
    _rare_item_drop: "Type[RegularItem]" = PureWater

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 10

    # other properties
    _morph_chance: float = 0.75

    # misc
    _palette: int = 8


class DryBones(Enemy):
    """DryBones enemy class"""

    _monster_id: int = 19

    # vital status
    _fp: int = 100
    _attack: int = 74
    _magic_attack: int = 7
    _speed: int = 9

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 12
    _coins: int = 5
    _rare_item_drop: "Type[RegularItem]" = PureWater
    _common_item_drop: "Type[RegularItem]" = MaxMushroom
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.BONK
    _sound_on_approach: ApproachSound = ApproachSound.DRY_BONES

    # misc
    _boss: bool = True
    _palette: int = 8


class Greaper(Enemy):
    """Greaper enemy class"""

    _monster_id: int = 20

    # vital status
    _hp: int = 148
    _fp: int = 100
    _attack: int = 72
    _defense: int = 50
    _magic_attack: int = 40
    _magic_defense: int = 20
    _speed: int = 30
    _evade: int = 30
    _magic_evade: int = 30

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 13
    _rare_item_drop: "Type[RegularItem]" = PureWater
    _common_item_drop: "Type[RegularItem]" = HoneySyrup
    _yoshi_cookie_item: "Type[RegularItem]" = HoneySyrup

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 10

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE

    # misc
    _palette: int = 8


class Sparky(Enemy):
    """Sparky enemy class"""

    _monster_id: int = 21

    # vital status
    _hp: int = 120
    _fp: int = 12
    _attack: int = 40
    _defense: int = 1
    _magic_attack: int = 38
    _magic_defense: int = 50
    _speed: int = 19
    _evade: int = 6

    # effect nullification
    _status_immunities: List[Status] = []

    # element resistances
    _resistances: List[Element] = [Element.FIRE]

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # rewards
    _xp: int = 4
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = FireBomb

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 70

    # other properties
    _morph_chance: float = 0.25
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY

    # misc
    _palette: int = 8


class Chomp(Enemy):
    """Chomp enemy class"""

    _monster_id: int = 22

    # vital status
    _hp: int = 100
    _fp: int = 100
    _attack: int = 60
    _defense: int = 65
    _magic_attack: int = 5
    _magic_defense: int = 31
    _speed: int = 10

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 10
    _common_item_drop: "Type[RegularItem]" = Mushroom
    _yoshi_cookie_item: "Type[RegularItem]" = Bracer

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # other properties
    _morph_chance: float = 0.75
    _sound_on_hit: HitSound = HitSound.CLAW

    # misc
    _palette: int = 16


class Pandorite(Enemy):
    """Pandorite enemy class"""

    _monster_id: int = 23

    # vital status
    _hp: int = 300
    _fp: int = 50
    _attack: int = 30
    _defense: int = 20
    _magic_attack: int = 20
    _magic_defense: int = 20
    _speed: int = 1

    # effect nullification
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]

    # element weaknesses
    _weaknesses: List[Element] = [Element.JUMP]

    # element resistances
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
    ]

    # special status
    _ohko_immune: bool = True

    # rewards
    _xp: int = 20
    _coins: int = 30
    _rare_item_drop: "Type[RegularItem]" = FlowerJar
    _common_item_drop: "Type[RegularItem]" = FlowerJar
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # other properties
    _sound_on_hit: HitSound = HitSound.CLAW

    # misc
    _boss: bool = True
    _palette: int = 16


class ShyRanger(Enemy):
    """ShyRanger enemy class"""

    _monster_id: int = 24

    # vital status
    _hp: int = 300
    _fp: int = 100
    _attack: int = 100
    _defense: int = 80
    _magic_attack: int = 4
    _magic_defense: int = 10
    _speed: int = 43
    _evade: int = 50

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
        Element.JUMP,
    ]

    # rewards
    _xp: int = 60
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = KerokeroCola

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 40

    # other properties
    _morph_chance: float = 0.25

    # special status
    _ohko_immune: bool = True
    _palette: int = 8


class Bobomb(Enemy):
    """Bobomb enemy class"""

    _monster_id: int = 111

    # vital status
    _hp: int = 90
    _fp: int = 100
    _attack: int = 50
    _defense: int = 38
    _magic_attack: int = 1
    _magic_defense: int = 10
    _speed: int = 1

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER, Element.JUMP]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 4
    _common_item_drop: "Type[RegularItem]" = PickMeUp
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP

    # other properties
    _sound_on_hit: HitSound = HitSound.KNOCK

    # misc
    _palette: int = 8


class BobombHenchman(Bobomb, Henchman):
    """BobombHenchman enemy class"""

    _monster_id: int = 25

    # misc
    _boss: bool = True

    # boss shuffle attributes
    _ratio_hp: float = 0.075
    _ratio_fp: float = 10.0
    _ratio_attack: float = 0.83
    _ratio_defense: float = 0.9
    _ratio_magic_attack: float = 0.05
    _ratio_magic_defense: float = 0.25
    _ratio_speed: float = 0.07
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 0.0


class Spookum(Enemy):
    """Spookum enemy class"""

    _monster_id: int = 26

    # vital status
    _hp: int = 98
    _fp: int = 100
    _attack: int = 50
    _defense: int = 45
    _magic_attack: int = 32
    _magic_defense: int = 5
    _speed: int = 18

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 8
    _coins: int = 4
    _common_item_drop: "Type[RegularItem]" = MidMushroom
    _yoshi_cookie_item: "Type[RegularItem]" = SleepyBomb

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 40

    # other properties
    _morph_chance: float = 0.75
    _sound_on_hit: HitSound = HitSound.PUNCH

    # misc
    _palette: int = 8


class HammerBro(Enemy):
    """HammerBro enemy class"""

    _monster_id: int = 27

    # vital status
    _hp: int = 50
    _fp: int = 1
    _attack: int = 6
    _defense: int = 13
    _magic_attack: int = 6
    _magic_defense: int = 8
    _speed: int = 10
    _evade: int = 10

    # rewards
    _xp: int = 3
    _coins: int = 10
    _rare_item_drop: "Type[RegularItem]" = FlowerJar
    _common_item_drop: "Type[RegularItem]" = FlowerJar
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80

    # other properties
    _sound_on_hit: HitSound = HitSound.KNOCK
    _status_immunities: List[Status] = [Status.SLEEP]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # special status
    _ohko_immune: bool = True

    # misc
    _boss: bool = True
    _palette: int = 16

    # boss shuffle attributes
    _ratio_hp: float = 0.5
    _ratio_fp: float = 0.5


class Buzzer(Enemy):
    """Buzzer enemy class"""

    _monster_id: int = 28

    # vital status
    _hp: int = 43
    _fp: int = 100
    _attack: int = 37
    _defense: int = 15
    _magic_attack: int = 4
    _magic_defense: int = 1
    _speed: int = 25
    _evade: int = 30

    # rewards
    _xp: int = 4
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 70

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER, Element.JUMP]

    # element resistances
    _resistances: List[Element] = []

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA

    # misc
    _palette: int = 8
    _flying: bool = True


class Ameboid(Enemy):
    """Ameboid enemy class"""

    _monster_id: int = 29

    # vital status
    _hp: int = 220
    _fp: int = 100
    _attack: int = 130
    _defense: int = 1
    _magic_attack: int = 30
    _magic_defense: int = 120
    _speed: int = 1
    _magic_evade: int = 50

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 10
    _common_item_drop: "Type[RegularItem]" = RoyalSyrup
    _yoshi_cookie_item: "Type[RegularItem]" = MaxMushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX

    # other properties
    _morph_chance: float = 1.0
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA

    # misc
    _palette: int = 8


class Gecko(Enemy):
    """Gecko enemy class"""

    _monster_id: int = 30

    # vital status
    _hp: int = 92
    _fp: int = 100
    _attack: int = 68
    _defense: int = 46
    _magic_attack: int = 9
    _magic_defense: int = 32
    _speed: int = 22
    _evade: int = 14

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = [Element.THUNDER]

    # rewards
    _xp: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = FroggieDrink

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PUNCH

    # misc
    _palette: int = 8


class Wiggler(Enemy):
    """Wiggler enemy class"""

    _monster_id: int = 31

    # vital status
    _hp: int = 120
    _fp: int = 100
    _attack: int = 40
    _defense: int = 25
    _magic_attack: int = 18
    _magic_defense: int = 20
    _speed: int = 10

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 6
    _coins: int = 10
    _rare_item_drop: "Type[RegularItem]" = HoneySyrup
    _yoshi_cookie_item: "Type[RegularItem]" = AbleJuice

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 80

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH

    # misc
    _palette: int = 16


class Crusty(Enemy):
    """Crusty enemy class"""

    _monster_id: int = 32

    # vital status
    _hp: int = 80
    _fp: int = 100
    _attack: int = 100
    _defense: int = 100
    _magic_attack: int = 12
    _magic_defense: int = 35
    _speed: int = 6

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER, Element.FIRE]

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 25
    _coins: int = 7
    _rare_item_drop: "Type[RegularItem]" = HoneySyrup
    _common_item_drop: "Type[RegularItem]" = RoyalSyrup
    _yoshi_cookie_item: "Type[RegularItem]" = Bracer

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # other properties
    _morph_chance: float = 0.75
    _sound_on_hit: HitSound = HitSound.CLAW

    # misc
    _palette: int = 24


class Kamek(Enemy):
    """Kamek enemy class"""

    _monster_id: int = 33

    # vital status
    _hp: int = 1600
    _fp: int = 250
    _attack: int = 100
    _defense: int = 60
    _magic_attack: int = 120
    _magic_defense: int = 100
    _speed: int = 12

    # effect nullification
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
    ]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # other properties
    _sound_on_hit: HitSound = HitSound.PIERCE

    # rewards
    _xp: int = 30
    _coins: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # special status
    _ohko_immune: bool = True

    # misc
    _boss: bool = True
    _palette: int = 16

    # boss shuffle attributes
    _ratio_hp: float = 1.0
    _ratio_fp: float = 1.0


class Leuko(Enemy):
    """Leuko enemy class"""

    _monster_id: int = 34

    # vital status
    _hp: int = 220
    _fp: int = 100
    _attack: int = 65
    _defense: int = 50
    _magic_attack: int = 42
    _magic_defense: int = 60
    _speed: int = 3
    _magic_evade: int = 30

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = [Element.THUNDER]

    # rewards
    _xp: int = 20
    _coins: int = 3
    _rare_item_drop: "Type[RegularItem]" = MidMushroom
    _common_item_drop: "Type[RegularItem]" = HoneySyrup
    _yoshi_cookie_item: "Type[RegularItem]" = Megalixir

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 60

    # other properties
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.SLAP

    # misc
    _palette: int = 16


class Jawful(Enemy):
    """Jawful enemy class"""

    _monster_id: int = 35

    # vital status
    _hp: int = 278
    _fp: int = 100
    _attack: int = 130
    _defense: int = 110
    _magic_attack: int = 8
    _magic_defense: int = 12
    _speed: int = 200

    # effect nullification
    _status_immunities: List[Status] = [Status.FEAR]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 27
    _yoshi_cookie_item: "Type[RegularItem]" = RockCandy
    _rare_item_drop: "Type[RegularItem]" = SleepyBomb

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX

    # other properties
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.CLAW

    # misc
    _palette: int = 16


class Enigma(Enemy):
    """Enigma enemy class"""

    _monster_id: int = 36
    _hp: int = 150
    _speed: int = 25
    _attack: int = 55
    _defense: int = 40
    _magic_attack: int = 30
    _magic_defense: int = 35
    _fp: int = 100
    _evade: int = 20
    _morph_chance: float = 0.75
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 100

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.JUMP]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 10
    _coins: int = 5
    _yoshi_cookie_item: "Type[RegularItem]" = Energizer
    _common_item_drop: "Type[RegularItem]" = MapleSyrup


class Blaster(Enemy):
    """Blaster enemy class"""

    _monster_id: int = 37
    _hp: int = 120
    _speed: int = 1
    _attack: int = 70
    _defense: int = 70
    _magic_defense: int = 10
    _fp: int = 100
    _morph_chance: float = 0.75
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 0

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 12
    _yoshi_cookie_item: "Type[RegularItem]" = FrightBomb
    _rare_item_drop: "Type[RegularItem]" = PickMeUp


class Guerrilla(Enemy):
    """Guerrilla enemy class"""

    _monster_id: int = 38
    _hp: int = 135
    _speed: int = 7
    _attack: int = 42
    _defense: int = 32
    _magic_attack: int = 1
    _magic_defense: int = 5
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.GUERRILLA
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 8
    _coins: int = 8
    _yoshi_cookie_item: "Type[RegularItem]" = AbleJuice
    _rare_item_drop: "Type[RegularItem]" = AbleJuice


class Babayaga(Enemy):
    """Babayaga enemy class"""

    _monster_id: int = 39
    _hp: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Hobgoblin(Enemy):
    """Hobgoblin enemy class"""

    _monster_id: int = 40
    _hp: int = 50
    _speed: int = 5
    _attack: int = 22
    _defense: int = 22
    _magic_attack: int = 8
    _magic_defense: int = 12
    _fp: int = 8
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 4
    _coins: int = 3
    _yoshi_cookie_item: "Type[RegularItem]" = PureWater
    _common_item_drop: "Type[RegularItem]" = PureWater
    _rare_item_drop: "Type[RegularItem]" = PureWater


class Reacher(Enemy):
    """Reacher enemy class"""

    _monster_id: int = 41
    _hp: int = 184
    _speed: int = 3
    _attack: int = 95
    _defense: int = 75
    _magic_attack: int = 8
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.CLAW
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 30
    _coins: int = 8
    _yoshi_cookie_item: "Type[RegularItem]" = PickMeUp
    _common_item_drop: "Type[RegularItem]" = RoyalSyrup
    _rare_item_drop: "Type[RegularItem]" = PickMeUp


class Shogun(Enemy):
    """Shogun enemy class"""

    _monster_id: int = 42
    _hp: int = 150
    _speed: int = 12
    _attack: int = 100
    _defense: int = 80
    _magic_attack: int = 1
    _magic_defense: int = 32
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.JAB
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = [
        Status.FEAR,
        Status.SLEEP,
    ]

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 24
    _coins: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = RoyalSyrup
    _rare_item_drop: "Type[RegularItem]" = PickMeUp


class Orbuser(Enemy):
    """Orbuser enemy class"""

    _monster_id: int = 43
    _hp: int = 8
    _speed: int = 15
    _attack: int = 42
    _defense: int = 80
    _magic_attack: int = 28
    _magic_defense: int = 40
    _fp: int = 20
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
    ]
    # rewards
    _xp: int = 5
    _coins: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = MapleSyrup
    _rare_item_drop: "Type[RegularItem]" = HoneySyrup


class HeavyTroopa(Enemy):
    """HeavyTroopa enemy class"""

    _monster_id: int = 44
    _hp: int = 250
    _speed: int = 3
    _attack: int = 160
    _defense: int = 100
    _magic_attack: int = 1
    _magic_defense: int = 50
    _fp: int = 100
    _evade: int = 2
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 50
    _flying: bool = True

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.JUMP]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 32
    _coins: int = 4
    _yoshi_cookie_item: "Type[RegularItem]" = Crystalline
    _common_item_drop: "Type[RegularItem]" = Crystalline


class Shadow(Enemy):
    """Shadow enemy class"""

    _monster_id: int = 45
    _hp: int = 85
    _speed: int = 18
    _attack: int = 24
    _defense: int = 5
    _magic_attack: int = 20
    _magic_defense: int = 20
    _fp: int = 14
    _evade: int = 10
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 60

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 3
    _coins: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = HoneySyrup
    _common_item_drop: "Type[RegularItem]" = PickMeUp


class Cluster(Enemy):
    """Cluster enemy class"""

    _monster_id: int = 46
    _hp: int = 60
    _speed: int = 20
    _attack: int = 50
    _defense: int = 50
    _magic_attack: int = 21
    _magic_defense: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.PULSAR
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 100

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 8
    _coins: int = 8
    _yoshi_cookie_item: "Type[RegularItem]" = PickMeUp
    _rare_item_drop: "Type[RegularItem]" = PickMeUp


class BahamuttKamek(Enemy):
    """BahamuttKamek enemy class"""

    _monster_id: int = 47
    _boss: bool = True
    _hp: int = 500
    _speed: int = 8
    _attack: int = 170
    _defense: int = 100
    _magic_attack: int = 80
    _magic_defense: int = 20
    _fp: int = 100
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.3125
    _ratio_fp: float = 0.4
    _ratio_attack: float = 1.7
    _ratio_defense: float = 1.6667
    _ratio_magic_attack: float = 0.6667
    _ratio_magic_defense: float = 0.2
    _ratio_speed: float = 0.6667
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 0.0

    _sprite: int = 699


class BahamuttChester(Enemy):
    """BahamuttChester enemy class"""

    _monster_id: int = 171
    _boss: bool = True
    _hp: int = 500
    _speed: int = 8
    _attack: int = 170
    _defense: int = 100
    _magic_attack: int = 80
    _magic_defense: int = 20
    _fp: int = 100
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 5 / 12
    _ratio_fp: float = 1.0
    _ratio_attack: float = 17 / 22
    _ratio_defense: float = 5 / 6
    _ratio_magic_attack: float = 2 / 3
    _ratio_magic_defense: float = 0.25
    _ratio_speed: float = 8.0
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 0.0


class Octolot(Enemy):
    """Octolot enemy class"""

    _monster_id: int = 48
    _hp: int = 99
    _speed: int = 3
    _attack: int = 38
    _defense: int = 27
    _magic_attack: int = 25
    _magic_defense: int = 30
    _fp: int = 100
    _evade: int = 10
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.DEEP_KNOCK
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 60

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE, Element.ICE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 6
    _coins: int = 4
    _yoshi_cookie_item: "Type[RegularItem]" = HoneySyrup
    _common_item_drop: "Type[RegularItem]" = HoneySyrup
    _rare_item_drop: "Type[RegularItem]" = HoneySyrup


class Frogog(Enemy):
    """Frogog enemy class"""

    _monster_id: int = 49
    _hp: int = 80
    _speed: int = 8
    _attack: int = 15
    _defense: int = 8
    _magic_defense: int = 8
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE, Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 3
    _coins: int = 4
    _yoshi_cookie_item: "Type[RegularItem]" = AbleJuice
    _rare_item_drop: "Type[RegularItem]" = Mushroom


class Clerk(Enemy):
    """Clerk enemy class"""

    _monster_id: int = 50
    _boss: bool = True
    _hp: int = 500
    _speed: int = 15
    _attack: int = 160
    _defense: int = 100
    _magic_attack: int = 47
    _magic_defense: int = 60
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 50
    _coins: int = 20
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _anchor: bool = True
    _ratio_hp: float = 0.5556
    _ratio_fp: float = 0.3333

    # shuffled overworld sprites
    sprite_width = 60
    sprite_height = 58

    _sprite: int = 702


class Gunyolk(Enemy):
    """Gunyolk enemy class"""

    _monster_id: int = 51
    _boss: bool = True
    _hp: int = 1500
    _speed: int = 25
    _attack: int = 200
    _defense: int = 130
    _magic_attack: int = 120
    _magic_defense: int = 80
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80
    sprite_width = 71
    sprite_height = 63

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE, Element.THUNDER]

    # element resistances
    _resistances: List[Element] = [Element.FIRE]

    # rewards
    _xp: int = 100
    _coins: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.6
    _ratio_fp: float = 0.5
    _ratio_attack: float = 1.0
    _ratio_defense: float = 1.04
    _ratio_magic_attack: float = 1.2632
    _ratio_magic_defense: float = 0.9412
    _ratio_speed: float = 0.7143

    _sprite: int = 705


class Boomer(Enemy):
    """Boomer enemy class"""

    _monster_id: int = 52
    _boss: bool = True
    _hp: int = 2000
    _speed: int = 18
    _attack: int = 200
    _defense: int = 140
    _magic_attack: int = 35
    _magic_defense: int = 26
    _fp: int = 200
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # effect nullification
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 55
    _coins: int = 9
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 1.0
    _ratio_fp: float = 1.0

    # shuffled overworld sprites
    sprite_width = 52
    sprite_width = 49

    _sprite: int = 701

    def update_world_entities(self):
        """Update Red Boomer and Blue Boomer's stats"""
        bank = self.world.monsters_attacks_and_items_animation_scripts.get_bank(
            SUBROUTINES_0X353437
        )
        for name, value in zip(
            [
                "set_boomer_red_attack",
                "set_boomer_red_defense",
                "set_boomer_red_magic_attack",
                "set_boomer_red_magic_defense",
                "set_boomer_blue_attack",
                "set_boomer_blue_defense",
                "set_boomer_blue_magic_attack",
                "set_boomer_blue_magic_defense",
            ],
            [
                self.attack,
                self.defense,
                self.magic_attack,
                self.magic_defense,
                int(round(min(self.attack * 3 / 5, 255))),
                int(round(min(self.defense * 9 / 14, 255))),
                int(round(min(self.magic_attack * 100 / 35, 255))),
                int(round(min(self.magic_defense * 45 / 13, 255))),
            ],
        ):
            cmd = bank.get_command_by_name(name)
            assert isinstance(cmd, SetAMEM16BitToConst)
            cmd.set_value(value)


class Remocon(Enemy):
    """Remocon enemy class"""

    _monster_id: int = 53
    _hp: int = 88
    _speed: int = 5
    _attack: int = 56
    _defense: int = 52
    _magic_attack: int = 25
    _magic_defense: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = [Element.ICE, Element.THUNDER]

    # rewards
    _xp: int = 8
    _coins: int = 7
    _yoshi_cookie_item: "Type[RegularItem]" = PickMeUp
    _common_item_drop: "Type[RegularItem]" = HoneySyrup


class Snapdragon(Enemy):
    """Snapdragon enemy class"""

    _monster_id: int = 54
    _hp: int = 90
    _speed: int = 4
    _attack: int = 28
    _defense: int = 25
    _magic_attack: int = 31
    _magic_defense: int = 25
    _fp: int = 100
    _morph_chance: float = 0.75
    _sound_on_hit: HitSound = HitSound.SLAP
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 4
    _coins: int = 3
    _yoshi_cookie_item: "Type[RegularItem]" = SleepyBomb
    _rare_item_drop: "Type[RegularItem]" = Mushroom


class Stumpet(Enemy):
    """Stumpet enemy class"""

    _monster_id: int = 55
    _hp: int = 500
    _speed: int = 1
    _attack: int = 200
    _defense: int = 120
    _magic_attack: int = 6
    _magic_defense: int = 60
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80

    # rewards
    _xp: int = 70
    _coins: int = 15
    _yoshi_cookie_item: "Type[RegularItem]" = RoyalSyrup
    _common_item_drop: "Type[RegularItem]" = FireBomb
    _rare_item_drop: "Type[RegularItem]" = FrightBomb


class Dodo(Enemy):
    """Dodo enemy class"""

    _monster_id: int = 56
    _boss: bool = True
    _hp: int = 1000
    _speed: int = 10
    _attack: int = 140
    _defense: int = 100
    _magic_attack: int = 9
    _magic_defense: int = 60
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
    ]
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 2

    # rewards
    _xp: int = 40
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.4167
    _ratio_fp: float = 0.2857
    _ratio_attack: float = 1.1667
    _ratio_defense: float = 1.25
    _ratio_magic_attack: float = 0.1125
    _ratio_magic_defense: float = 1.0
    _ratio_speed: float = 0.05
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 1.0

    _sprite: int = 696

    def update_world_entities(self):
        monsterscript: MonsterScript = self.world.monster_scripts.scripts[
            self.monster_id
        ]

        # update dodo's HP
        _, command = monsterscript.get_command_by_name("dodo_solo_ends")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.6))


class Jester(Enemy):
    """Jester enemy class"""

    _monster_id: int = 57
    _boss: bool = True
    _hp: int = 151
    _speed: int = 20
    _attack: int = 48
    _defense: int = 35
    _magic_attack: int = 22
    _magic_defense: int = 35
    _fp: int = 12
    _magic_evade: int = 80
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 10
    _coins: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = HoneySyrup


class Artichoker(Enemy):
    """Artichoker enemy class"""

    _monster_id: int = 58
    _hp: int = 200
    _speed: int = 7
    _attack: int = 50
    _defense: int = 54
    _magic_attack: int = 27
    _magic_defense: int = 24
    _fp: int = 100
    _magic_evade: int = 20
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE, Element.JUMP]

    # element resistances
    _resistances: List[Element] = [Element.THUNDER]

    # rewards
    _xp: int = 12
    _coins: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = MidMushroom
    _rare_item_drop: "Type[RegularItem]" = FrightBomb


class Arachne(Enemy):
    """Arachne enemy class"""

    _monster_id: int = 59
    _hp: int = 82
    _speed: int = 14
    _attack: int = 35
    _defense: int = 35
    _magic_attack: int = 6
    _fp: int = 100
    _morph_chance: float = 0.75
    _sound_on_hit: HitSound = HitSound.CLAW
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 6
    _coins: int = 6
    _yoshi_cookie_item: "Type[RegularItem]" = Energizer
    _common_item_drop: "Type[RegularItem]" = AbleJuice


class Carriboscis(Enemy):
    """Carriboscis enemy class"""

    _monster_id: int = 60
    _hp: int = 90
    _speed: int = 30
    _attack: int = 55
    _defense: int = 44
    _magic_attack: int = 28
    _magic_defense: int = 22
    _fp: int = 100
    _evade: int = 13
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 60

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE, Element.JUMP]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 10
    _coins: int = 4
    _yoshi_cookie_item: "Type[RegularItem]" = HoneySyrup
    _rare_item_drop: "Type[RegularItem]" = AbleJuice


class Hippopo(Enemy):
    """Hippopo enemy class"""

    _monster_id: int = 61
    _hp: int = 400
    _speed: int = 6
    _attack: int = 150
    _defense: int = 110
    _magic_attack: int = 85
    _magic_defense: int = 53
    _fp: int = 100
    _magic_evade: int = 15
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.SMASH
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 80
    _one_per_battle: bool = True

    # effect nullification
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 80
    _coins: int = 50
    _yoshi_cookie_item: "Type[RegularItem]" = Megalixir
    _common_item_drop: "Type[RegularItem]" = RockCandy


class Mastadoom(Enemy):
    """Mastadoom enemy class"""

    _monster_id: int = 62
    _hp: int = 180
    _speed: int = 3
    _attack: int = 90
    _defense: int = 65
    _magic_attack: int = 30
    _magic_defense: int = 50
    _fp: int = 100
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.SMASH
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _resistances: List[Element] = [Element.THUNDER]

    # element resistances
    _weaknesses: List[Element] = [Element.FIRE]

    # rewards
    _xp: int = 20
    _yoshi_cookie_item: "Type[RegularItem]" = Crystalline
    _rare_item_drop: "Type[RegularItem]" = MidMushroom


class Corkpedite(Enemy):
    """Corkpedite enemy class"""

    _monster_id: int = 63
    _hp: int = 200
    _speed: int = 5
    _attack: int = 130
    _defense: int = 110
    _magic_attack: int = 80
    _magic_defense: int = 20
    _fp: int = 100
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.SMASH
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # rewards
    _xp: int = 50
    _coins: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = Crystalline
    _rare_item_drop: "Type[RegularItem]" = FrightBomb


class Terracotta(Enemy):
    """Terracotta enemy class"""

    _monster_id: int = 64
    _hp: int = 180
    _speed: int = 23
    _attack: int = 120
    _defense: int = 85
    _magic_attack: int = 36
    _magic_defense: int = 35
    _fp: int = 100
    _morph_chance: float = 1.0
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [Element.FIRE]

    # rewards
    _xp: int = 25
    _yoshi_cookie_item: "Type[RegularItem]" = MidMushroom
    _rare_item_drop: "Type[RegularItem]" = Mushroom


class Spikester(Enemy):
    """Spikester enemy class"""

    _monster_id: int = 65
    _hp: int = 50
    _speed: int = 19
    _attack: int = 48
    _defense: int = 60
    _magic_attack: int = 12
    _magic_defense: int = 4
    _fp: int = 100
    _morph_chance: float = 0.75
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 6
    _coins: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = Bracer


class Malakoopa(Enemy):
    """Malakoopa enemy class"""

    _monster_id: int = 66
    _hp: int = 95
    _speed: int = 35
    _attack: int = 130
    _defense: int = 120
    _magic_attack: int = 47
    _magic_defense: int = 98
    _fp: int = 100
    _evade: int = 20
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 60
    _flying: bool = True

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 23
    _coins: int = 3
    _yoshi_cookie_item: "Type[RegularItem]" = MapleSyrup
    _rare_item_drop: "Type[RegularItem]" = HoneySyrup


class Pounder(Enemy):
    """Pounder enemy class"""

    _monster_id: int = 67
    _hp: int = 180
    _speed: int = 25
    _attack: int = 130
    _defense: int = 70
    _magic_attack: int = 45
    _magic_defense: int = 60
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 24
    _coins: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = Energizer


class PounderHenchman(Pounder):
    """PounderHenchman enemy class"""

    _monster_id: int = 116

    # misc
    _boss: bool = True

    # boss shuffle attributes
    _ratio_hp: float = 0.1343
    _ratio_fp: float = 0.25
    _ratio_attack: float = 1.0
    _ratio_defense: float = 0.6364
    _ratio_magic_attack: float = 0.75
    _ratio_magic_defense: float = 0.8571
    _ratio_speed: float = 1.0
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 0.0


class Poundette(Enemy):
    """Poundette enemy class"""

    _monster_id: int = 68
    _hp: int = 150
    _speed: int = 30
    _attack: int = 140
    _defense: int = 60
    _magic_attack: int = 66
    _magic_defense: int = 45
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 28
    _coins: int = 3
    _yoshi_cookie_item: "Type[RegularItem]" = Energizer


class PoundetteHenchman(Poundette):
    """PoundetteHenchman enemy class"""

    _monster_id: int = 132

    # misc
    _boss: bool = True

    # boss shuffle attributes
    _ratio_hp: float = 0.0938
    _ratio_fp: float = 0.2
    _ratio_attack: float = 0.7368
    _ratio_defense: float = 0.5
    _ratio_magic_attack: float = 1.1579
    _ratio_magic_defense: float = 0.5625
    _ratio_speed: float = 0.8571
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 0.0


class Sackit(Enemy):
    """Sackit enemy class"""

    _monster_id: int = 69
    _hp: int = 152
    _speed: int = 26
    _attack: int = 70
    _defense: int = 53
    _magic_attack: int = 13
    _magic_defense: int = 20
    _fp: int = 100
    _evade: int = 20
    _morph_chance: float = 1.0
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 20
    _coins: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = MaxMushroom
    _common_item_drop: "Type[RegularItem]" = RoyalSyrup
    _rare_item_drop: "Type[RegularItem]" = MaxMushroom


class GuGoomba(Enemy):
    """GuGoomba enemy class"""

    _monster_id: int = 70
    _hp: int = 132
    _speed: int = 14
    _attack: int = 115
    _defense: int = 66
    _magic_attack: int = 13
    _magic_defense: int = 66
    _fp: int = 100
    _magic_evade: int = 50
    _morph_chance: float = 1.0
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 15
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = FroggieDrink
    _rare_item_drop: "Type[RegularItem]" = MaxMushroom


class Chewy(Enemy):
    """Chewy enemy class"""

    _monster_id: int = 71
    _hp: int = 90
    _speed: int = 6
    _attack: int = 110
    _defense: int = 82
    _magic_attack: int = 70
    _magic_defense: int = 52
    _fp: int = 100
    _magic_evade: int = 50
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # effect nullification
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 14
    _yoshi_cookie_item: "Type[RegularItem]" = BadMushroom
    _common_item_drop: "Type[RegularItem]" = SleepyBomb


class Fireball(Enemy):
    """Fireball enemy class"""

    _monster_id: int = 72
    _hp: int = 10
    _speed: int = 42
    _attack: int = 55
    _defense: int = 16
    _magic_attack: int = 30
    _magic_defense: int = 16
    _fp: int = 100
    _evade: int = 50
    _magic_evade: int = 30
    _morph_chance: float = 0.25
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 30

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE, Element.JUMP]

    # element resistances
    _resistances: List[Element] = [Element.FIRE]

    # rewards
    _xp: int = 8
    _yoshi_cookie_item: "Type[RegularItem]" = FireBomb
    _common_item_drop: "Type[RegularItem]" = PickMeUp


class MrKipper(Enemy):
    """MrKipper enemy class"""

    _monster_id: int = 73
    _hp: int = 133
    _speed: int = 23
    _attack: int = 75
    _defense: int = 45
    _magic_attack: int = 14
    _magic_defense: int = 10
    _fp: int = 100
    _evade: int = 13
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 70
    _flying: bool = True
    _high_flying: bool = True

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER, Element.ICE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 8
    _coins: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _common_item_drop: "Type[RegularItem]" = AbleJuice


class FactoryChief(Enemy):
    """FactoryChief enemy class"""

    _monster_id: int = 74
    _boss: bool = True
    _hp: int = 1000
    _speed: int = 45
    _attack: int = 200
    _defense: int = 120
    _magic_attack: int = 70
    _magic_defense: int = 90
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # rewards
    _xp: int = 80
    _coins: int = 90
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # boss shuffle attributes
    _ratio_hp: float = 0.4
    _ratio_fp: float = 0.5
    _ratio_attack: float = 1.0
    _ratio_defense: float = 0.96
    _ratio_magic_attack: float = 0.7368
    _ratio_magic_defense: float = 1.0588
    _ratio_speed: float = 1.2857


class BandanaBlue(Henchman):
    """BandanaBlue enemy class"""

    _monster_id: int = 75
    _boss: bool = True
    _hp: int = 150
    _speed: int = 30
    _attack: int = 80
    _defense: int = 60
    _magic_attack: int = 20
    _magic_defense: int = 30
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER, Element.FIRE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 20
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.1829
    _ratio_fp: float = 1.0
    _ratio_attack: float = 0.9412
    _ratio_defense: float = 0.75
    _ratio_magic_attack: float = 0.8
    _ratio_magic_defense: float = 0.5
    _ratio_speed: float = 2.3077


class Manager(Enemy):
    """Manager enemy class"""

    _monster_id: int = 76
    _boss: bool = True
    _hp: int = 800
    _speed: int = 25
    _attack: int = 170
    _defense: int = 110
    _magic_attack: int = 60
    _magic_defense: int = 70
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 60
    _coins: int = 40
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _anchor: bool = True
    _ratio_hp: float = 0.597
    _ratio_fp: float = 0.25
    _ratio_attack: float = 1.3077
    _ratio_defense: float = 1.0
    _ratio_magic_attack: float = 1.0
    _ratio_magic_defense: float = 1.0
    _ratio_speed: float = 1.0

    _sprite: int = 703


class Bluebird(Enemy):
    """Bluebird enemy class"""

    _monster_id: int = 77
    _hp: int = 200
    _speed: int = 29
    _attack: int = 95
    _defense: int = 50
    _magic_attack: int = 80
    _magic_defense: int = 94
    _fp: int = 100
    _evade: int = 8
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _resistances: List[Element] = [Element.ICE]
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [Status.SLEEP]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 100
    _flying: bool = True

    # rewards
    _xp: int = 14
    _coins: int = 6
    _yoshi_cookie_item: "Type[RegularItem]" = Bracer
    _common_item_drop: "Type[RegularItem]" = Bracer


class BluebirdHenchman(Bluebird, Henchman):
    """BluebirdHenchman enemy class"""

    _monster_id: int = 141

    # boss shuffle attributes
    _anchor: bool = False
    _ratio_hp: float = 200 / 2400
    _ratio_fp: float = 100 / 350
    _ratio_attack: float = 95 / 260
    _ratio_defense: float = 50 / 180
    _ratio_magic_attack: float = 80 / 89
    _ratio_magic_defense: float = 94 / 120
    _ratio_evade: float = 0.8

    # rewards
    _xp: int = 14
    _coins: int = 6
    _yoshi_cookie_item: "Type[RegularItem]" = Bracer
    _common_item_drop: "Type[RegularItem]" = Bracer


class AlleyRat(Enemy):
    """AlleyRat enemy class"""

    _monster_id: int = 79
    _hp: int = 105
    _speed: int = 21
    _attack: int = 70
    _defense: int = 55
    _magic_attack: int = 13
    _magic_defense: int = 12
    _fp: int = 100
    _evade: int = 15
    _morph_chance: float = 1.0
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 40

    # rewards
    _xp: int = 9
    _coins: int = 3
    _yoshi_cookie_item: "Type[RegularItem]" = AbleJuice
    _rare_item_drop: "Type[RegularItem]" = Mushroom

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []


class Chow(Enemy):
    """Chow enemy class"""

    _monster_id: int = 80
    _hp: int = 80
    _speed: int = 27
    _attack: int = 82
    _defense: int = 77
    _magic_attack: int = 8
    _magic_defense: int = 28
    _fp: int = 100
    _morph_chance: float = 1.0
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.FEAR,
    ]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 15
    _coins: int = 3
    _yoshi_cookie_item: "Type[RegularItem]" = FrightBomb


class Magmus(Enemy):
    """Magmus enemy class"""

    _monster_id: int = 81
    _hp: int = 50
    _speed: int = 6
    _attack: int = 110
    _defense: int = 140
    _magic_attack: int = 3
    _magic_defense: int = 25
    _fp: int = 100
    _magic_evade: int = 10
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _resistances: List[Element] = [Element.FIRE, Element.JUMP]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 40

    # rewards
    _xp: int = 18
    _coins: int = 3
    _yoshi_cookie_item: "Type[RegularItem]" = Bracer
    _rare_item_drop: "Type[RegularItem]" = Bracer


class LilBoo(Enemy):
    """LilBoo enemy class"""

    _monster_id: int = 82
    _hp: int = 66
    _speed: int = 27
    _attack: int = 120
    _defense: int = 20
    _magic_attack: int = 74
    _magic_defense: int = 120
    _fp: int = 100
    _evade: int = 50
    _magic_evade: int = 20
    _morph_chance: float = 1.0
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 10

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 28
    _yoshi_cookie_item: "Type[RegularItem]" = FreshenUp


class Vomer(Enemy):
    """Vomer enemy class"""

    _monster_id: int = 83
    _boss: bool = True
    _speed: int = 10
    _attack: int = 110
    _magic_attack: int = 9
    _fp: int = 100
    _magic_evade: int = 5
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.BONK
    _sound_on_approach: ApproachSound = ApproachSound.DRY_BONES

    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # effect nullification
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 19
    _yoshi_cookie_item: "Type[RegularItem]" = PureWater
    _rare_item_drop: "Type[RegularItem]" = PureWater


class GlumReaper(Enemy):
    """GlumReaper enemy class"""

    _monster_id: int = 84
    _hp: int = 180
    _speed: int = 35
    _attack: int = 120
    _defense: int = 55
    _magic_attack: int = 60
    _magic_defense: int = 80
    _fp: int = 100
    _evade: int = 20
    _magic_evade: int = 10
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 50

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 35
    _coins: int = 3
    _yoshi_cookie_item: "Type[RegularItem]" = PureWater
    _common_item_drop: "Type[RegularItem]" = PureWater


class Pyrosphere(Enemy):
    """Pyrosphere enemy class"""

    _monster_id: int = 85
    _hp: int = 167
    _speed: int = 24
    _attack: int = 105
    _defense: int = 66
    _magic_attack: int = 100
    _magic_defense: int = 48
    _fp: int = 100
    _evade: int = 7
    _morph_chance: float = 0.25
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [Status.POISON]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 70

    # rewards
    _xp: int = 17
    _coins: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = FireBomb


class PyrosphereHenchman(Pyrosphere, Henchman):
    """PyrosphereHenchman enemy class"""

    _monster_id: int = 183

    # boss shuffle attributes
    _anchor: bool = False
    _ratio_hp: float = 167 / 3200
    _ratio_fp: float = 0.5
    _ratio_attack: float = 105 / 350
    _ratio_defense: float = 66 / 160
    _ratio_magic_attack: float = 100 / 200
    _ratio_magic_defense: float = 48 / 170
    _ratio_speed: float = 24 / 26
    _ratio_evade: float = 0.35

    # rewards
    _xp: int = 17
    _coins: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = FireBomb


class ChompChomp(Enemy):
    """ChompChomp enemy class"""

    _monster_id: int = 86
    _hp: int = 150
    _speed: int = 10
    _attack: int = 100
    _defense: int = 92
    _magic_attack: int = 14
    _magic_defense: int = 30
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.CLAW
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 12
    _coins: int = 5
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _common_item_drop: "Type[RegularItem]" = Crystalline


class Hidon(Enemy):
    """Hidon enemy class"""

    _monster_id: int = 87
    _boss: bool = True
    _hp: int = 600
    _speed: int = 1
    _attack: int = 110
    _defense: int = 90
    _magic_attack: int = 60
    _magic_defense: int = 30
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
    ]
    _weaknesses: List[Element] = [Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # rewards
    # xp = 50
    _xp: int = 42
    _coins: int = 100
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 1.0
    _ratio_fp: float = 1.0


class SlingShy(Enemy):
    """SlingShy enemy class"""

    _monster_id: int = 88
    _hp: int = 120
    _speed: int = 16
    _attack: int = 108
    _defense: int = 80
    _magic_attack: int = 42
    _magic_defense: int = 21
    _fp: int = 100
    _morph_chance: float = 1.0
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 80

    # rewards
    _xp: int = 3
    _coins: int = 20
    _yoshi_cookie_item: "Type[RegularItem]" = MapleSyrup
    _rare_item_drop: "Type[RegularItem]" = HoneySyrup

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []


class Robomb(Enemy):
    """Robomb enemy class"""

    _monster_id: int = 89
    _hp: int = 42
    _speed: int = 2
    _attack: int = 54
    _defense: int = 63
    _magic_attack: int = 1
    _magic_defense: int = 20
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE, Element.JUMP]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 6
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = PickMeUp
    _common_item_drop: "Type[RegularItem]" = PickMeUp


class ShyGuy(Enemy):
    """ShyGuy enemy class"""

    _monster_id: int = 90
    _hp: int = 78
    _speed: int = 14
    _attack: int = 29
    _defense: int = 30
    _magic_attack: int = 20
    _magic_defense: int = 6
    _fp: int = 100
    _evade: int = 10
    _morph_chance: float = 1.0
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 2
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = HoneySyrup


class ShyGuyHenchman(ShyGuy, Henchman):
    """ShyGuyHenchman enemy class"""

    _monster_id: int = 185

    # boss shuffle attributes
    # Taken from Sling Shy for closer match
    _anchor: bool = False
    _ratio_hp: float = 0.06
    _ratio_fp: float = 0.5
    _ratio_attack: float = 0.54
    _ratio_defense: float = 4 / 7
    _ratio_magic_attack: float = 1.2
    _ratio_magic_defense: float = 21 / 26
    _ratio_speed: float = 8 / 9
    _ratio_evade: float = 0
    _ratio_magic_evade: float = 0.0

    # rewards
    _xp: int = 2
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = HoneySyrup


class Ninja(Enemy):
    """Ninja enemy class"""

    _monster_id: int = 91
    _boss: bool = True
    _hp: int = 235
    _speed: int = 28
    _attack: int = 130
    _defense: int = 76
    _magic_attack: int = 51
    _magic_defense: int = 67
    _fp: int = 100
    _evade: int = 30
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.PIERCE
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [
        Element.ICE,
        Element.FIRE,
        Element.THUNDER,
    ]

    # rewards
    _xp: int = 32
    _coins: int = 6
    _yoshi_cookie_item: "Type[RegularItem]" = PowerBlast
    _common_item_drop: "Type[RegularItem]" = MapleSyrup


class Stinger(Enemy):
    """Stinger enemy class"""

    _monster_id: int = 92
    _hp: int = 65
    _speed: int = 33
    _attack: int = 78
    _defense: int = 80
    _magic_attack: int = 23
    _magic_defense: int = 10
    _fp: int = 100
    _evade: int = 25
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 70
    _flying: bool = True

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 13
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = AbleJuice
    _rare_item_drop: "Type[RegularItem]" = AbleJuice


class Goombette(Henchman):
    """Goombette enemy class"""

    _monster_id: int = 93
    _boss: bool = True
    _hp: int = 100
    _speed: int = 16
    _attack: int = 90
    _defense: int = 80
    _magic_attack: int = 30
    _magic_defense: int = 30
    _fp: int = 100
    _evade: int = 20
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    # made this up
    _xp: int = 2

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = []

    # boss shuffle attributes
    _ratio_hp: float = 0.1667
    _ratio_fp: float = 1.0
    _ratio_attack: float = 0.8182
    _ratio_defense: float = 0.8889
    _ratio_magic_attack: float = 0.5
    _ratio_magic_defense: float = 1.0
    _ratio_speed: float = 16.0
    _ratio_evade: float = 1.0
    _ratio_magic_evade: float = 0.0


class Geckit(Enemy):
    """Geckit enemy class"""

    _monster_id: int = 94
    _hp: int = 100
    _speed: int = 25
    _attack: int = 84
    _defense: int = 63
    _magic_attack: int = 20
    _magic_defense: int = 8
    _fp: int = 100
    _evade: int = 14
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PUNCH
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = [Element.FIRE]

    # rewards
    _xp: int = 18
    _yoshi_cookie_item: "Type[RegularItem]" = Energizer
    _rare_item_drop: "Type[RegularItem]" = AbleJuice


class Jabit(Enemy):
    """Jabit enemy class"""

    _monster_id: int = 95
    _hp: int = 150
    _speed: int = 13
    _attack: int = 120
    _defense: int = 95
    _magic_attack: int = 27
    _magic_defense: int = 34
    _fp: int = 100
    _morph_chance: float = 1.0
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 18
    _yoshi_cookie_item: "Type[RegularItem]" = Bracer
    _common_item_drop: "Type[RegularItem]" = PickMeUp


class Starcruster(Enemy):
    """Starcruster enemy class"""

    _monster_id: int = 96
    _hp: int = 72
    _speed: int = 11
    _attack: int = 135
    _defense: int = 145
    _magic_attack: int = 16
    _magic_defense: int = 53
    _fp: int = 100
    _magic_evade: int = 10
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.CLAW
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 36
    _coins: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = Crystalline
    _common_item_drop: "Type[RegularItem]" = Crystalline


class Merlin(Enemy):
    """Merlin enemy class"""

    _monster_id: int = 97
    _boss: bool = True
    _hp: int = 169
    _speed: int = 20
    _attack: int = 124
    _defense: int = 63
    _magic_attack: int = 90
    _magic_defense: int = 130
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 50
    _coins: int = 20
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Muckle(Enemy):
    """Muckle enemy class"""

    _monster_id: int = 98
    _boss: bool = True
    _hp: int = 320
    _speed: int = 2
    _attack: int = 90
    _defense: int = 44
    _magic_attack: int = 90
    _magic_defense: int = 44
    _fp: int = 100
    _evade: int = 1
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.SLAP
    _resistances: List[Element] = [Element.ICE]
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 60

    # rewards
    _xp: int = 6
    _coins: int = 3
    _yoshi_cookie_item: "Type[RegularItem]" = IceBomb
    _common_item_drop: "Type[RegularItem]" = IceBomb


class Forkies(Enemy):
    """Forkies enemy class"""

    _monster_id: int = 99
    _hp: int = 350
    _speed: int = 200
    _attack: int = 170
    _defense: int = 120
    _magic_attack: int = 45
    _magic_defense: int = 128
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.CLAW
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 32
    _coins: int = 7
    _yoshi_cookie_item: "Type[RegularItem]" = RoyalSyrup
    _rare_item_drop: "Type[RegularItem]" = SleepyBomb


class Gorgon(Enemy):
    """Gorgon enemy class"""

    _monster_id: int = 100
    _hp: int = 140
    _speed: int = 16
    _attack: int = 86
    _defense: int = 73
    _magic_attack: int = 24
    _magic_defense: int = 52
    _fp: int = 100
    _evade: int = 11
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 30

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 20
    _yoshi_cookie_item: "Type[RegularItem]" = MapleSyrup
    _rare_item_drop: "Type[RegularItem]" = MidMushroom


class BigBertha(Enemy):
    """BigBertha enemy class"""

    _monster_id: int = 101
    _hp: int = 350
    _speed: int = 1
    _attack: int = 170
    _defense: int = 130
    _fp: int = 100
    _morph_chance: float = 1.0
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 35
    _coins: int = 7
    _yoshi_cookie_item: "Type[RegularItem]" = PickMeUp


class ChainedKong(Enemy):
    """ChainedKong enemy class"""

    _monster_id: int = 102
    _hp: int = 355
    _speed: int = 17
    _attack: int = 150
    _defense: int = 80
    _magic_attack: int = 22
    _magic_defense: int = 50
    _fp: int = 100
    _evade: int = 10
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.GUERRILLA
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = [Element.FIRE]

    # rewards
    _xp: int = 35
    _coins: int = 8
    _yoshi_cookie_item: "Type[RegularItem]" = PickMeUp
    _rare_item_drop: "Type[RegularItem]" = MaxMushroom


class Fautso(Enemy):
    """Fautso enemy class"""

    _monster_id: int = 103
    _boss: bool = True
    _hp: int = 420
    _speed: int = 14
    _attack: int = 130
    _defense: int = 100
    _magic_attack: int = 60
    _magic_defense: int = 60
    _fp: int = 100
    _evade: int = 10
    _sound_on_hit: HitSound = HitSound.SMASH
    _resistances: List[Element] = [Element.THUNDER, Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE, Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.FEAR,
        Status.POISON,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.4667
    _ratio_fp: float = 1.0
    _ratio_attack: float = 0.7222
    _ratio_defense: float = 0.9091
    _ratio_magic_attack: float = 0.75
    _ratio_magic_defense: float = 1.5
    _ratio_speed: float = 14.0
    _ratio_evade: float = 1.0
    _ratio_magic_evade: float = 0.0


class Strawhead(Enemy):
    """Strawhead enemy class"""

    _monster_id: int = 104
    _hp: int = 131
    _speed: int = 9
    _attack: int = 80
    _defense: int = 63
    _magic_attack: int = 18
    _magic_defense: int = 12
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 17
    _coins: int = 12
    _yoshi_cookie_item: "Type[RegularItem]" = PureWater
    _common_item_drop: "Type[RegularItem]" = PureWater
    _rare_item_drop: "Type[RegularItem]" = PureWater


class Juju(Enemy):
    """Juju enemy class"""

    _monster_id: int = 105
    _hp: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.CLAW
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class ArmoredAnt(Enemy):
    """ArmoredAnt enemy class"""

    _monster_id: int = 106
    _hp: int = 230
    _speed: int = 12
    _attack: int = 130
    _defense: int = 120
    _magic_attack: int = 24
    _magic_defense: int = 80
    _fp: int = 100
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.JAB
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = [Element.FIRE]

    # rewards
    _xp: int = 30
    _coins: int = 5
    _yoshi_cookie_item: "Type[RegularItem]" = PowerBlast
    _common_item_drop: "Type[RegularItem]" = PowerBlast


class Orbison(Enemy):
    """Orbison enemy class"""

    _monster_id: int = 107
    _hp: int = 30
    _speed: int = 25
    _attack: int = 113
    _defense: int = 140
    _magic_attack: int = 63
    _magic_defense: int = 65
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.JUMP]

    # element resistances
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
    ]

    # rewards
    _xp: int = 18
    _yoshi_cookie_item: "Type[RegularItem]" = RoyalSyrup
    _common_item_drop: "Type[RegularItem]" = PureWater


class TuboTroopa(Enemy):
    """TuboTroopa enemy class"""

    _monster_id: int = 108
    _hp: int = 500
    _speed: int = 5
    _attack: int = 200
    _defense: int = 80
    _magic_attack: int = 7
    _magic_defense: int = 34
    _fp: int = 100
    _evade: int = 1
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 90
    _flying: bool = True

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 40
    _coins: int = 11
    _yoshi_cookie_item: "Type[RegularItem]" = Elixir
    _common_item_drop: "Type[RegularItem]" = RockCandy


class Doppel(Enemy):
    """Doppel enemy class"""

    _monster_id: int = 109
    _hp: int = 333
    _speed: int = 40
    _attack: int = 140
    _defense: int = 60
    _magic_attack: int = 44
    _magic_defense: int = 50
    _fp: int = 100
    _evade: int = 19
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 100

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 40
    _coins: int = 12
    _yoshi_cookie_item: "Type[RegularItem]" = PickMeUp
    _rare_item_drop: "Type[RegularItem]" = PureWater


class Pulsar(Enemy):
    """Pulsar enemy class"""

    _monster_id: int = 110
    _hp: int = 69
    _speed: int = 8
    _attack: int = 75
    _defense: int = 90
    _magic_attack: int = 33
    _magic_defense: int = 35
    _fp: int = 100
    _evade: int = 10
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.PULSAR
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 100

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 15
    _coins: int = 12
    _yoshi_cookie_item: "Type[RegularItem]" = PickMeUp
    _rare_item_drop: "Type[RegularItem]" = PickMeUp


class Octovader(Enemy):
    """Octovader enemy class"""

    _monster_id: int = 112
    _hp: int = 250
    _speed: int = 5
    _attack: int = 90
    _defense: int = 50
    _magic_attack: int = 63
    _magic_defense: int = 50
    _fp: int = 100
    _evade: int = 9
    _magic_evade: int = 8
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.DEEP_KNOCK
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 100

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = [Element.THUNDER]

    # rewards
    _xp: int = 30
    _coins: int = 8
    _yoshi_cookie_item: "Type[RegularItem]" = FroggieDrink
    _common_item_drop: "Type[RegularItem]" = PowerBlast


class Ribbite(Enemy):
    """Ribbite enemy class"""

    _monster_id: int = 113
    _hp: int = 250
    _speed: int = 15
    _attack: int = 115
    _defense: int = 20
    _magic_attack: int = 31
    _magic_defense: int = 29
    _fp: int = 100
    _morph_chance: float = 1.0
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [Status.FEAR]
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 80

    # rewards
    _xp: int = 22
    _coins: int = 8
    _yoshi_cookie_item: "Type[RegularItem]" = Elixir
    _common_item_drop: "Type[RegularItem]" = Elixir


class Director(Enemy):
    """Director enemy class"""

    _monster_id: int = 114
    _boss: bool = True
    _hp: int = 1000
    _speed: int = 35
    _attack: int = 190
    _defense: int = 120
    _magic_attack: int = 57
    _magic_defense: int = 80
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 70
    _coins: int = 80
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _anchor: bool = True
    _ratio_hp: float = 0.625
    _ratio_fp: float = 0.2

    _sprite: int = 704


class Puppox(Enemy):
    """Puppox enemy class"""

    _monster_id: int = 117
    _hp: int = 300
    _speed: int = 9
    _attack: int = 145
    _defense: int = 110
    _magic_attack: int = 20
    _magic_defense: int = 32
    _fp: int = 100
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.KNOCK
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = [Element.THUNDER]

    # rewards
    _xp: int = 30
    _coins: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = RockCandy
    _rare_item_drop: "Type[RegularItem]" = FreshenUp


class FinkFlower(Enemy):
    """FinkFlower enemy class"""

    _monster_id: int = 118
    _hp: int = 200
    _speed: int = 4
    _attack: int = 95
    _defense: int = 32
    _magic_attack: int = 63
    _magic_defense: int = 90
    _fp: int = 100
    _magic_evade: int = 12
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SLAP
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 20
    _coins: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = MaxMushroom
    _rare_item_drop: "Type[RegularItem]" = MidMushroom


class Lumbler(Enemy):
    """Lumbler enemy class"""

    _monster_id: int = 119
    _boss: bool = True
    _hp: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Springer(Enemy):
    """Springer enemy class"""

    _monster_id: int = 120
    _hp: int = 122
    _speed: int = 16
    _attack: int = 155
    _defense: int = 110
    _magic_attack: int = 100
    _magic_defense: int = 79
    _fp: int = 100
    _evade: int = 30
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 29
    _coins: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = Elixir
    _rare_item_drop: "Type[RegularItem]" = Energizer


class Harlequin(Enemy):
    """Harlequin enemy class"""

    _monster_id: int = 121
    _hp: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Kriffid(Enemy):
    """Kriffid enemy class"""

    _monster_id: int = 122
    _hp: int = 320
    _speed: int = 8
    _attack: int = 95
    _defense: int = 100
    _magic_attack: int = 50
    _magic_defense: int = 40
    _fp: int = 100
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [Status.POISON]
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80

    # rewards
    _xp: int = 35
    _coins: int = 6
    _yoshi_cookie_item: "Type[RegularItem]" = Crystalline
    _common_item_drop: "Type[RegularItem]" = BadMushroom


class Spinthra(Enemy):
    """Spinthra enemy class"""

    _monster_id: int = 123
    _hp: int = 230
    _speed: int = 19
    _attack: int = 110
    _defense: int = 70
    _magic_attack: int = 4
    _magic_defense: int = 32
    _fp: int = 100
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.CLAW
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = [Status.POISON]

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 30
    _coins: int = 4
    _yoshi_cookie_item: "Type[RegularItem]" = PowerBlast
    _rare_item_drop: "Type[RegularItem]" = Bracer


class Radish(Enemy):
    """Radish enemy class"""

    _monster_id: int = 124
    _hp: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Crippo(Enemy):
    """Crippo enemy class"""

    _monster_id: int = 125
    _hp: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class MastaBlasta(Enemy):
    """MastaBlasta enemy class"""

    _monster_id: int = 126
    _hp: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Piledriver(Enemy):
    """Piledriver enemy class"""

    _monster_id: int = 127
    _hp: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Apprentice(Enemy):
    """Apprentice enemy class"""

    _monster_id: int = 128
    _boss: bool = True
    _hp: int = 120
    _speed: int = 20
    _attack: int = 50
    _defense: int = 50
    _magic_attack: int = 20
    _magic_defense: int = 20
    _fp: int = 32
    _sound_on_hit: HitSound = HitSound.PUNCH
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 1
    _coins: int = 4
    _yoshi_cookie_item: "Type[RegularItem]" = SleepyBomb
    _common_item_drop: "Type[RegularItem]" = MidMushroom


class ApprenticeHenchman(Apprentice, Henchman):
    """ApprenticeHenchman enemy class"""

    _monster_id: int = 129

    # boss shuffle attributes
    _ratio_hp: float = 3 / 35
    _ratio_fp: float = 0.33
    _ratio_attack: float = 50 / 255
    _ratio_defense: float = 50 / 235
    _ratio_magic_attack: float = 1.0
    _ratio_magic_defense: float = 0.5
    _ratio_speed: float = 10 / 51


class BoxBoy(Enemy):
    """BoxBoy enemy class"""

    _monster_id: int = 134
    _boss: bool = True
    _hp: int = 900
    _speed: int = 1
    _attack: int = 180
    _defense: int = 110
    _magic_attack: int = 80
    _magic_defense: int = 40
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
    ]
    _weaknesses: List[Element] = [Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # rewards
    _xp: int = 100
    _coins: int = 150
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 1.0
    _ratio_fp: float = 1.0


class Shelly(ShellySupport):
    """Shelly enemy class"""

    _monster_id: int = 135
    _boss: bool = True
    _hp: int = 500
    _defense: int = 80
    _fp: int = 100
    _ohko_immune: bool = True
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # effect nullification
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 500 / 777
    _ratio_fp: float = 0.0
    _ratio_attack: float = 0.0
    _ratio_defense: float = 0.6154
    _ratio_magic_attack: float = 0.0
    _ratio_magic_defense: float = 0.0
    _ratio_speed: float = 0.0
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 0.0

    # Specific to Shelly

    _position: int = 1
    _vanilla: bool = True
    _summons: List[int] = [0x28]
    _summon_event: Optional[int] = None

    def update_world_entities(self):
        monsterscript: MonsterScript = self.world.monster_scripts.scripts[
            self.monster_id
        ]

        # update shelly's HP
        _, command = monsterscript.get_command_by_name("shelly_hp_phase_1")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.8))
        _, command = monsterscript.get_command_by_name("shelly_hp_phase_2")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.6))
        _, command = monsterscript.get_command_by_name("shelly_hp_phase_3")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.4))
        _, command = monsterscript.get_command_by_name("shelly_hp_phase_4")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.2))

        # update shelly summons
        index, _ = monsterscript.get_command_by_name("shelly_summon")
        if self.summon_event is not None:
            monsterscript.insert_after_identifier(
                "shelly_summon", RunBattleEvent(self.summon_event)
            )
        for identifier in self.summons:
            monsterscript.insert_after_identifier(
                "shelly_summon", cast(CallTarget, identifier)
            )
        monsterscript.delete_at_index(index)

        # remove the two commands that show the shell fragment if not part of birdetta fight
        if not self.vanilla:
            bank = self.world.monsters_attacks_and_items_animation_scripts.get_bank(
                BATTLE_EVENTS
            )
            index = bank.scripts[BE0092_SHELLY_BREAKS].get_index_of_identifier(
                "set_shelly_fragment"
            )
            bank.scripts[BE0092_SHELLY_BREAKS].delete_at_index(index)
            bank.scripts[BE0092_SHELLY_BREAKS].delete_at_index(index)


class Superspike(Enemy):
    """Superspike enemy class"""

    _monster_id: int = 136
    _boss: bool = True
    _hp: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class DodoSolo(Enemy):
    """DodoSolo enemy class"""

    _monster_id: int = 137
    _boss: bool = True
    _hp: int = 800
    _speed: int = 10
    _attack: int = 140
    _defense: int = 100
    _magic_attack: int = 9
    _magic_defense: int = 60
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
    ]
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 70
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 1.0
    _ratio_fp: float = 1.0

    _sprite: int = 695


class Oerlikon(Enemy):
    """Oerlikon enemy class"""

    _monster_id: int = 138
    _hp: int = 85
    _speed: int = 20
    _attack: int = 120
    _defense: int = 125
    _magic_attack: int = 17
    _magic_defense: int = 50
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _resistances: List[Element] = [Element.FIRE, Element.JUMP]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _xp: int = 22
    _yoshi_cookie_item: "Type[RegularItem]" = Energizer
    _rare_item_drop: "Type[RegularItem]" = Energizer


class Chester(Enemy):
    """Chester enemy class"""

    _monster_id: int = 139
    _boss: bool = True
    _anchor: bool = True
    _hp: int = 1200
    _speed: int = 1
    _attack: int = 220
    _defense: int = 120
    _magic_attack: int = 120
    _magic_defense: int = 80
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [
        Element.ICE,
        Element.FIRE,
        Element.THUNDER,
    ]
    _weaknesses: List[Element] = [Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # rewards
    _xp: int = 150
    _coins: int = 200
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class CorkpediteBody(Enemy):
    """CorkpediteBody enemy class"""

    _monster_id: int = 140
    _hp: int = 300
    _speed: int = 5
    _attack: int = 100
    _defense: int = 99
    _magic_attack: int = 6
    _magic_defense: int = 1
    _fp: int = 100
    _morph_chance: float = 1.0
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP

    # rewards
    _xp: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Torte(Henchman):
    """Torte enemy class"""

    _monster_id: int = 142
    _boss: bool = True
    _hp: int = 100
    _speed: int = 99
    _attack: int = 60
    _defense: int = 50
    _magic_attack: int = 8
    _magic_defense: int = 27
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.TORTE
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    # made this up
    _xp: int = 3

    # boss shuffle attributes
    _ratio_hp: float = 0.0667
    _ratio_fp: float = 0.5
    _ratio_attack: float = 0.8824
    _ratio_defense: float = 3.3333
    _ratio_magic_attack: float = 0.2857
    _ratio_magic_defense: float = 0.675
    _ratio_speed: float = 6.1875
    _ratio_evade: float = 1.0
    _ratio_magic_evade: float = 1.0


class Shyaway(Enemy):
    """Shyaway enemy class"""

    _monster_id: int = 143
    _hp: int = 140
    _speed: int = 25
    _attack: int = 90
    _defense: int = 50
    _magic_attack: int = 39
    _magic_defense: int = 73
    _fp: int = 100
    _evade: int = 40
    _morph_chance: float = 1.0
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 100

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 1
    _coins: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = MapleSyrup
    _rare_item_drop: "Type[RegularItem]" = HoneySyrup


class JinxClone(Enemy):
    """JinxClone enemy class"""

    _monster_id: int = 144
    _boss: bool = True
    _hp: int = 320
    _speed: int = 22
    _attack: int = 180
    _defense: int = 120
    _magic_defense: int = 35
    _evade: int = 30
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # effect nullification
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.FEAR,
    ]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.2
    _ratio_fp: float = 0.0
    _ratio_attack: float = 1.8
    _ratio_defense: float = 2.0
    _ratio_magic_attack: float = 0.0
    _ratio_magic_defense: float = 0.35
    _ratio_speed: float = 1.8333
    _ratio_evade: float = 1.0
    _ratio_magic_evade: float = 0.0


class MachineMadeShyster(Enemy):
    """MachineMadeShyster enemy class"""

    _monster_id: int = 145
    _hp: int = 100
    _speed: int = 36
    _attack: int = 135
    _defense: int = 95
    _magic_attack: int = 90
    _magic_defense: int = 65
    _fp: int = 250
    _evade: int = 10
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 28
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class MachineMadeShysterHenchman(MachineMadeShyster, Henchman):
    """MachineMadeShysterHenchman enemy class"""

    _monster_id: int = 214

    # boss shuffle attributes
    _ratio_hp: float = 0.05
    _ratio_fp: float = 1.0
    _ratio_attack: float = 135 / 230
    _ratio_defense: float = 19 / 26
    _ratio_magic_attack: float = 0.9
    _ratio_magic_defense: float = 0.65
    _ratio_speed: float = 1.2
    _ratio_evade: float = 1.0
    _ratio_magic_evade: float = 0.0


class MachineMadeDrillBit(Enemy):
    """MachineMadeDrillBit enemy class"""

    _monster_id: int = 146
    _boss: bool = True
    _hp: int = 180
    _speed: int = 24
    _attack: int = 130
    _defense: int = 82
    _magic_attack: int = 31
    _magic_defense: int = 69
    _fp: int = 100
    _morph_chance: float = 1.0
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Formless(Enemy):
    """Formless enemy class"""

    _monster_id: int = 147
    _boss: bool = True
    _hp: int = 10
    _speed: int = 2
    _magic_attack: int = 50
    _fp: int = 100
    _evade: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [Element.FIRE, Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 1 / 62
    _ratio_fp: float = 1.0
    _ratio_attack: float = 0.0
    _ratio_defense: float = 0.0
    _ratio_magic_attack: float = 0.625
    _ratio_magic_defense: float = 0.0
    _ratio_speed: float = 0.08
    _ratio_magic_evade: float = 0.0


class Mokura(Enemy):
    """Mokura enemy class"""

    _monster_id: int = 148
    _boss: bool = True
    _hp: int = 620
    _speed: int = 25
    _attack: int = 120
    _defense: int = 75
    _magic_attack: int = 80
    _magic_defense: int = 90
    _fp: int = 100
    _evade: int = 20
    _magic_evade: int = 10
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [Element.FIRE, Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _xp: int = 90
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _common_item_drop: "Type[RegularItem]" = KerokeroCola
    _rare_item_drop: "Type[RegularItem]" = RoyalSyrup


class FireCrystal(Henchman):
    """FireCrystal enemy class"""

    _monster_id: int = 149
    _boss: bool = True
    _hp: int = 2500
    _speed: int = 10
    _defense: int = 100
    _magic_attack: int = 130
    _magic_defense: int = 60
    _fp: int = 250
    _evade: int = 10
    _ohko_immune: bool = True
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # rewards
    _xp: int = 40
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.6104
    _ratio_fp: float = 1.25
    _ratio_attack: float = 0.0
    _ratio_defense: float = 1.0
    _ratio_magic_attack: float = 1.3
    _ratio_magic_defense: float = 0.75
    _ratio_speed: float = 0.2
    _ratio_evade: float = 1.0
    _ratio_magic_evade: float = 0.0


class WaterCrystal(Henchman):
    """WaterCrystal enemy class"""

    _monster_id: int = 150
    _boss: bool = True
    _hp: int = 1800
    _speed: int = 12
    _defense: int = 130
    _magic_attack: int = 120
    _magic_defense: int = 50
    _fp: int = 250
    _evade: int = 20
    _ohko_immune: bool = True
    _resistances: List[Element] = [Element.ICE]
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # rewards
    _xp: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.4395
    _ratio_fp: float = 1.25
    _ratio_attack: float = 0.0
    _ratio_defense: float = 1.3
    _ratio_magic_attack: float = 1.2
    _ratio_magic_defense: float = 0.625
    _ratio_speed: float = 0.24
    _ratio_evade: float = 1.0
    _ratio_magic_evade: float = 0.0


class EarthCrystal(Henchman):
    """EarthCrystal enemy class"""

    _monster_id: int = 151
    _boss: bool = True
    _hp: int = 3200
    _speed: int = 1
    _defense: int = 70
    _magic_attack: int = 80
    _magic_defense: int = 33
    _fp: int = 250
    _evade: int = 5
    _ohko_immune: bool = True
    _resistances: List[Element] = [Element.JUMP]
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # rewards
    _xp: int = 50
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.7813
    _ratio_fp: float = 1.25
    _ratio_attack: float = 0.0
    _ratio_defense: float = 0.7
    _ratio_magic_attack: float = 0.8
    _ratio_magic_defense: float = 0.4125
    _ratio_speed: float = 0.02
    _ratio_evade: float = 1.0
    _ratio_magic_evade: float = 0.0


class WindCrystal(Henchman):
    """WindCrystal enemy class"""

    _monster_id: int = 152
    _boss: bool = True
    _hp: int = 800
    _speed: int = 30
    _defense: int = 200
    _magic_attack: int = 60
    _magic_defense: int = 88
    _fp: int = 250
    _evade: int = 30
    _ohko_immune: bool = True
    _resistances: List[Element] = [Element.THUNDER]
    _weaknesses: List[Element] = [Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # rewards
    _xp: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.1953
    _ratio_fp: float = 1.25
    _ratio_attack: float = 0.0
    _ratio_defense: float = 0.2
    _ratio_magic_attack: float = 0.6
    _ratio_magic_defense: float = 1.1
    _ratio_speed: float = 0.6
    _ratio_evade: float = 1.0
    _ratio_magic_evade: float = 0.0


class MarioClone(AllyClone):
    """MarioClone enemy class"""

    _monster_id: int = 153
    _boss: bool = True
    _hp: int = 200
    _speed: int = 20
    _attack: int = 100
    _defense: int = 90
    _magic_attack: int = 33
    _magic_defense: int = 50
    _fp: int = 25
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.KNOCK
    _resistances: List[Element] = [Element.FIRE, Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _xp: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.1667
    _ratio_fp: float = 0.1
    _ratio_attack: float = 0.8333
    _ratio_defense: float = 1.125
    _ratio_magic_attack: float = 1.65
    _ratio_magic_defense: float = 1.25
    _ratio_speed: float = 5.0
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 0.0


class PeachClone(AllyClone):
    """PeachClone enemy class"""

    _monster_id: int = 154
    _boss: bool = True
    _hp: int = 120
    _speed: int = 20
    _attack: int = 90
    _defense: int = 60
    _magic_attack: int = 62
    _magic_defense: int = 70
    _fp: int = 180
    _ohko_immune: bool = True
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.1
    _ratio_fp: float = 0.72
    _ratio_attack: float = 0.75
    _ratio_defense: float = 0.75
    _ratio_magic_attack: float = 3.1
    _ratio_magic_defense: float = 1.75
    _ratio_speed: float = 5.0
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 0.0


class BowserClone(AllyClone):
    """BowserClone enemy class"""

    _monster_id: int = 155
    _boss: bool = True
    _hp: int = 300
    _speed: int = 12
    _attack: int = 130
    _defense: int = 100
    _magic_attack: int = 12
    _fp: int = 1
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [Element.FIRE, Element.JUMP]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _xp: int = 100
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.25
    _ratio_fp: float = 0.004
    _ratio_attack: float = 1.0833
    _ratio_defense: float = 1.25
    _ratio_magic_attack: float = 0.6
    _ratio_magic_defense: float = 0.0
    _ratio_speed: float = 3.0
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 0.0


class GenoClone(AllyClone):
    """GenoClone enemy class"""

    _monster_id: int = 156
    _boss: bool = True
    _hp: int = 250
    _speed: int = 30
    _attack: int = 120
    _defense: int = 80
    _magic_attack: int = 60
    _magic_defense: int = 30
    _fp: int = 40
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _resistances: List[Element] = [Element.ICE]
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _xp: int = 40
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.2083
    _ratio_fp: float = 0.16
    _ratio_attack: float = 1.0
    _ratio_defense: float = 1.0
    _ratio_magic_attack: float = 3.0
    _ratio_magic_defense: float = 0.75
    _ratio_speed: float = 7.5
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 0.0


class MallowClone(AllyClone):
    """MallowClone enemy class"""

    _monster_id: int = 157
    _boss: bool = True
    _hp: int = 150
    _speed: int = 14
    _attack: int = 80
    _defense: int = 65
    _magic_attack: int = 70
    _magic_defense: int = 80
    _fp: int = 80
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.KNOCK
    _resistances: List[Element] = [Element.ICE, Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _xp: int = 60
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.125
    _ratio_fp: float = 0.32
    _ratio_attack: float = 0.6667
    _ratio_defense: float = 0.8125
    _ratio_magic_attack: float = 3.5
    _ratio_magic_defense: float = 2.0
    _ratio_speed: float = 3.5
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 0.0


class Shyster(Enemy):
    """Shyster enemy class"""

    _monster_id: int = 158
    _hp: int = 30
    _speed: int = 18
    _attack: int = 20
    _defense: int = 26
    _magic_attack: int = 18
    _magic_defense: int = 10
    _fp: int = 2
    _evade: int = 10
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 3
    _coins: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = HoneySyrup
    _common_item_drop: "Type[RegularItem]" = HoneySyrup


class Kinklink(Enemy):
    """Kinklink enemy class"""

    _monster_id: int = 159
    _boss: bool = True
    _hp: int = 60
    _speed: int = 99
    _defense: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class HanginShy(Enemy):
    """HanginShy enemy class"""

    _monster_id: int = 161
    _boss: bool = True
    _hp: int = 10
    _speed: int = 200
    _fp: int = 100
    _ohko_immune: bool = True
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Smelter(Enemy):
    """Smelter enemy class"""

    _monster_id: int = 162
    _boss: bool = True
    _hp: int = 1500
    _defense: int = 120
    _magic_defense: int = 100
    _fp: int = 100
    _ohko_immune: bool = True
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.75
    _ratio_fp: float = 100 / 250
    _ratio_attack: float = 0.0
    _ratio_defense: float = 120 / 130
    _ratio_magic_attack: float = 0.0
    _ratio_magic_defense: float = 1.0


class MachineMadeMack(Enemy):
    """MachineMadeMack enemy class"""

    _monster_id: int = 163
    _boss: bool = True
    _hp: int = 300
    _speed: int = 10
    _attack: int = 160
    _defense: int = 120
    _magic_attack: int = 95
    _magic_defense: int = 40
    _fp: int = 250
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 120
    _coins: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = FireBomb


class MachineMadeBowyer(Enemy):
    """MachineMadeBowyer enemy class"""

    _monster_id: int = 164
    _boss: bool = True
    _hp: int = 1000
    _speed: int = 200
    _attack: int = 150
    _defense: int = 120
    _magic_attack: int = 90
    _magic_defense: int = 80
    _fp: int = 250
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 150
    _coins: int = 40
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = IceBomb


class MachineMadeYaridovich(Enemy):
    """MachineMadeYaridovich enemy class"""

    _monster_id: int = 165
    _boss: bool = True
    _hp: int = 800
    _speed: int = 18
    _attack: int = 180
    _defense: int = 130
    _magic_attack: int = 90
    _magic_defense: int = 50
    _fp: int = 250
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 180
    _coins: int = 50
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = RockCandy


class MachineMadeAxemPink(Enemy):
    """MachineMadeAxemPink enemy class"""

    _monster_id: int = 166
    _hp: int = 100
    _speed: int = 35
    _attack: int = 95
    _defense: int = 90
    _magic_attack: int = 40
    _magic_defense: int = 100
    _fp: int = 200
    _evade: int = 25
    _magic_evade: int = 10
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _resistances: List[Element] = [Element.ICE]
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _xp: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = MapleSyrup


class MachineMadeAxemPinkHenchman(MachineMadeAxemPink, Henchman):
    """MachineMadeAxemPinkHenchman enemy class"""

    _monster_id: int = 174

    # boss shuffle attributes
    _ratio_hp: float = 100 / (800 + 400 + 550 + 600 + 450 + 999)
    _ratio_fp: float = 200 / (100 + 200 + 100 + 100 + 200 + 100)
    _ratio_attack: float = 40 / (150 + 120 + 140 + 170 + 110 + 0)
    _ratio_defense: float = 100 / (100 + 80 + 120 + 130 + 60 + 100)
    _ratio_magic_attack: float = 40 / (24 + 80 + 4 + 6 + 90 + 120)
    _ratio_magic_defense: float = 100 / (80 + 100 + 40 + 60 + 120 + 100)
    _ratio_speed: float = 35 / (30 + 25 + 35 + 3 + 20 + 200)
    _ratio_evade: float = 25 / (10 + 25 + 30 + 0 + 0 + 0)
    _ratio_magic_evade: float = 10 / (0 + 10 + 0 + 0 + 20 + 0)

    # rewards
    _xp: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = MapleSyrup


class MachineMadeAxemBlack(Enemy):
    """MachineMadeAxemBlack enemy class"""

    _monster_id: int = 167
    _hp: int = 120
    _speed: int = 55
    _attack: int = 120
    _defense: int = 110
    _magic_attack: int = 4
    _magic_defense: int = 40
    _fp: int = 100
    _evade: int = 30
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 20
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = MaxMushroom


class MachineMadeAxemBlackHenchman(MachineMadeAxemBlack, Henchman):
    """MachineMadeAxemBlackHenchman enemy class"""

    _monster_id: int = 173

    # boss shuffle attributes
    _ratio_hp: float = 120 / (800 + 400 + 550 + 600 + 450 + 999)
    _ratio_fp: float = 100 / (100 + 200 + 100 + 100 + 200 + 100)
    _ratio_attack: float = 120 / (150 + 120 + 140 + 170 + 110 + 0)
    _ratio_defense: float = 40 / (100 + 80 + 120 + 130 + 60 + 100)
    _ratio_magic_attack: float = 4 / (24 + 80 + 4 + 6 + 90 + 120)
    _ratio_magic_defense: float = 40 / (80 + 100 + 40 + 60 + 120 + 100)
    _ratio_speed: float = 55 / (30 + 25 + 35 + 3 + 20 + 200)
    _ratio_evade: float = 30 / (10 + 25 + 30 + 0 + 0 + 0)
    _ratio_magic_evade: float = 0 / (0 + 10 + 0 + 0 + 20 + 0)

    # rewards
    _xp: int = 20
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = MaxMushroom


class MachineMadeAxemRed(Enemy):
    """MachineMadeAxemRed enemy class"""

    _monster_id: int = 168
    _hp: int = 180
    _speed: int = 45
    _attack: int = 135
    _defense: int = 95
    _magic_attack: int = 24
    _magic_defense: int = 80
    _fp: int = 100
    _evade: int = 10
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY

    # rewards
    _xp: int = 50
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = RoyalSyrup


class MachineMadeAxemRedHenchman(MachineMadeAxemRed, Henchman):
    """MachineMadeAxemRedHenchman enemy class"""

    _monster_id: int = 201

    # boss shuffle attributes
    _ratio_hp: float = 180 / (800 + 400 + 550 + 600 + 450 + 999)
    _ratio_fp: float = 100 / (100 + 200 + 100 + 100 + 200 + 100)
    _ratio_attack: float = 135 / (150 + 120 + 140 + 170 + 110 + 0)
    _ratio_defense: float = 95 / (100 + 80 + 120 + 130 + 60 + 100)
    _ratio_magic_attack: float = 24 / (24 + 80 + 4 + 6 + 90 + 120)
    _ratio_magic_defense: float = 80 / (80 + 100 + 40 + 60 + 120 + 100)
    _ratio_speed: float = 45 / (30 + 25 + 35 + 3 + 20 + 200)
    _ratio_evade: float = 10 / (10 + 25 + 30 + 0 + 0 + 0)
    _ratio_magic_evade: float = 0 / (0 + 10 + 0 + 0 + 20 + 0)

    # rewards
    _xp: int = 50
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = RoyalSyrup


class MachineMadeAxemYellow(Enemy):
    """MachineMadeAxemYellow enemy class"""

    _monster_id: int = 169
    _hp: int = 200
    _speed: int = 20
    _attack: int = 140
    _defense: int = 130
    _magic_attack: int = 16
    _magic_defense: int = 20
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _resistances: List[Element] = [Element.THUNDER]
    _weaknesses: List[Element] = [Element.JUMP]
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.POISON,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX

    # rewards
    _xp: int = 25
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = MaxMushroom


class MachineMadeAxemYellowHenchman(MachineMadeAxemYellow, Henchman):
    """MachineMadeAxemYellowHenchman enemy class"""

    _monster_id: int = 242

    # boss shuffle attributes
    _ratio_hp: float = 200 / (800 + 400 + 550 + 600 + 450 + 999)
    _ratio_fp: float = 100 / (100 + 200 + 100 + 100 + 200 + 100)
    _ratio_attack: float = 140 / (150 + 120 + 140 + 170 + 110 + 0)
    _ratio_defense: float = 20 / (100 + 80 + 120 + 130 + 60 + 100)
    _ratio_magic_attack: float = 16 / (24 + 80 + 4 + 6 + 90 + 120)
    _ratio_magic_defense: float = 20 / (80 + 100 + 40 + 60 + 120 + 100)
    _ratio_speed: float = 20 / (30 + 25 + 35 + 3 + 20 + 200)
    _ratio_evade: float = 0 / (10 + 25 + 30 + 0 + 0 + 0)
    _ratio_magic_evade: float = 0 / (0 + 10 + 0 + 0 + 20 + 0)

    # rewards
    _xp: int = 25
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = MaxMushroom


class MachineMadeAxemGreen(Enemy):
    """MachineMadeAxemGreen enemy class"""

    _monster_id: int = 170
    _hp: int = 80
    _speed: int = 40
    _attack: int = 105
    _defense: int = 80
    _magic_attack: int = 80
    _magic_defense: int = 120
    _fp: int = 250
    _magic_evade: int = 20
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = RoyalSyrup


class MachineMadeAxemGreenHenchman(MachineMadeAxemGreen, Henchman):
    """MachineMadeAxemGreenHenchman enemy class"""

    _monster_id: int = 232

    # boss shuffle attributes
    _ratio_hp: float = 80 / (800 + 400 + 550 + 600 + 450 + 999)
    _ratio_fp: float = 250 / (100 + 200 + 100 + 100 + 200 + 100)
    _ratio_attack: float = 105 / (150 + 120 + 140 + 170 + 110 + 0)
    _ratio_defense: float = 80 / (100 + 80 + 120 + 130 + 60 + 100)
    _ratio_magic_attack: float = 80 / (24 + 80 + 4 + 6 + 90 + 120)
    _ratio_magic_defense: float = 120 / (80 + 100 + 40 + 60 + 120 + 100)
    _ratio_speed: float = 40 / (30 + 25 + 35 + 3 + 20 + 200)
    _ratio_evade: float = 0 / (10 + 25 + 30 + 0 + 0 + 0)
    _ratio_magic_evade: float = 20 / (0 + 10 + 0 + 0 + 20 + 0)

    # rewards
    _xp: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = RoyalSyrup


class Starslap(Enemy):
    """Starslap enemy class"""

    _monster_id: int = 176
    _boss: bool = True
    _hp: int = 62
    _speed: int = 9
    _attack: int = 25
    _defense: int = 24
    _magic_attack: int = 4
    _magic_defense: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _weaknesses: List[Element] = [Element.THUNDER, Element.FIRE]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 50

    # effect nullification
    _status_immunities: List[Status] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 2
    _coins: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Mukumuku(Enemy):
    """Mukumuku enemy class"""

    _monster_id: int = 177
    _hp: int = 108
    _speed: int = 11
    _attack: int = 60
    _defense: int = 47
    _magic_attack: int = 22
    _magic_defense: int = 30
    _fp: int = 100
    _magic_evade: int = 80
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _resistances: List[Element] = [Element.THUNDER]
    _weaknesses: List[Element] = [Element.FIRE]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # rewards
    _xp: int = 8
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = MukuCookie
    _rare_item_drop: "Type[RegularItem]" = MapleSyrup


class Zeostar(Enemy):
    """Zeostar enemy class"""

    _monster_id: int = 178
    _hp: int = 90
    _speed: int = 10
    _attack: int = 75
    _defense: int = 60
    _magic_attack: int = 28
    _magic_defense: int = 20
    _fp: int = 4
    _morph_chance: float = 0.75
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _weaknesses: List[Element] = [Element.THUNDER, Element.FIRE]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 50

    # effect nullification
    _status_immunities: List[Status] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 10
    _coins: int = 3
    _yoshi_cookie_item: "Type[RegularItem]" = SleepyBomb
    _rare_item_drop: "Type[RegularItem]" = Mushroom


class Jagger(Enemy):
    """Jagger enemy class"""

    _monster_id: int = 179
    _boss: bool = True
    _hp: int = 600
    _speed: int = 30
    _attack: int = 120
    _defense: int = 80
    _magic_defense: int = 50
    _fp: int = 100
    _evade: int = 10
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.KNOCK
    _resistances: List[Element] = [Element.FIRE, Element.JUMP]
    _status_immunities: List[Status] = [Status.POISON]
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _xp: int = 50
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 1.0
    _ratio_fp: float = 1.0


class EmptyEnemy(ShellySupport):
    """EmptyEnemy enemy class"""

    _monster_id: int = 180
    _boss: bool = True
    _hp: int = 9999
    _fp: int = 100
    _speed: int = 255

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # Specific to Shelly
    _summons: List[int] = [0x28]
    _summon_event: Union[int, None] = None
    _sprite_sub: bool = False
    _formation_id: Union[int, None] = None


class Smithy2TankHead(Enemy):
    """Smithy2TankHead enemy class"""

    _monster_id: int = 181
    _boss: bool = True
    _hp: int = 8000
    _speed: int = 50
    _attack: int = 250
    _defense: int = 130
    _magic_attack: int = 10
    _magic_defense: int = 50
    _fp: int = 30
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.KNOCK
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    _ratio_hp: float = 8000 / 10000
    _ratio_attack: float = 250 / 186.875
    _ratio_defense: float = 130 / 121.25
    _ratio_magic_attack: float = 10 / 86
    _ratio_magic_defense: float = 50 / 97.5

    def update_world_entities(self):
        monsterscript: MonsterScript = self.world.monster_scripts.scripts[
            self.monster_id
        ]

        # update HP
        _, command = monsterscript.get_command_by_name("tank_threshold_lowest")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.25))
        _, command = monsterscript.get_command_by_name("tank_threshold_mid")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.5))
        _, command = monsterscript.get_command_by_name("tank_threshold_highest")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.75))


class Smithy2SafeHead(Enemy):
    """Smithy2SafeHead enemy class"""

    _monster_id: int = 182
    _boss: bool = True
    _hp: int = 8000
    _attack: int = 40
    _defense: int = 150
    _magic_attack: int = 70
    _magic_defense: int = 100
    _fp: int = 120
    _ohko_immune: bool = True
    _resistances: List[Element] = [
        Element.THUNDER,
        Element.FIRE,
        Element.JUMP,
    ]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    _ratio_hp: float = 8000 / 10000
    _ratio_attack: float = 40 / 186.875
    _ratio_defense: float = 150 / 121.25
    _ratio_magic_attack: float = 70 / 86
    _ratio_magic_defense: float = 100 / 97.5

    def update_world_entities(self):
        monsterscript: MonsterScript = self.world.monster_scripts.scripts[
            self.monster_id
        ]

        # update HP
        _, command = monsterscript.get_command_by_name("chest_threshold_lowest")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.25))
        _, command = monsterscript.get_command_by_name("chest_threshold_mid")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.5))
        _, command = monsterscript.get_command_by_name("chest_threshold_highest")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.75))


class Microbomb(Enemy):
    """Microbomb enemy class"""

    _monster_id: int = 184
    _boss: bool = True
    _hp: int = 30
    _speed: int = 15
    _attack: int = 42
    _defense: int = 30
    _magic_attack: int = 6
    _magic_defense: int = 10
    _fp: int = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _weaknesses: List[Element] = [Element.FIRE, Element.JUMP]
    _status_immunities: List[Status] = [Status.SLEEP]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # element resistances
    _resistances: List[Element] = []

    # boss shuffle attributes
    _ratio_hp: float = 0.025
    _ratio_fp: float = 10.0
    _ratio_attack: float = 0.7
    _ratio_defense: float = 0.71
    _ratio_magic_attack: float = 0.27
    _ratio_magic_defense: float = 0.25
    _ratio_speed: float = 1.0
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 0.0


class Grit(Enemy):
    """Grit enemy class"""

    _monster_id: int = 186
    _boss: bool = True
    _hp: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Neosquid(Enemy):
    """Neosquid enemy class"""

    _monster_id: int = 187
    _boss: bool = True
    _hp: int = 800
    _speed: int = 20
    _attack: int = 180
    _defense: int = 80
    _magic_attack: int = 86
    _magic_defense: int = 50
    _fp: int = 200
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # effect nullification
    _status_immunities: List[Status] = [Status.SLEEP]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 40
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.3636
    _ratio_fp: float = 0.3333
    _ratio_attack: float = 1.5652
    _ratio_defense: float = 0.7407
    _ratio_magic_attack: float = 1.5926
    _ratio_magic_defense: float = 0.8065
    _ratio_speed: float = 0.3077


class YaridovichMirage(Enemy):
    """YaridovichMirage enemy class"""

    _monster_id: int = 188
    _boss: bool = True
    _hp: int = 500
    _speed: int = 16
    _attack: int = 100
    _defense: int = 40
    _magic_attack: int = 60
    _magic_defense: int = 10
    _fp: int = 100
    _sound_on_hit: HitSound = HitSound.CLAW
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.3333
    _ratio_fp: float = 1.0
    _ratio_attack: float = 0.8
    _ratio_defense: float = 0.4706
    _ratio_magic_attack: float = 0.8571
    _ratio_magic_defense: float = 0.1333
    _ratio_speed: float = 0.8


class Helio(Enemy):
    """Helio enemy class"""

    _monster_id: int = 189
    _boss: bool = True
    _hp: int = 10
    _attack: int = 140
    _fp: int = 100
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.0031
    _ratio_fp: float = 0.5
    _ratio_attack: float = 0.8
    _ratio_defense: float = 0.0
    _ratio_magic_attack: float = 0.0
    _ratio_magic_defense: float = 0.0
    _ratio_speed: float = 0.0
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 0.0


class RightEye(Enemy):
    """RightEye enemy class"""

    _monster_id: int = 190
    _boss: bool = True
    _hp: int = 500
    _speed: int = 17
    _attack: int = 128
    _defense: int = 100
    _magic_attack: int = 82
    _magic_defense: int = 36
    _fp: int = 200
    _ohko_immune: bool = True
    _resistances: List[Element] = [Element.THUNDER]
    _weaknesses: List[Element] = [Element.FIRE, Element.JUMP]
    _status_immunities: List[Status] = [Status.SLEEP]
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # rewards
    _xp: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.2273
    _ratio_fp: float = 0.3333
    _ratio_attack: float = 1.113
    _ratio_defense: float = 0.9259
    _ratio_magic_attack: float = 1.5185
    _ratio_magic_defense: float = 0.5806
    _ratio_speed: float = 0.2615

    def update_world_entities(self):
        # set right eye's revival HP in monster behaviour
        bank: AnimationScriptBank = (
            self.world.monsters_attacks_and_items_animation_scripts.get_bank(
                SUBROUTINES_0X353437
            )
        )
        command = bank.get_command_by_name("right_eye_revival_hp")
        assert isinstance(command, SetAMEM16BitToConst)
        command.set_value(round(self.hp * 1.2))

        # replace exor revival command
        monsterscript: MonsterScript = self.world.monster_scripts.scripts[
            self.monster_id
        ]
        index, _ = monsterscript.get_command_by_name("right_eye_revive_exor")
        if self.world.settings.is_boolean_flag_enabled(NoGenoWhirlExor):
            monsterscript.replace_at_index(
                index, SetTargetable(MONSTER_1_SET, "right_eye_revive_exor")
            )


class LeftEye(Enemy):
    """LeftEye enemy class"""

    _monster_id: int = 191
    _boss: bool = True
    _hp: int = 300
    _speed: int = 21
    _attack: int = 153
    _defense: int = 130
    _magic_attack: int = 47
    _magic_defense: int = 80
    _fp: int = 200
    _ohko_immune: bool = True
    _resistances: List[Element] = [Element.THUNDER]
    _weaknesses: List[Element] = [Element.FIRE, Element.JUMP]
    _status_immunities: List[Status] = [Status.SLEEP]
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # rewards
    _xp: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.1364
    _ratio_fp: float = 0.3333
    _ratio_attack: float = 1.3304
    _ratio_defense: float = 1.2037
    _ratio_magic_attack: float = 0.8704
    _ratio_magic_defense: float = 1.2903
    _ratio_speed: float = 0.3231

    def update_world_entities(self):
        # set left eye's revival HP in monster behaviour
        bank: AnimationScriptBank = (
            self.world.monsters_attacks_and_items_animation_scripts.get_bank(
                SUBROUTINES_0X353437
            )
        )
        command = bank.get_command_by_name("left_eye_revival_hp")
        assert isinstance(command, SetAMEM16BitToConst)
        command.set_value(self.hp)

        # replace exor revival command
        monsterscript: MonsterScript = self.world.monster_scripts.scripts[
            self.monster_id
        ]
        index, _ = monsterscript.get_command_by_name("left_eye_revive_exor")
        if self.world.settings.is_boolean_flag_enabled(NoGenoWhirlExor):
            monsterscript.replace_at_index(
                index, SetTargetable(MONSTER_1_SET, "left_eye_revive_exor")
            )


class KnifeGuy(Enemy):
    """KnifeGuy enemy class"""

    _monster_id: int = 192
    _boss: bool = True
    _hp: int = 700
    _speed: int = 25
    _attack: int = 70
    _defense: int = 55
    _magic_attack: int = 20
    _magic_defense: int = 10
    _fp: int = 35
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [Element.THUNDER]
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [Status.SLEEP]
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # rewards
    _xp: int = 40
    _coins: int = 15
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.44
    _ratio_fp: float = 0.41
    _ratio_attack: float = 1.08
    _ratio_defense: float = 1.15
    _ratio_magic_attack: float = 0.87
    _ratio_magic_defense: float = 0.4
    _ratio_speed: float = 1.25

    _sprite: int = 690


class GrateGuy(Enemy):
    """GrateGuy enemy class"""

    _monster_id: int = 193
    _boss: bool = True
    _hp: int = 900
    _speed: int = 14
    _attack: int = 60
    _defense: int = 40
    _magic_attack: int = 25
    _magic_defense: int = 40
    _fp: int = 50
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [Status.SLEEP]
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # rewards
    _xp: int = 50
    _coins: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _common_item_drop: "Type[RegularItem]" = FlowerJar
    _rare_item_drop: "Type[RegularItem]" = FlowerJar

    # boss shuffle attributes
    _ratio_hp: float = 0.56
    _ratio_fp: float = 0.59
    _ratio_attack: float = 0.92
    _ratio_defense: float = 0.83
    _ratio_magic_attack: float = 1.09
    _ratio_magic_defense: float = 1.6
    _ratio_speed: float = 0.7

    _sprite: int = 689


class Bundt(Enemy):
    """Bundt enemy class"""

    _monster_id: int = 194
    _boss: bool = True
    _hp: int = 900
    _speed: int = 16
    _attack: int = 65
    _defense: int = 10
    _magic_attack: int = 25
    _magic_defense: int = 50
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
    ]
    _weaknesses: List[Element] = [Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
    ]
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # rewards
    # xp = 25
    _xp: int = 23
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.6
    _ratio_fp: float = 0.5
    _ratio_attack: float = 0.9559
    _ratio_defense: float = 0.6667
    _ratio_magic_attack: float = 0.8929
    _ratio_magic_defense: float = 1.25
    _ratio_speed: float = 1.0

    def get_patch(self):
        """Update battle event triggers based on HP to use shuffled HP value instead.

        Returns:
            randomizer.logic.patch.Patch: Patch data

        """
        patch = super().get_patch()

        if self.world.chocolate_cake:
            patch.add_data(0x2547AC, CHOCOLATE_CAKE.to_bytes())
        return patch


class Jinx1(Enemy):
    """Jinx1 enemy class"""

    _monster_id: int = 195
    _boss: bool = True
    _hp: int = 600
    _speed: int = 30
    _attack: int = 140
    _defense: int = 100
    _magic_defense: int = 80
    _fp: int = 100
    _evade: int = 30
    _magic_evade: int = 25
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
    ]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _xp: int = 75
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 1.0
    _ratio_fp: float = 1.0

    _name_override: str = "JINX 1"

    def update_world_entities(self):
        monsterscript: MonsterScript = self.world.monster_scripts.scripts[
            self.monster_id
        ]

        # update HP
        _, command = monsterscript.get_command_by_name("jinx1_def")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.5))


class Jinx2(Enemy):
    """Jinx2 enemy class"""

    _monster_id: int = 196
    _boss: bool = True
    _hp: int = 800
    _speed: int = 32
    _attack: int = 160
    _defense: int = 120
    _magic_defense: int = 90
    _fp: int = 100
    _evade: int = 30
    _magic_evade: int = 25
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
    ]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _xp: int = 100
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 1.0
    _ratio_fp: float = 1.0

    _name_override: str = "JINX 2"

    def update_world_entities(self):
        monsterscript: MonsterScript = self.world.monster_scripts.scripts[
            self.monster_id
        ]

        # update HP
        _, command = monsterscript.get_command_by_name("jinx2_def")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.5))


class CountDown(Enemy):
    """CountDown enemy class"""

    _monster_id: int = 197
    _boss: bool = True
    _hp: int = 2400
    _speed: int = 5
    _defense: int = 80
    _magic_attack: int = 120
    _magic_defense: int = 80
    _fp: int = 100
    _ohko_immune: bool = True
    _weaknesses: List[Element] = [Element.THUNDER, Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 140
    _coins: int = 100
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.5
    _ratio_fp: float = 0.3333
    _ratio_attack: float = 0.0
    _ratio_defense: float = 0.7477
    _ratio_magic_attack: float = 2.2642
    _ratio_magic_defense: float = 1.3333
    _ratio_speed: float = 0.625


class DingALing(Henchman):
    """DingALing enemy class"""

    _monster_id: int = 198
    _boss: bool = True
    _hp: int = 1200
    _speed: int = 10
    _attack: int = 180
    _defense: int = 120
    _magic_attack: int = 20
    _magic_defense: int = 50
    _fp: int = 100
    _ohko_immune: bool = True
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.25
    _ratio_fp: float = 0.3333
    _ratio_attack: float = 1.5
    _ratio_defense: float = 1.1215
    _ratio_magic_attack: float = 0.3774
    _ratio_magic_defense: float = 0.8333
    _ratio_speed: float = 1.25


class Belome1(Enemy):
    """Belome1 enemy class"""

    _monster_id: int = 199
    _boss: bool = True
    _hp: int = 500
    _speed: int = 4
    _attack: int = 30
    _defense: int = 25
    _magic_attack: int = 15
    _magic_defense: int = 20
    _fp: int = 30
    _magic_evade: int = 10
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [Status.SLEEP]
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 30
    _coins: int = 40
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 1.0
    _ratio_fp: float = 1.0
    _name_override: str = "BELOME 1"

    _sprite: int = 687

    def update_world_entities(self):
        monsterscript: MonsterScript = self.world.monster_scripts.scripts[
            self.monster_id
        ]

        # update HP
        _, command = monsterscript.get_command_by_name("belome_hp")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.6))


class Belome2(Enemy):
    """Belome2 enemy class"""

    _monster_id: int = 200
    _boss: bool = True
    _hp: int = 1200
    _speed: int = 4
    _attack: int = 120
    _defense: int = 80
    _magic_attack: int = 20
    _magic_defense: int = 40
    _fp: int = 250
    _magic_evade: int = 25
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _status_immunities: List[Status] = [Status.SLEEP]
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 80
    _coins: int = 20
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 1.0
    _ratio_fp: float = 1.0

    _name_override: str = "BELOME 2"
    _sprite: int = 693


class Smilax(Enemy):
    """Smilax enemy class"""

    _monster_id: int = 202
    _boss: bool = True
    _hp: int = 200
    _speed: int = 5
    _attack: int = 100
    _defense: int = 80
    _magic_attack: int = 70
    _magic_defense: int = 50
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.0769
    _ratio_fp: float = 0.1111
    _ratio_attack: float = 0.71
    _ratio_defense: float = 1.0
    _ratio_magic_attack: float = 1.0
    _ratio_magic_defense: float = 0.63
    _ratio_speed: float = 2.50


class Thrax(Enemy):
    """Thrax enemy class"""

    _monster_id: int = 203
    _boss: bool = True
    _hp: int = 10
    _speed: int = 200
    _fp: int = 100
    _ohko_immune: bool = True
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # effect nullification
    _status_immunities: List[Status] = [Status.SLEEP]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Megasmilax(Enemy):
    """Megasmilax enemy class"""

    _monster_id: int = 204
    _boss: bool = True
    _hp: int = 1000
    _speed: int = 2
    _attack: int = 140
    _defense: int = 80
    _magic_attack: int = 70
    _magic_defense: int = 80
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 120
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # Boss shuffle attributes
    _anchor: bool = True
    _ratio_hp: float = 0.3846
    _ratio_fp: float = 0.1111


class Birdetta(Enemy):
    """Birdetta enemy class"""

    _monster_id: int = 205
    _boss: bool = True
    _hp: int = 777
    _speed: int = 10
    _attack: int = 160
    _defense: int = 130
    _magic_attack: int = 6
    _magic_defense: int = 100
    _fp: int = 100
    _ohko_immune: bool = True
    _resistances: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    # xp = 60
    _xp: int = 48
    _coins: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # Boss shuffle attributes
    _ratio_hp: float = 1.0
    _ratio_fp: float = 1.0

    _name_override: str = "BIRDETTA"


class Eggbert(Henchman):
    """Eggbert enemy class"""

    _monster_id: int = 206
    _boss: bool = True
    _hp: int = 10
    _attack: int = 210
    _fp: int = 100
    _ohko_immune: bool = True
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    # made this up
    _xp: int = 3

    # boss shuffle attributes
    _ratio_hp: float = 0.01
    _ratio_fp: float = 1.0
    _ratio_attack: float = 1.31
    _ratio_defense: float = 0.0
    _ratio_magic_attack: float = 0.0
    _ratio_magic_defense: float = 0.0
    _ratio_speed: float = 0.0
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 0.0


class AxemYellow(Henchman):
    """AxemYellow enemy class"""

    _monster_id: int = 207
    _boss: bool = True
    _hp: int = 600
    _speed: int = 3
    _attack: int = 170
    _defense: int = 130
    _magic_attack: int = 6
    _magic_defense: int = 60
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _resistances: List[Element] = [Element.THUNDER]
    _weaknesses: List[Element] = [Element.JUMP]
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.POISON,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _xp: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.1579
    _ratio_fp: float = 0.125
    _ratio_attack: float = 1.4783
    _ratio_defense: float = 1.3265
    _ratio_magic_attack: float = 0.1538
    _ratio_magic_defense: float = 0.7229
    _ratio_speed: float = 0.0577
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 0.0


class Punchinello(Enemy):
    """Punchinello enemy class"""

    _monster_id: int = 208
    _boss: bool = True
    _hp: int = 1200
    _speed: int = 15
    _attack: int = 60
    _defense: int = 42
    _magic_attack: int = 22
    _magic_defense: int = 40
    _fp: int = 10
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80
    battle_sesw_only = True

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _xp: int = 70
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 1.0
    _ratio_fp: float = 1.0

    def update_world_entities(self):
        monsterscript: MonsterScript = self.world.monster_scripts.scripts[
            self.monster_id
        ]

        # update HP
        _, command = monsterscript.get_command_by_name("punch_hp_1")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 2 / 3))
        _, command = monsterscript.get_command_by_name("punch_hp_2")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 2 / 3))
        _, command = monsterscript.get_command_by_name("punch_hp_3")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 1 / 3))
        _, command = monsterscript.get_command_by_name("punch_hp_4")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 1 / 3))


class TentaclesRight(Enemy):
    """TentaclesRight enemy class"""

    _monster_id: int = 209
    _boss: bool = True
    _hp: int = 260
    _speed: int = 21
    _attack: int = 82
    _defense: int = 50
    _magic_attack: int = 35
    _magic_defense: int = 40
    _fp: int = 100
    _sound_on_hit: HitSound = HitSound.SLAP
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.0985
    _ratio_fp: float = 0.1111
    _ratio_attack: float = 0.82
    _ratio_defense: float = 0.625
    _ratio_magic_attack: float = 1.1667
    _ratio_magic_defense: float = 1.0
    _ratio_speed: float = 2.625


class AxemRed(Enemy):
    """AxemRed enemy class"""

    _monster_id: int = 210
    _boss: bool = True
    _hp: int = 800
    _speed: int = 30
    _attack: int = 150
    _defense: int = 100
    _magic_attack: int = 24
    _magic_defense: int = 80
    _fp: int = 100
    _evade: int = 10
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _xp: int = 40
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.2106
    _ratio_fp: float = 0.125
    _ratio_attack: float = 1.3043
    _ratio_defense: float = 1.0204
    _ratio_magic_attack: float = 0.6154
    _ratio_magic_defense: float = 0.9639
    _ratio_speed: float = 0.5769
    _ratio_evade: float = 0.9091
    _ratio_magic_evade: float = 0.0


class AxemGreen(Henchman):
    """AxemGreen enemy class"""

    _monster_id: int = 211
    _boss: bool = True
    _hp: int = 450
    _speed: int = 20
    _attack: int = 110
    _defense: int = 60
    _magic_attack: int = 90
    _magic_defense: int = 120
    _fp: int = 200
    _magic_evade: int = 20
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 20
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.1185
    _ratio_fp: float = 0.25
    _ratio_attack: float = 0.9565
    _ratio_defense: float = 0.6122
    _ratio_magic_attack: float = 0.0
    _ratio_magic_defense: float = 1.4458
    _ratio_speed: float = 0.3846
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 4.0


class KingBomb(Enemy):
    """KingBomb enemy class"""

    _monster_id: int = 212
    _boss: bool = True
    _hp: int = 500
    _defense: int = 130
    _magic_attack: int = 80
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _weaknesses: List[Element] = [Element.FIRE, Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.3125
    _ratio_fp: float = 0.4
    _ratio_attack: float = 0.0
    _ratio_defense: float = 2.1667
    _ratio_magic_attack: float = 0.6667
    _ratio_magic_defense: float = 0.0
    _ratio_speed: float = 0.0
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 0.0

    _sprite: int = 700

    def update_world_entities(self):
        if self.world.settings.is_boolean_flag_enabled(FixMagikoopa):
            monsterscript: MonsterScript = self.world.monster_scripts.scripts[
                self.monster_id
            ]
            monsterscript.insert_after_nth_command_of_type(
                0, IfTurnCounterEquals, ClearVar(0x7EE000)
            )


class MezzoBomb(Enemy):
    """MezzoBomb enemy class"""

    _monster_id: int = 213
    _boss: bool = True
    _hp: int = 150
    _speed: int = 1
    _attack: int = 70
    _defense: int = 40
    _magic_defense: int = 10
    _fp: int = 100
    _sound_on_hit: HitSound = HitSound.SMASH
    _weaknesses: List[Element] = [Element.FIRE, Element.JUMP]
    _status_immunities: List[Status] = [Status.SLEEP]
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.125
    _ratio_fp: float = 10.0
    _ratio_attack: float = 1.17
    _ratio_defense: float = 0.95
    _ratio_magic_attack: float = 0.0
    _ratio_magic_defense: float = 0.25
    _ratio_speed: float = 0.07
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 0.0


class Raspberry(Enemy):
    """Raspberry enemy class"""

    _monster_id: int = 215
    _boss: bool = True
    _hp: int = 600
    _speed: int = 16
    _attack: int = 70
    _defense: int = 20
    _magic_attack: int = 30
    _magic_defense: int = 30
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
    ]
    _weaknesses: List[Element] = [Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
    ]
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    # xp = 50
    _xp: int = 46
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.4
    _ratio_fp: float = 0.5
    _ratio_attack: float = 1.0294
    _ratio_defense: float = 1.3333
    _ratio_magic_attack: float = 1.0714
    _ratio_magic_defense: float = 0.75
    _ratio_speed: float = 1.0

    def get_patch(self):
        """Update battle event triggers based on HP to use shuffled HP value instead.

        Returns:
            randomizer.logic.patch.Patch: Patch data

        """
        patch = super().get_patch()

        if self.world.chocolate_cake:
            patch.add_data(0x254770, CHOCOLATE_RASPBERRY.to_bytes())
        return patch


class KingCalamari(Enemy):
    """KingCalamari enemy class"""

    _monster_id: int = 216
    _boss: bool = True
    _hp: int = 800
    _speed: int = 8
    _attack: int = 100
    _defense: int = 80
    _magic_attack: int = 30
    _magic_defense: int = 40
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.DEEP_JAB
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 100
    _coins: int = 100
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # Boss shuffle attributes
    _anchor: bool = True
    _ratio_hp: float = 0.303
    _ratio_fp: float = 0.1111


class TentaclesLeft(Enemy):
    """TentaclesLeft enemy class"""

    _monster_id: int = 217
    _boss: bool = True
    _hp: int = 200
    _speed: int = 21
    _attack: int = 87
    _defense: int = 70
    _magic_attack: int = 35
    _magic_defense: int = 23
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SLAP
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.0758
    _ratio_fp: float = 0.1111
    _ratio_attack: float = 0.87
    _ratio_defense: float = 1.0
    _ratio_magic_attack: float = 1.1667
    _ratio_magic_defense: float = 0.575
    _ratio_speed: float = 2.625


class Jinx3(Enemy):
    """Jinx3 enemy class"""

    _monster_id: int = 218
    _boss: bool = True
    _hp: int = 1000
    _speed: int = 35
    _attack: int = 180
    _defense: int = 140
    _magic_defense: int = 100
    _fp: int = 100
    _evade: int = 30
    _magic_evade: int = 25
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
    ]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _xp: int = 150
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 1.0
    _ratio_fp: float = 1.0

    _name_override: str = "JINX 3"

    def update_world_entities(self):
        monsterscript: MonsterScript = self.world.monster_scripts.scripts[
            self.monster_id
        ]

        # update HP
        _, command = monsterscript.get_command_by_name("jinx3_def_1")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.6))
        _, command = monsterscript.get_command_by_name("jinx3_def_2")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.3))


class Zombone(Enemy):
    """Zombone enemy class"""

    _monster_id: int = 219
    _boss: bool = True
    _hp: int = 1800
    _speed: int = 6
    _attack: int = 190
    _defense: int = 60
    _magic_attack: int = 80
    _magic_defense: int = 100
    _fp: int = 100
    _magic_evade: int = 10
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [Element.ICE, Element.FIRE]
    _weaknesses: List[Element] = [Element.THUNDER, Element.JUMP]
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # rewards
    _xp: int = 50
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.5625
    _ratio_fp: float = 0.5
    _ratio_attack: float = 1.0857
    _ratio_defense: float = 0.75
    _ratio_magic_attack: float = 0.8
    _ratio_magic_defense: float = 1.1765
    _ratio_speed: float = 0.4615
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 2.0


class CzarDragon(Enemy):
    """CzarDragon enemy class"""

    _monster_id: int = 220
    _boss: bool = True
    _hp: int = 1400
    _speed: int = 20
    _attack: int = 160
    _defense: int = 100
    _magic_attack: int = 120
    _magic_defense: int = 70
    _fp: int = 100
    _evade: int = 20
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [Status.SLEEP]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # rewards
    _xp: int = 100
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.4375
    _ratio_fp: float = 0.5
    _ratio_attack: float = 0.9143
    _ratio_defense: float = 1.25
    _ratio_magic_attack: float = 1.2
    _ratio_magic_defense: float = 0.8235
    _ratio_speed: float = 1.5385
    _ratio_evade: float = 2.0
    _ratio_magic_evade: float = 0.0

    _sprite: int = 698


class Cloaker(Enemy):
    """Cloaker enemy class"""

    _monster_id: int = 221
    _boss: bool = True
    _hp: int = 1200
    _speed: int = 20
    _attack: int = 170
    _defense: int = 130
    _magic_attack: int = 12
    _magic_defense: int = 20
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 60
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.3934
    _ratio_fp: float = 0.1429
    _ratio_attack: float = 1.1688
    _ratio_defense: float = 1.3
    _ratio_magic_attack: float = 0.2105
    _ratio_magic_defense: float = 0.2222
    _ratio_speed: float = 1.1111


class Domino(Enemy):
    """Domino enemy class"""

    _monster_id: int = 222
    _boss: bool = True
    _hp: int = 900
    _speed: int = 25
    _attack: int = 65
    _defense: int = 80
    _magic_attack: int = 120
    _magic_defense: int = 150
    _fp: int = 250
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 60
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.2951
    _ratio_fp: float = 0.3571
    _ratio_attack: float = 0.4221
    _ratio_defense: float = 0.8
    _ratio_magic_attack: float = 2.1053
    _ratio_magic_defense: float = 1.6667
    _ratio_speed: float = 1.3889


class MadAdder(Enemy):
    """MadAdder enemy class"""

    _monster_id: int = 223
    _boss: bool = True
    _hp: int = 1500
    _speed: int = 10
    _attack: int = 150
    _defense: int = 70
    _magic_attack: int = 90
    _magic_defense: int = 180
    _fp: int = 250
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 200
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _common_item_drop: "Type[RegularItem]" = Crystalline
    _rare_item_drop: "Type[RegularItem]" = Crystalline

    # boss shuffle attributes
    _ratio_hp: float = 0.4918
    _ratio_fp: float = 0.3571
    _ratio_attack: float = 0.974
    _ratio_defense: float = 0.7
    _ratio_magic_attack: float = 1.5789
    _ratio_magic_defense: float = 2.0
    _ratio_speed: float = 0.5556


class Mack(Enemy):
    """Mack enemy class"""

    _monster_id: int = 224
    _boss: bool = True
    _hp: int = 480
    _speed: int = 8
    _attack: int = 22
    _defense: int = 25
    _magic_attack: int = 15
    _magic_defense: int = 20
    _fp: int = 28
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    # xp = 24
    _xp: int = 12
    # coins = 20
    _coins: int = 12
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # Boss shuffle attributes
    _anchor: bool = True
    _ratio_hp: float = 0.8

    _sprite: int = 686


class Bodyguard(Henchman):
    """Bodyguard enemy class"""

    _monster_id: int = 225
    _boss: bool = True
    _hp: int = 30
    _speed: int = 15
    _attack: int = 20
    _defense: int = 22
    _magic_attack: int = 19
    _magic_defense: int = 12
    _fp: int = 3
    _evade: int = 10
    _sound_on_hit: HitSound = HitSound.KNOCK
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # Boss shuffle attributes
    _ratio_hp: float = 0.05
    _ratio_fp: float = 0.1071
    _ratio_attack: float = 0.91
    _ratio_defense: float = 0.88
    _ratio_magic_attack: float = 1.27
    _ratio_magic_defense: float = 0.6
    _ratio_speed: float = 1.88
    _ratio_evade: float = 0.1
    _ratio_magic_evade: float = 0.0

    # this isn't from the original game
    _xp: int = 3
    _coins: int = 2


class Yaridovich(Enemy):
    """Yaridovich enemy class"""

    _monster_id: int = 226
    _boss: bool = True
    _hp: int = 1500
    _speed: int = 20
    _attack: int = 125
    _defense: int = 85
    _magic_attack: int = 70
    _magic_defense: int = 75
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 120
    _coins: int = 50
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 1.0
    _ratio_fp: float = 1.0
    # battle_push_length = 78

    _sprite: int = 692


class DrillBit(Henchman):
    """DrillBit enemy class"""

    _monster_id: int = 227
    _boss: bool = True
    _hp: int = 80
    _speed: int = 15
    _attack: int = 85
    _defense: int = 70
    _magic_attack: int = 40
    _magic_defense: int = 56
    _fp: int = 100
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # rewards
    _xp: int = 11
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # boss shuffle attributes
    _ratio_hp: float = 0.04
    _ratio_fp: float = 0.4
    _ratio_attack: float = 17 / 46
    _ratio_defense: float = 7 / 13
    _ratio_magic_attack: float = 0.4
    _ratio_magic_defense: float = 0.56
    _ratio_speed: float = 0.5
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 0.0


class YaridovichDrillBit(Henchman):
    """YaridovichDrillBit enemy class"""

    _monster_id: int = 244
    _hp: int = 80
    _speed: int = 15
    _attack: int = 85
    _defense: int = 70
    _magic_attack: int = 40
    _magic_defense: int = 56
    _fp: int = 100
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 2

    # rewards
    _xp: int = 11
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    # Attuned to ratio of machine made drill bit to machine made yarid.
    _ratio_hp: float = 180 / 800
    _ratio_fp: float = 100 / 250
    _ratio_attack: float = 130 / 180
    _ratio_defense: float = 82 / 130
    _ratio_magic_attack: float = 31 / 90
    _ratio_magic_defense: float = 69 / 50
    _ratio_speed: float = 24 / 18


class AxemPink(Henchman):
    """AxemPink enemy class"""

    _monster_id: int = 228
    _boss: bool = True
    _hp: int = 400
    _speed: int = 25
    _attack: int = 120
    _defense: int = 80
    _magic_attack: int = 80
    _magic_defense: int = 100
    _fp: int = 200
    _evade: int = 25
    _magic_evade: int = 10
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _resistances: List[Element] = [Element.ICE]
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _xp: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.1053
    _ratio_fp: float = 0.25
    _ratio_attack: float = 1.0435
    _ratio_defense: float = 0.8163
    _ratio_magic_attack: float = 2.0513
    _ratio_magic_defense: float = 1.2048
    _ratio_speed: float = 0.4808
    _ratio_evade: float = 2.2727
    _ratio_magic_evade: float = 2.0


class AxemBlack(Henchman):
    """AxemBlack enemy class"""

    _monster_id: int = 229
    _boss: bool = True
    _hp: int = 550
    _speed: int = 35
    _attack: int = 140
    _defense: int = 120
    _magic_attack: int = 4
    _magic_defense: int = 40
    _fp: int = 100
    _evade: int = 30
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 40
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.1448
    _ratio_fp: float = 0.125
    _ratio_attack: float = 1.2174
    _ratio_defense: float = 1.2245
    _ratio_magic_attack: float = 0.1026
    _ratio_magic_defense: float = 0.4819
    _ratio_speed: float = 0.6731
    _ratio_evade: float = 2.7273
    _ratio_magic_evade: float = 0.0


class Bowyer(Enemy):
    """Bowyer enemy class"""

    _monster_id: int = 230
    _boss: bool = True
    _hp: int = 720
    _speed: int = 10
    _attack: int = 50
    _defense: int = 40
    _magic_attack: int = 30
    _magic_defense: int = 35
    _fp: int = 250
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 60
    _coins: int = 50
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _common_item_drop: "Type[RegularItem]" = FlowerBox
    _rare_item_drop: "Type[RegularItem]" = FlowerBox

    _sprite: int = 688


class AeroBowyer(Henchman):
    """AeroBowyer enemy class"""

    # Borrow stats from Bob-omb to be relatively reasonable to match Bowyer
    _monster_id: int = 231
    _boss: bool = True
    _hp: int = 90
    _speed: int = 1
    _attack: int = 50
    _defense: int = 38
    _magic_attack: int = 1
    _magic_defense: int = 10
    _fp: int = 100
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 4
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.125
    _ratio_fp: float = 0.4
    _ratio_attack: float = 1.0
    _ratio_defense: float = 0.95
    _ratio_magic_attack: float = 1 / 30
    _ratio_magic_defense: float = 10 / 35
    _ratio_speed: float = 1.5
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 0.0


class AeroSmithy(Henchman):
    """AeroSmithy enemy class"""

    # Borrow stats from Poundette to be relatively reasonable to match Smithy
    _monster_id: int = 175
    _boss: bool = True
    _hp: int = 150
    _speed: int = 30
    _attack: int = 140
    _defense: int = 60
    _magic_attack: int = 66
    _magic_defense: int = 45
    _fp: int = 100
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 28
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.075
    _ratio_fp: float = 0.4
    _ratio_attack: float = 14 / 23
    _ratio_defense: float = 6 / 13
    _ratio_magic_attack: float = 0.66
    _ratio_magic_defense: float = 0.45
    _ratio_speed: float = 1.0
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 0.0


class Exor(Enemy):
    """Exor enemy class"""

    _monster_id: int = 233
    _boss: bool = True
    _hp: int = 1800
    _speed: int = 200
    _defense: int = 120
    _magic_defense: int = 80
    _ohko_immune: bool = True
    _resistances: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _xp: int = 100
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.8182
    _ratio_fp: float = 0.0
    _ratio_attack: float = 0.0
    _ratio_defense: float = 1.1111
    _ratio_magic_attack: float = 0.0
    _ratio_magic_defense: float = 1.2903
    _ratio_speed: float = 3.0769

    def update_world_entities(self):
        # replace exor revival command
        monsterscript: MonsterScript = self.world.monster_scripts.scripts[
            self.monster_id
        ]
        index, _ = monsterscript.get_command_by_name("protect_exor")
        if self.world.settings.is_boolean_flag_enabled(NoGenoWhirlExor):
            monsterscript.replace_at_index(
                index, SetUntargetable(MONSTER_1_SET, "protect_exor")
            )


class Smithy1(Enemy):
    """Smithy1 enemy class"""

    _monster_id: int = 234
    _boss: bool = True
    _hp: int = 2000
    _speed: int = 30
    _attack: int = 230
    _defense: int = 130
    _magic_attack: int = 100
    _magic_defense: int = 100
    _fp: int = 250
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    _ratio_hp: float = 2000 / 10000
    _ratio_attack: float = 230 / 186.875
    _ratio_defense: float = 130 / 121.25
    _ratio_magic_attack: float = 100 / 86
    _ratio_magic_defense: float = 100 / 97.5


class Shyper(Enemy):
    """Shyper enemy class"""

    _monster_id: int = 235
    _boss: bool = True
    _hp: int = 400
    _speed: int = 42
    _attack: int = 170
    _defense: int = 80
    _magic_attack: int = 70
    _magic_defense: int = 50
    _fp: int = 30
    _evade: int = 20
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.KNOCK
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Smithy2Body(Enemy):
    """Smithy2Body enemy class"""

    _monster_id: int = 236
    _boss: bool = True
    _hp: int = 1000
    _speed: int = 30
    _attack: int = 180
    _defense: int = 80
    _magic_attack: int = 20
    _magic_defense: int = 60
    _fp: int = 50
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    _ratio_hp: float = 1000 / 10000
    _ratio_attack: float = 180 / 186.875
    _ratio_defense: float = 80 / 121.25
    _ratio_magic_attack: float = 20 / 86
    _ratio_magic_defense: float = 60 / 97.5


class Smithy2Head(Enemy):
    """Smithy2Head enemy class"""

    _monster_id: int = 237
    _boss: bool = True
    _hp: int = 8000
    _speed: int = 40
    _attack: int = 180
    _defense: int = 80
    _magic_attack: int = 60
    _magic_defense: int = 50
    _fp: int = 50
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    _ratio_hp: float = 8000 / 10000
    _ratio_attack: float = 180 / 186.875
    _ratio_defense: float = 80 / 121.25
    _ratio_magic_attack: float = 60 / 86
    _ratio_magic_defense: float = 50 / 97.5

    def update_world_entities(self):
        monsterscript: MonsterScript = self.world.monster_scripts.scripts[
            self.monster_id
        ]

        # update HP
        _, command = monsterscript.get_command_by_name("smithy2_threshold_lowest")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.25))
        _, command = monsterscript.get_command_by_name("smithy2_threshold_mid")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.5))
        _, command = monsterscript.get_command_by_name("smithy2_threshold_highest")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.75))


class Smithy2MageHead(Enemy):
    """Smithy2MageHead enemy class"""

    _monster_id: int = 238
    _boss: bool = True
    _hp: int = 8000
    _speed: int = 35
    _attack: int = 135
    _defense: int = 50
    _magic_attack: int = 130
    _magic_defense: int = 150
    _fp: int = 250
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
    ]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    _ratio_hp: float = 8000 / 10000
    _ratio_attack: float = 135 / 186.875
    _ratio_defense: float = 50 / 121.25
    _ratio_magic_attack: float = 130 / 86
    _ratio_magic_defense: float = 150 / 97.5

    def update_world_entities(self):
        monsterscript: MonsterScript = self.world.monster_scripts.scripts[
            self.monster_id
        ]

        # update HP
        _, command = monsterscript.get_command_by_name("mage_threshold_lowest")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.25))
        _, command = monsterscript.get_command_by_name("mage_threshold_mid")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.5))
        _, command = monsterscript.get_command_by_name("mage_threshold_highest")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.75))


class Smithy2ChestHead(Enemy):
    """Smithy2ChestHead enemy class"""

    _monster_id: int = 239
    _boss: bool = True
    _hp: int = 8000
    _speed: int = 18
    _attack: int = 150
    _defense: int = 120
    _magic_attack: int = 78
    _magic_defense: int = 80
    _fp: int = 250
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _resistances: List[Element] = [Element.THUNDER]
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    _ratio_hp: float = 8000 / 10000
    _ratio_attack: float = 150 / 186.875
    _ratio_defense: float = 120 / 121.25
    _ratio_magic_attack: float = 78 / 86
    _ratio_magic_defense: float = 80 / 97.5

    def update_world_entities(self):
        monsterscript: MonsterScript = self.world.monster_scripts.scripts[
            self.monster_id
        ]

        # update HP
        _, command = monsterscript.get_command_by_name("chest_threshold_lowest")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.25))
        _, command = monsterscript.get_command_by_name("chest_threshold_mid")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.5))
        _, command = monsterscript.get_command_by_name("chest_threshold_highest")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.75))


class Croco1(Enemy):
    """Croco1 enemy class"""

    _monster_id: int = 240
    _boss: bool = True
    _hp: int = 320
    _speed: int = 16
    _attack: int = 25
    _defense: int = 25
    _magic_attack: int = 30
    _magic_defense: int = 18
    _fp: int = 12
    _evade: int = 20
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 16
    _coins: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _common_item_drop: "Type[RegularItem]" = FlowerTab
    _rare_item_drop: "Type[RegularItem]" = FlowerTab

    # boss shuffle attributes
    _ratio_hp: float = 1.0
    _ratio_fp: float = 1.0

    _name_override: str = "CROCO 1"

    def update_world_entities(self):
        monsterscript: MonsterScript = self.world.monster_scripts.scripts[
            self.monster_id
        ]

        # update HP
        _, command = monsterscript.get_command_by_name("croco_heal_threshold")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 16 / 5))


class Croco2(Enemy):
    """Croco2 enemy class"""

    _monster_id: int = 241
    _boss: bool = True
    _hp: int = 750
    _speed: int = 20
    _attack: int = 52
    _defense: int = 50
    _magic_attack: int = 27
    _magic_defense: int = 50
    _fp: int = 12
    _evade: int = 20
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 30
    _coins: int = 50
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = FlowerBox

    # boss shuffle attributes
    _ratio_hp: float = 1.0
    _ratio_fp: float = 1.0
    _name_override: str = "CROCO 2"

    def update_world_entities(self):
        monsterscript: MonsterScript = self.world.monster_scripts.scripts[
            self.monster_id
        ]

        # update HP
        _, command = monsterscript.get_command_by_name("croco2_item_steal")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 40 / 75))


class Earthlink(Enemy):
    """Earthlink enemy class"""

    _monster_id: int = 243
    _boss: bool = True
    _hp: int = 2500
    _speed: int = 16
    _attack: int = 220
    _defense: int = 120
    _magic_attack: int = 5
    _magic_defense: int = 10
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 200
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _common_item_drop: "Type[RegularItem]" = PowerBlast
    _rare_item_drop: "Type[RegularItem]" = PowerBlast

    # boss shuffle attributes
    _ratio_hp: float = 0.8197
    _ratio_fp: float = 0.1429
    _ratio_attack: float = 1.4286
    _ratio_defense: float = 1.2
    _ratio_magic_attack: float = 0.0877
    _ratio_magic_defense: float = 0.1111
    _ratio_speed: float = 0.8889


class AxemRangers(Enemy):
    """AxemRangers enemy class"""

    _monster_id: int = 245
    _boss: bool = True
    _hp: int = 999
    _speed: int = 200
    _defense: int = 100
    _magic_attack: int = 120
    _magic_defense: int = 100
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 50
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.263
    _ratio_fp: float = 0.125
    _ratio_attack: float = 0.0
    _ratio_defense: float = 1.0204
    _ratio_magic_attack: float = 3.0769
    _ratio_magic_defense: float = 1.2048
    _ratio_speed: float = 3.8462
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 0.0


class Booster(Enemy):
    """Booster enemy class"""

    _monster_id: int = 246
    _boss: bool = True
    _hp: int = 800
    _speed: int = 24
    _attack: int = 75
    _defense: int = 55
    _magic_attack: int = 1
    _magic_defense: int = 40
    _fp: int = 2
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.AMANITA_TERRAPIN
    _weaknesses: List[Element] = [Element.JUMP]
    _status_immunities: List[Status] = [Status.SLEEP]
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 60
    _coins: int = 100
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = FlowerBox

    # Boss shuffle attributes
    _anchor: bool = True
    _ratio_hp: float = 0.57
    _ratio_fp: float = 0.02

    def update_world_entities(self):
        monsterscript: MonsterScript = self.world.monster_scripts.scripts[
            self.monster_id
        ]

        # update HP
        _, command = monsterscript.get_command_by_name("booster_hits_hard")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 8 / 5))


class Booster2(Enemy):
    """Booster2 enemy class"""

    _monster_id: int = 247
    _boss: bool = True
    _hp: int = 10
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _palette: int = 16
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Snifit(Enemy):
    """Snifit enemy class"""

    _monster_id: int = 248
    _boss: bool = True
    _hp: int = 200
    _speed: int = 26
    _attack: int = 60
    _defense: int = 60
    _magic_attack: int = 20
    _magic_defense: int = 20
    _fp: int = 32
    _sound_on_hit: HitSound = HitSound.PUNCH
    _weaknesses: List[Element] = [Element.ICE]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 2
    _coins: int = 15
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = Mushroom


class SnifitHenchman(Snifit, Henchman):
    """SnifitHenchman enemy class"""

    _monster_id: int = 115

    # boss shuffle attributes
    _ratio_hp: float = 0.14
    _ratio_fp: float = 0.33
    _ratio_attack: float = 0.80
    _ratio_defense: float = 1.09
    _ratio_magic_attack: float = 1.0
    _ratio_magic_defense: float = 0.5
    _ratio_speed: float = 1.08
    _ratio_evade: float = 0.0
    _ratio_magic_evade: float = 0.0
    _xp: int = 2
    _coins: int = 15
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = Mushroom


class Johnny(Enemy):
    """Johnny enemy class"""

    _monster_id: int = 249
    _boss: bool = True
    _hp: int = 820
    _speed: int = 13
    _attack: int = 85
    _defense: int = 80
    _magic_attack: int = 25
    _magic_defense: int = 60
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _status_immunities: List[Status] = [Status.SLEEP]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 90
    _coins: int = 50
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 1.0
    _ratio_fp: float = 1.0

    _sprite: int = 691

    def update_world_entities(self):
        monsterscript: MonsterScript = self.world.monster_scripts.scripts[
            self.monster_id
        ]

        # update HP
        _, command = monsterscript.get_command_by_name("johnny_def")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 20 / 41))


class JohnnySolo(Enemy):
    """JohnnySolo enemy class"""

    _monster_id: int = 250
    _boss: bool = True
    _hp: int = 400
    _speed: int = 30
    _attack: int = 90
    _defense: int = 100
    _magic_defense: int = 32
    _fp: int = 100
    _evade: int = 10
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [Element.FIRE, Element.JUMP]
    _status_immunities: List[Status] = [Status.POISON]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.4878
    _ratio_fp: float = 1.0
    _ratio_attack: float = 1.0588
    _ratio_defense: float = 1.25
    _ratio_magic_attack: float = 0.0
    _ratio_magic_defense: float = 0.5333
    _ratio_speed: float = 2.3077
    _ratio_evade: float = 1.0
    _ratio_magic_evade: float = 1.0


class Valentina(Enemy):
    """Valentina enemy class"""

    _monster_id: int = 251
    _boss: bool = True
    _hp: int = 2000
    _speed: int = 200
    _attack: int = 120
    _defense: int = 80
    _magic_attack: int = 80
    _magic_defense: int = 60
    _fp: int = 250
    _evade: int = 10
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 24
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _xp: int = 120
    _coins: int = 200
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # Boss shuffle attributes
    _anchor: bool = True
    _ratio_hp: float = 0.8333
    _ratio_fp: float = 0.7143

    _sprite: int = 697

    def update_world_entities(self):
        monsterscript: MonsterScript = self.world.monster_scripts.scripts[
            self.monster_id
        ]

        # update HP
        _, command = monsterscript.get_command_by_name("return_dodo")
        if isinstance(command, IfHPBelow):
            command.set_threshold(self.round_for_battle_script(self.hp * 0.6))


class Cloaker2(Enemy):
    """Cloaker2 enemy class"""

    _monster_id: int = 252
    _boss: bool = True
    _hp: int = 1200
    _speed: int = 20
    _attack: int = 180
    _defense: int = 130
    _magic_attack: int = 12
    _magic_defense: int = 20
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 60
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.3934
    _ratio_fp: float = 0.1429
    _ratio_attack: float = 1.1688
    _ratio_defense: float = 1.3
    _ratio_magic_attack: float = 0.2105
    _ratio_magic_defense: float = 0.2222
    _ratio_speed: float = 1.1111


class Domino2(Enemy):
    """Domino2 enemy class"""

    _monster_id: int = 253
    _boss: bool = True
    _hp: int = 900
    _speed: int = 25
    _attack: int = 65
    _defense: int = 80
    _magic_attack: int = 120
    _magic_defense: int = 150
    _fp: int = 250
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 60
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 0.2951
    _ratio_fp: float = 0.3571
    _ratio_attack: float = 0.4221
    _ratio_defense: float = 0.8
    _ratio_magic_attack: float = 2.1053
    _ratio_magic_defense: float = 1.6667
    _ratio_speed: float = 1.3889


class Candle(Enemy):
    """Candle enemy class"""

    _monster_id: int = 254
    _boss: bool = True
    _hp: int = 10
    _fp: int = 100
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 8
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []


class Culex(Enemy):
    """Culex enemy class"""

    _monster_id: int = 255
    _boss: bool = True
    _hp: int = 4096
    _speed: int = 50
    _attack: int = 250
    _defense: int = 100
    _magic_attack: int = 100
    _magic_defense: int = 80
    _fp: int = 200
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _palette: int = 32
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 10

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 600
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    _ratio_hp: float = 1.0
    _ratio_fp: float = 1.0

    _sprite: int = 694
