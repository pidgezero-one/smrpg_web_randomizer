"""ROM's PackCollection disassembled from the original game."""

from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (
    Formation,
    FormationMember,
    FormationPack,
    PackCollection,
)
from smrpgpatchbuilder.datatypes.battles.music import (
    NormalBattleMusic,
    MidbossMusic,
    BossMusic,
    Smithy1Music,
    CorndillyMusic,
    BoosterHillMusic,
    VolcanoMusic,
    CulexMusic,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import Battlefield
from ..enemies.enemies import *
from ..variables.pack_names import *
from ..variables.battle_event_names import *


# ============================================================================
# Formation Declarations
# ============================================================================

FORM0000_ONE_SNIFIT = Formation(
    id=0,
    members=[
        FormationMember(SNIFITEnemyHenchman, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
    can_run_away=False,
)

FORM0001_TWO_SPIKEY = Formation(
    id=1,
    members=[
        FormationMember(SPIKEYEnemy, 135, 127),
        FormationMember(SPIKEYEnemy, 199, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0002_ONE_SPIKEY_ONE_SKYTROOPA = Formation(
    id=2,
    members=[
        FormationMember(SPIKEYEnemy, 135, 119),
        FormationMember(SKYTROOPAEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0003_THREE_SPIKEY = Formation(
    id=3,
    members=[
        FormationMember(SPIKEYEnemy, 135, 119),
        FormationMember(SPIKEYEnemy, 199, 119),
        FormationMember(SPIKEYEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0004_TWO_SPIKEY_ONE_FROGOG = Formation(
    id=4,
    members=[
        FormationMember(SPIKEYEnemy, 135, 119),
        FormationMember(SPIKEYEnemy, 199, 151),
        FormationMember(FROGOGEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0005_ONE_SKYTROOPA = Formation(
    id=5,
    members=[
        FormationMember(SKYTROOPAEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0006_TWO_SKYTROOPA = Formation(
    id=6,
    members=[
        FormationMember(SKYTROOPAEnemy, 135, 119),
        FormationMember(SKYTROOPAEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0007_TWO_SKYTROOPA_ONE_GOOMBA = Formation(
    id=7,
    members=[
        FormationMember(SKYTROOPAEnemy, 167, 103),
        FormationMember(SKYTROOPAEnemy, 231, 135),
        None,
        FormationMember(GOOMBAEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0008_TWO_SKYTROOPA_ONE_FROGOG = Formation(
    id=8,
    members=[
        FormationMember(SKYTROOPAEnemy, 199, 151),
        FormationMember(SKYTROOPAEnemy, 135, 119),
        FormationMember(FROGOGEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0009_TWO_GOOMBA = Formation(
    id=9,
    members=[
        FormationMember(GOOMBAEnemy, 135, 119),
        FormationMember(GOOMBAEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0010_THREE_GOOMBA = Formation(
    id=10,
    members=[
        FormationMember(GOOMBAEnemy, 167, 111),
        FormationMember(GOOMBAEnemy, 167, 135),
        FormationMember(GOOMBAEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0011_ONE_GOOMBA_ONE_FROGOG_ONE_SPIKEY = Formation(
    id=11,
    members=[
        FormationMember(GOOMBAEnemy, 167, 135),
        FormationMember(FROGOGEnemy, 167, 111),
        FormationMember(SPIKEYEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0012_TWO_GOOMBA_ONE_SPIKEY = Formation(
    id=12,
    members=[
        FormationMember(GOOMBAEnemy, 167, 111),
        FormationMember(GOOMBAEnemy, 215, 135),
        FormationMember(SPIKEYEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0013_ONE_K9 = Formation(
    id=13,
    members=[
        FormationMember(K9Enemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0014_TWO_K9 = Formation(
    id=14,
    members=[
        FormationMember(K9Enemy, 199, 159),
        FormationMember(K9Enemy, 151, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0015_TWO_K9_ONE_SPIKEY = Formation(
    id=15,
    members=[
        FormationMember(K9Enemy, 135, 119),
        FormationMember(K9Enemy, 199, 151),
        FormationMember(SPIKEYEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0016_ONE_K9_TWO_FROGOG = Formation(
    id=16,
    members=[
        FormationMember(K9Enemy, 183, 127),
        FormationMember(FROGOGEnemy, 215, 143),
        FormationMember(FROGOGEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0017_TWO_SHYSTER = Formation(
    id=17,
    members=[
        FormationMember(BODYGUARDEnemy, 167, 119),
        FormationMember(BODYGUARDEnemy, 199, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0018_THREE_SHYSTER = Formation(
    id=18,
    members=[
        FormationMember(BODYGUARDEnemy, 151, 111),
        FormationMember(BODYGUARDEnemy, 215, 143),
        FormationMember(BODYGUARDEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0019_TWO_RATFUNK = Formation(
    id=19,
    members=[
        FormationMember(RATFUNKEnemy, 199, 143),
        FormationMember(RATFUNKEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0020_TWO_RATFUNK_ONE_SHADOW = Formation(
    id=20,
    members=[
        FormationMember(RATFUNKEnemy, 135, 119),
        FormationMember(RATFUNKEnemy, 199, 151),
        FormationMember(SHADOWEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0021_TWO_RATFUNK_ONE_HOBGOBLIN = Formation(
    id=21,
    members=[
        FormationMember(RATFUNKEnemy, 135, 119),
        FormationMember(RATFUNKEnemy, 199, 151),
        FormationMember(HOBGOBLINEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0022_ONE_RATFUNK_TWO_HOBGOBLIN = Formation(
    id=22,
    members=[
        FormationMember(RATFUNKEnemy, 167, 135),
        None,
        FormationMember(HOBGOBLINEnemy, 167, 103),
        FormationMember(HOBGOBLINEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0023_ONE_THEBIGBOO_ONE_SHADOW = Formation(
    id=23,
    members=[
        FormationMember(THEBIGBOOEnemy, 151, 119),
        FormationMember(SHADOWEnemy, 199, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0024_ONE_THEBIGBOO_ONE_SHADOW_ONE_HOBGOBLIN = Formation(
    id=24,
    members=[
        FormationMember(THEBIGBOOEnemy, 119, 119),
        FormationMember(SHADOWEnemy, 167, 135),
        FormationMember(HOBGOBLINEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0025_THREE_THEBIGBOO_ONE_SHADOW = Formation(
    id=25,
    members=[
        FormationMember(THEBIGBOOEnemy, 231, 135),
        FormationMember(THEBIGBOOEnemy, 151, 143),
        FormationMember(THEBIGBOOEnemy, 167, 103),
        FormationMember(SHADOWEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0026_TWO_GOBY = Formation(
    id=26,
    members=[
        FormationMember(GOBYEnemy, 135, 119),
        FormationMember(GOBYEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0027_THREE_GOBY = Formation(
    id=27,
    members=[
        FormationMember(GOBYEnemy, 151, 119),
        FormationMember(GOBYEnemy, 215, 119),
        FormationMember(GOBYEnemy, 183, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0028_TWO_CROOK = Formation(
    id=28,
    members=[
        FormationMember(CROOKEnemyStatic, 167, 111),
        FormationMember(CROOKEnemyStatic, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0029_TWO_CROOK_ONE_SHYGUY = Formation(
    id=29,
    members=[
        FormationMember(CROOKEnemyStatic, 199, 143),
        FormationMember(CROOKEnemyStatic, 151, 119),
        FormationMember(SHYGUYEnemyStatic, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0030_ONE_CROOK_TWO_SNAPDRAGON = Formation(
    id=30,
    members=[
        FormationMember(CROOKEnemyStatic, 183, 127),
        FormationMember(SNAPDRAGONEnemy, 151, 111),
        FormationMember(SNAPDRAGONEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0031_ONE_CROOK_ONE_STARSLAP_ONE_ARACHNE = Formation(
    id=31,
    members=[
        FormationMember(CROOKEnemyStatic, 199, 159),
        None,
        None,
        FormationMember(STARSLAPEnemy, 215, 127),
        FormationMember(ARACHNEEnemy, 167, 103),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0032_ONE_SHYGUY_ONE_STARSLAP = Formation(
    id=32,
    members=[
        FormationMember(SHYGUYEnemyStatic, 151, 111),
        None,
        FormationMember(STARSLAPEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0033_TWO_SHYGUY_ONE_SNAPDRAGON = Formation(
    id=33,
    members=[
        FormationMember(SHYGUYEnemyStatic, 135, 103),
        FormationMember(SHYGUYEnemyStatic, 215, 143),
        None,
        FormationMember(SNAPDRAGONEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0034_ONE_SHYGUY_ONE_CROOK_ONE_ARACHNE = Formation(
    id=34,
    members=[
        FormationMember(SHYGUYEnemyStatic, 231, 135),
        None,
        FormationMember(CROOKEnemyStatic, 199, 143),
        FormationMember(ARACHNEEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0035_ONE_STARSLAP_ONE_SHYGUY = Formation(
    id=35,
    members=[
        FormationMember(STARSLAPEnemy, 199, 159),
        FormationMember(SHYGUYEnemyStatic, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0036_ONE_STARSLAP_ONE_ARACHNE = Formation(
    id=36,
    members=[
        FormationMember(STARSLAPEnemy, 215, 151),
        FormationMember(ARACHNEEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0037_ONE_STARSLAP_TWO_SNAPDRAGON = Formation(
    id=37,
    members=[
        FormationMember(STARSLAPEnemy, 167, 135),
        FormationMember(SNAPDRAGONEnemy, 151, 111),
        FormationMember(SNAPDRAGONEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0038_FOUR_STARSLAP = Formation(
    id=38,
    members=[
        FormationMember(STARSLAPEnemy, 199, 151),
        FormationMember(STARSLAPEnemy, 167, 103),
        FormationMember(STARSLAPEnemy, 231, 135),
        FormationMember(STARSLAPEnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0039_ONE_WIGGLER = Formation(
    id=39,
    members=[
        FormationMember(WIGGLEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0040_ONE_WIGGLER_ONE_AMANITA = Formation(
    id=40,
    members=[
        FormationMember(WIGGLEREnemy, 151, 111),
        FormationMember(AMANITAEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0041_TWO_WIGGLER = Formation(
    id=41,
    members=[
        FormationMember(WIGGLEREnemy, 151, 111),
        FormationMember(WIGGLEREnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0042_ONE_WIGGLER_ONE_GUERRILLA = Formation(
    id=42,
    members=[
        FormationMember(WIGGLEREnemy, 151, 119),
        None,
        FormationMember(GUERRILLAEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0043_TWO_AMANITA = Formation(
    id=43,
    members=[
        FormationMember(AMANITAEnemy, 135, 127),
        FormationMember(AMANITAEnemy, 199, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0044_TWO_AMANITA_ONE_BUZZER = Formation(
    id=44,
    members=[
        FormationMember(AMANITAEnemy, 199, 151),
        FormationMember(AMANITAEnemy, 135, 119),
        FormationMember(BUZZEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0045_TWO_AMANITA_ONE_OCTOLOT = Formation(
    id=45,
    members=[
        FormationMember(AMANITAEnemy, 199, 151),
        FormationMember(AMANITAEnemy, 135, 119),
        FormationMember(OCTOLOTEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0046_ONE_AMANITA_ONE_GUERRILLA_ONE_BUZZER = Formation(
    id=46,
    members=[
        FormationMember(AMANITAEnemy, 151, 127),
        None,
        FormationMember(GUERRILLAEnemy, 215, 143),
        FormationMember(BUZZEREnemy, 183, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0047_ONE_BUZZER_ONE_OCTOLOT = Formation(
    id=47,
    members=[
        FormationMember(BUZZEREnemy, 135, 119),
        FormationMember(OCTOLOTEnemy, 199, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0048_TWO_BUZZER_ONE_AMANITA = Formation(
    id=48,
    members=[
        FormationMember(BUZZEREnemy, 167, 103),
        FormationMember(BUZZEREnemy, 231, 135),
        FormationMember(AMANITAEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0049_ONE_BUZZER_ONE_GUERRILLA = Formation(
    id=49,
    members=[
        FormationMember(BUZZEREnemy, 199, 151),
        None,
        FormationMember(GUERRILLAEnemy, 151, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0050_ONE_BUZZER_ONE_GUERRILLA = Formation(
    id=50,
    members=[
        FormationMember(BUZZEREnemy, 199, 159),
        None,
        FormationMember(GUERRILLAEnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0051_ONE_SPARKY = Formation(
    id=51,
    members=[
        FormationMember(SPARKYEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0052_TWO_SPARKY_ONE_SHYRANGER = Formation(
    id=52,
    members=[
        FormationMember(SPARKYEnemy, 167, 111),
        FormationMember(SPARKYEnemy, 215, 135),
        FormationMember(SHYRANGEREnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0053_THREE_SPARKY = Formation(
    id=53,
    members=[
        FormationMember(SPARKYEnemy, 167, 135),
        FormationMember(SPARKYEnemy, 151, 111),
        FormationMember(SPARKYEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0054_ONE_APPRENTICE = Formation(
    id=54,
    members=[
        FormationMember(APPRENTICEEnemyHenchman, 183, 127),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0055_ONE_BELOMEENEMY3_ONE_MARIOCLONES_ONE_TOADSTOOL3 = Formation(
    id=55,
    members=[
        FormationMember(BELOMEEnemy3, 183, 127),
        FormationMember(MARIOCLONESEnemy, 135, 119, hidden_at_start=True),
        FormationMember(TOADSTOOL3Enemy, 215, 159, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0056_ONE_PIRANHAPLANT = Formation(
    id=56,
    members=[
        FormationMember(PIRANHAPLANTEnemyStatic, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0057_TWO_PIRANHAPLANT_ONE_SHYRANGER = Formation(
    id=57,
    members=[
        FormationMember(PIRANHAPLANTEnemyStatic, 215, 143),
        FormationMember(PIRANHAPLANTEnemyStatic, 151, 111),
        FormationMember(SHYRANGEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0058_THREE_PIRANHAPLANT = Formation(
    id=58,
    members=[
        FormationMember(PIRANHAPLANTEnemyStatic, 167, 111),
        FormationMember(PIRANHAPLANTEnemyStatic, 167, 135),
        FormationMember(PIRANHAPLANTEnemyStatic, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0059_FIVE_PIRANHAPLANT = Formation(
    id=59,
    members=[
        FormationMember(PIRANHAPLANTEnemyStatic, 151, 143),
        FormationMember(PIRANHAPLANTEnemyStatic, 151, 111),
        FormationMember(PIRANHAPLANTEnemyStatic, 199, 119),
        FormationMember(PIRANHAPLANTEnemyStatic, 231, 143),
        FormationMember(PIRANHAPLANTEnemyStatic, 199, 159),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0060_ONE_BOBOMB = Formation(
    id=60,
    members=[
        FormationMember(BOBOMBEnemyStatic, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0061_TWO_BOBOMB_ONE_CLUSTER = Formation(
    id=61,
    members=[
        FormationMember(BOBOMBEnemyStatic, 135, 119),
        FormationMember(BOBOMBEnemyStatic, 199, 151),
        FormationMember(CLUSTEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0062_FOUR_BOBOMB = Formation(
    id=62,
    members=[
        FormationMember(BOBOMBEnemyStatic, 151, 127),
        FormationMember(BOBOMBEnemyStatic, 167, 103),
        FormationMember(BOBOMBEnemyStatic, 199, 151),
        FormationMember(BOBOMBEnemyStatic, 215, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0063_TWO_BOBOMB_ONE_ENIGMA_ONE_CLUSTER = Formation(
    id=63,
    members=[
        FormationMember(BOBOMBEnemyStatic, 135, 119),
        FormationMember(BOBOMBEnemyStatic, 199, 151),
        FormationMember(ENIGMAEnemy, 183, 111),
        FormationMember(CLUSTEREnemy, 215, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0064_ONE_SPARKY_ONE_ENIGMA = Formation(
    id=64,
    members=[
        FormationMember(SPARKYEnemy, 199, 151),
        FormationMember(ENIGMAEnemy, 167, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0065_TWO_SPARKY_ONE_BOBOMB = Formation(
    id=65,
    members=[
        FormationMember(SPARKYEnemy, 167, 111),
        FormationMember(SPARKYEnemy, 215, 135),
        FormationMember(BOBOMBEnemyStatic, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0066_ONE_SPARKY_TWO_CLUSTER = Formation(
    id=66,
    members=[
        FormationMember(SPARKYEnemy, 183, 127),
        FormationMember(CLUSTEREnemy, 231, 143),
        FormationMember(CLUSTEREnemy, 151, 103),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0067_TWO_SPARKY_TWO_ENIGMA = Formation(
    id=67,
    members=[
        FormationMember(SPARKYEnemy, 183, 143),
        FormationMember(SPARKYEnemy, 151, 127),
        FormationMember(ENIGMAEnemy, 167, 103),
        FormationMember(ENIGMAEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0068_TWO_MAGMITE = Formation(
    id=68,
    members=[
        FormationMember(MAGMITEEnemy, 167, 111),
        FormationMember(MAGMITEEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0069_ONE_MAGMITE_ONE_BOBOMB_ONE_SPARKY = Formation(
    id=69,
    members=[
        FormationMember(MAGMITEEnemy, 151, 111),
        FormationMember(BOBOMBEnemyStatic, 183, 127),
        FormationMember(SPARKYEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0070_TWO_MAGMITE_TWO_CLUSTER = Formation(
    id=70,
    members=[
        FormationMember(MAGMITEEnemy, 151, 127),
        FormationMember(MAGMITEEnemy, 183, 143),
        FormationMember(CLUSTEREnemy, 167, 103),
        FormationMember(CLUSTEREnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0071_TWO_MAGMITE_ONE_BOBOMB_ONE_CLUSTER = Formation(
    id=71,
    members=[
        FormationMember(MAGMITEEnemy, 135, 103),
        FormationMember(MAGMITEEnemy, 231, 151),
        FormationMember(BOBOMBEnemyStatic, 167, 135),
        None,
        FormationMember(CLUSTEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0072_ONE_LAKITU = Formation(
    id=72,
    members=[
        FormationMember(LAKITUEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0073_ONE_LAKITU_ONE_SPIKESTER_ONE_ARTICHOKER = Formation(
    id=73,
    members=[
        FormationMember(LAKITUEnemy, 135, 119),
        FormationMember(SPIKESTEREnemy, 199, 159),
        FormationMember(ARTICHOKEREnemy, 183, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0074_THREE_LAKITU = Formation(
    id=74,
    members=[
        FormationMember(LAKITUEnemy, 151, 111),
        FormationMember(LAKITUEnemy, 183, 127),
        FormationMember(LAKITUEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0075_TWO_LAKITU_ONE_ARTICHOKER = Formation(
    id=75,
    members=[
        FormationMember(LAKITUEnemy, 231, 151),
        FormationMember(LAKITUEnemy, 135, 103),
        None,
        FormationMember(ARTICHOKEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0076_ONE_SPIKESTER_ONE_CARROBOSCIS = Formation(
    id=76,
    members=[
        FormationMember(SPIKESTEREnemy, 215, 143),
        FormationMember(CARROBOSCISEnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0077_TWO_SPIKESTER_ONE_ARTICHOKER = Formation(
    id=77,
    members=[
        FormationMember(SPIKESTEREnemy, 199, 151),
        FormationMember(SPIKESTEREnemy, 135, 119),
        FormationMember(ARTICHOKEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0078_ONE_SPIKESTER_TWO_CARROBOSCIS = Formation(
    id=78,
    members=[
        FormationMember(SPIKESTEREnemy, 183, 127),
        FormationMember(CARROBOSCISEnemy, 135, 119),
        FormationMember(CARROBOSCISEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0079_FOUR_SPIKESTER_ONE_CARROBOSCIS = Formation(
    id=79,
    members=[
        FormationMember(SPIKESTEREnemy, 119, 111),
        FormationMember(SPIKESTEREnemy, 215, 159),
        FormationMember(SPIKESTEREnemy, 215, 135),
        FormationMember(SPIKESTEREnemy, 167, 111),
        FormationMember(CARROBOSCISEnemy, 151, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0080_ONE_SPOOKUM_ONE_ORBUSER = Formation(
    id=80,
    members=[
        FormationMember(SPOOKUMEnemy, 199, 135),
        FormationMember(ORBUSEREnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0081_TWO_SPOOKUM_ONE_JESTER = Formation(
    id=81,
    members=[
        FormationMember(SPOOKUMEnemy, 135, 119),
        FormationMember(SPOOKUMEnemy, 199, 151),
        FormationMember(JESTEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0082_ONE_SPOOKUM_ONE_REMOCON_ONE_ORBUSER = Formation(
    id=82,
    members=[
        FormationMember(SPOOKUMEnemy, 151, 111),
        FormationMember(REMOCONEnemy, 167, 151),
        FormationMember(ORBUSEREnemy, 215, 127),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0083_TWO_SPOOKUM_ONE_REMOCON = Formation(
    id=83,
    members=[
        FormationMember(SPOOKUMEnemy, 135, 119),
        FormationMember(SPOOKUMEnemy, 199, 151),
        FormationMember(REMOCONEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0084_ONE_ROBOMB = Formation(
    id=84,
    members=[
        FormationMember(ROBOMBEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0085_THREE_ROBOMB = Formation(
    id=85,
    members=[
        FormationMember(ROBOMBEnemy, 183, 127),
        FormationMember(ROBOMBEnemy, 199, 119),
        FormationMember(ROBOMBEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0086_TWO_ROBOMB_ONE_REMOCON = Formation(
    id=86,
    members=[
        FormationMember(ROBOMBEnemy, 215, 143),
        FormationMember(ROBOMBEnemy, 151, 111),
        FormationMember(REMOCONEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0087_FOUR_ROBOMB_ONE_ORBUSER = Formation(
    id=87,
    members=[
        FormationMember(ROBOMBEnemy, 135, 127),
        FormationMember(ROBOMBEnemy, 231, 127),
        FormationMember(ROBOMBEnemy, 183, 103),
        FormationMember(ROBOMBEnemy, 183, 151),
        FormationMember(ORBUSEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0088_ONE_CHOMP_ONE_JESTER = Formation(
    id=88,
    members=[
        FormationMember(CHOMPEnemy, 215, 143),
        FormationMember(JESTEREnemy, 167, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0089_ONE_CHOMP_ONE_ROBOMB_ONE_REMOCON = Formation(
    id=89,
    members=[
        FormationMember(CHOMPEnemy, 215, 143),
        FormationMember(ROBOMBEnemy, 151, 135),
        FormationMember(REMOCONEnemy, 167, 103),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0090_TWO_CHOMP_ONE_ORBUSER = Formation(
    id=90,
    members=[
        FormationMember(CHOMPEnemy, 151, 111),
        FormationMember(CHOMPEnemy, 215, 143),
        FormationMember(ORBUSEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0091_ONE_CHOMP_TWO_JESTER = Formation(
    id=91,
    members=[
        FormationMember(CHOMPEnemy, 199, 119),
        None,
        FormationMember(JESTEREnemy, 135, 103),
        FormationMember(JESTEREnemy, 231, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0092_ONE_BLASTER_ONE_SPOOKUM = Formation(
    id=92,
    members=[
        FormationMember(BLASTEREnemy, 167, 135),
        FormationMember(SPOOKUMEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0093_ONE_BLASTER_ONE_SPOOKUM_ONE_REMOCON = Formation(
    id=93,
    members=[
        FormationMember(BLASTEREnemy, 167, 135),
        FormationMember(SPOOKUMEnemy, 151, 111),
        FormationMember(REMOCONEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0094_TWO_BLASTER_ONE_SPOOKUM = Formation(
    id=94,
    members=[
        FormationMember(BLASTEREnemy, 199, 151),
        FormationMember(BLASTEREnemy, 135, 119),
        FormationMember(SPOOKUMEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0095_ONE_BLASTER_TWO_ROBOMB_TWO_SPOOKUM = Formation(
    id=95,
    members=[
        FormationMember(BLASTEREnemy, 199, 119),
        FormationMember(ROBOMBEnemy, 135, 103),
        FormationMember(ROBOMBEnemy, 231, 151),
        FormationMember(SPOOKUMEnemy, 151, 127),
        FormationMember(SPOOKUMEnemy, 183, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0096_ONE_CULEX3D_ONE_FIRECRYS3D_ONE_WATERCRYS3D_ONE_EARTHCRYS3D_ONE_WINDCRYS3D = Formation(
    id=96,
    members=[
        FormationMember(CULEX3DEnemy, 183, 103),
        FormationMember(FIRECRYS3DEnemy, 105, 133, hidden_at_start=True),
        FormationMember(WATERCRYS3DEnemy, 121, 149, hidden_at_start=True),
        FormationMember(EARTHCRYS3DEnemy, 153, 165, hidden_at_start=True),
        FormationMember(WINDCRYS3DEnemy, 185, 173, hidden_at_start=True),
    ],
    music=CulexMusic(),
    unknown_bit=True,
)

FORM0097_ONE_MUKUMUKU = Formation(
    id=97,
    members=[
        FormationMember(MUKUMUKUEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0098_TWO_MUKUMUKU = Formation(
    id=98,
    members=[
        FormationMember(MUKUMUKUEnemy, 151, 119),
        FormationMember(MUKUMUKUEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0099_TWO_MUKUMUKU_ONE_PULSAR = Formation(
    id=99,
    members=[
        FormationMember(MUKUMUKUEnemy, 151, 111),
        FormationMember(MUKUMUKUEnemy, 215, 143),
        FormationMember(PULSAREnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0100_ONE_MUKUMUKU_ONE_PULSAR_ONE_GECKO = Formation(
    id=100,
    members=[
        FormationMember(MUKUMUKUEnemy, 183, 143),
        FormationMember(PULSAREnemy, 151, 111),
        FormationMember(GECKOEnemy, 231, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0101_TWO_SACKIT = Formation(
    id=101,
    members=[
        FormationMember(SACKITEnemy, 199, 151),
        FormationMember(SACKITEnemy, 167, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0102_TWO_SACKIT_ONE_MUKUMUKU_ONE_GECKO = Formation(
    id=102,
    members=[
        FormationMember(SACKITEnemy, 151, 127),
        FormationMember(SACKITEnemy, 183, 143),
        FormationMember(MUKUMUKUEnemy, 167, 103),
        FormationMember(GECKOEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0103_ONE_SACKIT_TWO_PULSAR = Formation(
    id=103,
    members=[
        FormationMember(SACKITEnemy, 167, 135),
        None,
        None,
        FormationMember(PULSAREnemy, 167, 103),
        FormationMember(PULSAREnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0104_ONE_SACKIT_ONE_MASTADOOM = Formation(
    id=104,
    members=[
        FormationMember(SACKITEnemy, 215, 143),
        FormationMember(MASTADOOMEnemy, 167, 103),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0105_ONE_GECKO_ONE_SACKIT = Formation(
    id=105,
    members=[
        FormationMember(GECKOEnemy, 151, 119),
        FormationMember(SACKITEnemy, 199, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0106_ONE_GECKO_ONE_MASTADOOM = Formation(
    id=106,
    members=[
        FormationMember(GECKOEnemy, 151, 119),
        FormationMember(MASTADOOMEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0107_TWO_GECKO_TWO_MUKUMUKU_TWO_SACKIT = Formation(
    id=107,
    members=[
        FormationMember(GECKOEnemy, 183, 143),
        FormationMember(GECKOEnemy, 151, 127),
        FormationMember(MUKUMUKUEnemy, 135, 103),
        FormationMember(MUKUMUKUEnemy, 231, 151),
        FormationMember(SACKITEnemy, 183, 111),
        FormationMember(SACKITEnemy, 215, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0108_TWO_GECKO_ONE_MASTADOOM = Formation(
    id=108,
    members=[
        FormationMember(GECKOEnemy, 135, 103),
        FormationMember(GECKOEnemy, 231, 151),
        FormationMember(MASTADOOMEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0109_TWO_ZEOSTAR = Formation(
    id=109,
    members=[
        FormationMember(ZEOSTAREnemy, 135, 119),
        FormationMember(ZEOSTAREnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0110_TWO_ZEOSTAR_ONE_BLOOBER = Formation(
    id=110,
    members=[
        FormationMember(ZEOSTAREnemy, 151, 135),
        FormationMember(ZEOSTAREnemy, 183, 103),
        FormationMember(BLOOBEREnemyStatic, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0111_TWO_ZEOSTAR_TWO_LEUKO = Formation(
    id=111,
    members=[
        FormationMember(ZEOSTAREnemy, 199, 119),
        FormationMember(ZEOSTAREnemy, 167, 135),
        FormationMember(LEUKOEnemy, 167, 103),
        FormationMember(LEUKOEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0112_ONE_ZEOSTAR_ONE_LEUKO_ONE_CRUSTY = Formation(
    id=112,
    members=[
        FormationMember(ZEOSTAREnemy, 183, 127),
        FormationMember(LEUKOEnemy, 215, 143),
        FormationMember(CRUSTYEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0113_ONE_BLOOBER_ONE_MRKIPPER = Formation(
    id=113,
    members=[
        FormationMember(BLOOBEREnemyStatic, 151, 111),
        FormationMember(MRKIPPEREnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0114_THREE_BLOOBER = Formation(
    id=114,
    members=[
        FormationMember(BLOOBEREnemyStatic, 183, 127),
        FormationMember(BLOOBEREnemyStatic, 231, 143),
        FormationMember(BLOOBEREnemyStatic, 135, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0115_TWO_BLOOBER_ONE_MRKIPPER_ONE_CRUSTY = Formation(
    id=115,
    members=[
        FormationMember(BLOOBEREnemyStatic, 151, 111),
        FormationMember(BLOOBEREnemyStatic, 231, 151),
        FormationMember(MRKIPPEREnemy, 151, 143),
        FormationMember(CRUSTYEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0116_TWO_BLOOBER_TWO_ZEOSTAR_ONE_LEUKO = Formation(
    id=116,
    members=[
        FormationMember(BLOOBEREnemyStatic, 231, 135),
        FormationMember(BLOOBEREnemyStatic, 167, 103),
        FormationMember(ZEOSTAREnemy, 135, 127),
        FormationMember(ZEOSTAREnemy, 183, 151),
        FormationMember(LEUKOEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0117_THREE_MRKIPPER = Formation(
    id=117,
    members=[
        FormationMember(MRKIPPEREnemy, 151, 103),
        FormationMember(MRKIPPEREnemy, 215, 151),
        FormationMember(MRKIPPEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0118_TWO_MRKIPPER_ONE_CRUSTY = Formation(
    id=118,
    members=[
        FormationMember(MRKIPPEREnemy, 199, 151),
        FormationMember(MRKIPPEREnemy, 135, 119),
        FormationMember(CRUSTYEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0119_TWO_MRKIPPER_ONE_CRUSTY = Formation(
    id=119,
    members=[
        FormationMember(MRKIPPEREnemy, 135, 119),
        FormationMember(MRKIPPEREnemy, 231, 135),
        FormationMember(CRUSTYEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0120_FOUR_MRKIPPER = Formation(
    id=120,
    members=[
        FormationMember(MRKIPPEREnemy, 215, 127),
        FormationMember(MRKIPPEREnemy, 199, 151),
        FormationMember(MRKIPPEREnemy, 167, 103),
        FormationMember(MRKIPPEREnemy, 151, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0121_FOUR_BANDANARED = Formation(
    id=121,
    members=[
        FormationMember(BANDANAREDEnemyHenchman, 151, 127),
        FormationMember(BANDANAREDEnemyHenchman, 183, 143),
        FormationMember(BANDANAREDEnemyHenchman, 167, 103),
        FormationMember(BANDANAREDEnemyHenchman, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0122_FIVE_BANDANARED = Formation(
    id=122,
    members=[
        FormationMember(BANDANAREDEnemyHenchman, 199, 151),
        FormationMember(BANDANAREDEnemyHenchman, 135, 119),
        FormationMember(BANDANAREDEnemyHenchman, 215, 127),
        FormationMember(BANDANAREDEnemyHenchman, 167, 135),
        FormationMember(BANDANAREDEnemyHenchman, 183, 111),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0123_ONE_BOOSTERENEMY2_THREE_SNIFIT2_ONE_BOOSTERDUMMY = Formation(
    id=123,
    members=[
        FormationMember(BOOSTEREnemy2, 184, 116),
        FormationMember(SNIFIT2Enemy, 156, 132),
        FormationMember(SNIFIT2Enemy, 143, 104),
        FormationMember(SNIFIT2Enemy, 212, 138),
        FormationMember(BOOSTERDUMMY, 0, 0),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0124_ONE_PUNCHINELLO2_ONE_STRONGBOBOMB3_ONE_STRONGBOBOMB1_ONE_STRONGBOBOMB4_ONE_STRONGBOBOMB2 = Formation(
    id=124,
    members=[
        FormationMember(PUNCHINELLO2Enemy, 188, 116),
        FormationMember(STRONGBOBOMB3Enemy, 145, 103, hidden_at_start=True),
        FormationMember(STRONGBOBOMB1Enemy, 150, 129, hidden_at_start=True),
        FormationMember(STRONGBOBOMB4Enemy, 182, 142, hidden_at_start=True),
        FormationMember(STRONGBOBOMB2Enemy, 223, 142, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0125_TWO_DRYBONES = Formation(
    id=125,
    members=[
        FormationMember(DRYBONESEnemy, 199, 151),
        FormationMember(DRYBONESEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0126_TWO_DRYBONES_ONE_GREAPER = Formation(
    id=126,
    members=[
        FormationMember(DRYBONESEnemy, 135, 119),
        FormationMember(DRYBONESEnemy, 199, 151),
        FormationMember(GREAPEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0127_ONE_DRYBONES_ONE_GREAPER_ONE_REACHER = Formation(
    id=127,
    members=[
        FormationMember(DRYBONESEnemy, 135, 119),
        FormationMember(GREAPEREnemy, 199, 151),
        FormationMember(REACHEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0128_TWO_DRYBONES_TWO_GREAPER_ONE_REACHER = Formation(
    id=128,
    members=[
        FormationMember(DRYBONESEnemy, 167, 103),
        FormationMember(DRYBONESEnemy, 231, 135),
        FormationMember(GREAPEREnemy, 151, 127),
        FormationMember(GREAPEREnemy, 183, 143),
        FormationMember(REACHEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0129_ONE_ALLEYRAT_ONE_GORGON = Formation(
    id=129,
    members=[
        FormationMember(ALLEYRATEnemy, 199, 151),
        FormationMember(GORGONEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0130_TWO_ALLEYRAT_TWO_GREAPER = Formation(
    id=130,
    members=[
        FormationMember(ALLEYRATEnemy, 135, 119),
        FormationMember(ALLEYRATEnemy, 199, 151),
        FormationMember(GREAPEREnemy, 215, 127),
        FormationMember(GREAPEREnemy, 183, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0131_TWO_ALLEYRAT_TWO_GORGON = Formation(
    id=131,
    members=[
        FormationMember(ALLEYRATEnemy, 151, 127),
        FormationMember(ALLEYRATEnemy, 199, 151),
        FormationMember(GORGONEnemy, 183, 111),
        FormationMember(GORGONEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0132_ONE_ALLEYRAT_ONE_REACHER_ONE_GORGON = Formation(
    id=132,
    members=[
        FormationMember(ALLEYRATEnemy, 231, 135),
        FormationMember(REACHEREnemy, 167, 135),
        FormationMember(GORGONEnemy, 167, 103),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0133_ONE_GREAPER = Formation(
    id=133,
    members=[
        FormationMember(GREAPEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0134_TWO_GREAPER_ONE_REACHER = Formation(
    id=134,
    members=[
        FormationMember(GREAPEREnemy, 151, 119),
        FormationMember(GREAPEREnemy, 199, 143),
        FormationMember(REACHEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0135_ONE_GREAPER_ONE_STRAWHEAD_ONE_REACHER = Formation(
    id=135,
    members=[
        FormationMember(GREAPEREnemy, 167, 135),
        FormationMember(STRAWHEADEnemy, 215, 135),
        FormationMember(REACHEREnemy, 167, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0136_ONE_GREAPER_ONE_GORGON_TWO_STRAWHEAD = Formation(
    id=136,
    members=[
        FormationMember(GREAPEREnemy, 167, 135),
        FormationMember(GORGONEnemy, 199, 119),
        FormationMember(STRAWHEADEnemy, 215, 143),
        FormationMember(STRAWHEADEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0137_ONE_BUNDT2_ONE_RASPBERRY2_TWO_TORTE2_ONE_CANDLE = Formation(
    id=137,
    members=[
        FormationMember(BUNDT2Enemy, 199, 127),
        FormationMember(RASPBERRY2Enemy, 199, 119),
        FormationMember(TORTE2Enemy, 199, 151),
        FormationMember(TORTE2Enemy, 135, 119),
        FormationMember(CANDLEEnemy, 0, 0),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
    run_event_at_load=BE0017_BEGIN_BUNDT_POSTGAME,
)

FORM0138_THREE_CROOK = Formation(
    id=138,
    members=[
        FormationMember(CROOKEnemyHenchman, 135, 119),
        FormationMember(CROOKEnemyHenchman, 199, 119),
        FormationMember(CROOKEnemyHenchman, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0139_FIVE_CROOK = Formation(
    id=139,
    members=[
        FormationMember(CROOKEnemyHenchman, 167, 103),
        FormationMember(CROOKEnemyHenchman, 135, 119),
        FormationMember(CROOKEnemyHenchman, 183, 127),
        FormationMember(CROOKEnemyHenchman, 199, 151),
        FormationMember(CROOKEnemyHenchman, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0140_ONE_STINGER_ONE_FINKFLOWER = Formation(
    id=140,
    members=[
        FormationMember(STINGEREnemy, 151, 111),
        FormationMember(FINKFLOWEREnemy, 199, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0141_TWO_STINGER_ONE_OCTOVADER = Formation(
    id=141,
    members=[
        FormationMember(STINGEREnemy, 135, 111),
        FormationMember(STINGEREnemy, 215, 151),
        FormationMember(OCTOVADEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0142_ONE_STINGER_TWO_FINKFLOWER = Formation(
    id=142,
    members=[
        FormationMember(STINGEREnemy, 199, 119),
        None,
        FormationMember(FINKFLOWEREnemy, 215, 143),
        FormationMember(FINKFLOWEREnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0143_FOUR_STINGER = Formation(
    id=143,
    members=[
        FormationMember(STINGEREnemy, 183, 111),
        FormationMember(STINGEREnemy, 199, 151),
        FormationMember(STINGEREnemy, 215, 127),
        FormationMember(STINGEREnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0144_ONE_CHOW_ONE_OCTOVADER = Formation(
    id=144,
    members=[
        FormationMember(CHOWEnemy, 135, 119),
        FormationMember(OCTOVADEREnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0145_ONE_CHOW_ONE_SHOGUN = Formation(
    id=145,
    members=[
        FormationMember(CHOWEnemy, 151, 111),
        FormationMember(SHOGUNEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0146_ONE_CHOW_ONE_SHOGUN_ONE_OCTOVADER = Formation(
    id=146,
    members=[
        FormationMember(CHOWEnemy, 199, 151),
        FormationMember(SHOGUNEnemy, 135, 119),
        FormationMember(OCTOVADEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0147_ONE_CHOW_ONE_FINKFLOWER_TWO_SHOGUN = Formation(
    id=147,
    members=[
        FormationMember(CHOWEnemy, 167, 135),
        FormationMember(FINKFLOWEREnemy, 199, 119),
        FormationMember(SHOGUNEnemy, 135, 119),
        FormationMember(SHOGUNEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0148_ONE_CHOMPCHOMP = Formation(
    id=148,
    members=[
        FormationMember(CHOMPCHOMPEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0149_TWO_CHOMPCHOMP = Formation(
    id=149,
    members=[
        FormationMember(CHOMPCHOMPEnemy, 151, 111),
        FormationMember(CHOMPCHOMPEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0150_THREE_CHOMPCHOMP = Formation(
    id=150,
    members=[
        FormationMember(CHOMPCHOMPEnemy, 151, 111),
        FormationMember(CHOMPCHOMPEnemy, 199, 119),
        FormationMember(CHOMPCHOMPEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0151_FOUR_CHOMPCHOMP = Formation(
    id=151,
    members=[
        FormationMember(CHOMPCHOMPEnemy, 135, 119),
        FormationMember(CHOMPCHOMPEnemy, 183, 111),
        FormationMember(CHOMPCHOMPEnemy, 215, 127),
        FormationMember(CHOMPCHOMPEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0152_ONE_SHYAWAY = Formation(
    id=152,
    members=[
        FormationMember(SHYAWAYEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0153_TWO_SHYAWAY_ONE_KRIFFID = Formation(
    id=153,
    members=[
        FormationMember(SHYAWAYEnemy, 151, 111),
        FormationMember(SHYAWAYEnemy, 215, 143),
        FormationMember(KRIFFIDEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0154_TWO_SHYAWAY_ONE_RIBBITE = Formation(
    id=154,
    members=[
        FormationMember(SHYAWAYEnemy, 167, 103),
        FormationMember(SHYAWAYEnemy, 231, 135),
        FormationMember(RIBBITEEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0155_ONE_SHYAWAY_ONE_GECKIT_ONE_RIBBITE = Formation(
    id=155,
    members=[
        FormationMember(SHYAWAYEnemy, 215, 135),
        None,
        FormationMember(GECKITEnemy, 167, 143),
        None,
        FormationMember(RIBBITEEnemy, 167, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0156_TWO_CHEWY = Formation(
    id=156,
    members=[
        FormationMember(CHEWYEnemy, 151, 111),
        FormationMember(CHEWYEnemy, 183, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0157_TWO_CHEWY_ONE_SHYAWAY = Formation(
    id=157,
    members=[
        FormationMember(CHEWYEnemy, 135, 119),
        FormationMember(CHEWYEnemy, 199, 151),
        FormationMember(SHYAWAYEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0158_ONE_CHEWY_ONE_SPINTHRA = Formation(
    id=158,
    members=[
        FormationMember(CHEWYEnemy, 151, 111),
        FormationMember(SPINTHRAEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0159_TWO_CHEWY_TWO_GECKIT_ONE_KRIFFID = Formation(
    id=159,
    members=[
        FormationMember(CHEWYEnemy, 183, 151),
        FormationMember(CHEWYEnemy, 135, 127),
        FormationMember(GECKITEnemy, 231, 143),
        FormationMember(GECKITEnemy, 151, 103),
        FormationMember(KRIFFIDEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0160_ONE_GECKIT_ONE_SPINTHRA = Formation(
    id=160,
    members=[
        FormationMember(GECKITEnemy, 199, 151),
        FormationMember(SPINTHRAEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0161_TWO_GECKIT_ONE_SPINTHRA = Formation(
    id=161,
    members=[
        FormationMember(GECKITEnemy, 183, 135),
        FormationMember(GECKITEnemy, 215, 151),
        FormationMember(SPINTHRAEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0162_TWO_GECKIT_TWO_CHEWY_ONE_SHYAWAY = Formation(
    id=162,
    members=[
        FormationMember(GECKITEnemy, 151, 127),
        FormationMember(GECKITEnemy, 183, 143),
        FormationMember(CHEWYEnemy, 167, 103),
        FormationMember(CHEWYEnemy, 231, 135),
        FormationMember(SHYAWAYEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0163_TWO_GECKIT_ONE_SPINTHRA_ONE_KRIFFID = Formation(
    id=163,
    members=[
        FormationMember(GECKITEnemy, 151, 127),
        FormationMember(GECKITEnemy, 183, 143),
        FormationMember(SPINTHRAEnemy, 151, 103),
        FormationMember(KRIFFIDEnemy, 231, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0164_ONE_BIRDY_ONE_HEAVYTROOPA = Formation(
    id=164,
    members=[
        FormationMember(BIRDYEnemyStatic, 135, 119),
        FormationMember(HEAVYTROOPAEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0165_THREE_BIRDY = Formation(
    id=165,
    members=[
        FormationMember(BIRDYEnemyStatic, 215, 119),
        FormationMember(BIRDYEnemyStatic, 151, 119),
        FormationMember(BIRDYEnemyStatic, 183, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0166_TWO_BIRDY_ONE_HEAVYTROOPA = Formation(
    id=166,
    members=[
        FormationMember(BIRDYEnemyStatic, 199, 151),
        FormationMember(BIRDYEnemyStatic, 135, 119),
        FormationMember(HEAVYTROOPAEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0167_FIVE_BIRDY = Formation(
    id=167,
    members=[
        FormationMember(BIRDYEnemyStatic, 151, 111),
        FormationMember(BIRDYEnemyStatic, 215, 143),
        FormationMember(BIRDYEnemyStatic, 151, 143),
        FormationMember(BIRDYEnemyStatic, 215, 111),
        FormationMember(BIRDYEnemyStatic, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0168_TWO_BLUEBIRD = Formation(
    id=168,
    members=[
        FormationMember(BLUEBIRDEnemyStatic, 199, 151),
        FormationMember(BLUEBIRDEnemyStatic, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0169_TWO_BLUEBIRD_ONE_HEAVYTROOPA = Formation(
    id=169,
    members=[
        FormationMember(BLUEBIRDEnemyStatic, 167, 103),
        FormationMember(BLUEBIRDEnemyStatic, 231, 135),
        FormationMember(HEAVYTROOPAEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0170_FOUR_BLUEBIRD = Formation(
    id=170,
    members=[
        FormationMember(BLUEBIRDEnemyStatic, 183, 143),
        FormationMember(BLUEBIRDEnemyStatic, 183, 111),
        FormationMember(BLUEBIRDEnemyStatic, 231, 135),
        FormationMember(BLUEBIRDEnemyStatic, 135, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0171_TWO_BLUEBIRD_ONE_HEAVYTROOPA = Formation(
    id=171,
    members=[
        FormationMember(BLUEBIRDEnemyStatic, 151, 111),
        FormationMember(BLUEBIRDEnemyStatic, 215, 143),
        None,
        None,
        FormationMember(HEAVYTROOPAEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0172_ONE_PINWHEEL = Formation(
    id=172,
    members=[
        FormationMember(PINWHEELEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0173_ONE_PINWHEEL_ONE_MUCKLE = Formation(
    id=173,
    members=[
        FormationMember(PINWHEELEnemy, 135, 119),
        FormationMember(MUCKLEEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0174_TWO_PINWHEEL_TWO_MUCKLE = Formation(
    id=174,
    members=[
        FormationMember(PINWHEELEnemy, 151, 127),
        FormationMember(PINWHEELEnemy, 183, 143),
        FormationMember(MUCKLEEnemy, 151, 103),
        FormationMember(MUCKLEEnemy, 231, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0175_THREE_PINWHEEL_TWO_SLINGSHY = Formation(
    id=175,
    members=[
        FormationMember(PINWHEELEnemy, 151, 143),
        FormationMember(PINWHEELEnemy, 135, 119),
        FormationMember(PINWHEELEnemy, 199, 151),
        FormationMember(SLINGSHYEnemy, 167, 111),
        FormationMember(SLINGSHYEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0176_TWO_SHAMAN = Formation(
    id=176,
    members=[
        FormationMember(SHAMANEnemy, 151, 111),
        FormationMember(SHAMANEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0177_ONE_SHAMAN_ONE_ORBISON_ONE_JAWFUL = Formation(
    id=177,
    members=[
        FormationMember(SHAMANEnemy, 135, 119),
        FormationMember(ORBISONEnemy, 199, 151),
        FormationMember(JAWFULEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0178_TWO_SHAMAN_ONE_JAWFUL = Formation(
    id=178,
    members=[
        FormationMember(SHAMANEnemy, 167, 103),
        FormationMember(SHAMANEnemy, 231, 135),
        FormationMember(JAWFULEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0179_TWO_SHAMAN_TWO_SLINGSHY_ONE_JAWFUL = Formation(
    id=179,
    members=[
        FormationMember(SHAMANEnemy, 167, 103),
        FormationMember(SHAMANEnemy, 231, 135),
        FormationMember(SLINGSHYEnemy, 135, 127),
        FormationMember(SLINGSHYEnemy, 183, 151),
        FormationMember(JAWFULEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0180_ONE_SLINGSHY_ONE_ORBISON = Formation(
    id=180,
    members=[
        FormationMember(SLINGSHYEnemy, 135, 119),
        FormationMember(ORBISONEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0181_ONE_SLINGSHY_TWO_ORBISON = Formation(
    id=181,
    members=[
        FormationMember(SLINGSHYEnemy, 183, 127),
        FormationMember(ORBISONEnemy, 151, 111),
        FormationMember(ORBISONEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0182_ONE_SLINGSHY_TWO_ORBISON_ONE_JAWFUL = Formation(
    id=182,
    members=[
        FormationMember(SLINGSHYEnemy, 167, 135),
        FormationMember(ORBISONEnemy, 151, 111),
        FormationMember(ORBISONEnemy, 215, 143),
        FormationMember(JAWFULEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0183_TWO_SLINGSHY_TWO_PINWHEEL_ONE_MUCKLE = Formation(
    id=183,
    members=[
        FormationMember(SLINGSHYEnemy, 183, 143),
        FormationMember(SLINGSHYEnemy, 151, 127),
        FormationMember(PINWHEELEnemy, 151, 111),
        FormationMember(PINWHEELEnemy, 215, 143),
        FormationMember(MUCKLEEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0184_ONE_MAGMUS = Formation(
    id=184,
    members=[
        FormationMember(MAGMUSEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0185_TWO_MAGMUS_ONE_ARMOREDANT = Formation(
    id=185,
    members=[
        FormationMember(MAGMUSEnemy, 151, 111),
        FormationMember(MAGMUSEnemy, 215, 143),
        FormationMember(ARMOREDANTEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0186_THREE_MAGMUS_TWO_OERLIKON = Formation(
    id=186,
    members=[
        FormationMember(MAGMUSEnemy, 151, 103),
        FormationMember(MAGMUSEnemy, 231, 143),
        FormationMember(MAGMUSEnemy, 199, 119),
        FormationMember(OERLIKONEnemy, 151, 127),
        FormationMember(OERLIKONEnemy, 183, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0187_TWO_MAGMUS_TWO_ARMOREDANT = Formation(
    id=187,
    members=[
        FormationMember(MAGMUSEnemy, 119, 119),
        FormationMember(MAGMUSEnemy, 167, 143),
        FormationMember(ARMOREDANTEnemy, 167, 111),
        FormationMember(ARMOREDANTEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0188_ONE_OERLIKON_ONE_VOMER = Formation(
    id=188,
    members=[
        FormationMember(OERLIKONEnemy, 135, 119),
        FormationMember(VOMEREnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0189_THREE_OERLIKON = Formation(
    id=189,
    members=[
        FormationMember(OERLIKONEnemy, 183, 127),
        FormationMember(OERLIKONEnemy, 135, 119),
        FormationMember(OERLIKONEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0190_ONE_OERLIKON_ONE_CHAINEDKONG_ONE_ARMOREDANT = Formation(
    id=190,
    members=[
        FormationMember(OERLIKONEnemy, 215, 151),
        FormationMember(CHAINEDKONGEnemy, 183, 127),
        FormationMember(ARMOREDANTEnemy, 135, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0191_TWO_OERLIKON_ONE_CHAINEDKONG = Formation(
    id=191,
    members=[
        FormationMember(OERLIKONEnemy, 135, 127),
        FormationMember(OERLIKONEnemy, 183, 151),
        FormationMember(CHAINEDKONGEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0192_THREE_PYROSPHERE = Formation(
    id=192,
    members=[
        FormationMember(PYROSPHEREEnemy, 151, 135),
        FormationMember(PYROSPHEREEnemy, 215, 135),
        FormationMember(PYROSPHEREEnemy, 183, 103),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0193_TWO_PYROSPHERE_ONE_CHAINEDKONG = Formation(
    id=193,
    members=[
        FormationMember(PYROSPHEREEnemy, 199, 143),
        FormationMember(PYROSPHEREEnemy, 151, 119),
        FormationMember(CHAINEDKONGEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0194_ONE_CORKPEDITE_ONE_BODY_ONE_PYROSPHERE = Formation(
    id=194,
    members=[
        FormationMember(CORKPEDITEEnemy, 135, 119),
        FormationMember(BODYEnemy, 151, 111),
        FormationMember(PYROSPHEREEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0195_TWO_PYROSPHERE_ONE_STUMPET = Formation(
    id=195,
    members=[
        FormationMember(PYROSPHEREEnemy, 199, 151),
        FormationMember(PYROSPHEREEnemy, 199, 119),
        FormationMember(STUMPETEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0196_ONE_VOMER_ONE_CHAINEDKONG = Formation(
    id=196,
    members=[
        FormationMember(VOMEREnemy, 151, 111),
        FormationMember(CHAINEDKONGEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0197_THREE_VOMER = Formation(
    id=197,
    members=[
        FormationMember(VOMEREnemy, 151, 103),
        FormationMember(VOMEREnemy, 183, 127),
        FormationMember(VOMEREnemy, 215, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0198_ONE_CORKPEDITE_ONE_BODY_ONE_VOMER = Formation(
    id=198,
    members=[
        FormationMember(CORKPEDITEEnemy, 199, 151),
        FormationMember(BODYEnemy, 215, 143),
        FormationMember(VOMEREnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0199_TWO_VOMER_ONE_STUMPET = Formation(
    id=199,
    members=[
        FormationMember(VOMEREnemy, 151, 135),
        FormationMember(VOMEREnemy, 151, 103),
        FormationMember(STUMPETEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0200_ONE_TERRACOTTA = Formation(
    id=200,
    members=[
        FormationMember(TERRACOTTAEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0201_THREE_TERRACOTTA = Formation(
    id=201,
    members=[
        FormationMember(TERRACOTTAEnemy, 183, 151),
        FormationMember(TERRACOTTAEnemy, 151, 119),
        FormationMember(TERRACOTTAEnemy, 215, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0202_ONE_TERRACOTTA_TWO_FORKIES = Formation(
    id=202,
    members=[
        FormationMember(TERRACOTTAEnemy, 183, 127),
        FormationMember(FORKIESEnemy, 151, 111),
        FormationMember(FORKIESEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0203_TWO_TERRACOTTA_TWO_GUGOOMBA_ONE_FORKIES = Formation(
    id=203,
    members=[
        FormationMember(TERRACOTTAEnemy, 135, 127),
        FormationMember(TERRACOTTAEnemy, 183, 151),
        FormationMember(GUGOOMBAEnemy, 231, 135),
        FormationMember(GUGOOMBAEnemy, 167, 103),
        FormationMember(FORKIESEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0204_ONE_MALAKOOPA_ONE_TUBOTROOPA = Formation(
    id=204,
    members=[
        FormationMember(MALAKOOPAEnemy, 135, 127),
        FormationMember(TUBOTROOPAEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0205_TWO_MALAKOOPA_ONE_TUBOTROOPA = Formation(
    id=205,
    members=[
        FormationMember(MALAKOOPAEnemy, 135, 119),
        FormationMember(MALAKOOPAEnemy, 199, 151),
        FormationMember(TUBOTROOPAEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0206_TWO_MALAKOOPA_ONE_TERRACOTTA_ONE_TUBOTROOPA = Formation(
    id=206,
    members=[
        FormationMember(MALAKOOPAEnemy, 135, 103),
        FormationMember(MALAKOOPAEnemy, 231, 151),
        FormationMember(TERRACOTTAEnemy, 167, 135),
        FormationMember(TUBOTROOPAEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0207_ONE_MALAKOOPA_TWO_TUBOTROOPA = Formation(
    id=207,
    members=[
        FormationMember(MALAKOOPAEnemy, 183, 127),
        None,
        None,
        FormationMember(TUBOTROOPAEnemy, 135, 103),
        FormationMember(TUBOTROOPAEnemy, 231, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0208_TWO_GUGOOMBA = Formation(
    id=208,
    members=[
        FormationMember(GUGOOMBAEnemy, 151, 111),
        FormationMember(GUGOOMBAEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0209_TWO_GUGOOMBA_ONE_STARCRUSTER = Formation(
    id=209,
    members=[
        FormationMember(GUGOOMBAEnemy, 231, 151),
        FormationMember(GUGOOMBAEnemy, 135, 103),
        FormationMember(STARCRUSTEREnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0210_ONE_GUGOOMBA_ONE_FORKIES_ONE_STARCRUSTER = Formation(
    id=210,
    members=[
        FormationMember(GUGOOMBAEnemy, 231, 143),
        FormationMember(FORKIESEnemy, 199, 119),
        FormationMember(STARCRUSTEREnemy, 151, 103),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0211_TWO_GUGOOMBA_TWO_MALAKOOPA_TWO_TERRACOTTA = Formation(
    id=211,
    members=[
        FormationMember(GUGOOMBAEnemy, 199, 151),
        FormationMember(GUGOOMBAEnemy, 135, 119),
        FormationMember(MALAKOOPAEnemy, 167, 135),
        FormationMember(MALAKOOPAEnemy, 199, 119),
        FormationMember(TERRACOTTAEnemy, 167, 103),
        FormationMember(TERRACOTTAEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0212_ONE_BIGBERTHA = Formation(
    id=212,
    members=[
        FormationMember(BIGBERTHAEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0213_TWO_BIGBERTHA = Formation(
    id=213,
    members=[
        FormationMember(BIGBERTHAEnemy, 151, 111),
        FormationMember(BIGBERTHAEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0214_ONE_BIGBERTHA_ONE_FORKIES = Formation(
    id=214,
    members=[
        FormationMember(BIGBERTHAEnemy, 215, 143),
        FormationMember(FORKIESEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0215_TWO_BIGBERTHA_ONE_TERRACOTTA = Formation(
    id=215,
    members=[
        FormationMember(BIGBERTHAEnemy, 135, 111),
        FormationMember(BIGBERTHAEnemy, 215, 151),
        FormationMember(TERRACOTTAEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0216_ONE_JOHNNYENEMY2 = Formation(
    id=216,
    members=[
        FormationMember(JOHNNYEnemy2, 165, 121),
        FormationMember(WATERCRYSTALEnemy, 0, 0, hidden_at_start=True),
        FormationMember(WATERCRYSTALEnemy, 0, 0, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0217_ONE_JINXENEMY4_ONE_TEAMGAUGE = Formation(
    id=217,
    members=[
        FormationMember(JINXEnemy4, 181, 122),
        FormationMember(TeamGaugeEnemy, 36, 200),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0218_ONE_NINJA = Formation(
    id=218,
    members=[
        FormationMember(NINJAEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0219_ONE_NINJA_ONE_DOPPEL = Formation(
    id=219,
    members=[
        FormationMember(NINJAEnemy, 151, 119),
        FormationMember(DOPPELEnemy, 199, 159),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0220_TWO_NINJA_ONE_HIPPOPO = Formation(
    id=220,
    members=[
        FormationMember(NINJAEnemy, 199, 151),
        FormationMember(NINJAEnemy, 135, 119),
        FormationMember(HIPPOPOEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0221_FIVE_NINJA = Formation(
    id=221,
    members=[
        FormationMember(NINJAEnemy, 135, 119),
        FormationMember(NINJAEnemy, 183, 127),
        FormationMember(NINJAEnemy, 167, 103),
        FormationMember(NINJAEnemy, 231, 135),
        FormationMember(NINJAEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0222_ONE_SPRINGER_ONE_GLUMREAPER = Formation(
    id=222,
    members=[
        FormationMember(SPRINGEREnemy, 215, 143),
        FormationMember(GLUMREAPEREnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0223_TWO_SPRINGER_ONE_PUPPOX = Formation(
    id=223,
    members=[
        FormationMember(SPRINGEREnemy, 231, 135),
        FormationMember(SPRINGEREnemy, 167, 103),
        FormationMember(PUPPOXEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0224_ONE_SPRINGER_TWO_PUPPOX = Formation(
    id=224,
    members=[
        FormationMember(SPRINGEREnemy, 183, 127),
        FormationMember(PUPPOXEnemy, 215, 143),
        FormationMember(PUPPOXEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0225_TWO_MADMALLET = Formation(
    id=225,
    members=[
        FormationMember(MADMALLETEnemyStatic, 151, 119),
        FormationMember(MADMALLETEnemyStatic, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0226_THREE_MADMALLET = Formation(
    id=226,
    members=[
        FormationMember(MADMALLETEnemyStatic, 151, 127),
        FormationMember(MADMALLETEnemyStatic, 199, 151),
        FormationMember(MADMALLETEnemyStatic, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0227_FIVE_MADMALLET = Formation(
    id=227,
    members=[
        FormationMember(MADMALLETEnemyStatic, 183, 127),
        FormationMember(MADMALLETEnemyStatic, 135, 127),
        FormationMember(MADMALLETEnemyStatic, 231, 135),
        FormationMember(MADMALLETEnemyStatic, 167, 103),
        FormationMember(MADMALLETEnemyStatic, 183, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0228_ONE_POUNDER = Formation(
    id=228,
    members=[
        FormationMember(POUNDEREnemyStatic, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0229_THREE_POUNDER = Formation(
    id=229,
    members=[
        FormationMember(POUNDEREnemyStatic, 183, 127),
        FormationMember(POUNDEREnemyStatic, 231, 135),
        FormationMember(POUNDEREnemyStatic, 167, 103),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0230_FIVE_POUNDER = Formation(
    id=230,
    members=[
        FormationMember(POUNDEREnemyStatic, 167, 135),
        FormationMember(POUNDEREnemyStatic, 199, 143),
        FormationMember(POUNDEREnemyStatic, 151, 119),
        FormationMember(POUNDEREnemyStatic, 167, 103),
        FormationMember(POUNDEREnemyStatic, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0231_ONE_POUNDETTE = Formation(
    id=231,
    members=[
        FormationMember(POUNDETTEEnemyStatic, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0232_THREE_POUNDETTE = Formation(
    id=232,
    members=[
        FormationMember(POUNDETTEEnemyStatic, 183, 127),
        FormationMember(POUNDETTEEnemyStatic, 151, 111),
        FormationMember(POUNDETTEEnemyStatic, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0233_SIX_POUNDETTE = Formation(
    id=233,
    members=[
        FormationMember(POUNDETTEEnemyStatic, 167, 135),
        FormationMember(POUNDETTEEnemyStatic, 199, 119),
        FormationMember(POUNDETTEEnemyStatic, 135, 119),
        FormationMember(POUNDETTEEnemyStatic, 167, 103),
        FormationMember(POUNDETTEEnemyStatic, 199, 151),
        FormationMember(POUNDETTEEnemyStatic, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0234_FIVE_AMEBOID = Formation(
    id=234,
    members=[
        FormationMember(AMEBOIDEnemy, 183, 127),
        FormationMember(AMEBOIDEnemy, 167, 103, hidden_at_start=True),
        FormationMember(AMEBOIDEnemy, 135, 119, hidden_at_start=True),
        FormationMember(AMEBOIDEnemy, 231, 135, hidden_at_start=True),
        FormationMember(AMEBOIDEnemy, 199, 151, hidden_at_start=True),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0235_THREE_GLUMREAPER = Formation(
    id=235,
    members=[
        FormationMember(GLUMREAPEREnemy, 183, 127),
        FormationMember(GLUMREAPEREnemy, 135, 119),
        FormationMember(GLUMREAPEREnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0236_ONE_GLUMREAPER_ONE_HIPPOPO = Formation(
    id=236,
    members=[
        FormationMember(GLUMREAPEREnemy, 215, 159),
        FormationMember(HIPPOPOEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0237_TWO_GLUMREAPER_TWO_DOPPEL = Formation(
    id=237,
    members=[
        FormationMember(GLUMREAPEREnemy, 151, 127),
        FormationMember(GLUMREAPEREnemy, 183, 143),
        FormationMember(DOPPELEnemy, 167, 103),
        FormationMember(DOPPELEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0238_TWO_GLUMREAPER_TWO_LILBOO = Formation(
    id=238,
    members=[
        FormationMember(GLUMREAPEREnemy, 135, 111),
        FormationMember(GLUMREAPEREnemy, 215, 151),
        FormationMember(LILBOOEnemy, 167, 135),
        FormationMember(LILBOOEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0239_ONE_LILBOO = Formation(
    id=239,
    members=[
        FormationMember(LILBOOEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0240_TWO_LILBOO_ONE_HIPPOPO = Formation(
    id=240,
    members=[
        FormationMember(LILBOOEnemy, 183, 151),
        FormationMember(LILBOOEnemy, 215, 135),
        FormationMember(HIPPOPOEnemy, 151, 111),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0241_TWO_LILBOO_ONE_PUPPOX_ONE_DOPPEL = Formation(
    id=241,
    members=[
        FormationMember(LILBOOEnemy, 167, 143),
        FormationMember(LILBOOEnemy, 199, 119),
        FormationMember(PUPPOXEnemy, 151, 103),
        FormationMember(DOPPELEnemy, 215, 159),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0242_FOUR_LILBOO = Formation(
    id=242,
    members=[
        FormationMember(LILBOOEnemy, 167, 135),
        FormationMember(LILBOOEnemy, 151, 111),
        FormationMember(LILBOOEnemy, 215, 143),
        FormationMember(LILBOOEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0243_ONE_JABIT_ONE_MADMALLET = Formation(
    id=243,
    members=[
        FormationMember(JABITEnemy, 215, 135),
        FormationMember(MADMALLETEnemyStatic, 151, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0244_ONE_JABIT_ONE_POUNDER_ONE_POUNDETTE = Formation(
    id=244,
    members=[
        FormationMember(JABITEnemy, 151, 143),
        FormationMember(POUNDEREnemyStatic, 151, 111),
        FormationMember(POUNDETTEEnemyStatic, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0245_SIX_JABIT = Formation(
    id=245,
    members=[
        FormationMember(JABITEnemy, 135, 119),
        FormationMember(JABITEnemy, 167, 135),
        FormationMember(JABITEnemy, 231, 135),
        FormationMember(JABITEnemy, 167, 103),
        FormationMember(JABITEnemy, 199, 119),
        FormationMember(JABITEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0246_TWO_JABIT_TWO_MADMALLET_TWO_POUNDETTE = Formation(
    id=246,
    members=[
        FormationMember(JABITEnemy, 151, 127),
        FormationMember(JABITEnemy, 183, 143),
        FormationMember(MADMALLETEnemyStatic, 135, 103),
        FormationMember(MADMALLETEnemyStatic, 183, 111),
        FormationMember(POUNDETTEEnemyStatic, 215, 127),
        FormationMember(POUNDETTEEnemyStatic, 231, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0247_THREE_RATFUNK = Formation(
    id=247,
    members=[
        FormationMember(RATFUNKEnemy, 135, 119),
        FormationMember(RATFUNKEnemy, 199, 151),
        FormationMember(RATFUNKEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0248_FIVE_RATFUNK = Formation(
    id=248,
    members=[
        FormationMember(RATFUNKEnemy, 135, 127),
        FormationMember(RATFUNKEnemy, 167, 103),
        FormationMember(RATFUNKEnemy, 183, 151),
        FormationMember(RATFUNKEnemy, 231, 135),
        FormationMember(RATFUNKEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0249_ONE_ARTICHOKER = Formation(
    id=249,
    members=[
        FormationMember(ARTICHOKEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0250_TWO_ARTICHOKER = Formation(
    id=250,
    members=[
        FormationMember(ARTICHOKEREnemy, 151, 119),
        FormationMember(ARTICHOKEREnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0251_ONE_PUNCHINELLO_FOUR_MICROBOMB = Formation(
    id=251,
    members=[
        FormationMember(PUNCHINELLOEnemy, 199, 119),
        FormationMember(MICROBOMBEnemy, 135, 119, hidden_at_start=True),
        FormationMember(MICROBOMBEnemy, 151, 135, hidden_at_start=True),
        FormationMember(MICROBOMBEnemy, 183, 151, hidden_at_start=True),
        FormationMember(MICROBOMBEnemy, 215, 159, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0252_TWO_FIREBALL = Formation(
    id=252,
    members=[
        FormationMember(FIREBALLEnemy, 151, 111),
        FormationMember(FIREBALLEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0253_THREE_FIREBALL = Formation(
    id=253,
    members=[
        FormationMember(FIREBALLEnemy, 167, 135),
        FormationMember(FIREBALLEnemy, 167, 111),
        FormationMember(FIREBALLEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0254_ONE_STUMPET_TWO_MAGMUS = Formation(
    id=254,
    members=[
        FormationMember(STUMPETEnemy, 183, 127),
        FormationMember(MAGMUSEnemy, 119, 127),
        FormationMember(MAGMUSEnemy, 183, 159),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0255_ONE_STUMPET_THREE_MAGMUS = Formation(
    id=255,
    members=[
        FormationMember(STUMPETEnemy, 151, 111),
        FormationMember(MAGMUSEnemy, 183, 159),
        FormationMember(MAGMUSEnemy, 199, 135),
        FormationMember(MAGMUSEnemy, 231, 159),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0256_ONE_CORKPEDITE_ONE_BODY_ONE_OERLIKON = Formation(
    id=256,
    members=[
        FormationMember(CORKPEDITEEnemy, 151, 111),
        FormationMember(BODYEnemy, 167, 103),
        FormationMember(OERLIKONEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0257_ONE_CORKPEDITE_ONE_BODY_TWO_OERLIKON = Formation(
    id=257,
    members=[
        FormationMember(CORKPEDITEEnemy, 151, 111),
        FormationMember(BODYEnemy, 167, 103),
        FormationMember(OERLIKONEnemy, 183, 159),
        FormationMember(OERLIKONEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0258_ONE_CLERK_TWO_MADMALLETENEMYHENCHMAN = Formation(
    id=258,
    members=[
        FormationMember(CLERKEnemy, 199, 119),
        FormationMember(MADMALLETEnemyHenchman, 135, 119),
        FormationMember(MADMALLETEnemyHenchman, 199, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0259_ONE_MANAGER_THREE_POUNDERENEMYHENCHMAN = Formation(
    id=259,
    members=[
        FormationMember(MANAGEREnemy, 199, 119),
        FormationMember(POUNDEREnemyHenchman, 151, 111),
        FormationMember(POUNDEREnemyHenchman, 167, 135),
        FormationMember(POUNDEREnemyHenchman, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0260_ONE_DIRECTOR_FOUR_POUNDETTEENEMYHENCHMAN = Formation(
    id=260,
    members=[
        FormationMember(DIRECTOREnemy, 183, 127),
        FormationMember(POUNDETTEEnemyHenchman, 135, 119),
        FormationMember(POUNDETTEEnemyHenchman, 167, 103),
        FormationMember(POUNDETTEEnemyHenchman, 199, 151),
        FormationMember(POUNDETTEEnemyHenchman, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0261_ONE_GUNYOLK_ONE_FACTORYCHIEF = Formation(
    id=261,
    members=[
        FormationMember(GUNYOLKEnemy, 199, 103),
        FormationMember(FACTORYCHIEFEnemy, 231, 151),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0262_THREE_MADMALLETENEMYHENCHMAN = Formation(
    id=262,
    members=[
        FormationMember(MADMALLETEnemyHenchman, 151, 111),
        FormationMember(MADMALLETEnemyHenchman, 167, 135),
        FormationMember(MADMALLETEnemyHenchman, 215, 143),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0263_ONE_APPRENTICE = Formation(
    id=263,
    members=[
        FormationMember(APPRENTICEEnemyStatic, 183, 127),
    ],
    music=NormalBattleMusic(),
)

FORM0264_THREE_MACHINEMADEDRILLBIT = Formation(
    id=264,
    members=[
        FormationMember(MACHINEMADEDrillbitEnemy, 183, 127),
        FormationMember(MACHINEMADEDrillbitEnemy, 167, 103),
        FormationMember(MACHINEMADEDrillbitEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0265_ONE_SHYGUY = Formation(
    id=265,
    members=[
        FormationMember(SHYGUYEnemyStatic, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0266_ONE_PANDORITE = Formation(
    id=266,
    members=[
        FormationMember(PANDORITEEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0267_ONE_HIDON_FOUR_GOOMBETTE = Formation(
    id=267,
    members=[
        FormationMember(HIDONEnemy, 167, 119),
        FormationMember(GOOMBETTEEnemy, 135, 111, hidden_at_start=True),
        FormationMember(GOOMBETTEEnemy, 135, 135, hidden_at_start=True),
        FormationMember(GOOMBETTEEnemy, 167, 151, hidden_at_start=True),
        FormationMember(GOOMBETTEEnemy, 215, 151, hidden_at_start=True),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0268_ONE_BOXBOY_ONE_FAUTSO = Formation(
    id=268,
    members=[
        FormationMember(BOXBOYEnemy, 183, 127),
        FormationMember(FAUTSOEnemy, 151, 111, hidden_at_start=True),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0269_ONE_CHESTER_ONE_BAHAMUTTENEMY2 = Formation(
    id=269,
    members=[
        FormationMember(CHESTEREnemy, 183, 127),
        FormationMember(BAHAMUTTEnemy2, 135, 119, hidden_at_start=True),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0270_TWO_AERO = Formation(
    id=270,
    members=[
        FormationMember(AEROEnemy, 167, 119),
        FormationMember(AEROEnemy, 199, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0271_ONE_BOOSTER_THREE_SNIFITENEMYHENCHMAN = Formation(
    id=271,
    members=[
        FormationMember(BOOSTEREnemy, 183, 127),
        FormationMember(SNIFITEnemyHenchman, 135, 119),
        FormationMember(SNIFITEnemyHenchman, 151, 143),
        FormationMember(SNIFITEnemyHenchman, 199, 151),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
    run_event_at_load=BE0012_DIALOGUE_FROM_BOOSTER_FIGHT,
)

FORM0272_ONE_BOOSTERENEMY2 = Formation(
    id=272,
    members=[
        FormationMember(BOOSTEREnemy2, 183, 127),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0273_ONE_CROCO1 = Formation(
    id=273,
    members=[
        FormationMember(CROCO1Enemy, 183, 127),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0274_ONE_CROCO2 = Formation(
    id=274,
    members=[
        FormationMember(CROCO2Enemy, 183, 127),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0275_ONE_MACHINEMADEAXEMBLACK = Formation(
    id=275,
    members=[
        FormationMember(MACHINEMADEAxemBlackEnemy, 183, 127),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0276_ONE_JOHNNY_FOUR_BANDANABLUE_TWO_WATERCRYSTAL = Formation(
    id=276,
    members=[
        FormationMember(JOHNNYEnemy, 183, 127),
        FormationMember(BANDANABLUEEnemy, 135, 111),
        FormationMember(BANDANABLUEEnemy, 135, 135),
        FormationMember(BANDANABLUEEnemy, 183, 159),
        FormationMember(BANDANABLUEEnemy, 215, 151),
        FormationMember(WATERCRYSTALEnemy, 0, 0, hidden_at_start=True),
        FormationMember(WATERCRYSTALEnemy, 0, 0, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0277_ONE_KINGCALAMARI_TWO_TENTACLESENEMY2_THREE_TENTACLES = Formation(
    id=277,
    members=[
        FormationMember(KINGCALAMARIEnemy, 222, 94, hidden_at_start=True),
        FormationMember(TENTACLESEnemy2, 136, 115, hidden_at_start=True),
        FormationMember(TENTACLESEnemy2, 112, 127, hidden_at_start=True),
        FormationMember(TENTACLESEnemy, 193, 143, hidden_at_start=True),
        FormationMember(TENTACLESEnemy, 168, 156, hidden_at_start=True),
        FormationMember(TENTACLESEnemy, 135, 143, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
    run_event_at_load=BE0026_INTRO_SCENE_TENTACLES_RISE_FROM_HOLES,
)

FORM0278_ONE_BELOME1 = Formation(
    id=278,
    members=[
        FormationMember(BELOME1Enemy, 183, 127),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0279_ONE_BELOME2_ONE_MARIOCLONE_ONE_TOADSTOOL2 = Formation(
    id=279,
    members=[
        FormationMember(BELOME2Enemy, 183, 127),
        FormationMember(MARIOCLONEEnemy, 135, 119, hidden_at_start=True),
        FormationMember(TOADSTOOL2Enemy, 215, 159, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0280_ONE_TERRAPIN = Formation(
    id=280,
    members=[
        FormationMember(TERRAPINEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0281_ONE_VALENTINA_ONE_DODO = Formation(
    id=281,
    members=[
        FormationMember(VALENTINAEnemy, 183, 127),
        FormationMember(DODOEnemy, 199, 151, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0282_ONE_CZARDRAGON_ONE_ZOMBONE_FOUR_HELIO = Formation(
    id=282,
    members=[
        FormationMember(CZARDRAGONEnemy, 183, 143),
        FormationMember(ZOMBONEEnemy, 183, 143, hidden_at_start=True),
        FormationMember(HELIOEnemy, 167, 119, hidden_at_start=True),
        FormationMember(HELIOEnemy, 135, 135, hidden_at_start=True),
        FormationMember(HELIOEnemy, 199, 167, hidden_at_start=True),
        FormationMember(HELIOEnemy, 231, 151, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0283_FIVE_SMILAX_ONE_MEGASMILAX = Formation(
    id=283,
    members=[
        FormationMember(SMILAXEnemy, 180, 157),
        FormationMember(SMILAXEnemy, 164, 175, hidden_at_start=True),
        FormationMember(SMILAXEnemy, 143, 119, hidden_at_start=True),
        FormationMember(SMILAXEnemy, 207, 151, hidden_at_start=True),
        FormationMember(SMILAXEnemy, 191, 127, hidden_at_start=True),
        FormationMember(MEGASMILAXEnemy, 175, 111, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
    run_event_at_load=BE0058_THRAX_IS_THERE,
)

FORM0284_ONE_COUNTDOWN_TWO_DINGALING = Formation(
    id=284,
    members=[
        FormationMember(COUNTDOWNEnemy, 150, 93),
        FormationMember(DINGALINGEnemy, 158, 52),
        FormationMember(DINGALINGEnemy, 194, 67),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0285_ONE_BIRDETTA_ONE_SHELLY_FOUR_EGGBERT = Formation(
    id=285,
    members=[
        FormationMember(BIRDETTAEnemy, 167, 118, hidden_at_start=True),
        FormationMember(SHELLYEnemy, 171, 103),
        FormationMember(EGGBERTEnemy, 135, 119, hidden_at_start=True),
        FormationMember(EGGBERTEnemy, 135, 135, hidden_at_start=True),
        FormationMember(EGGBERTEnemy, 167, 151, hidden_at_start=True),
        FormationMember(EGGBERTEnemy, 199, 151, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0286_ONE_BUNDT_ONE_RASPBERRY_TWO_TORTE = Formation(
    id=286,
    members=[
        FormationMember(BUNDTEnemy, 199, 127),
        FormationMember(RASPBERRYEnemy, 199, 119),
        FormationMember(TORTEEnemy, 199, 151),
        FormationMember(TORTEEnemy, 135, 119),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0287_ONE_KNIFEGUY_ONE_GRATEGUY = Formation(
    id=287,
    members=[
        FormationMember(KNIFEGUYEnemy, 151, 119),
        FormationMember(GRATEGUYEnemy, 199, 143),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0288_ONE_JINX1 = Formation(
    id=288,
    members=[
        FormationMember(JINX1Enemy, 183, 127),
    ],
    music=MidbossMusic(),
    run_event_at_load=BE0071_JINX_USES_TRIPLE_KICK,
    can_run_away=False,
    unknown_bit=True,
)

FORM0289_ONE_MACK_FOUR_BODYGUARD = Formation(
    id=289,
    members=[
        FormationMember(MACKEnemy, 199, 119),
        FormationMember(BODYGUARDEnemy, 135, 111),
        FormationMember(BODYGUARDEnemy, 151, 127),
        FormationMember(BODYGUARDEnemy, 183, 143),
        FormationMember(BODYGUARDEnemy, 215, 151),
    ],
    music=BossMusic(),
    unknown_bit=True,
)

FORM0290_ONE_YARIDOVICH_ONE_YARIDOVICHMIRAGE = Formation(
    id=290,
    members=[
        FormationMember(YARIDOVICHEnemy, 183, 127),
        FormationMember(YARIDOVICHMirageEnemy, 183, 127, hidden_at_start=True),
    ],
    music=BossMusic(),
    unknown_bit=True,
)

FORM0291_ONE_BOWYER = Formation(
    id=291,
    members=[
        FormationMember(BOWYEREnemy, 183, 127),
    ],
    music=BossMusic(),
    unknown_bit=True,
    run_event_at_load=BE0014_SET_7EE001_TO_PARTY_SIZE_AT_START_OF_FIGHT,
)

FORM0292_ONE_AXEMRANGERS_ONE_AXEMRED_ONE_AXEMBLACK_ONE_AXEMPINK_ONE_AXEMGREEN_ONE_AXEMYELLOW = Formation(
    id=292,
    members=[
        FormationMember(AXEMRANGERSEnemy, 201, 79),
        FormationMember(AXEMREDEnemy, 135, 111, hidden_at_start=True),
        FormationMember(AXEMBLACKEnemy, 135, 127, hidden_at_start=True),
        FormationMember(AXEMPINKEnemy, 151, 143, hidden_at_start=True),
        FormationMember(AXEMGREENEnemy, 183, 151, hidden_at_start=True),
        FormationMember(AXEMYELLOWEnemy, 215, 151, hidden_at_start=True),
    ],
    music=BossMusic(),
    unknown_bit=True,
    run_event_at_load=BE0061_ONLY_MARIO_IS_THERE,
)

FORM0293_TWO_HAMMERBRO = Formation(
    id=293,
    members=[
        FormationMember(HAMMERBROEnemy, 135, 127),
        FormationMember(HAMMERBROEnemy, 199, 143),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0294_ONE_CLOAKER_ONE_DOMINO_ONE_MADADDER = Formation(
    id=294,
    members=[
        FormationMember(CLOAKEREnemy, 151, 111),
        FormationMember(DOMINOEnemy, 215, 159),
        FormationMember(MADADDEREnemy, 167, 135, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
    run_event_at_load=BE0052_INTRO_SCENE_DOMINO_CLOAKER_S_INTRODUCTION,
)

FORM0295_ONE_SMITHY1_ONE_SMELTER_TWO_MACHINEMADEBODYGUARD = Formation(
    id=295,
    members=[
        FormationMember(SMITHY1Enemy, 199, 127),
        FormationMember(SMELTEREnemy, 87, 87),
        FormationMember(MACHINEMADEBodyguardEnemy, 135, 127, hidden_at_start=True),
        FormationMember(MACHINEMADEBodyguardEnemy, 199, 159, hidden_at_start=True),
    ],
    music=Smithy1Music(),
    unknown_bit=True,
)

FORM0296_ONE_EXOR_ONE_NEOSQUID_ONE_RIGHTEYE_ONE_LEFTEYE = Formation(
    id=296,
    members=[
        FormationMember(EXOREnemy, 193, 64),
        FormationMember(NEOSQUIDEnemy, 187, 136),
        FormationMember(RIGHTEYEEnemy, 174, 145, hidden_at_start=True),
        FormationMember(LEFTEYEEnemy, 203, 157, hidden_at_start=True),
    ],
    music=BossMusic(),
    unknown_bit=True,
    run_event_at_load=BE0080_EXOR_FIGHT_BEGINS,
)

FORM0297_ONE_JINX2 = Formation(
    id=297,
    members=[
        FormationMember(JINX2Enemy, 183, 127),
    ],
    music=MidbossMusic(),
    run_event_at_load=BE0072_JINX_USES_QUICKSILVER,
    can_run_away=False,
    unknown_bit=True,
)

FORM0298_ONE_JINX3 = Formation(
    id=298,
    members=[
        FormationMember(JINX3Enemy, 183, 127),
    ],
    music=MidbossMusic(),
    run_event_at_load=BE0073_JINX_USES_BOMBS_AWAY,
    can_run_away=False,
    unknown_bit=True,
)

FORM0299_ONE_JAGGER = Formation(
    id=299,
    members=[
        FormationMember(JAGGEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0300_THREE_HEAVYTROOPA = Formation(
    id=300,
    members=[
        FormationMember(HEAVYTROOPAEnemy, 167, 135),
        FormationMember(HEAVYTROOPAEnemy, 151, 103),
        FormationMember(HEAVYTROOPAEnemy, 231, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0301 = Formation(
    id=301,
    members=[
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0302_FOUR_HELIO = Formation(
    id=302,
    members=[
        FormationMember(HELIOEnemy, 167, 119),
        FormationMember(HELIOEnemy, 135, 135),
        FormationMember(HELIOEnemy, 199, 167),
        FormationMember(HELIOEnemy, 231, 151),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0303_TWO_BODYGUARD = Formation(
    id=303,
    members=[
        FormationMember(BODYGUARDEnemy, 167, 119),
        FormationMember(BODYGUARDEnemy, 199, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0304_THREE_BODYGUARD = Formation(
    id=304,
    members=[
        FormationMember(BODYGUARDEnemy, 151, 111),
        FormationMember(BODYGUARDEnemy, 215, 143),
        FormationMember(BODYGUARDEnemy, 167, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0305_ONE_GENOCLONE = Formation(
    id=305,
    members=[
        FormationMember(GENOCLONEEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0306_ONE_BOWSERCLONE = Formation(
    id=306,
    members=[
        FormationMember(BOWSERCLONEEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0307_ONE_TOADSTOOL2 = Formation(
    id=307,
    members=[
        FormationMember(TOADSTOOL2Enemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0308_ONE_MARIOCLONE = Formation(
    id=308,
    members=[
        FormationMember(MARIOCLONEEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0309_ONE_MALLOWCLONE = Formation(
    id=309,
    members=[
        FormationMember(MALLOWCLONEEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0310_ONE_MACHINEMADEAXEMPINK_ONE_MACHINEMADEAXEMRED_ONE_MACHINEMADEAXEMGREEN = Formation(
    id=310,
    members=[
        FormationMember(MACHINEMADEAxemPinkEnemy, 151, 111),
        None,
        FormationMember(MACHINEMADEAxemRedEnemy, 151, 143),
        None,
        FormationMember(MACHINEMADEAxemGreenEnemy, 215, 143),
    ],
    music=BossMusic(),
    unknown_bit=True,
)

FORM0311_TWO_MACHINEMADEAXEMBLACK_TWO_MACHINEMADEAXEMYELLOW = Formation(
    id=311,
    members=[
        FormationMember(MACHINEMADEAxemBlackEnemy, 151, 119),
        FormationMember(MACHINEMADEAxemBlackEnemy, 231, 127),
        FormationMember(MACHINEMADEAxemYellowEnemy, 199, 143),
        FormationMember(MACHINEMADEAxemYellowEnemy, 183, 103),
    ],
    music=BossMusic(),
    unknown_bit=True,
)

FORM0312_THREE_BLOOBER = Formation(
    id=312,
    members=[
        FormationMember(BLOOBEREnemyStatic, 183, 127),
        FormationMember(BLOOBEREnemyStatic, 231, 143),
        FormationMember(BLOOBEREnemyStatic, 135, 111),
    ],
    music=None,
)

FORM0313_THREE_SHOGUN = Formation(
    id=313,
    members=[
        FormationMember(SHOGUNEnemy, 167, 135),
        FormationMember(SHOGUNEnemy, 151, 111),
        FormationMember(SHOGUNEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0314_ONE_FORMLESS_ONE_MOKURA = Formation(
    id=314,
    members=[
        FormationMember(FORMLESSEnemy, 167, 135),
        FormationMember(MOKURAEnemy, 167, 135, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0315_ONE_DODOENEMYSOLO = Formation(
    id=315,
    members=[
        FormationMember(DODOEnemySolo, 183, 127),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0316_ONE_KAMEK_ONE_TERRAPIN = Formation(
    id=316,
    members=[
        FormationMember(KAMEKEnemy, 215, 111),
        FormationMember(TERRAPINEnemy, 167, 135, hidden_at_start=True),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0317_ONE_BOOMER_TWO_HANGINSHY = Formation(
    id=317,
    members=[
        FormationMember(BOOMEREnemy, 215, 143),
        FormationMember(HANGINSHYEnemy, 66, 115),
        FormationMember(HANGINSHYEnemy, 186, 74),
    ],
    music=MidbossMusic(),
    unknown_bit=True,
)

FORM0318_ONE_MACHINEMADEMACK_FOUR_MACHINEMADEBODYGUARD = Formation(
    id=318,
    members=[
        FormationMember(MACHINEMADEMackEnemy, 199, 119),
        FormationMember(MACHINEMADEBodyguardEnemy, 135, 111),
        FormationMember(MACHINEMADEBodyguardEnemy, 151, 127),
        FormationMember(MACHINEMADEBodyguardEnemy, 183, 143),
        FormationMember(MACHINEMADEBodyguardEnemy, 215, 151),
    ],
    music=BossMusic(),
    unknown_bit=True,
)

FORM0319_ONE_MACHINEMADEBOWYER = Formation(
    id=319,
    members=[
        FormationMember(MACHINEMADEBowyerEnemy, 183, 127),
    ],
    music=BossMusic(),
    unknown_bit=True,
)

FORM0320_ONE_MACHINEMADEYARIDOVICH_FOUR_MACHINEMADEDRILLBIT = Formation(
    id=320,
    members=[
        FormationMember(MACHINEMADEYaridovichEnemy, 183, 127),
        FormationMember(MACHINEMADEDrillbitEnemy, 135, 119, hidden_at_start=True),
        FormationMember(MACHINEMADEDrillbitEnemy, 167, 103, hidden_at_start=True),
        FormationMember(MACHINEMADEDrillbitEnemy, 199, 151, hidden_at_start=True),
        FormationMember(MACHINEMADEDrillbitEnemy, 231, 135, hidden_at_start=True),
    ],
    music=BossMusic(),
    unknown_bit=True,
)

FORM0321_ONE_SMITHYBODY_ONE_SMITHY2 = Formation(
    id=321,
    members=[
        FormationMember(SMITHYBodyEnemy, 183, 135, hidden_at_start=True),
        FormationMember(SMITHY2Enemy, 183, 175),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0322_ONE_CULEX_ONE_FIRECRYSTAL_ONE_WATERCRYSTAL_ONE_EARTHCRYSTAL_ONE_WINDCRYSTAL = Formation(
    id=322,
    members=[
        FormationMember(CULEXEnemy, 183, 103),
        FormationMember(FIRECRYSTALEnemy, 135, 103, hidden_at_start=True),
        FormationMember(WATERCRYSTALEnemy, 151, 119, hidden_at_start=True),
        FormationMember(EARTHCRYSTALEnemy, 183, 135, hidden_at_start=True),
        FormationMember(WINDCRYSTALEnemy, 215, 143, hidden_at_start=True),
    ],
    music=CulexMusic(),
    unknown_bit=True,
)

FORM0323_ONE_FIRECRYSTAL = Formation(
    id=323,
    members=[
        FormationMember(FIRECRYSTALEnemy, 183, 127, hidden_at_start=True),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
    run_event_at_load=BE0076_SOLO_FIRE_CRYSTAL_APPEARS,
)

FORM0324_ONE_WATERCRYSTAL = Formation(
    id=324,
    members=[
        FormationMember(WATERCRYSTALEnemy, 183, 127, hidden_at_start=True),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
    run_event_at_load=BE0020_SOLO_WATER_CRYSTAL_APPEARS,
)

FORM0325_ONE_EARTHCRYSTAL = Formation(
    id=325,
    members=[
        FormationMember(EARTHCRYSTALEnemy, 183, 127, hidden_at_start=True),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
    run_event_at_load=BE0011_SOLO_EARTH_CRYSTAL_APPEARS,
)

FORM0326_ONE_WINDCRYSTAL = Formation(
    id=326,
    members=[
        FormationMember(WINDCRYSTALEnemy, 183, 127, hidden_at_start=True),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
    run_event_at_load=BE0001_SOLO_WIND_CRYSTAL_APPEARS,
)

FORM0327_THREE_GOOMBETTE = Formation(
    id=327,
    members=[
        FormationMember(GOOMBETTEEnemy, 183, 127),
        FormationMember(GOOMBETTEEnemy, 231, 135),
        FormationMember(GOOMBETTEEnemy, 167, 103),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0328_ONE_EGGBERT = Formation(
    id=328,
    members=[
        FormationMember(EGGBERTEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0329_THREE_EGGBERT = Formation(
    id=329,
    members=[
        FormationMember(EGGBERTEnemy, 167, 111),
        FormationMember(EGGBERTEnemy, 167, 135),
        FormationMember(EGGBERTEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0330_FOUR_EGGBERT = Formation(
    id=330,
    members=[
        FormationMember(EGGBERTEnemy, 135, 127),
        FormationMember(EGGBERTEnemy, 183, 111),
        FormationMember(EGGBERTEnemy, 183, 151),
        FormationMember(EGGBERTEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0331_FOUR_TERRACOTTA = Formation(
    id=331,
    members=[
        FormationMember(TERRACOTTAEnemy, 135, 127),
        FormationMember(TERRACOTTAEnemy, 183, 111),
        FormationMember(TERRACOTTAEnemy, 183, 151),
        FormationMember(TERRACOTTAEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0332_TWO_OERLIKON_ONE_STARCRUSTER = Formation(
    id=332,
    members=[
        FormationMember(OERLIKONEnemy, 135, 119),
        FormationMember(OERLIKONEnemy, 199, 151),
        FormationMember(STARCRUSTEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0333_ONE_SACKIT_TWO_BIGBERTHA = Formation(
    id=333,
    members=[
        FormationMember(SACKITEnemy, 167, 135),
        None,
        FormationMember(BIGBERTHAEnemy, 151, 103),
        FormationMember(BIGBERTHAEnemy, 231, 143),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0334_TWO_CHOW_ONE_FORKIES = Formation(
    id=334,
    members=[
        FormationMember(CHOWEnemy, 135, 111),
        FormationMember(CHOWEnemy, 215, 151),
        FormationMember(FORKIESEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0335_ONE_ALLEYRAT_TWO_ARMOREDANT = Formation(
    id=335,
    members=[
        FormationMember(ALLEYRATEnemy, 199, 119),
        FormationMember(ARMOREDANTEnemy, 135, 119),
        FormationMember(ARMOREDANTEnemy, 199, 151),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0336_THREE_BLOOBER_ONE_STARCRUSTER = Formation(
    id=336,
    members=[
        FormationMember(BLOOBEREnemyStatic, 199, 119),
        FormationMember(BLOOBEREnemyStatic, 183, 151),
        FormationMember(BLOOBEREnemyStatic, 231, 151),
        FormationMember(STARCRUSTEREnemy, 135, 103),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0337_FOUR_STINGER = Formation(
    id=337,
    members=[
        FormationMember(STINGEREnemy, 151, 111),
        FormationMember(STINGEREnemy, 167, 127),
        FormationMember(STINGEREnemy, 199, 143),
        FormationMember(STINGEREnemy, 231, 151),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0338_TWO_GECKIT_ONE_CHAINEDKONG = Formation(
    id=338,
    members=[
        FormationMember(GECKITEnemy, 215, 151),
        FormationMember(GECKITEnemy, 135, 111),
        FormationMember(CHAINEDKONGEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0339_ONE_ROBOMB_TWO_BIGBERTHA = Formation(
    id=339,
    members=[
        FormationMember(ROBOMBEnemy, 167, 135),
        None,
        FormationMember(BIGBERTHAEnemy, 167, 111),
        FormationMember(BIGBERTHAEnemy, 215, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0340_FOUR_VOMER = Formation(
    id=340,
    members=[
        FormationMember(VOMEREnemy, 151, 127),
        FormationMember(VOMEREnemy, 183, 143),
        FormationMember(VOMEREnemy, 151, 103),
        FormationMember(VOMEREnemy, 231, 143),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0341_TWO_MAGMUS_TWO_PULSAR = Formation(
    id=341,
    members=[
        FormationMember(MAGMUSEnemy, 151, 127),
        FormationMember(MAGMUSEnemy, 183, 143),
        FormationMember(PULSAREnemy, 151, 103),
        FormationMember(PULSAREnemy, 231, 143),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0342 = Formation(
    id=342,
    members=[
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0343_FIVE_GUGOOMBA = Formation(
    id=343,
    members=[
        FormationMember(GUGOOMBAEnemy, 151, 127),
        FormationMember(GUGOOMBAEnemy, 183, 143),
        FormationMember(GUGOOMBAEnemy, 199, 119),
        FormationMember(GUGOOMBAEnemy, 167, 103),
        FormationMember(GUGOOMBAEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0344_TWO_MALAKOOPA_ONE_TUBOTROOPA = Formation(
    id=344,
    members=[
        FormationMember(MALAKOOPAEnemy, 135, 111),
        FormationMember(MALAKOOPAEnemy, 215, 151),
        FormationMember(TUBOTROOPAEnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0345_TWO_THEBIGBOO_TWO_ORBISON = Formation(
    id=345,
    members=[
        FormationMember(THEBIGBOOEnemy, 183, 143),
        FormationMember(THEBIGBOOEnemy, 151, 127),
        FormationMember(ORBISONEnemy, 167, 103),
        FormationMember(ORBISONEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0346_FIVE_SLINGSHY = Formation(
    id=346,
    members=[
        FormationMember(SLINGSHYEnemy, 167, 135),
        FormationMember(SLINGSHYEnemy, 167, 119),
        FormationMember(SLINGSHYEnemy, 199, 135),
        FormationMember(SLINGSHYEnemy, 167, 103),
        FormationMember(SLINGSHYEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0347_TWO_CHEWY_TWO_SHYAWAY = Formation(
    id=347,
    members=[
        FormationMember(CHEWYEnemy, 151, 127),
        FormationMember(CHEWYEnemy, 183, 143),
        FormationMember(SHYAWAYEnemy, 167, 103),
        FormationMember(SHYAWAYEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0348_ONE_MRKIPPER_TWO_MUCKLE = Formation(
    id=348,
    members=[
        FormationMember(MRKIPPEREnemy, 167, 135),
        FormationMember(MUCKLEEnemy, 167, 103),
        FormationMember(MUCKLEEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0349_TWO_AMANITA_ONE_ORBISON = Formation(
    id=349,
    members=[
        FormationMember(AMANITAEnemy, 215, 143),
        FormationMember(AMANITAEnemy, 151, 111),
        FormationMember(ORBISONEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0350_TWO_GREAPER_ONE_GLUMREAPER = Formation(
    id=350,
    members=[
        FormationMember(GREAPEREnemy, 215, 143),
        FormationMember(GREAPEREnemy, 151, 111),
        FormationMember(GLUMREAPEREnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0351_THREE_PYROSPHERE = Formation(
    id=351,
    members=[
        FormationMember(PYROSPHEREEnemy, 183, 127),
        FormationMember(PYROSPHEREEnemy, 151, 111),
        FormationMember(PYROSPHEREEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0352_THREE_LAKITU = Formation(
    id=352,
    members=[
        FormationMember(LAKITUEnemy, 183, 127),
        FormationMember(LAKITUEnemy, 151, 111),
        FormationMember(LAKITUEnemy, 215, 143),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0353_TWO_ZEOSTAR_TWO_SHAMAN = Formation(
    id=353,
    members=[
        FormationMember(ZEOSTAREnemy, 151, 127),
        FormationMember(ZEOSTAREnemy, 183, 143),
        FormationMember(SHAMANEnemy, 167, 103),
        FormationMember(SHAMANEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0354_SIX_SHAMAN = Formation(
    id=354,
    members=[
        FormationMember(SHAMANEnemy, 135, 119),
        FormationMember(SHAMANEnemy, 167, 103),
        FormationMember(SHAMANEnemy, 167, 135),
        FormationMember(SHAMANEnemy, 199, 119),
        FormationMember(SHAMANEnemy, 199, 151),
        FormationMember(SHAMANEnemy, 231, 135),
    ],
    music=NormalBattleMusic(),
    can_run_away=False,
    unknown_bit=True,
)

FORM0355_ONE_AXEMBLACK = Formation(
    id=355,
    members=[
        FormationMember(AXEMBLACKEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0356_ONE_AXEMPINK = Formation(
    id=356,
    members=[
        FormationMember(AXEMPINKEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0357_ONE_AXEMYELLOW = Formation(
    id=357,
    members=[
        FormationMember(AXEMYELLOWEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0358_ONE_AXEMGREEN = Formation(
    id=358,
    members=[
        FormationMember(AXEMGREENEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0359_ONE_DINGALING = Formation(
    id=359,
    members=[
        FormationMember(DINGALINGEnemy, 183, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0360_ONE_DRILLBIT = Formation(
    id=360,
    members=[
        FormationMember(DRILLBITEnemy, 135, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0361_ONE_DRILLBIT = Formation(
    id=361,
    members=[
        FormationMember(DRILLBITEnemy, 167, 103),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)
FORM0362_TWO_BOBOMB_ONE_CLUSTER = Formation(
    id=362,
    members=[
        FormationMember(BOBOMBEnemyStatic, 135, 119),
        FormationMember(BOBOMBEnemyStatic, 199, 151),
        FormationMember(CLUSTEREnemy, 199, 119),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0363_FOUR_BOBOMB = Formation(
    id=363,
    members=[
        FormationMember(BOBOMBEnemyStatic, 151, 127),
        FormationMember(BOBOMBEnemyStatic, 167, 103),
        FormationMember(BOBOMBEnemyStatic, 199, 151),
        FormationMember(BOBOMBEnemyStatic, 215, 127),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)

FORM0364_ONE_BOXBOY_ONE_FAUTSO = Formation(
    id=364,
    members=[
        FormationMember(BOXBOYEnemy, 183, 127),
        FormationMember(FAUTSOEnemy, 151, 111, hidden_at_start=True),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)


# Dedicated henchman formation for the Punchinello boss-room henchman pack
# (PACK152). FORM0060/0061/0062 are shared with the regular Moleville bob-omb
# encounter (PACK036), so PACK152 needs its own formation built from the
# dedicated BOBOMBEnemyHenchman (monster_id 111) — which Punchinello registers
# in boss_enemy_types — to keep it out of randomize_enemy_formations.
FORM0365_THREE_BOBOMBHENCHMAN = Formation(
    id=365,
    members=[
        FormationMember(BOBOMBEnemyHenchman, 167, 111),
        FormationMember(BOBOMBEnemyHenchman, 167, 135),
        FormationMember(BOBOMBEnemyHenchman, 215, 135),
    ],
    music=NormalBattleMusic(),
    unknown_bit=True,
)


# ============================================================================
# Pack Definitions
# ============================================================================

# Initialize packs array with None values
packs: list[FormationPack] = [None] * 256  # type: ignore

packs[PACK000_TOWER_HENCHMAN_1] = FormationPack(FORM0000_ONE_SNIFIT)
packs[PACK001_TOWER_HENCHMAN_2] = FormationPack(FORM0000_ONE_SNIFIT)
packs[PACK002_SPIKEYS_AND_TROOPAS] = FormationPack(FORM0001_TWO_SPIKEY, FORM0002_ONE_SPIKEY_ONE_SKYTROOPA, FORM0002_ONE_SPIKEY_ONE_SKYTROOPA)
packs[PACK003_SPIKEYS_AND_FROGS] = FormationPack(FORM0003_THREE_SPIKEY, FORM0004_TWO_SPIKEY_ONE_FROGOG, FORM0004_TWO_SPIKEY_ONE_FROGOG)
packs[PACK004_JUST_TROOPAS] = FormationPack(FORM0005_ONE_SKYTROOPA, FORM0006_TWO_SKYTROOPA, FORM0006_TWO_SKYTROOPA)
packs[PACK005_TROOPAS_WITH_FROGS_OR_GOOMBAS] = FormationPack(FORM0007_TWO_SKYTROOPA_ONE_GOOMBA, FORM0008_TWO_SKYTROOPA_ONE_FROGOG, FORM0006_TWO_SKYTROOPA)
packs[PACK006_JUST_GOOMBAS] = FormationPack(FORM0009_TWO_GOOMBA, FORM0010_THREE_GOOMBA, FORM0009_TWO_GOOMBA)
packs[PACK007_GOOMBAS_WITH_FROGS_OR_SPIKEYS] = FormationPack(FORM0011_ONE_GOOMBA_ONE_FROGOG_ONE_SPIKEY, FORM0012_TWO_GOOMBA_ONE_SPIKEY, FORM0010_THREE_GOOMBA)
packs[PACK008_K9S_WITH_SPIKEYS] = FormationPack(FORM0013_ONE_K9, FORM0014_TWO_K9, FORM0015_TWO_K9_ONE_SPIKEY)
packs[PACK009_K9S_WITH_SPIKEYS_OR_FROGS] = FormationPack(FORM0016_ONE_K9_TWO_FROGOG, FORM0015_TWO_K9_ONE_SPIKEY, FORM0014_TWO_K9)
packs[PACK010_KINGDOM_HENCHMEN_1] = FormationPack(FORM0017_TWO_SHYSTER, FORM0018_THREE_SHYSTER, FORM0017_TWO_SHYSTER)
packs[PACK011_KINGDOM_HENCHMEN_2] = FormationPack(FORM0017_TWO_SHYSTER, FORM0018_THREE_SHYSTER, FORM0018_THREE_SHYSTER)
packs[PACK012_RATFUNKS_WITH_SHADOW_OR_HOBGOBLIN] = FormationPack(FORM0019_TWO_RATFUNK, FORM0020_TWO_RATFUNK_ONE_SHADOW, FORM0021_TWO_RATFUNK_ONE_HOBGOBLIN)
packs[PACK013_RATFUNKS_ALWAYS_WITH_ONE_OTHER_MONSTER] = FormationPack(FORM0022_ONE_RATFUNK_TWO_HOBGOBLIN, FORM0021_TWO_RATFUNK_ONE_HOBGOBLIN, FORM0020_TWO_RATFUNK_ONE_SHADOW)
packs[PACK014_BIGBOO_ALWAYS_WITH_ONE_OTHER_MONSTER_1] = FormationPack(FORM0023_ONE_THEBIGBOO_ONE_SHADOW, FORM0023_ONE_THEBIGBOO_ONE_SHADOW, FORM0024_ONE_THEBIGBOO_ONE_SHADOW_ONE_HOBGOBLIN)
packs[PACK015_BIGBOO_ALWAYS_WITH_ONE_OTHER_MONSTER_2] = FormationPack(FORM0025_THREE_THEBIGBOO_ONE_SHADOW, FORM0024_ONE_THEBIGBOO_ONE_SHADOW_ONE_HOBGOBLIN, FORM0023_ONE_THEBIGBOO_ONE_SHADOW)
packs[PACK016_MULTIPLE_GOBYS_BIASED_2] = FormationPack(FORM0026_TWO_GOBY, FORM0026_TWO_GOBY, FORM0027_THREE_GOBY)
packs[PACK017_MULTIPLE_GOBYS_BIASED_3] = FormationPack(FORM0027_THREE_GOBY, FORM0027_THREE_GOBY, FORM0026_TWO_GOBY)
packs[PACK018_CROOKS_WITH_SHYGUY_OR_SNAPDRAGON] = FormationPack(FORM0028_TWO_CROOK, FORM0029_TWO_CROOK_ONE_SHYGUY, FORM0030_ONE_CROOK_TWO_SNAPDRAGON)
packs[PACK019_CROOKS_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0031_ONE_CROOK_ONE_STARSLAP_ONE_ARACHNE, FORM0030_ONE_CROOK_TWO_SNAPDRAGON, FORM0029_TWO_CROOK_ONE_SHYGUY)
packs[PACK020_SHYGUYS_WITH_STARSLAP_OR_SNAPDRAGON] = FormationPack(FORM0032_ONE_SHYGUY_ONE_STARSLAP, FORM0032_ONE_SHYGUY_ONE_STARSLAP, FORM0033_TWO_SHYGUY_ONE_SNAPDRAGON)
packs[PACK021_SHYGUY_STARSLAP_SNAPDRAGON_CROOK_ARACHNE] = FormationPack(FORM0034_ONE_SHYGUY_ONE_CROOK_ONE_ARACHNE, FORM0033_TWO_SHYGUY_ONE_SNAPDRAGON, FORM0032_ONE_SHYGUY_ONE_STARSLAP)
packs[PACK022_STARSLAP_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0035_ONE_STARSLAP_ONE_SHYGUY, FORM0036_ONE_STARSLAP_ONE_ARACHNE, FORM0037_ONE_STARSLAP_TWO_SNAPDRAGON)
packs[PACK023_STARSLAPS_SOMETIMES_WITH_OTHER_MONSTERS] = FormationPack(FORM0038_FOUR_STARSLAP, FORM0037_ONE_STARSLAP_TWO_SNAPDRAGON, FORM0036_ONE_STARSLAP_ONE_ARACHNE)
packs[PACK024_WIGGLERS_WITH_AMANITA] = FormationPack(FORM0039_ONE_WIGGLER, FORM0040_ONE_WIGGLER_ONE_AMANITA, FORM0041_TWO_WIGGLER)
packs[PACK025_WIGGLERS_WITH_GUERRILLA_OR_AMANITA] = FormationPack(FORM0042_ONE_WIGGLER_ONE_GUERRILLA, FORM0041_TWO_WIGGLER, FORM0040_ONE_WIGGLER_ONE_AMANITA)
packs[PACK026_AMANITAS_WITH_BUZZER_OR_OCTOLOT] = FormationPack(FORM0043_TWO_AMANITA, FORM0044_TWO_AMANITA_ONE_BUZZER, FORM0045_TWO_AMANITA_ONE_OCTOLOT)
packs[PACK027_AMANITAS_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0046_ONE_AMANITA_ONE_GUERRILLA_ONE_BUZZER, FORM0045_TWO_AMANITA_ONE_OCTOLOT, FORM0044_TWO_AMANITA_ONE_BUZZER)
packs[PACK028_BUZZERS_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0047_ONE_BUZZER_ONE_OCTOLOT, FORM0048_TWO_BUZZER_ONE_AMANITA, FORM0049_ONE_BUZZER_ONE_GUERRILLA)
packs[PACK029_BUZZERS_WITH_AMANITA] = FormationPack(FORM0050_ONE_BUZZER_ONE_GUERRILLA, FORM0049_ONE_BUZZER_ONE_GUERRILLA, FORM0048_TWO_BUZZER_ONE_AMANITA)
packs[PACK030_SPARKY_WITH_SHYRANGER] = FormationPack(FORM0051_ONE_SPARKY, FORM0052_TWO_SPARKY_ONE_SHYRANGER, FORM0053_THREE_SPARKY)
packs[PACK031_MULTIPLE_SPARKY_WITH_SHYRANGER] = FormationPack(FORM0053_THREE_SPARKY, FORM0053_THREE_SPARKY, FORM0052_TWO_SPARKY_ONE_SHYRANGER)
packs[PACK032_TOWER_PASS_HENCHMAN] = FormationPack(FORM0054_ONE_APPRENTICE)
packs[PACK033_POSTGAME_TEMPLE] = FormationPack(FORM0055_ONE_BELOMEENEMY3_ONE_MARIOCLONES_ONE_TOADSTOOL3)
packs[PACK034_PIRANHA_WITH_SHYRANGER] = FormationPack(FORM0056_ONE_PIRANHAPLANT, FORM0057_TWO_PIRANHAPLANT_ONE_SHYRANGER, FORM0058_THREE_PIRANHAPLANT)
packs[PACK035_MULTIPLE_PIRANHA_WITH_SHYRANGER] = FormationPack(FORM0059_FIVE_PIRANHAPLANT, FORM0058_THREE_PIRANHAPLANT, FORM0057_TWO_PIRANHAPLANT_ONE_SHYRANGER)
packs[PACK036_BOBOMB_WITH_CLUSTER] = FormationPack(FORM0060_ONE_BOBOMB, FORM0061_TWO_BOBOMB_ONE_CLUSTER, FORM0062_FOUR_BOBOMB)
packs[PACK037_BOBOMB_WITH_CLUSTER_SOMETIMES_ENIGMA] = FormationPack(FORM0063_TWO_BOBOMB_ONE_ENIGMA_ONE_CLUSTER, FORM0362_TWO_BOBOMB_ONE_CLUSTER, FORM0363_FOUR_BOBOMB)
packs[PACK038_SPARKY_WITH_ALWAYS_OTHER_ENEMIES_1] = FormationPack(FORM0064_ONE_SPARKY_ONE_ENIGMA, FORM0065_TWO_SPARKY_ONE_BOBOMB, FORM0066_ONE_SPARKY_TWO_CLUSTER)
packs[PACK039_SPARKY_WITH_ALWAYS_OTHER_ENEMIES_2] = FormationPack(FORM0067_TWO_SPARKY_TWO_ENIGMA, FORM0066_ONE_SPARKY_TWO_CLUSTER, FORM0065_TWO_SPARKY_ONE_BOBOMB)
packs[PACK040_MAGMITES_WITH_SPARKY_BOBOMB_OR_CLUSTER] = FormationPack(FORM0068_TWO_MAGMITE, FORM0069_ONE_MAGMITE_ONE_BOBOMB_ONE_SPARKY, FORM0070_TWO_MAGMITE_TWO_CLUSTER)
packs[PACK041_MAGMITES_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0071_TWO_MAGMITE_ONE_BOBOMB_ONE_CLUSTER, FORM0070_TWO_MAGMITE_TWO_CLUSTER, FORM0069_ONE_MAGMITE_ONE_BOBOMB_ONE_SPARKY)
packs[PACK042_LAKITU_WITH_SPIKESTER_ARTICHOKER] = FormationPack(FORM0072_ONE_LAKITU, FORM0073_ONE_LAKITU_ONE_SPIKESTER_ONE_ARTICHOKER, FORM0074_THREE_LAKITU)
packs[PACK043_LAKITU_USUALLY_WITH_ARTICHOKER] = FormationPack(FORM0075_TWO_LAKITU_ONE_ARTICHOKER, FORM0074_THREE_LAKITU, FORM0073_ONE_LAKITU_ONE_SPIKESTER_ONE_ARTICHOKER)
packs[PACK044_SPIKESTER_WITH_OTHER_ENEMIES] = FormationPack(FORM0076_ONE_SPIKESTER_ONE_CARROBOSCIS, FORM0077_TWO_SPIKESTER_ONE_ARTICHOKER, FORM0078_ONE_SPIKESTER_TWO_CARROBOSCIS)
packs[PACK045_MULTIPLE_SPIKESTER_WITH_OTHER_ENEMIES] = FormationPack(FORM0079_FOUR_SPIKESTER_ONE_CARROBOSCIS, FORM0078_ONE_SPIKESTER_TWO_CARROBOSCIS, FORM0077_TWO_SPIKESTER_ONE_ARTICHOKER)
packs[PACK046_SPOOKUM_WITH_OTHER_MONSTERS] = FormationPack(FORM0080_ONE_SPOOKUM_ONE_ORBUSER, FORM0081_TWO_SPOOKUM_ONE_JESTER, FORM0082_ONE_SPOOKUM_ONE_REMOCON_ONE_ORBUSER)
packs[PACK047_MULTIPLE_SPOOKUM_WITH_OTHER_MONSTERS] = FormationPack(FORM0083_TWO_SPOOKUM_ONE_REMOCON, FORM0082_ONE_SPOOKUM_ONE_REMOCON_ONE_ORBUSER, FORM0081_TWO_SPOOKUM_ONE_JESTER)
packs[PACK048_ROBOMB_WITH_REMOCON] = FormationPack(FORM0084_ONE_ROBOMB, FORM0085_THREE_ROBOMB, FORM0086_TWO_ROBOMB_ONE_REMOCON)
packs[PACK049_ROBOMB_WITH_REMOCON_OR_ORBUSER] = FormationPack(FORM0087_FOUR_ROBOMB_ONE_ORBUSER, FORM0086_TWO_ROBOMB_ONE_REMOCON, FORM0085_THREE_ROBOMB)
packs[PACK050_CHOMP_WITH_OTHER_MONSTERS_1] = FormationPack(FORM0088_ONE_CHOMP_ONE_JESTER, FORM0089_ONE_CHOMP_ONE_ROBOMB_ONE_REMOCON, FORM0090_TWO_CHOMP_ONE_ORBUSER)
packs[PACK051_CHOMP_WITH_OTHER_MONSTERS_2] = FormationPack(FORM0091_ONE_CHOMP_TWO_JESTER, FORM0090_TWO_CHOMP_ONE_ORBUSER, FORM0089_ONE_CHOMP_ONE_ROBOMB_ONE_REMOCON)
packs[PACK052_BLASTERS_AND_SPOOKUMS_1] = FormationPack(FORM0092_ONE_BLASTER_ONE_SPOOKUM, FORM0093_ONE_BLASTER_ONE_SPOOKUM_ONE_REMOCON, FORM0094_TWO_BLASTER_ONE_SPOOKUM)
packs[PACK053_BLASTERS_AND_SPOOKUMS_2] = FormationPack(FORM0095_ONE_BLASTER_TWO_ROBOMB_TWO_SPOOKUM, FORM0094_TWO_BLASTER_ONE_SPOOKUM, FORM0093_ONE_BLASTER_ONE_SPOOKUM_ONE_REMOCON)
packs[PACK054_TOWER_HENCHMAN_3] = FormationPack(FORM0000_ONE_SNIFIT)
packs[PACK055_MONSTRO_DOOR_POSTGAME] = FormationPack(FORM0096_ONE_CULEX3D_ONE_FIRECRYS3D_ONE_WATERCRYS3D_ONE_EARTHCRYS3D_ONE_WINDCRYS3D)
packs[PACK056_MUKU_PULSAR_GECKO] = FormationPack(FORM0097_ONE_MUKUMUKU, FORM0098_TWO_MUKUMUKU, FORM0099_TWO_MUKUMUKU_ONE_PULSAR)
packs[PACK057_MUKU_PULSAR_GECKO_MULTI] = FormationPack(FORM0100_ONE_MUKUMUKU_ONE_PULSAR_ONE_GECKO, FORM0099_TWO_MUKUMUKU_ONE_PULSAR, FORM0098_TWO_MUKUMUKU)
packs[PACK058_SACKIT_WITH_OTHER_MONSTERS] = FormationPack(FORM0101_TWO_SACKIT, FORM0102_TWO_SACKIT_ONE_MUKUMUKU_ONE_GECKO, FORM0103_ONE_SACKIT_TWO_PULSAR)
packs[PACK059_SACKIT_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0104_ONE_SACKIT_ONE_MASTADOOM, FORM0103_ONE_SACKIT_TWO_PULSAR, FORM0102_TWO_SACKIT_ONE_MUKUMUKU_ONE_GECKO)
packs[PACK060_GECKO_PACK_1] = FormationPack(FORM0105_ONE_GECKO_ONE_SACKIT, FORM0106_ONE_GECKO_ONE_MASTADOOM, FORM0107_TWO_GECKO_TWO_MUKUMUKU_TWO_SACKIT)
packs[PACK061_GECKO_PACK_2] = FormationPack(FORM0108_TWO_GECKO_ONE_MASTADOOM, FORM0107_TWO_GECKO_TWO_MUKUMUKU_TWO_SACKIT, FORM0106_ONE_GECKO_ONE_MASTADOOM)
packs[PACK062_ZEOSTAR_WITH_BLOOBER_OR_LEUKO] = FormationPack(FORM0109_TWO_ZEOSTAR, FORM0110_TWO_ZEOSTAR_ONE_BLOOBER, FORM0111_TWO_ZEOSTAR_TWO_LEUKO)
packs[PACK063_ZEOSTAR_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0112_ONE_ZEOSTAR_ONE_LEUKO_ONE_CRUSTY, FORM0111_TWO_ZEOSTAR_TWO_LEUKO, FORM0110_TWO_ZEOSTAR_ONE_BLOOBER)
packs[PACK064_BLOOBER_PACK_1] = FormationPack(FORM0113_ONE_BLOOBER_ONE_MRKIPPER, FORM0114_THREE_BLOOBER, FORM0115_TWO_BLOOBER_ONE_MRKIPPER_ONE_CRUSTY)
packs[PACK065_BLOOBER_PACK_2] = FormationPack(FORM0116_TWO_BLOOBER_TWO_ZEOSTAR_ONE_LEUKO, FORM0115_TWO_BLOOBER_ONE_MRKIPPER_ONE_CRUSTY, FORM0114_THREE_BLOOBER)
packs[PACK066_KIPPER_PACK_1] = FormationPack(FORM0117_THREE_MRKIPPER, FORM0118_TWO_MRKIPPER_ONE_CRUSTY, FORM0119_TWO_MRKIPPER_ONE_CRUSTY)
packs[PACK067_KIPPER_PACK_2] = FormationPack(FORM0120_FOUR_MRKIPPER, FORM0119_TWO_MRKIPPER_ONE_CRUSTY, FORM0118_TWO_MRKIPPER_ONE_CRUSTY)
packs[PACK068_SHIP_HENCHMAN_1] = FormationPack(FORM0121_FOUR_BANDANARED)
packs[PACK069_SHIP_HENCHMAN_2] = FormationPack(FORM0122_FIVE_BANDANARED)
packs[PACK070_TOWER_POSTGAME] = FormationPack(FORM0123_ONE_BOOSTERENEMY2_THREE_SNIFIT2_ONE_BOOSTERDUMMY)
packs[PACK071_MINES_POSTGAME] = FormationPack(FORM0124_ONE_PUNCHINELLO2_ONE_STRONGBOBOMB3_ONE_STRONGBOBOMB1_ONE_STRONGBOBOMB4_ONE_STRONGBOBOMB2)
packs[PACK072_DRYBONES_WITH_GREAPER_REACHER] = FormationPack(FORM0125_TWO_DRYBONES, FORM0126_TWO_DRYBONES_ONE_GREAPER, FORM0127_ONE_DRYBONES_ONE_GREAPER_ONE_REACHER)
packs[PACK073_DRYBONES_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0128_TWO_DRYBONES_TWO_GREAPER_ONE_REACHER, FORM0127_ONE_DRYBONES_ONE_GREAPER_ONE_REACHER, FORM0126_TWO_DRYBONES_ONE_GREAPER)
packs[PACK074_ALLEYRAT_PACK_1] = FormationPack(FORM0129_ONE_ALLEYRAT_ONE_GORGON, FORM0130_TWO_ALLEYRAT_TWO_GREAPER, FORM0131_TWO_ALLEYRAT_TWO_GORGON)
packs[PACK075_ALLEYRAT_PACK_2] = FormationPack(FORM0132_ONE_ALLEYRAT_ONE_REACHER_ONE_GORGON, FORM0131_TWO_ALLEYRAT_TWO_GORGON, FORM0130_TWO_ALLEYRAT_TWO_GREAPER)
packs[PACK076_GREAPER_WITH_REACHER_STRAWHEAD] = FormationPack(FORM0133_ONE_GREAPER, FORM0134_TWO_GREAPER_ONE_REACHER, FORM0135_ONE_GREAPER_ONE_STRAWHEAD_ONE_REACHER)
packs[PACK077_GREAPER_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0136_ONE_GREAPER_ONE_GORGON_TWO_STRAWHEAD, FORM0135_ONE_GREAPER_ONE_STRAWHEAD_ONE_REACHER, FORM0134_TWO_GREAPER_ONE_REACHER)
packs[PACK078_CHAPEL_POSTGAME] = FormationPack(FORM0137_ONE_BUNDT2_ONE_RASPBERRY2_TWO_TORTE2_ONE_CANDLE)
packs[PACK079_MINES_HENCHMAN_RIGHT] = FormationPack(FORM0138_THREE_CROOK, FORM0139_FIVE_CROOK, FORM0138_THREE_CROOK)
packs[PACK080_STINGER_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0140_ONE_STINGER_ONE_FINKFLOWER, FORM0141_TWO_STINGER_ONE_OCTOVADER, FORM0142_ONE_STINGER_TWO_FINKFLOWER)
packs[PACK081_STINGER_WITH_OCTOVADER_OR_FINKFLOWER] = FormationPack(FORM0143_FOUR_STINGER, FORM0142_ONE_STINGER_TWO_FINKFLOWER, FORM0141_TWO_STINGER_ONE_OCTOVADER)
packs[PACK082_CHOW_PACK_1] = FormationPack(FORM0144_ONE_CHOW_ONE_OCTOVADER, FORM0145_ONE_CHOW_ONE_SHOGUN, FORM0146_ONE_CHOW_ONE_SHOGUN_ONE_OCTOVADER)
packs[PACK083_CHOW_PACK_2] = FormationPack(FORM0147_ONE_CHOW_ONE_FINKFLOWER_TWO_SHOGUN, FORM0146_ONE_CHOW_ONE_SHOGUN_ONE_OCTOVADER, FORM0145_ONE_CHOW_ONE_SHOGUN)
packs[PACK084_CHOMPCHOMP_PACK_1] = FormationPack(FORM0148_ONE_CHOMPCHOMP, FORM0149_TWO_CHOMPCHOMP, FORM0150_THREE_CHOMPCHOMP)
packs[PACK085_CHOMPCHOMP_PACK_2] = FormationPack(FORM0151_FOUR_CHOMPCHOMP, FORM0150_THREE_CHOMPCHOMP, FORM0149_TWO_CHOMPCHOMP)
packs[PACK086_SHYAWAY_WITH_KRIFFID_OR_RIBBITE] = FormationPack(FORM0152_ONE_SHYAWAY, FORM0153_TWO_SHYAWAY_ONE_KRIFFID, FORM0154_TWO_SHYAWAY_ONE_RIBBITE)
packs[PACK087_SHYAWAY_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0155_ONE_SHYAWAY_ONE_GECKIT_ONE_RIBBITE, FORM0154_TWO_SHYAWAY_ONE_RIBBITE, FORM0153_TWO_SHYAWAY_ONE_KRIFFID)
packs[PACK088_CHEWY_WITH_SHYAWAY_OR_SPINTHRA] = FormationPack(FORM0156_TWO_CHEWY, FORM0157_TWO_CHEWY_ONE_SHYAWAY, FORM0158_ONE_CHEWY_ONE_SPINTHRA)
packs[PACK089_CHEWY_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0159_TWO_CHEWY_TWO_GECKIT_ONE_KRIFFID, FORM0158_ONE_CHEWY_ONE_SPINTHRA, FORM0157_TWO_CHEWY_ONE_SHYAWAY)
packs[PACK090_GECKIT_PACK_1] = FormationPack(FORM0160_ONE_GECKIT_ONE_SPINTHRA, FORM0161_TWO_GECKIT_ONE_SPINTHRA, FORM0162_TWO_GECKIT_TWO_CHEWY_ONE_SHYAWAY)
packs[PACK091_GECKIT_PACK_2] = FormationPack(FORM0163_TWO_GECKIT_ONE_SPINTHRA_ONE_KRIFFID, FORM0162_TWO_GECKIT_TWO_CHEWY_ONE_SHYAWAY, FORM0161_TWO_GECKIT_ONE_SPINTHRA)
packs[PACK092_BIRDY_PACK_1] = FormationPack(FORM0164_ONE_BIRDY_ONE_HEAVYTROOPA, FORM0165_THREE_BIRDY, FORM0166_TWO_BIRDY_ONE_HEAVYTROOPA)
packs[PACK093_BIRDY_PACK_2] = FormationPack(FORM0167_FIVE_BIRDY, FORM0166_TWO_BIRDY_ONE_HEAVYTROOPA, FORM0165_THREE_BIRDY)
packs[PACK094_BLUEBIRD_PACK_1] = FormationPack(FORM0168_TWO_BLUEBIRD, FORM0169_TWO_BLUEBIRD_ONE_HEAVYTROOPA, FORM0170_FOUR_BLUEBIRD)
packs[PACK095_BLUEBIRD_PACK_2] = FormationPack(FORM0171_TWO_BLUEBIRD_ONE_HEAVYTROOPA, FORM0170_FOUR_BLUEBIRD, FORM0169_TWO_BLUEBIRD_ONE_HEAVYTROOPA)
packs[PACK096_PINWHEEL_WITH_MUCKLE] = FormationPack(FORM0172_ONE_PINWHEEL, FORM0173_ONE_PINWHEEL_ONE_MUCKLE, FORM0174_TWO_PINWHEEL_TWO_MUCKLE)
packs[PACK097_PINWHEEL_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0175_THREE_PINWHEEL_TWO_SLINGSHY, FORM0174_TWO_PINWHEEL_TWO_MUCKLE, FORM0173_ONE_PINWHEEL_ONE_MUCKLE)
packs[PACK098_SHAMAN_WITH_ORBISON_JAWFUL] = FormationPack(FORM0176_TWO_SHAMAN, FORM0177_ONE_SHAMAN_ONE_ORBISON_ONE_JAWFUL, FORM0178_TWO_SHAMAN_ONE_JAWFUL)
packs[PACK099_SHAMAN_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0179_TWO_SHAMAN_TWO_SLINGSHY_ONE_JAWFUL, FORM0178_TWO_SHAMAN_ONE_JAWFUL, FORM0177_ONE_SHAMAN_ONE_ORBISON_ONE_JAWFUL)
packs[PACK100_SLINGSHY_PACK_1] = FormationPack(FORM0180_ONE_SLINGSHY_ONE_ORBISON, FORM0181_ONE_SLINGSHY_TWO_ORBISON, FORM0182_ONE_SLINGSHY_TWO_ORBISON_ONE_JAWFUL)
packs[PACK101_SLINGSHY_PACK_2] = FormationPack(FORM0183_TWO_SLINGSHY_TWO_PINWHEEL_ONE_MUCKLE, FORM0182_ONE_SLINGSHY_TWO_ORBISON_ONE_JAWFUL, FORM0181_ONE_SLINGSHY_TWO_ORBISON)
packs[PACK102_MAGMUS_WITH_ARMOREDANT_OERLIKON] = FormationPack(FORM0184_ONE_MAGMUS, FORM0185_TWO_MAGMUS_ONE_ARMOREDANT, FORM0186_THREE_MAGMUS_TWO_OERLIKON)
packs[PACK103_MAGMUS_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0187_TWO_MAGMUS_TWO_ARMOREDANT, FORM0186_THREE_MAGMUS_TWO_OERLIKON, FORM0185_TWO_MAGMUS_ONE_ARMOREDANT)
packs[PACK104_OERLIKON_PACK_1] = FormationPack(FORM0188_ONE_OERLIKON_ONE_VOMER, FORM0189_THREE_OERLIKON, FORM0190_ONE_OERLIKON_ONE_CHAINEDKONG_ONE_ARMOREDANT)
packs[PACK105_OERLIKON_PACK_2] = FormationPack(FORM0191_TWO_OERLIKON_ONE_CHAINEDKONG, FORM0190_ONE_OERLIKON_ONE_CHAINEDKONG_ONE_ARMOREDANT, FORM0189_THREE_OERLIKON)
packs[PACK106_PYROSPHERE_WITH_CHAINEDKONG_CORKPEDITE] = FormationPack(FORM0192_THREE_PYROSPHERE, FORM0193_TWO_PYROSPHERE_ONE_CHAINEDKONG, FORM0194_ONE_CORKPEDITE_ONE_BODY_ONE_PYROSPHERE)
packs[PACK107_PYROSPHERE_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0195_TWO_PYROSPHERE_ONE_STUMPET, FORM0194_ONE_CORKPEDITE_ONE_BODY_ONE_PYROSPHERE, FORM0193_TWO_PYROSPHERE_ONE_CHAINEDKONG)
packs[PACK108_VOMER_PACK_1] = FormationPack(FORM0196_ONE_VOMER_ONE_CHAINEDKONG, FORM0197_THREE_VOMER, FORM0198_ONE_CORKPEDITE_ONE_BODY_ONE_VOMER)
packs[PACK109_VOMER_PACK_2] = FormationPack(FORM0199_TWO_VOMER_ONE_STUMPET, FORM0198_ONE_CORKPEDITE_ONE_BODY_ONE_VOMER, FORM0197_THREE_VOMER)
packs[PACK110_TERRACOTTA_PACK_1] = FormationPack(FORM0200_ONE_TERRACOTTA, FORM0201_THREE_TERRACOTTA, FORM0202_ONE_TERRACOTTA_TWO_FORKIES)
packs[PACK111_TERRACOTTA_PACK_2] = FormationPack(FORM0203_TWO_TERRACOTTA_TWO_GUGOOMBA_ONE_FORKIES, FORM0202_ONE_TERRACOTTA_TWO_FORKIES, FORM0201_THREE_TERRACOTTA)
packs[PACK112_MALAKOOPA_PACK_1] = FormationPack(FORM0204_ONE_MALAKOOPA_ONE_TUBOTROOPA, FORM0205_TWO_MALAKOOPA_ONE_TUBOTROOPA, FORM0206_TWO_MALAKOOPA_ONE_TERRACOTTA_ONE_TUBOTROOPA)
packs[PACK113_MALAKOOPA_PACK_2] = FormationPack(FORM0207_ONE_MALAKOOPA_TWO_TUBOTROOPA, FORM0206_TWO_MALAKOOPA_ONE_TERRACOTTA_ONE_TUBOTROOPA, FORM0205_TWO_MALAKOOPA_ONE_TUBOTROOPA)
packs[PACK114_GUGOOMBA_PACK_1] = FormationPack(FORM0208_TWO_GUGOOMBA, FORM0209_TWO_GUGOOMBA_ONE_STARCRUSTER, FORM0210_ONE_GUGOOMBA_ONE_FORKIES_ONE_STARCRUSTER)
packs[PACK115_GUGOOMBA_PACK_2] = FormationPack(FORM0211_TWO_GUGOOMBA_TWO_MALAKOOPA_TWO_TERRACOTTA, FORM0210_ONE_GUGOOMBA_ONE_FORKIES_ONE_STARCRUSTER, FORM0209_TWO_GUGOOMBA_ONE_STARCRUSTER)
packs[PACK116_BIGBERTHA_PACK_1] = FormationPack(FORM0212_ONE_BIGBERTHA, FORM0213_TWO_BIGBERTHA, FORM0214_ONE_BIGBERTHA_ONE_FORKIES)
packs[PACK117_BIGBERTHA_PACK_2] = FormationPack(FORM0215_TWO_BIGBERTHA_ONE_TERRACOTTA, FORM0214_ONE_BIGBERTHA_ONE_FORKIES, FORM0213_TWO_BIGBERTHA)
packs[PACK118_SHIP_POSTGAME] = FormationPack(FORM0216_ONE_JOHNNYENEMY2)
packs[PACK119_DOJO_POSTGAME] = FormationPack(FORM0217_ONE_JINXENEMY4_ONE_TEAMGAUGE)
packs[PACK120_NINJA_PACK_1] = FormationPack(FORM0218_ONE_NINJA, FORM0219_ONE_NINJA_ONE_DOPPEL, FORM0220_TWO_NINJA_ONE_HIPPOPO)
packs[PACK121_NINJA_PACK_2] = FormationPack(FORM0221_FIVE_NINJA, FORM0220_TWO_NINJA_ONE_HIPPOPO, FORM0219_ONE_NINJA_ONE_DOPPEL)
packs[PACK122_SPRINGER_PACK_1] = FormationPack(FORM0222_ONE_SPRINGER_ONE_GLUMREAPER, FORM0223_TWO_SPRINGER_ONE_PUPPOX, FORM0222_ONE_SPRINGER_ONE_GLUMREAPER)
packs[PACK123_SPRINGER_PACK_2] = FormationPack(FORM0224_ONE_SPRINGER_TWO_PUPPOX, FORM0223_TWO_SPRINGER_ONE_PUPPOX, FORM0222_ONE_SPRINGER_ONE_GLUMREAPER)
packs[PACK124_MADMALLET_PACK_1] = FormationPack(FORM0225_TWO_MADMALLET, FORM0226_THREE_MADMALLET, FORM0227_FIVE_MADMALLET)
packs[PACK125_MADMALLET_PACK_2] = FormationPack(FORM0227_FIVE_MADMALLET, FORM0226_THREE_MADMALLET, FORM0225_TWO_MADMALLET)
packs[PACK126_POUNDER_PACK_1] = FormationPack(FORM0228_ONE_POUNDER, FORM0229_THREE_POUNDER, FORM0230_FIVE_POUNDER)
packs[PACK126_POUNDER_PACK_2] = FormationPack(FORM0230_FIVE_POUNDER, FORM0229_THREE_POUNDER, FORM0228_ONE_POUNDER)
packs[PACK128_POUNDETTE_PACK_1] = FormationPack(FORM0231_ONE_POUNDETTE, FORM0232_THREE_POUNDETTE, FORM0233_SIX_POUNDETTE)
packs[PACK128_POUNDETTE_PACK_2] = FormationPack(FORM0233_SIX_POUNDETTE, FORM0232_THREE_POUNDETTE, FORM0231_ONE_POUNDETTE)
packs[PACK130_AMEBOIDS] = FormationPack(FORM0234_FIVE_AMEBOID)
packs[PACK131_AMEBOIDS_DUPE] = FormationPack(FORM0234_FIVE_AMEBOID)
packs[PACK132_GLUMREAPER_WITH_HIPPOPO_DOPPEL] = FormationPack(FORM0235_THREE_GLUMREAPER, FORM0236_ONE_GLUMREAPER_ONE_HIPPOPO, FORM0237_TWO_GLUMREAPER_TWO_DOPPEL)
packs[PACK133_GLUMREAPER_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(FORM0238_TWO_GLUMREAPER_TWO_LILBOO, FORM0237_TWO_GLUMREAPER_TWO_DOPPEL, FORM0236_ONE_GLUMREAPER_ONE_HIPPOPO)
packs[PACK134_LILBOO_PACK_1] = FormationPack(FORM0239_ONE_LILBOO, FORM0240_TWO_LILBOO_ONE_HIPPOPO, FORM0241_TWO_LILBOO_ONE_PUPPOX_ONE_DOPPEL)
packs[PACK135_LILBOO_PACK_2] = FormationPack(FORM0242_FOUR_LILBOO, FORM0241_TWO_LILBOO_ONE_PUPPOX_ONE_DOPPEL, FORM0240_TWO_LILBOO_ONE_HIPPOPO)
packs[PACK136_JABITS_HAMMERS_PACK_1] = FormationPack(FORM0243_ONE_JABIT_ONE_MADMALLET, FORM0244_ONE_JABIT_ONE_POUNDER_ONE_POUNDETTE, FORM0245_SIX_JABIT)
packs[PACK137_JABITS_HAMMERS_PACK_2] = FormationPack(FORM0246_TWO_JABIT_TWO_MADMALLET_TWO_POUNDETTE, FORM0245_SIX_JABIT, FORM0244_ONE_JABIT_ONE_POUNDER_ONE_POUNDETTE)
packs[PACK138_RATFUNKS_ONLY] = FormationPack(FORM0247_THREE_RATFUNK, FORM0248_FIVE_RATFUNK, FORM0247_THREE_RATFUNK)
packs[PACK139_ARTICHOKERS_ONLY] = FormationPack(FORM0249_ONE_ARTICHOKER, FORM0250_TWO_ARTICHOKER, FORM0249_ONE_ARTICHOKER)
packs[PACK140_MINES_BOSS_2] = FormationPack(FORM0251_ONE_PUNCHINELLO_FOUR_MICROBOMB)
packs[PACK141_MINES_HENCHMAN_LEFT] = FormationPack(FORM0138_THREE_CROOK, FORM0139_FIVE_CROOK, FORM0138_THREE_CROOK)
packs[PACK142_MINES_HENCHMAN_MIDDLE] = FormationPack(FORM0138_THREE_CROOK, FORM0139_FIVE_CROOK, FORM0138_THREE_CROOK)
packs[PACK143_TOWER_FIREBALLS] = FormationPack(FORM0252_TWO_FIREBALL, FORM0253_THREE_FIREBALL, FORM0252_TWO_FIREBALL)
packs[PACK144_STUMPET_ENCOUNTER] = FormationPack(FORM0254_ONE_STUMPET_TWO_MAGMUS, FORM0255_ONE_STUMPET_THREE_MAGMUS, FORM0254_ONE_STUMPET_TWO_MAGMUS)
packs[PACK145_CORKPEDITE_ENCOUNTER] = FormationPack(FORM0256_ONE_CORKPEDITE_ONE_BODY_ONE_OERLIKON, FORM0257_ONE_CORKPEDITE_ONE_BODY_TWO_OERLIKON, FORM0256_ONE_CORKPEDITE_ONE_BODY_ONE_OERLIKON)
packs[PACK146_FACTORY_BOSS_RUSH_1] = FormationPack(FORM0258_ONE_CLERK_TWO_MADMALLETENEMYHENCHMAN)
packs[PACK147_FACTORY_BOSS_RUSH_2] = FormationPack(FORM0259_ONE_MANAGER_THREE_POUNDERENEMYHENCHMAN)
packs[PACK148_FACTORY_BOSS_RUSH_3] = FormationPack(FORM0260_ONE_DIRECTOR_FOUR_POUNDETTEENEMYHENCHMAN)
packs[PACK149_FACTORY_BOSS_RUSH_4] = FormationPack(FORM0261_ONE_GUNYOLK_ONE_FACTORYCHIEF)
packs[PACK150_FACTORY_BOSS_RUSH_HENCHMAN] = FormationPack(FORM0262_THREE_MADMALLETENEMYHENCHMAN)
packs[PACK151_UNUSED] = FormationPack(FORM0263_ONE_APPRENTICE)
packs[PACK152_MINES_BOSS_ROOM_HENCHMAN] = FormationPack(FORM0365_THREE_BOBOMBHENCHMAN)
packs[PACK153_UNUSED] = FormationPack(FORM0264_THREE_MACHINEMADEDRILLBIT)
packs[PACK154_UNUSED] = FormationPack(FORM0265_ONE_SHYGUY)
packs[PACK155_POSSIBLY_UNUSED] = FormationPack(FORM0226_THREE_MADMALLET)
packs[PACK156_SEWER_CHEST_FIGHT] = FormationPack(FORM0266_ONE_PANDORITE)
packs[PACK157_SHIP_CHEST_FIGHT] = FormationPack(FORM0267_ONE_HIDON_FOUR_GOOMBETTE)
packs[PACK158_VALLEY_CHEST_FIGHT] = FormationPack(FORM0268_ONE_BOXBOY_ONE_FAUTSO)
packs[PACK159_SIX_DOOR_RUSH_FIGHT] = FormationPack(FORM0269_ONE_CHESTER_ONE_BAHAMUTTENEMY2)
packs[PACK160_SLOTS_CHEST_FIGHT] = FormationPack(FORM0364_ONE_BOXBOY_ONE_FAUTSO)
packs[PACK161_TOWER_FIRST_FIGHT] = FormationPack(FORM0271_ONE_BOOSTER_THREE_SNIFITENEMYHENCHMAN)
packs[PACK162__UNUSED] = FormationPack(FORM0272_ONE_BOOSTERENEMY2)
packs[PACK163_BANDITS_WAY_BOSS] = FormationPack(FORM0273_ONE_CROCO1)
packs[PACK164_MINES_FIRST_BOSS] = FormationPack(FORM0274_ONE_CROCO2)
packs[PACK165_UNUSED] = FormationPack(FORM0275_ONE_MACHINEMADEAXEMBLACK)
packs[PACK166_SHIP_SECOND_BOSS] = FormationPack(FORM0276_ONE_JOHNNY_FOUR_BANDANABLUE_TWO_WATERCRYSTAL)
packs[PACK167_SHIP_FIRST_BOSS] = FormationPack(FORM0277_ONE_KINGCALAMARI_TWO_TENTACLESENEMY2_THREE_TENTACLES)
packs[PACK168_SEWER_BOSS] = FormationPack(FORM0278_ONE_BELOME1)
packs[PACK169_TEMPLE_BOSS] = FormationPack(FORM0279_ONE_BELOME2_ONE_MARIOCLONE_ONE_TOADSTOOL2)
packs[PACK170_UNUSED] = FormationPack(FORM0280_ONE_TERRAPIN)
packs[PACK171_NIMBUS_CASTLE_THIRD_BOSS] = FormationPack(FORM0281_ONE_VALENTINA_ONE_DODO)
packs[PACK172_VOLCANO_FIRST_BOSS] = FormationPack(FORM0282_ONE_CZARDRAGON_ONE_ZOMBONE_FOUR_HELIO)
packs[PACK173_VALLEY_BOSS] = FormationPack(FORM0283_FIVE_SMILAX_ONE_MEGASMILAX)
packs[PACK174_FACTORY_FIRST_BOSS] = FormationPack(FORM0284_ONE_COUNTDOWN_TWO_DINGALING)
packs[PACK175_NIMBUS_CASTLE_SECOND_BOSS] = FormationPack(FORM0285_ONE_BIRDETTA_ONE_SHELLY_FOUR_EGGBERT)
packs[PACK176_CHAPEL_BOSS] = FormationPack(FORM0286_ONE_BUNDT_ONE_RASPBERRY_TWO_TORTE)
packs[PACK177_TOWER_SECOND_BOSS] = FormationPack(FORM0287_ONE_KNIFEGUY_ONE_GRATEGUY)
packs[PACK178_DOJO_FIGHT_1] = FormationPack(FORM0288_ONE_JINX1)
packs[PACK179_MUSHROOM_KINGDOM_BOSS] = FormationPack(FORM0289_ONE_MACK_FOUR_BODYGUARD)
packs[PACK180_SEASIDE_BOSS] = FormationPack(FORM0290_ONE_YARIDOVICH_ONE_YARIDOVICHMIRAGE)
packs[PACK181_FOREST_BOSS] = FormationPack(FORM0291_ONE_BOWYER)
packs[PACK182_VOLCANO_BOSS] = FormationPack(FORM0292_ONE_AXEMRANGERS_ONE_AXEMRED_ONE_AXEMBLACK_ONE_AXEMPINK_ONE_AXEMGREEN_ONE_AXEMYELLOW)
packs[PACK183_MUSHROOM_WAY_BOSS] = FormationPack(FORM0293_TWO_HAMMERBRO)
packs[PACK184_FACTORY_SECOND_BOSS] = FormationPack(FORM0294_ONE_CLOAKER_ONE_DOMINO_ONE_MADADDER)
packs[PACK185_FINAL_BOSS] = FormationPack(FORM0295_ONE_SMITHY1_ONE_SMELTER_TWO_MACHINEMADEBODYGUARD)
packs[PACK186_KEEP_THIRD_BOSS] = FormationPack(FORM0296_ONE_EXOR_ONE_NEOSQUID_ONE_RIGHTEYE_ONE_LEFTEYE)
packs[PACK187_DOJO_SECOND_BOSS] = FormationPack(FORM0297_ONE_JINX2)
packs[PACK188_DOJO_THIRD_BOSS] = FormationPack(FORM0298_ONE_JINX3)
packs[PACK189_DOJO_PREFIGHT] = FormationPack(FORM0299_ONE_JAGGER)
packs[PACK190_UNUSED] = FormationPack(FORM0192_THREE_PYROSPHERE)
packs[PACK191_HEAVY_TROOPAS] = FormationPack(FORM0300_THREE_HEAVYTROOPA)
packs[PACK192_UNUSED] = FormationPack(FORM0301)
packs[PACK193_UNUSED] = FormationPack(FORM0302_FOUR_HELIO)
packs[PACK194_UNUSED] = FormationPack(FORM0303_TWO_BODYGUARD, FORM0304_THREE_BODYGUARD, FORM0303_TWO_BODYGUARD)
packs[PACK195_UNUSED] = FormationPack(FORM0303_TWO_BODYGUARD, FORM0304_THREE_BODYGUARD, FORM0304_THREE_BODYGUARD)
packs[PACK196_UNUSED] = FormationPack(FORM0305_ONE_GENOCLONE)
packs[PACK197_UNUSED] = FormationPack(FORM0306_ONE_BOWSERCLONE)
packs[PACK198_UNUSED] = FormationPack(FORM0307_ONE_TOADSTOOL2)
packs[PACK199_CROOKS_ONLY] = FormationPack(FORM0138_THREE_CROOK, FORM0139_FIVE_CROOK, FORM0138_THREE_CROOK)
packs[PACK200_UNUSED] = FormationPack(FORM0308_ONE_MARIOCLONE)
packs[PACK201_UNUSED] = FormationPack(FORM0165_THREE_BIRDY, FORM0167_FIVE_BIRDY, FORM0165_THREE_BIRDY)
packs[PACK202_UNUSED] = FormationPack(FORM0309_ONE_MALLOWCLONE)
packs[PACK203_UNUSED] = FormationPack(FORM0310_ONE_MACHINEMADEAXEMPINK_ONE_MACHINEMADEAXEMRED_ONE_MACHINEMADEAXEMGREEN, FORM0311_TWO_MACHINEMADEAXEMBLACK_TWO_MACHINEMADEAXEMYELLOW, FORM0310_ONE_MACHINEMADEAXEMPINK_ONE_MACHINEMADEAXEMRED_ONE_MACHINEMADEAXEMGREEN)
packs[PACK204_UNUSED] = FormationPack(FORM0312_THREE_BLOOBER)
packs[PACK205_UNUSED] = FormationPack(FORM0168_TWO_BLUEBIRD, FORM0170_FOUR_BLUEBIRD, FORM0168_TWO_BLUEBIRD)
packs[PACK206_DESERT_SHOGUNS] = FormationPack(FORM0313_THREE_SHOGUN)
packs[PACK207_LANDS_END_CLOUD] = FormationPack(FORM0314_ONE_FORMLESS_ONE_MOKURA)
packs[PACK208_NIMBUS_CASTLE_FIRST_BOSS] = FormationPack(FORM0315_ONE_DODOENEMYSOLO)
packs[PACK209_KEEP_FIRST_BOSS] = FormationPack(FORM0316_ONE_KAMEK_ONE_TERRAPIN)
packs[PACK210_KEEP_SECOND_BOSS] = FormationPack(FORM0317_ONE_BOOMER_TWO_HANGINSHY)
packs[PACK211_MACHINE_MACK_PACK] = FormationPack(FORM0318_ONE_MACHINEMADEMACK_FOUR_MACHINEMADEBODYGUARD)
packs[PACK212_MACHINE_BOWYER_PACK] = FormationPack(FORM0319_ONE_MACHINEMADEBOWYER)
packs[PACK213_MACHINE_YARIDOVICH_PACK] = FormationPack(FORM0320_ONE_MACHINEMADEYARIDOVICH_FOUR_MACHINEMADEDRILLBIT)
packs[PACK214_FACTORY_MACHINE_AXEMS] = FormationPack(FORM0310_ONE_MACHINEMADEAXEMPINK_ONE_MACHINEMADEAXEMRED_ONE_MACHINEMADEAXEMGREEN, FORM0311_TWO_MACHINEMADEAXEMBLACK_TWO_MACHINEMADEAXEMYELLOW, FORM0310_ONE_MACHINEMADEAXEMPINK_ONE_MACHINEMADEAXEMRED_ONE_MACHINEMADEAXEMGREEN)
packs[PACK215_SMITHY_2_PACK] = FormationPack(FORM0321_ONE_SMITHYBODY_ONE_SMITHY2)
packs[PACK216_MONSTRO_DOOR_BOSS] = FormationPack(FORM0322_ONE_CULEX_ONE_FIRECRYSTAL_ONE_WATERCRYSTAL_ONE_EARTHCRYSTAL_ONE_WINDCRYSTAL)
packs[PACK217_UNUSED] = FormationPack(FORM0323_ONE_FIRECRYSTAL)
packs[PACK218_UNUSED] = FormationPack(FORM0324_ONE_WATERCRYSTAL)
packs[PACK219_UNUSED] = FormationPack(FORM0325_ONE_EARTHCRYSTAL)
packs[PACK220_UNUSED] = FormationPack(FORM0326_ONE_WINDCRYSTAL)
packs[PACK221_UNUSED] = FormationPack(FORM0327_THREE_GOOMBETTE)
packs[PACK222_UNUSED] = FormationPack(FORM0056_ONE_PIRANHAPLANT, FORM0058_THREE_PIRANHAPLANT, FORM0059_FIVE_PIRANHAPLANT)
packs[PACK223_UNUSED] = FormationPack(FORM0328_ONE_EGGBERT, FORM0329_THREE_EGGBERT, FORM0330_FOUR_EGGBERT)
packs[PACK224_OBSTACLE_TERRA_COTTA] = FormationPack(FORM0331_FOUR_TERRACOTTA)
packs[PACK225_OBSTACLE_OERLIKON] = FormationPack(FORM0332_TWO_OERLIKON_ONE_STARCRUSTER)
packs[PACK226_OBSTACLE_SACKIT] = FormationPack(FORM0333_ONE_SACKIT_TWO_BIGBERTHA)
packs[PACK227_OBSTACLE_CHOW] = FormationPack(FORM0334_TWO_CHOW_ONE_FORKIES)
packs[PACK228_OBSTACLE_ALLEYRAT] = FormationPack(FORM0335_ONE_ALLEYRAT_TWO_ARMOREDANT)
packs[PACK229_OBSTACLE_BLOOBER] = FormationPack(FORM0336_THREE_BLOOBER_ONE_STARCRUSTER)
packs[PACK230_OBSTACLE_STINGER] = FormationPack(FORM0337_FOUR_STINGER)
packs[PACK231_OBSTACLE_GECKIT] = FormationPack(FORM0338_TWO_GECKIT_ONE_CHAINEDKONG)
packs[PACK232_OBSTACLE_ROBOMB] = FormationPack(FORM0339_ONE_ROBOMB_TWO_BIGBERTHA)
packs[PACK233_OBSTACLE_VOMER] = FormationPack(FORM0340_FOUR_VOMER)
packs[PACK234_OBSTACLE_MAGMUS] = FormationPack(FORM0341_TWO_MAGMUS_TWO_PULSAR)
packs[PACK235_UNUSED] = FormationPack(FORM0342)
packs[PACK236_OBSTACLE_GUGOOMBA] = FormationPack(FORM0343_FIVE_GUGOOMBA)
packs[PACK237_OBSTACLE_MALAKOOPA] = FormationPack(FORM0344_TWO_MALAKOOPA_ONE_TUBOTROOPA)
packs[PACK238_OBSTACLE_BIGBOO] = FormationPack(FORM0345_TWO_THEBIGBOO_TWO_ORBISON)
packs[PACK239_OBSTACLE_SLINGSHY] = FormationPack(FORM0346_FIVE_SLINGSHY)
packs[PACK240_OBSTACLE_CHEWY] = FormationPack(FORM0347_TWO_CHEWY_TWO_SHYAWAY)
packs[PACK241_OBSTACLE_KIPPER] = FormationPack(FORM0348_ONE_MRKIPPER_TWO_MUCKLE)
packs[PACK242_OBSTACLE_AMANITA] = FormationPack(FORM0349_TWO_AMANITA_ONE_ORBISON)
packs[PACK243_OBSTACLE_GREAPER] = FormationPack(FORM0350_TWO_GREAPER_ONE_GLUMREAPER)
packs[PACK244_OBSTACLE_PYROSPHERE] = FormationPack(FORM0351_THREE_PYROSPHERE)
packs[PACK245_OBSTACLE_LAKITU] = FormationPack(FORM0352_THREE_LAKITU)
packs[PACK246_OBSTACLE_ZEOSTAR] = FormationPack(FORM0353_TWO_ZEOSTAR_TWO_SHAMAN)
packs[PACK247_OBSTACLE_SHAMANS] = FormationPack(FORM0354_SIX_SHAMAN)
packs[PACK248_UNUSED] = FormationPack(FORM0355_ONE_AXEMBLACK)
packs[PACK249_UNUSED] = FormationPack(FORM0356_ONE_AXEMPINK)
packs[PACK250_UNUSED] = FormationPack(FORM0357_ONE_AXEMYELLOW)
packs[PACK251_UNUSED] = FormationPack(FORM0358_ONE_AXEMGREEN)
packs[PACK252_UNUSED] = FormationPack(FORM0359_ONE_DINGALING)
packs[PACK253_UNUSED] = FormationPack(FORM0360_ONE_DRILLBIT)
packs[PACK254_UNUSED] = FormationPack(FORM0361_ONE_DRILLBIT)
packs[PACK255_UNUSED] = FormationPack(FORM0301)

# Pack Collection
pack_collection = PackCollection(packs[:256])

