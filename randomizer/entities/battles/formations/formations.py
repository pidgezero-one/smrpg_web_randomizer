# pylint: disable=C0302

"""Formation class instances."""

from typing import List, Optional

from randomizer.entities.enemies import (
    K9,
    AeroBowyer,
    AeroSmithy,
    AlleyRat,
    Amanita,
    Ameboid,
    Apprentice,
    ApprenticeHenchman,
    Arachne,
    ArmoredAnt,
    Artichoker,
    AxemBlack,
    AxemGreen,
    AxemPink,
    AxemRangers,
    AxemRed,
    AxemYellow,
    BahamuttChester,
    BahamuttKamek,
    BandanaBlue,
    BandanaRed,
    BandanaRedHenchman,
    Belome1,
    Belome2,
    BigBertha,
    Birdetta,
    Birdy,
    BirdyHenchman,
    Blaster,
    Bloober,
    BlooberHenchman,
    Bluebird,
    BluebirdHenchman,
    Bobomb,
    BobombHenchman,
    Bodyguard,
    Boomer,
    Booster,
    Booster2,
    BowserClone,
    Bowyer,
    BoxBoy,
    Bundt,
    Buzzer,
    Carriboscis,
    ChainedKong,
    Chester,
    Chewy,
    Chomp,
    ChompChomp,
    Chow,
    Clerk,
    Cloaker,
    Cloaker2,
    Cluster,
    Corkpedite,
    CorkpediteBody,
    CountDown,
    Croco1,
    Croco2,
    Crook,
    CrookHenchman,
    Crusty,
    Culex,
    CzarDragon,
    DingALing,
    Director,
    Dodo,
    DodoSolo,
    Domino,
    Domino2,
    Doppel,
    DrillBit,
    DryBones,
    EarthCrystal,
    Earthlink,
    Eggbert,
    EmptyEnemy,
    Enigma,
    Exor,
    FactoryChief,
    Fautso,
    FinkFlower,
    FireCrystal,
    Fireball,
    Forkies,
    Formless,
    Frogog,
    Geckit,
    Gecko,
    GenoClone,
    GlumReaper,
    Goby,
    Goomba,
    Goombette,
    Gorgon,
    GrateGuy,
    Greaper,
    GuGoomba,
    Guerrilla,
    Gunyolk,
    HammerBro,
    HanginShy,
    HeavyTroopa,
    Helio,
    Hidon,
    Hippopo,
    Hobgoblin,
    Jabit,
    Jagger,
    Jawful,
    Jester,
    Jinx1,
    Jinx2,
    Jinx3,
    JinxClone,
    Johnny,
    JohnnySolo,
    KingBomb,
    KingCalamari,
    KnifeGuy,
    Kriffid,
    Lakitu,
    LeftEye,
    Leuko,
    LilBoo,
    MachineMadeAxemBlack,
    MachineMadeAxemBlackHenchman,
    MachineMadeAxemGreen,
    MachineMadeAxemGreenHenchman,
    MachineMadeAxemPink,
    MachineMadeAxemPinkHenchman,
    MachineMadeAxemRed,
    MachineMadeAxemRedHenchman,
    MachineMadeAxemYellow,
    MachineMadeAxemYellowHenchman,
    MachineMadeBowyer,
    MachineMadeDrillBit,
    MachineMadeMack,
    MachineMadeShyster,
    MachineMadeShysterHenchman,
    MachineMadeYaridovich,
    Mack,
    MadAdder,
    MadMallet,
    MadMalletHenchman,
    Kamek,
    Magmite,
    Magmus,
    Malakoopa,
    MallowClone,
    Manager,
    MarioClone,
    Mastadoom,
    Megasmilax,
    MezzoBomb,
    Microbomb,
    Mokura,
    MrKipper,
    Muckle,
    Mukumuku,
    Neosquid,
    Ninja,
    Octolot,
    Octovader,
    Oerlikon,
    Orbison,
    Orbuser,
    Pandorite,
    PeachClone,
    Pinwheel,
    PiranhaPlant,
    PiranhaPlantHenchman,
    Pounder,
    PounderHenchman,
    Poundette,
    PoundetteHenchman,
    Pulsar,
    Punchinello,
    Puppox,
    Pyrosphere,
    PyrosphereHenchman,
    Raspberry,
    Ratfunk,
    Reacher,
    Remocon,
    Ribbite,
    RightEye,
    Robomb,
    Sackit,
    Shadow,
    Shaman,
    Shelly,
    Shogun,
    ShyGuy,
    ShyGuyHenchman,
    ShyRanger,
    Shyaway,
    Shyster,
    Skytroopa,
    SlingShy,
    Smelter,
    Smilax,
    Smithy1,
    Smithy2Body,
    Smithy2ChestHead,
    Smithy2Head,
    Smithy2MageHead,
    Smithy2SafeHead,
    Smithy2TankHead,
    Snapdragon,
    Snifit,
    SnifitHenchman,
    Sparky,
    Spikester,
    Spikey,
    Spinthra,
    Spookum,
    Springer,
    Starcruster,
    Starslap,
    Stinger,
    Strawhead,
    Stumpet,
    TentaclesLeft,
    TentaclesRight,
    Terracotta,
    Terrapin,
    TheBigBoo,
    Torte,
    TuboTroopa,
    Valentina,
    Vomer,
    WaterCrystal,
    Wiggler,
    WindCrystal,
    Yaridovich,
    YaridovichDrillBit,
    YaridovichMirage,
    Zeostar,
    Zombone,
)
from randomizer.types.battles.formations_packs.types import (
    FormationMember,
    Formation,
)
from randomizer.types.battles.formations_packs import (
    AxemBossFormation,
    Belome2BossFormation,
    CloakerDominoFormation,
    CulexBossFormation,
    ExorBossFormation,
    JohnnyBossFormation,
    KingCalamariBossFormation,
    MegasmilaxBossFormation,
    ValentinaBossFormation,
)
from randomizer.types.battles.ids import (
    FORM0000_ONE_BOBOMB_HENCHMAN,
    FORM0001_FOUR_BOBOMB_HENCHMEN,
    FORM0002_APPRENTICE_HENCHMAN,
    FORM0004_TWO_SPIKEYS,
    FORM0005_SPIKEY_AND_TROOPA,
    FORM0006_TWO_SPIKEYS_FROG,
    FORM0007_THREE_SPIKEYS,
    FORM0008_ONE_TROOPA,
    FORM0009_TWO_TROOPAS,
    FORM0010_TWO_TROOPAS_FROG,
    FORM0011_TWO_TROOPAS_GOOMBA,
    FORM0012_TWO_GOOMBAS,
    FORM0013_THREE_GOOMBAS,
    FORM0014_TWO_GOOMBAS_SPIKEY,
    FORM0015_GOOMBA_FROG_SPIKEY,
    FORM0016_ONE_K9,
    FORM0017_TWO_K9,
    FORM0018_TWO_K9_SPIKEY,
    FORM0019_ONE_K9_TWO_FROG,
    FORM0020_TWO_BODYGUARDS,
    FORM0021_TWO_SHYSTER,
    FORM0022_THREE_SHYSTER,
    FORM0023_THREE_BODYGUARD,
    FORM0024_TWO_RATFUNKS,
    FORM0025_TWO_RATFUNKS_ONE_SHADOW,
    FORM0026_TWO_RATFUNKS_ONE_HOBGOBLIN,
    FORM0027_ONE_RATFUNK_TWO_HOBGOBLINS,
    FORM0029_ONE_BIGBOO_ONE_SHADOW,
    FORM0030_BIGBOO_SHADOW_HOBGOBLIN,
    FORM0031_THREE_BIGBOO_ONE_SHADOW,
    FORM0033_TWO_GOBYS,
    FORM0034_THREE_GOBYS,
    FORM0036_TWO_CROOKS,
    FORM0037_TWO_CROOKS_ONE_SHYGUY,
    FORM0038_ONE_CROOK_TWO_SNAPDRAGONS,
    FORM0039_CROOK_STARSLAP_ARACHNE,
    FORM0040_ONE_SHYGUY_HENCHMAN,
    FORM0041_ONE_SHYGUY_ONE_STARSLAP,
    FORM0042_TWO_SHYGUYS_ONE_SNAPDRAGON,
    FORM0043_SHYGUY_CROOK_ARACHNE,
    FORM0044_STARSLAP_SHYGUY,
    FORM0045_STARSLAP_ARACHNE,
    FORM0046_STARSLAP_TWO_SNAPDRAGONS,
    FORM0047_FOUR_STARSLAPS,
    FORM0048_ONE_WIGGLER,
    FORM0049_ONE_WIGGLER_ONE_AMANITA,
    FORM0050_TWO_WIGGLERS,
    FORM0051_ONE_WIGGLER_ONE_GUERRILLA,
    FORM0052_TWO_AMANITAS,
    FORM0053_TWO_AMANITAS_ONE_BUZZER,
    FORM0054_TWO_AMANITAS_ONE_OCTOLOT,
    FORM0055_AMANITA_BUZZER_GUERRILLA,
    FORM0056_BUZZER_OCTOLOT,
    FORM0057_TWO_BUZZERS_ONE_AMANITA,
    FORM0058_BUZZER_GUERRILLA,
    FORM0059_BUZZER_GUERRILLA_2,
    FORM0060_ONE_SPARKY,
    FORM0061_TWO_SPARKY_ONE_SHYRANGER,
    FORM0062_THREE_SPARKY,
    FORM0068_ONE_PIRANHA,
    FORM0069_TWO_PIRANHA_ONE_SHYRANGER,
    FORM0070_THREE_PIRANHA,
    FORM0071_FIVE_PIRANHA,
    FORM0072_ONE_BOBOMB,
    FORM0073_TWO_BOBOMB_ONE_CLUSTER,
    FORM0074_FOUR_BOBOMB,
    FORM0075_TWO_BOBOMB_ENIGMA_CLUSTER,
    FORM0076_SPARKY_ENIGMA,
    FORM0077_TWO_SPARKY_ONE_BOBOMB,
    FORM0078_ONE_SPARKY_TWO_CLUSTER,
    FORM0079_TWO_SPARKY_TWO_ENIGMA,
    FORM0080_TWO_MAGMITE,
    FORM0081_MAGMITE_BOBOMB_SPARKY,
    FORM0082_TWO_MAGMITE_TWO_CLUSTER,
    FORM0083_TWO_MAGMITE_BOBOMB_CLUSTER,
    FORM0084_ONE_LAKITU,
    FORM0085_LAKITU_SPIKESTER_ARTICHOKER,
    FORM0086_THREE_LAKITU,
    FORM0087_TWO_LAKITU_ONE_ARTICHOKER,
    FORM0088_SPIKESTER_CARROBOSCIS,
    FORM0089_TWO_SPIKESTER_ONE_ARTICHOKER,
    FORM0090_ONE_SPIKESTER_TWO_CARROBOSCIS,
    FORM0091_FOUR_SPIKESTER_ONE_CARROBOSCIS,
    FORM0092_SPOOKUM_ORBUSER,
    FORM0093_TWO_SPOOKUM_ONE_JESTER,
    FORM0094_SPOOKUM_REMOCON_ORBUSER,
    FORM0095_TWO_SPOOKUM_ONE_REMOCON,
    FORM0096_ONE_ROBOMB,
    FORM0097_THREE_ROBOMB,
    FORM0098_TWO_ROBOMB_ONE_REMOCON,
    FORM0099_FOUR_ROBOMB_ONE_ORBUSER,
    FORM0100_CHOMP_JESTER,
    FORM0101_CHOMP_ROBOMB_REMOCON,
    FORM0102_TWO_CHOMP_ONE_ORBUSER,
    FORM0103_ONE_CHOMP_TWO_JESTER,
    FORM0104_BLASTER_SPOOKUM,
    FORM0105_BLASTER_SPOOKUM_REMOCON,
    FORM0106_TWO_BLASTER_ONE_SPOOKUM,
    FORM0107_BLASTER_TWO_ROBOMB_TWO_SPOOKUM,
    FORM0108_ONE_TORTE,
    FORM0109_TWO_TORTE,
    FORM0110_THREE_TORTE,
    FORM0111_FOUR_TORTE,
    FORM0112_ONE_MUKU,
    FORM0113_TWO_MUKU,
    FORM0114_TWO_MUKU_ONE_PULSAR,
    FORM0115_MUKU_PULSAR_GECKO,
    FORM0116_TWO_SACKIT,
    FORM0117_TWO_SACKIT_MUKU_GECKO,
    FORM0118_ONE_SACKIT_TWO_PULSAR,
    FORM0119_SACKIT_MASTADOOM,
    FORM0120_GECKO_SACKIT,
    FORM0121_GECKO_MASTADOOM,
    FORM0122_TWO_GECKO_TWO_MUKU_TWO_SACKIT,
    FORM0123_TWO_GECKO_ONE_MASTADOOM,
    FORM0124_TWO_ZEOSTAR,
    FORM0125_TWO_ZEOSTAR_ONE_BLOOBER,
    FORM0126_TWO_ZEOSTAR_TWO_LEUKO,
    FORM0127_ZEOSTAR_LEUKO_CRUSTY,
    FORM0128_BLOOPER_KIPPER,
    FORM0129_THREE_BLOOBER,
    FORM0130_TWO_BLOOBER_KIPPER_CRUSTY,
    FORM0131_TWO_BLOOBER_TWO_ZEOSTAR_ONE_LEUKO,
    FORM0132_THREE_KIPPER,
    FORM0133_TWO_KIPPER_ONE_CRUSTY,
    FORM0134_TWO_KIPPER_ONE_CRUSTY_2,
    FORM0135_FOUR_KIPPER,
    FORM0136_FOUR_BANDANA_RED,
    FORM0137_FIVE_BANDANA_RED,
    FORM0140_ONE_BANDANABLUE,
    FORM0141_FOUR_BANDANARED_HENCHMEN,
    FORM0142_FOUR_BANDANABLUE,
    FORM0143_FIVE_BANDANARED_HENCHMEN,
    FORM0144_TWO_DRYBONES,
    FORM0145_TWO_DRYBONES_ONE_GREAPER,
    FORM0146_DRYBONES_GREAPER_REACHER,
    FORM0147_TWO_DRYBONES_TWO_GREAPER_ONE_REACHER,
    FORM0148_ALLEYRAT_GORGON,
    FORM0149_TWO_ALLEYRAT_TWO_GREAPER,
    FORM0150_TWO_ALLEYRAT_TWO_GORGON,
    FORM0151_ALLEYRAT_REACHER_GORGON,
    FORM0152_ONE_GREAPER,
    FORM0153_TWO_GREAPER_ONE_REACHER,
    FORM0154_GREAPER_STRAWHEAD_REACHER,
    FORM0155_GREAPER_GORGON_TWO_STRAWHEAD,
    FORM0156_ONE_DRILLBIT,
    FORM0157_TWO_DRILLBIT,
    FORM0158_THREE_DRILLBIT,
    FORM0159_FIVE_DRILLBIT,
    FORM0160_STINGER_FINKFLOWER,
    FORM0161_TWO_STINGER_ONE_OCTOVADER,
    FORM0162_ONE_STINGER_TWO_FINKFLOWER,
    FORM0163_FOUR_STINGER,
    FORM0164_CHOW_OCTOVADER,
    FORM0165_CHOW_SHOGUN,
    FORM0166_CHOW_SHOGUN_OCTOVADER,
    FORM0167_CHOW_FINKFLOWER_TWO_SHOGUN,
    FORM0168_ONE_CHOMPCHOMP,
    FORM0169_TWO_CHOMPCHOMP,
    FORM0170_THREE_CHOMPCHOMP,
    FORM0171_FOUR_CHOMPCHOMP,
    FORM0172_ONE_SHYAWAY,
    FORM0173_TWO_SHYAWAY_ONE_KRIFFID,
    FORM0174_TWO_SHYAWAY_ONE_RIBBITE,
    FORM0175_SHYAWAY_GECKIT_RIBBITE,
    FORM0176_TWO_CHEWY,
    FORM0177_TWO_CHEWY_ONE_SHYAWAY,
    FORM0178_CHEWY_SPINTHRA,
    FORM0179_TWO_CHEWY_TWO_GECKIT_ONE_KRIFFID,
    FORM0180_GECKIT_SPINTHRA,
    FORM0181_TWO_GECKIT_ONE_SPINTHRA,
    FORM0182_TWO_GECKIT_TWO_CHEWY_ONE_SHYAWAY,
    FORM0183_TWO_GECKIT_SPINTHRA_KRIFFID,
    FORM0184_BIRDY_HEAVYTROOPA,
    FORM0185_THREE_BIRDY,
    FORM0186_TWO_BIRDY_ONE_HEAVYTROOPA,
    FORM0187_FIVE_BIRDY,
    FORM0188_TWO_BLUEBIRD,
    FORM0189_TWO_BLUEBIRD_ONE_HEAVYTROOPA,
    FORM0190_FOUR_BLUEBIRD,
    FORM0191_TWO_BLUEBIRD_ONE_HEAVYTROOPA_2,
    FORM0192_ONE_PINWHEEL,
    FORM0193_PINWHEEL_MUCKLE,
    FORM0194_TWO_PINWHEEL_TWO_MUCKLE,
    FORM0195_THREE_PINWHEEL_TWO_SLINGSHY,
    FORM0196_TWO_SHAMAN,
    FORM0197_SHAMAN_ORBISON_JAWFUL,
    FORM0198_TWO_SHAMAN_ONE_JAWFUL,
    FORM0199_TWO_SHAMAN_TWO_SLINGSHY_JAWFUL,
    FORM0200_SLINGSHY_ORBISON,
    FORM0201_ONE_SLINGSHY_TWO_ORBISON,
    FORM0202_SLINGSHY_TWO_ORBISON_JAWFUL,
    FORM0203_TWO_SLINGSHY_TWO_PINWHEEL_MUCKLE,
    FORM0204_ONE_MAGMUS,
    FORM0205_TWO_MAGMUS_ONE_ARMOREDANT,
    FORM0206_THREE_MAGMUS_TWO_OERLIKON,
    FORM0207_TWO_MAGMUS_TWO_ARMOREDANT,
    FORM0208_OERLIKON_VOMER,
    FORM0209_THREE_OERLIKON,
    FORM0210_OERLIKON_CHAINEDKONG_ARMOREDANT,
    FORM0211_TWO_OERLIKON_ONE_CHAINEDKONG,
    FORM0212_THREE_PYROSPHERE,
    FORM0213_TWO_PYROSPHERE_ONE_CHAINEDKONG,
    FORM0214_CORKPEDITE_BODY_PYROSPHERE,
    FORM0215_TWO_PYROSPHERE_ONE_STUMPET,
    FORM0216_VOMER_CHAINEDKONG,
    FORM0217_THREE_VOMER,
    FORM0218_CORKPEDITE_BODY_VOMER,
    FORM0219_TWO_VOMER_ONE_STUMPET,
    FORM0220_ONE_TERRACOTTA,
    FORM0221_THREE_TERRACOTTA,
    FORM0222_ONE_TERRACOTTA_TWO_FORKIES,
    FORM0223_TWO_TERRACOTTA_TWO_GUGOOMBA_ONE_FORKIES,
    FORM0224_MALAKOOPA_TUBOTROOPA,
    FORM0225_TWO_MALAKOOPA_ONE_TUBOTROOPA,
    FORM0226_TWO_MALAKOOPA_TERRACOTTA_TUBOTROOPA,
    FORM0227_ONE_MALAKOOPA_TWO_TUBOTROOPA,
    FORM0228_TWO_GUGOOMBA,
    FORM0229_TWO_GUGOOMBA_ONE_STARCRUSTER,
    FORM0230_GUGOOMBA_FORKIES_STARCRUSTER,
    FORM0231_TWO_GUGOOMBA_TWO_MALAKOOPA_TWO_TERRACOTTA,
    FORM0232_ONE_BIGBERTHA,
    FORM0233_TWO_BIGBERTHA,
    FORM0234_BIGBERTHA_FORKIES,
    FORM0235_TWO_BIGBERTHA_ONE_TERRACOTTA,
    FORM0240_ONE_NINJA,
    FORM0241_NINJA_DOPPEL,
    FORM0242_TWO_NINJA_ONE_HIPPOPO,
    FORM0243_FIVE_NINJA,
    FORM0244_SPRINGER_GLUMREAPER,
    FORM0246_TWO_SPRINGER_ONE_PUPPOX,
    FORM0247_ONE_SPRINGER_TWO_PUPPOX,
    FORM0248_FIVE_AMEBOID,
    FORM0252_THREE_GLUMREAPER,
    FORM0253_GLUMREAPER_HIPPOPO,
    FORM0254_TWO_GLUMREAPER_TWO_DOPPEL,
    FORM0255_TWO_GLUMREAPER_TWO_LILBOO,
    FORM0256_ONE_LILBOO,
    FORM0257_TWO_LILBOO_ONE_HIPPOPO,
    FORM0258_TWO_LILBOO_PUPPOX_DOPPEL,
    FORM0259_FOUR_LILBOO,
    FORM0260_TWO_MADMALLET,
    FORM0261_THREE_MADMALLET,
    FORM0262_FIVE_MADMALLET,
    FORM0263_THREE_MADMALLET_HENCHMEN,
    FORM0264_ONE_POUNDER,
    FORM0265_THREE_POUNDER,
    FORM0266_FIVE_POUNDER,
    FORM0268_PANDORITE_BOSS_FIGHT,
    FORM0269_HIDON_BOSS_FIGHT,
    FORM0270_BOXBOY_BOSS_FIGHT,
    FORM0271_CHESTER_BOSS_FIGHT,
    FORM0272_TWO_BLUEBIRD_HENCHMEN,
    FORM0274_BOOSTER_BOSS_FIGHT,
    FORM0275_BOOSTER_DUMMY,
    FORM0276_SNIFIT_HENCHMAN,
    FORM0277_CROCO1_BOSS_FIGHT,
    FORM0278_CROCO2_BOSS_FIGHT,
    FORM0279_FOUR_BLUEBIRD_HENCHMEN,
    FORM0280_JOHNNY_BOSS_FIGHT,
    FORM0285_KING_CALAMARI_BOSS_FIGHT,
    FORM0286_BELOME_1_BOSS_FIGHT,
    FORM0287_BELOME_2_BOSS_FIGHT,
    FORM0289_VALENTINA_BOSS_FIGHT,
    FORM0293_CZAR_DRAGON_BOSS_FIGHT,
    FORM0294_MEGASMILAX_BOSS_FIGHT,
    FORM0295_COUNTDOWN_BOSS_FIGHT,
    FORM0297_BIRDETTA_BOSS_FIGHT,
    FORM0298_BUNDT_BOSS_FIGHT,
    FORM0299_KGGG_BOSS_FIGHT,
    FORM0300_HELIO_HENCHMEN,
    FORM0301_JINX_1_BOSS_FIGHT,
    FORM0302_MACK_BOSS_FIGHT,
    FORM0303_YARIDOVICH_BOSS_FIGHT,
    FORM0304_AXEM_BOSS_FIGHT,
    FORM0305_BOWYER_BOSS_FIGHT,
    FORM0307_EXOR_BOSS_FIGHT,
    FORM0308_SMITHY_1_BOSS_FIGHT,
    FORM0309_CLOAKER_DOMINO_FIGHT,
    FORM0310_THREE_RATFUNK,
    FORM0311_FIVE_RATFUNK,
    FORM0312_ONE_ARTICHOKER,
    FORM0313_TWO_ARTICHOKERS,
    FORM0314_PUNCHINELLO_BOSS_FIGHT,
    FORM0315_HAMMERBRO_BOSS_FIGHT,
    FORM0316_THREE_CROOK_HENCHMEN,
    FORM0317_FIVE_CROOK_HENCHMEN,
    FORM0318_ONE_SNIFIT,
    FORM0319_ONE_STUMPET_TWO_MAGMUS,
    FORM0320_ONE_POUNDETTE,
    FORM0321_THREE_POUNDETTES,
    FORM0322_SIX_POUNDETTES,
    FORM0325_JABIT_MADMALLET,
    FORM0325_JABIT_POUNDER_POUNDETTE,
    FORM0326_SIX_JABIT,
    FORM0327_JABITS_MADMALLETS_POUNDETTES,
    FORM0328_TWO_FIREBALL,
    FORM0329_THREE_FIREBALL,
    FORM0330_ONE_STUMPET_THREE_MAGMUS,
    FORM0331_CORKPEDITE_OERLIKON,
    FORM0332_CORKPEDITE_TWO_OERLIKONS,
    FORM0333_JINX_2_BOSS_FIGHT,
    FORM0334_JINX_3_BOSS_FIGHT,
    FORM0335_JAGGER_BOSS_FIGHT,
    FORM0345_FIVE_BIRDY_HENCHMEN,
    FORM0346_THREE_AXEM_HENCHMEN,
    FORM0347_FOUR_AXEM_HENCHMEN,
    FORM0348_THREE_BLOOBER_HENCHMEN,
    FORM0349_TWO_BOWYER_AEROS,
    FORM0350_CULEX_BOSS_FIGHT,
    FORM0351_MOKURA_BOSS_FIGHT,
    FORM0352_THREE_PYROSPHERE_HENCHMEN,
    FORM0353_ONE_FIRE_CRYSTAL,
    FORM0354_THREE_SHOGUNS,
    FORM0355_THREE_HEAVY_TROOPA,
    FORM0356_DODO_BOSS_FIGHT,
    FORM0357_KAMEK_BOSS_FIGHT,
    FORM0358_BOOMER_BOSS_FIGHT,
    FORM0359_MACHINE_MACK,
    FORM0360_MACHINE_BOWYER,
    FORM0361_MACHINE_YARIDOVICH,
    FORM0362_THREE_MACHINE_AXEMS,
    FORM0363_SMITHY_2,
    FORM0364_CLERK_BOSS_FIGHT,
    FORM0365_MANAGER_BOSS_FIGHT,
    FORM0366_DIRECTOR_BOSS_FIGHT,
    FORM0367_GUNYOLK_BOSS_FIGHT,
    FORM0368_THREE_MAD_MALLETS,
    FORM0369_ONE_APPRENTICE,
    FORM0370_FOUR_MACHINE_AXEMS,
    FORM0371_FOUR_TERRA_COTTA_KEEP,
    FORM0372_TWO_OERLIKON_ONE_STARCRUSTER_KEEP,
    FORM0373_ONE_SACKIT_TWO_BIGBERTHA_KEEP,
    FORM0374_ONE_CHOW_TWO_FORKIES_KEEP,
    FORM0375_ONE_ALLEYRAT_TWO_ARMOREDANT_KEEP,
    FORM0376_THREE_BLOOBER_ONE_STARCRUSTER_KEEP,
    FORM0377_FOUR_STINGER_KEEP,
    FORM0378_TWO_GECKIT_ONE_CHAINEDKONG_KEEP,
    FORM0379_ONE_ROBOMB_TWO_BIGBERTHA_KEEP,
    FORM0380_FOUR_VOMER_KEEP,
    FORM0381_TWO_MAGMUS_TWO_PULSAR_KEEP,
    FORM0382_FIVE_GUGOOMBAS_KEEP,
    FORM0383_TWO_MALAKOOPAS_ONE_TUBOTROOPA_KEEP,
    FORM0384_TWO_BIGBOO_TWO_ORBISON_KEEP,
    FORM0385_FIVE_SLINGSHY_KEEP,
    FORM0386_TWO_CHEWY_TWO_SHYAWAY_KEEP,
    FORM0387_ONE_MRKIPPER_TWO_MUCKLES_KEEP,
    FORM0388_TWO_AMANITAS_ONE_ORBISON_KEEP,
    FORM0389_TWO_GREAPERS_ONE_GLUMREAPER_KEEP,
    FORM0390_THREE_PYROSPHERE_KEEP,
    FORM0391_THREE_LAKITU_KEEP,
    FORM0392_TWO_ZEOSTAR_TWO_SHAMAN_KEEP,
    FORM0393_SIX_SHAMANS_KEEP,
    FORM0394_THREE_MACHINE_SHYSTERS,
    FORM0395_THREE_MACHINE_DRILLBITS,
    FORM0405_ONE_WATER_CRYSTAL,
    FORM0406_ONE_EARTH_CRYSTAL,
    FORM0407_ONE_WIND_CRYSTAL,
    FORM0408_THREE_GOOMBETTES,
    FORM0409_ONE_PIRANHA_HENCHMAN,
    FORM0410_THREE_PIRANHA_HENCHMEN,
    FORM0411_FIVE_PIRANHA_HENCHMEN,
    FORM0412_ONE_EGGBERT,
    FORM0413_THREE_EGGBERTS,
    FORM0414_FOUR_EGGBERTS,
    FORM0415_SOLO_AXEM_BLACK,
    FORM0416_SOLO_AXEM_PINK,
    FORM0417_SOLO_AXEM_YELLOW,
    FORM0418_SOLO_AXEM_GREEN,
    FORM0419_SOLO_DINGALING,
    FORM0420_SMITHY_HENCHMEN_MIX,
    FORM0421_FOUR_DRILLBITS,
    FORM0422_ONE_DRILLBIT_TWO_AEROS,
    FORM0423_TWO_MACHINE_SHYSTER_HENCHMEN,
    FORM0424_TWO_DRILLBITS_ONE_MACHINE_SHYSTER,
    FORM0425_FIVE_AEROS,
    FORM0426_TWO_AEROS_ONE_MACHINE_SHYSTER,
    FORM0427_THREE_CROOKS,
    FORM0428_FIVE_CROOKS,
    FORM0429_THREE_BIRDY_HENCHMEN,
    FORM0430_SOLO_MARIO_CLONE,
    FORM0431_SOLO_MALLOW_CLONE,
    FORM0432_SOLO_GENO_CLONE,
    FORM0433_SOLO_BOWSER_CLONE,
    FORM0434_SOLO_TOADSTOOL_CLONE,
    TOTAL_FORMATIONS,
)
from randomizer.types.battle_animation_scripts.ids import (
    BE0011_SOLO_EARTH_CRYSTAL_APPEARS,
    BE0012_DIALOGUE_FROM_BOOSTER_FIGHT,
    BE0014_SET_7EE00A_TO_PARTY_SIZE_AT_START_OF_FIGHT,
    BE0020_SOLO_WATER_CRYSTAL_APPEARS,
    BE0026_INTRO_SCENE_TENTACLES_RISE_FROM_HOLES,
    BE0035_BOOSTER_EATS_CAKE,
    BE0052_INTRO_SCENE_DOMINO_CLOAKER_S_INTRODUCTION,
    BE0058_THRAX_IS_THERE,
    BE0061_ONLY_MARIO_IS_THERE,
    BE0071_JINX_USES_TRIPLE_KICK,
    BE0072_JINX_USES_QUICKSILVER,
    BE0073_JINX_USES_BOMBS_AWAY,
    BE0076_SOLO_FIRE_CRYSTAL_APPEARS,
    BE0080_EXOR_FIGHT_BEGINS,
)
from randomizer.types.bosses import BattleMusic, Battlefields

