from typing import Sequence

from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import (
    SOUTHEAST,
    SOUTHWEST,
    NORTHEAST,
    NORTHWEST,
)
from ...types.physical_objects import (
    BossNPC,
    PixelShift,
    SpriteAnimation,
    SpriteAnimationCollection,
)
from ..rooms.npcs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments.sequence_speeds import (
    FAST,
)

croco_bag_loop = SpriteAnimation(sequence_id=5, total_duration=104)
croco_bag_hit = SpriteAnimation(sequence_id=4, contact_frame=152, total_duration=158)
croco_bag_summon = SpriteAnimation(sequence_id=6, total_duration=136)
croco_recoil = SpriteAnimation(sequence_id=2, total_duration=16)
mack_hit = SpriteAnimation(sequence_id=4, contact_frame=22, total_duration=28)
mack_hit_fast = SpriteAnimation(
    sequence_id=4, contact_frame=13, total_duration=16, speed=FAST
)
mack_challenge = SpriteAnimation(sequence_id=2, total_duration=12)

# Booster animations
booster_laugh = SpriteAnimation(sequence_id=2, total_duration=20, contact_frame=20)
booster_jump = SpriteAnimation(sequence_id=4)
booster_recoil = SpriteAnimation(sequence_id=2, total_duration=16)
booster_cry = SpriteAnimation(sequence_id=13, total_duration=20)

# Johnny animations
small_johnny_sit = SpriteAnimation(sequence_id=10)

# Valentina animations
valentina_stand = SpriteAnimation(sequence_id=10)
valentina_laugh = SpriteAnimation(sequence_id=2)
valentina_hit = SpriteAnimation(sequence_id=3, contact_frame=18, total_duration=28)
valentina_taunt = SpriteAnimation(sequence_id=4, total_duration=58)
valentina_recoil = SpriteAnimation(sequence_id=2, total_duration=34)

# Magikoopa animations
small_magikoopa_hit = SpriteAnimation(
    sequence_id=10, contact_frame=44, total_duration=72
)

# Shovel Knight animations
shovelknight_tile = SpriteAnimation(sequence_id=2)
shovelknight_tapping = SpriteAnimation(sequence_id=3)

# Belome animations
belome_attack = SpriteAnimation(sequence_id=3, contact_frame=36, total_duration=48)
belome_attack_fast = SpriteAnimation(
    sequence_id=3, contact_frame=18, total_duration=24, speed=FAST
)
belome_wiggle = SpriteAnimation(sequence_id=4, total_duration=66)
belome_recoil = SpriteAnimation(sequence_id=2, total_duration=14)

# Boomer animations
boomer_alt_taunt = SpriteAnimation(sequence_id=1, total_duration=16)

# Terrapin animations
jagger_recoil = SpriteAnimation(sequence_id=2, total_duration=18)
jagger_look = SpriteAnimation(sequence_id=8)
jagger_punch = SpriteAnimation(sequence_id=4, contact_frame=54, total_duration=74)
jagger_taunt = SpriteAnimation(sequence_id=3, contact_frame=18, total_duration=38)

# Piranha Plant animations
piranha_taunt = SpriteAnimation(sequence_id=4, total_duration=16)
piranha_bite = SpriteAnimation(sequence_id=3, contact_frame=20, total_duration=52)
piranha_recoil = SpriteAnimation(sequence_id=2, total_duration=20)
piranha_chillin = SpriteAnimation(sequence_id=7, total_duration=16)

# Bloober animations
squid_recoil = SpriteAnimation(sequence_id=2, total_duration=16)
squid_hit = SpriteAnimation(sequence_id=3, contact_frame=36, total_duration=48)
squid_hit_fast = SpriteAnimation(
    sequence_id=3, contact_frame=18, total_duration=24, speed=FAST
)
squid_default = SpriteAnimation(sequence_id=0, total_duration=36)

# Jinx animations
jinx_punch = SpriteAnimation(sequence_id=3, contact_frame=10, total_duration=18)
jinx_recoil = SpriteAnimation(sequence_id=2, total_duration=16)

punchinello_hit = SpriteAnimation(sequence_id=3, contact_frame=24, total_duration=34)
punchinello_hit_fast = SpriteAnimation(sequence_id=3, contact_frame=16, total_duration=23, speed=FAST)
punchinello_cast = SpriteAnimation(sequence_id=4, contact_frame=46, total_duration=54)
punchinello_recoil = SpriteAnimation(sequence_id=2, total_duration=14)
punchinello_animations = SpriteAnimationCollection(
    recoil= punchinello_recoil,
    mines_punch= punchinello_hit,
    ship_beckon=punchinello_cast,
    dojo_challenge=punchinello_cast,
    statue_intro=punchinello_cast,
    statue_peck=punchinello_hit_fast,
    statue_flustered= punchinello_recoil,
    keep_challenge=punchinello_cast,
    keep_summon=punchinello_cast,
    chandelier_challenge=punchinello_cast,
    endgame_challenge=punchinello_cast
)
class HammerBroLargeObject(BossNPC):
    """Hammer Bro object in Mushroom Way Area 03."""

    _base = HAMMER_BRO_NPC


class HammerBroSmallObject(BossNPC):
    """Small Hammer Bro object in Mushroom Way Area 03."""

    _base = HAMMER_BRO_SMALL_NPC
    _eye_height = 20
    _evil_palette = [
        0x393939, 0xA5A5AD, 0x736B7B, 0xFFFFFF, 0x000010,
        0xF8A8A8, 0xF88888, 0xC80808, 0xD00808, 0xF05858,
        0xC00808, 0xE80808, 0x580000, 0x280000, 0x100000,
    ]


class HammerBroStatueObject(BossNPC):
    """Hammer Bro statue object in Mushroom Way Area 03."""

    _base = HAMMER_BRO_STATUE_NPC


class Croco1Object(BossNPC):
    """Croco 1 object in Mushroom Way Area 03."""

    _base = CROCO_1_NPC
    _eye_height = 16
    _evil_palette = [
        0xBDD6CE, 0x8CC694, 0xF86868, 0xFFFFFF, 0x7B8484,
        0xF85050, 0xF80808, 0xC00000, 0xE80000, 0xD80000,
        0xB00000, 0x800000, 0x700000, 0x580000, 0x181818,
    ]
    _tower_entrance_horizontal_shift = 9
    _animations = SpriteAnimationCollection(
        recoil=croco_recoil,
        tower_crying=croco_bag_loop,
        bandits_way_distracted=croco_bag_loop,
        mines_punch=croco_bag_hit,
        chapel_laugh=croco_bag_loop,
        dojo_challenge=croco_bag_summon,
        statue_flustered=croco_recoil,
        keep_challenge=croco_bag_summon,
        keep_summon=croco_bag_hit,
        chandelier_challenge=croco_bag_summon,
        endgame_challenge=croco_bag_summon,
        tower_toss=croco_bag_hit
    )


