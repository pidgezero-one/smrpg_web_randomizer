"""Enemy attack classes."""

from typing import List
from randomizer.types.enemy_attacks.classes import EnemyAttack
from randomizer.types.spells.enums import TempStatBuff, Status


class PhysicalAttack0(EnemyAttack):
    """PhysicalAttack0 enemy attack class"""

    _index: int = 0
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack1(EnemyAttack):
    """PhysicalAttack1 enemy attack class"""

    _index: int = 1
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack2(EnemyAttack):
    """PhysicalAttack2 enemy attack class"""

    _index: int = 2
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack3(EnemyAttack):
    """PhysicalAttack3 enemy attack class"""

    _index: int = 3
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack4(EnemyAttack):
    """PhysicalAttack4 enemy attack class"""

    _index: int = 4
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack5(EnemyAttack):
    """PhysicalAttack5 enemy attack class"""

    _index: int = 5
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack6(EnemyAttack):
    """PhysicalAttack6 enemy attack class"""

    _index: int = 6
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack7(EnemyAttack):
    """PhysicalAttack7 enemy attack class"""

    _index: int = 7
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack8(EnemyAttack):
    """PhysicalAttack8 enemy attack class"""

    _index: int = 8
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack9(EnemyAttack):
    """PhysicalAttack9 enemy attack class"""

    _index: int = 9
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack10(EnemyAttack):
    """PhysicalAttack10 enemy attack class"""

    _index: int = 10
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack11(EnemyAttack):
    """PhysicalAttack11 enemy attack class"""

    _index: int = 11
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack12(EnemyAttack):
    """PhysicalAttack12 enemy attack class"""

    _index: int = 12
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack13(EnemyAttack):
    """PhysicalAttack13 enemy attack class"""

    _index: int = 13
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack14(EnemyAttack):
    """PhysicalAttack14 enemy attack class"""

    _index: int = 14
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack15(EnemyAttack):
    """PhysicalAttack15 enemy attack class"""

    _index: int = 15
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack16(EnemyAttack):
    """PhysicalAttack16 enemy attack class"""

    _index: int = 16
    _attack_level: int = 1
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class Thornet(EnemyAttack):
    """Thornet enemy attack class"""

    _index: int = 17
    _attack_level: int = 1
    _hit_rate: int = 95
    _status_effects: List[Status] = [Status.POISON]
    _buffs: List[TempStatBuff] = []


class PhysicalAttack18(EnemyAttack):
    """PhysicalAttack18 enemy attack class"""

    _index: int = 18
    _attack_level: int = 3
    _hit_rate: int = 90
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class Funguspike(EnemyAttack):
    """Funguspike enemy attack class"""

    _index: int = 19
    _attack_level: int = 2
    _hit_rate: int = 95
    _status_effects: List[Status] = [Status.MUSHROOM]
    _buffs: List[TempStatBuff] = []


class PhysicalAttack20(EnemyAttack):
    """PhysicalAttack20 enemy attack class"""

    _index: int = 20
    _attack_level: int = 1
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack21(EnemyAttack):
    """PhysicalAttack21 enemy attack class"""

    _index: int = 21
    _attack_level: int = 2
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class FullHouse(EnemyAttack):
    """FullHouse enemy attack class"""

    _index: int = 22
    _attack_level: int = 2
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class WildCard(EnemyAttack):
    """WildCard enemy attack class"""

    _index: int = 23
    _attack_level: int = 3
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class RoyalFlush(EnemyAttack):
    """RoyalFlush enemy attack class"""

    _index: int = 24
    _attack_level: int = 4
    _hit_rate: int = 90
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack25(EnemyAttack):
    """PhysicalAttack25 enemy attack class"""

    _index: int = 25
    _attack_level: int = 1
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class SpritzBomb(EnemyAttack):
    """SpritzBomb enemy attack class"""

    _index: int = 26
    _attack_level: int = 2
    _hit_rate: int = 90
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack27(EnemyAttack):
    """PhysicalAttack27 enemy attack class"""

    _index: int = 27
    _attack_level: int = 1
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack28(EnemyAttack):
    """PhysicalAttack28 enemy attack class"""

    _index: int = 28
    _attack_level: int = 1
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack29(EnemyAttack):
    """PhysicalAttack29 enemy attack class"""

    _index: int = 29
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class Blazer(EnemyAttack):
    """Blazer enemy attack class"""

    _index: int = 30
    _ohko: bool = True
    _hide_numbers: bool = True
    _hit_rate: int = 90
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack31(EnemyAttack):
    """PhysicalAttack31 enemy attack class"""

    _index: int = 31
    _attack_level: int = 2
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack32(EnemyAttack):
    """PhysicalAttack32 enemy attack class"""

    _index: int = 32
    _attack_level: int = 2
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class Echofinder(EnemyAttack):
    """Echofinder enemy attack class"""

    _index: int = 33
    _attack_level: int = 1
    _hit_rate: int = 95
    _status_effects: List[Status] = [Status.MUTE]
    _buffs: List[TempStatBuff] = []


