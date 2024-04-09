# pylint: disable=C0301

"""Individual item class definitions."""

from copy import deepcopy
from random import choice
from typing import List, Optional, Type

from randomizer.types.dialogs.ids import (
    DI2911_TREASURE_SELLER_ITEM_1,
    DI2908_TREASURE_SELLER_ITEM_2,
    DI2914_TREASURE_SELLER_ITEM_3,
)
from randomizer.types.items import (
    Coins,
    InvincibilityStar,
    Item,
    KeyItem,
    MarrymoreGear,
    MimicFightChestAssignment,
    MiscReward,
    RegularEquip,
    RegularItem,
    SpecialEquip,
    StarPiece,
    Weapon,
    Armor,
    Accessory,
    ProgressiveItem,
    EffectType,
    EquipStats,
    ItemShuffleType,
    ItemUnique,
    EQUIP_STATS,
)
from randomizer.types.npcs.objects.types import ItemNPC
from randomizer.types.npcs.objects import (
    Banana,
    Beetle,
    Berry,
    BigCoin,
    BlueBomb,
    BlueCandy,
    BlueMusicDrink,
    BlueSyrup,
    Card,
    ChompItem,
    Cookie,
    DDrink,
    Egg,
    Empty,
    Fan,
    FrogDrink,
    GreenBomb,
    GreenCandy,
    GreenJuice,
    GreenMushroom,
    GreenShell,
    GreenSyrup,
    Hammer as HammerNPC,
    FroggieStick as FroggieStickNPC,
    Key,
    MicroBombItem,
    Music,
    PDrink,
    RDrink,
    RedBomb,
    RedJuice,
    RedMushroom,
    RedMusicDrink,
    RedShell,
    Parasol as ParasolNPC,
    RedSyrup,
    SmallCoin,
    SmallFrogCoin,
    StarDrink,
    TinyStar,
    FryingPan as FryingPanNPC,
    Crown as CrownNPC,
    Shoes as ShoesNPC,
    Brooch as BroochNPC,
    Ring as RingNPC,
    Feather as FeatherNPC,
    YellowBomb,
    YellowMushroom,
    YellowMusicDrink,
    YellowSyrup,
    Flower as FlowerNPC,
    RecoveryMushroom as RecoveryMushroomNPC,
    FrogCoin as FrogCoinNPC,
)
from randomizer.types.numbers import UInt16, UInt8
from randomizer.types.overworld_scripts.arguments.types import Flag, PartyCharacter
from randomizer.types.overworld_scripts.arguments import (
    SIGNAL_RING_STAR_PIECE_1,
    SIGNAL_RING_STAR_PIECE_2,
    SIGNAL_RING_STAR_PIECE_3,
    SIGNAL_RING_STAR_PIECE_4,
    SIGNAL_RING_STAR_PIECE_5,
    SIGNAL_RING_STAR_PIECE_6,
    SIGNAL_RING_STAR_PIECE_7,
    MARIO,
    MALLOW,
    GENO,
    TOADSTOOL,
    BOWSER,
)
from randomizer.types.overworld_scripts.event_scripts.ids import (
    E0256_RETURN,
    E3081_YOU_MISSED,
    E0157_NPC_QUEST_GRANT_1_FROG_COIN,
    E0158_NPC_QUEST_GRANT_MULTI_FROG_COIN,
    E0161_NPC_QUEST_GRANT_BEETLEMANIA,
    E0162_CHEST_GRANT_BEETLEMANIA,
    E0184_NPC_QUEST_GRANT_SINGLE_FIREWORKS,
    E0185_NPC_QUEST_GRANT_PROGRESSIVE_FIREWORKS,
    E0242_CHEST_6_GRANT,
    E0243_CHEST_5_GRANT,
    E0244_CHEST_4_GRANT,
    E0245_CHEST_3_GRANT,
    E0246_CHEST_2_GRANT,
    E0397_HEAL_IN_TOADSTOOLS_ROOM,
    E1293_COLLECT_FREESTANDING_SMALL_COIN,
    E1801_FREESTANDING_FLOWER,
    E2493_MIMIC_3,
    E2816_ASYNC_NO_ANIMATION_FROG_COIN,
    E2817_ASYNC_NO_ANIMATION_FLOWER,
    E2818_ASYNC_NO_ANIMATION_10_COIN,
    E2819_ASYNC_NO_ANIMATION_1_COIN,
    E2822_ASYNC_NO_ANIMATION_MUSHROOM,
    E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
    E3074_COIN_CHEST_MULTI_HIT_1,
    E3082_FROG_COIN_CHEST_MULTI_HIT_1,
    E3086_JUICE_BAR_CARD_UPGRADE,
    E3087_PROGRESSIVE_EGG_UPGRADE,
    E3091_MULTI_FROG_COIN_CHEST_SINGLE_HIT,
    E3097_JUICE_BAR_CARD_NPC_GRANT,
    E3098_PROGRESSIVE_EGG_NPC_GRANT,
    E3099_SHUFFLE_FIREWORKS_CHEST_GRANT,
    E3100_PROGRESSIVE_FIREWORKS_CHEST_GRANT,
    E3109_FREESTANDING_BEETLEMANIA_GRANT,
    E3110_FREESTANDING_JUICE_BAR_CARD_GRANT,
    E3111_FREESTANDING_PROGRESSIVE_EGG_GRANT,
    E3112_FREESTANDING_SHUFFLE_FIREWORKS_GRANT,
    E3113_FREESTANDING_PROGRESSIVE_FIREWORKS_GRANT,
    E3124_MIMIC_1_CHEST,
    E3126_MIMIC_2_CHEST,
    E3146_FREESTANDING_BIG_COIN,
    E3238_FREESTANDING_FROG_COIN,
    E3395_MIDAS_CAVE_BEETLEMANIA_GRANTER,
    E3396_MIDAS_CAVE_PROGRESSIVE_CARD_GRANTER,
    E3397_MIDAS_CAVE_PROGRESSIVE_EGG_GRANTER,
    E3398_MIDAS_CAVE_SINGLE_FIREWORK_GRANTER,
    E3399_MIDAS_CAVE_PROGRESSIVE_FIREWORK_GRANTER,
    E3406_FROG_COIN_CHEST_MULTI_HIT_2,
    E3407_FROG_COIN_CHEST_MULTI_HIT_3,
    E3408_FROG_COIN_CHEST_MULTI_HIT_4,
    E3409_FROG_COIN_CHEST_MULTI_HIT_5,
    E3410_FROG_COIN_CHEST_MULTI_HIT_6,
    E3931_GET_SHOES,
    E3932_GET_BROOCH,
    E3933_GET_RING,
    E3934_GET_CROWN,
    E3935_FREESTANDING_SHOES,
    E3936_FREESTANDING_BROOCH,
    E3937_FREESTANDING_RING,
    E3938_FREESTANDING_CROWN,
    E3939_RIVER_SHOES,
    E3940_RIVER_BROOCH,
    E3941_RIVER_RING,
    E3942_RIVER_CROWN,
    E3943_SHOES_CHEST,
    E3944_BROOCH_CHEST,
    E3945_RING_CHEST,
    E3946_CROWN_CHEST,
)
from randomizer.types.spells import Element, Status, TempStatBuff
from randomizer.types.world import GameWorld
from randomizer.types.world.flags import (
    FireworksSetting,
    FireworksOptions,
    CasinoWarp,
    StarPieceHints,
)


class Hammer(Weapon, RegularEquip):
    """Hammer item class"""

    _item_id: int = 5
    _description: str = "Pounds\x01enemies"
    _tier: int = 1
    _order: int = 53
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 10
    _variance: int = 1
    _price: int = 70
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _model: Type[ItemNPC] = HammerNPC
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Hammer”!\n I'm not sure if it does anything\n else.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Hammer”.\n I'm not sure if it does anything\n else.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Hammer”.\n I'm not sure if it does anything\n else.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class FroggieStick(Weapon, SpecialEquip):
    """FroggieStick item class"""

    _item_id: int = 6
    _description: str = "Frogfucius\x01made it"
    _tier: int = 1
    _order: int = 67
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 20
    _variance: int = 2
    _price: int = 180
    _special_equip: bool = True
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _model: Type[ItemNPC] = FroggieStickNPC
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Caster's Staff”!\n It looks pretty good at bonking.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Caster's Staff”.\n It looks pretty good at bonking.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Caster's Staff”.\n It looks pretty good at bonking.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class NokNokShell(Weapon, RegularEquip):
    """NokNokShell item class"""

    _item_id: int = 7
    _description: str = "Kick to attack"
    _tier: int = 1
    _order: int = 58
    _equip_chars: List[PartyCharacter] = [MARIO]
    _model: Type[ItemNPC] = GreenShell
    _attack: int = 20
    _variance: int = 2
    _price: int = 20
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Green Shell”!\n There's no turtle inside of it.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Green Shell”.\n There's no turtle inside of it.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Green Shell”.\n There's no turtle inside of it.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class PunchGlove(Weapon, RegularEquip):
    """PunchGlove item class"""

    _item_id: int = 8
    _description: str = "Knock out\x01power!"
    _tier: int = 1
    _order: int = 48
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 30
    _variance: int = 3
    _price: int = 36


class FingerShot(Weapon, RegularEquip):
    """FingerShot item class"""

    _item_id: int = 9
    _description: str = "Fingers shoot\x01bullets"
    _tier: int = 1
    _order: int = 70
    _equip_chars: List[PartyCharacter] = [GENO]
    _attack: int = 12
    _variance: int = 3
    _price: int = 50


class Cymbals(Weapon, RegularEquip):
    """Cymbals item class"""

    _item_id: int = 10
    _description: str = "Scare enemies\x01with a clash"
    _tier: int = 1
    _order: int = 60
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 30
    _variance: int = 3
    _price: int = 42
    _model: Type[ItemNPC] = Music


class Chomp(Weapon, SpecialEquip):
    """Chomp item class"""

    _item_id: int = 11
    _description: str = "Just spin me\x01at an enemy!"
    _tier: int = 1
    _order: int = 64
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _attack: int = 10
    _variance: int = 4
    _price: int = 140
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _model: Type[ItemNPC] = ChompItem
    _special_equip: bool = True
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Chain Chomp”!\n It's hungry to stir up some trouble.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Chain Chomp”.\n It's hungry to stir up some trouble.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Chain Chomp”.\n It's hungry to stir up some trouble.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class Masher(Weapon, RegularEquip):
    """Masher item class"""

    _item_id: int = 12
    _description: str = "Makes monster\x01mash!"
    _tier: int = 4
    _order: int = 54
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 50
    _variance: int = 30
    _price: int = 160
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _model: Type[ItemNPC] = HammerNPC
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Hammer”!\n I'm not sure if it does anything\n else.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Hammer”.\n I'm not sure if it does anything\n else.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Hammer”.\n I'm not sure if it does anything\n else.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class ChompShell(Weapon, RegularEquip):
    """ChompShell item class"""

    _item_id: int = 13
    _description: str = "It~s a\x01Kinklink shell"
    _model: Type[ItemNPC] = ChompItem
    _tier: int = 1
    _order: int = 65
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _attack: int = 9
    _variance: int = 3
    _price: int = 60


class SuperHammer(Weapon, RegularEquip):
    """SuperHammer item class"""

    _item_id: int = 14
    _description: str = "The standard\x01for hammers!"
    _tier: int = 2
    _order: int = 55
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 40
    _variance: int = 4
    _price: int = 70
    _model: Type[ItemNPC] = HammerNPC


class HandGun(Weapon, RegularEquip):
    """HandGun item class"""

    _item_id: int = 15
    _description: str = "It packs a kick"
    _tier: int = 1
    _order: int = 72
    _equip_chars: List[PartyCharacter] = [GENO]
    _attack: int = 24
    _variance: int = 4
    _price: int = 75


