from smrpgpatchbuilder.datatypes.enemy_attacks.classes import EnemyAttack as EnemyAttackBase, EnemyAttackCollection
from smrpgpatchbuilder.datatypes.spells.enums import Status, TempStatBuff
from smrpgpatchbuilder.datatypes.items.enums import ItemPrefix

class EnemyAttack(EnemyAttackBase):
    _remake_name: Optional[str] = None

    @property
    def remake_name(self) -> str:
        return self._remake_name or self._name



class Attack0(EnemyAttack):
    _index = 0
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class Attack1(EnemyAttack):
    _index = 1
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class Attack2(EnemyAttack):
    _index = 2
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class Attack3(EnemyAttack):
    _index = 3
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class Attack4(EnemyAttack):
    _index = 4
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class Attack5(EnemyAttack):
    _index = 5
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class Attack6(EnemyAttack):
    _index = 6
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class ATKDEF100Attack(EnemyAttack):
    _index = 7
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 100


class Attack8(EnemyAttack):
    _index = 8
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class Attack9(EnemyAttack):
    _index = 9
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class Attack10(EnemyAttack):
    _index = 10
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class Attack11(EnemyAttack):
    _index = 11
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class Attack12(EnemyAttack):
    _index = 12
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class Attack13(EnemyAttack):
    _index = 13
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class Attack14(EnemyAttack):
    _index = 14
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class Attack15(EnemyAttack):
    _index = 15
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class Attack16(EnemyAttack):
    _index = 16
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class ThornetAttack(EnemyAttack):
    _index = 17
    _name = ' Thornet'
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95
    _status_effects = [Status.POISON]


class FinalClawAttack(EnemyAttack):
    _index = 18
    _name = ' Final Claw'
    _attack_level = 0
    _ohko = True
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = False
    _hit_rate = 100


class FunguspikeAttack(EnemyAttack):
    _index = 19
    _name = ' Funguspike'
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95
    _status_effects = [Status.MUSHROOM]


class Attack20(EnemyAttack):
    _index = 20
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class Attack21(EnemyAttack):
    _index = 21
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class FullHouseAttack(EnemyAttack):
    _index = 22
    _name = ' Full House'
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95

    _remake_name = " Card Toss"


class WildCardAttack(EnemyAttack):
    _index = 23
    _name = ' Wild Card'
    _attack_level = 3
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95

    _remake_name = " Card Rain"


class ATKMATK5Attack(EnemyAttack):
    _index = 24
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 100


class Attack25(EnemyAttack):
    _index = 25
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class SpritzBombAttack(EnemyAttack):
    _index = 26
    _name = ' Spritz Bomb'
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 90


class Attack27(EnemyAttack):
    _index = 27
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class Attack28(EnemyAttack):
    _index = 28
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class Attack29(EnemyAttack):
    _index = 29
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class BlazerAttack(EnemyAttack):
    _index = 30
    _name = ' Blazer'
    _attack_level = 0
    _ohko = True
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = False
    _hit_rate = 90


class Attack31(EnemyAttack):
    _index = 31
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class Attack32(EnemyAttack):
    _index = 32
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class EchofinderAttack(EnemyAttack):
    _index = 33
    _name = ' Echofinder'
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95
    _status_effects = [Status.MUTE]


class ScrowBellAttack(EnemyAttack):
    _index = 34
    _name = " S'crow Bell"
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = True
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 90
    _status_effects = [Status.SCARECROW]


class DoomReverbAttack(EnemyAttack):
    _index = 35
    _name = ' Doom Reverb'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = True
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 90
    _status_effects = [Status.MUTE]


class SporeChimesAttack(EnemyAttack):
    _index = 36
    _name = ' Spore Chimes'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = True
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 90
    _status_effects = [Status.MUSHROOM]


class InkBlastAttack(EnemyAttack):
    _index = 37
    _name = ' Ink Blast'
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class GunkBallAttack(EnemyAttack):
    _index = 38
    _name = ' Gunk Ball'
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95
    _status_effects = [Status.MUTE]


class EndobubbleAttack(EnemyAttack):
    _index = 39
    _name = ' Endobubble'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = True
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 90
    _status_effects = [Status.FEAR]


class DUMMYAttack1(EnemyAttack):
    _index = 40
    _name = 'DUMMY'
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class SleepSauceAttack(EnemyAttack):
    _index = 41
    _name = ' Sleep-Sauce'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 95
    _status_effects = [Status.SLEEP]


class VenomDroolAttack(EnemyAttack):
    _index = 42
    _name = ' Venom Drool'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 95
    _status_effects = [Status.POISON]


class MushFunkAttack(EnemyAttack):
    _index = 43
    _name = ' Mush Funk'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = True
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 90
    _status_effects = [Status.MUSHROOM]

    _remake_name = " MushroomFunk"


