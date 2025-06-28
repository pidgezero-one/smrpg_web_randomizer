"""Definitions for henchmen belonging to certain bosses."""

from typing import Type
from randomizer.types.battles.ids.pack_ids import (
    PACK0000_SNIFIT_FIGHT,
    PACK0001_BOBOMB_HENCHMEN,
    PACK0010_REGULAR_SHYSTERS_BIASED_2,
    PACK0011_REGULAR_SHYSTERS_BIASED_3,
    PACK0032_APPRENTICE_HENCHMAN_FIGHT,
    PACK0036_BOBOMB_WITH_CLUSTER,
    PACK0054_TORTES,
    PACK0055_MULTIPLE_TORTES,
    PACK0068_BANDANA_REDS_1,
    PACK0069_BANDANA_REDS_2,
    PACK0070_BANDANA_BLUES,
    PACK0071_BANDANA_RED_HENCHMEN,
    PACK0092_BIRDY_PACK_1,
    PACK0093_BIRDY_PACK_2,
    PACK0094_BLUEBIRD_PACK_1,
    PACK0095_BLUEBIRD_PACK_2,
    PACK0126_POUNDER_PACK_1,
    PACK0128_POUNDETTE_PACK_1,
    PACK0141_CROOK_HENCHMEN_ONLY,
    PACK0142_SNIFIT_ONLY,
    PACK0150_MAD_MALLET_FACTORY_FIGHT,
    PACK0153_THREE_DRILLBIT_SUBSTITUTE,
    PACK0154_SINGLE_SHYGUY_HENCHMAN,
    PACK0155_MAD_MALLET_HENCHMEN,
    PACK0160_BOWYER_AERO_HENCHMEN,
    PACK0190_PYROSPHERE_HENCHMEN,
    PACK0193_HELIO_HENCHMEN,
    PACK0194_BODYGUARD_PACK_1,
    PACK0195_BODYGUARD_PACK_2,
    PACK0196_GENO_CLONE_HENCHMAN,
    PACK0197_BOWSER_CLONE_HENCHMAN,
    PACK0198_TOADSTOOL_CLONE_HENCHMAN,
    PACK0199_CROOKS_ONLY,
    PACK0200_MARIO_CLONE_HENCHMAN,
    PACK0201_BIRDY_HENCHMEN,
    PACK0202_MALLOW_CLONE_HENCHMAN,
    PACK0203_MACHINE_AXEM_HENCHMEN,
    PACK0204_BLOOBER_HENCHMEN,
    PACK0205_BLUEBIRD_HENCHMEN,
    PACK0217_FIRE_CRYSTAL_HENCHMAN,
    PACK0218_WATER_CRYSTAL_HENCHMAN,
    PACK0219_EARTH_CRYSTAL_HENCHMAN,
    PACK0220_WIND_CRYSTAL_HENCHMAN,
    PACK0221_GOOMBETTE_HENCHMEN,
    PACK0222_PIRANHA_HENCHMEN,
    PACK0223_EGGBERT_HENCHMEN,
    PACK0248_AXEM_BLACK_ALONE,
    PACK0249_AXEM_PINK_ALONE,
    PACK0250_AXEM_YELLOW_ALONE,
    PACK0251_AXEM_GREEN_ALONE,
    PACK0252_DINGALING_ALONE,
    PACK0253_SMITHY_HENCHMEN_PACK_1,
    PACK0254_SMITHY_HENCHMEN_PACK_2,
    PACK0255_SMITHY_HENCHMEN_PACK_3,
)
from randomizer.types.bosses.classes import Henchman
from randomizer.types.npcs.objects.types.classes import NPC
from randomizer.data.npcs.npcs import (
    AeroUpright,
    Apprentice,
    AxemBlack,
    AxemGreen,
    AxemPink,
    AxemYellow,
    BackSnifit,
    BandanaBlue,
    BandanaRed,
    Birdy,
    Bloober,
    Bluebird,
    BobOmb,
    BowserClone,
    Crook,
    DingalingGridplane,
    DrillBit,
    EarthCrystal,
    EggbertGridplane,
    FakeToad,
    FireCrystal,
    GenoClone,
    Goombette,
    GunyolkTop,
    Helio,
    Jabit,
    KnifeGuyGridplane,
    MachineAxemBlack,
    MachineAxemGreen,
    MachineAxemPink,
    MachineAxemRed,
    MachineAxemYellow,
    MachineDrillBit,
    MadMallet,
    MallowClone,
    MarioClone,
    Microbomb,
    PeachClone,
    PiranhaPlant,
    Pounder,
    Poundette,
    RedFireball,
    ShyGuy,
    Shyster,
    Snifit,
    TentacleExtending,
    TinyBloober,
    Torte,
    WaterCrystal,
    WindCrystal,
)


