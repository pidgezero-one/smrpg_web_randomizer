from django.core.management.base import BaseCommand
from randomizer.management.disassembler_common import (
    shortify,
    shortify_signed,
    byte_signed,
    writeline,
)
import re
from randomizer.types.sprites.constants.sprite_ids import *
from copy import deepcopy

ORIGINS = [
    "ABSOLUTE_POSITION",
    "CASTER_INITIAL_POSITION",
    "TARGET_CURRENT_POSITION",
    "CASTER_CURRENT_POSITION",
]

EFFECTS = [
    "EF0000____DUMMY",
    "EF0001____DUMMY",
    "EF0002_THUNDERSHOCK",
    "EF0003_THUNDERSHOCK__BG_MASK_",
    "EF0004_CRUSHER",
    "EF0005_METEOR_BLAST",
    "EF0006_BOLT",
    "EF0007_STAR_RAIN",
    "EF0008_FLAME__FIRE_ENGULF_",
    "EF0009_MUTE__BALLOON_",
    "EF0010_FLAME_STONE",
    "EF0011_BOWSER_CRUSH",
    "EF0012_SPELL_CAST_SPADE",
    "EF0013_SPELL_CAST_HEART",
    "EF0014_SPELL_CAST_CLUB",
    "EF0015_SPELL_CAST_DIAMOND",
    "EF0016_SPELL_CAST_STAR",
    "EF0017_TERRORIZE",
    "EF0018_SNOWY__SNOW_BG__4BPP_",
    "EF0019_SNOWY__SNOW_FG__2BPP_",
    "EF0020_ENDOBUBBLE__BLACK_BALL_ORB_",
    "EF0021____DUMMY",
    "EF0022_SOLIDIFY",
    "EF0023____DUMMY",
    "EF0024____DUMMY",
    "EF0025_PSYCH_BOMB__BG_",
    "EF0026____DUMMY",
    "EF0027_DARK_STAR",
    "EF0028_WILLY_WISP__BLUE_ORB_BALL_BG_",
    "EF0029____DUMMY",
    "EF0030____DUMMY",
    "EF0031____DUMMY",
    "EF0032_GENO_WHIRL",
    "EF0033____DUMMY",
    "EF0034____DUMMY",
    "EF0035____DUMMY",
    "EF0036_BLANK_WHITE_FLASH__2BPP_",
    "EF0037_BLANK_WHITE_FLASH__4BPP_",
    "EF0038_BOULDER",
    "EF0039_BLACK_BALL_ORB",
    "EF0040_BLANK_BLUE_FLASH__2BPP_",
    "EF0041_BLANK_RED_FLASH__2BPP_",
    "EF0042_BLANK_BLUE_FLASH__4BPP_",
    "EF0043_BLANK_RED_FLASH__4BPP_",
    "EF0044____DUMMY",
    "EF0045_BLANK_DARK_BLUE_FLASH__2BPP_",
    "EF0046_BLANK_DARK_BLUE_FLASH__4BPP_",
    "EF0047_METEOR_SHOWER__SNOW_CONFETTI_",
    "EF0048_PURPLE_VIOLET_FLASH__4BPP_",
    "EF0049_BROWN_FLASH__4BPP_",
    "EF0050_DARK_RED_BLAST",
    "EF0051_DARK_BLUE_BLAST",
    "EF0052_SNOW_CONFETTI__GREEN",
    "EF0053_LIGHT_BLUE_BLAST",
    "EF0054_BLACK_BALL_ORB",
    "EF0055_RED_BALL_ORB",
    "EF0056_GREEN_BALL_ORB",
    "EF0057_SNOW_CONFETTI__SLATE_GREEN",
    "EF0058_SNOW_CONFETTI__RED",
    "EF0059_ORANGE_RED_BLAST__FIRE_BOMB_",
    "EF0060_ICE_BOMB_SOLIDIFY_BG__BLUE_FREEZE_",
    "EF0061_STATIC_E___ELECTRIC_BLAST_",
    "EF0062_GREEN_STAR_BUNCHES",
    "EF0063_BLUE_STAR_BUNCHES",
    "EF0064_PINK_STAR_BUNCHES",
    "EF0065_YELLOW_STAR_BUNCHES",
    "EF0066_AURORA_FLASH",
    "EF0067_STORM",
    "EF0068_ELECTROSHOCK",
    "EF0069_SMITHY_TREASURE_HEAD_SPELL__RED",
    "EF0070_SMITHY_TREASURE_HEAD_SPELL__GREEN",
    "EF0071_SMITHY_TREASURE_HEAD_SPELL__BLUE",
    "EF0072_SMITHY_TREASURE_HEAD_SPELL__YELLOW",
    "EF0073____DUMMY",
    "EF0074____DUMMY",
    "EF0075____DUMMY",
    "EF0076_FLAME_WALL__ORANGE_RED_FIRE_",
    "EF0077_PETAL_BLAST_1",
    "EF0078_PETAL_BLAST_2",
    "EF0079_DRAIN_BEAM_BG__4BPP_",
    "EF0080_DRAIN_BEAM_FG__2BPP_",
    "EF0081____DUMMY",
    "EF0082_ELECTRIC_BOLT",
    "EF0083_SAND_STORM_BG__2BPP_",
    "EF0084____DUMMY",
    "EF0085_POLLEN_NAP__YELLOW_POLLEN_",
    "EF0086_GENO_BEAM__BLUE",
    "EF0087_GENO_BEAM__RED",
    "EF0088_GENO_BEAM__GOLD",
    "EF0089_GENO_BEAM__YELLOW",
    "EF0090_GENO_BEAM__GREEN",
    "EF0091_THUNDERBOLT",
    "EF0092_LIGHT_BEAM",
    "EF0093_METEOR_SHOWER",
    "EF0094_S__CROW_DUST__PURPLE_POLLEN_",
    "EF0095_HP_RAIN_BG",
    "EF0096_HP_RAIN_FG",
    "EF0097_WAVY_DARK_BLUE_LINES",
    "EF0098_WAVY_BLUE_LINES",
    "EF0099_WAVY_RED_LINES",
    "EF0100_WAVY_BROWN_LINES",
    "EF0101_SAND_STORM_FG__4BPP_",
    "EF0102_SLEDGE",
    "EF0103_ARROW_RAIN",
    "EF0104_SPEAR_RAIN",
    "EF0105_SWORD_RAIN",
    "EF0106_LIGHTNING_ORB__BG_WAVES_",
    "EF0107_ECHOFINDER",
    "EF0108_POISON_GAS_FG_1",
    "EF0109_POISON_GAS_FG_2",
    "EF0110_POISON_GAS_BG",
    "EF0111_SMITHY_TRANSFORMS__BEAM_EFFECT_",
    "EF0112_SMELTER__S_MOLTEN_METAL",
    "EF0113____DUMMY",
    "EF0114____DUMMY",
    "EF0115____DUMMY",
    "EF0116____DUMMY",
    "EF0117____DUMMY",
    "EF0118____DUMMY",
    "EF0119____DUMMY",
    "EF0120____DUMMY",
    "EF0121____DUMMY",
    "EF0122____DUMMY",
    "EF0123____DUMMY",
    "EF0124____DUMMY",
    "EF0125____DUMMY",
    "EF0126____DUMMY",
    "EF0127____DUMMY",
]

FLASH_COLOURS = ["NO_COLOUR", "RED", "GREEN", "YELLOW", "BLUE", "PINK", "AQUA", "WHITE"]

BONUS_MESSAGES = [
    "BM_ATTACK",
    "BM_DEFENSE",
    "BM_UP",
    "BM_HPMAX",
    "BM_ONCE",
    "BM_AGAIN",
    "BM_LUCKY",
]

SCREEN_EFFECTS = [
    "SEF0000_GENO_FLASH",
    "SEF0001_SNOWY",
    "SEF0002_TERRORIZE",
    "SEF0003_SHOCKER",
    "SEF0004_UNKNOWN",
    "SEF0005_SLASH_INSTANT_DEATH",
    "SEF0006_SCREEN_FLASHES_WHITE",
    "SEF0007_CHANGE_BATTLEFIELD",
    "SEF0008_COME_BACK",
    "SEF0009_GENO_BEAM",
    "SEF0010_GENO_BLAST",
    "SEF0011_HOWL",
    "SEF0012_WIN_BATTLE_WINDOW",
    "SEF0013_SET_BATTLEFIELD_COORDS",
    "SEF0014_SQUASH_BIG_STAR",
    "SEF0015_UNKNOWN",
    "SEF0016_UNKNOWN",
    "SEF0017_CORONA",
    "SEF0018_MEGA_DRAIN",
    "SEF0019_UNKNOWN",
    "SEF0020_UNKNOWN",
]

SOUNDS = [
    "S0000_SILENCE",
    "S0001_MENU_SELECT",
    "S0002_MENU_CANCEL",
    "S0003_MENU_SCROLL",
    "S0004_JUMP",
    "S0005_BIRDIE_TWEET",
    "S0006_BONUS_FLOWER_STATUS_UP",
    "S0007_ERROR_INCORRECT_ANSWER",
    "S0008_GET_DIZZY",
    "S0009_ARROW_SLING",
    "S0010_MALLOW_PUNCH_1",
    "S0011_SWOOSH_RUN_AWAY",
    "S0012_BOMB_EXPLOSION",
    "S0013_COIN",
    "S0014_ITEM_GET",
    "S0015_SPIKE_STING",
    "S0016_BITE",
    "S0017_STAR_GUN_SHOOT",
    "S0018_SUPER_JUMP_HIT_1",
    "S0019_DRAIN_BEAM",
    "S0020_AURORA_FLASH",
    "S0021_SCARECROW_BIRDIES",
    "S0022_CORONA_DESCENDS",
    "S0023_SMALL_LASER",
    "S0024_NULL",
    "S0025_SLAP_BIG",
    "S0026_FLAME_WALL",
    "S0027_ITEM_1_UP",
    "S0028_FLAME",
    "S0029_FIRE_SHOOT",
    "S0030_FIRE_THROW",
    "S0031_FIRE_HIT",
    "S0032_FIRE_BURN",
    "S0033_INSERT",
    "S0034_",
    "S0035_SPELL_POWER_UP",
    "S0036_SNOW",
    "S0037_MONSTER_ITEM_TOSS",
    "S0038_FRYING_PAN_HIT_2",
    "S0039_CLAW",
    "S0040_PIERCE",
    "S0041_SUPER_JUMP_HIT_4",
    "S0042_BLADE",
    "S0043_COIN_SHOWERS_INTO_FOUNTAIN",
    "S0044_BOLT",
    "S0045_HP_RAIN_CLOUD",
    "S0046_PLASMA_BOUNCE",
    "S0047_DRY_CLUNK",
    "S0048_MALLOW_PUNCH_2",
    "S0049_CYMBAL_CRASH",
    "S0050_SUPER_JUMP_HIT_5",
    "S0051_FIRE_THROW_BIG",
    "S0052_FINGER_SHOT_BULLETS",
    "S0053_THWOMP_HIT_GROUND",
    "S0054_HAMMER_HIT_1",
    "S0055_HAMMER_HIT_2",
    "S0056_SUPER_JUMP_HIT_1_UP",
    "S0057_FIRE_SPOUT",
    "S0058_SUPER_JUMP_HIT_2",
    "S0059_SUPER_JUMP_HIT_3",
    "S0060_CYMBAL_RESONANCE",
    "S0061_ITEM_USE",
    "S0062_MONSTER_RUN_AWAY",
    "S0063_GENO_BLAST_IGNITION",
    "S0064_EGG_HATCH",
    "S0065_YOSHI_CANT_MAKE_COOKIE",
    "S0066_RECOVER_HP",
    "S0067_RECOVER_FP",
    "S0068_RECOVER_DRINK",
    "S0069_GENO_POWER_UP",
    "S0070_GENO_BEAM",
    "S0071_PSYCHOPATH_DRUM_ROLL",
    "S0072_PSYCHOPATH_CLOUD_APPEARS",
    "S0073_PSYCHOPATH_MESSAGE",
    "S0074_QUACK",
    "S0075_YOSHI_TALK",
    "S0076_STAT_BOOST_SINGLE",
    "S0077_STAT_BOOST_MULTI",
    "S0078_TIMED_STAT_BOOST",
    "S0079_RUMBLE_SINGLE",
    "S0080_WALLOP_1",
    "S0081_WALLOP_2",
    "S0082_WALLOP_3",
    "S0083_FRYING_PAN_HIT_1",
    "S0084_WALLOP_4",
    "S0085_WALLOP_5",
    "S0086_LONG_FALL",
    "S0087_BIG_BOUNCE",
    "S0088_TICKING_BOMB",
    "S0089_COMMON_MONSTER_EXPLOSION",
    "S0090_BIRDIE_CALL",
    "S0091_NULL",
    "S0092_SPEAR_RAIN_SINGLE",
    "S0093_BOWYER_ARROW_LOCK_BUTTON",
    "S0094_SHOCKER",
    "S0095_BOWSERS_CRUSHER",
    "S0096_RUMBLE_MULTI",
    "S0097_PLASMA_TOSS",
    "S0098_CLICK",
    "S0099_WILLY_WISP",
    "S0100_ELECTROSHOCK_SPARKS",
    "S0101_STENCH",
    "S0102_STATIC_E",
    "S0103_CRYSTAL_HITS",
    "S0104_BLIZZARD",
    "S0105_ROCK_CANDY",
    "S0106_LIGHT_BEAM",
    "S0107_BUBBLE_POP",
    "S0108_HOWL",
    "S0109_GENO_HAND_CANNON_SHOOT",
    "S0110_HUGE_EXPLOSION",
    "S0111_SLEDGE",
    "S0112_SWING",
    "S0113_GENO_FINGER_SHOT_HIT",
    "S0114_SPIKEY_ATTACK",
    "S0115_TRANSFORM",
    "S0116_TERRAPIN_SWING",
    "S0117_STING",
    "S0118_GENO_BLAST_END",
    "S0119_METEOR_SWARM",
    "S0120_DEEP_SWALLOW",
    "S0121_BIG_SWING",
    "S0122_POISONED",
    "S0123_CHOMP_BITE",
    "S0124_GOOMBA_ROLL",
    "S0125_SPIKE_SHOT",
    "S0126_FLOPPING_HIT",
    "S0127_LIQUID_DROPLET",
    "S0128_AMANITA_CURLS",
    "S0129_THROW",
    "S0130_VALOR_UP_VIGOR_UP",
    "S0131_ECHOING_BUBBLE",
    "S0132_STINGER_POISON",
    "S0133_LULLABY_SAD_SONG",
    "S0134_BOO_DISAPPEARS",
    "S0135_BOO_APPEARS",
    "S0136_BOO_APPROACHES",
    "S0137_BOWSER_CRUSH_STOMP",
    "S0138_ENDOBUBBLE",
    "S0139_GUITAR_STRING",
    "S0140_S_CROW_BELL",
    "S0141_LULLABY_MARIO_THEME",
    "S0142_DRY_BONES_ATTACK",
    "S0143_TOSS",
    "S0144_LIGHTNING_ORB",
    "S0145_ARTICHOKER_SPINES",
    "S0146_SLAP",
    "S0147_NULL",
    "S0148_SMITHY_BULLET_FINGERS",
    "S0149_ENEMY_JUMPS_HIGH",
    "S0150_ENEMY_TAUNTS_THEN_HITS",
    "S0151_SPORES",
    "S0152_HIT",
    "S0153_GUERRILLA_THINKS",
    "S0154_BUZZING_BEE",
    "S0155_SPARKY_HIT",
    "S0156_CHOMP_BITE",
    "S0157_ENIGMA_SCATTERS",
    "S0158_YELP",
    "S0159_BIG_DEEP_HIT",
    "S0160_SLAP",
    "S0161_SPORE_CHIMES_DOOM_REVERB",
    "S0162_NULL",
    "S0163_NULL",
    "S0164_CARROBOSCIS_ATTACK",
    "S0165_SKY_TROOPA_FLAPS",
    "S0166_TAPPING_FEET",
    "S0167_BELOME_EATS",
    "S0168_TERRAPIN_ATTACK",
    "S0169_TELEPORT_ATTACK",
    "S0170_SUBMERGED_UNDER",
    "S0171_SLAP_POWERFUL",
    "S0172_WEAPON_TIMING",
    "S0173_TERRORIZE",
    "S0174_SOLIDIFY",
    "S0175_DEATHSICKLE",
    "S0176_BOSS_FADE_OUT_DEATH",
    "S0177_POISON_GAS_1",
    "S0178_POISON_GAS_2",
    "S0179_SLEEPY_BOMB",
    "S0180_SLEEPY_TIME_TIMED",
    "S0181_LAMB_S_LURE_SINGLE",
    "S0182_SHEEP_ATTACK_1",
    "S0183_FLOATING_LAMB",
    "S0184_SHEEP_ATTACK_2_MULTI",
    "S0185_GENO_FLASH_SHOOT",
    "S0186_GENO_FLASH_EXPLOSION",
    "S0187_MUTE_BALLOON_RISES",
    "S0188_PETAL_BLAST",
    "S0189_POLLEN_NAP",
    "S0190_COME_BACK",
    "S0191_MUTE_BALLOON_FAILS",
    "S0192_BIG_SHELL_KICK",
    "S0193_BIG_SHELL_HIT_1",
    "S0194_BIG_SHELL_HIT_2",
    "S0195_EXPLOSIVE_HIT",
    "S0196_GENO_FLASH_TRANSFORMATION",
    "S0197_GENO_STAR_GUN_HIT",
    "S0198_ICE_ROCK",
    "S0199_ARROW_RAIN",
    "S0200_SPEAR_RAIN_MULTI",
    "S0201_SWORD_RAIN",
    "S0202_CORONA_FLASH",
    "S0203_MEGA_DRAIN_SINGLE",
    "S0204_CHOMPING",
    "S0205_JINXED",
    "S0206_MONSTER_SWING",
    "S0207_MONSTER_TAUNT",
    "S0208_SMITHY_FORM_1_LIGHT_UP",
    "S0209_SMITHY_FORM_1_TRANSFORM",
    "S0210_BOOSTER_EXPRESS_TRAIN_HORN",
]
MUSIC = [
    "M0000_CURRENT",
    "M0001_DODO_SCOMING",
    "M0002_MUSHROOMKINGDOM",
    "M0003_FIGHTAGAINSTSTRONGERMONSTER",
    "M0004_YO_STERISLAND",
    "M0005_SEASIDETOWN",
    "M0006_FIGHTAGAINSTMONSTERS",
    "M0007_PIPEVAULT",
    "M0008_INVINCIBLESTAR",
    "M0009_VICTORY",
    "M0010_INTHEFLOWERGARDEN",
    "M0011_BOWSER_SCASTLE_1STTIME",
    "M0012_FIGHTAGAINSTBOWSER",
    "M0013_ROADISFULLOFDANGERS",
    "M0014_MARIO_SPAD",
    "M0015_HERE_SSOMEWEAPONS",
    "M0016_LET_SRACE",
    "M0017_TADPOLEPOND",
    "M0018_ROSETOWN",
    "M0019_RACETRAINING",
    "M0020_SHOCK",
    "M0021_SADSONG",
    "M0022_MIDASRIVER",
    "M0023_GOTASTARPIECE_PART1",
    "M0024_GOTASTARPIECE_PART2",
    "M0025_FIGHTAGAINSTANARMEDBOSS",
    "M0026_FORESTMAZE",
    "M0027_DUNGEONISFULLOFMONSTERS",
    "M0028_LET_SPLAYGENO",
    "M0029_STARTSLOTMENU",
    "M0030_LONGLONGAGO",
    "M0031_BOOSTER_STOWER",
    "M0032_ANDMYNAME_SBOOSTER",
    "M0033_MOLEVILLE",
    "M0034_STARHILL",
    "M0035_MOUNTAINRAILROAD",
    "M0036_EXPLANATION",
    "M0037_BOOSTERHILL_START",
    "M0038_BOOSTERHILL",
    "M0039_MARRYMORE",
    "M0040_NEWPARTNER",
    "M0041_SUNKENSHIP",
    "M0042_STILLTHEROADISFULLOFMONSTERS",
    "M0043_SILENCE",
    "M0044_SEA",
    "M0045_HEARTBEATINGALITTLEFASTER_PART1",
    "M0046_HEARTBEATINGALITTLEFASTER_PART2",
    "M0047_GRATEGUY_SCASINO",
    "M0048_GENOAWAKENS",
    "M0049_CELEBRATIONAL",
    "M0050_NIMBUSLAND",
    "M0051_MONSTROTOWN",
    "M0052_TOADOFSKY",
    "M0053_SILENCE",
    "M0054_HAPPYADVENTURE_DELIGHFULADVENTURE",
    "M0055_WORLDMAP",
    "M0056_FACTORY",
    "M0057_SWORDCRASHESANDSTARSSCATTER",
    "M0058_CONVERSATIONWITHCULEX",
    "M0059_FIGHTAGAINSTCULEX",
    "M0060_VICTORYAGAINSTCULEX",
    "M0061_VALENTINA",
    "M0062_BARRELVOLCANO",
    "M0063_AXEMRANGERSDROPIN",
    "M0064_THEEND",
    "M0065_GATE",
    "M0066_BOWSER_SCASTLE_2NDTIME",
    "M0067_WEAPONSFACTORY",
    "M0068_FIGHTAGAINSTSMITHY1",
    "M0069_FIGHTAGAINSTSMITHY2",
    "M0070_ENDINGPART1",
    "M0071_ENDINGPART2",
    "M0072_ENDINGPART3",
    "M0073_ENDINGPART4",
]