class Croco2Object(BossNPC):
    """Croco 2 object in Mushroom Way Area 03."""

    _base = CROCO_2_NPC
    _eye_height = 16
    _evil_palette = [
        0xBDD6CE, 0x8CC694, 0xF86868, 0xFFFFFF, 0x7B8484,
        0xF85050, 0xF80808, 0xC00000, 0xE80000, 0xD80000,
        0xB00000, 0x800000, 0x700000, 0x580000, 0x181818,
    ]
    _tower_entrance_horizontal_shift = 9
    _animations = SpriteAnimationCollection(
        recoil=croco_recoil,
        tower_crying=croco_bag_loop,
        bandits_way_distracted=croco_bag_loop,
        mines_punch=croco_bag_hit,
        chapel_laugh=croco_bag_loop,
        dojo_challenge=croco_bag_summon,
        statue_flustered=croco_recoil,
        keep_challenge=croco_bag_summon,
        keep_summon=croco_bag_hit,
        chandelier_challenge=croco_bag_summon,
        endgame_challenge=croco_bag_summon,
        tower_toss=croco_bag_hit
    )


class CrocoStatueObject(BossNPC):
    """Croco statue object in Mushroom Way Area 03."""

    _base = CROCO_STATUE_NPC
    _facing_shifts = {
        SOUTHWEST: PixelShift(3, 0),
        SOUTHEAST: PixelShift(-3, 0),
    }


class MackSmallObject(BossNPC):
    """Small Mack object in Mushroom Way Area 03."""

    _base = MACK_SMALL_NPC
    _eye_height = 21
    _evil_palette = [
        0x383838, 0x181818, 0x282838, 0x787878, 0x202020,
        0xB0B8A8, 0x181818, 0xF8F8F8, 0x504040, 0x000000,
        0x706878, 0xE8E8E8, 0xE82020, 0xF8F8F8, 0xE01010,
    ]


class MackMediumObject(BossNPC):
    """Medium Mack object in Mushroom Way Area 03."""

    _base = MACK_MEDIUM_NPC


class MackBattleObject(BossNPC):
    """Battle Mack object in Mushroom Way Area 03."""

    _base = MACK_NPC
    _animations = SpriteAnimationCollection(
        mines_punch=mack_hit,
        statue_peck=mack_hit_fast,
        statue_flustered=mack_challenge,
        chandelier_challenge=mack_challenge,
        endgame_challenge=mack_hit,
    )


class MackStatueObject(BossNPC):
    """Mack statue object in Mushroom Way Area 03."""

    _base = MACK_STATUE_NPC


class PandoriteSmallObject(BossNPC):
    """Small Pandorite object in Mushroom Way Area 03."""

    _base = PANDORITE_SMALL_NPC
    _evil_palette = [
        0xFFF7DE, 0xFFFF63, 0xFFEF63, 0x00FFAD, 0xFFEF00,
        0xFFE7B5, 0xF7BD8C, 0xE7A531, 0xF80000, 0xC00000,
        0xEF0000, 0xA00000, 0x089400, 0x085A00, 0x680000,
    ]
    _eye_height = 8
    _crown_height = 1


class PandoriteLargeObject(BossNPC):
    """Large Pandorite object in Mushroom Way Area 03."""

    _base = PANDORITE_NPC


class MimicStatueObject(BossNPC):
    """Mimic statue object in Mushroom Way Area 03."""

    _base = MIMIC_STATUEL_NPC
    _eye_height = 4
    _crown_height = 1


class Belome1SmallObject(BossNPC):
    """Small Belome 1 object in Mushroom Way Area 03."""
    _tower_entrance_horizontal_shift = -4
    _eye_height = 12
    _evil_palette = [
        0xF84848, 0xE00000, 0xF8A8A8, 0x680000, 0xFFFFFF,
        0x181818, 0xFFB510, 0x280000, 0xFFD608, 0xFFFFB5,
        0x5A2100, 0xCE8408, 0xFFD663, 0xF03030, 0x210000,
    ]

    _base = BELOME_SMALL_NPC


belome_animations = SpriteAnimationCollection(
    mines_punch=belome_attack,
    statue_intro=belome_wiggle,
    statue_flustered=belome_recoil,
    statue_peck=belome_attack_fast,
    chandelier_challenge=belome_attack,
    endgame_challenge=belome_attack,
)


class Belome1LargeObject(BossNPC):
    """Large Belome 1 object in Mushroom Way Area 03."""

    _base = BELOME_ST_TIME_NPC
    _animations = belome_animations
    _evil_palette = [
        0xFFFFFF, 0xF8A8A8, 0xFFD663, 0xF84848, 0xFFB510,
        0xFFFFB5, 0xFFD608, 0xE00000, 0xCE8408, 0x5A2100,
        0xF03030, 0x680000, 0x280000, 0x210000, 0x181818,
    ]


class Belome2SmallObject(BossNPC):
    """Small Belome 2 object in Mushroom Way Area 03."""

    _base = BELOME_2_SMALL_NPC
    _tower_entrance_horizontal_shift = -4
    _eye_height = 12
    _evil_palette = [
        0xF84848, 0xE00000, 0xF8A8A8, 0x680000, 0xFFFFFF,
        0x181818, 0xFFB510, 0x280000, 0xFFD608, 0xFFFFB5,
        0x5A2100, 0xCE8408, 0xFFD663, 0xF03030, 0x210000,
    ]


class Belome2LargeObject(BossNPC):
    """Large Belome 2 object in Mushroom Way Area 03."""

    _base = GOLDEN_BELOME_NPC
    _animations = belome_animations
    _evil_palette = [
        0xFFFFFF, 0xF8A8A8, 0xFFD663, 0xF84848, 0xFFB510,
        0xFFFFB5, 0xF84848, 0xE00000, 0xCE8408, 0xF03030,
        0xF03030, 0x680000, 0x280000, 0xCE8408, 0x210000,
    ]


class Belome3SmallObject(BossNPC):
    """Small Belome 3 object in Mushroom Way Area 03."""

    _base = BELOME_3_SMALL_NPC
    _tower_entrance_horizontal_shift = -4
    _eye_height = 12
    _evil_palette = [
        0xF84848, 0xE00000, 0xF8A8A8, 0x680000, 0xFFFFFF,
        0x181818, 0xFFB510, 0x280000, 0xFFD608, 0xFFFFB5,
        0x5A2100, 0xCE8408, 0xFFD663, 0xF03030, 0x210000,
    ]


class Belome3LargeObject(BossNPC):
    """Large Belome 3 object in Mushroom Way Area 03."""

    _base = BELOME_3_LARGE_2_NPC
    _animations = belome_animations
    _evil_palette = [
        0xFFFFFF, 0xF8A8A8, 0xF84848, 0xFFB510, 0xF84848,
        0xFFFFB5, 0xFFFFB5, 0xE00000, 0xCE8408, 0x5A2100,
        0xCE8408, 0x680000, 0x280000, 0x210000, 0x280000,
    ]


class BelomeSmallStatueObject(BossNPC):
    """Small Belome statue object in Mushroom Way Area 03."""
    _facing_shifts = {
        SOUTHWEST: PixelShift(3, 2),
        SOUTHEAST: PixelShift(-3, 2),
    }

    _base = BELOME_SMALL_STATUE
    _evil_palette = [
        0xF84848, 0xFFD608, 0xF8A8A8, 0x5A2100, 0xFFFFFF,
        0x181818, 0xF84848, 0x280000, 0xF84848, 0xF8A8A8,
        0x5A2100, 0xE00000, 0xF84848, 0x5A2100, 0x210000,
    ]