class ScrowFunkAttack(EnemyAttack):
    _index = 44
    _name = " S'crow Funk"
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 90
    _status_effects = [Status.SCARECROW]


class StenchAttack(EnemyAttack):
    _index = 45
    _name = ' Stench'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 90
    _status_effects = [Status.POISON]


class Attack46(EnemyAttack):
    _index = 46
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class Attack47(EnemyAttack):
    _index = 47
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 90
    _status_effects = [Status.FEAR]


class ViroPlasmAttack(EnemyAttack):
    _index = 48
    _name = ' Viro Plasm'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 90
    _status_effects = [Status.POISON]


class PsychoPlasmAttack(EnemyAttack):
    _index = 49
    _name = ' Psycho Plasm'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 90
    _status_effects = [Status.FEAR]


class Attack50(EnemyAttack):
    _index = 50
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 90
    _status_effects = [Status.MUTE]


class Attack51(EnemyAttack):
    _index = 51
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 90
    _status_effects = [Status.SLEEP]


class PollenNapAttack(EnemyAttack):
    _index = 52
    _name = ' Pollen Nap'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 90
    _status_effects = [Status.SLEEP]


class ScrowDustAttack(EnemyAttack):
    _index = 53
    _name = " S'crow Dust"
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 90
    _status_effects = [Status.SCARECROW]


class SporocystAttack(EnemyAttack):
    _index = 54
    _name = ' Sporocyst'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 90
    _status_effects = [Status.MUSHROOM]


class ATKMATKneg5Attack(EnemyAttack):
    _index = 55
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 100


class Attack56(EnemyAttack):
    _index = 56
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class Attack57(EnemyAttack):
    _index = 57
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 90


class LullaByeAttack(EnemyAttack):
    _index = 58
    _name = ' Lulla-Bye'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = True
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 99
    _status_effects = [Status.SLEEP]


class ElegyAttack(EnemyAttack):
    _index = 59
    _name = ' Elegy'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = True
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 99
    _status_effects = [Status.MUTE]


class BackfireAttack(EnemyAttack):
    _index = 60
    _name = ' Backfire'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class VaVaVoomAttack(EnemyAttack):
    _index = 61
    _name = ' Va Va Voom'
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class FunRunAttack(EnemyAttack):
    _index = 62
    _name = ' Fun & Run'
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class BodySlamAttack(EnemyAttack):
    _index = 63
    _name = ' Body Slam'
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class HowlAttack(EnemyAttack):
    _index = 64
    _name = ' Howl'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = True
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 99
    _status_effects = [Status.FEAR]


class ScreamAttack(EnemyAttack):
    _index = 65
    _name = ' Scream'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = True
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 99
    _status_effects = [Status.FEAR]


class IronMaidenAttack(EnemyAttack):
    _index = 66
    _name = ' Iron Maiden'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = True
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 99
    _status_effects = [Status.FEAR]


class FangsAttack(EnemyAttack):
    _index = 67
    _name = ' Fangs'
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class PoisonAttack(EnemyAttack):
    _index = 68
    _name = ' Poison'
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95
    _status_effects = [Status.POISON]


class CarniKissAttack(EnemyAttack):
    _index = 69
    _name = ' Carni-Kiss'
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class ClawAttack(EnemyAttack):
    _index = 70
    _name = ' Claw'
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class GrinderAttack(EnemyAttack):
    _index = 71
    _name = ' Grinder'
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class DarkClawAttack(EnemyAttack):
    _index = 72
    _name = ' Dark Claw'
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95
    _status_effects = [Status.POISON]


class ScytheAttack(EnemyAttack):
    _index = 73
    _name = ' Scythe'
    _attack_level = 0
    _ohko = True
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = False
    _hit_rate = 90


class MoralSupportAttack(EnemyAttack):
    _index = 74
    _name = ' Moral Support'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 100


class DeathsickleAttack(EnemyAttack):
    _index = 75
    _name = ' Deathsickle'
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95
    _status_effects = [Status.FEAR]


class EerieJigAttack(EnemyAttack):
    _index = 76
    _name = ' Eerie Jig'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 99
    _status_effects = [Status.SCARECROW]


class SomnusWaltzAttack(EnemyAttack):
    _index = 77
    _name = ' Somnus Waltz'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 99
    _status_effects = [Status.SLEEP]


class BOBOMBSUPERAttack(EnemyAttack):
    _index = 78
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 100


class SkewerAttack(EnemyAttack):
    _index = 79
    _name = ' Skewer'
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class PierceAttack(EnemyAttack):
    _index = 80
    _name = ' Pierce'
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 90


class MagicForceAttack(EnemyAttack):
    _index = 81
    _name = 'Magic Force'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 100
    _buffs = [TempStatBuff(3), TempStatBuff(5)]


