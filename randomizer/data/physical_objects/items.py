from ...types.physical_objects import ItemNPC
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import Packet
from ...data.variables.packet_names import *
from ...data.variables.event_script_names import *
from ...data.variables.sprite_names import *
from ...data.rooms.npcs import *


class DefaultItem(ItemNPC):
    _base = ITEM_BAG_NPC
    _chest_packet_id = P005_BRIEF_POOF_BAG
    _static_packet_id = P090_BAG_STATIC
    _falling_packet_id = P037_ITEM_BAG_FALL
    _chest_event_id: int = E0883_CHEST_ITEM_BAG_PACKET


class HammerObject(ItemNPC):
    _base = HAMMER_BASE
    _chest_packet_id = P208_HAMMER_CHEST
    _chest_event_id = E0922_CHEST_HAMMER_PACKET
    _static_packet_id = P206_HAMMER_STATIC
    _falling_packet_id = P207_HAMMER_FALL


class StickObject(ItemNPC):
    _base = FROGGIE_STICK_BASE
    _chest_packet_id = P211_STICK_CHEST
    _chest_event_id = E0923_CHEST_STICK_PACKET
    _static_packet_id = P209_STICK_STATIC
    _falling_packet_id = P210_STICK_FALL


class GreenShellObject(ItemNPC):
    _base = GREEN_SHELL_BASE
    _chest_packet_id = P223_GREEN_SHELL_CHEST
    _static_packet_id = P221_GREEN_SHELL_STATIC
    _falling_packet_id = P222_GREEN_SHELL_FALL
    _chest_event_id = E0927_CHEST_GREEN_SHELL_PACKET


class MusicObject(ItemNPC):
    _base = MUSIC_BASE
    _chest_packet_id = P168_MUSIC_NOTE_CHEST
    _static_packet_id = P166_MUSIC_NOTE_STATIC
    _falling_packet_id = P167_MUSIC_NOTE_FALL
    _chest_event_id = E0909_CHEST_MUSIC_PACKET


class ChompObject(ItemNPC):
    _base = CHOMP_BASE
    _chest_packet_id = P214_CHOMP_CHEST
    _chest_event_id = E0924_CHEST_CHOMP_PACKET
    _static_packet_id = P212_CHOMP_STATIC
    _falling_packet_id = P213_CHOMP_FALL


class RedShellObject(ItemNPC):
    _base = RED_SHELL_BASE
    _chest_packet_id = P220_RED_SHELL_CHEST
    _static_packet_id = P218_RED_SHELL_STATIC
    _falling_packet_id = P219_RED_SHELL_FALL
    _chest_event_id = E0926_CHEST_RED_SHELL_PACKET


class ParasolObject(ItemNPC):
    _base = PARASOL_BASE
    _chest_packet_id = P226_PARASOL_CHEST
    _chest_event_id = E0928_CHEST_CHEST_PARASOL_PACKET
    _static_packet_id = P224_PARASOL_STATIC
    _falling_packet_id = P225_PARASOL_FALL


class FanObject(ItemNPC):
    _base = FAN_BASE
    _chest_packet_id = P217_FAN_CHEST
    _chest_event_id = E2952_CLONE_RESERVED
    _static_packet_id = P215_FAN_STATIC
    _falling_packet_id = P216_FAN_FALL


class TinyStarObject(ItemNPC):
    _base = TINY_STAR_BASE
    _chest_packet_id = P081_STAR_PIECE_CHEST
    _static_packet_id = P085_STAR_PIECE_STATIC
    _falling_packet_id = P083_STAR_PIECE_FALL
    _chest_event_id = E0885_CHEST_STAR_PIECE_PACKET


class FryingPanObject(ItemNPC):
    _base = PAN_BASE
    _chest_packet_id = P205_FRYING_PAN_CHEST
    _chest_event_id = E0921_CHEST_FRYING_PAN_PACKET
    _static_packet_id = P203_FRYING_PAN_STATIC
    _falling_packet_id = P204_FRYING_PAN_FALL


