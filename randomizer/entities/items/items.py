from copy import deepcopy
from randomizer.types.items.constants import EQUIP_STATS, ITEMS_BASE_ADDRESS
from randomizer.types.items.enums import (
    EffectType,
    EquipStats,
    ItemShuffleType,
    ItemTempBuff,
    ItemUnique,
)
from randomizer.types.spells.enums import Element, Status

from randomizer.logic.patch import Patch
from randomizer.types.numbers.classes import BitMapSet, UInt16, UInt8
from randomizer.types.overworld_scripts.event_scripts.constants.script_ids import (
    E0256_RETURN,
    E3081_YOU_MISSED,
)
from randomizer.types.overworld_scripts.variables.classes import Flag
from randomizer.types.overworld_scripts.variables.variables import (
    SIGNAL_RING_STAR_PIECE_1,
    SIGNAL_RING_STAR_PIECE_2,
    SIGNAL_RING_STAR_PIECE_3,
    SIGNAL_RING_STAR_PIECE_4,
    SIGNAL_RING_STAR_PIECE_5,
    SIGNAL_RING_STAR_PIECE_6,
    SIGNAL_RING_STAR_PIECE_7,
)
from randomizer.types.items.classes import (
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
    ItemT,
    Weapon,
    Armor,
    Accessory,
    ProgressiveItem,
)
from randomizer.types.overworld_scripts.constants.area_objects import (
    PartyCharacter,
    MARIO,
    MALLOW,
    GENO,
    TOADSTOOL,
    BOWSER,
)