class BowyerSmallObject(BossNPC):
    """Small Bowyer object in Mushroom Way Area 03."""

    _base = BOWYER_SMALL_NPC
    _eye_height = 16
    _evil_palette = [
        0x303030, 0x181818, 0x101010, 0x000000, 0x000018,
        0xA00000, 0xF80000, 0x401010, 0xFFFFFF, 0xBDBDCE,
        0x7B1842, 0x6B7363, 0xFF73E7, 0xF80000, 0xA80000,
    ]


class BowyerStatueObject(BossNPC):
    """Bowyer statue object in Mushroom Way Area 03."""

    _base = BOWYER_STATUE_NPC


class BowyerLargeObject(BossNPC):
    """Large Bowyer object in Mushroom Way Area 03."""

    _base = BOWYER_NPC_BATTLE


# Punchinello
class PunchinelloSmallObject(BossNPC):
    """Small Punchinello object."""

    _base = PUNCHINELLO_SMALL_NPC
    _evil_palette = [
        0x181818, 0x101010, 0x000000, 0xA81818, 0xF80000,
        0x480000, 0x580000, 0x808068, 0xFFFFFF, 0xD0D8C0,
        0xB5B58C, 0xF7EF63, 0x9C6300, 0x303030, 0x000000,
    ]


class PunchinelloLargeObject(BossNPC):
    """Large Punchinello object."""

    _base = PUNCHINELLO_NPC
    _animations=punchinello_animations
    _evil_palette = [
        0xFFFFFF, 0xF7EF63, 0xD0D8C0, 0xB5B58C, 0x808068,
        0xF80000, 0x9C6300, 0x303030, 0x480000, 0x480000,
        0x181818, 0xA81818, 0x101010, 0x580000, 0x000000,
    ]


class Punchinello2LargeObject(BossNPC):
    """Large Punchinello object."""

    _base = PUNCHINELLO_POSTGAME_2_NPC
    _animations=punchinello_animations
    _evil_palette = [
        0xFFFFFF, 0xF7EF63, 0xD0D8C0, 0xB5B58C, 0x808068,
        0xF80000, 0x9C6300, 0x303030, 0x480000, 0x480000,
        0x181818, 0xA81818, 0x101010, 0x580000, 0x000000,
    ]


# Dodo
class DodoSmallObject(BossNPC):
    """Small Dodo object."""

    _base = DODO_SMALL_NPC
    _eye_height = 16
    _evil_palette = [
        0x181818, 0xF8F828, 0x4A524A, 0xC8A008, 0x883800,
        0x8C8C8C, 0xE7DEDE, 0xFFFFFF, 0x737373, 0xADADAD,
        0x292910, 0xE00808, 0x800008, 0xFFFFFF, 0x480000,
    ]


class DodoLargeObject(BossNPC):
    """Large Dodo object."""

    _base = DODO_NPC


# Birdetta
class BirdettaSmallObject(BossNPC):
    """Small Birdetta object."""

    _base = BIRDETTA_SMALL_NPC
    _eye_height = 6
    _evil_palette = [
        0xA85818, 0xF87820, 0x002000, 0x005000, 0x007038,
        0x000000, 0x00F8C8, 0x181818, 0x00D058, 0x00F858,
        0xF8F8F8, 0x00A048, 0x909090, 0x484848, 0x806060,
    ]


class BirdettaLargeObject(BossNPC):
    """Large Birdetta object."""

    _base = BIRDETTA_NPC
    _animations = SpriteAnimationCollection(
        statue_intro=SpriteAnimation(sequence_id=4),
        statue_peck=SpriteAnimation(sequence_id=3, contact_frame=20, total_duration=25, speed=FAST),
        statue_flustered=SpriteAnimation(sequence_id=2, total_duration=18)
    )


# Czar Dragon
class CzarDragonSmallObject(BossNPC):
    """Small Czar Dragon object."""

    _base = CZAR_DRAGON_SMALL_NPC
    _eye_height = 3
    _evil_palette = [
        0xF0F8F8, 0x00B0B8, 0x88F8F8, 0x002828, 0x08C8C8, 
        0x007070, 0x40F0F0, 0x009090, 0x003838, 0x08C8C8,
        0x002828, 0x003030, 0x009090, 0x006868, 0x003838
    ]


class CzarDragonMediumObject(BossNPC):
    """Medium Czar Dragon object."""

    _base = CZAR_DRAGON_BODY_NPC


class CzarDragonLargeObject(BossNPC):
    """Large Czar Dragon object."""

    _base = CZAR_DRAGON_NPC


# Boomer
class BoomerSmallObject(BossNPC):
    """Small Boomer object."""

    _base = BOOMER_SMALL_NPC
    _evil_palette = [
        0x000078, 0x423131, 0x1000BD, 0x9C8C8C, 0x000021,
        0x100808, 0x6B636B, 0x4284CE, 0x212121, 0x635A39,
        0x2929F7, 0xEFC6C6, 0xFFFFFF, 0x000000, 0x000000,
    ]


class BoomerLargeObject(BossNPC):
    """Large Boomer object."""

    _base = BOOMER_NPC


# Exor
class ExorSmallObject(BossNPC):
    """Small Exor object."""

    _base = EXOR_SMALL_NPC
    _evil_palette = [
        0xF8C0C0, 0xF86868, 0xC00000, 0xF80000, 0xD80000,
        0x000000, 0xB80000, 0xF80000, 0xF85050, 0xC00000,
        0x980000, 0x480000, 0xF88080, 0xB00000, 0xD00000
    ]


# Domino
class DominoSmallObject(BossNPC):
    """Small Domino object."""

    _base = DOMINO_SMALL_NPC
    _eye_height = 12
    _evil_palette = [
        0xF7E710, 0x52FFBD, 0x9C734A, 0xFFFF94, 0xFFFFDE,
        0x089431, 0x001000, 0xC80808, 0xA00808, 0xE80808,
        0x680000, 0xC80808, 0xF02828, 0x392908, 0x181818,
    ]


# Cloaker
class CloakerLargeObject(BossNPC):
    """Large Cloaker object."""

    _base = CLOAKER_ST_TIME_NPC


# Smithy
class SmithySmallObject(BossNPC):
    """Small Smithy object."""

    _base = SMITHY_SMALL_NPC
    _eye_height = 14
    _tower_entrance_horizontal_shift = -4
    _evil_palette = [
        0x080000, 0x7B848C, 0xF80000, 0x391008, 0x212121,
        0x6B6B63, 0xA80000, 0x525A6B, 0xFFFFFF, 0xBDBDAD,
        0xA81010, 0xCEEFFF, 0x4A4A42, 0x000000, 0x000000,
    ]


class SmithyLargeObject(BossNPC):
    """Large Smithy object."""

    _base = SMITHY_LOWER_NPC


