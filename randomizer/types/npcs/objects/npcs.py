from randomizer.types.npcs.animations.animations import (
    AXEM_BLACK_HIT,
    AXEM_GREEN_HIT,
    AXEM_GREEN_HIT_FAST,
    AXEM_PINK_HIT,
    AXEM_RED_HIT,
    AXEM_RED_HIT_FAST,
    AXEM_RED_RECOIL,
    AXEM_RED_TAUNT,
    AXEM_YELLOW_HIT,
    AXEM_YELLOW_HIT_FAST,
    BANDANA_ATTACK,
    BANDANA_TAUNT,
    BELOME_ATTACK,
    BELOME_ATTACK_FAST,
    BELOME_RECOIL,
    BELOME_WIGGLE,
    BIG_MAGIKOOPA_HIT,
    BIG_MAGIKOOPA_HIT_FAST,
    BIG_MAGIKOOPA_RECOIL,
    BIG_MAGIKOOPA_TAUNT,
    BIRDETTA_ATTACK,
    BIRDETTA_ATTACK_FAST,
    BIRDETTA_RECOIL,
    BIRDETTA_TAUNT,
    BOMB_TICK,
    BOOMER_ALT_TAUNT,
    BOOMER_RECOIL,
    BOOMER_TAUNT,
    BOOSTER_JUMP,
    BOOSTER_LAUGH,
    BOOSTER_PUNCH,
    BOOSTER_RECOIL,
    BOWSERCLONE_LAUGH,
    BOWSERCLONE_MAD,
    BOWYER_HIT,
    BOWYER_RECOIL,
    BOWYER_TAUNT,
    BOXBOY_ATTACK,
    BOXBOY_SHORT,
    BUNDT_RECOIL,
    BUNDT_TAUNT,
    CHESTER_ATTACK,
    CHESTER_ATTACK_FAST,
    CLOAKER_RECOIL,
    CROOK_SCRATCH,
    CZAR_DRAGON_HIT,
    CZAR_RECOIL,
    CZAR_TAUNT,
    DODO_PECK,
    DODO_TAUNT,
    DRILLBIT_HIT,
    DRILLBIT_HIT_FAST,
    EGGBERT_EXPAND,
    GENOCLONE_LAUGH,
    GENOCLONE_MAD,
    GOOMBETTE_HIT,
    GOOMBETTE_HIT_FAST,
    GOOMBETTE_TAUNT,
    GRATE_GUY_HIT,
    GRATE_GUY_HIT_FAST,
    GRATE_GUY_RECOIL,
    GRATE_GUY_TAUNT,
    HAMMER_BRO_BOP,
    HAMMER_BRO_BOP_FAST,
    HAMMER_BRO_RECOIL,
    HAMMER_BRO_TAUNT,
    HIDON_ATTACK,
    HIDON_ATTACK_FAST,
    JAGGER_LOOK,
    JAGGER_PUNCH,
    JAGGER_RECOIL,
    JAGGER_TAUNT,
    JOHNNY_HIT,
    JOHNNY_TAUNT,
    MACK_CHALLENGE,
    MACK_HIT,
    MACK_HIT_FAST,
    MALLOWCLONE_LAUGH,
    MALLOWCLONE_MAD,
    MARIOCLONE_HIT_FAST,
    MEGASMILAX_BITE,
    MEGASMILAX_RECOIL,
    MEGASMILAX_TAUNT,
    MIMIC_RECOIL,
    MIMIC_SHAKE,
    NINJA_HIT,
    NINJA_HIT_FAST,
    NINJA_RECOIL,
    NINJA_TAUNT,
    PANDORITE_ATTACK,
    PANDORITE_SHORT,
    PEACHCLONE_MAD,
    PIRANHA_BITE,
    PIRANHA_RECOIL,
    PIRANHA_TAUNT,
    PUNCHINELLO_HIT,
    PUNCHINELLO_HIT_FAST,
    PUNCHINELLO_JUMP,
    PUNCHINELLO_RECOIL,
    PUNCHINELLO_TAUNT,
    SHYGUY_HIT,
    SHYGUY_TAUNT,
    SHYSTER_FAST,
    SHYSTER_TAUNT,
    SMALL_JOHNNY_SIT,
    SMITHY_HIT,
    SMITHY_HIT_FAST,
    SNIFIT_SHOOT,
    SNIFIT_TAUNT,
    SQUID_HIT,
    SQUID_HIT_FAST,
    SQUID_RECOIL,
    TENTACLE_BECKON,
    TORTE_TAUNT,
    TORTE_TAUNT_FAST,
    VALENTINA_LAUGH,
    VALENTINA_RECOIL,
    VALENTINA_STAND,
    VALENTINA_TAUNT,
    YARIDOVICH_ALT_TAUNT,
    YARIDOVICH_HIT,
    YARIDOVICH_RECOIL,
    YARIDOVICH_TAUNT,
)
from randomizer.types.npcs.objects.enums import ShadowSize, VramStore
from randomizer.types.npcs.objects.palettes import (
    BELOME_2_LARGE_PALETTE,
    BELOME_2_SMALL_PALETTE,
    BOXBOY_FACE_PALETTE,
    CHESTER_FACE_PALETTE,
    CROCO_ALT_PALETTE,
    HIDON_FACE_PALETTE,
    JINX_2_ALT_PALETTE,
    JINX_3_ALT_PALETTE,
    PANDORITE_FACE_PALETTE,
)
from randomizer.types.npcs.animations.classes import SpriteAnimationCollection
from randomizer.types.npcs.objects.classes import (
    BigToad,
    CloneNPC,
    Coin,
    CrocoBase,
    Fireball,
    HammerNPC,
    ItemNPC,
    Jinx,
    MimicFace,
    MimicLarge,
    PartyNPC,
    NPC,
    ShovelKnightBoss,
    ShovelKnightBossLarge,
    SmallMagikoopa,
    SmallToad,
    StarPiece,
    Statue,
    StatueDetails,
    Trampoline,
    ValentinaBird,
    Villager,
    YoshiNPC,
)
from randomizer.types.overworld_scripts.event_scripts.constants.script_ids import (
    E0882_CHEST_KEY_PACKET,
    E0884_CHEST_FEATHER_PACKET,
    E0885_CHEST_STAR_PIECE_PACKET,
    E0886_CHEST_RING_PACKET,
    E0887_CHEST_BROOCH_PACKET,
    E0888_CHEST_SHOES_PACKET,
    E0889_CHEST_BANANA_PEEL_PACKET,
    E0890_CHEST_CROWN_PACKET,
    E0891_CHEST_BOMB_PACKET,
    E0892_CHEST_EGG_PACKET,
    E0893_CHEST_COOKIE_PACKET,
    E0894_CHEST_BERRY_PACKET,
    E0895_CHEST_CARD_PACKET,
    E0896_CHEST_GREEN_SYRUP_PACKET,
    E0897_CHEST_RED_SYRUP_PACKET,
    E0898_CHEST_BLUE_SYRUP_PACKET,
    E0899_CHEST_YELLOW_SYRUP_PACKET,
    E0900_CHEST_GREEN_JUICE_PACKET,
    E0901_CHEST_RED_JUICE_PACKET,
    E0902_CHEST_P_DRINK_PACKET,
    E0903_CHEST_D_DRINK_PACKET,
    E0904_CHEST_YELLOW_M_DRINK_PACKET,
    E0905_CHEST_BLUE_M_DRINK_PACKET,
    E0906_CHEST_FROG_DRINK_PACKET,
    E0907_CHEST_RED_M_DRINK_PACKET,
    E0908_CHEST_R_DRINK_PACKET,
    E0909_CHEST_MUSIC_PACKET,
    E0910_CHEST_STAR_DRINK_PACKET,
    E0911_CHEST_GREEN_CANDY_PACKET,
    E0912_CHEST_BLUE_CANDY_PACKET,
    E0913_CHEST_GREEN_BOMB_PACKET,
    E0914_CHEST_RED_BOMB_PACKET,
    E0915_CHEST_BLUE_BOMB_PACKET,
    E0916_CHEST_YELLOW_BOMB_PACKET,
    E0917_CHEST_BEETLE_PACKET,
    E0918_CHEST_RED_MUSHROOM_PACKET,
    E0919_CHEST_GREEN_MUSHROOM_PACKET,
    E0920_CHEST_YELLOW_MUSHROOM_PACKET,
    E0921_CHEST_FRYING_PAN_PACKET,
    E0922_CHEST_HAMMER_PACKET,
    E0923_CHEST_STICK_PACKET,
    E0924_CHEST_CHOMP_PACKET,
    E0926_CHEST_RED_SHELL_PACKET,
    E0927_CHEST_GREEN_SHELL_PACKET,
    E0928_CHEST_CHEST_PARASOL_PACKET,
    E2952_CLONE_RESERVED,
)
from randomizer.types.overworld_scripts.packets.classes import Packet
from randomizer.types.overworld_scripts.packets.packets import (
    P000_FLASHING_POOF_FLOWER,
    P001_FLASHING_POOF_MUSHROOM,
    P002_BRIEF_KEY,
    P016_BIG_COIN_BEING_COLLECTED,
    P018_SMALL_COIN_BEING_COLLECTED,
    P019_FROG_COIN_BEING_COLLECTED,
    P035_FLOWER_FALL,
    P036_MUSHROOM_FALL,
    P080_FEATHER_CHEST,
    P081_STAR_PIECE_CHEST,
    P082_FEATHER_FALL,
    P083_STAR_PIECE_FALL,
    P084_FEATHER_STATIC,
    P085_STAR_PIECE_STATIC,
    P086_FLOWER_STATIC,
    P087_MUSHROOM_STATIC,
    P088_KEY_STATIC,
    P089_KEY_FALLING,
    P091_RING_CHEST,
    P092_RING_FALL,
    P093_RING_STATIC,
    P094_BROOCH_STATIC,
    P095_BROOCH_FALL,
    P096_BROOCH_CHEST,
    P097_SHOES_STATIC,
    P098_SHOES_FALL,
    P099_SHOES_CHEST,
    P100_BANANA_STATIC,
    P101_BANANA_FALL,
    P102_BANANA_CHEST,
    P103_CROWN_CHEST,
    P104_CROWN_FALL,
    P105_CROWN_STATIC,
    P106_COIN_FALL,
    P107_SMALL_COIN_FALL,
    P108_FROG_COIN_FALL,
    P109_COIN_STATIC,
    P110_SMALL_COIN_STATIC,
    P111_FROG_COIN_STATIC,
    P112_BOMB_STATIC,
    P113_BOMB_FALL,
    P114_BOMB_CHEST,
    P115_EGG_STATIC,
    P116_EGG_FALLING,
    P117_EGG_CHEST,
    P118_COOKIE_STATIC,
    P119_COOKIE_FALL,
    P120_COOKIE_CHEST,
    P121_BERRY_STATIC,
    P122_BERRY_FALL,
    P123_BERRY_CHEST,
    P124_CARD_STATIC,
    P125_CARD_FALL,
    P126_CARD_CHEST,
    P127_GREEN_SYRUP_STATIC,
    P128_GREEN_SYRUP_FALL,
    P129_GREEN_SYRUP_CHEST,
    P130_RED_SYRUP_STATIC,
    P131_RED_SYRUP_FALL,
    P132_RED_SYRUP_CHEST,
    P133_BLUE_SYRUP_STATIC,
    P134_BLUE_SYRUP_FALL,
    P135_BLUE_SYRUP_CHEST,
    P136_YELLOW_SYRUP_STATIC,
    P137_YELLOW_SYRUP_FALL,
    P138_YELLOW_SYRUP_CHEST,
    P139_GREEN_JUICE_STATIC,
    P140_GREEN_JUICE_FALL,
    P141_GREEN_JUICE_CHEST,
    P142_RED_JUICE_STATIC,
    P143_RED_JUICE_FALL,
    P144_RED_JUICE_CHEST,
    P145_P_DRINK_STATIC,
    P146_P_DRINK_FALL,
    P147_P_DRINK_CHEST,
    P148_D_DRINK_CHEST,
    P149_D_DRINK_FALL,
    P150_D_DRINK_STATIC,
    P151_YELLOW_MUSIC_DRINK_CHEST,
    P152_YELLOW_MUSIC_DRINK_FALL,
    P153_YELLOW_MUSIC_DRINK_STATIC,
    P154_BLUE_MUSIC_DRINK_CHEST,
    P155_BLUE_MUSIC_DRINK_FALL,
    P156_BLUE_MUSIC_DRINK_STATIC,
    P157_FROG_DRINK_CHEST,
    P158_FROG_DRINK_FALL,
    P159_FROG_DRINK_STATIC,
    P160_RED_MUSIC_DRINK_CHEST,
    P161_RED_MUSIC_DRINK_FALL,
    P162_RED_MUSIC_DRINK_STATIC,
    P163_R_DRINK_STATIC,
    P164_R_DRINK_FALL,
    P165_R_DRINK_CHEST,
    P166_MUSIC_NOTE_STATIC,
    P167_MUSIC_NOTE_FALL,
    P168_MUSIC_NOTE_CHEST,
    P169_STAR_DRINK_STATIC,
    P170_STAR_DRINK_FALL,
    P171_STAR_DRINK_CHEST,
    P173_GREEN_CANDY_STATIC,
    P174_GREEN_CANDY_FALL,
    P175_GREEN_CANDY_CHEST,
    P176_BLUE_CANDY_STATIC,
    P177_BLUE_CANDY_FALL,
    P178_BLUE_CANDY_CHEST,
    P179_GREEN_BOMB_STATIC,
    P180_GREEN_BOMB_FALL,
    P181_GREEN_BOMB_CHEST,
    P182_RED_BOMB_STATIC,
    P183_RED_BOMB_FALL,
    P184_RED_BOMB_CHEST,
    P185_BLUE_BOMB_STATIC,
    P186_BLUE_BOMB_FALL,
    P187_BLUE_BOMB_CHEST,
    P188_YELLOW_BOMB_STATIC,
    P189_YELLOW_BOMB_FALL,
    P190_YELLOW_BOMB_CHEST,
    P191_BEETLE_STATIC,
    P192_BEETLE_FALL,
    P193_BEETLE_CHEST,
    P194_RED_MUSHROOM_STATIC,
    P195_RED_MUSHROOM_FALL,
    P196_RED_MUSHROOM_CHEST,
    P197_GREEN_MUSHROOM_STATIC,
    P198_GREEN_MUSHROOM_FALL,
    P199_GREEN_MUSHROOM_CHEST,
    P200_YELLOW_MUSHROOM_STATIC,
    P201_YELLOW_MUSHROOM_FALL,
    P202_YELLOW_MUSHROOM_CHEST,
    P203_FRYING_PAN_STATIC,
    P204_FRYING_PAN_FALL,
    P205_FRYING_PAN_CHEST,
    P206_HAMMER_STATIC,
    P207_HAMMER_FALL,
    P208_HAMMER_CHEST,
    P209_STICK_STATIC,
    P210_STICK_FALL,
    P211_STICK_CHEST,
    P212_CHOMP_STATIC,
    P213_CHOMP_FALL,
    P214_CHOMP_CHEST,
    P215_FAN_STATIC,
    P216_FAN_FALL,
    P217_FAN_CHEST,
    P218_RED_SHELL_STATIC,
    P219_RED_SHELL_FALL,
    P220_RED_SHELL_CHEST,
    P221_GREEN_SHELL_STATIC,
    P222_GREEN_SHELL_FALL,
    P223_GREEN_SHELL_CHEST,
    P224_PARASOL_STATIC,
    P225_PARASOL_FALL,
    P226_PARASOL_CHEST,
)
from randomizer.types.palettes.classes import Palette
from randomizer.types.sprites.constants.sprite_ids import (
    SPR0000_MARIO_WALKING_DOWN_LEFT,
    SPR0007_TOADSTOOL_WALKING_DOWN_LEFT,
    SPR0013_BOWSER_WALKING_DOWN_LEFT,
    SPR0019_MALLOW_WALKING_DOWN_LEFT,
    SPR0025_GENO_WALKING_DOWN_LEFT,
    SPR0045_YELLOW_YOSHI,
    SPR0046_PINK_YOSHI,
    SPR0047_BOSHI,
    SPR0048_CROCO,
    SPR0050_BOOSTER,
    SPR0051_GREEN_YOSHI_WALK,
    SPR0053_KING_NIMBUS,
    SPR0054_QUEEN_NIMBUS,
    SPR0055_JONATHAN_JONES,
    SPR0056_VALENTINA,
    SPR0057_MAGIKOOPA,
    SPR0059_TADPOLE,
    SPR0060_THWOMP,
    SPR0061_BIG_THWOMP,
    SPR0063_VALENTINA_STATUE,
    SPR0064_TOAD,
    SPR0065_WALLET_GUY_ALSO_CASINO_ASSISTANTS,
    SPR0066_RAINI,
    SPR0067_OLD_MAN,
    SPR0068_OLD_WOMAN,
    SPR0069_GREEN_BROWN_TOAD,
    SPR0070_CHANCELLOR,
    SPR0071_PA_MOLE,
    SPR0072_MA_MOLE,
    SPR0073_GIRL_MOLE_PINK_BOW,
    SPR0074_GIRL_MOLE_YELLOW_BOW,
    SPR0075_NIMBUSITE_BLUE,
    SPR0076_NIMBUSITE_RED,
    SPR0077_NIMBUSITE_BROWN_GREEN,
    SPR0078_NIMBUSITE_YELLOW_GREEN,
    SPR0079_NIMBUS_GUARD,
    SPR0080_TOADOFSKY,
    SPR0081_MALLOW_DOLL,
    SPR0082_BLUE_STAR_PIECE,
    SPR0083_PURPLE_STAR_PIECE,
    SPR0084_RED_STAR_PIECE,
    SPR0085_GOLD_STAR_PIECE,
    SPR0086_GREEN_STAR_PIECE,
    SPR0087_LIGHT_BLUE_STAR_PIECE,
    SPR0088_YELLOW_STAR_PIECE,
    SPR0090_BOWSER_DOLL,
    SPR0092_TOADSTOOL_DOLL,
    SPR0094_TREASURE_CHEST,
    SPR0096_MARIO_DOLL_SURPRISED,
    SPR0097_TOADSTOOL_S_PARACHUTE,
    SPR0098_ROLLING_BARREL,
    SPR0099_TRAMPOLINE_WARP,
    SPR0100_TRAMPOLINE_JUMP,
    SPR0101_TEETER_TOTTER,
    SPR0102_SAVE_POINT,
    SPR0103_CORKPEDITE,
    SPR0104_J_PUZZLE_BLOCK,
    SPR0105_YELLOW_STEPPING_BLOCK,
    SPR0106_WHIRLPOOL_WATER,
    SPR0107_HINOPIO,
    SPR0108_FACTORY_HEX_NUT,
    SPR0109_GREEN_SWITCH,
    SPR0112_MUSHROOM_BOY,
    SPR0113_MARRYMORE_MAN_GREEN,
    SPR0114_MARRYMORE_WOMAN_YELLOW,
    SPR0115_MARRYMORE_WOMAN_GREEN,
    SPR0116_MARRYMORE_KID_PURPLE,
    SPR0117_MARRYMORE_KID_BLUE_GREEN,
    SPR0118_MARRYMORE_BRIGHT_CARD_BUYER_BROWN_GREY,
    SPR0119_ROSE_TOWN_GARDENER_GREEN_GREY,
    SPR0120_OLD_WOMAN_GREEN_GREY,
    SPR0121_OLD_WOMAN_PURPLE_GREY,
    SPR0122_FAT_YOSHI_BABY,
    SPR0124_GAMEBOY_KID,
    SPR0125_FROGFUCIUS_STUDENT,
    SPR0126_CHOMP_BEHIND,
    SPR0127_WIGGLER_HEAD,
    SPR0128_BLOCK_SHADOW,
    SPR0129_RED_MAGIKOOPA,
    SPR0130_WIGGLER_BODY_SEGMENT,
    SPR0131_DODO_AS_PARSON,
    SPR0133_KNIFE_GUY_JUGGLER_STILL_RED_BALLS,
    SPR0134_KNIFE_GUY_JUGGLER,
    SPR0135_MINE_CART_BAD_PALETTE,
    SPR0137_FIREBALL_SURFACE_FROM_LAVA,
    SPR0138_PIRANHA_PLANT,
    SPR0139_GOOMBA,
    SPR0140_BULLET_BILL,
    SPR0141_GOLDEN_BULLET_BILL,
    SPR0142_FACTORY_CLERK_GREEN,
    SPR0143_LAND_S_END_CANNON,
    SPR0144_RED_DOT,
    SPR0146_COMMANDER_TROOPA,
    SPR0147_GOLDEN_BELOME,
    SPR0149_SHYGUY_IN_BOWSER_S_HELICOPTER,
    SPR0150_MACHINE_MADE_BOWYER,
    SPR0151_MACHINE_MADE_YARIDOVICH_OUT_OF_BATTLE,
    SPR0153_GUNYOLK_TOP_SECTION,
    SPR0154_GUNYOLK_OUTER_SECTION,
    SPR0155_FACTORY_CRANE,
    SPR0156_BLUE_GREEN_STAR_PIECE_SPINNING,
    SPR0157_SMITHY_S_HAMMER,
    SPR0158_SMITHY_S_CHEST,
    SPR0159_POISON_TOXIC_GAS,
    SPR0161_DYNA_AND_MITE,
    SPR0162_SEASIDE_TOWN_FAKE_GREEN,
    SPR0163_SEASIDE_TOWN_FAKE_ELDER_GREEN,
    SPR0164_SEASIDE_TOWN_ELDER_YELLOW_GREEN,
    SPR0165_MONSTERMAMA_GOLDEN_BROWN_RED,
    SPR0166_NIMBUS_GUARD,
    SPR0167_FACTORY_MANAGER_BLUE,
    SPR0168_FACTORY_DIRECTOR_RED,
    SPR0169_BOOMER_RED,
    SPR0170_DR_TOPPER_GREEN,
    SPR0171_SPARKLES_FROM_STAR_PIECE,
    SPR0172_GENO_DOLL,
    SPR0173_SMELTER_BACK_SECTION,
    SPR0174_AERO_UPRIGHT,
    SPR0175_GOLDEN_CHOMP_BACK,
    SPR0177_GRATE_GUY_FROM_CASINO,
    SPR0178_MARRYMORE_INN_KEEPER_BLUE_STRIPED_HAT,
    SPR0179_ROSE_TOWN_TREASURE_HOLDER,
    SPR0180_ROSE_TOWN_WOMAN_BLUE_PINK_BRAIDS,
    SPR0181_MARRYMORE_WOMAN_YELLOW,
    SPR0182_ROSE_TOWN_OLD_MAN_BLUE_GREY,
    SPR0183_OLD_WOMAN_GREY_RED,
    SPR0184_KID_RED_STRIPED_HAT,
    SPR0185_GAZ_PURPLE,
    SPR0188_CANNON_BALL,
    SPR0190_CROCO_OVERWORLD,
    SPR0191_JINX_OVERWORLD,
    SPR0192_COIN,
    SPR0193_SMALL_COIN,
    SPR0194_FROG_COIN,
    SPR0195_FLOWER,
    SPR0196_RING,
    SPR0197_SPARKLE_SIDEWAYS,
    SPR0198_SPARKLE_DOWNWARDS,
    SPR0199_FRYING_PAN_PACKET,
    SPR0200_EXPLOSION,
    SPR0201_MOKURA_S_CLOUD_BLUE,
    SPR0202_SHOES,
    SPR0205_MICROBOMB_PACKET,
    SPR0206_CARD,
    SPR0207_BROOCH,
    SPR0208_HAMMER_PACKET,
    SPR0209_STICK_PACKET,
    SPR0210_CHOMP_PACKET,
    SPR0211_FAN_PACKET,
    SPR0212_RED_MUSHROOM_ITEM,
    SPR0213_AXEM_RED_TELEPORT,
    SPR0214_GREEN_MUSHROOM_ITEM,
    SPR0215_YELLOW_MUSHROOM_ITEM,
    SPR0216_CROWN,
    SPR0217_GREEN_CANDY,
    SPR0218_BLUE_CANDY,
    SPR0219_RED_SYRUP,
    SPR0220_GREEN_SYRUP,
    SPR0221_YELLOW_SYRUP,
    SPR0222_BANANA_PEEL,
    SPR0223_BLUE_SYRUP,
    SPR0224_RED_BOMB,
    SPR0226_TINY_STAR,
    SPR0233_GREEN_BOMB,
    SPR0234_YELLOW_BOMB,
    SPR0235_BLUE_BOMB,
    SPR0236_GREEN_JUICE,
    SPR0237_EGG,
    SPR0238_RED_JUICE,
    SPR0239_BLUE_R_DRINK,
    SPR0240_YELLOW_D_DRINK,
    SPR0241_GREEN_P_DRINK,
    SPR0244_GREEN_FROG_DRINK,
    SPR0245_YELLOW_MUSIC_DRINK,
    SPR0246_BLUE_MUSIC_DRINK,
    SPR0247_RED_MUSIC_DRINK,
    SPR0248_RED_STAR_DRINK,
    SPR0249_RED_SHELL,
    SPR0250_GREEN_SHELL,
    SPR0251_PARASOL_PACKET,
    SPR0252_FEATHER,
    SPR0253_BERRY,
    SPR0254_YOSHI_COOKIE,
    SPR0255_BEETLE,
    SPR0256_TERRAPIN,
    SPR0257_SPIKEY,
    SPR0258_SKY_TROOPA,
    SPR0259_MAD_MALLET,
    SPR0260_SHAMAN,
    SPR0261_CROOK,
    SPR0262_GOOMBA,
    SPR0263_PIRANHA_PLANT,
    SPR0264_AMANITA,
    SPR0265_GOBY,
    SPR0266_BLOOBER,
    SPR0267_BANDANA_RED,
    SPR0268_LAKITU,
    SPR0269_BIRDY,
    SPR0270_PINWHEEL,
    SPR0271_RAT_FUNK,
    SPR0272_K,
    SPR0273_MAGMITE,
    SPR0274_THE_BIG_BOO,
    SPR0275_DRY_BONES,
    SPR0276_GREAPER,
    SPR0277_SPARKY,
    SPR0278_CHOMP,
    SPR0279_PANDORITE,
    SPR0281_BOB_OMB,
    SPR0282_SPOOKUM,
    SPR0283_HAMMER_BRO,
    SPR0284_BUZZER,
    SPR0285_AMEBOID,
    SPR0286_GECKO,
    SPR0287_WIGGLER,
    SPR0291_JAWFUL,
    SPR0294_GUERRILLA,
    SPR0298_SHOGUN,
    SPR0300_HEAVY_TROOPA,
    SPR0320_TERRA_COTTA,
    SPR0321_SPIKESTER,
    SPR0322_MALAKOOPA,
    SPR0323_POUNDER,
    SPR0324_POUNDETTE,
    SPR0325_SACKIT,
    SPR0326_GU_GOOMBA,
    SPR0327_CHEWY,
    SPR0328_FIREBALL,
    SPR0329_MR_KIPPER,
    SPR0330_FACTORY_CHIEF,
    SPR0331_BANDANA_BLUE,
    SPR0333_BLUEBIRD,
    SPR0335_ALLEY_RAT,
    SPR0336_CHOW,
    SPR0337_MAGMUS,
    SPR0338_LI_XX_L_BOO,
    SPR0339_VOMER,
    SPR0340_GLUM_REAPER,
    SPR0343_HIDON,
    SPR0344_SLING_SHY,
    SPR0345_ROB_OMB,
    SPR0346_SHY_GUY,
    SPR0347_NINJA,
    SPR0348_STINGER,
    SPR0350_GECKIT,
    SPR0351_JABIT,
    SPR0353_MERLIN,
    SPR0384_APPRENTICE,
    SPR0388_GENO_REDEMPTION,
    SPR0390_BOX_BOY,
    SPR0394_OERLIKON,
    SPR0395_CHESTER,
    SPR0398_TORTE,
    SPR0399_SHY_AWAY,
    SPR0401_MACHINE_MADE_SHYSTER,
    SPR0402_MACHINE_MADE_DRILL_BIT,
    SPR0409_MARIO_CLONE,
    SPR0410_TOADSTOOL,
    SPR0411_BOWSER_CLONE,
    SPR0412_GENO_CLONE,
    SPR0413_MALLOW_CLONE,
    SPR0414_SHYSTER,
    SPR0417_HANGIN_XX_SHY,
    SPR0419_MACHINE_MADE_MACK,
    SPR0422_MACHINE_MADE_AXEM_PINK,
    SPR0423_MACHINE_MADE_AXEM_BLACK,
    SPR0424_MACHINE_MADE_AXEM_RED,
    SPR0425_MACHINE_MADE_AXEM_YELLOW,
    SPR0426_MACHINE_MADE_AXEM_GREEN,
    SPR0432_STARSLAP,
    SPR0433_MUKUMUKU,
    SPR0434_ZEOSTAR,
    SPR0440_MICROBOMB,
    SPR0445_HELIO,
    SPR0450_BUNDT,
    SPR0458_SMILAX,
    SPR0459_THRAX,
    SPR0460_MEGASMILAX,
    SPR0461_BIRDETTA,
    SPR0462_EGGBERT,
    SPR0463_AXEM_YELLOW,
    SPR0464_PUNCHINELLO,
    SPR0466_AXEM_RED,
    SPR0467_AXEM_GREEN,
    SPR0477_CLOAKER_ST_TIME,
    SPR0478_DOMINO_ND_TIME,
    SPR0483_DRILL_BIT,
    SPR0484_AXEM_PINK,
    SPR0485_AXEM_BLACK,
    SPR0487_AERO,
    SPR0504_SNIFIT,
    SPR0572_COUNT_DOWN_GRIDPLANE,
    SPR0573_MOKURA,
    SPR0583_PANDORITE_SMALL,
    SPR0584_HIDON_SMALL,
    SPR0585_CHESTER_SMALL,
    SPR0586_BOX_BOY_SMALL,
    SPR0587_HAMMER_BRO_SMALL,
    SPR0588_MACK_SMALL,
    SPR0589_BELOME_SMALL,
    SPR0590_BELOME_SMALL,
    SPR0591_BOWYER_SMALL,
    SPR0592_PUNCHINELLO_SMALL,
    SPR0593_DODO_SMALL,
    SPR0594_BIRDETTA_SMALL,
    SPR0595_CZAR_DRAGON_SMALL,
    SPR0596_BOOMER_SMALL,
    SPR0597_EXOR_SMALL,
    SPR0598_DOMINO_SMALL,
    SPR0599_SMITHY_SMALL,
    SPR0600_MARIO_DOLL_UNAFFECTED_BY_MAIN_CHARACTER_PALETTE,
    SPR0602_GOLD_GOOMBA,
    SPR0605_BIG_FLOWER,
    SPR0606_SMALL_FROG_COIN,
    SPR0607_JINX_OVERWORLD,
    SPR0608_JINX_OVERWORLD,
    SPR0609_TERRAPIN_ENDING_CREDITS,
    SPR0610_STUMPET_HEAD,
    SPR0611_STUMPET_ROOTS_RIGHT,
    SPR0612_CZAR_DRAGON_BODY,
    SPR0613_GROWING_VINE_BEANSTALK,
    SPR0614_BRICK_BEANSTALK_BLOCK,
    SPR0615_WHIRLPOOL_DESERT,
    SPR0616_YELLOW_LETTER,
    SPR0617_YARIDOVICH_OUT_OF_BATTLE,
    SPR0618_TENTACLE_EXTENDING,
    SPR0619_SNIFIT_BLACK_BACK,
    SPR0620_FALLING_STEPPING_BRIDGE_BLOCK,
    SPR0621_OLD_CLASSIC_MARIO,
    SPR0623_SPLASH_WATER_DROPLETS,
    SPR0624_SMALL_SEA_FISH,
    SPR0625_SPLASH_WATER_GEYSER,
    SPR0626_BOWYER,
    SPR0627_MUSHROOM_HOUSE_DECOR_MAILBOX,
    SPR0628_LINK_SLEEPING_IN_ROSE_TOWN_INN,
    SPR0629_SAMUS_SLEEPING_IN_MUSHROOM_KINGDOM,
    SPR0630_GREY_STEPPING_STONE,
    SPR0631_HINOPIO_S_MODEL_AIRPLANE_BLUE_GREY,
    SPR0632_GREY_STONE_BLOCK,
    SPR0633_CULEX_SMALL,
    SPR0635_SPARKLE_CIRCULAR_WINDING,
    SPR0636_SMALL_FLOWER_STANDALONE,
    SPR0637_RECOVERY_MUSHROOM_STANDALONE,
    SPR0638_KEY_STANDALONE,
    SPR0639_ITEM_BAG_STANDALONE,
    SPR0640_MUSIC_NOTE_STANDALONE,
    SPR0641_AMANITA_MUSHROOM_STANDALONE,
    SPR0642_DINGALING_GRIDPLANE,
    SPR0643_EGGBERT_GRIDPLANE,
    SPR0644_FIRE_CRYSTAL_GRIDPLANE,
    SPR0645_WATER_CRYSTAL_GRIDPLANE,
    SPR0646_EARTH_CRYSTAL_GRIDPLANE,
    SPR0647_WIND_CRYSTAL_GRIDPLANE,
    SPR0648_GENO_ARM_SHOT,
    SPR0649_MACK_MEDIUM,
    SPR0650_KNIFE_GUY_GRIDPLANE,
    SPR0651_TINY_BLOOBER_STANDALONE,
    SPR0652_MIMIC_STATUE,
    SPR0653_CROCO_STATUE,
    SPR0654_BOOSTER_STATUE,
    SPR0655_JOHNNY_STATUE,
    SPR0656_MAGIKOOPA_STATUE,
    SPR0657_CLERK_MANAGER_DIRECTOR_STATUE,
    SPR0658_FAKE_ELDER_STATUE,
    SPR0659_GRATE_GUY_STATUE,
    SPR0660_JINX_STATUE,
    SPR0661_MOKURA_STATUE,
    SPR0662_JAGGER_STATUE,
    SPR0663_PIRANHA_PLANT_STATUE,
    SPR0664_BLOOBER_STATUE,
    SPR0665_FACTORY_CHIEF_STATUE,
    SPR0666_AXEM_RED_STATUE,
    SPR0667_BUNDT_STATUE,
    SPR0668_COUNT_DOWN_STATUE,
    SPR0669_HAMMER_BRO_STATUE,
    SPR0670_MACK_STATUE,
    SPR0671_SMALL_BELOME_STATUE,
    SPR0672_BELOME_LARGE_OVERWORLD,
    SPR0673_BOWYER_STATUE,
    SPR0674_PUNCHINELLO_STATUE,
    SPR0675_DODO_STATUE,
    SPR0676_BIRDETTA_STATUE,
    SPR0677_CZAR_DRAGON_STATUE,
    SPR0678_BOOMER_STATUE,
    SPR0679_EXOR_STATUE,
    SPR0680_DOMINO_STATUE,
    SPR0681_SMITHY_STATUE,
    SPR0682_CULEX_STATUE,
    SPR0683_MALLOW_STATUE_UNTINTED,
    SPR0685_CHOMPWEED,
    SPR0686_MACK_SUB,
    SPR0687_BELOME_SUB,
    SPR0688_BOWYER_SUB,
    SPR0689_KNIFE_GUY_SUB,
    SPR0690_GRATE_GUY_SUB,
    SPR0691_JOHNNY_SUB,
    SPR0692_YARIDOVICH_SUB,
    SPR0694_CULEX_SUB,
    SPR0695_DODO_SUB,
    SPR0697_VALENTINA_SUB,
    SPR0698_CZAR_DRAGON_SUB,
    SPR0701_BOOMER_SUB,
    SPR0702_CLERK_SUB,
    SPR0703_MANAGER_SUB,
    SPR0704_DIRECTOR_SUB,
    SPR0706_BEETLE_GRIDPLANE,
    SPR0707_BANANA_GRIDPLANE,
    SPR0708_CROWN_GRIDPLANE,
    SPR0709_BROOCH_GRIDPLANE,
    SPR0710_SHOES_GRIDPLANE,
    SPR0711_RING_GRIDPLANE,
    SPR0712_EMPTY,
    SPR0777_STAR_EGG_LITTLE_BROWN_BIRD,
    SPR0959_SMITHY_LOWER,
    SPR0960_GOOMBETTE_LOWER,
    SPR1023_EMPTY,
)