class ScrowBell(EnemyAttack):
    """ScrowBell enemy attack class"""

    _index: int = 34
    _damageless_flag_1: bool = True
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 90
    _status_effects: List[Status] = [Status.SCARECROW]
    _buffs: List[TempStatBuff] = []


class DoomReverb(EnemyAttack):
    """DoomReverb enemy attack class"""

    _index: int = 35
    _damageless_flag_1: bool = True
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 90
    _status_effects: List[Status] = [Status.MUTE]
    _buffs: List[TempStatBuff] = []


class SporeChimes(EnemyAttack):
    """SporeChimes enemy attack class"""

    _index: int = 36
    _damageless_flag_1: bool = True
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 90
    _status_effects: List[Status] = [Status.MUSHROOM]
    _buffs: List[TempStatBuff] = []


class InkBlast(EnemyAttack):
    """InkBlast enemy attack class"""

    _index: int = 37
    _attack_level: int = 1
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class GunkBall(EnemyAttack):
    """GunkBall enemy attack class"""

    _index: int = 38
    _attack_level: int = 1
    _hit_rate: int = 95
    _status_effects: List[Status] = [Status.MUTE]
    _buffs: List[TempStatBuff] = []


class Endobubble(EnemyAttack):
    """Endobubble enemy attack class"""

    _index: int = 39
    _damageless_flag_1: bool = True
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 90
    _status_effects: List[Status] = [Status.FEAR]
    _buffs: List[TempStatBuff] = []


class PhysicalAttack40(EnemyAttack):
    """PhysicalAttack40 enemy attack class"""

    _index: int = 40
    _attack_level: int = 1
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class SleepSauce(EnemyAttack):
    """SleepSauce enemy attack class"""

    _index: int = 41
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 95
    _status_effects: List[Status] = [Status.SLEEP]
    _buffs: List[TempStatBuff] = []


class VenomDrool(EnemyAttack):
    """VenomDrool enemy attack class"""

    _index: int = 42
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 95
    _status_effects: List[Status] = [Status.POISON]
    _buffs: List[TempStatBuff] = []


class MushFunk(EnemyAttack):
    """MushFunk enemy attack class"""

    _index: int = 43
    _damageless_flag_1: bool = True
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 90
    _status_effects: List[Status] = [Status.MUSHROOM]
    _buffs: List[TempStatBuff] = []


class ScrowFunk(EnemyAttack):
    """ScrowFunk enemy attack class"""

    _index: int = 44
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 90
    _status_effects: List[Status] = [Status.SCARECROW]
    _buffs: List[TempStatBuff] = []


class Stench(EnemyAttack):
    """Stench enemy attack class"""

    _index: int = 45
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 90
    _status_effects: List[Status] = [Status.POISON]
    _buffs: List[TempStatBuff] = []


class PhysicalAttack46(EnemyAttack):
    """PhysicalAttack46 enemy attack class"""

    _index: int = 46
    _attack_level: int = 1
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack47(EnemyAttack):
    """PhysicalAttack47 enemy attack class"""

    _index: int = 47
    _attack_level: int = 2
    _hit_rate: int = 90
    _status_effects: List[Status] = [Status.FEAR]
    _buffs: List[TempStatBuff] = []


class ViroPlasm(EnemyAttack):
    """ViroPlasm enemy attack class"""

    _index: int = 48
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 90
    _status_effects: List[Status] = [Status.POISON]
    _buffs: List[TempStatBuff] = []


class PsychoPlasm(EnemyAttack):
    """PsychoPlasm enemy attack class"""

    _index: int = 49
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 90
    _status_effects: List[Status] = [Status.FEAR]
    _buffs: List[TempStatBuff] = []