class CrownObject(ItemNPC):
    _base = CROWN_BASE
    _chest_packet_id = P103_CROWN_CHEST
    _static_packet_id = P105_CROWN_STATIC
    _falling_packet_id = P104_CROWN_FALL
    _chest_event_id = E0890_CHEST_CROWN_PACKET


class ShoesObject(ItemNPC):
    _base = SHOES_BASE
    _chest_packet_id = P099_SHOES_CHEST
    _static_packet_id = P097_SHOES_STATIC
    _falling_packet_id = P098_SHOES_FALL
    _chest_event_id = E0888_CHEST_SHOES_PACKET


class BroochObject(ItemNPC):
    _base = BROOCH_BASE
    _chest_packet_id = P096_BROOCH_CHEST
    _static_packet_id = P094_BROOCH_STATIC
    _falling_packet_id = P095_BROOCH_FALL
    _chest_event_id = E0887_CHEST_BROOCH_PACKET


class RingObject(ItemNPC):
    _base = RING_BASE
    _chest_packet_id = P091_RING_CHEST
    _static_packet_id = P093_RING_STATIC
    _falling_packet_id = P092_RING_FALL
    _chest_event_id = E0886_CHEST_RING_PACKET


class FeatherObject(ItemNPC):
    _base = FEATHER_BASE
    _chest_packet_id = P080_FEATHER_CHEST
    _chest_event_id = E0884_CHEST_FEATHER_PACKET
    _static_packet_id = P084_FEATHER_STATIC
    _falling_packet_id = P082_FEATHER_FALL


class RedMushroomObject(ItemNPC):
    _base = RED_MUSHROOM_BASE
    _chest_packet_id = P196_RED_MUSHROOM_CHEST
    _chest_event_id = E0918_CHEST_RED_MUSHROOM_PACKET
    _static_packet_id = P194_RED_MUSHROOM_STATIC
    _falling_packet_id = P195_RED_MUSHROOM_FALL


class GreenMushroomObject(ItemNPC):
    _base = GREEN_MUSHROOM_BASE
    _chest_packet_id = P199_GREEN_MUSHROOM_CHEST
    _chest_event_id = E0919_CHEST_GREEN_MUSHROOM_PACKET
    _static_packet_id = P197_GREEN_MUSHROOM_STATIC
    _falling_packet_id = P198_GREEN_MUSHROOM_FALL


class YellowMushroomObject(ItemNPC):
    _base = YELLOW_MUSHROOM_BASE
    _chest_packet_id = P202_YELLOW_MUSHROOM_CHEST
    _chest_event_id = E0920_CHEST_YELLOW_MUSHROOM_PACKET
    _static_packet_id = P200_YELLOW_MUSHROOM_STATIC
    _falling_packet_id = P201_YELLOW_MUSHROOM_FALL


class RedSyrupObject(ItemNPC):
    _base = RED_SYRUP_BASE
    _chest_packet_id = P132_RED_SYRUP_CHEST
    _static_packet_id = P130_RED_SYRUP_STATIC
    _falling_packet_id = P131_RED_SYRUP_FALL
    _chest_event_id = E0897_CHEST_RED_SYRUP_PACKET


class GreenSyrupObject(ItemNPC):
    _base = GREEN_SYRUP_BASE
    _chest_packet_id = P129_GREEN_SYRUP_CHEST
    _static_packet_id = P127_GREEN_SYRUP_STATIC
    _falling_packet_id = P128_GREEN_SYRUP_FALL
    _chest_event_id = E0896_CHEST_GREEN_SYRUP_PACKET


class YellowSyrupObject(ItemNPC):
    _base = YELLOW_SYRUP_BASE
    _chest_packet_id = P138_YELLOW_SYRUP_CHEST
    _static_packet_id = P136_YELLOW_SYRUP_STATIC
    _falling_packet_id = P137_YELLOW_SYRUP_FALL
    _chest_event_id = E0899_CHEST_YELLOW_SYRUP_PACKET


class BlueSyrupObject(ItemNPC):
    _base = BLUE_SYRUP_BASE
    _chest_packet_id = P135_BLUE_SYRUP_CHEST
    _static_packet_id = P133_BLUE_SYRUP_STATIC
    _falling_packet_id = P134_BLUE_SYRUP_FALL
    _chest_event_id = E0898_CHEST_BLUE_SYRUP_PACKET