class Mario(PartyNPC):
    _sprite_id: int = SPR0000_MARIO_WALKING_DOWN_LEFT
    _y_shift: int = 1
    _directions = VramStore.DIR7_ALL_DIRECTIONS
    _minecart_shift: int = 7


class Toadstool(PartyNPC):
    _sprite_id: int = SPR0007_TOADSTOOL_WALKING_DOWN_LEFT
    _y_shift: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE
    _minecart_shift: int = 6


class Bowser(PartyNPC):
    _sprite_id: int = SPR0013_BOWSER_WALKING_DOWN_LEFT
    _shadow_size = ShadowSize.OVAL_BIG
    _acute_axis: int = 6
    _obtuse_axis: int = 6
    _height: int = 14
    _y_shift: int = -2
    _directions = VramStore.DIR0_SWSE_NWNE


class Mallow(PartyNPC):
    _sprite_id: int = SPR0019_MALLOW_WALKING_DOWN_LEFT
    _height: int = 8
    _directions = VramStore.DIR0_SWSE_NWNE
    _minecart_shift: int = 4


class Geno(PartyNPC):
    _sprite_id: int = SPR0025_GENO_WALKING_DOWN_LEFT
    _y_shift: int = 1
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _directions = VramStore.DIR0_SWSE_NWNE
    _minecart_shift: int = 9


