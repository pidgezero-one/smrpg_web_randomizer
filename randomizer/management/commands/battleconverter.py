from django.core.management.base import BaseCommand

from randomizer.data.battlescripts import scripts

from randomizer.management.disassembler_common import (
    shortify,
    writeline,
)

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

TARGETS = [
    "MARIO",
    "TOADSTOOL",
    "BOWSER",
    "GENO",
    "MALLOW",
    "UNKNOWN_5",
    "UNKNOWN_6",
    "UNKNOWN_7",
    "UNKNOWN_8",
    "UNKNOWN_9",
    "UNKNOWN_10",
    "UNKNOWN_11",
    "UNKNOWN_12",
    "UNKNOWN_13",
    "UNKNOWN_14",
    "UNKNOWN_15",
    "SLOT_1",
    "SLOT_2",
    "SLOT_3",
    "MONSTER_1_SET",
    "MONSTER_2_SET",
    "MONSTER_3_SET",
    "MONSTER_4_SET",
    "MONSTER_5_SET",
    "MONSTER_6_SET",
    "MONSTER_7_SET",
    "MONSTER_8_SET",
    "SELF",
    "ALL_ALLIES_EXCLUDING_SELF",
    "RANDOM_ALLY_EXCLUDING_SELF_OPPONENT_IF_SOLO",
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
ATTACKS = [
    "PhysicalAttack0",
    "PhysicalAttack1",
    "PhysicalAttack2",
    "PhysicalAttack3",
    "PhysicalAttack4",
    "PhysicalAttack5",
    "PhysicalAttack6",
    "PhysicalAttack7",
    "PhysicalAttack8",
    "PhysicalAttack9",
    "PhysicalAttack10",
    "PhysicalAttack11",
    "PhysicalAttack12",
    "PhysicalAttack13",
    "PhysicalAttack14",
    "PhysicalAttack15",
    "PhysicalAttack16",
    "Thornet",
    "PhysicalAttack18",
    "Funguspike",
    "PhysicalAttack20",
    "PhysicalAttack21",
    "FullHouse",
    "WildCard",
    "RoyalFlush",
    "PhysicalAttack25",
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
    "SleepSauce",
    "VenomDrool",
    "MushFunk",
    "ScrowFunk",
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
    "HammerTime",
    "ValorUp",
    "PhysicalAttack98",
    "LastShot",
    "PhysicalAttack100",
    "PhysicalAttack101",
    "PhysicalAttack102",
    "PhysicalAttack103",
    "PhysicalAttack104",
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
    "PhysicalAttack124",
    "SilverBullet",
    "Terrapunch",
    "ScrowFangs",
    "Shaker",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "AttackDoNothing",
]
SPELLS = [
    "Jump",
    "FireOrb",
    "SuperJump",
    "SuperFlame",
    "UltraJump",
    "UltraFlame",
    "Therapy",
    "GroupHug",
    "SleepyTime",
    "ComeBack",
    "Mute",
    "PsychBomb",
    "Terrorize",
    "PoisonGas",
    "Crusher",
    "BowserCrush",
    "GenoBeam",
    "GenoBoost",
    "GenoWhirl",
    "GenoBlast",
    "GenoFlash",
    "Thunderbolt",
    "HPRain",
    "Psychopath",
    "Shocker",
    "Snowy",
    "StarRain",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
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
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "SpellDoNothing",
]

BATTLE_EVENTS = [
    "BE0000_UNUSED",
    "BE0001_SOLO_WIND_CRYSTAL_APPEARS",
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
    "BE0035_BOOSTER_EATS_CAKE",
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
    "BE0051_VALENTINA_DODO_END",
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
]
COMMANDS = ["COMMAND_ATTACK", "COMMAND_SPECIAL", "COMMAND_ITEM"]

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
VARIABLES = [
    "0x7EE000",
    "0x7EE001",
    "0x7EE002",
    "0x7EE003",
    "0x7EE004",
    "DESIGNATED_RANDOM_NUM_VAR",
    "ATTACK_PHASE_COUNTER",
    "0x7EE007",
    "0x7EE008",
    "0x7EE009",
    "PARTY_SIZE",
    "0x7EE00B",
    "0x7EE00C",
    "0x7EE00D",
    "0x7EE00E",
    "0x7EE00F",
]


def convert(command):
    name = command[0]
    cmdargs = command[1]

    cls = None
    args = {}
    include_argnames = True

    if name == "attack":
        cls = "Attack"
        if isinstance(cmdargs[0], int):
            args["attack_1"] = ATTACKS[cmdargs[0]]
        else:
            args["attack_1"] = ATTACKS[cmdargs[0].index]
        if len(cmdargs) > 1:
            if isinstance(cmdargs[1], int):
                args["attack_2"] = ATTACKS[cmdargs[1]]
            else:
                args["attack_2"] = ATTACKS[cmdargs[1].index]
            if isinstance(cmdargs[2], int):
                args["attack_3"] = ATTACKS[cmdargs[2]]
            else:
                args["attack_3"] = ATTACKS[cmdargs[2].index]
        include_argnames = False
    elif name == "set_target":
        cls = "SetTarget"
        args["target"] = TARGETS[cmdargs[0]]
        include_argnames = False
    elif name == "battle_dialog":
        cls = "RunBattleDialog"
        args["dialog_id"] = str(cmdargs[0])
        include_argnames = False
    elif name == "battle_event":
        cls = "RunBattleEvent"
        assert 0 <= cmdargs[0] <= 102
        args["event_id"] = BATTLE_EVENTS[cmdargs[0]]
        include_argnames = False
    elif name == "inc":
        cls = "IncreaseVarBy1"
        args["variable"] = VARIABLES[cmdargs[0] & 0x0F]
        include_argnames = False
    elif name == "dec":
        cls = "DecreaseVarBy1"
        args["variable"] = VARIABLES[cmdargs[0] & 0x0F]
        include_argnames = False
    elif name in ["set", "clear", "if_bits_set", "if_bits_clear"]:
        if name == "set":
            cls = "SetVarBits"
        elif name == "clear":
            cls = "ClearVarBits"
        elif name == "if_bits_set":
            cls = "IfVarBitsSet"
        elif name == "if_bits_clear":
            cls = "IfVarBitsClear"
        args["variable"] = VARIABLES[cmdargs[0] & 0x0F]
        bits = []
        for i in range(0, 8):
            comp = 1 << i
            if cmdargs[1] & comp == comp:
                bits.append(i)
        args["bits"] = "%r" % bits
        include_argnames = False
    elif name == "zero":
        cls = "ClearVar"
        args["variable"] = VARIABLES[cmdargs[0] & 0x0F]
        include_argnames = False
    elif name == "remove":
        cls = "RemoveTarget"
        args["target"] = TARGETS[cmdargs[0]]
        include_argnames = False
    elif name == "call":
        cls = "CallTarget"
        args["target"] = TARGETS[cmdargs[0]]
        include_argnames = False
    elif name == "invuln":
        cls = "MakeInvulnerable"
        args["target"] = TARGETS[cmdargs[0]]
        include_argnames = False
    elif name == "uninvuln":
        cls = "MakeVulnerable"
        args["target"] = TARGETS[cmdargs[0]]
        include_argnames = False
    elif name == "exit_battle":
        cls = "ExitBattle"
    elif name == "rand":
        cls = "Set7EE005ToRandomNumber"
        args["upper_bound"] = str(cmdargs[0])
    elif name == "cast_spell":
        cls = "CastSpell"
        if isinstance(cmdargs[0], int):
            args["spell_1"] = SPELLS[cmdargs[0]]
        else:
            args["spell_1"] = SPELLS[cmdargs[0].index]
        if len(cmdargs) > 1:
            if isinstance(cmdargs[1], int):
                args["spell_2"] = SPELLS[cmdargs[1]]
            else:
                args["spell_2"] = SPELLS[cmdargs[1].index]
            if isinstance(cmdargs[2], int):
                args["spell_3"] = SPELLS[cmdargs[2]]
            else:
                args["spell_3"] = SPELLS[cmdargs[2].index]
        include_argnames = False
    elif name == "animate":
        cls = "DoMonsterBehaviour"
        args["animation_id"] = str(cmdargs[0])
        include_argnames = False
    elif name == "set_untargetable":
        cls = "SetUntargetable"
        if cmdargs[0] == 0:
            args["target"] = TARGETS[0x1B]
        else:
            args["target"] = TARGETS[cmdargs[0] + 0x12]
        include_argnames = False
    elif name == "set_targetable":
        cls = "SetTargetable"
        if cmdargs[0] == 0:
            args["target"] = TARGETS[0x1B]
        else:
            args["target"] = TARGETS[cmdargs[0] + 0x12]
        include_argnames = False
    elif name in ["enable_command", "disable_command"]:
        if name == "enable_command":
            cls = "EnableCommand"
        elif name == "disable_command":
            cls = "DisableCommand"
        commands_set = []
        if cmdargs[0] & 0x01 == 0x01:
            commands_set.append("COMMAND_ATTACK")
        if cmdargs[0] & 0x02 == 0x02:
            commands_set.append("COMMAND_SPECIAL")
        if cmdargs[0] & 0x04 == 0x04:
            commands_set.append("COMMAND_ITEM")
        args["commands"] = "[%s]" % ", ".join(commands_set)
        include_argnames = False
    elif name == "remove_items":
        cls = "RemoveAllInventory"
    elif name == "return_items":
        cls = "RestoreInventory"
    elif name == "if_command":
        include_argnames = False
        cls = "IfTargetedByCommand"
        if cmdargs[0] == cmdargs[1]:
            args["commands"] = "[%s]" % COMMANDS[cmdargs[0] - 2]
        else:
            args["commands"] = "[%s]" % ", ".join(
                COMMANDS[cmdargs[0] - 2], COMMANDS[cmdargs[1] - 2]
            )
    elif name == "if_spell":
        include_argnames = False
        cls = "IfTargetedBySpell"
        nums = []
        for a in cmdargs:
            if isinstance(a, int):
                nums.append(a)
            else:
                nums.append(a.index)
        if nums[0] == nums[1]:
            args["spells"] = "[%s]" % SPELLS[nums[0]]
        else:
            args["spells"] = "[%s]" % ", ".join(SPELLS[nums[0]], SPELLS[nums[1]])

    elif name == "if_item":
        include_argnames = False
        cls = "IfTargetedByItem"
        nums = []
        for a in cmdargs:
            if isinstance(a, int):
                nums.append(a)
            else:
                nums.append(a.index)
        if nums[0] == nums[1]:
            args["items"] = "[%s]" % ITEMS[nums[0]]
        else:
            args["items"] = "[%s]" % ", ".join(ITEMS[nums[0]], ITEMS[nums[1]])
    elif name == "if_element":
        include_argnames = False
        cls = "IfTargetedByElement"
        elements = []
        if cmdargs[0] & 0x10 == 0x10:
            elements.append("Element.ICE")
        if cmdargs[0] & 0x20 == 0x20:
            elements.append("Element.THUNDER")
        if cmdargs[0] & 0x40 == 0x40:
            elements.append("Element.FIRE")
        if cmdargs[0] & 0x80 == 0x80:
            elements.append("Element.Jump")
        args["items"] = "[%s]" % ", ".join(elements)
    elif name == "if_attacked":
        cls = "IfTargetedByRegularAttack"
    elif name == "if_hp":
        cls = "IfHPBelow"
        args["threshold"] = str(cmdargs[0])
        include_argnames = False
    elif name in ["if_target_status", "if_not_target_status"]:
        if name == "if_target_status":
            cls = "IfTargetAfflictedBy"
        else:
            cls = "IfTargetNotAfflictedBy"
        elements = []
        args["target"] = TARGETS[cmdargs[0]]
        if cmdargs[1] & 0x01 == 0x01:
            elements.append("Status.Mute")
        if cmdargs[1] & (1 << 1) == (1 << 1):
            elements.append("Status.Sleep")
        if cmdargs[1] & (1 << 2) == (1 << 2):
            elements.append("Status.Poison")
        if cmdargs[1] & (1 << 3) == (1 << 3):
            elements.append("Status.Fear")
        if cmdargs[1] & (1 << 4) == (1 << 4):
            elements.append("Status.Berserk")
        if cmdargs[1] & (1 << 5) == (1 << 5):
            elements.append("Status.Mushroom")
        if cmdargs[1] & (1 << 6) == (1 << 6):
            elements.append("Status.Scarecrow")
        if cmdargs[1] & (1 << 7) == (1 << 7):
            elements.append("Status.Invincible")
        args["statuses"] = "[%s]" % ", ".join(elements)
        include_argnames = False
    elif name == "if_phase":
        cls = "IfTurnCounterEquals"
        args["phase"] = str(cmdargs[0])
        include_argnames = False
    elif name == "if_less_than":
        cls = "IfVarLessThan"
        args["variable"] = VARIABLES[cmdargs[0] & 0x0F]
        args["threshold"] = str(cmdargs[1])
        include_argnames = False
    elif name == "if_greater_or_equal":
        cls = "IfVarEqualOrGreaterThan"
        args["variable"] = VARIABLES[cmdargs[0] & 0x0F]
        args["threshold"] = str(cmdargs[1])
        include_argnames = False
    elif name == "if_target_alive":
        cls = "IfTargetAlive"
        include_argnames = False
    elif name == "if_target_dead":
        cls = "IfTargetKOed"
        include_argnames = False
    elif name == "if_monster_in_formation":
        cls = "IfCurrentlyInFormationID"
        args["formation_id"] = str(cmdargs[0])
        include_argnames = False
    elif name == "if_solo":
        cls = "IfLastMonsterStanding"
    elif name == "wait":
        cls = "Wait1Turn"
    elif name == "wait_return":
        cls = "Wait1TurnandRestartScript"
    elif name == "start_counter":
        cls = "StartCounterCommands"
    else:
        raise Exception("unknown command %s" % name)

    return cls, args, include_argnames


def convert_script(script):
    new_script = []

    for cmd in script:
        # print(cmd["identifier"])
        identifier = ""
        cls, args, include_argnames = convert(cmd)
        # print(cls, args)

        if cls is not None:
            arg_strings = []
            for key in args:
                if include_argnames:
                    arg_strings.append("%s=%s" % (key, args[key]))
                else:
                    arg_strings.append(args[key])
            arg_string = ", ".join(arg_strings)

            output = "%s(%s%s)" % (cls, arg_string, identifier)
            new_script.append(output)

    return new_script


def produce_battle_script(index, script):
    output = "# %i - %s" % (index, ENEMIES[index])
    output += "\n\nfrom randomizer.scripts.monster.script_imports import *"
    output += "\n\nscript = MonsterScript([\n\t"

    contents = convert_script(script)

    output += ",\n\t".join(contents)

    output += "\n])"

    return output


class Command(BaseCommand):
    def handle(self, *args, **options):
        export_file = open("randomizer/scripts/monster/monster_scripts.py", "w")
        export_file_output = (
            "from randomizer.types.monster_scripts.classes import MonsterScriptBank"
        )

        export_file_imports = ""
        export_file_exports = ""

        print(len(scripts))

        for i, script in enumerate(scripts):
            print(i, ENEMIES[i])
            output = produce_battle_script(i, script)
            file = open("randomizer/scripts/monster/scripts/script_%i.py" % (i), "w")
            writeline(file, output)
            file.close()
            export_file_imports += (
                "\nfrom .scripts.script_%i import script as script_%i" % (i, i)
            )
            export_file_exports += "\n\tscript_%i," % i

        export_file_output += export_file_imports
        export_file_output += "\n\nmonster_scripts = MonsterScriptBank(["
        export_file_output += export_file_exports
        export_file_output += "])"
        writeline(export_file, export_file_output)
        export_file.close()