# Culex
class CulexSmallObject(BossNPC):
    """Small Culex object."""

    _base = CULEX_SMALL_NPC
    _eye_height = 11
    _evil_palette = [
        0x180808, 0x585858, 0x383838, 0x101010, 0xC69C4A,
        0xFFD66B, 0x000000, 0x9C2918, 0x522110, 0xBD6329,
        0xF81818, 0x380000, 0xA80000, 0x780000, 0xF8A8A8,
    ]


class CulexLargeObject(BossNPC):
    """Large Culex object."""

    _base = CULEX_NPC
    _evil_palette = [
        0x180808, 0x585858, 0x383838, 0x101010, 0xC69C4A,
        0xFFD66B, 0x000000, 0x9C2918, 0x522110, 0xBD6329,
        0xF81818, 0x380000, 0xA80000, 0x780000, 0xF8A8A8,
    ]


# Bundt
class BundtSmallObject(BossNPC):
    """Small Bundt object."""

    _base = BUNDT_OBJECT_NPC
    _eye_height = 8
    _evil_palette = [
        0xFFFFFF, 0xF8B8B8, 0xF85050, 0xF88080, 0xF80000,
        0xF83030, 0xF80808, 0xF80000, 0xB80000, 0xF80000,
        0x700000, 0xC80000, 0x480000, 0xF88888, 0x300000,
    ]


class BundtLargeObject(BossNPC):
    """Large Bundt object."""

    _base = BUNDT_NPC
    _evil_palette = [
        0xFFFFFF, 0xF85050, 0xF88080, 0xF88080, 0xF88080,
        0xF83030, 0xB80000, 0xB80000, 0xB80000, 0x700000,
        0x700000, 0xC80000, 0x480000, 0xF85050, 0x300000,
    ]


class Bundt2LargeObject(BossNPC):
    """Large Bundt object."""

    _base = BUNDT_2_LARGE_2_NPC
    _evil_palette = [
        0xFFFFFF, 0xF85050, 0xF88080, 0xF88080, 0xF88080,
        0xF83030, 0xB80000, 0xB80000, 0xB80000, 0x700000,
        0x700000, 0xC80000, 0x480000, 0xF85050, 0x300000,
    ]


# Johnny (Jonathan Jones)
class JohnnySmallObject(BossNPC):
    """Small Johnny object."""

    _base = JONATHAN_JONES_NPC_2
    _eye_height = 20
    _animations = SpriteAnimationCollection(
        bandits_way_distracted=small_johnny_sit,
        tower_crying=small_johnny_sit,
        chapel_laugh=small_johnny_sit,
        ship_beckon=small_johnny_sit,
        ship_chair=small_johnny_sit,
        statue_intro=small_johnny_sit,
        dojo_challenge=small_johnny_sit,
        keep_challenge=small_johnny_sit,
        chandelier_challenge=small_johnny_sit,
        endgame_challenge=small_johnny_sit,
    )
    _evil_palette = [
        0xFFFFFF, 0xEFFF42, 0xFFCE94, 0xA59442, 0xB55A39,
        0x7B3118, 0x524A21, 0x423939, 0x6B3921, 0xA50000,
        0x310010, 0x5A634A, 0x422921, 0x5A0000, 0x181818,
    ]


class JohnnyLargeObject(BossNPC):
    """Large Johnny object."""

    _base = JOHNNY_NPC
    _evil_palette = [
        0xFFFFFF, 0x7B3118, 0xEFFF42, 0x524A21, 0x423939,
        0xFFCE94, 0xA59442, 0xB55A39, 0xA50000, 0x5A634A,
        0x310010, 0xA59442, 0xB55A39, 0x5A0000, 0x181818,
    ]


class Johnny2LargeObject(BossNPC):
    """Large Johnny object."""

    _base = JOHNNY_2_LARGE_2_NPC
    _evil_palette = [
        0xFFFFFF, 0x7B3118, 0xEFFF42, 0x524A21, 0x423939,
        0xFFCE94, 0xA59442, 0xB55A39, 0xA50000, 0x5A634A,
        0x310010, 0xA59442, 0xB55A39, 0x5A0000, 0x181818,
    ]


# Valentina
class ValentinaSmallObject(BossNPC):
    """Small Valentina object."""

    _base = VALENTINA_NPC_2
    _eye_height = 16
    _evil_palette = [
        0xF8F8F8, 0xF87800, 0xB84800, 0xF81010, 0xA00000,
        0x500000, 0x70F8F8, 0xF8B0D8, 0xB06880, 0xC0B880,
        0x807050, 0x584828, 0x282828, 0x000000, 0x181818
    ]
    _animations = SpriteAnimationCollection(
        bandits_way_distracted=valentina_stand,
        tower_crying=valentina_stand,
        chapel_laugh=valentina_laugh,
        ship_beckon=valentina_laugh,
        ship_chair=valentina_stand,
        dojo_challenge=valentina_laugh,
        statue_intro=valentina_laugh,
        keep_challenge=valentina_laugh,
        keep_summon=valentina_laugh,
        chandelier_challenge=valentina_laugh,
        endgame_challenge=valentina_laugh,
        look_at_ceiling_mold_id=8,
        look_at_ceiling=SpriteAnimation(sequence_id=10)
    )


class ValentinaLargeObject(BossNPC):
    """Large Valentina object."""

    _base = VALENTINA_NPC


# Knife Guy
class KnifeGuySmallObject(BossNPC):
    """Small Knife Guy object."""

    _base = KNIFE_GUY_JUGGLER_STILL_RED_BALLS_NPC


class KnifeGuyLargeObject(BossNPC):
    """Large Knife Guy object."""

    _base = KNIFE_GUY_NPC


# Grate Guy
class GrateGuySmallObject(BossNPC):
    """Small Grate Guy object."""

    _base = GRATE_GUY_FROM_CASINO_NPC
    _eye_height = 16
    _evil_palette = [
        0xFFFFFF, 0xADBDAD, 0x8C8484, 0x6B5263, 0xF8F8F8,
        0xB8B8B8, 0x888888, 0x484848, 0x101010, 0xF80000,
        0xE80000, 0xC00000, 0x800000, 0x380000, 0x181818,
    ]


class GrateGuyLargeObject(BossNPC):
    """Large Grate Guy object."""

    _base = GRATE_GUY_NPC


# Mokura
class MokuraLargeObject(BossNPC):
    """Large Mokura object."""

    _base = MOKURA_NPC


class MokuraSmallObject(BossNPC):
    """Small Mokura object."""

    _base = MOKURA_S_CLOUD_BLUE_NPC_2
    _eye_height = 4
    _crown_height = 1
    _evil_palette = [
        0xF8F0F0, 0xF8D8D8, 0xF8C0C0, 0xF8A8A8, 0xF88888,
        0xF87070, 0xF85050, 0xF82020, 0xF82020, 0xF80000,
        0xE00000, 0x000000, 0x000000, 0x000000, 0x300000,
    ]


# Yaridovich
class YaridovichLargeObject(BossNPC):
    """Large Yaridovich object."""

    _base = YARIDOVICH_NPC


# Missing Small/Medium Classes