class StarDrinkObject(ItemNPC):
    _base = STAR_DRINK_BASE
    _chest_packet_id = P171_STAR_DRINK_CHEST
    _static_packet_id = P169_STAR_DRINK_STATIC
    _falling_packet_id = P170_STAR_DRINK_FALL
    _chest_event_id = E0910_CHEST_STAR_DRINK_PACKET


class RDrinkObject(ItemNPC):
    _base = R_DRINK_BASE
    _chest_packet_id = P165_R_DRINK_CHEST
    _static_packet_id = P163_R_DRINK_STATIC
    _falling_packet_id = P164_R_DRINK_FALL
    _chest_event_id = E0908_CHEST_R_DRINK_PACKET


class DDrinkObject(ItemNPC):
    _base = D_DRINK_BASE
    _chest_packet_id = P148_D_DRINK_CHEST
    _static_packet_id = P150_D_DRINK_STATIC
    _falling_packet_id = P149_D_DRINK_FALL
    _chest_event_id = E0903_CHEST_D_DRINK_PACKET


class PDrinkObject(ItemNPC):
    _base = P_DRINK_BASE
    _chest_packet_id = P147_P_DRINK_CHEST
    _static_packet_id = P145_P_DRINK_STATIC
    _falling_packet_id = P146_P_DRINK_FALL
    _chest_event_id = E0902_CHEST_P_DRINK_PACKET


class GreenJuiceObject(ItemNPC):
    _base = GREEN_JUICE_BASE
    _chest_packet_id = P141_GREEN_JUICE_CHEST
    _static_packet_id = P139_GREEN_JUICE_STATIC
    _falling_packet_id = P140_GREEN_JUICE_FALL
    _chest_event_id = E0900_CHEST_GREEN_JUICE_PACKET


class YellowJuiceObject(ItemNPC):
    _base = YELLOW_JUICE_BASE
    _chest_packet_id = P229_YELLOW_JUICE_CHEST
    _static_packet_id = P227_YELLOW_JUICE_STATIC
    _falling_packet_id = P228_YELLOW_JUICE_FALL
    _chest_event_id = E0929_CHEST_YELLOW_JUICE_PACKET


class RedJuiceObject(ItemNPC):
    _base = RED_JUICE_BASE
    _chest_packet_id = P117_EGG_CHEST
    _static_packet_id = P115_EGG_STATIC
    _falling_packet_id = P116_EGG_FALLING
    _chest_event_id = E0892_CHEST_EGG_PACKET


class FrogDrinkObject(ItemNPC):
    _base = FROG_DRINK_BASE
    _chest_packet_id = P157_FROG_DRINK_CHEST
    _static_packet_id = P159_FROG_DRINK_STATIC
    _falling_packet_id = P158_FROG_DRINK_FALL
    _chest_event_id = E0906_CHEST_FROG_DRINK_PACKET


class CookieObject(ItemNPC):
    _base = COOKIE_BASE
    _chest_packet_id = P120_COOKIE_CHEST
    _chest_event_id = E0893_CHEST_COOKIE_PACKET
    _static_packet_id = P118_COOKIE_STATIC
    _falling_packet_id = P119_COOKIE_FALL


class YellowBombObject(ItemNPC):
    _base = YELLOW_BOMB_BASE
    _chest_packet_id = P190_YELLOW_BOMB_CHEST
    _static_packet_id = P188_YELLOW_BOMB_STATIC
    _falling_packet_id = P189_YELLOW_BOMB_FALL
    _chest_event_id = E0916_CHEST_YELLOW_BOMB_PACKET


class RedBombObject(ItemNPC):
    _base = RED_BOMB_BASE
    _chest_packet_id = P184_RED_BOMB_CHEST
    _static_packet_id = P182_RED_BOMB_STATIC
    _falling_packet_id = P183_RED_BOMB_FALL
    _chest_event_id = E0914_CHEST_RED_BOMB_PACKET


