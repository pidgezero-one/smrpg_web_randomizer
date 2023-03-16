"""Contextual names for frequently used sprite animations that need to be
inserted into overworld scripts depending on boss shuffling."""


from randomizer.types.npcs.animations.classes import SpriteAnimation
from randomizer.types.overworld_scripts.action_scripts.constants.sequence_speeds import (
    FAST,
    FASTEST,
    VERY_FAST,
)

CROCO_BAG_LOOP = SpriteAnimation(sequence_id=5, total_duration=104)
CROCO_BAG_HIT = SpriteAnimation(sequence_id=4, contact_frame=152, total_duration=158)
CROCO_BAG_SUMMON = SpriteAnimation(sequence_id=6, total_duration=136)
CROCO_RECOIL = SpriteAnimation(sequence_id=2, total_duration=16)


BOOSTER_LAUGH = SpriteAnimation(sequence_id=2)
BOOSTER_PUNCH = SpriteAnimation(
    sequence_id=3, contact_frame=74, total_duration=92, new_sprite_id=502
)
BOOSTER_JUMP = SpriteAnimation(sequence_id=4)
BOOSTER_RECOIL = SpriteAnimation(sequence_id=2, total_duration=16)


SMALL_JOHNNY_SIT = SpriteAnimation(sequence_id=10)


VALENTINA_STAND = SpriteAnimation(sequence_id=10)
VALENTINA_LAUGH = SpriteAnimation(sequence_id=2)
VALENTINA_HIT = SpriteAnimation(sequence_id=3, contact_frame=18, total_duration=28)
VALENTINA_TAUNT = SpriteAnimation(sequence_id=4, total_duration=58)
VALENTINA_RECOIL = SpriteAnimation(sequence_id=2, total_duration=34)


SMALL_MAGIKOOPA_HIT = SpriteAnimation(
    sequence_id=10, contact_frame=44, total_duration=72
)


SHOVELKNIGHT_TILE = SpriteAnimation(sequence_id=2)


BELOME_ATTACK = SpriteAnimation(sequence_id=3, contact_frame=36, total_duration=48)
BELOME_ATTACK_FAST = SpriteAnimation(
    sequence_id=3, contact_frame=18, total_duration=24, speed=FAST
)
BELOME_WIGGLE = SpriteAnimation(sequence_id=4, total_duration=66)
BELOME_RECOIL = SpriteAnimation(sequence_id=2, total_duration=14)


BOOMER_ALT_TAUNT = SpriteAnimation(sequence_id=1, total_duration=16)


JINX_PUNCH = SpriteAnimation(sequence_id=3, contact_frame=10, total_duration=18)
JINX_RECOIL = SpriteAnimation(sequence_id=2, total_duration=16)


JAGGER_RECOIL = SpriteAnimation(sequence_id=2, total_duration=18)
JAGGER_LOOK = SpriteAnimation(sequence_id=8)
JAGGER_PUNCH = SpriteAnimation(sequence_id=4, contact_frame=54, total_duration=74)
JAGGER_TAUNT = SpriteAnimation(sequence_id=3, contact_frame=18, total_duration=38)


HAMMER_HIT = SpriteAnimation(sequence_id=3, contact_frame=26, total_duration=36)


CROOK_SCRATCH = SpriteAnimation(sequence_id=4, total_duration=20, contact_frame=10)


PIRANHA_TAUNT = SpriteAnimation(sequence_id=4, total_duration=16)
PIRANHA_BITE = SpriteAnimation(sequence_id=3, contact_frame=20, total_duration=52)
PIRANHA_RECOIL = SpriteAnimation(sequence_id=2, total_duration=20)


SQUID_RECOIL = SpriteAnimation(sequence_id=2, total_duration=16)
SQUID_HIT = SpriteAnimation(sequence_id=3, contact_frame=36, total_duration=48)
SQUID_HIT_FAST = SpriteAnimation(
    sequence_id=3, contact_frame=18, total_duration=24, speed=FAST
)


BANDANA_ATTACK = SpriteAnimation(sequence_id=3, contact_frame=26, total_duration=50)
BANDANA_TAUNT = SpriteAnimation(sequence_id=4, total_duration=36)


BIRD_ATTACK = SpriteAnimation(sequence_id=3, contact_frame=24, total_duration=36)