class MackShyster1(Henchman):
    """Mack Shyster 1 henchman definition"""

    _pack_number: int = PACK0194_BODYGUARD_PACK_1
    _model: Type[NPC] = Shyster


class MackShyster2(Henchman):
    """Mack Shyster 2 henchman definition"""

    _pack_number: int = PACK0195_BODYGUARD_PACK_2
    _model: Type[NPC] = Shyster


class DefaultShyster1(Henchman):
    """Default Shyster 1 henchman definition"""

    _pack_number: int = PACK0010_REGULAR_SHYSTERS_BIASED_2
    _model: Type[NPC] = Shyster


class DefaultShyster2(Henchman):
    """Default Shyster 2 henchman definition"""

    _pack_number: int = PACK0011_REGULAR_SHYSTERS_BIASED_3
    _model: Type[NPC] = Shyster


class BowyerAero(Henchman):
    """Bowyer Aero henchman definition"""

    _pack_number: int = PACK0160_BOWYER_AERO_HENCHMEN
    _model: Type[NPC] = AeroUpright


class Croco2Crook(Henchman):
    """Croco2 Crook henchman definition"""

    _pack_number: int = PACK0141_CROOK_HENCHMEN_ONLY
    _model: Type[NPC] = Crook


class DefaultCrook(Henchman):
    """Default Crook henchman definition"""

    _pack_number: int = PACK0199_CROOKS_ONLY
    _model: Type[NPC] = Crook


class PunchinelloBobomb(Henchman):
    """Punchinello Bob-omb henchman definition"""

    _pack_number: int = PACK0001_BOBOMB_HENCHMEN
    _model: Type[NPC] = BobOmb


class DefaultMicrobomb(Henchman):
    """Default Microbomb henchman definition"""

    _model: Type[NPC] = Microbomb


class DefaultBobomb(Henchman):
    """Default Bob-omb henchman definition"""

    _pack_number: int = PACK0036_BOBOMB_WITH_CLUSTER
    _model: Type[NPC] = BobOmb


class BoosterSnifit(Henchman):
    """Booster Snifit henchman definition"""

    _pack_number: int = PACK0000_SNIFIT_FIGHT
    _model: Type[NPC] = Snifit


# Remove sequences from zoom animation if not snifit
class BoosterHillSnifit(Henchman):
    """Booster Hill Snifit henchman definition"""

    _model: Type[NPC] = BackSnifit


class DefaultSnifit(Henchman):
    """Default Snifit henchman definition"""

    _pack_number: int = PACK0142_SNIFIT_ONLY
    _model: Type[NPC] = Snifit


class BoosterApprentice(Henchman):
    """Booster Apprentice henchman definition"""

    _pack_number: int = PACK0032_APPRENTICE_HENCHMAN_FIGHT
    _model: Type[NPC] = Apprentice


class GrateGuyKnifeGuy(Henchman):
    """Grate Guy Knife Guy henchman definition"""

    _model: Type[NPC] = KnifeGuyGridplane


class BundtTorte1(Henchman):
    """Bundt Torte 1 henchman definition"""

    _pack_number: int = PACK0054_TORTES
    _model: Type[NPC] = Torte


class BundtTorte2(Henchman):
    """Bundt Torte 2 henchman definition"""

    _pack_number: int = PACK0055_MULTIPLE_TORTES
    _model: Type[NPC] = Torte


class KingCalamariTinyBloober(Henchman):
    """King Calamari Tiny Bloober henchman definition"""

    _pack_number: int = PACK0204_BLOOBER_HENCHMEN
    _model: Type[NPC] = TinyBloober


class KingCalamariBloober(Henchman):
    """King Calamari Bloober henchman definition"""

    _pack_number: int = PACK0204_BLOOBER_HENCHMEN
    _model: Type[NPC] = Bloober


class KingCalamariTentacle(Henchman):
    """King Calamari Tentacle henchman definition"""

    _model: Type[NPC] = TentacleExtending


class HidonGoombette(Henchman):
    """Hidon Goombette henchman definition"""

    _pack_number: int = PACK0221_GOOMBETTE_HENCHMEN
    _model: Type[NPC] = Goombette


class DefaultBandanaRed1(Henchman):
    """Default Bandana Red 1 henchman definition"""

    _pack_number: int = PACK0068_BANDANA_REDS_1
    _model: Type[NPC] = BandanaRed


class DefaultBandanaRed2(Henchman):
    """Default Bandana Red 2 henchman definition"""

    _pack_number: int = PACK0069_BANDANA_REDS_2
    _model: Type[NPC] = BandanaRed