class WhompGlove(Weapon, RegularEquip):
    """WhompGlove item class"""

    _item_id: int = 16
    _description: str = "The old double\x01whammie!"
    _tier: int = 2
    _order: int = 52
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 40
    _variance: int = 4
    _price: int = 72


class SlapGlove(Weapon, RegularEquip):
    """SlapGlove item class"""

    _item_id: int = 17
    _description: str = "It slaps ~em\x01silly"
    _tier: int = 2
    _order: int = 49
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _attack: int = 40
    _variance: int = 4
    _price: int = 100
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Little Glove”!\n You don't drink water out of it.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Little Glove”.\n You don't drink water out of it.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Little Glove”.\n You don't drink water out of it.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class TroopaShell(Weapon, RegularEquip):
    """TroopaShell item class"""

    _item_id: int = 18
    _description: str = "Kick with it!"
    _model: Type[ItemNPC] = RedShell
    _tier: int = 2
    _order: int = 59
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 50
    _variance: int = 5
    _price: int = 90


class Parasol(Weapon, RegularEquip):
    """Parasol item class"""

    _item_id: int = 19
    _description: str = "Inflicts\x01serious pain!"
    _model: Type[ItemNPC] = ParasolNPC
    _tier: int = 2
    _order: int = 68
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _attack: int = 50
    _variance: int = 5
    _price: int = 84


class HurlyGloves(Weapon, RegularEquip):
    """HurlyGloves item class"""

    _item_id: int = 20
    _description: str = "A classic\x01Mario}toss\x01attack"
    _tier: int = 1
    _order: int = 46
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _attack: int = 20
    _variance: int = 5
    _price: int = 92


class DoublePunch(Weapon, RegularEquip):
    """DoublePunch item class"""

    _item_id: int = 21
    _description: str = "A handy double\x01rocket punch"
    _tier: int = 2
    _order: int = 44
    _equip_chars: List[PartyCharacter] = [GENO]
    _attack: int = 35
    _variance: int = 5
    _price: int = 88


class RibbitStick(Weapon, RegularEquip):
    """RibbitStick item class"""

    _item_id: int = 22
    _description: str = "It~ll come\x01in handy"
    _model: Type[ItemNPC] = FroggieStickNPC
    _tier: int = 2
    _order: int = 69
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 50
    _variance: int = 5
    _price: int = 86


class SpikedLink(Weapon, RegularEquip):
    """SpikedLink item class"""

    _item_id: int = 23
    _description: str = "A studded ball\x01and chain!"
    _tier: int = 1
    _order: int = 66
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _model: Type[ItemNPC] = ChompItem
    _attack: int = 30
    _variance: int = 6
    _price: int = 94


class MegaGlove(Weapon, RegularEquip):
    """MegaGlove item class"""

    _item_id: int = 24
    _description: str = "Packs a mega\x01wallop!"
    _tier: int = 3
    _order: int = 47
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 60
    _variance: int = 6
    _price: int = 102


class WarFan(Weapon, RegularEquip):
    """WarFan item class"""

    _item_id: int = 25
    _description: str = "A mysterious\x01battle fan!"
    _model: Type[ItemNPC] = Fan
    _tier: int = 3
    _order: int = 63
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _attack: int = 60
    _variance: int = 6
    _price: int = 100


class HandCannon(Weapon, RegularEquip):
    """HandCannon item class"""

    _item_id: int = 26
    _description: str = "Shoots bullets\x01from elbow!"
    _tier: int = 2
    _order: int = 71
    _equip_chars: List[PartyCharacter] = [GENO]
    _attack: int = 45
    _variance: int = 6
    _price: int = 105


class StickyGlove(Weapon, RegularEquip):
    """StickyGlove item class"""

    _item_id: int = 27
    _description: str = "Launches a\x01punch attack."
    _tier: int = 3
    _order: int = 50
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 60
    _variance: int = 6
    _price: int = 98