formations: List[Optional[Formation]] = [None] * TOTAL_FORMATIONS
formations[FORM0000_ONE_BOBOMB_HENCHMAN] = Formation(
    [FormationMember(BobombHenchman, x_pos=183, y_pos=127)]
)
formations[FORM0001_FOUR_BOBOMB_HENCHMEN] = Formation(
    [
        FormationMember(BobombHenchman, x_pos=151, y_pos=127),
        FormationMember(BobombHenchman, x_pos=167, y_pos=103),
        FormationMember(BobombHenchman, x_pos=199, y_pos=151),
        FormationMember(BobombHenchman, x_pos=215, y_pos=127),
    ]
)
formations[FORM0002_APPRENTICE_HENCHMAN] = Formation(
    [FormationMember(ApprenticeHenchman, x_pos=183, y_pos=127)]
)
formations[3] = None
formations[FORM0004_TWO_SPIKEYS] = Formation(
    [
        FormationMember(Spikey, x_pos=135, y_pos=127),
        FormationMember(Spikey, x_pos=199, y_pos=143),
    ]
)
formations[FORM0005_SPIKEY_AND_TROOPA] = Formation(
    [
        FormationMember(Spikey, x_pos=135, y_pos=119),
        FormationMember(Skytroopa, x_pos=199, y_pos=151),
    ]
)
formations[FORM0006_TWO_SPIKEYS_FROG] = Formation(
    [
        FormationMember(Spikey, x_pos=135, y_pos=119),
        FormationMember(Spikey, x_pos=199, y_pos=151),
        FormationMember(Frogog, x_pos=199, y_pos=119),
    ]
)
formations[FORM0007_THREE_SPIKEYS] = Formation(
    [
        FormationMember(Spikey, x_pos=135, y_pos=119),
        FormationMember(Spikey, x_pos=199, y_pos=119),
        FormationMember(Spikey, x_pos=199, y_pos=151),
    ]
)
formations[FORM0008_ONE_TROOPA] = Formation(
    [FormationMember(Skytroopa, x_pos=167, y_pos=135)]
)
formations[FORM0009_TWO_TROOPAS] = Formation(
    [
        FormationMember(Skytroopa, x_pos=135, y_pos=119),
        FormationMember(Skytroopa, x_pos=199, y_pos=151),
    ]
)
formations[FORM0010_TWO_TROOPAS_FROG] = Formation(
    [
        FormationMember(Skytroopa, x_pos=199, y_pos=151),
        FormationMember(Skytroopa, x_pos=135, y_pos=119),
        FormationMember(Frogog, x_pos=183, y_pos=127),
    ]
)
formations[FORM0011_TWO_TROOPAS_GOOMBA] = Formation(
    [
        FormationMember(Skytroopa, x_pos=167, y_pos=103),
        FormationMember(Skytroopa, x_pos=231, y_pos=135),
        None,
        FormationMember(Goomba, x_pos=167, y_pos=135),
    ]
)
formations[FORM0012_TWO_GOOMBAS] = Formation(
    [
        FormationMember(Goomba, x_pos=135, y_pos=119),
        FormationMember(Goomba, x_pos=215, y_pos=135),
    ]
)
formations[FORM0013_THREE_GOOMBAS] = Formation(
    [
        FormationMember(Goomba, x_pos=167, y_pos=111),
        FormationMember(Goomba, x_pos=167, y_pos=135),
        FormationMember(Goomba, x_pos=215, y_pos=135),
    ]
)
formations[FORM0014_TWO_GOOMBAS_SPIKEY] = Formation(
    [
        FormationMember(Goomba, x_pos=167, y_pos=111),
        FormationMember(Goomba, x_pos=215, y_pos=135),
        FormationMember(Spikey, x_pos=167, y_pos=135),
    ]
)
formations[FORM0015_GOOMBA_FROG_SPIKEY] = Formation(
    [
        FormationMember(Goomba, x_pos=167, y_pos=135),
        FormationMember(Frogog, x_pos=167, y_pos=111),
        FormationMember(Spikey, x_pos=215, y_pos=135),
    ]
)
formations[FORM0016_ONE_K9] = Formation(
    [
        FormationMember(K9, x_pos=167, y_pos=135),
    ]
)
formations[FORM0017_TWO_K9] = Formation(
    [
        FormationMember(K9, x_pos=199, y_pos=159),
        FormationMember(K9, x_pos=151, y_pos=119),
    ]
)
formations[FORM0018_TWO_K9_SPIKEY] = Formation(
    [
        FormationMember(K9, x_pos=135, y_pos=119),
        FormationMember(K9, x_pos=199, y_pos=151),
        FormationMember(Spikey, x_pos=199, y_pos=119),
    ]
)
formations[FORM0019_ONE_K9_TWO_FROG] = Formation(
    [
        FormationMember(K9, x_pos=183, y_pos=127),
        FormationMember(Frogog, x_pos=215, y_pos=143),
        FormationMember(Frogog, x_pos=151, y_pos=111),
    ]
)
formations[FORM0020_TWO_BODYGUARDS] = Formation(
    [
        FormationMember(Bodyguard, x_pos=167, y_pos=119),
        FormationMember(Bodyguard, x_pos=199, y_pos=135),
    ]
)
formations[FORM0021_TWO_SHYSTER] = Formation(
    [
        FormationMember(Shyster, x_pos=167, y_pos=119),
        FormationMember(Shyster, x_pos=199, y_pos=135),
    ]
)
formations[FORM0022_THREE_SHYSTER] = Formation(
    [
        FormationMember(Shyster, x_pos=151, y_pos=111),
        FormationMember(Shyster, x_pos=215, y_pos=143),
        FormationMember(Shyster, x_pos=167, y_pos=135),
    ]
)
formations[FORM0023_THREE_BODYGUARD] = Formation(
    [
        FormationMember(Bodyguard, x_pos=151, y_pos=111),
        FormationMember(Bodyguard, x_pos=215, y_pos=143),
        FormationMember(Bodyguard, x_pos=167, y_pos=135),
    ]
)
formations[FORM0024_TWO_RATFUNKS] = Formation(
    [
        FormationMember(Ratfunk, x_pos=199, y_pos=143),
        FormationMember(Ratfunk, x_pos=151, y_pos=111),
    ]
)
formations[FORM0025_TWO_RATFUNKS_ONE_SHADOW] = Formation(
    [
        FormationMember(Ratfunk, x_pos=135, y_pos=119),
        FormationMember(Ratfunk, x_pos=199, y_pos=151),
        FormationMember(Shadow, x_pos=199, y_pos=119),
    ]
)
formations[FORM0026_TWO_RATFUNKS_ONE_HOBGOBLIN] = Formation(
    [
        FormationMember(Ratfunk, x_pos=135, y_pos=119),
        FormationMember(Ratfunk, x_pos=199, y_pos=151),
        FormationMember(Hobgoblin, x_pos=199, y_pos=119),
    ]
)
formations[FORM0027_ONE_RATFUNK_TWO_HOBGOBLINS] = Formation(
    [
        FormationMember(Ratfunk, x_pos=167, y_pos=135),
        None,
        FormationMember(Hobgoblin, x_pos=167, y_pos=103),
        FormationMember(Hobgoblin, x_pos=231, y_pos=135),
    ]
)
formations[28] = None
formations[FORM0029_ONE_BIGBOO_ONE_SHADOW] = Formation(
    [
        FormationMember(TheBigBoo, x_pos=151, y_pos=119),
        FormationMember(Shadow, x_pos=199, y_pos=143),
    ]
)
formations[FORM0030_BIGBOO_SHADOW_HOBGOBLIN] = Formation(
    [
        FormationMember(TheBigBoo, x_pos=119, y_pos=119),
        FormationMember(Shadow, x_pos=167, y_pos=135),
        FormationMember(Hobgoblin, x_pos=215, y_pos=143),
    ]
)
formations[FORM0031_THREE_BIGBOO_ONE_SHADOW] = Formation(
    [
        FormationMember(TheBigBoo, x_pos=231, y_pos=135),
        FormationMember(TheBigBoo, x_pos=151, y_pos=143),
        FormationMember(TheBigBoo, x_pos=167, y_pos=103),
        FormationMember(Shadow, x_pos=183, y_pos=127),
    ]
)
formations[32] = None
formations[FORM0033_TWO_GOBYS] = Formation(
    [
        FormationMember(Goby, x_pos=135, y_pos=119),
        FormationMember(Goby, x_pos=199, y_pos=151),
    ]
)
formations[FORM0034_THREE_GOBYS] = Formation(
    [
        FormationMember(Goby, x_pos=151, y_pos=119),
        FormationMember(Goby, x_pos=215, y_pos=119),
        FormationMember(Goby, x_pos=183, y_pos=151),
    ]
)
formations[35] = None
formations[FORM0036_TWO_CROOKS] = Formation(
    [
        FormationMember(Crook, x_pos=167, y_pos=111),
        FormationMember(Crook, x_pos=199, y_pos=151),
    ]
)
formations[FORM0037_TWO_CROOKS_ONE_SHYGUY] = Formation(
    [
        FormationMember(Crook, x_pos=199, y_pos=143),
        FormationMember(Crook, x_pos=151, y_pos=119),
        FormationMember(ShyGuy, x_pos=199, y_pos=119),
    ]
)
formations[FORM0038_ONE_CROOK_TWO_SNAPDRAGONS] = Formation(
    [
        FormationMember(Crook, x_pos=183, y_pos=127),
        FormationMember(Snapdragon, x_pos=151, y_pos=111),
        FormationMember(Snapdragon, x_pos=215, y_pos=143),
    ]
)
formations[FORM0039_CROOK_STARSLAP_ARACHNE] = Formation(
    [
        FormationMember(Crook, x_pos=199, y_pos=159),
        None,
        None,
        FormationMember(Starslap, x_pos=215, y_pos=127),
        FormationMember(Arachne, x_pos=167, y_pos=103),
    ]
)
formations[FORM0040_ONE_SHYGUY_HENCHMAN] = Formation(
    [
        FormationMember(ShyGuyHenchman, x_pos=167, y_pos=135),
    ]
)
formations[FORM0041_ONE_SHYGUY_ONE_STARSLAP] = Formation(
    [
        FormationMember(ShyGuy, x_pos=151, y_pos=111),
        None,
        FormationMember(Starslap, x_pos=199, y_pos=151),
    ]
)
formations[FORM0042_TWO_SHYGUYS_ONE_SNAPDRAGON] = Formation(
    [
        FormationMember(ShyGuy, x_pos=135, y_pos=103),
        FormationMember(ShyGuy, x_pos=215, y_pos=143),
        None,
        FormationMember(Snapdragon, x_pos=183, y_pos=127),
    ]
)
formations[FORM0043_SHYGUY_CROOK_ARACHNE] = Formation(
    [
        FormationMember(ShyGuy, x_pos=231, y_pos=135),
        None,
        FormationMember(Crook, x_pos=199, y_pos=143),
        FormationMember(Arachne, x_pos=151, y_pos=111),
    ]
)
formations[FORM0044_STARSLAP_SHYGUY] = Formation(
    [
        FormationMember(Starslap, x_pos=199, y_pos=159),
        FormationMember(ShyGuy, x_pos=151, y_pos=111),
    ]
)
formations[FORM0045_STARSLAP_ARACHNE] = Formation(
    [
        FormationMember(Starslap, x_pos=215, y_pos=151),
        FormationMember(Arachne, x_pos=151, y_pos=111),
    ]
)
formations[FORM0046_STARSLAP_TWO_SNAPDRAGONS] = Formation(
    [
        FormationMember(Starslap, x_pos=167, y_pos=135),
        FormationMember(Snapdragon, x_pos=151, y_pos=111),
        FormationMember(Snapdragon, x_pos=215, y_pos=143),
    ]
)
formations[FORM0047_FOUR_STARSLAPS] = Formation(
    [
        FormationMember(Starslap, x_pos=199, y_pos=151),
        FormationMember(Starslap, x_pos=167, y_pos=103),
        FormationMember(Starslap, x_pos=231, y_pos=135),
        FormationMember(Starslap, x_pos=135, y_pos=119),
    ]
)
formations[FORM0048_ONE_WIGGLER] = Formation(
    [
        FormationMember(Wiggler, x_pos=183, y_pos=127),
    ]
)
formations[FORM0049_ONE_WIGGLER_ONE_AMANITA] = Formation(
    [
        FormationMember(Wiggler, x_pos=151, y_pos=111),
        FormationMember(Amanita, x_pos=199, y_pos=151),
    ]
)
formations[FORM0050_TWO_WIGGLERS] = Formation(
    [
        FormationMember(Wiggler, x_pos=151, y_pos=111),
        FormationMember(Wiggler, x_pos=215, y_pos=143),
    ]
)
formations[FORM0051_ONE_WIGGLER_ONE_GUERRILLA] = Formation(
    [
        FormationMember(Wiggler, x_pos=151, y_pos=119),
        None,
        FormationMember(Guerrilla, x_pos=215, y_pos=143),
    ]
)
formations[FORM0052_TWO_AMANITAS] = Formation(
    [
        FormationMember(Amanita, x_pos=135, y_pos=127),
        FormationMember(Amanita, x_pos=199, y_pos=143),
    ]
)
formations[FORM0053_TWO_AMANITAS_ONE_BUZZER] = Formation(
    [
        FormationMember(Amanita, x_pos=199, y_pos=151),
        FormationMember(Amanita, x_pos=135, y_pos=119),
        FormationMember(Buzzer, x_pos=199, y_pos=119),
    ]
)
formations[FORM0054_TWO_AMANITAS_ONE_OCTOLOT] = Formation(
    [
        FormationMember(Amanita, x_pos=199, y_pos=151),
        FormationMember(Amanita, x_pos=135, y_pos=119),
        FormationMember(Octolot, x_pos=183, y_pos=127),
    ]
)
formations[FORM0055_AMANITA_BUZZER_GUERRILLA] = Formation(
    [
        FormationMember(Amanita, x_pos=151, y_pos=127),
        None,
        FormationMember(Guerrilla, x_pos=215, y_pos=143),
        FormationMember(Buzzer, x_pos=183, y_pos=111),
    ]
)
formations[FORM0056_BUZZER_OCTOLOT] = Formation(
    [
        FormationMember(Buzzer, x_pos=135, y_pos=119),
        FormationMember(Octolot, x_pos=199, y_pos=143),
    ]
)
formations[FORM0057_TWO_BUZZERS_ONE_AMANITA] = Formation(
    [
        FormationMember(Buzzer, x_pos=167, y_pos=103),
        FormationMember(Buzzer, x_pos=231, y_pos=135),
        FormationMember(Amanita, x_pos=167, y_pos=135),
    ]
)
formations[FORM0058_BUZZER_GUERRILLA] = Formation(
    [
        FormationMember(Buzzer, x_pos=199, y_pos=151),
        None,
        FormationMember(Guerrilla, x_pos=151, y_pos=119),
    ]
)
formations[FORM0059_BUZZER_GUERRILLA_2] = Formation(
    [
        FormationMember(Buzzer, x_pos=199, y_pos=159),
        None,
        FormationMember(Guerrilla, x_pos=135, y_pos=119),
    ]
)
formations[FORM0060_ONE_SPARKY] = Formation(
    [
        FormationMember(Sparky, x_pos=183, y_pos=127),
    ]
)
formations[FORM0061_TWO_SPARKY_ONE_SHYRANGER] = Formation(
    [
        FormationMember(Sparky, x_pos=167, y_pos=111),
        FormationMember(Sparky, x_pos=215, y_pos=135),
        FormationMember(ShyRanger, x_pos=167, y_pos=135),
    ]
)
formations[FORM0062_THREE_SPARKY] = Formation(
    [
        FormationMember(Sparky, x_pos=167, y_pos=135),
        FormationMember(Sparky, x_pos=151, y_pos=111),
        FormationMember(Sparky, x_pos=215, y_pos=143),
    ]
)
formations[63] = None
formations[64] = None
formations[65] = None
formations[66] = None
formations[67] = None
formations[FORM0068_ONE_PIRANHA] = Formation(
    [
        FormationMember(PiranhaPlant, x_pos=167, y_pos=135),
    ]
)
formations[FORM0069_TWO_PIRANHA_ONE_SHYRANGER] = Formation(
    [
        FormationMember(PiranhaPlant, x_pos=215, y_pos=143),
        FormationMember(PiranhaPlant, x_pos=151, y_pos=111),
        FormationMember(ShyRanger, x_pos=183, y_pos=127),
    ]
)
formations[FORM0070_THREE_PIRANHA] = Formation(
    [
        FormationMember(PiranhaPlant, x_pos=167, y_pos=111),
        FormationMember(PiranhaPlant, x_pos=167, y_pos=135),
        FormationMember(PiranhaPlant, x_pos=215, y_pos=135),
    ]
)
formations[FORM0071_FIVE_PIRANHA] = Formation(
    [
        FormationMember(PiranhaPlant, x_pos=151, y_pos=143),
        FormationMember(PiranhaPlant, x_pos=151, y_pos=111),
        FormationMember(PiranhaPlant, x_pos=199, y_pos=119),
        FormationMember(PiranhaPlant, x_pos=231, y_pos=143),
        FormationMember(PiranhaPlant, x_pos=199, y_pos=159),
    ]
)
formations[FORM0072_ONE_BOBOMB] = Formation(
    [
        FormationMember(Bobomb, x_pos=183, y_pos=127),
    ]
)
formations[FORM0073_TWO_BOBOMB_ONE_CLUSTER] = Formation(
    [
        FormationMember(Bobomb, x_pos=135, y_pos=119),
        FormationMember(Bobomb, x_pos=199, y_pos=151),
        FormationMember(Cluster, x_pos=199, y_pos=119),
    ]
)
formations[FORM0074_FOUR_BOBOMB] = Formation(
    [
        FormationMember(Bobomb, x_pos=151, y_pos=127),
        FormationMember(Bobomb, x_pos=167, y_pos=103),
        FormationMember(Bobomb, x_pos=199, y_pos=151),
        None,
        FormationMember(Bobomb, x_pos=215, y_pos=127),
    ]
)
formations[FORM0075_TWO_BOBOMB_ENIGMA_CLUSTER] = Formation(
    [
        FormationMember(Bobomb, x_pos=135, y_pos=119),
        FormationMember(Bobomb, x_pos=199, y_pos=151),
        FormationMember(Enigma, x_pos=183, y_pos=111),
        FormationMember(Cluster, x_pos=215, y_pos=127),
    ]
)
formations[FORM0076_SPARKY_ENIGMA] = Formation(
    [
        FormationMember(Sparky, x_pos=199, y_pos=151),
        FormationMember(Enigma, x_pos=167, y_pos=111),
    ]
)
formations[FORM0077_TWO_SPARKY_ONE_BOBOMB] = Formation(
    [
        FormationMember(Sparky, x_pos=167, y_pos=111),
        FormationMember(Sparky, x_pos=215, y_pos=135),
        FormationMember(Bobomb, x_pos=167, y_pos=135),
    ]
)
formations[FORM0078_ONE_SPARKY_TWO_CLUSTER] = Formation(
    [
        FormationMember(Sparky, x_pos=183, y_pos=127),
        FormationMember(Cluster, x_pos=231, y_pos=143),
        FormationMember(Cluster, x_pos=151, y_pos=103),
    ]
)
formations[FORM0079_TWO_SPARKY_TWO_ENIGMA] = Formation(
    [
        FormationMember(Sparky, x_pos=183, y_pos=143),
        FormationMember(Sparky, x_pos=151, y_pos=127),
        FormationMember(Enigma, x_pos=167, y_pos=103),
        FormationMember(Enigma, x_pos=231, y_pos=135),
    ]
)
formations[FORM0080_TWO_MAGMITE] = Formation(
    [
        FormationMember(Magmite, x_pos=167, y_pos=111),
        FormationMember(Magmite, x_pos=199, y_pos=151),
    ]
)
formations[FORM0081_MAGMITE_BOBOMB_SPARKY] = Formation(
    [
        FormationMember(Magmite, x_pos=151, y_pos=111),
        FormationMember(Bobomb, x_pos=183, y_pos=127),
        FormationMember(Sparky, x_pos=215, y_pos=143),
    ]
)
formations[FORM0082_TWO_MAGMITE_TWO_CLUSTER] = Formation(
    [
        FormationMember(Magmite, x_pos=151, y_pos=127),
        FormationMember(Magmite, x_pos=183, y_pos=143),
        FormationMember(Cluster, x_pos=167, y_pos=103),
        FormationMember(Cluster, x_pos=231, y_pos=135),
    ]
)
formations[FORM0083_TWO_MAGMITE_BOBOMB_CLUSTER] = Formation(
    [
        FormationMember(Magmite, x_pos=135, y_pos=103),
        FormationMember(Magmite, x_pos=231, y_pos=151),
        FormationMember(Bobomb, x_pos=167, y_pos=135),
        None,
        FormationMember(Cluster, x_pos=199, y_pos=119),
    ]
)
formations[FORM0084_ONE_LAKITU] = Formation(
    [
        FormationMember(Lakitu, x_pos=183, y_pos=127),
    ]
)
formations[FORM0085_LAKITU_SPIKESTER_ARTICHOKER] = Formation(
    [
        FormationMember(Lakitu, x_pos=135, y_pos=119),
        FormationMember(Spikester, x_pos=199, y_pos=159),
        FormationMember(Artichoker, x_pos=183, y_pos=119),
    ]
)
formations[FORM0086_THREE_LAKITU] = Formation(
    [
        FormationMember(Lakitu, x_pos=151, y_pos=111),
        FormationMember(Lakitu, x_pos=183, y_pos=127),
        FormationMember(Lakitu, x_pos=215, y_pos=143),
    ]
)
formations[FORM0087_TWO_LAKITU_ONE_ARTICHOKER] = Formation(
    [
        FormationMember(Lakitu, x_pos=231, y_pos=151),
        FormationMember(Lakitu, x_pos=135, y_pos=103),
        None,
        FormationMember(Artichoker, x_pos=183, y_pos=127),
    ]
)
formations[FORM0088_SPIKESTER_CARROBOSCIS] = Formation(
    [
        FormationMember(Spikester, x_pos=215, y_pos=143),
        FormationMember(Carriboscis, x_pos=135, y_pos=119),
    ]
)
formations[FORM0089_TWO_SPIKESTER_ONE_ARTICHOKER] = Formation(
    [
        FormationMember(Spikester, x_pos=199, y_pos=151),
        FormationMember(Spikester, x_pos=135, y_pos=119),
        FormationMember(Artichoker, x_pos=199, y_pos=119),
    ]
)
formations[FORM0090_ONE_SPIKESTER_TWO_CARROBOSCIS] = Formation(
    [
        FormationMember(Spikester, x_pos=183, y_pos=127),
        FormationMember(Carriboscis, x_pos=135, y_pos=119),
        FormationMember(Carriboscis, x_pos=199, y_pos=151),
    ]
)
formations[FORM0091_FOUR_SPIKESTER_ONE_CARROBOSCIS] = Formation(
    [
        FormationMember(Spikester, x_pos=119, y_pos=111),
        FormationMember(Spikester, x_pos=215, y_pos=159),
        FormationMember(Spikester, x_pos=215, y_pos=135),
        FormationMember(Spikester, x_pos=167, y_pos=111),
        FormationMember(Carriboscis, x_pos=151, y_pos=143),
    ]
)
formations[FORM0092_SPOOKUM_ORBUSER] = Formation(
    [
        FormationMember(Spookum, x_pos=199, y_pos=135),
        FormationMember(Orbuser, x_pos=135, y_pos=119),
    ],
    can_run_away=False,
)
formations[FORM0093_TWO_SPOOKUM_ONE_JESTER] = Formation(
    [
        FormationMember(Spookum, x_pos=135, y_pos=119),
        FormationMember(Spookum, x_pos=199, y_pos=151),
        FormationMember(Jester, x_pos=199, y_pos=119),
    ],
    can_run_away=False,
)
formations[FORM0094_SPOOKUM_REMOCON_ORBUSER] = Formation(
    [
        FormationMember(Spookum, x_pos=151, y_pos=111),
        FormationMember(Remocon, x_pos=167, y_pos=151),
        FormationMember(Orbuser, x_pos=215, y_pos=127),
    ],
    can_run_away=False,
)
formations[FORM0095_TWO_SPOOKUM_ONE_REMOCON] = Formation(
    [
        FormationMember(Spookum, x_pos=135, y_pos=119),
        FormationMember(Spookum, x_pos=199, y_pos=151),
        FormationMember(Remocon, x_pos=199, y_pos=119),
    ],
    can_run_away=False,
)
formations[FORM0096_ONE_ROBOMB] = Formation(
    [
        FormationMember(Robomb, x_pos=183, y_pos=127),
    ]
)
formations[FORM0097_THREE_ROBOMB] = Formation(
    [
        FormationMember(Robomb, x_pos=183, y_pos=127),
        FormationMember(Robomb, x_pos=199, y_pos=119),
        FormationMember(Robomb, x_pos=167, y_pos=135),
    ]
)
formations[FORM0098_TWO_ROBOMB_ONE_REMOCON] = Formation(
    [
        FormationMember(Robomb, x_pos=215, y_pos=143),
        FormationMember(Robomb, x_pos=151, y_pos=111),
        FormationMember(Remocon, x_pos=183, y_pos=127),
    ]
)
formations[FORM0099_FOUR_ROBOMB_ONE_ORBUSER] = Formation(
    [
        FormationMember(Robomb, x_pos=135, y_pos=127),
        FormationMember(Robomb, x_pos=231, y_pos=127),
        FormationMember(Robomb, x_pos=183, y_pos=103),
        FormationMember(Robomb, x_pos=183, y_pos=151),
        FormationMember(Orbuser, x_pos=183, y_pos=127),
    ]
)
formations[FORM0100_CHOMP_JESTER] = Formation(
    [
        FormationMember(Chomp, x_pos=215, y_pos=143),
        FormationMember(Jester, x_pos=167, y_pos=111),
    ]
)
formations[FORM0101_CHOMP_ROBOMB_REMOCON] = Formation(
    [
        FormationMember(Chomp, x_pos=215, y_pos=143),
        FormationMember(Robomb, x_pos=151, y_pos=135),
        FormationMember(Remocon, x_pos=167, y_pos=103),
    ]
)
formations[FORM0102_TWO_CHOMP_ONE_ORBUSER] = Formation(
    [
        FormationMember(Chomp, x_pos=151, y_pos=111),
        FormationMember(Chomp, x_pos=215, y_pos=143),
        FormationMember(Orbuser, x_pos=183, y_pos=127),
    ]
)
formations[FORM0103_ONE_CHOMP_TWO_JESTER] = Formation(
    [
        FormationMember(Chomp, x_pos=199, y_pos=119),
        None,
        FormationMember(Jester, x_pos=135, y_pos=103),
        FormationMember(Jester, x_pos=231, y_pos=151),
    ]
)
formations[FORM0104_BLASTER_SPOOKUM] = Formation(
    [
        FormationMember(Blaster, x_pos=167, y_pos=135),
        FormationMember(Spookum, x_pos=199, y_pos=119),
    ]
)
formations[FORM0105_BLASTER_SPOOKUM_REMOCON] = Formation(
    [
        FormationMember(Blaster, x_pos=167, y_pos=135),
        FormationMember(Spookum, x_pos=151, y_pos=111),
        FormationMember(Remocon, x_pos=215, y_pos=143),
    ]
)
formations[FORM0106_TWO_BLASTER_ONE_SPOOKUM] = Formation(
    [
        FormationMember(Blaster, x_pos=199, y_pos=151),
        FormationMember(Blaster, x_pos=135, y_pos=119),
        FormationMember(Spookum, x_pos=199, y_pos=119),
    ]
)
formations[FORM0107_BLASTER_TWO_ROBOMB_TWO_SPOOKUM] = Formation(
    [
        FormationMember(Blaster, x_pos=199, y_pos=119),
        FormationMember(Robomb, x_pos=135, y_pos=103),
        FormationMember(Robomb, x_pos=231, y_pos=151),
        FormationMember(Spookum, x_pos=151, y_pos=127),
        FormationMember(Spookum, x_pos=183, y_pos=143),
    ]
)
formations[FORM0108_ONE_TORTE] = Formation(
    [
        FormationMember(Torte, x_pos=183, y_pos=127),
    ]
)
formations[FORM0109_TWO_TORTE] = Formation(
    [
        FormationMember(Torte, x_pos=215, y_pos=143),
        FormationMember(Torte, x_pos=151, y_pos=111),
    ]
)
formations[FORM0110_THREE_TORTE] = Formation(
    [
        FormationMember(Torte, x_pos=183, y_pos=103),
        FormationMember(Torte, x_pos=151, y_pos=135),
        FormationMember(Torte, x_pos=215, y_pos=135),
    ]
)
formations[FORM0111_FOUR_TORTE] = Formation(
    [
        FormationMember(Torte, x_pos=167, y_pos=135),
        FormationMember(Torte, x_pos=199, y_pos=119),
        FormationMember(Torte, x_pos=151, y_pos=111),
        FormationMember(Torte, x_pos=215, y_pos=143),
    ]
)
formations[FORM0112_ONE_MUKU] = Formation(
    [
        FormationMember(Mukumuku, x_pos=183, y_pos=127),
    ]
)
formations[FORM0113_TWO_MUKU] = Formation(
    [
        FormationMember(Mukumuku, x_pos=151, y_pos=119),
        FormationMember(Mukumuku, x_pos=215, y_pos=135),
    ]
)
formations[FORM0114_TWO_MUKU_ONE_PULSAR] = Formation(
    [
        FormationMember(Mukumuku, x_pos=151, y_pos=111),
        FormationMember(Mukumuku, x_pos=215, y_pos=143),
        FormationMember(Pulsar, x_pos=167, y_pos=135),
    ]
)
formations[FORM0115_MUKU_PULSAR_GECKO] = Formation(
    [
        FormationMember(Mukumuku, x_pos=183, y_pos=143),
        FormationMember(Pulsar, x_pos=151, y_pos=111),
        FormationMember(Gecko, x_pos=231, y_pos=143),
    ]
)
formations[FORM0116_TWO_SACKIT] = Formation(
    [
        FormationMember(Sackit, x_pos=199, y_pos=151),
        FormationMember(Sackit, x_pos=167, y_pos=111),
    ]
)
formations[FORM0117_TWO_SACKIT_MUKU_GECKO] = Formation(
    [
        FormationMember(Sackit, x_pos=151, y_pos=127),
        FormationMember(Sackit, x_pos=183, y_pos=143),
        FormationMember(Mukumuku, x_pos=167, y_pos=103),
        FormationMember(Gecko, x_pos=231, y_pos=135),
    ]
)
formations[FORM0118_ONE_SACKIT_TWO_PULSAR] = Formation(
    [
        FormationMember(Sackit, x_pos=167, y_pos=135),
        None,
        None,
        FormationMember(Pulsar, x_pos=167, y_pos=103),
        FormationMember(Pulsar, x_pos=231, y_pos=135),
    ]
)
formations[FORM0119_SACKIT_MASTADOOM] = Formation(
    [
        FormationMember(Sackit, x_pos=215, y_pos=143),
        FormationMember(Mastadoom, x_pos=167, y_pos=103),
    ]
)
formations[FORM0120_GECKO_SACKIT] = Formation(
    [
        FormationMember(Gecko, x_pos=151, y_pos=119),
        FormationMember(Sackit, x_pos=199, y_pos=143),
    ]
)
formations[FORM0121_GECKO_MASTADOOM] = Formation(
    [
        FormationMember(Gecko, x_pos=151, y_pos=119),
        FormationMember(Mastadoom, x_pos=215, y_pos=135),
    ]
)
formations[FORM0122_TWO_GECKO_TWO_MUKU_TWO_SACKIT] = Formation(
    [
        FormationMember(Gecko, x_pos=183, y_pos=143),
        FormationMember(Gecko, x_pos=151, y_pos=127),
        FormationMember(Mukumuku, x_pos=135, y_pos=103),
        FormationMember(Mukumuku, x_pos=231, y_pos=151),
        FormationMember(Sackit, x_pos=183, y_pos=111),
        FormationMember(Sackit, x_pos=215, y_pos=127),
    ]
)
formations[FORM0123_TWO_GECKO_ONE_MASTADOOM] = Formation(
    [
        FormationMember(Gecko, x_pos=135, y_pos=103),
        FormationMember(Gecko, x_pos=231, y_pos=151),
        FormationMember(Mastadoom, x_pos=199, y_pos=119),
    ]
)
formations[FORM0124_TWO_ZEOSTAR] = Formation(
    [
        FormationMember(Zeostar, x_pos=135, y_pos=119),
        FormationMember(Zeostar, x_pos=215, y_pos=135),
    ]
)
formations[FORM0125_TWO_ZEOSTAR_ONE_BLOOBER] = Formation(
    [
        FormationMember(Zeostar, x_pos=151, y_pos=135),
        FormationMember(Zeostar, x_pos=183, y_pos=103),
        FormationMember(Bloober, x_pos=215, y_pos=135),
    ]
)
formations[FORM0126_TWO_ZEOSTAR_TWO_LEUKO] = Formation(
    [
        FormationMember(Zeostar, x_pos=199, y_pos=119),
        FormationMember(Zeostar, x_pos=167, y_pos=135),
        FormationMember(Leuko, x_pos=167, y_pos=103),
        FormationMember(Leuko, x_pos=231, y_pos=135),
    ]
)
formations[FORM0127_ZEOSTAR_LEUKO_CRUSTY] = Formation(
    [
        FormationMember(Zeostar, x_pos=183, y_pos=127),
        FormationMember(Leuko, x_pos=215, y_pos=143),
        FormationMember(Crusty, x_pos=151, y_pos=111),
    ]
)
formations[FORM0128_BLOOPER_KIPPER] = Formation(
    [
        FormationMember(Bloober, x_pos=151, y_pos=111),
        FormationMember(MrKipper, x_pos=215, y_pos=143),
    ]
)
formations[FORM0129_THREE_BLOOBER] = Formation(
    [
        FormationMember(Bloober, x_pos=183, y_pos=127),
        FormationMember(Bloober, x_pos=231, y_pos=143),
        FormationMember(Bloober, x_pos=135, y_pos=111),
    ]
)
formations[FORM0130_TWO_BLOOBER_KIPPER_CRUSTY] = Formation(
    [
        FormationMember(Bloober, x_pos=151, y_pos=111),
        FormationMember(Bloober, x_pos=231, y_pos=151),
        FormationMember(MrKipper, x_pos=151, y_pos=143),
        FormationMember(Crusty, x_pos=199, y_pos=119),
    ]
)
formations[FORM0131_TWO_BLOOBER_TWO_ZEOSTAR_ONE_LEUKO] = Formation(
    [
        FormationMember(Bloober, x_pos=231, y_pos=135),
        FormationMember(Bloober, x_pos=167, y_pos=103),
        FormationMember(Zeostar, x_pos=135, y_pos=127),
        FormationMember(Zeostar, x_pos=183, y_pos=151),
        FormationMember(Leuko, x_pos=183, y_pos=127),
    ]
)
formations[FORM0132_THREE_KIPPER] = Formation(
    [
        FormationMember(MrKipper, x_pos=151, y_pos=103),
        FormationMember(MrKipper, x_pos=215, y_pos=151),
        FormationMember(MrKipper, x_pos=183, y_pos=127),
    ]
)
formations[FORM0133_TWO_KIPPER_ONE_CRUSTY] = Formation(
    [
        FormationMember(MrKipper, x_pos=199, y_pos=151),
        FormationMember(MrKipper, x_pos=135, y_pos=119),
        FormationMember(Crusty, x_pos=199, y_pos=119),
    ]
)
formations[FORM0134_TWO_KIPPER_ONE_CRUSTY_2] = Formation(
    [
        FormationMember(MrKipper, x_pos=135, y_pos=119),
        FormationMember(MrKipper, x_pos=231, y_pos=135),
        FormationMember(Crusty, x_pos=183, y_pos=127),
    ]
)
formations[FORM0135_FOUR_KIPPER] = Formation(
    [
        FormationMember(MrKipper, x_pos=215, y_pos=127),
        FormationMember(MrKipper, x_pos=199, y_pos=151),
        FormationMember(MrKipper, x_pos=167, y_pos=103),
        FormationMember(MrKipper, x_pos=151, y_pos=127),
    ]
)
formations[FORM0136_FOUR_BANDANA_RED] = Formation(
    [
        FormationMember(BandanaRed, x_pos=151, y_pos=127),
        FormationMember(BandanaRed, x_pos=183, y_pos=143),
        FormationMember(BandanaRed, x_pos=167, y_pos=103),
        FormationMember(BandanaRed, x_pos=231, y_pos=135),
    ]
)
formations[FORM0137_FIVE_BANDANA_RED] = Formation(
    [
        FormationMember(BandanaRed, x_pos=199, y_pos=151),
        FormationMember(BandanaRed, x_pos=135, y_pos=119),
        FormationMember(BandanaRed, x_pos=215, y_pos=127),
        FormationMember(BandanaRed, x_pos=167, y_pos=135),
        FormationMember(BandanaRed, x_pos=183, y_pos=111),
    ]
)
formations[138] = None
formations[139] = None
formations[FORM0140_ONE_BANDANABLUE] = Formation(
    [
        FormationMember(BandanaBlue, x_pos=183, y_pos=127),
    ]
)
formations[FORM0141_FOUR_BANDANARED_HENCHMEN] = Formation(
    [
        FormationMember(BandanaRedHenchman, x_pos=151, y_pos=127),
        FormationMember(BandanaRedHenchman, x_pos=183, y_pos=143),
        FormationMember(BandanaRedHenchman, x_pos=167, y_pos=103),
        FormationMember(BandanaRedHenchman, x_pos=231, y_pos=135),
    ]
)
formations[FORM0142_FOUR_BANDANABLUE] = Formation(
    [
        FormationMember(BandanaBlue, x_pos=135, y_pos=127),
        FormationMember(BandanaBlue, x_pos=167, y_pos=111),
        FormationMember(BandanaBlue, x_pos=183, y_pos=151),
        FormationMember(BandanaBlue, x_pos=215, y_pos=135),
    ]
)
formations[FORM0143_FIVE_BANDANARED_HENCHMEN] = Formation(
    [
        FormationMember(BandanaRedHenchman, x_pos=199, y_pos=151),
        FormationMember(BandanaRedHenchman, x_pos=135, y_pos=119),
        FormationMember(BandanaRedHenchman, x_pos=215, y_pos=127),
        FormationMember(BandanaRedHenchman, x_pos=167, y_pos=135),
        FormationMember(BandanaRedHenchman, x_pos=183, y_pos=111),
    ]
)
formations[FORM0144_TWO_DRYBONES] = Formation(
    [
        FormationMember(DryBones, x_pos=199, y_pos=151),
        FormationMember(DryBones, x_pos=151, y_pos=111),
    ]
)
formations[FORM0145_TWO_DRYBONES_ONE_GREAPER] = Formation(
    [
        FormationMember(DryBones, x_pos=135, y_pos=119),
        FormationMember(DryBones, x_pos=199, y_pos=151),
        FormationMember(Greaper, x_pos=199, y_pos=119),
    ]
)
formations[FORM0146_DRYBONES_GREAPER_REACHER] = Formation(
    [
        FormationMember(DryBones, x_pos=135, y_pos=119),
        FormationMember(Greaper, x_pos=199, y_pos=151),
        FormationMember(Reacher, x_pos=199, y_pos=119),
    ]
)
formations[FORM0147_TWO_DRYBONES_TWO_GREAPER_ONE_REACHER] = Formation(
    [
        FormationMember(DryBones, x_pos=167, y_pos=103),
        FormationMember(DryBones, x_pos=231, y_pos=135),
        FormationMember(Greaper, x_pos=151, y_pos=127),
        FormationMember(Greaper, x_pos=183, y_pos=143),
        FormationMember(Reacher, x_pos=199, y_pos=119),
    ]
)
formations[FORM0148_ALLEYRAT_GORGON] = Formation(
    [
        FormationMember(AlleyRat, x_pos=199, y_pos=151),
        FormationMember(Gorgon, x_pos=151, y_pos=111),
    ]
)
formations[FORM0149_TWO_ALLEYRAT_TWO_GREAPER] = Formation(
    [
        FormationMember(AlleyRat, x_pos=135, y_pos=119),
        FormationMember(AlleyRat, x_pos=199, y_pos=151),
        FormationMember(Greaper, x_pos=215, y_pos=127),
        FormationMember(Greaper, x_pos=183, y_pos=111),
    ]
)
formations[FORM0150_TWO_ALLEYRAT_TWO_GORGON] = Formation(
    [
        FormationMember(AlleyRat, x_pos=151, y_pos=127),
        FormationMember(AlleyRat, x_pos=199, y_pos=151),
        FormationMember(Gorgon, x_pos=183, y_pos=111),
        FormationMember(Gorgon, x_pos=231, y_pos=135),
    ]
)
formations[FORM0151_ALLEYRAT_REACHER_GORGON] = Formation(
    [
        FormationMember(AlleyRat, x_pos=231, y_pos=135),
        FormationMember(Reacher, x_pos=167, y_pos=135),
        FormationMember(Gorgon, x_pos=167, y_pos=103),
    ]
)
formations[FORM0152_ONE_GREAPER] = Formation(
    [
        FormationMember(Greaper, x_pos=183, y_pos=127),
    ]
)
formations[FORM0153_TWO_GREAPER_ONE_REACHER] = Formation(
    [
        FormationMember(Greaper, x_pos=151, y_pos=119),
        FormationMember(Greaper, x_pos=199, y_pos=143),
        FormationMember(Reacher, x_pos=199, y_pos=119),
    ]
)
formations[FORM0154_GREAPER_STRAWHEAD_REACHER] = Formation(
    [
        FormationMember(Greaper, x_pos=167, y_pos=135),
        FormationMember(Strawhead, x_pos=215, y_pos=135),
        FormationMember(Reacher, x_pos=167, y_pos=111),
    ]
)
formations[FORM0155_GREAPER_GORGON_TWO_STRAWHEAD] = Formation(
    [
        FormationMember(Greaper, x_pos=167, y_pos=135),
        FormationMember(Gorgon, x_pos=199, y_pos=119),
        FormationMember(Strawhead, x_pos=215, y_pos=143),
        FormationMember(Strawhead, x_pos=151, y_pos=111),
    ]
)
formations[FORM0156_ONE_DRILLBIT] = Formation(
    [
        FormationMember(DrillBit, x_pos=183, y_pos=127),
    ]
)
formations[FORM0157_TWO_DRILLBIT] = Formation(
    [
        FormationMember(DrillBit, x_pos=167, y_pos=135),
        FormationMember(DrillBit, x_pos=199, y_pos=119),
    ]
)
formations[FORM0158_THREE_DRILLBIT] = Formation(
    [
        FormationMember(DrillBit, x_pos=151, y_pos=119),
        FormationMember(DrillBit, x_pos=183, y_pos=151),
        FormationMember(DrillBit, x_pos=215, y_pos=119),
    ]
)
formations[FORM0159_FIVE_DRILLBIT] = Formation(
    [
        FormationMember(DrillBit, x_pos=167, y_pos=119),
        FormationMember(DrillBit, x_pos=199, y_pos=151),
        FormationMember(DrillBit, x_pos=135, y_pos=119),
        FormationMember(DrillBit, x_pos=199, y_pos=119),
        FormationMember(DrillBit, x_pos=199, y_pos=135),
    ]
)
formations[FORM0160_STINGER_FINKFLOWER] = Formation(
    [
        FormationMember(Stinger, x_pos=151, y_pos=111),
        FormationMember(FinkFlower, x_pos=199, y_pos=143),
    ]
)
formations[FORM0161_TWO_STINGER_ONE_OCTOVADER] = Formation(
    [
        FormationMember(Stinger, x_pos=135, y_pos=111),
        FormationMember(Stinger, x_pos=215, y_pos=151),
        FormationMember(Octovader, x_pos=199, y_pos=119),
    ]
)
formations[FORM0162_ONE_STINGER_TWO_FINKFLOWER] = Formation(
    [
        FormationMember(Stinger, x_pos=199, y_pos=119),
        None,
        FormationMember(FinkFlower, x_pos=215, y_pos=143),
        FormationMember(FinkFlower, x_pos=151, y_pos=111),
    ]
)
formations[FORM0163_FOUR_STINGER] = Formation(
    [
        FormationMember(Stinger, x_pos=183, y_pos=111),
        FormationMember(Stinger, x_pos=199, y_pos=151),
        FormationMember(Stinger, x_pos=215, y_pos=127),
        FormationMember(Stinger, x_pos=135, y_pos=119),
    ]
)
formations[FORM0164_CHOW_OCTOVADER] = Formation(
    [
        FormationMember(Chow, x_pos=135, y_pos=119),
        FormationMember(Octovader, x_pos=199, y_pos=151),
    ]
)
formations[FORM0165_CHOW_SHOGUN] = Formation(
    [
        FormationMember(Chow, x_pos=151, y_pos=111),
        FormationMember(Shogun, x_pos=215, y_pos=143),
    ]
)
formations[FORM0166_CHOW_SHOGUN_OCTOVADER] = Formation(
    [
        FormationMember(Chow, x_pos=199, y_pos=151),
        FormationMember(Shogun, x_pos=135, y_pos=119),
        FormationMember(Octovader, x_pos=199, y_pos=119),
    ]
)
formations[FORM0167_CHOW_FINKFLOWER_TWO_SHOGUN] = Formation(
    [
        FormationMember(Chow, x_pos=167, y_pos=135),
        FormationMember(FinkFlower, x_pos=199, y_pos=119),
        FormationMember(Shogun, x_pos=135, y_pos=119),
        FormationMember(Shogun, x_pos=199, y_pos=151),
    ]
)
formations[FORM0168_ONE_CHOMPCHOMP] = Formation(
    [
        FormationMember(ChompChomp, x_pos=183, y_pos=127),
    ]
)
formations[FORM0169_TWO_CHOMPCHOMP] = Formation(
    [
        FormationMember(ChompChomp, x_pos=151, y_pos=111),
        FormationMember(ChompChomp, x_pos=215, y_pos=143),
    ]
)
formations[FORM0170_THREE_CHOMPCHOMP] = Formation(
    [
        FormationMember(ChompChomp, x_pos=151, y_pos=111),
        FormationMember(ChompChomp, x_pos=199, y_pos=119),
        FormationMember(ChompChomp, x_pos=215, y_pos=143),
    ]
)
formations[FORM0171_FOUR_CHOMPCHOMP] = Formation(
    [
        FormationMember(ChompChomp, x_pos=135, y_pos=119),
        FormationMember(ChompChomp, x_pos=183, y_pos=111),
        FormationMember(ChompChomp, x_pos=215, y_pos=127),
        FormationMember(ChompChomp, x_pos=199, y_pos=151),
    ]
)
formations[FORM0172_ONE_SHYAWAY] = Formation(
    [
        FormationMember(Shyaway, x_pos=183, y_pos=127),
    ]
)
formations[FORM0173_TWO_SHYAWAY_ONE_KRIFFID] = Formation(
    [
        FormationMember(Shyaway, x_pos=151, y_pos=111),
        FormationMember(Shyaway, x_pos=215, y_pos=143),
        FormationMember(Kriffid, x_pos=183, y_pos=127),
    ]
)
formations[FORM0174_TWO_SHYAWAY_ONE_RIBBITE] = Formation(
    [
        FormationMember(Shyaway, x_pos=167, y_pos=103),
        FormationMember(Shyaway, x_pos=231, y_pos=135),
        FormationMember(Ribbite, x_pos=183, y_pos=127),
    ]
)
formations[FORM0175_SHYAWAY_GECKIT_RIBBITE] = Formation(
    [
        FormationMember(Shyaway, x_pos=215, y_pos=135),
        None,
        FormationMember(Geckit, x_pos=167, y_pos=143),
        None,
        FormationMember(Ribbite, x_pos=167, y_pos=111),
    ]
)
formations[FORM0176_TWO_CHEWY] = Formation(
    [
        FormationMember(Chewy, x_pos=151, y_pos=111),
        FormationMember(Chewy, x_pos=183, y_pos=151),
    ]
)
formations[FORM0177_TWO_CHEWY_ONE_SHYAWAY] = Formation(
    [
        FormationMember(Chewy, x_pos=135, y_pos=119),
        FormationMember(Chewy, x_pos=199, y_pos=151),
        FormationMember(Shyaway, x_pos=199, y_pos=119),
    ]
)
formations[FORM0178_CHEWY_SPINTHRA] = Formation(
    [
        FormationMember(Chewy, x_pos=151, y_pos=111),
        FormationMember(Spinthra, x_pos=215, y_pos=143),
    ]
)
formations[FORM0179_TWO_CHEWY_TWO_GECKIT_ONE_KRIFFID] = Formation(
    [
        FormationMember(Chewy, x_pos=183, y_pos=151),
        FormationMember(Chewy, x_pos=135, y_pos=127),
        FormationMember(Geckit, x_pos=231, y_pos=143),
        FormationMember(Geckit, x_pos=151, y_pos=103),
        FormationMember(Kriffid, x_pos=199, y_pos=119),
    ]
)
formations[FORM0180_GECKIT_SPINTHRA] = Formation(
    [
        FormationMember(Geckit, x_pos=199, y_pos=151),
        FormationMember(Spinthra, x_pos=151, y_pos=111),
    ]
)
formations[FORM0181_TWO_GECKIT_ONE_SPINTHRA] = Formation(
    [
        FormationMember(Geckit, x_pos=183, y_pos=135),
        FormationMember(Geckit, x_pos=215, y_pos=151),
        FormationMember(Spinthra, x_pos=151, y_pos=111),
    ]
)
formations[FORM0182_TWO_GECKIT_TWO_CHEWY_ONE_SHYAWAY] = Formation(
    [
        FormationMember(Geckit, x_pos=151, y_pos=127),
        FormationMember(Geckit, x_pos=183, y_pos=143),
        FormationMember(Chewy, x_pos=167, y_pos=103),
        FormationMember(Chewy, x_pos=231, y_pos=135),
        FormationMember(Shyaway, x_pos=199, y_pos=119),
    ]
)
formations[FORM0183_TWO_GECKIT_SPINTHRA_KRIFFID] = Formation(
    [
        FormationMember(Geckit, x_pos=151, y_pos=127),
        FormationMember(Geckit, x_pos=183, y_pos=143),
        FormationMember(Spinthra, x_pos=151, y_pos=103),
        FormationMember(Kriffid, x_pos=231, y_pos=143),
    ]
)
formations[FORM0184_BIRDY_HEAVYTROOPA] = Formation(
    [
        FormationMember(Birdy, x_pos=135, y_pos=119),
        FormationMember(HeavyTroopa, x_pos=215, y_pos=135),
    ]
)
formations[FORM0185_THREE_BIRDY] = Formation(
    [
        FormationMember(Birdy, x_pos=215, y_pos=119),
        FormationMember(Birdy, x_pos=151, y_pos=119),
        FormationMember(Birdy, x_pos=183, y_pos=151),
    ]
)
formations[FORM0186_TWO_BIRDY_ONE_HEAVYTROOPA] = Formation(
    [
        FormationMember(Birdy, x_pos=199, y_pos=151),
        FormationMember(Birdy, x_pos=135, y_pos=119),
        FormationMember(HeavyTroopa, x_pos=199, y_pos=119),
    ]
)
formations[FORM0187_FIVE_BIRDY] = Formation(
    [
        FormationMember(Birdy, x_pos=151, y_pos=111),
        FormationMember(Birdy, x_pos=215, y_pos=143),
        FormationMember(Birdy, x_pos=151, y_pos=143),
        FormationMember(Birdy, x_pos=215, y_pos=111),
        FormationMember(Birdy, x_pos=183, y_pos=127),
    ]
)
formations[FORM0188_TWO_BLUEBIRD] = Formation(
    [
        FormationMember(Bluebird, x_pos=199, y_pos=151),
        FormationMember(Bluebird, x_pos=151, y_pos=111),
    ]
)
formations[FORM0189_TWO_BLUEBIRD_ONE_HEAVYTROOPA] = Formation(
    [
        FormationMember(Bluebird, x_pos=167, y_pos=103),
        FormationMember(Bluebird, x_pos=231, y_pos=135),
        FormationMember(HeavyTroopa, x_pos=167, y_pos=135),
    ]
)
formations[FORM0190_FOUR_BLUEBIRD] = Formation(
    [
        FormationMember(Bluebird, x_pos=183, y_pos=143),
        FormationMember(Bluebird, x_pos=183, y_pos=111),
        FormationMember(Bluebird, x_pos=231, y_pos=135),
        FormationMember(Bluebird, x_pos=135, y_pos=119),
    ]
)
formations[FORM0191_TWO_BLUEBIRD_ONE_HEAVYTROOPA_2] = Formation(
    [
        FormationMember(Bluebird, x_pos=151, y_pos=111),
        FormationMember(Bluebird, x_pos=215, y_pos=143),
        None,
        None,
        FormationMember(HeavyTroopa, x_pos=183, y_pos=127),
    ]
)
formations[FORM0192_ONE_PINWHEEL] = Formation(
    [FormationMember(Pinwheel, x_pos=183, y_pos=127)]
)
formations[FORM0193_PINWHEEL_MUCKLE] = Formation(
    [
        FormationMember(Pinwheel, x_pos=135, y_pos=119),
        FormationMember(Muckle, x_pos=215, y_pos=143),
    ]
)
formations[FORM0194_TWO_PINWHEEL_TWO_MUCKLE] = Formation(
    [
        FormationMember(Pinwheel, x_pos=151, y_pos=127),
        FormationMember(Pinwheel, x_pos=183, y_pos=143),
        FormationMember(Muckle, x_pos=151, y_pos=103),
        FormationMember(Muckle, x_pos=231, y_pos=143),
    ]
)
formations[FORM0195_THREE_PINWHEEL_TWO_SLINGSHY] = Formation(
    [
        FormationMember(Pinwheel, x_pos=151, y_pos=143),
        FormationMember(Pinwheel, x_pos=135, y_pos=119),
        FormationMember(Pinwheel, x_pos=199, y_pos=151),
        FormationMember(SlingShy, x_pos=167, y_pos=111),
        FormationMember(SlingShy, x_pos=215, y_pos=135),
    ]
)
formations[FORM0196_TWO_SHAMAN] = Formation(
    [
        FormationMember(Shaman, x_pos=151, y_pos=111),
        FormationMember(Shaman, x_pos=199, y_pos=151),
    ]
)
formations[FORM0197_SHAMAN_ORBISON_JAWFUL] = Formation(
    [
        FormationMember(Shaman, x_pos=135, y_pos=119),
        FormationMember(Orbison, x_pos=199, y_pos=151),
        FormationMember(Jawful, x_pos=199, y_pos=119),
    ]
)
formations[FORM0198_TWO_SHAMAN_ONE_JAWFUL] = Formation(
    [
        FormationMember(Shaman, x_pos=167, y_pos=103),
        FormationMember(Shaman, x_pos=231, y_pos=135),
        FormationMember(Jawful, x_pos=167, y_pos=135),
    ]
)
formations[FORM0199_TWO_SHAMAN_TWO_SLINGSHY_JAWFUL] = Formation(
    [
        FormationMember(Shaman, x_pos=167, y_pos=103),
        FormationMember(Shaman, x_pos=231, y_pos=135),
        FormationMember(SlingShy, x_pos=135, y_pos=127),
        FormationMember(SlingShy, x_pos=183, y_pos=151),
        FormationMember(Jawful, x_pos=183, y_pos=127),
    ]
)
formations[FORM0200_SLINGSHY_ORBISON] = Formation(
    [
        FormationMember(SlingShy, x_pos=135, y_pos=119),
        FormationMember(Orbison, x_pos=215, y_pos=135),
    ]
)
formations[FORM0201_ONE_SLINGSHY_TWO_ORBISON] = Formation(
    [
        FormationMember(SlingShy, x_pos=183, y_pos=127),
        FormationMember(Orbison, x_pos=151, y_pos=111),
        FormationMember(Orbison, x_pos=215, y_pos=143),
    ]
)
formations[FORM0202_SLINGSHY_TWO_ORBISON_JAWFUL] = Formation(
    [
        FormationMember(SlingShy, x_pos=167, y_pos=135),
        FormationMember(Orbison, x_pos=151, y_pos=111),
        FormationMember(Orbison, x_pos=215, y_pos=143),
        FormationMember(Jawful, x_pos=199, y_pos=119),
    ]
)
formations[FORM0203_TWO_SLINGSHY_TWO_PINWHEEL_MUCKLE] = Formation(
    [
        FormationMember(SlingShy, x_pos=183, y_pos=143),
        FormationMember(SlingShy, x_pos=151, y_pos=127),
        FormationMember(Pinwheel, x_pos=151, y_pos=111),
        FormationMember(Pinwheel, x_pos=215, y_pos=143),
        FormationMember(Muckle, x_pos=199, y_pos=119),
    ]
)
formations[FORM0204_ONE_MAGMUS] = Formation(
    [FormationMember(Magmus, x_pos=183, y_pos=127)]
)
formations[FORM0205_TWO_MAGMUS_ONE_ARMOREDANT] = Formation(
    [
        FormationMember(Magmus, x_pos=151, y_pos=111),
        FormationMember(Magmus, x_pos=215, y_pos=143),
        FormationMember(ArmoredAnt, x_pos=183, y_pos=127),
    ]
)
formations[FORM0206_THREE_MAGMUS_TWO_OERLIKON] = Formation(
    [
        FormationMember(Magmus, x_pos=151, y_pos=103),
        FormationMember(Magmus, x_pos=231, y_pos=143),
        FormationMember(Magmus, x_pos=199, y_pos=119),
        FormationMember(Oerlikon, x_pos=151, y_pos=127),
        FormationMember(Oerlikon, x_pos=183, y_pos=143),
    ]
)
formations[FORM0207_TWO_MAGMUS_TWO_ARMOREDANT] = Formation(
    [
        FormationMember(Magmus, x_pos=119, y_pos=119),
        FormationMember(Magmus, x_pos=167, y_pos=143),
        FormationMember(ArmoredAnt, x_pos=167, y_pos=111),
        FormationMember(ArmoredAnt, x_pos=215, y_pos=135),
    ]
)
formations[FORM0208_OERLIKON_VOMER] = Formation(
    [
        FormationMember(Oerlikon, x_pos=135, y_pos=119),
        FormationMember(Vomer, x_pos=215, y_pos=135),
    ]
)
formations[FORM0209_THREE_OERLIKON] = Formation(
    [
        FormationMember(Oerlikon, x_pos=183, y_pos=127),
        FormationMember(Oerlikon, x_pos=135, y_pos=119),
        FormationMember(Oerlikon, x_pos=231, y_pos=135),
    ]
)
formations[FORM0210_OERLIKON_CHAINEDKONG_ARMOREDANT] = Formation(
    [
        FormationMember(Oerlikon, x_pos=215, y_pos=151),
        FormationMember(ChainedKong, x_pos=183, y_pos=127),
        FormationMember(ArmoredAnt, x_pos=135, y_pos=111),
    ]
)
formations[FORM0211_TWO_OERLIKON_ONE_CHAINEDKONG] = Formation(
    [
        FormationMember(Oerlikon, x_pos=135, y_pos=127),
        FormationMember(Oerlikon, x_pos=183, y_pos=151),
        FormationMember(ChainedKong, x_pos=199, y_pos=119),
    ]
)
formations[FORM0212_THREE_PYROSPHERE] = Formation(
    [
        FormationMember(Pyrosphere, x_pos=151, y_pos=135),
        FormationMember(Pyrosphere, x_pos=215, y_pos=135),
        FormationMember(Pyrosphere, x_pos=183, y_pos=103),
    ]
)
formations[FORM0213_TWO_PYROSPHERE_ONE_CHAINEDKONG] = Formation(
    [
        FormationMember(Pyrosphere, x_pos=199, y_pos=143),
        FormationMember(Pyrosphere, x_pos=151, y_pos=119),
        FormationMember(ChainedKong, x_pos=199, y_pos=119),
    ]
)
formations[FORM0214_CORKPEDITE_BODY_PYROSPHERE] = Formation(
    [
        FormationMember(Corkpedite, x_pos=135, y_pos=119),
        FormationMember(CorkpediteBody, x_pos=151, y_pos=111),
        FormationMember(Pyrosphere, x_pos=215, y_pos=143),
    ]
)
formations[FORM0215_TWO_PYROSPHERE_ONE_STUMPET] = Formation(
    [
        FormationMember(Pyrosphere, x_pos=199, y_pos=151),
        FormationMember(Pyrosphere, x_pos=199, y_pos=119),
        FormationMember(Stumpet, x_pos=151, y_pos=111),
    ]
)
formations[FORM0216_VOMER_CHAINEDKONG] = Formation(
    [
        FormationMember(Vomer, x_pos=151, y_pos=111),
        FormationMember(ChainedKong, x_pos=215, y_pos=143),
    ]
)
formations[FORM0217_THREE_VOMER] = Formation(
    [
        FormationMember(Vomer, x_pos=151, y_pos=103),
        FormationMember(Vomer, x_pos=183, y_pos=127),
        FormationMember(Vomer, x_pos=215, y_pos=151),
    ]
)
formations[FORM0218_CORKPEDITE_BODY_VOMER] = Formation(
    [
        FormationMember(Corkpedite, x_pos=199, y_pos=151),
        FormationMember(CorkpediteBody, x_pos=215, y_pos=143),
        FormationMember(Vomer, x_pos=135, y_pos=119),
    ]
)
formations[FORM0219_TWO_VOMER_ONE_STUMPET] = Formation(
    [
        FormationMember(Vomer, x_pos=151, y_pos=135),
        FormationMember(Vomer, x_pos=151, y_pos=103),
        FormationMember(Stumpet, x_pos=215, y_pos=143),
    ]
)
formations[FORM0220_ONE_TERRACOTTA] = Formation(
    [
        FormationMember(Terracotta, x_pos=183, y_pos=127),
    ]
)
formations[FORM0221_THREE_TERRACOTTA] = Formation(
    [
        FormationMember(Terracotta, x_pos=183, y_pos=151),
        FormationMember(Terracotta, x_pos=151, y_pos=119),
        FormationMember(Terracotta, x_pos=215, y_pos=119),
    ]
)
formations[FORM0222_ONE_TERRACOTTA_TWO_FORKIES] = Formation(
    [
        FormationMember(Terracotta, x_pos=183, y_pos=127),
        FormationMember(Forkies, x_pos=151, y_pos=111),
        FormationMember(Forkies, x_pos=215, y_pos=143),
    ]
)
formations[FORM0223_TWO_TERRACOTTA_TWO_GUGOOMBA_ONE_FORKIES] = Formation(
    [
        FormationMember(Terracotta, x_pos=135, y_pos=127),
        FormationMember(Terracotta, x_pos=183, y_pos=151),
        FormationMember(GuGoomba, x_pos=231, y_pos=135),
        FormationMember(GuGoomba, x_pos=167, y_pos=103),
        FormationMember(Forkies, x_pos=183, y_pos=127),
    ]
)
formations[FORM0224_MALAKOOPA_TUBOTROOPA] = Formation(
    [
        FormationMember(Malakoopa, x_pos=135, y_pos=127),
        FormationMember(TuboTroopa, x_pos=215, y_pos=143),
    ]
)
formations[FORM0225_TWO_MALAKOOPA_ONE_TUBOTROOPA] = Formation(
    [
        FormationMember(Malakoopa, x_pos=135, y_pos=119),
        FormationMember(Malakoopa, x_pos=199, y_pos=151),
        FormationMember(TuboTroopa, x_pos=199, y_pos=119),
    ]
)
formations[FORM0226_TWO_MALAKOOPA_TERRACOTTA_TUBOTROOPA] = Formation(
    [
        FormationMember(Malakoopa, x_pos=135, y_pos=103),
        FormationMember(Malakoopa, x_pos=231, y_pos=151),
        FormationMember(Terracotta, x_pos=167, y_pos=135),
        FormationMember(TuboTroopa, x_pos=199, y_pos=119),
    ]
)
formations[FORM0227_ONE_MALAKOOPA_TWO_TUBOTROOPA] = Formation(
    [
        FormationMember(Malakoopa, x_pos=183, y_pos=127),
        None,
        None,
        FormationMember(TuboTroopa, x_pos=135, y_pos=103),
        FormationMember(TuboTroopa, x_pos=231, y_pos=151),
    ]
)
formations[FORM0228_TWO_GUGOOMBA] = Formation(
    [
        FormationMember(GuGoomba, x_pos=151, y_pos=111),
        FormationMember(GuGoomba, x_pos=199, y_pos=151),
    ]
)
formations[FORM0229_TWO_GUGOOMBA_ONE_STARCRUSTER] = Formation(
    [
        FormationMember(GuGoomba, x_pos=231, y_pos=151),
        FormationMember(GuGoomba, x_pos=135, y_pos=103),
        FormationMember(Starcruster, x_pos=167, y_pos=135),
    ]
)
formations[FORM0230_GUGOOMBA_FORKIES_STARCRUSTER] = Formation(
    [
        FormationMember(GuGoomba, x_pos=231, y_pos=143),
        FormationMember(Forkies, x_pos=199, y_pos=119),
        FormationMember(Starcruster, x_pos=151, y_pos=103),
    ]
)
formations[FORM0231_TWO_GUGOOMBA_TWO_MALAKOOPA_TWO_TERRACOTTA] = Formation(
    [
        FormationMember(GuGoomba, x_pos=199, y_pos=151),
        FormationMember(GuGoomba, x_pos=135, y_pos=119),
        FormationMember(Malakoopa, x_pos=167, y_pos=135),
        FormationMember(Malakoopa, x_pos=199, y_pos=119),
        FormationMember(Terracotta, x_pos=167, y_pos=103),
        FormationMember(Terracotta, x_pos=231, y_pos=135),
    ]
)
formations[FORM0232_ONE_BIGBERTHA] = Formation(
    [
        FormationMember(BigBertha, x_pos=183, y_pos=127),
    ]
)
formations[FORM0233_TWO_BIGBERTHA] = Formation(
    [
        FormationMember(BigBertha, x_pos=151, y_pos=111),
        FormationMember(BigBertha, x_pos=215, y_pos=143),
    ]
)
formations[FORM0234_BIGBERTHA_FORKIES] = Formation(
    [
        FormationMember(BigBertha, x_pos=215, y_pos=143),
        FormationMember(Forkies, x_pos=151, y_pos=111),
    ]
)
formations[FORM0235_TWO_BIGBERTHA_ONE_TERRACOTTA] = Formation(
    [
        FormationMember(BigBertha, x_pos=135, y_pos=111),
        FormationMember(BigBertha, x_pos=215, y_pos=151),
        FormationMember(Terracotta, x_pos=183, y_pos=127),
    ]
)
formations[236] = None
formations[237] = None
formations[238] = None
formations[239] = None
formations[FORM0240_ONE_NINJA] = Formation(
    [
        FormationMember(Ninja, x_pos=183, y_pos=127),
    ]
)
formations[FORM0241_NINJA_DOPPEL] = Formation(
    [
        FormationMember(Ninja, x_pos=151, y_pos=119),
        FormationMember(Doppel, x_pos=199, y_pos=159),
    ]
)
formations[FORM0242_TWO_NINJA_ONE_HIPPOPO] = Formation(
    [
        FormationMember(Ninja, x_pos=199, y_pos=151),
        FormationMember(Ninja, x_pos=135, y_pos=119),
        FormationMember(Hippopo, x_pos=199, y_pos=119),
    ]
)
formations[FORM0243_FIVE_NINJA] = Formation(
    [
        FormationMember(Ninja, x_pos=135, y_pos=119),
        FormationMember(Ninja, x_pos=183, y_pos=127),
        FormationMember(Ninja, x_pos=167, y_pos=103),
        FormationMember(Ninja, x_pos=231, y_pos=135),
        FormationMember(Ninja, x_pos=199, y_pos=151),
    ]
)
formations[FORM0244_SPRINGER_GLUMREAPER] = Formation(
    [
        FormationMember(Springer, x_pos=215, y_pos=143),
        FormationMember(GlumReaper, x_pos=135, y_pos=119),
    ]
)
formations[245] = None
formations[FORM0246_TWO_SPRINGER_ONE_PUPPOX] = Formation(
    [
        FormationMember(Springer, x_pos=231, y_pos=135),
        FormationMember(Springer, x_pos=167, y_pos=103),
        FormationMember(Puppox, x_pos=167, y_pos=135),
    ]
)
formations[FORM0247_ONE_SPRINGER_TWO_PUPPOX] = Formation(
    [
        FormationMember(Springer, x_pos=183, y_pos=127),
        FormationMember(Puppox, x_pos=215, y_pos=143),
        FormationMember(Puppox, x_pos=151, y_pos=111),
    ]
)
formations[FORM0248_FIVE_AMEBOID] = Formation(
    [
        FormationMember(Ameboid, x_pos=183, y_pos=127),
        FormationMember(Ameboid, x_pos=167, y_pos=103, hidden_at_start=True),
        FormationMember(Ameboid, x_pos=135, y_pos=119, hidden_at_start=True),
        FormationMember(Ameboid, x_pos=231, y_pos=135, hidden_at_start=True),
        FormationMember(Ameboid, x_pos=199, y_pos=151, hidden_at_start=True),
    ]
)
formations[249] = None
formations[250] = None
formations[251] = None
formations[FORM0252_THREE_GLUMREAPER] = Formation(
    [
        FormationMember(GlumReaper, x_pos=183, y_pos=127),
        FormationMember(GlumReaper, x_pos=135, y_pos=119),
        FormationMember(GlumReaper, x_pos=231, y_pos=135),
    ]
)
formations[FORM0253_GLUMREAPER_HIPPOPO] = Formation(
    [
        FormationMember(GlumReaper, x_pos=215, y_pos=159),
        FormationMember(Hippopo, x_pos=151, y_pos=111),
    ]
)
formations[FORM0254_TWO_GLUMREAPER_TWO_DOPPEL] = Formation(
    [
        FormationMember(GlumReaper, x_pos=151, y_pos=127),
        FormationMember(GlumReaper, x_pos=183, y_pos=143),
        FormationMember(Doppel, x_pos=167, y_pos=103),
        FormationMember(Doppel, x_pos=231, y_pos=135),
    ]
)
formations[FORM0255_TWO_GLUMREAPER_TWO_LILBOO] = Formation(
    [
        FormationMember(GlumReaper, x_pos=135, y_pos=111),
        FormationMember(GlumReaper, x_pos=215, y_pos=151),
        FormationMember(LilBoo, x_pos=167, y_pos=135),
        FormationMember(LilBoo, x_pos=199, y_pos=119),
    ]
)
formations[FORM0256_ONE_LILBOO] = Formation(
    [
        FormationMember(LilBoo, x_pos=183, y_pos=127),
    ]
)
formations[FORM0257_TWO_LILBOO_ONE_HIPPOPO] = Formation(
    [
        FormationMember(LilBoo, x_pos=183, y_pos=151),
        FormationMember(LilBoo, x_pos=215, y_pos=135),
        FormationMember(Hippopo, x_pos=151, y_pos=111),
    ]
)
formations[FORM0258_TWO_LILBOO_PUPPOX_DOPPEL] = Formation(
    [
        FormationMember(LilBoo, x_pos=167, y_pos=143),
        FormationMember(LilBoo, x_pos=199, y_pos=119),
        FormationMember(Puppox, x_pos=151, y_pos=103),
        FormationMember(Doppel, x_pos=215, y_pos=159),
    ]
)
formations[FORM0259_FOUR_LILBOO] = Formation(
    [
        FormationMember(LilBoo, x_pos=167, y_pos=135),
        FormationMember(LilBoo, x_pos=151, y_pos=111),
        FormationMember(LilBoo, x_pos=215, y_pos=143),
        FormationMember(LilBoo, x_pos=199, y_pos=119),
    ]
)
formations[FORM0260_TWO_MADMALLET] = Formation(
    [
        FormationMember(MadMallet, x_pos=151, y_pos=119),
        FormationMember(MadMallet, x_pos=215, y_pos=143),
    ]
)
formations[FORM0261_THREE_MADMALLET] = Formation(
    [
        FormationMember(MadMallet, x_pos=151, y_pos=127),
        FormationMember(MadMallet, x_pos=199, y_pos=151),
        FormationMember(MadMallet, x_pos=199, y_pos=119),
    ]
)
formations[FORM0262_FIVE_MADMALLET] = Formation(
    [
        FormationMember(MadMallet, x_pos=183, y_pos=127),
        FormationMember(MadMallet, x_pos=135, y_pos=127),
        FormationMember(MadMallet, x_pos=231, y_pos=135),
        FormationMember(MadMallet, x_pos=167, y_pos=103),
        FormationMember(MadMallet, x_pos=183, y_pos=151),
    ]
)
formations[FORM0263_THREE_MADMALLET_HENCHMEN] = Formation(
    [
        FormationMember(MadMalletHenchman, x_pos=151, y_pos=127),
        FormationMember(MadMalletHenchman, x_pos=199, y_pos=151),
        FormationMember(MadMalletHenchman, x_pos=199, y_pos=119),
    ]
)
formations[FORM0264_ONE_POUNDER] = Formation(
    [
        FormationMember(PounderHenchman, x_pos=183, y_pos=127),
    ]
)
formations[FORM0265_THREE_POUNDER] = Formation(
    [
        FormationMember(PounderHenchman, x_pos=183, y_pos=127),
        FormationMember(PounderHenchman, x_pos=231, y_pos=135),
        FormationMember(PounderHenchman, x_pos=167, y_pos=103),
    ]
)
formations[FORM0266_FIVE_POUNDER] = Formation(
    [
        FormationMember(PounderHenchman, x_pos=167, y_pos=135),
        FormationMember(PounderHenchman, x_pos=199, y_pos=143),
        FormationMember(PounderHenchman, x_pos=151, y_pos=119),
        FormationMember(PounderHenchman, x_pos=167, y_pos=103),
        FormationMember(PounderHenchman, x_pos=231, y_pos=135),
    ]
)
formations[267] = None
formations[FORM0268_PANDORITE_BOSS_FIGHT] = Formation(
    [
        FormationMember(Pandorite, x_pos=183, y_pos=127),
    ],
    can_run_away=False,
)
formations[FORM0269_HIDON_BOSS_FIGHT] = Formation(
    [
        FormationMember(Hidon, x_pos=167, y_pos=119),
        FormationMember(
            Goombette,
            x_pos=135,
            y_pos=111,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
        FormationMember(
            Goombette,
            x_pos=135,
            y_pos=135,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
        FormationMember(
            Goombette,
            x_pos=167,
            y_pos=151,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
        FormationMember(
            Goombette,
            x_pos=215,
            y_pos=151,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
    ],
    can_run_away=False,
)
formations[FORM0270_BOXBOY_BOSS_FIGHT] = Formation(
    [
        FormationMember(BoxBoy, x_pos=183, y_pos=127),
        FormationMember(
            Fautso,
            x_pos=151,
            y_pos=111,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
    ],
    can_run_away=False,
)
formations[FORM0271_CHESTER_BOSS_FIGHT] = Formation(
    [
        FormationMember(Chester, x_pos=183, y_pos=127),
        FormationMember(
            BahamuttChester,
            x_pos=135,
            y_pos=119,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
    ],
    can_run_away=False,
)
formations[FORM0272_TWO_BLUEBIRD_HENCHMEN] = Formation(
    [
        FormationMember(BluebirdHenchman, x_pos=199, y_pos=151),
        FormationMember(BluebirdHenchman, x_pos=151, y_pos=111),
    ]
)
formations[273] = None
formations[FORM0274_BOOSTER_BOSS_FIGHT] = Formation(
    [
        FormationMember(Booster, x_pos=183, y_pos=127),
        FormationMember(SnifitHenchman, x_pos=135, y_pos=119),
        FormationMember(SnifitHenchman, x_pos=151, y_pos=143),
        FormationMember(SnifitHenchman, x_pos=199, y_pos=151),
    ],
    run_event_at_load=BE0012_DIALOGUE_FROM_BOOSTER_FIGHT,
    music=BattleMusic.BOSS_1,
    can_run_away=False,
    additional_enemies_to_scale=[ApprenticeHenchman],
)
formations[FORM0275_BOOSTER_DUMMY] = Formation(
    [
        FormationMember(Booster2, 183, 127),
    ],
    music=BattleMusic.BOSS_1,
    can_run_away=False,
)
formations[FORM0276_SNIFIT_HENCHMAN] = Formation(
    [
        FormationMember(SnifitHenchman, x_pos=183, y_pos=127),
    ],
    can_run_away=False,
)
formations[FORM0277_CROCO1_BOSS_FIGHT] = Formation(
    [
        FormationMember(Croco1, x_pos=183, y_pos=127),
    ],
    music=BattleMusic.BOSS_1,
    can_run_away=False,
)
formations[FORM0278_CROCO2_BOSS_FIGHT] = Formation(
    [
        FormationMember(Croco2, x_pos=183, y_pos=127),
    ],
    run_event_at_load=BE0014_SET_7EE00A_TO_PARTY_SIZE_AT_START_OF_FIGHT,
    music=BattleMusic.BOSS_1,
    can_run_away=False,
    additional_enemies_to_scale=[CrookHenchman],
)
formations[FORM0279_FOUR_BLUEBIRD_HENCHMEN] = Formation(
    [
        FormationMember(BluebirdHenchman, x_pos=183, y_pos=143),
        FormationMember(BluebirdHenchman, x_pos=183, y_pos=111),
        FormationMember(BluebirdHenchman, x_pos=231, y_pos=135),
        FormationMember(BluebirdHenchman, x_pos=135, y_pos=119),
    ],
)
formations[FORM0280_JOHNNY_BOSS_FIGHT] = JohnnyBossFormation(
    [
        FormationMember(Johnny, x_pos=183, y_pos=127),
        FormationMember(BandanaBlue, x_pos=135, y_pos=111),
        FormationMember(BandanaBlue, x_pos=135, y_pos=135),
        FormationMember(BandanaBlue, x_pos=183, y_pos=159),
        FormationMember(BandanaBlue, x_pos=215, y_pos=151),
        # Water Crystals inserted because they use an empty sprite such as to not screw up vram
        # Johnny's 1v1 event will animate these two objects
        # since they get replaced with a Bandana Blue sprite anyway.
        # This prevents the game from crashing when you use Sheep Attack on the Bandana Blues,
        # thus preventing the game from trying to animate an object that no longer exists
        FormationMember(
            EmptyEnemy,
            x_pos=91,
            y_pos=111,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
        FormationMember(
            EmptyEnemy,
            x_pos=215,
            y_pos=181,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
    ],
    music=BattleMusic.BOSS_1,
    can_run_away=False,
    additional_enemies_to_scale=[JohnnySolo, BandanaRedHenchman],
)
formations[281] = None
formations[282] = None
formations[283] = None
formations[284] = None
formations[FORM0285_KING_CALAMARI_BOSS_FIGHT] = KingCalamariBossFormation(
    [
        FormationMember(KingCalamari, x_pos=222, y_pos=94),
        FormationMember(TentaclesLeft, x_pos=136, y_pos=115),
        FormationMember(TentaclesLeft, x_pos=112, y_pos=127),
        FormationMember(TentaclesRight, x_pos=193, y_pos=143),
        FormationMember(TentaclesRight, x_pos=168, y_pos=156),
        FormationMember(TentaclesRight, x_pos=135, y_pos=143),
    ],
    run_event_at_load=BE0026_INTRO_SCENE_TENTACLES_RISE_FROM_HOLES,
    music=BattleMusic.BOSS_1,
    battlefield_override=Battlefields.KING_CALAMARI,
    can_run_away=False,
    additional_enemies_to_scale=[BlooberHenchman],
    additional_enemies_for_stat_count=[TentaclesLeft, TentaclesLeft, TentaclesRight],
)
formations[FORM0286_BELOME_1_BOSS_FIGHT] = Formation(
    [
        FormationMember(Belome1, x_pos=183, y_pos=127),
    ],
    music=BattleMusic.BOSS_1,
    can_run_away=False,
)
formations[FORM0287_BELOME_2_BOSS_FIGHT] = Belome2BossFormation(
    [
        FormationMember(Belome2, x_pos=183, y_pos=127),
        FormationMember(
            MarioClone,
            x_pos=135,
            y_pos=119,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
        FormationMember(
            PeachClone,
            x_pos=215,
            y_pos=159,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
    ],
    music=BattleMusic.BOSS_1,
    can_run_away=False,
    additional_enemies_to_scale=[MallowClone, GenoClone, BowserClone],
)
formations[288] = None
formations[FORM0289_VALENTINA_BOSS_FIGHT] = ValentinaBossFormation(
    [
        FormationMember(Valentina, x_pos=183, y_pos=127),
        FormationMember(Dodo, x_pos=199, y_pos=151),
    ],
    run_event_at_load=BE0014_SET_7EE00A_TO_PARTY_SIZE_AT_START_OF_FIGHT,
    music=BattleMusic.BOSS_1,
    can_run_away=False,
    additional_enemies_to_scale=[BirdyHenchman, BluebirdHenchman],
)
formations[290] = None
formations[291] = None
formations[292] = None
formations[FORM0293_CZAR_DRAGON_BOSS_FIGHT] = Formation(
    [
        FormationMember(CzarDragon, x_pos=183, y_pos=143),
        FormationMember(Zombone, x_pos=183, y_pos=143, hidden_at_start=True),
        FormationMember(
            Helio,
            x_pos=167,
            y_pos=119,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
        FormationMember(
            Helio,
            x_pos=135,
            y_pos=135,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
        FormationMember(
            Helio,
            x_pos=199,
            y_pos=167,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
        FormationMember(
            Helio,
            x_pos=231,
            y_pos=151,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
    ],
    music=BattleMusic.BOSS_1,
    can_run_away=False,
    additional_enemies_to_scale=[PyrosphereHenchman],
)
formations[FORM0294_MEGASMILAX_BOSS_FIGHT] = MegasmilaxBossFormation(
    [
        FormationMember(Smilax, x_pos=180, y_pos=157),
        FormationMember(Smilax, x_pos=164, y_pos=175, hidden_at_start=True),
        FormationMember(Smilax, x_pos=143, y_pos=119, hidden_at_start=True),
        FormationMember(Smilax, x_pos=207, y_pos=151, hidden_at_start=True),
        FormationMember(Smilax, x_pos=191, y_pos=127, hidden_at_start=True),
        FormationMember(Megasmilax, x_pos=175, y_pos=111, hidden_at_start=True),
    ],
    run_event_at_load=BE0058_THRAX_IS_THERE,
    music=BattleMusic.BOSS_1,
    can_run_away=False,
    additional_enemies_to_scale=[PiranhaPlantHenchman],
    additional_enemies_for_stat_count=[Smilax, Smilax, Smilax],
)
formations[FORM0295_COUNTDOWN_BOSS_FIGHT] = Formation(
    [
        FormationMember(CountDown, x_pos=150, y_pos=93),
        FormationMember(DingALing, x_pos=158, y_pos=52),
        FormationMember(DingALing, x_pos=194, y_pos=67),
    ],
    run_event_at_load=BE0014_SET_7EE00A_TO_PARTY_SIZE_AT_START_OF_FIGHT,
    battlefield_override=Battlefields.COUNTDOWN,
    music=BattleMusic.BOSS_1,
    can_run_away=False,
)
formations[296] = None
formations[FORM0297_BIRDETTA_BOSS_FIGHT] = Formation(
    [
        FormationMember(Birdetta, x_pos=167, y_pos=118, hidden_at_start=True),
        FormationMember(Shelly, x_pos=171, y_pos=103, include_in_stat_totaling=False),
        FormationMember(
            Eggbert,
            x_pos=135,
            y_pos=119,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
        FormationMember(
            Eggbert,
            x_pos=135,
            y_pos=135,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
        FormationMember(
            Eggbert,
            x_pos=167,
            y_pos=151,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
        FormationMember(
            Eggbert,
            x_pos=199,
            y_pos=151,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
    ],
    battlefield_override=Battlefields.BIRDETTA,
    music=BattleMusic.BOSS_1,
    can_run_away=False,
)
formations[FORM0298_BUNDT_BOSS_FIGHT] = Formation(
    [
        FormationMember(Bundt, x_pos=199, y_pos=127),
        FormationMember(Raspberry, x_pos=199, y_pos=119),
        FormationMember(Torte, x_pos=199, y_pos=151, include_in_stat_totaling=False),
        FormationMember(Torte, x_pos=135, y_pos=119, include_in_stat_totaling=False),
    ],
    run_event_at_load=BE0014_SET_7EE00A_TO_PARTY_SIZE_AT_START_OF_FIGHT,
    music=BattleMusic.BOSS_1,
    can_run_away=False,
)
formations[FORM0299_KGGG_BOSS_FIGHT] = Formation(
    [
        FormationMember(KnifeGuy, x_pos=151, y_pos=119),
        FormationMember(GrateGuy, x_pos=199, y_pos=143),
    ],
    music=BattleMusic.BOSS_1,
    can_run_away=False,
)
formations[FORM0300_HELIO_HENCHMEN] = Formation(
    [
        FormationMember(Helio, x_pos=167, y_pos=119),
        FormationMember(Helio, x_pos=135, y_pos=135),
        FormationMember(Helio, x_pos=199, y_pos=167),
        FormationMember(Helio, x_pos=231, y_pos=151),
    ]
)
formations[FORM0301_JINX_1_BOSS_FIGHT] = Formation(
    [
        FormationMember(Jinx1, x_pos=183, y_pos=127),
    ],
    run_event_at_load=BE0071_JINX_USES_TRIPLE_KICK,
    music=BattleMusic.BOSS_1,
)
formations[FORM0302_MACK_BOSS_FIGHT] = Formation(
    [
        FormationMember(Mack, x_pos=199, y_pos=119),
        FormationMember(Bodyguard, x_pos=135, y_pos=111),
        FormationMember(Bodyguard, x_pos=151, y_pos=127),
        FormationMember(Bodyguard, x_pos=183, y_pos=143),
        FormationMember(Bodyguard, x_pos=215, y_pos=151),
    ],
    music=BattleMusic.BOSS_2,
    can_run_away=False,
)
formations[FORM0303_YARIDOVICH_BOSS_FIGHT] = Formation(
    [
        FormationMember(Yaridovich, x_pos=183, y_pos=127),
        FormationMember(
            YaridovichMirage,
            x_pos=183,
            y_pos=127,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
    ],
    music=BattleMusic.BOSS_2,
    can_run_away=False,
    additional_enemies_to_scale=[YaridovichDrillBit],
)
formations[FORM0304_AXEM_BOSS_FIGHT] = AxemBossFormation(
    [
        FormationMember(AxemRangers, x_pos=201, y_pos=79),
        FormationMember(AxemRed, x_pos=135, y_pos=111, hidden_at_start=True),
        FormationMember(AxemBlack, x_pos=135, y_pos=127, hidden_at_start=True),
        FormationMember(AxemPink, x_pos=151, y_pos=143, hidden_at_start=True),
        FormationMember(AxemGreen, x_pos=183, y_pos=151, hidden_at_start=True),
        FormationMember(AxemYellow, x_pos=215, y_pos=151, hidden_at_start=True),
    ],
    run_event_at_load=BE0061_ONLY_MARIO_IS_THERE,
    battlefield_override=Battlefields.AXEM_RANGERS,
    music=BattleMusic.BOSS_2,
    can_run_away=False,
    additional_enemies_to_scale=[
        MachineMadeAxemBlackHenchman,
        MachineMadeAxemGreenHenchman,
        MachineMadeAxemPinkHenchman,
        MachineMadeAxemRedHenchman,
        MachineMadeAxemYellowHenchman,
    ],
)
formations[FORM0305_BOWYER_BOSS_FIGHT] = Formation(
    [
        FormationMember(Bowyer, x_pos=183, y_pos=127),
    ],
    run_event_at_load=BE0014_SET_7EE00A_TO_PARTY_SIZE_AT_START_OF_FIGHT,
    music=BattleMusic.BOSS_2,
    can_run_away=False,
    additional_enemies_to_scale=[AeroBowyer],
)
formations[306] = None
formations[FORM0307_EXOR_BOSS_FIGHT] = ExorBossFormation(
    [
        FormationMember(Exor, x_pos=193, y_pos=64),
        FormationMember(Neosquid, x_pos=187, y_pos=136),
        FormationMember(RightEye, x_pos=174, y_pos=145, hidden_at_start=True),
        FormationMember(LeftEye, x_pos=203, y_pos=157, hidden_at_start=True),
    ],
    run_event_at_load=BE0080_EXOR_FIGHT_BEGINS,
    battlefield_override=Battlefields.EXOR,
    music=BattleMusic.BOSS_2,
    can_run_away=False,
)
formations[FORM0308_SMITHY_1_BOSS_FIGHT] = Formation(
    [
        FormationMember(Smithy1, x_pos=199, y_pos=127),
        FormationMember(Smelter, x_pos=87, y_pos=87, include_in_stat_totaling=False),
        FormationMember(
            MachineMadeShysterHenchman,
            x_pos=135,
            y_pos=127,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
        FormationMember(
            MachineMadeShysterHenchman,
            x_pos=199,
            y_pos=159,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
        FormationMember(Smithy2Head, x_pos=199, y_pos=127, hidden_at_start=True),
    ],
    run_event_at_load=BE0014_SET_7EE00A_TO_PARTY_SIZE_AT_START_OF_FIGHT,
    battlefield_override=Battlefields.SMITHY,
    music=BattleMusic.SMITHY,
    can_run_away=False,
    additional_enemies_to_scale=[
        AeroSmithy,
        DrillBit,
        Smithy2Body,
        Smithy2TankHead,
        Smithy2ChestHead,
        Smithy2SafeHead,
        Smithy2MageHead,
    ],
)
formations[FORM0309_CLOAKER_DOMINO_FIGHT] = CloakerDominoFormation(
    [
        FormationMember(Cloaker, x_pos=151, y_pos=111),
        FormationMember(Domino, x_pos=215, y_pos=159),
        FormationMember(MadAdder, x_pos=167, y_pos=135, hidden_at_start=True),
    ],
    run_event_at_load=BE0052_INTRO_SCENE_DOMINO_CLOAKER_S_INTRODUCTION,
    battlefield_override=Battlefields.CLOAKER_DOMINO,
    music=BattleMusic.BOSS_1,
    can_run_away=False,
    additional_enemies_for_stat_count=[Earthlink],
    additional_enemies_to_scale=[Cloaker2, Domino2],
)
formations[FORM0310_THREE_RATFUNK] = Formation(
    [
        FormationMember(Ratfunk, x_pos=135, y_pos=119),
        FormationMember(Ratfunk, x_pos=199, y_pos=151),
        FormationMember(Ratfunk, x_pos=199, y_pos=119),
    ]
)
formations[FORM0311_FIVE_RATFUNK] = Formation(
    [
        FormationMember(Ratfunk, x_pos=135, y_pos=127),
        FormationMember(Ratfunk, x_pos=167, y_pos=103),
        FormationMember(Ratfunk, x_pos=183, y_pos=151),
        FormationMember(Ratfunk, x_pos=231, y_pos=135),
        FormationMember(Ratfunk, x_pos=183, y_pos=127),
    ]
)
formations[FORM0312_ONE_ARTICHOKER] = Formation(
    [
        FormationMember(Artichoker, x_pos=183, y_pos=127),
    ],
    can_run_away=False,
)
formations[FORM0313_TWO_ARTICHOKERS] = Formation(
    [
        FormationMember(Artichoker, x_pos=151, y_pos=119),
        FormationMember(Artichoker, x_pos=215, y_pos=143),
    ],
    can_run_away=False,
)
formations[FORM0314_PUNCHINELLO_BOSS_FIGHT] = Formation(
    [
        FormationMember(Punchinello, x_pos=199, y_pos=119),
        FormationMember(
            Microbomb,
            x_pos=135,
            y_pos=119,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
        FormationMember(
            Microbomb,
            x_pos=151,
            y_pos=135,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
        FormationMember(
            Microbomb,
            x_pos=183,
            y_pos=151,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
        FormationMember(
            Microbomb,
            x_pos=215,
            y_pos=159,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
    ],
    music=BattleMusic.BOSS_1,
    can_run_away=False,
    additional_enemies_to_scale=[BobombHenchman, MezzoBomb],
)
formations[FORM0315_HAMMERBRO_BOSS_FIGHT] = Formation(
    [
        FormationMember(HammerBro, x_pos=135, y_pos=127),
        FormationMember(HammerBro, x_pos=199, y_pos=143),
    ],
    music=BattleMusic.BOSS_1,
    can_run_away=False,
)
formations[FORM0316_THREE_CROOK_HENCHMEN] = Formation(
    [
        FormationMember(CrookHenchman, x_pos=135, y_pos=119),
        FormationMember(CrookHenchman, x_pos=199, y_pos=119),
        FormationMember(CrookHenchman, x_pos=199, y_pos=151),
    ]
)
formations[FORM0317_FIVE_CROOK_HENCHMEN] = Formation(
    [
        FormationMember(CrookHenchman, x_pos=167, y_pos=103),
        FormationMember(CrookHenchman, x_pos=135, y_pos=119),
        FormationMember(CrookHenchman, x_pos=183, y_pos=127),
        FormationMember(CrookHenchman, x_pos=199, y_pos=151),
        FormationMember(CrookHenchman, x_pos=231, y_pos=135),
    ]
)
formations[FORM0318_ONE_SNIFIT] = Formation(
    [
        FormationMember(Snifit, x_pos=167, y_pos=135),
    ],
    can_run_away=False,
)
formations[FORM0319_ONE_STUMPET_TWO_MAGMUS] = Formation(
    [
        FormationMember(Stumpet, x_pos=183, y_pos=127),
        FormationMember(Magmus, x_pos=119, y_pos=127),
        FormationMember(Magmus, x_pos=183, y_pos=159),
    ],
    can_run_away=False,
)
formations[FORM0320_ONE_POUNDETTE] = Formation(
    [
        FormationMember(PoundetteHenchman, x_pos=183, y_pos=127),
    ]
)
formations[FORM0321_THREE_POUNDETTES] = Formation(
    [
        FormationMember(PoundetteHenchman, x_pos=183, y_pos=127),
        FormationMember(PoundetteHenchman, x_pos=151, y_pos=111),
        FormationMember(PoundetteHenchman, x_pos=215, y_pos=143),
    ]
)
formations[FORM0322_SIX_POUNDETTES] = Formation(
    [
        FormationMember(PoundetteHenchman, x_pos=167, y_pos=135),
        FormationMember(PoundetteHenchman, x_pos=199, y_pos=119),
        FormationMember(PoundetteHenchman, x_pos=135, y_pos=119),
        FormationMember(PoundetteHenchman, x_pos=167, y_pos=103),
        FormationMember(PoundetteHenchman, x_pos=199, y_pos=151),
        FormationMember(PoundetteHenchman, x_pos=231, y_pos=135),
    ]
)
formations[323] = None
formations[FORM0325_JABIT_MADMALLET] = Formation(
    [
        FormationMember(Jabit, x_pos=215, y_pos=135),
        FormationMember(MadMallet, x_pos=151, y_pos=119),
    ]
)
formations[FORM0325_JABIT_POUNDER_POUNDETTE] = Formation(
    [
        FormationMember(Jabit, x_pos=151, y_pos=143),
        FormationMember(Pounder, x_pos=151, y_pos=111),
        FormationMember(Poundette, x_pos=215, y_pos=143),
    ]
)
formations[FORM0326_SIX_JABIT] = Formation(
    [
        FormationMember(Jabit, x_pos=135, y_pos=119),
        FormationMember(Jabit, x_pos=167, y_pos=135),
        FormationMember(Jabit, x_pos=231, y_pos=135),
        FormationMember(Jabit, x_pos=167, y_pos=103),
        FormationMember(Jabit, x_pos=199, y_pos=119),
        FormationMember(Jabit, x_pos=199, y_pos=151),
    ]
)
formations[FORM0327_JABITS_MADMALLETS_POUNDETTES] = Formation(
    [
        FormationMember(Jabit, x_pos=151, y_pos=127),
        FormationMember(Jabit, x_pos=183, y_pos=143),
        FormationMember(MadMallet, x_pos=135, y_pos=103),
        FormationMember(MadMallet, x_pos=183, y_pos=111),
        FormationMember(Poundette, x_pos=215, y_pos=127),
        FormationMember(Poundette, x_pos=231, y_pos=151),
    ]
)
formations[FORM0328_TWO_FIREBALL] = Formation(
    [
        FormationMember(Fireball, x_pos=151, y_pos=111),
        FormationMember(Fireball, x_pos=199, y_pos=151),
    ],
    can_run_away=False,
)
formations[FORM0329_THREE_FIREBALL] = Formation(
    [
        FormationMember(Fireball, x_pos=167, y_pos=135),
        FormationMember(Fireball, x_pos=167, y_pos=111),
        FormationMember(Fireball, x_pos=215, y_pos=135),
    ],
    can_run_away=False,
)
formations[FORM0330_ONE_STUMPET_THREE_MAGMUS] = Formation(
    [
        FormationMember(Stumpet, x_pos=151, y_pos=111),
        FormationMember(Magmus, x_pos=183, y_pos=159),
        FormationMember(Magmus, x_pos=199, y_pos=135),
        FormationMember(Magmus, x_pos=231, y_pos=159),
    ],
)
formations[FORM0331_CORKPEDITE_OERLIKON] = Formation(
    [
        FormationMember(Corkpedite, x_pos=151, y_pos=111),
        FormationMember(CorkpediteBody, x_pos=167, y_pos=103),
        FormationMember(Oerlikon, x_pos=199, y_pos=151),
    ]
)
formations[FORM0332_CORKPEDITE_TWO_OERLIKONS] = Formation(
    [
        FormationMember(Corkpedite, x_pos=151, y_pos=111),
        FormationMember(CorkpediteBody, x_pos=167, y_pos=103),
        FormationMember(Oerlikon, x_pos=183, y_pos=159),
        FormationMember(Oerlikon, x_pos=215, y_pos=143),
    ]
)
formations[FORM0333_JINX_2_BOSS_FIGHT] = Formation(
    [
        FormationMember(Jinx2, x_pos=183, y_pos=127),
    ],
    run_event_at_load=BE0072_JINX_USES_QUICKSILVER,
    music=BattleMusic.BOSS_1,
)
formations[FORM0334_JINX_3_BOSS_FIGHT] = Formation(
    [
        FormationMember(Jinx3, x_pos=183, y_pos=127),
    ],
    run_event_at_load=BE0073_JINX_USES_BOMBS_AWAY,
    music=BattleMusic.BOSS_1,
)
formations[FORM0335_JAGGER_BOSS_FIGHT] = Formation(
    [
        FormationMember(Jagger, x_pos=183, y_pos=127),
    ],
)
formations[336] = None
formations[337] = None
formations[338] = None
formations[339] = None
formations[340] = None
formations[341] = None
formations[342] = None
formations[343] = None
formations[344] = None
formations[FORM0345_FIVE_BIRDY_HENCHMEN] = Formation(
    [
        FormationMember(BirdyHenchman, x_pos=151, y_pos=111),
        FormationMember(BirdyHenchman, x_pos=215, y_pos=143),
        FormationMember(BirdyHenchman, x_pos=151, y_pos=143),
        FormationMember(BirdyHenchman, x_pos=215, y_pos=111),
        FormationMember(BirdyHenchman, x_pos=183, y_pos=127),
    ],
)
formations[FORM0346_THREE_AXEM_HENCHMEN] = Formation(
    [
        FormationMember(MachineMadeAxemPinkHenchman, x_pos=151, y_pos=111),
        None,
        FormationMember(MachineMadeAxemRedHenchman, x_pos=151, y_pos=143),
        None,
        FormationMember(MachineMadeAxemGreenHenchman, x_pos=215, y_pos=143),
    ],
    music=BattleMusic.BOSS_2,
)
formations[FORM0347_FOUR_AXEM_HENCHMEN] = Formation(
    [
        FormationMember(MachineMadeAxemBlackHenchman, x_pos=151, y_pos=119),
        FormationMember(MachineMadeAxemBlackHenchman, x_pos=231, y_pos=127),
        FormationMember(MachineMadeAxemYellowHenchman, x_pos=199, y_pos=143),
        FormationMember(MachineMadeAxemYellowHenchman, x_pos=183, y_pos=103),
    ],
    music=BattleMusic.BOSS_2,
)
formations[FORM0348_THREE_BLOOBER_HENCHMEN] = Formation(
    [
        FormationMember(BlooberHenchman, x_pos=183, y_pos=127),
        FormationMember(BlooberHenchman, x_pos=231, y_pos=143),
        FormationMember(BlooberHenchman, x_pos=135, y_pos=111),
    ],
)
formations[FORM0349_TWO_BOWYER_AEROS] = Formation(
    [
        FormationMember(AeroBowyer, x_pos=167, y_pos=119),
        FormationMember(AeroBowyer, x_pos=199, y_pos=135),
    ],
)
formations[FORM0350_CULEX_BOSS_FIGHT] = CulexBossFormation(
    [
        FormationMember(Culex, x_pos=183, y_pos=103),
        FormationMember(
            FireCrystal,
            x_pos=135,
            y_pos=103,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
        FormationMember(
            WaterCrystal,
            x_pos=151,
            y_pos=119,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
        FormationMember(
            EarthCrystal,
            x_pos=183,
            y_pos=135,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
        FormationMember(
            WindCrystal,
            x_pos=215,
            y_pos=143,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
    ],
    can_run_away=False,
    music=BattleMusic.CULEX,
)
formations[FORM0351_MOKURA_BOSS_FIGHT] = Formation(
    [
        FormationMember(Formless, x_pos=167, y_pos=135, include_in_stat_totaling=False),
        FormationMember(Mokura, x_pos=167, y_pos=135, hidden_at_start=True),
    ],
    can_run_away=False,
    music=BattleMusic.BOSS_1,
)
formations[FORM0352_THREE_PYROSPHERE_HENCHMEN] = Formation(
    [
        FormationMember(PyrosphereHenchman, x_pos=151, y_pos=135),
        FormationMember(PyrosphereHenchman, x_pos=215, y_pos=135),
        FormationMember(PyrosphereHenchman, x_pos=183, y_pos=103),
    ],
)
formations[FORM0353_ONE_FIRE_CRYSTAL] = Formation(
    [
        FormationMember(FireCrystal, x_pos=183, y_pos=127),
    ],
    run_event_at_load=BE0076_SOLO_FIRE_CRYSTAL_APPEARS,
)
formations[FORM0354_THREE_SHOGUNS] = Formation(
    [
        FormationMember(Shogun, x_pos=167, y_pos=135),
        FormationMember(Shogun, x_pos=151, y_pos=111),
        FormationMember(Shogun, x_pos=215, y_pos=143),
    ],
)
formations[FORM0355_THREE_HEAVY_TROOPA] = Formation(
    [
        FormationMember(HeavyTroopa, x_pos=167, y_pos=135),
        FormationMember(HeavyTroopa, x_pos=151, y_pos=103),
        FormationMember(HeavyTroopa, x_pos=231, y_pos=143),
    ],
)
formations[FORM0356_DODO_BOSS_FIGHT] = Formation(
    [
        FormationMember(DodoSolo, x_pos=183, y_pos=127),
    ],
    can_run_away=False,
    music=BattleMusic.BOSS_1,
)
formations[FORM0357_KAMEK_BOSS_FIGHT] = Formation(
    [
        FormationMember(Kamek, x_pos=215, y_pos=111),
        FormationMember(
            Terrapin,
            x_pos=167,
            y_pos=135,
            hidden_at_start=True,
            include_in_stat_totaling=False,
        ),
    ],
    can_run_away=False,
    music=BattleMusic.BOSS_1,
    additional_enemies_to_scale=[JinxClone, KingBomb, BahamuttKamek],
)
formations[FORM0358_BOOMER_BOSS_FIGHT] = Formation(
    [
        FormationMember(Boomer, x_pos=215, y_pos=143),
        FormationMember(HanginShy, x_pos=66, y_pos=115, include_in_stat_totaling=False),
        FormationMember(HanginShy, x_pos=186, y_pos=74, include_in_stat_totaling=False),
    ],
    can_run_away=False,
    music=BattleMusic.BOSS_1,
    additional_enemies_to_scale=[ShyGuyHenchman],
)
formations[FORM0359_MACHINE_MACK] = Formation(
    [
        FormationMember(MachineMadeMack, x_pos=199, y_pos=119),
        FormationMember(MachineMadeShyster, x_pos=135, y_pos=111),
        FormationMember(MachineMadeShyster, x_pos=151, y_pos=127),
        FormationMember(MachineMadeShyster, x_pos=183, y_pos=143),
        FormationMember(MachineMadeShyster, x_pos=215, y_pos=151),
    ],
    music=BattleMusic.BOSS_2,
)
formations[FORM0360_MACHINE_BOWYER] = Formation(
    [
        FormationMember(MachineMadeBowyer, x_pos=183, y_pos=127),
    ],
    music=BattleMusic.BOSS_2,
)
formations[FORM0361_MACHINE_YARIDOVICH] = Formation(
    [
        FormationMember(MachineMadeYaridovich, x_pos=183, y_pos=127),
        FormationMember(
            MachineMadeDrillBit, x_pos=135, y_pos=119, hidden_at_start=True
        ),
        FormationMember(
            MachineMadeDrillBit, x_pos=167, y_pos=103, hidden_at_start=True
        ),
        FormationMember(
            MachineMadeDrillBit, x_pos=199, y_pos=151, hidden_at_start=True
        ),
        FormationMember(
            MachineMadeDrillBit, x_pos=231, y_pos=135, hidden_at_start=True
        ),
    ],
    music=BattleMusic.BOSS_2,
)
formations[FORM0362_THREE_MACHINE_AXEMS] = Formation(
    [
        FormationMember(MachineMadeAxemPink, x_pos=151, y_pos=111),
        None,
        FormationMember(MachineMadeAxemRed, x_pos=151, y_pos=143),
        None,
        FormationMember(MachineMadeAxemGreen, x_pos=215, y_pos=143),
    ],
    music=BattleMusic.BOSS_2,
)
formations[FORM0363_SMITHY_2] = Formation(
    [
        FormationMember(Smithy2Body, x_pos=183, y_pos=135),
        FormationMember(Smithy2Head, x_pos=183, y_pos=175),
    ],
    can_run_away=False,
)
formations[FORM0364_CLERK_BOSS_FIGHT] = Formation(
    [
        FormationMember(Clerk, x_pos=199, y_pos=119),
        FormationMember(MadMalletHenchman, x_pos=135, y_pos=119),
        FormationMember(MadMalletHenchman, x_pos=199, y_pos=151),
    ],
    can_run_away=False,
)
formations[FORM0365_MANAGER_BOSS_FIGHT] = Formation(
    [
        FormationMember(Manager, x_pos=199, y_pos=119),
        FormationMember(PounderHenchman, x_pos=151, y_pos=111),
        FormationMember(PounderHenchman, x_pos=167, y_pos=135),
        FormationMember(PounderHenchman, x_pos=215, y_pos=143),
    ],
    can_run_away=False,
)
formations[FORM0366_DIRECTOR_BOSS_FIGHT] = Formation(
    [
        FormationMember(Director, x_pos=183, y_pos=127),
        FormationMember(PoundetteHenchman, x_pos=135, y_pos=119),
        FormationMember(PoundetteHenchman, x_pos=167, y_pos=103),
        FormationMember(PoundetteHenchman, x_pos=199, y_pos=151),
        FormationMember(PoundetteHenchman, x_pos=231, y_pos=135),
    ],
    can_run_away=False,
)
formations[FORM0367_GUNYOLK_BOSS_FIGHT] = Formation(
    [
        FormationMember(Gunyolk, x_pos=199, y_pos=103),
        FormationMember(FactoryChief, x_pos=231, y_pos=151),
    ],
    can_run_away=False,
    music=BattleMusic.BOSS_1,
)
formations[FORM0368_THREE_MAD_MALLETS] = Formation(
    [
        FormationMember(MadMallet, x_pos=151, y_pos=111),
        FormationMember(MadMallet, x_pos=167, y_pos=135),
        FormationMember(MadMallet, x_pos=215, y_pos=143),
    ],
    can_run_away=False,
)
formations[FORM0369_ONE_APPRENTICE] = Formation(
    [
        FormationMember(Apprentice, x_pos=183, y_pos=127),
    ],
    can_run_away=False,
)
formations[FORM0370_FOUR_MACHINE_AXEMS] = Formation(
    [
        FormationMember(MachineMadeAxemBlack, x_pos=151, y_pos=119),
        FormationMember(MachineMadeAxemBlack, x_pos=231, y_pos=127),
        FormationMember(MachineMadeAxemYellow, x_pos=199, y_pos=143),
        FormationMember(MachineMadeAxemYellow, x_pos=183, y_pos=103),
    ],
    music=BattleMusic.BOSS_2,
)
formations[FORM0371_FOUR_TERRA_COTTA_KEEP] = Formation(
    [
        FormationMember(Terracotta, x_pos=135, y_pos=127),
        FormationMember(Terracotta, x_pos=183, y_pos=111),
        FormationMember(Terracotta, x_pos=183, y_pos=151),
        FormationMember(Terracotta, x_pos=231, y_pos=135),
    ],
    can_run_away=False,
)
formations[FORM0372_TWO_OERLIKON_ONE_STARCRUSTER_KEEP] = Formation(
    [
        FormationMember(Oerlikon, x_pos=135, y_pos=119),
        FormationMember(Oerlikon, x_pos=199, y_pos=151),
        FormationMember(Starcruster, x_pos=199, y_pos=119),
    ],
    can_run_away=False,
)
formations[FORM0373_ONE_SACKIT_TWO_BIGBERTHA_KEEP] = Formation(
    [
        FormationMember(Sackit, x_pos=167, y_pos=135),
        None,
        FormationMember(BigBertha, x_pos=151, y_pos=103),
        FormationMember(BigBertha, x_pos=231, y_pos=143),
    ],
    can_run_away=False,
)
formations[FORM0374_ONE_CHOW_TWO_FORKIES_KEEP] = Formation(
    [
        FormationMember(Chow, x_pos=135, y_pos=111),
        FormationMember(Chow, x_pos=215, y_pos=151),
        FormationMember(Forkies, x_pos=199, y_pos=119),
    ],
    can_run_away=False,
)
formations[FORM0375_ONE_ALLEYRAT_TWO_ARMOREDANT_KEEP] = Formation(
    [
        FormationMember(AlleyRat, x_pos=199, y_pos=119),
        FormationMember(ArmoredAnt, x_pos=135, y_pos=119),
        FormationMember(ArmoredAnt, x_pos=199, y_pos=151),
    ],
    can_run_away=False,
)
formations[FORM0376_THREE_BLOOBER_ONE_STARCRUSTER_KEEP] = Formation(
    [
        FormationMember(Bloober, x_pos=199, y_pos=119),
        FormationMember(Bloober, x_pos=183, y_pos=151),
        FormationMember(Bloober, x_pos=231, y_pos=151),
        FormationMember(Starcruster, x_pos=135, y_pos=103),
    ],
    can_run_away=False,
)
formations[FORM0377_FOUR_STINGER_KEEP] = Formation(
    [
        FormationMember(Stinger, x_pos=151, y_pos=111),
        FormationMember(Stinger, x_pos=167, y_pos=127),
        FormationMember(Stinger, x_pos=199, y_pos=143),
        FormationMember(Stinger, x_pos=231, y_pos=151),
    ],
    can_run_away=False,
)
formations[FORM0378_TWO_GECKIT_ONE_CHAINEDKONG_KEEP] = Formation(
    [
        FormationMember(Geckit, x_pos=215, y_pos=151),
        FormationMember(Geckit, x_pos=135, y_pos=111),
        FormationMember(ChainedKong, x_pos=199, y_pos=119),
    ],
    can_run_away=False,
)
formations[FORM0379_ONE_ROBOMB_TWO_BIGBERTHA_KEEP] = Formation(
    [
        FormationMember(Robomb, x_pos=167, y_pos=135),
        None,
        FormationMember(BigBertha, x_pos=167, y_pos=111),
        FormationMember(BigBertha, x_pos=215, y_pos=135),
    ],
    can_run_away=False,
)
formations[FORM0380_FOUR_VOMER_KEEP] = Formation(
    [
        FormationMember(Vomer, x_pos=151, y_pos=127),
        FormationMember(Vomer, x_pos=183, y_pos=143),
        FormationMember(Vomer, x_pos=151, y_pos=103),
        FormationMember(Vomer, x_pos=231, y_pos=143),
    ],
    can_run_away=False,
)
formations[FORM0381_TWO_MAGMUS_TWO_PULSAR_KEEP] = Formation(
    [
        FormationMember(Magmus, x_pos=151, y_pos=127),
        FormationMember(Magmus, x_pos=183, y_pos=143),
        FormationMember(Pulsar, x_pos=151, y_pos=103),
        FormationMember(Pulsar, x_pos=231, y_pos=143),
    ],
    can_run_away=False,
)
formations[FORM0382_FIVE_GUGOOMBAS_KEEP] = Formation(
    [
        FormationMember(GuGoomba, x_pos=151, y_pos=127),
        FormationMember(GuGoomba, x_pos=183, y_pos=143),
        FormationMember(GuGoomba, x_pos=199, y_pos=119),
        FormationMember(GuGoomba, x_pos=167, y_pos=103),
        FormationMember(GuGoomba, x_pos=231, y_pos=135),
    ],
    can_run_away=False,
)
formations[FORM0383_TWO_MALAKOOPAS_ONE_TUBOTROOPA_KEEP] = Formation(
    [
        FormationMember(Malakoopa, x_pos=135, y_pos=111),
        FormationMember(Malakoopa, x_pos=215, y_pos=151),
        FormationMember(TuboTroopa, x_pos=199, y_pos=119),
    ],
    can_run_away=False,
)
formations[FORM0384_TWO_BIGBOO_TWO_ORBISON_KEEP] = Formation(
    [
        FormationMember(TheBigBoo, x_pos=183, y_pos=143),
        FormationMember(TheBigBoo, x_pos=151, y_pos=127),
        FormationMember(Orbison, x_pos=167, y_pos=103),
        FormationMember(Orbison, x_pos=231, y_pos=135),
    ],
    can_run_away=False,
)
formations[FORM0385_FIVE_SLINGSHY_KEEP] = Formation(
    [
        FormationMember(SlingShy, x_pos=167, y_pos=135),
        FormationMember(SlingShy, x_pos=167, y_pos=119),
        FormationMember(SlingShy, x_pos=199, y_pos=135),
        FormationMember(SlingShy, x_pos=167, y_pos=103),
        FormationMember(SlingShy, x_pos=231, y_pos=135),
    ],
    can_run_away=False,
)
formations[FORM0386_TWO_CHEWY_TWO_SHYAWAY_KEEP] = Formation(
    [
        FormationMember(Chewy, x_pos=151, y_pos=127),
        FormationMember(Chewy, x_pos=183, y_pos=143),
        FormationMember(Shyaway, x_pos=167, y_pos=103),
        FormationMember(Shyaway, x_pos=231, y_pos=135),
    ],
    can_run_away=False,
)
formations[FORM0387_ONE_MRKIPPER_TWO_MUCKLES_KEEP] = Formation(
    [
        FormationMember(MrKipper, x_pos=167, y_pos=135),
        FormationMember(Muckle, x_pos=167, y_pos=103),
        FormationMember(Muckle, x_pos=231, y_pos=135),
    ],
    can_run_away=False,
)
formations[FORM0388_TWO_AMANITAS_ONE_ORBISON_KEEP] = Formation(
    [
        FormationMember(Amanita, x_pos=215, y_pos=143),
        FormationMember(Amanita, x_pos=151, y_pos=111),
        FormationMember(Orbison, x_pos=183, y_pos=127),
    ],
    can_run_away=False,
)
formations[FORM0389_TWO_GREAPERS_ONE_GLUMREAPER_KEEP] = Formation(
    [
        FormationMember(Greaper, x_pos=215, y_pos=143),
        FormationMember(Greaper, x_pos=151, y_pos=111),
        FormationMember(GlumReaper, x_pos=183, y_pos=127),
    ],
    can_run_away=False,
)
formations[FORM0390_THREE_PYROSPHERE_KEEP] = Formation(
    [
        FormationMember(Pyrosphere, x_pos=183, y_pos=127),
        FormationMember(Pyrosphere, x_pos=151, y_pos=111),
        FormationMember(Pyrosphere, x_pos=215, y_pos=143),
    ],
    can_run_away=False,
)
formations[FORM0391_THREE_LAKITU_KEEP] = Formation(
    [
        FormationMember(Lakitu, x_pos=183, y_pos=127),
        FormationMember(Lakitu, x_pos=151, y_pos=111),
        FormationMember(Lakitu, x_pos=215, y_pos=143),
    ],
    can_run_away=False,
)
formations[FORM0392_TWO_ZEOSTAR_TWO_SHAMAN_KEEP] = Formation(
    [
        FormationMember(Zeostar, x_pos=151, y_pos=127),
        FormationMember(Zeostar, x_pos=183, y_pos=143),
        FormationMember(Shaman, x_pos=167, y_pos=103),
        FormationMember(Shaman, x_pos=231, y_pos=135),
    ],
    can_run_away=False,
)
formations[FORM0393_SIX_SHAMANS_KEEP] = Formation(
    [
        FormationMember(Shaman, x_pos=135, y_pos=119),
        FormationMember(Shaman, x_pos=167, y_pos=103),
        FormationMember(Shaman, x_pos=167, y_pos=135),
        FormationMember(Shaman, x_pos=199, y_pos=119),
        FormationMember(Shaman, x_pos=199, y_pos=151),
        FormationMember(Shaman, x_pos=231, y_pos=135),
    ],
    can_run_away=False,
)
formations[FORM0394_THREE_MACHINE_SHYSTERS] = Formation(
    [
        FormationMember(MachineMadeShyster, x_pos=199, y_pos=119),
        FormationMember(MachineMadeShyster, x_pos=135, y_pos=119),
        FormationMember(MachineMadeShyster, x_pos=199, y_pos=151),
    ],
)
formations[FORM0395_THREE_MACHINE_DRILLBITS] = Formation(
    [
        FormationMember(YaridovichDrillBit, x_pos=183, y_pos=127),
        FormationMember(YaridovichDrillBit, x_pos=167, y_pos=103),
        FormationMember(YaridovichDrillBit, x_pos=231, y_pos=135),
    ],
)
formations[396] = None
formations[397] = None
formations[398] = None
formations[399] = None
formations[400] = None
formations[401] = None
formations[402] = None
formations[403] = None
formations[404] = None
formations[FORM0405_ONE_WATER_CRYSTAL] = Formation(
    [FormationMember(WaterCrystal, x_pos=183, y_pos=127)],
    run_event_at_load=BE0020_SOLO_WATER_CRYSTAL_APPEARS,
)
formations[FORM0406_ONE_EARTH_CRYSTAL] = Formation(
    [
        FormationMember(EarthCrystal, x_pos=183, y_pos=127),
    ],
    run_event_at_load=BE0011_SOLO_EARTH_CRYSTAL_APPEARS,
)
formations[FORM0407_ONE_WIND_CRYSTAL] = Formation(
    [
        FormationMember(WindCrystal, x_pos=183, y_pos=127),
    ],
    run_event_at_load=BE0035_BOOSTER_EATS_CAKE,
)
formations[FORM0408_THREE_GOOMBETTES] = Formation(
    [
        FormationMember(Goombette, x_pos=183, y_pos=127),
        FormationMember(Goombette, x_pos=231, y_pos=135),
        FormationMember(Goombette, x_pos=167, y_pos=103),
    ]
)
formations[FORM0409_ONE_PIRANHA_HENCHMAN] = Formation(
    [
        FormationMember(PiranhaPlantHenchman, x_pos=167, y_pos=135),
    ]
)
formations[FORM0410_THREE_PIRANHA_HENCHMEN] = Formation(
    [
        FormationMember(PiranhaPlantHenchman, x_pos=167, y_pos=111),
        FormationMember(PiranhaPlantHenchman, x_pos=167, y_pos=135),
        FormationMember(PiranhaPlantHenchman, x_pos=215, y_pos=135),
    ]
)
formations[FORM0411_FIVE_PIRANHA_HENCHMEN] = Formation(
    [
        FormationMember(PiranhaPlantHenchman, x_pos=151, y_pos=143),
        FormationMember(PiranhaPlantHenchman, x_pos=151, y_pos=111),
        FormationMember(PiranhaPlantHenchman, x_pos=199, y_pos=119),
        FormationMember(PiranhaPlantHenchman, x_pos=231, y_pos=143),
        FormationMember(PiranhaPlantHenchman, x_pos=199, y_pos=159),
    ]
)
formations[FORM0412_ONE_EGGBERT] = Formation(
    [
        FormationMember(Eggbert, x_pos=183, y_pos=127),
    ]
)
formations[FORM0413_THREE_EGGBERTS] = Formation(
    [
        FormationMember(Eggbert, x_pos=167, y_pos=111),
        FormationMember(Eggbert, x_pos=167, y_pos=135),
        FormationMember(Eggbert, x_pos=215, y_pos=135),
    ]
)
formations[FORM0414_FOUR_EGGBERTS] = Formation(
    [
        FormationMember(Eggbert, x_pos=135, y_pos=127),
        FormationMember(Eggbert, x_pos=183, y_pos=111),
        FormationMember(Eggbert, x_pos=183, y_pos=151),
        FormationMember(Eggbert, x_pos=231, y_pos=135),
    ]
)
formations[FORM0415_SOLO_AXEM_BLACK] = Formation(
    [
        FormationMember(AxemBlack, x_pos=183, y_pos=127),
    ]
)
formations[FORM0416_SOLO_AXEM_PINK] = Formation(
    [
        FormationMember(AxemPink, x_pos=183, y_pos=127),
    ]
)
formations[FORM0417_SOLO_AXEM_YELLOW] = Formation(
    [
        FormationMember(AxemYellow, x_pos=183, y_pos=127),
    ]
)
formations[FORM0418_SOLO_AXEM_GREEN] = Formation(
    [
        FormationMember(AxemGreen, x_pos=183, y_pos=127),
    ]
)
formations[FORM0419_SOLO_DINGALING] = Formation(
    [
        FormationMember(DingALing, x_pos=183, y_pos=127),
    ],
    run_event_at_load=BE0014_SET_7EE00A_TO_PARTY_SIZE_AT_START_OF_FIGHT,
)
formations[FORM0420_SMITHY_HENCHMEN_MIX] = Formation(
    [
        FormationMember(MachineMadeShysterHenchman, x_pos=151, y_pos=111),
        FormationMember(AeroSmithy, x_pos=215, y_pos=127),
        FormationMember(DrillBit, x_pos=167, y_pos=151),
    ]
)
formations[FORM0421_FOUR_DRILLBITS] = Formation(
    [
        FormationMember(DrillBit, x_pos=135, y_pos=119),
        FormationMember(DrillBit, x_pos=167, y_pos=103),
        FormationMember(DrillBit, x_pos=199, y_pos=151),
        FormationMember(DrillBit, x_pos=231, y_pos=135),
    ]
)
formations[FORM0422_ONE_DRILLBIT_TWO_AEROS] = Formation(
    [
        FormationMember(DrillBit, x_pos=183, y_pos=127),
        FormationMember(AeroSmithy, x_pos=215, y_pos=143),
        FormationMember(AeroSmithy, x_pos=151, y_pos=111),
    ]
)
formations[FORM0423_TWO_MACHINE_SHYSTER_HENCHMEN] = Formation(
    [
        FormationMember(MachineMadeShysterHenchman, x_pos=167, y_pos=119),
        FormationMember(MachineMadeShysterHenchman, x_pos=199, y_pos=135),
    ]
)
formations[FORM0424_TWO_DRILLBITS_ONE_MACHINE_SHYSTER] = Formation(
    [
        FormationMember(DrillBit, x_pos=231, y_pos=135),
        FormationMember(DrillBit, x_pos=167, y_pos=103),
        FormationMember(MachineMadeShysterHenchman, x_pos=167, y_pos=135),
    ]
)
formations[FORM0425_FIVE_AEROS] = Formation(
    [
        FormationMember(AeroSmithy, x_pos=167, y_pos=103),
        FormationMember(AeroSmithy, x_pos=135, y_pos=119),
        FormationMember(AeroSmithy, x_pos=183, y_pos=127),
        FormationMember(AeroSmithy, x_pos=199, y_pos=151),
        FormationMember(AeroSmithy, x_pos=231, y_pos=135),
    ]
)
formations[FORM0426_TWO_AEROS_ONE_MACHINE_SHYSTER] = Formation(
    [
        FormationMember(AeroSmithy, x_pos=231, y_pos=135),
        FormationMember(AeroSmithy, x_pos=167, y_pos=103),
        FormationMember(MachineMadeShysterHenchman, x_pos=167, y_pos=135),
    ]
)
formations[FORM0427_THREE_CROOKS] = Formation(
    [
        FormationMember(Crook, x_pos=135, y_pos=119),
        FormationMember(Crook, x_pos=199, y_pos=119),
        FormationMember(Crook, x_pos=199, y_pos=151),
    ]
)
formations[FORM0428_FIVE_CROOKS] = Formation(
    [
        FormationMember(Crook, x_pos=167, y_pos=103),
        FormationMember(Crook, x_pos=135, y_pos=119),
        FormationMember(Crook, x_pos=183, y_pos=127),
        FormationMember(Crook, x_pos=199, y_pos=151),
        FormationMember(Crook, x_pos=231, y_pos=135),
    ]
)
formations[FORM0429_THREE_BIRDY_HENCHMEN] = Formation(
    [
        FormationMember(BirdyHenchman, x_pos=215, y_pos=119),
        FormationMember(BirdyHenchman, x_pos=151, y_pos=119),
        FormationMember(BirdyHenchman, x_pos=183, y_pos=151),
    ]
)
formations[FORM0430_SOLO_MARIO_CLONE] = Formation(
    [
        FormationMember(MarioClone, x_pos=183, y_pos=127),
    ]
)
formations[FORM0431_SOLO_MALLOW_CLONE] = Formation(
    [
        FormationMember(MallowClone, x_pos=183, y_pos=127),
    ]
)
formations[FORM0432_SOLO_GENO_CLONE] = Formation(
    [
        FormationMember(GenoClone, x_pos=183, y_pos=127),
    ]
)
formations[FORM0433_SOLO_BOWSER_CLONE] = Formation(
    [
        FormationMember(BowserClone, x_pos=183, y_pos=127),
    ]
)
formations[FORM0434_SOLO_TOADSTOOL_CLONE] = Formation(
    [
        FormationMember(PeachClone, x_pos=183, y_pos=127),
    ]
)
formations[435] = None
formations[436] = None
formations[437] = None
formations[438] = None
formations[439] = None
formations[440] = None
formations[441] = None
formations[442] = None
formations[443] = None
formations[444] = None
formations[445] = None
formations[446] = None
formations[447] = None
formations[448] = None
formations[449] = None
formations[450] = None
formations[451] = None
formations[452] = None
formations[453] = None
formations[454] = None
formations[455] = None
formations[456] = None
formations[457] = None
formations[458] = None
formations[459] = None
formations[460] = None
formations[461] = None
formations[462] = None
formations[463] = None
formations[464] = None
formations[465] = None
formations[466] = None
formations[467] = None
formations[468] = None
formations[469] = None
formations[470] = None
formations[471] = None
formations[472] = None
formations[473] = None
formations[474] = None
formations[475] = None
formations[476] = None
formations[477] = None
formations[478] = None
formations[479] = None
formations[480] = None
formations[481] = None
formations[482] = None
formations[483] = None
formations[484] = None
formations[485] = None
formations[486] = None
formations[487] = None
formations[488] = None
formations[489] = None
formations[490] = None
formations[491] = None
formations[492] = None
formations[493] = None
formations[494] = None
formations[495] = None
formations[496] = None
formations[497] = None
formations[498] = None
formations[499] = None
formations[500] = None
formations[501] = None
formations[502] = None
formations[503] = None
formations[504] = None
formations[505] = None
formations[506] = None
formations[507] = None
formations[508] = None
formations[509] = None
formations[510] = None
formations[511] = None
