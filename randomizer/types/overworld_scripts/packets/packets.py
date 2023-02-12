from randomizer.types.sprites.constants.sprite_ids import *
from randomizer.types.overworld_scripts.action_scripts.constants.script_ids import *
from .classes import Packet

P000_FLASHING_POOF_FLOWER = Packet(
    packet_id=0,
    sprite_id=SPR0195_FLOWER,
    shadow=False,
    action_script_id=A0910_FLOWER_FLASH_THEN_POOF,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P001_FLASHING_POOF_MUSHROOM = Packet(
    packet_id=1,
    sprite_id=SPR0195_FLOWER,
    shadow=False,
    action_script_id=A0908_MUSHROOM_FLASH_THEN_POOF,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P002_BRIEF_KEY = Packet(
    packet_id=2,
    sprite_id=SPR0195_FLOWER,
    shadow=False,
    action_script_id=A0913_KEY_APPEARS_BRIEFLY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P003_BRIEF_STAR = Packet(
    packet_id=3,
    sprite_id=SPR0195_FLOWER,
    shadow=False,
    action_script_id=A0909_STAR_APPEARS_BRIEFLY,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 2, 4, 1, 0, 0]),
)
P004_MIMIC_POOF_ON_DEFEAT = Packet(
    packet_id=4,
    sprite_id=SPR0195_FLOWER,
    shadow=False,
    action_script_id=A0912_POOF_WHEN_MIMIC_3_DEFEATED,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 2, 3, 1, 0, 0]),
)
P005_BRIEF_POOF_BAG = Packet(
    packet_id=5,
    sprite_id=SPR0195_FLOWER,
    shadow=False,
    action_script_id=A0127_BAG_APPEARS_BRIEFLY_THEN_POOFS,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P006_STATIC_SIDEWAYS_SPARKLE = Packet(
    packet_id=6,
    sprite_id=SPR0197_SPARKLE_SIDEWAYS,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P007_STATIC_SIDEWAYS_SPARKLE = Packet(
    packet_id=7,
    sprite_id=SPR0197_SPARKLE_SIDEWAYS,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P008_STATIC_EXPLOSION = Packet(
    packet_id=8,
    sprite_id=SPR0200_EXPLOSION,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P009_STATIC_BLUE_CLOUD = Packet(
    packet_id=9,
    sprite_id=SPR0201_MOKURA_S_CLOUD_BLUE,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P010_STATIC_SMALL_FROG_COIN = Packet(
    packet_id=10,
    sprite_id=SPR0202_SHOES,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P011_STATIC_LEVELUP_TEXT = Packet(
    packet_id=11,
    sprite_id=SPR0203_LEVEL_UP_TEXT_FROM_INVINCIBLE_STAR,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P012_STATIC_GREY_EXPLOSION = Packet(
    packet_id=12,
    sprite_id=SPR0204_GREY_EXPLOSION_WHEN_ENCOUNTERING_FIREBALLS,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P013_STATIC_MICROBOMB = Packet(
    packet_id=13,
    sprite_id=SPR0205_MICROBOMB_PACKET,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P014_UNUSED = Packet(
    packet_id=14,
    sprite_id=SPR0255_BEETLE,
    shadow=False,
    action_script_id=A0914_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([3, 3, 1, 4, 1, 0, 0]),
)
P015_UNUSED = Packet(
    packet_id=15,
    sprite_id=SPR0255_BEETLE,
    shadow=False,
    action_script_id=A0915_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([3, 3, 1, 4, 1, 0, 0]),
)
P016_BIG_COIN_BEING_COLLECTED = Packet(
    packet_id=16,
    sprite_id=SPR0192_COIN,
    shadow=False,
    action_script_id=A0904_COIN_GETS_COLLECTED,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 5, 3, 3, 1, 0, 0]),
)
P017_SMALL_MINIGAME_COIN = Packet(
    packet_id=17,
    sprite_id=SPR0193_SMALL_COIN,
    shadow=False,
    action_script_id=A0171_MINIGAME_COIN_SPINS,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 5, 3, 4, 1, 0, 0]),
)
P018_SMALL_COIN_BEING_COLLECTED = Packet(
    packet_id=18,
    sprite_id=SPR0193_SMALL_COIN,
    shadow=False,
    action_script_id=A0904_COIN_GETS_COLLECTED,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 5, 3, 3, 1, 0, 0]),
)
P019_FROG_COIN_BEING_COLLECTED = Packet(
    packet_id=19,
    sprite_id=SPR0194_FROG_COIN,
    shadow=False,
    action_script_id=A0911_FROG_COIN_GETS_COLLECTED,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 5, 3, 3, 1, 0, 0]),
)
P020_WATER_DROPLETS_USE_7016_701A = Packet(
    packet_id=20,
    sprite_id=SPR0238_RED_JUICE,
    shadow=False,
    action_script_id=A0167_SPAWN_AT_7016_701A_CALCULATED,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 3, 3, 3, 1, 0, 0]),
)
P021_FLASHING_SMALL_EXPLOSION = Packet(
    packet_id=21,
    sprite_id=SPR0200_EXPLOSION,
    shadow=False,
    action_script_id=A0623_SMALL_EXPLOSION_FLASH_7_TIMES,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 3, 1, 4, 1, 0, 0]),
)
P022_RECURSIVE_SPARKLES = Packet(
    packet_id=22,
    sprite_id=SPR0197_SPARKLE_SIDEWAYS,
    shadow=False,
    action_script_id=A0446_SUMMON_EXTRA_SPARKLES,
    unknown_bits=[True, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 3, 0, 0]),
)
P023_LOOPING_SINGLE_SPARKLE = Packet(
    packet_id=23,
    sprite_id=SPR0197_SPARKLE_SIDEWAYS,
    shadow=False,
    action_script_id=A0447_LOOPING_SINGLE_SPARKLE,
    unknown_bits=[True, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 3, 0, 0]),
)
P024_REGULAR_SOUND_EXPLOSION = Packet(
    packet_id=24,
    sprite_id=SPR0200_EXPLOSION,
    shadow=False,
    action_script_id=A0063_EXPLOSION_WITH_SOUND,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 3, 2, 3, 1, 0, 0]),
)
P025_UNUSED = Packet(
    packet_id=25,
    sprite_id=SPR0201_MOKURA_S_CLOUD_BLUE,
    shadow=False,
    action_script_id=A0063_EXPLOSION_WITH_SOUND,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P026_UNUSED = Packet(
    packet_id=26,
    sprite_id=SPR0236_GREEN_JUICE,
    shadow=False,
    action_script_id=A0621_SEQ_10_STORE_BUTTON_INPUT_AND_MAKE_SOUND,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 6, 1, 4, 1, 0, 0]),
)
P027_UNUSED = Packet(
    packet_id=27,
    sprite_id=SPR0237_EGG,
    shadow=False,
    action_script_id=A0622_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 4, 1, 4, 1, 0, 0]),
)
P028_MUSHROOM_THROWN_SOUTHWEST = Packet(
    packet_id=28,
    sprite_id=SPR0195_FLOWER,
    shadow=True,
    action_script_id=A0907_MUSHROOM_THROWN_SOUTHWEST,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P029_SPARKLE_LINE_LOOPED = Packet(
    packet_id=29,
    sprite_id=SPR0198_SPARKLE_DOWNWARDS,
    shadow=False,
    action_script_id=A0507_SPARKLE_LINE_LOOPED,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 3, 3, 3, 1, 0, 0]),
)
P030_WATER_SPLASH_DROPS_SFX = Packet(
    packet_id=30,
    sprite_id=SPR0238_RED_JUICE,
    shadow=False,
    action_script_id=A0720_WATER_SPLASH_DROPS_SFX,
    unknown_bits=[True, False, False],
    unknown_bytes=bytearray([0, 3, 2, 3, 3, 0, 0]),
)
P031_LEVELUP_TEXT = Packet(
    packet_id=31,
    sprite_id=SPR0203_LEVEL_UP_TEXT_FROM_INVINCIBLE_STAR,
    shadow=False,
    action_script_id=A0620_LEVELUP_TEXT,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 3, 3, 3, 1, 0, 0]),
)
P032_BLUE_CLOUD = Packet(
    packet_id=32,
    sprite_id=SPR0201_MOKURA_S_CLOUD_BLUE,
    shadow=False,
    action_script_id=A0651_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P033_BOMB_EXPLOSION = Packet(
    packet_id=33,
    sprite_id=SPR0200_EXPLOSION,
    shadow=False,
    action_script_id=A0303_BOMB_EXPLOSION,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P034_GREY_EXPLOSION_SFX = Packet(
    packet_id=34,
    sprite_id=SPR0204_GREY_EXPLOSION_WHEN_ENCOUNTERING_FIREBALLS,
    shadow=False,
    action_script_id=A0063_EXPLOSION_WITH_SOUND,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 3, 2, 3, 1, 0, 0]),
)
P035_FLOWER_FALL = Packet(
    packet_id=35,
    sprite_id=SPR0195_FLOWER,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P036_MUSHROOM_FALL = Packet(
    packet_id=36,
    sprite_id=SPR0195_FLOWER,
    shadow=True,
    action_script_id=A0916_SEQ_1_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P037_ITEM_BAG_FALL = Packet(
    packet_id=37,
    sprite_id=SPR0195_FLOWER,
    shadow=True,
    action_script_id=A0918_SEQ_5_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P038_MUSHROOM_FALL_DEFAULT_PRIORITY = Packet(
    packet_id=38,
    sprite_id=SPR0195_FLOWER,
    shadow=True,
    action_script_id=A0921_SEQ_1_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P039_UNUSED = Packet(
    packet_id=39,
    sprite_id=SPR0192_COIN,
    shadow=False,
    action_script_id=A0915_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([1, 3, 1, 4, 1, 0, 0]),
)
P040_UNUSED = Packet(
    packet_id=40,
    sprite_id=SPR0208_HAMMER_PACKET,
    shadow=False,
    action_script_id=A0929_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 7, 1, 4, 0, 0, 0]),
)
P041_UNUSED = Packet(
    packet_id=41,
    sprite_id=SPR0209_STICK_PACKET,
    shadow=False,
    action_script_id=A0929_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 7, 1, 4, 0, 0, 0]),
)
P042_UNUSED = Packet(
    packet_id=42,
    sprite_id=SPR0210_CHOMP_PACKET,
    shadow=False,
    action_script_id=A0929_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 7, 1, 4, 0, 0, 0]),
)
P043_UNUSED = Packet(
    packet_id=43,
    sprite_id=SPR0211_FAN_PACKET,
    shadow=False,
    action_script_id=A0929_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 7, 1, 4, 0, 0, 0]),
)
P044_UNUSED = Packet(
    packet_id=44,
    sprite_id=SPR0212_RED_MUSHROOM_ITEM,
    shadow=False,
    action_script_id=A0929_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 7, 1, 4, 0, 0, 0]),
)
P045_TELEPORTATION_SHINE = Packet(
    packet_id=45,
    sprite_id=SPR0213_AXEM_RED_TELEPORT,
    shadow=False,
    action_script_id=A0940_TELEPORTATION_SHINE,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 3, 1, 4, 0, 0, 0]),
)
P046_UNUSED = Packet(
    packet_id=46,
    sprite_id=SPR0205_MICROBOMB_PACKET,
    shadow=False,
    action_script_id=A0939_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([1, 0, 1, 3, 0, 0, 0]),
)
P047_BLUE_FIRE_TRAIL = Packet(
    packet_id=47,
    sprite_id=SPR0201_MOKURA_S_CLOUD_BLUE,
    shadow=False,
    action_script_id=A0943_BLUE_FIRE_TRAIL,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 2, 4, 1, 0, 0]),
)
P048_UNUSED = Packet(
    packet_id=48,
    sprite_id=SPR0198_SPARKLE_DOWNWARDS,
    shadow=False,
    action_script_id=A0938_UNUSED,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 3, 3, 3, 1, 0, 0]),
)
P049_HAMMER_SPARKS_SFX = Packet(
    packet_id=49,
    sprite_id=SPR0198_SPARKLE_DOWNWARDS,
    shadow=False,
    action_script_id=A0952_HAMMER_SPARKS_SFX,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 3, 3, 3, 1, 0, 0]),
)
P050_WATER_BLAST_SFX = Packet(
    packet_id=50,
    sprite_id=SPR0242_WHITE_GAS_CLOUD,
    shadow=False,
    action_script_id=A0249_WATER_BLAST_SFX,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 7, 1, 4, 1, 0, 0]),
)
P051_DRILL_BIT = Packet(
    packet_id=51,
    sprite_id=SPR0243_MACHINE_MADE_DRILL_BIT,
    shadow=False,
    action_script_id=A0250_DRILL_BIT,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 7, 1, 4, 2, 0, 0]),
)
P052_BOMB_EXPLOSION_FASTER = Packet(
    packet_id=52,
    sprite_id=SPR0200_EXPLOSION,
    shadow=False,
    action_script_id=A0195_BOMB_EXPLOSION_FASTER,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P053_UNUSED = Packet(
    packet_id=53,
    sprite_id=SPR0194_FROG_COIN,
    shadow=False,
    action_script_id=A0196_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 5, 3, 3, 1, 0, 0]),
)
P054_LEVELUP_BONUS_POW = Packet(
    packet_id=54,
    sprite_id=SPR0230_LEVEL_UP_BONUS_POW_POWER,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P055_LEVELUP_BONUS_S = Packet(
    packet_id=55,
    sprite_id=SPR0231_LEVEL_UP_BONUS_STAR_MAGIC,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P056_LEVELUP_BONUS_HP = Packet(
    packet_id=56,
    sprite_id=SPR0232_LEVEL_UP_BONUS_HP,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P057_UNUSED = Packet(
    packet_id=57,
    sprite_id=SPR0233_GREEN_BOMB,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P058_UNUSED = Packet(
    packet_id=58,
    sprite_id=SPR0234_YELLOW_BOMB,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P059_UNUSED = Packet(
    packet_id=59,
    sprite_id=SPR0235_BLUE_BOMB,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P060_UNUSED = Packet(
    packet_id=60,
    sprite_id=SPR0236_GREEN_JUICE,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P061_UNUSED = Packet(
    packet_id=61,
    sprite_id=SPR0237_EGG,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P062_UNUSED = Packet(
    packet_id=62,
    sprite_id=SPR0238_RED_JUICE,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P063_UNUSED = Packet(
    packet_id=63,
    sprite_id=SPR0239_BLUE_R_DRINK,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P064_COIN_SHOWER_E = Packet(
    packet_id=64,
    sprite_id=SPR0192_COIN,
    shadow=False,
    action_script_id=A0896_COIN_SHOWER_E,
    unknown_bits=[False, True, True],
    unknown_bytes=bytearray([0, 3, 1, 4, 1, 0, 0]),
)
P065_COIN_SHOWER_SE = Packet(
    packet_id=65,
    sprite_id=SPR0192_COIN,
    shadow=False,
    action_script_id=A0897_COIN_SHOWER_SE,
    unknown_bits=[False, True, True],
    unknown_bytes=bytearray([0, 3, 1, 4, 1, 0, 0]),
)
P066_COIN_SHOWER_S = Packet(
    packet_id=66,
    sprite_id=SPR0192_COIN,
    shadow=False,
    action_script_id=A0898_COIN_SHOWER_S,
    unknown_bits=[False, True, True],
    unknown_bytes=bytearray([0, 3, 1, 4, 1, 0, 0]),
)
P067_COIN_SHOWER_SW = Packet(
    packet_id=67,
    sprite_id=SPR0192_COIN,
    shadow=False,
    action_script_id=A0899_COIN_SHOWER_SW,
    unknown_bits=[False, True, True],
    unknown_bytes=bytearray([0, 3, 1, 4, 1, 0, 0]),
)
P068_COIN_SHOWER_W = Packet(
    packet_id=68,
    sprite_id=SPR0192_COIN,
    shadow=False,
    action_script_id=A0900_COIN_SHOWER_W,
    unknown_bits=[False, True, True],
    unknown_bytes=bytearray([0, 3, 1, 4, 1, 0, 0]),
)
P069_COIN_SHOWER_NW = Packet(
    packet_id=69,
    sprite_id=SPR0192_COIN,
    shadow=False,
    action_script_id=A0901_COIN_SHOWER_NW,
    unknown_bits=[False, True, True],
    unknown_bytes=bytearray([0, 3, 1, 4, 1, 0, 0]),
)
P070_COIN_SHOWER_N = Packet(
    packet_id=70,
    sprite_id=SPR0192_COIN,
    shadow=False,
    action_script_id=A0902_COIN_SHOWER_N,
    unknown_bits=[False, True, True],
    unknown_bytes=bytearray([0, 3, 1, 4, 1, 0, 0]),
)
P071_COIN_SHOWER_NE = Packet(
    packet_id=71,
    sprite_id=SPR0192_COIN,
    shadow=False,
    action_script_id=A0903_COIN_SHOWER_NE,
    unknown_bits=[False, True, True],
    unknown_bytes=bytearray([0, 3, 1, 4, 1, 0, 0]),
)
P072_COIN_SHOWER_E_DB = Packet(
    packet_id=72,
    sprite_id=SPR0192_COIN,
    shadow=False,
    action_script_id=A0905_COIN_SHOWER_E_DB,
    unknown_bits=[False, True, True],
    unknown_bytes=bytearray([0, 3, 1, 4, 1, 0, 0]),
)
P073_UNUSED = Packet(
    packet_id=73,
    sprite_id=SPR0249_RED_SHELL,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P074_UNUSED = Packet(
    packet_id=74,
    sprite_id=SPR0250_GREEN_SHELL,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P075_UNUSED = Packet(
    packet_id=75,
    sprite_id=SPR0251_PARASOL_PACKET,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P076_UNUSED = Packet(
    packet_id=76,
    sprite_id=SPR0252_FEATHER,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P077_UNUSED = Packet(
    packet_id=77,
    sprite_id=SPR0253_BERRY,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P078_UNUSED = Packet(
    packet_id=78,
    sprite_id=SPR0254_YOSHI_COOKIE,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P079_UNUSED = Packet(
    packet_id=79,
    sprite_id=SPR0255_BEETLE,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 0, 0, 0, 0, 0]),
)
P080_FEATHER_CHEST = Packet(
    packet_id=80,
    sprite_id=SPR0252_FEATHER,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P081_STAR_PIECE_CHEST = Packet(
    packet_id=81,
    sprite_id=SPR0226_TINY_STAR,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P082_FEATHER_FALL = Packet(
    packet_id=82,
    sprite_id=SPR0252_FEATHER,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P083_STAR_PIECE_FALL = Packet(
    packet_id=83,
    sprite_id=SPR0226_TINY_STAR,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P084_FEATHER_STATIC = Packet(
    packet_id=84,
    sprite_id=SPR0252_FEATHER,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P085_STAR_PIECE_STATIC = Packet(
    packet_id=85,
    sprite_id=SPR0226_TINY_STAR,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P086_FLOWER_STATIC = Packet(
    packet_id=86,
    sprite_id=SPR0195_FLOWER,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P087_MUSHROOM_STATIC = Packet(
    packet_id=87,
    sprite_id=SPR0195_FLOWER,
    shadow=False,
    action_script_id=A0581_SEQUENCE_1_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P088_KEY_STATIC = Packet(
    packet_id=88,
    sprite_id=SPR0195_FLOWER,
    shadow=False,
    action_script_id=A0721_SEQUENCE_2_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P089_KEY_FALLING = Packet(
    packet_id=89,
    sprite_id=SPR0195_FLOWER,
    shadow=True,
    action_script_id=A0204_SEQUENCE_2_FALL,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P090_BAG_STATIC = Packet(
    packet_id=90,
    sprite_id=SPR0195_FLOWER,
    shadow=False,
    action_script_id=A0545_SEQUENCE_5_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P091_RING_CHEST = Packet(
    packet_id=91,
    sprite_id=SPR0196_RING,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P092_RING_FALL = Packet(
    packet_id=92,
    sprite_id=SPR0196_RING,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P093_RING_STATIC = Packet(
    packet_id=93,
    sprite_id=SPR0196_RING,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P094_BROOCH_STATIC = Packet(
    packet_id=94,
    sprite_id=SPR0207_BROOCH,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P095_BROOCH_FALL = Packet(
    packet_id=95,
    sprite_id=SPR0207_BROOCH,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P096_BROOCH_CHEST = Packet(
    packet_id=96,
    sprite_id=SPR0207_BROOCH,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P097_SHOES_STATIC = Packet(
    packet_id=97,
    sprite_id=SPR0202_SHOES,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P098_SHOES_FALL = Packet(
    packet_id=98,
    sprite_id=SPR0202_SHOES,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P099_SHOES_CHEST = Packet(
    packet_id=99,
    sprite_id=SPR0202_SHOES,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P100_BANANA_STATIC = Packet(
    packet_id=100,
    sprite_id=SPR0222_BANANA_PEEL,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P101_BANANA_FALL = Packet(
    packet_id=101,
    sprite_id=SPR0222_BANANA_PEEL,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P102_BANANA_CHEST = Packet(
    packet_id=102,
    sprite_id=SPR0222_BANANA_PEEL,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P103_CROWN_CHEST = Packet(
    packet_id=103,
    sprite_id=SPR0216_CROWN,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P104_CROWN_FALL = Packet(
    packet_id=104,
    sprite_id=SPR0216_CROWN,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P105_CROWN_STATIC = Packet(
    packet_id=105,
    sprite_id=SPR0216_CROWN,
    shadow=True,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P106_COIN_FALL = Packet(
    packet_id=106,
    sprite_id=SPR0192_COIN,
    shadow=True,
    action_script_id=A0916_SEQ_1_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P107_SMALL_COIN_FALL = Packet(
    packet_id=107,
    sprite_id=SPR0193_SMALL_COIN,
    shadow=True,
    action_script_id=A0916_SEQ_1_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P108_FROG_COIN_FALL = Packet(
    packet_id=108,
    sprite_id=SPR0194_FROG_COIN,
    shadow=True,
    action_script_id=A0916_SEQ_1_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P109_COIN_STATIC = Packet(
    packet_id=109,
    sprite_id=SPR0192_COIN,
    shadow=False,
    action_script_id=A0925_SPINNING_STATIC_COIN,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P110_SMALL_COIN_STATIC = Packet(
    packet_id=110,
    sprite_id=SPR0193_SMALL_COIN,
    shadow=False,
    action_script_id=A0925_SPINNING_STATIC_COIN,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P111_FROG_COIN_STATIC = Packet(
    packet_id=111,
    sprite_id=SPR0194_FROG_COIN,
    shadow=False,
    action_script_id=A0925_SPINNING_STATIC_COIN,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P112_BOMB_STATIC = Packet(
    packet_id=112,
    sprite_id=SPR0205_MICROBOMB_PACKET,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P113_BOMB_FALL = Packet(
    packet_id=113,
    sprite_id=SPR0205_MICROBOMB_PACKET,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P114_BOMB_CHEST = Packet(
    packet_id=114,
    sprite_id=SPR0205_MICROBOMB_PACKET,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P115_EGG_STATIC = Packet(
    packet_id=115,
    sprite_id=SPR0237_EGG,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P116_EGG_FALLING = Packet(
    packet_id=116,
    sprite_id=SPR0237_EGG,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P117_EGG_CHEST = Packet(
    packet_id=117,
    sprite_id=SPR0237_EGG,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P118_COOKIE_STATIC = Packet(
    packet_id=118,
    sprite_id=SPR0254_YOSHI_COOKIE,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P119_COOKIE_FALL = Packet(
    packet_id=119,
    sprite_id=SPR0254_YOSHI_COOKIE,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P120_COOKIE_CHEST = Packet(
    packet_id=120,
    sprite_id=SPR0254_YOSHI_COOKIE,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P121_BERRY_STATIC = Packet(
    packet_id=121,
    sprite_id=SPR0253_BERRY,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P122_BERRY_FALL = Packet(
    packet_id=122,
    sprite_id=SPR0253_BERRY,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P123_BERRY_CHEST = Packet(
    packet_id=123,
    sprite_id=SPR0253_BERRY,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P124_CARD_STATIC = Packet(
    packet_id=124,
    sprite_id=SPR0206_CARD,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P125_CARD_FALL = Packet(
    packet_id=125,
    sprite_id=SPR0206_CARD,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P126_CARD_CHEST = Packet(
    packet_id=126,
    sprite_id=SPR0206_CARD,
    shadow=False,
    action_script_id=A0525_SPINNING_CARD,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P127_GREEN_SYRUP_STATIC = Packet(
    packet_id=127,
    sprite_id=SPR0220_GREEN_SYRUP,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P128_GREEN_SYRUP_FALL = Packet(
    packet_id=128,
    sprite_id=SPR0220_GREEN_SYRUP,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P129_GREEN_SYRUP_CHEST = Packet(
    packet_id=129,
    sprite_id=SPR0220_GREEN_SYRUP,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P130_RED_SYRUP_STATIC = Packet(
    packet_id=130,
    sprite_id=SPR0219_RED_SYRUP,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P131_RED_SYRUP_FALL = Packet(
    packet_id=131,
    sprite_id=SPR0219_RED_SYRUP,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P132_RED_SYRUP_CHEST = Packet(
    packet_id=132,
    sprite_id=SPR0219_RED_SYRUP,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P133_BLUE_SYRUP_STATIC = Packet(
    packet_id=133,
    sprite_id=SPR0223_BLUE_SYRUP,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P134_BLUE_SYRUP_FALL = Packet(
    packet_id=134,
    sprite_id=SPR0223_BLUE_SYRUP,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P135_BLUE_SYRUP_CHEST = Packet(
    packet_id=135,
    sprite_id=SPR0223_BLUE_SYRUP,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P136_YELLOW_SYRUP_STATIC = Packet(
    packet_id=136,
    sprite_id=SPR0221_YELLOW_SYRUP,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P137_YELLOW_SYRUP_FALL = Packet(
    packet_id=137,
    sprite_id=SPR0221_YELLOW_SYRUP,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P138_YELLOW_SYRUP_CHEST = Packet(
    packet_id=138,
    sprite_id=SPR0221_YELLOW_SYRUP,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P139_GREEN_JUICE_STATIC = Packet(
    packet_id=139,
    sprite_id=SPR0236_GREEN_JUICE,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P140_GREEN_JUICE_FALL = Packet(
    packet_id=140,
    sprite_id=SPR0236_GREEN_JUICE,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P141_GREEN_JUICE_CHEST = Packet(
    packet_id=141,
    sprite_id=SPR0236_GREEN_JUICE,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P142_RED_JUICE_STATIC = Packet(
    packet_id=142,
    sprite_id=SPR0238_RED_JUICE,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P143_RED_JUICE_FALL = Packet(
    packet_id=143,
    sprite_id=SPR0238_RED_JUICE,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P144_RED_JUICE_CHEST = Packet(
    packet_id=144,
    sprite_id=SPR0238_RED_JUICE,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P145_P_DRINK_STATIC = Packet(
    packet_id=145,
    sprite_id=SPR0241_GREEN_P_DRINK,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P146_P_DRINK_FALL = Packet(
    packet_id=146,
    sprite_id=SPR0241_GREEN_P_DRINK,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P147_P_DRINK_CHEST = Packet(
    packet_id=147,
    sprite_id=SPR0241_GREEN_P_DRINK,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P148_D_DRINK_CHEST = Packet(
    packet_id=148,
    sprite_id=SPR0240_YELLOW_D_DRINK,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P149_D_DRINK_FALL = Packet(
    packet_id=149,
    sprite_id=SPR0240_YELLOW_D_DRINK,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P150_D_DRINK_STATIC = Packet(
    packet_id=150,
    sprite_id=SPR0240_YELLOW_D_DRINK,
    shadow=True,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P151_YELLOW_MUSIC_DRINK_CHEST = Packet(
    packet_id=151,
    sprite_id=SPR0245_YELLOW_MUSIC_DRINK,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P152_YELLOW_MUSIC_DRINK_FALL = Packet(
    packet_id=152,
    sprite_id=SPR0245_YELLOW_MUSIC_DRINK,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P153_YELLOW_MUSIC_DRINK_STATIC = Packet(
    packet_id=153,
    sprite_id=SPR0245_YELLOW_MUSIC_DRINK,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P154_BLUE_MUSIC_DRINK_CHEST = Packet(
    packet_id=154,
    sprite_id=SPR0246_BLUE_MUSIC_DRINK,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P155_BLUE_MUSIC_DRINK_FALL = Packet(
    packet_id=155,
    sprite_id=SPR0246_BLUE_MUSIC_DRINK,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P156_BLUE_MUSIC_DRINK_STATIC = Packet(
    packet_id=156,
    sprite_id=SPR0246_BLUE_MUSIC_DRINK,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P157_FROG_DRINK_CHEST = Packet(
    packet_id=157,
    sprite_id=SPR0244_GREEN_FROG_DRINK,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P158_FROG_DRINK_FALL = Packet(
    packet_id=158,
    sprite_id=SPR0244_GREEN_FROG_DRINK,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P159_FROG_DRINK_STATIC = Packet(
    packet_id=159,
    sprite_id=SPR0244_GREEN_FROG_DRINK,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P160_RED_MUSIC_DRINK_CHEST = Packet(
    packet_id=160,
    sprite_id=SPR0247_RED_MUSIC_DRINK,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P161_RED_MUSIC_DRINK_FALL = Packet(
    packet_id=161,
    sprite_id=SPR0247_RED_MUSIC_DRINK,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P162_RED_MUSIC_DRINK_STATIC = Packet(
    packet_id=162,
    sprite_id=SPR0247_RED_MUSIC_DRINK,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P163_R_DRINK_STATIC = Packet(
    packet_id=163,
    sprite_id=SPR0239_BLUE_R_DRINK,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P164_R_DRINK_FALL = Packet(
    packet_id=164,
    sprite_id=SPR0239_BLUE_R_DRINK,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P165_R_DRINK_CHEST = Packet(
    packet_id=165,
    sprite_id=SPR0239_BLUE_R_DRINK,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P166_MUSIC_NOTE_STATIC = Packet(
    packet_id=166,
    sprite_id=SPR0195_FLOWER,
    shadow=False,
    action_script_id=A0202_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P167_MUSIC_NOTE_FALL = Packet(
    packet_id=167,
    sprite_id=SPR0195_FLOWER,
    shadow=True,
    action_script_id=A0583_EMPTY,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P168_MUSIC_NOTE_CHEST = Packet(
    packet_id=168,
    sprite_id=SPR0195_FLOWER,
    shadow=False,
    action_script_id=A0687_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P169_STAR_DRINK_STATIC = Packet(
    packet_id=169,
    sprite_id=SPR0248_RED_STAR_DRINK,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P170_STAR_DRINK_FALL = Packet(
    packet_id=170,
    sprite_id=SPR0248_RED_STAR_DRINK,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P171_STAR_DRINK_CHEST = Packet(
    packet_id=171,
    sprite_id=SPR0248_RED_STAR_DRINK,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P172_UNUSED = Packet(
    packet_id=172,
    sprite_id=SPR0209_STICK_PACKET,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P173_GREEN_CANDY_STATIC = Packet(
    packet_id=173,
    sprite_id=SPR0217_GREEN_CANDY,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P174_GREEN_CANDY_FALL = Packet(
    packet_id=174,
    sprite_id=SPR0217_GREEN_CANDY,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P175_GREEN_CANDY_CHEST = Packet(
    packet_id=175,
    sprite_id=SPR0217_GREEN_CANDY,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P176_BLUE_CANDY_STATIC = Packet(
    packet_id=176,
    sprite_id=SPR0218_BLUE_CANDY,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P177_BLUE_CANDY_FALL = Packet(
    packet_id=177,
    sprite_id=SPR0218_BLUE_CANDY,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P178_BLUE_CANDY_CHEST = Packet(
    packet_id=178,
    sprite_id=SPR0218_BLUE_CANDY,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P179_GREEN_BOMB_STATIC = Packet(
    packet_id=179,
    sprite_id=SPR0233_GREEN_BOMB,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P180_GREEN_BOMB_FALL = Packet(
    packet_id=180,
    sprite_id=SPR0233_GREEN_BOMB,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P181_GREEN_BOMB_CHEST = Packet(
    packet_id=181,
    sprite_id=SPR0233_GREEN_BOMB,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P182_RED_BOMB_STATIC = Packet(
    packet_id=182,
    sprite_id=SPR0224_RED_BOMB,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P183_RED_BOMB_FALL = Packet(
    packet_id=183,
    sprite_id=SPR0224_RED_BOMB,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P184_RED_BOMB_CHEST = Packet(
    packet_id=184,
    sprite_id=SPR0224_RED_BOMB,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P185_BLUE_BOMB_STATIC = Packet(
    packet_id=185,
    sprite_id=SPR0235_BLUE_BOMB,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P186_BLUE_BOMB_FALL = Packet(
    packet_id=186,
    sprite_id=SPR0235_BLUE_BOMB,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P187_BLUE_BOMB_CHEST = Packet(
    packet_id=187,
    sprite_id=SPR0235_BLUE_BOMB,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P188_YELLOW_BOMB_STATIC = Packet(
    packet_id=188,
    sprite_id=SPR0234_YELLOW_BOMB,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P189_YELLOW_BOMB_FALL = Packet(
    packet_id=189,
    sprite_id=SPR0234_YELLOW_BOMB,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P190_YELLOW_BOMB_CHEST = Packet(
    packet_id=190,
    sprite_id=SPR0234_YELLOW_BOMB,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P191_BEETLE_STATIC = Packet(
    packet_id=191,
    sprite_id=SPR0255_BEETLE,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P192_BEETLE_FALL = Packet(
    packet_id=192,
    sprite_id=SPR0255_BEETLE,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P193_BEETLE_CHEST = Packet(
    packet_id=193,
    sprite_id=SPR0255_BEETLE,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P194_RED_MUSHROOM_STATIC = Packet(
    packet_id=194,
    sprite_id=SPR0212_RED_MUSHROOM_ITEM,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P195_RED_MUSHROOM_FALL = Packet(
    packet_id=195,
    sprite_id=SPR0212_RED_MUSHROOM_ITEM,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P196_RED_MUSHROOM_CHEST = Packet(
    packet_id=196,
    sprite_id=SPR0212_RED_MUSHROOM_ITEM,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P197_GREEN_MUSHROOM_STATIC = Packet(
    packet_id=197,
    sprite_id=SPR0214_GREEN_MUSHROOM_ITEM,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P198_GREEN_MUSHROOM_FALL = Packet(
    packet_id=198,
    sprite_id=SPR0214_GREEN_MUSHROOM_ITEM,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P199_GREEN_MUSHROOM_CHEST = Packet(
    packet_id=199,
    sprite_id=SPR0214_GREEN_MUSHROOM_ITEM,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P200_YELLOW_MUSHROOM_STATIC = Packet(
    packet_id=200,
    sprite_id=SPR0215_YELLOW_MUSHROOM_ITEM,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P201_YELLOW_MUSHROOM_FALL = Packet(
    packet_id=201,
    sprite_id=SPR0215_YELLOW_MUSHROOM_ITEM,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P202_YELLOW_MUSHROOM_CHEST = Packet(
    packet_id=202,
    sprite_id=SPR0215_YELLOW_MUSHROOM_ITEM,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P203_FRYING_PAN_STATIC = Packet(
    packet_id=203,
    sprite_id=SPR0199_FRYING_PAN_PACKET,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P204_FRYING_PAN_FALL = Packet(
    packet_id=204,
    sprite_id=SPR0199_FRYING_PAN_PACKET,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P205_FRYING_PAN_CHEST = Packet(
    packet_id=205,
    sprite_id=SPR0199_FRYING_PAN_PACKET,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P206_HAMMER_STATIC = Packet(
    packet_id=206,
    sprite_id=SPR0208_HAMMER_PACKET,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P207_HAMMER_FALL = Packet(
    packet_id=207,
    sprite_id=SPR0208_HAMMER_PACKET,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P208_HAMMER_CHEST = Packet(
    packet_id=208,
    sprite_id=SPR0208_HAMMER_PACKET,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P209_STICK_STATIC = Packet(
    packet_id=209,
    sprite_id=SPR0209_STICK_PACKET,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P210_STICK_FALL = Packet(
    packet_id=210,
    sprite_id=SPR0209_STICK_PACKET,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P211_STICK_CHEST = Packet(
    packet_id=211,
    sprite_id=SPR0209_STICK_PACKET,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P212_CHOMP_STATIC = Packet(
    packet_id=212,
    sprite_id=SPR0210_CHOMP_PACKET,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P213_CHOMP_FALL = Packet(
    packet_id=213,
    sprite_id=SPR0210_CHOMP_PACKET,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P214_CHOMP_CHEST = Packet(
    packet_id=214,
    sprite_id=SPR0210_CHOMP_PACKET,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P215_FAN_STATIC = Packet(
    packet_id=215,
    sprite_id=SPR0211_FAN_PACKET,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P216_FAN_FALL = Packet(
    packet_id=216,
    sprite_id=SPR0211_FAN_PACKET,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P217_FAN_CHEST = Packet(
    packet_id=217,
    sprite_id=SPR0211_FAN_PACKET,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P218_RED_SHELL_STATIC = Packet(
    packet_id=218,
    sprite_id=SPR0249_RED_SHELL,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P219_RED_SHELL_FALL = Packet(
    packet_id=219,
    sprite_id=SPR0249_RED_SHELL,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P220_RED_SHELL_CHEST = Packet(
    packet_id=220,
    sprite_id=SPR0249_RED_SHELL,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P221_GREEN_SHELL_STATIC = Packet(
    packet_id=221,
    sprite_id=SPR0250_GREEN_SHELL,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P222_GREEN_SHELL_FALL = Packet(
    packet_id=222,
    sprite_id=SPR0250_GREEN_SHELL,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P223_GREEN_SHELL_CHEST = Packet(
    packet_id=223,
    sprite_id=SPR0250_GREEN_SHELL,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P224_PARASOL_STATIC = Packet(
    packet_id=224,
    sprite_id=SPR0251_PARASOL_PACKET,
    shadow=False,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 1, 3, 1, 0, 0]),
)
P225_PARASOL_FALL = Packet(
    packet_id=225,
    sprite_id=SPR0251_PARASOL_PACKET,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0, 0, 1, 4, 1, 0, 0]),
)
P226_PARASOL_CHEST = Packet(
    packet_id=226,
    sprite_id=SPR0251_PARASOL_PACKET,
    shadow=False,
    action_script_id=A0992_DEFAULT_SEQUENCE_IN_CHEST,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0, 0, 3, 3, 1, 0, 0]),
)
P227_UNUSED = Packet(packet_id=227)
P228_UNUSED = Packet(packet_id=228)
P229_UNUSED = Packet(packet_id=229)
P230_UNUSED = Packet(packet_id=230)
P231_UNUSED = Packet(packet_id=231)
P232_UNUSED = Packet(packet_id=232)
P233_UNUSED = Packet(packet_id=233)
P234_UNUSED = Packet(packet_id=234)
P235_UNUSED = Packet(packet_id=235)
P236_UNUSED = Packet(packet_id=236)
P237_UNUSED = Packet(packet_id=237)
P238_UNUSED = Packet(packet_id=238)
P239_UNUSED = Packet(packet_id=239)
P240_UNUSED = Packet(packet_id=240)
P241_UNUSED = Packet(packet_id=241)
P242_UNUSED = Packet(packet_id=242)
P243_UNUSED = Packet(packet_id=243)
P244_UNUSED = Packet(packet_id=244)
P245_UNUSED = Packet(packet_id=245)
P246_UNUSED = Packet(packet_id=246)
P247_UNUSED = Packet(packet_id=247)
P248_UNUSED = Packet(packet_id=248)
P249_UNUSED = Packet(packet_id=249)
P250_UNUSED = Packet(packet_id=250)
P251_UNUSED = Packet(packet_id=251)
P252_UNUSED = Packet(packet_id=252)
P253_UNUSED = Packet(packet_id=253)
P254_UNUSED = Packet(packet_id=254)
P255_UNUSED = Packet(packet_id=255)
