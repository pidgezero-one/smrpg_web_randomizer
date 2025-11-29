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


# Initialize packs array with None values
packs: list[FormationPack] = [None] * 256 # type: ignore


packs[PACK000_SNIFIT_FIGHT] = FormationPack(
    # henchman
    Formation(
        members=[
            FormationMember(SNIFITEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK001_BOBOMB_HENCHMEN] = FormationPack(
    # henchman
    Formation(
        members=[
            FormationMember(BOBOMBEnemy, x_pos=183, y_pos=127)
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),

    Formation(
        members=[
            FormationMember(BOBOMBEnemy, x_pos=151, y_pos=127),
            FormationMember(BOBOMBEnemy, x_pos=167, y_pos=103),
            FormationMember(BOBOMBEnemy, x_pos=199, y_pos=151),
            FormationMember(BOBOMBEnemy, x_pos=215, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),

    Formation(
        members=[
            FormationMember(BOBOMBEnemy, x_pos=151, y_pos=127),
            FormationMember(BOBOMBEnemy, x_pos=167, y_pos=103),
            FormationMember(BOBOMBEnemy, x_pos=199, y_pos=151),
            FormationMember(BOBOMBEnemy, x_pos=215, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK002_SPIKEYS_AND_TROOPAS] = FormationPack(
    Formation(
        members=[
            FormationMember(SPIKEYEnemy, 135, 127),
            FormationMember(SPIKEYEnemy, 199, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPIKEYEnemy, 135, 119),
            FormationMember(SKYTROOPAEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPIKEYEnemy, 135, 119),
            FormationMember(SKYTROOPAEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK003_SPIKEYS_AND_FROGS] = FormationPack(
    Formation(
        members=[
            FormationMember(SPIKEYEnemy, 135, 119),
            FormationMember(SPIKEYEnemy, 199, 119),
            FormationMember(SPIKEYEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPIKEYEnemy, 135, 119),
            FormationMember(SPIKEYEnemy, 199, 151),
            FormationMember(FROGOGEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPIKEYEnemy, 135, 119),
            FormationMember(SPIKEYEnemy, 199, 151),
            FormationMember(FROGOGEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK004_JUST_TROOPAS] = FormationPack(
    Formation(
        members=[
            FormationMember(SKYTROOPAEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SKYTROOPAEnemy, 135, 119),
            FormationMember(SKYTROOPAEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SKYTROOPAEnemy, 135, 119),
            FormationMember(SKYTROOPAEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SKYTROOPAEnemy, 199, 151),
            FormationMember(SKYTROOPAEnemy, 135, 119),
            FormationMember(FROGOGEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SKYTROOPAEnemy, 135, 119),
            FormationMember(SKYTROOPAEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK006_JUST_GOOMBAS] = FormationPack(
    Formation(
        members=[
            FormationMember(GOOMBAEnemy, 135, 119),
            FormationMember(GOOMBAEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GOOMBAEnemy, 167, 111),
            FormationMember(GOOMBAEnemy, 167, 135),
            FormationMember(GOOMBAEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GOOMBAEnemy, 135, 119),
            FormationMember(GOOMBAEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK007_GOOMBAS_WITH_FROGS_OR_SPIKEYS] = FormationPack(
    Formation(
        members=[
            FormationMember(GOOMBAEnemy, 167, 135),
            FormationMember(FROGOGEnemy, 167, 111),
            FormationMember(SPIKEYEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GOOMBAEnemy, 167, 111),
            FormationMember(GOOMBAEnemy, 215, 135),
            FormationMember(SPIKEYEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GOOMBAEnemy, 167, 111),
            FormationMember(GOOMBAEnemy, 167, 135),
            FormationMember(GOOMBAEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK008_K9S_WITH_SPIKEYS] = FormationPack(
    Formation(
        members=[
            FormationMember(K9Enemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(K9Enemy, 199, 159),
            FormationMember(K9Enemy, 151, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(K9Enemy, 135, 119),
            FormationMember(K9Enemy, 199, 151),
            FormationMember(SPIKEYEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK009_K9S_WITH_SPIKEYS_OR_FROGS] = FormationPack(
    Formation(
        members=[
            FormationMember(K9Enemy, 183, 127),
            FormationMember(FROGOGEnemy, 215, 143),
            FormationMember(FROGOGEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(K9Enemy, 135, 119),
            FormationMember(K9Enemy, 199, 151),
            FormationMember(SPIKEYEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(K9Enemy, 199, 159),
            FormationMember(K9Enemy, 151, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK010_REGULAR_SHYSTERS_BIASED_2] = FormationPack(
    # field
    Formation(
        members=[
            FormationMember(SHYSTEREnemy, 167, 119),
            FormationMember(SHYSTEREnemy, 199, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SHYSTEREnemy, 151, 111),
            FormationMember(SHYSTEREnemy, 215, 143),
            FormationMember(SHYSTEREnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SHYSTEREnemy, 167, 119),
            FormationMember(SHYSTEREnemy, 199, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK011_REGULAR_SHYSTERS_BIASED_3] = FormationPack(
    # field
    Formation(
        members=[
            FormationMember(SHYSTEREnemy, 167, 119),
            FormationMember(SHYSTEREnemy, 199, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SHYSTEREnemy, 151, 111),
            FormationMember(SHYSTEREnemy, 215, 143),
            FormationMember(SHYSTEREnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SHYSTEREnemy, 151, 111),
            FormationMember(SHYSTEREnemy, 215, 143),
            FormationMember(SHYSTEREnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK012_RATFUNKS_WITH_SHADOW_OR_HOBGOBLIN] = FormationPack(
    Formation(
        members=[
            FormationMember(RATFUNKEnemy, 199, 143),
            FormationMember(RATFUNKEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(RATFUNKEnemy, 135, 119),
            FormationMember(RATFUNKEnemy, 199, 151),
            FormationMember(SHADOWEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(RATFUNKEnemy, 135, 119),
            FormationMember(RATFUNKEnemy, 199, 151),
            FormationMember(HOBGOBLINEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(RATFUNKEnemy, 135, 119),
            FormationMember(RATFUNKEnemy, 199, 151),
            FormationMember(HOBGOBLINEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(RATFUNKEnemy, 135, 119),
            FormationMember(RATFUNKEnemy, 199, 151),
            FormationMember(SHADOWEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK014_BIGBOO_ALWAYS_WITH_ONE_OTHER_MONSTER_1] = FormationPack(
    Formation(
        members=[
            FormationMember(THEBIGBOOEnemy, 151, 119),
            FormationMember(SHADOWEnemy, 199, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(THEBIGBOOEnemy, 151, 119),
            FormationMember(SHADOWEnemy, 199, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(THEBIGBOOEnemy, 119, 119),
            FormationMember(SHADOWEnemy, 167, 135),
            FormationMember(HOBGOBLINEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(THEBIGBOOEnemy, 119, 119),
            FormationMember(SHADOWEnemy, 167, 135),
            FormationMember(HOBGOBLINEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(THEBIGBOOEnemy, 151, 119),
            FormationMember(SHADOWEnemy, 199, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK016_MULTIPLE_GOBYS_BIASED_2] = FormationPack(
    Formation(
        members=[
            FormationMember(GOBYEnemy, 135, 119),
            FormationMember(GOBYEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GOBYEnemy, 135, 119),
            FormationMember(GOBYEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GOBYEnemy, 151, 119),
            FormationMember(GOBYEnemy, 215, 119),
            FormationMember(GOBYEnemy, 183, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK017_MULTIPLE_GOBYS_BIASED_3] = FormationPack(
    Formation(
        members=[
            FormationMember(GOBYEnemy, 151, 119),
            FormationMember(GOBYEnemy, 215, 119),
            FormationMember(GOBYEnemy, 183, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GOBYEnemy, 151, 119),
            FormationMember(GOBYEnemy, 215, 119),
            FormationMember(GOBYEnemy, 183, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GOBYEnemy, 135, 119),
            FormationMember(GOBYEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK018_CROOKS_WITH_SHYGUY_OR_SNAPDRAGON] = FormationPack(
    Formation(
        members=[
            FormationMember(CROOKEnemy, 167, 111),
            FormationMember(CROOKEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CROOKEnemy, 199, 143),
            FormationMember(CROOKEnemy, 151, 119),
            FormationMember(SHYGUYEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CROOKEnemy, 183, 127),
            FormationMember(SNAPDRAGONEnemy, 151, 111),
            FormationMember(SNAPDRAGONEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK019_CROOKS_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(CROOKEnemy, 199, 159),
            None,
            None,
            FormationMember(STARSLAPEnemy, 215, 127),
            FormationMember(ARACHNEEnemy, 167, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CROOKEnemy, 183, 127),
            FormationMember(SNAPDRAGONEnemy, 151, 111),
            FormationMember(SNAPDRAGONEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CROOKEnemy, 199, 143),
            FormationMember(CROOKEnemy, 151, 119),
            FormationMember(SHYGUYEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK020_SHYGUYS_WITH_STARSLAP_OR_SNAPDRAGON] = FormationPack(
    Formation(
        members=[
            FormationMember(SHYGUYEnemy, 151, 111),
            None,
            FormationMember(STARSLAPEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SHYGUYEnemy, 151, 111),
            None,
            FormationMember(STARSLAPEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SHYGUYEnemy, 135, 103),
            FormationMember(SHYGUYEnemy, 215, 143),
            None,
            FormationMember(SNAPDRAGONEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK021_SHYGUY_STARSLAP_SNAPDRAGON_CROOK_ARACHNE] = FormationPack(
    Formation(
        members=[
            FormationMember(SHYGUYEnemy, 231, 135),
            None,
            FormationMember(CROOKEnemy, 199, 143),
            FormationMember(ARACHNEEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SHYGUYEnemy, 135, 103),
            FormationMember(SHYGUYEnemy, 215, 143),
            None,
            FormationMember(SNAPDRAGONEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SHYGUYEnemy, 151, 111),
            None,
            FormationMember(STARSLAPEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK022_STARSLAP_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(STARSLAPEnemy, 199, 159),
            FormationMember(SHYGUYEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(STARSLAPEnemy, 215, 151),
            FormationMember(ARACHNEEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(STARSLAPEnemy, 167, 135),
            FormationMember(SNAPDRAGONEnemy, 151, 111),
            FormationMember(SNAPDRAGONEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(STARSLAPEnemy, 167, 135),
            FormationMember(SNAPDRAGONEnemy, 151, 111),
            FormationMember(SNAPDRAGONEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(STARSLAPEnemy, 215, 151),
            FormationMember(ARACHNEEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK024_WIGGLERS_WITH_AMANITA] = FormationPack(
    Formation(
        members=[
            FormationMember(WIGGLEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(WIGGLEREnemy, 151, 111),
            FormationMember(AMANITAEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(WIGGLEREnemy, 151, 111),
            FormationMember(WIGGLEREnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK025_WIGGLERS_WITH_GUERRILLA_OR_AMANITA] = FormationPack(
    Formation(
        members=[
            FormationMember(WIGGLEREnemy, 151, 119),
            None,
            FormationMember(GUERRILLAEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(WIGGLEREnemy, 151, 111),
            FormationMember(WIGGLEREnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(WIGGLEREnemy, 151, 111),
            FormationMember(AMANITAEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK026_AMANITAS_WITH_BUZZER_OR_OCTOLOT] = FormationPack(
    Formation(
        members=[
            FormationMember(AMANITAEnemy, 135, 127),
            FormationMember(AMANITAEnemy, 199, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(AMANITAEnemy, 199, 151),
            FormationMember(AMANITAEnemy, 135, 119),
            FormationMember(BUZZEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(AMANITAEnemy, 199, 151),
            FormationMember(AMANITAEnemy, 135, 119),
            FormationMember(OCTOLOTEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(AMANITAEnemy, 199, 151),
            FormationMember(AMANITAEnemy, 135, 119),
            FormationMember(OCTOLOTEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(AMANITAEnemy, 199, 151),
            FormationMember(AMANITAEnemy, 135, 119),
            FormationMember(BUZZEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK028_BUZZERS_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(BUZZEREnemy, 135, 119),
            FormationMember(OCTOLOTEnemy, 199, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BUZZEREnemy, 167, 103),
            FormationMember(BUZZEREnemy, 231, 135),
            FormationMember(AMANITAEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BUZZEREnemy, 199, 151),
            None,
            FormationMember(GUERRILLAEnemy, 151, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK029_BUZZERS_WITH_AMANITA] = FormationPack(
    Formation(
        members=[
            FormationMember(BUZZEREnemy, 199, 159),
            None,
            FormationMember(GUERRILLAEnemy, 135, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BUZZEREnemy, 199, 151),
            None,
            FormationMember(GUERRILLAEnemy, 151, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BUZZEREnemy, 167, 103),
            FormationMember(BUZZEREnemy, 231, 135),
            FormationMember(AMANITAEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK030_SPARKY_WITH_SHYRANGER] = FormationPack(
    Formation(
        members=[
            FormationMember(SPARKYEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPARKYEnemy, 167, 111),
            FormationMember(SPARKYEnemy, 215, 135),
            FormationMember(SHYRANGEREnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPARKYEnemy, 167, 135),
            FormationMember(SPARKYEnemy, 151, 111),
            FormationMember(SPARKYEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK031_MULTIPLE_SPARKY_WITH_SHYRANGER] = FormationPack(
    Formation(
        members=[
            FormationMember(SPARKYEnemy, 167, 135),
            FormationMember(SPARKYEnemy, 151, 111),
            FormationMember(SPARKYEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPARKYEnemy, 167, 135),
            FormationMember(SPARKYEnemy, 151, 111),
            FormationMember(SPARKYEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPARKYEnemy, 167, 111),
            FormationMember(SPARKYEnemy, 215, 135),
            FormationMember(SHYRANGEREnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK032_APPRENTICE_HENCHMAN_FIGHT] = FormationPack(
    # henchman
    Formation(
        members=[
            FormationMember(APPRENTICEEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK033_UNUSED] = FormationPack(
    # put belome 3 here
    Formation(
        members=[
            FormationMember(GOOMBAEnemy, 167, 135),
            None,
            FormationMember(PIRANHAPLANTEnemy, 231, 151),
            FormationMember(PIRANHAPLANTEnemy, 135, 103),
            FormationMember(SPARKYEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GOOMBAEnemy, 135, 119),
            FormationMember(GOOMBAEnemy, 199, 151),
            FormationMember(PIRANHAPLANTEnemy, 199, 119),
            FormationMember(PIRANHAPLANTEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GOOMBAEnemy, 199, 151),
            FormationMember(GOOMBAEnemy, 135, 119),
            FormationMember(SHYRANGEREnemy, 183, 111),
            FormationMember(SHYRANGEREnemy, 215, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK034_PIRANHA_WITH_SHYRANGER] = FormationPack(
    Formation(
        members=[
            FormationMember(PIRANHAPLANTEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(PIRANHAPLANTEnemy, 215, 143),
            FormationMember(PIRANHAPLANTEnemy, 151, 111),
            FormationMember(SHYRANGEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(PIRANHAPLANTEnemy, 167, 111),
            FormationMember(PIRANHAPLANTEnemy, 167, 135),
            FormationMember(PIRANHAPLANTEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK035_MULTIPLE_PIRANHA_WITH_SHYRANGER] = FormationPack(
    Formation(
        members=[
            FormationMember(PIRANHAPLANTEnemy, 151, 143),
            FormationMember(PIRANHAPLANTEnemy, 151, 111),
            FormationMember(PIRANHAPLANTEnemy, 199, 119),
            FormationMember(PIRANHAPLANTEnemy, 231, 143),
            FormationMember(PIRANHAPLANTEnemy, 199, 159),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(PIRANHAPLANTEnemy, 167, 111),
            FormationMember(PIRANHAPLANTEnemy, 167, 135),
            FormationMember(PIRANHAPLANTEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(PIRANHAPLANTEnemy, 215, 143),
            FormationMember(PIRANHAPLANTEnemy, 151, 111),
            FormationMember(SHYRANGEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK036_BOBOMB_WITH_CLUSTER] = FormationPack(
    Formation(
        members=[
            FormationMember(BOBOMBEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BOBOMBEnemy, 135, 119),
            FormationMember(BOBOMBEnemy, 199, 151),
            FormationMember(CLUSTEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BOBOMBEnemy, 151, 127),
            FormationMember(BOBOMBEnemy, 167, 103),
            FormationMember(BOBOMBEnemy, 199, 151),
            FormationMember(BOBOMBEnemy, 215, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK037_BOBOMB_WITH_CLUSTER_SOMETIMES_ENIGMA] = FormationPack(
    Formation(
        members=[
            FormationMember(BOBOMBEnemy, 135, 119),
            FormationMember(BOBOMBEnemy, 199, 151),
            FormationMember(ENIGMAEnemy, 183, 111),
            FormationMember(CLUSTEREnemy, 215, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BOBOMBEnemy, 151, 127),
            FormationMember(BOBOMBEnemy, 167, 103),
            FormationMember(BOBOMBEnemy, 199, 151),
            FormationMember(BOBOMBEnemy, 215, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BOBOMBEnemy, 135, 119),
            FormationMember(BOBOMBEnemy, 199, 151),
            FormationMember(CLUSTEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK038_SPARKY_WITH_ALWAYS_OTHER_ENEMIES_1] = FormationPack(
    Formation(
        members=[
            FormationMember(SPARKYEnemy, 199, 151),
            FormationMember(ENIGMAEnemy, 167, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPARKYEnemy, 167, 111),
            FormationMember(SPARKYEnemy, 215, 135),
            FormationMember(BOBOMBEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPARKYEnemy, 183, 127),
            FormationMember(CLUSTEREnemy, 231, 143),
            FormationMember(CLUSTEREnemy, 151, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPARKYEnemy, 183, 127),
            FormationMember(CLUSTEREnemy, 231, 143),
            FormationMember(CLUSTEREnemy, 151, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPARKYEnemy, 167, 111),
            FormationMember(SPARKYEnemy, 215, 135),
            FormationMember(BOBOMBEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK040_MAGMITES_WITH_SPARKY_BOBOMB_OR_CLUSTER] = FormationPack(
    Formation(
        members=[
            FormationMember(MAGMITEEnemy, 167, 111),
            FormationMember(MAGMITEEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(MAGMITEEnemy, 151, 111),
            FormationMember(BOBOMBEnemy, 183, 127),
            FormationMember(SPARKYEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(MAGMITEEnemy, 151, 127),
            FormationMember(MAGMITEEnemy, 183, 143),
            FormationMember(CLUSTEREnemy, 167, 103),
            FormationMember(CLUSTEREnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK041_MAGMITES_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(MAGMITEEnemy, 135, 103),
            FormationMember(MAGMITEEnemy, 231, 151),
            FormationMember(BOBOMBEnemy, 167, 135),
            None,
            FormationMember(CLUSTEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(MAGMITEEnemy, 151, 127),
            FormationMember(MAGMITEEnemy, 183, 143),
            FormationMember(CLUSTEREnemy, 167, 103),
            FormationMember(CLUSTEREnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(MAGMITEEnemy, 151, 111),
            FormationMember(BOBOMBEnemy, 183, 127),
            FormationMember(SPARKYEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK042_LAKITU_WITH_SPIKESTER_ARTICHOKER] = FormationPack(
    Formation(
        members=[
            FormationMember(LAKITUEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(LAKITUEnemy, 135, 119),
            FormationMember(SPIKESTEREnemy, 199, 159),
            FormationMember(ARTICHOKEREnemy, 183, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(LAKITUEnemy, 151, 111),
            FormationMember(LAKITUEnemy, 183, 127),
            FormationMember(LAKITUEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(LAKITUEnemy, 151, 111),
            FormationMember(LAKITUEnemy, 183, 127),
            FormationMember(LAKITUEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(LAKITUEnemy, 135, 119),
            FormationMember(SPIKESTEREnemy, 199, 159),
            FormationMember(ARTICHOKEREnemy, 183, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK044_SPIKESTER_WITH_OTHER_ENEMIES] = FormationPack(
    Formation(
        members=[
            FormationMember(SPIKESTEREnemy, 215, 143),
            FormationMember(CARROBOSCISEnemy, 135, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPIKESTEREnemy, 199, 151),
            FormationMember(SPIKESTEREnemy, 135, 119),
            FormationMember(ARTICHOKEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPIKESTEREnemy, 183, 127),
            FormationMember(CARROBOSCISEnemy, 135, 119),
            FormationMember(CARROBOSCISEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPIKESTEREnemy, 183, 127),
            FormationMember(CARROBOSCISEnemy, 135, 119),
            FormationMember(CARROBOSCISEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPIKESTEREnemy, 199, 151),
            FormationMember(SPIKESTEREnemy, 135, 119),
            FormationMember(ARTICHOKEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK046_SPOOKUM_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(SPOOKUMEnemy, 199, 135),
            FormationMember(ORBUSEREnemy, 135, 119),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPOOKUMEnemy, 135, 119),
            FormationMember(SPOOKUMEnemy, 199, 151),
            FormationMember(JESTEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPOOKUMEnemy, 151, 111),
            FormationMember(REMOCONEnemy, 167, 151),
            FormationMember(ORBUSEREnemy, 215, 127),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPOOKUMEnemy, 151, 111),
            FormationMember(REMOCONEnemy, 167, 151),
            FormationMember(ORBUSEREnemy, 215, 127),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPOOKUMEnemy, 135, 119),
            FormationMember(SPOOKUMEnemy, 199, 151),
            FormationMember(JESTEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK048_ROBOMB_WITH_REMOCON] = FormationPack(
    Formation(
        members=[
            FormationMember(ROBOMBEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(ROBOMBEnemy, 183, 127),
            FormationMember(ROBOMBEnemy, 199, 119),
            FormationMember(ROBOMBEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(ROBOMBEnemy, 215, 143),
            FormationMember(ROBOMBEnemy, 151, 111),
            FormationMember(REMOCONEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(ROBOMBEnemy, 215, 143),
            FormationMember(ROBOMBEnemy, 151, 111),
            FormationMember(REMOCONEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(ROBOMBEnemy, 183, 127),
            FormationMember(ROBOMBEnemy, 199, 119),
            FormationMember(ROBOMBEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK050_CHOMP_WITH_OTHER_MONSTERS_1] = FormationPack(
    Formation(
        members=[
            FormationMember(CHOMPEnemy, 215, 143),
            FormationMember(JESTEREnemy, 167, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CHOMPEnemy, 215, 143),
            FormationMember(ROBOMBEnemy, 151, 135),
            FormationMember(REMOCONEnemy, 167, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CHOMPEnemy, 151, 111),
            FormationMember(CHOMPEnemy, 215, 143),
            FormationMember(ORBUSEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CHOMPEnemy, 151, 111),
            FormationMember(CHOMPEnemy, 215, 143),
            FormationMember(ORBUSEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CHOMPEnemy, 215, 143),
            FormationMember(ROBOMBEnemy, 151, 135),
            FormationMember(REMOCONEnemy, 167, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK052_BLASTERS_AND_SPOOKUMS_1] = FormationPack(
    Formation(
        members=[
            FormationMember(BLASTEREnemy, 167, 135),
            FormationMember(SPOOKUMEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BLASTEREnemy, 167, 135),
            FormationMember(SPOOKUMEnemy, 151, 111),
            FormationMember(REMOCONEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BLASTEREnemy, 199, 151),
            FormationMember(BLASTEREnemy, 135, 119),
            FormationMember(SPOOKUMEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BLASTEREnemy, 199, 151),
            FormationMember(BLASTEREnemy, 135, 119),
            FormationMember(SPOOKUMEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BLASTEREnemy, 167, 135),
            FormationMember(SPOOKUMEnemy, 151, 111),
            FormationMember(REMOCONEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK054_TORTES] = FormationPack(
    Formation(
        members=[
            FormationMember(TORTEEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(TORTEEnemy, 215, 143),
            FormationMember(TORTEEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(TORTEEnemy, 183, 103),
            FormationMember(TORTEEnemy, 151, 135),
            FormationMember(TORTEEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK055_MULTIPLE_TORTES] = FormationPack(
    Formation(
        members=[
            FormationMember(TORTEEnemy, 167, 135),
            FormationMember(TORTEEnemy, 199, 119),
            FormationMember(TORTEEnemy, 151, 111),
            FormationMember(TORTEEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(TORTEEnemy, 183, 103),
            FormationMember(TORTEEnemy, 151, 135),
            FormationMember(TORTEEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(TORTEEnemy, 215, 143),
            FormationMember(TORTEEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK056_MUKU_PULSAR_GECKO] = FormationPack(
    Formation(
        members=[
            FormationMember(MUKUMUKUEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(MUKUMUKUEnemy, 151, 119),
            FormationMember(MUKUMUKUEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(MUKUMUKUEnemy, 151, 111),
            FormationMember(MUKUMUKUEnemy, 215, 143),
            FormationMember(PULSAREnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK057_MUKU_PULSAR_GECKO_MULTI] = FormationPack(
    Formation(
        members=[
            FormationMember(MUKUMUKUEnemy, 183, 143),
            FormationMember(PULSAREnemy, 151, 111),
            FormationMember(GECKOEnemy, 231, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(MUKUMUKUEnemy, 151, 111),
            FormationMember(MUKUMUKUEnemy, 215, 143),
            FormationMember(PULSAREnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(MUKUMUKUEnemy, 151, 119),
            FormationMember(MUKUMUKUEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK058_SACKIT_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(SACKITEnemy, 199, 151),
            FormationMember(SACKITEnemy, 167, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SACKITEnemy, 151, 127),
            FormationMember(SACKITEnemy, 183, 143),
            FormationMember(MUKUMUKUEnemy, 167, 103),
            FormationMember(GECKOEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
)
packs[PACK059_SACKIT_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(SACKITEnemy, 215, 143),
            FormationMember(MASTADOOMEnemy, 167, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SACKITEnemy, 151, 127),
            FormationMember(SACKITEnemy, 183, 143),
            FormationMember(MUKUMUKUEnemy, 167, 103),
            FormationMember(GECKOEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK060_GECKO_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(GECKOEnemy, 151, 119),
            FormationMember(SACKITEnemy, 199, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GECKOEnemy, 151, 119),
            FormationMember(MASTADOOMEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
)
packs[PACK061_GECKO_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(GECKOEnemy, 135, 103),
            FormationMember(GECKOEnemy, 231, 151),
            FormationMember(MASTADOOMEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GECKOEnemy, 151, 119),
            FormationMember(MASTADOOMEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK062_ZEOSTAR_WITH_BLOOBER_OR_LEUKO] = FormationPack(
    Formation(
        members=[
            FormationMember(ZEOSTAREnemy, 135, 119),
            FormationMember(ZEOSTAREnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(ZEOSTAREnemy, 151, 135),
            FormationMember(ZEOSTAREnemy, 183, 103),
            FormationMember(BLOOBEREnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(ZEOSTAREnemy, 199, 119),
            FormationMember(ZEOSTAREnemy, 167, 135),
            FormationMember(LEUKOEnemy, 167, 103),
            FormationMember(LEUKOEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK063_ZEOSTAR_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(ZEOSTAREnemy, 183, 127),
            FormationMember(LEUKOEnemy, 215, 143),
            FormationMember(CRUSTYEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(ZEOSTAREnemy, 199, 119),
            FormationMember(ZEOSTAREnemy, 167, 135),
            FormationMember(LEUKOEnemy, 167, 103),
            FormationMember(LEUKOEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(ZEOSTAREnemy, 151, 135),
            FormationMember(ZEOSTAREnemy, 183, 103),
            FormationMember(BLOOBEREnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK064_BLOOBER_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(BLOOBEREnemy, 151, 111),
            FormationMember(MRKIPPEREnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BLOOBEREnemy, 183, 127),
            FormationMember(BLOOBEREnemy, 231, 143),
            FormationMember(BLOOBEREnemy, 135, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BLOOBEREnemy, 151, 111),
            FormationMember(BLOOBEREnemy, 231, 151),
            FormationMember(MRKIPPEREnemy, 151, 143),
            FormationMember(CRUSTYEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK065_BLOOBER_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(BLOOBEREnemy, 231, 135),
            FormationMember(BLOOBEREnemy, 167, 103),
            FormationMember(ZEOSTAREnemy, 135, 127),
            FormationMember(ZEOSTAREnemy, 183, 151),
            FormationMember(LEUKOEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BLOOBEREnemy, 151, 111),
            FormationMember(BLOOBEREnemy, 231, 151),
            FormationMember(MRKIPPEREnemy, 151, 143),
            FormationMember(CRUSTYEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BLOOBEREnemy, 183, 127),
            FormationMember(BLOOBEREnemy, 231, 143),
            FormationMember(BLOOBEREnemy, 135, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK066_KIPPER_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(MRKIPPEREnemy, 151, 103),
            FormationMember(MRKIPPEREnemy, 215, 151),
            FormationMember(MRKIPPEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(MRKIPPEREnemy, 199, 151),
            FormationMember(MRKIPPEREnemy, 135, 119),
            FormationMember(CRUSTYEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(MRKIPPEREnemy, 135, 119),
            FormationMember(MRKIPPEREnemy, 231, 135),
            FormationMember(CRUSTYEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(MRKIPPEREnemy, 135, 119),
            FormationMember(MRKIPPEREnemy, 231, 135),
            FormationMember(CRUSTYEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(MRKIPPEREnemy, 199, 151),
            FormationMember(MRKIPPEREnemy, 135, 119),
            FormationMember(CRUSTYEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK068_BANDANA_REDS_1] = FormationPack(
    Formation(
        members=[
            FormationMember(BANDANAREDEnemy, 151, 127),
            FormationMember(BANDANAREDEnemy, 183, 143),
            FormationMember(BANDANAREDEnemy, 167, 103),
            FormationMember(BANDANAREDEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK069_BANDANA_REDS_2] = FormationPack(
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
    )
)
packs[PACK070_BANDANA_BLUES] = FormationPack(
    Formation(
        members=[
            FormationMember(BANDANABLUEEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BANDANABLUEEnemy, 135, 127),
            FormationMember(BANDANABLUEEnemy, 167, 111),
            FormationMember(BANDANABLUEEnemy, 183, 151),
            FormationMember(BANDANABLUEEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BANDANABLUEEnemy, 135, 127),
            FormationMember(BANDANABLUEEnemy, 167, 111),
            FormationMember(BANDANABLUEEnemy, 183, 151),
            FormationMember(BANDANABLUEEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK071_BANDANA_RED_HENCHMEN] = FormationPack(
    # henchman
    Formation(
        members=[
            FormationMember(BANDANAREDEnemy, x_pos=151, y_pos=127),
            FormationMember(BANDANAREDEnemy, x_pos=183, y_pos=143),
            FormationMember(BANDANAREDEnemy, x_pos=167, y_pos=103),
            FormationMember(BANDANAREDEnemy, x_pos=231, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BANDANAREDEnemy, x_pos=199, y_pos=151),
            FormationMember(BANDANAREDEnemy, x_pos=135, y_pos=119),
            FormationMember(BANDANAREDEnemy, x_pos=215, y_pos=127),
            FormationMember(BANDANAREDEnemy, x_pos=167, y_pos=135),
            FormationMember(BANDANAREDEnemy, x_pos=183, y_pos=111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BANDANAREDEnemy, x_pos=151, y_pos=127),
            FormationMember(BANDANAREDEnemy, x_pos=183, y_pos=143),
            FormationMember(BANDANAREDEnemy, x_pos=167, y_pos=103),
            FormationMember(BANDANAREDEnemy, x_pos=231, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK072_DRYBONES_WITH_GREAPER_REACHER] = FormationPack(
    Formation(
        members=[
            FormationMember(DRYBONESEnemy, 199, 151),
            FormationMember(DRYBONESEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(DRYBONESEnemy, 135, 119),
            FormationMember(DRYBONESEnemy, 199, 151),
            FormationMember(GREAPEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(DRYBONESEnemy, 135, 119),
            FormationMember(GREAPEREnemy, 199, 151),
            FormationMember(REACHEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(DRYBONESEnemy, 135, 119),
            FormationMember(GREAPEREnemy, 199, 151),
            FormationMember(REACHEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(DRYBONESEnemy, 135, 119),
            FormationMember(DRYBONESEnemy, 199, 151),
            FormationMember(GREAPEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK074_ALLEYRAT_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(ALLEYRATEnemy, 199, 151),
            FormationMember(GORGONEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(ALLEYRATEnemy, 135, 119),
            FormationMember(ALLEYRATEnemy, 199, 151),
            FormationMember(GREAPEREnemy, 215, 127),
            FormationMember(GREAPEREnemy, 183, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(ALLEYRATEnemy, 151, 127),
            FormationMember(ALLEYRATEnemy, 199, 151),
            FormationMember(GORGONEnemy, 183, 111),
            FormationMember(GORGONEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK075_ALLEYRAT_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(ALLEYRATEnemy, 231, 135),
            FormationMember(REACHEREnemy, 167, 135),
            FormationMember(GORGONEnemy, 167, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(ALLEYRATEnemy, 151, 127),
            FormationMember(ALLEYRATEnemy, 199, 151),
            FormationMember(GORGONEnemy, 183, 111),
            FormationMember(GORGONEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(ALLEYRATEnemy, 135, 119),
            FormationMember(ALLEYRATEnemy, 199, 151),
            FormationMember(GREAPEREnemy, 215, 127),
            FormationMember(GREAPEREnemy, 183, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK076_GREAPER_WITH_REACHER_STRAWHEAD] = FormationPack(
    Formation(
        members=[
            FormationMember(GREAPEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GREAPEREnemy, 151, 119),
            FormationMember(GREAPEREnemy, 199, 143),
            FormationMember(REACHEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GREAPEREnemy, 167, 135),
            FormationMember(STRAWHEADEnemy, 215, 135),
            FormationMember(REACHEREnemy, 167, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GREAPEREnemy, 167, 135),
            FormationMember(STRAWHEADEnemy, 215, 135),
            FormationMember(REACHEREnemy, 167, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GREAPEREnemy, 151, 119),
            FormationMember(GREAPEREnemy, 199, 143),
            FormationMember(REACHEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK078_DRILLBIT_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(DRILLBITEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(DRILLBITEnemy, 167, 135),
            FormationMember(DRILLBITEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(DRILLBITEnemy, 151, 119),
            FormationMember(DRILLBITEnemy, 183, 151),
            FormationMember(DRILLBITEnemy, 215, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK079_DRILLBIT_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(DRILLBITEnemy, 167, 119),
            FormationMember(DRILLBITEnemy, 199, 151),
            FormationMember(DRILLBITEnemy, 135, 119),
            FormationMember(DRILLBITEnemy, 199, 119),
            FormationMember(DRILLBITEnemy, 199, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(DRILLBITEnemy, 151, 119),
            FormationMember(DRILLBITEnemy, 183, 151),
            FormationMember(DRILLBITEnemy, 215, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(DRILLBITEnemy, 167, 135),
            FormationMember(DRILLBITEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK080_STINGER_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(STINGEREnemy, 151, 111),
            FormationMember(FINKFLOWEREnemy, 199, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(STINGEREnemy, 135, 111),
            FormationMember(STINGEREnemy, 215, 151),
            FormationMember(OCTOVADEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(STINGEREnemy, 199, 119),
            None,
            FormationMember(FINKFLOWEREnemy, 215, 143),
            FormationMember(FINKFLOWEREnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(STINGEREnemy, 199, 119),
            None,
            FormationMember(FINKFLOWEREnemy, 215, 143),
            FormationMember(FINKFLOWEREnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(STINGEREnemy, 135, 111),
            FormationMember(STINGEREnemy, 215, 151),
            FormationMember(OCTOVADEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK082_CHOW_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(CHOWEnemy, 135, 119),
            FormationMember(OCTOVADEREnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CHOWEnemy, 151, 111),
            FormationMember(SHOGUNEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CHOWEnemy, 199, 151),
            FormationMember(SHOGUNEnemy, 135, 119),
            FormationMember(OCTOVADEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CHOWEnemy, 199, 151),
            FormationMember(SHOGUNEnemy, 135, 119),
            FormationMember(OCTOVADEREnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CHOWEnemy, 151, 111),
            FormationMember(SHOGUNEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK084_CHOMPCHOMP_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(CHOMPCHOMPEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CHOMPCHOMPEnemy, 151, 111),
            FormationMember(CHOMPCHOMPEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CHOMPCHOMPEnemy, 151, 111),
            FormationMember(CHOMPCHOMPEnemy, 199, 119),
            FormationMember(CHOMPCHOMPEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CHOMPCHOMPEnemy, 151, 111),
            FormationMember(CHOMPCHOMPEnemy, 199, 119),
            FormationMember(CHOMPCHOMPEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CHOMPCHOMPEnemy, 151, 111),
            FormationMember(CHOMPCHOMPEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK086_SHYAWAY_WITH_KRIFFID_OR_RIBBITE] = FormationPack(
    Formation(
        members=[
            FormationMember(SHYAWAYEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SHYAWAYEnemy, 151, 111),
            FormationMember(SHYAWAYEnemy, 215, 143),
            FormationMember(KRIFFIDEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SHYAWAYEnemy, 167, 103),
            FormationMember(SHYAWAYEnemy, 231, 135),
            FormationMember(RIBBITEEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SHYAWAYEnemy, 167, 103),
            FormationMember(SHYAWAYEnemy, 231, 135),
            FormationMember(RIBBITEEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SHYAWAYEnemy, 151, 111),
            FormationMember(SHYAWAYEnemy, 215, 143),
            FormationMember(KRIFFIDEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK088_CHEWY_WITH_SHYAWAY_OR_SPINTHRA] = FormationPack(
    Formation(
        members=[
            FormationMember(CHEWYEnemy, 151, 111),
            FormationMember(CHEWYEnemy, 183, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CHEWYEnemy, 135, 119),
            FormationMember(CHEWYEnemy, 199, 151),
            FormationMember(SHYAWAYEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CHEWYEnemy, 151, 111),
            FormationMember(SPINTHRAEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CHEWYEnemy, 151, 111),
            FormationMember(SPINTHRAEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CHEWYEnemy, 135, 119),
            FormationMember(CHEWYEnemy, 199, 151),
            FormationMember(SHYAWAYEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK090_GECKIT_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(GECKITEnemy, 199, 151),
            FormationMember(SPINTHRAEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GECKITEnemy, 183, 135),
            FormationMember(GECKITEnemy, 215, 151),
            FormationMember(SPINTHRAEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GECKITEnemy, 183, 135),
            FormationMember(GECKITEnemy, 215, 151),
            FormationMember(SPINTHRAEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK092_BIRDY_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(BIRDYEnemy, 135, 119),
            FormationMember(HEAVYTROOPAEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BIRDYEnemy, 215, 119),
            FormationMember(BIRDYEnemy, 151, 119),
            FormationMember(BIRDYEnemy, 183, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BIRDYEnemy, 199, 151),
            FormationMember(BIRDYEnemy, 135, 119),
            FormationMember(HEAVYTROOPAEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK093_BIRDY_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(BIRDYEnemy, 151, 111),
            FormationMember(BIRDYEnemy, 215, 143),
            FormationMember(BIRDYEnemy, 151, 143),
            FormationMember(BIRDYEnemy, 215, 111),
            FormationMember(BIRDYEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BIRDYEnemy, 199, 151),
            FormationMember(BIRDYEnemy, 135, 119),
            FormationMember(HEAVYTROOPAEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BIRDYEnemy, 215, 119),
            FormationMember(BIRDYEnemy, 151, 119),
            FormationMember(BIRDYEnemy, 183, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK094_BLUEBIRD_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(BLUEBIRDEnemy, 199, 151),
            FormationMember(BLUEBIRDEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BLUEBIRDEnemy, 167, 103),
            FormationMember(BLUEBIRDEnemy, 231, 135),
            FormationMember(HEAVYTROOPAEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BLUEBIRDEnemy, 183, 143),
            FormationMember(BLUEBIRDEnemy, 183, 111),
            FormationMember(BLUEBIRDEnemy, 231, 135),
            FormationMember(BLUEBIRDEnemy, 135, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK095_BLUEBIRD_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(BLUEBIRDEnemy, 151, 111),
            FormationMember(BLUEBIRDEnemy, 215, 143),
            None,
            None,
            FormationMember(HEAVYTROOPAEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BLUEBIRDEnemy, 183, 143),
            FormationMember(BLUEBIRDEnemy, 183, 111),
            FormationMember(BLUEBIRDEnemy, 231, 135),
            FormationMember(BLUEBIRDEnemy, 135, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BLUEBIRDEnemy, 167, 103),
            FormationMember(BLUEBIRDEnemy, 231, 135),
            FormationMember(HEAVYTROOPAEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK096_PINWHEEL_WITH_MUCKLE] = FormationPack(
    Formation(
        members=[
            FormationMember(PINWHEELEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(PINWHEELEnemy, 135, 119),
            FormationMember(MUCKLEEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(PINWHEELEnemy, 151, 127),
            FormationMember(PINWHEELEnemy, 183, 143),
            FormationMember(MUCKLEEnemy, 151, 103),
            FormationMember(MUCKLEEnemy, 231, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(PINWHEELEnemy, 151, 127),
            FormationMember(PINWHEELEnemy, 183, 143),
            FormationMember(MUCKLEEnemy, 151, 103),
            FormationMember(MUCKLEEnemy, 231, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(PINWHEELEnemy, 135, 119),
            FormationMember(MUCKLEEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK098_SHAMAN_WITH_ORBISON_JAWFUL] = FormationPack(
    Formation(
        members=[
            FormationMember(SHAMANEnemy, 151, 111),
            FormationMember(SHAMANEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SHAMANEnemy, 135, 119),
            FormationMember(ORBISONEnemy, 199, 151),
            FormationMember(JAWFULEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SHAMANEnemy, 167, 103),
            FormationMember(SHAMANEnemy, 231, 135),
            FormationMember(JAWFULEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SHAMANEnemy, 167, 103),
            FormationMember(SHAMANEnemy, 231, 135),
            FormationMember(JAWFULEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SHAMANEnemy, 135, 119),
            FormationMember(ORBISONEnemy, 199, 151),
            FormationMember(JAWFULEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK100_SLINGSHY_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(SLINGSHYEnemy, 135, 119),
            FormationMember(ORBISONEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SLINGSHYEnemy, 183, 127),
            FormationMember(ORBISONEnemy, 151, 111),
            FormationMember(ORBISONEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SLINGSHYEnemy, 167, 135),
            FormationMember(ORBISONEnemy, 151, 111),
            FormationMember(ORBISONEnemy, 215, 143),
            FormationMember(JAWFULEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SLINGSHYEnemy, 167, 135),
            FormationMember(ORBISONEnemy, 151, 111),
            FormationMember(ORBISONEnemy, 215, 143),
            FormationMember(JAWFULEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SLINGSHYEnemy, 183, 127),
            FormationMember(ORBISONEnemy, 151, 111),
            FormationMember(ORBISONEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK102_MAGMUS_WITH_ARMOREDANT_OERLIKON] = FormationPack(
    Formation(
        members=[
            FormationMember(MAGMUSEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(MAGMUSEnemy, 151, 111),
            FormationMember(MAGMUSEnemy, 215, 143),
            FormationMember(ARMOREDANTEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(MAGMUSEnemy, 151, 111),
            FormationMember(MAGMUSEnemy, 215, 143),
            FormationMember(ARMOREDANTEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK104_OERLIKON_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(OERLIKONEnemy, 135, 119),
            FormationMember(VOMEREnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(OERLIKONEnemy, 183, 127),
            FormationMember(OERLIKONEnemy, 135, 119),
            FormationMember(OERLIKONEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(OERLIKONEnemy, 215, 151),
            FormationMember(CHAINEDKONGEnemy, 183, 127),
            FormationMember(ARMOREDANTEnemy, 135, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK105_OERLIKON_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(OERLIKONEnemy, 135, 127),
            FormationMember(OERLIKONEnemy, 183, 151),
            FormationMember(CHAINEDKONGEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(OERLIKONEnemy, 215, 151),
            FormationMember(CHAINEDKONGEnemy, 183, 127),
            FormationMember(ARMOREDANTEnemy, 135, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(OERLIKONEnemy, 183, 127),
            FormationMember(OERLIKONEnemy, 135, 119),
            FormationMember(OERLIKONEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK106_PYROSPHERE_WITH_CHAINEDKONG_CORKPEDITE] = FormationPack(
    Formation(
        members=[
            FormationMember(PYROSPHEREEnemy, 151, 135),
            FormationMember(PYROSPHEREEnemy, 215, 135),
            FormationMember(PYROSPHEREEnemy, 183, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(PYROSPHEREEnemy, 199, 143),
            FormationMember(PYROSPHEREEnemy, 151, 119),
            FormationMember(CHAINEDKONGEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CORKPEDITEEnemy, 135, 119),
            FormationMember(BODYEnemy, 151, 111),
            FormationMember(PYROSPHEREEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK107_PYROSPHERE_ALWAYS_WITH_OTHER_MONSTERS] = FormationPack(
    Formation(
        members=[
            FormationMember(PYROSPHEREEnemy, 199, 151),
            FormationMember(PYROSPHEREEnemy, 199, 119),
            FormationMember(STUMPETEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CORKPEDITEEnemy, 135, 119),
            FormationMember(BODYEnemy, 151, 111),
            FormationMember(PYROSPHEREEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(PYROSPHEREEnemy, 199, 143),
            FormationMember(PYROSPHEREEnemy, 151, 119),
            FormationMember(CHAINEDKONGEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK108_VOMER_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(VOMEREnemy, 151, 111),
            FormationMember(CHAINEDKONGEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(VOMEREnemy, 151, 103),
            FormationMember(VOMEREnemy, 183, 127),
            FormationMember(VOMEREnemy, 215, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CORKPEDITEEnemy, 199, 151),
            FormationMember(BODYEnemy, 215, 143),
            FormationMember(VOMEREnemy, 135, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK109_VOMER_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(VOMEREnemy, 151, 135),
            FormationMember(VOMEREnemy, 151, 103),
            FormationMember(STUMPETEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CORKPEDITEEnemy, 199, 151),
            FormationMember(BODYEnemy, 215, 143),
            FormationMember(VOMEREnemy, 135, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(VOMEREnemy, 151, 103),
            FormationMember(VOMEREnemy, 183, 127),
            FormationMember(VOMEREnemy, 215, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK110_TERRACOTTA_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(TERRACOTTAEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(TERRACOTTAEnemy, 183, 151),
            FormationMember(TERRACOTTAEnemy, 151, 119),
            FormationMember(TERRACOTTAEnemy, 215, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(TERRACOTTAEnemy, 183, 127),
            FormationMember(FORKIESEnemy, 151, 111),
            FormationMember(FORKIESEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(TERRACOTTAEnemy, 183, 127),
            FormationMember(FORKIESEnemy, 151, 111),
            FormationMember(FORKIESEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(TERRACOTTAEnemy, 183, 151),
            FormationMember(TERRACOTTAEnemy, 151, 119),
            FormationMember(TERRACOTTAEnemy, 215, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK112_MALAKOOPA_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(MALAKOOPAEnemy, 135, 127),
            FormationMember(TUBOTROOPAEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(MALAKOOPAEnemy, 135, 119),
            FormationMember(MALAKOOPAEnemy, 199, 151),
            FormationMember(TUBOTROOPAEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(MALAKOOPAEnemy, 135, 103),
            FormationMember(MALAKOOPAEnemy, 231, 151),
            FormationMember(TERRACOTTAEnemy, 167, 135),
            FormationMember(TUBOTROOPAEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(MALAKOOPAEnemy, 135, 103),
            FormationMember(MALAKOOPAEnemy, 231, 151),
            FormationMember(TERRACOTTAEnemy, 167, 135),
            FormationMember(TUBOTROOPAEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(MALAKOOPAEnemy, 135, 119),
            FormationMember(MALAKOOPAEnemy, 199, 151),
            FormationMember(TUBOTROOPAEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK114_GUGOOMBA_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(GUGOOMBAEnemy, 151, 111),
            FormationMember(GUGOOMBAEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GUGOOMBAEnemy, 231, 151),
            FormationMember(GUGOOMBAEnemy, 135, 103),
            FormationMember(STARCRUSTEREnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GUGOOMBAEnemy, 231, 143),
            FormationMember(FORKIESEnemy, 199, 119),
            FormationMember(STARCRUSTEREnemy, 151, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GUGOOMBAEnemy, 231, 143),
            FormationMember(FORKIESEnemy, 199, 119),
            FormationMember(STARCRUSTEREnemy, 151, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GUGOOMBAEnemy, 231, 151),
            FormationMember(GUGOOMBAEnemy, 135, 103),
            FormationMember(STARCRUSTEREnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK116_BIGBERTHA_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(BIGBERTHAEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BIGBERTHAEnemy, 151, 111),
            FormationMember(BIGBERTHAEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BIGBERTHAEnemy, 215, 143),
            FormationMember(FORKIESEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK117_BIGBERTHA_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(BIGBERTHAEnemy, 135, 111),
            FormationMember(BIGBERTHAEnemy, 215, 151),
            FormationMember(TERRACOTTAEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BIGBERTHAEnemy, 215, 143),
            FormationMember(FORKIESEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(BIGBERTHAEnemy, 151, 111),
            FormationMember(BIGBERTHAEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK118_MAGIKOOPA_INTRO] = FormationPack(
    Formation(
        members=[
            FormationMember(KAMEKEnemy, 199, 119),
            FormationMember(TERRACOTTAEnemy, 135, 103, hidden_at_start=True),
            FormationMember(TERRACOTTAEnemy, 231, 151, hidden_at_start=True),
            FormationMember(TERRACOTTAEnemy, 135, 127, hidden_at_start=True),
            FormationMember(TERRACOTTAEnemy, 183, 151, hidden_at_start=True),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(KAMEKEnemy, 199, 119),
            FormationMember(MALAKOOPAEnemy, 215, 143, hidden_at_start=True),
            FormationMember(MALAKOOPAEnemy, 151, 111, hidden_at_start=True),
            FormationMember(TUBOTROOPAEnemy, 167, 135, hidden_at_start=True),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(KAMEKEnemy, 199, 119),
            FormationMember(GUGOOMBAEnemy, 119, 119, hidden_at_start=True),
            FormationMember(GUGOOMBAEnemy, 199, 159, hidden_at_start=True),
            FormationMember(STARCRUSTEREnemy, 167, 135, hidden_at_start=True),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK119_MAGIKOOPA_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(KAMEKEnemy, 199, 119),
            FormationMember(FORKIESEnemy, 135, 111, hidden_at_start=True),
            FormationMember(STARCRUSTEREnemy, 215, 151, hidden_at_start=True),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(KAMEKEnemy, 199, 119),
            FormationMember(GUGOOMBAEnemy, 119, 119, hidden_at_start=True),
            FormationMember(GUGOOMBAEnemy, 199, 159, hidden_at_start=True),
            FormationMember(STARCRUSTEREnemy, 167, 135, hidden_at_start=True),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(KAMEKEnemy, 199, 119),
            FormationMember(MALAKOOPAEnemy, 215, 143, hidden_at_start=True),
            FormationMember(MALAKOOPAEnemy, 151, 111, hidden_at_start=True),
            FormationMember(TUBOTROOPAEnemy, 167, 135, hidden_at_start=True),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK120_NINJA_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(NINJAEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(NINJAEnemy, 151, 119),
            FormationMember(DOPPELEnemy, 199, 159),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(NINJAEnemy, 199, 151),
            FormationMember(NINJAEnemy, 135, 119),
            FormationMember(HIPPOPOEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(NINJAEnemy, 199, 151),
            FormationMember(NINJAEnemy, 135, 119),
            FormationMember(HIPPOPOEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(NINJAEnemy, 151, 119),
            FormationMember(DOPPELEnemy, 199, 159),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK122_SPRINGER_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(SPRINGEREnemy, 215, 143),
            FormationMember(GLUMREAPEREnemy, 135, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPRINGEREnemy, 231, 135),
            FormationMember(SPRINGEREnemy, 167, 103),
            FormationMember(PUPPOXEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPRINGEREnemy, 215, 143),
            FormationMember(GLUMREAPEREnemy, 135, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK123_SPRINGER_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(SPRINGEREnemy, 183, 127),
            FormationMember(PUPPOXEnemy, 215, 143),
            FormationMember(PUPPOXEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPRINGEREnemy, 231, 135),
            FormationMember(SPRINGEREnemy, 167, 103),
            FormationMember(PUPPOXEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SPRINGEREnemy, 215, 143),
            FormationMember(GLUMREAPEREnemy, 135, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK124_MADMALLET_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(MADMALLETEnemy, 151, 119),
            FormationMember(MADMALLETEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(MADMALLETEnemy, 151, 127),
            FormationMember(MADMALLETEnemy, 199, 151),
            FormationMember(MADMALLETEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(MADMALLETEnemy, 183, 127),
            FormationMember(MADMALLETEnemy, 135, 127),
            FormationMember(MADMALLETEnemy, 231, 135),
            FormationMember(MADMALLETEnemy, 167, 103),
            FormationMember(MADMALLETEnemy, 183, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK125_MADMALLET_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(MADMALLETEnemy, 183, 127),
            FormationMember(MADMALLETEnemy, 135, 127),
            FormationMember(MADMALLETEnemy, 231, 135),
            FormationMember(MADMALLETEnemy, 167, 103),
            FormationMember(MADMALLETEnemy, 183, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(MADMALLETEnemy, 151, 127),
            FormationMember(MADMALLETEnemy, 199, 151),
            FormationMember(MADMALLETEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(MADMALLETEnemy, 151, 119),
            FormationMember(MADMALLETEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK126_POUNDER_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(POUNDEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(POUNDEREnemy, 183, 127),
            FormationMember(POUNDEREnemy, 231, 135),
            FormationMember(POUNDEREnemy, 167, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(POUNDEREnemy, 167, 135),
            FormationMember(POUNDEREnemy, 199, 143),
            FormationMember(POUNDEREnemy, 151, 119),
            FormationMember(POUNDEREnemy, 167, 103),
            FormationMember(POUNDEREnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK126_POUNDER_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(POUNDEREnemy, 167, 135),
            FormationMember(POUNDEREnemy, 199, 143),
            FormationMember(POUNDEREnemy, 151, 119),
            FormationMember(POUNDEREnemy, 167, 103),
            FormationMember(POUNDEREnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(POUNDEREnemy, 183, 127),
            FormationMember(POUNDEREnemy, 231, 135),
            FormationMember(POUNDEREnemy, 167, 103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(POUNDEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK128_POUNDETTE_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(POUNDETTEEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(POUNDETTEEnemy, 183, 127),
            FormationMember(POUNDETTEEnemy, 151, 111),
            FormationMember(POUNDETTEEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(POUNDETTEEnemy, 167, 135),
            FormationMember(POUNDETTEEnemy, 199, 119),
            FormationMember(POUNDETTEEnemy, 135, 119),
            FormationMember(POUNDETTEEnemy, 167, 103),
            FormationMember(POUNDETTEEnemy, 199, 151),
            FormationMember(POUNDETTEEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK128_POUNDETTE_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(POUNDETTEEnemy, 167, 135),
            FormationMember(POUNDETTEEnemy, 199, 119),
            FormationMember(POUNDETTEEnemy, 135, 119),
            FormationMember(POUNDETTEEnemy, 167, 103),
            FormationMember(POUNDETTEEnemy, 199, 151),
            FormationMember(POUNDETTEEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(POUNDETTEEnemy, 183, 127),
            FormationMember(POUNDETTEEnemy, 151, 111),
            FormationMember(POUNDETTEEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(POUNDETTEEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
)
packs[PACK132_GLUMREAPER_WITH_HIPPOPO_DOPPEL] = FormationPack(
    Formation(
        members=[
            FormationMember(GLUMREAPEREnemy, 183, 127),
            FormationMember(GLUMREAPEREnemy, 135, 119),
            FormationMember(GLUMREAPEREnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GLUMREAPEREnemy, 215, 159),
            FormationMember(HIPPOPOEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GLUMREAPEREnemy, 151, 127),
            FormationMember(GLUMREAPEREnemy, 183, 143),
            FormationMember(DOPPELEnemy, 167, 103),
            FormationMember(DOPPELEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GLUMREAPEREnemy, 151, 127),
            FormationMember(GLUMREAPEREnemy, 183, 143),
            FormationMember(DOPPELEnemy, 167, 103),
            FormationMember(DOPPELEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(GLUMREAPEREnemy, 215, 159),
            FormationMember(HIPPOPOEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK134_LILBOO_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(LILBOOEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(LILBOOEnemy, 183, 151),
            FormationMember(LILBOOEnemy, 215, 135),
            FormationMember(HIPPOPOEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(LILBOOEnemy, 167, 143),
            FormationMember(LILBOOEnemy, 199, 119),
            FormationMember(PUPPOXEnemy, 151, 103),
            FormationMember(DOPPELEnemy, 215, 159),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(LILBOOEnemy, 167, 143),
            FormationMember(LILBOOEnemy, 199, 119),
            FormationMember(PUPPOXEnemy, 151, 103),
            FormationMember(DOPPELEnemy, 215, 159),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(LILBOOEnemy, 183, 151),
            FormationMember(LILBOOEnemy, 215, 135),
            FormationMember(HIPPOPOEnemy, 151, 111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK136_JABITS_HAMMERS_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(JABITEnemy, 215, 135),
            FormationMember(MADMALLETEnemy, 151, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(JABITEnemy, 151, 143),
            FormationMember(POUNDEREnemy, 151, 111),
            FormationMember(POUNDETTEEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
)
packs[PACK137_JABITS_HAMMERS_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(JABITEnemy, 151, 127),
            FormationMember(JABITEnemy, 183, 143),
            FormationMember(MADMALLETEnemy, 135, 103),
            FormationMember(MADMALLETEnemy, 183, 111),
            FormationMember(POUNDETTEEnemy, 215, 127),
            FormationMember(POUNDETTEEnemy, 231, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(JABITEnemy, 151, 143),
            FormationMember(POUNDEREnemy, 151, 111),
            FormationMember(POUNDETTEEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK138_RATFUNKS_ONLY] = FormationPack(
    Formation(
        members=[
            FormationMember(RATFUNKEnemy, 135, 119),
            FormationMember(RATFUNKEnemy, 199, 151),
            FormationMember(RATFUNKEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(RATFUNKEnemy, 135, 119),
            FormationMember(RATFUNKEnemy, 199, 151),
            FormationMember(RATFUNKEnemy, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK139_ARTICHOKERS_ONLY] = FormationPack(
    Formation(
        members=[
            FormationMember(ARTICHOKEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(ARTICHOKEREnemy, 151, 119),
            FormationMember(ARTICHOKEREnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(ARTICHOKEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK140_PUNCHINELLO_STATIC] = FormationPack(
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
        unknown_bit=True,
    )
)
packs[PACK141_CROOK_HENCHMEN_ONLY] = FormationPack(
    # henchman
    Formation(
        members=[
            FormationMember(CROOKEnemy, 135, 119),
            FormationMember(CROOKEnemy, 199, 119),
            FormationMember(CROOKEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CROOKEnemy, 167, 103),
            FormationMember(CROOKEnemy, 135, 119),
            FormationMember(CROOKEnemy, 183, 127),
            FormationMember(CROOKEnemy, 199, 151),
            FormationMember(CROOKEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CROOKEnemy, 135, 119),
            FormationMember(CROOKEnemy, 199, 119),
            FormationMember(CROOKEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK142_SNIFIT_ONLY] = FormationPack(
    # henchman
    Formation(
        members=[
            FormationMember(SNIFITEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK143_TOWER_FIREBALLS] = FormationPack(
    Formation(
        members=[
            FormationMember(FIREBALLEnemy, 151, 111),
            FormationMember(FIREBALLEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(FIREBALLEnemy, 167, 135),
            FormationMember(FIREBALLEnemy, 167, 111),
            FormationMember(FIREBALLEnemy, 215, 135),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(FIREBALLEnemy, 151, 111),
            FormationMember(FIREBALLEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(STUMPETEnemy, 151, 111),
            FormationMember(MAGMUSEnemy, 183, 159),
            FormationMember(MAGMUSEnemy, 199, 135),
            FormationMember(MAGMUSEnemy, 231, 159),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(STUMPETEnemy, 183, 127),
            FormationMember(MAGMUSEnemy, 119, 127),
            FormationMember(MAGMUSEnemy, 183, 159),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK145_CORKPEDITE_ENCOUNTER] = FormationPack(
    Formation(
        members=[
            FormationMember(CORKPEDITEEnemy, 151, 111),
            FormationMember(BODYEnemy, 167, 103),
            FormationMember(OERLIKONEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CORKPEDITEEnemy, 151, 111),
            FormationMember(BODYEnemy, 167, 103),
            FormationMember(OERLIKONEnemy, 183, 159),
            FormationMember(OERLIKONEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(CORKPEDITEEnemy, 151, 111),
            FormationMember(BODYEnemy, 167, 103),
            FormationMember(OERLIKONEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK146_CLERK_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(CLERKEnemy, 199, 119),
            FormationMember(MADMALLETEnemy, 135, 119),
            FormationMember(MADMALLETEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK147_MANAGER_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(MANAGEREnemy, 199, 119),
            FormationMember(POUNDEREnemy, 151, 111),
            FormationMember(POUNDEREnemy, 167, 135),
            FormationMember(POUNDEREnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK148_DIRECTOR_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(DIRECTOREnemy, 183, 127),
            FormationMember(POUNDETTEEnemy, 135, 119),
            FormationMember(POUNDETTEEnemy, 167, 103),
            FormationMember(POUNDETTEEnemy, 199, 151),
            FormationMember(POUNDETTEEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK149_GUNYOLK_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(GUNYOLKEnemy, 199, 103),
            FormationMember(FACTORYCHIEFEnemy, 231, 151),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK150_MAD_MALLET_FACTORY_FIGHT] = FormationPack(
    Formation(
        members=[
            FormationMember(MADMALLETEnemy, 151, 111),
            FormationMember(MADMALLETEnemy, 167, 135),
            FormationMember(MADMALLETEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK151_APPRENTICE_FIGHT] = FormationPack(
    Formation(
        members=[
            FormationMember(APPRENTICEEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK152_THREE_MACHINE_SHYSTER_SUBSTITUTE] = FormationPack(
    Formation(
        members=[
            FormationMember(MACHINEMADEBodyguardEnemy, 199, 119),
            FormationMember(MACHINEMADEBodyguardEnemy, 135, 119),
            FormationMember(MACHINEMADEBodyguardEnemy, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK153_THREE_DRILLBIT_SUBSTITUTE] = FormationPack(
    Formation(
        members=[
            FormationMember(MACHINEMADEDrillbitEnemy, 183, 127),
            FormationMember(MACHINEMADEDrillbitEnemy, 167, 103),
            FormationMember(MACHINEMADEDrillbitEnemy, 231, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK154_SINGLE_SHYGUY_HENCHMAN] = FormationPack(
    # henchman
    Formation(
        members=[
            FormationMember(SHYGUYEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK155_MAD_MALLET_HENCHMEN] = FormationPack(
    # henchman
    Formation(
        members=[
            FormationMember(MADMALLETEnemy, x_pos=151, y_pos=127),
            FormationMember(MADMALLETEnemy, x_pos=199, y_pos=151),
            FormationMember(MADMALLETEnemy, x_pos=199, y_pos=119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK156_PANDORITE_FIGHT_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(PANDORITEEnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK157_HIDON_FIGHT_STATIC] = FormationPack(
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
        unknown_bit=True,
    )
)
packs[PACK158_BOXBOY_FIGHT_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(BOXBOYEnemy, 183, 127),
            FormationMember(FAUTSOEnemy, 151, 111, hidden_at_start=True),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK159_CHESTER_FIGHT_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(CHESTEREnemy, 183, 127),
            FormationMember(BAHAMUTTEnemy2, 135, 119, hidden_at_start=True),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK160_BOWYER_AERO_HENCHMEN] = FormationPack(
    Formation(
        members=[
            FormationMember(AEROEnemy, x_pos=167, y_pos=119),
            FormationMember(AEROEnemy, x_pos=199, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK161_BOOSTER_FIGHT_STATIC] = FormationPack(
    # henchmen
    Formation(
        members=[
            FormationMember(BOOSTEREnemy, 183, 127),
            FormationMember(SNIFITEnemy, 135, 119),
            FormationMember(SNIFITEnemy, 151, 143),
            FormationMember(SNIFITEnemy, 199, 151),
        ],
        run_event_at_load=BE0012_DIALOGUE_FROM_BOOSTER_FIGHT,
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK162_DUMMY_BOOSTER_POSSIBLY_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(BOOSTEREnemy2, 183, 127),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK163_CROCO1_FIGHT_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(CROCO1Enemy, 183, 127),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK164_CROCO2_FIGHT_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(CROCO2Enemy, 183, 127),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK165_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(MACHINEMADEEnemy16, 183, 127),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK166_JOHNNY_FIGHT_STATIC] = FormationPack(
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
        unknown_bit=True,
    )
)
packs[PACK167_CALAMARI_FIGHT_STATIC] = FormationPack(
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
        unknown_bit=True,
    )
)
packs[PACK168_BELOME1_FIGHT_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(BELOME1Enemy, 183, 127),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK169_BELOME2_FIGHT_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(BELOME2Enemy, 183, 127),
            FormationMember(MARIOCLONEEnemy, 135, 119, hidden_at_start=True),
            FormationMember(TOADSTOOL2Enemy, 215, 159, hidden_at_start=True),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK170_UNUSED] = FormationPack(
    Formation(
        members=[
            FormationMember(TERRAPINEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK171_VALENTINA_FIGHT_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(VALENTINAEnemy, 183, 127),
            FormationMember(DODOEnemy, 199, 151, hidden_at_start=True),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK172_CZAR_FIGHT_STATIC] = FormationPack(
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
        unknown_bit=True,
    )
)
packs[PACK173_MEGASMILAX_FIGHT_STATIC] = FormationPack(
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
        unknown_bit=True,
    )
)
packs[PACK174_COUNTDOWN_FIGHT_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(COUNTDOWNEnemy, 150, 93),
            FormationMember(DINGALINGEnemy, 158, 52),
            FormationMember(DINGALINGEnemy, 194, 67),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK175_BIRDETTA_FIGHT_STATIC] = FormationPack(
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
        unknown_bit=True,
    )
)
packs[PACK176_BUNDT_FIGHT_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(BUNDTEnemy, 199, 127),
            FormationMember(RASPBERRYEnemy, 199, 119),
            FormationMember(TORTEEnemy, 199, 151),
            FormationMember(TORTEEnemy, 135, 119),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK177_KGGG_FIGHT_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(KNIFEGUYEnemy, 151, 119),
            FormationMember(GRATEGUYEnemy, 199, 143),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK178_JINX1_FIGHT_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(JINX1Enemy, 183, 127),
        ],
        run_event_at_load=BE0071_JINX_USES_TRIPLE_KICK,
        music=MidbossMusic(),
    )
)
packs[PACK179_MACK_FIGHT_STATIC] = FormationPack(
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
        unknown_bit=True,
    )
)
packs[PACK180_YARIDOVICH_FIGHT_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(YARIDOVICHEnemy, 183, 127),
            FormationMember(YARIDOVICHMirageEnemy, 183, 127, hidden_at_start=True),
        ],
        music=BossMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK181_BOWYER_FIGHT_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(BOWYEREnemy, 183, 127),
        ],
        run_event_at_load=BE0014_SET_7EE00A_TO_PARTY_SIZE_AT_START_OF_FIGHT,
        music=BossMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK182_AXEM_FIGHT_STATIC] = FormationPack(
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
        unknown_bit=True,
    )
)
packs[PACK183_HAMMERBRO_FIGHT_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(HAMMERBROEnemy, 135, 127),
            FormationMember(HAMMERBROEnemy, 199, 143),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK184_CLOAKER_DOMINO_FIGHT_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(CLOAKEREnemy, 151, 111),
            FormationMember(DOMINOEnemy, 215, 159),
            FormationMember(MADADDEREnemy, 167, 135, hidden_at_start=True),
        ],
        run_event_at_load=BE0052_INTRO_SCENE_DOMINO_CLOAKER_S_INTRODUCTION,
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK185_SMITHY1_FIGHT_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(SMITHY1Enemy, 199, 127),
            FormationMember(SMELTEREnemy, 87, 87),
            FormationMember(MACHINEMADEBodyguardEnemy, 135, 127, hidden_at_start=True),
            FormationMember(MACHINEMADEBodyguardEnemy, 199, 159, hidden_at_start=True),
        ],
        music=Smithy1Music(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK186_EXOR_FIGHT_STATIC] = FormationPack(
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
        unknown_bit=True,
    )
)
packs[PACK187_JINX2_FIGHT_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(JINX2Enemy, 183, 127),
        ],
        run_event_at_load=BE0072_JINX_USES_QUICKSILVER,
        music=MidbossMusic(),
    )
)
packs[PACK188_JINX3_FIGHT_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(JINX3Enemy, 183, 127),
        ],
        run_event_at_load=BE0073_JINX_USES_BOMBS_AWAY,
        music=MidbossMusic(),
    )
)
packs[PACK189_JAGGER_FIGHT_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(JAGGEREnemy, 183, 127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK190_PYROSPHERE_HENCHMEN] = FormationPack(
    # henchman
    Formation(
        members=[
            FormationMember(PYROSPHEREEnemy, x_pos=151, y_pos=135),
            FormationMember(PYROSPHEREEnemy, x_pos=215, y_pos=135),
            FormationMember(PYROSPHEREEnemy, x_pos=183, y_pos=103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK191_HEAVY_TROOPAS] = FormationPack(
    Formation(
        members=[
            FormationMember(HEAVYTROOPAEnemy, 167, 135),
            FormationMember(HEAVYTROOPAEnemy, 151, 103),
            FormationMember(HEAVYTROOPAEnemy, 231, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK192_UNUSED] = FormationPack(
    Formation(
        members=[
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK193_HELIO_HENCHMEN] = FormationPack(
    Formation(
        members=[
            FormationMember(HELIOEnemy, x_pos=167, y_pos=119),
            FormationMember(HELIOEnemy, x_pos=135, y_pos=135),
            FormationMember(HELIOEnemy, x_pos=199, y_pos=167),
            FormationMember(HELIOEnemy, x_pos=231, y_pos=151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK194_BODYGUARD_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(BODYGUARDEnemy, x_pos=167, y_pos=119),
            FormationMember(BODYGUARDEnemy, x_pos=199, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
    Formation(
        members=[
            FormationMember(BODYGUARDEnemy, x_pos=151, y_pos=111),
            FormationMember(BODYGUARDEnemy, x_pos=215, y_pos=143),
            FormationMember(BODYGUARDEnemy, x_pos=167, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
    Formation(
        members=[
            FormationMember(BODYGUARDEnemy, x_pos=167, y_pos=119),
            FormationMember(BODYGUARDEnemy, x_pos=199, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
)
packs[PACK195_BODYGUARD_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(BODYGUARDEnemy, x_pos=167, y_pos=119),
            FormationMember(BODYGUARDEnemy, x_pos=199, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
    Formation(
        members=[
            FormationMember(BODYGUARDEnemy, x_pos=151, y_pos=111),
            FormationMember(BODYGUARDEnemy, x_pos=215, y_pos=143),
            FormationMember(BODYGUARDEnemy, x_pos=167, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
    Formation(
        members=[
            FormationMember(BODYGUARDEnemy, x_pos=151, y_pos=111),
            FormationMember(BODYGUARDEnemy, x_pos=215, y_pos=143),
            FormationMember(BODYGUARDEnemy, x_pos=167, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
)
packs[PACK196_GENO_CLONE_HENCHMAN] = FormationPack(
    Formation(
        members=[
            FormationMember(GENOCLONEEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK197_BOWSER_CLONE_HENCHMAN] = FormationPack(
    Formation(
        members=[
            FormationMember(BOWSERCLONEEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK198_TOADSTOOL_CLONE_HENCHMAN] = FormationPack(
    Formation(
        members=[
            FormationMember(TOADSTOOL2Enemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK199_CROOKS_ONLY] = FormationPack(
    Formation(
        members=[
            FormationMember(CROOKEnemy, x_pos=135, y_pos=119),
            FormationMember(CROOKEnemy, x_pos=199, y_pos=119),
            FormationMember(CROOKEnemy, x_pos=199, y_pos=151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
    Formation(
        members=[
            FormationMember(CROOKEnemy, x_pos=167, y_pos=103),
            FormationMember(CROOKEnemy, x_pos=135, y_pos=119),
            FormationMember(CROOKEnemy, x_pos=183, y_pos=127),
            FormationMember(CROOKEnemy, x_pos=199, y_pos=151),
            FormationMember(CROOKEnemy, x_pos=231, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
    Formation(
        members=[
            FormationMember(CROOKEnemy, x_pos=135, y_pos=119),
            FormationMember(CROOKEnemy, x_pos=199, y_pos=119),
            FormationMember(CROOKEnemy, x_pos=199, y_pos=151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
)
packs[PACK200_MARIO_CLONE_HENCHMAN] = FormationPack(
    Formation(
        members=[
            FormationMember(MARIOCLONEEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK201_BIRDY_HENCHMEN] = FormationPack(
    # henchman
    Formation(
        [
            FormationMember(BIRDYEnemy, x_pos=215, y_pos=119),
            FormationMember(BIRDYEnemy, x_pos=151, y_pos=119),
            FormationMember(BIRDYEnemy, x_pos=183, y_pos=151),
        ]
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
    Formation(
        [
            FormationMember(BIRDYEnemy, x_pos=151, y_pos=111),
            FormationMember(BIRDYEnemy, x_pos=215, y_pos=143),
            FormationMember(BIRDYEnemy, x_pos=151, y_pos=143),
            FormationMember(BIRDYEnemy, x_pos=215, y_pos=111),
            FormationMember(BIRDYEnemy, x_pos=183, y_pos=127),
        ]
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
    Formation(
        [
            FormationMember(BIRDYEnemy, x_pos=215, y_pos=119),
            FormationMember(BIRDYEnemy, x_pos=151, y_pos=119),
            FormationMember(BIRDYEnemy, x_pos=183, y_pos=151),
        ]
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
)
packs[PACK202_MALLOW_CLONE_HENCHMAN] = FormationPack(
    Formation(
        members=[
            FormationMember(MALLOWCLONEEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK203_MACHINE_AXEM_HENCHMEN] = FormationPack(
    # henchmen
    Formation(
        [
            FormationMember(MACHINEMADEAxemPinkEnemy, x_pos=151, y_pos=111),
            None,
            FormationMember(MACHINEMADEAxemRedEnemy, x_pos=151, y_pos=143),
            None,
            FormationMember(MACHINEMADEAxemGreenEnemy, x_pos=215, y_pos=143),
        ],
        music=BossMusic(),
        unknown_bit=True,
    ),
    Formation(
        [
            FormationMember(MACHINEMADEAxemBlackEnemy, x_pos=151, y_pos=119),
            FormationMember(MACHINEMADEAxemBlackEnemy, x_pos=231, y_pos=127),
            FormationMember(MACHINEMADEAxemYellowEnemy, x_pos=199, y_pos=143),
            FormationMember(MACHINEMADEAxemYellowEnemy, x_pos=183, y_pos=103),
        ],
        music=BossMusic(),
        unknown_bit=True,
    ),
    Formation(
        [
            FormationMember(MACHINEMADEAxemPinkEnemy, x_pos=151, y_pos=111),
            None,
            FormationMember(MACHINEMADEAxemRedEnemy, x_pos=151, y_pos=143),
            None,
            FormationMember(MACHINEMADEAxemGreenEnemy, x_pos=215, y_pos=143),
        ],
        music=BossMusic(),
        unknown_bit=True,
    ),
)
packs[PACK204_BLOOBER_HENCHMEN] = FormationPack(
    # henchmen
    Formation(
        members=[
            FormationMember(BLOOBEREnemy, x_pos=183, y_pos=127),
            FormationMember(BLOOBEREnemy, x_pos=231, y_pos=143),
            FormationMember(BLOOBEREnemy, x_pos=135, y_pos=111),
        ],
        music=None,
    )
)
packs[PACK205_BLUEBIRD_HENCHMEN] = FormationPack(
    # henchmen
    Formation(
        members=[
            FormationMember(BLUEBIRDEnemy, x_pos=199, y_pos=151),
            FormationMember(BLUEBIRDEnemy, x_pos=151, y_pos=111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
    Formation(
        members=[
            FormationMember(BLUEBIRDEnemy, x_pos=183, y_pos=143),
            FormationMember(BLUEBIRDEnemy, x_pos=183, y_pos=111),
            FormationMember(BLUEBIRDEnemy, x_pos=231, y_pos=135),
            FormationMember(BLUEBIRDEnemy, x_pos=135, y_pos=119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
    Formation(
        members=[
            FormationMember(BLUEBIRDEnemy, x_pos=199, y_pos=151),
            FormationMember(BLUEBIRDEnemy, x_pos=151, y_pos=111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
)
packs[PACK206_DESERT_SHOGUNS] = FormationPack(
    Formation(
        members=[
            FormationMember(SHOGUNEnemy, 167, 135),
            FormationMember(SHOGUNEnemy, 151, 111),
            FormationMember(SHOGUNEnemy, 215, 143),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK207_MOKURA_BOSS_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(FORMLESSEnemy, 167, 135),
            FormationMember(MOKURAEnemy, 167, 135, hidden_at_start=True),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK208_DODO_BOSS_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(DODOEnemySolo, 183, 127),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK209_MAGIKOOPA_BOSS_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(KAMEKEnemy, 215, 111),
            FormationMember(TERRAPINEnemy, 167, 135, hidden_at_start=True),
        ],
        run_event_at_load=BE0101_MAGIKOOPA_IS_THERE,
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
)
packs[PACK210_BOOMER_BOSS_STATIC] = FormationPack(
    Formation(
        members=[
            FormationMember(BOOMEREnemy, 215, 143),
            FormationMember(HANGINSHYEnemy, 66, 115),
            FormationMember(HANGINSHYEnemy, 186, 74),
        ],
        music=MidbossMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
)
packs[PACK212_MACHINE_BOWYER_PACK] = FormationPack(
    Formation(
        members=[
            FormationMember(MACHINEMADEBowyerEnemy, 183, 127),
        ],
        music=BossMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(MACHINEMADEAxemBlackEnemy, 151, 119),
            FormationMember(MACHINEMADEAxemBlackEnemy, 231, 127),
            FormationMember(MACHINEMADEAxemYellowEnemy, 199, 143),
            FormationMember(MACHINEMADEAxemYellowEnemy, 183, 103),
        ],
        music=BossMusic(),
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
)
packs[PACK215_SMITHY_2_PACK] = FormationPack(
    Formation(
        members=[
            FormationMember(SMITHYBodyEnemy, 183, 135, hidden_at_start=True),
            FormationMember(SMITHY2Enemy, 183, 175),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK216_CULEX_BOSS_STATIC] = FormationPack(
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
        unknown_bit=True,
    )
)
packs[PACK217_FIRE_CRYSTAL_HENCHMAN] = FormationPack(
    Formation(
        members=[
            FormationMember(FIRECRYSTALEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
        run_event_at_load=BE0076_SOLO_FIRE_CRYSTAL_APPEARS,
    )
)
packs[PACK218_WATER_CRYSTAL_HENCHMAN] = FormationPack(
    Formation(
        members=[
            FormationMember(WATERCRYSTALEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
        run_event_at_load=BE0020_SOLO_WATER_CRYSTAL_APPEARS
    )
)
packs[PACK219_EARTH_CRYSTAL_HENCHMAN] = FormationPack(
    Formation(
        members=[
            FormationMember(EARTHCRYSTALEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
        run_event_at_load=BE0011_SOLO_EARTH_CRYSTAL_APPEARS
    )
)
packs[PACK220_WIND_CRYSTAL_HENCHMAN] = FormationPack(
    Formation(
        members=[
            FormationMember(WINDCRYSTALEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
        run_event_at_load=BE0001_SOLO_WIND_CRYSTAL_APPEARS
    )
)
packs[PACK221_GOOMBETTE_HENCHMEN] = FormationPack(
    Formation(
        members=[
            FormationMember(GOOMBETTEEnemy, x_pos=183, y_pos=127),
            FormationMember(GOOMBETTEEnemy, x_pos=231, y_pos=135),
            FormationMember(GOOMBETTEEnemy, x_pos=167, y_pos=103),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
# henchman
packs[PACK222_PIRANHA_HENCHMEN] = FormationPack(
    Formation(
        members=[
            FormationMember(PIRANHAPLANTEnemy, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ), 
    Formation(
        [
            FormationMember(PIRANHAPLANTEnemy, x_pos=167, y_pos=111),
            FormationMember(PIRANHAPLANTEnemy, x_pos=167, y_pos=135),
            FormationMember(PIRANHAPLANTEnemy, x_pos=215, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    Formation(
        [
            FormationMember(PIRANHAPLANTEnemy, x_pos=151, y_pos=143),
            FormationMember(PIRANHAPLANTEnemy, x_pos=151, y_pos=111),
            FormationMember(PIRANHAPLANTEnemy, x_pos=199, y_pos=119),
            FormationMember(PIRANHAPLANTEnemy, x_pos=231, y_pos=143),
            FormationMember(PIRANHAPLANTEnemy, x_pos=199, y_pos=159),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK223_EGGBERT_HENCHMEN] = FormationPack(
    Formation(
        members=[
            FormationMember(EGGBERTEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
    Formation(
        members=[
            FormationMember(EGGBERTEnemy, x_pos=167, y_pos=111),
            FormationMember(EGGBERTEnemy, x_pos=167, y_pos=135),
            FormationMember(EGGBERTEnemy, x_pos=215, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
    Formation(
        members=[
            FormationMember(EGGBERTEnemy, x_pos=135, y_pos=127),
            FormationMember(EGGBERTEnemy, x_pos=183, y_pos=111),
            FormationMember(EGGBERTEnemy, x_pos=183, y_pos=151),
            FormationMember(EGGBERTEnemy, x_pos=231, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
)
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
)
packs[PACK229_OBSTACLE_BLOOBER] = FormationPack(
    Formation(
        members=[
            FormationMember(BLOOBEREnemy, 199, 119),
            FormationMember(BLOOBEREnemy, 183, 151),
            FormationMember(BLOOBEREnemy, 231, 151),
            FormationMember(STARCRUSTEREnemy, 135, 103),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
)
packs[PACK235_CHESTER_DUPE] = FormationPack(
    Formation(
        members=[
            FormationMember(CHESTEREnemy, 183, 127),
            FormationMember(BAHAMUTTEnemy, 135, 119, hidden_at_start=True),
        ],
        music=NormalBattleMusic(),
        can_run_away=False,
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
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
        unknown_bit=True,
    )
)
packs[PACK248_AXEM_BLACK_ALONE] = FormationPack(
    Formation(
        members=[
            FormationMember(AXEMBLACKEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK249_AXEM_PINK_ALONE] = FormationPack(
    Formation(
        members=[
            FormationMember(AXEMPINKEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK250_AXEM_YELLOW_ALONE] = FormationPack(
    Formation(
        members=[
            FormationMember(AXEMYELLOWEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK251_AXEM_GREEN_ALONE] = FormationPack(
    Formation(
        members=[
            FormationMember(AXEMGREENEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK252_DINGALING_ALONE] = FormationPack(
    Formation(
        members=[
            FormationMember(DINGALINGEnemy, x_pos=183, y_pos=127),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
packs[PACK253_SMITHY_HENCHMEN_PACK_1] = FormationPack(
    Formation(
        members=[
            FormationMember(MACHINEMADEBodyguardEnemy2, x_pos=151, y_pos=111),
            FormationMember(AEROEnemy2, x_pos=215, y_pos=127),
            FormationMember(DRILLBITEnemy2, x_pos=167, y_pos=151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
    Formation(
        members=[
            FormationMember(DRILLBITEnemy2, x_pos=135, y_pos=119),
            FormationMember(DRILLBITEnemy2, x_pos=167, y_pos=103),
            FormationMember(DRILLBITEnemy2, x_pos=199, y_pos=151),
            FormationMember(DRILLBITEnemy2, x_pos=231, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
    Formation(
        members=[
            FormationMember(DRILLBITEnemy2, x_pos=183, y_pos=127),
            FormationMember(AEROEnemy2, x_pos=215, y_pos=143),
            FormationMember(AEROEnemy2, x_pos=151, y_pos=111),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
)
packs[PACK254_SMITHY_HENCHMEN_PACK_2] = FormationPack(
    Formation(
        members=[
            FormationMember(MACHINEMADEBodyguardEnemy2, x_pos=151, y_pos=111),
            FormationMember(AEROEnemy2, x_pos=215, y_pos=127),
            FormationMember(DRILLBITEnemy2, x_pos=167, y_pos=151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
    Formation(
        members=[
            FormationMember(MACHINEMADEBodyguardEnemy2, x_pos=167, y_pos=119),
            FormationMember(MACHINEMADEBodyguardEnemy2, x_pos=199, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
    Formation(
        members=[
            FormationMember(DRILLBITEnemy2, x_pos=231, y_pos=135),
            FormationMember(DRILLBITEnemy2, x_pos=167, y_pos=103),
            FormationMember(MACHINEMADEBodyguardEnemy2, x_pos=167, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
)
packs[PACK255_SMITHY_HENCHMEN_PACK_3] = FormationPack(
    Formation(
        members=[
            FormationMember(MACHINEMADEBodyguardEnemy2, x_pos=151, y_pos=111),
            FormationMember(AEROEnemy2, x_pos=215, y_pos=127),
            FormationMember(DRILLBITEnemy2, x_pos=167, y_pos=151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
    Formation(
        members=[
            FormationMember(AEROEnemy2, x_pos=167, y_pos=103),
            FormationMember(AEROEnemy2, x_pos=135, y_pos=119),
            FormationMember(AEROEnemy2, x_pos=183, y_pos=127),
            FormationMember(AEROEnemy2, x_pos=199, y_pos=151),
            FormationMember(AEROEnemy2, x_pos=231, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
    Formation(
        members=[
            FormationMember(AEROEnemy2, x_pos=231, y_pos=135),
            FormationMember(AEROEnemy2, x_pos=167, y_pos=103),
            FormationMember(MACHINEMADEBodyguardEnemy2, x_pos=167, y_pos=135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    ),
)

# Pack Collection
pack_collection = PackCollection(packs)