class UltraHammer(Weapon, RegularEquip):
    """UltraHammer item class"""

    _item_id: int = 28
    _description: str = "The ultimate\x01hammer!"
    _tier: int = 3
    _order: int = 56
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 70
    _variance: int = 7
    _price: int = 115
    _model: Type[ItemNPC] = HammerNPC
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Hammer”!\n I'm not sure if it does anything\n else.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Hammer”.\n I'm not sure if it does anything\n else.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Hammer”.\n I'm not sure if it does anything\n else.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class SuperSlap(Weapon, RegularEquip):
    """SuperSlap item class"""

    _item_id: int = 29
    _description: str = "The Princess~\x01mega}slap!"
    _tier: int = 3
    _order: int = 51
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _attack: int = 70
    _variance: int = 7
    _price: int = 110
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Big Glove”!\n You don't drink water out of it.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Big Glove”.\n You don't drink water out of it.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Big Glove”.\n You don't drink water out of it.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class DrillClaw(Weapon, RegularEquip):
    """DrillClaw item class"""

    _item_id: int = 30
    _description: str = "A drilling\x01claw!"
    _tier: int = 2
    _order: int = 45
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _attack: int = 40
    _variance: int = 7
    _price: int = 118
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Drilling Appendage”!\n I bet you could do some real damage\n with this.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Drilling Appendage”.\n I bet you could do some real damage\n with this.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Drilling Appendage”.\n I bet you could do some real damage\n with this.[await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class StarGun(Weapon, RegularEquip):
    """StarGun item class"""

    _item_id: int = 31
    _description: str = "Try shooting\x01stars!"
    _tier: int = 3
    _order: int = 73
    _equip_chars: List[PartyCharacter] = [GENO]
    _model: Type[ItemNPC] = TinyStar
    _attack: int = 57
    _variance: int = 7
    _price: int = 120
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Celestial Launcher”!\n I bet you could do some real damage\n with this.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Celestial Launcher”.\n I bet you could do some real damage\n with this.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Celestial Launcher”.\n I bet you could do some real damage\n with this.[await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class SonicCymbal(Weapon, RegularEquip):
    """SonicCymbal item class"""

    _item_id: int = 32
    _description: str = "Puts noise to\x01work for you!"
    _tier: int = 3
    _order: int = 61
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 70
    _variance: int = 7
    _price: int = 108
    _model: Type[ItemNPC] = Music
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Psych Percussion”!\n This could catch monsters\n off-guard.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Psych Percussion”.\n This could catch monsters\n off-guard.[await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Psych Percussion”.\n This could catch monsters\n off-guard.[await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class LazyShellWeapon(Weapon, SpecialEquip):
    """LazyShellWeapon item class"""

    _item_id: int = 33
    _description: str = "Toss a shell\x01at an enemy!"
    _model: Type[ItemNPC] = RedShell
    _tier: int = 4
    _order: int = 57
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 90
    _variance: int = 40
    _price: int = 200
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _special_equip: bool = True
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: An “Oversized Shell”!\n You could do some real damage\n with this.[await][await] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: An “Oversized Shell”.\n You could do some real damage\n with this.[await][await] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: An “Oversized Shell”.\n You could do some real damage\n with this.[await][await] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class FryingPan(Weapon, RegularEquip):
    """FryingPan item class"""

    _item_id: int = 34
    _description: str = "Enough iron to\x01be dangerous!"
    _model: Type[ItemNPC] = FryingPanNPC
    _tier: int = 4
    _order: int = 62
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _attack: int = 90
    _variance: int = 20
    _price: int = 300
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Metal Plate”![await]\n Don't know what it’s used for,\n but I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Metal Plate”.[await]\n Don't know what it’s used for,\n but it's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Metal Plate”.[await]\n Don't know what it’s used for,\n but I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class LuckyHammer(Weapon, RegularEquip):
    """LuckyHammer item class"""

    _item_id: int = 35
    _description: str = "A lucky hammer!"
    _tier: int = 1
    _order: int = 54
    _equip_chars: List[PartyCharacter] = [MARIO]
    _price: int = 123
    _model: Type[ItemNPC] = HammerNPC


class Shirt(Armor, RegularEquip):
    """Shirt item class"""

    _item_id: int = 37
    _description: str = "It~s a\x01shirt!"
    _tier: int = 1
    _order: int = 102
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 6
    _magic_defense: int = 6
    _price: int = 7


class Pants(Armor, RegularEquip):
    """Pants item class"""

    _item_id: int = 38
    _description: str = "It~s a pair\x01of pants!"
    _tier: int = 1
    _order: int = 95
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 6
    _magic_defense: int = 3
    _price: int = 7


class ThickShirt(Armor, RegularEquip):
    """ThickShirt item class"""

    _item_id: int = 39
    _description: str = "A padded shirt"
    _tier: int = 1
    _order: int = 106
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 12
    _magic_defense: int = 8
    _price: int = 14


class ThickPants(Armor, RegularEquip):
    """ThickPants item class"""

    _item_id: int = 40
    _description: str = "Padded pants"
    _tier: int = 1
    _order: int = 105
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 12
    _magic_defense: int = 6
    _price: int = 14


class MegaShirt(Armor, RegularEquip):
    """MegaShirt item class"""

    _item_id: int = 41
    _description: str = "Durable stay}\x01pressed shirt"
    _tier: int = 1
    _order: int = 93
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 18
    _magic_defense: int = 10
    _price: int = 22


class MegaPants(Armor, RegularEquip):
    """MegaPants item class"""

    _item_id: int = 42
    _description: str = "Durable work\x01pants"
    _tier: int = 1
    _order: int = 92
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 18
    _magic_defense: int = 9
    _price: int = 22


class WorkPants(Armor, RegularEquip):
    """WorkPants item class"""

    _item_id: int = 43
    _description: str = "Sweaty\x01work pants!"
    _tier: int = 1
    _order: int = 107
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 5
    _attack: int = 10
    _defense: int = 15
    _magic_attack: int = 10
    _magic_defense: int = 5
    _price: int = 22

    @property
    def primary_stats(self) -> List[EquipStats]:
        """Primary stats of this item, depending on the type."""
        return deepcopy(EQUIP_STATS)


class MegaCape(Armor, RegularEquip):
    """MegaCape item class"""

    _item_id: int = 44
    _description: str = "Durable\x01pressed cape"
    _tier: int = 1
    _order: int = 91
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 6
    _magic_defense: int = 3
    _price: int = 22


class HappyShirt(Armor, RegularEquip):
    """HappyShirt item class"""

    _item_id: int = 45
    _description: str = "A lucky shirt"
    _tier: int = 1
    _order: int = 87
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 38


class HappyPants(Armor, RegularEquip):
    """HappyPants item class"""

    _item_id: int = 46
    _description: str = "A lucky\x01pair of pants"
    _tier: int = 1
    _order: int = 85
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 38


class HappyCape(Armor, RegularEquip):
    """HappyCape item class"""

    _item_id: int = 47
    _description: str = "A lucky cape"
    _tier: int = 1
    _order: int = 84
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 12
    _magic_defense: int = 6
    _price: int = 38


class HappyShell(Armor, RegularEquip):
    """HappyShell item class"""

    _item_id: int = 48
    _description: str = "A lucky shell"
    _model: Type[ItemNPC] = GreenShell
    _tier: int = 1
    _order: int = 86
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _defense: int = 6
    _magic_defense: int = 3
    _price: int = 38


class PolkaDress(Armor, RegularEquip):
    """PolkaDress item class"""

    _item_id: int = 49
    _description: str = "A flashy dress"
    _tier: int = 1
    _order: int = 96
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 160
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Casual Gown”!\n It's pink with little polka dots![await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Casual Gown”.\n It's pink with little polka dots![await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Casual Gown”.\n It's pink with little polka dots![await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class SailorShirt(Armor, RegularEquip):
    """SailorShirt item class"""

    _item_id: int = 50
    _description: str = "A sailor~s\x01suit"
    _tier: int = 1
    _order: int = 101
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 30
    _magic_defense: int = 15
    _price: int = 50


class SailorPants(Armor, RegularEquip):
    """SailorPants item class"""

    _item_id: int = 51
    _description: str = "A sailor~s\x01pants"
    _tier: int = 1
    _order: int = 100
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 30
    _magic_defense: int = 15
    _price: int = 50


class SailorCape(Armor, RegularEquip):
    """SailorCape item class"""

    _item_id: int = 52
    _description: str = "A sailor~s\x01cape"
    _tier: int = 1
    _order: int = 99
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 18
    _magic_defense: int = 9
    _price: int = 50


class NauticaDress(Armor, RegularEquip):
    """NauticaDress item class"""

    _item_id: int = 53
    _description: str = "A female\x01sailor~s dress"
    _tier: int = 1
    _order: int = 94
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _defense: int = 30
    _magic_defense: int = 15
    _price: int = 50


class CourageShell(Armor, RegularEquip):
    """CourageShell item class"""

    _item_id: int = 54
    _description: str = "A stout shell"
    _model: Type[ItemNPC] = GreenShell
    _tier: int = 1
    _order: int = 74
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _defense: int = 12
    _magic_defense: int = 6
    _price: int = 60


class FuzzyShirt(Armor, RegularEquip):
    """FuzzyShirt item class"""

    _item_id: int = 55
    _description: str = "A fuzzy shirt"
    _tier: int = 2
    _order: int = 83
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 36
    _magic_defense: int = 18
    _price: int = 70


class FuzzyPants(Armor, RegularEquip):
    """FuzzyPants item class"""

    _item_id: int = 56
    _description: str = "Fuzzy pants"
    _tier: int = 2
    _order: int = 82
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 36
    _magic_defense: int = 18
    _price: int = 70


class FuzzyCape(Armor, RegularEquip):
    """FuzzyCape item class"""

    _item_id: int = 57
    _description: str = "A fuzzy cape"
    _tier: int = 1
    _order: int = 80
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 70


class FuzzyDress(Armor, RegularEquip):
    """FuzzyDress item class"""

    _item_id: int = 58
    _description: str = "A fuzzy dress"
    _tier: int = 2
    _order: int = 81
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _defense: int = 36
    _magic_defense: int = 18
    _price: int = 70


class FireShirt(Armor, RegularEquip):
    """FireShirt item class"""

    _item_id: int = 59
    _description: str = "Determined\x01person~s shirt"
    _tier: int = 2
    _order: int = 79
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 42
    _magic_defense: int = 21
    _price: int = 90


class FirePants(Armor, RegularEquip):
    """FirePants item class"""

    _item_id: int = 60
    _description: str = "Determined\x01person~s pants"
    _tier: int = 2
    _order: int = 77
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 42
    _magic_defense: int = 21
    _price: int = 90
    _elemental_immunities: List[Element] = []


class FireCape(Armor, RegularEquip):
    """FireCape item class"""

    _item_id: int = 61
    _description: str = "Determined\x01person~s cape"
    _tier: int = 1
    _order: int = 75
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 30
    _magic_defense: int = 15
    _price: int = 90


class FireShell(Armor, RegularEquip):
    """FireShell item class"""

    _item_id: int = 62
    _description: str = "Determined\x01person~s shell"
    _model: Type[ItemNPC] = RedShell
    _tier: int = 1
    _order: int = 78
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _defense: int = 18
    _magic_defense: int = 9
    _price: int = 90


class FireDress(Armor, RegularEquip):
    """FireDress item class"""

    _item_id: int = 63
    _description: str = "Determined\x01woman~s dress"
    _tier: int = 2
    _order: int = 76
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _defense: int = 42
    _magic_defense: int = 21
    _price: int = 90


class HeroShirt(Armor, RegularEquip):
    """HeroShirt item class"""

    _item_id: int = 64
    _description: str = "A legendary\x01shirt."
    _tier: int = 3
    _order: int = 89
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 48
    _magic_defense: int = 24
    _price: int = 100


class PrincePants(Armor, RegularEquip):
    """PrincePants item class"""

    _item_id: int = 65
    _description: str = "Legendary\x01pants!"
    _tier: int = 3
    _order: int = 97
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 48
    _magic_defense: int = 24
    _price: int = 100
    _model: Type[ItemNPC] = CrownNPC


class StarCape(Armor, RegularEquip):
    """StarCape item class"""

    _item_id: int = 66
    _description: str = "A legendary\x01cape."
    _model: Type[ItemNPC] = TinyStar
    _tier: int = 2
    _order: int = 103
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 36
    _magic_defense: int = 18
    _price: int = 100


class HealShell(Armor, RegularEquip):
    """HealShell item class"""

    _item_id: int = 67
    _description: str = "A legendary\x01shell."
    _model: Type[ItemNPC] = GreenShell
    _tier: int = 1
    _order: int = 88
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 100


class RoyalDress(Armor, RegularEquip):
    """RoyalDress item class"""

    _item_id: int = 68
    _description: str = "A legendary\x01dress!"
    _tier: int = 3
    _order: int = 98
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _defense: int = 48
    _magic_defense: int = 24
    _price: int = 100
    _model: Type[ItemNPC] = CrownNPC


class SuperSuit(Armor, SpecialEquip):
    """SuperSuit item class"""

    _item_id: int = 69
    _description: str = "A truly fine\x01suit!"
    _tier: int = 4
    _order: int = 104
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 30
    _attack: int = 50
    _defense: int = 50
    _magic_attack: int = 50
    _magic_defense: int = 50
    _elemental_immunities: List[Element] = [
        Element.ICE,
        Element.FIRE,
        Element.THUNDER,
        Element.JUMP,
    ]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
        Status.BERSERK,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _price: int = 700
    _special_equip: bool = True
    _original_effect_type: EffectType = EffectType.ELEMENTAL_IMMUNITY
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Jumpsuit”!\n It looks pretty powerful, right?[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Jumpsuit”.\n It looks pretty powerful, right?[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Jumpsuit”.\n It looks pretty powerful, right?[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }

    @property
    def primary_stats(self) -> List[EquipStats]:
        """Primary stats of this item, depending on the type."""
        return EQUIP_STATS


class LazyShellArmor(Armor, SpecialEquip):
    """LazyShellArmor item class"""

    _item_id: int = 70
    _description: str = "A stout and\x01durable shell."
    _model: Type[ItemNPC] = RedShell
    _tier: int = 4
    _order: int = 90
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = -50
    _attack: int = -50
    _defense: int = 127
    _magic_attack: int = -50
    _magic_defense: int = 127
    _elemental_immunities: List[Element] = [
        Element.ICE,
        Element.FIRE,
        Element.THUNDER,
        Element.JUMP,
    ]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
        Status.BERSERK,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _special_equip: bool = True
    _price: int = 222
    _original_effect_type: EffectType = EffectType.ELEMENTAL_IMMUNITY
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: An “Oversized Shell”!\n It's quite beefy and protective.[await]\n I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: An “Oversized Shell”.\n It's quite beefy and protective.[await]\n It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: An “Oversized Shell”.\n It's quite beefy and protective.[await]\n I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class ZoomShoes(Accessory, SpecialEquip):
    """ZoomShoes item class"""

    _item_id: int = 74
    _description: str = "Speed up by 10!"
    _tier: int = 1
    _order: int = 128
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 10
    _defense: int = 5
    _magic_defense: int = 5
    _price: int = 100
    _model: Type[ItemNPC] = ShoesNPC
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _special_equip: bool = True
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: “Pegasus Boots”!\n These will make you fast like Sonic![await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: “Pegasus Boots”.\n These will make you fast like Sonic![await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: “Pegasus Boots”.\n These will make you fast like Sonic![await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }

    @property
    def primary_stats(self) -> List[EquipStats]:
        """Primary stats of this item, depending on the type."""
        return [EquipStats.SPEED]


class SafetyBadge(Accessory, RegularEquip):
    """SafetyBadge item class"""

    _item_id: int = 75
    _description: str = "Prevents Mute \x9c\x01Poison attacks"
    _tier: int = 2
    _order: int = 121
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _defense: int = 5
    _magic_defense: int = 5
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
        Status.BERSERK,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _price: int = 500
    _original_effect_type: EffectType = EffectType.STATUS_PROTECTION
    _model: Type[ItemNPC] = BroochNPC
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Status Protector”!\n It can prevent weird things from\n happening to you.[await][pause] I'll sell it to\n you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Status Protector”.\n It can prevent weird things from\n happening to you.[await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Status Protector”.\n It can prevent weird things from\n happening to you.[await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class JumpShoes(Accessory, RegularEquip):
    """JumpShoes item class"""

    _item_id: int = 76
    _description: str = "Use jump attacks\x01against any foe"
    _tier: int = 1
    _order: int = 118
    _equip_chars: List[PartyCharacter] = [MARIO]
    _speed: int = 2
    _defense: int = 1
    _magic_attack: int = 5
    _magic_defense: int = 1
    _price: int = 30
    _model: Type[ItemNPC] = ShoesNPC
    _arbitrary_value: UInt16 = UInt16(1)


class SafetyRing(Accessory, RegularEquip):
    """SafetyRing item class"""

    _item_id: int = 77
    _description: str = "Guards against\x01mortal blows."
    _tier: int = 4
    _order: int = 122
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 5
    _defense: int = 5
    _magic_defense: int = 5
    _prevent_ko: bool = True
    _elemental_immunities: List[Element] = [
        Element.ICE,
        Element.FIRE,
        Element.THUNDER,
        Element.JUMP,
    ]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
        Status.BERSERK,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _price: int = 800
    _original_effect_type: EffectType = EffectType.ELEMENTAL_IMMUNITY
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _model: Type[ItemNPC] = RingNPC
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Protective Charm”!\n Never go into battle without it.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Protective Charm”.\n Never go into battle without it.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Protective Charm”.\n Never go into battle without it.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class Amulet(Accessory, RegularEquip):
    """Amulet item class"""

    _item_id: int = 78
    _description: str = "Great item,\x01bad smell!"
    _tier: int = 2
    _order: int = 108
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = -5
    _attack: int = 7
    _defense: int = 7
    _magic_attack: int = 7
    _magic_defense: int = 7
    _elemental_resistances: List[Element] = [
        Element.ICE,
        Element.FIRE,
        Element.THUNDER,
        Element.JUMP,
    ]
    _price: int = 200
    _original_effect_type: EffectType = EffectType.ELEMENTAL_RESISTANCE
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _model: Type[ItemNPC] = BroochNPC
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Stinky Charm”!\n It'll help you weather the elements.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Stinky Charm”.\n It'll help you weather the elements.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Stinky Charm”.\n It'll help you weather the elements.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class ScroogeRing(Accessory, RegularEquip):
    """ScroogeRing item class"""

    _item_id: int = 79
    _description: str = "Cuts FP use\x01in half\x01during battle"
    _tier: int = 1
    _order: int = 123
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _price: int = 50
    _frog_coin_item: bool = True
    _model: Type[ItemNPC] = RingNPC
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Mage Totem”!\n It might help with spellcasting.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Mage Totem”.\n It might help with spellcasting.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Mage Totem”.\n It might help with spellcasting.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }
    _arbitrary_value: UInt16 = UInt16(1)


class ExpBooster(Accessory, RegularEquip):
    """ExpBooster item class"""

    _item_id: int = 80
    _description: str = "Doubles Exp.\x01when equipped"
    _tier: int = 4
    _order: int = 113
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _price: int = 22
    _frog_coin_item: bool = True
    _original_effect_type: EffectType = EffectType.FEW_EFFECTS
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Training Device”!\n This'll make you strong in no time![await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Training Device”.\n This'll make you strong in no time![await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Training Device”.\n This'll make you strong in no time![await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }
    _arbitrary_value: UInt16 = UInt16(10)


class AttackScarf(Accessory, SpecialEquip):
    """AttackScarf item class"""

    _item_id: int = 81
    _description: str = "So comfy it~ll\x01make you jump!"
    _tier: int = 4
    _order: int = 110
    _equip_chars: List[PartyCharacter] = [MARIO]
    _speed: int = 30
    _attack: int = 30
    _defense: int = 30
    _magic_attack: int = 30
    _magic_defense: int = 30
    _prevent_ko: bool = True
    _price: int = 1500
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _special_equip: bool = True
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Jumper's Scarf”!\n It could save your life![await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Jumper's Scarf”.\n It could save your life![await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Jumper's Scarf”.\n It could save your life![await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class RareScarf(Accessory, RegularEquip):
    """RareScarf item class"""

    _item_id: int = 82
    _description: str = "Raises defense\x01power!"
    _tier: int = 1
    _order: int = 120
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _defense: int = 15
    _magic_defense: int = 15
    _price: int = 150
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: An “Unusual Garment”!\n I don't see these around often.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: An “Unusual Garment”.\n I don't see these around often.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: An “Unusual Garment”.\n I don't see these around often.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }

    @property
    def primary_stats(self) -> List[EquipStats]:
        """Primary stats of this item, depending on the type."""
        return [EquipStats.DEFENSE, EquipStats.MAGIC_DEFENSE]


class BtubRing(Accessory, RegularEquip):
    """BtubRing item class"""

    _item_id: int = 83
    _description: str = "You~ll win her\x01heart with this!"
    _tier: int = 1
    _order: int = 111
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _elemental_resistances: List[Element] = [
        Element.ICE,
        Element.FIRE,
        Element.THUNDER,
        Element.JUMP,
    ]
    _price: int = 145
    _model: Type[ItemNPC] = RingNPC
    _arbitrary_value: UInt16 = UInt16(1)


class AntidotePin(Accessory, RegularEquip):
    """AntidotePin item class"""

    _item_id: int = 84
    _description: str = "Prevents\x01poison damage"
    _tier: int = 1
    _order: int = 109
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _defense: int = 2
    _magic_defense: int = 2
    _status_immunities: List[Status] = [Status.POISON]
    _price: int = 28
    _original_effect_type: EffectType = EffectType.STATUS_PROTECTION
    _model: Type[ItemNPC] = BroochNPC


class WakeUpPin(Accessory, RegularEquip):
    """WakeUpPin item class"""

    _item_id: int = 85
    _description: str = "Prevents Mute \x9c\x01Sleep attacks"
    _tier: int = 1
    _order: int = 127
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _defense: int = 3
    _magic_defense: int = 3
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
    ]
    _price: int = 42
    _original_effect_type: EffectType = EffectType.STATUS_PROTECTION
    _model: Type[ItemNPC] = BroochNPC


class FearlessPin(Accessory, RegularEquip):
    """FearlessPin item class"""

    _item_id: int = 86
    _description: str = "Prevents Fear\x01attacks"
    _tier: int = 1
    _order: int = 114
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _defense: int = 5
    _magic_defense: int = 5
    _status_immunities: List[Status] = [Status.FEAR]
    _price: int = 130
    _original_effect_type: EffectType = EffectType.STATUS_PROTECTION
    _model: Type[ItemNPC] = BroochNPC


class TrueformPin(Accessory, RegularEquip):
    """TrueformPin item class"""

    _item_id: int = 87
    _description: str = "You won~t be\x01turned into\x01Mushrooms or\x01Scarecrows!"
    _tier: int = 1
    _order: int = 126
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _defense: int = 4
    _magic_defense: int = 4
    _status_immunities: List[Status] = [
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _price: int = 60
    _original_effect_type: EffectType = EffectType.STATUS_PROTECTION
    _model: Type[ItemNPC] = BroochNPC


class CoinTrick(Accessory, RegularEquip):
    """CoinTrick item class"""

    _item_id: int = 88
    _description: str = "Doubles the\x01coins you win\x01in battle"
    _tier: int = 1
    _order: int = 112
    _equip_chars: List[PartyCharacter] = [MARIO]
    _price: int = 36
    _frog_coin_item: bool = True
    _original_effect_type: EffectType = EffectType.FEW_EFFECTS
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Fortune Charm”!\n It's sure to make you very rich.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Fortune Charm”.\n It's sure to make you very rich.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Fortune Charm”.\n It's sure to make you very rich.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }
    _arbitrary_value: UInt16 = UInt16(2)


class GhostMedal(Accessory, SpecialEquip):
    """GhostMedal item class"""

    _item_id: int = 89
    _description: str = "Raises defense\x01while attacking"
    _tier: int = 2
    _order: int = 116
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _temp_buffs: List[TempStatBuff] = [
        TempStatBuff.DEFENSE,
        TempStatBuff.MAGIC_DEFENSE,
    ]
    _price: int = 1600
    _original_effect_type: EffectType = EffectType.BUFFS
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _special_equip: bool = True
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Scavenger's Prize”!\n It resembles a medal of honor.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Scavenger's Prize”.\n It resembles a medal of honor.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Scavenger's Prize”.\n It resembles a medal of honor.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class JinxBelt(Accessory, SpecialEquip):
    """JinxBelt item class"""

    _item_id: int = 90
    _description: str = "Jinx~s emblem\x01of power!"
    _tier: int = 4
    _order: int = 117
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 12
    _attack: int = 27
    _defense: int = 27
    _prevent_ko: bool = True
    _special_equip: bool = True
    _price: int = 1998
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Martial Sash”!\n A true fighter would love this.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Martial Sash”.\n A true fighter would love this.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Martial Sash”.\n A true fighter would love this.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class Feather(Accessory, RegularEquip):
    """Feather item class"""

    _item_id: int = 91
    _description: str = "Speed up by 20"
    _tier: int = 1
    _order: int = 115
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 20
    _defense: int = 5
    _magic_defense: int = 5
    _price: int = 666
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _model: Type[ItemNPC] = FeatherNPC
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Fluttering Quill”!\n It's pretty exotic, isn't it?[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Fluttering Quill”.\n It's pretty exotic, isn't it?[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Fluttering Quill”.\n It's pretty exotic, isn't it?[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }

    @property
    def primary_stats(self) -> List[EquipStats]:
        """Primary stats of this item, depending on the type."""
        return [EquipStats.SPEED]


class TroopaPin(Accessory, RegularEquip):
    """TroopaPin item class"""

    _item_id: int = 92
    _description: str = 'Grants "Troopa#\x01confidence!'
    _tier: int = 2
    _order: int = 125
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 20
    _temp_buffs: List[TempStatBuff] = [
        TempStatBuff.ATTACK,
        TempStatBuff.MAGIC_ATTACK,
    ]
    _price: int = 1000
    _original_effect_type: EffectType = EffectType.BUFFS
    _model: Type[ItemNPC] = BroochNPC
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Military Decoration”!\n I wonder what powers it bestows?[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Military Decoration”.\n I wonder what powers it bestows?[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Military Decoration”.\n I wonder what powers it bestows?[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class SignalRing(Accessory, RegularEquip):
    """SignalRing item class"""

    _item_id: int = 93
    _description: str = "Noise indicates\x01a hidden chest."
    _tier: int = 1
    _order: int = 124
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 10
    _price: int = 600
    _model: Type[ItemNPC] = RingNPC
    _unique: ItemUnique = ItemUnique.ALWAYS
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Treasure Beacon”!\n I wonder what it can help you find?[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Treasure Beacon”.\n I wonder what it can help you find?[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Treasure Beacon”.\n I wonder what it can help you find?[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }

    @property
    def arbitrary_value(self) -> UInt16:
        if self.world is not None and self.world.settings.is_boolean_flag_enabled(
            StarPieceHints
        ):
            return UInt16(10)
        return UInt16(1)

    def set_tier(self, tier: int = 1):
        # Make this a top tier item if signal ring hints are turned on
        if self.world is not None and self.world.settings.is_boolean_flag_enabled(
            StarPieceHints
        ):
            super().set_tier(4)
        else:
            super().set_tier(tier)

    def __init__(self, world: Optional[GameWorld] = None):
        super().__init__(world)
        self.set_tier()


class QuartzCharm(Accessory, SpecialEquip):
    """QuartzCharm item class"""

    _item_id: int = 94
    _description: str = "Shining source\x01of power!"
    _tier: int = 4
    _order: int = 119
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _prevent_ko: bool = True
    _temp_buffs: List[TempStatBuff] = [
        TempStatBuff.ATTACK,
        TempStatBuff.MAGIC_ATTACK,
        TempStatBuff.DEFENSE,
        TempStatBuff.MAGIC_DEFENSE,
    ]
    _price: int = 7
    _original_effect_type: EffectType = EffectType.BUFFS
    _model: Type[ItemNPC] = RingNPC
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _special_equip: bool = True
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Crystal Ring”!\n It could save your life![await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Crystal Ring”.\n It could save your life![await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Crystal Ring”.\n It could save your life![await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class Mushroom(RegularItem):
    """Mushroom item class"""

    _item_id: int = 96
    _description: str = "Recovers 30 HP"
    _order: int = 15
    _consumable: bool = True
    _price: int = 4
    _tier: int = 1
    _model: Type[ItemNPC] = RedMushroom
    _room_service: str = "Mushroom........"


class MidMushroom(RegularItem):
    """MidMushroom item class"""

    _item_id: int = 97
    _description: str = "Recovers 80 HP"
    _order: int = 13
    _consumable: bool = True
    _price: int = 20
    _tier: int = 2
    _model: Type[ItemNPC] = GreenMushroom
    _room_service: str = "Mid Mushroom...."


class MaxMushroom(RegularItem):
    """MaxMushroom item class"""

    _item_id: int = 98
    _description: str = "Recovers all HP"
    _order: int = 11
    _consumable: bool = True
    _price: int = 78
    _tier: int = 3
    _model: Type[ItemNPC] = YellowMushroom
    _room_service: str = "Max Mushroom...."


class HoneySyrup(RegularItem):
    """HoneySyrup item class"""

    _item_id: int = 99
    _description: str = "Recovers 10 FP"
    _model: Type[ItemNPC] = RedSyrup
    _order: int = 8
    _consumable: bool = True
    _price: int = 10
    _tier: int = 1
    _room_service: str = "Honey Syrup......"


class MapleSyrup(RegularItem):
    """MapleSyrup item class"""

    _item_id: int = 100
    _description: str = "Recovers 40 FP"
    _model: Type[ItemNPC] = GreenSyrup
    _order: int = 10
    _consumable: bool = True
    _price: int = 30
    _tier: int = 2
    _room_service: str = "Maple Syrup......"


class RoyalSyrup(RegularItem):
    """RoyalSyrup item class"""

    _item_id: int = 101
    _description: str = "Recovers all FP"
    _model: Type[ItemNPC] = YellowSyrup
    _order: int = 21
    _consumable: bool = True
    _price: int = 101
    _tier: int = 3
    _room_service: str = "Royal Syrup......"


class PickMeUp(RegularItem):
    """PickMeUp item class"""

    _item_id: int = 102
    _description: str = "Revives downed\x01allies"
    _order: int = 17
    _consumable: bool = True
    _price: int = 5
    _tier: int = 1
    _room_service: str = "Pick Me Up......."
    _model: Type[ItemNPC] = StarDrink


class AbleJuice(RegularItem):
    """AbleJuice item class"""

    _item_id: int = 103
    _description: str = "Heal status\x01ailments"
    _model: Type[ItemNPC] = RDrink
    _consumable: bool = True
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
        Status.BERSERK,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _price: int = 4
    _tier: int = 1
    _room_service: str = "Able Juice........"


class Bracer(RegularItem):
    """Bracer item class"""

    _item_id: int = 104
    _description: str = "Raises ally~s\x01def. in battle"
    _order: int = 2
    _consumable: bool = True
    _temp_buffs: List[TempStatBuff] = [
        TempStatBuff.DEFENSE,
        TempStatBuff.MAGIC_DEFENSE,
    ]
    _price: int = 50
    _frog_coin_item: bool = True
    _tier: int = 2
    _rank_value: int = 10
    _room_service: str = "Bracer..........."
    _model: Type[ItemNPC] = DDrink


class Energizer(RegularItem):
    """Energizer item class"""

    _item_id: int = 105
    _description: str = "Raises ally~s\x01battle power\x01during battle"
    _order: int = 5
    _consumable: bool = True
    _temp_buffs: List[TempStatBuff] = [
        TempStatBuff.ATTACK,
        TempStatBuff.MAGIC_ATTACK,
    ]
    _price: int = 50
    _frog_coin_item: bool = True
    _tier: int = 2
    _room_service: str = "Energizer........"
    _model: Type[ItemNPC] = PDrink


class YoshiAde(RegularItem):
    """YoshiAde item class"""

    _item_id: int = 106
    _description: str = "Power raised\x01during battle"
    _model: Type[ItemNPC] = GreenJuice
    _order: int = 23
    _consumable: bool = True
    _temp_buffs: List[TempStatBuff] = [
        TempStatBuff.ATTACK,
        TempStatBuff.MAGIC_ATTACK,
        TempStatBuff.DEFENSE,
        TempStatBuff.MAGIC_DEFENSE,
    ]
    _price: int = 200
    _tier: int = 3
    _room_service: str = "Yoshi Ade........"


class RedEssence(RegularItem):
    """RedEssence item class"""

    _item_id: int = 107
    _description: str = "Become invincible\x01for 3 turns"
    _model: Type[ItemNPC] = RedJuice
    _order: int = 19
    _consumable: bool = True
    _status_immunities: List[Status] = [Status.INVINCIBLE]
    _price: int = 400
    _tier: int = 4
    _room_service: str = "Red Essence......"


class KerokeroCola(RegularItem):
    """KerokeroCola item class"""

    _item_id: int = 108
    _description: str = "All members\x01recover fully"
    _order: int = 9
    _consumable: bool = True
    _price: int = 400
    _tier: int = 4
    _room_service: str = "KerokeroCola....."
    _model: Type[ItemNPC] = FrogDrink


class YoshiCookie(RegularItem):
    """YoshiCookie item class"""

    _item_id: int = 109
    _description: str = "Summons Yoshi\x01during battle"
    _order: int = 26
    _consumable: bool = True
    _price: int = 100
    _model: Type[ItemNPC] = Cookie
    _tier: int = 1
    _room_service: str = "Yoshi Cookie......"


class PureWater(RegularItem):
    """PureWater item class"""

    _item_id: int = 110
    _description: str = "Defeats ghosts\x01in a wink"
    _model: Type[ItemNPC] = BlueSyrup
    _order: int = 30
    _consumable: bool = True
    _price: int = 150
    _tier: int = 1
    _room_service: str = "Pure Water......."


class SleepyBomb(RegularItem):
    """SleepyBomb item class"""

    _item_name: str = "Sleepy Bomb"
    _item_id: int = 111
    _description: str = "Puts enemies\x01to sleep"
    _order: int = 32
    _consumable: bool = True
    _status_immunities: List[Status] = [Status.SLEEP]
    _model: Type[ItemNPC] = YellowBomb
    _price: int = 25
    _frog_coin_item: bool = True
    _tier: int = 1
    _room_service: str = "Sleepy Bomb......"


class BadMushroom(RegularItem):
    """BadMushroom item class"""

    _item_name: str = "Bad Mushroom"
    _item_id: int = 112
    _description: str = "Poisons\x01an enemy"
    _order: int = 1
    _consumable: bool = True
    _status_immunities: List[Status] = [Status.MUSHROOM]
    _price: int = 30
    _tier: int = 2
    _model: Type[ItemNPC] = RedMushroom
    _room_service: str = "Bad Mushroom...."


class FireBomb(RegularItem):
    """FireBomb item class"""

    _item_name: str = "Fire Bomb"
    _item_id: int = 113
    _description: str = "Hit all\x01enemies w/fire"
    _model: Type[ItemNPC] = RedBomb
    _order: int = 27
    _consumable: bool = True
    _price: int = 200
    _tier: int = 3
    _room_service: str = "Fire Bomb........."


class IceBomb(RegularItem):
    """IceBomb item class"""

    _item_name: str = "Ice Bomb"
    _item_id: int = 114
    _description: str = "Hit all\x01enemies w/ice"
    _model: Type[ItemNPC] = BlueBomb
    _order: int = 29
    _consumable: bool = True
    _price: int = 250
    _tier: int = 3
    _room_service: str = "Ice Bomb.........."


class FlowerTab(RegularItem):
    """FlowerTab item class"""

    _item_id: int = 115
    _description: str = "Raise FP by 1"
    _order: int = 43
    _consumable: bool = True
    _price: int = 200
    _tier: int = 2
    _room_service: str = "Flower Tab......."


class FlowerJar(RegularItem):
    """FlowerJar item class"""

    _item_id: int = 116
    _description: str = "Raise FP by 3"
    _order: int = 42
    _consumable: bool = True
    _price: int = 600
    _tier: int = 3
    _room_service: str = "Flower Jar......."


class FlowerBox(RegularItem):
    """FlowerBox item class"""

    _item_id: int = 117
    _description: str = "Raise FP by 5"
    _order: int = 41
    _consumable: bool = True
    _price: int = 1000
    _tier: int = 4
    _room_service: str = "Flower Box......."


class YoshiCandy(RegularItem):
    """YoshiCandy item class"""

    _item_id: int = 118
    _description: str = "Heals 100 HP"
    _order: int = 25
    _consumable: bool = True
    _price: int = 140
    _model: Type[ItemNPC] = GreenCandy
    _tier: int = 2
    _room_service: str = "Yoshi Candy......"


class FroggieDrink(RegularItem):
    """FroggieDrink item class"""

    _item_id: int = 119
    _description: str = "Party heals\x0130 HP"
    _order: int = 7
    _consumable: bool = True
    _price: int = 16
    _tier: int = 1
    _room_service: str = "FroggieDrink......"
    _model: Type[ItemNPC] = YellowMusicDrink


class MukuCookie(RegularItem):
    """MukuCookie item class"""

    _item_id: int = 120
    _description: str = "Party heals\x0169 HP"
    _order: int = 24
    _consumable: bool = True
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
        Status.BERSERK,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _model: Type[ItemNPC] = Cookie
    _price: int = 69
    _tier: int = 3
    _room_service: str = "Muku Cookie......"


class Elixir(RegularItem):
    """Elixir item class"""

    _item_id: int = 121
    _description: str = "Party heals\x0180 HP"
    _order: int = 4
    _consumable: bool = True
    _price: int = 48
    _tier: int = 2
    _room_service: str = "Elixir............."
    _model: Type[ItemNPC] = BlueMusicDrink


class Megalixir(RegularItem):
    """Megalixir item class"""

    _item_id: int = 122
    _description: str = "Party heals\x01150 HP"
    _order: int = 12
    _consumable: bool = True
    _price: int = 120
    _tier: int = 3
    _room_service: str = "Megalixir.........."
    _model: Type[ItemNPC] = RedMusicDrink


class SeeYa(RegularItem):
    """SeeYa item class"""

    _item_id: int = 123
    _description: str = "Run away from\x01battles"
    _order: int = 39
    _price: int = 250
    _frog_coin_item: bool = True
    _tier: int = 3
    _unique: ItemUnique = ItemUnique.ALWAYS
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: An “Eject Button”!\n Sounds useful in a pinch, doesn't\n it?[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: An “Eject Button”.\n Sounds useful in a pinch, doesn't\n it?[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: An “Eject Button”.\n Sounds useful in a pinch, doesn't\n it?[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class TempleKey(KeyItem):
    """TempleKey item class"""

    _item_id: int = 124
    _order: int = 150
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Key
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Golden Key”!\n I wonder what it opens?[await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Golden Key”.\n I wonder what it opens?[await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Golden Key”.\n I wonder what it opens?[await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class GoodieBag(RegularItem):
    """GoodieBag item class"""

    _item_id: int = 125
    _order: int = 35
    _price: int = 1110
    _tier: int = 2
    _unique: ItemUnique = ItemUnique.ALWAYS
    _description: str = "It's packed\x01full of coins"
    _model: Type[ItemNPC] = SmallCoin
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Coin Sack”!\n It could make you rich![await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Coin Sack”.\n It could make you rich![await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Coin Sack”.\n It could make you rich![await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class EarlierTimes(RegularItem):
    """EarlierTimes item class"""

    _item_id: int = 126
    _description: str = "Use it to start\x01a battle over"
    _order: int = 34
    _price: int = 375
    _frog_coin_item: bool = True
    _tier: int = 1
    _unique: ItemUnique = ItemUnique.ALWAYS
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Reset Button”!\n Sounds useful in a pinch, doesn't\n it?[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Reset Button”.\n Sounds useful in a pinch, doesn't\n it?[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Reset Button”.\n Sounds useful in a pinch, doesn't\n it?[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class FreshenUp(RegularItem):
    """FreshenUp item class"""

    _item_id: int = 127
    _description: str = "Heals party\x01status ailments"
    _order: int = 6
    _consumable: bool = True
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
        Status.BERSERK,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _price: int = 50
    _model: Type[ItemNPC] = RDrink
    _tier: int = 2
    _room_service: str = "Freshen Up........"


class RareFrogCoin(KeyItem):
    """RareFrogCoin item class"""

    _item_id: int = 128
    _order: int = 144
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = SmallFrogCoin
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Green Coin”!\n It looks different from most Frog\n Coins.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Green Coin”.\n It looks different from most Frog\n Coins.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Green Coin”.\n It looks different from most Frog\n Coins.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class Wallet(RegularItem):
    """Wallet item class"""

    _item_id: int = 129
    _description: str = "A fat wallet"
    _order: int = 152
    _price: int = 246
    _model: Type[ItemNPC] = SmallCoin
    _tier: int = 1
    _unique: ItemUnique = ItemUnique.ALWAYS
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Coin Sack”!\n It looks like it belongs to someone.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Coin Sack”.\n It looks like it belongs to someone.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Coin Sack”.\n It looks like it belongs to someone.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class CricketPie(KeyItem):
    """CricketPie item class"""

    _item_id: int = 130
    _order: int = 138
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Cookie
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Baked Pastry”!\n Sorta makes you curious, doesn't\n it?[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Baked Pastry”.\n Sorta makes you curious, doesn't\n it?[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Baked Pastry”.\n Sorta makes you curious, doesn't\n it?[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class RockCandy(RegularItem):
    """RockCandy item class"""

    _item_name: str = "Rock Candy"
    _item_id: int = 131
    _description: str = "Attack all\x01enemies"
    _model: Type[ItemNPC] = BlueCandy
    _order: int = 31
    _consumable: bool = True
    _price: int = 400
    _tier: int = 4
    _room_service: str = "Rock Candy......"


class CastleKey1(KeyItem):
    """CastleKey1 item class"""

    _item_id: int = 132
    _order: int = 135
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Key
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Golden Key”!\n I wonder what it opens?[await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Golden Key”.\n I wonder what it opens?[await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Golden Key”.\n I wonder what it opens?[await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class CastleKey2(KeyItem):
    """CastleKey2 item class"""

    _item_id: int = 134
    _order: int = 136
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Key
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Golden Key”!\n I wonder what it opens?[await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Golden Key”.\n I wonder what it opens?[await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Golden Key”.\n I wonder what it opens?[await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class BambinoBomb(KeyItem):
    """BambinoBomb item class"""

    _item_id: int = 135
    _order: int = 136
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = MicroBombItem


class SheepAttack(RegularItem):
    """SheepAttack item class"""

    _item_id: int = 136
    _description: str = "Baah, baah..."
    _order: int = 40
    _price: int = 150
    _is_subitem: bool = True
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Egg
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: “Shepherd's Bait”!\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class CarboCookie(RegularItem):
    """CarboCookie item class"""

    _item_id: int = 137
    _description: str = "Kid's love 'em"
    _order: int = 134
    _unique: ItemUnique = ItemUnique.ALWAYS
    _is_subitem: bool = True
    _model: Type[ItemNPC] = Cookie
    _price: int = 2
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Trade Item”! It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }

    def __init__(self, world: Optional[GameWorld]):
        super().__init__(world)
        if world is None:
            return
        if world.settings.is_flag_value(
            FireworksSetting, FireworksOptions.SHUFFLE_ONE
        ) or world.settings.is_flag_value(
            FireworksSetting, FireworksOptions.PROGRESSIVE
        ):
            self.set_price(0)
            self.set_description("")


class ShinyStone(RegularItem):
    """ShinyStone item class"""

    _item_id: int = 138
    _order: int = 148
    _description: str = "A pretty stone!"
    _is_subitem: bool = True
    _unique: ItemUnique = ItemUnique.ALWAYS
    _price: int = 4
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Trade Item”! It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }

    def __init__(self, world: Optional[GameWorld]):
        super().__init__(world)
        if world is None:
            return
        if world.settings.is_flag_value(
            FireworksSetting, FireworksOptions.SHUFFLE_ONE
        ) or world.settings.is_flag_value(
            FireworksSetting, FireworksOptions.PROGRESSIVE
        ):
            self.set_price(0)
            self.set_description("")


class RoomKey(KeyItem):
    """RoomKey item class"""

    _item_id: int = 140
    _order: int = 145
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Key
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Golden Key”!\n I wonder what it opens?[await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Golden Key”.\n I wonder what it opens?[await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Golden Key”.\n I wonder what it opens?[await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class ElderKey(KeyItem):
    """ElderKey item class"""

    _item_id: int = 141
    _order: int = 140
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Key
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Golden Key”!\n I wonder what it opens?[await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Golden Key”.\n I wonder what it opens?[await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Golden Key”.\n I wonder what it opens?[await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class ShedKey(KeyItem):
    """ShedKey item class"""

    _item_id: int = 142
    _order: int = 147
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Key
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Golden Key”!\n I wonder what it opens?[await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Golden Key”.\n I wonder what it opens?[await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Golden Key”.\n I wonder what it opens?[await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class LambsLure(RegularItem):
    """LambsLure item class"""

    _item_id: int = 143
    _description: str = "Baa, baa..."
    _order: int = 36
    _price: int = 40
    _unique: ItemUnique = ItemUnique.ALWAYS
    _is_subitem: bool = True
    _model: Type[ItemNPC] = Egg
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: “Shepherd's Bait”!\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class FrightBomb(RegularItem):
    """FrightBomb item class"""

    _item_name: str = "Fright Bomb"
    _item_id: int = 144
    _description: str = "Inflict fear\x01on one enemy"
    _model: Type[ItemNPC] = GreenBomb
    _order: int = 28
    _consumable: bool = True
    _status_immunities: List[Status] = [Status.FEAR]
    _price: int = 100
    _tier: int = 2
    _room_service: str = "Fright Bomb......"


class MysteryEgg(RegularItem):
    """MysteryEgg item class"""

    _item_id: int = 145
    _description: str = "A product of\x01pure love..."
    _order: int = 38
    _is_subitem: bool = True
    _price: int = 200
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Egg
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: “Shepherd's Bait”!\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class BeetleBox(RegularItem):
    """BeetleBox item class"""

    _item_id: int = 146
    _order: int = 130
    _unique: ItemUnique = ItemUnique.ALWAYS


class BeetleBox2(RegularItem):
    """BeetleBox2 item class"""

    _item_id: int = 147
    _order: int = 131
    _unique: ItemUnique = ItemUnique.ALWAYS


class LuckyJewel(RegularItem):
    """LuckyJewel item class"""

    _item_id: int = 148
    _description: str = "Summons Luck\x01at will"
    _order: int = 37
    _price: int = 100
    _unique: ItemUnique = ItemUnique.ALWAYS
    _tier: int = 1
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: An “Lucky Jewel”!\n It’s sure to bring you plenty of\n good luck.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: An “Lucky Jewel”.\n It’s sure to bring you plenty of\n good luck.[await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: An “Lucky Jewel”.\n It’s sure to bring you plenty of\n good luck.[await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class SopranoCard(KeyItem):
    """SopranoCard item class"""

    _item_id: int = 150
    _order: int = 149
    _shuffle_as_key_item: bool = True
    _is_subitem: bool = True
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Card
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Musical Card”!\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class AltoCard(KeyItem):
    """AltoCard item class"""

    _item_id: int = 151
    _order: int = 129
    _shuffle_as_key_item: bool = True
    _is_subitem: bool = True
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Card
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Musical Card”!\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class TenorCard(KeyItem):
    """TenorCard item class"""

    _item_id: int = 152
    _order: int = 151
    _shuffle_as_key_item: bool = True
    _is_subitem: bool = True
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Card
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Musical Card”!\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class Crystalline(RegularItem):
    """Crystalline item class"""

    _item_id: int = 153
    _description: str = "Raises party's\x01Defense in\x01battle"
    _order: int = 3
    _consumable: bool = True
    _temp_buffs: List[TempStatBuff] = [
        TempStatBuff.DEFENSE,
        TempStatBuff.MAGIC_DEFENSE,
    ]
    _price: int = 125
    _frog_coin_item: bool = True
    _tier: int = 3
    _room_service: str = "Crystalline......."
    _model: Type[ItemNPC] = DDrink


class PowerBlast(RegularItem):
    """PowerBlast item class"""

    _item_id: int = 154
    _description: str = "Raises party's\x01Attack Power\x01in battle"
    _order: int = 18
    _consumable: bool = True
    _temp_buffs: List[TempStatBuff] = [
        TempStatBuff.ATTACK,
        TempStatBuff.MAGIC_ATTACK,
    ]
    _price: int = 125
    _frog_coin_item: bool = True
    _tier: int = 3
    _room_service: str = "Power Blast......"
    _model: Type[ItemNPC] = PDrink


class WiltShroom(RegularItem):
    """WiltShroom item class"""

    _item_id: int = 155
    _description: str = "It's wilted..."
    _order: int = 22
    _consumable: bool = True
    _price: int = 8
    _tier: int = 1
    _model: Type[ItemNPC] = Banana
    _room_service: str = "Wilt Shroom......"


class RottenMush(RegularItem):
    """RottenMush item class"""

    _item_id: int = 156
    _description: str = "Eeew,\x01it's rotten!"
    _order: int = 20
    _consumable: bool = True
    _price: int = 4
    _tier: int = 1
    _model: Type[ItemNPC] = Banana
    _room_service: str = "Rotten Mush....."


class MoldyMush(RegularItem):
    """MoldyMush item class"""

    _item_id: int = 157
    _description: str = "Gross!\x01There's mold\x01growing on it."
    _order: int = 14
    _consumable: bool = True
    _price: int = 2
    _tier: int = 1
    _model: Type[ItemNPC] = Banana
    _room_service: str = "Moldy Mush......."


class Seed(KeyItem):
    """Seed item class"""

    _item_id: int = 158
    _order: int = 146
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Berry
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Mysterious Seed”!\n I wonder what will grow from it?[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Mysterious Seed”.\n I wonder what will grow from it?[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Mysterious Seed”.\n I wonder what will grow from it?[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class Fertilizer(KeyItem):
    """Fertilizer item class"""

    _item_id: int = 159
    _order: int = 141
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Bag of Dirt”!\n It seems different from the soil\n I dug it out of.[await][pause] I'll sell it to you\n for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Bag of Dirt”.\n It seems different from the soil\n I dug it out of.[await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Bag of Dirt”.\n It seems different from the soil\n I dug it out of.[await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class WasteBasket(Item):
    """WasteBasket item class"""

    _item_id: int = 160


class BigBooFlag(KeyItem):
    """BigBooFlag item class"""

    _item_id: int = 161
    _order: int = 132
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _model: Type[ItemNPC] = Card
    _unique: ItemUnique = ItemUnique.ALWAYS
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: An “Invisible Flag”!\n I wonder if someone is looking for\n this?[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: An “Invisible Flag”.\n I wonder if someone is looking for\n this?[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: An “Invisible Flag”.\n I wonder if someone is looking for\n this?[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class DryBonesFlag(KeyItem):
    """DryBonesFlag item class"""

    _item_id: int = 162
    _order: int = 139
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _model: Type[ItemNPC] = Card
    _unique: ItemUnique = ItemUnique.ALWAYS
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: An “Invisible Flag”!\n I wonder if someone is looking for\n this?[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: An “Invisible Flag”.\n I wonder if someone is looking for\n this?[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: An “Invisible Flag”.\n I wonder if someone is looking for\n this?[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class GreaperFlag(KeyItem):
    """GreaperFlag item class"""

    _item_id: int = 163
    _order: int = 143
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _model: Type[ItemNPC] = Card
    _unique: ItemUnique = ItemUnique.ALWAYS
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: An “Invisible Flag”!\n I wonder if someone is looking for\n this?[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: An “Invisible Flag”.\n I wonder if someone is looking for\n this?[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: An “Invisible Flag”.\n I wonder if someone is looking for\n this?[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class CricketJam(KeyItem):
    """CricketJam item class"""

    _item_id: int = 166
    _order: int = 137
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _model: Type[ItemNPC] = GreenJuice
    _shuffle_as_key_item: bool = True
    _unique: ItemUnique = ItemUnique.ALWAYS
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: “Green Jelly”!\n Sorta makes you curious, doesn't\n it?[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: “Green Jelly”.\n Sorta makes you curious, doesn't\n it?[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: “Green Jelly”.\n Sorta makes you curious, doesn't\n it?[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class Fireworks(RegularItem):
    """Fireworks item class"""

    _item_id: int = 172
    _description: str = "A gorgeous\x01firework"
    _unique: ItemUnique = ItemUnique.ALWAYS
    _chest_event: int = E3099_SHUFFLE_FIREWORKS_CHEST_GRANT
    _npc_event: int = E0184_NPC_QUEST_GRANT_SINGLE_FIREWORKS
    _is_subitem: bool = True
    _overworld_event: int = E3112_FREESTANDING_SHUFFLE_FIREWORKS_GRANT
    _overworld_midas_event: int = E3398_MIDAS_CAVE_SINGLE_FIREWORK_GRANTER
    _price: int = 500
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Trade Item”! It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }

    def __init__(self, world: Optional[GameWorld]):
        super().__init__(world)
        if world is None:
            return
        if world.settings.is_flag_value(
            FireworksSetting, FireworksOptions.SHUFFLE_ONE
        ) or world.settings.is_flag_value(
            FireworksSetting, FireworksOptions.PROGRESSIVE
        ):
            self.set_price(0)
            self.set_description("")
        if world.settings.is_flag_value(FireworksSetting, FireworksOptions.SHUFFLE_ONE):
            self.set_shuffle_as_key_item(True)
            self.set_subitem(False)


class BrightCard(KeyItem):
    """BrightCard item class"""

    _item_id: int = 174
    _model: Type[ItemNPC] = Card
    _order: int = 133
    _unique: ItemUnique = ItemUnique.ALWAYS
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _shuffle_as_key_item: bool = True
    _tier: int = 1
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Shiny Card”!\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Shiny Card”.\n It's sure to bring you an air of\n prestige.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Shiny Card”.\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }

    def set_tier(self, tier: int = 1):
        # Make this a top tier item if signal ring hints are turned on
        if self.world is not None and self.world.settings.is_boolean_flag_enabled(
            CasinoWarp
        ):
            super().set_tier(4)
        else:
            super().set_tier(tier)

    def __init__(self, world: Optional[GameWorld] = None):
        super().__init__(world)
        self.set_tier()


class Mushroom2(RegularItem):
    """Mushroom2 item class"""

    _item_id: int = 175
    _description: str = "Recoers 30 HP,\x01but..."
    _order: int = 16
    _consumable: bool = True
    _status_immunities: List[Status] = [Status.MUSHROOM]
    _price: int = 4
    _tier: int = 1
    _model: Type[ItemNPC] = RedMushroom
    _room_service: str = "Mushroom........"

    def __init__(self, world: Optional[GameWorld] = None):
        super().__init__(world)
        if world is not None:
            self.set_status_immunities(
                [
                    choice(
                        [
                            Status.BERSERK,
                            Status.FEAR,
                            Status.INVINCIBLE,
                            Status.MUSHROOM,
                            Status.MUTE,
                            Status.POISON,
                            Status.SCARECROW,
                            Status.SLEEP,
                        ]
                    )
                ]
            )


class StarEgg(RegularItem):
    """StarEgg item class"""

    _item_id: int = 176
    _description: str = "Reusable battle\x01item"
    _order: int = 33
    _price: int = 700
    _tier: int = 4
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Egg
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: An “Adorable Bomb”!\n Seems like it'll last a long time![await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: An “Adorable Bomb”.\n Seems like it'll last a long time![await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: An “Adorable Bomb”.\n Seems like it'll last a long time![await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class ProgressiveCard(ProgressiveItem, KeyItem):
    """ProgressiveCard item class"""

    _item_id: int = 195
    _model: Type[ItemNPC] = Card
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _chest_event: int = E3086_JUICE_BAR_CARD_UPGRADE
    _npc_event: int = E3097_JUICE_BAR_CARD_NPC_GRANT
    _overworld_event: int = E3110_FREESTANDING_JUICE_BAR_CARD_GRANT
    _overworld_midas_event: int = E3396_MIDAS_CAVE_PROGRESSIVE_CARD_GRANTER
    _is_key: bool = True
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Musical Card”!\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class ProgressiveEgg(ProgressiveItem):
    """ProgressiveEgg item class"""

    _item_id: int = 196
    _model: Type[ItemNPC] = Egg
    _unique: ItemUnique = ItemUnique.ALWAYS
    _tier: int = 2
    _chest_event: int = E3087_PROGRESSIVE_EGG_UPGRADE
    _npc_event: int = E3098_PROGRESSIVE_EGG_NPC_GRANT
    _overworld_event: int = E3111_FREESTANDING_PROGRESSIVE_EGG_GRANT
    _overworld_midas_event: int = E3397_MIDAS_CAVE_PROGRESSIVE_EGG_GRANTER
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: “Shepherd's Bait”!\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class ProgressiveFireworks(ProgressiveItem):
    """ProgressiveFireworks item class"""

    _item_id: int = 197
    _unique: ItemUnique = ItemUnique.ALWAYS
    _chest_event: int = E3100_PROGRESSIVE_FIREWORKS_CHEST_GRANT
    _npc_event: int = E0185_NPC_QUEST_GRANT_PROGRESSIVE_FIREWORKS
    _overworld_event: int = E3113_FREESTANDING_PROGRESSIVE_FIREWORKS_GRANT
    _overworld_midas_event: int = E3399_MIDAS_CAVE_PROGRESSIVE_FIREWORK_GRANTER
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Trade Item”! It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class MimicFightInitiator1(MimicFightChestAssignment):
    """MimicFightInitiator1 item class"""

    _item_id: int = 211
    _unique: ItemUnique = ItemUnique.ALWAYS
    _tier: int = 1
    _chest_event: int = E3124_MIMIC_1_CHEST


class MimicFightInitiator2(MimicFightChestAssignment):
    """MimicFightInitiator2 item class"""

    _item_id: int = 212
    _unique: ItemUnique = ItemUnique.ALWAYS
    _tier: int = 1
    _chest_event: int = E3126_MIMIC_2_CHEST


class MimicFightInitiator3(MimicFightChestAssignment):
    """MimicFightInitiator3 item class"""

    _item_id: int = 213
    _unique: ItemUnique = ItemUnique.ALWAYS
    _tier: int = 1
    _chest_event: int = E2493_MIMIC_3


class Coins10(Coins):
    """Coins10 item class"""

    _item_id: int = 193
    _tier: int = 1
    _overworld_event: int = E3146_FREESTANDING_BIG_COIN
    _overworld_midas_event: int = E2818_ASYNC_NO_ANIMATION_10_COIN
    _model: Type[ItemNPC] = BigCoin
    _amount = 10

    def __init__(self, world):
        super().__init__(10, world)


class Coins1(Coins):
    """Coins1 item class"""

    _item_id: int = 194
    _tier: int = 1
    _overworld_event: int = E1293_COLLECT_FREESTANDING_SMALL_COIN
    _overworld_midas_event: int = E2819_ASYNC_NO_ANIMATION_1_COIN
    # _model: Type[ItemNPC] = SmallCoin
    # _amount = 1

    def __init__(self, world):
        super().__init__(1, world)


class Coins5(Coins):
    """Coins5 item class"""

    _amount = 5

    def __init__(self, world):
        super().__init__(5, world)


class Coins8(Coins):
    """Coins8 item class"""

    _amount = 8

    def __init__(self, world):
        super().__init__(8, world)


class Coins20(Coins):
    """Coins20 item class"""

    _amount = 20

    def __init__(self, world):
        super().__init__(20, world)


class Coins50(Coins):
    """Coins50 item class"""

    _amount = 50

    def __init__(self, world):
        super().__init__(50, world)


class Coins100(Coins):
    """Coins100 item class"""

    _amount = 100

    def __init__(self, world):
        super().__init__(100, world)


class Coins150(Coins):
    """Coins150 item class"""

    _amount = 150

    def __init__(self, world):
        super().__init__(150, world)


class Beetlemania(MiscReward):
    """Beetlemania item class"""

    _item_id: int = 164
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Beetle
    _tier: int = 1
    _chest_event: int = E0162_CHEST_GRANT_BEETLEMANIA
    _npc_event: int = E0161_NPC_QUEST_GRANT_BEETLEMANIA
    _overworld_event: int = E3109_FREESTANDING_BEETLEMANIA_GRANT
    _overworld_midas_event: int = E3395_MIDAS_CAVE_BEETLEMANIA_GRANTER
    _price: int = 500
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Handheld Game”!\n Sounds pretty fun, doesn't it?[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Handheld Game”.\n Sounds pretty fun, doesn't it?[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Handheld Game”.\n Sounds pretty fun, doesn't it?[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class SlotMachineChest(MiscReward):
    """SlotMachineChest item class"""

    _item_id: int = 214
    _tier: int = 2
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY


class InfiniteCoins(MiscReward):
    """InfiniteCoins item class"""

    _item_id: int = 240
    _unique: ItemUnique = ItemUnique.ALWAYS
    _chest_event: int = E3074_COIN_CHEST_MULTI_HIT_1
    _tier: int = 2
    _chest_70a7_lower: int = 0
    _chest_70a7_upper: int = 15


class StarPiece1(StarPiece):
    """StarPiece1 item class"""

    _hint_bit: Flag = SIGNAL_RING_STAR_PIECE_1


class StarPiece2(StarPiece):
    """StarPiece2 item class"""

    _hint_bit: Flag = SIGNAL_RING_STAR_PIECE_2


class StarPiece3(StarPiece):
    """StarPiece3 item class"""

    _hint_bit: Flag = SIGNAL_RING_STAR_PIECE_3


class StarPiece4(StarPiece):
    """StarPiece4 item class"""

    _hint_bit: Flag = SIGNAL_RING_STAR_PIECE_4


class StarPiece5(StarPiece):
    """StarPiece5 item class"""

    _hint_bit: Flag = SIGNAL_RING_STAR_PIECE_5


class StarPiece6(StarPiece):
    """StarPiece6 item class"""

    _hint_bit: Flag = SIGNAL_RING_STAR_PIECE_6


class StarPiece7(StarPiece):
    """StarPiece7 item class"""

    _hint_bit: Flag = SIGNAL_RING_STAR_PIECE_7


class Nothing(MiscReward):
    """Nothing item class"""

    _chest_event: int = E3081_YOU_MISSED
    _npc_event: int = E0256_RETURN
    _model: Type[ItemNPC] = Empty
    _overworld_midas_event: int = E0256_RETURN
    _overworld_event: int = E0256_RETURN


class Flower(MiscReward):
    """Flower item class"""

    _item_id: int = 198
    _tier: int = 1
    _model: Type[ItemNPC] = FlowerNPC
    _chest_70a7_upper: int = 2
    _chest_event: int = E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST
    _overworld_event: int = E1801_FREESTANDING_FLOWER
    _overworld_midas_event: int = E2817_ASYNC_NO_ANIMATION_FLOWER


class RecoveryMushroom(MiscReward):
    """RecoveryMushroom item class"""

    _item_id: int = 199
    _tier: int = 1
    _chest_event: int = E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST
    _overworld_event: int = E2822_ASYNC_NO_ANIMATION_MUSHROOM
    _npc_event: int = E0397_HEAL_IN_TOADSTOOLS_ROOM
    _overworld_midas_event: int = E2822_ASYNC_NO_ANIMATION_MUSHROOM
    _model: Type[ItemNPC] = RecoveryMushroomNPC


class FrogCoin(MiscReward):
    """FrogCoin item class"""

    _item_id: int = 200
    _tier: int = 1
    _model: Type[ItemNPC] = FrogCoinNPC
    _chest_70a7_upper: int = 3
    _chest_event: int = E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST
    _npc_event: int = E0157_NPC_QUEST_GRANT_1_FROG_COIN
    _overworld_event: int = E3238_FREESTANDING_FROG_COIN
    _overworld_midas_event: int = E2816_ASYNC_NO_ANIMATION_FROG_COIN


class MultiFrogCoin(MiscReward):
    """MultiFrogCoin item class"""

    _item_id: int = 215
    _tier: int = 2
    _amount: int = 0
    _multiplier: int = 0
    _chest_event: int = E3091_MULTI_FROG_COIN_CHEST_SINGLE_HIT
    _quick_chest_event: int = E3082_FROG_COIN_CHEST_MULTI_HIT_1
    _model: Type[ItemNPC] = FrogCoinNPC
    _npc_event: int = E0158_NPC_QUEST_GRANT_MULTI_FROG_COIN
    _chest_70a7_upper: int = 0

    @property
    def amount(self) -> UInt16:
        """The amount of coins included in this grant."""
        return UInt16(self._amount)

    def _set_amount(self, amount: int) -> None:
        self._amount = amount

    @property
    def multiplier(self) -> UInt8:
        """Used in the calculation logic that determines the number of times
        you can hit a chest to fully deplete it at this grant's coin amount."""
        return UInt8(self._multiplier)

    def _set_multiplier(self, multiplier: int) -> None:
        self._multiplier = multiplier

    def get_chest_event(self, parent):
        """Returns the specific coin chest event to run, depending on the
        central granter event used for this chest. This is necessary because
        multiple chests in the same room need to use a different bit to
        control whether or not they can be considered depleted, and up to
        six chests can be present in one room."""
        if parent == E0246_CHEST_2_GRANT:
            return E3406_FROG_COIN_CHEST_MULTI_HIT_2
        if parent == E0245_CHEST_3_GRANT:
            return E3407_FROG_COIN_CHEST_MULTI_HIT_3
        if parent == E0244_CHEST_4_GRANT:
            return E3408_FROG_COIN_CHEST_MULTI_HIT_4
        if parent == E0243_CHEST_5_GRANT:
            return E3409_FROG_COIN_CHEST_MULTI_HIT_5
        if parent == E0242_CHEST_6_GRANT:
            return E3410_FROG_COIN_CHEST_MULTI_HIT_6
        return E3082_FROG_COIN_CHEST_MULTI_HIT_1

    @property
    def chest_event(self):
        raise ValueError("use get_chest_event for multifrogcoins")

    def __init__(self, world, amount):
        """

        Args:
            world (randomizer.logic.main.GameWorld):
            amount (int)

        """
        super().__init__(world)
        hits: int = amount
        loops: int = hits // 16
        leftover: int = hits - 15 * loops
        self._set_multiplier(loops)
        self._set_chest_70a7_lower(leftover)
        self._set_amount(amount)


class FrogCoins2(MultiFrogCoin):
    """FrogCoins2 item class"""

    _amount = 2

    def __init__(self, world):
        super().__init__(2, world)


class FrogCoins3(MultiFrogCoin):
    """FrogCoins3 item class"""

    _amount = 3

    def __init__(self, world):
        super().__init__(3, world)


class FrogCoins10(MultiFrogCoin):
    """FrogCoins10 item class"""

    _amount = 10

    def __init__(self, world):
        super().__init__(10, world)


class FrogCoins20(MultiFrogCoin):
    """FrogCoins20 item class"""

    _amount = 20

    def __init__(self, world):
        super().__init__(20, world)


class YouMissed(MiscReward):
    """YouMissed item class"""

    _item_id: int = 210
    _tier: int = 1
    _chest_event: int = 3081


class BanditsWayStar(InvincibilityStar):
    """BanditsWayStar item class"""

    _item_id: int = 201
    _tier: int = 1


class KeroSewersStar(InvincibilityStar):
    """KeroSewersStar item class"""

    _item_id: int = 202
    _tier: int = 1
    _chest_70a7_lower: int = 1


class MolevilleMinesStar(InvincibilityStar):
    """MolevilleMinesStar item class"""

    _item_id: int = 203
    _tier: int = 2
    _chest_70a7_lower: int = 2


class SeaStar(InvincibilityStar):
    """SeaStar item class"""

    _item_id: int = 204
    _tier: int = 3
    _chest_70a7_lower: int = 3


class LandsEndVolcanoStar(InvincibilityStar):
    """LandsEndVolcanoStar item class"""

    _item_id: int = 205
    _tier: int = 4
    _chest_70a7_lower: int = 5


class NimbusLandStar(InvincibilityStar):
    """NimbusLandStar item class"""

    _item_id: int = 206
    _tier: int = 2
    _chest_70a7_lower: int = 7


class LandsEndStar2(InvincibilityStar):
    """LandsEndStar2 item class"""

    _item_id: int = 207
    _tier: int = 3
    _chest_70a7_lower: int = 8


class LandsEndStar3(InvincibilityStar):
    """LandsEndStar3 item class"""

    _item_id: int = 208
    _tier: int = 3
    _chest_70a7_lower: int = 9


class Shoes(MarrymoreGear):
    """Shoes item class"""

    _id: int = 230
    _unique: ItemUnique = ItemUnique.ALWAYS
    _chest_event: int = E3943_SHOES_CHEST
    _npc_event: int = E3931_GET_SHOES
    _overworld_event: int = E3935_FREESTANDING_SHOES
    _overworld_midas_event: int = E3939_RIVER_SHOES
    _model: Type[ItemNPC] = ShoesNPC
    _price: int = 0
    _tier: int = 1
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Pair of Fancy Shoes”!\n I bet they would look great on you.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Pair of Fancy Shoes”.\n I bet they would look great on you.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Pair of Fancy Shoes”.\n I bet they would look great on you.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class Brooch(MarrymoreGear):
    """Brooch item class"""

    _id: int = 231
    _unique: ItemUnique = ItemUnique.ALWAYS
    _chest_event: int = E3944_BROOCH_CHEST
    _npc_event: int = E3932_GET_BROOCH
    _overworld_event: int = E3936_FREESTANDING_BROOCH
    _overworld_midas_event: int = E3940_RIVER_BROOCH
    _model: Type[ItemNPC] = BroochNPC
    _price: int = 0
    _tier: int = 1
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Shiny Brooch”! It\n looks made for special occasions.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Shiny Brooch”. It\n looks made for special occasions.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Shiny Brooch”. It\n looks made for special occasions.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class Ring(MarrymoreGear):
    """Ring item class"""

    _id: int = 232
    _unique: ItemUnique = ItemUnique.ALWAYS
    _chest_event: int = E3945_RING_CHEST
    _npc_event: int = E3933_GET_RING
    _overworld_event: int = E3937_FREESTANDING_RING
    _overworld_midas_event: int = E3941_RIVER_RING
    _model: Type[ItemNPC] = RingNPC
    _price: int = 0
    _tier: int = 1
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Diamond Ring”! It's\n a great gift for someone special.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Diamond Ring”. It's\n a great gift for someone special.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Diamond Ring”. It's\n a great gift for someone special.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class Crown(MarrymoreGear):
    """Crown item class"""

    _id: int = 233
    _unique: ItemUnique = ItemUnique.ALWAYS
    _chest_event: int = E3946_CROWN_CHEST
    _npc_event: int = E3934_GET_CROWN
    _overworld_event: int = E3938_FREESTANDING_CROWN
    _overworld_midas_event: int = E3942_RIVER_CROWN
    _model: Type[ItemNPC] = CrownNPC
    _price: int = 0
    _tier: int = 1
    _dialog_replacements: "dict[int, str]" = {
        DI2911_TREASURE_SELLER_ITEM_1: """ Item #1: A “Royal Crown”!\n It looks pretty important![await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        DI2908_TREASURE_SELLER_ITEM_2: """ Item #2: A “Royal Crown”.\n It looks pretty important![await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        DI2914_TREASURE_SELLER_ITEM_3: """ Item #3: A “Royal Crown”.\n It looks pretty important![await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


# type: ignore # this is too annoying to debug
def initiate_items(world: GameWorld) -> List[Item]:
    """Instantiate each item for use in the game world."""

    items: List[Item] = [
        # literal items
        Hammer(world),
        FroggieStick(world),
        NokNokShell(world),
        PunchGlove(world),
        FingerShot(world),
        Cymbals(world),
        Chomp(world),
        Masher(world),
        ChompShell(world),
        SuperHammer(world),
        HandGun(world),
        WhompGlove(world),
        SlapGlove(world),
        TroopaShell(world),
        Parasol(world),
        HurlyGloves(world),
        DoublePunch(world),
        RibbitStick(world),
        SpikedLink(world),
        MegaGlove(world),
        WarFan(world),
        HandCannon(world),
        StickyGlove(world),
        UltraHammer(world),
        SuperSlap(world),
        DrillClaw(world),
        StarGun(world),
        SonicCymbal(world),
        LazyShellWeapon(world),
        FryingPan(world),
        LuckyHammer(world),
        Shirt(world),
        Pants(world),
        ThickShirt(world),
        ThickPants(world),
        MegaShirt(world),
        MegaPants(world),
        WorkPants(world),
        MegaCape(world),
        HappyShirt(world),
        HappyPants(world),
        HappyCape(world),
        HappyShell(world),
        PolkaDress(world),
        SailorShirt(world),
        SailorPants(world),
        SailorCape(world),
        NauticaDress(world),
        CourageShell(world),
        FuzzyShirt(world),
        FuzzyPants(world),
        FuzzyCape(world),
        FuzzyDress(world),
        FireShirt(world),
        FirePants(world),
        FireCape(world),
        FireShell(world),
        FireDress(world),
        HeroShirt(world),
        PrincePants(world),
        StarCape(world),
        HealShell(world),
        RoyalDress(world),
        SuperSuit(world),
        LazyShellArmor(world),
        ZoomShoes(world),
        SafetyBadge(world),
        JumpShoes(world),
        SafetyRing(world),
        Amulet(world),
        ScroogeRing(world),
        ExpBooster(world),
        AttackScarf(world),
        RareScarf(world),
        BtubRing(world),
        AntidotePin(world),
        WakeUpPin(world),
        FearlessPin(world),
        TrueformPin(world),
        CoinTrick(world),
        GhostMedal(world),
        JinxBelt(world),
        Feather(world),
        TroopaPin(world),
        SignalRing(world),
        QuartzCharm(world),
        Mushroom(world),
        MidMushroom(world),
        MaxMushroom(world),
        HoneySyrup(world),
        MapleSyrup(world),
        RoyalSyrup(world),
        PickMeUp(world),
        AbleJuice(world),
        Bracer(world),
        Energizer(world),
        YoshiAde(world),
        RedEssence(world),
        KerokeroCola(world),
        YoshiCookie(world),
        PureWater(world),
        SleepyBomb(world),
        BadMushroom(world),
        FireBomb(world),
        IceBomb(world),
        FlowerTab(world),
        FlowerJar(world),
        FlowerBox(world),
        YoshiCandy(world),
        FroggieDrink(world),
        MukuCookie(world),
        Elixir(world),
        Megalixir(world),
        SeeYa(world),
        TempleKey(world),
        GoodieBag(world),
        EarlierTimes(world),
        FreshenUp(world),
        RareFrogCoin(world),
        Wallet(world),
        CricketPie(world),
        RockCandy(world),
        CastleKey1(world),
        CastleKey2(world),
        BambinoBomb(world),
        SheepAttack(world),
        CarboCookie(world),
        ShinyStone(world),
        RoomKey(world),
        ElderKey(world),
        ShedKey(world),
        LambsLure(world),
        FrightBomb(world),
        MysteryEgg(world),
        BeetleBox(world),
        BeetleBox2(world),
        LuckyJewel(world),
        SopranoCard(world),
        AltoCard(world),
        TenorCard(world),
        Crystalline(world),
        PowerBlast(world),
        WiltShroom(world),
        RottenMush(world),
        MoldyMush(world),
        Seed(world),
        Fertilizer(world),
        BigBooFlag(world),
        DryBonesFlag(world),
        GreaperFlag(world),
        CricketJam(world),
        Fireworks(world),
        BrightCard(world),
        Mushroom2(world),
        StarEgg(world),
        # ad-hoc items
        ProgressiveCard(world),
        ProgressiveEgg(world),
        ProgressiveFireworks(world),
        MimicFightInitiator1(world),
        MimicFightInitiator2(world),
        MimicFightInitiator3(world),
        Beetlemania(world),
        SlotMachineChest(world),
        InfiniteCoins(world),
        StarPiece1(world),
        StarPiece2(world),
        StarPiece3(world),
        StarPiece4(world),
        StarPiece5(world),
        StarPiece6(world),
        StarPiece7(world),
        Nothing(world),
        Flower(world),
        RecoveryMushroom(world),
        FrogCoin(world),
        Coins1(world),
        Coins10(world),
        YouMissed(world),
        BanditsWayStar(world),
        KeroSewersStar(world),
        MolevilleMinesStar(world),
        SeaStar(world),
        LandsEndVolcanoStar(world),
        NimbusLandStar(world),
        LandsEndStar2(world),
        LandsEndStar3(world),
        Shoes(world),
        Brooch(world),
        Ring(world),
        Crown(world),
    ]

    return items