FIREBALL_SPIN = SpriteAnimation(sequence_id=3, contact_frame=40, total_duration=62)
FIREBALL_RECOIL = SpriteAnimation(sequence_id=2, total_duration=12)
FIREBALL_SPIN_FAST = SpriteAnimation(
    sequence_id=3, contact_frame=20, total_duration=31, speed=FAST
)


PANDORITE_ATTACK = SpriteAnimation(sequence_id=3, contact_frame=70, total_duration=80)
PANDORITE_SHORT = SpriteAnimation(sequence_id=3, contact_frame=8, total_duration=80)
MIMIC_SHAKE = SpriteAnimation(sequence_id=4, total_duration=58)
MIMIC_RECOIL = SpriteAnimation(sequence_id=2, total_duration=12)


BOMB_TICK = SpriteAnimation(sequence_id=4)
BOMB_RECOIL = SpriteAnimation(sequence_id=2, total_duration=16)


HAMMER_BRO_BOP = SpriteAnimation(sequence_id=3, contact_frame=36, total_duration=48)
HAMMER_BRO_BOP_FAST = SpriteAnimation(
    sequence_id=3, contact_frame=16, total_duration=21, speed=FAST
)
HAMMER_BRO_TAUNT = SpriteAnimation(sequence_id=5, total_duration=20)
HAMMER_BRO_RECOIL = SpriteAnimation(sequence_id=2, total_duration=12)


SHOVELKNIGHT_ATTACK = SpriteAnimation(
    sequence_id=3, contact_frame=16, total_duration=22, speed=FAST
)
SHOVELKNIGHT_TAUNT = SpriteAnimation(sequence_id=4, total_duration=44)
SHOVELKNIGHT_RECOIL = SpriteAnimation(sequence_id=2, total_duration=24)
SHOVELKNIGHT_ALT_TAUNT = SpriteAnimation(sequence_id=5)


BOOMER_HIT = SpriteAnimation(sequence_id=3, contact_frame=42, total_duration=52)
BOOMER_TAUNT = SpriteAnimation(sequence_id=4, total_duration=48)
BOOMER_RECOIL = SpriteAnimation(sequence_id=2, total_duration=18)


DODO_PECK = SpriteAnimation(sequence_id=3, contact_frame=16, total_duration=22)
DODO_TAUNT = SpriteAnimation(sequence_id=4, total_duration=66)


NINJA_HIT = SpriteAnimation(sequence_id=3, contact_frame=26, total_duration=38)
NINJA_HIT_FAST = SpriteAnimation(sequence_id=3, contact_frame=13, total_duration=19)
NINJA_TAUNT = SpriteAnimation(sequence_id=4, total_duration=54)
NINJA_RECOIL = SpriteAnimation(sequence_id=2, total_duration=14)


HIDON_ATTACK = SpriteAnimation(sequence_id=3, contact_frame=60, total_duration=60)
HIDON_ATTACK_FAST = SpriteAnimation(
    sequence_id=3, contact_frame=18, total_duration=30, speed=FAST
)


SHYGUY_SPIN = SpriteAnimation(sequence_id=5)
SHYGUY_HIT = SpriteAnimation(sequence_id=3, contact_frame=32, total_duration=40)
SHYGUY_TAUNT = SpriteAnimation(sequence_id=4, total_duration=110)
SHYGUY_RECOIL = SpriteAnimation(sequence_id=2, total_duration=14)


BIG_MAGIKOOPA_HIT = SpriteAnimation(sequence_id=3, contact_frame=38, total_duration=62)
BIG_MAGIKOOPA_HIT_FAST = SpriteAnimation(
    sequence_id=3, contact_frame=14, total_duration=32, speed=VERY_FAST
)
BIG_MAGIKOOPA_TAUNT = SpriteAnimation(sequence_id=4, total_duration=60)
BIG_MAGIKOOPA_RECOIL = SpriteAnimation(sequence_id=2, total_duration=16)


SNIFIT_SHOOT = SpriteAnimation(sequence_id=4, total_duration=60)
SNIFIT_TAUNT = SpriteAnimation(sequence_id=5, contact_frame=30, total_duration=46)
SNIFIT_RECOIL = SpriteAnimation(sequence_id=2, total_duration=16)


BOXBOY_ATTACK = SpriteAnimation(sequence_id=3, contact_frame=76, total_duration=98)
BOXBOY_SHORT = SpriteAnimation(sequence_id=3, contact_frame=8, total_duration=98)


CHESTER_ATTACK = SpriteAnimation(sequence_id=3, contact_frame=50, total_duration=64)
CHESTER_ATTACK_FAST = SpriteAnimation(
    sequence_id=3, contact_frame=18, total_duration=26
)