class PhysicalAttack50(EnemyAttack):
    """PhysicalAttack50 enemy attack class"""

    _index: int = 50
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 90
    _status_effects: List[Status] = [Status.MUTE]
    _buffs: List[TempStatBuff] = []


class PhysicalAttack51(EnemyAttack):
    """PhysicalAttack51 enemy attack class"""

    _index: int = 51
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 90
    _status_effects: List[Status] = [Status.SLEEP]
    _buffs: List[TempStatBuff] = []


class PollenNap(EnemyAttack):
    """PollenNap enemy attack class"""

    _index: int = 52
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 90
    _status_effects: List[Status] = [Status.SLEEP]
    _buffs: List[TempStatBuff] = []


class ScrowDust(EnemyAttack):
    """ScrowDust enemy attack class"""

    _index: int = 53
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 90
    _status_effects: List[Status] = [Status.SCARECROW]
    _buffs: List[TempStatBuff] = []


class Sporocyst(EnemyAttack):
    """Sporocyst enemy attack class"""

    _index: int = 54
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 90
    _status_effects: List[Status] = [Status.MUSHROOM]
    _buffs: List[TempStatBuff] = []


class Toxicyst(EnemyAttack):
    """Toxicyst enemy attack class"""

    _index: int = 55
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 90
    _status_effects: List[Status] = [Status.POISON]
    _buffs: List[TempStatBuff] = []


class PhysicalAttack56(EnemyAttack):
    """PhysicalAttack56 enemy attack class"""

    _index: int = 56
    _attack_level: int = 1
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack57(EnemyAttack):
    """PhysicalAttack57 enemy attack class"""

    _index: int = 57
    _attack_level: int = 2
    _hit_rate: int = 90
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class LullaBye(EnemyAttack):
    """LullaBye enemy attack class"""

    _index: int = 58
    _damageless_flag_1: bool = True
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 99
    _status_effects: List[Status] = [Status.SLEEP]
    _buffs: List[TempStatBuff] = []


class Elegy(EnemyAttack):
    """Elegy enemy attack class"""

    _index: int = 59
    _damageless_flag_1: bool = True
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 99
    _status_effects: List[Status] = [Status.MUTE]
    _buffs: List[TempStatBuff] = []


class Backfire(EnemyAttack):
    """Backfire enemy attack class"""

    _index: int = 60
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class VaVaVoom(EnemyAttack):
    """VaVaVoom enemy attack class"""

    _index: int = 61
    _attack_level: int = 1
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class FunRun(EnemyAttack):
    """FunRun enemy attack class"""

    _index: int = 62
    _attack_level: int = 1
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class BodySlam(EnemyAttack):
    """BodySlam enemy attack class"""

    _index: int = 63
    _attack_level: int = 2
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class Howl(EnemyAttack):
    """Howl enemy attack class"""

    _index: int = 64
    _damageless_flag_1: bool = True
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 99
    _status_effects: List[Status] = [Status.FEAR]
    _buffs: List[TempStatBuff] = []


class Scream(EnemyAttack):
    """Scream enemy attack class"""

    _index: int = 65
    _damageless_flag_1: bool = True
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 99
    _status_effects: List[Status] = [Status.FEAR]
    _buffs: List[TempStatBuff] = []


class IronMaiden(EnemyAttack):
    """IronMaiden enemy attack class"""

    _index: int = 66
    _damageless_flag_1: bool = True
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 99
    _status_effects: List[Status] = [Status.FEAR]
    _buffs: List[TempStatBuff] = []


class Fangs(EnemyAttack):
    """Fangs enemy attack class"""

    _index: int = 67
    _attack_level: int = 1
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class Poison(EnemyAttack):
    """Poison enemy attack class"""

    _index: int = 68
    _attack_level: int = 1
    _hit_rate: int = 95
    _status_effects: List[Status] = [Status.POISON]
    _buffs: List[TempStatBuff] = []


class CarniKiss(EnemyAttack):
    """CarniKiss enemy attack class"""

    _index: int = 69
    _attack_level: int = 2
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class Claw(EnemyAttack):
    """Claw enemy attack class"""

    _index: int = 70
    _attack_level: int = 2
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class Grinder(EnemyAttack):
    """Grinder enemy attack class"""

    _index: int = 71
    _attack_level: int = 2
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class DarkClaw(EnemyAttack):
    """DarkClaw enemy attack class"""

    _index: int = 72
    _attack_level: int = 1
    _hit_rate: int = 95
    _status_effects: List[Status] = [Status.POISON]
    _buffs: List[TempStatBuff] = []