class YellowYoshi(YoshiNPC):
    _sprite_id: int = SPR0045_YELLOW_YOSHI
    _byte2_bit0: bool = True
    _byte2_bit3: bool = True


class PinkYoshi(YoshiNPC):
    _sprite_id: int = SPR0046_PINK_YOSHI


class Boshi(YoshiNPC):
    _sprite_id: int = SPR0047_BOSHI
    _min_vram_size: int = 0


class Croco(CrocoBase):
    _sprite_id: int = SPR0048_CROCO


class RideYoshi(YoshiNPC):
    _sprite_id: int = 49
    _directions = VramStore.DIR7_ALL_DIRECTIONS


class Booster(NPC):
    _sprite_id: int = SPR0050_BOOSTER
    _directions = VramStore.DIR0_SWSE_NWNE
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _y_shift: int = 2

    _animations = SpriteAnimationCollection(
        recoil=BOOSTER_RECOIL,
        bandits_way_distracted=BOOSTER_LAUGH,
        mines_punch=BOOSTER_PUNCH,
        chapel_laugh=BOOSTER_LAUGH,
        ship_beckon=BOOSTER_LAUGH,
        ship_chair=BOOSTER_LAUGH,
        dojo_challenge=BOOSTER_JUMP,
        statue_intro=BOOSTER_LAUGH,
        statue_flustered=BOOSTER_JUMP,
        keep_challenge=BOOSTER_JUMP,
        keep_summon=BOOSTER_LAUGH,
        chandelier_challenge=BOOSTER_PUNCH,
        endgame_challenge=BOOSTER_PUNCH,
    )
    _eye_height: int = 17


class GreenYoshi(YoshiNPC):
    _sprite_id: int = SPR0051_GREEN_YOSHI_WALK
    _min_vram_size: int = 0
    _byte2_bit0: bool = True
    _byte2_bit4: bool = True


class KingNimbus(NPC):
    _sprite_id: int = SPR0053_KING_NIMBUS
    _directions = VramStore.DIR0_SWSE_NWNE
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 11
    _y_shift: int = 1


class QueenNimbus(NPC):
    _sprite_id: int = SPR0054_QUEEN_NIMBUS
    _directions = VramStore.DIR0_SWSE_NWNE
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 11
    _y_shift: int = 1


class JohnnySmall(NPC):
    _sprite_id: int = SPR0055_JONATHAN_JONES
    _directions = VramStore.DIR0_SWSE_NWNE
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 11
    _y_shift: int = 2

    _animations = SpriteAnimationCollection(
        bandits_way_distracted=SMALL_JOHNNY_SIT,
        chapel_laugh=SMALL_JOHNNY_SIT,
        ship_beckon=SMALL_JOHNNY_SIT,
        ship_chair=SMALL_JOHNNY_SIT,
        dojo_challenge=SMALL_JOHNNY_SIT,
        keep_challenge=SMALL_JOHNNY_SIT,
        chandelier_challenge=SMALL_JOHNNY_SIT,
        endgame_challenge=SMALL_JOHNNY_SIT,
    )
    _eye_height: int = 20


class ValentinaSmall(NPC):
    _sprite_id: int = SPR0056_VALENTINA
    _directions = VramStore.DIR0_SWSE_NWNE
    _y_shift: int = 1

    _eye_height: int = 16
    _animations = SpriteAnimationCollection(
        bandits_way_distracted=VALENTINA_STAND,
        chapel_laugh=VALENTINA_LAUGH,
        ship_beckon=VALENTINA_LAUGH,
        ship_chair=VALENTINA_STAND,
        dojo_challenge=VALENTINA_LAUGH,
        statue_intro=VALENTINA_LAUGH,
        keep_challenge=VALENTINA_LAUGH,
        keep_summon=VALENTINA_LAUGH,
        chandelier_challenge=VALENTINA_LAUGH,
        endgame_challenge=VALENTINA_LAUGH,
    )


class MagikoopaSmall(SmallMagikoopa):
    _sprite_id: int = SPR0057_MAGIKOOPA


class Frogfucius(NPC):
    _sprite_id: int = 58
    _directions = VramStore.DIR0_SWSE_NWNE
    _height: int = 11


class Tadpole(NPC):
    _sprite_id: int = SPR0059_TADPOLE
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _directions = VramStore.DIR0_SWSE_NWNE
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 5
    _y_shift: int = 1


class Thwomp(NPC):
    _sprite_id: int = SPR0060_THWOMP
    _acute_axis: int = 8
    _obtuse_axis: int = 6
    _height: int = 11
    _shadow_size = ShadowSize.OVAL_BIG


class BigThwomp(NPC):
    _sprite_id: int = SPR0061_BIG_THWOMP
    _acute_axis: int = 14
    _obtuse_axis: int = 8
    _height: int = 18
    _shadow_size = ShadowSize.OVAL_BIG
    _min_vram_size: int = 2


class NimbusLandStatue(NPC):
    _sprite_id: int = SPR0063_VALENTINA_STATUE
    _show_shadow: bool = False


class RedSmallToad(SmallToad):
    _sprite_id: int = SPR0064_TOAD


class BlueToad(BigToad):
    _sprite_id: int = SPR0065_WALLET_GUY_ALSO_CASINO_ASSISTANTS


class PinkToad(BigToad):
    _sprite_id: int = SPR0066_RAINI


class OldBlueToad(BigToad):
    _sprite_id: int = SPR0067_OLD_MAN


class OldRedToad(BigToad):
    _sprite_id: int = SPR0068_OLD_WOMAN


class GreenSmallToad(SmallToad):
    _sprite_id: int = SPR0069_GREEN_BROWN_TOAD


class Chancellor(Villager):
    _sprite_id: int = SPR0070_CHANCELLOR
    _height: int = 9
    _y_shift: int = 1


class PaMole(Villager):
    _sprite_id: int = SPR0071_PA_MOLE
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _y_shift: int = 2


class MaMole(Villager):
    _sprite_id: int = SPR0072_MA_MOLE
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _y_shift: int = 2


class PinkMole(Villager):
    _sprite_id: int = SPR0073_GIRL_MOLE_PINK_BOW
    _height: int = 6
    _y_shift: int = 1


class YellowMole(Villager):
    _sprite_id: int = SPR0074_GIRL_MOLE_YELLOW_BOW
    _height: int = 6
    _y_shift: int = 1


class BlueNimbite(Villager):
    _sprite_id: int = SPR0075_NIMBUSITE_BLUE
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 11
    _y_shift: int = 1


class RedNimbite(Villager):
    _sprite_id: int = SPR0076_NIMBUSITE_RED
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 11
    _y_shift: int = 1


class BrownNimbite(Villager):
    _sprite_id: int = SPR0077_NIMBUSITE_BROWN_GREEN
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 11
    _y_shift: int = 1


class GreenNimbite(Villager):
    _sprite_id: int = SPR0078_NIMBUSITE_YELLOW_GREEN
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 11
    _y_shift: int = 1


class NimbusGuard(Villager):
    _sprite_id: int = SPR0079_NIMBUS_GUARD
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 11


class Toadofsky(NPC):
    _sprite_id: int = SPR0080_TOADOFSKY
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 11


class MallowDoll(NPC):
    _sprite_id: int = SPR0081_MALLOW_DOLL
    _shadow_size = ShadowSize.OVAL_SMALL
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 3
    _y_shift: int = 1


class BlueStarPiece(StarPiece):
    _sprite_id: int = SPR0082_BLUE_STAR_PIECE


class PurpleStarPiece(StarPiece):
    _sprite_id: int = SPR0083_PURPLE_STAR_PIECE


class RedStarPiece(StarPiece):
    _sprite_id: int = SPR0084_RED_STAR_PIECE


class OrangeStarPiece(StarPiece):
    _sprite_id: int = SPR0085_GOLD_STAR_PIECE


class GreenStarPiece(StarPiece):
    _sprite_id: int = SPR0086_GREEN_STAR_PIECE


class IndigoStarPiece(StarPiece):
    _sprite_id: int = SPR0087_LIGHT_BLUE_STAR_PIECE


class YellowStarPiece(StarPiece):
    _sprite_id: int = SPR0088_YELLOW_STAR_PIECE


class BowserDoll(NPC):
    _sprite_id: int = SPR0090_BOWSER_DOLL
    _shadow_size = ShadowSize.OVAL_SMALL
    _directions = VramStore.DIR0_SWSE_NWNE
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 3
    _y_shift: int = 1


class ToadstoolDoll(NPC):
    _sprite_id: int = SPR0092_TOADSTOOL_DOLL
    _shadow_size = ShadowSize.OVAL_SMALL
    _directions = VramStore.DIR0_SWSE_NWNE
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 3
    _y_shift: int = 1


class TreasureChest(NPC):
    _sprite_id: int = SPR0094_TREASURE_CHEST
    _shadow_size = ShadowSize.BLOCK
    _y_shift: int = -2
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 8
    _min_vram_size: int = 1


class MidasRiverMario(NPC):
    _sprite_id: int = SPR0096_MARIO_DOLL_SURPRISED
    _shadow_size = ShadowSize.OVAL_SMALL
    _acute_axis: int = 2
    _obtuse_axis: int = 2
    _height: int = 5
    _y_shift: int = 1


class Parachute(NPC):
    _sprite_id: int = SPR0097_TOADSTOOL_S_PARACHUTE
    _shadow_size = ShadowSize.OVAL_SMALL
    _show_shadow: bool = False
    _sprite_id: int = 97
    _acute_axis: int = 8
    _obtuse_axis: int = 8
    _y_shift: int = 1


class Barrel(NPC):
    _sprite_id: int = SPR0098_ROLLING_BARREL
    _shadow_size = ShadowSize.OVAL_SMALL
    _show_shadow: bool = False
    _y_shift: int = 1
    _acute_axis: int = 6
    _obtuse_axis: int = 6
    _height: int = 11


class WarpTrampoline(Trampoline):
    _sprite_id: int = SPR0099_TRAMPOLINE_WARP


class JumpTrampoline(Trampoline):
    _sprite_id: int = SPR0100_TRAMPOLINE_JUMP


class Seesaw(NPC):
    _sprite_id: int = SPR0101_TEETER_TOTTER
    _shadow_size = ShadowSize.OVAL_SMALL
    _show_shadow: bool = False
    _y_shift: int = 1
    _acute_axis: int = 14
    _obtuse_axis: int = 5
    _height: int = 5
    _min_vram_size: int = 2


class SavePoint(NPC):
    _sprite_id: int = SPR0102_SAVE_POINT
    _y_shift: int = -2
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 7
    _shadow_size = ShadowSize.BLOCK


class Corkpedite(NPC):
    _sprite_id: int = SPR0103_CORKPEDITE
    _shadow_size = ShadowSize.OVAL_SMALL
    _show_shadow: bool = False
    _y_shift: int = 1
    _acute_axis: int = 14
    _obtuse_axis: int = 14
    _height: int = 23
    _min_vram_size: int = 3


class JBlock(NPC):
    _sprite_id: int = SPR0104_J_PUZZLE_BLOCK
    _y_shift: int = 1
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 7
    _shadow_size = ShadowSize.BLOCK
    _show_shadow: bool = False


class YellowPlatform(NPC):
    _sprite_id: int = SPR0105_YELLOW_STEPPING_BLOCK
    _y_shift: int = -1
    _acute_axis: int = 6
    _obtuse_axis: int = 6
    _height: int = 4
    _shadow_size = ShadowSize.BLOCK


class WhirlpoolBubble(NPC):
    _sprite_id: int = SPR0106_WHIRLPOOL_WATER
    _y_shift: int = 1
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 1
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL


class Hinopio(NPC):
    _sprite_id: int = SPR0107_HINOPIO
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 10
    _directions = VramStore.DIR0_SWSE_NWNE


class FactoryNut(NPC):
    _sprite_id: int = SPR0108_FACTORY_HEX_NUT
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 2
    _obtuse_axis: int = 2
    _height: int = 11


class GreenSwitch(NPC):
    _sprite_id: int = SPR0109_GREEN_SWITCH
    _shadow_size = ShadowSize.OVAL_BIG
    _y_shift: int = -2
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 3


class RedToad(BigToad):
    _sprite_id: int = SPR0112_MUSHROOM_BOY


class GreenToad(BigToad):
    _sprite_id: int = SPR0113_MARRYMORE_MAN_GREEN


class YellowToad(BigToad):
    _sprite_id: int = SPR0114_MARRYMORE_WOMAN_YELLOW


class TurquoiseToad(BigToad):
    _sprite_id: int = SPR0115_MARRYMORE_WOMAN_GREEN


class PinkSmallToad(SmallToad):
    _sprite_id: int = SPR0116_MARRYMORE_KID_PURPLE


class BlueSmallToad(SmallToad):
    _sprite_id: int = SPR0117_MARRYMORE_KID_BLUE_GREEN


class OldBrownToad(BigToad):
    _sprite_id: int = SPR0118_MARRYMORE_BRIGHT_CARD_BUYER_BROWN_GREY


class OldGreenToad(BigToad):
    _sprite_id: int = SPR0119_ROSE_TOWN_GARDENER_GREEN_GREY


class OldDarkGreenToad(BigToad):
    _sprite_id: int = SPR0120_OLD_WOMAN_GREEN_GREY


class OldPinkToad(BigToad):
    _sprite_id: int = SPR0121_OLD_WOMAN_PURPLE_GREY


class FatYoshi(NPC):
    _sprite_id: int = SPR0122_FAT_YOSHI_BABY
    _acute_axis: int = 5
    _obtuse_axis: int = 5


class PurpleSmallToad(SmallToad):
    _sprite_id: int = SPR0124_GAMEBOY_KID


class FrogDisciple(NPC):
    _sprite_id: int = SPR0125_FROGFUCIUS_STUDENT
    _y_shift: int = 1
    _acute_axis: int = 4
    _height: int = 10


class ChompBehind(NPC):
    _sprite_id: int = SPR0126_CHOMP_BEHIND
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 9
    _obtuse_axis: int = 9
    _height: int = 10
    _min_vram_size: int = 2


class WigglerHead(NPC):
    _sprite_id: int = SPR0127_WIGGLER_HEAD
    _directions = VramStore.DIR0_SWSE_NWNE
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 9


class BlockShadow(NPC):
    _sprite_id: int = SPR0128_BLOCK_SHADOW
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = -7
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 0


class RedMagikoopa(SmallMagikoopa):
    _sprite_id: int = SPR0129_RED_MAGIKOOPA

    _eye_height: int = 12


class WigglerBody(NPC):
    _sprite_id: int = SPR0130_WIGGLER_BODY_SEGMENT
    _directions = VramStore.DIR0_SWSE_NWNE
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 7
    _y_shift: int = 1


class ParsonDodo(NPC):
    _sprite_id: int = SPR0131_DODO_AS_PARSON
    _shadow_size = ShadowSize.OVAL_BIG
    _min_vram_size: int = 4
    _acute_axis: int = 2
    _obtuse_axis: int = 2
    _height: int = 5


class KnifeGuySmall(NPC):
    _sprite_id: int = SPR0133_KNIFE_GUY_JUGGLER_STILL_RED_BALLS
    _min_vram_size: int = 2
    _y_shift: int = 1
    _acute_axis: int = 7
    _obtuse_axis: int = 7


class KnifeGuySmall2(NPC):
    _sprite_id: int = SPR0134_KNIFE_GUY_JUGGLER
    _min_vram_size: int = 2
    _y_shift: int = 1
    _acute_axis: int = 7
    _obtuse_axis: int = 7


class Minecart(NPC):
    _sprite_id: int = SPR0135_MINE_CART_BAD_PALETTE
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 5
    _acute_axis: int = 6
    _obtuse_axis: int = 7
    _height: int = 8


class FlatFireball(NPC):
    _sprite_id: int = SPR0137_FIREBALL_SURFACE_FROM_LAVA
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 5


class PipePiranhaPlant(NPC):
    _sprite_id: int = SPR0138_PIRANHA_PLANT
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1


class ThumpGoomba(NPC):
    _sprite_id: int = SPR0139_GOOMBA
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 10


