from ...types.physical_objects import HenchmanNPC, SpriteAnimation, SpriteAnimationCollection
from ..rooms.npcs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments.sequence_speeds import FAST, FASTEST, VERY_FAST

class ShysterHenchman(HenchmanNPC):
    """Shyster henchman NPC for boss fights."""

    _base = SHYSTER_NPC
    _recoil = 2
    _tower_crying = 3
    _bandits_way_distracted = 3
    _mines_punch = 4
    _tower_bullet = 4
    _tower_toss = 4
    _chapel_laugh = 3
    _kitchen_prep = 4
    _ship_beckon = 4
    _dojo_challenge = 4
    _statue_intro = 3
    _statue_peck = 4
    _statue_flustered = 2
    _keep_challenge = 4
    _keep_summon = 4
    _chandelier_challenge = 4
    _factory_pierce = 4
    _endgame_challenge = 4


class CrookHenchman(HenchmanNPC):
    """Crook henchman NPC for boss fights."""

    _base = CROOK_NPC
    _recoil = 2
    _mines_punch = 3
    _tower_bullet = 3
    _tower_toss = 3
    _kitchen_prep = 3
    _ship_beckon = 3
    _dojo_challenge = 3
    _statue_flustered = 2
    _keep_challenge = 3
    _keep_summon = 3
    _chandelier_challenge = 3
    _factory_pierce = 3
    _endgame_challenge = 3


class BobOmbHenchman(HenchmanNPC):
    """Bob-omb henchman NPC for boss fights."""

    _base = BOB_OMB_NPC
    _recoil = 2
    _tower_crying = 4
    _bandits_way_distracted = 4
    _mines_punch = 4
    _tower_bullet = 4
    _chapel_laugh = 4
    _kitchen_prep = 4
    _ship_beckon = 4
    _dojo_challenge = 4
    _statue_intro = 4
    _statue_flustered = 2
    _keep_challenge = 4
    _keep_summon = 4
    _chandelier_challenge = 4
    _factory_pierce = 4
    _endgame_challenge = 4


class MicrobombHenchman(HenchmanNPC):
    """Microbomb henchman NPC for boss fights."""

    _base = MICROBOMB_NPC


class SpookumHenchman(HenchmanNPC):
    """Spookum henchman NPC for boss fights."""

    _base = SPOOKUM_NPC
    _recoil = 2
    _tower_crying = 4
    _bandits_way_distracted = 4
    _mines_punch = 3
    _tower_bullet = 5
    _tower_toss = 5
    _chapel_laugh = 4
    _kitchen_prep = 4
    _ship_beckon = 3
    _dojo_challenge = 3
    _statue_intro = 4
    _statue_peck = 3
    _statue_flustered = 2
    _keep_challenge = 3
    _keep_summon = 5
    _chandelier_challenge = 3
    _factory_pierce = 3
    _endgame_challenge = 3

class SnifitHenchman(HenchmanNPC):
    """Snifit henchman NPC for boss fights."""

    _base = SNIFIT_NPC
    _recoil = 2
    _tower_crying = 4
    _bandits_way_distracted = 4
    _mines_punch = 3
    _tower_bullet = 5
    _tower_toss = 5
    _chapel_laugh = 4
    _kitchen_prep = 4
    _ship_beckon = 3
    _dojo_challenge = 3
    _statue_intro = 4
    _statue_peck = 3
    _statue_flustered = 2
    _keep_challenge = 3
    _keep_summon = 5
    _chandelier_challenge = 3
    _factory_pierce = 3
    _endgame_challenge = 3


class TorteHenchman(HenchmanNPC):
    """Torte henchman NPC for boss fights."""

    _base = TORTE_NPC
    _recoil = 2
    _mines_punch = 3
    _tower_bullet = 3
    _tower_toss = 3
    _kitchen_prep = 3
    _ship_beckon = 3
    _dojo_challenge = 3
    _statue_intro = 3
    _statue_flustered = 2
    _keep_challenge = 3
    _keep_summon = 3
    _chandelier_challenge = 3
    _factory_pierce = 3
    _endgame_challenge = 3