class BlueBombObject(ItemNPC):
    _base = BLUE_BOMB_BASE
    _chest_packet_id = P187_BLUE_BOMB_CHEST
    _static_packet_id = P185_BLUE_BOMB_STATIC
    _falling_packet_id = P186_BLUE_BOMB_FALL
    _chest_event_id = E0915_CHEST_BLUE_BOMB_PACKET


class GreenCandyObject(ItemNPC):
    _base = GREEN_CANDY_BASE
    _chest_packet_id = P175_GREEN_CANDY_CHEST
    _static_packet_id = P173_GREEN_CANDY_STATIC
    _falling_packet_id = P174_GREEN_CANDY_FALL
    _chest_event_id = E0911_CHEST_GREEN_CANDY_PACKET


class YellowMusicDrinkObject(ItemNPC):
    _base = YELLOW_MUSIC_DRINK_BASE
    _chest_packet_id = P151_YELLOW_MUSIC_DRINK_CHEST
    _static_packet_id = P153_YELLOW_MUSIC_DRINK_STATIC
    _falling_packet_id = P152_YELLOW_MUSIC_DRINK_FALL
    _chest_event_id = E0904_CHEST_YELLOW_M_DRINK_PACKET


class BlueMusicDrinkObject(ItemNPC):
    _base = BLUE_MUSIC_DRINK_BASE
    _chest_packet_id = P154_BLUE_MUSIC_DRINK_CHEST
    _static_packet_id = P156_BLUE_MUSIC_DRINK_STATIC
    _falling_packet_id = P155_BLUE_MUSIC_DRINK_FALL
    _chest_event_id = E0905_CHEST_BLUE_M_DRINK_PACKET


class RedMusicDrinkObject(ItemNPC):
    _base = RED_MUSIC_DRINK_BASE
    _chest_packet_id = P160_RED_MUSIC_DRINK_CHEST
    _static_packet_id = P162_RED_MUSIC_DRINK_STATIC
    _falling_packet_id = P161_RED_MUSIC_DRINK_FALL
    _chest_event_id = E0907_CHEST_RED_M_DRINK_PACKET


class KeyObject(ItemNPC):
    _base = KEY_BASE
    _chest_packet_id = P002_BRIEF_KEY
    _static_packet_id = P088_KEY_STATIC
    _falling_packet_id = P089_KEY_FALLING
    _chest_event_id = E0882_CHEST_KEY_PACKET


class SmallCoinObject(ItemNPC):
    _base = SMALL_COIN_BASE
    _chest_packet_id = P018_SMALL_COIN_BEING_COLLECTED
    _static_packet_id = P110_SMALL_COIN_STATIC
    _falling_packet_id = P107_SMALL_COIN_FALL


class SmallFrogCoinObject(ItemNPC):
    _base = SMALL_FROG_COIN_BASE
    _chest_packet_id = P019_FROG_COIN_BEING_COLLECTED
    _static_packet_id = P111_FROG_COIN_STATIC
    _falling_packet_id = P108_FROG_COIN_FALL
    _chest_70a7_upper = 3


class BlueCandyObject(ItemNPC):
    _base = BLUE_CANDY_BASE
    _chest_packet_id = P178_BLUE_CANDY_CHEST
    _static_packet_id = P176_BLUE_CANDY_STATIC
    _falling_packet_id = P177_BLUE_CANDY_FALL
    _chest_event_id = E0912_CHEST_BLUE_CANDY_PACKET


class MicrobombObject(ItemNPC):
    _base = MICROBOMB_BASE
    _chest_packet_id = P114_BOMB_CHEST
    _static_packet_id = P112_BOMB_STATIC
    _falling_packet_id = P113_BOMB_FALL
    _chest_event_id = E0891_CHEST_BOMB_PACKET


class EggObject(ItemNPC):
    _base = EGG_BASE
    _chest_packet_id = P117_EGG_CHEST
    _static_packet_id = P115_EGG_STATIC
    _falling_packet_id = P116_EGG_FALLING
    _chest_event_id = E0892_CHEST_EGG_PACKET