TARGETS = [
    "MARIO",
    "TOADSTOOL",
    "BOWSER",
    "GENO",
    "MALLOW",
    "UNKNOWN_05",
    "UNKNOWN_06",
    "UNKNOWN_07",
    "UNKNOWN_08",
    "UNKNOWN_09",
    "UNKNOWN_10",
    "UNKNOWN_11",
    "UNKNOWN_12",
    "UNKNOWN_13",
    "UNKNOWN_14",
    "UNKNOWN_15",
    "CHARACTER_IN_SLOT_1",
    "CHARACTER_IN_SLOT_2",
    "CHARACTER_IN_SLOT_3",
    "MONSTER_1_SET",
    "MONSTER_2_SET",
    "MONSTER_3_SET",
    "MONSTER_4_SET",
    "MONSTER_5_SET",
    "MONSTER_6_SET",
    "MONSTER_7_SET",
    "MONSTER_8_SET",
    "SELF",
    "ALL_ALLIES_NOT_SELF",
    "RANDOM_ALLY_NOT_SELF",
    "ALL_ALLIES_AND_SELF",
    "RANDOM_ALLY_OR_SELF",
    "UNKNOWN_32",
    "UNKNOWN_33",
    "UNKNOWN_34",
    "ALL_OPPONENTS",
    "AT_LEAST_ONE_OPPONENT",
    "RANDOM_OPPONENT",
    "UNKNOWN_38",
    "AT_LEAST_ONE_ALLY",
    "MONSTER_1_CALL",
    "MONSTER_2_CALL",
    "MONSTER_3_CALL",
    "MONSTER_4_CALL",
    "MONSTER_5_CALL",
    "MONSTER_6_CALL",
    "MONSTER_7_CALL",
    "MONSTER_8_CALL",
]

ITEMS = [
    None,
    None,
    None,
    None,
    None,
    "Hammer",
    "FroggieStick",
    "NokNokShell",
    "PunchGlove",
    "FingerShot",
    "Cymbals",
    "Chomp",
    "Masher",
    "ChompShell",
    "SuperHammer",
    "HandGun",
    "WhompGlove",
    "SlapGlove",
    "TroopaShell",
    "Parasol",
    "HurlyGloves",
    "DoublePunch",
    "RibbitStick",
    "SpikedLink",
    "MegaGlove",
    "WarFan",
    "HandCannon",
    "StickyGlove",
    "UltraHammer",
    "SuperSlap",
    "DrillClaw",
    "StarGun",
    "SonicCymbal",
    "LazyShellWeapon",
    "FryingPan",
    "LuckyHammer",
    None,
    "Shirt",
    "Pants",
    "ThickShirt",
    "ThickPants",
    "MegaShirt",
    "MegaPants",
    "WorkPants",
    "MegaCape",
    "HappyShirt",
    "HappyPants",
    "HappyCape",
    "HappyShell",
    "PolkaDress",
    "SailorShirt",
    "SailorPants",
    "SailorCape",
    "NauticaDress",
    "CourageShell",
    "FuzzyShirt",
    "FuzzyPants",
    "FuzzyCape",
    "FuzzyDress",
    "FireShirt",
    "FirePants",
    "FireCape",
    "FireShell",
    "FireDress",
    "HeroShirt",
    "PrincePants",
    "StarCape",
    "HealShell",
    "RoyalDress",
    "SuperSuit",
    "LazyShellArmor",
    None,
    None,
    None,
    "ZoomShoes",
    "SafetyBadge",
    "JumpShoes",
    "SafetyRing",
    "Amulet",
    "ScroogeRing",
    "ExpBooster",
    "AttackScarf",
    "RareScarf",
    "BtubRing",
    "AntidotePin",
    "WakeUpPin",
    "FearlessPin",
    "TrueformPin",
    "CoinTrick",
    "GhostMedal",
    "JinxBelt",
    "Feather",
    "TroopaPin",
    "SignalRing",
    "QuartzCharm",
    None,
    "Mushroom",
    "MidMushroom",
    "MaxMushroom",
    "HoneySyrup",
    "MapleSyrup",
    "RoyalSyrup",
    "PickMeUp",
    "AbleJuice",
    "Bracer",
    "Energizer",
    "YoshiAde",
    "RedEssence",
    "KerokeroCola",
    "YoshiCookie",
    "PureWater",
    "SleepyBomb",
    "BadMushroom",
    "FireBomb",
    "IceBomb",
    "FlowerTab",
    "FlowerJar",
    "FlowerBox",
    "YoshiCandy",
    "FroggieDrink",
    "MukuCookie",
    "Elixir",
    "Megalixir",
    "SeeYa",
    "TempleKey",
    "GoodieBag",
    "EarlierTimes",
    "FreshenUp",
    "RareFrogCoin",
    "Wallet",
    "CricketPie",
    "RockCandy",
    "CastleKey1",
    None,
    "CastleKey2",
    "BambinoBomb",
    "SheepAttack",
    "CarboCookie",
    "ShinyStone",
    None,
    "RoomKey",
    "ElderKey",
    "ShedKey",
    "LambsLure",
    "FrightBomb",
    "MysteryEgg",
    None,
    None,
    "LuckyJewel",
    None,
    "SopranoCard",
    "AltoCard",
    "TenorCard",
    "Crystalline",
    "PowerBlast",
    "WiltShroom",
    "RottenMush",
    "MoldyMush",
    "Seed",
    "Fertilizer",
    "WasteBasket",
    "BigBooFlag",
    "DryBonesFlag",
    "GreaperFlag",
    None,
    None,
    "CricketJam",
    None,
    None,
    None,
    None,
    None,
    "Fireworks",
    None,
    "BrightCard",
    "Mushroom2",
    "StarEgg",
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    "Shoes",
    "Brooch",
    "Ring",
    "Crown",
]

MASKS = [
    "NO_MASK",
    "INCLINE_1",
    "INCLINE_2",
    "CIRCLE_MASK",
    "DOME_MASK",
    "POLYGON_MASK",
    "WAVY_CIRCLE_MASK",
    "CYLINDER_MASK",
]

ENEMIES = [
    "Terrapin",
    "Spikey",
    "Skytroopa",
    "MadMallet",
    "Shaman",
    "Crook",
    "Goomba",
    "PiranhaPlant",
    "Amanita",
    "Goby",
    "Bloober",
    "BandanaRed",
    "Lakitu",
    "Birdy",
    "Pinwheel",
    "Ratfunk",
    "K9",
    "Magmite",
    "TheBigBoo",
    "DryBones",
    "Greaper",
    "Sparky",
    "Chomp",
    "Pandorite",
    "ShyRanger",
    "BobombHenchman",
    "Spookum",
    "HammerBro",
    "Buzzer",
    "Ameboid",
    "Gecko",
    "Wiggler",
    "Crusty",
    "Magikoopa",
    "Leuko",
    "Jawful",
    "Enigma",
    "Blaster",
    "Guerrilla",
    "Babayaga",
    "Hobgoblin",
    "Reacher",
    "Shogun",
    "Orbuser",
    "HeavyTroopa",
    "Shadow",
    "Cluster",
    "BahamuttMagikoopa",
    "Octolot",
    "Frogog",
    "Clerk",
    "Gunyolk",
    "Boomer",
    "Remocon",
    "Snapdragon",
    "Stumpet",
    "Dodo",
    "Jester",
    "Artichoker",
    "Arachne",
    "Carriboscis",
    "Hippopo",
    "Mastadoom",
    "Corkpedite",
    "Terracotta",
    "Spikester",
    "Malakoopa",
    "Pounder",
    "Poundette",
    "Sackit",
    "GuGoomba",
    "Chewy",
    "Fireball",
    "CrookHenchman",
    "MrKipper",
    "FactoryChief",
    "BandanaBlue",
    "Manager",
    "Bluebird",
    "AlleyRat",
    "Chow",
    "Magmus",
    "LilBoo",
    "Vomer",
    "GlumReaper",
    "Pyrosphere",
    "ChompChomp",
    "Hidon",
    "SlingShy",
    "Robomb",
    "ShyGuy",
    "Ninja",
    "Stinger",
    "Goombette",
    "Geckit",
    "Jabit",
    "Starcruster",
    "Merlin",
    "Muckle",
    "Forkies",
    "Gorgon",
    "BigBertha",
    "ChainedKong",
    "Fautso",
    "Strawhead",
    "Juju",
    "ArmoredAnt",
    "Orbison",
    "TuboTroopa",
    "Doppel",
    "Pulsar",
    "Bobomb",
    "Octovader",
    "Ribbite",
    "Director",
    "SnifitHenchman",
    "None",
    "Puppox",
    "FinkFlower",
    "Lumbler",
    "Springer",
    "Harlequin",
    "Kriffid",
    "Spinthra",
    "Radish",
    "Crippo",
    "MastaBlasta",
    "Piledriver",
    "Apprentice",
    "ApprenticeHenchman",
    "BandanaRedHenchman",
    "PiranhaPlantHenchman",
    "None",
    "MadMalletHenchman",
    "BoxBoy",
    "Shelly",
    "Superspike",
    "DodoSolo",
    "Oerlikon",
    "Chester",
    "CorkpediteBody",
    "BluebirdHenchman",
    "Torte",
    "Shyaway",
    "JinxClone",
    "MachineMadeShyster",
    "MachineMadeDrillBit",
    "Formless",
    "Mokura",
    "FireCrystal",
    "WaterCrystal",
    "EarthCrystal",
    "WindCrystal",
    "MarioClone",
    "PeachClone",
    "BowserClone",
    "GenoClone",
    "MallowClone",
    "Shyster",
    "Kinklink",
    "BirdyHenchman",
    "HanginShy",
    "Smelter",
    "MachineMadeMack",
    "MachineMadeBowyer",
    "MachineMadeYaridovich",
    "MachineMadeAxemPink",
    "MachineMadeAxemBlack",
    "MachineMadeAxemRed",
    "MachineMadeAxemYellow",
    "MachineMadeAxemGreen",
    "BahamuttChester",
    "BlooberHenchman",
    "MachineMadeAxemBlackHenchman",
    "MachineMadeAxemPinkHenchman",
    "AeroSmithy",
    "Starslap",
    "Mukumuku",
    "Zeostar",
    "Jagger",
    "EmptyEnemy",
    "Smithy2TankHead",
    "Smithy2SafeHead",
    "PyrosphereHenchman",
    "Microbomb",
    "ShyGuyHenchman",
    "Grit",
    "Neosquid",
    "YaridovichMirage",
    "Helio",
    "RightEye",
    "LeftEye",
    "KnifeGuy",
    "GrateGuy",
    "Bundt",
    "Jinx1",
    "Jinx2",
    "CountDown",
    "DingALing",
    "Belome1",
    "Belome2",
    "MachineMadeAxemRedHenchman",
    "Smilax",
    "Thrax",
    "Megasmilax",
    "Birdo",
    "Eggbert",
    "AxemYellow",
    "Punchinello",
    "TentaclesRight",
    "AxemRed",
    "AxemGreen",
    "KingBomb",
    "MezzoBomb",
    "MachineMadeShysterHenchman",
    "Raspberry",
    "KingCalamari",
    "TentaclesLeft",
    "Jinx3",
    "Zombone",
    "CzarDragon",
    "Cloaker",
    "Domino",
    "MadAdder",
    "Mack",
    "Bodyguard",
    "Yaridovich",
    "DrillBit",
    "AxemPink",
    "AxemBlack",
    "Bowyer",
    "AeroBowyer",
    "MachineMadeAxemGreenHenchman",
    "Exor",
    "Smithy1",
    "Shyper",
    "Smithy2Body",
    "Smithy2Head",
    "Smithy2MageHead",
    "Smithy2ChestHead",
    "Croco1",
    "Croco2",
    "MachineMadeAxemYellowHenchman",
    "Earthlink",
    "YaridovichDrillBit",
    "AxemRangers",
    "Booster",
    "Booster2",
    "Snifit",
    "Johnny",
    "JohnnySolo",
    "Valentina",
    "Cloaker2",
    "Domino2",
    "Candle",
    "Culex",
]