class JohnnyBandanaRed(Henchman):
    """Johnny Bandana Red henchman definition"""

    _pack_number: int = PACK0071_BANDANA_RED_HENCHMEN
    _model: Type[NPC] = BandanaRed


class JohnnyBandanaBlue(Henchman):
    """Johnny Bandana Blue henchman definition"""

    _pack_number: int = PACK0070_BANDANA_BLUES
    _model: Type[NPC] = BandanaBlue


class YaridovichHenchman(Henchman):
    """Yaridovich henchman definition"""

    _pack_number: int = PACK0153_THREE_DRILLBIT_SUBSTITUTE
    _model: Type[NPC] = FakeToad


class Belome2MarioClone(Henchman):
    """Belome 2 Mario Clone henchman definition"""

    _pack_number: int = PACK0200_MARIO_CLONE_HENCHMAN
    _model: Type[NPC] = MarioClone


class Belome2MallowClone(Henchman):
    """Belome 2 Mallow Clone henchman definition"""

    _pack_number: int = PACK0202_MALLOW_CLONE_HENCHMAN
    _model: Type[NPC] = MallowClone


class Belome2GenoClone(Henchman):
    """Belome 2 Geno Clone henchman definition"""

    _pack_number: int = PACK0196_GENO_CLONE_HENCHMAN
    _model: Type[NPC] = GenoClone


class Belome2BowserClone(Henchman):
    """Belome 2 Bowser Clone henchman definition"""

    _pack_number: int = PACK0197_BOWSER_CLONE_HENCHMAN
    _model: Type[NPC] = BowserClone


class Belome2PeachClone(Henchman):
    """Belome 2 Peach Clone henchman definition"""

    _pack_number: int = PACK0198_TOADSTOOL_CLONE_HENCHMAN
    _model: Type[NPC] = PeachClone


class CulexFireCrystal(Henchman):
    """Culex Fire Crystal henchman definition"""

    _pack_number: int = PACK0217_FIRE_CRYSTAL_HENCHMAN
    _model: Type[NPC] = FireCrystal


class CulexWaterCrystal(Henchman):
    """Culex Water Crystal henchman definition"""

    _pack_number: int = PACK0218_WATER_CRYSTAL_HENCHMAN
    _model: Type[NPC] = WaterCrystal


class CulexEarthCrystal(Henchman):
    """Culex Earth Crystal henchman definition"""

    _pack_number: int = PACK0219_EARTH_CRYSTAL_HENCHMAN
    _model: Type[NPC] = EarthCrystal


class CulexWindCrystal(Henchman):
    """Culex Wind Crystal henchman definition"""

    _pack_number: int = PACK0220_WIND_CRYSTAL_HENCHMAN
    _model: Type[NPC] = WindCrystal


class MegaSmilaxPiranha(Henchman):
    """Megasmilax Piranha Plant henchman definition"""

    _pack_number: int = PACK0222_PIRANHA_HENCHMEN
    _model: Type[NPC] = PiranhaPlant


class BirdettaEggbert(Henchman):
    """Birdetta Eggbert henchman definition"""

    _pack_number: int = PACK0223_EGGBERT_HENCHMEN
    _model: Type[NPC] = EggbertGridplane


class DefaultBluebird1(Henchman):
    """Default Bluebird 1 henchman definition"""

    _pack_number: int = PACK0094_BLUEBIRD_PACK_1
    _model: Type[NPC] = Bluebird


class DefaultBluebird2(Henchman):
    """Default Bluebird 2 henchman definition"""

    _pack_number: int = PACK0095_BLUEBIRD_PACK_2
    _model: Type[NPC] = Bluebird


class DefaultBirdy1(Henchman):
    """Default Birdy 1 henchman definition"""

    _pack_number: int = PACK0092_BIRDY_PACK_1
    _model: Type[NPC] = Birdy


class DefaultBirdy2(Henchman):
    """Default Birdy 2 henchman definition"""

    _pack_number: int = PACK0093_BIRDY_PACK_2
    _model: Type[NPC] = Birdy


class ValentinaBluebird(Henchman):
    """Valentina Bluebird henchman definition"""

    _pack_number: int = PACK0205_BLUEBIRD_HENCHMEN
    _model: Type[NPC] = Bluebird


class ValentinaBirdy(Henchman):
    """Valentina Birdy henchman definition"""

    _pack_number: int = PACK0201_BIRDY_HENCHMEN
    _model: Type[NPC] = Birdy


class CzarPyrosphere(Henchman):
    """Czar Dragon Pyrosphere henchman definition"""

    _pack_number: int = PACK0190_PYROSPHERE_HENCHMEN
    _model: Type[NPC] = RedFireball