class BulletBill(NPC):
    _sprite_id: int = SPR0140_BULLET_BILL
    _directions = VramStore.DIR0_SWSE_NWNE
    _y_shift: int = 1
    _acute_axis: int = 3
    _obtuse_axis: int = 7
    _height: int = 6


class GoldenBulletBill(NPC):
    _sprite_id: int = SPR0141_GOLDEN_BULLET_BILL
    _directions = VramStore.DIR0_SWSE_NWNE
    _y_shift: int = 1
    _acute_axis: int = 3
    _obtuse_axis: int = 7
    _height: int = 6


class ClerkSmall(ShovelKnightBoss):
    _sprite_id: int = SPR0142_FACTORY_CLERK_GREEN


class LandsEndCannon(NPC):
    _sprite_id: int = SPR0143_LAND_S_END_CANNON
    _shadow_size = ShadowSize.OVAL_BIG
    _y_shift: int = 1
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 11


class BerryGridplane(ItemNPC):
    _sprite_id: int = SPR0144_RED_DOT
    _y_shift: int = 1


class CommanderTroopa(NPC):
    _sprite_id: int = SPR0146_COMMANDER_TROOPA
    _y_shift: int = -1
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 7
    _directions = VramStore.DIR0_SWSE_NWNE
    _min_vram_size: int = 1


class BelomeStatue(NPC):
    _sprite_id: int = SPR0147_GOLDEN_BELOME
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 2
    _acute_axis: int = 10
    _obtuse_axis: int = 10
    _height: int = 18
    _min_vram_size: int = 5

    _animations = SpriteAnimationCollection(
        mines_punch=BELOME_ATTACK,
        statue_intro=BELOME_WIGGLE,
        statue_flustered=BELOME_RECOIL,
        statue_peck=BELOME_ATTACK_FAST,
        chandelier_challenge=BELOME_ATTACK,
        endgame_challenge=BELOME_ATTACK,
    )


class ShyGuyClownCar(NPC):
    _sprite_id: int = SPR0149_SHYGUY_IN_BOWSER_S_HELICOPTER
    _y_shift: int = 1
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 1
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL


class MachineBowyer(NPC):
    _sprite_id: int = SPR0150_MACHINE_MADE_BOWYER
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 14
    _obtuse_axis: int = 9
    _height: int = 16
    _min_vram_size: int = 3


class MachineYaridOverworld(NPC):
    _sprite_id: int = SPR0151_MACHINE_MADE_YARIDOVICH_OUT_OF_BATTLE
    _y_shift: int = 1
    _acute_axis: int = 6
    _obtuse_axis: int = 6
    _height: int = 15
    _min_vram_size: int = 2


class GunyolkTop(NPC):
    _sprite_id: int = SPR0153_GUNYOLK_TOP_SECTION
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 1


class GunyolkOuter(NPC):
    _sprite_id: int = SPR0154_GUNYOLK_OUTER_SECTION
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 1
    _min_vram_size: int = 1


class Crane(NPC):
    _sprite_id: int = SPR0155_FACTORY_CRANE
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 8
    _min_vram_size: int = 1


class SpinningStarPiece(NPC):
    _sprite_id: int = SPR0156_BLUE_GREEN_STAR_PIECE_SPINNING
    _show_shadow: bool = False
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 1
    _y_shift: int = 1


class SmithyHammer(NPC):
    _sprite_id: int = SPR0157_SMITHY_S_HAMMER
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 1
    _y_shift: int = 1
    _min_vram_size: int = 1


class SmithyBodyOverworld(NPC):
    _sprite_id: int = SPR0158_SMITHY_S_CHEST
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 1
    _y_shift: int = 1


class PoisonGas(NPC):
    _sprite_id: int = SPR0159_POISON_TOXIC_GAS
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 0
    _y_shift: int = 1
    _min_vram_size: int = 3


class DynaMite(NPC):
    _sprite_id: int = SPR0161_DYNA_AND_MITE
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 8
    _y_shift: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE


class FakeToad(BigToad):
    _sprite_id: int = SPR0162_SEASIDE_TOWN_FAKE_GREEN


class FakeElder(BigToad):
    _sprite_id: int = SPR0163_SEASIDE_TOWN_FAKE_ELDER_GREEN

    _eye_height: int = 10


class Elder(BigToad):
    _sprite_id: int = SPR0164_SEASIDE_TOWN_ELDER_YELLOW_GREEN


class Monstromama(BigToad):
    _sprite_id: int = SPR0165_MONSTERMAMA_GOLDEN_BROWN_RED
    _byte5_bit7: bool = False


class NimbusGuardPurple(Villager):
    _sprite_id: int = SPR0166_NIMBUS_GUARD
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 11
    _y_shift: int = 0
    _byte5_bit7: bool = False


class ManagerSmall(ShovelKnightBoss):
    _sprite_id: int = SPR0167_FACTORY_MANAGER_BLUE


class DirectorSmall(ShovelKnightBoss):
    _sprite_id: int = SPR0168_FACTORY_DIRECTOR_RED


class BoomerOverworld(NPC):
    _sprite_id: int = SPR0169_BOOMER_RED
    _acute_axis: int = 8
    _obtuse_axis: int = 8
    _height: int = 17
    _y_shift: int = 1
    _min_vram_size: int = 3

    _animations = SpriteAnimationCollection(
        chandelier_challenge=BOOMER_ALT_TAUNT, endgame_challenge=BOOMER_ALT_TAUNT
    )


class DrTopper(NPC):
    _sprite_id: int = SPR0170_DR_TOPPER_GREEN
    _acute_axis: int = 9
    _obtuse_axis: int = 9
    _height: int = 18
    _y_shift: int = 1
    _min_vram_size: int = 3


class StarPieceSparkle(NPC):
    _sprite_id: int = SPR0171_SPARKLES_FROM_STAR_PIECE
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 1
    _y_shift: int = 1


class GenoDoll(NPC):
    _sprite_id: int = SPR0172_GENO_DOLL
    _shadow_size = ShadowSize.OVAL_SMALL
    _directions = VramStore.DIR0_SWSE_NWNE
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 3
    _y_shift: int = 1


class SmelterSection(NPC):
    _sprite_id: int = SPR0173_SMELTER_BACK_SECTION
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 1
    _y_shift: int = 1


class AeroShot(NPC):
    _sprite_id: int = SPR0174_AERO_UPRIGHT
    _shadow_size = ShadowSize.OVAL_SMALL
    _acute_axis: int = 3
    _obtuse_axis: int = 3
    _height: int = 13
    _y_shift: int = 1


class GoldenChompBehind(NPC):
    _sprite_id: int = SPR0175_GOLDEN_CHOMP_BACK
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 9
    _obtuse_axis: int = 9
    _height: int = 10
    _min_vram_size: int = 2


class GrateGuySmall(NPC):
    _sprite_id: int = SPR0177_GRATE_GUY_FROM_CASINO
    _directions = VramStore.DIR0_SWSE_NWNE
    _y_shift: int = 1

    _eye_height: int = 16


class BlueStripedToad(BigToad):
    _sprite_id: int = SPR0178_MARRYMORE_INN_KEEPER_BLUE_STRIPED_HAT


class RedStripedToad(BigToad):
    _sprite_id: int = SPR0179_ROSE_TOWN_TREASURE_HOLDER


class PinkStripedToad(BigToad):
    _sprite_id: int = SPR0180_ROSE_TOWN_WOMAN_BLUE_PINK_BRAIDS


class YellowStripedToad(BigToad):
    _sprite_id: int = SPR0181_MARRYMORE_WOMAN_YELLOW


class OldBlueStripedToad(BigToad):
    _sprite_id: int = SPR0182_ROSE_TOWN_OLD_MAN_BLUE_GREY


class OldRedStripedToad(BigToad):
    _sprite_id: int = SPR0183_OLD_WOMAN_GREY_RED


class RedStripedSmallToad(SmallToad):
    _sprite_id: int = SPR0184_KID_RED_STRIPED_HAT


class PinkStripedSmallToad(SmallToad):
    _sprite_id: int = SPR0185_GAZ_PURPLE


class Cannonball(NPC):
    _sprite_id: int = SPR0188_CANNON_BALL
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 8


class Croco2(CrocoBase):
    _sprite_id: int = SPR0190_CROCO_OVERWORLD
    _alt_palette: Palette = CROCO_ALT_PALETTE


class Jinx2(Jinx):
    _sprite_id: int = SPR0191_JINX_OVERWORLD
    _alt_palette: Palette = JINX_2_ALT_PALETTE


class BigCoin(Coin):
    _sprite_id: int = SPR0192_COIN
    _height: int = 6
    _y_shift: int = 5
    _min_vram_size: int = 1
    _chest_packet: Packet = P016_BIG_COIN_BEING_COLLECTED
    _static_packet: Packet = P109_COIN_STATIC
    _falling_packet: Packet = P106_COIN_FALL


class SmallCoin(Coin):
    _sprite_id: int = SPR0193_SMALL_COIN
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 1
    _y_shift: int = 1
    _min_vram_size: int = 1
    _chest_packet: Packet = P018_SMALL_COIN_BEING_COLLECTED
    _static_packet: Packet = P110_SMALL_COIN_STATIC
    _falling_packet: Packet = P107_SMALL_COIN_FALL


class FrogCoin(Coin):
    _sprite_id: int = SPR0194_FROG_COIN
    _height: int = 6
    _y_shift: int = 5
    _min_vram_size: int = 1
    _chest_packet: Packet = P019_FROG_COIN_BEING_COLLECTED
    _static_packet: Packet = P111_FROG_COIN_STATIC
    _falling_packet: Packet = P108_FROG_COIN_FALL
    _chest_70A7_upper: int = 3


class SlotFlower(NPC):
    _sprite_id: int = SPR0195_FLOWER
    _acute_axis: int = 3
    _obtuse_axis: int = 3
    _height: int = 3
    _y_shift: int = 1


class Ring(ItemNPC):
    _sprite_id: int = SPR0196_RING
    _chest_packet: Packet = P091_RING_CHEST
    _static_packet: Packet = P093_RING_STATIC
    _falling_packet: Packet = P092_RING_FALL
    _chest_event: int = E0886_CHEST_RING_PACKET


class SparkleSideways(NPC):
    _sprite_id: int = SPR0197_SPARKLE_SIDEWAYS
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 1


class SparkleDown(NPC):
    _sprite_id: int = SPR0198_SPARKLE_DOWNWARDS
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 1


class FryingPan(ItemNPC):
    _sprite_id: int = SPR0199_FRYING_PAN_PACKET
    _chest_packet: Packet = P205_FRYING_PAN_CHEST
    _chest_event: int = E0921_CHEST_FRYING_PAN_PACKET
    _static_packet: Packet = P203_FRYING_PAN_STATIC
    _falling_packet: Packet = P204_FRYING_PAN_FALL


class Explosion(NPC):
    _sprite_id: int = SPR0200_EXPLOSION
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 1


class MokuraCloud(NPC):
    _sprite_id: int = SPR0201_MOKURA_S_CLOUD_BLUE
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 3
    _obtuse_axis: int = 3
    _height: int = 3

    _eye_height: int = 4
    _crown: int = 1


class Shoes(ItemNPC):
    _sprite_id: int = SPR0202_SHOES
    _chest_packet: Packet = P099_SHOES_CHEST
    _static_packet: Packet = P097_SHOES_STATIC
    _falling_packet: Packet = P098_SHOES_FALL
    _chest_event: int = E0888_CHEST_SHOES_PACKET


class MicroBombItem(ItemNPC):
    _sprite_id: int = SPR0205_MICROBOMB_PACKET
    _y_shift: int = 1
    _chest_packet: Packet = P114_BOMB_CHEST
    _static_packet: Packet = P112_BOMB_STATIC
    _falling_packet: Packet = P113_BOMB_FALL
    _chest_event: int = E0891_CHEST_BOMB_PACKET


class Card(ItemNPC):
    _sprite_id: int = SPR0206_CARD
    _chest_packet: Packet = P126_CARD_CHEST
    _chest_event: int = E0895_CHEST_CARD_PACKET
    _static_packet: Packet = P124_CARD_STATIC
    _falling_packet: Packet = P125_CARD_FALL
    _hover: int = True


class Brooch(ItemNPC):
    _sprite_id: int = SPR0207_BROOCH
    _chest_packet: Packet = P096_BROOCH_CHEST
    _static_packet: Packet = P094_BROOCH_STATIC
    _falling_packet: Packet = P095_BROOCH_FALL
    _chest_event: int = E0887_CHEST_BROOCH_PACKET


class Hammer(ItemNPC):
    _sprite_id: int = SPR0208_HAMMER_PACKET
    _chest_packet: Packet = P208_HAMMER_CHEST
    _chest_event: int = E0922_CHEST_HAMMER_PACKET
    _static_packet: Packet = P206_HAMMER_STATIC
    _falling_packet: Packet = P207_HAMMER_FALL


class FroggieStick(ItemNPC):
    _sprite_id: int = SPR0209_STICK_PACKET
    _chest_packet: Packet = P211_STICK_CHEST
    _chest_event: int = E0923_CHEST_STICK_PACKET
    _static_packet: Packet = P209_STICK_STATIC
    _falling_packet: Packet = P210_STICK_FALL


class ChompItem(ItemNPC):
    _sprite_id: int = SPR0210_CHOMP_PACKET
    _chest_packet: Packet = P214_CHOMP_CHEST
    _chest_event: int = E0924_CHEST_CHOMP_PACKET
    _static_packet: Packet = P212_CHOMP_STATIC
    _falling_packet: Packet = P213_CHOMP_FALL


class Fan(ItemNPC):
    _sprite_id: int = SPR0211_FAN_PACKET
    _chest_packet: Packet = P217_FAN_CHEST
    _chest_event: int = E2952_CLONE_RESERVED
    _static_packet: Packet = P215_FAN_STATIC
    _falling_packet: Packet = P216_FAN_FALL


class RedMushroom(ItemNPC):
    _sprite_id: int = SPR0212_RED_MUSHROOM_ITEM
    _chest_packet: Packet = P196_RED_MUSHROOM_CHEST
    _chest_event: int = E0918_CHEST_RED_MUSHROOM_PACKET
    _static_packet: Packet = P194_RED_MUSHROOM_STATIC
    _falling_packet: Packet = P195_RED_MUSHROOM_FALL


class Teleport(NPC):
    _sprite_id: int = SPR0213_AXEM_RED_TELEPORT
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 3


class GreenMushroom(ItemNPC):
    _sprite_id: int = SPR0214_GREEN_MUSHROOM_ITEM
    _chest_packet: Packet = P199_GREEN_MUSHROOM_CHEST
    _chest_event: int = E0919_CHEST_GREEN_MUSHROOM_PACKET
    _static_packet: Packet = P197_GREEN_MUSHROOM_STATIC
    _falling_packet: Packet = P198_GREEN_MUSHROOM_FALL


class YellowMushroom(ItemNPC):
    _sprite_id: int = SPR0215_YELLOW_MUSHROOM_ITEM
    _chest_packet: Packet = P202_YELLOW_MUSHROOM_CHEST
    _chest_event: int = E0920_CHEST_YELLOW_MUSHROOM_PACKET
    _static_packet: Packet = P200_YELLOW_MUSHROOM_STATIC
    _falling_packet: Packet = P201_YELLOW_MUSHROOM_FALL


class Crown(ItemNPC):
    _sprite_id: int = SPR0216_CROWN
    _chest_packet: Packet = P103_CROWN_CHEST
    _static_packet: Packet = P105_CROWN_STATIC
    _falling_packet: Packet = P104_CROWN_FALL
    _chest_event: int = E0890_CHEST_CROWN_PACKET


class GreenCandy(ItemNPC):
    _sprite_id: int = SPR0217_GREEN_CANDY
    _chest_packet: Packet = P175_GREEN_CANDY_CHEST
    _static_packet: Packet = P173_GREEN_CANDY_STATIC
    _falling_packet: Packet = P174_GREEN_CANDY_FALL
    _chest_event: int = E0911_CHEST_GREEN_CANDY_PACKET


class BlueCandy(ItemNPC):
    _sprite_id: int = SPR0218_BLUE_CANDY
    _chest_packet: Packet = P178_BLUE_CANDY_CHEST
    _static_packet: Packet = P176_BLUE_CANDY_STATIC
    _falling_packet: Packet = P177_BLUE_CANDY_FALL
    _chest_event: int = E0912_CHEST_BLUE_CANDY_PACKET


class RedSyrup(ItemNPC):
    _sprite_id: int = SPR0219_RED_SYRUP
    _chest_packet: Packet = P132_RED_SYRUP_CHEST
    _static_packet: Packet = P130_RED_SYRUP_STATIC
    _falling_packet: Packet = P131_RED_SYRUP_FALL
    _chest_event: int = E0897_CHEST_RED_SYRUP_PACKET


class GreenSyrup(ItemNPC):
    _sprite_id: int = SPR0220_GREEN_SYRUP
    _chest_packet: Packet = P129_GREEN_SYRUP_CHEST
    _static_packet: Packet = P127_GREEN_SYRUP_STATIC
    _falling_packet: Packet = P128_GREEN_SYRUP_FALL
    _chest_event: int = E0896_CHEST_GREEN_SYRUP_PACKET


class YellowSyrup(ItemNPC):
    _sprite_id: int = SPR0221_YELLOW_SYRUP
    _chest_packet: Packet = P138_YELLOW_SYRUP_CHEST
    _static_packet: Packet = P136_YELLOW_SYRUP_STATIC
    _falling_packet: Packet = P137_YELLOW_SYRUP_FALL
    _chest_event: int = E0899_CHEST_YELLOW_SYRUP_PACKET


class Banana(ItemNPC):
    _sprite_id: int = SPR0222_BANANA_PEEL
    _chest_packet: Packet = P102_BANANA_CHEST
    _static_packet: Packet = P100_BANANA_STATIC
    _falling_packet: Packet = P101_BANANA_FALL
    _chest_event: int = E0889_CHEST_BANANA_PEEL_PACKET