class BlooberHenchman(HenchmanNPC):
    """Bloober henchman NPC for boss fights."""

    _base = BLOOBER_NPC
    _recoil = 2
    _tower_crying = 0
    _bandits_way_distracted = 0
    _mines_punch = 3
    _tower_bullet = 3
    _tower_toss = 3
    _chapel_laugh = 0
    _kitchen_prep = 3
    _ship_beckon = 3
    _dojo_challenge = 3
    _statue_intro = 5
    _statue_peck = 3
    _statue_flustered = 2
    _keep_challenge = 3
    _keep_summon = 3
    _chandelier_challenge = 3
    _factory_pierce = 3
    _endgame_challenge = 3
    _tpose_mold_id = 1
    _tpose = 6


class TinyBlooberHenchman(HenchmanNPC):
    """Tiny Bloober henchman NPC for boss fights."""

    _base = TINY_BLOOBER


class GoombetteLowerHenchman(HenchmanNPC):
    """Goombette henchman NPC for boss fights."""

    _base = GOOMBETTE_LOWER_NPC
    _recoil = 2
    _tower_crying = 2
    _bandits_way_distracted = 2
    _mines_punch = 3
    _tower_bullet = 3
    _tower_toss = 3
    _chapel_laugh = 2
    _kitchen_prep = 3
    _ship_beckon = 3
    _dojo_challenge = 3
    _statue_intro = 2
    _statue_flustered = 2
    _keep_challenge = 3
    _keep_summon = 3
    _chandelier_challenge = 3
    _factory_pierce = 3
    _endgame_challenge = 3


class BandanaBlueHenchman(HenchmanNPC):
    """Bandana Blue henchman NPC for boss fights."""

    _base = BANDANA_BLUE_NPC
    _recoil = 2
    _mines_punch = 3
    _tower_bullet = 4
    _tower_toss = 4
    _kitchen_prep = 3
    _ship_beckon = 4
    _dojo_challenge = 4
    _statue_intro = 4
    _statue_peck = 3
    _statue_flustered = 2
    _keep_challenge = 4
    _keep_summon = 4
    _chandelier_challenge = 4
    _factory_pierce = 3
    _endgame_challenge = 4


class BandanaRedHenchman(HenchmanNPC):
    """Bandana Red henchman NPC for boss fights."""

    _base = BANDANA_RED_NPC
    _recoil = 2
    _mines_punch = 3
    _tower_bullet = 4
    _tower_toss = 4
    _kitchen_prep = 3
    _ship_beckon = 4
    _dojo_challenge = 4
    _statue_intro = 4
    _statue_peck = 3
    _statue_flustered = 2
    _keep_challenge = 4
    _keep_summon = 4
    _chandelier_challenge = 4
    _factory_pierce = 3
    _endgame_challenge = 4


class DrillbitHenchman(HenchmanNPC):
    """Drillbit (Fake Seaside Town Toad) henchman NPC for boss fights."""

    _base = SEASIDE_TOWN_FAKE_GREEN_NPC
    _recoil = 2
    _tower_crying = 4
    _bandits_way_distracted = 4
    _mines_punch = 3
    _tower_bullet = 3
    _tower_toss = 3
    _chapel_laugh = 4
    _kitchen_prep = 3
    _ship_beckon = 3
    _ship_chair = 4
    _dojo_challenge = 3
    _statue_intro = 4
    _statue_flustered = 2
    _keep_challenge = 3
    _keep_summon = 3
    _chandelier_challenge = 5
    _factory_pierce = 3
    _endgame_challenge = 3


class MokuraHenchman(HenchmanNPC):
    """Mokura henchman NPC for boss fights."""

    _base = MOKURA_S_CLOUD_BLUE_NPC_2


class MariocloneHenchman(HenchmanNPC):
    """Mario clone henchman NPC for boss fights."""

    _base = MARIO_CLONE_WALKING_DOWN_LEFT_NPC
    _tower_crying = 14
    _bandits_way_distracted = 5
    _mines_punch = 14
    _tower_bullet = 5
    _tower_toss = 5
    _chapel_laugh = 14
    _kitchen_prep = 14
    _ship_beckon = 14
    _ship_chair = 14
    _dojo_challenge = 14
    _statue_intro = 14
    _keep_challenge = 14
    _keep_summon = 14
    _chandelier_challenge = 14
    _factory_pierce = 14
    _endgame_challenge = 14
    _look_at_camera = 13