SCRIPT_NAMES = {
    "battle_events": [
        "BE0000_UNUSED",
        "BE0001_UNUSED",
        "BE0002_BELOME_SWALLOWS_MALLOW",
        "BE0003_UNUSED",
        "BE0004_MACK_JUMPS_OUT_OF_BATTLE_OFF_SCREEN",
        "BE0005_MACK_RETURNS_TO_BATTLE",
        "BE0006_BELOME_SPITS_OUT_MALLOW",
        "BE0007_COUNTDOWN_RUNS_SCHEDULE_1_00_3_00_5_00_6_00_7_00",
        "BE0008_COUNTDOWN_RUNS_SCHEDULE_6_00_9_00_10_00_12_00",
        "BE0009_PUNCHINELLO_INTERLUDES_AND_PREPARES_TO_SUMMON_BOB_OMBS",
        "BE0010_PUNCHINELLO_INTERLUDES_AND_PREPARES_TO_SUMMON_MEZZO_BOMBS",
        "BE0011_SOLO_EARTH_CRYSTAL_APPEARS",
        "BE0012_DIALOGUE_FROM_BOOSTER_FIGHT",
        "BE0013_UNKNOWN",
        "BE0014_SET_7EE00A_TO_PARTY_SIZE_AT_START_OF_FIGHT",
        "BE0015_CROCO_STEALS_ITEMS_YOU_WANT_THEM_BACK",
        "BE0016_CROCO_RETURNS_ITEMS_ENOUGH_HERE_S_YOUR_JUNK",
        "BE0017_UNUSED",
        "BE0018_KNIFE_GUY_GRATE_GUY_PAIR_UP_PIGGY_BACK",
        "BE0019_KNIFE_GUY_GRATE_GUY_SEPARATE_YIKES_THEY_RE_PRETTY_TOUGH",
        "BE0020_SOLO_WATER_CRYSTAL_APPEARS",
        "BE0021_JOHNNY_CHALLENGES_MARIO_TO_A_ONE_ON_ONE",
        "BE0022_YARIDOVICH_MIRAGE_ATTACK",
        "BE0023_YARIDOVICH_MIRAGE_IS_DESTROYED_RETURN_TO_SINGLE_FORM",
        "BE0024_MACHINE_MADE_YARIDOVICH_MULTIPLIER",
        "BE0025_DRILL_BIT",
        "BE0026_INTRO_SCENE_TENTACLES_RISE_FROM_HOLES",
        "BE0027_BEAT_TENTACLES_MOVE_ON_TO_NEXT",
        "BE0028_BEAT_TENTACLES_MOVE_ON_TO_KING_CALAMARI",
        "BE0029_UNUSED",
        "BE0030_UNUSED",
        "BE0031_UNUSED",
        "BE0032_BUNDT_MOVES_AGAIN_BOTH_COOKS_RUN_AWAY",
        "BE0033_CANDLES_APPEAR_ON_BUNDT",
        "BE0034_BLOW_THOSE_CANDLES_OUT",
        "BE0035_SOLO_WIND_CRYSTAL_APPEARS",
        "BE0036_TENTACLES_THROW_CHARACTER_OFF_SCREEN",
        "BE0037_UNUSED",
        "BE0038_UNUSED",
        "BE0039_UNUSED",
        "BE0040_UNUSED",
        "BE0041_UNUSED",
        "BE0042_BB_BOMBS_EXPLODE",
        "BE0043_UNUSED",
        "BE0044_CZAR_DRAGON_DIES",
        "BE0045_ZOMBONE_DIES",
        "BE0046_CZAR_DRAGON_SUMMONS_HELIOS",
        "BE0047_UNKNOWN",
        "BE0048_VALENTINA_SUMMONS_DODO_DODO_CARRIES_OFF_MIDDLE_CHARACTER",
        "BE0049_DODO_FLUTTERS_AND_LEAVES_BATTLE",
        "BE0050_DODO_RETURNS_TO_VALENTINA_S_FORMATION",
        "BE0051_UNUSED",
        "BE0052_INTRO_SCENE_DOMINO_CLOAKER_S_INTRODUCTION",
        "BE0053_DOMINO_TEAMS_UP_WITH_MAD_ADDER",
        "BE0054_CLOAKER_TEAMS_UP_WITH_EARTHLINK",
        "BE0055_SHY_AWAY_WATERS_SMILAX_PART_1",
        "BE0056_SHY_AWAY_WATERS_SMILAX_PART_2",
        "BE0057_SHY_AWAY_WATERS_SMILAX_PART_3",
        "BE0058_THRAX_IS_THERE",
        "BE0059_BELOME_CONFRONTS_A_CHARACTER_YOU_ALL_LOOK_DELICIOUS",
        "BE0060_BELOME_CLONES_SOMEONE",
        "BE0061_ONLY_MARIO_IS_THERE",
        "BE0062_UNUSED",
        "BE0063_UNUSED",
        "BE0064_UNUSED",
        "BE0065_UNUSED",
        "BE0066_UNUSED",
        "BE0067_AXEM_RANGERS_GROUP_FORMATION",
        "BE0068_UNUSED",
        "BE0069_AXEM_RANGERS_ARE_DEFEATED",
        "BE0070_JINX_USES_JINXED",
        "BE0071_JINX_USES_TRIPLE_KICK",
        "BE0072_JINX_USES_QUICKSILVER",
        "BE0073_JINX_USES_BOMBS_AWAY",
        "BE0074_CULEX_SUMMONS_CRYSTALS",
        "BE0075_FORMLESS_CHANGES_INTO_MOKURA",
        "BE0076_SOLO_FIRE_CRYSTAL_APPEARS",
        "BE0077_SCREEN_FLASHES_WHITE",
        "BE0078_DODO_FLUTTERS_AND_EXITS_BATTLE",
        "BE0079_MAGIKOOPA_SUMMONS_MONSTER",
        "BE0080_EXOR_FIGHT_BEGINS",
        "BE0081_EXOR_IS_DEFEATED_CRIES_AND_OPENS_MOUTH",
        "BE0082_SMITHY_1ST_FORM_IS_BEATEN_GROUND_SHAKES_ETC",
        "BE0083_SCREEN_FLASHES_WHITE",
        "BE0084_SCREEN_FLASHES_WHITE",
        "BE0085_FEAR_ROULETTE",
        "BE0086_SMELTER_POURS_MOLTEN_LIQUID_SMITHY_WELDS",
        "BE0087_SMITHY_TRANSFORMS_INTO_TANK_HEAD",
        "BE0088_SMITHY_TRANSFORMS_INTO_MAGIC_HEAD",
        "BE0089_SMITHY_TRANSFORMS_INTO_CHEST_HEAD",
        "BE0090_SMITHY_TRANSFORMS_INTO_BOX_HEAD",
        "BE0091_SMITHY_S_HEAD_FADES_BEFORE_TRANSFORMING_INTO_OTHER_HEAD",
        "BE0092_SHELLY_BREAKS",
        "BE0093_BEAM_OF_LIGHT_FORMS_AROUND_SMITHY_HEAD_BEFORE_BODY_APPEARS",
        "BE0094_PUNCHINELLO_S_BOMBS_EXPLODE_IF_STILL_ALIVE",
        "BE0095_BOMBS_EXPLODE",
        "BE0096_NOTHING",
        "BE0097_SMITHY_WAITS_BEFORE_TRANSFORMING_HEAD",
        "BE0098_SMITHY_IS_DEFEATED",
        "BE0099_UNKNOWN",
        "BE0100_EARTHLINK_MAD_ADDER_COLLAPSES_AND_DIES",
        "BE0101_MAGIKOOPA_IS_THERE",
        "BE0102_NONE",
    ],
    "ally_spells": [
        "Jump",
        "Fire Orb",
        "Super Jump",
        "Super Flame",
        "Ultra Jump",
        "Ultra Flame",
        "Therapy",
        "Group Hug",
        "Sleepy Time",
        "Come Back",
        "Mute",
        "Psych Bomb",
        "Terrorize",
        "Poison Gas",
        "Crusher",
        "Bowser Crush",
        "Geno Beam",
        "Geno Boost",
        "Geno Whirl",
        "Geno Blast",
        "Geno Flash",
        "Thunderbolt",
        "HP Rain",
        "Psychopath",
        "Shocker",
        "Snowy",
        "Star Rain",
    ],
    "flower_bonus": [
        "(empty flower bonus message)",
        "Attack Up!",
        "Defense Up!",
        "HP Max!",
        "Once Again!",
        "Lucky!",
    ],
    "items": [  # offset 96
        "Mushroom",
        "MidMushroom",
        "MaxMushroom",
        "HoneySyrup",
        "MapleSyrup",
        "RoyalSyrup",
        "PickMeUp",
        "AbleJuice",
        "Bracer",
        "Energizer",
        "YoshiAde",
        "RedEssence",
        "KerokeroCola",
        "YoshiCookie",
        "PureWater",
        "SleepyBomb",
        "BadMushroom",
        "FireBomb",
        "IceBomb",
        "FlowerTab",
        "FlowerJar",
        "FlowerBox",
        "YoshiCandy",
        "FroggieDrink",
        "MukuCookie",
        "Elixir",
        "Megalixir",
        "SeeYa",
        "TempleKey",
        "GoodieBag",
        "EarlierTimes",
        "FreshenUp",
        "RareFrogCoin",
        "Wallet",
        "CricketPie",
        "RockCandy",
        "CastleKey1",
        "DebugBomb",
        "CastleKey2",
        "BambinoBomb",
        "SheepAttack",
        "CarboCookie",
        "ShinyStone",
        "DUMMY_43" "RoomKey",
        "ElderKey",
        "ShedKey",
        "LambsLure",
        "FrightBomb",
        "MysteryEgg",
        "BeetleBox",
        "BeetleBox2",
        "LuckyJewel",
        "DUMMY_53" "SopranoCard",
        "AltoCard",
        "TenorCard",
        "Crystalline",
        "PowerBlast",
        "WiltShroom",
        "RottenMush",
        "MoldyMush",
        "Seed",
        "Fertilizer",
        "WasteBasket",
        "BigBooFlag",
        "DryBonesFlag",
        "GreaperFlag",
        "SecretGame",
        "ScrowBomb",
        "CricketJam",
        "BaneBomb",
        "DoomBomb",
        "FearBomb",
        "SleepBomb",
        "MuteBomb",
        "Fireworks",
        "Bomb",
        "BrightCard",
        "Mushroom2",
        "StarEgg",
    ],
    "misses": [
        "Weapon",
        "Armor",
        "Accessory",
        "Space",
        "Space",
        "Hammer",
        "FroggieStick",
        "NokNokShell",
        "PunchGlove",
        "FingerShot",
        "Cymbals",
        "Chomp",
        "Masher",
        "ChompShell",
        "SuperHammer",
        "HandGun",
        "WhompGlove",
        "SlapGlove",
        "TroopaShell",
        "Parasol",
        "HurlyGloves",
        "DoublePunch",
        "RibbitStick",
        "SpikedLink",
        "MegaGlove",
        "WarFan",
        "HandCannon",
        "StickyGlove",
        "UltraHammer",
        "SuperSlap",
        "DrillClaw",
        "StarGun",
        "SonicCymbal",
        "LazyShellWeapon",
        "FryingPan",
        "LuckyHammer",
    ],
    "weapons": [
        "Weapon",
        "Armor",
        "Accessory",
        "Space",
        "Space",
        "Hammer",
        "FroggieStick",
        "NokNokShell",
        "PunchGlove",
        "FingerShot",
        "Cymbals",
        "Chomp",
        "Masher",
        "ChompShell",
        "SuperHammer",
        "HandGun",
        "WhompGlove",
        "SlapGlove",
        "TroopaShell",
        "Parasol",
        "HurlyGloves",
        "DoublePunch",
        "RibbitStick",
        "SpikedLink",
        "MegaGlove",
        "WarFan",
        "HandCannon",
        "StickyGlove",
        "UltraHammer",
        "SuperSlap",
        "DrillClaw",
        "StarGun",
        "SonicCymbal",
        "LazyShellWeapon",
        "FryingPan",
        "LuckyHammer",
    ],
    "monster_attacks": [
        "PhysicalAttack0",
        "PhysicalAttack2",
        "PhysicalAttack4",
        "PhysicalAttack5",
        "PhysicalAttack6",
        "PhysicalAttack7",
        "PhysicalAttack8",
        "PhysicalAttack9",
        "PhysicalAttack10",
        "PhysicalAttack11",
        "PhysicalAttack12",
        "PhysicalAttack15",
        "Thornet",
        "PhysicalAttack18",
        "Funguspike",
        "PhysicalAttack20",
        "PhysicalAttack21",
        "FullHouse",
        "WildCard",
        "RoyalFlush",
        "SpritzBomb",
        "PhysicalAttack27",
        "PhysicalAttack28",
        "PhysicalAttack29",
        "Blazer",
        "PhysicalAttack31",
        "PhysicalAttack32",
        "Echofinder",
        "ScrowBell",
        "DoomReverb",
        "SporeChimes",
        "InkBlast",
        "GunkBall",
        "Endobubble",
        "PhysicalAttack40",
        "VenomDrool",
        "MushFunk",
        "Stench",
        "PhysicalAttack46",
        "PhysicalAttack47",
        "ViroPlasm",
        "PsychoPlasm",
        "PhysicalAttack50",
        "PhysicalAttack51",
        "PollenNap",
        "ScrowDust",
        "Sporocyst",
        "Toxicyst",
        "PhysicalAttack56",
        "PhysicalAttack57",
        "LullaBye",
        "Elegy",
        "Backfire",
        "VaVaVoom",
        "FunRun",
        "BodySlam",
        "Howl",
        "Scream",
        "IronMaiden",
        "Fangs",
        "Poison",
        "CarniKiss",
        "Claw",
        "Grinder",
        "DarkClaw",
        "Scythe",
        "Sickle",
        "Deathsickle",
        "EerieJig",
        "SomnusWaltz",
        "DahliaDance",
        "Skewer",
        "Pierce",
        "PhysicalAttack81",
        "Magnum",
        "Psyche",
        "Migraine",
        "PhysicalAttack85",
        "PhysicalAttack86",
        "Multistrike",
        "FlutterHush",
        "PhysicalAttack89",
        "PhysicalAttack90",
        "PhysicalAttack91",
        "FearRoulette",
        "PhysicalAttack93",
        "PhysicalAttack94",
        "PhysicalAttack95",
        "ValorUp",
        "LastShot",
        "PhysicalAttack101",
        "PhysicalAttack105",
        "Gnight",
        "PhysicalAttack107",
        "PhysicalAttack108",
        "Chomp",
        "GetTough",
        "PhysicalAttack111",
        "Missedme",
        "PhysicalAttack113",
        "LocoExpress",
        "PhysicalAttack115",
        "PhysicalAttack116",
        "PhysicalAttack117",
        "PhysicalAttack118",
        "Jinxed",
        "TripleKick",
        "Quicksilver",
        "BombsAway",
        "Vigorup",
        "SilverBullet",
        "Terrapunch",
        "ScrowFangs",
        "Shaker",
    ],
    "monster_entrances": [
        "ENT0000_NONE",
        "ENT0001_SLIDE_IN",
        "ENT0002_LONG_JUMP",
        "ENT0003_HOP_3_TIMES",
        "ENT0004_DROP_FROM_ABOVE",
        "ENT0005_ZOOM_IN_FROM_RIGHT",
        "ENT0006_ZOOM_IN_FROM_LEFT",
        "ENT0007_SPREAD_OUT_FROM_BACK",
        "ENT0008_HOVER_IN",
        "ENT0009_READY_TO_ATTACK",
        "ENT0010_FADE_IN",
        "ENT0011_SLOW_DROP_FROM_ABOVE",
        "ENT0012_WAIT_THEN_APPEAR",
        "ENT0013_SPREAD_FROM_FRONT",
        "ENT0014_SPREAD_FROM_MIDDLE",
        "ENT0015_READY_TO_ATTACK",
    ],
    "monster_spells": [  # offset: 64
        "Drain",
        "LightningOrb",
        "Flame",
        "Bolt",
        "Crystal",
        "FlameStone",
        "MegaDrain",
        "WillyWisp",
        "DiamondSaw",
        "Electroshock",
        "Blast",
        "Storm",
        "IceRock",
        "Escape",
        "DarkStar",
        "Recover",
        "MegaRecover",
        "FlameWall",
        "StaticE",
        "SandStorm",
        "Blizzard",
        "DrainBeam",
        "MeteorBlast",
        "LightBeam",
        "WaterBlast",
        "Solidify",
        "PetalBlast",
        "AuroraFlash",
        "Boulder",
        "Corona",
        "MeteorSwarm",
        "KnockOut",
        "WeirdMushroom",
        "BreakerBeam",
        "Shredder",
        "Sledge",
        "SwordRain",
        "SpearRain",
        "ArrowRain",
        "BigBang",
        "ChestScrow",
        "ChestFear",
        "ChestMute",
        "ChestPoison",
        "ChainSaw",
    ],
}


searchable_vars = globals()


def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] == obj]


def get_var_name_string(id, prefix):
    candidates = namestr(id, searchable_vars)
    r = re.compile("^%s.*" % prefix)
    newlist = list(filter(r.match, candidates))
    if len(newlist) != 1:
        print("%s %r" % (prefix, id))
        raise Exception(newlist)
    return newlist[0]


def get_sprite_name(id):
    return get_var_name_string(id, "SPR")