class CzarHelio(Henchman):
    """Czar Dragon Helio henchman definition"""

    _pack_number: int = PACK0193_HELIO_HENCHMEN
    _model: Type[NPC] = Helio


class AxemRangersAxemBlack(Henchman):
    """Axem Black henchman definition"""

    _pack_number: int = PACK0248_AXEM_BLACK_ALONE
    _model: Type[NPC] = AxemBlack


class AxemRangersAxemPink(Henchman):
    """Axem Pink henchman definition"""

    _pack_number: int = PACK0249_AXEM_PINK_ALONE
    _model: Type[NPC] = AxemPink


class AxemRangersAxemYellow(Henchman):
    """Axem Yellow henchman definition"""

    _pack_number: int = PACK0250_AXEM_YELLOW_ALONE
    _model: Type[NPC] = AxemYellow


class AxemRangersAxemGreen(Henchman):
    """Axem Green henchman definition"""

    _pack_number: int = PACK0251_AXEM_GREEN_ALONE
    _model: Type[NPC] = AxemGreen


class AxemRangersMachine1(Henchman):
    """Machine Axem Red henchman definition"""

    _pack_number: int = PACK0203_MACHINE_AXEM_HENCHMEN
    _model: Type[NPC] = MachineAxemRed


class AxemRangersMachine2(Henchman):
    """Machine Axem Pink henchman definition"""

    _pack_number: int = PACK0203_MACHINE_AXEM_HENCHMEN
    _model: Type[NPC] = MachineAxemPink


class AxemRangersMachine3(Henchman):
    """Machine Axem Black henchman definition"""

    _pack_number: int = PACK0203_MACHINE_AXEM_HENCHMEN
    _model: Type[NPC] = MachineAxemBlack


class AxemRangersMachine4(Henchman):
    """Machine Axem Yellow henchman definition"""

    _pack_number: int = PACK0203_MACHINE_AXEM_HENCHMEN
    _model: Type[NPC] = MachineAxemYellow


class AxemRangersMachine5(Henchman):
    """Machine Axem Green henchman definition"""

    _pack_number: int = PACK0203_MACHINE_AXEM_HENCHMEN
    _model: Type[NPC] = MachineAxemGreen


class BoomerShyGuy(Henchman):
    """Boomer Shy Guy henchman definition"""

    _pack_number: int = PACK0154_SINGLE_SHYGUY_HENCHMAN
    _model: Type[NPC] = ShyGuy


class CountdownDingALing(Henchman):
    """Count Down Ding-a-ling henchman definition"""

    _pack_number: int = PACK0252_DINGALING_ALONE
    _model: Type[NPC] = DingalingGridplane


class DefaultMadMallet(Henchman):
    """Default Mad Mallet henchman definition"""

    _pack_number: int = PACK0150_MAD_MALLET_FACTORY_FIGHT
    _model: Type[NPC] = MadMallet


class ClerkMadMallet(Henchman):
    """Clerk Mad Mallet henchman definition"""

    _pack_number: int = PACK0155_MAD_MALLET_HENCHMEN
    _model: Type[NPC] = MadMallet


class ManagerPounder(Henchman):
    """Manager Pounder henchman definition"""

    _pack_number: int = PACK0126_POUNDER_PACK_1
    _model: Type[NPC] = Pounder


class DirectorPoundette(Henchman):
    """Director Poundette henchman definition"""

    _pack_number: int = PACK0128_POUNDETTE_PACK_1
    _model: Type[NPC] = Poundette


class DefaultUnpaintedDrillBit(Henchman):
    """Default Unpainted Drill Bit henchman definition"""

    _model: Type[NPC] = MachineDrillBit


class DefaultPaintedDrillBit(Henchman):
    """Default Painted Drill Bit henchman definition"""

    _model: Type[NPC] = Jabit


class GunyolkPiece(Henchman):
    """Gunyolk section henchman definition"""

    _model: Type[NPC] = GunyolkTop


class SmithyDrillBit(Henchman):
    """Smithy Drill Bit henchman definition"""

    _pack_number: int = PACK0253_SMITHY_HENCHMEN_PACK_1
    _model: Type[NPC] = DrillBit


class SmithyShyster(Henchman):
    """Smithy Shyster henchman definition"""

    _pack_number: int = PACK0254_SMITHY_HENCHMEN_PACK_2
    _model: Type[NPC] = Shyster


class SmithyAero(Henchman):
    """Smithy Aero henchman definition"""

    _pack_number: int = PACK0255_SMITHY_HENCHMEN_PACK_3
    _model: Type[NPC] = AeroUpright