TORTE_TAUNT = SpriteAnimation(sequence_id=3, total_duration=40)
TORTE_TAUNT_FAST = SpriteAnimation(sequence_id=3, total_duration=20, speed=FAST)


MARIOCLONE_HIT_FAST = SpriteAnimation(
    sequence_id=0, contact_frame=8, total_duration=16, speed=FAST
)


PEACHCLONE_MAD = SpriteAnimation(sequence_id=4, contact_frame=12, total_duration=24)


BOWSERCLONE_LAUGH = SpriteAnimation(sequence_id=2, contact_frame=8, total_duration=16)
BOWSERCLONE_MAD = SpriteAnimation(sequence_id=4, contact_frame=12, total_duration=24)


GENOCLONE_LAUGH = SpriteAnimation(sequence_id=2, contact_frame=8, total_duration=16)
GENOCLONE_MAD = SpriteAnimation(sequence_id=4, contact_frame=6, total_duration=12)


MALLOWCLONE_LAUGH = SpriteAnimation(sequence_id=2, contact_frame=8, total_duration=16)
MALLOWCLONE_MAD = SpriteAnimation(sequence_id=4, contact_frame=8, total_duration=16)


SHYSTER_TAUNT = SpriteAnimation(sequence_id=4, contact_frame=56, total_duration=56)
SHYSTER_FAST = SpriteAnimation(
    sequence_id=4, contact_frame=28, total_duration=28, speed=FAST
)
SHYSTER_RECOIL = SpriteAnimation(sequence_id=2, total_duration=14)


AXEM_GREEN_HIT = SpriteAnimation(sequence_id=3, contact_frame=56, total_duration=84)
AXEM_GREEN_HIT_FAST = SpriteAnimation(
    sequence_id=3, contact_frame=28, total_duration=42, speed=FAST
)
AXEM_YELLOW_HIT = SpriteAnimation(sequence_id=3, contact_frame=82, total_duration=108)
AXEM_YELLOW_HIT_FAST = SpriteAnimation(
    sequence_id=3, contact_frame=41, total_duration=54, speed=FAST
)
AXEM_BLACK_HIT = SpriteAnimation(sequence_id=3, contact_frame=16, total_duration=64)
AXEM_PINK_HIT = SpriteAnimation(sequence_id=3, contact_frame=26, total_duration=58)
AXEM_RED_HIT = SpriteAnimation(sequence_id=3, contact_frame=26, total_duration=66)
AXEM_RED_HIT_FAST = SpriteAnimation(
    sequence_id=3, contact_frame=13, total_duration=33, speed=FAST
)
AXEM_RED_TAUNT = SpriteAnimation(sequence_id=4, total_duration=120)
AXEM_RED_RECOIL = SpriteAnimation(sequence_id=2, total_duration=22)


BUNDT_RECOIL = SpriteAnimation(sequence_id=2, total_duration=30)
BUNDT_TAUNT = SpriteAnimation(sequence_id=4, contact_frame=74, total_duration=82)
BUNDT_SHORT = SpriteAnimation(
    sequence_id=4, contact_frame=13, total_duration=16, speed=FASTEST
)


MEGASMILAX_RECOIL = SpriteAnimation(sequence_id=2, total_duration=14)
MEGASMILAX_BITE = SpriteAnimation(sequence_id=3, contact_frame=18, total_duration=28)
MEGASMILAX_TAUNT = SpriteAnimation(sequence_id=4, total_duration=38)


BIRDETTA_ATTACK = SpriteAnimation(sequence_id=3, contact_frame=40, total_duration=50)
BIRDETTA_ATTACK_FAST = SpriteAnimation(
    sequence_id=3, contact_frame=14, total_duration=18, speed=FASTEST
)
BIRDETTA_RECOIL = SpriteAnimation(sequence_id=2, total_duration=18)
BIRDETTA_TAUNT = SpriteAnimation(sequence_id=4, total_duration=48)


EGGBERT_EXPAND = SpriteAnimation(sequence_id=2, total_duration=32)


PUNCHINELLO_HIT = SpriteAnimation(sequence_id=3, contact_frame=26, total_duration=34)
PUNCHINELLO_HIT_FAST = SpriteAnimation(
    sequence_id=3, contact_frame=14, total_duration=24, speed=FAST
)
PUNCHINELLO_TAUNT = SpriteAnimation(sequence_id=4, total_duration=54)
PUNCHINELLO_RECOIL = SpriteAnimation(sequence_id=2, total_duration=14)
PUNCHINELLO_JUMP = SpriteAnimation(sequence_id=5, total_duration=34)