class MallowcloneHenchman(HenchmanNPC):
    """Mallow clone henchman NPC for boss fights."""

    _base = MALLOW_WALKING_DOWN_LEFT_NPC_2
    _tower_crying = 4
    _bandits_way_distracted = 8
    _mines_punch = 4
    _tower_bullet = 2
    _tower_toss = 2
    _chapel_laugh = 2
    _kitchen_prep = 4
    _ship_beckon = 2
    _dojo_challenge = 4
    _statue_intro = 2
    _statue_flustered = 4
    _keep_challenge = 4
    _keep_summon = 2
    _chandelier_challenge = 4
    _factory_pierce = 4
    _endgame_challenge = 4
    _look_at_camera = 10


class GenocloneHenchman(HenchmanNPC):
    """Geno clone henchman NPC for boss fights."""

    _base = GENO_WALKING_DOWN_LEFT_NPC_2_CLONEABLE
    _tower_crying = 4
    _bandits_way_distracted = 8
    _mines_punch = 4
    _tower_bullet = 2
    _tower_toss = 2
    _chapel_laugh = 2
    _kitchen_prep = 4
    _ship_beckon = 2
    _dojo_challenge = 4
    _statue_intro = 2
    _statue_flustered = 4
    _keep_challenge = 4
    _keep_summon = 2
    _chandelier_challenge = 4
    _factory_pierce = 4
    _endgame_challenge = 4
    _look_at_camera = 10


class BowsercloneHenchman(HenchmanNPC):
    """Bowser clone henchman NPC for boss fights."""

    _base = BOWSER_WALKING_DOWN_LEFT_NPC
    _tower_crying = 4
    _bandits_way_distracted = 8
    _mines_punch = 4
    _tower_bullet = 2
    _tower_toss = 2
    _chapel_laugh = 2
    _kitchen_prep = 4
    _ship_beckon = 2
    _dojo_challenge = 4
    _statue_intro = 2
    _statue_flustered = 4
    _keep_challenge = 4
    _keep_summon = 2
    _chandelier_challenge = 4
    _factory_pierce = 4
    _endgame_challenge = 4
    _look_at_camera = 10


class BowsercloneHenchman_2(HenchmanNPC):
    """Bowser clone henchman NPC variant 2 for boss fights."""

    _base = BOWSER_WALKING_DOWN_LEFT_NPC_2
    _tower_crying = 4
    _bandits_way_distracted = 8
    _mines_punch = 4
    _tower_bullet = 2
    _tower_toss = 2
    _chapel_laugh = 2
    _kitchen_prep = 4
    _ship_beckon = 2
    _dojo_challenge = 4
    _statue_intro = 2
    _statue_flustered = 4
    _keep_challenge = 4
    _keep_summon = 2
    _chandelier_challenge = 4
    _factory_pierce = 4
    _endgame_challenge = 4
    _look_at_camera = 10


class PeachcloneHenchman(HenchmanNPC):
    """Peach clone henchman NPC for boss fights."""

    _base = TOADSTOOL_WALKING_DOWN_LEFT_LOW_VRAM
    _tower_crying = 4
    _bandits_way_distracted = 8
    _mines_punch = 4
    _tower_bullet = 2
    _tower_toss = 2
    _chapel_laugh = 2
    _kitchen_prep = 4
    _ship_beckon = 2
    _dojo_challenge = 4
    _statue_intro = 2
    _statue_flustered = 4
    _keep_challenge = 4
    _keep_summon = 2
    _chandelier_challenge = 4
    _factory_pierce = 4
    _endgame_challenge = 4
    _look_at_camera = 10


class FireCrystalHenchman(HenchmanNPC):
    """Fire Crystal henchman NPC for boss fights."""

    _base = FIRE_CRYSTAL_GRIDPLANE_NPC


class WaterCrystalHenchman(HenchmanNPC):
    """Water Crystal henchman NPC for boss fights."""

    _base = WATER_CRYSTAL_GRIDPLANE_NPC


class EarthCrystalHenchman(HenchmanNPC):
    """Earth Crystal henchman NPC for boss fights."""

    _base = EARTH_CRYSTAL_GRIDPLANE_NPC


class WindCrystalHenchman(HenchmanNPC):
    """Wind Crystal henchman NPC for boss fights."""

    _base = WIND_CRYSTAL_GRIDPLANE_NPC