class Scythe(EnemyAttack):
    """Scythe enemy attack class"""

    _index: int = 73
    _ohko: bool = True
    _hide_numbers: bool = True
    _hit_rate: int = 90
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class Sickle(EnemyAttack):
    """Sickle enemy attack class"""

    _index: int = 74
    _attack_level: int = 1
    _hit_rate: int = 95
    _status_effects: List[Status] = [Status.SCARECROW]
    _buffs: List[TempStatBuff] = []


class Deathsickle(EnemyAttack):
    """Deathsickle enemy attack class"""

    _index: int = 75
    _attack_level: int = 2
    _hit_rate: int = 95
    _status_effects: List[Status] = [Status.FEAR]
    _buffs: List[TempStatBuff] = []


class EerieJig(EnemyAttack):
    """EerieJig enemy attack class"""

    _index: int = 76
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 99
    _status_effects: List[Status] = [Status.SCARECROW]
    _buffs: List[TempStatBuff] = []


class SomnusWaltz(EnemyAttack):
    """SomnusWaltz enemy attack class"""

    _index: int = 77
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 99
    _status_effects: List[Status] = [Status.SLEEP]
    _buffs: List[TempStatBuff] = []


class DahliaDance(EnemyAttack):
    """DahliaDance enemy attack class"""

    _index: int = 78
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 99
    _status_effects: List[Status] = [Status.MUSHROOM]
    _buffs: List[TempStatBuff] = []


class Skewer(EnemyAttack):
    """Skewer enemy attack class"""

    _index: int = 79
    _attack_level: int = 1
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class Pierce(EnemyAttack):
    """Pierce enemy attack class"""

    _index: int = 80
    _attack_level: int = 2
    _hit_rate: int = 90
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack81(EnemyAttack):
    """PhysicalAttack81 enemy attack class"""

    _index: int = 81
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class Magnum(EnemyAttack):
    """Magnum enemy attack class"""

    _index: int = 82
    _ohko: bool = True
    _hide_numbers: bool = True
    _hit_rate: int = 90
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class Psyche(EnemyAttack):
    """Psyche enemy attack class"""

    _index: int = 83
    _ohko: bool = True
    _hide_numbers: bool = True
    _hit_rate: int = 80
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class Migraine(EnemyAttack):
    """Migraine enemy attack class"""

    _index: int = 84
    _ohko: bool = True
    _hide_numbers: bool = True
    _hit_rate: int = 80
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack85(EnemyAttack):
    """PhysicalAttack85 enemy attack class"""

    _index: int = 85
    _hit_rate: int = 99
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack86(EnemyAttack):
    """PhysicalAttack86 enemy attack class"""

    _index: int = 86
    _attack_level: int = 2
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class Multistrike(EnemyAttack):
    """Multistrike enemy attack class"""

    _index: int = 87
    _attack_level: int = 1
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class FlutterHush(EnemyAttack):
    """FlutterHush enemy attack class"""

    _index: int = 88
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 90
    _status_effects: List[Status] = [Status.MUTE]
    _buffs: List[TempStatBuff] = []


class PhysicalAttack89(EnemyAttack):
    """PhysicalAttack89 enemy attack class"""

    _index: int = 89
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack90(EnemyAttack):
    """PhysicalAttack90 enemy attack class"""

    _index: int = 90
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack91(EnemyAttack):
    """PhysicalAttack91 enemy attack class"""

    _index: int = 91
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 85
    _status_effects: List[Status] = [Status.SLEEP]
    _buffs: List[TempStatBuff] = []


class FearRoulette(EnemyAttack):
    """FearRoulette enemy attack class"""

    _index: int = 92
    _ohko: bool = True
    _hide_numbers: bool = True
    _hit_rate: int = 99
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack93(EnemyAttack):
    """PhysicalAttack93 enemy attack class"""

    _index: int = 93
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack94(EnemyAttack):
    """PhysicalAttack94 enemy attack class"""

    _index: int = 94
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack95(EnemyAttack):
    """PhysicalAttack95 enemy attack class"""

    _index: int = 95
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class HammerTime(EnemyAttack):
    """HammerTime enemy attack class"""

    _index: int = 96
    _attack_level: int = 2
    _hit_rate: int = 90
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class ValorUp(EnemyAttack):
    """ValorUp enemy attack class"""

    _index: int = 97
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 100
    _buffs: List[TempStatBuff] = [TempStatBuff.MAGIC_DEFENSE, TempStatBuff.DEFENSE]
    _status_effects: List[Status] = []