CZAR_DRAGON_HIT = SpriteAnimation(sequence_id=3, contact_frame=56, total_duration=66)
CZAR_RECOIL = SpriteAnimation(sequence_id=2, total_duration=14)
CZAR_TAUNT = SpriteAnimation(sequence_id=5)


CLOAKER_HIT = SpriteAnimation(sequence_id=3, contact_frame=38, total_duration=50)
CLOAKER_RECOIL = SpriteAnimation(sequence_id=2, total_duration=16)


MACK_HIT = SpriteAnimation(sequence_id=4, contact_frame=22, total_duration=28)
MACK_HIT_FAST = SpriteAnimation(
    sequence_id=4, contact_frame=13, total_duration=16, speed=FAST
)
MACK_CHALLENGE = SpriteAnimation(sequence_id=2, total_duration=12)


YARIDOVICH_HIT = SpriteAnimation(sequence_id=3, contact_frame=78, total_duration=84)
YARIDOVICH_TAUNT = SpriteAnimation(sequence_id=4, total_duration=40)
YARIDOVICH_TAUNT_FAST = SpriteAnimation(
    sequence_id=4, total_duration=40, contact_frame=15, speed=FAST
)
YARIDOVICH_ALT_TAUNT = SpriteAnimation(sequence_id=1, total_duration=48)
YARIDOVICH_RECOIL = SpriteAnimation(sequence_id=2, total_duration=16)


DRILLBIT_HIT = SpriteAnimation(sequence_id=3, contact_frame=54, total_duration=64)
DRILLBIT_HIT_FAST = SpriteAnimation(
    sequence_id=3, contact_frame=27, total_duration=32, speed=FAST
)
DRILLBIT_TAUNT = SpriteAnimation(sequence_id=4, total_duration=56)
DRILLBIT_RECOIL = SpriteAnimation(sequence_id=2, total_duration=14)


BOWYER_HIT = SpriteAnimation(sequence_id=3, contact_frame=76, total_duration=82)
BOWYER_TAUNT = SpriteAnimation(sequence_id=4, total_duration=62)
BOWYER_RECOIL = SpriteAnimation(sequence_id=2, total_duration=16)


JOHNNY_HIT = SpriteAnimation(sequence_id=3, contact_frame=48, total_duration=84)
JOHNNY_TAUNT = SpriteAnimation(sequence_id=4, total_duration=62)
JOHNNY_RECOIL = SpriteAnimation(sequence_id=2, total_duration=16)

TENTACLE_BECKON = SpriteAnimation(sequence_id=1, new_sprite_id=223)


DINGALING_ATTACK = SpriteAnimation(sequence_id=4, contact_frame=32, total_duration=44)
DINGALING_ATTACK_FAST = SpriteAnimation(
    sequence_id=4, contact_frame=16, total_duration=22, speed=FAST
)
DINGALING_TAUNT = SpriteAnimation(sequence_id=7, total_duration=62)
DINGALING_CIRCLE = SpriteAnimation(sequence_id=3, contact_frame=22, total_duration=34)
COUNTDOWN_LOOP = SpriteAnimation(sequence_id=9, total_duration=32)


GRATE_GUY_HIT = SpriteAnimation(sequence_id=4, contact_frame=52, total_duration=62)
GRATE_GUY_HIT_FAST = SpriteAnimation(
    sequence_id=4, contact_frame=14, total_duration=17, speed=VERY_FAST
)
GRATE_GUY_TAUNT = SpriteAnimation(sequence_id=3, total_duration=64)
GRATE_GUY_RECOIL = SpriteAnimation(sequence_id=2, total_duration=20)


SMITHY_HIT = SpriteAnimation(sequence_id=1, contact_frame=76, total_duration=122)
SMITHY_HIT_FAST = SpriteAnimation(
    sequence_id=1, contact_frame=14, total_duration=24, speed=FASTEST
)

GOOMBETTE_HIT = SpriteAnimation(sequence_id=3, contact_frame=42, total_duration=52)
GOOMBETTE_TAUNT = SpriteAnimation(sequence_id=2, total_duration=12)
GOOMBETTE_HIT_FAST = SpriteAnimation(
    sequence_id=3, contact_frame=21, total_duration=26, speed=FAST
)