class PiranhaPlantHenchman(HenchmanNPC):
    """Piranha Plant henchman NPC for boss fights."""

    _base = PIRANHA_PLANT_NPC_3
    _recoil = 2
    _tower_crying = 7
    _bandits_way_distracted = 7
    _mines_punch = 4
    _tower_bullet = 8
    _tower_toss = 8
    _chapel_laugh = 7
    _kitchen_prep = 3
    _ship_beckon = 3
    _ship_chair = 7
    _dojo_challenge = 3
    _statue_intro = 7
    _statue_peck = 4
    _statue_flustered = 2
    _keep_challenge = 3
    _keep_summon = 8
    _chandelier_challenge = 3
    _factory_pierce = 4
    _endgame_challenge = 3
    _tpose_mold_id = 3
    _tpose = 5


class FeatherHenchman(HenchmanNPC):
    """Feather henchman NPC for Dodo boss fight."""

    _base = FEATHER_NPC


class EggbertHenchman(HenchmanNPC):
    """Eggbert henchman NPC for boss fights."""

    _base = EGGBERT_GRIDPLANE_NPC
    _recoil = 2
    _tower_crying = 2
    _bandits_way_distracted = 2
    _mines_punch = 2
    _tower_bullet = 2
    _tower_toss = 2
    _chapel_laugh = 2
    _kitchen_prep = 2
    _ship_beckon = 2
    _dojo_challenge = 2
    _statue_intro = 2
    _statue_flustered = 2
    _keep_challenge = 2
    _keep_summon = 2
    _chandelier_challenge = 2
    _factory_pierce = 2
    _endgame_challenge = 2


class BluebirdHenchman(HenchmanNPC):
    """Bluebird henchman NPC for boss fights."""

    _base = BLUEBIRD_NPC_STATIC
    _recoil = 2
    _mines_punch = 3
    _tower_bullet = 4
    _tower_toss = 4
    _kitchen_prep = 3
    _ship_beckon = 4
    _dojo_challenge = 4
    _statue_intro = 4
    _statue_peck = 3
    _statue_flustered = 2
    _keep_challenge = 4
    _keep_summon = 4
    _chandelier_challenge = 4
    _factory_pierce = 3
    _endgame_challenge = 4


class BirdyHenchman(HenchmanNPC):
    """Birdy henchman NPC for boss fights."""

    _base = BIRDY_NPC
    _recoil = 2
    _mines_punch = 3
    _tower_bullet = 4
    _tower_toss = 4
    _kitchen_prep = 3
    _ship_beckon = 4
    _dojo_challenge = 4
    _statue_intro = 4
    _statue_peck = 3
    _statue_flustered = 2
    _keep_challenge = 4
    _keep_summon = 4
    _chandelier_challenge = 4
    _factory_pierce = 3
    _endgame_challenge = 4


class HelioHenchman(HenchmanNPC):
    """Helio henchman NPC for boss fights."""

    _base = HELIO_NPC


class SparkyHenchman(HenchmanNPC):
    """Sparky/Pyrosphere henchman NPC for boss fights."""

    _base = SPARKY_NPC
    _recoil = 2
    _mines_punch = 3
    _tower_bullet = 3
    _tower_toss = 3
    _kitchen_prep = 3
    _ship_beckon = 3
    _dojo_challenge = 3
    _statue_intro = 3
    _statue_flustered = 2
    _keep_challenge = 3
    _keep_summon = 3
    _chandelier_challenge = 3
    _factory_pierce = 3
    _endgame_challenge = 3


class AxemBlackHenchman(HenchmanNPC):
    """Axem Black henchman NPC for boss fights."""

    _base = AXEM_BLACK_NPC
    _recoil = 2
    _tower_crying = 7
    _bandits_way_distracted = 7
    _mines_punch = 7
    _tower_bullet = 3
    _tower_toss = 3
    _chapel_laugh = 7
    _kitchen_prep = 3
    _ship_beckon = 4
    _dojo_challenge = 4
    _statue_intro = 4
    _statue_peck = 3
    _statue_flustered = 2
    _keep_challenge = 4
    _keep_summon = 4
    _chandelier_challenge = 4
    _factory_pierce = 3
    _endgame_challenge = 4


class AxemPinkHenchman(HenchmanNPC):
    """Axem Pink henchman NPC for boss fights."""

    _base = AXEM_PINK_NPC
    _recoil = 2
    _tower_crying = 6
    _bandits_way_distracted = 6
    _mines_punch = 3
    _tower_bullet = 4
    _tower_toss = 4
    _chapel_laugh = 6
    _kitchen_prep = 3
    _ship_beckon = 4
    _dojo_challenge = 4
    _statue_intro = 4
    _statue_peck = 3
    _statue_flustered = 2
    _keep_challenge = 4
    _keep_summon = 4
    _chandelier_challenge = 4
    _factory_pierce = 3
    _endgame_challenge = 4