class MagnumAttack(EnemyAttack):
    _index = 82
    _name = ' Magnum'
    _attack_level = 0
    _ohko = True
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = False
    _hit_rate = 90


class PsycheAttack(EnemyAttack):
    _index = 83
    _name = ' Psyche!'
    _attack_level = 0
    _ohko = True
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = False
    _hit_rate = 80


class MigraineAttack(EnemyAttack):
    _index = 84
    _name = ' Migraine'
    _attack_level = 0
    _ohko = True
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = False
    _hit_rate = 80


class BOBOMBBOMBAttack(EnemyAttack):
    _index = 85
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 99


class Attack86(EnemyAttack):
    _index = 86
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class MultistrikeAttack(EnemyAttack):
    _index = 87
    _name = ' Multistrike'
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class FlutterHushAttack(EnemyAttack):
    _index = 88
    _name = ' Flutter Hush'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 90
    _status_effects = [Status.MUTE]


class Attack89(EnemyAttack):
    _index = 89
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class Attack90(EnemyAttack):
    _index = 90
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class CULEXTURNSAttack(EnemyAttack):
    _index = 91
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 100


class FearRouletteAttack(EnemyAttack):
    _index = 92
    _name = 'Fear Roulette'
    _attack_level = 0
    _ohko = True
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = False
    _hit_rate = 99


class ValorForceAttack(EnemyAttack):
    _index = 93
    _name = ' Valor Force'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 100
    _buffs = [TempStatBuff(6)]


class MeteorAttack(EnemyAttack):
    _index = 94
    _name = ' Meteor'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 100


class VigorForceAttack(EnemyAttack):
    _index = 95
    _name = ' Vigor Force'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 100
    _buffs = [TempStatBuff(4)]


class HammerTimeAttack(EnemyAttack):
    _index = 96
    _name = ' Hammer Time'
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 90


class ValorUpAttack(EnemyAttack):
    _index = 97
    _name = ' Valor Up'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 100
    _buffs = [TempStatBuff(5), TempStatBuff(6)]


class DUMMYAttack2(EnemyAttack):
    _index = 98
    _name = 'DUMMY'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class LastShotAttack(EnemyAttack):
    _index = 99
    _name = ' Last Shot!'
    _attack_level = 3
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 100

    _remake_name = " Last Shot"


class DUMMYAttack3(EnemyAttack):
    _index = 100
    _name = 'DUMMY'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class DUMMYAttack4(EnemyAttack):
    _index = 101
    _name = 'DUMMY'
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 90


class DUMMYAttack5(EnemyAttack):
    _index = 102
    _name = 'DUMMY'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 100


class DUMMYAttack6(EnemyAttack):
    _index = 103
    _name = 'DUMMY'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 100


class DUMMYAttack7(EnemyAttack):
    _index = 104
    _name = 'DUMMY'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 100


class DUMMYAttack8(EnemyAttack):
    _index = 105
    _name = 'DUMMY'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class GnightAttack(EnemyAttack):
    _index = 106
    _name = " G'night"
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 90
    _status_effects = [Status.SLEEP]


class DUMMYAttack9(EnemyAttack):
    _index = 107
    _name = 'DUMMY'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class DUMMYAttack10(EnemyAttack):
    _index = 108
    _name = 'DUMMY'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 100


class ChompAttack(EnemyAttack):
    _index = 109
    _name = ' Chomp'
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 90

    _remake_name = " Monster Toss"


class GetToughAttack(EnemyAttack):
    _index = 110
    _name = ' Get Tough!'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 100
    _buffs = [TempStatBuff(5), TempStatBuff(6)]


class DUMMYAttack11(EnemyAttack):
    _index = 111
    _name = 'DUMMY'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class MissedmeAttack(EnemyAttack):
    _index = 112
    _name = ' Missed me!'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 95


class DUMMYAttack12(EnemyAttack):
    _index = 113
    _name = 'DUMMY'
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class LocoExpressAttack(EnemyAttack):
    _index = 114
    _name = ' Loco Express'
    _attack_level = 3
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 90


class DUMMYAttack13(EnemyAttack):
    _index = 115
    _name = 'DUMMY'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class DUMMYAttack14(EnemyAttack):
    _index = 116
    _name = 'DUMMY'
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 90


class DUMMYAttack15(EnemyAttack):
    _index = 117
    _name = 'DUMMY'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class DUMMYAttack16(EnemyAttack):
    _index = 118
    _name = 'DUMMY'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class JinxedAttack(EnemyAttack):
    _index = 119
    _name = ' Jinxed'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 100


class TripleKickAttack(EnemyAttack):
    _index = 120
    _name = ' Triple Kick'
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class QuicksilverAttack(EnemyAttack):
    _index = 121
    _name = ' Quicksilver'
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 90