class PhysicalAttack98(EnemyAttack):
    """PhysicalAttack98 enemy attack class"""

    _index: int = 98
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class LastShot(EnemyAttack):
    """LastShot enemy attack class"""

    _index: int = 99
    _attack_level: int = 3
    _hit_rate: int = 100
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack100(EnemyAttack):
    """PhysicalAttack100 enemy attack class"""

    _index: int = 100
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack101(EnemyAttack):
    """PhysicalAttack101 enemy attack class"""

    _index: int = 101
    _attack_level: int = 1
    _hit_rate: int = 90
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack102(EnemyAttack):
    """PhysicalAttack102 enemy attack class"""

    _index: int = 102
    _hit_rate: int = 100
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack103(EnemyAttack):
    """PhysicalAttack103 enemy attack class"""

    _index: int = 103
    _hit_rate: int = 100
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack104(EnemyAttack):
    """PhysicalAttack104 enemy attack class"""

    _index: int = 104
    _hit_rate: int = 100
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack105(EnemyAttack):
    """PhysicalAttack105 enemy attack class"""

    _index: int = 105
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class Gnight(EnemyAttack):
    """Gnight enemy attack class"""

    _index: int = 106
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 90
    _status_effects: List[Status] = [Status.SLEEP]
    _buffs: List[TempStatBuff] = []


class PhysicalAttack107(EnemyAttack):
    """PhysicalAttack107 enemy attack class"""

    _index: int = 107
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack108(EnemyAttack):
    """PhysicalAttack108 enemy attack class"""

    _index: int = 108
    _hit_rate: int = 100
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class Chomp(EnemyAttack):
    """Chomp enemy attack class"""

    _index: int = 109
    _attack_level: int = 2
    _hit_rate: int = 90
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class GetTough(EnemyAttack):
    """GetTough enemy attack class"""

    _index: int = 110
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 100
    _buffs: List[TempStatBuff] = [TempStatBuff.MAGIC_DEFENSE, TempStatBuff.DEFENSE]
    _status_effects: List[Status] = []


class PhysicalAttack111(EnemyAttack):
    """PhysicalAttack111 enemy attack class"""

    _index: int = 111
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class Missedme(EnemyAttack):
    """Missedme enemy attack class"""

    _index: int = 112
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack113(EnemyAttack):
    """PhysicalAttack113 enemy attack class"""

    _index: int = 113
    _attack_level: int = 1
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class LocoExpress(EnemyAttack):
    """LocoExpress enemy attack class"""

    _index: int = 114
    _attack_level: int = 3
    _hit_rate: int = 90
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack115(EnemyAttack):
    """PhysicalAttack115 enemy attack class"""

    _index: int = 115
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack116(EnemyAttack):
    """PhysicalAttack116 enemy attack class"""

    _index: int = 116
    _attack_level: int = 1
    _hit_rate: int = 90
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack117(EnemyAttack):
    """PhysicalAttack117 enemy attack class"""

    _index: int = 117
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class PhysicalAttack118(EnemyAttack):
    """PhysicalAttack118 enemy attack class"""

    _index: int = 118
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class Jinxed(EnemyAttack):
    """Jinxed enemy attack class"""

    _index: int = 119
    _hit_rate: int = 100
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class TripleKick(EnemyAttack):
    """TripleKick enemy attack class"""

    _index: int = 120
    _attack_level: int = 1
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class Quicksilver(EnemyAttack):
    """Quicksilver enemy attack class"""

    _index: int = 121
    _attack_level: int = 2
    _hit_rate: int = 90
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class BombsAway(EnemyAttack):
    """BombsAway enemy attack class"""

    _index: int = 122
    _attack_level: int = 3
    _hit_rate: int = 90
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class Vigorup(EnemyAttack):
    """Vigorup enemy attack class"""

    _index: int = 123
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 100
    _buffs: List[TempStatBuff] = [TempStatBuff.MAGIC_ATTACK, TempStatBuff.ATTACK]
    _status_effects: List[Status] = []