class AxemYellowHenchman(HenchmanNPC):
    """Axem Yellow henchman NPC for boss fights."""

    _base = AXEM_YELLOW_NPC
    _recoil = 2
    _tower_crying = 6
    _bandits_way_distracted = 6
    _mines_punch = 3
    _tower_bullet = 4
    _tower_toss = 4
    _chapel_laugh = 6
    _kitchen_prep = 3
    _ship_beckon = 4
    _dojo_challenge = 4
    _statue_intro = 4
    _statue_peck = 3
    _statue_flustered = 2
    _keep_challenge = 4
    _keep_summon = 4
    _chandelier_challenge = 4
    _factory_pierce = 3
    _endgame_challenge = 4


class AxemGreenHenchman(HenchmanNPC):
    """Axem Green henchman NPC for boss fights."""

    _base = AXEM_GREEN_NPC
    _recoil = 2
    _tower_crying = 6
    _bandits_way_distracted = 6
    _mines_punch = 3
    _tower_bullet = 4
    _tower_toss = 4
    _chapel_laugh = 6
    _kitchen_prep = 3
    _ship_beckon = 4
    _dojo_challenge = 4
    _statue_intro = 4
    _statue_peck = 3
    _statue_flustered = 2
    _keep_challenge = 4
    _keep_summon = 4
    _chandelier_challenge = 4
    _factory_pierce = 3
    _endgame_challenge = 4


class JinxCloneHenchman(HenchmanNPC):
    """Jinx clone henchman NPC for boss fights."""

    _base = JINX_1
    _recoil = 2
    _mines_punch = 3
    _tower_bullet = 4
    _tower_toss = 3
    _kitchen_prep = 3
    _ship_beckon = 3
    _dojo_challenge = 3
    _statue_intro = 5
    _statue_flustered = 2
    _keep_challenge = 5
    _keep_summon = 4
    _chandelier_challenge = 5
    _factory_pierce = 3
    _endgame_challenge = 5


class DingalingHenchman(HenchmanNPC):
    """Ding-a-ling henchman NPC for boss fights."""

    _base = DINGALING_GRIDPLANE_NPC


class MadMalletHenchman(HenchmanNPC):
    """Mad Mallet henchman NPC for boss fights."""

    _base = MAD_MALLET_NPC
    _recoil = 2
    _mines_punch = 5
    _tower_bullet = 5
    _tower_toss = 5
    _kitchen_prep = 3
    _ship_beckon = 3
    _dojo_challenge = 3
    _statue_peck = 3
    _statue_flustered = 2
    _keep_challenge = 3
    _keep_summon = 5
    _chandelier_challenge = 3
    _factory_pierce = 3
    _endgame_challenge = 3


class PounderHenchman(HenchmanNPC):
    """Pounder henchman NPC for boss fights."""

    _base = POUNDER_NPC
    _recoil = 2
    _mines_punch = 5
    _tower_bullet = 5
    _tower_toss = 5
    _kitchen_prep = 3
    _ship_beckon = 3
    _dojo_challenge = 3
    _statue_peck = 3
    _statue_flustered = 2
    _keep_challenge = 3
    _keep_summon = 5
    _chandelier_challenge = 3
    _factory_pierce = 3
    _endgame_challenge = 3


class PoundetteHenchman(HenchmanNPC):
    """Poundette henchman NPC for boss fights."""

    _base = POUNDETTE_NPC
    _recoil = 2
    _mines_punch = 5
    _tower_bullet = 5
    _tower_toss = 5
    _kitchen_prep = 3
    _ship_beckon = 3
    _dojo_challenge = 3
    _statue_peck = 3
    _statue_flustered = 2
    _keep_challenge = 3
    _keep_summon = 5
    _chandelier_challenge = 3
    _factory_pierce = 3
    _endgame_challenge = 3


class AeroHenchman(HenchmanNPC):
    """Aero henchman NPC for boss fights."""

    _base = AERO_NPC
    _recoil = 2
    _mines_punch = 3
    _tower_bullet = 3
    _tower_toss = 3
    _kitchen_prep = 3
    _ship_beckon = 3
    _dojo_challenge = 3
    _statue_flustered = 2
    _keep_challenge = 3
    _keep_summon = 3
    _chandelier_challenge = 3
    _factory_pierce = 3
    _endgame_challenge = 3