class BlueSyrup(ItemNPC):
    _sprite_id: int = SPR0223_BLUE_SYRUP
    _chest_packet: Packet = P135_BLUE_SYRUP_CHEST
    _static_packet: Packet = P133_BLUE_SYRUP_STATIC
    _falling_packet: Packet = P134_BLUE_SYRUP_FALL
    _chest_event: int = E0898_CHEST_BLUE_SYRUP_PACKET


class RedBomb(ItemNPC):
    _sprite_id: int = SPR0224_RED_BOMB
    _chest_packet: Packet = P184_RED_BOMB_CHEST
    _static_packet: Packet = P182_RED_BOMB_STATIC
    _falling_packet: Packet = P183_RED_BOMB_FALL
    _chest_event: int = E0914_CHEST_RED_BOMB_PACKET


class TinyStar(ItemNPC):
    _sprite_id: int = SPR0226_TINY_STAR
    _chest_packet: Packet = P081_STAR_PIECE_CHEST
    _static_packet: Packet = P085_STAR_PIECE_STATIC
    _falling_packet: Packet = P083_STAR_PIECE_FALL
    _chest_event: int = E0885_CHEST_STAR_PIECE_PACKET


class GreenBomb(ItemNPC):
    _sprite_id: int = SPR0233_GREEN_BOMB
    _chest_packet: Packet = P181_GREEN_BOMB_CHEST
    _static_packet: Packet = P179_GREEN_BOMB_STATIC
    _falling_packet: Packet = P180_GREEN_BOMB_FALL
    _chest_event: int = E0913_CHEST_GREEN_BOMB_PACKET


class YellowBomb(ItemNPC):
    _sprite_id: int = SPR0234_YELLOW_BOMB
    _chest_packet: Packet = P190_YELLOW_BOMB_CHEST
    _static_packet: Packet = P188_YELLOW_BOMB_STATIC
    _falling_packet: Packet = P189_YELLOW_BOMB_FALL
    _chest_event: int = E0916_CHEST_YELLOW_BOMB_PACKET


class BlueBomb(ItemNPC):
    _sprite_id: int = SPR0235_BLUE_BOMB
    _chest_packet: Packet = P187_BLUE_BOMB_CHEST
    _static_packet: Packet = P185_BLUE_BOMB_STATIC
    _falling_packet: Packet = P186_BLUE_BOMB_FALL
    _chest_event: int = E0915_CHEST_BLUE_BOMB_PACKET


class GreenJuice(ItemNPC):
    _sprite_id: int = SPR0236_GREEN_JUICE
    _chest_packet: Packet = P141_GREEN_JUICE_CHEST
    _static_packet: Packet = P139_GREEN_JUICE_STATIC
    _falling_packet: Packet = P140_GREEN_JUICE_FALL
    _chest_event: int = E0900_CHEST_GREEN_JUICE_PACKET


class Egg(ItemNPC):
    _sprite_id: int = SPR0237_EGG
    _chest_packet: Packet = P117_EGG_CHEST
    _static_packet: Packet = P115_EGG_STATIC
    _falling_packet: Packet = P116_EGG_FALLING
    _chest_event: int = E0892_CHEST_EGG_PACKET


class RedJuice(ItemNPC):
    _sprite_id: int = SPR0238_RED_JUICE
    _chest_packet: Packet = P144_RED_JUICE_CHEST
    _static_packet: Packet = P142_RED_JUICE_STATIC
    _falling_packet: Packet = P143_RED_JUICE_FALL
    _chest_event: int = E0901_CHEST_RED_JUICE_PACKET


class RDrink(ItemNPC):
    _sprite_id: int = SPR0239_BLUE_R_DRINK
    _chest_packet: Packet = P165_R_DRINK_CHEST
    _static_packet: Packet = P163_R_DRINK_STATIC
    _falling_packet: Packet = P164_R_DRINK_FALL
    _chest_event: int = E0908_CHEST_R_DRINK_PACKET


class DDrink(ItemNPC):
    _sprite_id: int = SPR0240_YELLOW_D_DRINK
    _chest_packet: Packet = P148_D_DRINK_CHEST
    _static_packet: Packet = P150_D_DRINK_STATIC
    _falling_packet: Packet = P149_D_DRINK_FALL
    _chest_event: int = E0903_CHEST_D_DRINK_PACKET


class PDrink(ItemNPC):
    _sprite_id: int = SPR0241_GREEN_P_DRINK
    _chest_packet: Packet = P147_P_DRINK_CHEST
    _static_packet: Packet = P145_P_DRINK_STATIC
    _falling_packet: Packet = P146_P_DRINK_FALL
    _chest_event: int = E0902_CHEST_P_DRINK_PACKET


class FrogDrink(ItemNPC):
    _sprite_id: int = SPR0244_GREEN_FROG_DRINK
    _chest_packet: Packet = P157_FROG_DRINK_CHEST
    _static_packet: Packet = P159_FROG_DRINK_STATIC
    _falling_packet: Packet = P158_FROG_DRINK_FALL
    _chest_event: int = E0906_CHEST_FROG_DRINK_PACKET


class YellowMusicDrink(ItemNPC):
    _sprite_id: int = SPR0245_YELLOW_MUSIC_DRINK
    _chest_packet: Packet = P151_YELLOW_MUSIC_DRINK_CHEST
    _static_packet: Packet = P153_YELLOW_MUSIC_DRINK_STATIC
    _falling_packet: Packet = P152_YELLOW_MUSIC_DRINK_FALL
    _chest_event: int = E0904_CHEST_YELLOW_M_DRINK_PACKET


class BlueMusicDrink(ItemNPC):
    _sprite_id: int = SPR0246_BLUE_MUSIC_DRINK
    _chest_packet: Packet = P154_BLUE_MUSIC_DRINK_CHEST
    _static_packet: Packet = P156_BLUE_MUSIC_DRINK_STATIC
    _falling_packet: Packet = P155_BLUE_MUSIC_DRINK_FALL
    _chest_event: int = E0905_CHEST_BLUE_M_DRINK_PACKET


class RedMusicDrink(ItemNPC):
    _sprite_id: int = SPR0247_RED_MUSIC_DRINK
    _chest_packet: Packet = P160_RED_MUSIC_DRINK_CHEST
    _static_packet: Packet = P162_RED_MUSIC_DRINK_STATIC
    _falling_packet: Packet = P161_RED_MUSIC_DRINK_FALL
    _chest_event: int = E0907_CHEST_RED_M_DRINK_PACKET


class StarDrink(ItemNPC):
    _sprite_id: int = SPR0248_RED_STAR_DRINK
    _chest_packet: Packet = P171_STAR_DRINK_CHEST
    _static_packet: Packet = P169_STAR_DRINK_STATIC
    _falling_packet: Packet = P170_STAR_DRINK_FALL
    _chest_event: int = E0910_CHEST_STAR_DRINK_PACKET


class RedShell(ItemNPC):
    _sprite_id: int = SPR0249_RED_SHELL
    _chest_packet: Packet = P220_RED_SHELL_CHEST
    _static_packet: Packet = P218_RED_SHELL_STATIC
    _falling_packet: Packet = P219_RED_SHELL_FALL
    _chest_event: int = E0926_CHEST_RED_SHELL_PACKET
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 5


class GreenShell(ItemNPC):
    _sprite_id: int = SPR0250_GREEN_SHELL
    _chest_packet: Packet = P223_GREEN_SHELL_CHEST
    _static_packet: Packet = P221_GREEN_SHELL_STATIC
    _falling_packet: Packet = P222_GREEN_SHELL_FALL
    _chest_event: int = E0927_CHEST_GREEN_SHELL_PACKET
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 5


class Parasol(ItemNPC):
    _sprite_id: int = SPR0251_PARASOL_PACKET
    _chest_packet: Packet = P226_PARASOL_CHEST
    _chest_event: int = E0928_CHEST_CHEST_PARASOL_PACKET
    _static_packet: Packet = P224_PARASOL_STATIC
    _falling_packet: Packet = P225_PARASOL_FALL


class Feather(ItemNPC):
    _sprite_id: int = SPR0252_FEATHER
    _chest_packet: Packet = P080_FEATHER_CHEST
    _chest_event: int = E0884_CHEST_FEATHER_PACKET
    _static_packet: Packet = P084_FEATHER_STATIC
    _falling_packet: Packet = P082_FEATHER_FALL


class Berry(ItemNPC):
    _sprite_id: int = SPR0253_BERRY
    _y_shift: int = 1
    _chest_packet: Packet = P123_BERRY_CHEST
    _chest_event: int = E0894_CHEST_BERRY_PACKET
    _static_packet: Packet = P121_BERRY_STATIC
    _falling_packet: Packet = P122_BERRY_FALL


class Cookie(ItemNPC):
    _sprite_id: int = SPR0254_YOSHI_COOKIE
    _chest_packet: Packet = P120_COOKIE_CHEST
    _chest_event: int = E0893_CHEST_COOKIE_PACKET
    _static_packet: Packet = P118_COOKIE_STATIC
    _falling_packet: Packet = P119_COOKIE_FALL


class Beetle(ItemNPC):
    _sprite_id: int = SPR0255_BEETLE
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _chest_packet: Packet = P193_BEETLE_CHEST
    _chest_event: int = E0917_CHEST_BEETLE_PACKET
    _static_packet: Packet = P191_BEETLE_STATIC
    _falling_packet: Packet = P192_BEETLE_FALL


class Terrapin(NPC):
    _sprite_id: int = SPR0256_TERRAPIN
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 11
    _y_shift: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE

    _animations = SpriteAnimationCollection(
        bandits_way_distracted=JAGGER_LOOK,
        mines_punch=JAGGER_PUNCH,
        chapel_laugh=JAGGER_LOOK,
        ship_beckon=JAGGER_TAUNT,
        dojo_challenge=JAGGER_PUNCH,
        statue_intro=JAGGER_LOOK,
        statue_peck=JAGGER_TAUNT,
        statue_flustered=JAGGER_RECOIL,
        keep_challenge=JAGGER_PUNCH,
        keep_summon=JAGGER_PUNCH,
        chandelier_challenge=JAGGER_PUNCH,
        endgame_challenge=JAGGER_PUNCH,
    )


class Spikey(NPC):
    _sprite_id: int = SPR0257_SPIKEY
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 9
    _y_shift: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE


class SkyTroopa(NPC):
    _sprite_id: int = SPR0258_SKY_TROOPA
    _acute_axis: int = 6
    _obtuse_axis: int = 6
    _height: int = 10
    _y_shift: int = 2
    _directions = VramStore.DIR0_SWSE_NWNE


class MadMallet(HammerNPC):
    _sprite_id: int = SPR0259_MAD_MALLET


class Shaman(NPC):
    _sprite_id: int = SPR0260_SHAMAN
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 10
    _y_shift: int = -1
    _directions = VramStore.DIR0_SWSE_NWNE


class Crook(NPC):
    _sprite_id: int = SPR0261_CROOK
    _acute_axis: int = 6
    _obtuse_axis: int = 6
    _height: int = 7
    _y_shift: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE
    _min_vram_size: int = 1

    _animations = SpriteAnimationCollection(
        tower_bullet=CROOK_SCRATCH,
        kitchen_prep=CROOK_SCRATCH,
        factory_pierce=CROOK_SCRATCH,
    )


class Goomba(NPC):
    _sprite_id: int = SPR0262_GOOMBA
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 8
    _y_shift: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE


class PiranhaPlant(NPC):
    _sprite_id: int = SPR0263_PIRANHA_PLANT
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 11
    _y_shift: int = 1

    _animations = SpriteAnimationCollection(
        recoil=PIRANHA_RECOIL,
        bandits_way_distracted=PIRANHA_TAUNT,
        mines_punch=PIRANHA_BITE,
        chapel_laugh=PIRANHA_TAUNT,
        ship_beckon=PIRANHA_TAUNT,
        dojo_challenge=PIRANHA_BITE,
        statue_intro=PIRANHA_BITE,
        statue_peck=PIRANHA_BITE,
        statue_flustered=PIRANHA_RECOIL,
        keep_challenge=PIRANHA_BITE,
        keep_summon=PIRANHA_BITE,
        chandelier_challenge=PIRANHA_BITE,
        endgame_challenge=PIRANHA_BITE,
    )
    _eye_height: int = 14


class Amanita(NPC):
    _sprite_id: int = SPR0264_AMANITA
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 9
    _y_shift: int = 1


class Goby(NPC):
    _sprite_id: int = SPR0265_GOBY
    _acute_axis: int = 6
    _obtuse_axis: int = 6
    _height: int = 9
    _y_shift: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE


class Bloober(NPC):
    _sprite_id: int = SPR0266_BLOOBER
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 11
    _y_shift: int = -2

    _animations = SpriteAnimationCollection(
        tower_bullet=SQUID_HIT,
        recoil=SQUID_RECOIL,
        mines_punch=SQUID_HIT,
        dojo_challenge=SQUID_HIT,
        statue_peck=SQUID_HIT_FAST,
        statue_flustered=SQUID_RECOIL,
        keep_challenge=SQUID_HIT,
        keep_summon=SQUID_HIT,
        chandelier_challenge=SQUID_HIT,
        endgame_challenge=SQUID_HIT,
    )
    _eye_height: int = 10


class BandanaRed(NPC):
    _sprite_id: int = SPR0267_BANDANA_RED
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 10
    _y_shift: int = 2
    _directions = VramStore.DIR0_SWSE_NWNE
    _min_vram_size: int = 1

    _animations = SpriteAnimationCollection(
        tower_bullet=BANDANA_TAUNT,
        kitchen_prep=BANDANA_ATTACK,
        factory_pierce=BANDANA_ATTACK,
    )


class Lakitu(NPC):
    _sprite_id: int = SPR0268_LAKITU
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 11
    _y_shift: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE


class Birdy(ValentinaBird):
    _sprite_id: int = SPR0269_BIRDY


class Pinwheel(NPC):
    _sprite_id: int = SPR0270_PINWHEEL
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 11
    _y_shift: int = 4


class RatFunk(NPC):
    _sprite_id: int = SPR0271_RAT_FUNK
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 9
    _directions = VramStore.DIR0_SWSE_NWNE


class K9(NPC):
    _sprite_id: int = SPR0272_K
    _acute_axis: int = 6
    _obtuse_axis: int = 6
    _height: int = 11
    _min_vram_size: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE


class Magmite(NPC):
    _sprite_id: int = SPR0273_MAGMITE
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 7
    _min_vram_size: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE


class BigBoo(NPC):
    _sprite_id: int = SPR0274_THE_BIG_BOO
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 10
    _y_shift: int = 3
    _directions = VramStore.DIR0_SWSE_NWNE


class DryBones(NPC):
    _sprite_id: int = SPR0275_DRY_BONES
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _y_shift: int = 1
    _min_vram_size: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE


class Greaper(NPC):
    _sprite_id: int = SPR0276_GREAPER
    _acute_axis: int = 8
    _obtuse_axis: int = 8
    _height: int = 11
    _y_shift: int = 3
    _min_vram_size: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE


class RedFireball(Fireball):
    _sprite_id: int = SPR0277_SPARKY


class Chomp(NPC):
    _sprite_id: int = SPR0278_CHOMP
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 9
    _obtuse_axis: int = 9
    _height: int = 9
    _min_vram_size: int = 2


class PandoriteLarge(MimicLarge):
    _sprite_id: int = SPR0279_PANDORITE

    _animations = SpriteAnimationCollection(
        mines_punch=PANDORITE_ATTACK,
        statue_intro=MIMIC_SHAKE,
        statue_peck=PANDORITE_SHORT,
        statue_flustered=MIMIC_RECOIL,
        chandelier_challenge=PANDORITE_ATTACK,
        endgame_challenge=PANDORITE_ATTACK,
    )


class BobOmb(NPC):
    _sprite_id: int = SPR0281_BOB_OMB
    _y_shift: int = 1
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 10
    _min_vram_size: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE

    _animations = SpriteAnimationCollection(
        tower_bullet=BOMB_TICK, kitchen_prep=BOMB_TICK, factory_pierce=BOMB_TICK
    )


class Spookum(NPC):
    _sprite_id: int = SPR0282_SPOOKUM
    _y_shift: int = 2
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 10
    _directions = VramStore.DIR0_SWSE_NWNE


class HammerBroLarge(NPC):
    _sprite_id: int = SPR0283_HAMMER_BRO
    _y_shift: int = 1
    _acute_axis: int = 8
    _obtuse_axis: int = 7
    _height: int = 19
    _min_vram_size: int = 3

    _animations = SpriteAnimationCollection(
        mines_punch=HAMMER_BRO_BOP,
        statue_intro=HAMMER_BRO_TAUNT,
        statue_peck=HAMMER_BRO_BOP_FAST,
        statue_flustered=HAMMER_BRO_RECOIL,
        chandelier_challenge=HAMMER_BRO_TAUNT,
        endgame_challenge=HAMMER_BRO_TAUNT,
    )


class Buzzer(NPC):
    _sprite_id: int = SPR0284_BUZZER
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 11
    _y_shift: int = 2
    _min_vram_size: int = 1


class Ameboid(NPC):
    _sprite_id: int = SPR0285_AMEBOID
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 8
    _y_shift: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE


class Gecko(NPC):
    _sprite_id: int = SPR0286_GECKO
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 5
    _directions = VramStore.DIR0_SWSE_NWNE
    _min_vram_size: int = 1


class Wiggler(NPC):
    _sprite_id: int = SPR0287_WIGGLER
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _acute_axis: int = 4
    _obtuse_axis: int = 8
    _height: int = 13
    _y_shift: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE
    _min_vram_size: int = 2


class Jawful(NPC):
    _sprite_id: int = SPR0291_JAWFUL
    _shadow_size = ShadowSize.OVAL_BIG
    _y_shift: int = 1
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 13
    _min_vram_size: int = 3


class Guerrilla(NPC):
    _sprite_id: int = SPR0294_GUERRILLA
    _shadow_size = ShadowSize.OVAL_BIG
    _y_shift: int = -1
    _acute_axis: int = 13
    _obtuse_axis: int = 13
    _height: int = 19
    _min_vram_size: int = 5