class PhysicalAttack124(EnemyAttack):
    """PhysicalAttack124 enemy attack class"""

    _index: int = 124
    _hit_rate: int = 100
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class SilverBullet(EnemyAttack):
    """SilverBullet enemy attack class"""

    _index: int = 125
    _ohko: bool = True
    _hide_numbers: bool = True
    _hit_rate: int = 99
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class Terrapunch(EnemyAttack):
    """Terrapunch enemy attack class"""

    _index: int = 126
    _attack_level: int = 2
    _hit_rate: int = 95
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class ScrowFangs(EnemyAttack):
    """ScrowFangs enemy attack class"""

    _index: int = 127
    _hide_numbers: bool = True
    _damageless_flag_2: bool = True
    _hit_rate: int = 85
    _status_effects: List[Status] = [Status.SCARECROW]
    _buffs: List[TempStatBuff] = []


class Shaker(EnemyAttack):
    """Shaker enemy attack class"""

    _index: int = 128
    _ohko: bool = True
    _hide_numbers: bool = True
    _hit_rate: int = 99
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


class AttackDoNothing(EnemyAttack):
    """AttackDoNothing enemy attack class"""

    _index: int = 251
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []


# ********************* Default lists for the world.


def get_default_enemy_attacks(world):
    """

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        list[EnemyAttack]: Default list of objects for the world.

    """
    return [
        PhysicalAttack0(world),
        PhysicalAttack2(world),
        PhysicalAttack4(world),
        PhysicalAttack5(world),
        PhysicalAttack6(world),
        PhysicalAttack7(world),
        PhysicalAttack8(world),
        PhysicalAttack9(world),
        PhysicalAttack10(world),
        PhysicalAttack11(world),
        PhysicalAttack12(world),
        PhysicalAttack15(world),
        Thornet(world),
        PhysicalAttack18(world),
        Funguspike(world),
        PhysicalAttack20(world),
        PhysicalAttack21(world),
        FullHouse(world),
        WildCard(world),
        RoyalFlush(world),
        SpritzBomb(world),
        PhysicalAttack27(world),
        PhysicalAttack28(world),
        PhysicalAttack29(world),
        Blazer(world),
        PhysicalAttack31(world),
        PhysicalAttack32(world),
        Echofinder(world),
        ScrowBell(world),
        DoomReverb(world),
        SporeChimes(world),
        InkBlast(world),
        GunkBall(world),
        Endobubble(world),
        PhysicalAttack40(world),
        VenomDrool(world),
        MushFunk(world),
        Stench(world),
        PhysicalAttack46(world),
        PhysicalAttack47(world),
        ViroPlasm(world),
        PsychoPlasm(world),
        PhysicalAttack50(world),
        PhysicalAttack51(world),
        PollenNap(world),
        ScrowDust(world),
        Sporocyst(world),
        Toxicyst(world),
        PhysicalAttack56(world),
        PhysicalAttack57(world),
        LullaBye(world),
        Elegy(world),
        Backfire(world),
        VaVaVoom(world),
        FunRun(world),
        BodySlam(world),
        Howl(world),
        Scream(world),
        IronMaiden(world),
        Fangs(world),
        Poison(world),
        CarniKiss(world),
        Claw(world),
        Grinder(world),
        DarkClaw(world),
        Scythe(world),
        Sickle(world),
        Deathsickle(world),
        EerieJig(world),
        SomnusWaltz(world),
        DahliaDance(world),
        Skewer(world),
        Pierce(world),
        PhysicalAttack81(world),
        Magnum(world),
        Psyche(world),
        Migraine(world),
        PhysicalAttack85(world),
        PhysicalAttack86(world),
        Multistrike(world),
        FlutterHush(world),
        PhysicalAttack89(world),
        PhysicalAttack90(world),
        PhysicalAttack91(world),
        FearRoulette(world),
        PhysicalAttack93(world),
        PhysicalAttack94(world),
        PhysicalAttack95(world),
        ValorUp(world),
        LastShot(world),
        PhysicalAttack101(world),
        PhysicalAttack105(world),
        Gnight(world),
        PhysicalAttack107(world),
        PhysicalAttack108(world),
        Chomp(world),
        GetTough(world),
        PhysicalAttack111(world),
        Missedme(world),
        PhysicalAttack113(world),
        LocoExpress(world),
        PhysicalAttack115(world),
        PhysicalAttack116(world),
        PhysicalAttack117(world),
        PhysicalAttack118(world),
        Jinxed(world),
        TripleKick(world),
        Quicksilver(world),
        BombsAway(world),
        Vigorup(world),
        SilverBullet(world),
        Terrapunch(world),
        ScrowFangs(world),
        Shaker(world),
    ]