class MagikoopaSmallObject(BossNPC):
    """Small Magikoopa object."""

    _base = RED_MAGIKOOPA_NPC
    _animations = SpriteAnimationCollection(
        mines_punch=small_magikoopa_hit,
        ship_beckon=small_magikoopa_hit,
        dojo_challenge=small_magikoopa_hit,
        keep_challenge=small_magikoopa_hit,
        keep_summon=small_magikoopa_hit,
        chandelier_challenge=small_magikoopa_hit,
        endgame_challenge=small_magikoopa_hit,
        tower_toss=small_magikoopa_hit
    )
    _evil_palette = [
        0xFFFFFF, 0xB59C9C, 0x7B5A63, 0xB56329, 0xC60029,
        0x8C0029, 0x5A0018, 0x310042, 0x00FF00, 0xFFFF00,
        0xFFB500, 0x8C3900, 0xDE0800, 0x4A1000, 0x181818,
    ]


class ClerkSmallObject(BossNPC):
    """Small Clerk object."""

    _base = FACTORY_CLERK_GREEN_NPC_2
    _eye_height = 10
    _animations = SpriteAnimationCollection(
        bandits_way_distracted=shovelknight_tapping,
        tower_crying=shovelknight_tapping,
        chapel_laugh=shovelknight_tapping,
        ship_chair=shovelknight_tapping,
        dojo_challenge=shovelknight_tile,
        keep_challenge=shovelknight_tile,
        keep_summon=shovelknight_tile,
        chandelier_challenge=shovelknight_tile,
        endgame_challenge=shovelknight_tile,
        look_at_ceiling_mold_id=1,
        tower_toss=shovelknight_tile,
        look_at_ceiling=SpriteAnimation(sequence_id=2)
    )
    _evil_palette = [
        0xE7EFEF, 0xBDC6CE, 0x9C9C9C, 0x736B6B, 0x525252,
        0x424242, 0x313131, 0x383838, 0x181818, 0xF81818,
        0xC00000, 0x980000, 0x312118, 0x300000, 0x101010,
    ]


class ManagerSmallObject(BossNPC):
    """Small Manager object."""

    _base = FACTORY_MANAGER_BLUE_NPC
    _eye_height = 10
    _animations = SpriteAnimationCollection(
        bandits_way_distracted=shovelknight_tapping,
        tower_crying=shovelknight_tapping,
        chapel_laugh=shovelknight_tapping,
        ship_chair=shovelknight_tapping,
        dojo_challenge=shovelknight_tile,
        keep_challenge=shovelknight_tile,
        keep_summon=shovelknight_tile,
        chandelier_challenge=shovelknight_tile,
        endgame_challenge=shovelknight_tile,
        look_at_ceiling_mold_id=1,
        tower_toss=shovelknight_tile,
        look_at_ceiling=SpriteAnimation(sequence_id=2)
    )
    _evil_palette = [
        0xE7EFEF, 0xBDC6CE, 0x9C9C9C, 0x736B6B, 0x525252,
        0x424242, 0x313131, 0x383838, 0x181818, 0xF81818,
        0xC00000, 0x980000, 0x312118, 0x300000, 0x101010,
    ]


class DirectorSmallObject(BossNPC):
    """Small Director object."""

    _base = FACTORY_DIRECTOR_RED_NPC
    _eye_height = 10
    _animations = SpriteAnimationCollection(
        bandits_way_distracted=shovelknight_tapping,
        tower_crying=shovelknight_tapping,
        chapel_laugh=shovelknight_tapping,
        ship_chair=shovelknight_tapping,
        dojo_challenge=shovelknight_tile,
        keep_challenge=shovelknight_tile,
        keep_summon=shovelknight_tile,
        chandelier_challenge=shovelknight_tile,
        endgame_challenge=shovelknight_tile,
        look_at_ceiling_mold_id=1,
        tower_toss=shovelknight_tile,
        look_at_ceiling=SpriteAnimation(sequence_id=2)
    )
    _evil_palette = [
        0xE7EFEF, 0xBDC6CE, 0x9C9C9C, 0x736B6B, 0x525252,
        0x424242, 0x313131, 0x383838, 0x181818, 0xF81818,
        0xC00000, 0x980000, 0x312118, 0x300000, 0x101010,
    ]


class HidonSmallObject(BossNPC):
    """Small Hidon object."""

    _base = HIDON_SMALL_NPC
    _eye_height = 8
    _crown_height = 1
    _evil_palette = [
        0xFFF7DE, 0xFFFF63, 0xFFEF63, 0x00FFAD, 0xFFEF00,
        0xFFE7B5, 0xF7BD8C, 0xE7A531, 0xF80000, 0xC00000,
        0xEF0000, 0xA00000, 0x089400, 0x085A00, 0x680000,
    ]


class ChesterSmallObject(BossNPC):
    """Small Chester object."""

    _base = CHESTER_SMALL_NPC
    _eye_height = 8
    _crown_height = 1
    _evil_palette = [
        0xFFF7DE, 0xFFFF63, 0xFFEF63, 0x00FFAD, 0xFFEF00,
        0xFFE7B5, 0xF7BD8C, 0xE7A531, 0xF80000, 0xC00000,
        0xEF0000, 0xA00000, 0x089400, 0x085A00, 0x680000,
    ]


class BoxBoySmallObject(BossNPC):
    """Small Box Boy object."""

    _base = BOX_BOY_SMALL_NPC
    _eye_height = 8
    _crown_height = 1
    _evil_palette = [
        0xFFF7DE, 0xFFFF63, 0xFFEF63, 0x00FFAD, 0xFFEF00,
        0xFFE7B5, 0xF7BD8C, 0xE7A531, 0xF80000, 0xC00000,
        0xEF0000, 0xA00000, 0x089400, 0x085A00, 0x680000,
    ]


# Missing Large Classes


class ClerkLargeObject(BossNPC):
    """Large Clerk object."""

    _base = CLERK_LARGE_NPC


class ClerkBattleObject(BossNPC):
    """Battle Clerk object."""

    _base = CLERK_NPC


class ManagerLargeObject(BossNPC):
    """Large Manager object."""

    _base = MANAGER_LARGE_NPC


class ManagerBattleObject(BossNPC):
    """Battle Manager object."""

    _base = MANAGER_NPC


class DirectorBattleObject(BossNPC):
    """Battle Director object."""

    _base = DIRECTOR_NPC


class DirectorLargeObject(BossNPC):
    """Large Director object."""

    _base = DIRECTOR_LARGE_NPC


class HidonLargeObject(BossNPC):
    """Large Hidon object."""

    _base = HIDON_NPC


class ChesterLargeObject(BossNPC):
    """Large Chester object."""

    _base = CHESTER_NPC


class BoxBoyLargeObject(BossNPC):
    """Large Box Boy object."""

    _base = BOX_BOY_NPC


class MagikoopaLargeObject(BossNPC):
    """Large Magikoopa object."""

    _base = MAGIKOOPA_LARGE_NPC


class DominoLargeObject(BossNPC):
    """Large Domino object."""

    _base = DOMINO_LARGE_NPC


class MackLargeObject(BossNPC):
    """Large Mack object."""

    _base = MACK_LARGE_NPC


# Missing Statue Classes