class Shogun(NPC):
    _sprite_id: int = SPR0298_SHOGUN
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 10
    _min_vram_size: int = 3


class HeavyTropa(NPC):
    _sprite_id: int = SPR0300_HEAVY_TROOPA
    _shadow_size = ShadowSize.OVAL_BIG
    _acute_axis: int = 10
    _obtuse_axis: int = 13
    _height: int = 15
    _min_vram_size: int = 2


class ClerkLarge(ShovelKnightBossLarge):
    _sprite_id: int = SPR0702_CLERK_SUB


class BoomerLarge(NPC):
    _sprite_id: int = SPR0701_BOOMER_SUB
    _shadow_size = ShadowSize.OVAL_BIG
    _y_shift: int = 2
    _acute_axis: int = 9
    _obtuse_axis: int = 9
    _height: int = 22
    _min_vram_size: int = 3

    _animations = SpriteAnimationCollection(
        # mines_punch=boomer_hit, # vram issues
        statue_intro=BOOMER_TAUNT,
        # statue_peck=boomer_hit, # vram issues
        statue_flustered=BOOMER_RECOIL,
        chandelier_challenge=BOOMER_TAUNT,
        endgame_challenge=BOOMER_TAUNT,
    )


class DodoLarge(NPC):
    _sprite_id: int = SPR0695_DODO_SUB
    _shadow_size = ShadowSize.OVAL_BIG
    _acute_axis: int = 9
    _obtuse_axis: int = 9
    _height: int = 14
    _min_vram_size: int = 3
    _directions = VramStore.DIR0_SWSE_NWNE

    _animations = SpriteAnimationCollection(
        mines_punch=DODO_PECK,
        statue_intro=DODO_TAUNT,
        statue_flustered=DODO_TAUNT,
        statue_peck=DODO_PECK,
        chandelier_challenge=DODO_TAUNT,
        endgame_challenge=DODO_TAUNT,
    )


class TerraCotta(NPC):
    _sprite_id: int = SPR0320_TERRA_COTTA
    _directions = VramStore.DIR0_SWSE_NWNE
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 11
    _y_shift: int = 1


class Spikester(NPC):
    _sprite_id: int = SPR0321_SPIKESTER
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 9
    _y_shift: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE


class Malakoopa(NPC):
    _sprite_id: int = SPR0322_MALAKOOPA
    _acute_axis: int = 6
    _obtuse_axis: int = 6
    _height: int = 10
    _y_shift: int = 2
    _directions = VramStore.DIR0_SWSE_NWNE


class Pounder(HammerNPC):
    _sprite_id: int = SPR0323_POUNDER


class Poundette(HammerNPC):
    _sprite_id: int = SPR0324_POUNDETTE


class Sackit(NPC):
    _sprite_id: int = SPR0325_SACKIT
    _acute_axis: int = 6
    _obtuse_axis: int = 6
    _height: int = 7
    _y_shift: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE
    _min_vram_size: int = 1


class GuGoomba(NPC):
    _sprite_id: int = SPR0326_GU_GOOMBA
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 8
    _y_shift: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE


class Chewy(NPC):
    _sprite_id: int = SPR0327_CHEWY
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 11
    _y_shift: int = 1


class BlueFireball(Fireball):
    _sprite_id: int = SPR0328_FIREBALL


class MrKipper(NPC):
    _sprite_id: int = SPR0329_MR_KIPPER
    _acute_axis: int = 6
    _obtuse_axis: int = 6
    _height: int = 9
    _y_shift: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE


class FactoryChief(NPC):
    _sprite_id: int = SPR0330_FACTORY_CHIEF
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _y_shift: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE

    _eye_height: int = 16
    _animations = SpriteAnimationCollection(
        recoil=NINJA_RECOIL,
        mines_punch=NINJA_HIT,
        chapel_laugh=NINJA_TAUNT,
        ship_beckon=NINJA_TAUNT,
        dojo_challenge=NINJA_HIT,
        statue_intro=NINJA_TAUNT,
        statue_peck=NINJA_HIT_FAST,
        statue_flustered=NINJA_RECOIL,
        keep_challenge=NINJA_HIT,
        keep_summon=NINJA_TAUNT,
        chandelier_challenge=NINJA_HIT,
        endgame_challenge=NINJA_HIT,
    )


class BandanaBlue(NPC):
    _sprite_id: int = SPR0331_BANDANA_BLUE
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 10
    _y_shift: int = 2
    _directions = VramStore.DIR0_SWSE_NWNE
    _min_vram_size: int = 1

    _animations = SpriteAnimationCollection(
        tower_bullet=BANDANA_TAUNT,
        kitchen_prep=BANDANA_ATTACK,
        factory_pierce=BANDANA_ATTACK,
    )


class ManagerLarge(ShovelKnightBossLarge):
    _sprite_id: int = SPR0703_MANAGER_SUB


class Bluebird(ValentinaBird):
    _sprite_id: int = SPR0333_BLUEBIRD


class AlleyRat(NPC):
    _sprite_id: int = SPR0335_ALLEY_RAT
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 9
    _directions = VramStore.DIR0_SWSE_NWNE


class Chow(NPC):
    _sprite_id: int = SPR0336_CHOW
    _acute_axis: int = 6
    _obtuse_axis: int = 6
    _height: int = 11
    _min_vram_size: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE


class Magmus(NPC):
    _sprite_id: int = SPR0337_MAGMUS
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 7
    _min_vram_size: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE


class LilBoo(NPC):
    _sprite_id: int = SPR0338_LI_XX_L_BOO
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 10
    _y_shift: int = 3
    _directions = VramStore.DIR0_SWSE_NWNE


class Vomer(NPC):
    _sprite_id: int = SPR0339_VOMER
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _y_shift: int = 1
    _min_vram_size: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE


class GlumReaper(NPC):
    _sprite_id: int = SPR0340_GLUM_REAPER
    _acute_axis: int = 8
    _obtuse_axis: int = 8
    _height: int = 11
    _y_shift: int = 3
    _min_vram_size: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE


class HidonLarge(MimicLarge):
    _sprite_id: int = SPR0343_HIDON
    _animations = SpriteAnimationCollection(
        mines_punch=HIDON_ATTACK,
        statue_flustered=MIMIC_RECOIL,
        statue_peck=HIDON_ATTACK_FAST,
        statue_intro=MIMIC_SHAKE,
        chandelier_challenge=HIDON_ATTACK,
        endgame_challenge=HIDON_ATTACK,
    )


class SlingShy(NPC):
    _sprite_id: int = SPR0344_SLING_SHY
    _y_shift: int = 1
    _height: int = 7
    _directions = VramStore.DIR0_SWSE_NWNE


class RobOmb(NPC):
    _sprite_id: int = SPR0345_ROB_OMB
    _y_shift: int = 1
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 10
    _min_vram_size: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE


class ShyGuy(NPC):
    _sprite_id: int = SPR0346_SHY_GUY
    _y_shift: int = 1
    _height: int = 7
    _directions = VramStore.DIR0_SWSE_NWNE

    _animations = SpriteAnimationCollection(
        tower_bullet=SHYGUY_HIT, kitchen_prep=SHYGUY_TAUNT, factory_pierce=SHYGUY_HIT
    )


class Ninja(NPC):
    _sprite_id: int = SPR0347_NINJA
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 11
    _y_shift: int = 2
    _directions = VramStore.DIR0_SWSE_NWNE


class Stinger(NPC):
    _sprite_id: int = SPR0348_STINGER
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 11
    _y_shift: int = 2
    _min_vram_size: int = 1


class Geckit(NPC):
    _sprite_id: int = SPR0350_GECKIT
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 5
    _directions = VramStore.DIR0_SWSE_NWNE
    _min_vram_size: int = 1


class Jabit(NPC):
    _sprite_id: int = SPR0351_JABIT
    _y_shift: int = 2
    _height: int = 11
    _directions = VramStore.DIR0_SWSE_NWNE


class MagikoopaLarge(NPC):
    _sprite_id: int = SPR0353_MERLIN
    _shadow_size = ShadowSize.OVAL_BIG
    _y_shift: int = 1
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 13
    _min_vram_size: int = 2

    _animations = SpriteAnimationCollection(
        mines_punch=BIG_MAGIKOOPA_HIT,
        statue_intro=BIG_MAGIKOOPA_TAUNT,
        statue_peck=BIG_MAGIKOOPA_HIT_FAST,
        statue_flustered=BIG_MAGIKOOPA_RECOIL,
        chandelier_challenge=BIG_MAGIKOOPA_TAUNT,
        endgame_challenge=BIG_MAGIKOOPA_TAUNT,
    )


class Apprentice(NPC):
    _sprite_id: int = SPR0384_APPRENTICE
    _y_shift: int = 2
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 9
    _directions = VramStore.DIR0_SWSE_NWNE
    _byte5_bit6: bool = True
    _byte5_bit7: bool = True
    _byte6_bit2: bool = True

    _animations = SpriteAnimationCollection(
        tower_bullet=SNIFIT_SHOOT,
        kitchen_prep=SNIFIT_TAUNT,
        factory_pierce=SNIFIT_TAUNT,
    )


class GenoRedemption(NPC):
    _sprite_id: int = SPR0388_GENO_REDEMPTION
    _y_shift: int = 1
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 1
    _min_vram_size: int = 1


class BoxBoyLarge(MimicLarge):
    _sprite_id: int = SPR0390_BOX_BOY

    _animations = SpriteAnimationCollection(
        mines_punch=BOXBOY_ATTACK,
        statue_intro=MIMIC_SHAKE,
        statue_peck=BOXBOY_SHORT,
        statue_flustered=MIMIC_RECOIL,
        chandelier_challenge=BOXBOY_ATTACK,
        endgame_challenge=BOXBOY_ATTACK,
    )


class Oerlikon(NPC):
    _sprite_id: int = SPR0394_OERLIKON
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 9
    _y_shift: int = 1
    _directions = VramStore.DIR0_SWSE_NWNE


class ChesterLarge(MimicLarge):
    _sprite_id: int = SPR0395_CHESTER

    _animations = SpriteAnimationCollection(
        mines_punch=CHESTER_ATTACK,
        statue_intro=MIMIC_SHAKE,
        statue_peck=CHESTER_ATTACK_FAST,
        statue_flustered=MIMIC_RECOIL,
        chandelier_challenge=CHESTER_ATTACK,
        endgame_challenge=CHESTER_ATTACK,
    )


class Torte(NPC):
    _sprite_id: int = SPR0398_TORTE
    _acute_axis: int = 2
    _obtuse_axis: int = 2
    _height: int = 11
    _directions = VramStore.DIR0_SWSE_NWNE

    _animations = SpriteAnimationCollection(
        tower_bullet=TORTE_TAUNT,
        kitchen_prep=TORTE_TAUNT,
        factory_pierce=TORTE_TAUNT_FAST,
    )


class ShyAway(NPC):
    _sprite_id: int = SPR0399_SHY_AWAY
    _acute_axis: int = 6
    _obtuse_axis: int = 6
    _height: int = 10
    _directions = VramStore.DIR0_SWSE_NWNE
    _min_vram_size: int = 1


class MachineShyster(NPC):
    _sprite_id: int = SPR0401_MACHINE_MADE_SHYSTER
    _y_shift: int = 1
    _height: int = 11
    _directions = VramStore.DIR0_SWSE_NWNE
    _shadow_size = ShadowSize.OVAL_SMALL


class MachineDrillBit(NPC):
    _sprite_id: int = SPR0402_MACHINE_MADE_DRILL_BIT
    _y_shift: int = 2
    _height: int = 11
    _directions = VramStore.DIR0_SWSE_NWNE
    _shadow_size = ShadowSize.OVAL_SMALL


class MarioClone(CloneNPC):
    _sprite_id: int = SPR0409_MARIO_CLONE
    _y_shift: int = 1
    _animations = SpriteAnimationCollection(
        kitchen_prep=MARIOCLONE_HIT_FAST, factory_pierce=MARIOCLONE_HIT_FAST
    )


class PeachClone(CloneNPC):
    _sprite_id: int = SPR0410_TOADSTOOL
    _y_shift: int = 1

    _animations = SpriteAnimationCollection(
        tower_bullet=PEACHCLONE_MAD,
        kitchen_prep=PEACHCLONE_MAD,
        factory_pierce=PEACHCLONE_MAD,
    )


class BowserClone(CloneNPC):
    _sprite_id: int = SPR0411_BOWSER_CLONE
    _shadow_size = ShadowSize.OVAL_BIG
    _acute_axis: int = 6
    _obtuse_axis: int = 6
    _height: int = 14
    _y_shift: int = -2

    _animations = SpriteAnimationCollection(
        tower_bullet=BOWSERCLONE_LAUGH,
        kitchen_prep=BOWSERCLONE_MAD,
        factory_pierce=BOWSERCLONE_MAD,
    )


class GenoClone(CloneNPC):
    _sprite_id: int = SPR0412_GENO_CLONE
    _y_shift: int = 1
    _acute_axis: int = 4
    _obtuse_axis: int = 4

    _animations = SpriteAnimationCollection(
        tower_bullet=GENOCLONE_LAUGH,
        kitchen_prep=GENOCLONE_MAD,
        factory_pierce=GENOCLONE_MAD,
    )


class MallowClone(CloneNPC):
    _sprite_id: int = SPR0413_MALLOW_CLONE
    _height: int = 8

    _animations = SpriteAnimationCollection(
        tower_bullet=MALLOWCLONE_LAUGH,
        kitchen_prep=MALLOWCLONE_MAD,
        factory_pierce=MALLOWCLONE_MAD,
    )


class Shyster(NPC):
    _sprite_id: int = SPR0414_SHYSTER
    _y_shift: int = 1
    _height: int = 11
    _directions = VramStore.DIR0_SWSE_NWNE
    _shadow_size = ShadowSize.OVAL_SMALL

    _animations = SpriteAnimationCollection(
        tower_bullet=SHYSTER_TAUNT,
        kitchen_prep=SHYSTER_TAUNT,
        factory_pierce=SHYSTER_FAST,
    )


class HanginShy(NPC):
    _sprite_id: int = SPR0417_HANGIN_XX_SHY
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 1
    _min_vram_size: int = 1


class MachineMack(NPC):
    _sprite_id: int = SPR0419_MACHINE_MADE_MACK
    _shadow_size = ShadowSize.OVAL_BIG
    _y_shift: int = 1
    _acute_axis: int = 13
    _obtuse_axis: int = 13
    _height: int = 23
    _min_vram_size: int = 3


class MachineAxemPink(NPC):
    _sprite_id: int = SPR0422_MACHINE_MADE_AXEM_PINK
    _acute_axis: int = 5
    _obtuse_axis: int = 5

    _animations = SpriteAnimationCollection(
        tower_bullet=AXEM_PINK_HIT,
        kitchen_prep=AXEM_PINK_HIT,
        factory_pierce=AXEM_PINK_HIT,
    )


class MachineAxemBlack(NPC):
    _sprite_id: int = SPR0423_MACHINE_MADE_AXEM_BLACK
    _acute_axis: int = 5
    _obtuse_axis: int = 5

    _animations = SpriteAnimationCollection(
        tower_bullet=AXEM_BLACK_HIT,
        kitchen_prep=AXEM_BLACK_HIT,
        factory_pierce=AXEM_BLACK_HIT,
    )


class MachineAxemRed(NPC):
    _sprite_id: int = SPR0424_MACHINE_MADE_AXEM_RED
    _acute_axis: int = 5
    _obtuse_axis: int = 5

    _animations = SpriteAnimationCollection(
        tower_bullet=AXEM_RED_HIT,
        kitchen_prep=AXEM_RED_HIT,
        factory_pierce=AXEM_RED_HIT,
    )


class MachineAxemYellow(NPC):
    _sprite_id: int = SPR0425_MACHINE_MADE_AXEM_YELLOW
    _acute_axis: int = 5
    _obtuse_axis: int = 5

    _animations = SpriteAnimationCollection(
        tower_bullet=AXEM_YELLOW_HIT_FAST, kitchen_prep=AXEM_YELLOW_HIT
    )


class MachineAxemGreen(NPC):
    _sprite_id: int = SPR0426_MACHINE_MADE_AXEM_GREEN
    _acute_axis: int = 5
    _obtuse_axis: int = 5

    _animations = SpriteAnimationCollection(
        tower_bullet=AXEM_GREEN_HIT,
        kitchen_prep=AXEM_GREEN_HIT,
        factory_pierce=AXEM_GREEN_HIT_FAST,
    )


class Starslap(NPC):
    _sprite_id: int = SPR0432_STARSLAP
    _y_shift: int = -4
    _acute_axis: int = 6
    _obtuse_axis: int = 6
    _height: int = 6


class Mukumuku(NPC):
    _sprite_id: int = SPR0433_MUKUMUKU
    _y_shift: int = 3
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 9


class Zeostar(NPC):
    _sprite_id: int = SPR0434_ZEOSTAR
    _y_shift: int = -4
    _acute_axis: int = 6
    _obtuse_axis: int = 6
    _height: int = 6


class Microbomb(NPC):
    _sprite_id: int = SPR0440_MICROBOMB
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 2
    _obtuse_axis: int = 2
    _height: int = 3

    _animations = SpriteAnimationCollection(
        tower_bullet=BOMB_TICK, kitchen_prep=BOMB_TICK, factory_pierce=BOMB_TICK
    )


class Helio(NPC):
    _sprite_id: int = SPR0445_HELIO
    _shadow_size = ShadowSize.OVAL_SMALL
    _show_shadow: bool = False


class BundtLarge(NPC):
    _sprite_id: int = SPR0450_BUNDT
    _min_vram_size: int = 3
    _shadow_size = ShadowSize.OVAL_BIG
    _y_shift: int = 1
    _acute_axis: int = 13
    _obtuse_axis: int = 13
    _height: int = 23

    _animations = SpriteAnimationCollection(
        mines_punch=BUNDT_TAUNT,
        statue_intro=BUNDT_TAUNT,
        statue_flustered=BUNDT_RECOIL,
        chandelier_challenge=BUNDT_TAUNT,
        endgame_challenge=BUNDT_TAUNT,
    )