banks = {
    "flower_bonus": {
        "pointers": {"start": 0x02F455, "end": 0x02F460},
        "start": 0x02F461,
        "end": 0x02F4A0,
    },
    "toad_tutorial": {"start": 0x02F4BF, "end": 0x02F50D},
    "monster_spells": {
        "pointers": {"start": 0x351026, "end": 0x35107F},
        "start": 0x351080,
        "end": 0x351492,
    },
    "monster_attacks": {
        "pointers": {"start": 0x351493, "end": 0x351594},
        "start": 0x351595,
        "end": 0x352127,
    },
    "monster_entrances": {
        "pointers": {"start": 0x352128, "end": 0x352147},
        "start": 0x352148,
        "end": 0x3523C3,
    },
    "misses": {
        "pointers": {"start": 0x35816D, "end": 0x3581B6},
        "start": 0x3581B7,
        "end": 0x35826E,
    },
    "items": {
        "pointers": {"start": 0x35C761, "end": 0x35C802},
        "start": 0x35C803,
        "end": 0x35C967,
    },
    "ally_spells": {
        "pointers": {
            "start": 0x35C992,
            "end": 0x35C9C7,  # NOTE: Adjusted due to cloen spells!
        },
        "start": 0x35C9C8,
        "end": 0x35CAAB,
    },
    "weapons": {
        "pointers": {"start": 0x35ECA2, "end": 0x35ECE9},
        "start": 0x35ECEA,
        "end": 0x35F111,
    },
    "battle_events": {
        "pointers": {"start": 0x3A6004, "end": 0x3A60CF},
        "start": 0x3A60D0,
        "end": 0x3A705C
        # "end": 0x3A7036,  # changed this cause i inserted a party size subroutine
    },
    "behaviour_0_0x3505C6": {"start": 0x3505C6, "end": 0x3505D9},
    "behaviour_1_0x3505DA": {"start": 0x3505DA, "end": 0x3505FD},
    "behaviour_2_0x350635": {"start": 0x350635, "end": 0x350668},
    "behaviour_3_0x350669": {"start": 0x350669, "end": 0x3506A6},
    "behaviour_4_0x3506A7": {"start": 0x3506A7, "end": 0x3506FF},
    "behaviour_5_0x350737": {"start": 0x350737, "end": 0x350758},
    "behaviour_6_0x350790": {"start": 0x350790, "end": 0x350795},
    "behaviour_7_0x350796": {"start": 0x350796, "end": 0x3507A1},
    "behaviour_8_0x3507A2": {"start": 0x3507A2, "end": 0x3507E8},
    "behaviour_9_0x3507E9": {"start": 0x3507E9, "end": 0x35082F},
    "behaviour_10_0x350830": {"start": 0x350830, "end": 0x350869},
    "behaviour_11_0x35086A": {"start": 0x35086A, "end": 0x350897},
    "behaviour_12_0x3508A4": {"start": 0x3508A4, "end": 0x3508B9},
    "behaviour_13_0x3508BA": {"start": 0x3508BA, "end": 0x3508DE},
    "behaviour_14_0x350916": {"start": 0x350916, "end": 0x35091B},
    "behaviour_15_0x35091C": {"start": 0x35091C, "end": 0x350927},
    "behaviour_16_0x350928": {"start": 0x350928, "end": 0x35096E},
    "behaviour_17_0x35096F": {"start": 0x35096F, "end": 0x3508B7},
    "behaviour_18_0x35099D": {"start": 0x35099D, "end": 0x3509D4},
    # Skip this one
    "behaviour_20_0x3509D5": {"start": 0x3509D5, "end": 0x350A00},
    "behaviour_21_0x350A38": {"start": 0x350A38, "end": 0x350A3D},
    "behaviour_22_0x350A3E": {"start": 0x350A3E, "end": 0x350A4E},
    "behaviour_23_0x350A55": {"start": 0x350A55, "end": 0x350A9B},
    "behaviour_24_0x350A9C": {"start": 0x350A9C, "end": 0x350ABC},
    "behaviour_25_0x350ABD": {"start": 0x350ABD, "end": 0x350AD2},
    "behaviour_26_0x350AF7": {"start": 0x350AF7, "end": 0x350B2C},
    "behaviour_27_0x350B2D": {"start": 0x350B2D, "end": 0x350B7F},
    "behaviour_28_0x350BB7": {"start": 0x350BB7, "end": 0x350BF2},
    "behaviour_29_0x350BF3": {"start": 0x350BF3, "end": 0x350BF8},
    "behaviour_30_0x350BF9": {"start": 0x350BF9, "end": 0x350BFC},
    "behaviour_31_0x350BFD": {"start": 0x350BFD, "end": 0x350C0D},
    "behaviour_32_0x350C14": {"start": 0x350C14, "end": 0x350C5A},
    "behaviour_33_0x350C5B": {"start": 0x350C5B, "end": 0x350C9D},
    "behaviour_34_0x350C9E": {"start": 0x350C9E, "end": 0x350CDB},
    "behaviour_35_0x350CDC": {"start": 0x350CDC, "end": 0x350CF1},
    "behaviour_36_0x350D22": {"start": 0x350D22, "end": 0x350D35},
    "behaviour_37_0x350D36": {"start": 0x350D36, "end": 0x350D71},
    "behaviour_38_0x350D72": {"start": 0x350D72, "end": 0x350D9C},
    "behaviour_39_0x350D9D": {"start": 0x350D9D, "end": 0x350DA2},
    "behaviour_40_0x350DA3": {"start": 0x350DA3, "end": 0x350DAE},
    "behaviour_41_0x350DAF": {"start": 0x350DAF, "end": 0x350DEC},
    "behaviour_42_0x350DED": {"start": 0x350DED, "end": 0x350E37},
    "behaviour_43_0x350E38": {"start": 0x350E38, "end": 0x350E49},
    "behaviour_44_0x350E4A": {"start": 0x350E4A, "end": 0x350E5F},
    "behaviour_45_0x350E84": {"start": 0x350E84, "end": 0x350E97},
    "behaviour_46_0x350E98": {"start": 0x350E98, "end": 0x350ED0},
    "behaviour_47_0x350EEE": {"start": 0x350EEE, "end": 0x350F19},
    "behaviour_48_0x350F1A": {"start": 0x350F1A, "end": 0x350F43},
    "behaviour_49_0x350F44": {"start": 0x350F44, "end": 0x350F49},
    "behaviour_50_0x350F4A": {"start": 0x350F4A, "end": 0x350F55},
    "behaviour_51_0x350F56": {"start": 0x350F56, "end": 0x350F6A},
    "behaviour_52_0x350F6B": {"start": 0x350F6B, "end": 0x350F79},
    "behaviour_53_0x350F7A": {"start": 0x350F7A, "end": 0x351025},
    # flower subroutines
    "subroutines_0x02f50e": {"start": 0x02F50E, "end": 0x02F51D},  # size:
    # battle behaviour subroutines
    "subroutines_0x350402": {
        "start": 0x350402,
        "end": 0x350467,
    },  # size:     102     95
    "subroutines_0x350606": {"start": 0x350606, "end": 0x350606},  # size:     1
    "subroutines_0x35061e": {"start": 0x35061E, "end": 0x3506FF},  # size:     226
    "subroutines_0x350761": {"start": 0x350761, "end": 0x350761},  # size:     1
    "subroutines_0x3508e7": {"start": 0x3508E7, "end": 0x3508E7},  # size:     1
    "subroutines_0x3508ff": {"start": 0x3508FF, "end": 0x350915},  # size:     134
    "subroutines_0x350a09": {"start": 0x350A09, "end": 0x350A09},  # size:     1
    "subroutines_0x350a21": {"start": 0x350A21, "end": 0x350A37},  # size:     46
    "subroutines_0x350b88": {"start": 0x350B88, "end": 0x350B88},  # size:     1
    "subroutines_0x3523C4": {"start": 0x3523C4, "end": 0x3523FC},  # size:     693
    "subroutines_0x350ED1": {"start": 0x350ED1, "end": 0x350EED},
    "subroutines_0x351080": {"start": 0x351080, "end": 0x351492},  # size:     1043
    # distance: 258
    "subroutines_0x351595": {"start": 0x351595, "end": 0x352127},  # size:     2963
    # distance: 32
    "subroutines_0x352148": {"start": 0x352148, "end": 0x3523FC},  # size:     693
    # distance: 15
    "subroutines_0x35240c": {"start": 0x35240C, "end": 0x352456},  # size:     75
    # distance: 30
    "subroutines_0x352475": {"start": 0x352475, "end": 0x352569},  # size:     245
    # distance: 12
    "subroutines_0x352576": {"start": 0x352576, "end": 0x3525A2},  # size:     45
    # distance: 50
    "subroutines_0x3525d5": {"start": 0x3525D5, "end": 0x3525DD},  # size:     9
    # distance: 216
    "subroutines_0x3526b6": {"start": 0x3526B6, "end": 0x3526BD},  # size:     8
    # distance: 98
    "subroutines_0x352720": {"start": 0x352720, "end": 0x352731},  # size:     18
    # distance: 158
    "subroutines_0x3527d0": {"start": 0x3527D0, "end": 0x3527D9},  # size:     10
    # distance: 780
    "subroutines_0x352ae6": {"start": 0x352AE6, "end": 0x352AED},  # size:     8
    # distance: 50
    "subroutines_0x352b20": {"start": 0x352B20, "end": 0x352B28},  # size:     9
    # distance: 216
    "subroutines_0x352c01": {"start": 0x352C01, "end": 0x352C08},  # size:     8
    # distance: 38
    "subroutines_0x352c2f": {"start": 0x352C2F, "end": 0x352C40},  # size:     18
    # distance: 38
    "subroutines_0x352c67": {"start": 0x352C67, "end": 0x352C78},  # size:     18
    # distance: 57
    "subroutines_0x352cb2": {"start": 0x352CB2, "end": 0x352CBA},  # size:     9
    # distance: 88
    "subroutines_0x352d13": {"start": 0x352D13, "end": 0x352D1A},  # size:     8
    # distance: 68
    "subroutines_0x352d5f": {"start": 0x352D5F, "end": 0x352D67},  # size:     9
    # distance: 88
    "subroutines_0x352dc0": {"start": 0x352DC0, "end": 0x352DC7},  # size:     8
    # distance: 57
    "subroutines_0x352e01": {"start": 0x352E01, "end": 0x352E09},  # size:     9
    # distance: 85
    "subroutines_0x352e5f": {"start": 0x352E5F, "end": 0x352E66},  # size:     8
    # distance: 86
    "subroutines_0x352ebd": {"start": 0x352EBD, "end": 0x352ECE},  # size:     18
    # distance: 86
    "subroutines_0x352f25": {"start": 0x352F25, "end": 0x3530F2},  # size:     462
    # distance: 72
    "subroutines_0x35313b": {"start": 0x35313B, "end": 0x3531ED},  # size:     15
    # distance: 61
    "subroutines_0x3531f8": {"start": 0x3531F8, "end": 0x3532D0},  # size:     217
    # distance: 158
    "subroutines_0x35336f": {"start": 0x35336F, "end": 0x35342B},  # size:     189
    # distance: 11
    "subroutines_0x353437": {"start": 0x353437, "end": 0x353705},  # size:     719
    # distance: 88
    "subroutines_0x35375e": {"start": 0x35375E, "end": 0x353963},  # size:     518
    # distance: 14
    "subroutines_0x353972": {"start": 0x353972, "end": 0x353ACE},  # size:     349
    # distance: 18
    "subroutines_0x353ae1": {"start": 0x353AE1, "end": 0x353C6F},  # size:     399
    # distance: 18
    "subroutines_0x353c82": {"start": 0x353C82, "end": 0x353DCB},  # size:     330
    # distance: 14
    "subroutines_0x353dda": {"start": 0x353DDA, "end": 0x353F10},  # size:     311
    # distance: 42
    "subroutines_0x353f3b": {"start": 0x353F3B, "end": 0x353F6A},  # size:     48
    # distance: 22
    "subroutines_0x353f81": {"start": 0x353F81, "end": 0x3540AF},  # size:     303
    # distance: 26
    "subroutines_0x3540ca": {"start": 0x3540CA, "end": 0x3542BE},  # size:     501
    # distance: 30
    "subroutines_0x3542dd": {"start": 0x3542DD, "end": 0x3542FF},  # size:     35
    # distance: 6
    "subroutines_0x354306": {"start": 0x354306, "end": 0x3543B8},  # size:     179
    # distance: 14
    "subroutines_0x3543c7": {"start": 0x3543C7, "end": 0x35458B},  # size:     453
    # distance: 18
    "subroutines_0x35459e": {"start": 0x35459E, "end": 0x3547C1},  # size:     548
    # distance: 56
    "subroutines_0x3547fa": {"start": 0x3547FA, "end": 0x354891},  # size:     152
    # distance: 42
    "subroutines_0x3548bc": {"start": 0x3548BC, "end": 0x3548F3},  # size:     56
    # distance: 12
    "subroutines_0x354900": {"start": 0x354900, "end": 0x354914},  # size:     21
    # distance: 35
    "subroutines_0x354938": {"start": 0x354938, "end": 0x354A17},  # size:     224
    # distance: 12
    "subroutines_0x354a24": {"start": 0x354A24, "end": 0x354AF3},  # size:     208
    # distance: 23
    "subroutines_0x354b0b": {"start": 0x354B0B, "end": 0x354B30},  # size:     38
    # distance: 4
    "subroutines_0x354b35": {"start": 0x354B35, "end": 0x354BB3},  # size:     127
    # distance: 6
    "subroutines_0x354bba": {"start": 0x354BBA, "end": 0x354C83},  # size:     202
    # distance: 6
    "subroutines_0x354c8a": {"start": 0x354C8A, "end": 0x354CF8},  # size:     111
    # distance: 14
    "subroutines_0x354d07": {"start": 0x354D07, "end": 0x354E00},  # size:     250
    # distance: 30
    "subroutines_0x354e1f": {"start": 0x354E1F, "end": 0x354E6B},  # size:     77
    # distance: 6
    "subroutines_0x354e72": {"start": 0x354E72, "end": 0x354F10},  # size:     159
    # distance: 8
    "subroutines_0x354f19": {"start": 0x354F19, "end": 0x354FC3},  # size:     171
    # distance: 24
    "subroutines_0x354fdc": {"start": 0x354FDC, "end": 0x3551CA},  # size:     495
    # distance: 210
    "subroutines_0x3551fe": {"start": 0x3551FE, "end": 0x355233},  # size:     54
    "subroutines_0x35529d": {"start": 0x35529D, "end": 0x3552C4},  # size:     40
    # distance: 12
    "subroutines_0x3552d1": {"start": 0x3552D1, "end": 0x355498},  # size:     456
    # distance: 217
    "subroutines_0x35549d": {"start": 0x35549D, "end": 0x35554D},  # size:     177
    # distance: 12
    "subroutines_0x35555a": {"start": 0x35555A, "end": 0x3555B5},  # size:     92
    # distance: 2
    "subroutines_0x3555b8": {"start": 0x3555B8, "end": 0x3555D4},  # size:     29
    # distance: 12
    "subroutines_0x3555e1": {"start": 0x3555E1, "end": 0x3556E2},  # size:     258
    # distance: 10
    "subroutines_0x3556ed": {"start": 0x3556ED, "end": 0x3557C5},  # size:     217
    # distance: 8
    "subroutines_0x3557ce": {"start": 0x3557CE, "end": 0x3558A7},  # size:     218
    # distance: 8
    "subroutines_0x3558b0": {"start": 0x3558B0, "end": 0x355950},  # size:     161
    # distance: 8
    "subroutines_0x355959": {"start": 0x355959, "end": 0x3559EF},  # size:     151
    # distance: 12
    "subroutines_0x3559fc": {"start": 0x3559FC, "end": 0x355AD8},  # size:     221
    # distance: 251
    "subroutines_0x355bd4": {"start": 0x355BD4, "end": 0x355DB5},  # size:     482
    # distance: 4
    "subroutines_0x355dba": {"start": 0x355DBA, "end": 0x355E00},  # size:     71
    # distance: 14
    "subroutines_0x355e0f": {"start": 0x355E0F, "end": 0x355F1C},  # size:     270
    # distance: 239
    "subroutines_0x35600c": {"start": 0x35600C, "end": 0x356040},  # size:     53
    # distance: 2
    "subroutines_0x356043": {"start": 0x356043, "end": 0x35605E},  # size:     28
    # distance: 2
    "subroutines_0x356061": {"start": 0x356061, "end": 0x356075},  # size:     21
    # distance: 2
    "subroutines_0x356078": {"start": 0x356078, "end": 0x356086},  # size:     15
    # distance: 2
    "subroutines_0x356089": {"start": 0x356089, "end": 0x3560A8},  # size:     32
    # distance: 2
    "subroutines_0x3560ab": {"start": 0x3560AB, "end": 0x3560CC},  # size:     34
    # distance: 51
    "subroutines_0x356100": {"start": 0x356100, "end": 0x356130},  # size:     49
    # distance: 2
    "subroutines_0x356133": {"start": 0x356133, "end": 0x356151},  # size:     31
    # distance: 2
    "subroutines_0x356154": {"start": 0x356154, "end": 0x356179},  # size:     38
    # distance: 2
    "subroutines_0x35617c": {"start": 0x35617C, "end": 0x3561AC},  # size:     49
    # distance: 2
    "subroutines_0x3561af": {"start": 0x3561AF, "end": 0x3561DF},  # size:     49
    # distance: 145
    "subroutines_0x356271": {"start": 0x356271, "end": 0x3563A5},  # size:     309
    # distance: 63
    "subroutines_0x3563e5": {"start": 0x3563E5, "end": 0x356455},  # size:     113
    # distance: 129
    "subroutines_0x3564d7": {"start": 0x3564D7, "end": 0x35651C},  # size:     70
    # distance: 8
    "subroutines_0x356525": {"start": 0x356525, "end": 0x35659F},  # size:     123
    # distance: 2
    "subroutines_0x3565a2": {"start": 0x3565A2, "end": 0x3565FE},  # size:     93
    # distance: 80
    "subroutines_0x35664f": {"start": 0x35664F, "end": 0x3566BE},  # size:     112
    # distance: 149
    "subroutines_0x356754": {"start": 0x356754, "end": 0x35678A},  # size:     55
    # distance: 108
    "subroutines_0x3567f7": {"start": 0x3567F7, "end": 0x35682A},  # size:     52
    # distance: 6
    "subroutines_0x356831": {"start": 0x356831, "end": 0x356918},  # size:     232
    # distance: 2
    "subroutines_0x35691b": {"start": 0x35691B, "end": 0x356968},  # size:     78
    # distance: 2
    "subroutines_0x35696b": {"start": 0x35696B, "end": 0x3569A9},  # size:     63
    # distance: 122
    "subroutines_0x356a24": {"start": 0x356A24, "end": 0x356A7D},  # size:     90
    # distance: 4
    "subroutines_0x356a82": {"start": 0x356A82, "end": 0x356B14},  # size:     147
    # distance: 54
    "subroutines_0x356b4b": {"start": 0x356B4B, "end": 0x356B65},  # size:     27
    # distance: 32
    "subroutines_0x356b86": {"start": 0x356B86, "end": 0x356BF1},  # size:     108
    # distance: 20
    "subroutines_0x356c06": {"start": 0x356C06, "end": 0x356C87},  # size:     130
    # distance: 410
    "subroutines_0x356e22": {"start": 0x356E22, "end": 0x356EAF},  # size:     142
    # distance: 6
    "subroutines_0x356eb6": {"start": 0x356EB6, "end": 0x356F14},  # size:     95
    # distance: 32
    "subroutines_0x356f35": {"start": 0x356F35, "end": 0x357345},  # size:     1041
    # distance: 2
    "subroutines_0x357348": {"start": 0x357348, "end": 0x357399},  # size:     82
    # distance: 18
    "subroutines_0x3573ac": {"start": 0x3573AC, "end": 0x3575FB},  # size:     592
    # distance: 8
    "subroutines_0x357604": {"start": 0x357604, "end": 0x3576B7},  # size:     180
    # distance: 6
    "subroutines_0x3576be": {"start": 0x3576BE, "end": 0x3578B3},  # size:     502
    # distance: 61
    "subroutines_0x3578f1": {"start": 0x3578F1, "end": 0x35791C},  # size:     44
    # distance: 1
    "subroutines_0x35791e": {"start": 0x35791E, "end": 0x35794F},  # size:     50
    # distance: 1
    "subroutines_0x357951": {"start": 0x357951, "end": 0x3579A0},  # size:     80
    # distance: 1
    "subroutines_0x3579a2": {"start": 0x3579A2, "end": 0x357AE3},  # size:     322
    # distance: 1
    "subroutines_0x357ae5": {"start": 0x357AE5, "end": 0x357B71},  # size:     141
    # distance: 1
    "subroutines_0x357b73": {"start": 0x357B73, "end": 0x357C43},  # size:     209
    # distance: 19
    "subroutines_0x357c57": {"start": 0x357C57, "end": 0x357CF5},  # size:     159
    # distance: 21
    "subroutines_0x357d0b": {"start": 0x357D0B, "end": 0x357F73},  # size:     617
    # distance: 44
    "subroutines_0x357fa0": {"start": 0x357FA0, "end": 0x357FE1},  # size:     66
    # distance: 22
    "subroutines_0x357ff8": {"start": 0x357FF8, "end": 0x358071},  # size:     122
    # distance: 20
    "subroutines_0x358086": {"start": 0x358086, "end": 0x35809C},  # size:     23
    # distance: 23
    "subroutines_0x3580b4": {"start": 0x3580B4, "end": 0x358132},  # size:     127
    # distance: 51
    "subroutines_0x358166": {"start": 0x358166, "end": 0x35816A},  # size:     5
    # distance: 76
    "subroutines_0x358323": {"start": 0x358323, "end": 0x35837B},  # size:     89
    # distance: 6
    "subroutines_0x358382": {"start": 0x358382, "end": 0x3583DA},  # size:     89
    # distance: 6
    "subroutines_0x3583e1": {"start": 0x3583E1, "end": 0x358439},  # size:     89
    # distance: 6
    "subroutines_0x358440": {"start": 0x358440, "end": 0x358498},  # size:     89
    # distance: 38
    "subroutines_0x3584bf": {"start": 0x3584BF, "end": 0x358684},  # size:     454
    # distance: 56
    "subroutines_0x3586bd": {"start": 0x3586BD, "end": 0x3588DE},  # size:     546
    # distance: 21
    "subroutines_0x3588f4": {"start": 0x3588F4, "end": 0x358915},  # size:     34
    # distance: 889
    "subroutines_0x358c8f": {"start": 0x358C8F, "end": 0x35924B},  # size:     1469
    # distance: 6
    "subroutines_0x359252": {"start": 0x359252, "end": 0x359396},  # size:     325
    # distance: 12
    "subroutines_0x3593a3": {"start": 0x3593A3, "end": 0x3595C0},  # size:     542
    # distance: 6
    "subroutines_0x3595c7": {"start": 0x3595C7, "end": 0x3597EC},  # size:     550
    # distance: 10
    "subroutines_0x3597f7": {"start": 0x3597F7, "end": 0x3599E5},  # size:     495
    # distance: 4
    "subroutines_0x3599ea": {"start": 0x3599EA, "end": 0x359C08},  # size:     543
    # distance: 10
    "subroutines_0x359c13": {"start": 0x359C13, "end": 0x359E0A},  # size:     504
    # distance: 12
    "subroutines_0x359e17": {"start": 0x359E17, "end": 0x359F19},  # size:     259
    # distance: 18
    "subroutines_0x359f2c": {"start": 0x359F2C, "end": 0x35A0A4},  # size:     377
    # distance: 34
    "subroutines_0x35a0c7": {"start": 0x35A0C7, "end": 0x35A2FF},  # size:     569
    # distance: 161
    "subroutines_0x35a3a1": {"start": 0x35A3A1, "end": 0x35A3B7},  # size:     23
    # distance: 105
    "subroutines_0x35a421": {"start": 0x35A421, "end": 0x35A48E},  # size:     110
    # distance: 79
    "subroutines_0x35a4de": {"start": 0x35A4DE, "end": 0x35A4E6},  # size:     9
    # distance: 20
    "subroutines_0x35a4fb": {"start": 0x35A4FB, "end": 0x35A69F},  # size:     421
    # distance: 1
    "subroutines_0x35a6a1": {"start": 0x35A6A1, "end": 0x35A770},  # size:     208
    # distance: 12
    "subroutines_0x35a77d": {"start": 0x35A77D, "end": 0x35A97B},  # size:     511
    # distance: 18
    "subroutines_0x35a98e": {"start": 0x35A98E, "end": 0x35ABAC},  # size:     543
    # distance: 44
    "subroutines_0x35abd9": {"start": 0x35ABD9, "end": 0x35ABF5},  # size:     29
    # distance: 90
    "subroutines_0x35ac50": {"start": 0x35AC50, "end": 0x35AC58},  # size:     9
    # distance: 12
    "subroutines_0x35ac65": {"start": 0x35AC65, "end": 0x35AD49},  # size:     229
    # distance: 18
    "subroutines_0x35ad5c": {"start": 0x35AD5C, "end": 0x35B019},  # size:     702
    # distance: 30
    "subroutines_0x35b038": {"start": 0x35B038, "end": 0x35B35C},  # size:     805
    # distance: 8
    "subroutines_0x35b365": {"start": 0x35B365, "end": 0x35B43C},  # size:     216
    # distance: 50
    "subroutines_0x35b46f": {"start": 0x35B46F, "end": 0x35B5FF},  # size:     401
    # distance: 96
    "subroutines_0x35b660": {"start": 0x35B660, "end": 0x35B944},  # size:     741
    # distance: 90
    "subroutines_0x35b99f": {"start": 0x35B99F, "end": 0x35B9A7},  # size:     9
    # distance: 10
    "subroutines_0x35b9b2": {"start": 0x35B9B2, "end": 0x35BA90},  # size:     97
    # distance: 10
    "subroutines_0x35ba9b": {"start": 0x35BA9B, "end": 0x35BBC6},  # size:     300
    # distance: 38
    "subroutines_0x35bbed": {"start": 0x35BBED, "end": 0x35BE03},  # size:     535
    # distance: 10
    "subroutines_0x35be0e": {"start": 0x35BE0E, "end": 0x35BEAF},  # size:     162
    # distance: 8
    "subroutines_0x35beb8": {"start": 0x35BEB8, "end": 0x35BF61},  # size:     170
    # distance: 14
    "subroutines_0x35bf70": {"start": 0x35BF70, "end": 0x35C123},  # size:     436
    # distance: 10
    "subroutines_0x35c12e": {"start": 0x35C12E, "end": 0x35C292},  # size:     357
    # distance: 10
    "subroutines_0x35c29d": {"start": 0x35C29D, "end": 0x35C2DC},  # size:     64
    # distance: 42
    "subroutines_0x35c307": {"start": 0x35C307, "end": 0x35C362},  # size:     92
    # distance: 10
    "subroutines_0x35c36d": {"start": 0x35C36D, "end": 0x35C4BD},  # size:     337
    # distance: 8
    "subroutines_0x35c4c6": {"start": 0x35C4C6, "end": 0x35C5FD},  # size:     312
    # distance: 6
    "subroutines_0x35c604": {"start": 0x35C604, "end": 0x35C685},  # size:     130
    # distance: 4
    "subroutines_0x35c68a": {"start": 0x35C68A, "end": 0x35C711},  # size:     136
    # distance: 13
    "subroutines_0x35c71f": {"start": 0x35C71F, "end": 0x35C760},  # size:     66
    # distance: 162
    "subroutines_0x35c968": {"start": 0x35C968, "end": 0x35C991},  # size:     399
    # distance: 54
    "subroutines_0x35caac": {"start": 0x35CAAC, "end": 0x35CF28},  # size:     1377
    # distance: 12
    "subroutines_0x35cf35": {"start": 0x35CF35, "end": 0x35D186},  # size:     594
    # distance: 10
    "subroutines_0x35d191": {"start": 0x35D191, "end": 0x35D1FD},  # size:     109
    # distance: 10
    "subroutines_0x35d208": {"start": 0x35D208, "end": 0x35D2D4},  # size:     205
    # distance: 14
    "subroutines_0x35d2e3": {"start": 0x35D2E3, "end": 0x35D38D},  # size:     171
    # distance: 1
    "subroutines_0x35d38f": {"start": 0x35D38F, "end": 0x35D45C},  # size:     206
    # distance: 16
    "subroutines_0x35d46d": {"start": 0x35D46D, "end": 0x35D74A},  # size:     734
    # distance: 20
    "subroutines_0x35d75f": {"start": 0x35D75F, "end": 0x35DAD8},  # size:     890
    # distance: 10
    "subroutines_0x35dae3": {"start": 0x35DAE3, "end": 0x35DB50},  # size:     110
    # distance: 12
    "subroutines_0x35db5d": {"start": 0x35DB5D, "end": 0x35DC6B},  # size:     271
    # distance: 4
    "subroutines_0x35dc70": {"start": 0x35DC70, "end": 0x35DC8E},  # size:     31
    # distance: 4
    "subroutines_0x35dc93": {"start": 0x35DC93, "end": 0x35DCB1},  # size:     31
    # distance: 4
    "subroutines_0x35dcb6": {"start": 0x35DCB6, "end": 0x35DCD4},  # size:     31
    # distance: 20
    "subroutines_0x35dce9": {"start": 0x35DCE9, "end": 0x35DCFC},  # size:     20
    # distance: 4
    "subroutines_0x35dd01": {"start": 0x35DD01, "end": 0x35DFC7},  # size:     711
    # distance: 6
    "subroutines_0x35dfce": {"start": 0x35DFCE, "end": 0x35E044},  # size:     119
    # distance: 4
    "subroutines_0x35e049": {"start": 0x35E049, "end": 0x35E07B},  # size:     51
    # distance: 26
    "subroutines_0x35e096": {"start": 0x35E096, "end": 0x35E5D7},  # size:     1346
    # distance: 8
    "subroutines_0x35e5e0": {"start": 0x35E5E0, "end": 0x35E758},  # size:     377
    # distance: 20
    "subroutines_0x35e76d": {"start": 0x35E76D, "end": 0x35E865},  # size:     249
    # distance: 6
    "subroutines_0x35e86c": {"start": 0x35E86C, "end": 0x35E9C2},  # size:     343
    # distance: 4
    "subroutines_0x35e9c7": {"start": 0x35E9C7, "end": 0x35EA0B},  # size:     69
    # distance: 10
    "subroutines_0x35ea16": {"start": 0x35EA16, "end": 0x35EAF8},  # size:     227
    # distance: 14
    "subroutines_0x35eb07": {"start": 0x35EB07, "end": 0x35ECA1},  # size:     411
    # distance: 72
    "subroutines_0x35f112": {"start": 0x35F112, "end": 0x35F123},  # size:     1082
    # distance: 4
    "subroutines_0x35f128": {"start": 0x35F128, "end": 0x35F136},  # size:     15
    # distance: 8
    "subroutines_0x35f13f": {"start": 0x35F13F, "end": 0x35F1BD},  # size:     127
    # distance: 6
    "subroutines_0x35f1c4": {"start": 0x35F1C4, "end": 0x35F214},  # size:     81
    # distance: 4
    "subroutines_0x35f219": {"start": 0x35F219, "end": 0x35F262},  # size:     74
    # distance: 4
    "subroutines_0x35f267": {"start": 0x35F267, "end": 0x35F2B0},  # size:     74
    # distance: 4
    "subroutines_0x35f2b5": {"start": 0x35F2B5, "end": 0x35F2FE},  # size:     74
    # distance: 6
    "subroutines_0x35f305": {"start": 0x35F305, "end": 0x35F35E},  # size:     90
    # distance: 10
    "subroutines_0x35f369": {"start": 0x35F369, "end": 0x35F390},  # size:     40
    # distance: 6
    "subroutines_0x35f397": {"start": 0x35F397, "end": 0x35F3E7},  # size:     81
    # distance: 6
    "subroutines_0x35f3ee": {"start": 0x35F3EE, "end": 0x35F43E},  # size:     81
    # distance: 6
    "subroutines_0x35f445": {"start": 0x35F445, "end": 0x35F49D},  # size:     89
    # distance: 4
    "subroutines_0x35f4a2": {"start": 0x35F4A2, "end": 0x35F4A8},  # size:     7
    # distance: 6
    "subroutines_0x35f4af": {"start": 0x35F4AF, "end": 0x35F541},  # size:     147
    # distance: 6
    "subroutines_0x35f548": {"start": 0x35F548, "end": 0x35F5E3},  # size:     156
    # distance: 8
    "subroutines_0x35f5ec": {"start": 0x35F5EC, "end": 0x35F729},  # size:     318
    # distance: 8
    "subroutines_0x35f732": {"start": 0x35F732, "end": 0x35F782},  # size:     81
    # distance: 8
    "subroutines_0x35f78b": {"start": 0x35F78B, "end": 0x35F816},  # size:     140
    # distance: 14
    "subroutines_0x35f825": {"start": 0x35F825, "end": 0x35F92B},  # size:     263
    # distance: 4
    "subroutines_0x35f930": {"start": 0x35F930, "end": 0x35F965},  # size:     54
    # distance: 4
    "subroutines_0x35f96a": {"start": 0x35F96A, "end": 0x35F9A1},  # size:     56
    # distance: 18
    "subroutines_0x35f9b4": {"start": 0x35F9B4, "end": 0x35FA94},  # size:     225
    # distance: 66
    "subroutines_0x35fad7": {"start": 0x35FAD7, "end": 0x35FC88},  # size:     434
    # distance: 6
    "subroutines_0x35fc8f": {"start": 0x35FC8F, "end": 0x35FD47},  # size:     185
    # distance: 4
    "subroutines_0x35fd4c": {"start": 0x35FD4C, "end": 0x35FD8F},  # size:     68
    # distance: 10
    "subroutines_0x35fd9a": {"start": 0x35FD9A, "end": 0x35FEEA},  # size:     337
    # "subroutines_0x3a60d0": {"start": 0x3A647C, "end": 0x3A6493},  # size:     718
    # distance: 205
    "subroutines_0x3a711f": {"start": 0x3A711F, "end": 0x3A715C},  # size:     62
    # distance: 125
    "subroutines_0x3a71da": {"start": 0x3A71DA, "end": 0x3A72B5},  # size:     220
    # distance: 24
    "subroutines_0x3a72ce": {"start": 0x3A72CE, "end": 0x3A7327},  # size:     90
    # distance: 11
    "subroutines_0x3a7333": {"start": 0x3A7333, "end": 0x3A751A},  # size:     488
    # distance: 22
    "subroutines_0x3a7531": {"start": 0x3A7531, "end": 0x3A7551},  # size:     33
    # distance: 12
    "subroutines_0x3a755e": {"start": 0x3A755E, "end": 0x3A76F3},  # size:     406
    # distance: 14
    "subroutines_0x3a7702": {"start": 0x3A7702, "end": 0x3A785C},  # size:     347
    # distance: 11
    "subroutines_0x3a7868": {"start": 0x3A7868, "end": 0x3A7885},  # size:     30
    # distance: 50
    "subroutines_0x3a78b8": {"start": 0x3A78B8, "end": 0x3A78C0},  # size:     9
    # distance: 216
    "subroutines_0x3a7999": {"start": 0x3A7999, "end": 0x3A79A0},  # size:     8
    # distance: 98
    "subroutines_0x3a7a03": {"start": 0x3A7A03, "end": 0x3A7A14},  # size:     18
    # distance: 126
    "subroutines_0x3a7a93": {"start": 0x3A7A93, "end": 0x3A7A9B},  # size:     9
    # distance: 558
    "subroutines_0x3a7cca": {"start": 0x3A7CCA, "end": 0x3A7CD1},  # size:     8
    # distance: 50
    "subroutines_0x3a7d04": {"start": 0x3A7D04, "end": 0x3A7D0C},  # size:     9
    # distance: 216
    "subroutines_0x3a7de5": {"start": 0x3A7DE5, "end": 0x3A7DEC},  # size:     8
    # distance: 38
    "subroutines_0x3a7e13": {"start": 0x3A7E13, "end": 0x3A7E24},  # size:     18
    # distance: 38
    "subroutines_0x3a7e4b": {"start": 0x3A7E4B, "end": 0x3A7E5C},  # size:     18
    # distance: 57
    "subroutines_0x3a7e96": {"start": 0x3A7E96, "end": 0x3A7EA6},  # size:     17
    # distance: 62
    "subroutines_0x3a7ee5": {"start": 0x3A7EE5, "end": 0x3A7EFE},  # size:     26
    # distance: 68
    "subroutines_0x3a7f43": {"start": 0x3A7F43, "end": 0x3A7F53},  # size:     17
    # distance: 62
    "subroutines_0x3a7f92": {"start": 0x3A7F92, "end": 0x3A7FAB},  # size:     26
    # distance: 57
    "subroutines_0x3a7fe5": {"start": 0x3A7FE5, "end": 0x3A7FF5},  # size:     17
    # distance: 68
    "subroutines_0x3a803a": {"start": 0x3A803A, "end": 0x3A804A},  # size:     17
    # distance: 68
    "subroutines_0x3a808f": {"start": 0x3A808F, "end": 0x3A8097},  # size:     9
    # distance: 20
    "subroutines_0x3a80ac": {"start": 0x3A80AC, "end": 0x3A80B5},  # size:     10
    # distance: 60
    "subroutines_0x3a80f2": {"start": 0x3A80F2, "end": 0x3A80FB},  # size:     10
    # distance: 10
    "subroutines_0x3a8106": {"start": 0x3A8106, "end": 0x3A812D},  # size:     40
    # distance: 20
    "subroutines_0x3a8142": {"start": 0x3A8142, "end": 0x3A8155},  # size:     20
    # distance: 10
    "subroutines_0x3a8160": {"start": 0x3A8160, "end": 0x3A8169},  # size:     10
    # distance: 10
    "subroutines_0x3a8174": {"start": 0x3A8174, "end": 0x3A817D},  # size:     10
    # distance: 20
    "subroutines_0x3a8192": {"start": 0x3A8192, "end": 0x3A81B9},  # size:     40
    # distance: 10
    "subroutines_0x3a81c4": {"start": 0x3A81C4, "end": 0x3A81EB},  # size:     40
    # distance: 10
    "subroutines_0x3a81f6": {"start": 0x3A81F6, "end": 0x3A821D},  # size:     40
    # distance: 20
    "subroutines_0x3a8232": {"start": 0x3A8232, "end": 0x3A823B},  # size:     10
    # distance: 40
    "subroutines_0x3a8264": {"start": 0x3A8264, "end": 0x3A826D},  # size:     10
    # distance: 20
    "subroutines_0x3a8282": {"start": 0x3A8282, "end": 0x3A829F},  # size:     30
    # distance: 10
    "subroutines_0x3a82aa": {"start": 0x3A82AA, "end": 0x3A82C7},  # size:     30
    # distance: 10
    "subroutines_0x3a82d2": {"start": 0x3A82D2, "end": 0x3A82E5},  # size:     20
    # distance: 20
    "subroutines_0x3a82fa": {"start": 0x3A82FA, "end": 0x3A8303},  # size:     10
    # distance: 30
    "subroutines_0x3a8322": {"start": 0x3A8322, "end": 0x3A832B},  # size:     10
    # distance: 10
    "subroutines_0x3a8336": {"start": 0x3A8336, "end": 0x3A8349},  # size:     20
    # distance: 10
    "subroutines_0x3a8354": {"start": 0x3A8354, "end": 0x3A835D},  # size:     10
    # distance: 250
    "subroutines_0x3a8458": {"start": 0x3A8458, "end": 0x3A8461},  # size:     10
    # distance: 130
    "subroutines_0x3a84e4": {"start": 0x3A84E4, "end": 0x3A84ED},  # size:     10
    # distance: 60
    "subroutines_0x3a852a": {"start": 0x3A852A, "end": 0x3A853D},  # size:     20
    # distance: 30
    "subroutines_0x3a855c": {"start": 0x3A855C, "end": 0x3A8579},  # size:     30
    # distance: 10
    "subroutines_0x3a8584": {"start": 0x3A8584, "end": 0x3A858D},  # size:     10
    # distance: 40
    "subroutines_0x3a85b6": {"start": 0x3A85B6, "end": 0x3A85BF},  # size:     10
    # distance: 180
    "subroutines_0x3a8674": {"start": 0x3A8674, "end": 0x3A867F},  # size:     12
    # distance: 24
    "subroutines_0x3a8698": {"start": 0x3A8698, "end": 0x3A87BB},  # size:     292
    # distance: 150
    "subroutines_0x3a8852": {"start": 0x3A8852, "end": 0x3A8891},  # size:     64
    # distance: 2
    "subroutines_0x3a8894": {"start": 0x3A8894, "end": 0x3A88DE},  # size:     75
    # distance: 32
    "subroutines_0x3a88ff": {"start": 0x3A88FF, "end": 0x3A8A67},  # size:     361
    # distance: 22
    "subroutines_0x3a8a7e": {"start": 0x3A8A7E, "end": 0x3A8ABF},  # size:     66
    # distance: 40
    "subroutines_0x3a8ae8": {"start": 0x3A8AE8, "end": 0x3A8BB0},  # size:     201
    # distance: 51
    "subroutines_0x3a8be4": {"start": 0x3A8BE4, "end": 0x3A8C89},  # size:     166
    # distance: 22
    "subroutines_0x3a8ca0": {"start": 0x3A8CA0, "end": 0x3A8E6F},  # size:     464
    # distance: 8
    "subroutines_0x3a8e78": {"start": 0x3A8E78, "end": 0x3A9523},  # size:     1708
    # distance: 14
    "subroutines_0x3a9532": {"start": 0x3A9532, "end": 0x3A96B8},  # size:     391
    # distance: 4
    "subroutines_0x3a96bd": {"start": 0x3A96BD, "end": 0x3A971C},  # size:     96
    # distance: 8
    "subroutines_0x3a9725": {"start": 0x3A9725, "end": 0x3A97CD},  # size:     169
    # distance: 4
    "subroutines_0x3a97d2": {"start": 0x3A97D2, "end": 0x3A985B},  # size:     138
    # distance: 14
    "subroutines_0x3a986a": {"start": 0x3A986A, "end": 0x3A9D74},  # size:     1291
    # distance: 6
    "subroutines_0x3a9d7b": {"start": 0x3A9D7B, "end": 0x3A9EB6},  # size:     316
    # distance: 10
    "subroutines_0x3a9ec1": {"start": 0x3A9EC1, "end": 0x3A9F8A},  # size:     202
    # distance: 8
    "subroutines_0x3a9f93": {"start": 0x3A9F93, "end": 0x3AA069},  # size:     215
    # distance: 6
    "subroutines_0x3aa070": {"start": 0x3AA070, "end": 0x3AA140},  # size:     209
    # distance: 58
    "subroutines_0x3aa17b": {"start": 0x3AA17B, "end": 0x3AA242},  # size:     200
    # distance: 69
    "subroutines_0x3aa288": {"start": 0x3AA288, "end": 0x3AA53E},  # size:     695
    # distance: 127
    "subroutines_0x3aa5be": {"start": 0x3AA5BE, "end": 0x3AA655},  # size:     152
    # distance: 81
    "subroutines_0x3aa6a7": {"start": 0x3AA6A7, "end": 0x3AA8EC},  # size:     582
    # distance: 5
    "subroutines_0x3aa8f2": {"start": 0x3AA8F2, "end": 0x3ABBC1},  # size:     4816
    # distance: 4
    "subroutines_0x3abbc6": {"start": 0x3ABBC6, "end": 0x3AC146},  # size:     1409
    # distance: 1
    "subroutines_0x3ac148": {"start": 0x3AC148, "end": 0x3AC1EF},  # size:     168
    # distance: 1
    "subroutines_0x3ac1f1": {"start": 0x3AC1F1, "end": 0x3AC777},  # size:     1415
    # distance: 29
    "subroutines_0x3ac795": {"start": 0x3AC795, "end": 0x3AC7B1},  # size:     29
    # distance: 29
    "subroutines_0x3ac7cf": {"start": 0x3AC7CF, "end": 0x3ACCAF},  # size:     1249
    # distance: 1
    "subroutines_0x3accb1": {"start": 0x3ACCB1, "end": 0x3ACF43},  # size:     659
    # distance: 4
    "subroutines_0x3acf48": {"start": 0x3ACF48, "end": 0x3AD6F3},  # size:     1964
    # distance: 15
    "subroutines_0x3ad703": {"start": 0x3AD703, "end": 0x3AECF6},  # size:     3239
}