class NimbusLandStatueObject(BossNPC):
    """Nimbus Land statue object."""

    _base = VALENTINA_STATUE_NPC


class BelomeStatueObject(BossNPC):
    """Belome statue object."""

    _base = GOLDEN_BELOME_NPC


class BoosterObject(BossNPC):
    """Booster object."""

    _base = BOOSTER_NPC
    _animations = SpriteAnimationCollection(
        recoil=booster_recoil,
        tower_crying=booster_cry,
        bandits_way_distracted=booster_laugh,
        mines_punch=booster_laugh,
        chapel_laugh=booster_laugh,
        ship_beckon=booster_laugh,
        ship_chair=booster_laugh,
        dojo_challenge=booster_jump,
        statue_intro=booster_laugh,
        statue_flustered=booster_jump,
        keep_challenge=booster_jump,
        keep_summon=booster_laugh,
        chandelier_challenge=booster_jump,
        endgame_challenge=booster_jump,
        tpose_mold_id=12,
        tower_toss=booster_laugh,
        tpose=SpriteAnimation(sequence_id=15, total_duration=16)
    )
    _evil_palette = [
        0xFFFFFF, 0xADADCE, 0xEF5252, 0xC62129, 0x8C0000,
        0x4A0000, 0xF80000, 0x600000, 0x6B8CFF, 0xFFCE94,
        0xB58452, 0x7B5229, 0x393131, 0x5A5273, 0x181818,
    ]


class BoosterStatueObject(BossNPC):
    """Booster statue object."""

    _base = BOOSTER_STATUE_NPC


class JohnnyStatueObject(BossNPC):
    """Johnny statue object."""

    _base = JOHNNY_STATUE_NPC


class MagikoopaStatueObject(BossNPC):
    """Magikoopa statue object."""

    _base = MAGIKOOPA_STATUE_NPC
    _facing_shifts = {
        SOUTHEAST: PixelShift(2, 0),
        NORTHWEST: PixelShift(-3, 0),
        NORTHEAST: PixelShift(3, 0),
    }


class ValentinaStatueObject(BossNPC):
    """Valentina statue object."""

    _base = VALENTINA_STATUE_NPC
    _facing_shifts = {
        SOUTHEAST: PixelShift(-3, 0),
        NORTHWEST: PixelShift(-3, 0),
        NORTHEAST: PixelShift(-3, 0),
    }


class ShovelKnightStatueObject(BossNPC):
    """Shovel Knight statue object (Clerk/Manager/Director)."""

    _base = SHOVEL_KNIGHT_STATUE_NPC
    _facing_shifts = {
        SOUTHWEST: PixelShift(3, 0),
        SOUTHEAST: PixelShift(-3, 0),
        NORTHWEST: PixelShift(5, 0),
        NORTHEAST: PixelShift(5, 0),
    }


class YaridovichStatueObject(BossNPC):
    """Yaridovich statue object."""

    _base = YARIDOVICH_STATUE_NPC


class GrateGuyStatueObject(BossNPC):
    """Grate Guy statue object."""

    _base = GRATE_GUY_STATUE_NPC
    _facing_shifts = {
        NORTHEAST: PixelShift(-5, 0),
        NORTHWEST: PixelShift(-2, 0),
        SOUTHEAST: PixelShift(-5, 0),
    }


class JinxStatueObject(BossNPC):
    """Jinx statue object."""

    _base = JINX_STATUE_NPC
    _facing_shifts = {
        NORTHEAST: PixelShift(-2, -1),
        NORTHWEST: PixelShift(3, -1),
        SOUTHEAST: PixelShift(-2, -2),
    }


class MokuraStatueObject(BossNPC):
    """Mokura statue object."""

    _base = MOKURA_STATUE_NPC


class TerrapinObject(BossNPC):
    """Terrapin object."""

    _base = TERRAPIN_NPC
    _animations = SpriteAnimationCollection(
        bandits_way_distracted=jagger_look,
        tower_crying=jagger_look,
        mines_punch=jagger_punch,
        chapel_laugh=jagger_look,
        ship_beckon=jagger_taunt,
        dojo_challenge=jagger_punch,
        statue_intro=jagger_look,
        statue_peck=jagger_taunt,
        statue_flustered=jagger_recoil,
        keep_challenge=jagger_punch,
        keep_summon=jagger_punch,
        chandelier_challenge=jagger_punch,
        endgame_challenge=jagger_punch,
        look_at_ceiling_mold_id=6,
        tower_toss=jagger_punch,
        look_at_ceiling=SpriteAnimation(sequence_id=6),
        look_at_camera=SpriteAnimation(sequence_id=6)
    )
    _evil_palette = [
        0xFFFFFF, 0xFFEF73, 0xC69431, 0x734A08, 0x423910,
        0xDE845A, 0xB51839, 0x5A0000, 0x290000, 0xE7E7EF,
        0xBDBDC6, 0x73737B, 0x4A4242, 0x312939, 0x181818,
    ]


class TerrapinStatueObject(BossNPC):
    """Terrapin statue object."""

    _base = TERRAPIN_STATUE_NPC


class PiranhaPlantObject(BossNPC):
    """Piranha Plant object."""

    _base = PIRANHA_PLANT_NPC_3
    _eye_height = 14
    _animations = SpriteAnimationCollection(
        recoil=piranha_recoil,
        bandits_way_distracted=piranha_taunt,
        mines_punch=piranha_bite,
        chapel_laugh=piranha_chillin,
        ship_beckon=piranha_taunt,
        dojo_challenge=piranha_bite,
        statue_intro=piranha_bite,
        statue_peck=piranha_bite,
        statue_flustered=piranha_recoil,
        keep_challenge=piranha_bite,
        keep_summon=piranha_bite,
        chandelier_challenge=piranha_bite,
        endgame_challenge=piranha_bite,
        tpose_mold_id=3,
        tower_toss=piranha_bite,
        tpose=SpriteAnimation(sequence_id=6, total_duration=16)
    )
    _evil_palette = [
        0xFFFFFF, 0xD6D6D6, 0xA5A5AD, 0x7B7B73, 0x636B63,
        0x4A4A4A, 0x212929, 0x008400, 0x003900, 0xFF00FF,
        0xC600C6, 0x730073, 0x290029, 0x00D600, 0x181818,
    ]


class PiranhaPlantStatueObject(BossNPC):
    """Piranha Plant statue object."""

    _base = PIRANHA_PLANT_STATUE_NPC


class MegasmilaxLargeObject(BossNPC):
    """Large Megasmilax object."""

    _base = MEGASMILAX_NPC


class BlooberObject(BossNPC):
    """Bloober object."""

    _base = BLOOBER_NPC
    _eye_height = 10
    _animations = SpriteAnimationCollection(
        tower_bullet=squid_hit,
        recoil=squid_recoil,
        mines_punch=squid_hit,
        dojo_challenge=squid_hit,
        statue_peck=squid_hit_fast,
        statue_flustered=squid_recoil,
        keep_challenge=squid_hit,
        keep_summon=squid_hit,
        chandelier_challenge=squid_hit,
        endgame_challenge=squid_hit,
        chapel_laugh=squid_default, 
        look_at_ceiling_mold_id=1,
        tpose_mold_id=2,
        tower_toss=squid_hit,
        tpose=SpriteAnimation(sequence_id=5, total_duration=12),
        look_at_ceiling=SpriteAnimation(sequence_id=6)
    )
    _evil_palette = [
        0xF80000, 0xF80000, 0xF00000, 0xF00000, 0xE80000,
        0xE00000, 0xC00000, 0xA00000, 0x900000, 0x780000,
        0x600000, 0x300000, 0x000000, 0x000000, 0x180000,
    ]


