"""ROM's PackCollection disassembled from the original game."""

from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (
    Formation,
    FormationMember,
    FormationPack,
    PackCollection)
from smrpgpatchbuilder.datatypes.battles.music import (
    NormalBattleMusic,
    MidbossMusic,
    BossMusic,
    Smithy1Music,
    CorndillyMusic,
    BoosterHillMusic,
    VolcanoMusic,
    CulexMusic)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import Battlefield
from ..enemies.enemies import *
from ..variables.pack_names import *
from ..variables.battle_event_names import *


# Initialize packs array with None values
packs: list[FormationPack] = [None] * 256 # type: ignore

#
packs[PACK000_TOWER_HENCHMAN_1] = FormationPack(
    Formation(
        members=[
            FormationMember(SNIFITEnemyStatic, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
        can_run_away=False
    )
)
#
packs[PACK001_TOWER_HENCHMAN_2] = FormationPack(
    Formation(
        members=[
            FormationMember(SNIFITEnemyStatic, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
        can_run_away=False
    )
)
packs[PACK002_SPIKEYS_AND_TROOPAS] = FormationPack(
    Formation(
        members=[
            FormationMember(SPIKEYEnemy, 135, 127),
            FormationMember(SPIKEYEnemy, 199, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPIKEYEnemy, 135, 119),
            FormationMember(SKYTROOPAEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPIKEYEnemy, 135, 119),
            FormationMember(SKYTROOPAEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK003_SPIKEYS_AND_FROGS] = FormationPack(
    Formation(
        members=[
            FormationMember(SPIKEYEnemy, 135, 119),
            FormationMember(SPIKEYEnemy, 199, 119),
            FormationMember(SPIKEYEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPIKEYEnemy, 135, 119),
            FormationMember(SPIKEYEnemy, 199, 151),
            FormationMember(FROGOGEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPIKEYEnemy, 135, 119),
            FormationMember(SPIKEYEnemy, 199, 151),
            FormationMember(FROGOGEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK004_JUST_TROOPAS] = FormationPack(
    Formation(
        members=[
            FormationMember(SKYTROOPAEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SKYTROOPAEnemy, 135, 119),
            FormationMember(SKYTROOPAEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SKYTROOPAEnemy, 135, 119),
            FormationMember(SKYTROOPAEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK005_TROOPAS_WITH_FROGS_OR_GOOMBAS] = FormationPack(
    Formation(
        members=[
            FormationMember(SKYTROOPAEnemy, 167, 103),
            FormationMember(SKYTROOPAEnemy, 231, 135),
            None,
            FormationMember(GOOMBAEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SKYTROOPAEnemy, 199, 151),
            FormationMember(SKYTROOPAEnemy, 135, 119),
            FormationMember(FROGOGEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SKYTROOPAEnemy, 135, 119),
            FormationMember(SKYTROOPAEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK006_JUST_GOOMBAS] = FormationPack(
    Formation(
        members=[
            FormationMember(GOOMBAEnemy, 135, 119),
            FormationMember(GOOMBAEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GOOMBAEnemy, 167, 111),
            FormationMember(GOOMBAEnemy, 167, 135),
            FormationMember(GOOMBAEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GOOMBAEnemy, 135, 119),
            FormationMember(GOOMBAEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK007_GOOMBAS_WITH_FROGS_OR_SPIKEYS] = FormationPack(
    Formation(
        members=[
            FormationMember(GOOMBAEnemy, 167, 135),
            FormationMember(FROGOGEnemy, 167, 111),
            FormationMember(SPIKEYEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GOOMBAEnemy, 167, 111),
            FormationMember(GOOMBAEnemy, 215, 135),
            FormationMember(SPIKEYEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GOOMBAEnemy, 167, 111),
            FormationMember(GOOMBAEnemy, 167, 135),
            FormationMember(GOOMBAEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK008_K9S_WITH_SPIKEYS] = FormationPack(
    Formation(
        members=[
            FormationMember(K9Enemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(K9Enemy, 199, 159),
            FormationMember(K9Enemy, 151, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(K9Enemy, 135, 119),
            FormationMember(K9Enemy, 199, 151),
            FormationMember(SPIKEYEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK009_K9S_WITH_SPIKEYS_OR_FROGS] = FormationPack(
    Formation(
        members=[
            FormationMember(K9Enemy, 183, 127),
            FormationMember(FROGOGEnemy, 215, 143),
            FormationMember(FROGOGEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(K9Enemy, 135, 119),
            FormationMember(K9Enemy, 199, 151),
            FormationMember(SPIKEYEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(K9Enemy, 199, 159),
            FormationMember(K9Enemy, 151, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK010_KINGDOM_HENCHMEN_1] = FormationPack(
    # field
    Formation(
        members=[
            FormationMember(SHYSTEREnemy, 167, 119),
            FormationMember(SHYSTEREnemy, 199, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SHYSTEREnemy, 151, 111),
            FormationMember(SHYSTEREnemy, 215, 143),
            FormationMember(SHYSTEREnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SHYSTEREnemy, 167, 119),
            FormationMember(SHYSTEREnemy, 199, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK011_KINGDOM_HENCHMEN_2] = FormationPack(
    # field
    Formation(
        members=[
            FormationMember(SHYSTEREnemy, 167, 119),
            FormationMember(SHYSTEREnemy, 199, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SHYSTEREnemy, 151, 111),
            FormationMember(SHYSTEREnemy, 215, 143),
            FormationMember(SHYSTEREnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SHYSTEREnemy, 151, 111),
            FormationMember(SHYSTEREnemy, 215, 143),
            FormationMember(SHYSTEREnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK012_RATFUNKS_WITH_SHADOW_OR_HOBGOBLIN] = FormationPack(
    Formation(
        members=[
            FormationMember(RATFUNKEnemy, 199, 143),
            FormationMember(RATFUNKEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(RATFUNKEnemy, 135, 119),
            FormationMember(RATFUNKEnemy, 199, 151),
            FormationMember(SHADOWEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(RATFUNKEnemy, 135, 119),
            FormationMember(RATFUNKEnemy, 199, 151),
            FormationMember(HOBGOBLINEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK013_RATFUNKS_ALWAYS_WITH_ONE_OTHER_MONSTER] = FormationPack(
    Formation(
        members=[
            FormationMember(RATFUNKEnemy, 167, 135),
            None,
            FormationMember(HOBGOBLINEnemy, 167, 103),
            FormationMember(HOBGOBLINEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(RATFUNKEnemy, 135, 119),
            FormationMember(RATFUNKEnemy, 199, 151),
            FormationMember(HOBGOBLINEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(RATFUNKEnemy, 135, 119),
            FormationMember(RATFUNKEnemy, 199, 151),
            FormationMember(SHADOWEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK014_BIGBOO_ALWAYS_WITH_ONE_OTHER_MONSTER_1] = FormationPack(
    Formation(
        members=[
            FormationMember(THEBIGBOOEnemy, 151, 119),
            FormationMember(SHADOWEnemy, 199, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(THEBIGBOOEnemy, 151, 119),
            FormationMember(SHADOWEnemy, 199, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(THEBIGBOOEnemy, 119, 119),
            FormationMember(SHADOWEnemy, 167, 135),
            FormationMember(HOBGOBLINEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK015_BIGBOO_ALWAYS_WITH_ONE_OTHER_MONSTER_2] = FormationPack(
    Formation(
        members=[
            FormationMember(THEBIGBOOEnemy, 231, 135),
            FormationMember(THEBIGBOOEnemy, 151, 143),
            FormationMember(THEBIGBOOEnemy, 167, 103),
            FormationMember(SHADOWEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(THEBIGBOOEnemy, 119, 119),
            FormationMember(SHADOWEnemy, 167, 135),
            FormationMember(HOBGOBLINEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(THEBIGBOOEnemy, 151, 119),
            FormationMember(SHADOWEnemy, 199, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK016_MULTIPLE_GOBYS_BIASED_2] = FormationPack(
    Formation(
        members=[
            FormationMember(GOBYEnemy, 135, 119),
            FormationMember(GOBYEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GOBYEnemy, 135, 119),
            FormationMember(GOBYEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GOBYEnemy, 151, 119),
            FormationMember(GOBYEnemy, 215, 119),
            FormationMember(GOBYEnemy, 183, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK017_MULTIPLE_GOBYS_BIASED_3] = FormationPack(
    Formation(
        members=[
            FormationMember(GOBYEnemy, 151, 119),
            FormationMember(GOBYEnemy, 215, 119),
            FormationMember(GOBYEnemy, 183, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GOBYEnemy, 151, 119),
            FormationMember(GOBYEnemy, 215, 119),
            FormationMember(GOBYEnemy, 183, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GOBYEnemy, 135, 119),
            FormationMember(GOBYEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK018_CROOKS_WITH_SHYGUY_OR_SNAPDRAGON] = FormationPack(
    Formation(
        members=[
            FormationMember(CROOKEnemyStatic, 167, 111),
            FormationMember(CROOKEnemyStatic, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CROOKEnemyStatic, 199, 143),
            FormationMember(CROOKEnemyStatic, 151, 119),
            FormationMember(SHYGUYEnemyStatic, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CROOKEnemyStatic, 183, 127),
            FormationMember(SNAPDRAGONEnemy, 151, 111),
            FormationMember(SNAPDRAGONEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK019_CROOKS_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(CROOKEnemyStatic, 199, 159),
            None,
            None,
            FormationMember(STARSLAPEnemy, 215, 127),
            FormationMember(ARACHNEEnemy, 167, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CROOKEnemyStatic, 183, 127),
            FormationMember(SNAPDRAGONEnemy, 151, 111),
            FormationMember(SNAPDRAGONEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CROOKEnemyStatic, 199, 143),
            FormationMember(CROOKEnemyStatic, 151, 119),
            FormationMember(SHYGUYEnemyStatic, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK020_SHYGUYS_WITH_STARSLAP_OR_SNAPDRAGON] = FormationPack(
    Formation(
        members=[
            FormationMember(SHYGUYEnemyStatic, 151, 111),
            None,
            FormationMember(STARSLAPEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SHYGUYEnemyStatic, 151, 111),
            None,
            FormationMember(STARSLAPEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SHYGUYEnemyStatic, 135, 103),
            FormationMember(SHYGUYEnemyStatic, 215, 143),
            None,
            FormationMember(SNAPDRAGONEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK021_SHYGUY_STARSLAP_SNAPDRAGON_CROOK_ARACHNE] = FormationPack(
    Formation(
        members=[
            FormationMember(SHYGUYEnemyStatic, 231, 135),
            None,
            FormationMember(CROOKEnemyStatic, 199, 143),
            FormationMember(ARACHNEEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SHYGUYEnemyStatic, 135, 103),
            FormationMember(SHYGUYEnemyStatic, 215, 143),
            None,
            FormationMember(SNAPDRAGONEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SHYGUYEnemyStatic, 151, 111),
            None,
            FormationMember(STARSLAPEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK022_STARSLAP_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(STARSLAPEnemy, 199, 159),
            FormationMember(SHYGUYEnemyStatic, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(STARSLAPEnemy, 215, 151),
            FormationMember(ARACHNEEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(STARSLAPEnemy, 167, 135),
            FormationMember(SNAPDRAGONEnemy, 151, 111),
            FormationMember(SNAPDRAGONEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK023_STARSLAPS_SOMETIMES_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(STARSLAPEnemy, 199, 151),
            FormationMember(STARSLAPEnemy, 167, 103),
            FormationMember(STARSLAPEnemy, 231, 135),
            FormationMember(STARSLAPEnemy, 135, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(STARSLAPEnemy, 167, 135),
            FormationMember(SNAPDRAGONEnemy, 151, 111),
            FormationMember(SNAPDRAGONEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(STARSLAPEnemy, 215, 151),
            FormationMember(ARACHNEEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK024_WIGGLERS_WITH_AMANITA] = FormationPack(
    Formation(
        members=[
            FormationMember(WIGGLEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(WIGGLEREnemy, 151, 111),
            FormationMember(AMANITAEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(WIGGLEREnemy, 151, 111),
            FormationMember(WIGGLEREnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK025_WIGGLERS_WITH_GUERRILLA_OR_AMANITA] = FormationPack(
    Formation(
        members=[
            FormationMember(WIGGLEREnemy, 151, 119),
            None,
            FormationMember(GUERRILLAEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(WIGGLEREnemy, 151, 111),
            FormationMember(WIGGLEREnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(WIGGLEREnemy, 151, 111),
            FormationMember(AMANITAEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK026_AMANITAS_WITH_BUZZER_OR_OCTOLOT] = FormationPack(
    Formation(
        members=[
            FormationMember(AMANITAEnemy, 135, 127),
            FormationMember(AMANITAEnemy, 199, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(AMANITAEnemy, 199, 151),
            FormationMember(AMANITAEnemy, 135, 119),
            FormationMember(BUZZEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(AMANITAEnemy, 199, 151),
            FormationMember(AMANITAEnemy, 135, 119),
            FormationMember(OCTOLOTEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK027_AMANITAS_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(AMANITAEnemy, 151, 127),
            None,
            FormationMember(GUERRILLAEnemy, 215, 143),
            FormationMember(BUZZEREnemy, 183, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(AMANITAEnemy, 199, 151),
            FormationMember(AMANITAEnemy, 135, 119),
            FormationMember(OCTOLOTEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(AMANITAEnemy, 199, 151),
            FormationMember(AMANITAEnemy, 135, 119),
            FormationMember(BUZZEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK028_BUZZERS_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(BUZZEREnemy, 135, 119),
            FormationMember(OCTOLOTEnemy, 199, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BUZZEREnemy, 167, 103),
            FormationMember(BUZZEREnemy, 231, 135),
            FormationMember(AMANITAEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BUZZEREnemy, 199, 151),
            None,
            FormationMember(GUERRILLAEnemy, 151, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK029_BUZZERS_WITH_AMANITA] = FormationPack(
    Formation(
        members=[
            FormationMember(BUZZEREnemy, 199, 159),
            None,
            FormationMember(GUERRILLAEnemy, 135, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BUZZEREnemy, 199, 151),
            None,
            FormationMember(GUERRILLAEnemy, 151, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BUZZEREnemy, 167, 103),
            FormationMember(BUZZEREnemy, 231, 135),
            FormationMember(AMANITAEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK030_SPARKY_WITH_SHYRANGER] = FormationPack(
    Formation(
        members=[
            FormationMember(SPARKYEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPARKYEnemy, 167, 111),
            FormationMember(SPARKYEnemy, 215, 135),
            FormationMember(SHYRANGEREnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPARKYEnemy, 167, 135),
            FormationMember(SPARKYEnemy, 151, 111),
            FormationMember(SPARKYEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK031_MULTIPLE_SPARKY_WITH_SHYRANGER] = FormationPack(
    Formation(
        members=[
            FormationMember(SPARKYEnemy, 167, 135),
            FormationMember(SPARKYEnemy, 151, 111),
            FormationMember(SPARKYEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPARKYEnemy, 167, 135),
            FormationMember(SPARKYEnemy, 151, 111),
            FormationMember(SPARKYEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPARKYEnemy, 167, 111),
            FormationMember(SPARKYEnemy, 215, 135),
            FormationMember(SHYRANGEREnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK032_TOWER_PASS_HENCHMAN] = FormationPack(
    Formation(
        members=[
            FormationMember(APPRENTICEEnemyStatic, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
        can_run_away=False)
)
#
packs[PACK033_POSTGAME_TEMPLE] = FormationPack(
    # put belome 3 here
    Formation(
        members=[
            FormationMember(BELOMEEnemy3, 183, 127),
            FormationMember(MARIOCLONESEnemy, 135, 119, hidden_at_start=True),
            FormationMember(TOADSTOOL3Enemy, 215, 159, hidden_at_start=True),
        ],
        music=MidbossMusic(),
        unknown_bit=True,
        can_run_away=False)
)
packs[PACK034_PIRANHA_WITH_SHYRANGER] = FormationPack(
    Formation(
        members=[
            FormationMember(PIRANHAPLANTEnemyStatic, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(PIRANHAPLANTEnemyStatic, 215, 143),
            FormationMember(PIRANHAPLANTEnemyStatic, 151, 111),
            FormationMember(SHYRANGEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(PIRANHAPLANTEnemyStatic, 167, 111),
            FormationMember(PIRANHAPLANTEnemyStatic, 167, 135),
            FormationMember(PIRANHAPLANTEnemyStatic, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK035_MULTIPLE_PIRANHA_WITH_SHYRANGER] = FormationPack(
    Formation(
        members=[
            FormationMember(PIRANHAPLANTEnemyStatic, 151, 143),
            FormationMember(PIRANHAPLANTEnemyStatic, 151, 111),
            FormationMember(PIRANHAPLANTEnemyStatic, 199, 119),
            FormationMember(PIRANHAPLANTEnemyStatic, 231, 143),
            FormationMember(PIRANHAPLANTEnemyStatic, 199, 159),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(PIRANHAPLANTEnemyStatic, 167, 111),
            FormationMember(PIRANHAPLANTEnemyStatic, 167, 135),
            FormationMember(PIRANHAPLANTEnemyStatic, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(PIRANHAPLANTEnemyStatic, 215, 143),
            FormationMember(PIRANHAPLANTEnemyStatic, 151, 111),
            FormationMember(SHYRANGEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK036_BOBOMB_WITH_CLUSTER] = FormationPack(
    Formation(
        members=[
            FormationMember(BOBOMBEnemyStatic, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BOBOMBEnemyStatic, 135, 119),
            FormationMember(BOBOMBEnemyStatic, 199, 151),
            FormationMember(CLUSTEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BOBOMBEnemyStatic, 151, 127),
            FormationMember(BOBOMBEnemyStatic, 167, 103),
            FormationMember(BOBOMBEnemyStatic, 199, 151),
            FormationMember(BOBOMBEnemyStatic, 215, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK037_BOBOMB_WITH_CLUSTER_SOMETIMES_ENIGMA] = FormationPack(
    Formation(
        members=[
            FormationMember(BOBOMBEnemyStatic, 135, 119),
            FormationMember(BOBOMBEnemyStatic, 199, 151),
            FormationMember(ENIGMAEnemy, 183, 111),
            FormationMember(CLUSTEREnemy, 215, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BOBOMBEnemyStatic, 151, 127),
            FormationMember(BOBOMBEnemyStatic, 167, 103),
            FormationMember(BOBOMBEnemyStatic, 199, 151),
            FormationMember(BOBOMBEnemyStatic, 215, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BOBOMBEnemyStatic, 135, 119),
            FormationMember(BOBOMBEnemyStatic, 199, 151),
            FormationMember(CLUSTEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK038_SPARKY_WITH_ALWAYS_OTHER_ENEMIES_1] = FormationPack(
    Formation(
        members=[
            FormationMember(SPARKYEnemy, 199, 151),
            FormationMember(ENIGMAEnemy, 167, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPARKYEnemy, 167, 111),
            FormationMember(SPARKYEnemy, 215, 135),
            FormationMember(BOBOMBEnemyStatic, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPARKYEnemy, 183, 127),
            FormationMember(CLUSTEREnemy, 231, 143),
            FormationMember(CLUSTEREnemy, 151, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK039_SPARKY_WITH_ALWAYS_OTHER_ENEMIES_2] = FormationPack(
    Formation(
        members=[
            FormationMember(SPARKYEnemy, 183, 143),
            FormationMember(SPARKYEnemy, 151, 127),
            FormationMember(ENIGMAEnemy, 167, 103),
            FormationMember(ENIGMAEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPARKYEnemy, 183, 127),
            FormationMember(CLUSTEREnemy, 231, 143),
            FormationMember(CLUSTEREnemy, 151, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPARKYEnemy, 167, 111),
            FormationMember(SPARKYEnemy, 215, 135),
            FormationMember(BOBOMBEnemyStatic, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK040_MAGMITES_WITH_SPARKY_BOBOMB_OR_CLUSTER] = FormationPack(
    Formation(
        members=[
            FormationMember(MAGMITEEnemy, 167, 111),
            FormationMember(MAGMITEEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MAGMITEEnemy, 151, 111),
            FormationMember(BOBOMBEnemyStatic, 183, 127),
            FormationMember(SPARKYEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MAGMITEEnemy, 151, 127),
            FormationMember(MAGMITEEnemy, 183, 143),
            FormationMember(CLUSTEREnemy, 167, 103),
            FormationMember(CLUSTEREnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK041_MAGMITES_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(MAGMITEEnemy, 135, 103),
            FormationMember(MAGMITEEnemy, 231, 151),
            FormationMember(BOBOMBEnemyStatic, 167, 135),
            None,
            FormationMember(CLUSTEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MAGMITEEnemy, 151, 127),
            FormationMember(MAGMITEEnemy, 183, 143),
            FormationMember(CLUSTEREnemy, 167, 103),
            FormationMember(CLUSTEREnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MAGMITEEnemy, 151, 111),
            FormationMember(BOBOMBEnemyStatic, 183, 127),
            FormationMember(SPARKYEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK042_LAKITU_WITH_SPIKESTER_ARTICHOKER] = FormationPack(
    Formation(
        members=[
            FormationMember(LAKITUEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(LAKITUEnemy, 135, 119),
            FormationMember(SPIKESTEREnemy, 199, 159),
            FormationMember(ARTICHOKEREnemy, 183, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(LAKITUEnemy, 151, 111),
            FormationMember(LAKITUEnemy, 183, 127),
            FormationMember(LAKITUEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK043_LAKITU_USUALLY_WITH_ARTICHOKER] = FormationPack(
    Formation(
        members=[
            FormationMember(LAKITUEnemy, 231, 151),
            FormationMember(LAKITUEnemy, 135, 103),
            None,
            FormationMember(ARTICHOKEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(LAKITUEnemy, 151, 111),
            FormationMember(LAKITUEnemy, 183, 127),
            FormationMember(LAKITUEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(LAKITUEnemy, 135, 119),
            FormationMember(SPIKESTEREnemy, 199, 159),
            FormationMember(ARTICHOKEREnemy, 183, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK044_SPIKESTER_WITH_OTHER_ENEMIES] = FormationPack(
    Formation(
        members=[
            FormationMember(SPIKESTEREnemy, 215, 143),
            FormationMember(CARROBOSCISEnemy, 135, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPIKESTEREnemy, 199, 151),
            FormationMember(SPIKESTEREnemy, 135, 119),
            FormationMember(ARTICHOKEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPIKESTEREnemy, 183, 127),
            FormationMember(CARROBOSCISEnemy, 135, 119),
            FormationMember(CARROBOSCISEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK045_MULTIPLE_SPIKESTER_WITH_OTHER_ENEMIES] = FormationPack(
    Formation(
        members=[
            FormationMember(SPIKESTEREnemy, 119, 111),
            FormationMember(SPIKESTEREnemy, 215, 159),
            FormationMember(SPIKESTEREnemy, 215, 135),
            FormationMember(SPIKESTEREnemy, 167, 111),
            FormationMember(CARROBOSCISEnemy, 151, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPIKESTEREnemy, 183, 127),
            FormationMember(CARROBOSCISEnemy, 135, 119),
            FormationMember(CARROBOSCISEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPIKESTEREnemy, 199, 151),
            FormationMember(SPIKESTEREnemy, 135, 119),
            FormationMember(ARTICHOKEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK046_SPOOKUM_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(SPOOKUMEnemy, 199, 135),
            FormationMember(ORBUSEREnemy, 135, 119),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPOOKUMEnemy, 135, 119),
            FormationMember(SPOOKUMEnemy, 199, 151),
            FormationMember(JESTEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPOOKUMEnemy, 151, 111),
            FormationMember(REMOCONEnemy, 167, 151),
            FormationMember(ORBUSEREnemy, 215, 127),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK047_MULTIPLE_SPOOKUM_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(SPOOKUMEnemy, 135, 119),
            FormationMember(SPOOKUMEnemy, 199, 151),
            FormationMember(REMOCONEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPOOKUMEnemy, 151, 111),
            FormationMember(REMOCONEnemy, 167, 151),
            FormationMember(ORBUSEREnemy, 215, 127),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPOOKUMEnemy, 135, 119),
            FormationMember(SPOOKUMEnemy, 199, 151),
            FormationMember(JESTEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK048_ROBOMB_WITH_REMOCON] = FormationPack(
    Formation(
        members=[
            FormationMember(ROBOMBEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(ROBOMBEnemy, 183, 127),
            FormationMember(ROBOMBEnemy, 199, 119),
            FormationMember(ROBOMBEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(ROBOMBEnemy, 215, 143),
            FormationMember(ROBOMBEnemy, 151, 111),
            FormationMember(REMOCONEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK049_ROBOMB_WITH_REMOCON_OR_ORBUSER] = FormationPack(
    Formation(
        members=[
            FormationMember(ROBOMBEnemy, 135, 127),
            FormationMember(ROBOMBEnemy, 231, 127),
            FormationMember(ROBOMBEnemy, 183, 103),
            FormationMember(ROBOMBEnemy, 183, 151),
            FormationMember(ORBUSEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(ROBOMBEnemy, 215, 143),
            FormationMember(ROBOMBEnemy, 151, 111),
            FormationMember(REMOCONEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(ROBOMBEnemy, 183, 127),
            FormationMember(ROBOMBEnemy, 199, 119),
            FormationMember(ROBOMBEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK050_CHOMP_WITH_OTHER_MONSTERS_1] = FormationPack(
    Formation(
        members=[
            FormationMember(CHOMPEnemy, 215, 143),
            FormationMember(JESTEREnemy, 167, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CHOMPEnemy, 215, 143),
            FormationMember(ROBOMBEnemy, 151, 135),
            FormationMember(REMOCONEnemy, 167, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CHOMPEnemy, 151, 111),
            FormationMember(CHOMPEnemy, 215, 143),
            FormationMember(ORBUSEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK051_CHOMP_WITH_OTHER_MONSTERS_2] = FormationPack(
    Formation(
        members=[
            FormationMember(CHOMPEnemy, 199, 119),
            None,
            FormationMember(JESTEREnemy, 135, 103),
            FormationMember(JESTEREnemy, 231, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CHOMPEnemy, 151, 111),
            FormationMember(CHOMPEnemy, 215, 143),
            FormationMember(ORBUSEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CHOMPEnemy, 215, 143),
            FormationMember(ROBOMBEnemy, 151, 135),
            FormationMember(REMOCONEnemy, 167, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK052_BLASTERS_AND_SPOOKUMS_1] = FormationPack(
    Formation(
        members=[
            FormationMember(BLASTEREnemy, 167, 135),
            FormationMember(SPOOKUMEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BLASTEREnemy, 167, 135),
            FormationMember(SPOOKUMEnemy, 151, 111),
            FormationMember(REMOCONEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BLASTEREnemy, 199, 151),
            FormationMember(BLASTEREnemy, 135, 119),
            FormationMember(SPOOKUMEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK053_BLASTERS_AND_SPOOKUMS_2] = FormationPack(
    Formation(
        members=[
            FormationMember(BLASTEREnemy, 199, 119),
            FormationMember(ROBOMBEnemy, 135, 103),
            FormationMember(ROBOMBEnemy, 231, 151),
            FormationMember(SPOOKUMEnemy, 151, 127),
            FormationMember(SPOOKUMEnemy, 183, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BLASTEREnemy, 199, 151),
            FormationMember(BLASTEREnemy, 135, 119),
            FormationMember(SPOOKUMEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BLASTEREnemy, 167, 135),
            FormationMember(SPOOKUMEnemy, 151, 111),
            FormationMember(REMOCONEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK054_TOWER_HENCHMAN_3] = FormationPack(
    Formation(
        members=[
            FormationMember(SNIFITEnemyStatic, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
        can_run_away=False
    )
)
#
packs[PACK055_MONSTRO_DOOR_POSTGAME] = FormationPack(
    Formation(
        members=[
            FormationMember(CULEX3DEnemy, 183, 103),
            FormationMember(FIRECRYS3DEnemy, 135, 103, hidden_at_start=True),
            FormationMember(FIRECRYS3DEnemy, 151, 119, hidden_at_start=True),
            FormationMember(FIRECRYS3DEnemy, 183, 135, hidden_at_start=True),
            FormationMember(FIRECRYS3DEnemy, 215, 143, hidden_at_start=True),
        ],
        run_event_at_load=BE0077_CULEX_3D,
        music=CulexMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK056_MUKU_PULSAR_GECKO] = FormationPack(
    Formation(
        members=[
            FormationMember(MUKUMUKUEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MUKUMUKUEnemy, 151, 119),
            FormationMember(MUKUMUKUEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MUKUMUKUEnemy, 151, 111),
            FormationMember(MUKUMUKUEnemy, 215, 143),
            FormationMember(PULSAREnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK057_MUKU_PULSAR_GECKO_MULTI] = FormationPack(
    Formation(
        members=[
            FormationMember(MUKUMUKUEnemy, 183, 143),
            FormationMember(PULSAREnemy, 151, 111),
            FormationMember(GECKOEnemy, 231, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MUKUMUKUEnemy, 151, 111),
            FormationMember(MUKUMUKUEnemy, 215, 143),
            FormationMember(PULSAREnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MUKUMUKUEnemy, 151, 119),
            FormationMember(MUKUMUKUEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK058_SACKIT_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(SACKITEnemy, 199, 151),
            FormationMember(SACKITEnemy, 167, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SACKITEnemy, 151, 127),
            FormationMember(SACKITEnemy, 183, 143),
            FormationMember(MUKUMUKUEnemy, 167, 103),
            FormationMember(GECKOEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SACKITEnemy, 167, 135),
            None,
            None,
            FormationMember(PULSAREnemy, 167, 103),
            FormationMember(PULSAREnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK059_SACKIT_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(SACKITEnemy, 215, 143),
            FormationMember(MASTADOOMEnemy, 167, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SACKITEnemy, 167, 135),
            None,
            None,
            FormationMember(PULSAREnemy, 167, 103),
            FormationMember(PULSAREnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SACKITEnemy, 151, 127),
            FormationMember(SACKITEnemy, 183, 143),
            FormationMember(MUKUMUKUEnemy, 167, 103),
            FormationMember(GECKOEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK060_GECKO_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(GECKOEnemy, 151, 119),
            FormationMember(SACKITEnemy, 199, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GECKOEnemy, 151, 119),
            FormationMember(MASTADOOMEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GECKOEnemy, 183, 143),
            FormationMember(GECKOEnemy, 151, 127),
            FormationMember(MUKUMUKUEnemy, 135, 103),
            FormationMember(MUKUMUKUEnemy, 231, 151),
            FormationMember(SACKITEnemy, 183, 111),
            FormationMember(SACKITEnemy, 215, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK061_GECKO_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(GECKOEnemy, 135, 103),
            FormationMember(GECKOEnemy, 231, 151),
            FormationMember(MASTADOOMEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GECKOEnemy, 183, 143),
            FormationMember(GECKOEnemy, 151, 127),
            FormationMember(MUKUMUKUEnemy, 135, 103),
            FormationMember(MUKUMUKUEnemy, 231, 151),
            FormationMember(SACKITEnemy, 183, 111),
            FormationMember(SACKITEnemy, 215, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GECKOEnemy, 151, 119),
            FormationMember(MASTADOOMEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK062_ZEOSTAR_WITH_BLOOBER_OR_LEUKO] = FormationPack(
    Formation(
        members=[
            FormationMember(ZEOSTAREnemy, 135, 119),
            FormationMember(ZEOSTAREnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(ZEOSTAREnemy, 151, 135),
            FormationMember(ZEOSTAREnemy, 183, 103),
            FormationMember(BLOOBEREnemyStatic, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(ZEOSTAREnemy, 199, 119),
            FormationMember(ZEOSTAREnemy, 167, 135),
            FormationMember(LEUKOEnemy, 167, 103),
            FormationMember(LEUKOEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK063_ZEOSTAR_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(ZEOSTAREnemy, 183, 127),
            FormationMember(LEUKOEnemy, 215, 143),
            FormationMember(CRUSTYEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(ZEOSTAREnemy, 199, 119),
            FormationMember(ZEOSTAREnemy, 167, 135),
            FormationMember(LEUKOEnemy, 167, 103),
            FormationMember(LEUKOEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(ZEOSTAREnemy, 151, 135),
            FormationMember(ZEOSTAREnemy, 183, 103),
            FormationMember(BLOOBEREnemyStatic, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK064_BLOOBER_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(BLOOBEREnemyStatic, 151, 111),
            FormationMember(MRKIPPEREnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BLOOBEREnemyStatic, 183, 127),
            FormationMember(BLOOBEREnemyStatic, 231, 143),
            FormationMember(BLOOBEREnemyStatic, 135, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BLOOBEREnemyStatic, 151, 111),
            FormationMember(BLOOBEREnemyStatic, 231, 151),
            FormationMember(MRKIPPEREnemy, 151, 143),
            FormationMember(CRUSTYEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK065_BLOOBER_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(BLOOBEREnemyStatic, 231, 135),
            FormationMember(BLOOBEREnemyStatic, 167, 103),
            FormationMember(ZEOSTAREnemy, 135, 127),
            FormationMember(ZEOSTAREnemy, 183, 151),
            FormationMember(LEUKOEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BLOOBEREnemyStatic, 151, 111),
            FormationMember(BLOOBEREnemyStatic, 231, 151),
            FormationMember(MRKIPPEREnemy, 151, 143),
            FormationMember(CRUSTYEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BLOOBEREnemyStatic, 183, 127),
            FormationMember(BLOOBEREnemyStatic, 231, 143),
            FormationMember(BLOOBEREnemyStatic, 135, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK066_KIPPER_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(MRKIPPEREnemy, 151, 103),
            FormationMember(MRKIPPEREnemy, 215, 151),
            FormationMember(MRKIPPEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MRKIPPEREnemy, 199, 151),
            FormationMember(MRKIPPEREnemy, 135, 119),
            FormationMember(CRUSTYEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MRKIPPEREnemy, 135, 119),
            FormationMember(MRKIPPEREnemy, 231, 135),
            FormationMember(CRUSTYEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK067_KIPPER_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(MRKIPPEREnemy, 215, 127),
            FormationMember(MRKIPPEREnemy, 199, 151),
            FormationMember(MRKIPPEREnemy, 167, 103),
            FormationMember(MRKIPPEREnemy, 151, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MRKIPPEREnemy, 135, 119),
            FormationMember(MRKIPPEREnemy, 231, 135),
            FormationMember(CRUSTYEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MRKIPPEREnemy, 199, 151),
            FormationMember(MRKIPPEREnemy, 135, 119),
            FormationMember(CRUSTYEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK068_SHIP_HENCHMAN_1] = FormationPack(
    Formation(
        members=[
            FormationMember(BANDANAREDEnemy, 151, 127),
            FormationMember(BANDANAREDEnemy, 183, 143),
            FormationMember(BANDANAREDEnemy, 167, 103),
            FormationMember(BANDANAREDEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
        can_run_away=False
    )
)
#
packs[PACK069_SHIP_HENCHMAN_2] = FormationPack(
    Formation(
        members=[
            FormationMember(BANDANAREDEnemy, 199, 151),
            FormationMember(BANDANAREDEnemy, 135, 119),
            FormationMember(BANDANAREDEnemy, 215, 127),
            FormationMember(BANDANAREDEnemy, 167, 135),
            FormationMember(BANDANAREDEnemy, 183, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
        can_run_away=False
    )
)
#
packs[PACK070_TOWER_POSTGAME] = FormationPack(
    Formation(
        members=[
            FormationMember(BOOSTEREnemy2, 184, 116),
            FormationMember(SNIFIT2Enemy, 156, 132),
            FormationMember(SNIFIT2Enemy, 143, 104),
            FormationMember(SNIFIT2Enemy, 212, 138),
            FormationMember(BOOSTERDUMMY, 0, 0),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK071_MINES_POSTGAME] = FormationPack(
    Formation(
        members=[
            FormationMember(PUNCHINELLO2Enemy, 188, 116),
            FormationMember(STRONGBOBOMB3Enemy, 145, 103, hidden_at_start=True),
            FormationMember(STRONGBOBOMB1Enemy, 150, 129, hidden_at_start=True),
            FormationMember(STRONGBOBOMB4Enemy, 182, 142, hidden_at_start=True),
            FormationMember(STRONGBOBOMB2Enemy, 223, 142, hidden_at_start=True),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK072_DRYBONES_WITH_GREAPER_REACHER] = FormationPack(
    Formation(
        members=[
            FormationMember(DRYBONESEnemy, 199, 151),
            FormationMember(DRYBONESEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(DRYBONESEnemy, 135, 119),
            FormationMember(DRYBONESEnemy, 199, 151),
            FormationMember(GREAPEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(DRYBONESEnemy, 135, 119),
            FormationMember(GREAPEREnemy, 199, 151),
            FormationMember(REACHEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK073_DRYBONES_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(DRYBONESEnemy, 167, 103),
            FormationMember(DRYBONESEnemy, 231, 135),
            FormationMember(GREAPEREnemy, 151, 127),
            FormationMember(GREAPEREnemy, 183, 143),
            FormationMember(REACHEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(DRYBONESEnemy, 135, 119),
            FormationMember(GREAPEREnemy, 199, 151),
            FormationMember(REACHEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(DRYBONESEnemy, 135, 119),
            FormationMember(DRYBONESEnemy, 199, 151),
            FormationMember(GREAPEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK074_ALLEYRAT_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(ALLEYRATEnemy, 199, 151),
            FormationMember(GORGONEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(ALLEYRATEnemy, 135, 119),
            FormationMember(ALLEYRATEnemy, 199, 151),
            FormationMember(GREAPEREnemy, 215, 127),
            FormationMember(GREAPEREnemy, 183, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(ALLEYRATEnemy, 151, 127),
            FormationMember(ALLEYRATEnemy, 199, 151),
            FormationMember(GORGONEnemy, 183, 111),
            FormationMember(GORGONEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK075_ALLEYRAT_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(ALLEYRATEnemy, 231, 135),
            FormationMember(REACHEREnemy, 167, 135),
            FormationMember(GORGONEnemy, 167, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(ALLEYRATEnemy, 151, 127),
            FormationMember(ALLEYRATEnemy, 199, 151),
            FormationMember(GORGONEnemy, 183, 111),
            FormationMember(GORGONEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(ALLEYRATEnemy, 135, 119),
            FormationMember(ALLEYRATEnemy, 199, 151),
            FormationMember(GREAPEREnemy, 215, 127),
            FormationMember(GREAPEREnemy, 183, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK076_GREAPER_WITH_REACHER_STRAWHEAD] = FormationPack(
    Formation(
        members=[
            FormationMember(GREAPEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GREAPEREnemy, 151, 119),
            FormationMember(GREAPEREnemy, 199, 143),
            FormationMember(REACHEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GREAPEREnemy, 167, 135),
            FormationMember(STRAWHEADEnemy, 215, 135),
            FormationMember(REACHEREnemy, 167, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK077_GREAPER_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(GREAPEREnemy, 167, 135),
            FormationMember(GORGONEnemy, 199, 119),
            FormationMember(STRAWHEADEnemy, 215, 143),
            FormationMember(STRAWHEADEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GREAPEREnemy, 167, 135),
            FormationMember(STRAWHEADEnemy, 215, 135),
            FormationMember(REACHEREnemy, 167, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GREAPEREnemy, 151, 119),
            FormationMember(GREAPEREnemy, 199, 143),
            FormationMember(REACHEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK078_CHAPEL_POSTGAME] = FormationPack(
    Formation(
        members=[
            FormationMember(BUNDT2Enemy, 199, 127),
            FormationMember(RASPBERRY2Enemy, 199, 119),
            FormationMember(TORTE2Enemy, 199, 151),
            FormationMember(TORTE2Enemy, 135, 119),
            FormationMember(CANDLEEnemy, 0, 0),
        ],
        run_event_at_load=BE0017_BEGIN_BUNDT_POSTGAME,
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK079_MINES_HENCHMAN_RIGHT] =  FormationPack(
    Formation(
        members=[
            FormationMember(CROOKEnemyStatic, 135, 119),
            FormationMember(CROOKEnemyStatic, 199, 119),
            FormationMember(CROOKEnemyStatic, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CROOKEnemyStatic, 167, 103),
            FormationMember(CROOKEnemyStatic, 135, 119),
            FormationMember(CROOKEnemyStatic, 183, 127),
            FormationMember(CROOKEnemyStatic, 199, 151),
            FormationMember(CROOKEnemyStatic, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CROOKEnemyStatic, 135, 119),
            FormationMember(CROOKEnemyStatic, 199, 119),
            FormationMember(CROOKEnemyStatic, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK080_STINGER_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(STINGEREnemy, 151, 111),
            FormationMember(FINKFLOWEREnemy, 199, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(STINGEREnemy, 135, 111),
            FormationMember(STINGEREnemy, 215, 151),
            FormationMember(OCTOVADEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(STINGEREnemy, 199, 119),
            None,
            FormationMember(FINKFLOWEREnemy, 215, 143),
            FormationMember(FINKFLOWEREnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK081_STINGER_WITH_OCTOVADER_OR_FINKFLOWER] = FormationPack(
    Formation(
        members=[
            FormationMember(STINGEREnemy, 183, 111),
            FormationMember(STINGEREnemy, 199, 151),
            FormationMember(STINGEREnemy, 215, 127),
            FormationMember(STINGEREnemy, 135, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(STINGEREnemy, 199, 119),
            None,
            FormationMember(FINKFLOWEREnemy, 215, 143),
            FormationMember(FINKFLOWEREnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(STINGEREnemy, 135, 111),
            FormationMember(STINGEREnemy, 215, 151),
            FormationMember(OCTOVADEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK082_CHOW_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(CHOWEnemy, 135, 119),
            FormationMember(OCTOVADEREnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CHOWEnemy, 151, 111),
            FormationMember(SHOGUNEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CHOWEnemy, 199, 151),
            FormationMember(SHOGUNEnemy, 135, 119),
            FormationMember(OCTOVADEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK083_CHOW_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(CHOWEnemy, 167, 135),
            FormationMember(FINKFLOWEREnemy, 199, 119),
            FormationMember(SHOGUNEnemy, 135, 119),
            FormationMember(SHOGUNEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CHOWEnemy, 199, 151),
            FormationMember(SHOGUNEnemy, 135, 119),
            FormationMember(OCTOVADEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CHOWEnemy, 151, 111),
            FormationMember(SHOGUNEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK084_CHOMPCHOMP_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(CHOMPCHOMPEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CHOMPCHOMPEnemy, 151, 111),
            FormationMember(CHOMPCHOMPEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CHOMPCHOMPEnemy, 151, 111),
            FormationMember(CHOMPCHOMPEnemy, 199, 119),
            FormationMember(CHOMPCHOMPEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK085_CHOMPCHOMP_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(CHOMPCHOMPEnemy, 135, 119),
            FormationMember(CHOMPCHOMPEnemy, 183, 111),
            FormationMember(CHOMPCHOMPEnemy, 215, 127),
            FormationMember(CHOMPCHOMPEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CHOMPCHOMPEnemy, 151, 111),
            FormationMember(CHOMPCHOMPEnemy, 199, 119),
            FormationMember(CHOMPCHOMPEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CHOMPCHOMPEnemy, 151, 111),
            FormationMember(CHOMPCHOMPEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK086_SHYAWAY_WITH_KRIFFID_OR_RIBBITE] = FormationPack(
    Formation(
        members=[
            FormationMember(SHYAWAYEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SHYAWAYEnemy, 151, 111),
            FormationMember(SHYAWAYEnemy, 215, 143),
            FormationMember(KRIFFIDEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SHYAWAYEnemy, 167, 103),
            FormationMember(SHYAWAYEnemy, 231, 135),
            FormationMember(RIBBITEEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK087_SHYAWAY_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(SHYAWAYEnemy, 215, 135),
            None,
            FormationMember(GECKITEnemy, 167, 143),
            None,
            FormationMember(RIBBITEEnemy, 167, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SHYAWAYEnemy, 167, 103),
            FormationMember(SHYAWAYEnemy, 231, 135),
            FormationMember(RIBBITEEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SHYAWAYEnemy, 151, 111),
            FormationMember(SHYAWAYEnemy, 215, 143),
            FormationMember(KRIFFIDEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK088_CHEWY_WITH_SHYAWAY_OR_SPINTHRA] = FormationPack(
    Formation(
        members=[
            FormationMember(CHEWYEnemy, 151, 111),
            FormationMember(CHEWYEnemy, 183, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CHEWYEnemy, 135, 119),
            FormationMember(CHEWYEnemy, 199, 151),
            FormationMember(SHYAWAYEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CHEWYEnemy, 151, 111),
            FormationMember(SPINTHRAEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK089_CHEWY_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(CHEWYEnemy, 183, 151),
            FormationMember(CHEWYEnemy, 135, 127),
            FormationMember(GECKITEnemy, 231, 143),
            FormationMember(GECKITEnemy, 151, 103),
            FormationMember(KRIFFIDEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CHEWYEnemy, 151, 111),
            FormationMember(SPINTHRAEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CHEWYEnemy, 135, 119),
            FormationMember(CHEWYEnemy, 199, 151),
            FormationMember(SHYAWAYEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK090_GECKIT_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(GECKITEnemy, 199, 151),
            FormationMember(SPINTHRAEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GECKITEnemy, 183, 135),
            FormationMember(GECKITEnemy, 215, 151),
            FormationMember(SPINTHRAEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GECKITEnemy, 151, 127),
            FormationMember(GECKITEnemy, 183, 143),
            FormationMember(CHEWYEnemy, 167, 103),
            FormationMember(CHEWYEnemy, 231, 135),
            FormationMember(SHYAWAYEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK091_GECKIT_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(GECKITEnemy, 151, 127),
            FormationMember(GECKITEnemy, 183, 143),
            FormationMember(SPINTHRAEnemy, 151, 103),
            FormationMember(KRIFFIDEnemy, 231, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GECKITEnemy, 151, 127),
            FormationMember(GECKITEnemy, 183, 143),
            FormationMember(CHEWYEnemy, 167, 103),
            FormationMember(CHEWYEnemy, 231, 135),
            FormationMember(SHYAWAYEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GECKITEnemy, 183, 135),
            FormationMember(GECKITEnemy, 215, 151),
            FormationMember(SPINTHRAEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK092_BIRDY_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(BIRDYEnemyStatic, 135, 119),
            FormationMember(HEAVYTROOPAEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BIRDYEnemyStatic, 215, 119),
            FormationMember(BIRDYEnemyStatic, 151, 119),
            FormationMember(BIRDYEnemyStatic, 183, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BIRDYEnemyStatic, 199, 151),
            FormationMember(BIRDYEnemyStatic, 135, 119),
            FormationMember(HEAVYTROOPAEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK093_BIRDY_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(BIRDYEnemyStatic, 151, 111),
            FormationMember(BIRDYEnemyStatic, 215, 143),
            FormationMember(BIRDYEnemyStatic, 151, 143),
            FormationMember(BIRDYEnemyStatic, 215, 111),
            FormationMember(BIRDYEnemyStatic, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BIRDYEnemyStatic, 199, 151),
            FormationMember(BIRDYEnemyStatic, 135, 119),
            FormationMember(HEAVYTROOPAEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BIRDYEnemyStatic, 215, 119),
            FormationMember(BIRDYEnemyStatic, 151, 119),
            FormationMember(BIRDYEnemyStatic, 183, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK094_BLUEBIRD_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(BLUEBIRDEnemyStatic, 199, 151),
            FormationMember(BLUEBIRDEnemyStatic, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BLUEBIRDEnemyStatic, 167, 103),
            FormationMember(BLUEBIRDEnemyStatic, 231, 135),
            FormationMember(HEAVYTROOPAEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BLUEBIRDEnemyStatic, 183, 143),
            FormationMember(BLUEBIRDEnemyStatic, 183, 111),
            FormationMember(BLUEBIRDEnemyStatic, 231, 135),
            FormationMember(BLUEBIRDEnemyStatic, 135, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK095_BLUEBIRD_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(BLUEBIRDEnemyStatic, 151, 111),
            FormationMember(BLUEBIRDEnemyStatic, 215, 143),
            None,
            None,
            FormationMember(HEAVYTROOPAEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BLUEBIRDEnemyStatic, 183, 143),
            FormationMember(BLUEBIRDEnemyStatic, 183, 111),
            FormationMember(BLUEBIRDEnemyStatic, 231, 135),
            FormationMember(BLUEBIRDEnemyStatic, 135, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BLUEBIRDEnemyStatic, 167, 103),
            FormationMember(BLUEBIRDEnemyStatic, 231, 135),
            FormationMember(HEAVYTROOPAEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK096_PINWHEEL_WITH_MUCKLE] = FormationPack(
    Formation(
        members=[
            FormationMember(PINWHEELEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(PINWHEELEnemy, 135, 119),
            FormationMember(MUCKLEEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(PINWHEELEnemy, 151, 127),
            FormationMember(PINWHEELEnemy, 183, 143),
            FormationMember(MUCKLEEnemy, 151, 103),
            FormationMember(MUCKLEEnemy, 231, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK097_PINWHEEL_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(PINWHEELEnemy, 151, 143),
            FormationMember(PINWHEELEnemy, 135, 119),
            FormationMember(PINWHEELEnemy, 199, 151),
            FormationMember(SLINGSHYEnemy, 167, 111),
            FormationMember(SLINGSHYEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(PINWHEELEnemy, 151, 127),
            FormationMember(PINWHEELEnemy, 183, 143),
            FormationMember(MUCKLEEnemy, 151, 103),
            FormationMember(MUCKLEEnemy, 231, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(PINWHEELEnemy, 135, 119),
            FormationMember(MUCKLEEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK098_SHAMAN_WITH_ORBISON_JAWFUL] = FormationPack(
    Formation(
        members=[
            FormationMember(SHAMANEnemy, 151, 111),
            FormationMember(SHAMANEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SHAMANEnemy, 135, 119),
            FormationMember(ORBISONEnemy, 199, 151),
            FormationMember(JAWFULEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SHAMANEnemy, 167, 103),
            FormationMember(SHAMANEnemy, 231, 135),
            FormationMember(JAWFULEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK099_SHAMAN_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(SHAMANEnemy, 167, 103),
            FormationMember(SHAMANEnemy, 231, 135),
            FormationMember(SLINGSHYEnemy, 135, 127),
            FormationMember(SLINGSHYEnemy, 183, 151),
            FormationMember(JAWFULEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SHAMANEnemy, 167, 103),
            FormationMember(SHAMANEnemy, 231, 135),
            FormationMember(JAWFULEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SHAMANEnemy, 135, 119),
            FormationMember(ORBISONEnemy, 199, 151),
            FormationMember(JAWFULEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK100_SLINGSHY_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(SLINGSHYEnemy, 135, 119),
            FormationMember(ORBISONEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SLINGSHYEnemy, 183, 127),
            FormationMember(ORBISONEnemy, 151, 111),
            FormationMember(ORBISONEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SLINGSHYEnemy, 167, 135),
            FormationMember(ORBISONEnemy, 151, 111),
            FormationMember(ORBISONEnemy, 215, 143),
            FormationMember(JAWFULEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK101_SLINGSHY_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(SLINGSHYEnemy, 183, 143),
            FormationMember(SLINGSHYEnemy, 151, 127),
            FormationMember(PINWHEELEnemy, 151, 111),
            FormationMember(PINWHEELEnemy, 215, 143),
            FormationMember(MUCKLEEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SLINGSHYEnemy, 167, 135),
            FormationMember(ORBISONEnemy, 151, 111),
            FormationMember(ORBISONEnemy, 215, 143),
            FormationMember(JAWFULEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SLINGSHYEnemy, 183, 127),
            FormationMember(ORBISONEnemy, 151, 111),
            FormationMember(ORBISONEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK102_MAGMUS_WITH_ARMOREDANT_OERLIKON] = FormationPack(
    Formation(
        members=[
            FormationMember(MAGMUSEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MAGMUSEnemy, 151, 111),
            FormationMember(MAGMUSEnemy, 215, 143),
            FormationMember(ARMOREDANTEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MAGMUSEnemy, 151, 103),
            FormationMember(MAGMUSEnemy, 231, 143),
            FormationMember(MAGMUSEnemy, 199, 119),
            FormationMember(OERLIKONEnemy, 151, 127),
            FormationMember(OERLIKONEnemy, 183, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK103_MAGMUS_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(MAGMUSEnemy, 119, 119),
            FormationMember(MAGMUSEnemy, 167, 143),
            FormationMember(ARMOREDANTEnemy, 167, 111),
            FormationMember(ARMOREDANTEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MAGMUSEnemy, 151, 103),
            FormationMember(MAGMUSEnemy, 231, 143),
            FormationMember(MAGMUSEnemy, 199, 119),
            FormationMember(OERLIKONEnemy, 151, 127),
            FormationMember(OERLIKONEnemy, 183, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MAGMUSEnemy, 151, 111),
            FormationMember(MAGMUSEnemy, 215, 143),
            FormationMember(ARMOREDANTEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK104_OERLIKON_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(OERLIKONEnemy, 135, 119),
            FormationMember(VOMEREnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(OERLIKONEnemy, 183, 127),
            FormationMember(OERLIKONEnemy, 135, 119),
            FormationMember(OERLIKONEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(OERLIKONEnemy, 215, 151),
            FormationMember(CHAINEDKONGEnemy, 183, 127),
            FormationMember(ARMOREDANTEnemy, 135, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK105_OERLIKON_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(OERLIKONEnemy, 135, 127),
            FormationMember(OERLIKONEnemy, 183, 151),
            FormationMember(CHAINEDKONGEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(OERLIKONEnemy, 215, 151),
            FormationMember(CHAINEDKONGEnemy, 183, 127),
            FormationMember(ARMOREDANTEnemy, 135, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(OERLIKONEnemy, 183, 127),
            FormationMember(OERLIKONEnemy, 135, 119),
            FormationMember(OERLIKONEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK106_PYROSPHERE_WITH_CHAINEDKONG_CORKPEDITE] = FormationPack(
    Formation(
        members=[
            FormationMember(PYROSPHEREEnemy, 151, 135),
            FormationMember(PYROSPHEREEnemy, 215, 135),
            FormationMember(PYROSPHEREEnemy, 183, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(PYROSPHEREEnemy, 199, 143),
            FormationMember(PYROSPHEREEnemy, 151, 119),
            FormationMember(CHAINEDKONGEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CORKPEDITEEnemy, 135, 119),
            FormationMember(BODYEnemy, 151, 111),
            FormationMember(PYROSPHEREEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK107_PYROSPHERE_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(PYROSPHEREEnemy, 199, 151),
            FormationMember(PYROSPHEREEnemy, 199, 119),
            FormationMember(STUMPETEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CORKPEDITEEnemy, 135, 119),
            FormationMember(BODYEnemy, 151, 111),
            FormationMember(PYROSPHEREEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(PYROSPHEREEnemy, 199, 143),
            FormationMember(PYROSPHEREEnemy, 151, 119),
            FormationMember(CHAINEDKONGEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK108_VOMER_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(VOMEREnemy, 151, 111),
            FormationMember(CHAINEDKONGEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(VOMEREnemy, 151, 103),
            FormationMember(VOMEREnemy, 183, 127),
            FormationMember(VOMEREnemy, 215, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CORKPEDITEEnemy, 199, 151),
            FormationMember(BODYEnemy, 215, 143),
            FormationMember(VOMEREnemy, 135, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK109_VOMER_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(VOMEREnemy, 151, 135),
            FormationMember(VOMEREnemy, 151, 103),
            FormationMember(STUMPETEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CORKPEDITEEnemy, 199, 151),
            FormationMember(BODYEnemy, 215, 143),
            FormationMember(VOMEREnemy, 135, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(VOMEREnemy, 151, 103),
            FormationMember(VOMEREnemy, 183, 127),
            FormationMember(VOMEREnemy, 215, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK110_TERRACOTTA_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(TERRACOTTAEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(TERRACOTTAEnemy, 183, 151),
            FormationMember(TERRACOTTAEnemy, 151, 119),
            FormationMember(TERRACOTTAEnemy, 215, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(TERRACOTTAEnemy, 183, 127),
            FormationMember(FORKIESEnemy, 151, 111),
            FormationMember(FORKIESEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK111_TERRACOTTA_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(TERRACOTTAEnemy, 135, 127),
            FormationMember(TERRACOTTAEnemy, 183, 151),
            FormationMember(GUGOOMBAEnemy, 231, 135),
            FormationMember(GUGOOMBAEnemy, 167, 103),
            FormationMember(FORKIESEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(TERRACOTTAEnemy, 183, 127),
            FormationMember(FORKIESEnemy, 151, 111),
            FormationMember(FORKIESEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(TERRACOTTAEnemy, 183, 151),
            FormationMember(TERRACOTTAEnemy, 151, 119),
            FormationMember(TERRACOTTAEnemy, 215, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK112_MALAKOOPA_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(MALAKOOPAEnemy, 135, 127),
            FormationMember(TUBOTROOPAEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MALAKOOPAEnemy, 135, 119),
            FormationMember(MALAKOOPAEnemy, 199, 151),
            FormationMember(TUBOTROOPAEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MALAKOOPAEnemy, 135, 103),
            FormationMember(MALAKOOPAEnemy, 231, 151),
            FormationMember(TERRACOTTAEnemy, 167, 135),
            FormationMember(TUBOTROOPAEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK113_MALAKOOPA_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(MALAKOOPAEnemy, 183, 127),
            None,
            None,
            FormationMember(TUBOTROOPAEnemy, 135, 103),
            FormationMember(TUBOTROOPAEnemy, 231, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MALAKOOPAEnemy, 135, 103),
            FormationMember(MALAKOOPAEnemy, 231, 151),
            FormationMember(TERRACOTTAEnemy, 167, 135),
            FormationMember(TUBOTROOPAEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MALAKOOPAEnemy, 135, 119),
            FormationMember(MALAKOOPAEnemy, 199, 151),
            FormationMember(TUBOTROOPAEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK114_GUGOOMBA_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(GUGOOMBAEnemy, 151, 111),
            FormationMember(GUGOOMBAEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GUGOOMBAEnemy, 231, 151),
            FormationMember(GUGOOMBAEnemy, 135, 103),
            FormationMember(STARCRUSTEREnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GUGOOMBAEnemy, 231, 143),
            FormationMember(FORKIESEnemy, 199, 119),
            FormationMember(STARCRUSTEREnemy, 151, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK115_GUGOOMBA_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(GUGOOMBAEnemy, 199, 151),
            FormationMember(GUGOOMBAEnemy, 135, 119),
            FormationMember(MALAKOOPAEnemy, 167, 135),
            FormationMember(MALAKOOPAEnemy, 199, 119),
            FormationMember(TERRACOTTAEnemy, 167, 103),
            FormationMember(TERRACOTTAEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GUGOOMBAEnemy, 231, 143),
            FormationMember(FORKIESEnemy, 199, 119),
            FormationMember(STARCRUSTEREnemy, 151, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GUGOOMBAEnemy, 231, 151),
            FormationMember(GUGOOMBAEnemy, 135, 103),
            FormationMember(STARCRUSTEREnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK116_BIGBERTHA_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(BIGBERTHAEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BIGBERTHAEnemy, 151, 111),
            FormationMember(BIGBERTHAEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BIGBERTHAEnemy, 215, 143),
            FormationMember(FORKIESEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK117_BIGBERTHA_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(BIGBERTHAEnemy, 135, 111),
            FormationMember(BIGBERTHAEnemy, 215, 151),
            FormationMember(TERRACOTTAEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BIGBERTHAEnemy, 215, 143),
            FormationMember(FORKIESEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BIGBERTHAEnemy, 151, 111),
            FormationMember(BIGBERTHAEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK118_SHIP_POSTGAME] = FormationPack(
    Formation(
        members=[
            FormationMember(JOHNNYEnemy2, 165, 121),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK119_DOJO_POSTGAME] = FormationPack(
    Formation(
        members=[
            FormationMember(JINXEnemy4, 181, 122),
            FormationMember(TeamGaugeEnemy, 36, 200),
        ],
        music=MidbossMusic())
)
packs[PACK120_NINJA_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(NINJAEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(NINJAEnemy, 151, 119),
            FormationMember(DOPPELEnemy, 199, 159),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(NINJAEnemy, 199, 151),
            FormationMember(NINJAEnemy, 135, 119),
            FormationMember(HIPPOPOEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK121_NINJA_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(NINJAEnemy, 135, 119),
            FormationMember(NINJAEnemy, 183, 127),
            FormationMember(NINJAEnemy, 167, 103),
            FormationMember(NINJAEnemy, 231, 135),
            FormationMember(NINJAEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(NINJAEnemy, 199, 151),
            FormationMember(NINJAEnemy, 135, 119),
            FormationMember(HIPPOPOEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(NINJAEnemy, 151, 119),
            FormationMember(DOPPELEnemy, 199, 159),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK122_SPRINGER_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(SPRINGEREnemy, 215, 143),
            FormationMember(GLUMREAPEREnemy, 135, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPRINGEREnemy, 231, 135),
            FormationMember(SPRINGEREnemy, 167, 103),
            FormationMember(PUPPOXEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPRINGEREnemy, 215, 143),
            FormationMember(GLUMREAPEREnemy, 135, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK123_SPRINGER_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(SPRINGEREnemy, 183, 127),
            FormationMember(PUPPOXEnemy, 215, 143),
            FormationMember(PUPPOXEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPRINGEREnemy, 231, 135),
            FormationMember(SPRINGEREnemy, 167, 103),
            FormationMember(PUPPOXEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(SPRINGEREnemy, 215, 143),
            FormationMember(GLUMREAPEREnemy, 135, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK124_MADMALLET_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(MADMALLETEnemyStatic, 151, 119),
            FormationMember(MADMALLETEnemyStatic, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MADMALLETEnemyStatic, 151, 127),
            FormationMember(MADMALLETEnemyStatic, 199, 151),
            FormationMember(MADMALLETEnemyStatic, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MADMALLETEnemyStatic, 183, 127),
            FormationMember(MADMALLETEnemyStatic, 135, 127),
            FormationMember(MADMALLETEnemyStatic, 231, 135),
            FormationMember(MADMALLETEnemyStatic, 167, 103),
            FormationMember(MADMALLETEnemyStatic, 183, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK125_MADMALLET_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(MADMALLETEnemyStatic, 183, 127),
            FormationMember(MADMALLETEnemyStatic, 135, 127),
            FormationMember(MADMALLETEnemyStatic, 231, 135),
            FormationMember(MADMALLETEnemyStatic, 167, 103),
            FormationMember(MADMALLETEnemyStatic, 183, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MADMALLETEnemyStatic, 151, 127),
            FormationMember(MADMALLETEnemyStatic, 199, 151),
            FormationMember(MADMALLETEnemyStatic, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MADMALLETEnemyStatic, 151, 119),
            FormationMember(MADMALLETEnemyStatic, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK126_POUNDER_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(POUNDEREnemyStatic, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(POUNDEREnemyStatic, 183, 127),
            FormationMember(POUNDEREnemyStatic, 231, 135),
            FormationMember(POUNDEREnemyStatic, 167, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(POUNDEREnemyStatic, 167, 135),
            FormationMember(POUNDEREnemyStatic, 199, 143),
            FormationMember(POUNDEREnemyStatic, 151, 119),
            FormationMember(POUNDEREnemyStatic, 167, 103),
            FormationMember(POUNDEREnemyStatic, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK126_POUNDER_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(POUNDEREnemyStatic, 167, 135),
            FormationMember(POUNDEREnemyStatic, 199, 143),
            FormationMember(POUNDEREnemyStatic, 151, 119),
            FormationMember(POUNDEREnemyStatic, 167, 103),
            FormationMember(POUNDEREnemyStatic, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(POUNDEREnemyStatic, 183, 127),
            FormationMember(POUNDEREnemyStatic, 231, 135),
            FormationMember(POUNDEREnemyStatic, 167, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(POUNDEREnemyStatic, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK128_POUNDETTE_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(POUNDETTEEnemyStatic, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(POUNDETTEEnemyStatic, 183, 127),
            FormationMember(POUNDETTEEnemyStatic, 151, 111),
            FormationMember(POUNDETTEEnemyStatic, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(POUNDETTEEnemyStatic, 167, 135),
            FormationMember(POUNDETTEEnemyStatic, 199, 119),
            FormationMember(POUNDETTEEnemyStatic, 135, 119),
            FormationMember(POUNDETTEEnemyStatic, 167, 103),
            FormationMember(POUNDETTEEnemyStatic, 199, 151),
            FormationMember(POUNDETTEEnemyStatic, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK128_POUNDETTE_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(POUNDETTEEnemyStatic, 167, 135),
            FormationMember(POUNDETTEEnemyStatic, 199, 119),
            FormationMember(POUNDETTEEnemyStatic, 135, 119),
            FormationMember(POUNDETTEEnemyStatic, 167, 103),
            FormationMember(POUNDETTEEnemyStatic, 199, 151),
            FormationMember(POUNDETTEEnemyStatic, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(POUNDETTEEnemyStatic, 183, 127),
            FormationMember(POUNDETTEEnemyStatic, 151, 111),
            FormationMember(POUNDETTEEnemyStatic, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(POUNDETTEEnemyStatic, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK130_AMEBOIDS] = FormationPack(
    Formation(
        members=[
            FormationMember(AMEBOIDEnemy, 183, 127),
            FormationMember(AMEBOIDEnemy, 167, 103, hidden_at_start=True),
            FormationMember(AMEBOIDEnemy, 135, 119, hidden_at_start=True),
            FormationMember(AMEBOIDEnemy, 231, 135, hidden_at_start=True),
            FormationMember(AMEBOIDEnemy, 199, 151, hidden_at_start=True),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK131_AMEBOIDS_DUPE] = FormationPack(
    Formation(
        members=[
            FormationMember(AMEBOIDEnemy, 183, 127),
            FormationMember(AMEBOIDEnemy, 167, 103, hidden_at_start=True),
            FormationMember(AMEBOIDEnemy, 135, 119, hidden_at_start=True),
            FormationMember(AMEBOIDEnemy, 231, 135, hidden_at_start=True),
            FormationMember(AMEBOIDEnemy, 199, 151, hidden_at_start=True),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK132_GLUMREAPER_WITH_HIPPOPO_DOPPEL] = FormationPack(
    Formation(
        members=[
            FormationMember(GLUMREAPEREnemy, 183, 127),
            FormationMember(GLUMREAPEREnemy, 135, 119),
            FormationMember(GLUMREAPEREnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GLUMREAPEREnemy, 215, 159),
            FormationMember(HIPPOPOEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GLUMREAPEREnemy, 151, 127),
            FormationMember(GLUMREAPEREnemy, 183, 143),
            FormationMember(DOPPELEnemy, 167, 103),
            FormationMember(DOPPELEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK133_GLUMREAPER_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(GLUMREAPEREnemy, 135, 111),
            FormationMember(GLUMREAPEREnemy, 215, 151),
            FormationMember(LILBOOEnemy, 167, 135),
            FormationMember(LILBOOEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GLUMREAPEREnemy, 151, 127),
            FormationMember(GLUMREAPEREnemy, 183, 143),
            FormationMember(DOPPELEnemy, 167, 103),
            FormationMember(DOPPELEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(GLUMREAPEREnemy, 215, 159),
            FormationMember(HIPPOPOEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK134_LILBOO_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(LILBOOEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(LILBOOEnemy, 183, 151),
            FormationMember(LILBOOEnemy, 215, 135),
            FormationMember(HIPPOPOEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(LILBOOEnemy, 167, 143),
            FormationMember(LILBOOEnemy, 199, 119),
            FormationMember(PUPPOXEnemy, 151, 103),
            FormationMember(DOPPELEnemy, 215, 159),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK135_LILBOO_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(LILBOOEnemy, 167, 135),
            FormationMember(LILBOOEnemy, 151, 111),
            FormationMember(LILBOOEnemy, 215, 143),
            FormationMember(LILBOOEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(LILBOOEnemy, 167, 143),
            FormationMember(LILBOOEnemy, 199, 119),
            FormationMember(PUPPOXEnemy, 151, 103),
            FormationMember(DOPPELEnemy, 215, 159),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(LILBOOEnemy, 183, 151),
            FormationMember(LILBOOEnemy, 215, 135),
            FormationMember(HIPPOPOEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK136_JABITS_HAMMERS_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(JABITEnemy, 215, 135),
            FormationMember(MADMALLETEnemyStatic, 151, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(JABITEnemy, 151, 143),
            FormationMember(POUNDEREnemyStatic, 151, 111),
            FormationMember(POUNDETTEEnemyStatic, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(JABITEnemy, 135, 119),
            FormationMember(JABITEnemy, 167, 135),
            FormationMember(JABITEnemy, 231, 135),
            FormationMember(JABITEnemy, 167, 103),
            FormationMember(JABITEnemy, 199, 119),
            FormationMember(JABITEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK137_JABITS_HAMMERS_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(JABITEnemy, 151, 127),
            FormationMember(JABITEnemy, 183, 143),
            FormationMember(MADMALLETEnemyStatic, 135, 103),
            FormationMember(MADMALLETEnemyStatic, 183, 111),
            FormationMember(POUNDETTEEnemyStatic, 215, 127),
            FormationMember(POUNDETTEEnemyStatic, 231, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(JABITEnemy, 135, 119),
            FormationMember(JABITEnemy, 167, 135),
            FormationMember(JABITEnemy, 231, 135),
            FormationMember(JABITEnemy, 167, 103),
            FormationMember(JABITEnemy, 199, 119),
            FormationMember(JABITEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(JABITEnemy, 151, 143),
            FormationMember(POUNDEREnemyStatic, 151, 111),
            FormationMember(POUNDETTEEnemyStatic, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK138_RATFUNKS_ONLY] = FormationPack(
    Formation(
        members=[
            FormationMember(RATFUNKEnemy, 135, 119),
            FormationMember(RATFUNKEnemy, 199, 151),
            FormationMember(RATFUNKEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(RATFUNKEnemy, 135, 127),
            FormationMember(RATFUNKEnemy, 167, 103),
            FormationMember(RATFUNKEnemy, 183, 151),
            FormationMember(RATFUNKEnemy, 231, 135),
            FormationMember(RATFUNKEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(RATFUNKEnemy, 135, 119),
            FormationMember(RATFUNKEnemy, 199, 151),
            FormationMember(RATFUNKEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK139_ARTICHOKERS_ONLY] = FormationPack(
    Formation(
        members=[
            FormationMember(ARTICHOKEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(ARTICHOKEREnemy, 151, 119),
            FormationMember(ARTICHOKEREnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(ARTICHOKEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK140_MINES_BOSS_2] = FormationPack(
    Formation(
        members=[
            FormationMember(PUNCHINELLOEnemy, 199, 119),
            FormationMember(MICROBOMBEnemy, 135, 119, hidden_at_start=True),
            FormationMember(MICROBOMBEnemy, 151, 135, hidden_at_start=True),
            FormationMember(MICROBOMBEnemy, 183, 151, hidden_at_start=True),
            FormationMember(MICROBOMBEnemy, 215, 159, hidden_at_start=True),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK141_MINES_HENCHMAN_LEFT] = FormationPack(
    Formation(
        members=[
            FormationMember(CROOKEnemyStatic, 135, 119),
            FormationMember(CROOKEnemyStatic, 199, 119),
            FormationMember(CROOKEnemyStatic, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CROOKEnemyStatic, 167, 103),
            FormationMember(CROOKEnemyStatic, 135, 119),
            FormationMember(CROOKEnemyStatic, 183, 127),
            FormationMember(CROOKEnemyStatic, 199, 151),
            FormationMember(CROOKEnemyStatic, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CROOKEnemyStatic, 135, 119),
            FormationMember(CROOKEnemyStatic, 199, 119),
            FormationMember(CROOKEnemyStatic, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK142_MINES_HENCHMAN_MIDDLE] = FormationPack(
    Formation(
        members=[
            FormationMember(CROOKEnemyStatic, 135, 119),
            FormationMember(CROOKEnemyStatic, 199, 119),
            FormationMember(CROOKEnemyStatic, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CROOKEnemyStatic, 167, 103),
            FormationMember(CROOKEnemyStatic, 135, 119),
            FormationMember(CROOKEnemyStatic, 183, 127),
            FormationMember(CROOKEnemyStatic, 199, 151),
            FormationMember(CROOKEnemyStatic, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CROOKEnemyStatic, 135, 119),
            FormationMember(CROOKEnemyStatic, 199, 119),
            FormationMember(CROOKEnemyStatic, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK143_TOWER_FIREBALLS] = FormationPack(
    Formation(
        members=[
            FormationMember(FIREBALLEnemy, 151, 111),
            FormationMember(FIREBALLEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(FIREBALLEnemy, 167, 135),
            FormationMember(FIREBALLEnemy, 167, 111),
            FormationMember(FIREBALLEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(FIREBALLEnemy, 151, 111),
            FormationMember(FIREBALLEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK144_STUMPET_ENCOUNTER] = FormationPack(
    Formation(
        members=[
            FormationMember(STUMPETEnemy, 183, 127),
            FormationMember(MAGMUSEnemy, 119, 127),
            FormationMember(MAGMUSEnemy, 183, 159),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(STUMPETEnemy, 151, 111),
            FormationMember(MAGMUSEnemy, 183, 159),
            FormationMember(MAGMUSEnemy, 199, 135),
            FormationMember(MAGMUSEnemy, 231, 159),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(STUMPETEnemy, 183, 127),
            FormationMember(MAGMUSEnemy, 119, 127),
            FormationMember(MAGMUSEnemy, 183, 159),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK145_CORKPEDITE_ENCOUNTER] = FormationPack(
    Formation(
        members=[
            FormationMember(CORKPEDITEEnemy, 151, 111),
            FormationMember(BODYEnemy, 167, 103),
            FormationMember(OERLIKONEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CORKPEDITEEnemy, 151, 111),
            FormationMember(BODYEnemy, 167, 103),
            FormationMember(OERLIKONEnemy, 183, 159),
            FormationMember(OERLIKONEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(CORKPEDITEEnemy, 151, 111),
            FormationMember(BODYEnemy, 167, 103),
            FormationMember(OERLIKONEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK146_FACTORY_BOSS_RUSH_1] = FormationPack(
    Formation(
        members=[
            FormationMember(CLERKEnemy, 199, 119),
            FormationMember(MADMALLETEnemyHenchman, 135, 119),
            FormationMember(MADMALLETEnemyHenchman, 199, 151),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK147_FACTORY_BOSS_RUSH_2] = FormationPack(
    Formation(
        members=[
            FormationMember(MANAGEREnemy, 199, 119),
            FormationMember(POUNDEREnemyHenchman, 151, 111),
            FormationMember(POUNDEREnemyHenchman, 167, 135),
            FormationMember(POUNDEREnemyHenchman, 215, 143),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK148_FACTORY_BOSS_RUSH_3] = FormationPack(
    Formation(
        members=[
            FormationMember(DIRECTOREnemy, 183, 127),
            FormationMember(POUNDETTEEnemyHenchman, 135, 119),
            FormationMember(POUNDETTEEnemyHenchman, 167, 103),
            FormationMember(POUNDETTEEnemyHenchman, 199, 151),
            FormationMember(POUNDETTEEnemyHenchman, 231, 135),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK149_FACTORY_BOSS_RUSH_4] = FormationPack(
    Formation(
        members=[
            FormationMember(GUNYOLKEnemy, 199, 103),
            FormationMember(FACTORYCHIEFEnemy, 231, 151),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK150_FACTORY_BOSS_RUSH_HENCHMAN] = FormationPack(
    Formation(
        members=[
            FormationMember(MADMALLETEnemyHenchman, 151, 111),
            FormationMember(MADMALLETEnemyHenchman, 167, 135),
            FormationMember(MADMALLETEnemyHenchman, 215, 143),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK151_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(APPRENTICEEnemyStatic, 183, 127),
        ],
        music=NormalBattleMusic(),
        can_run_away=False)
)
#
packs[PACK152_MINES_BOSS_ROOM_HENCHMAN] = FormationPack(
    Formation(
        members=[
            FormationMember(BOBOMBEnemyStatic, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BOBOMBEnemyStatic, 135, 119),
            FormationMember(BOBOMBEnemyStatic, 199, 151),
            FormationMember(CLUSTEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(BOBOMBEnemyStatic, 151, 127),
            FormationMember(BOBOMBEnemyStatic, 167, 103),
            FormationMember(BOBOMBEnemyStatic, 199, 151),
            FormationMember(BOBOMBEnemyStatic, 215, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK153_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(MACHINEMADEDrillbitEnemy, 183, 127),
            FormationMember(MACHINEMADEDrillbitEnemy, 167, 103),
            FormationMember(MACHINEMADEDrillbitEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK154_UNUSED] = FormationPack(
    # henchman
    Formation(
        members=[
            FormationMember(SHYGUYEnemyStatic, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK155_POSSIBLY_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(MADMALLETEnemyStatic, x_pos=151, y_pos=127),
            FormationMember(MADMALLETEnemyStatic, x_pos=199, y_pos=151),
            FormationMember(MADMALLETEnemyStatic, x_pos=199, y_pos=119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK156_SEWER_CHEST_FIGHT] = FormationPack(
    Formation(
        members=[
            FormationMember(PANDORITEEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK157_SHIP_CHEST_FIGHT] = FormationPack(
    Formation(
        members=[
            FormationMember(HIDONEnemy, 167, 119),
            FormationMember(GOOMBETTEEnemy, 135, 111, hidden_at_start=True),
            FormationMember(GOOMBETTEEnemy, 135, 135, hidden_at_start=True),
            FormationMember(GOOMBETTEEnemy, 167, 151, hidden_at_start=True),
            FormationMember(GOOMBETTEEnemy, 215, 151, hidden_at_start=True),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)

packs[PACK158_VALLEY_CHEST_FIGHT] = FormationPack(
    Formation(
        members=[
            FormationMember(BOXBOYEnemy, 183, 127),
            FormationMember(FAUTSOEnemy, 151, 111, hidden_at_start=True),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK159_SIX_DOOR_RUSH_FIGHT] = FormationPack(
    Formation(
        members=[
            FormationMember(CHESTEREnemy, 183, 127),
            FormationMember(BAHAMUTTEnemy2, 135, 119, hidden_at_start=True),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK160_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(AEROEnemy, x_pos=167, y_pos=119),
            FormationMember(AEROEnemy, x_pos=199, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK161_TOWER_FIRST_FIGHT] = FormationPack(
    Formation(
        members=[
            FormationMember(BOOSTEREnemy, 183, 127),
            FormationMember(SNIFITEnemyHenchman, 135, 119),
            FormationMember(SNIFITEnemyHenchman, 151, 143),
            FormationMember(SNIFITEnemyHenchman, 199, 151),
        ],
        run_event_at_load=BE0012_DIALOGUE_FROM_BOOSTER_FIGHT,
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK162__UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(BOOSTEREnemy2, 183, 127),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK163_BANDITS_WAY_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(CROCO1Enemy, 183, 127),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK164_MINES_FIRST_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(CROCO2Enemy, 183, 127),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK165_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(MACHINEMADEAxemBlackEnemy, 183, 127),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK166_SHIP_SECOND_BOSS] = FormationPack(
    Formation(
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
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK167_SHIP_FIRST_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(KINGCALAMARIEnemy, 222, 94, hidden_at_start=True),
            FormationMember(TENTACLESEnemy2, 136, 115, hidden_at_start=True),
            FormationMember(TENTACLESEnemy2, 112, 127, hidden_at_start=True),
            FormationMember(TENTACLESEnemy, 193, 143, hidden_at_start=True),
            FormationMember(TENTACLESEnemy, 168, 156, hidden_at_start=True),
            FormationMember(TENTACLESEnemy, 135, 143, hidden_at_start=True),
        ],
        run_event_at_load=BE0026_INTRO_SCENE_TENTACLES_RISE_FROM_HOLES,
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK168_SEWER_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(BELOME1Enemy, 183, 127),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK169_TEMPLE_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(BELOME2Enemy, 183, 127),
            FormationMember(MARIOCLONEEnemy, 135, 119, hidden_at_start=True),
            FormationMember(TOADSTOOL2Enemy, 215, 159, hidden_at_start=True),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK170_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(TERRAPINEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK171_NIMBUS_CASTLE_THIRD_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(VALENTINAEnemy, 183, 127),
            FormationMember(DODOEnemy, 199, 151, hidden_at_start=True),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK172_VOLCANO_FIRST_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(CZARDRAGONEnemy, 183, 143),
            FormationMember(ZOMBONEEnemy, 183, 143, hidden_at_start=True),
            FormationMember(HELIOEnemy, 167, 119, hidden_at_start=True),
            FormationMember(HELIOEnemy, 135, 135, hidden_at_start=True),
            FormationMember(HELIOEnemy, 199, 167, hidden_at_start=True),
            FormationMember(HELIOEnemy, 231, 151, hidden_at_start=True),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK173_VALLEY_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(SMILAXEnemy, 180, 157),
            FormationMember(SMILAXEnemy, 164, 175, hidden_at_start=True),
            FormationMember(SMILAXEnemy, 143, 119, hidden_at_start=True),
            FormationMember(SMILAXEnemy, 207, 151, hidden_at_start=True),
            FormationMember(SMILAXEnemy, 191, 127, hidden_at_start=True),
            FormationMember(MEGASMILAXEnemy, 175, 111, hidden_at_start=True),
        ],
        run_event_at_load=BE0058_THRAX_IS_THERE,
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK174_FACTORY_FIRST_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(COUNTDOWNEnemy, 150, 93),
            FormationMember(DINGALINGEnemy, 158, 52),
            FormationMember(DINGALINGEnemy, 194, 67),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK175_NIMBUS_CASTLE_SECOND_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(BIRDETTAEnemy, 167, 118, hidden_at_start=True),
            FormationMember(SHELLYEnemy, 171, 103),
            FormationMember(EGGBERTEnemy, 135, 119, hidden_at_start=True),
            FormationMember(EGGBERTEnemy, 135, 135, hidden_at_start=True),
            FormationMember(EGGBERTEnemy, 167, 151, hidden_at_start=True),
            FormationMember(EGGBERTEnemy, 199, 151, hidden_at_start=True),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK176_CHAPEL_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(BUNDTEnemy, 199, 127),
            FormationMember(RASPBERRYEnemy, 199, 119),
            FormationMember(TORTEEnemy, 199, 151),
            FormationMember(TORTEEnemy, 135, 119),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK177_TOWER_SECOND_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(KNIFEGUYEnemy, 151, 119),
            FormationMember(GRATEGUYEnemy, 199, 143),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK178_DOJO_FIGHT_1] = FormationPack(
    Formation(
        members=[
            FormationMember(JINX1Enemy, 183, 127),
        ],
        run_event_at_load=BE0071_JINX_USES_TRIPLE_KICK,
        music=MidbossMusic())
)
#
packs[PACK179_MUSHROOM_KINGDOM_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(MACKEnemy, 199, 119),
            FormationMember(BODYGUARDEnemy, 135, 111),
            FormationMember(BODYGUARDEnemy, 151, 127),
            FormationMember(BODYGUARDEnemy, 183, 143),
            FormationMember(BODYGUARDEnemy, 215, 151),
        ],
        music=BossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK180_SEASIDE_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(YARIDOVICHEnemy, 183, 127),
            FormationMember(YARIDOVICHMirageEnemy, 183, 127, hidden_at_start=True),
        ],
        music=BossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK181_FOREST_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(BOWYEREnemy, 183, 127),
        ],
        run_event_at_load=BE0014_SET_7EE00A_TO_PARTY_SIZE_AT_START_OF_FIGHT,
        music=BossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK182_VOLCANO_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(AXEMRANGERSEnemy, 201, 79),
            FormationMember(AXEMREDEnemy, 135, 111, hidden_at_start=True),
            FormationMember(AXEMBLACKEnemy, 135, 127, hidden_at_start=True),
            FormationMember(AXEMPINKEnemy, 151, 143, hidden_at_start=True),
            FormationMember(AXEMGREENEnemy, 183, 151, hidden_at_start=True),
            FormationMember(AXEMYELLOWEnemy, 215, 151, hidden_at_start=True),
        ],
        run_event_at_load=BE0061_ONLY_MARIO_IS_THERE,
        music=BossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK183_MUSHROOM_WAY_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(HAMMERBROEnemy, 135, 127),
            FormationMember(HAMMERBROEnemy, 199, 143),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK184_FACTORY_SECOND_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(CLOAKEREnemy, 151, 111),
            FormationMember(DOMINOEnemy, 215, 159),
            FormationMember(MADADDEREnemy, 167, 135, hidden_at_start=True),
        ],
        run_event_at_load=BE0052_INTRO_SCENE_DOMINO_CLOAKER_S_INTRODUCTION,
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK185_FINAL_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(SMITHY1Enemy, 199, 127),
            FormationMember(SMELTEREnemy, 87, 87),
            FormationMember(MACHINEMADEBodyguardEnemy, 135, 127, hidden_at_start=True),
            FormationMember(MACHINEMADEBodyguardEnemy, 199, 159, hidden_at_start=True),
        ],
        music=Smithy1Music(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK186_KEEP_THIRD_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(EXOREnemy, 193, 64),
            FormationMember(NEOSQUIDEnemy, 187, 136),
            FormationMember(RIGHTEYEEnemy, 174, 145, hidden_at_start=True),
            FormationMember(LEFTEYEEnemy, 203, 157, hidden_at_start=True),
        ],
        run_event_at_load=BE0080_EXOR_FIGHT_BEGINS,
        music=BossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK187_DOJO_SECOND_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(JINX2Enemy, 183, 127),
        ],
        run_event_at_load=BE0072_JINX_USES_QUICKSILVER,
        music=MidbossMusic())
)
#
packs[PACK188_DOJO_THIRD_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(JINX3Enemy, 183, 127),
        ],
        run_event_at_load=BE0073_JINX_USES_BOMBS_AWAY,
        music=MidbossMusic())
)
#
packs[PACK189_DOJO_PREFIGHT] = FormationPack(
    Formation(
        members=[
            FormationMember(JAGGEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK190_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(PYROSPHEREEnemy, x_pos=151, y_pos=135),
            FormationMember(PYROSPHEREEnemy, x_pos=215, y_pos=135),
            FormationMember(PYROSPHEREEnemy, x_pos=183, y_pos=103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK191_HEAVY_TROOPAS] = FormationPack(
    Formation(
        members=[
            FormationMember(HEAVYTROOPAEnemy, 167, 135),
            FormationMember(HEAVYTROOPAEnemy, 151, 103),
            FormationMember(HEAVYTROOPAEnemy, 231, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK192_UNUSED] = FormationPack(
    Formation(
        members=[
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK193_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(HELIOEnemy, x_pos=167, y_pos=119),
            FormationMember(HELIOEnemy, x_pos=135, y_pos=135),
            FormationMember(HELIOEnemy, x_pos=199, y_pos=167),
            FormationMember(HELIOEnemy, x_pos=231, y_pos=151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK194_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(BODYGUARDEnemy, x_pos=167, y_pos=119),
            FormationMember(BODYGUARDEnemy, x_pos=199, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True),
    Formation(
        members=[
            FormationMember(BODYGUARDEnemy, x_pos=151, y_pos=111),
            FormationMember(BODYGUARDEnemy, x_pos=215, y_pos=143),
            FormationMember(BODYGUARDEnemy, x_pos=167, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True),
    Formation(
        members=[
            FormationMember(BODYGUARDEnemy, x_pos=167, y_pos=119),
            FormationMember(BODYGUARDEnemy, x_pos=199, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True))
#
packs[PACK195_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(BODYGUARDEnemy, x_pos=167, y_pos=119),
            FormationMember(BODYGUARDEnemy, x_pos=199, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True),
    Formation(
        members=[
            FormationMember(BODYGUARDEnemy, x_pos=151, y_pos=111),
            FormationMember(BODYGUARDEnemy, x_pos=215, y_pos=143),
            FormationMember(BODYGUARDEnemy, x_pos=167, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True),
    Formation(
        members=[
            FormationMember(BODYGUARDEnemy, x_pos=151, y_pos=111),
            FormationMember(BODYGUARDEnemy, x_pos=215, y_pos=143),
            FormationMember(BODYGUARDEnemy, x_pos=167, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True))
#
packs[PACK196_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(GENOCLONEEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK197_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(BOWSERCLONEEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK198_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(TOADSTOOL2Enemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
packs[PACK199_CROOKS_ONLY] = FormationPack(
    Formation(
        members=[
            FormationMember(CROOKEnemyStatic, x_pos=135, y_pos=119),
            FormationMember(CROOKEnemyStatic, x_pos=199, y_pos=119),
            FormationMember(CROOKEnemyStatic, x_pos=199, y_pos=151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True),
    Formation(
        members=[
            FormationMember(CROOKEnemyStatic, x_pos=167, y_pos=103),
            FormationMember(CROOKEnemyStatic, x_pos=135, y_pos=119),
            FormationMember(CROOKEnemyStatic, x_pos=183, y_pos=127),
            FormationMember(CROOKEnemyStatic, x_pos=199, y_pos=151),
            FormationMember(CROOKEnemyStatic, x_pos=231, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True),
    Formation(
        members=[
            FormationMember(CROOKEnemyStatic, x_pos=135, y_pos=119),
            FormationMember(CROOKEnemyStatic, x_pos=199, y_pos=119),
            FormationMember(CROOKEnemyStatic, x_pos=199, y_pos=151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True))
#
packs[PACK200_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(MARIOCLONEEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK201_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(BIRDYEnemyStatic, x_pos=215, y_pos=119),
            FormationMember(BIRDYEnemyStatic, x_pos=151, y_pos=119),
            FormationMember(BIRDYEnemyStatic, x_pos=183, y_pos=151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True),
    Formation(
        members=[
            FormationMember(BIRDYEnemyStatic, x_pos=151, y_pos=111),
            FormationMember(BIRDYEnemyStatic, x_pos=215, y_pos=143),
            FormationMember(BIRDYEnemyStatic, x_pos=151, y_pos=143),
            FormationMember(BIRDYEnemyStatic, x_pos=215, y_pos=111),
            FormationMember(BIRDYEnemyStatic, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True),
    Formation(
        members=[
            FormationMember(BIRDYEnemyStatic, x_pos=215, y_pos=119),
            FormationMember(BIRDYEnemyStatic, x_pos=151, y_pos=119),
            FormationMember(BIRDYEnemyStatic, x_pos=183, y_pos=151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK202_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(MALLOWCLONEEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK203_UNUSED] = FormationPack(
    Formation(
        [
            FormationMember(MACHINEMADEAxemPinkEnemy, x_pos=151, y_pos=111),
            None,
            FormationMember(MACHINEMADEAxemRedEnemy, x_pos=151, y_pos=143),
            None,
            FormationMember(MACHINEMADEAxemGreenEnemy, x_pos=215, y_pos=143),
        ],
        music=BossMusic(),
        unknown_bit=True),
    Formation(
        [
            FormationMember(MACHINEMADEAxemBlackEnemy, x_pos=151, y_pos=119),
            FormationMember(MACHINEMADEAxemBlackEnemy, x_pos=231, y_pos=127),
            FormationMember(MACHINEMADEAxemYellowEnemy, x_pos=199, y_pos=143),
            FormationMember(MACHINEMADEAxemYellowEnemy, x_pos=183, y_pos=103),
        ],
        music=BossMusic(),
        unknown_bit=True),
    Formation(
        [
            FormationMember(MACHINEMADEAxemPinkEnemy, x_pos=151, y_pos=111),
            None,
            FormationMember(MACHINEMADEAxemRedEnemy, x_pos=151, y_pos=143),
            None,
            FormationMember(MACHINEMADEAxemGreenEnemy, x_pos=215, y_pos=143),
        ],
        music=BossMusic(),
        unknown_bit=True))
#
packs[PACK204_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(BLOOBEREnemyStatic, x_pos=183, y_pos=127),
            FormationMember(BLOOBEREnemyStatic, x_pos=231, y_pos=143),
            FormationMember(BLOOBEREnemyStatic, x_pos=135, y_pos=111),
        ],
        music=None)
)
#
packs[PACK205_UNUSED] = FormationPack(
    # henchmen
    Formation(
        members=[
            FormationMember(BLUEBIRDEnemyStatic, x_pos=199, y_pos=151),
            FormationMember(BLUEBIRDEnemyStatic, x_pos=151, y_pos=111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True),
    Formation(
        members=[
            FormationMember(BLUEBIRDEnemyStatic, x_pos=183, y_pos=143),
            FormationMember(BLUEBIRDEnemyStatic, x_pos=183, y_pos=111),
            FormationMember(BLUEBIRDEnemyStatic, x_pos=231, y_pos=135),
            FormationMember(BLUEBIRDEnemyStatic, x_pos=135, y_pos=119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True),
    Formation(
        members=[
            FormationMember(BLUEBIRDEnemyStatic, x_pos=199, y_pos=151),
            FormationMember(BLUEBIRDEnemyStatic, x_pos=151, y_pos=111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True))
packs[PACK206_DESERT_SHOGUNS] = FormationPack(
    Formation(
        members=[
            FormationMember(SHOGUNEnemy, 167, 135),
            FormationMember(SHOGUNEnemy, 151, 111),
            FormationMember(SHOGUNEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK207_LANDS_END_CLOUD] = FormationPack(
    Formation(
        members=[
            FormationMember(FORMLESSEnemy, 167, 135),
            FormationMember(MOKURAEnemy, 167, 135, hidden_at_start=True),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK208_NIMBUS_CASTLE_FIRST_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(DODOEnemySolo, 183, 127),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK209_KEEP_FIRST_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(KAMEKEnemy, 215, 111),
            FormationMember(TERRAPINEnemy, 167, 135, hidden_at_start=True),
        ],
        run_event_at_load=BE0101_MAGIKOOPA_IS_THERE,
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK210_KEEP_SECOND_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(BOOMEREnemy, 215, 143),
            FormationMember(HANGINSHYEnemy, 66, 115),
            FormationMember(HANGINSHYEnemy, 186, 74),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK211_MACHINE_MACK_PACK] = FormationPack(
    Formation(
        members=[
            FormationMember(MACHINEMADEMackEnemy, 199, 119),
            FormationMember(MACHINEMADEBodyguardEnemy, 135, 111),
            FormationMember(MACHINEMADEBodyguardEnemy, 151, 127),
            FormationMember(MACHINEMADEBodyguardEnemy, 183, 143),
            FormationMember(MACHINEMADEBodyguardEnemy, 215, 151),
        ],
        music=BossMusic(),
        unknown_bit=True)
)
packs[PACK212_MACHINE_BOWYER_PACK] = FormationPack(
    Formation(
        members=[
            FormationMember(MACHINEMADEBowyerEnemy, 183, 127),
        ],
        music=BossMusic(),
        unknown_bit=True)
)
packs[PACK213_MACHINE_YARIDOVICH_PACK] = FormationPack(
    Formation(
        members=[
            FormationMember(MACHINEMADEYaridovichEnemy, 183, 127),
            FormationMember(MACHINEMADEDrillbitEnemy, 135, 119, hidden_at_start=True),
            FormationMember(MACHINEMADEDrillbitEnemy, 167, 103, hidden_at_start=True),
            FormationMember(MACHINEMADEDrillbitEnemy, 199, 151, hidden_at_start=True),
            FormationMember(MACHINEMADEDrillbitEnemy, 231, 135, hidden_at_start=True),
        ],
        music=BossMusic(),
        unknown_bit=True)
)
packs[PACK214_FACTORY_MACHINE_AXEMS] = FormationPack(
    Formation(
        members=[
            FormationMember(MACHINEMADEAxemPinkEnemy, 151, 111),
            None,
            FormationMember(MACHINEMADEAxemRedEnemy, 151, 143),
            None,
            FormationMember(MACHINEMADEAxemGreenEnemy, 215, 143),
        ],
        music=BossMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MACHINEMADEAxemBlackEnemy, 151, 119),
            FormationMember(MACHINEMADEAxemBlackEnemy, 231, 127),
            FormationMember(MACHINEMADEAxemYellowEnemy, 199, 143),
            FormationMember(MACHINEMADEAxemYellowEnemy, 183, 103),
        ],
        music=BossMusic(),
        unknown_bit=True)
    ,
    Formation(
        members=[
            FormationMember(MACHINEMADEAxemPinkEnemy, 151, 111),
            None,
            FormationMember(MACHINEMADEAxemRedEnemy, 151, 143),
            None,
            FormationMember(MACHINEMADEAxemGreenEnemy, 215, 143),
        ],
        music=BossMusic(),
        unknown_bit=True)
)
packs[PACK215_SMITHY_2_PACK] = FormationPack(
    Formation(
        members=[
            FormationMember(SMITHYBodyEnemy, 183, 135, hidden_at_start=True),
            FormationMember(SMITHY2Enemy, 183, 175),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK216_MONSTRO_DOOR_BOSS] = FormationPack(
    Formation(
        members=[
            FormationMember(CULEXEnemy, 183, 103),
            FormationMember(FIRECRYSTALEnemy, 135, 103, hidden_at_start=True),
            FormationMember(WATERCRYSTALEnemy, 151, 119, hidden_at_start=True),
            FormationMember(EARTHCRYSTALEnemy, 183, 135, hidden_at_start=True),
            FormationMember(WINDCRYSTALEnemy, 215, 143, hidden_at_start=True),
        ],
        music=CulexMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK217_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(FIRECRYSTALEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
        run_event_at_load=BE0076_SOLO_FIRE_CRYSTAL_APPEARS)
)
#
packs[PACK218_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(WATERCRYSTALEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
        run_event_at_load=BE0020_SOLO_WATER_CRYSTAL_APPEARS
    )
)
#
packs[PACK219_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(EARTHCRYSTALEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
        run_event_at_load=BE0011_SOLO_EARTH_CRYSTAL_APPEARS
    )
)
#
packs[PACK220_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(WINDCRYSTALEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
        run_event_at_load=BE0001_SOLO_WIND_CRYSTAL_APPEARS
    )
)
#
packs[PACK221_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(GOOMBETTEEnemy, x_pos=183, y_pos=127),
            FormationMember(GOOMBETTEEnemy, x_pos=231, y_pos=135),
            FormationMember(GOOMBETTEEnemy, x_pos=167, y_pos=103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
# 
packs[PACK222_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(PIRANHAPLANTEnemyStatic, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True), 
    Formation(
        [
            FormationMember(PIRANHAPLANTEnemyStatic, x_pos=167, y_pos=111),
            FormationMember(PIRANHAPLANTEnemyStatic, x_pos=167, y_pos=135),
            FormationMember(PIRANHAPLANTEnemyStatic, x_pos=215, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True),
    Formation(
        [
            FormationMember(PIRANHAPLANTEnemyStatic, x_pos=151, y_pos=143),
            FormationMember(PIRANHAPLANTEnemyStatic, x_pos=151, y_pos=111),
            FormationMember(PIRANHAPLANTEnemyStatic, x_pos=199, y_pos=119),
            FormationMember(PIRANHAPLANTEnemyStatic, x_pos=231, y_pos=143),
            FormationMember(PIRANHAPLANTEnemyStatic, x_pos=199, y_pos=159),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK223_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(EGGBERTEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True),
    Formation(
        members=[
            FormationMember(EGGBERTEnemy, x_pos=167, y_pos=111),
            FormationMember(EGGBERTEnemy, x_pos=167, y_pos=135),
            FormationMember(EGGBERTEnemy, x_pos=215, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True),
    Formation(
        members=[
            FormationMember(EGGBERTEnemy, x_pos=135, y_pos=127),
            FormationMember(EGGBERTEnemy, x_pos=183, y_pos=111),
            FormationMember(EGGBERTEnemy, x_pos=183, y_pos=151),
            FormationMember(EGGBERTEnemy, x_pos=231, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True))
packs[PACK224_OBSTACLE_TERRA_COTTA] = FormationPack(
    Formation(
        members=[
            FormationMember(TERRACOTTAEnemy, 135, 127),
            FormationMember(TERRACOTTAEnemy, 183, 111),
            FormationMember(TERRACOTTAEnemy, 183, 151),
            FormationMember(TERRACOTTAEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK225_OBSTACLE_OERLIKON] = FormationPack(
    Formation(
        members=[
            FormationMember(OERLIKONEnemy, 135, 119),
            FormationMember(OERLIKONEnemy, 199, 151),
            FormationMember(STARCRUSTEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK226_OBSTACLE_SACKIT] = FormationPack(
    Formation(
        members=[
            FormationMember(SACKITEnemy, 167, 135),
            None,
            FormationMember(BIGBERTHAEnemy, 151, 103),
            FormationMember(BIGBERTHAEnemy, 231, 143),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK227_OBSTACLE_CHOW] = FormationPack(
    Formation(
        members=[
            FormationMember(CHOWEnemy, 135, 111),
            FormationMember(CHOWEnemy, 215, 151),
            FormationMember(FORKIESEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK228_OBSTACLE_ALLEYRAT] = FormationPack(
    Formation(
        members=[
            FormationMember(ALLEYRATEnemy, 199, 119),
            FormationMember(ARMOREDANTEnemy, 135, 119),
            FormationMember(ARMOREDANTEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK229_OBSTACLE_BLOOBER] = FormationPack(
    Formation(
        members=[
            FormationMember(BLOOBEREnemyStatic, 199, 119),
            FormationMember(BLOOBEREnemyStatic, 183, 151),
            FormationMember(BLOOBEREnemyStatic, 231, 151),
            FormationMember(STARCRUSTEREnemy, 135, 103),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK230_OBSTACLE_STINGER] = FormationPack(
    Formation(
        members=[
            FormationMember(STINGEREnemy, 151, 111),
            FormationMember(STINGEREnemy, 167, 127),
            FormationMember(STINGEREnemy, 199, 143),
            FormationMember(STINGEREnemy, 231, 151),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK231_OBSTACLE_GECKIT] = FormationPack(
    Formation(
        members=[
            FormationMember(GECKITEnemy, 215, 151),
            FormationMember(GECKITEnemy, 135, 111),
            FormationMember(CHAINEDKONGEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK232_OBSTACLE_ROBOMB] = FormationPack(
    Formation(
        members=[
            FormationMember(ROBOMBEnemy, 167, 135),
            None,
            FormationMember(BIGBERTHAEnemy, 167, 111),
            FormationMember(BIGBERTHAEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK233_OBSTACLE_VOMER] = FormationPack(
    Formation(
        members=[
            FormationMember(VOMEREnemy, 151, 127),
            FormationMember(VOMEREnemy, 183, 143),
            FormationMember(VOMEREnemy, 151, 103),
            FormationMember(VOMEREnemy, 231, 143),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK234_OBSTACLE_MAGMUS] = FormationPack(
    Formation(
        members=[
            FormationMember(MAGMUSEnemy, 151, 127),
            FormationMember(MAGMUSEnemy, 183, 143),
            FormationMember(PULSAREnemy, 151, 103),
            FormationMember(PULSAREnemy, 231, 143),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
#
packs[PACK235_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(CHESTEREnemy, 183, 127),
            FormationMember(BAHAMUTTEnemy, 135, 119, hidden_at_start=True),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK236_OBSTACLE_GUGOOMBA] = FormationPack(
    Formation(
        members=[
            FormationMember(GUGOOMBAEnemy, 151, 127),
            FormationMember(GUGOOMBAEnemy, 183, 143),
            FormationMember(GUGOOMBAEnemy, 199, 119),
            FormationMember(GUGOOMBAEnemy, 167, 103),
            FormationMember(GUGOOMBAEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK237_OBSTACLE_MALAKOOPA] = FormationPack(
    Formation(
        members=[
            FormationMember(MALAKOOPAEnemy, 135, 111),
            FormationMember(MALAKOOPAEnemy, 215, 151),
            FormationMember(TUBOTROOPAEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK238_OBSTACLE_BIGBOO] = FormationPack(
    Formation(
        members=[
            FormationMember(THEBIGBOOEnemy, 183, 143),
            FormationMember(THEBIGBOOEnemy, 151, 127),
            FormationMember(ORBISONEnemy, 167, 103),
            FormationMember(ORBISONEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK239_OBSTACLE_SLINGSHY] = FormationPack(
    Formation(
        members=[
            FormationMember(SLINGSHYEnemy, 167, 135),
            FormationMember(SLINGSHYEnemy, 167, 119),
            FormationMember(SLINGSHYEnemy, 199, 135),
            FormationMember(SLINGSHYEnemy, 167, 103),
            FormationMember(SLINGSHYEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK240_OBSTACLE_CHEWY] = FormationPack(
    Formation(
        members=[
            FormationMember(CHEWYEnemy, 151, 127),
            FormationMember(CHEWYEnemy, 183, 143),
            FormationMember(SHYAWAYEnemy, 167, 103),
            FormationMember(SHYAWAYEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK241_OBSTACLE_KIPPER] = FormationPack(
    Formation(
        members=[
            FormationMember(MRKIPPEREnemy, 167, 135),
            FormationMember(MUCKLEEnemy, 167, 103),
            FormationMember(MUCKLEEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK242_OBSTACLE_AMANITA] = FormationPack(
    Formation(
        members=[
            FormationMember(AMANITAEnemy, 215, 143),
            FormationMember(AMANITAEnemy, 151, 111),
            FormationMember(ORBISONEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK243_OBSTACLE_GREAPER] = FormationPack(
    Formation(
        members=[
            FormationMember(GREAPEREnemy, 215, 143),
            FormationMember(GREAPEREnemy, 151, 111),
            FormationMember(GLUMREAPEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK244_OBSTACLE_PYROSPHERE] = FormationPack(
    Formation(
        members=[
            FormationMember(PYROSPHEREEnemy, 183, 127),
            FormationMember(PYROSPHEREEnemy, 151, 111),
            FormationMember(PYROSPHEREEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK245_OBSTACLE_LAKITU] = FormationPack(
    Formation(
        members=[
            FormationMember(LAKITUEnemy, 183, 127),
            FormationMember(LAKITUEnemy, 151, 111),
            FormationMember(LAKITUEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK246_OBSTACLE_ZEOSTAR] = FormationPack(
    Formation(
        members=[
            FormationMember(ZEOSTAREnemy, 151, 127),
            FormationMember(ZEOSTAREnemy, 183, 143),
            FormationMember(SHAMANEnemy, 167, 103),
            FormationMember(SHAMANEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True)
)
packs[PACK247_OBSTACLE_SHAMANS] = FormationPack(
    Formation(
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
        unknown_bit=True)
)
#
packs[PACK248_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(AXEMBLACKEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK249_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(AXEMPINKEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK250_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(AXEMYELLOWEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK251_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(AXEMGREENEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
# 
packs[PACK252_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(DINGALINGEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
# 
packs[PACK253_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(DRILLBITEnemy, x_pos=135, y_pos=119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True)
)
#
packs[PACK254_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(DRILLBITEnemy, x_pos=167, y_pos=103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True))
#
packs[PACK255_UNUSED] = FormationPack(
    Formation(
        members=[],
        music=NormalBattleMusic(),
        unknown_bit=True)
)

# Pack Collection
pack_collection = PackCollection(packs)