class BombsAwayAttack(EnemyAttack):
    _index = 122
    _name = ' Bombs Away'
    _attack_level = 3
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 90


class VigorupAttack(EnemyAttack):
    _index = 123
    _name = ' Vigor up!'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 100
    _buffs = [TempStatBuff(3), TempStatBuff(4)]


class SpeedForceAttack(EnemyAttack):
    _index = 124
    _name = ' Speed Force'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 100


class SilverBulletAttack(EnemyAttack):
    _index = 125
    _name = 'Silver Bullet'
    _attack_level = 0
    _ohko = True
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = False
    _hit_rate = 99


class TerrapunchAttack(EnemyAttack):
    _index = 126
    _name = ' Terrapunch'
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


class ScrowFangsAttack(EnemyAttack):
    _index = 127
    _name = " S'crow Fangs"
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 85
    _status_effects = [Status.SCARECROW]


class ShakerAttack(EnemyAttack):
    _index = 128
    _name = ' Shaker'
    _attack_level = 0
    _ohko = True
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = False
    _hit_rate = 99



collection = EnemyAttackCollection([
    Attack0(),
    Attack1(),
    Attack2(),
    Attack3(),
    Attack4(),
    Attack5(),
    Attack6(),
    Attack7(),
    Attack8(),
    Attack9(),
    Attack10(),
    Attack11(),
    Attack12(),
    Attack13(),
    Attack14(),
    Attack15(),
    Attack16(),
    ThornetAttack(),
    Attack18(),
    FunguspikeAttack(),
    Attack20(),
    Attack21(),
    FullHouseAttack(),
    WildCardAttack(),
    RoyalFlushAttack(),
    Attack25(),
    SpritzBombAttack(),
    Attack27(),
    Attack28(),
    Attack29(),
    BlazerAttack(),
    Attack31(),
    Attack32(),
    EchofinderAttack(),
    ScrowBellAttack(),
    DoomReverbAttack(),
    SporeChimesAttack(),
    InkBlastAttack(),
    GunkBallAttack(),
    EndobubbleAttack(),
    DUMMYAttack1(),
    SleepSauceAttack(),
    VenomDroolAttack(),
    MushFunkAttack(),
    ScrowFunkAttack(),
    StenchAttack(),
    Attack46(),
    Attack47(),
    ViroPlasmAttack(),
    PsychoPlasmAttack(),
    Attack50(),
    Attack51(),
    PollenNapAttack(),
    ScrowDustAttack(),
    SporocystAttack(),
    ToxicystAttack(),
    Attack56(),
    Attack57(),
    LullaByeAttack(),
    ElegyAttack(),
    BackfireAttack(),
    VaVaVoomAttack(),
    FunRunAttack(),
    BodySlamAttack(),
    HowlAttack(),
    ScreamAttack(),
    IronMaidenAttack(),
    FangsAttack(),
    PoisonAttack(),
    CarniKissAttack(),
    ClawAttack(),
    GrinderAttack(),
    DarkClawAttack(),
    ScytheAttack(),
    MoralSupportAttack(),
    DeathsickleAttack(),
    EerieJigAttack(),
    SomnusWaltzAttack(),
    BOBOMBSUPERAttack(),
    SkewerAttack(),
    PierceAttack(),
    Attack81(),
    MagnumAttack(),
    PsycheAttack(),
    MigraineAttack(),
    BOBOMBBOMBAttack(),
    Attack86(),
    MultistrikeAttack(),
    FlutterHushAttack(),
    Attack89(),
    Attack90(),
    CULEXTURNSAttack(),
    FearRouletteAttack(),
    ValorForceAttack(),
    MeteorAttack(),
    VigorForceAttack(),
    HammerTimeAttack(),
    ValorUpAttack(),
    DUMMYAttack2(),
    LastShotAttack(),
    DUMMYAttack3(),
    DUMMYAttack4(),
    DUMMYAttack5(),
    DUMMYAttack6(),
    DUMMYAttack7(),
    DUMMYAttack8(),
    GnightAttack(),
    DUMMYAttack9(),
    DUMMYAttack10(),
    ChompAttack(),
    GetToughAttack(),
    DUMMYAttack11(),
    MissedmeAttack(),
    DUMMYAttack12(),
    LocoExpressAttack(),
    DUMMYAttack13(),
    DUMMYAttack14(),
    DUMMYAttack15(),
    DUMMYAttack16(),
    JinxedAttack(),
    TripleKickAttack(),
    QuicksilverAttack(),
    BombsAwayAttack(),
    VigorupAttack(),
     SpeedForceAttack(),
    SilverBulletAttack(),
    TerrapunchAttack(),
    ScrowFangsAttack(),
    ShakerAttack(),
])