# Subroutines in item animations aren't actually disassembled.
# ie star egg references 0x35CEFC


command_lens = [
    9,
    8,
    1,
    6,
    4,
    1,
    6,
    1,
    8,
    3,
    1,
    8,
    6,
    1,
    1,
    1,  # 0x00
    3,
    1,
    2,
    1,
    1,
    1,
    1,
    1,
    3,
    1,
    2,
    2,
    2,
    1,
    2,
    2,  # 0x10
    4,
    4,
    4,
    4,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    4,
    4,
    4,
    4,  # 0x20
    2,
    2,
    2,
    2,
    2,
    2,
    3,
    3,
    5,
    5,
    1,
    1,
    3,
    1,
    1,
    6,  # 0x30
    3,
    3,
    8,
    2,
    2,
    1,
    1,
    4,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,  # 0x40
    3,
    3,
    5,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    3,
    1,
    5,
    1,
    1,  # 0x50
    1,
    1,
    1,
    2,
    3,
    1,
    1,
    1,
    4,
    1,
    3,
    4,
    1,
    1,
    1,
    1,  # 0x60
    1,
    1,
    3,
    1,
    3,
    3,
    1,
    2,
    2,
    5,
    3,
    1,
    1,
    1,
    2,
    1,  # 0x70
    4,
    1,
    1,
    2,
    3,
    3,
    7,
    1,
    1,
    1,
    2,
    5,
    1,
    1,
    3,
    2,  # 0x80
    1,
    1,
    1,
    1,
    1,
    1,
    5,
    1,
    1,
    1,
    1,
    5,
    9,
    2,
    3,
    1,  # 0x90
    1,
    1,
    5,
    2,
    1,
    1,
    1,
    3,
    3,
    1,
    1,
    2,
    1,
    1,
    2,
    1,  # 0xA0
    2,
    4,
    1,
    1,
    1,
    1,
    3,
    1,
    1,
    1,
    4,
    2,
    3,
    3,
    3,
    2,  # 0xB0
    5,
    1,
    1,
    2,
    1,
    1,
    10,
    2,
    2,
    2,
    1,
    2,
    1,
    1,
    8,
    6,  # 0xC0
    4,
    1,
    2,
    4,
    6,
    4,
    1,
    1,
    3,
    1,
    1,
    2,
    1,
    6,
    1,
    1,  # 0xD0
    1,
    4,
    1,
    1,
    1,
    2,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,  # 0xE0
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,  # 0xF0
]

# command_lens = [
#   9, 8, 1, 6, 4, 1, 6, 1, 8, 3, 1, 8, 6, 1, 1, 1, # 0x00
#   3, 1, 2, 1, 1, 1, 1, 1, 3, 1, 2, 2, 2, 1, 2, 2, # 0x10
#   4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4, # 0x20
#   2, 2, 2, 2, 2, 2, 3, 3, 5, 5, 1, 1, 3, 1, 1, 6, # 0x30
#   3, 3, 8, 2, 2, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, # 0x40
#   3, 3, 5, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 5, 1, 1, # 0x50
#   1, 1, 1, 2, 3, 1, 1, 1, 4, 1, 3, 4, 1, 1, 1, 1, # 0x60
#   1, 1, 3, 1, 3, 3, 1, 2, 2, 5, 3, 1, 1, 1, 2, 1, # 0x70
#   4, 1, 1, 2, 3, 3, 7, 1, 1, 1, 2, 5, 1, 1, 3, 2, # 0x80
#   1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 5, 9, 2, 3, 1, # 0x90
#   1, 1, 5, 2, 1, 1, 1, 3, 3, 1, 1, 2, 1, 1, 2, 1, # 0xA0
#   2, 4, 1, 1, 1, 1, 3, 1, 1, 1, 4, 2, 3, 3, 3, 2, # 0xB0
#   5, 1, 1, 2, 1, 1,10, 2, 2, 2, 1, 2, 1, 1, 8, 6, # 0xC0
#   4, 1, 2, 4, 6, 4, 1, 1, 3, 1, 1, 2, 1, 6, 1, 1, # 0xD0
#   1, 4, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, # 0xE0
#   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  # 0xF0
# ]


def tok(rom, start, end, bank):
    dex = start
    script = []
    while dex <= end:
        cmd = rom[dex]
        l = command_lens[cmd]
        bytestring = [("0x%02x" % i) for i in rom[dex : dex + l]]
        # print('0x%06x' % dex, bytestring)
        script.append((rom[dex : dex + l], dex))
        dex += l
    return script


jmp_cmds = [
    0x09,
    0x10,
    0x24,
    0x25,
    0x26,
    0x27,
    0x28,
    0x29,
    0x2A,
    0x2B,
    0x38,
    0x39,
    0x50,
    0x51,
    0x5D,
    0x64,
    0x68,
    0xCE,
    0xCF,
    0xD0,
    0xD8,
]

jmp_cmds_1 = [0x68]