class BlooberStatueObject(BossNPC):
    """Bloober statue object."""

    _base = BLOOBER_STATUE_NPC


class FactoryChiefStatueObject(BossNPC):
    """Factory Chief statue object."""

    _base = FACTORY_CHIEF_STATUE_NPC
    _facing_shifts = {
        SOUTHWEST: PixelShift(1, 0),
        SOUTHEAST: PixelShift(-1, 0),
    }


chief_stab = SpriteAnimation(sequence_id=3, contact_frame=26, total_duration=38)
chief_stab_fast = SpriteAnimation(sequence_id=3, contact_frame=13, total_duration=19, speed=FAST)
chief_recoil = SpriteAnimation(sequence_id=2, total_duration=14)
chief_cast = SpriteAnimation(sequence_id=4, total_duration=52, contact_frame=32)

class FactoryChiefObject(BossNPC):
    """Factory Chief object."""

    _base = FACTORY_CHIEF_NPC
    _animations = SpriteAnimationCollection(
        recoil=chief_recoil,
        tower_crying=chief_cast,
        bandits_way_distracted=chief_cast,
        mines_punch=chief_stab,
        chapel_laugh=chief_cast,
        ship_beckon=chief_cast,
        dojo_challenge=chief_stab,
        statue_intro=chief_cast,
        statue_peck=chief_stab_fast,
        statue_flustered=chief_recoil,
        keep_challenge=chief_stab,
        keep_summon=chief_cast,
        chandelier_challenge=chief_stab,
        endgame_challenge=chief_stab,
        look_at_ceiling_mold_id=17,
        tower_toss=chief_cast,
        look_at_ceiling=SpriteAnimation(sequence_id=5)
    )
    _evil_palette = [
        0xADB5AD, 0xFF6329, 0xF74210, 0xAD5A29, 0xFFFFFF,
        0x526352, 0xFF00FF, 0xC61810, 0x941008, 0x293110,
        0x311008, 0x001000, 0x210000, 0x001000, 0x000000,
    ]

red_recoil=SpriteAnimation(sequence_id=2, total_duration=22)
red_attack=SpriteAnimation(sequence_id=8, contact_frame=26, total_duration=66)
red_attack_fast=SpriteAnimation(sequence_id=8, contact_frame=18, total_duration=44, speed=FAST)
red_cast=SpriteAnimation(sequence_id=4, contact_frame=82, total_duration=120)


class AxemRedObject(BossNPC):
    """Axem Red object."""

    _base = AXEM_RED_NPC_2_LOW_VRAM
    _eye_height = 15
    _animations = SpriteAnimationCollection(
        recoil=red_recoil,
        bandits_way_distracted=red_cast,
        mines_punch=red_attack,
        dojo_challenge=red_cast,
        ship_beckon=red_cast,
        statue_intro=red_cast,
        statue_peck=red_attack_fast,
        statue_flustered=red_recoil,
        keep_challenge=red_cast,
        keep_summon=red_cast,
        chandelier_challenge=red_cast,
        endgame_challenge=red_cast,
        tower_toss=red_attack
    )
    _evil_palette = [
        0xFFFFFF, 0xD6D6DE, 0xADADB5, 0x73737B, 0x4A4242,
        0x293131, 0xADADB5, 0x73737B, 0x524A4A, 0x313131,
        0xCECED6, 0x9C9CA5, 0x6B6B73, 0x313139, 0x181818,
    ]


class AxemRedStatueObject(BossNPC):
    """Axem Red statue object."""

    _base = AXEM_RED_STATUE_NPC
    _facing_shifts = {
        SOUTHWEST: PixelShift(-5, 0),
    }


class BundtStatueObject(BossNPC):
    """Bundt statue object."""

    _base = BUNDT_STATUE_NPC
    _facing_shifts = {
        SOUTHWEST: PixelShift(3, 0),
        SOUTHEAST: PixelShift(-3, 0),
    }


class CountDownGridplaneObject(BossNPC):
    """Count Down gridplane object."""

    _base = COUNT_DOWN_GRIDPLANE_NPC
    _eye_height = 6
    _evil_palette = [
        0x2858F8, 0xD06870, 0xE04838, 0x1848F8, 0x484878,
        0xE82008, 0x1028A8, 0x4858C8, 0x000000, 0x382828,
        0x982820, 0x402008, 0xF8A820, 0xF8D820, 0x98A0B0,
    ]


class CountDownStatueObject(BossNPC):
    """Count Down statue object."""

    _base = COUNT_DOWN_STATUE_NPC
    _facing_shifts = {
        SOUTHWEST: PixelShift(-4, -1),
        SOUTHEAST: PixelShift(4, -1),
    }


class PunchinelloStatueObject(BossNPC):
    """Punchinello statue object."""

    _base = PUNCHINELLO_STATUE_NPC


class DodoStatueObject(BossNPC):
    """Dodo statue object."""

    _base = DODO_STATUE_NPC


class BirdettaStatueObject(BossNPC):
    """Birdetta statue object."""

    _base = BIRDETTA_STATUE_NPC


class CzarStatueObject(BossNPC):
    """Czar Dragon statue object."""

    _base = CZAR_DRAGON_STATUE_NPC
    _facing_shifts = {
        SOUTHWEST: PixelShift(-7, 1),
    }


class BoomerStatueObject(BossNPC):
    """Boomer statue object."""

    _base = BOOMER_STATUE_NPC


class ExorStatueObject(BossNPC):
    """Exor statue object."""

    _base = EXOR_STATUE_NPC


class DominoStatueObject(BossNPC):
    """Domino statue object."""

    _base = DOMINO_STATUE_NPC


class SmithyStatueObject(BossNPC):
    """Smithy statue object."""

    _base = SMITHY_STATUE_NPC
    _facing_shifts = {
        SOUTHWEST: PixelShift(8, 0),
        SOUTHEAST: PixelShift(-8, 0),
    }


class CulexStatueObject(BossNPC):
    """Culex statue object."""

    _base = CULEX_STATUE_NPC


class MallowStatueObject(BossNPC):
    """Mallow statue object."""

    _base = MALLOW_STATUE_NPC


class MachineYaridOverworldObject(BossNPC):
    """Machine Made Yaridovich overworld object."""

    _base = MACHINE_YARID_OVERWORLD_NPC


class SmithyBodyOverworldObject(BossNPC):
    """Smithy body overworld object."""

    _base = SMITHY_BODY_OVERWORLD_NPC


class BoomerOverworldObject(BossNPC):
    """Boomer overworld object."""

    _base = BOOMER_RED_NPC
    _animations = SpriteAnimationCollection(
        chandelier_challenge=boomer_alt_taunt, endgame_challenge=boomer_alt_taunt
    )