class Smilax(NPC):
    _sprite_id: int = SPR0458_SMILAX
    _shadow_size = ShadowSize.OVAL_SMALL
    _show_shadow: bool = False
    _y_shift: int = 1
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 7


class Thrax(NPC):
    _sprite_id: int = SPR0459_THRAX
    _shadow_size = ShadowSize.OVAL_SMALL
    _show_shadow: bool = False
    _y_shift: int = 1
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 7


class Megasmilax(NPC):
    _sprite_id: int = SPR0460_MEGASMILAX
    _min_vram_size: int = 3
    _shadow_size = ShadowSize.OVAL_BIG
    _y_shift: int = 1
    _acute_axis: int = 11
    _obtuse_axis: int = 11
    _height: int = 13

    _animations = SpriteAnimationCollection(
        mines_punch=MEGASMILAX_BITE,
        statue_flustered=MEGASMILAX_RECOIL,
        statue_peck=MEGASMILAX_BITE,
        chandelier_challenge=MEGASMILAX_TAUNT,
        endgame_challenge=MEGASMILAX_TAUNT,
    )


class BirdettaLarge(NPC):
    _sprite_id: int = SPR0461_BIRDETTA
    _shadow_size = ShadowSize.OVAL_BIG
    _min_vram_size: int = 4
    _y_shift: int = 1
    _acute_axis: int = 9
    _obtuse_axis: int = 11
    _height: int = 23

    _animations = SpriteAnimationCollection(
        mines_punch=BIRDETTA_ATTACK,
        statue_flustered=BIRDETTA_RECOIL,
        statue_peck=BIRDETTA_ATTACK_FAST,
        statue_intro=BIRDETTA_TAUNT,
        chandelier_challenge=BIRDETTA_ATTACK,
        endgame_challenge=BIRDETTA_ATTACK,
    )


class Eggbert(NPC):
    _sprite_id: int = SPR0462_EGGBERT
    _shadow_size = ShadowSize.OVAL_SMALL
    _show_shadow: bool = False
    _acute_axis: int = 2
    _obtuse_axis: int = 2
    _height: int = 5

    _animations = SpriteAnimationCollection(
        tower_bullet=EGGBERT_EXPAND,
        kitchen_prep=EGGBERT_EXPAND,
        factory_pierce=EGGBERT_EXPAND,
    )


class AxemYellow(NPC):
    _sprite_id: int = SPR0463_AXEM_YELLOW
    _acute_axis: int = 5
    _obtuse_axis: int = 5

    _animations = SpriteAnimationCollection(
        tower_bullet=AXEM_YELLOW_HIT_FAST, kitchen_prep=AXEM_YELLOW_HIT
    )


class PunchinelloLarge(NPC):
    _sprite_id: int = SPR0464_PUNCHINELLO
    _shadow_size = ShadowSize.OVAL_SMALL
    _show_shadow: bool = False
    _y_shift: int = 1
    _acute_axis: int = 11
    _obtuse_axis: int = 8
    _height: int = 19
    _min_vram_size: int = 2

    _animations = SpriteAnimationCollection(
        mines_punch=PUNCHINELLO_HIT,
        statue_intro=PUNCHINELLO_JUMP,
        statue_peck=PUNCHINELLO_HIT_FAST,
        statue_flustered=PUNCHINELLO_RECOIL,
        chandelier_challenge=PUNCHINELLO_TAUNT,
        endgame_challenge=PUNCHINELLO_TAUNT,
    )


class AxemRed(NPC):
    _sprite_id: int = SPR0466_AXEM_RED
    _acute_axis: int = 5
    _obtuse_axis: int = 5

    _eye_height: int = 15
    _animations = SpriteAnimationCollection(
        bandits_way_distracted=AXEM_RED_TAUNT,
        mines_punch=AXEM_RED_HIT,
        ship_beckon=AXEM_RED_HIT,
        dojo_challenge=AXEM_RED_TAUNT,
        statue_intro=AXEM_RED_TAUNT,
        statue_peck=AXEM_RED_HIT_FAST,
        statue_flustered=AXEM_RED_RECOIL,
        keep_challenge=AXEM_RED_TAUNT,
        keep_summon=AXEM_RED_HIT,
        chandelier_challenge=AXEM_RED_TAUNT,
        endgame_challenge=AXEM_RED_TAUNT,
    )


class AxemGreen(NPC):
    _sprite_id: int = SPR0467_AXEM_GREEN
    _acute_axis: int = 5
    _obtuse_axis: int = 5

    _animations = SpriteAnimationCollection(
        tower_bullet=AXEM_GREEN_HIT,
        kitchen_prep=AXEM_GREEN_HIT,
        factory_pierce=AXEM_GREEN_HIT_FAST,
    )


class CloakerLarge(NPC):
    _sprite_id: int = SPR0477_CLOAKER_ST_TIME
    _shadow_size = ShadowSize.OVAL_BIG
    _y_shift: int = 1
    _acute_axis: int = 8
    _obtuse_axis: int = 8
    _height: int = 17
    _min_vram_size: int = 3

    _animations = SpriteAnimationCollection(
        # mines_punch=cloaker_hit, # breaks vram
        # statue_peck=cloaker_hit, # breaks vram
        statue_flustered=CLOAKER_RECOIL,
        # chandelier_challenge=cloaker_hit, # breaks vram
        # endgame_challenge=cloaker_hit # breaks vram
    )


class DominoLarge(NPC):
    _sprite_id: int = SPR0478_DOMINO_ND_TIME
    _shadow_size = ShadowSize.OVAL_BIG
    _y_shift: int = 1
    _acute_axis: int = 8
    _obtuse_axis: int = 8
    _height: int = 17
    _min_vram_size: int = 3

    _animations = SpriteAnimationCollection(statue_flustered=CLOAKER_RECOIL)


class DrillBit(NPC):
    _sprite_id: int = SPR0483_DRILL_BIT
    _y_shift: int = 2
    _height: int = 11
    _directions = VramStore.DIR0_SWSE_NWNE
    _shadow_size = ShadowSize.OVAL_SMALL

    _animations = SpriteAnimationCollection(
        tower_bullet=DRILLBIT_HIT,
        kitchen_prep=DRILLBIT_HIT,
        factory_pierce=DRILLBIT_HIT_FAST,
    )


class AxemPink(NPC):
    _sprite_id: int = SPR0484_AXEM_PINK
    _acute_axis: int = 5
    _obtuse_axis: int = 5

    _animations = SpriteAnimationCollection(
        tower_bullet=AXEM_PINK_HIT,
        kitchen_prep=AXEM_PINK_HIT,
        factory_pierce=AXEM_PINK_HIT,
    )


class AxemBlack(NPC):
    _sprite_id: int = SPR0485_AXEM_BLACK
    _acute_axis: int = 5
    _obtuse_axis: int = 5

    _animations = SpriteAnimationCollection(
        tower_bullet=AXEM_BLACK_HIT,
        kitchen_prep=AXEM_BLACK_HIT,
        factory_pierce=AXEM_BLACK_HIT,
    )


class AeroUpright(NPC):
    _sprite_id: int = SPR0487_AERO
    _shadow_size = ShadowSize.OVAL_SMALL
    _acute_axis: int = 3
    _obtuse_axis: int = 3
    _height: int = 13
    _y_shift: int = 1


class Snifit(NPC):
    _sprite_id: int = SPR0504_SNIFIT
    _y_shift: int = 2
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 9
    _directions = VramStore.DIR0_SWSE_NWNE

    _animations = SpriteAnimationCollection(
        tower_bullet=SNIFIT_SHOOT,
        kitchen_prep=SNIFIT_TAUNT,
        factory_pierce=SNIFIT_TAUNT,
    )


class CountDownGridplane(NPC):
    _sprite_id: int = SPR0572_COUNT_DOWN_GRIDPLANE
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 11
    _obtuse_axis: int = 11
    _height: int = 13


class MokuraLarge(NPC):
    _sprite_id: int = SPR0573_MOKURA
    _show_shadow: bool = False
    _y_shift: int = 2
    _acute_axis: int = 10
    _obtuse_axis: int = 10
    _height: int = 18
    _shadow_size = ShadowSize.OVAL_SMALL
    _min_vram_size: int = 5


class PandoriteSmall(MimicFace):
    _sprite_id: int = SPR0583_PANDORITE_SMALL
    _y_shift: int = 1

    _alt_palette: Palette = PANDORITE_FACE_PALETTE


class HidonSmall(MimicFace):
    _sprite_id: int = SPR0584_HIDON_SMALL
    _y_shift: int = 1
    _alt_palette: Palette = HIDON_FACE_PALETTE


class ChesterSmall(MimicFace):
    _sprite_id: int = SPR0585_CHESTER_SMALL
    _y_shift: int = 1

    _alt_palette: Palette = CHESTER_FACE_PALETTE


class BoxBoySmall(MimicFace):
    _sprite_id: int = SPR0586_BOX_BOY_SMALL
    _y_shift: int = 1

    _alt_palette: Palette = BOXBOY_FACE_PALETTE


class HammerBroSmall(NPC):
    _sprite_id: int = SPR0587_HAMMER_BRO_SMALL
    _y_shift: int = 1
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 13
    _eye_height: int = 6


class MackSmall(NPC):
    _sprite_id: int = SPR0588_MACK_SMALL
    _y_shift: int = 1

    _eye_height: int = 19


class Belome1Small(NPC):
    _sprite_id: int = SPR0589_BELOME_SMALL
    _y_shift: int = 1
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 13


class Belome2Small(NPC):
    _sprite_id: int = SPR0590_BELOME_SMALL
    _y_shift: int = 1
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 13
    _alt_palette: Palette = BELOME_2_SMALL_PALETTE


class BowyerSmall(NPC):
    _sprite_id: int = SPR0591_BOWYER_SMALL
    _y_shift: int = 1

    _eye_height: int = 16


class PunchinelloSmall(NPC):
    _sprite_id: int = SPR0592_PUNCHINELLO_SMALL
    _y_shift: int = 1
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 13


class DodoSmall(NPC):
    _sprite_id: int = SPR0593_DODO_SMALL
    _y_shift: int = 1
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 13


class BirdettaSmall(NPC):
    _sprite_id: int = SPR0594_BIRDETTA_SMALL
    _y_shift: int = 1

    _eye_height: int = 6


class CzarDragonSmall(NPC):
    _sprite_id: int = SPR0595_CZAR_DRAGON_SMALL
    _y_shift: int = 1
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 13

    _eye_height: int = 3


class BoomerSmall(NPC):
    _sprite_id: int = SPR0596_BOOMER_SMALL
    _y_shift: int = 1


class ExorSmall(NPC):
    _sprite_id: int = SPR0597_EXOR_SMALL
    _y_shift: int = 1
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 13


class DominoSmall(NPC):
    _sprite_id: int = SPR0598_DOMINO_SMALL
    _y_shift: int = 1
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 13


class SmithySmall(NPC):
    _sprite_id: int = SPR0599_SMITHY_SMALL
    _y_shift: int = 1
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 13


class MarioDoll(NPC):
    _sprite_id: int = SPR0600_MARIO_DOLL_UNAFFECTED_BY_MAIN_CHARACTER_PALETTE
    _shadow_size = ShadowSize.OVAL_SMALL
    _directions = VramStore.DIR0_SWSE_NWNE
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 3
    _y_shift: int = 1


class GoldGoomba(NPC):
    _sprite_id: int = SPR0602_GOLD_GOOMBA
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 10


class BigFlower(ItemNPC):
    _sprite_id: int = SPR0605_BIG_FLOWER
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _chest_packet: Packet = P000_FLASHING_POOF_FLOWER
    _static_packet: Packet = P086_FLOWER_STATIC
    _falling_packet: Packet = P035_FLOWER_FALL
    _chest_70A7_upper: int = 2


class SmallFrogCoin(Coin):
    _sprite_id: int = SPR0606_SMALL_FROG_COIN
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _chest_packet: Packet = P019_FROG_COIN_BEING_COLLECTED
    _static_packet: Packet = P111_FROG_COIN_STATIC
    _falling_packet: Packet = P108_FROG_COIN_FALL
    _chest_70A7_upper: int = 3
    _acute_axis: int = 2
    _obtuse_axis: int = 2
    _height: int = 3
    _min_vram_size: int = 1


class Jinx1(Jinx):
    _sprite_id: int = SPR0607_JINX_OVERWORLD


class Jinx3(Jinx):
    _sprite_id: int = SPR0608_JINX_OVERWORLD

    _alt_palette: Palette = JINX_3_ALT_PALETTE


class TerrapinEnding(NPC):
    _sprite_id: int = SPR0609_TERRAPIN_ENDING_CREDITS
    _y_shift: int = 1
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 11
    _directions = VramStore.DIR0_SWSE_NWNE


class StumpetHead(NPC):
    _sprite_id: int = SPR0610_STUMPET_HEAD
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _acute_axis: int = 10
    _obtuse_axis: int = 10
    _height: int = 18
    _min_vram_size: int = 3


class StumpetRoot(NPC):
    _sprite_id: int = SPR0611_STUMPET_ROOTS_RIGHT
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 3


class CzarBody(NPC):
    _sprite_id: int = SPR0612_CZAR_DRAGON_BODY
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _acute_axis: int = 10
    _obtuse_axis: int = 10
    _height: int = 18
    _min_vram_size: int = 3


class VineBeanstalm(NPC):
    _sprite_id: int = SPR0613_GROWING_VINE_BEANSTALK
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 1
    _min_vram_size: int = 3


class BrownBrick(NPC):
    _sprite_id: int = SPR0614_BRICK_BEANSTALK_BLOCK
    _show_shadow: bool = False
    _shadow_size = ShadowSize.BLOCK
    _y_shift: int = 1
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 7


class SandWhirlpool(NPC):
    _sprite_id: int = SPR0615_WHIRLPOOL_DESERT
    _y_shift: int = 1
    _acute_axis: int = 9
    _obtuse_axis: int = 9
    _height: int = 0
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _min_vram_size: int = 1


class Letter(NPC):
    _sprite_id: int = SPR0616_YELLOW_LETTER
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 7


class YaridOverworld(NPC):
    _sprite_id: int = SPR0617_YARIDOVICH_OUT_OF_BATTLE
    _y_shift: int = 1
    _acute_axis: int = 11
    _obtuse_axis: int = 11
    _height: int = 15
    _min_vram_size: int = 2

    _animations = SpriteAnimationCollection(
        chandelier_challenge=YARIDOVICH_ALT_TAUNT,
        endgame_challenge=YARIDOVICH_ALT_TAUNT,
    )
    # may need adjusting


class TentacleExtending(NPC):
    _sprite_id: int = SPR0618_TENTACLE_EXTENDING
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 2
    _obtuse_axis: int = 9
    _height: int = 5
    _min_vram_size: int = 1

    _animations = SpriteAnimationCollection(ship_beckon=TENTACLE_BECKON)


class BackSnifit(NPC):
    _sprite_id: int = SPR0619_SNIFIT_BLACK_BACK
    _y_shift: int = 1
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 11


class DonutLift(NPC):
    _sprite_id: int = SPR0620_FALLING_STEPPING_BRIDGE_BLOCK
    _shadow_size = ShadowSize.BLOCK
    _y_shift: int = -1
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 7


class NESProtagonist(NPC):
    _sprite_id: int = SPR0621_OLD_CLASSIC_MARIO
    _height: int = 1


class SplashWaterDroplets(NPC):
    _sprite_id: int = SPR0623_SPLASH_WATER_DROPLETS
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 2
    _obtuse_axis: int = 2
    _height: int = 3


class Fish(NPC):
    _sprite_id: int = SPR0624_SMALL_SEA_FISH
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 2
    _obtuse_axis: int = 2
    _height: int = 3


class Geyser(NPC):
    _sprite_id: int = SPR0625_SPLASH_WATER_GEYSER
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 1


class BowyerOverworld(NPC):
    _sprite_id: int = SPR0626_BOWYER
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 6
    _obtuse_axis: int = 8
    _height: int = 16
    _min_vram_size: int = 3


class MushroomLamp(NPC):
    _sprite_id: int = SPR0627_MUSHROOM_HOUSE_DECOR_MAILBOX
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 3


class Link(NPC):
    _sprite_id: int = SPR0628_LINK_SLEEPING_IN_ROSE_TOWN_INN
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 2


class Samus(NPC):
    _sprite_id: int = SPR0629_SAMUS_SLEEPING_IN_MUSHROOM_KINGDOM
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 5
    _obtuse_axis: int = 5
    _height: int = 2


class GreyBlock(NPC):
    _sprite_id: int = SPR0630_GREY_STEPPING_STONE
    _shadow_size = ShadowSize.BLOCK
    _y_shift: int = -2
    _acute_axis: int = 6
    _obtuse_axis: int = 6
    _height: int = 4


class PlaneModel(NPC):
    _sprite_id: int = SPR0631_HINOPIO_S_MODEL_AIRPLANE_BLUE_GREY
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _acute_axis: int = 3
    _obtuse_axis: int = 3
    _height: int = 6


class GreyBrick(NPC):
    _sprite_id: int = SPR0632_GREY_STONE_BLOCK
    _shadow_size = ShadowSize.BLOCK
    _y_shift: int = -3
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 7


class CulexSmall(NPC):
    _sprite_id: int = SPR0633_CULEX_SMALL
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 11

    _eye_height: int = 12


class CircularSparkle(NPC):
    _sprite_id: int = SPR0635_SPARKLE_CIRCULAR_WINDING
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 1


class Flower(ItemNPC):
    _sprite_id: int = SPR0636_SMALL_FLOWER_STANDALONE
    _y_shift: int = 1
    _chest_packet: Packet = P000_FLASHING_POOF_FLOWER
    _static_packet: Packet = P086_FLOWER_STATIC
    _falling_packet: Packet = P035_FLOWER_FALL
    _chest_70A7_upper: int = 2