class GreenBombObject(ItemNPC):
    _base = GREEN_BOMB_BASE
    _chest_packet_id = P181_GREEN_BOMB_CHEST
    _static_packet_id = P179_GREEN_BOMB_STATIC
    _falling_packet_id = P180_GREEN_BOMB_FALL
    _chest_event_id = E0913_CHEST_GREEN_BOMB_PACKET


class CardObject(ItemNPC):
    _base = CARD_BASE
    _chest_packet_id = P126_CARD_CHEST
    _chest_event_id = E0895_CHEST_CARD_PACKET
    _static_packet_id = P124_CARD_STATIC
    _falling_packet_id = P125_CARD_FALL


class BananaObject(ItemNPC):
    _base = BANANA_BASE
    _chest_packet_id = P102_BANANA_CHEST
    _static_packet_id = P100_BANANA_STATIC
    _falling_packet_id = P101_BANANA_FALL
    _chest_event_id = E0889_CHEST_BANANA_PEEL_PACKET


class BerryObject(ItemNPC):
    _base = BERRY_BASE
    _chest_packet_id = P123_BERRY_CHEST
    _chest_event_id = E0894_CHEST_BERRY_PACKET
    _static_packet_id = P121_BERRY_STATIC
    _falling_packet_id = P122_BERRY_FALL


class BigCoinObject(ItemNPC):
    _base = BIG_COIN_BASE
    _chest_packet_id = P016_BIG_COIN_BEING_COLLECTED
    _static_packet_id = P109_COIN_STATIC
    _falling_packet_id = P106_COIN_FALL


class BeetleObject(ItemNPC):
    _base = BEETLE_BASE
    _chest_packet_id = P193_BEETLE_CHEST
    _chest_event_id = E0917_CHEST_BEETLE_PACKET
    _static_packet_id = P191_BEETLE_STATIC
    _falling_packet_id = P192_BEETLE_FALL


class FlowerObject(ItemNPC):
    _base = FLOWER_BASE
    _chest_70a7_upper = 2
    _chest_packet_id = P000_FLASHING_POOF_FLOWER
    _static_packet_id = P086_FLOWER_STATIC
    _falling_packet_id = P035_FLOWER_FALL


class RecoveryMushroomObject(ItemNPC):
    _base = RECOVERY_MUSHROOM_BASE
    _chest_packet_id = P001_FLASHING_POOF_MUSHROOM
    _static_packet_id = P087_MUSHROOM_STATIC
    _falling_packet_id = P036_MUSHROOM_FALL


class FrogCoinObject(ItemNPC):
    _base = FROG_COIN_BASE
    _chest_packet_id = P019_FROG_COIN_BEING_COLLECTED
    _static_packet_id = P111_FROG_COIN_STATIC
    _falling_packet_id = P108_FROG_COIN_FALL


class GloveObject(ItemNPC):
    _base = GLOVE_BASE
    _chest_packet_id = P232_GLOVE_CHEST
    _static_packet_id = P230_GLOVE_STATIC
    _falling_packet_id = P231_GLOVE_FALL
    _chest_event_id = E0950_CHEST_GLOVE_PACKET

class ProgressiveFireworksObject(ItemNPC):
    _base = ITEM_BAG_NPC
    _chest_packet_id = P233_CRYSTAL_CHEST
    _static_packet_id = P090_BAG_STATIC
    _falling_packet_id = P037_ITEM_BAG_FALL
    _chest_event_id = E3100_PROGRESSIVE_FIREWORKS_CHEST_GRANT

class CrystalObject(ItemNPC):
    _base = CRYSTAL_BASE
    _chest_packet_id = P233_CRYSTAL_CHEST
    _static_packet_id = P235_CRYSTAL_STATIC
    _falling_packet_id = P234_CRYSTAL_FALL
    _chest_event_id = E0951_CRYSTAL_CHEST_PACKET

# possibilities for more models
# urchin
# heart
# tiny bloober
# tiny toad
# character dolls (maybe in the future when they can be recruited in chests)
# cannonball
# tiny clouds
# amanita mushroom
# goombette
# tiny magmite
# shaman's wand?
# knife guy's knife
# bowyer arrow
# helio
# remo con x
# tiny gorgon
# lamb's lure sheep