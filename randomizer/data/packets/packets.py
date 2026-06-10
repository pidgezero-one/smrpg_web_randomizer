from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.packet import (
    Packet as PacketBase,
    PacketCollection,
)
from ..variables.sprite_names import *
from ..variables.action_script_names import *

class Packet(PacketBase):
    # Whether this packet should be allocated through the NPC-slot path at
    # $C1:95DD instead of the bitmap allocator at $C1:9547. Packets in vanilla
    # with id < 8 took the NPC slot path; the SMRPG-web patch widens that
    # gate. Subclasses override to opt in. Read by `GameWorld.build_patch`
    # which iterates `self.packets.packets` to assemble the allowlist for
    # the inline range-check ASM at $C1:80C8.
    #
    # Why a class flag (not a hardcoded ID list): packet IDs can shuffle, and
    # editing one place (the class) keeps source-of-truth co-located with the
    # packet definition rather than a parallel allowlist.
    goes_to_npc_slot_buffer: bool = False


class BoosterHillPacket(Packet):
    # Booster Hill prize packets (both falling room-54 variants spawned by
    # CreatePacketAtObjectCoords and standing room-14 variants spawned by
    # CreatePacketAt7010WithEvent). Both stay on the vanilla bitmap path
    # at $C1:9547 — `goes_to_npc_slot_buffer = False` (inherited).
    #
    # An earlier vram_size-based routing patch incorrectly swept these onto
    # the NPC slot path because they share vram_size=0 with chest items,
    # which is what made them invisible in the original bug report. Routing
    # standing variants to NPC slot path was also tried and confirmed to
    # leave them invisible — chest-style allocation isn't applicable here.
    def __init__(self, packet_id: int, sprite_id: int, action_script_id: int) -> None:
        super().__init__(
            packet_id,
            sprite_id,
            action_script_id,
            0,
            0,
            1,
            4,
            False,
            True,
            False,
            False,
            0,
            0,
        )


class ChestPacket(Packet):
    # Chest item/coin/spell packets all share the small-VRAM footprint that
    # makes the NPC slot allocator path safe and avoids the bitmap-allocator
    # corruption seen on chest spawns.
    goes_to_npc_slot_buffer: bool = True

    def __init__(
        self,
        packet_id: int,
        sprite_id: int,
        action_script_id: int,
        b0: int = 0,
        vram_size: int = 0,
        sprite_priority: int = 3,
        layer_priority: int = 3,
        b2b2: bool = False,
        b2b3: bool = False,
        b2b4: bool = False,
        show_shadow: bool = False,
        b2: int = 0,
        b4: int = 0,
    ) -> None:
        super().__init__(
            packet_id,
            sprite_id,
            action_script_id,
            b0,
            vram_size,
            sprite_priority,
            layer_priority,
            b2b2,
            b2b3,
            b2b4,
            show_shadow,
            b2,
            b4,
        )


class ShipPrizePacket(Packet):
    def __init__(self, packet_id: int, sprite_id: int, action_script_id: int) -> None:
        super().__init__(
            packet_id,
            sprite_id,
            action_script_id,
            0,
            0,
            1,
            4,
            False,
            True,
            False,
            True,
            0,
            0,
        )