from randomizer.logic import flags
from randomizer.helpers.flag_helpers import FireworksOptions
from randomizer.types.npcs.objects.classes import ItemNPC
from randomizer.types.npcs.objects.npcs import (
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

from typing import List, Optional, Sequence, Type, TypeVar

from randomizer.types.world.classes import GameWorld
from randomizer.types.world.flags.flags import FireworksSetting


class Hammer(Weapon, RegularEquip):
    _item_id: int = 5
    _description: str = "Pounds\x01enemies"
    _tier: int = 5
    _order: int = 53
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 10
    _variance: int = 1
    _price: int = 70
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _model: Type[ItemNPC] = HammerNPC
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Hammer”!\n I'm not sure if it does anything\n else.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Hammer”.\n I'm not sure if it does anything\n else.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Hammer”.\n I'm not sure if it does anything\n else.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class FroggieStick(Weapon, SpecialEquip):
    _item_id: int = 6
    _description: str = "Frogfucius\x01made it"
    _tier: int = 5
    _order: int = 67
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 20
    _variance: int = 2
    _price: int = 180
    _special_equip: bool = True
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _model: Type[ItemNPC] = FroggieStickNPC
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Caster's Staff”!\n It looks pretty good at bonking.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Caster's Staff”.\n It looks pretty good at bonking.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Caster's Staff”.\n It looks pretty good at bonking.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class NokNokShell(Weapon, RegularEquip):
    _item_id: int = 7
    _description: str = "Kick to attack"
    _tier: int = 5
    _order: int = 58
    _equip_chars: List[PartyCharacter] = [MARIO]
    _model: Type[ItemNPC] = GreenShell
    _attack: int = 20
    _variance: int = 2
    _price: int = 20
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Green Shell”!\n There's no turtle inside of it.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Green Shell”.\n There's no turtle inside of it.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Green Shell”.\n There's no turtle inside of it.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class PunchGlove(Weapon, RegularEquip):
    _item_id: int = 8
    _description: str = "Knock out\x01power!"
    _tier: int = 5
    _order: int = 48
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 30
    _variance: int = 3
    _price: int = 36


class FingerShot(Weapon, RegularEquip):
    _item_id: int = 9
    _description: str = "Fingers shoot\x01bullets"
    _tier: int = 5
    _order: int = 70
    _equip_chars: List[PartyCharacter] = [GENO]
    _attack: int = 12
    _variance: int = 3
    _price: int = 50


class Cymbals(Weapon, RegularEquip):
    _item_id: int = 10
    _description: str = "Scare enemies\x01with a clash"
    _tier: int = 5
    _order: int = 60
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 30
    _variance: int = 3
    _price: int = 42
    _model: Type[ItemNPC] = Music


class Chomp(Weapon, SpecialEquip):
    _item_id: int = 11
    _description: str = "Just spin me\x01at an enemy!"
    _tier: int = 3
    _order: int = 64
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _attack: int = 10
    _variance: int = 4
    _price: int = 140
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _model: Type[ItemNPC] = ChompItem
    _special_equip: bool = True
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Chain Chomp”!\n It's hungry to stir up some trouble.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Chain Chomp”.\n It's hungry to stir up some trouble.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Chain Chomp”.\n It's hungry to stir up some trouble.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class Masher(Weapon, RegularEquip):
    _item_id: int = 12
    _description: str = "Makes monster\x01mash!"
    _tier: int = 3
    _order: int = 54
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 50
    _variance: int = 30
    _price: int = 160
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _model: Type[ItemNPC] = HammerNPC
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Hammer”!\n I'm not sure if it does anything\n else.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Hammer”.\n I'm not sure if it does anything\n else.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Hammer”.\n I'm not sure if it does anything\n else.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class ChompShell(Weapon, RegularEquip):
    _item_id: int = 13
    _description: str = "It~s a\x01Kinklink shell"
    _model: Type[ItemNPC] = ChompItem
    _tier: int = 5
    _order: int = 65
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _attack: int = 9
    _variance: int = 3
    _price: int = 60


class SuperHammer(Weapon, RegularEquip):
    _item_id: int = 14
    _description: str = "The standard\x01for hammers!"
    _tier: int = 5
    _order: int = 55
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 40
    _variance: int = 4
    _price: int = 70
    _model: Type[ItemNPC] = HammerNPC


class HandGun(Weapon, RegularEquip):
    _item_id: int = 15
    _description: str = "It packs a kick"
    _tier: int = 5
    _order: int = 72
    _equip_chars: List[PartyCharacter] = [GENO]
    _attack: int = 24
    _variance: int = 4
    _price: int = 75


class WhompGlove(Weapon, RegularEquip):
    _item_id: int = 16
    _description: str = "The old double\x01whammie!"
    _tier: int = 5
    _order: int = 52
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 40
    _variance: int = 4
    _price: int = 72


class SlapGlove(Weapon, RegularEquip):
    _item_id: int = 17
    _description: str = "It slaps ~em\x01silly"
    _tier: int = 5
    _order: int = 49
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _attack: int = 40
    _variance: int = 4
    _price: int = 100
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Little Glove”!\n You don't drink water out of it.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Little Glove”.\n You don't drink water out of it.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Little Glove”.\n You don't drink water out of it.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class TroopaShell(Weapon, RegularEquip):
    _item_id: int = 18
    _description: str = "Kick with it!"
    _model: Type[ItemNPC] = RedShell
    _tier: int = 5
    _order: int = 59
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 50
    _variance: int = 5
    _price: int = 90


class Parasol(Weapon, RegularEquip):
    _item_id: int = 19
    _description: str = "Inflicts\x01serious pain!"
    _model: Type[ItemNPC] = ParasolNPC
    _tier: int = 5
    _order: int = 68
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _attack: int = 50
    _variance: int = 5
    _price: int = 84


class HurlyGloves(Weapon, RegularEquip):
    _item_id: int = 20
    _description: str = "A classic\x01Mario}toss\x01attack"
    _tier: int = 5
    _order: int = 46
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _attack: int = 20
    _variance: int = 5
    _price: int = 92

    def get_patch(self) -> Patch:
        """Get patch for this item.

        Returns:
            randomizer.logic.patch.Patch:
        """
        patch = super().get_patch()

        # Alter Hurly Gloves animation script so it thinks Mario is dead and always uses the doll.  This avoids softlock
        # issues in some situations when Mario is alive but not present, or Mario uses the gloves to throw himself!
        patch.add_data(
            0x35F672, bytes([0x20, 0x0F, 0x01, 0x00, 0x2C, 0x0F, 0x00, 0x00])
        )
        patch.add_data(
            0x35F5F8, bytes([0x20, 0x0F, 0x01, 0x00, 0x2C, 0x0F, 0x00, 0x00])
        )

        return patch


class DoublePunch(Weapon, RegularEquip):
    _item_id: int = 21
    _description: str = "A handy double\x01rocket punch"
    _tier: int = 5
    _order: int = 44
    _equip_chars: List[PartyCharacter] = [GENO]
    _attack: int = 35
    _variance: int = 5
    _price: int = 88


class RibbitStick(Weapon, RegularEquip):
    _item_id: int = 22
    _description: str = "It~ll come\x01in handy"
    _model: Type[ItemNPC] = FroggieStickNPC
    _tier: int = 5
    _order: int = 69
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 50
    _variance: int = 5
    _price: int = 86


class SpikedLink(Weapon, RegularEquip):
    _item_id: int = 23
    _description: str = "A studded ball\x01and chain!"
    _tier: int = 4
    _order: int = 66
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _model: Type[ItemNPC] = ChompItem
    _attack: int = 30
    _variance: int = 6
    _price: int = 94


class MegaGlove(Weapon, RegularEquip):
    _item_id: int = 24
    _description: str = "Packs a mega\x01wallop!"
    _tier: int = 4
    _order: int = 47
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 60
    _variance: int = 6
    _price: int = 102


class WarFan(Weapon, RegularEquip):
    _item_id: int = 25
    _description: str = "A mysterious\x01battle fan!"
    _model: Type[ItemNPC] = Fan
    _tier: int = 4
    _order: int = 63
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _attack: int = 60
    _variance: int = 6
    _price: int = 100


class HandCannon(Weapon, RegularEquip):
    _item_id: int = 26
    _description: str = "Shoots bullets\x01from elbow!"
    _tier: int = 3
    _order: int = 71
    _equip_chars: List[PartyCharacter] = [GENO]
    _attack: int = 45
    _variance: int = 6
    _price: int = 105


class StickyGlove(Weapon, RegularEquip):
    _item_id: int = 27
    _description: str = "Launches a\x01punch attack."
    _tier: int = 4
    _order: int = 50
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 60
    _variance: int = 6
    _price: int = 98


class UltraHammer(Weapon, RegularEquip):
    _item_id: int = 28
    _description: str = "The ultimate\x01hammer!"
    _tier: int = 2
    _order: int = 56
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 70
    _variance: int = 7
    _price: int = 115
    _model: Type[ItemNPC] = HammerNPC
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Hammer”!\n I'm not sure if it does anything\n else.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Hammer”.\n I'm not sure if it does anything\n else.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Hammer”.\n I'm not sure if it does anything\n else.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class SuperSlap(Weapon, RegularEquip):
    _item_id: int = 29
    _description: str = "The Princess~\x01mega}slap!"
    _tier: int = 2
    _order: int = 51
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _attack: int = 70
    _variance: int = 7
    _price: int = 110
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Big Glove”!\n You don't drink water out of it.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Big Glove”.\n You don't drink water out of it.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Big Glove”.\n You don't drink water out of it.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class DrillClaw(Weapon, RegularEquip):
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
        2911: """ Item #1: A “Drilling Appendage”!\n I bet you could do some real damage\n with this.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Drilling Appendage”.\n I bet you could do some real damage\n with this.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Drilling Appendage”.\n I bet you could do some real damage\n with this.[await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class StarGun(Weapon, RegularEquip):
    _item_id: int = 31
    _description: str = "Try shooting\x01stars!"
    _tier: int = 1
    _order: int = 73
    _equip_chars: List[PartyCharacter] = [GENO]
    _model: Type[ItemNPC] = TinyStar
    _attack: int = 57
    _variance: int = 7
    _price: int = 120
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Celestial Launcher”!\n I bet you could do some real damage\n with this.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Celestial Launcher”.\n I bet you could do some real damage\n with this.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Celestial Launcher”.\n I bet you could do some real damage\n with this.[await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class SonicCymbal(Weapon, RegularEquip):
    _item_id: int = 32
    _description: str = "Puts noise to\x01work for you!"
    _tier: int = 2
    _order: int = 61
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 70
    _variance: int = 7
    _price: int = 108
    _model: Type[ItemNPC] = Music
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Psych Percussion”!\n This could catch monsters\n off-guard.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Psych Percussion”.\n This could catch monsters\n off-guard.[await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Psych Percussion”.\n This could catch monsters\n off-guard.[await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class LazyShellWeapon(Weapon, SpecialEquip):
    _item_id: int = 33
    _description: str = "Toss a shell\x01at an enemy!"
    _model: Type[ItemNPC] = RedShell
    _tier: int = 1
    _order: int = 57
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 90
    _variance: int = 40
    _price: int = 200
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _special_equip: bool = True
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: An “Oversized Shell”!\n You could do some real damage\n with this.[await][await] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: An “Oversized Shell”.\n You could do some real damage\n with this.[await][await] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: An “Oversized Shell”.\n You could do some real damage\n with this.[await][await] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class FryingPan(Weapon, RegularEquip):
    _item_id: int = 34
    _description: str = "Enough iron to\x01be dangerous!"
    _model: Type[ItemNPC] = FryingPanNPC
    _tier: int = 1
    _order: int = 62
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _attack: int = 90
    _variance: int = 20
    _price: int = 300
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Metal Plate”![await]\n Don't know what it’s used for,\n but I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Metal Plate”.[await]\n Don't know what it’s used for,\n but it's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Metal Plate”.[await]\n Don't know what it’s used for,\n but I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class LuckyHammer(Weapon, RegularEquip):
    _item_id: int = 35
    _description: str = "A lucky hammer!"
    _tier: int = 1
    _order: int = 54
    _equip_chars: List[PartyCharacter] = [MARIO]
    _price: int = 123
    _model: Type[ItemNPC] = HammerNPC


class Shirt(Armor, RegularEquip):
    _item_id: int = 37
    _description: str = "It~s a\x01shirt!"
    _tier: int = 5
    _order: int = 102
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 6
    _magic_defense: int = 6
    _price: int = 7


class Pants(Armor, RegularEquip):
    _item_id: int = 38
    _description: str = "It~s a pair\x01of pants!"
    _tier: int = 5
    _order: int = 95
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 6
    _magic_defense: int = 3
    _price: int = 7


class ThickShirt(Armor, RegularEquip):
    _item_id: int = 39
    _description: str = "A padded shirt"
    _tier: int = 5
    _order: int = 106
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 12
    _magic_defense: int = 8
    _price: int = 14


class ThickPants(Armor, RegularEquip):
    _item_id: int = 40
    _description: str = "Padded pants"
    _tier: int = 5
    _order: int = 105
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 12
    _magic_defense: int = 6
    _price: int = 14


class MegaShirt(Armor, RegularEquip):
    _item_id: int = 41
    _description: str = "Durable stay}\x01pressed shirt"
    _tier: int = 5
    _order: int = 93
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 18
    _magic_defense: int = 10
    _price: int = 22


class MegaPants(Armor, RegularEquip):
    _item_id: int = 42
    _description: str = "Durable work\x01pants"
    _tier: int = 5
    _order: int = 92
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 18
    _magic_defense: int = 9
    _price: int = 22


class WorkPants(Armor, RegularEquip):
    _item_id: int = 43
    _description: str = "Sweaty\x01work pants!"
    _tier: int = 5
    _order: int = 107
    _equip_chars: List[PartyCharacter] = [
        MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
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
    _item_id: int = 44
    _description: str = "Durable\x01pressed cape"
    _tier: int = 5
    _order: int = 91
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 6
    _magic_defense: int = 3
    _price: int = 22


class HappyShirt(Armor, RegularEquip):
    _item_id: int = 45
    _description: str = "A lucky shirt"
    _tier: int = 5
    _order: int = 87
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 38


class HappyPants(Armor, RegularEquip):
    _item_id: int = 46
    _description: str = "A lucky\x01pair of pants"
    _tier: int = 5
    _order: int = 85
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 38


class HappyCape(Armor, RegularEquip):
    _item_id: int = 47
    _description: str = "A lucky cape"
    _tier: int = 5
    _order: int = 84
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 12
    _magic_defense: int = 6
    _price: int = 38


class HappyShell(Armor, RegularEquip):
    _item_id: int = 48
    _description: str = "A lucky shell"
    _model: Type[ItemNPC] = GreenShell
    _tier: int = 5
    _order: int = 86
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _defense: int = 6
    _magic_defense: int = 3
    _price: int = 38


class PolkaDress(Armor, RegularEquip):
    _item_id: int = 49
    _description: str = "A flashy dress"
    _tier: int = 5
    _order: int = 96
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 160
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Casual Gown”!\n It's pink with little polka dots![await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Casual Gown”.\n It's pink with little polka dots![await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Casual Gown”.\n It's pink with little polka dots![await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class SailorShirt(Armor, RegularEquip):
    _item_id: int = 50
    _description: str = "A sailor~s\x01suit"
    _tier: int = 5
    _order: int = 101
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 30
    _magic_defense: int = 15
    _price: int = 50


class SailorPants(Armor, RegularEquip):
    _item_id: int = 51
    _description: str = "A sailor~s\x01pants"
    _tier: int = 5
    _order: int = 100
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 30
    _magic_defense: int = 15
    _price: int = 50


class SailorCape(Armor, RegularEquip):
    _item_id: int = 52
    _description: str = "A sailor~s\x01cape"
    _tier: int = 5
    _order: int = 99
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 18
    _magic_defense: int = 9
    _price: int = 50


class NauticaDress(Armor, RegularEquip):
    _item_id: int = 53
    _description: str = "A female\x01sailor~s dress"
    _tier: int = 5
    _order: int = 94
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _defense: int = 30
    _magic_defense: int = 15
    _price: int = 50


class CourageShell(Armor, RegularEquip):
    _item_id: int = 54
    _description: str = "A stout shell"
    _model: Type[ItemNPC] = GreenShell
    _tier: int = 4
    _order: int = 74
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _defense: int = 12
    _magic_defense: int = 6
    _price: int = 60


class FuzzyShirt(Armor, RegularEquip):
    _item_id: int = 55
    _description: str = "A fuzzy shirt"
    _tier: int = 4
    _order: int = 83
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 36
    _magic_defense: int = 18
    _price: int = 70


class FuzzyPants(Armor, RegularEquip):
    _item_id: int = 56
    _description: str = "Fuzzy pants"
    _tier: int = 4
    _order: int = 82
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 36
    _magic_defense: int = 18
    _price: int = 70


class FuzzyCape(Armor, RegularEquip):
    _item_id: int = 57
    _description: str = "A fuzzy cape"
    _tier: int = 4
    _order: int = 80
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 70


class FuzzyDress(Armor, RegularEquip):
    _item_id: int = 58
    _description: str = "A fuzzy dress"
    _tier: int = 4
    _order: int = 81
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _defense: int = 36
    _magic_defense: int = 18
    _price: int = 70


class FireShirt(Armor, RegularEquip):
    _item_id: int = 59
    _description: str = "Determined\x01person~s shirt"
    _tier: int = 4
    _order: int = 79
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 42
    _magic_defense: int = 21
    _price: int = 90


class FirePants(Armor, RegularEquip):
    _item_id: int = 60
    _description: str = "Determined\x01person~s pants"
    _tier: int = 4
    _order: int = 77
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 42
    _magic_defense: int = 21
    _price: int = 90
    _elemental_immunities: List[Element] = []


class FireCape(Armor, RegularEquip):
    _item_id: int = 61
    _description: str = "Determined\x01person~s cape"
    _tier: int = 4
    _order: int = 75
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 30
    _magic_defense: int = 15
    _price: int = 90


class FireShell(Armor, RegularEquip):
    _item_id: int = 62
    _description: str = "Determined\x01person~s shell"
    _model: Type[ItemNPC] = RedShell
    _tier: int = 4
    _order: int = 78
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _defense: int = 18
    _magic_defense: int = 9
    _price: int = 90


class FireDress(Armor, RegularEquip):
    _item_id: int = 63
    _description: str = "Determined\x01woman~s dress"
    _tier: int = 4
    _order: int = 76
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _defense: int = 42
    _magic_defense: int = 21
    _price: int = 90


class HeroShirt(Armor, RegularEquip):
    _item_id: int = 64
    _description: str = "A legendary\x01shirt."
    _tier: int = 3
    _order: int = 89
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 48
    _magic_defense: int = 24
    _price: int = 100


class PrincePants(Armor, RegularEquip):
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
    _item_id: int = 66
    _description: str = "A legendary\x01cape."
    _model: Type[ItemNPC] = TinyStar
    _tier: int = 3
    _order: int = 103
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 36
    _magic_defense: int = 18
    _price: int = 100


class HealShell(Armor, RegularEquip):
    _item_id: int = 67
    _description: str = "A legendary\x01shell."
    _model: Type[ItemNPC] = GreenShell
    _tier: int = 3
    _order: int = 88
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 100


class RoyalDress(Armor, RegularEquip):
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
    _item_id: int = 69
    _description: str = "A truly fine\x01suit!"
    _tier: int = 1
    _order: int = 104
    _equip_chars: List[PartyCharacter] = [
        MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
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
        2911: """ Item #1: A “Jumpsuit”!\n It looks pretty powerful, right?[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Jumpsuit”.\n It looks pretty powerful, right?[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Jumpsuit”.\n It looks pretty powerful, right?[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }

    @property
    def primary_stats(self) -> List[EquipStats]:
        """Primary stats of this item, depending on the type."""
        return EQUIP_STATS


class LazyShellArmor(Armor, SpecialEquip):
    _item_id: int = 70
    _description: str = "A stout and\x01durable shell."
    _model: Type[ItemNPC] = RedShell
    _tier: int = 1
    _order: int = 90
    _equip_chars: List[PartyCharacter] = [
        MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
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
        2911: """ Item #1: An “Oversized Shell”!\n It's quite beefy and protective.[await]\n I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: An “Oversized Shell”.\n It's quite beefy and protective.[await]\n It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: An “Oversized Shell”.\n It's quite beefy and protective.[await]\n I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class ZoomShoes(Accessory, SpecialEquip):
    _item_id: int = 74
    _description: str = "Speed up by 10!"
    _tier: int = 4
    _order: int = 128
    _equip_chars: List[PartyCharacter] = [
        MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 10
    _defense: int = 5
    _magic_defense: int = 5
    _price: int = 100
    _model: Type[ItemNPC] = ShoesNPC
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _special_equip: bool = True
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: “Pegasus Boots”!\n These will make you fast like Sonic![await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: “Pegasus Boots”.\n These will make you fast like Sonic![await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: “Pegasus Boots”.\n These will make you fast like Sonic![await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }

    @property
    def primary_stats(self) -> List[EquipStats]:
        """Primary stats of this item, depending on the type."""
        return [EquipStats.Speed]


class SafetyBadge(Accessory, RegularEquip):
    _item_id: int = 75
    _description: str = "Prevents Mute \x9c\x01Poison attacks"
    _tier: int = 2
    _order: int = 121
    _equip_chars: List[PartyCharacter] = [
        MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
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
        2911: """ Item #1: A “Status Protector”!\n It can prevent weird things from\n happening to you.[await][pause] I'll sell it to\n you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Status Protector”.\n It can prevent weird things from\n happening to you.[await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Status Protector”.\n It can prevent weird things from\n happening to you.[await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class JumpShoes(Accessory, RegularEquip):
    _item_id: int = 76
    _description: str = "Use jump attacks\x01against any foe"
    _tier: int = 5
    _order: int = 118
    _equip_chars: List[PartyCharacter] = [MARIO]
    _speed: int = 2
    _defense: int = 1
    _magic_attack: int = 5
    _magic_defense: int = 1
    _price: int = 30
    _model: Type[ItemNPC] = ShoesNPC


class SafetyRing(Accessory, RegularEquip):
    _item_id: int = 77
    _description: str = "Guards against\x01mortal blows."
    _tier: int = 1
    _order: int = 122
    _equip_chars: List[PartyCharacter] = [
        MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
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
        2911: """ Item #1: A “Protective Charm”!\n Never go into battle without it.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Protective Charm”.\n Never go into battle without it.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Protective Charm”.\n Never go into battle without it.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class Amulet(Accessory, RegularEquip):
    _item_id: int = 78
    _description: str = "Great item,\x01bad smell!"
    _tier: int = 2
    _order: int = 108
    _equip_chars: List[PartyCharacter] = [
        MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
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
        2911: """ Item #1: A “Stinky Charm”!\n It'll help you weather the elements.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Stinky Charm”.\n It'll help you weather the elements.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Stinky Charm”.\n It'll help you weather the elements.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class ScroogeRing(Accessory, RegularEquip):
    _item_id: int = 79
    _description: str = "Cuts FP use\x01in half\x01during battle"
    _tier: int = 3
    _order: int = 123
    _equip_chars: List[PartyCharacter] = [
        MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _price: int = 50
    _frog_coin_item: bool = True
    _model: Type[ItemNPC] = RingNPC
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Mage Totem”!\n It might help with spellcasting.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Mage Totem”.\n It might help with spellcasting.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Mage Totem”.\n It might help with spellcasting.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class ExpBooster(Accessory, RegularEquip):
    _item_id: int = 80
    _description: str = "Doubles Exp.\x01when equipped"
    _tier: int = 3
    _order: int = 113
    _equip_chars: List[PartyCharacter] = [
        MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _price: int = 22
    _frog_coin_item: bool = True
    _original_effect_type: EffectType = EffectType.FEW_EFFECTS
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Training Device”!\n This'll make you strong in no time![await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Training Device”.\n This'll make you strong in no time![await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Training Device”.\n This'll make you strong in no time![await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class AttackScarf(Accessory, SpecialEquip):
    _item_id: int = 81
    _description: str = "So comfy it~ll\x01make you jump!"
    _tier: int = 1
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
        2911: """ Item #1: A “Jumper's Scarf”!\n It could save your life![await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Jumper's Scarf”.\n It could save your life![await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Jumper's Scarf”.\n It could save your life![await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class RareScarf(Accessory, RegularEquip):
    _item_id: int = 82
    _description: str = "Raises defense\x01power!"
    _tier: int = 3
    _order: int = 120
    _equip_chars: List[PartyCharacter] = [
        MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _defense: int = 15
    _magic_defense: int = 15
    _price: int = 150
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: An “Unusual Garment”!\n I don't see these around often.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: An “Unusual Garment”.\n I don't see these around often.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: An “Unusual Garment”.\n I don't see these around often.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }

    @property
    def primary_stats(self) -> List[EquipStats]:
        """Primary stats of this item, depending on the type."""
        return [EquipStats.DEFENSE, EquipStats.MAGIC_DEFENSE]


class BtubRing(Accessory, RegularEquip):
    _item_id: int = 83
    _description: str = "You~ll win her\x01heart with this!"
    _tier: int = 2
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


class AntidotePin(Accessory, RegularEquip):
    _item_id: int = 84
    _description: str = "Prevents\x01poison damage"
    _tier: int = 3
    _order: int = 109
    _equip_chars: List[PartyCharacter] = [
        MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _defense: int = 2
    _magic_defense: int = 2
    _status_immunities: List[Status] = [Status.POISON]
    _price: int = 28
    _original_effect_type: EffectType = EffectType.STATUS_PROTECTION
    _model: Type[ItemNPC] = BroochNPC


class WakeUpPin(Accessory, RegularEquip):
    _item_id: int = 85
    _description: str = "Prevents Mute \x9c\x01Sleep attacks"
    _tier: int = 3
    _order: int = 127
    _equip_chars: List[PartyCharacter] = [
        MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
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
    _item_id: int = 86
    _description: str = "Prevents Fear\x01attacks"
    _tier: int = 3
    _order: int = 114
    _equip_chars: List[PartyCharacter] = [
        MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _defense: int = 5
    _magic_defense: int = 5
    _status_immunities: List[Status] = [Status.FEAR]
    _price: int = 130
    _original_effect_type: EffectType = EffectType.STATUS_PROTECTION
    _model: Type[ItemNPC] = BroochNPC


class TrueformPin(Accessory, RegularEquip):
    _item_id: int = 87
    _description: str = "You won~t be\x01turned into\x01Mushrooms or\x01Scarecrows!"
    _tier: int = 3
    _order: int = 126
    _equip_chars: List[PartyCharacter] = [
        MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
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
    _item_id: int = 88
    _description: str = "Doubles the\x01coins you win\x01in battle"
    _tier: int = 4
    _order: int = 112
    _equip_chars: List[PartyCharacter] = [MARIO]
    _price: int = 36
    _frog_coin_item: bool = True
    _original_effect_type: EffectType = EffectType.FEW_EFFECTS
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Fortune Charm”!\n It's sure to make you very rich.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Fortune Charm”.\n It's sure to make you very rich.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Fortune Charm”.\n It's sure to make you very rich.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class GhostMedal(Accessory, SpecialEquip):
    _item_id: int = 89
    _description: str = "Raises defense\x01while attacking"
    _tier: int = 2
    _order: int = 116
    _equip_chars: List[PartyCharacter] = [
        MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _temp_buffs: List[ItemTempBuff] = [
        ItemTempBuff.DEFENSE,
        ItemTempBuff.MAGIC_DEFENSE,
    ]
    _price: int = 1600
    _original_effect_type: EffectType = EffectType.BUFFS
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _special_equip: bool = True
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Scavenger's Prize”!\n It resembles a medal of honor.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Scavenger's Prize”.\n It resembles a medal of honor.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Scavenger's Prize”.\n It resembles a medal of honor.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class JinxBelt(Accessory, SpecialEquip):
    _item_id: int = 90
    _description: str = "Jinx~s emblem\x01of power!"
    _tier: int = 1
    _order: int = 117
    _equip_chars: List[PartyCharacter] = [
        MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 12
    _attack: int = 27
    _defense: int = 27
    _prevent_ko: bool = True
    _special_equip: bool = True
    _price: int = 1998
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Martial Sash”!\n A true fighter would love this.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Martial Sash”.\n A true fighter would love this.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Martial Sash”.\n A true fighter would love this.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class Feather(Accessory, RegularEquip):
    _item_id: int = 91
    _description: str = "Speed up by 20"
    _tier: int = 2
    _order: int = 115
    _equip_chars: List[PartyCharacter] = [
        MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 20
    _defense: int = 5
    _magic_defense: int = 5
    _price: int = 666
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _model: Type[ItemNPC] = FeatherNPC
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Fluttering Quill”!\n It's pretty exotic, isn't it?[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Fluttering Quill”.\n It's pretty exotic, isn't it?[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Fluttering Quill”.\n It's pretty exotic, isn't it?[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }

    @property
    def primary_stats(self) -> List[EquipStats]:
        """Primary stats of this item, depending on the type."""
        return [EquipStats.Speed]


class TroopaPin(Accessory, RegularEquip):
    _item_id: int = 92
    _description: str = 'Grants "Troopa#\x01confidence!'
    _tier: int = 2
    _order: int = 125
    _equip_chars: List[PartyCharacter] = [
        MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 20
    _temp_buffs: List[ItemTempBuff] = [
        ItemTempBuff.ATTACK,
        ItemTempBuff.MAGIC_ATTACK,
    ]
    _price: int = 1000
    _original_effect_type: EffectType = EffectType.BUFFS
    _model: Type[ItemNPC] = BroochNPC
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Military Decoration”!\n I wonder what powers it bestows?[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Military Decoration”.\n I wonder what powers it bestows?[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Military Decoration”.\n I wonder what powers it bestows?[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class SignalRing(Accessory, RegularEquip):
    _item_id: int = 93
    _description: str = "Noise indicates\x01a hidden chest."
    _tier: int = 4
    _order: int = 124
    _equip_chars: List[PartyCharacter] = [
        MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 10
    _price: int = 600
    _model: Type[ItemNPC] = RingNPC
    _unique: ItemUnique = ItemUnique.ALWAYS
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Treasure Beacon”!\n I wonder what it can help you find?[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Treasure Beacon”.\n I wonder what it can help you find?[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Treasure Beacon”.\n I wonder what it can help you find?[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class QuartzCharm(Accessory, SpecialEquip):
    _item_id: int = 94
    _description: str = "Shining source\x01of power!"
    _tier: int = 1
    _order: int = 119
    _equip_chars: List[PartyCharacter] = [
        MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _prevent_ko: bool = True
    _temp_buffs: List[ItemTempBuff] = [
        ItemTempBuff.ATTACK,
        ItemTempBuff.MAGIC_ATTACK,
        ItemTempBuff.DEFENSE,
        ItemTempBuff.MAGIC_DEFENSE,
    ]
    _price: int = 7
    _original_effect_type: EffectType = EffectType.BUFFS
    _model: Type[ItemNPC] = RingNPC
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY
    _special_equip: bool = True
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Crystal Ring”!\n It could save your life![await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Crystal Ring”.\n It could save your life![await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Crystal Ring”.\n It could save your life![await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class Mushroom(RegularItem):
    _item_id: int = 96
    _description: str = "Recovers 30 HP"
    _order: int = 15
    _consumable: bool = True
    _price: int = 4
    _tier: int = 5
    _model: Type[ItemNPC] = RedMushroom
    _room_service: str = "Mushroom........"


class MidMushroom(RegularItem):
    _item_id: int = 97
    _description: str = "Recovers 80 HP"
    _order: int = 13
    _consumable: bool = True
    _price: int = 20
    _tier: int = 4
    _model: Type[ItemNPC] = GreenMushroom
    _room_service: str = "Mid Mushroom...."


class MaxMushroom(RegularItem):
    _item_id: int = 98
    _description: str = "Recovers all HP"
    _order: int = 11
    _consumable: bool = True
    _price: int = 78
    _tier: int = 3
    _model: Type[ItemNPC] = YellowMushroom
    _room_service: str = "Max Mushroom...."


class HoneySyrup(RegularItem):
    _item_id: int = 99
    _description: str = "Recovers 10 FP"
    _model: Type[ItemNPC] = RedSyrup
    _order: int = 8
    _consumable: bool = True
    _price: int = 10
    _tier: int = 5
    _room_service: str = "Honey Syrup......"


class MapleSyrup(RegularItem):
    _item_id: int = 100
    _description: str = "Recovers 40 FP"
    _model: Type[ItemNPC] = GreenSyrup
    _order: int = 10
    _consumable: bool = True
    _price: int = 30
    _tier: int = 4
    _room_service: str = "Maple Syrup......"


class RoyalSyrup(RegularItem):
    _item_id: int = 101
    _description: str = "Recovers all FP"
    _model: Type[ItemNPC] = YellowSyrup
    _order: int = 21
    _consumable: bool = True
    _price: int = 101
    _tier: int = 3
    _room_service: str = "Royal Syrup......"


class PickMeUp(RegularItem):
    _item_id: int = 102
    _description: str = "Revives downed\x01allies"
    _order: int = 17
    _consumable: bool = True
    _price: int = 5
    _tier: int = 4
    _room_service: str = "Pick Me Up......."
    _model: Type[ItemNPC] = StarDrink


class AbleJuice(RegularItem):
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
    _tier: int = 5
    _room_service: str = "Able Juice........"


class Bracer(RegularItem):
    _item_id: int = 104
    _description: str = "Raises ally~s\x01def. in battle"
    _order: int = 2
    _consumable: bool = True
    _temp_buffs: List[ItemTempBuff] = [
        ItemTempBuff.DEFENSE,
        ItemTempBuff.MAGIC_DEFENSE,
    ]
    _price: int = 50
    _frog_coin_item: bool = True
    _tier: int = 4
    _rank_value: int = 10
    _room_service: str = "Bracer..........."
    _model: Type[ItemNPC] = DDrink


class Energizer(RegularItem):
    _item_id: int = 105
    _description: str = "Raises ally~s\x01battle power\x01during battle"
    _order: int = 5
    _consumable: bool = True
    _temp_buffs: List[ItemTempBuff] = [
        ItemTempBuff.ATTACK,
        ItemTempBuff.MAGIC_ATTACK,
    ]
    _price: int = 50
    _frog_coin_item: bool = True
    _tier: int = 4
    _room_service: str = "Energizer........"
    _model: Type[ItemNPC] = PDrink


class YoshiAde(RegularItem):
    _item_id: int = 106
    _description: str = "Power raised\x01during battle"
    _model: Type[ItemNPC] = GreenJuice
    _order: int = 23
    _consumable: bool = True
    _temp_buffs: List[ItemTempBuff] = [
        ItemTempBuff.ATTACK,
        ItemTempBuff.MAGIC_ATTACK,
        ItemTempBuff.DEFENSE,
        ItemTempBuff.MAGIC_DEFENSE,
    ]
    _price: int = 200
    _tier: int = 3
    _room_service: str = "Yoshi Ade........"


class RedEssence(RegularItem):
    _item_id: int = 107
    _description: str = "Become invincible\x01for 3 turns"
    _model: Type[ItemNPC] = RedJuice
    _order: int = 19
    _consumable: bool = True
    _status_immunities: List[Status] = [Status.INVINCIBLE]
    _price: int = 400
    _tier: int = 1
    _room_service: str = "Red Essence......"


class KerokeroCola(RegularItem):
    _item_id: int = 108
    _description: str = "All members\x01recover fully"
    _order: int = 9
    _consumable: bool = True
    _price: int = 400
    _tier: int = 1
    _room_service: str = "KerokeroCola....."
    _model: Type[ItemNPC] = FrogDrink


class YoshiCookie(RegularItem):
    _item_id: int = 109
    _description: str = "Summons Yoshi\x01during battle"
    _order: int = 26
    _consumable: bool = True
    _price: int = 100
    _model: Type[ItemNPC] = Cookie
    _tier: int = 5
    _room_service: str = "Yoshi Cookie......"


class PureWater(RegularItem):
    _item_id: int = 110
    _description: str = "Defeats ghosts\x01in a wink"
    _model: Type[ItemNPC] = BlueSyrup
    _order: int = 30
    _consumable: bool = True
    _price: int = 150
    _tier: int = 4
    _room_service: str = "Pure Water......."


class SleepyBomb(RegularItem):
    _item_name: str = "Sleepy Bomb"
    _item_id: int = 111
    _description: str = "Puts enemies\x01to sleep"
    _order: int = 32
    _consumable: bool = True
    _status_immunities: List[Status] = [Status.SLEEP]
    _model: Type[ItemNPC] = YellowBomb
    _price: int = 25
    _frog_coin_item: bool = True
    _tier: int = 4
    _room_service: str = "Sleepy Bomb......"


class BadMushroom(RegularItem):
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
    _item_id: int = 115
    _description: str = "Raise FP by 1"
    _order: int = 43
    _consumable: bool = True
    _price: int = 200
    _tier: int = 4
    _room_service: str = "Flower Tab......."


class FlowerJar(RegularItem):
    _item_id: int = 116
    _description: str = "Raise FP by 3"
    _order: int = 42
    _consumable: bool = True
    _price: int = 600
    _tier: int = 3
    _room_service: str = "Flower Jar......."


class FlowerBox(RegularItem):
    _item_id: int = 117
    _description: str = "Raise FP by 5"
    _order: int = 41
    _consumable: bool = True
    _price: int = 1000
    _tier: int = 2
    _room_service: str = "Flower Box......."


class YoshiCandy(RegularItem):
    _item_id: int = 118
    _description: str = "Heals 100 HP"
    _order: int = 25
    _consumable: bool = True
    _price: int = 140
    _model: Type[ItemNPC] = GreenCandy
    _tier: int = 4
    _room_service: str = "Yoshi Candy......"


class FroggieDrink(RegularItem):
    _item_id: int = 119
    _description: str = "Party heals\x0130 HP"
    _order: int = 7
    _consumable: bool = True
    _price: int = 16
    _tier: int = 4
    _room_service: str = "FroggieDrink......"
    _model: Type[ItemNPC] = YellowMusicDrink


class MukuCookie(RegularItem):
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
    _item_id: int = 121
    _description: str = "Party heals\x0180 HP"
    _order: int = 4
    _consumable: bool = True
    _price: int = 48
    _tier: int = 3
    _room_service: str = "Elixir............."
    _model: Type[ItemNPC] = BlueMusicDrink


class Megalixir(RegularItem):
    _item_id: int = 122
    _description: str = "Party heals\x01150 HP"
    _order: int = 12
    _consumable: bool = True
    _price: int = 120
    _tier: int = 2
    _room_service: str = "Megalixir.........."
    _model: Type[ItemNPC] = RedMusicDrink


class SeeYa(RegularItem):
    _item_id: int = 123
    _description: str = "Run away from\x01battles"
    _order: int = 39
    _price: int = 250
    _frog_coin_item: bool = True
    _tier: int = 3
    _unique: ItemUnique = ItemUnique.ALWAYS
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: An “Eject Button”!\n Sounds useful in a pinch, doesn't\n it?[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: An “Eject Button”.\n Sounds useful in a pinch, doesn't\n it?[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: An “Eject Button”.\n Sounds useful in a pinch, doesn't\n it?[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class TempleKey(KeyItem):
    _item_id: int = 124
    _order: int = 150
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Key
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Golden Key”!\n I wonder what it opens?[await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Golden Key”.\n I wonder what it opens?[await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Golden Key”.\n I wonder what it opens?[await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class GoodieBag(RegularItem):
    _item_id: int = 125
    _order: int = 35
    _price: int = 1110
    _tier: int = 4
    _unique: ItemUnique = ItemUnique.ALWAYS
    _description: str = "It's packed\x01full of coins"
    _model: Type[ItemNPC] = SmallCoin
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Coin Sack”!\n It could make you rich![await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Coin Sack”.\n It could make you rich![await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Coin Sack”.\n It could make you rich![await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class EarlierTimes(RegularItem):
    _item_id: int = 126
    _description: str = "Use it to start\x01a battle over"
    _order: int = 34
    _price: int = 375
    _frog_coin_item: bool = True
    _tier: int = 5
    _unique: ItemUnique = ItemUnique.ALWAYS
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Reset Button”!\n Sounds useful in a pinch, doesn't\n it?[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Reset Button”.\n Sounds useful in a pinch, doesn't\n it?[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Reset Button”.\n Sounds useful in a pinch, doesn't\n it?[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class FreshenUp(RegularItem):
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
    _tier: int = 3
    _room_service: str = "Freshen Up........"


class RareFrogCoin(KeyItem):
    _item_id: int = 128
    _order: int = 144
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = SmallFrogCoin
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Green Coin”!\n It looks different from most Frog\n Coins.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Green Coin”.\n It looks different from most Frog\n Coins.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Green Coin”.\n It looks different from most Frog\n Coins.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class Wallet(RegularItem):
    _item_id: int = 129
    _description: str = "A fat wallet"
    _order: int = 152
    _price: int = 246
    _model: Type[ItemNPC] = SmallCoin
    _tier: int = 5
    _unique: ItemUnique = ItemUnique.ALWAYS
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Coin Sack”!\n It looks like it belongs to someone.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Coin Sack”.\n It looks like it belongs to someone.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Coin Sack”.\n It looks like it belongs to someone.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class CricketPie(KeyItem):
    _item_id: int = 130
    _order: int = 138
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Cookie
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Baked Pastry”!\n Sorta makes you curious, doesn't\n it?[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Baked Pastry”.\n Sorta makes you curious, doesn't\n it?[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Baked Pastry”.\n Sorta makes you curious, doesn't\n it?[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class RockCandy(RegularItem):
    _item_name: str = "Rock Candy"
    _item_id: int = 131
    _description: str = "Attack all\x01enemies"
    _model: Type[ItemNPC] = BlueCandy
    _order: int = 31
    _consumable: bool = True
    _price: int = 400
    _tier: int = 1
    _room_service: str = "Rock Candy......"


class CastleKey1(KeyItem):
    _item_id: int = 132
    _order: int = 135
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Key
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Golden Key”!\n I wonder what it opens?[await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Golden Key”.\n I wonder what it opens?[await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Golden Key”.\n I wonder what it opens?[await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class CastleKey2(KeyItem):
    _item_id: int = 134
    _order: int = 136
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Key
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Golden Key”!\n I wonder what it opens?[await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Golden Key”.\n I wonder what it opens?[await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Golden Key”.\n I wonder what it opens?[await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class BambinoBomb(KeyItem):
    _item_id: int = 135
    _order: int = 136
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = MicroBombItem


class SheepAttack(RegularItem):
    _item_id: int = 136
    _description: str = "Baah, baah..."
    _order: int = 40
    _price: int = 150
    _is_subitem: bool = True
    _tier: int = 3
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Egg
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: “Shepherd's Bait”!\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class CarboCookie(RegularItem):
    _item_id: int = 137
    _description: str = "Kid's love 'em"
    _order: int = 134
    _unique: ItemUnique = ItemUnique.ALWAYS
    _is_subitem: bool = True
    _model: Type[ItemNPC] = Cookie
    _price: int = 2
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Trade Item”! It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }

    def __init__(self, world: Optional[GameWorld]):
        super().__init__(world)
        if world is None:
            return
        if world.settings.is_flag_value(
            FireworksSetting, FireworksOptions.shuffle1
        ) or world.settings.is_flag_value(
            FireworksSetting, FireworksOptions.progressive
        ):
            self.set_price(0)
            self.set_description("")


class ShinyStone(RegularItem):
    _item_id: int = 138
    _order: int = 148
    _description: str = "A pretty stone!"
    _is_subitem: bool = True
    _unique: ItemUnique = ItemUnique.ALWAYS
    _price: int = 4
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Trade Item”! It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }

    def __init__(self, world: Optional[GameWorld]):
        super().__init__(world)
        if world is None:
            return
        if world.settings.is_flag_value(
            FireworksSetting, FireworksOptions.shuffle1
        ) or world.settings.is_flag_value(
            FireworksSetting, FireworksOptions.progressive
        ):
            self.set_price(0)
            self.set_description("")


class RoomKey(KeyItem):
    _item_id: int = 140
    _order: int = 145
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Key
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Golden Key”!\n I wonder what it opens?[await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Golden Key”.\n I wonder what it opens?[await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Golden Key”.\n I wonder what it opens?[await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class ElderKey(KeyItem):
    _item_id: int = 141
    _order: int = 140
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Key
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Golden Key”!\n I wonder what it opens?[await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Golden Key”.\n I wonder what it opens?[await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Golden Key”.\n I wonder what it opens?[await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class ShedKey(KeyItem):
    _item_id: int = 142
    _order: int = 147
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Key
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Golden Key”!\n I wonder what it opens?[await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Golden Key”.\n I wonder what it opens?[await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Golden Key”.\n I wonder what it opens?[await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class LambsLure(RegularItem):
    _item_id: int = 143
    _description: str = "Baa, baa..."
    _order: int = 36
    _price: int = 40
    _unique: ItemUnique = ItemUnique.ALWAYS
    _is_subitem: bool = True
    _model: Type[ItemNPC] = Egg
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: “Shepherd's Bait”!\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class FrightBomb(RegularItem):
    _item_name: str = "Fright Bomb"
    _item_id: int = 144
    _description: str = "Inflict fear\x01on one enemy"
    _model: Type[ItemNPC] = GreenBomb
    _order: int = 28
    _consumable: bool = True
    _status_immunities: List[Status] = [Status.FEAR]
    _price: int = 100
    _tier: int = 3
    _room_service: str = "Fright Bomb......"


class MysteryEgg(RegularItem):
    _item_id: int = 145
    _description: str = "A product of\x01pure love..."
    _order: int = 38
    _is_subitem: bool = True
    _price: int = 200
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Egg
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: “Shepherd's Bait”!\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class BeetleBox(RegularItem):
    _item_id: int = 146
    _order: int = 130
    _unique: ItemUnique = ItemUnique.ALWAYS


class BeetleBox2(RegularItem):
    _item_id: int = 147
    _order: int = 131
    _unique: ItemUnique = ItemUnique.ALWAYS


class LuckyJewel(RegularItem):
    _item_id: int = 148
    _description: str = "Summons Luck\x01at will"
    _order: int = 37
    _price: int = 100
    _unique: ItemUnique = ItemUnique.ALWAYS
    _tier: int = 5
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: An “Lucky Jewel”!\n It’s sure to bring you plenty of\n good luck.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: An “Lucky Jewel”.\n It’s sure to bring you plenty of\n good luck.[await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: An “Lucky Jewel”.\n It’s sure to bring you plenty of\n good luck.[await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class SopranoCard(KeyItem):
    _item_id: int = 150
    _order: int = 149
    _shuffle_as_key_item: bool = True
    _is_subitem: bool = True
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Card
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Musical Card”!\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class AltoCard(KeyItem):
    _item_id: int = 151
    _order: int = 129
    _shuffle_as_key_item: bool = True
    _is_subitem: bool = True
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Card
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Musical Card”!\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class TenorCard(KeyItem):
    _item_id: int = 152
    _order: int = 151
    _shuffle_as_key_item: bool = True
    _is_subitem: bool = True
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Card
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Musical Card”!\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class Crystalline(RegularItem):
    _item_id: int = 153
    _description: str = "Raises party's\x01Defense in\x01battle"
    _order: int = 3
    _consumable: bool = True
    _temp_buffs: List[ItemTempBuff] = [
        ItemTempBuff.DEFENSE,
        ItemTempBuff.MAGIC_DEFENSE,
    ]
    _price: int = 125
    _frog_coin_item: bool = True
    _tier: int = 2
    _room_service: str = "Crystalline......."
    _model: Type[ItemNPC] = DDrink


class PowerBlast(RegularItem):
    _item_id: int = 154
    _description: str = "Raises party's\x01Attack Power\x01in battle"
    _order: int = 18
    _consumable: bool = True
    _temp_buffs: List[ItemTempBuff] = [
        ItemTempBuff.ATTACK,
        ItemTempBuff.MAGIC_ATTACK,
    ]
    _price: int = 125
    _frog_coin_item: bool = True
    _tier: int = 2
    _room_service: str = "Power Blast......"
    _model: Type[ItemNPC] = PDrink


class WiltShroom(RegularItem):
    _item_id: int = 155
    _description: str = "It's wilted..."
    _order: int = 22
    _consumable: bool = True
    _price: int = 8
    _tier: int = 5
    _model: Type[ItemNPC] = Banana
    _room_service: str = "Wilt Shroom......"


class RottenMush(RegularItem):
    _item_id: int = 156
    _description: str = "Eeew,\x01it's rotten!"
    _order: int = 20
    _consumable: bool = True
    _price: int = 4
    _tier: int = 5
    _model: Type[ItemNPC] = Banana
    _room_service: str = "Rotten Mush....."


class MoldyMush(RegularItem):
    _item_id: int = 157
    _description: str = "Gross!\x01There's mold\x01growing on it."
    _order: int = 14
    _consumable: bool = True
    _price: int = 2
    _tier: int = 5
    _model: Type[ItemNPC] = Banana
    _room_service: str = "Moldy Mush......."


class Seed(KeyItem):
    _item_id: int = 158
    _order: int = 146
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Berry
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Mysterious Seed”!\n I wonder what will grow from it?[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Mysterious Seed”.\n I wonder what will grow from it?[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Mysterious Seed”.\n I wonder what will grow from it?[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class Fertilizer(KeyItem):
    _item_id: int = 159
    _order: int = 141
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Bag of Dirt”!\n It seems different from the soil\n I dug it out of.[await][pause] I'll sell it to you\n for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Bag of Dirt”.\n It seems different from the soil\n I dug it out of.[await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Bag of Dirt”.\n It seems different from the soil\n I dug it out of.[await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class WasteBasket(Item):
    _item_id: int = 160


class BigBooFlag(KeyItem):
    _item_id: int = 161
    _order: int = 132
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _model: Type[ItemNPC] = Card
    _unique: ItemUnique = ItemUnique.ALWAYS
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: An “Invisible Flag”!\n I wonder if someone is looking for\n this?[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: An “Invisible Flag”.\n I wonder if someone is looking for\n this?[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: An “Invisible Flag”.\n I wonder if someone is looking for\n this?[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class DryBonesFlag(KeyItem):
    _item_id: int = 162
    _order: int = 139
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _model: Type[ItemNPC] = Card
    _unique: ItemUnique = ItemUnique.ALWAYS
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: An “Invisible Flag”!\n I wonder if someone is looking for\n this?[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: An “Invisible Flag”.\n I wonder if someone is looking for\n this?[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: An “Invisible Flag”.\n I wonder if someone is looking for\n this?[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class GreaperFlag(KeyItem):
    _item_id: int = 163
    _order: int = 143
    _shuffle_as_key_item: bool = True
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _model: Type[ItemNPC] = Card
    _unique: ItemUnique = ItemUnique.ALWAYS
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: An “Invisible Flag”!\n I wonder if someone is looking for\n this?[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: An “Invisible Flag”.\n I wonder if someone is looking for\n this?[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: An “Invisible Flag”.\n I wonder if someone is looking for\n this?[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class CricketJam(KeyItem):
    _item_id: int = 166
    _order: int = 137
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _model: Type[ItemNPC] = GreenJuice
    _shuffle_as_key_item: bool = True
    _unique: ItemUnique = ItemUnique.ALWAYS
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: “Green Jelly”!\n Sorta makes you curious, doesn't\n it?[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: “Green Jelly”.\n Sorta makes you curious, doesn't\n it?[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: “Green Jelly”.\n Sorta makes you curious, doesn't\n it?[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class Fireworks(RegularItem):
    _item_id: int = 172
    _description: str = "A gorgeous\x01firework"
    _unique: ItemUnique = ItemUnique.ALWAYS
    _chest_event: int = 3099
    _npc_event: int = 184
    _is_subitem: bool = True
    _overworld_event: int = 3112
    _overworld_midas_event: int = 3398
    _price: int = 500
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Trade Item”! It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }

    def __init__(self, world: Optional[GameWorld]):
        super().__init__(world)
        if world is None:
            return
        if world.settings.is_flag_value(
            FireworksSetting, FireworksOptions.shuffle1
        ) or world.settings.is_flag_value(
            FireworksSetting, FireworksOptions.progressive
        ):
            self.set_price(0)
            self.set_description("")
        if world.settings.is_flag_value(FireworksSetting, FireworksOptions.shuffle1):
            self.set_shuffle_as_key_item(True)
            self.set_subitem(False)


class BrightCard(KeyItem):
    _item_id: int = 174
    _model: Type[ItemNPC] = Card
    _order: int = 133
    _unique: ItemUnique = ItemUnique.ALWAYS
    _shuffle_as_key_item: bool = True
    _tier: int = 1
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Shiny Card”!\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Shiny Card”.\n It's sure to bring you an air of\n prestige.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Shiny Card”.\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class Mushroom2(RegularItem):
    _item_id: int = 175
    _description: str = "Recoers 30 HP,\x01but..."
    _order: int = 16
    _consumable: bool = True
    _status_immunities: List[Status] = [Status.MUSHROOM]
    _price: int = 4
    _tier: int = 5
    _model: Type[ItemNPC] = RedMushroom
    _room_service: str = "Mushroom........"


class StarEgg(RegularItem):
    _item_id: int = 176
    _description: str = "Reusable battle\x01item"
    _order: int = 33
    _price: int = 700
    _tier: int = 1
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Egg
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: An “Adorable Bomb”!\n Seems like it'll last a long time![await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: An “Adorable Bomb”.\n Seems like it'll last a long time![await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: An “Adorable Bomb”.\n Seems like it'll last a long time![await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class ProgressiveCard(ProgressiveItem, KeyItem):
    _item_id: int = 195
    _model: Type[ItemNPC] = Card
    _shuffle_type: ItemShuffleType = ItemShuffleType.REQUIRED
    _unique: ItemUnique = ItemUnique.ALWAYS
    _chest_event: int = 3086
    _npc_event: int = 3097
    _overworld_event: int = 3110
    _overworld_midas_event: int = 3396
    _is_key: bool = True
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Musical Card”!\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class ProgressiveEgg(ProgressiveItem):
    _item_id: int = 196
    _model: Type[ItemNPC] = Egg
    _unique: ItemUnique = ItemUnique.ALWAYS
    _tier: int = 2
    _chest_event: int = 3087
    _npc_event: int = 3098
    _overworld_event: int = 3111
    _overworld_midas_event: int = 3397
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: “Shepherd's Bait”!\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class ProgressiveFireworks(ProgressiveItem):
    _item_id: int = 197
    _unique: ItemUnique = ItemUnique.ALWAYS
    _chest_event: int = 3100
    _npc_event: int = 185
    _overworld_event: int = 3113
    _overworld_midas_event: int = 3399
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Trade Item”! It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class MimicFightInitiator1(MimicFightChestAssignment):
    _item_id: int = 211
    _unique: ItemUnique = ItemUnique.ALWAYS
    _tier: int = 1
    _chest_event: int = 3124


class MimicFightInitiator2(MimicFightChestAssignment):
    _item_id: int = 212
    _unique: ItemUnique = ItemUnique.ALWAYS
    _tier: int = 1
    _chest_event: int = 3126


class MimicFightInitiator3(MimicFightChestAssignment):
    _item_id: int = 213
    _unique: ItemUnique = ItemUnique.ALWAYS
    _tier: int = 1
    _chest_event: int = 2493


class Coins10(Coins):
    _item_id: int = 193
    _tier: int = 1
    _overworld_event: int = 3146
    _overworld_midas_event: int = 2818
    _model: Type[ItemNPC] = BigCoin
    _amount = 10

    def __init__(self, world):
        super().__init__(10, world)


class Coins1(Coins):
    _item_id: int = 194
    _tier: int = 1
    _overworld_event: int = 1293
    _overworld_midas_event: int = 2819
    # _model: Type[ItemNPC] = SmallCoin
    # _amount = 1

    def __init__(self, world):
        super().__init__(1, world)


class Coins5(Coins):
    _amount = 5

    def __init__(self, world):
        super().__init__(5, world)


class Coins8(Coins):
    _amount = 8

    def __init__(self, world):
        super().__init__(8, world)


class Coins20(Coins):
    _amount = 20

    def __init__(self, world):
        super().__init__(20, world)


class Coins50(Coins):
    _amount = 50

    def __init__(self, world):
        super().__init__(50, world)


class Coins100(Coins):
    _amount = 100

    def __init__(self, world):
        super().__init__(100, world)


class Coins150(Coins):
    _amount = 150

    def __init__(self, world):
        super().__init__(150, world)


class Beetlemania(MiscReward):
    _item_id: int = 164
    _unique: ItemUnique = ItemUnique.ALWAYS
    _model: Type[ItemNPC] = Beetle
    _tier: int = 1
    _chest_event: int = 162
    _npc_event: int = 161
    _overworld_event: int = 3109
    _overworld_midas_event: int = 3395
    _price: int = 500
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Handheld Game”!\n Sounds pretty fun, doesn't it?[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Handheld Game”.\n Sounds pretty fun, doesn't it?[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Handheld Game”.\n Sounds pretty fun, doesn't it?[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class SlotMachineChest(MiscReward):
    _item_id: int = 214
    _tier: int = 2
    _unique: ItemUnique = ItemUnique.BALANCED_ONLY


class InfiniteCoins(MiscReward):
    _item_id: int = 240
    _unique: ItemUnique = ItemUnique.ALWAYS
    _chest_event: int = 3074
    _tier: int = 2
    _chest_70a7_lower: int = 0
    _chest_70a7_upper: int = 15


class StarPiece1(StarPiece):
    _hint_bit: Flag = SIGNAL_RING_STAR_PIECE_1


class StarPiece2(StarPiece):
    _hint_bit: Flag = SIGNAL_RING_STAR_PIECE_2


class StarPiece3(StarPiece):
    _hint_bit: Flag = SIGNAL_RING_STAR_PIECE_3


class StarPiece4(StarPiece):
    _hint_bit: Flag = SIGNAL_RING_STAR_PIECE_4


class StarPiece5(StarPiece):
    _hint_bit: Flag = SIGNAL_RING_STAR_PIECE_5


class StarPiece6(StarPiece):
    _hint_bit: Flag = SIGNAL_RING_STAR_PIECE_6


class StarPiece7(StarPiece):
    _hint_bit: Flag = SIGNAL_RING_STAR_PIECE_7


class Nothing(MiscReward):
    _chest_event: int = E3081_YOU_MISSED
    _npc_event: int = E0256_RETURN
    _model: Type[ItemNPC] = Empty
    _overworld_midas_event: int = E0256_RETURN
    _overworld_event: int = E0256_RETURN


class Flower(MiscReward):
    _item_id: int = 198
    _tier: int = 1
    _model: Type[ItemNPC] = FlowerNPC
    _chest_70a7_upper: int = 2
    _packet: int = 35
    _chest_event: int = 3072
    _overworld_event: int = 1801
    _overworld_midas_event: int = 2817


class RecoveryMushroom(MiscReward):
    _item_id: int = 199
    _tier: int = 1
    _packet: int = 36
    _chest_event: int = 3072
    _overworld_event: int = 2822
    _npc_event: int = 397
    _overworld_midas_event: int = 2822
    _model: Type[ItemNPC] = RecoveryMushroomNPC


class FrogCoin(MiscReward):
    _item_id: int = 200
    _tier: int = 1
    _model: Type[ItemNPC] = FrogCoinNPC
    _chest_70a7_upper: int = 3
    _chest_event: int = 3072
    _npc_event: int = 157
    _overworld_event: int = 3238
    _overworld_midas_event: int = 2816


class MultiFrogCoin(MiscReward):
    _item_id: int = 215
    _tier: int = 2
    _amount: int = 0
    _multiplier: int = 0
    _chest_event: int = 3091
    _quick_chest_event: int = 3082
    _model: Type[ItemNPC] = FrogCoinNPC
    _npc_event: int = 158
    _chest_70a7_upper: int = 0

    @property
    def amount(self) -> UInt16:
        return UInt16(self._amount)

    def _set_amount(self, amount: int) -> None:
        self._amount = amount

    @property
    def multiplier(self) -> UInt8:
        return UInt8(self._multiplier)

    def _set_multiplier(self, multiplier: int) -> None:
        self._multiplier = multiplier

    def get_chest_event(self, parent):
        if parent == 246:
            return 3406
        elif parent == 245:
            return 3407
        elif parent == 244:
            return 3408
        elif parent == 243:
            return 3409
        elif parent == 242:
            return 3410
        else:
            return 3082

    @property
    def chest_event(self):
        raise Exception("use get_chest_event for multifrogcoins")

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
    _amount = 2

    def __init__(self, world):
        super().__init__(2, world)


class FrogCoins3(MultiFrogCoin):
    _amount = 3

    def __init__(self, world):
        super().__init__(3, world)


class FrogCoins10(MultiFrogCoin):
    _amount = 10

    def __init__(self, world):
        super().__init__(10, world)


class FrogCoins20(MultiFrogCoin):
    _amount = 20

    def __init__(self, world):
        super().__init__(20, world)


class YouMissed(MiscReward):
    _item_id: int = 210
    _tier: int = 1
    _chest_event: int = 3081


class BanditsWayStar(InvincibilityStar):
    _item_id: int = 201
    _tier: int = 1


class KeroSewersStar(InvincibilityStar):
    _item_id: int = 202
    _tier: int = 1
    _chest_70a7_lower: int = 1


class MolevilleMinesStar(InvincibilityStar):
    _item_id: int = 203
    _tier: int = 2
    _chest_70a7_lower: int = 2


class SeaStar(InvincibilityStar):
    _item_id: int = 204
    _tier: int = 3
    _chest_70a7_lower: int = 3


class LandsEndVolcanoStar(InvincibilityStar):
    _item_id: int = 205
    _tier: int = 4
    _chest_70a7_lower: int = 5


class NimbusLandStar(InvincibilityStar):
    _item_id: int = 206
    _tier: int = 2
    _chest_70a7_lower: int = 7


class LandsEndStar2(InvincibilityStar):
    _item_id: int = 207
    _tier: int = 3
    _chest_70a7_lower: int = 8


class LandsEndStar3(InvincibilityStar):
    _item_id: int = 208
    _tier: int = 3
    _chest_70a7_lower: int = 9


class Shoes(MarrymoreGear):
    _id: int = 230
    _unique: ItemUnique = ItemUnique.ALWAYS
    _chest_event: int = 3943
    _npc_event: int = 3931
    _overworld_event: int = 3935
    _overworld_midas_event: int = 3939
    _model: Type[ItemNPC] = ShoesNPC
    _price: int = 0
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Pair of Fancy Shoes”!\n I bet they would look great on you.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Pair of Fancy Shoes”.\n I bet they would look great on you.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Pair of Fancy Shoes”.\n I bet they would look great on you.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class Brooch(MarrymoreGear):
    _id: int = 231
    _unique: ItemUnique = ItemUnique.ALWAYS
    _chest_event: int = 3944
    _npc_event: int = 3932
    _overworld_event: int = 3936
    _overworld_midas_event: int = 3940
    _model: Type[ItemNPC] = BroochNPC
    _price: int = 0
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Shiny Brooch”! It\n looks made for special occasions.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Shiny Brooch”. It\n looks made for special occasions.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Shiny Brooch”. It\n looks made for special occasions.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class Ring(MarrymoreGear):
    _id: int = 232
    _unique: ItemUnique = ItemUnique.ALWAYS
    _chest_event: int = 3945
    _npc_event: int = 3933
    _overworld_event: int = 3937
    _overworld_midas_event: int = 3941
    _model: Type[ItemNPC] = RingNPC
    _price: int = 0
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Diamond Ring”! It's\n a great gift for someone special.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Diamond Ring”. It's\n a great gift for someone special.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Diamond Ring”. It's\n a great gift for someone special.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


class Crown(MarrymoreGear):
    _id: int = 233
    _unique: ItemUnique = ItemUnique.ALWAYS
    _chest_event: int = 3946
    _npc_event: int = 3934
    _overworld_event: int = 3938
    _overworld_midas_event: int = 3942
    _model: Type[ItemNPC] = CrownNPC
    _price: int = 0
    _dialog_replacements: "dict[int, str]" = {
        2911: """ Item #1: A “Royal Crown”!\n It looks pretty important![await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        2908: """ Item #2: A “Royal Crown”.\n It looks pretty important![await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        2914: """ Item #3: A “Royal Crown”.\n It looks pretty important![await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
    }


# type: ignore # this is too annoying to debug
def initiate_items(world: GameWorld) -> List[ItemT]:
    """Instantiate each item for use in the game world."""

    items: List[ItemT] = [
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
        Crown(world),  # type: ignore
    ]

    return items