def string_byte(word):
    # print(type(word))
    if type(word) == str:
        return '''"%s"''' % word
    else:
        return "0x%02x" % word


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("-r", "--rom", dest="rom", help="Path to a Mario RPG rom")

        parser.add_argument(
            "-d",
            "--debug",
            action="store_true",
            help="If set, dumps to a gitignored folder instead of overwriting the scripts sourced by SMRPG Randomizer",
        )

    def handle(self, *args, **options):
        debug = options["debug"]

        global rom
        rom = bytearray(open(options["rom"], "rb").read())

        scripts_data = []
        commands_by_address = {}

        scripts = []

        relevant_pointers = []

        known_addresses_covered = {
            "02": [False] * 0x10000,
            "35": [False] * 0x10000,
            "3A": [False] * 0x10000,
        }

        scripts_with_headers = {"22": [], "70": [], "85": []}

        SPECIAL_CASE_BREAKS = [
            0x356076,
            0x356087,
            0x3560A9,
            0x3560CD,
            0x3560FE,
            0x356131,
            0x356152,
            0x35617A,
            0x3561AD,
            0x3561E0,
            0x356213,
            0x35624B,
            0x3A8A68,
            0x3A8AC0,
            0x3A8C8A,
        ]

        collective_data = {"35": [], "3A": [], "02": []}
        queue_addresses = {"35": [], "3A": [], "02": []}
        separated_data = {}

        references = {}
        references_by_bank = {}

        for key, bank in banks.items():

            hint = ""
            coverage = "35"
            if "subroutine" in key:
                coverage = key[-6:-4].upper()
            elif key == "battle_events":
                coverage = "3A"
                hint = key
            elif key in ["toad_tutorial", "flower_bonus"]:
                coverage = "02"
                hint = key
            else:
                hint = key

            # print(key)
            # print('\n\n\n')

            bank_num = bank["start"] & 0xFF0000

            ptrs = []
            cmd_lengths = []

            data = []

            addresses_to_jump_to = []

            offset = 0
            if key == "battle_events":
                offset = 2

            amem = [0] * 16
            if "pointers" in bank:
                for ind, i in enumerate(
                    range(bank["pointers"]["start"], bank["pointers"]["end"], 2)
                ):
                    ptrs.append(shortify(rom, i) + bank_num)
                    addresses_to_jump_to.append(
                        (
                            shortify(rom, i) + bank_num,
                            deepcopy(amem),
                            "%s %s"
                            % (
                                hint,
                                str(ind)
                                if ind >= len(SCRIPT_NAMES[key])
                                else SCRIPT_NAMES[key][ind],
                            ),
                            [],
                        )
                    )
                for i in range(len(ptrs)):
                    this_script = []
                    if i < len(ptrs) - 1:
                        cmd_lengths.append(ptrs[i + 1] - ptrs[i])
                    else:
                        cmd_lengths.append(bank["end"] - ptrs[i] + 1)
                    offset_2 = 0
            else:
                addresses_to_jump_to.append((bank["start"], deepcopy(amem), hint, []))

            searching: bool = True
            i: int = 0
            while searching:

                extra_offset = 0
                if key == "battle_events" and i in [22]:
                    extra_offset = 2
                    base_header_ptr = (
                        shortify(rom, bank["pointers"]["start"] + i * 2) + bank_num
                    )
                    scripts_with_headers["22"].append(
                        shortify(rom, base_header_ptr + 2) + bank_num
                    )
                elif key == "battle_events" and i in [70, 85]:
                    base_header_ptr = (
                        shortify(rom, bank["pointers"]["start"] + i * 2) + bank_num
                    )
                    extra_offset = 4
                    if i == 70:
                        scripts_with_headers["70"].append(
                            shortify(rom, base_header_ptr + 2) + bank_num
                        )
                        scripts_with_headers["70"].append(
                            shortify(rom, base_header_ptr + 4) + bank_num
                        )
                    if i == 85:
                        scripts_with_headers["85"].append(
                            shortify(rom, base_header_ptr + 2) + bank_num
                        )
                        scripts_with_headers["85"].append(
                            shortify(rom, base_header_ptr + 4) + bank_num
                        )

                end_found = False
                amem = deepcopy(addresses_to_jump_to[i][1])
                is_subroutine = True
                if "pointers" in bank and (i < len(cmd_lengths)):
                    is_subroutine = False
                    addr = addresses_to_jump_to[i][0] + offset + extra_offset
                    # print(
                    #     "%s script %i: searching 0x%06X, amem = %r (script length %i)"
                    #     % (key, i, addr, amem, cmd_lengths[i])
                    # )
                else:
                    addr = addresses_to_jump_to[i][0] + extra_offset
                    # print("%s searching 0x%06X, amem = %r" % (key, addr, amem))
                current_addr = addr
                if addr not in references:
                    references[addr] = []
                references[addr].extend(addresses_to_jump_to[i][3])
                references[addr] = list(set(references[addr]))

                while not end_found:
                    opcode = rom[current_addr]
                    length = command_lens[opcode]
                    command = rom[current_addr : current_addr + length]
                    cvr_range = current_addr & 0xFFFF

                    # if current_addr <= 0x300000:
                    #     print(
                    #         "     0x%06X, 0x%02X, %i" % (current_addr, opcode, length)
                    #     )

                    if "pointers" in bank and (i < len(cmd_lengths)):
                        for c in range(cvr_range - offset, cvr_range + length):
                            known_addresses_covered[coverage][c] = True
                    else:
                        for c in range(cvr_range, cvr_range + length):
                            known_addresses_covered[coverage][c] = True

                    # if opcode in [
                    #     0x20,
                    #     0x21,
                    #     0x22,
                    #     0x23,
                    #     0x2C,
                    #     0x2D,
                    #     0x2E,
                    #     0x2F,
                    #     0x30,
                    #     0x31,
                    #     0x32,
                    #     0x33,
                    #     0x34,
                    #     0x35,
                    #     0x6A,
                    #     0x6B,
                    # ]:
                    # if addr == 0x3A88FF:
                    #     print(
                    #         "0x%06x: opcode 0x%02X, cmd length %i, cmd %r"
                    #         % (
                    #             current_addr,
                    #             opcode,
                    #             length,
                    #             [f"0x{c:02x}" for c in command],
                    #         )
                    #     )

                    # set amem
                    if opcode in [0x20, 0x21]:
                        if command[1] & 0x30 == 0x30:
                            index1 = command[2]
                            index2 = command[1] & 0x0F
                            if index1 <= 0x0F:
                                amem[index2] = amem[index1]
                        elif command[1] & 0x30 == 0x00 and command[1] <= 0x0F:
                            amem[command[1]] = shortify(command, 2)
                    elif opcode in [0x22, 0x23] and command[1] & 0x30 == 0x30:
                        index1 = command[2]
                        index2 = command[1] & 0x0F
                        if index1 <= 0x0F:
                            amem[index1] = amem[index2]
                    elif opcode in [0x2C, 0x2D]:
                        if command[1] & 0x30 == 0x30:
                            index1 = command[2]
                            index2 = command[1] & 0x0F
                            if index1 <= 0x0F:
                                amem[index2] += amem[index1]
                        elif command[1] & 0x30 == 0x00 and command[1] <= 0x0F:
                            amem[command[1]] += shortify(command, 2)
                    elif opcode in [0x2E, 0x2F]:
                        if command[1] & 0x30 == 0x30:
                            index1 = command[2]
                            index2 = command[1] & 0x0F
                            if index1 <= 0x0F:
                                amem[index2] -= amem[index1]
                        elif command[1] & 0x30 == 0x00 and command[1] <= 0x0F:
                            amem[command[1]] -= shortify(command, 2)
                    elif opcode in [0x30, 0x31] and command[1] <= 0x0F:
                        amem[command[1]] += 1
                    elif opcode in [0x32, 0x33] and command[1] <= 0x0F:
                        amem[command[1]] -= 1
                    elif opcode in [0x34, 0x35] and command[1] <= 0x0F:
                        amem[command[1]] = 0
                    elif opcode in [0x6A, 0x6B] and command[1] <= 0x0F:
                        amem[command[1]] = max(0, command[2] - 1)

                    amem_was = deepcopy(amem)

                    jump_voided = False

                    if opcode in jmp_cmds or opcode in jmp_cmds_1:
                        if opcode in jmp_cmds_1:
                            address_byte = command[-3:-1]
                        else:
                            address_byte = command[-2:]

                        target_addr = (
                            bank_num + (address_byte[1] << 8) + address_byte[0]
                        )
                        # if target_addr >= 0x3AD703:
                        #     print(
                        #         "1",
                        #         hex(addr),
                        #         addresses_to_jump_to[i][1],
                        #         addresses_to_jump_to[i][2],
                        #         addresses_to_jump_to[i][3],
                        #     )

                        important_amem_indexes = [0]

                        if opcode in [36, 37]:
                            index1 = command[1]
                            important_amem_indexes.append(index1 & 0x0F)
                            if command[1] & 0xF0 == 0:
                                amem[index1] = shortify(command, 2)
                            # if command[1] & 0xF0 == 0 and amem[index1] != shortify(
                            #     command, 2
                            # ):
                            # jump_voided = True
                            # pass
                            elif command[1] & 0xF0 == 3:
                                index2 = command[2]
                                # important_amem_indexes.append(index2 & 0x0F)
                                amem[index1] = amem[index2]
                                # if index2 <= 0x0F and amem[index1] != amem[index2]:
                                # jump_voided = True
                                # pass
                        elif opcode in [38, 39]:
                            index1 = command[1]
                            important_amem_indexes.append(index1 & 0x0F)
                            if command[1] & 0xF0 == 0:
                                amem[index1] = abs(shortify(command, 2) - 1)
                            # if command[1] & 0xF0 == 0 and amem[index1] == shortify(
                            #     command, 2
                            # ):
                            # jump_voided = True
                            # pass
                            elif command[1] & 0xF0 == 3:
                                index2 = command[2]
                                # important_amem_indexes.append(index2 & 0x0F)
                                amem[index1] = abs(amem[index2] - 1)
                                # if index2 <= 0x0F and amem[index1] == amem[index2]:
                                # jump_voided = True
                                # pass
                        elif opcode in [40, 41]:
                            index1 = command[1]
                            important_amem_indexes.append(index1 & 0x0F)
                            if command[1] & 0xF0 == 0:
                                amem[index1] = shortify(command, 2) - 1
                            # if command[1] & 0xF0 == 0 and amem[index1] >= shortify(
                            #     command, 2
                            # ):
                            # jump_voided = True
                            # pass
                            elif command[1] & 0xF0 == 3:
                                index2 = command[2]
                                # important_amem_indexes.append(index2 & 0x0F)
                                amem[index1] = amem[index2] - 1
                                # if index2 <= 0x0F and amem[index1] >= amem[index2]:
                                # jump_voided = True
                                # pass
                        elif opcode in [42, 43]:
                            index1 = command[1]
                            important_amem_indexes.append(index1 & 0x0F)
                            if command[1] & 0xF0 == 0:
                                amem[index1] = shortify(command, 2)
                            # if command[1] & 0xF0 == 0 and amem[index1] < shortify(
                            #     command, 2
                            # ):
                            # jump_voided = True
                            # pass
                            elif command[1] & 0xF0 == 3:
                                index2 = command[2]
                                # important_amem_indexes.append(index2 & 0x0F)
                                amem[index1] = amem[index2]
                                # if index2 <= 0x0F and amem[index1] < amem[index2]:
                                # jump_voided = True
                                # pass
                        elif opcode == 56:
                            index1 = command[1]
                            important_amem_indexes.append(index1 & 0x0F)
                            amem[index1] = command[2]
                            # if amem[index1] & command[2] != command[2]:
                            # jump_voided = True
                            # pass
                        elif opcode == 57:
                            index1 = command[1]
                            important_amem_indexes.append(index1 & 0x0F)
                            amem[index1] = ~command[2]
                            # if amem[index1] | ~command[2] != ~command[2]:
                            # jump_voided = True
                            # pass
                        elif opcode == 0x64:
                            if amem[0] >= 0x10:
                                amem[0] = 0
                            target_addr = (target_addr & 0xFF0000) + shortify(
                                rom, target_addr + amem[0] * 2
                            )
                        elif opcode == 0x68:
                            if amem[0] >= 0x40:
                                amem[0] = 0
                            target_addr = (target_addr & 0xFF0000) + shortify(
                                rom, target_addr + amem[0] * 2
                            )
                            if target_addr in [0x356919, 0x356969]:
                                target_addr += 2
                            else:
                                target_addr = (target_addr & 0xFF0000) + shortify(
                                    rom, target_addr + command[3]
                                )
                        if target_addr >= bank_num + 0x10000:
                            raise Exception("illegal addr 0x%06x" % target_addr)
                        dc = deepcopy(addresses_to_jump_to[i][3])
                        if (
                            "subroutine" not in addresses_to_jump_to[i][2]
                            and addresses_to_jump_to[i][2] != ""
                        ):
                            dc.append(addresses_to_jump_to[i][2])
                        if target_addr not in references:
                            references[target_addr] = []
                        references[target_addr].append(addresses_to_jump_to[i][2])
                        references[target_addr] = list(set(references[target_addr]))
                        # if target_addr >= 0x3AD703:
                        #     print("2", hex(target_addr), references[target_addr])
                        tup = (target_addr, deepcopy(amem), "", dc)
                        # if current_addr <= 0x300000:
                        #     print(f"0x{opcode:02X}", important_amem_indexes)
                        for t in [
                            t for t in addresses_to_jump_to if t[0] == target_addr
                        ]:
                            same_amem_count = 0
                            for a in important_amem_indexes:
                                if t[1][a] == amem[a]:
                                    same_amem_count += 1
                            if same_amem_count == len(important_amem_indexes):
                                jump_voided = True
                                break

                        if not jump_voided:
                            addresses_to_jump_to.append(tup)
                            if opcode in [0x68, 0x64, 0x5D]:
                                queue_addresses[coverage].append(hex(target_addr))
                            # if 0x350000 <= current_addr <= 0x352000:
                            #     print(
                            #         "new    (by 0x%02X @ 0x%02X): (0x%06X, %r)"
                            #         % (opcode, current_addr, tup[0], tup[1][0])
                            #     )
                        else:
                            pass
                            # if 0x350000 <= current_addr <= 0x352000:
                            #     print(
                            #         "exists (by 0x%02X @ 0x%02X): (0x%06X, %r)"
                            #         % (opcode, current_addr, tup[0], tup[1][0])
                            #     )
                        amem = deepcopy(amem_was)

                    if opcode in [0x09, 0x11, 0x07, 0x5E]:
                        end_found = True
                        # print("case 1")
                    elif (
                        # "pointers" in bank
                        not is_subroutine
                        and i < len(cmd_lengths)
                        and (current_addr + length >= addr + cmd_lengths[i])
                    ):
                        end_found = True
                        # print("case 2")
                    # elif "pointers" not in bank and (
                    #     current_addr + length >= bank["end"] + 1
                    # ):
                    #     end_found = True
                    elif current_addr + length in SPECIAL_CASE_BREAKS:
                        end_found = True
                    elif 0x3A0000 <= current_addr + length < 0x3A60D0:
                        end_found = True
                        # print("case 3")
                    current_addr += length

                i += 1
                if i >= len(addresses_to_jump_to):
                    searching = False

            if "pointers" in bank:
                for i in range(len(ptrs)):
                    if key == "battle_events" and i in [22]:
                        extra_offset = 2
                    elif key == "battle_events" and i in [70, 85]:
                        extra_offset = 4
                    else:
                        extra_offset = 0
                    this_script = []
                    #        writeline(file, '    [')
                    if i < len(ptrs) - 1:
                        cmd_lengths.append(ptrs[i + 1] - ptrs[i])
                        script_content = tok(
                            rom,
                            ptrs[i] + offset + extra_offset,
                            ptrs[i + 1] - 1,
                            bank_num,
                        )
                    else:
                        cmd_lengths.append(bank["end"] - ptrs[i])
                        script_content = tok(
                            rom, ptrs[i] + offset + extra_offset, bank["end"], bank_num
                        )
                    offset_2 = 0
                    for c in script_content:
                        byte_string = [("0x%02x" % b) for b in c[0]]
                        byte_string = ", ".join(byte_string)
                        addr_ = ptrs[i] + offset + extra_offset + offset_2
                        addr = hex(addr_)
                        #            writeline(file, '''        {'id': 'command_%s', 'addr': %s, 'data': [%s]},''' % (addr, addr, byte_string))
                        if addr in queue_addresses[coverage]:
                            ider = "queuestart_%s" % addr
                        else:
                            ider = "command_%s" % (addr)
                        this_script.append(
                            {
                                "id": ider,
                                "addr": addr_,
                                "data": list(c[0]),
                            }
                        )
                        offset_2 += len(c[0])

                    scripts.append(script_content)
                    #        writeline(file, '    ], # %i' % i)
                    data.append(this_script)
            else:
                this_script = []
                #    writeline(file, '    [')
                script_content = tok(rom, bank["start"], bank["end"], bank_num)
                offset_2 = 0
                for c in script_content:
                    byte_string = [("0x%02x" % b) for b in c[0]]
                    byte_string = ", ".join(byte_string)
                    addr_ = bank["start"] + offset_2
                    addr = hex(addr_)
                    #            writeline(file, '''        {'id': 'command_%s', 'addr': %s, 'data': [%s]},''' % (addr, addr, byte_string))
                    if addr in queue_addresses[coverage]:
                        ider = "queuestart_%s" % addr
                    else:
                        ider = "command_%s" % (addr)
                    this_script.append(
                        {
                            "id": ider,
                            "addr": addr_,
                            "data": list(c[0]),
                            "length": len(c[0]),
                        }
                    )
                    offset_2 += len(c[0])
                scripts.append(script_content)
                #    writeline(file, '    ]')
                data.append(this_script)
            # writeline(file, ']')

            collective_data[coverage].extend(data)
            separated_data[key] = data

        for key, bank in banks.items():
            add_refs = []
            for addr in range(bank["start"], bank["end"]):
                if addr in references and len(references[addr]) > 0:
                    add_refs.extend(references[addr])
            add_refs = list(set(add_refs))
            references_by_bank[bank["start"]] = deepcopy(
                [a for a in add_refs if a != ""]
            )

        if False:  # print ranges
            for key in known_addresses_covered:

                # print("    Ranges for %s: [" % key)
                state: bool = False
                st = bank_num
                en = 0
                distance = 0
                size = 0
                for i, b in enumerate(known_addresses_covered[key]):
                    if b != state:
                        state = b
                        if state:
                            st = int(key, 16) * 0x10000 + i
                            distance = st - en
                            print(
                                "                              # distance: %i"
                                % (distance)
                            )
                        else:
                            en = int(key, 16) * 0x10000 + i  # - 1
                            size = en - st
                            print(
                                "        'subroutines_0x%06x': {'start': 0x%06x, 'end': 0x%06x}, # size:     %i"
                                % (st, st, en - 1, size)
                            )
                print("    ]")

        output_02collection = "from randomizer.types.battle_animation_scripts.classes import AnimationScriptBankCollection"
        output_35collection = "from randomizer.types.battle_animation_scripts.classes import AnimationScriptBankCollection"
        output_3Acollection = "from randomizer.types.battle_animation_scripts.classes import AnimationScriptBankCollection"

        output_02collection_import = ""
        output_02collection_export = ""
        output_35collection_import = ""
        output_35collection_export = ""
        output_3Acollection_import = ""
        output_3Acollection_export = ""

        for key, bank in banks.items():

            coverage = "35"
            if "subroutine" in key:
                coverage = key[-6:-4].upper()
            elif key == "battle_events":
                coverage = "3A"
            elif key in ["toad_tutorial", "flower_bonus"]:
                coverage = "02"

            if "subroutine" in key:
                hv = key[-6:]
                export_dest = "randomizer/scripts/animation/subroutines"
                export_file = open("%s/export_0x%s.py" % (export_dest, hv.upper()), "w")
                # if key == "subroutines_0x353437":
                #     print("%s/0x%s.py" % (dest, hv.upper()))
                if coverage == "02":
                    output_02collection_import += (
                        "\nfrom .subroutines.export_0x%s import bank as subroutine_0x%s"
                        % (hv.upper(), hv.upper())
                    )
                    output_02collection_export += "\n\tsubroutine_0x%s," % hv.upper()
                if coverage == "35":
                    output_35collection_import += (
                        "\nfrom .subroutines.export_0x%s import bank as subroutine_0x%s"
                        % (hv.upper(), hv.upper())
                    )
                    output_35collection_export += "\n\tsubroutine_0x%s," % hv.upper()
                if coverage == "3A":
                    output_3Acollection_import += (
                        "\nfrom .subroutines.export_0x%s import bank as subroutine_0x%s"
                        % (hv.upper(), hv.upper())
                    )
                    output_3Acollection_export += "\n\tsubroutine_0x%s," % hv.upper()
            elif "behaviour" in key:
                spl = key.split("_")
                export_file = open(
                    "randomizer/scripts/animation/monster_behaviours/export_%s.py"
                    % (spl[1]),
                    "w",
                )
                output_35collection_import += (
                    "\nfrom .monster_behaviours.export_%s import bank as monster_behaviour_%s"
                    % (spl[1], spl[1])
                )
                output_35collection_export += "\n\tmonster_behaviour_%s," % spl[1]
            else:
                export_dest = "randomizer/scripts/animation/" + key
                export_file = open("%s/export.py" % export_dest, "w")
                if coverage == "02":
                    output_02collection_import += (
                        "\nfrom .%s.export import bank as %s"
                        % (
                            key,
                            key,
                        )
                    )
                    output_02collection_export += "\n\t%s," % key
                if coverage == "35":
                    output_35collection_import += (
                        "\nfrom .%s.export import bank as %s"
                        % (
                            key,
                            key,
                        )
                    )
                    output_35collection_export += "\n\t%s," % key
                if coverage == "3A":
                    output_3Acollection_import += (
                        "\nfrom .%s.export import bank as %s"
                        % (
                            key,
                            key,
                        )
                    )
                    output_3Acollection_export += "\n\t%s," % key

            import_body = ""
            export_body = ""

            # when reassembling battle scripts: before each script body, need to insert 2 bytes
            # that are a pointer to its own start
            # ie: values in pointer bank @ 3A6004 for script 0: 0xD0 0x60
            # actual value at 3A60D0: 0xD2 0x60
            # actual script 0 begins at 3A60D2

            # replace jump addresses with IDs if in the same bank
            for index, script in enumerate(separated_data[key]):
                if key == "battle_events":
                    for search_script in collective_data[coverage]:
                        for search_command in search_script:
                            for header_addr_index, header_addr in enumerate(
                                scripts_with_headers["22"]
                            ):
                                # print(hex(search_command["addr"]), hex(header_addr))
                                if search_command["addr"] == header_addr:
                                    scripts_with_headers["22"][
                                        header_addr_index
                                    ] = search_command["id"]
                                    relevant_pointers.append(search_command["id"])
                            for header_addr_index, header_addr in enumerate(
                                scripts_with_headers["70"]
                            ):
                                if search_command["addr"] == header_addr:
                                    scripts_with_headers["70"][
                                        header_addr_index
                                    ] = search_command["id"]
                                    relevant_pointers.append(search_command["id"])
                            for header_addr_index, header_addr in enumerate(
                                scripts_with_headers["85"]
                            ):
                                if search_command["addr"] == header_addr:
                                    scripts_with_headers["85"][
                                        header_addr_index
                                    ] = search_command["id"]
                                    relevant_pointers.append(search_command["id"])

                for cmd_index, command in enumerate(script):
                    if (
                        command["data"][0] in jmp_cmds
                        or command["data"][0] in jmp_cmds_1
                    ):
                        if command["data"][0] in jmp_cmds_1:
                            address = command["data"][-3:-1]
                        else:
                            address = command["data"][-2:]

                        byte_string = [("0x%02x" % b) for b in address]
                        # byte_string1 = [("0x%02x" % b) for b in command["data"]]
                        # print(command, byte_string1, byte_string)
                        dest = (
                            (command["addr"] & 0xFF0000)
                            + (address[1] << 8)
                            + address[0]
                        )
                        # print(hex(dest), len(data))

                        found = None
                        for search_index, search_script in enumerate(
                            collective_data[coverage]
                        ):
                            for search_cmd_index, search_command in enumerate(
                                search_script
                            ):
                                # print (command, hex(dest), search_command)
                                if search_command["addr"] == dest:
                                    found = search_command["id"]
                        if found is not None:
                            if command["data"][0] in jmp_cmds_1:
                                del command["data"][-3:-1]
                                command["data"].insert(-1, found)
                            else:
                                del command["data"][-2:]
                                command["data"].append(found)
                            relevant_pointers.append(found)
                        separated_data[key][index][cmd_index]["data"] = command["data"]

            for index, script in enumerate(separated_data[key]):

                script_alias = ""

                if "subroutine" in key:
                    hv = key[-6:]
                    dest = "randomizer/scripts/animation/subroutines/contents"
                    file = open("%s/subroutine_0x%s.py" % (dest, hv.upper()), "w")
                    # if key == "subroutines_0x353437":
                    #     print("%s/0x%s.py" % (dest, hv.upper()))
                    script_alias = "subroutine_0x%s" % hv.upper()
                    import_body += "\nfrom .contents.%s import script as %s" % (
                        script_alias,
                        script_alias,
                    )
                elif "behaviour" in key:
                    spl = key.split("_")
                    file = open(
                        "randomizer/scripts/animation/monster_behaviours/contents/script_%s.py"
                        % (spl[1]),
                        "w",
                    )
                    script_alias = "subroutine_0x%s" % spl[1]
                    import_body += "\nfrom .contents.%s import script as %s" % (
                        script_alias,
                        script_alias,
                    )
                else:
                    dest = "randomizer/scripts/animation/" + key
                    file = open("%s/contents/script_%i.py" % (dest, index), "w")
                    script_alias = "script_%i" % index
                    import_body += "\nfrom .contents.%s import script as %s" % (
                        script_alias,
                        script_alias,
                    )

                output = ""
                if "behaviour" in key:
                    output = "# %s" % key
                elif key == "toad_tutorial":
                    output = "# %s" % key
                elif key in [
                    "flower_bonus",
                    "monster_spells",
                    "monster_attacks",
                    "monster_entrances",
                    "misses",
                    "items",
                    "ally_spells",
                    "weapons",
                    "battle_events",
                ] and index < len(SCRIPT_NAMES[key]):
                    output = "# %s" % SCRIPT_NAMES[key][index]
                elif "subroutine" in key:
                    hv = int(key[-8:], 16)
                    if hv in references_by_bank:
                        output = "# referenced by %s" % ", ".join(
                            references_by_bank[hv]
                        )

                output += (
                    "\n\nfrom randomizer.scripts.animation.script_imports import *"
                )
                if key == "battle_events":
                    if index == 22:
                        output += (
                            """\n\nscript = BattleAnimationScript(header=["%s"], script = [\n\t"""
                            % scripts_with_headers["22"][0]
                        )
                    elif index == 70:
                        output += (
                            """\n\nscript = BattleAnimationScript(header=["%s, %s"], script = [\n\t"""
                            % (
                                scripts_with_headers["70"][0],
                                scripts_with_headers["70"][1],
                            )
                        )
                    elif index == 85:
                        output += (
                            """\n\nscript = BattleAnimationScript(header=["%s, %s"], script = [\n\t"""
                            % (
                                scripts_with_headers["85"][0],
                                scripts_with_headers["85"][1],
                            )
                        )
                    else:
                        output += "\n\nscript = BattleAnimationScript(script=[\n\t"
                elif (
                    "subroutines_" in key
                    or "behaviour_" in key
                    or key in ["toad_tutorial"]
                ):
                    output += (
                        """\n\nscript = SubroutineOrBanklessScript(expected_size = %i, script = [\n\t"""
                        % (banks[key]["end"] - banks[key]["start"] + 1)
                    )
                else:
                    output += "\n\nscript = AnimationScript([\n\t"

                # print(key)
                contents = get_script(script, relevant_pointers)
                # print(key, index, contents)

                output += ",\n\t".join(contents)

                output += "\n])"

                writeline(file, output)

                export_body += "\n\t\t%s," % script_alias
            export_output = "from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank"
            export_output += (
                "\nfrom randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import %s"
                % (key.upper())
            )
            export_output += import_body
            export_output += "\n\nbank = AnimationScriptBank("
            export_output += "\n\tname = %s," % key.upper()
            export_output += "\n\tstart = 0x%06x," % bank["start"]
            export_output += "\n\tend = 0x%06x," % bank["end"]
            if "pointers" in bank:
                export_output += (
                    "\n\tpointer_table_start = 0x%06x," % bank["pointers"]["start"]
                )
            export_output += "\n\tscripts = ["
            export_output += export_body

            export_output += "\n\t]"
            export_output += "\n)"
            writeline(export_file, export_output)

        output_02collection += output_02collection_import
        output_02collection += "\n\ncollection = AnimationScriptBankCollection(["
        output_02collection += output_02collection_export
        output_02collection += "\n])"
        output_35collection += output_35collection_import
        output_35collection += "\n\ncollection = AnimationScriptBankCollection(["
        output_35collection += output_35collection_export
        output_35collection += "\n])"
        output_3Acollection += output_3Acollection_import
        output_3Acollection += "\n\ncollection = AnimationScriptBankCollection(["
        output_3Acollection += output_3Acollection_export
        output_3Acollection += "\n])"

        collection02_dest = "randomizer/scripts/animation/collection_0x02xxxx.py"
        collection02_file = open(collection02_dest, "w")
        collection35_dest = "randomizer/scripts/animation/collection_0x35xxxx.py"
        collection35_file = open(collection35_dest, "w")
        collection3A_dest = "randomizer/scripts/animation/collection_0x3Axxxx.py"
        collection3A_file = open(collection3A_dest, "w")
        writeline(collection02_file, output_02collection)
        writeline(collection35_file, output_35collection)
        writeline(collection3A_file, output_3Acollection)