class RecoveryMushroom(ItemNPC):
    _sprite_id: int = SPR0637_RECOVERY_MUSHROOM_STANDALONE
    _y_shift: int = 1
    _chest_packet: Packet = P001_FLASHING_POOF_MUSHROOM
    _static_packet: Packet = P087_MUSHROOM_STATIC
    _falling_packet: Packet = P036_MUSHROOM_FALL


class Key(ItemNPC):
    _sprite_id: int = SPR0638_KEY_STANDALONE
    _y_shift: int = 1
    _chest_packet: Packet = P002_BRIEF_KEY
    _static_packet: Packet = P088_KEY_STATIC
    _falling_packet: Packet = P089_KEY_FALLING
    _chest_event: int = E0882_CHEST_KEY_PACKET


class ItemBag(ItemNPC):
    _sprite_id: int = SPR0639_ITEM_BAG_STANDALONE
    _y_shift: int = 1


class Music(ItemNPC):
    _sprite_id: int = SPR0640_MUSIC_NOTE_STANDALONE
    _y_shift: int = 1
    _chest_packet: Packet = P168_MUSIC_NOTE_CHEST
    _static_packet: Packet = P166_MUSIC_NOTE_STATIC
    _falling_packet: Packet = P167_MUSIC_NOTE_FALL
    _chest_event: int = E0909_CHEST_MUSIC_PACKET


class TinyMushroom(NPC):
    _sprite_id: int = SPR0641_AMANITA_MUSHROOM_STANDALONE
    _shadow_size = ShadowSize.OVAL_SMALL


class DingalingGridplane(NPC):
    _sprite_id: int = SPR0642_DINGALING_GRIDPLANE
    _y_shift: int = -6
    _acute_axis: int = 11
    _obtuse_axis: int = 11
    _height: int = 13


class EggbertGridplane(NPC):
    _sprite_id: int = SPR0643_EGGBERT_GRIDPLANE
    _shadow_size = ShadowSize.OVAL_SMALL
    _show_shadow: bool = False
    _acute_axis: int = 2
    _obtuse_axis: int = 2
    _height: int = 5

    _animations = SpriteAnimationCollection(
        tower_bullet=EGGBERT_EXPAND,
        kitchen_prep=EGGBERT_EXPAND,
        factory_pierce=EGGBERT_EXPAND,
    )


class FireCrystal(NPC):
    _sprite_id: int = SPR0644_FIRE_CRYSTAL_GRIDPLANE
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 5
    _obtuse_axis: int = 5


class WaterCrystal(NPC):
    _sprite_id: int = SPR0645_WATER_CRYSTAL_GRIDPLANE
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 5
    _obtuse_axis: int = 5


class EarthCrystal(NPC):
    _sprite_id: int = SPR0646_EARTH_CRYSTAL_GRIDPLANE
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 5
    _obtuse_axis: int = 5


class WindCrystal(NPC):
    _sprite_id: int = SPR0647_WIND_CRYSTAL_GRIDPLANE
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 5
    _obtuse_axis: int = 5


class GenoBullet(NPC):
    _sprite_id: int = SPR0648_GENO_ARM_SHOT
    _shadow_size = ShadowSize.OVAL_SMALL
    _show_shadow: bool = False
    _y_shift: int = 1
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 1


class MackMedium(NPC):
    _sprite_id: int = SPR0649_MACK_MEDIUM
    _shadow_size = ShadowSize.OVAL_BIG
    _y_shift: int = 1
    _acute_axis: int = 13
    _obtuse_axis: int = 13
    _height: int = 23
    _min_vram_size: int = 3


class KnifeGuyGridplane(NPC):
    _sprite_id: int = SPR0650_KNIFE_GUY_GRIDPLANE
    _min_vram_size: int = 0
    _y_shift: int = 1
    _acute_axis: int = 7
    _obtuse_axis: int = 7


class TinyBloober(NPC):
    _sprite_id: int = SPR0651_TINY_BLOOBER_STANDALONE
    _acute_axis: int = 2
    _obtuse_axis: int = 2
    _height: int = 7
    _y_shift: int = 1


class MimicStatue(MimicFace, Statue):
    _sprite_id: int = SPR0652_MIMIC_STATUE


class CrocoStatue(CrocoBase, Statue):
    _sprite_id: int = SPR0653_CROCO_STATUE
    _details = StatueDetails(horizontal_pixel_shift=-3)


class BoosterStatue(Booster, Statue):
    _sprite_id: int = SPR0654_BOOSTER_STATUE


class JohnnyStatue(JohnnySmall, Statue):
    _sprite_id: int = SPR0655_JOHNNY_STATUE


class MagikoopaStatue(SmallMagikoopa, Statue):
    _sprite_id: int = SPR0656_MAGIKOOPA_STATUE

    _details = StatueDetails(
        horizontal_pixel_shift=2,
        north_facing_horizontal_pixel_shift=-4,
        north_facing_vertical_pixel_shift=-1,
    )


class ValentinaStatue(NimbusLandStatue, Statue):
    _sprite_id: int = SPR0063_VALENTINA_STATUE


class ShovelKnightStatue(ShovelKnightBoss, Statue):
    _sprite_id: int = SPR0657_CLERK_MANAGER_DIRECTOR_STATUE
    _details = StatueDetails(
        horizontal_pixel_shift=-3,
        north_facing_horizontal_pixel_shift=-5,
    )


class YaridovichStatue(FakeElder, Statue):
    _sprite_id: int = SPR0658_FAKE_ELDER_STATUE


class GrateGuyStatue(GrateGuySmall, Statue):
    _sprite_id: int = SPR0659_GRATE_GUY_STATUE
    _details = StatueDetails(
        horizontal_pixel_shift=-3,
        north_facing_horizontal_pixel_shift=-2,
    )


class JinxStatue(Jinx, Statue):
    _sprite_id: int = SPR0660_JINX_STATUE


class MokuraStatue(MokuraCloud, Statue):
    _sprite_id: int = SPR0661_MOKURA_STATUE


class TerrapinStatue(Terrapin, Statue):
    _sprite_id: int = SPR0662_JAGGER_STATUE


class PiranhaPlantStatue(PiranhaPlant, Statue):
    _sprite_id: int = SPR0663_PIRANHA_PLANT_STATUE


class BlooberStatue(Bloober, Statue):
    _sprite_id: int = SPR0664_BLOOBER_STATUE


class FactoryChiefStatue(FactoryChief, Statue):
    _sprite_id: int = SPR0665_FACTORY_CHIEF_STATUE
    _details = StatueDetails(horizontal_pixel_shift=-1)


class AxemRedStatue(AxemRed, Statue):
    _sprite_id: int = SPR0666_AXEM_RED_STATUE
    _details = StatueDetails(horizontal_pixel_shift=-6)


class BundtSmall(NPC):
    _sprite_id: int = SPR0712_EMPTY
    _shadow_size = ShadowSize.OVAL_BIG
    _y_shift: int = 1
    _acute_axis: int = 7
    _obtuse_axis: int = 7
    _height: int = 8

    _eye_height: int = 8


class BundtStatue(BundtSmall, Statue):
    _sprite_id: int = SPR0667_BUNDT_STATUE
    _details = StatueDetails(horizontal_pixel_shift=-3)


class CountDownStatue(CountDownGridplane, Statue):
    _sprite_id: int = SPR0668_COUNT_DOWN_STATUE
    _details = StatueDetails(
        horizontal_pixel_shift=4,
        vertical_pixel_shift=-1,
    )


class HammerBroStatue(HammerBroSmall, Statue):
    _sprite_id: int = SPR0669_HAMMER_BRO_STATUE


class MackStatue(MackSmall, Statue):
    _sprite_id: int = SPR0670_MACK_STATUE


class SmallBelomeStatue(Belome1Small, Statue):
    _sprite_id: int = SPR0671_SMALL_BELOME_STATUE


class Belome2Large(NPC):
    _sprite_id: int = SPR0672_BELOME_LARGE_OVERWORLD
    _min_vram_size: int = 5
    _shadow_size = ShadowSize.OVAL_BIG
    _y_shift: int = 2
    _acute_axis: int = 10
    _obtuse_axis: int = 10
    _height: int = 18

    _animations = SpriteAnimationCollection(
        mines_punch=BELOME_ATTACK,
        statue_intro=BELOME_WIGGLE,
        statue_flustered=BELOME_RECOIL,
        statue_peck=BELOME_ATTACK_FAST,
        chandelier_challenge=BELOME_ATTACK,
        endgame_challenge=BELOME_ATTACK,
    )

    _alt_palette: Palette = BELOME_2_LARGE_PALETTE


class BowyerStatue(BowyerSmall, Statue):
    _sprite_id: int = SPR0673_BOWYER_STATUE


class PunchinelloStatue(PunchinelloSmall, Statue):
    _sprite_id: int = SPR0674_PUNCHINELLO_STATUE


class DodoStatue(DodoSmall, Statue):
    _sprite_id: int = SPR0675_DODO_STATUE


class BirdettaStatue(BirdettaSmall, Statue):
    _sprite_id: int = SPR0676_BIRDETTA_STATUE


class CzarStatue(CzarDragonSmall, Statue):
    _sprite_id: int = SPR0677_CZAR_DRAGON_STATUE


class BoomerStatue(BoomerSmall, Statue):
    _sprite_id: int = SPR0678_BOOMER_STATUE


class ExorStatue(ExorSmall, Statue):
    _sprite_id: int = SPR0679_EXOR_STATUE


class DominoStatue(DominoSmall, Statue):
    _sprite_id: int = SPR0680_DOMINO_STATUE


class SmithyStatue(SmithySmall, Statue):
    _sprite_id: int = SPR0681_SMITHY_STATUE


class CulexStatue(CulexSmall, Statue):
    _sprite_id: int = SPR0682_CULEX_STATUE


class MallowStatue(NPC):
    _sprite_id: int = SPR0683_MALLOW_STATUE_UNTINTED
    _height: int = 8


class Chompweed(NPC):
    _sprite_id: int = SPR0685_CHOMPWEED
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _height: int = 6


class MackLarge(NPC):
    _sprite_id: int = SPR0686_MACK_SUB
    _shadow_size = ShadowSize.OVAL_BIG
    _y_shift: int = 1
    _acute_axis: int = 13
    _obtuse_axis: int = 13
    _height: int = 23
    _min_vram_size: int = 3

    _animations = SpriteAnimationCollection(
        mines_punch=MACK_HIT,
        statue_peck=MACK_HIT_FAST,
        statue_flustered=MACK_CHALLENGE,
        chandelier_challenge=MACK_CHALLENGE,
        endgame_challenge=MACK_HIT,
    )


class Belome1Large(NPC):
    _sprite_id: int = SPR0687_BELOME_SUB
    _min_vram_size: int = 5
    _shadow_size = ShadowSize.OVAL_BIG
    _y_shift: int = 2
    _acute_axis: int = 10
    _obtuse_axis: int = 10
    _height: int = 18

    _animations = SpriteAnimationCollection(
        mines_punch=BELOME_ATTACK,
        statue_intro=BELOME_WIGGLE,
        statue_flustered=BELOME_RECOIL,
        statue_peck=BELOME_ATTACK_FAST,
        chandelier_challenge=BELOME_ATTACK,
        endgame_challenge=BELOME_ATTACK,
    )


class BowyerLarge(NPC):
    _sprite_id: int = SPR0688_BOWYER_SUB
    _y_shift: int = 1
    _acute_axis: int = 14
    _obtuse_axis: int = 15
    _height: int = 16
    _min_vram_size: int = 5
    _shadow_size = ShadowSize.OVAL_SMALL
    _show_shadow: bool = False

    _animations = SpriteAnimationCollection(
        mines_punch=BOWYER_HIT,
        statue_intro=BOWYER_TAUNT,
        statue_flustered=BOWYER_RECOIL,
        chandelier_challenge=BOWYER_TAUNT,
        endgame_challenge=BOWYER_TAUNT,
    )


class JohnnyLarge(NPC):
    _sprite_id: int = SPR0691_JOHNNY_SUB
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 13
    _obtuse_axis: int = 13
    _height: int = 23
    _min_vram_size: int = 7

    _animations = SpriteAnimationCollection(
        mines_punch=JOHNNY_HIT,
        chandelier_challenge=JOHNNY_TAUNT,
        endgame_challenge=JOHNNY_TAUNT,
    )


class YaridovichLarge(NPC):
    _sprite_id: int = SPR0692_YARIDOVICH_SUB
    _shadow_size = ShadowSize.OVAL_BIG
    _y_shift: int = 1
    _acute_axis: int = 13
    _obtuse_axis: int = 13
    _height: int = 23
    _min_vram_size: int = 7

    _animations = SpriteAnimationCollection(
        mines_punch=YARIDOVICH_HIT,
        statue_intro=YARIDOVICH_TAUNT,
        statue_flustered=YARIDOVICH_RECOIL,
        chandelier_challenge=YARIDOVICH_TAUNT,
        endgame_challenge=YARIDOVICH_TAUNT,
    )


class KnifeGuyLarge(NPC):
    _sprite_id: int = SPR0689_KNIFE_GUY_SUB
    _min_vram_size: int = 3
    _shadow_size = ShadowSize.OVAL_BIG
    _y_shift: int = 1
    _acute_axis: int = 11
    _obtuse_axis: int = 11
    _height: int = 13


class GrateGuyLarge(NPC):
    _sprite_id: int = SPR0690_GRATE_GUY_SUB
    _min_vram_size: int = 3
    _shadow_size = ShadowSize.OVAL_BIG
    _y_shift: int = 1
    _acute_axis: int = 11
    _obtuse_axis: int = 11
    _height: int = 13

    _animations = SpriteAnimationCollection(
        mines_punch=GRATE_GUY_HIT,
        statue_intro=GRATE_GUY_TAUNT,
        statue_peck=GRATE_GUY_HIT_FAST,
        statue_flustered=GRATE_GUY_RECOIL,
        chandelier_challenge=GRATE_GUY_TAUNT,
        endgame_challenge=GRATE_GUY_TAUNT,
    )


class CulexLarge(NPC):
    _sprite_id: int = SPR0694_CULEX_SUB
    _shadow_size = ShadowSize.OVAL_BIG
    _y_shift: int = 1
    _acute_axis: int = 13
    _obtuse_axis: int = 13
    _height: int = 31
    _min_vram_size: int = 7


class ValentinaLarge(NPC):
    _sprite_id: int = SPR0697_VALENTINA_SUB
    _shadow_size = ShadowSize.OVAL_BIG
    _y_shift: int = 1
    _acute_axis: int = 13
    _obtuse_axis: int = 13
    _height: int = 23
    _min_vram_size: int = 5

    _animations = SpriteAnimationCollection(
        # mines_punch=valentina_hit,
        statue_intro=VALENTINA_TAUNT,
        # statue_peck=valentina_hit,
        statue_flustered=VALENTINA_RECOIL,
        chandelier_challenge=VALENTINA_TAUNT,
        endgame_challenge=VALENTINA_TAUNT,
    )


class CzarDragonLarge(NPC):
    _sprite_id: int = SPR0698_CZAR_DRAGON_SUB
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _acute_axis: int = 10
    _obtuse_axis: int = 10
    _height: int = 18
    _min_vram_size: int = 3

    _animations = SpriteAnimationCollection(
        mines_punch=CZAR_DRAGON_HIT,
        statue_intro=CZAR_TAUNT,
        statue_flustered=CZAR_RECOIL,
    )


class DirectorLarge(ShovelKnightBossLarge):
    _sprite_id: int = SPR0704_DIRECTOR_SUB


class BeetleGridplane(ItemNPC):
    _sprite_id: int = SPR0706_BEETLE_GRIDPLANE
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1


class BananaGridplane(ItemNPC):
    _sprite_id: int = SPR0707_BANANA_GRIDPLANE
    _show_shadow: bool = False
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1


class CrownGridplane(ItemNPC):
    _sprite_id: int = SPR0708_CROWN_GRIDPLANE


class BroochGridplane(ItemNPC):
    _sprite_id: int = SPR0709_BROOCH_GRIDPLANE


class ShoesGridplane(ItemNPC):
    _sprite_id: int = SPR0710_SHOES_GRIDPLANE


class RingGridplane(ItemNPC):
    _sprite_id: int = SPR0711_RING_GRIDPLANE


class TinyBird(NPC):
    _sprite_id: int = SPR0777_STAR_EGG_LITTLE_BROWN_BIRD
    _shadow_size = ShadowSize.OVAL_SMALL
    _y_shift: int = 1
    _acute_axis: int = 1
    _obtuse_axis: int = 1
    _height: int = 1


class SmithyLarge(NPC):
    _sprite_id: int = SPR0959_SMITHY_LOWER
    _shadow_size = ShadowSize.BLOCK
    _acute_axis: int = 12
    _obtuse_axis: int = 15
    _height: int = 13

    _animations = SpriteAnimationCollection(
        mines_punch=SMITHY_HIT,
        statue_peck=SMITHY_HIT_FAST,
        chandelier_challenge=SMITHY_HIT,
        endgame_challenge=SMITHY_HIT,
    )


class Goombette(NPC):
    _sprite_id: int = SPR0960_GOOMBETTE_LOWER
    _shadow_size = ShadowSize.OVAL_SMALL
    _acute_axis: int = 2
    _obtuse_axis: int = 2
    _height: int = 7
    _directions = VramStore.DIR0_SWSE_NWNE

    _animations = SpriteAnimationCollection(
        tower_bullet=GOOMBETTE_HIT,
        kitchen_prep=GOOMBETTE_TAUNT,
        factory_pierce=GOOMBETTE_HIT_FAST,
    )


class Empty(ItemNPC):
    _sprite_id: int = SPR1023_EMPTY
    _shadow_size = ShadowSize.OVAL_SMALL
    _show_shadow: bool = False
    _y_shift: int = 1
    _acute_axis: int = 4
    _obtuse_axis: int = 4
    _height: int = 9