class YaridovichSmallObject(BossNPC):
    """Small Yaridovich object."""

    _base = SEASIDE_TOWN_FAKE_ELDER_GREEN_NPC
    _eye_height = 10
    _evil_palette = [
        0xFFFFFF, 0xFFCEA5, 0xB57B5A, 0xBD4A42, 0x8C1810,
        0x310800, 0xE79C00, 0xC66B00, 0x943900, 0xCECECE,
        0xADCE94, 0x7B9C42, 0x427300, 0x294A00, 0x181818,
    ]


class YaridOverworldObject(BossNPC):
    """Yaridovich overworld object."""

    _base = YARIDOVICH_OUT_OF_BATTLE_NPC


class BowyerOverworldObject(BossNPC):
    """Bowyer overworld object."""

    _base = BOWYER_NPC_LARGE


# Postgame bosses - Small versions
class Punchinello2SmallObject(BossNPC):
    """Small Punchinello 2 object."""

    _base = PUNCHINELLO_2_SMALL_NPC
    _evil_palette = [
        0x181818, 0x101010, 0x000000, 0xA81818, 0xF80000,
        0x480000, 0x580000, 0x808068, 0xFFFFFF, 0xD0D8C0,
        0xB5B58C, 0xF7EF63, 0x9C6300, 0x303030, 0x000000,
    ]


class Booster2SmallObject(BossNPC):
    """Small Booster 2 object."""

    _base = BOOSTER_2_SMALL_NPC
    _evil_palette = [
        0xFFFFFF, 0xADADCE, 0xEF5252, 0xC62129, 0x8C0000,
        0x4A0000, 0xF80000, 0x600000, 0x6B8CFF, 0xFFCE94,
        0xB58452, 0x7B5229, 0x393131, 0x5A5273, 0x181818,
    ]
    _animations = SpriteAnimationCollection(
        recoil=booster_recoil,
        tower_crying=booster_cry,
        bandits_way_distracted=booster_laugh,
        mines_punch=booster_laugh,
        chapel_laugh=booster_laugh,
        ship_beckon=booster_laugh,
        ship_chair=booster_laugh,
        dojo_challenge=booster_jump,
        statue_intro=booster_laugh,
        statue_flustered=booster_jump,
        keep_challenge=booster_jump,
        keep_summon=booster_laugh,
        chandelier_challenge=booster_jump,
        endgame_challenge=booster_jump,
        tpose_mold_id=12,
        tower_toss=booster_laugh,
        tpose=SpriteAnimation(sequence_id=15, total_duration=16)

    )


class Bundt2SmallObject(BossNPC):
    """Small Bundt 2 object."""

    _base = BUNDT_2_SMALL_NPC
    _eye_height = 8
    _evil_palette = [
        0xFFFFFF, 0xF8B8B8, 0xF85050, 0xF88080, 0xF80000,
        0xF83030, 0xF80808, 0xF80000, 0xB80000, 0xF80000,
        0x700000, 0xC80000, 0x480000, 0xF88888, 0x300000,
    ]


class Johnny2SmallObject(BossNPC):
    """Small Johnny 2 object."""

    _base = JOHNNY_2_SMALL_NPC
    _eye_height = 20
    _animations = SpriteAnimationCollection(
        bandits_way_distracted=small_johnny_sit,
        tower_crying=small_johnny_sit,
        chapel_laugh=small_johnny_sit,
        ship_beckon=small_johnny_sit,
        ship_chair=small_johnny_sit,
        statue_intro=small_johnny_sit,
        dojo_challenge=small_johnny_sit,
        keep_challenge=small_johnny_sit,
        chandelier_challenge=small_johnny_sit,
        endgame_challenge=small_johnny_sit,
    )
    _evil_palette = [
        0xFFFFFF, 0xEFFF42, 0xFFCE94, 0xA59442, 0xB55A39,
        0x7B3118, 0x524A21, 0x423939, 0x6B3921, 0xA50000,
        0x310010, 0x5A634A, 0x422921, 0x5A0000, 0x181818,
    ]


jinx_animations = SpriteAnimationCollection(
    recoil=jinx_recoil,
    mines_punch=jinx_punch,
    ship_beckon=jinx_punch,
    dojo_challenge=jinx_punch,
    statue_intro=jinx_punch,
    statue_peck=jinx_punch,
    keep_challenge=jinx_punch,
    keep_summon=jinx_punch,
    chandelier_challenge=jinx_punch,
    endgame_challenge=jinx_punch,
    tower_toss=jinx_punch
)


class Jinx1SmallObject(BossNPC):
    """Small Jinx 1 object."""

    _base = JINX_1
    _eye_height = 4
    _crown_height = 1
    _animations = jinx_animations
    _evil_palette = [
        0xFFFFFF, 0xE7B56B, 0x9C5242, 0x6B294A, 0x5A1829,
        0xC60000, 0x6B0000, 0x310000, 0xFFFF00, 0xF80000,
        0x480000, 0x181818, 0xE7DEDE, 0x9C8C8C, 0x181818,
    ]


class Jinx2SmallObject(BossNPC):
    """Small Jinx 2 object."""

    _base = JINX_2
    _eye_height = 4
    _crown_height = 1
    _animations = jinx_animations
    _evil_palette = [
        0xFFFFFF, 0xE7B56B, 0x9C5242, 0x6B294A, 0x5A1829,
        0xC60000, 0x6B0000, 0x310000, 0xFFFF00, 0xF80000,
        0x480000, 0x181818, 0xE7DEDE, 0x9C8C8C, 0x181818,
    ]


class Jinx3SmallObject(BossNPC):
    """Small Jinx 3 object."""

    _base = JINX_3
    _eye_height = 4
    _crown_height = 1
    _animations = jinx_animations
    _evil_palette = [
        0xFFFFFF, 0xE7B56B, 0x9C5242, 0x6B294A, 0x5A1829,
        0xC60000, 0x6B0000, 0x310000, 0xFFFF00, 0xF80000,
        0x480000, 0x181818, 0xE7DEDE, 0x9C8C8C, 0x181818,
    ]


class Jinx4SmallObject(BossNPC):
    """Small Jinx 4 object."""

    _base = JINX_4
    _eye_height = 4
    _crown_height = 1
    _animations = jinx_animations
    _evil_palette = [
        0xFFFFFF, 0xE7B56B, 0x9C5242, 0x6B294A, 0x5A1829,
        0xC60000, 0x6B0000, 0x310000, 0xFFFF00, 0xF80000,
        0x480000, 0x181818, 0xE7DEDE, 0x9C8C8C, 0x181818,
    ]


class Culex3DSmallObject(BossNPC):
    """Small Culex 3D object."""

    _base = CULEX_2_SMALL_NPC
    _eye_height = 11
    _evil_palette = [
        0x180808, 0x585858, 0x383838, 0x101010, 0xC69C4A,
        0xFFD66B, 0x000000, 0x9C2918, 0x522110, 0xBD6329,
        0xF81818, 0x380000, 0xA80000, 0x780000, 0xF8A8A8,
    ]