def get_script(script, valid_identifiers):
    # print("")
    # print(script)

    new_script = []

    for cmd in script:
        identifier = ""
        cls, args, use_identifier, include_argnames = convert_event_script_command(
            cmd, valid_identifiers
        )

        if cls is not None:
            arg_strings = []
            for key in args:
                if include_argnames:
                    arg_strings.append("%s=%s" % (key, args[key]))
                else:
                    arg_strings.append(args[key])
            try:
                arg_string = ", ".join(arg_strings)
            except:
                raise Exception(cls)

            if use_identifier:
                if len(arg_string) > 0:
                    arg_string += ", "
                identifier = 'identifier="%s"' % cmd["id"]

            output = "%s(%s%s)" % (cls, arg_string, identifier)
            new_script.append(output)

    return new_script


def convert_event_script_command(command, valid_identifiers):
    # print(command)
    cmd = command["data"]
    use_identifier: bool = (
        command["id"] in valid_identifiers or "queuestart" in command["id"]
    )
    # use_identifier: bool = False
    args = {}
    cls = None
    include_argnames = True

    opcode = cmd[0]

    if opcode == 0x00:
        cls = "NewSpriteAtCoords"
        args["sprite_id"] = get_sprite_name(shortify(cmd, 3) & 0x3FF)
        args["sequence"] = str(cmd[5] & 0x0F)
        args["priority"] = str((cmd[6] & 0x30) >> 4)
        args["vram_address"] = f"0x{shortify(cmd, 7):04X}"
        args["palette_row"] = str(cmd[6] & 0x0F)
        if (cmd[1] & 0x01) == 0x01:
            args["overwrite_vram"] = "True"
        if (cmd[2] & 0x08) == 0x08:
            args["looping"] = "True"
        if (cmd[2] & 0x10) == 0x10:
            args["param_2_and_0x10"] = "True"
        if (cmd[2] & 0x20) == 0x20:
            args["overwrite_palette"] = "True"
        if (cmd[6] & 0x40) == 0x40:
            args["mirror_sprite"] = "True"
        if (cmd[6] & 0x80) == 0x80:
            args["invert_sprite"] = "True"
        if (cmd[1] & 0x40) == 0x40:
            args["behind_all_sprites"] = "True"
        if (cmd[1] & 0x80) == 0x80:
            args["overlap_all_sprites"] = "True"
    elif opcode == 0x01 or opcode == 0x0B:
        if opcode == 0x01:
            cls = "SetAMEM32ToXYZCoords"
        elif opcode == 0x0B:
            cls = "SetAMEM40ToXYZCoords"
        args["origin"] = ORIGINS[((cmd[1] >> 4) & 0b11)]
        args["x"] = str(shortify_signed(cmd, 2))
        args["y"] = str(shortify_signed(cmd, 4))
        args["z"] = str(shortify_signed(cmd, 6))
        if (cmd[1] & 0x01) == 0x01:
            args["set_x"] = "True"
        if (cmd[1] & 0x02) == 0x02:
            args["set_y"] = "True"
        if (cmd[1] & 0x04) == 0x04:
            args["set_z"] = "True"
    elif opcode == 0x03:
        cls = "DrawSpriteAtAMEM32Coords"
        args["sprite_id"] = get_sprite_name(shortify(cmd, 3) & 0x3FF)
        args["sequence"] = cmd[5] & 0x0F
        if (cmd[1] & 0x01) == 0x01:
            args["store_to_vram"] = "True"
        if (cmd[2] & 0x08) == 0x08:
            args["looping"] = "True"
        if (cmd[2] & 0x20) == 0x20:
            args["store_palette"] = "True"
    elif opcode == 0x04:
        cls = "PauseScriptUntil"
        if cmd[1] == 6:
            args["condition"] = "SPRITE_SHIFT_COMPLETE"
        elif cmd[1] == 8:
            args["condition"] = "BUTTON_PRESSED"
        elif cmd[1] == 0x10:
            args["condition"] = "FRAMES_ELAPSED"
            args["frames"] = str(shortify(cmd, 2))
        else:
            args["condition"] = f"0x{cmd[1]:02X}"
    elif opcode == 0x05:
        cls = "RemoveObject"
    elif opcode == 0x07:
        cls = "ReturnObjectQueue"
    elif opcode == 0x08:
        cls = "MoveObject"
        args["speed"] = str(shortify_signed(cmd, 6))
        args["start_position"] = str(shortify_signed(cmd, 2))
        args["end_position"] = str(shortify_signed(cmd, 4))
        if (cmd[1] & 0x04) == 0x04:
            args["apply_to_x"] = "True"
        if (cmd[1] & 0x02) == 0x02:
            args["apply_to_y"] = "True"
        if (cmd[1] & 0x01) == 0x01:
            args["apply_to_z"] = "True"
        if (cmd[1] & 0x20) == 0x20:
            args["should_set_start_position"] = "True"
        if (cmd[1] & 0x40) == 0x40:
            args["should_set_end_position"] = "True"
        if (cmd[1] & 0x80) == 0x80:
            args["should_set_speed"] = "True"
    elif opcode == 0x09:
        cls = "Jmp"
        args["destinations"] = '["%s"]' % cmd[1]
        include_argnames = False
    elif opcode == 0x0A:
        cls = "Pause1Frame"
    elif opcode == 0x0C:
        cls = "MoveSpriteToCoords"
        if cmd[1] & 0x0E == 0:
            args["condition"] = "SHIFT_TYPE_0X00"
        elif cmd[1] & 0x0E == 2:
            args["condition"] = "SHIFT_TYPE_SHIFT"
        elif cmd[1] & 0x0E == 4:
            args["condition"] = "SHIFT_TYPE_TRANSFER"
        elif cmd[1] & 0x0E == 6:
            args["condition"] = "SHIFT_TYPE_0X04"
        elif cmd[1] & 0x0E == 8:
            args["condition"] = "SHIFT_TYPE_0X08"
        else:
            raise Exception("invalid shift type: %r" & command)
        args["speed"] = str(shortify_signed(cmd, 2))
        args["arch_height"] = str(shortify_signed(cmd, 4))
    elif opcode == 0x0E:
        cls = "ResetTargetMappingMemory"
    elif opcode == 0x0F:
        cls = "ResetObjectMappingMemory"
    elif opcode == 0x10:
        cls = "RunSubroutine"
        args["destinations"] = '["%s"]' % cmd[1]
        include_argnames = False
    elif opcode == 0x11:
        cls = "ReturnSubroutine"
    elif opcode == 0x1A:
        cls = "VisibilityOn"
    elif opcode == 0x1B:
        cls = "VisibilityOff"
    elif (
        opcode
        in [
            0x20,
            0x21,
            0x24,
            0x25,
            0x26,
            0x27,
            0x28,
            0x29,
            0x2A,
            0x2B,
            0x2C,
            0x2D,
            0x2E,
            0x2F,
        ]
        and cmd[1] & 0xF0 <= 0x60
    ) or (opcode in [0x22, 0x23] and 0x10 <= cmd[1] & 0xF0 <= 0x60):
        byte2 = cmd[1] & 0xF0
        include_argnames = False
        if opcode == 0x20:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "SetAMEM8BitToConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "SetAMEM8BitTo7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "SetAMEM8BitTo7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "SetAMEM8BitToAMEM"
                args["source_amem"] = f"0x{(cmd[2] + 0x60):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "SetAMEM8BitToOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "SetAMEM8BitTo7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "SetAMEM8BitToOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" & command)
        elif opcode == 0x21:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "SetAMEM16BitToConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "SetAMEM16BitTo7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "SetAMEM16BitTo7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "SetAMEM16BitToAMEM"
                args["source_amem"] = f"0x{(cmd[2] + 0x60):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "SetAMEM16BitToOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "SetAMEM16BitTo7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "SetAMEM16BitToOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" & command)
        elif opcode == 0x22:
            if byte2 == 0x10:
                cls = "Set7E1xToAMEM8Bit"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "Set7FToAMEM8Bit"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "SetAMEMToAMEM8Bit"
                args["dest_amem"] = f"0x{(cmd[2] + 0x60):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "SetOMEMCurrentToAMEM8Bit"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "Set7E5xToAMEM8Bit"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "SetOMEMMainToAMEM8Bit"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" & command)
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
        elif opcode == 0x23:
            if byte2 == 0x10:
                cls = "Set7E1xToAMEM16Bit"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "Set7FToAMEM16Bit"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "SetAMEMToAMEM16Bit"
                args["dest_amem"] = f"0x{(cmd[2] + 0x60):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "SetOMEMCurrentToAMEM16Bit"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "Set7E5xToAMEM16Bit"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "SetOMEMMainToAMEM16Bit"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" & command)
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
        elif opcode == 0x24:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "JmpIfAMEM8BitEqualsConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "JmpIfAMEM8BitEquals7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "JmpIfAMEM8BitEquals7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "JmpIfAMEM8BitEqualsAMEM"
                args["source_amem"] = f"0x{(cmd[2] + 0x60):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "JmpIfAMEM8BitEqualsOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "JmpIfAMEM8BitEquals7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "JmpIfAMEM8BitEqualsOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" & command)
            args["destinations"] = '["%s"]' % cmd[len(cmd) - 1]
        elif opcode == 0x25:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "JmpIfAMEM16BitEqualsConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "JmpIfAMEM16BitEquals7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "JmpIfAMEM16BitEqjmpsEqualsuals7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "JmpIfAMEM16BitEqualsAMEM"
                args["source_amem"] = f"0x{(cmd[2] + 0x60):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "JmpIfAMEM16BitEqualsOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "JmpIfAMEM16BitEquals7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "JmpIfAMEM16BitEqualsOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" & command)
            args["destinations"] = '["%s"]' % cmd[len(cmd) - 1]
        elif opcode == 0x26:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "JmpIfAMEM8BitNotEqualsConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "JmpIfAMEM8BitNotEquals7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "JmpIfAMEM8BitNotEquals7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "JmpIfAMEM8BitNotEqualsAMEM"
                args["source_amem"] = f"0x{(cmd[2] + 0x60):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "JmpIfAMEM8BitNotEqualsOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "JmpIfAMEM8BitNotEquals7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "JmpIfAMEM8BitNotEqualsOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" & command)
            args["destinations"] = '["%s"]' % cmd[len(cmd) - 1]
        elif opcode == 0x27:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "JmpIfAMEM16BitNotEqualsConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "JmpIfAMEM16BitNotEquals7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "JmpIfAMEM16BitNotEquals7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "JmpIfAMEM16BitNotEqualsAMEM"
                args["source_amem"] = f"0x{(cmd[2] + 0x60):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "JmpIfAMEM16BitNotEqualsOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "JmpIfAMEM16BitNotEquals7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "JmpIfAMEM16BitNotEq16BitualsOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" & command)
            args["destinations"] = '["%s"]' % cmd[len(cmd) - 1]
        elif opcode == 0x28:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "JmpIfAMEM8BitLessThanConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "JmpIfAMEM8BitLessThan7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "JmpIfAMEM8BitLessThan7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "JmpIfAMEM8BitLessThanAMEM"
                args["source_amem"] = f"0x{(cmd[2] + 0x60):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "JmpIfAMEM8BitLessThanOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "JmpIfAMEM8BitLessThan7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "JmpIfAMEM8BitLessThanOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" & command)
            args["destinations"] = '["%s"]' % cmd[len(cmd) - 1]
        elif opcode == 0x29:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "JmpIfAMEM16BitLessThanConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "JmpIfAMEM16BitLessThan7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "JmpIfAMEM16BitLessThan7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "JmpIfAMEM16BitLessThanAMEM"
                args["source_amem"] = f"0x{(cmd[2] + 0x60):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "JmpIfAMEM16BitLessThanOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "JmpIfAMEM16BitLessThan7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "JmpIfAMEM16BitLessThanOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" & command)
            args["destinations"] = '["%s"]' % cmd[len(cmd) - 1]
        elif opcode == 0x2A:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "JmpIfAMEM8BitGreaterOrEqualThanConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "JmpIfAMEM8BitGreaterOrEqualThan7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "JmpIfAMEM8BitGreaterOrEqualThan7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "JmpIfAMEM8BitGreaterOrEqualThanAMEM"
                args["source_amem"] = f"0x{(cmd[2] + 0x60):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "JmpIfAMEM8BitGreaterOrEqualThanOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "JmpIfAMEM8BitGreaterOrEqualThan7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "JmpIfAMEM8BitGreaterOrEqualThanOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" & command)
            args["destinations"] = '["%s"]' % cmd[len(cmd) - 1]
        elif opcode == 0x2B:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "JmpIfAMEM16BitGreaterOrEqualThanConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "JmpIfAMEM16BitGreaterOrEqualThan7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "JmpIfAMEM16BitGreaterOrEqualThan7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "JmpIfAMEM16BitGreaterOrEqualThanAMEM"
                args["source_amem"] = f"0x{(cmd[2] + 0x60):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "JmpIfAMEM16BitGreaterOrEqualThanOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "JmpIfAMEM16BitGreaterOrEqualThan7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "JmpIfAMEM16BitGreaterOrEqualThanOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" & command)
            args["destinations"] = '["%s"]' % cmd[len(cmd) - 1]
        elif opcode == 0x2C:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "IncAMEM8BitByConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "IncAMEM8BitBy7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "IncAMEM8BitBy7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "IncAMEM8BitByAMEM"
                args["source_amem"] = f"0x{(cmd[2] + 0x60):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "IncAMEM8BitByOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "IncAMEM8BitBy7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "IncAMEM8BitByOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" & command)
        elif opcode == 0x2D:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "IncAMEM16BitByConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "IncAMEM16BitBy7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "IncAMEM16BitBy7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "IncAMEM16BitByAMEM"
                args["source_amem"] = f"0x{(cmd[2] + 0x60):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "IncAMEM16BitByOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "IncAMEM16BitBy7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "IncAMEM16BitByOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
        elif opcode == 0x2E:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "DecAMEM8BitByConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "DecAMEM8BitBy7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "DecAMEM8BitBy7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "DecAMEM8BitByAMEM"
                args["source_amem"] = f"0x{(cmd[2] + 0x60):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "DecAMEM8BitByOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "DecAMEM8BitBy7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "DecAMEM8BitByOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" & command)
        elif opcode == 0x2F:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "DecAMEM16BitByConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "DecAMEM16BitBy7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "DecAMEM16BitBy7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "DecAMEM16BitByAMEM"
                args["source_amem"] = f"0x{(cmd[2] + 0x60):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "DecAMEM16BitByOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "DecAMEM16BitBy7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "DecAMEM16BitByOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" & command)
    elif opcode in [0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2A, 0x2B]:
        cls = "UnknownJmp%02X" % opcode
        args["byte_1"] = str(cmd[1])
        args["destinations"] = '["%s"]' % cmd[len(cmd) - 1]
        include_argnames = False
    elif opcode in [0x30, 0x31, 0x32, 0x33, 0x34, 0x35]:
        if opcode == 0x30:
            cls = "IncAMEM8Bit"
        elif opcode == 0x31:
            cls = "IncAMEM16Bit"
        elif opcode == 0x32:
            cls = "DecAMEM8Bit"
        elif opcode == 0x33:
            cls = "DecAMEM16Bit"
        elif opcode == 0x34:
            cls = "ClearAMEM8Bit"
        elif opcode == 0x35:
            cls = "ClearAMEM16Bit"
        args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
        include_argnames = False
    elif opcode in [0x36, 0x37, 0x38, 0x39, 0x40, 0x41]:
        if opcode == 0x36:
            cls = "SetAMEMBits"
        elif opcode == 0x37:
            cls = "ClearAMEMBits"
        elif opcode == 0x38:
            cls = "JmpIfAMEMBitsSet"
        elif opcode == 0x39:
            cls = "JmpIfAMEMBitsClear"
        elif opcode == 0x40:
            cls = "PauseScriptUntilAMEMBitsSet"
        elif opcode == 0x41:
            cls = "PauseScriptUntilAMEMBitsClear"
        args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
        bits = []
        for b in range(0, 8):
            if cmd[2] & (1 << b) != 0:
                bits.append(b)
        args["bits"] = "%r" % bits
        if opcode in [0x38, 0x39]:
            args["destinations"] = '["%s"]' % cmd[len(cmd) - 1]
        include_argnames = False
    elif opcode == 0x3A:
        cls = "AttackTimerBegins"
    elif opcode == 0x43:
        cls = "SpriteSequence"
        args["sequence"] = str(cmd[1] & 0x0F)
        if cmd[1] & 0x10 == 0x10:
            args["looping_on"] = "True"
        if cmd[1] & 0x20 == 0x20:
            args["looping_off"] = "True"
        if cmd[1] & 0x40 == 0x40:
            args["bit_6"] = "True"
        if cmd[1] & 0x80 == 0x80:
            args["mirror"] = "True"
    elif opcode == 0x45:
        cls = "SetAMEM60ToCurrentTarget"
    elif opcode == 0x4E:
        cls = "PauseScriptUntilSpriteSequenceDone"
    elif opcode == 0x50:
        cls = "JmpIfTargetDisabled"
        args["destinations"] = '["%s"]' % cmd[len(cmd) - 1]
        include_argnames = False
    elif opcode == 0x51:
        cls = "JmpIfTargetEnabled"
        args["destinations"] = '["%s"]' % cmd[len(cmd) - 1]
        include_argnames = False
    elif opcode == 0x5D:
        cls = "SpriteQueue"
        args["field_object"] = str(cmd[2])
        args["destinations"] = '["%s"]' % cmd[len(cmd) - 1]
        if cmd[1] & 0x01 == 0x01:
            args["bit_0"] = "True"
        if cmd[1] & 0x02 == 0x02:
            args["bit_1"] = "True"
        if cmd[1] & 0x04 == 0x04:
            args["bit_2"] = "True"
        if cmd[1] & 0x08 == 0x08:
            args["character_slot"] = "True"
        if cmd[1] & 0x10 == 0x10:
            args["bit_4"] = "True"
        if cmd[1] & 0x20 == 0x20:
            args["bit_5"] = "True"
        if cmd[1] & 0x40 == 0x40:
            args["current_target"] = "True"
        if cmd[1] & 0x80 == 0x80:
            args["bit_7"] = "True"
    elif opcode == 0x5E:
        cls = "ReturnSpriteQueue"
    elif opcode == 0x63 and 0 <= cmd[1] <= 2:
        cls = "DisplayMessageAtOMEM60As"
        if cmd[1] == 0:
            args["type"] = "BATTLE_DIALOGUE"
        elif cmd[1] == 1:
            args["type"] = "PSYCHOPATH_MESSAGE"
        elif cmd[1] == 2:
            args["type"] = "BATTLE_MESSAGE"
        include_argnames = False
    elif opcode == 0x64:
        cls = "ObjectQueueAtOffsetAndIndexAtAMEM60"
        if isinstance(cmd[len(cmd) - 1], str):
            args["destinations"] = '["%s"]' % cmd[len(cmd) - 1]
        else:
            args[
                "target_address"
            ] = f"0x{hex(command['addr'])[2:4].upper()}{shortify(cmd, 1):04X}"
    elif opcode == 0x68:
        cls = "ObjectQueueAtOffsetAndIndex"
        args["index"] = str(cmd[3])
        if isinstance(cmd[len(cmd) - 1], str):
            args["destinations"] = '["%s"]' % cmd[len(cmd) - 1]
        else:
            args[
                "target_address"
            ] = f"0x{hex(command['addr'])[2:4].upper()}{shortify(cmd, 1):04X}"
    elif opcode == 0x69:
        cls = "SetOMEM60To072C"
    elif opcode == 0x6A:
        cls = "SetAMEMToRandom"
        args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
        args["upper_bound"] = str(cmd[2])
    elif opcode == 0x6B:
        cls = "SetAMEMToRandom"
        args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
        args["upper_bound"] = str(shortify(cmd, 2))
    elif opcode == 0x70:
        cls = "EnableSpritesOnSubscreen"
    elif opcode == 0x71:
        cls = "DisableSpritesOnSubscreen"
    elif opcode == 0x72:
        cls = "NewEffectObject"
        args["effect"] = EFFECTS[cmd[2]]
        if cmd[1] & 0x01 == 0x01:
            args["looping_on"] = "True"
        if cmd[1] & 0x02 == 0x02:
            args["playback_off"] = "True"
        if cmd[1] & 0x04 == 0x04:
            args["looping_off"] = "True"
        if cmd[1] & 0x08 == 0x08:
            args["bit_3"] = "True"
    elif opcode == 0x73:
        cls = "Pause2Frames"
    elif opcode == 0x74 and cmd[1:] in [
        [0x04, 0x00],
        [0x08, 0x00],
        [0x00, 0x02],
        [0x00, 0x04],
        [0x00, 0x08],
    ]:
        cls = "PauseScriptUntil"
        if cmd[1:] == [0x04, 0x00]:
            args["condition"] = "SEQ_4BPP_COMPLETE"
        elif cmd[1:] == [0x08, 0x00]:
            args["condition"] = "SEQ_2BPP_COMPLETE"
        elif cmd[1:] == [0x00, 0x02]:
            args["condition"] = "FADE_IN_COMPLETE"
        elif cmd[1:] == [0x00, 0x04]:
            args["condition"] = "FADE_4BPP_COMPLETE"
        elif cmd[1:] == [0x00, 0x08]:
            args["condition"] = "FADE_2BPP_COMPLETE"
    elif opcode == 0x75:
        cls = "PauseScriptUntilBitsClear"
        args["bits"] = str(shortify(cmd, 1))
        include_argnames = False
    elif opcode == 0x76:
        cls = "ClearEffectIndex"
    elif opcode in [0x77, 0x78]:
        if opcode == 0x77:
            cls = "Layer3On"
        else:
            cls = "Layer3Off"
        if cmd[1] & 0xF0 == 0:
            args["property"] = "TRANSPARENCY_OFF"
        elif cmd[1] & 0xF0 == 0x10:
            args["property"] = "OVERLAP_ALL"
        elif cmd[1] & 0xF0 == 0x20:
            args["property"] = "OVERLAP_NONE"
        elif cmd[1] & 0xF0 == 0x30:
            args["property"] = "OVERLAP_ALL_EXCEPT_ALLIES"
        else:
            raise Exception("invalid property type at %r" % command)
        if cmd[1] & 0x01 == 0x01:
            args["bit_0"] = "True"
        if cmd[1] & 0x02 == 0x02:
            args["bpp4"] = "True"
        if cmd[1] & 0x04 == 0x04:
            args["bpp4"] = "True"
        if cmd[1] & 0x08 == 0x08:
            args["set_invisible"] = "True"
    elif opcode == 0x7A and 0 <= cmd[1] <= 2:
        cls = "DisplayMessage"
        if cmd[1] == 0:
            args["type"] = "BATTLE_DIALOGUE"
        elif cmd[1] == 1:
            args["type"] = "PSYCHOPATH_MESSAGE"
        elif cmd[1] == 2:
            args["type"] = "BATTLE_MESSAGE"
        args["dialog_id"] = str(cmd[2])
        include_argnames = False
    elif opcode == 0x7B:
        cls = "PauseScriptUntilDialogClosed"
    elif opcode == 0x7E:
        cls = "FadeOutObject"
        args["duration"] = str(cmd[1])
    elif opcode == 0x7F:
        cls = "ResetSpriteSequence"
    elif opcode == 0x80:
        cls = "ShineEffect"
        args["colour_count"] = str(cmd[2] & 0x0F)
        args["starting_colour_index"] = str((cmd[2] & 0xF0) >> 4)
        args["glow_duration"] = str(cmd[3])
        if cmd[1] == 1:
            args["west"] = "True"
        elif cmd[1] == 0:
            args["east"] = "True"
        else:
            raise Exception(command)
    elif opcode == 0x85:
        if cmd[1] == 0:
            cls = "FadeOutEffect"
        elif cmd[1] == 0x10:
            cls = "FadeOutSprite"
        elif cmd[1] == 0x20:
            cls = "FadeOutScreen"
        elif cmd[1] == 2:
            cls = "FadeInEffect"
        elif cmd[1] == 0x12:
            cls = "FadeInSprite"
        elif cmd[1] == 0x22:
            cls = "FadeInScreen"
        args["duration"] = cmd[2]
    elif opcode == 0x86 and cmd[1] in [1, 2, 4]:
        if cmd[1] == 1:
            cls = "ShakeScreen"
        elif cmd[1] == 2:
            cls = "ShakeSprites"
        elif cmd[1] == 4:
            cls = "ShakeScreenAndSprites"
        args["amount"] = str(cmd[4])
        args["speed"] = str(shortify(cmd, 5))
    elif opcode == 0x87:
        cls = "StopShakingObject"
    elif opcode == 0x8E:
        cls = "ScreenFlashWithDuration"
        args["colour"] = FLASH_COLOURS[cmd[1] & 0x07]
        args["duration"] = str(cmd[2])
        if cmd[1] & 0xF8 != 0:
            args["unknown_upper"] = str(cmd[1] & 0xF8)
        include_argnames = False
    elif opcode == 0x8F:
        cls = "ScreenFlash"
        args["colour"] = FLASH_COLOURS[cmd[1] & 0x07]
        if cmd[1] & 0xF8 != 0:
            args["unknown_upper"] = str(cmd[1] & 0xF8)
        include_argnames = False
    elif opcode == 0x95:
        cls = "InitializeBonusMessageSequence"
    elif opcode == 0x96:
        cls = "DisplayBonusMessage"
        args["message"] = BONUS_MESSAGES[cmd[1]]
        args["x"] = str(byte_signed(cmd[2]))
        args["y"] = str(byte_signed(cmd[3]))
    elif opcode == 0x97:
        cls = "PauseScriptUntilBonusMessageComplete"
    elif opcode == 0xA3:
        cls = "ScreenEffect"
        args["message"] = SCREEN_EFFECTS[cmd[1]]
        include_argnames = False
    elif opcode in [0xAB, 0xAE]:
        cls = "PlaySound"
        # print(command)
        args["sound"] = SOUNDS[cmd[1]]
        if opcode == 0xAE:
            args["channel"] = "4"
    elif opcode == 0xB0:
        cls = "PlayMusicAtCurrentVolume"
        args["sound"] = MUSIC[cmd[1]]
        include_argnames = False
    elif opcode == 0xB1:
        cls = "PlayMusicAtVolume"
        args["sound"] = MUSIC[cmd[1]]
        args["volume"] = str(shortify(cmd, 2))
        include_argnames = False
    elif opcode == 0xB2:
        cls = "StopCurrentSoundEffect"
    elif opcode == 0xB6:
        cls = "FadeCurrentMusicToVolume"
        args["speed"] = str(cmd[1])
        args["volume"] = str(cmd[2])
    elif opcode == 0xBB:
        cls = "SetTarget"
        args["target"] = TARGETS[cmd[1]]
        include_argnames = False
    elif opcode in [0xBC, 0xBD]:
        include_argnames = False
        if cmd[2] == 0:
            cls = (
                "AddItemToStandardInventory"
                if opcode == 0xBC
                else "AddItemToKeyItemInventory"
            )
            args["target"] = ITEMS[cmd[1]]
        elif cmd[2] == 0xFF:
            cls = (
                "RemoveItemFromStandardInventory"
                if opcode == 0xBC
                else "RemoveItemFromKeyItemInventory"
            )
            args["target"] = ITEMS[256 - cmd[1]]
        else:
            raise Exception(command)
    elif opcode == 0xBE:
        cls = "AddCoins"
        args["amount"] = str(shortify(cmd, 1))
        include_argnames = False
    elif opcode == 0xBF:
        cls = "AddYoshiCookiesToInventory"
        args["amount"] = str(cmd[1])
        include_argnames = False
    elif opcode == 0xC3:
        cls = "DoMaskEffect"
        args["effect"] = MASKS[cmd[1] & 0x07]
        if cmd[1] & 0xF8 != 0:
            args["unknown_upper"] = str(cmd[1] & 0xF8)
        include_argnames = False
    elif opcode == 0xC6:
        cls = "SetMaskCoords"
        include_argnames = False
        args["point1"] = "(%s, %s)" % (byte_signed(cmd[1]), byte_signed(cmd[2]))
        args["point2"] = "(%s, %s)" % (byte_signed(cmd[3]), byte_signed(cmd[4]))
        args["point3"] = "(%s, %s)" % (byte_signed(cmd[5]), byte_signed(cmd[6]))
        args["point4"] = "(%s, %s)" % (byte_signed(cmd[7]), byte_signed(cmd[8]))
    elif opcode == 0xCB:
        cls = "SetSequenceSpeed"
        args["speed"] = str(cmd[1])
        include_argnames = False
    elif opcode == 0xCC:
        cls = "StartTrackingAllyButtonInputs"
    elif opcode == 0xCD:
        cls = "EndTrackingAllyButtonInputs"
    elif opcode == 0xCE:
        cls = "TimingForOneTieredButtonPress"
        args["start_accepting_input"] = str(cmd[1])
        args["end_accepting_input"] = str(cmd[2])
        args["partial_start"] = str(cmd[3])
        args["perfect_start"] = str(cmd[4])
        args["perfect_end"] = str(cmd[5])
        args["destinations"] = '["%s"]' % cmd[len(cmd) - 1]
    elif opcode == 0xCF:
        cls = "TimingForOneBinaryButtonPress"
        args["start_accepting_input"] = str(cmd[1])
        args["end_accepting_input"] = str(cmd[2])
        args["timed_hit_ends"] = str(cmd[3])
        args["destinations"] = '["%s"]' % cmd[len(cmd) - 1]
    elif opcode == 0xD0:
        cls = "TimingForMultipleButtonPresses"
        args["start_accepting_input"] = str(cmd[1])
        args["destinations"] = '["%s"]' % cmd[len(cmd) - 1]
    elif opcode == 0xD1:
        cls = "TimingForButtonMashUnknown"
    elif opcode == 0xD2:
        cls = "TimingForButtonMashCount"
        args["max_presses"] = str(cmd[1])
    elif opcode == 0xD3:
        cls = "TimingForOneBinaryButtonPress"
        args["start_accepting_input"] = str(cmd[1])
        args["end_accepting_input"] = str(cmd[2])
        args["max_presses"] = str(cmd[3])
    elif opcode == 0xD4:
        cls = "TimingForChargePress"
        args["charge_level_1_end"] = str(cmd[1])
        args["charge_level_2_end"] = str(cmd[2])
        args["charge_level_3_end"] = str(cmd[3])
        args["charge_level_4_end"] = str(cmd[4])
        args["overcharge_end"] = str(cmd[5])
    elif opcode == 0xD5:
        cls = "SummonMonster"
        args["monster"] = ENEMIES[cmd[2]]
        args["position"] = cmd[3]
        if cmd[1] & 0x01 == 0x01:
            args["bit_0"] = "True"
        if cmd[1] & 0x02 == 0x02:
            args["bit_1"] = "True"
        if cmd[1] & 0x04 == 0x04:
            args["bit_2"] = "True"
        if cmd[1] & 0x08 == 0x08:
            args["bit_3"] = "True"
        if cmd[1] & 0x10 == 0x10:
            args["bit_4"] = "True"
        if cmd[1] & 0x20 == 0x20:
            args["bit_5"] = "True"
        if cmd[1] & 0x40 == 0x40:
            args["bit_6"] = "True"
        if cmd[1] & 0x80 == 0x80:
            args["bit_7"] = "True"
    elif opcode == 0xD8:
        cls = "MuteTimingJmp"
        args["destinations"] = '["%s"]' % cmd[1]
        include_argnames = False
    elif opcode == 0xD9:
        cls = "DisplayCantRunDialog"
    elif opcode == 0xE0:
        cls = "StoreOMEM60ToItemInventory"
    elif opcode == 0xE1:
        cls = "RunBattleEvent"
        args["script_id"] = SCRIPT_NAMES["battle_events"][shortify(cmd, 1)]
        if cmd[3] != 0:
            args["offset"] = str(cmd[3])
    else:
        cls = "Db"
        include_argnames = False
        args["args"] = "%r" % bytearray(cmd)

    return cls, args, use_identifier, include_argnames


# empty space filler: 0x11

# man, i have no idea, i think im just gonna hard patch addresses

# screen flash none = 2 bytes {0x8F 0x00}
# screen flash none 0 frames = 3 bytes {0x8F 0x00 0x00}

# theoretically, could we have multiple battle events for walking on KC/CD depending on # of party members,
# and battle logic picks which of the 3 to run?
# maybe THAT'S worth disassembling for
# figure out which battle events are unused somehow

# also need to make solo crystal battle events

# also need to disassemble battle text to not deadname birdetta