P000_FLASHING_POOF_FLOWER = ChestPacket(
    packet_id=0,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0910_FLOWER_FLASH_THEN_POOF,
)
P001_FLASHING_POOF_MUSHROOM = ChestPacket(
    packet_id=1,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0908_MUSHROOM_FLASH_THEN_POOF,
)
P002_FLOWER_PACK_CHEST_ITEM = ChestPacket(
    packet_id=2,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0992_CHEST_ITEMS_WITH_SPECIFIC_IDS,
)
P003_BRIEF_STAR = ChestPacket(
    packet_id=3,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0909_STAR_APPEARS_BRIEFLY,
    sprite_priority=2,
    layer_priority=4,
)
P004_MIMIC_3_POOF_ON_DEFEAT = ChestPacket(
    packet_id=4,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0912_POOF_WHEN_MIMIC_3_DEFEATED,
)
P005_BRIEF_POOF_BAG = ChestPacket(
    packet_id=5,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0127_BAG_APPEARS_BRIEFLY_THEN_POOFS,
)
P006_FEATHER_CHEST = ChestPacket(
    packet_id=6,
    sprite_id=SPR0252_FEATHER,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P007_STAR_PIECE_CHEST = ChestPacket(
    packet_id=7,
    sprite_id=SPR0226_TINY_STAR,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P008_RED_CHEST_ITEM = ChestPacket(
    packet_id=8,
    sprite_id=SPR0219_RED_ITEM_COLLECTION,
    action_script_id=A0992_CHEST_ITEMS_WITH_SPECIFIC_IDS,
)
P009_GREEN_CHEST_ITEM = ChestPacket(
    packet_id=9,
    sprite_id=SPR0220_GREEN_ITEM_COLLECTION,
    action_script_id=A0992_CHEST_ITEMS_WITH_SPECIFIC_IDS,
)
P010_BLUE_CHEST_ITEM = ChestPacket(
    packet_id=10,
    sprite_id=SPR0223_BLUE_ITEM_COLLECTION,
    action_script_id=A0992_CHEST_ITEMS_WITH_SPECIFIC_IDS,
)
P011_YELLOW_CHEST_ITEM = ChestPacket(
    packet_id=11,
    sprite_id=SPR0221_YELLOW_ITEM_COLLECTION,
    action_script_id=A0992_CHEST_ITEMS_WITH_SPECIFIC_IDS,
)
P012_FLOWER_STATIC = ChestPacket(
    packet_id=12,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0793_DEFAULT_SEQUENCE_STATIC,
)
P013_MUSHROOM_STATIC = ChestPacket(
    packet_id=13,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0581_SEQUENCE_1_STATIC,
)
P014_PLAYER_ENTERS_WATER = Packet(
    packet_id=14,
    sprite_id=SPR0255_BEETLE,
    action_script_id=A0914_PLAYER_ENTERS_WATER,
    show_shadow=False,
    b0=3,
    vram_size=3,
    sprite_priority=1,
    layer_priority=4,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P015_PLAYER_ENTERS_WATER = Packet(
    packet_id=15,
    sprite_id=SPR0255_BEETLE,
    action_script_id=A0915_PLAYER_ENTERS_WATER,
    show_shadow=False,
    b0=3,
    vram_size=3,
    sprite_priority=1,
    layer_priority=4,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P016_BIG_COIN_BEING_COLLECTED = Packet(
    packet_id=16,
    sprite_id=SPR0192_COIN,
    action_script_id=A0904_COIN_GETS_COLLECTED,
    show_shadow=False,
    b0=0,
    vram_size=5,
    sprite_priority=3,
    layer_priority=3,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P017_SMALL_MINIGAME_COIN = Packet(
    packet_id=17,
    sprite_id=SPR0193_SMALL_COIN,
    action_script_id=A0171_MINIGAME_COIN_SPINS,
    show_shadow=False,
    b0=0,
    vram_size=5,
    sprite_priority=3,
    layer_priority=4,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P018_SMALL_COIN_BEING_COLLECTED = Packet(
    packet_id=18,
    sprite_id=SPR0193_SMALL_COIN,
    action_script_id=A0904_COIN_GETS_COLLECTED,
    show_shadow=False,
    b0=0,
    vram_size=5,
    sprite_priority=3,
    layer_priority=3,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P019_FROG_COIN_BEING_COLLECTED = Packet(
    packet_id=19,
    sprite_id=SPR0194_FROG_COIN,
    action_script_id=A0911_FROG_COIN_GETS_COLLECTED,
    show_shadow=False,
    b0=0,
    vram_size=5,
    sprite_priority=3,
    layer_priority=3,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P020_WATER_SPLASH = Packet(
    packet_id=20,
    sprite_id=SPR0210_SPLASH_WATER_DROPLETS,
    action_script_id=A0167_SPAWN_AT_7016_701A_CALCULATED,
    show_shadow=False,
    b0=0,
    vram_size=3,
    sprite_priority=3,
    layer_priority=3,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P021_FLASHING_SMALL_EXPLOSION = Packet(
    packet_id=21,
    sprite_id=SPR0200_EXPLOSION,
    action_script_id=A0623_SMALL_EXPLOSION_FLASH_7_TIMES,
    show_shadow=False,
    b0=0,
    vram_size=3,
    sprite_priority=1,
    layer_priority=4,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P022_RECURSIVE_SPARKLES = Packet(
    packet_id=22,
    sprite_id=SPR0197_SPARKLE_SIDEWAYS,
    action_script_id=A0446_SUMMON_EXTRA_SPARKLES,
    show_shadow=False,
    b0=0,
    vram_size=1,
    sprite_priority=3,
    layer_priority=3,
    b2b2=True,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P023_LOOPING_SINGLE_SPARKLE = Packet(
    packet_id=23,
    sprite_id=SPR0197_SPARKLE_SIDEWAYS,
    action_script_id=A0447_LOOPING_SINGLE_SPARKLE,
    show_shadow=False,
    b0=0,
    vram_size=1,
    sprite_priority=3,
    layer_priority=3,
    b2b2=True,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P024_REGULAR_SOUND_EXPLOSION = Packet(
    packet_id=24,
    sprite_id=SPR0200_EXPLOSION,
    action_script_id=A0063_EXPLOSION_WITH_SOUND,
    show_shadow=False,
    b0=0,
    vram_size=3,
    sprite_priority=2,
    layer_priority=3,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P025_RING_CHEST = ChestPacket(
    packet_id=25,
    sprite_id=SPR0196_RING,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P026_SUNKEN_SHIP_TRAMPOLINE_PUZZLE = ShipPrizePacket(
    packet_id=26,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0870_SUNKEN_SHIP_TRAMPOLINE_PUZZLE,
)
P027_SUNKEN_SHIP_TROOPA_PUZZLE = ShipPrizePacket(
    packet_id=27,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0871_SUNKEN_SHIP_TROOPA_PUZZLE,
)
P028_MUSHROOM_THROWN_SOUTHWEST = Packet(
    packet_id=28,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0907_MUSHROOM_THROWN_SOUTHWEST,
    show_shadow=True,
    b0=0,
    vram_size=1,
    sprite_priority=1,
    layer_priority=4,
    b2b2=False,
    b2b3=True,
    b2b4=False,
    b2=0,
    b4=0,
)
P029_SUNKEN_SHIP_3D_MAZE = ShipPrizePacket(
    packet_id=29,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0872_SUNKEN_SHIP_3D_MAZE_PRIZE,
)
P030_WATER_SPLASH_DROPS_SFX = Packet(
    packet_id=30,
    sprite_id=SPR0210_SPLASH_WATER_DROPLETS,
    action_script_id=A0720_WATER_SPLASH_DROPS_SFX,
    show_shadow=False,
    b0=0,
    vram_size=3,
    sprite_priority=2,
    layer_priority=3,
    b2b2=True,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P031_LEVELUP_TEXT = Packet(
    packet_id=31,
    sprite_id=SPR0203_LEVEL_UP_TEXT_FROM_INVINCIBLE_STAR,
    action_script_id=A0620_LEVELUP_TEXT,
    show_shadow=False,
    b0=0,
    vram_size=3,
    sprite_priority=3,
    layer_priority=3,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P032_BLUE_CLOUD = Packet(
    packet_id=32,
    sprite_id=SPR0201_MOKURA_S_CLOUD_BLUE,
    action_script_id=A0651_MOKURA_PACKET,
    show_shadow=False,
    b0=0,
    vram_size=1,
    sprite_priority=1,
    layer_priority=3,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P033_BOMB_EXPLOSION = Packet(
    packet_id=33,
    sprite_id=SPR0200_EXPLOSION,
    action_script_id=A0303_BOMB_EXPLOSION,
    show_shadow=False,
    b0=0,
    vram_size=1,
    sprite_priority=1,
    layer_priority=3,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P034_GREY_EXPLOSION_SFX = Packet(
    packet_id=34,
    sprite_id=SPR0204_GREY_EXPLOSION_WHEN_ENCOUNTERING_FIREBALLS,
    action_script_id=A0063_EXPLOSION_WITH_SOUND,
    show_shadow=False,
    b0=0,
    vram_size=3,
    sprite_priority=2,
    layer_priority=3,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P035_SUNKEN_SHIP_CANNONBALL_PUZZLE = ShipPrizePacket(
    packet_id=35,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0874_SUNKEN_SHIP_CANNONBALL,
)
P036_BARREL_PUZZLE_PRIZE = ShipPrizePacket(
    packet_id=36,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0873_BARREL_PUZZLE,
)
P037_SHIP_STAIRCASE = ShipPrizePacket(
    packet_id=37,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0875_SHIP_STAIRCASE,
)
P038_BOOSTER_HILL_PRIZE_0 = BoosterHillPacket(
    packet_id=38,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0065_BOOSTER_HILL_PRIZE_0,
)
P039_BOOSTER_HILL_PRIZE_1 = BoosterHillPacket(
    packet_id=39,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0066_BOOSTER_HILL_PRIZE_1,
)
P040_BROOCH_CHEST = ChestPacket(
    packet_id=40,
    sprite_id=SPR0207_BROOCH,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P041_BOOSTER_HILL_PRIZE_2 = BoosterHillPacket(
    packet_id=41,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0067_BOOSTER_HILL_PRIZE_2,
)
P042_BOOSTER_HILL_PRIZE_3 = BoosterHillPacket(
    packet_id=42,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0068_BOOSTER_HILL_PRIZE_3,
)
P043_SHOES_CHEST = ChestPacket(
    packet_id=43,
    sprite_id=SPR0202_SHOES,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P044_BOOSTER_HILL_PRIZE_4 = BoosterHillPacket(
    packet_id=44,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0069_BOOSTER_HILL_PRIZE_4,
)
P045_TELEPORTATION_SHINE = Packet(
    packet_id=45,
    sprite_id=SPR0213_AXEM_RED_TELEPORT,
    action_script_id=A0940_TELEPORTATION_SHINE,
    show_shadow=False,
    b0=0,
    vram_size=3,
    sprite_priority=1,
    layer_priority=4,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P046_BOOSTER_HILL_PRIZE_5 = BoosterHillPacket(
    packet_id=46,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0070_BOOSTER_HILL_PRIZE_5,
)
P047_BLUE_FIRE_TRAIL = Packet(
    packet_id=47,
    sprite_id=SPR0201_MOKURA_S_CLOUD_BLUE,
    action_script_id=A0943_BLUE_FIRE_TRAIL,
    show_shadow=False,
    b0=0,
    vram_size=1,
    sprite_priority=2,
    layer_priority=4,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P048_BANANA_CHEST = ChestPacket(
    packet_id=48,
    sprite_id=SPR0222_BANANA_PEEL,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P049_HAMMER_SPARKS_SFX = Packet(
    packet_id=49,
    sprite_id=SPR0198_SPARKLE_DOWNWARDS,
    action_script_id=A0952_HAMMER_SPARKS_SFX,
    show_shadow=False,
    b0=0,
    vram_size=3,
    sprite_priority=3,
    layer_priority=3,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P050_WATER_BLAST_SFX = Packet(
    packet_id=50,
    sprite_id=SPR0242_WHITE_GAS_CLOUD,
    action_script_id=A0249_WATER_BLAST_SFX,
    show_shadow=False,
    b0=0,
    vram_size=7,
    sprite_priority=1,
    layer_priority=4,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P051_DRILL_BIT = Packet(
    packet_id=51,
    sprite_id=SPR0243_MACHINE_MADE_DRILL_BIT,
    action_script_id=A0250_DRILL_BIT,
    show_shadow=False,
    b0=0,
    vram_size=7,
    sprite_priority=1,
    layer_priority=4,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=2,
)
P052_BOMB_EXPLOSION_FASTER = Packet(
    packet_id=52,
    sprite_id=SPR0200_EXPLOSION,
    action_script_id=A0195_BOMB_EXPLOSION_FASTER,
    show_shadow=False,
    b0=0,
    vram_size=1,
    sprite_priority=1,
    layer_priority=3,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P053_CROWN_CHEST = ChestPacket(
    packet_id=53,
    sprite_id=SPR0216_CROWN,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P054_LEVELUP_BONUS_POW = Packet(
    packet_id=54,
    sprite_id=SPR0833_LEVEL_UP_BONUS_POW_POWER,
    action_script_id=A0000_DO_NOTHING,
    show_shadow=False,
    b0=0,
    vram_size=1,
    sprite_priority=0,
    layer_priority=0,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P055_LEVELUP_BONUS_S = Packet(
    packet_id=55,
    sprite_id=SPR0834_LEVEL_UP_BONUS_STAR_MAGIC,
    action_script_id=A0000_DO_NOTHING,
    show_shadow=False,
    b0=0,
    vram_size=1,
    sprite_priority=0,
    layer_priority=0,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P056_LEVELUP_BONUS_HP = Packet(
    packet_id=56,
    sprite_id=SPR0835_LEVEL_UP_BONUS_HP,
    action_script_id=A0000_DO_NOTHING,
    show_shadow=False,
    b0=0,
    vram_size=1,
    sprite_priority=0,
    layer_priority=0,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P057_BOOSTER_HILL_PRIZE_6 = BoosterHillPacket(
    packet_id=57,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0071_BOOSTER_HILL_PRIZE_6,
)
P058_BOOSTER_HILL_PRIZE_7 = BoosterHillPacket(
    packet_id=58,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0072_BOOSTER_HILL_PRIZE_7,
)
P059_BOOSTER_HILL_PRIZE_8 = BoosterHillPacket(
    packet_id=59,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0073_BOOSTER_HILL_PRIZE_8,
)
P060_BOOSTER_HILL_PRIZE_9 = BoosterHillPacket(
    packet_id=60,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0074_BOOSTER_HILL_PRIZE_9,
)
P061_BOOSTER_HILL_PRIZE_10 = BoosterHillPacket(
    packet_id=61,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0075_BOOSTER_HILL_PRIZE_10,
)
P062_SPLASH = Packet(
    packet_id=62,
    sprite_id=SPR0210_SPLASH_WATER_DROPLETS,
    action_script_id=A0000_DO_NOTHING,
    show_shadow=False,
    b0=0,
    vram_size=1,
    sprite_priority=0,
    layer_priority=0,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P063_BOOSTER_HILL_PRIZE_12 = BoosterHillPacket(
    packet_id=63,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0077_BOOSTER_HILL_PRIZE_12,
)
P064_FROG_COIN_CHEST_STILL = ChestPacket(
    packet_id=64,
    sprite_id=SPR0234_STATIC_FROG_COIN,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P065_BOOSTER_HILL_PRIZE_13 = BoosterHillPacket(
    packet_id=65,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0082_BOOSTER_HILL_PRIZE_13,
)
P066_BOOSTER_HILL_PRIZE_14 = BoosterHillPacket(
    packet_id=66,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0083_BOOSTER_HILL_PRIZE_14,
)
P067_BOMB_CHEST = ChestPacket(
    packet_id=67,
    sprite_id=SPR0205_MICROBOMB_PACKET,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P068_BOOSTER_HILL_PRIZE_15 = BoosterHillPacket(
    packet_id=68,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0084_BOOSTER_HILL_PRIZE_15,
)
P069_BOOSTER_HILL_PRIZE_STANDING_0 = BoosterHillPacket(
    packet_id=69,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0143_BOOSTER_HILL_PRIZE_STANDING_0,
)
P070_EGG_CHEST = ChestPacket(
    packet_id=70,
    sprite_id=SPR0237_EGG,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P071_BOOSTER_HILL_PRIZE_STANDING_1 = BoosterHillPacket(
    packet_id=71,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0086_BOOSTER_HILL_PRIZE_STANDING_2,
)
P072_BOOSTER_HILL_PRIZE_STANDING_2 = BoosterHillPacket(
    packet_id=72,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0085_BOOSTER_HILL_PRIZE_STANDING_1,
)
P073_COOKIE_CHEST = ChestPacket(
    packet_id=73,
    sprite_id=SPR0254_YOSHI_COOKIE,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P074_BOOSTER_HILL_PRIZE_STANDING_3 = BoosterHillPacket(
    packet_id=74,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0089_BOOSTER_HILL_PRIZE_STANDING_3,
)
P075_BOOSTER_HILL_PRIZE_STANDING_4 = BoosterHillPacket(
    packet_id=75,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0090_BOOSTER_HILL_PRIZE_STANDING_4,
)
P076_BERRY_CHEST = ChestPacket(
    packet_id=76,
    sprite_id=SPR0253_BERRY,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P077_BOOSTER_HILL_PRIZE_STANDING_5 = BoosterHillPacket(
    packet_id=77,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0093_BOOSTER_HILL_PRIZE_STANDING_5,
)
P078_BOOSTER_HILL_PRIZE_STANDING_6 = BoosterHillPacket(
    packet_id=78,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0094_BOOSTER_HILL_PRIZE_STANDING_6,
)
P079_CARD_CHEST = ChestPacket(
    packet_id=79,
    sprite_id=SPR0206_CARD,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P080_BOOSTER_HILL_PRIZE_STANDING_7 = BoosterHillPacket(
    packet_id=80,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0096_BOOSTER_HILL_PRIZE_STANDING_7,
)
P081_BOOSTER_HILL_PRIZE_STANDING_8 = BoosterHillPacket(
    packet_id=81,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0097_BOOSTER_HILL_PRIZE_STANDING_8,
)
P082_BOOSTER_HILL_PRIZE_STANDING_9 = BoosterHillPacket(
    packet_id=82,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0100_BOOSTER_HILL_PRIZE_STANDING_9,
)
P083_BOOSTER_HILL_PRIZE_STANDING_10 = BoosterHillPacket(
    packet_id=83,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0114_BOOSTER_HILL_PRIZE_STANDING_10,
)
P084_BOOSTER_HILL_PRIZE_STANDING_11 = BoosterHillPacket(
    packet_id=84,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0137_BOOSTER_HILL_PRIZE_STANDING_11,
)
P085_BOOSTER_HILL_PRIZE_STANDING_12 = BoosterHillPacket(
    packet_id=85,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0139_BOOSTER_HILL_PRIZE_STANDING_12,
)
P086_BOOSTER_HILL_PRIZE_STANDING_13 = BoosterHillPacket(
    packet_id=86,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0140_BOOSTER_HILL_PRIZE_STANDING_13,
)
P087_BOOSTER_HILL_PRIZE_STANDING_14 = BoosterHillPacket(
    packet_id=87,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0141_BOOSTER_HILL_PRIZE_STANDING_14,
)
P088_BOOSTER_HILL_PRIZE_STANDING_15 = BoosterHillPacket(
    packet_id=88,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0142_BOOSTER_HILL_PRIZE_STANDING_15,
)
P089_BEETLE_CHEST = ChestPacket(
    packet_id=89,
    sprite_id=SPR0251_BEETLE_PACKET_COPY,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P090_SMALL_COIN_STILL = ChestPacket(
    packet_id=90,
    sprite_id=SPR0236_COIN_STATIC_SMALL,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P091_CHEST_COIN_STILL = ChestPacket(
    packet_id=91,
    sprite_id=SPR0235_STATIC_COIN,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P092_GLOVE_CHEST = ChestPacket(
    packet_id=92,
    sprite_id=SPR0208_GLOVE,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P093_CRYSTAL_CHEST = ChestPacket(
    packet_id=93,
    sprite_id=SPR0209_SHINY_STONE,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P094_FIRE_SPELL_CHEST = ChestPacket(
    packet_id=94,
    sprite_id=SPR0214_RED_BALL,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P095_BLUE_SPELL_CHEST = ChestPacket(
    packet_id=95,
    sprite_id=SPR0215_BLUE_BALL,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P096_GREEN_SPELL_CHEST = ChestPacket(
    packet_id=96,
    sprite_id=SPR0217_GREEN_BALL,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P097_YELLOW_SPELL_CHEST = ChestPacket(
    packet_id=97,
    sprite_id=SPR0218_YELLOW_BALL,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P098_GRAY_SPELL_CHEST = ChestPacket(
    packet_id=98,
    sprite_id=SPR0224_GRAY_BALL,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P099_BAG_STATIC = Packet(
    packet_id=99,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0545_SEQUENCE_5_STATIC,
    show_shadow=False,
    b0=0,
    vram_size=0,
    sprite_priority=3,
    layer_priority=3,
    b2b2=False,
    b2b3=False,
    b2b4=False,
    b2=0,
    b4=0,
)
P100_BOOSTER_HILL_PRIZE_11 = BoosterHillPacket(
    packet_id=100,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0076_BOOSTER_HILL_PRIZE_11,
)
P101_FLOWER_COLLECTION = ChestPacket(
    packet_id=101,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A0992_CHEST_ITEMS_WITH_SPECIFIC_IDS,
)
P102_SMALL_FROG_COIN_STILL = ChestPacket(
    packet_id=102,
    sprite_id=SPR0238_STATIC_FROG_COIN_SMALL,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P103_MIMIC_1_POOF_ON_DEFEAT = ChestPacket(
    packet_id=103,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A1017_MIMIC_1_POOF_WHEN_DEFEATED,
)
P104_MIMIC_2_POOF_ON_DEFEAT = ChestPacket(
    packet_id=104,
    sprite_id=SPR0195_FLOWER,
    action_script_id=A1018_MIMIC_2_POOF_WHEN_DEFEATED,
)
P105_MARIO_DOLL = ChestPacket(
    packet_id=105,
    sprite_id=SPR0233_MARIO_DOLL,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P106_MALLOW_DOLL = ChestPacket(
    packet_id=106,
    sprite_id=SPR0199_MALLOW_DOLL,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P107_GENO_DOLL = ChestPacket(
    packet_id=107,
    sprite_id=SPR0239_GENO_DOLL,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P108_TOADSTOOL_DOLL = ChestPacket(
    packet_id=108,
    sprite_id=SPR0240_TOADSTOOL_DOLL,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P109_BOWSER_DOLL = ChestPacket(
    packet_id=109,
    sprite_id=SPR0241_BOWSER_DOLL,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
    vram_size=1
)
P110_MOKURA_CHEST = ChestPacket(
    packet_id=110,
    sprite_id=SPR0201_MOKURA_S_CLOUD_BLUE,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P111_BLUE_CLOUD_CHEST = ChestPacket(
    packet_id=111,
    sprite_id=SPR0201_MOKURA_S_CLOUD_BLUE,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P112_JINX_CHEST = ChestPacket(
    packet_id=112,
    sprite_id=SPR0244_JINX_PACKET,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P113_CHOMP_CHEST = ChestPacket(
    packet_id=113,
    sprite_id=SPR0245_CHOMP_BALL,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P114_STICK_CHEST = ChestPacket(
    packet_id=114,
    sprite_id=SPR0246_STICK_PACKET,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P115_HAMMER_CHEST = ChestPacket(
    packet_id=115,
    sprite_id=SPR0247_HAMMER_PACKET,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P116_AP_ITEM = ChestPacket(
    packet_id=116,
    sprite_id=SPR0248_ARCHIPELAGO,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P117_RED_SHELL_CHEST = ChestPacket(
    packet_id=117,
    sprite_id=SPR0249_RED_SHELL,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P118_GREEN_SHELL_CHEST = ChestPacket(
    packet_id=118,
    sprite_id=SPR0250_GREEN_SHELL,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P119_BAND_CHEST = ChestPacket(
    packet_id=119,
    sprite_id=SPR0212_BAND_PACKET,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P120_PAN_PACKET = ChestPacket(
    packet_id=120,
    sprite_id=SPR0225_FRYING_PAN_PACKET,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P121_FAN_PACKET = ChestPacket(
    packet_id=121,
    sprite_id=SPR0227_FAN_PACKET,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P122_GUN_PACKET = ChestPacket(
    packet_id=122,
    sprite_id=SPR0228_GUN_PACKET,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P123_PANTS_PACKET = ChestPacket(
    packet_id=123,
    sprite_id=SPR0229_PANTS,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P124_OVERALLS_PACKET = ChestPacket(
    packet_id=124,
    sprite_id=SPR0230_OVERALLS,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P125_DRESS_PACKET = ChestPacket(
    packet_id=125,
    sprite_id=SPR0231_DRESS,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P126_CAPE_PACKET = ChestPacket(
    packet_id=126,
    sprite_id=SPR0232_CAPE,
    action_script_id=A1007_CHEST_SEQUENCE_0_DEFAULT,
)
P127_UNUSED = None
P128_UNUSED = None
P129_UNUSED = None
P130_UNUSED = None
P131_UNUSED = None
P132_UNUSED = None
P133_UNUSED = None
P134_UNUSED = None
P135_UNUSED = None
P136_UNUSED = None
P137_UNUSED = None
P138_UNUSED = None
P139_UNUSED = None
P140_UNUSED = None
P141_UNUSED = None
P142_UNUSED = None
P143_UNUSED = None
P144_UNUSED = None
P145_UNUSED = None
P146_UNUSED = None
P147_UNUSED = None
P148_UNUSED = None
P149_UNUSED = None
P150_UNUSED = None
P151_UNUSED = None
P152_UNUSED = None
P153_UNUSED = None
P154_UNUSED = None
P155_UNUSED = None
P156_UNUSED = None
P157_UNUSED = None
P158_UNUSED = None
P159_UNUSED = None
P160_UNUSED = None
P161_UNUSED = None
P162_UNUSED = None
P163_UNUSED = None
P164_UNUSED = None
P165_UNUSED = None
P166_UNUSED = None
P167_UNUSED = None
P168_UNUSED = None
P169_UNUSED = None
P170_UNUSED = None
P171_UNUSED = None
P172_UNUSED = None
P173_UNUSED = None
P174_UNUSED = None
P175_UNUSED = None
P176_UNUSED = None
P177_UNUSED = None
P178_UNUSED = None
P179_UNUSED = None
P180_UNUSED = None
P181_UNUSED = None
P182_UNUSED = None
P183_UNUSED = None
P184_UNUSED = None
P185_UNUSED = None
P186_UNUSED = None
P187_UNUSED = None
P188_UNUSED = None
P189_UNUSED = None
P190_UNUSED = None
P191_UNUSED = None
P192_UNUSED = None
P193_UNUSED = None
P194_UNUSED = None
P195_UNUSED = None
P196_UNUSED = None
P197_UNUSED = None
P198_UNUSED = None
P199_UNUSED = None
P200_UNUSED = None
P201_UNUSED = None
P202_UNUSED = None
P203_UNUSED = None
P204_UNUSED = None
P205_UNUSED = None
P206_UNUSED = None
P207_UNUSED = None
P208_UNUSED = None
P209_UNUSED = None
P210_UNUSED = None
P211_UNUSED = None
P212_UNUSED = None
P213_UNUSED = None
P214_UNUSED = None
P215_UNUSED = None
P216_UNUSED = None
P217_UNUSED = None
P218_UNUSED = None
P219_UNUSED = None
P220_UNUSED = None
P221_UNUSED = None
P222_UNUSED = None
P223_UNUSED = None
P224_UNUSED = None
P225_UNUSED = None
P226_UNUSED = None
P227_UNUSED = None
P228_UNUSED = None
P229_UNUSED = None
P230_UNUSED = None
P231_UNUSED = None
P232_UNUSED = None
P233_UNUSED = None
P234_UNUSED = None
P235_UNUSED = None
P236_UNUSED = None
P237_UNUSED = None
P238_UNUSED = None
P239_UNUSED = None
P240_UNUSED = None
P241_UNUSED = None
P242_UNUSED = None
P243_UNUSED = None
P244_UNUSED = None
P245_UNUSED = None
P246_UNUSED = None
P247_UNUSED = None
P248_UNUSED = None
P249_UNUSED = None
P250_UNUSED = None
P251_UNUSED = None
P252_UNUSED = None
P253_UNUSED = None
P254_UNUSED = None
P255_UNUSED = None

# Packet Collection
ALL_PACKETS = PacketCollection(
    [
        P000_FLASHING_POOF_FLOWER,
        P001_FLASHING_POOF_MUSHROOM,
        P002_FLOWER_PACK_CHEST_ITEM,
        P003_BRIEF_STAR,
        P004_MIMIC_3_POOF_ON_DEFEAT,
        P005_BRIEF_POOF_BAG,
        P006_FEATHER_CHEST,
        P007_STAR_PIECE_CHEST,
        P008_RED_CHEST_ITEM,
        P009_GREEN_CHEST_ITEM,
        P010_BLUE_CHEST_ITEM,
        P011_YELLOW_CHEST_ITEM,
        P012_FLOWER_STATIC,
        P013_MUSHROOM_STATIC,
        P014_PLAYER_ENTERS_WATER,
        P015_PLAYER_ENTERS_WATER,
        P016_BIG_COIN_BEING_COLLECTED,
        P017_SMALL_MINIGAME_COIN,
        P018_SMALL_COIN_BEING_COLLECTED,
        P019_FROG_COIN_BEING_COLLECTED,
        P020_WATER_SPLASH,
        P021_FLASHING_SMALL_EXPLOSION,
        P022_RECURSIVE_SPARKLES,
        P023_LOOPING_SINGLE_SPARKLE,
        P024_REGULAR_SOUND_EXPLOSION,
        P025_RING_CHEST,
        P026_SUNKEN_SHIP_TRAMPOLINE_PUZZLE,
        P027_SUNKEN_SHIP_TROOPA_PUZZLE,
        P028_MUSHROOM_THROWN_SOUTHWEST,
        P029_SUNKEN_SHIP_3D_MAZE,
        P030_WATER_SPLASH_DROPS_SFX,
        P031_LEVELUP_TEXT,
        P032_BLUE_CLOUD,
        P033_BOMB_EXPLOSION,
        P034_GREY_EXPLOSION_SFX,
        P035_SUNKEN_SHIP_CANNONBALL_PUZZLE,
        P036_BARREL_PUZZLE_PRIZE,
        P037_SHIP_STAIRCASE,
        P038_BOOSTER_HILL_PRIZE_0,
        P039_BOOSTER_HILL_PRIZE_1,
        P040_BROOCH_CHEST,
        P041_BOOSTER_HILL_PRIZE_2,
        P042_BOOSTER_HILL_PRIZE_3,
        P043_SHOES_CHEST,
        P044_BOOSTER_HILL_PRIZE_4,
        P045_TELEPORTATION_SHINE,
        P046_BOOSTER_HILL_PRIZE_5,
        P047_BLUE_FIRE_TRAIL,
        P048_BANANA_CHEST,
        P049_HAMMER_SPARKS_SFX,
        P050_WATER_BLAST_SFX,
        P051_DRILL_BIT,
        P052_BOMB_EXPLOSION_FASTER,
        P053_CROWN_CHEST,
        P054_LEVELUP_BONUS_POW,
        P055_LEVELUP_BONUS_S,
        P056_LEVELUP_BONUS_HP,
        P057_BOOSTER_HILL_PRIZE_6,
        P058_BOOSTER_HILL_PRIZE_7,
        P059_BOOSTER_HILL_PRIZE_8,
        P060_BOOSTER_HILL_PRIZE_9,
        P061_BOOSTER_HILL_PRIZE_10,
        P062_SPLASH,
        P063_BOOSTER_HILL_PRIZE_12,
        P064_FROG_COIN_CHEST_STILL,
        P065_BOOSTER_HILL_PRIZE_13,
        P066_BOOSTER_HILL_PRIZE_14,
        P067_BOMB_CHEST,
        P068_BOOSTER_HILL_PRIZE_15,
        P069_BOOSTER_HILL_PRIZE_STANDING_0,
        P070_EGG_CHEST,
        P071_BOOSTER_HILL_PRIZE_STANDING_1,
        P072_BOOSTER_HILL_PRIZE_STANDING_2,
        P073_COOKIE_CHEST,
        P074_BOOSTER_HILL_PRIZE_STANDING_3,
        P075_BOOSTER_HILL_PRIZE_STANDING_4,
        P076_BERRY_CHEST,
        P077_BOOSTER_HILL_PRIZE_STANDING_5,
        P078_BOOSTER_HILL_PRIZE_STANDING_6,
        P079_CARD_CHEST,
        P080_BOOSTER_HILL_PRIZE_STANDING_7,
        P081_BOOSTER_HILL_PRIZE_STANDING_8,
        P082_BOOSTER_HILL_PRIZE_STANDING_9,
        P083_BOOSTER_HILL_PRIZE_STANDING_10,
        P084_BOOSTER_HILL_PRIZE_STANDING_11,
        P085_BOOSTER_HILL_PRIZE_STANDING_12,
        P086_BOOSTER_HILL_PRIZE_STANDING_13,
        P087_BOOSTER_HILL_PRIZE_STANDING_14,
        P088_BOOSTER_HILL_PRIZE_STANDING_15,
        P089_BEETLE_CHEST,
        P090_SMALL_COIN_STILL,
        P091_CHEST_COIN_STILL,
        P092_GLOVE_CHEST,
        P093_CRYSTAL_CHEST,
        P094_FIRE_SPELL_CHEST,
        P095_BLUE_SPELL_CHEST,
        P096_GREEN_SPELL_CHEST,
        P097_YELLOW_SPELL_CHEST,
        P098_GRAY_SPELL_CHEST,
        P099_BAG_STATIC,
        P100_BOOSTER_HILL_PRIZE_11,
        P101_FLOWER_COLLECTION,
        P102_SMALL_FROG_COIN_STILL,
        P103_MIMIC_1_POOF_ON_DEFEAT,
        P104_MIMIC_2_POOF_ON_DEFEAT,
        P105_MARIO_DOLL,
        P106_MALLOW_DOLL,
        P107_GENO_DOLL,
        P108_TOADSTOOL_DOLL,
        P109_BOWSER_DOLL,
        P110_MOKURA_CHEST,
        P111_BLUE_CLOUD_CHEST,
        P112_JINX_CHEST,
        P113_CHOMP_CHEST,
        P114_STICK_CHEST,
        P115_HAMMER_CHEST,
        P116_AP_ITEM,
        P117_RED_SHELL_CHEST,
        P118_GREEN_SHELL_CHEST,
        P119_BAND_CHEST,
        P120_PAN_PACKET,
        P121_FAN_PACKET,
        P122_GUN_PACKET,
        P123_PANTS_PACKET,
        P124_OVERALLS_PACKET,
        P125_DRESS_PACKET,
        P126_CAPE_PACKET,
        P127_UNUSED,
        P128_UNUSED,
        P129_UNUSED,
        P130_UNUSED,
        P131_UNUSED,
        P132_UNUSED,
        P133_UNUSED,
        P134_UNUSED,
        P135_UNUSED,
        P136_UNUSED,
        P137_UNUSED,
        P138_UNUSED,
        P139_UNUSED,
        P140_UNUSED,
        P141_UNUSED,
        P142_UNUSED,
        P143_UNUSED,
        P144_UNUSED,
        P145_UNUSED,
        P146_UNUSED,
        P147_UNUSED,
        P148_UNUSED,
        P149_UNUSED,
        P150_UNUSED,
        P151_UNUSED,
        P152_UNUSED,
        P153_UNUSED,
        P154_UNUSED,
        P155_UNUSED,
        P156_UNUSED,
        P157_UNUSED,
        P158_UNUSED,
        P159_UNUSED,
        P160_UNUSED,
        P161_UNUSED,
        P162_UNUSED,
        P163_UNUSED,
        P164_UNUSED,
        P165_UNUSED,
        P166_UNUSED,
        P167_UNUSED,
        P168_UNUSED,
        P169_UNUSED,
        P170_UNUSED,
        P171_UNUSED,
        P172_UNUSED,
        P173_UNUSED,
        P174_UNUSED,
        P175_UNUSED,
        P176_UNUSED,
        P177_UNUSED,
        P178_UNUSED,
        P179_UNUSED,
        P180_UNUSED,
        P181_UNUSED,
        P182_UNUSED,
        P183_UNUSED,
        P184_UNUSED,
        P185_UNUSED,
        P186_UNUSED,
        P187_UNUSED,
        P188_UNUSED,
        P189_UNUSED,
        P190_UNUSED,
        P191_UNUSED,
        P192_UNUSED,
        P193_UNUSED,
        P194_UNUSED,
        P195_UNUSED,
        P196_UNUSED,
        P197_UNUSED,
        P198_UNUSED,
        P199_UNUSED,
        P200_UNUSED,
        P201_UNUSED,
        P202_UNUSED,
        P203_UNUSED,
        P204_UNUSED,
        P205_UNUSED,
        P206_UNUSED,
        P207_UNUSED,
        P208_UNUSED,
        P209_UNUSED,
        P210_UNUSED,
        P211_UNUSED,
        P212_UNUSED,
        P213_UNUSED,
        P214_UNUSED,
        P215_UNUSED,
        P216_UNUSED,
        P217_UNUSED,
        P218_UNUSED,
        P219_UNUSED,
        P220_UNUSED,
        P221_UNUSED,
        P222_UNUSED,
        P223_UNUSED,
        P224_UNUSED,
        P225_UNUSED,
        P226_UNUSED,
        P227_UNUSED,
        P228_UNUSED,
        P229_UNUSED,
        P230_UNUSED,
        P231_UNUSED,
        P232_UNUSED,
        P233_UNUSED,
        P234_UNUSED,
        P235_UNUSED,
        P236_UNUSED,
        P237_UNUSED,
        P238_UNUSED,
        P239_UNUSED,
        P240_UNUSED,
        P241_UNUSED,
        P242_UNUSED,
        P243_UNUSED,
        P244_UNUSED,
        P245_UNUSED,
        P246_UNUSED,
        P247_UNUSED,
        P248_UNUSED,
        P249_UNUSED,
        P250_UNUSED,
        P251_UNUSED,
        P252_UNUSED,
        P253_UNUSED,
        P254_UNUSED,
        P255_UNUSED,
    ]
)
