# Data module for item/shop data.

import enum
import random
import math

from randomizer.helpers.flag_helpers import FireworksOptions, PlayableCharacters
from randomizer.logic import utils
from randomizer.logic.patch import Patch
from randomizer.data.characters import Mario, Mallow, Geno, Bowser, Peach
from randomizer.logic import flags
from randomizer.data import npcs, bosses, spells


class OverworldItem:
    model = None
    action_script = 15
    hover = False
    static_packet = None
    falling_packet = None
    treasure_packet = None
    chest_event = None

    def __init__(
        self,
        model,
        action_script=15,
        static_packet=90,
        falling_packet=37,
        treasure_packet=5,
        chest_event=883,
        hover=False,
    ):
        self.model = model
        self.action_script = action_script
        self.static_packet = static_packet
        self.falling_packet = falling_packet
        self.treasure_packet = treasure_packet
        self.chest_event = chest_event
        self.hover = hover


class ItemShuffleType(enum.Enum):
    """Enumeration for key item types for shuffling."""

    Required = enum.auto()
    Extra = enum.auto()


class ItemUnique(enum.Enum):
    """Enumeration for items that may need to be restricted by how many times they can appear."""

    Always = enum.auto()
    BalancedOnly = enum.auto()
    Never = enum.auto()


class EffectType(enum.Enum):
    Normal = enum.auto()
    ElementalImmunity = enum.auto()
    ElementalResistance = enum.auto()
    StatusProtection = enum.auto()
    FewEffects = enum.auto()
    Buffs = enum.auto()


class Item:
    """Parent class representing an item."""

    # Global item address info.
    BASE_ADDRESS = 0x3A014D
    BASE_PRICE_ADDRESS = 0x3A40F2
    BASE_DESC_POINTER_ADDRESS = 0x3A2F20
    DESC_DATA_POINTER_OFFSET = 0x3A0000
    BASE_DESC_DATA_ADDRESSES = (
        (0x3A3120, 0x3A40F1),
        (0x3A55F0, 0x3A5FFF),
    )

    # Total number of items in the data.
    NUM_ITEMS = 256

    # Stats used during equipment randomization.
    EQUIP_STATS = ["speed", "attack", "defense", "magic_attack", "magic_defense"]

    # Default per-item attributes.
    index = 0
    description = ""
    tier = 999
    order = 0
    item_type = 0
    consumable = False
    equip_chars = []
    speed = 0
    attack = 0
    defense = 0
    magic_attack = 0
    magic_defense = 0
    variance = 0
    prevent_ko = False
    elemental_immunities = []
    elemental_resistances = []
    status_immunities = []
    status_buffs = []
    price = 0
    frog_coin_item = False
    effect_type = EffectType.Normal
    is_key = False
    is_subitem = False

    # Shuffle properties
    shuffle_type = ItemShuffleType.Extra
    unique = ItemUnique.Never
    rank_value = 0
    rank_order = 0
    rank_order_reverse = 0
    arbitrary_value = 0
    tier = 0

    # Shuffle event builders
    model = npcs.ItemBag
    chest_70A7_lower = 0
    chest_70A7_upper = 0
    packet = 37
    chest_event = None
    quick_chest_event = None
    npc_event = None
    overworld_event = None
    overworld_midas_event = None
    dialog_replacements = []

    special_equip = False  # "special equip" refers to the 10 equips that can normally be obtained from turning in key items or completing monsto town sidequests

    # Flag to override whether we include the item stats in the patch data.  By default, we only include equipment but
    # a small handful of consumable items have their effects shuffled as well.
    include_stats_in_patch = False

    def __init__(self, world):
        """

        Args:
            world (randomizer.logic.main.GameWorld):

        """
        self.world = world
        self._rank = None

    def __str__(self):
        return "<{}: price {}>".format(self.name, self.price)

    def __repr__(self):
        return str(self)

    def get_chest_event(self, parent):
        return self.chest_event

    @property
    def name(self):
        return self.__class__.__name__

    @property
    def is_weapon(self):
        """:rtype: bool"""
        return self.item_type & 0x3 == 0

    @property
    def is_armor(self):
        """:rtype: bool"""
        return self.item_type & 0x3 == 1

    @property
    def is_accessory(self):
        """:rtype: bool"""
        return self.item_type & 0x3 == 2

    @property
    def is_equipment(self):
        """:rtype: bool"""
        return self.is_weapon or self.is_armor or self.is_accessory

    @property
    def is_frog_coin_item(self):
        """:rtype: bool"""
        return self.frog_coin_item

    def become_frog_coin_item(self):
        """:rtype: bool"""
        if self.is_frog_coin_item:
            return False

        self.price = max(math.ceil(self.rank_value / 5), 1)
        self.frog_coin_item = True
        return True

    def unbecome_frog_coin_item(self):
        """:rtype: bool"""
        if not self.is_frog_coin_item:
            return False

        factor = float(random.randint(50, random.randint(50, 100)))
        price = int(round(self.price * factor))
        self.price = min(price, 9999)
        self.frog_coin_item = False
        return True

    @property
    def max_price(self):
        """
        Returns:
            int: Max allowed price for this item based on whether it's a frog coin item or not.
        """
        return 99 if self.is_frog_coin_item else 9999

    @property
    def primary_stats(self):
        """Primary stats of this item, depending on the type.

        :rtype: list[str]
        """
        if self.is_weapon:
            if self.attack >= self.magic_attack:
                return ["attack"]
            else:
                return ["magic_attack"]
        # Exclude Work Pants and Super Suit, include Rare Scarf
        elif (self.is_armor and self.index not in [43, 69]) or self.index == 82:
            return ["defense", "magic_defense"]
        # Speed items are the Zoom Shoes and Feather
        elif self.index in [74, 91]:
            return ["speed"]
        return self.EQUIP_STATS

    @property
    def stat_point_value(self):
        """Overall stat point score for rough item power during shuffle.

        :rtype: int
        """
        score = 0
        for attr in self.EQUIP_STATS:
            value = getattr(self, attr)
            # Subtract any negative value from overall score.
            if value < 0:
                score += value
            # For primary stat, add the raw value.
            elif attr in self.primary_stats:
                score += value
            # If item has positive stat outside of primary stats, consider that double points for the score.
            else:
                score += 2 * value
        return score

    def get_similar(self, candidates):
        """Get a random similar item from a list of potential candidates for this one.

        :type candidates: list[Item]
        :rtype: Item
        """
        # If this is a special item, don't replace it.
        if self.rank_value <= 0:
            return self
        elif self not in candidates:
            return self

        # Sort by rank and mutate our position within the list to get a replacement item.
        candidates = sorted(candidates, key=lambda c: c.rank_value)
        index = candidates.index(self)
        index = utils.mutate_normal(index, maximum=len(candidates) - 1)
        return candidates[index]

    def build_equipment_description(self):
        """Generate shop/menu description text for the item based on shuffled stats.

        :rtype: str
        """
        if not self.is_equipment:
            return ""

        desc = ""

        # Elemental immunities and resistances.
        if self.elemental_immunities:
            desc += "\x96\x98"
            desc += utils.add_desc_fields(
                (
                    ("\x80\x98", 6, self.elemental_immunities),
                    ("\x81", 4, self.elemental_immunities),
                    ("\x82", 5, self.elemental_immunities),
                )
            )
        else:
            desc += "\x99" * 4
        desc += "\x99"

        if self.elemental_resistances:
            desc += "\x97\x98"
            desc += utils.add_desc_fields(
                (
                    ("\x80\x98", 6, self.elemental_resistances),
                    ("\x81", 4, self.elemental_resistances),
                    ("\x82", 5, self.elemental_resistances),
                )
            )
        else:
            desc += "\x99" * 4
        desc += "\x01"

        # Speed
        desc += ["\x93", "\x94"][self.speed < 0]
        desc += str(abs(self.speed)).ljust(3, "\x99") + "\x99"

        # Status immunities
        desc += utils.add_desc_fields(
            (
                ("\x83", 0, self.status_immunities),
                ("\x84", 1, self.status_immunities),
                ("\x85", 2, self.status_immunities),
                ("\x86", 3, self.status_immunities),
                ("\x98\x87", 5, self.status_immunities),
                ("\x88", 6, self.status_immunities),
                ("\x89", True, self.prevent_ko),
                ("\x8A", 4, self.status_immunities),
            )
        )
        desc += "\x01"

        # Physical attack/defense
        desc += ["\x8B", "\x8C"][self.attack < 0]
        desc += ["\x20", "\x95"][4 in self.status_buffs]
        desc += str(abs(self.attack)).ljust(3, "\x99")
        desc += "\x99"
        desc += ["\x8F", "\x90"][self.defense < 0]
        desc += ["\x20", "\x95"][6 in self.status_buffs]
        desc += str(abs(self.defense)).ljust(3, "\x99")
        desc += "\x01"

        # Magic attack/defense
        desc += ["\x8D", "\x8E"][self.magic_attack < 0]
        desc += ["\x20", "\x95"][3 in self.status_buffs]
        desc += str(abs(self.magic_attack)).ljust(3, "\x99")
        desc += "\x99"
        desc += ["\x91", "\x92"][self.magic_defense < 0]
        desc += ["\x20", "\x95"][5 in self.status_buffs]
        desc += str(abs(self.magic_defense)).ljust(3, "\x99")

        return desc

    def get_patch(self):
        """Get patch for this item.

        :return: Patch data.
        :rtype: randomizer.logic.patch.Patch
        """
        patch = Patch()
        base_addr = self.BASE_ADDRESS + (self.index * 18)

        # For non-shop items with no price (key items), there is no randomization.
        # if self.is_key or self.price == 0 or not self.price:
        #     return patch

        # Only modify equipment properties.
        if self.is_equipment or self.include_stats_in_patch:
            data = bytearray()

            # Only include initial item type and inflict/protect flags for equipment.
            if self.is_equipment:
                # Item type and instant KO protection.
                val = self.item_type
                if self.prevent_ko:
                    val |= 1 << 7
                data += utils.ByteField(val).as_bytes()

                # Inflict/protect flags for status ailments/buffs.
                val = 0
                if self.status_immunities:
                    val += 1 << 0
                if self.status_buffs:
                    val += 1 << 1
                data += utils.ByteField(val).as_bytes()

                # Which characters can equip
                data += utils.BitMapSet(
                    1, [c.index for c in self.equip_chars]
                ).as_bytes()

                patch.add_data(base_addr, data)

            # Stats and special properties.
            data = bytearray()
            data += utils.BitMapSet(1, self.elemental_immunities).as_bytes()
            data += utils.BitMapSet(1, self.elemental_resistances).as_bytes()
            data += utils.BitMapSet(1, self.status_immunities).as_bytes()
            data += utils.BitMapSet(1, self.status_buffs).as_bytes()
            data += utils.ByteField(self.speed).as_bytes()
            data += utils.ByteField(self.attack).as_bytes()
            data += utils.ByteField(self.defense).as_bytes()
            data += utils.ByteField(self.magic_attack).as_bytes()
            data += utils.ByteField(self.magic_defense).as_bytes()
            data += utils.ByteField(self.variance).as_bytes()
            patch.add_data(base_addr + 5, data)

        # Price
        price_addr = self.BASE_PRICE_ADDRESS + (self.index * 2)
        patch.add_data(price_addr, utils.ByteField(self.price, num_bytes=2).as_bytes())

        return patch

    @classmethod
    def build_descriptions_patch(cls, world):
        """Build patch data for item descriptions.  These use pointers, so we need to do them all together.

        :type world: randomizer.logic.main.GameWorld
        :return: Patch data.
        :rtype: randomizer.logic.patch.Patch
        """
        patch = Patch()

        # Begin text data with a single null byte to use for all empty descriptions to save space.
        pointer_data = bytearray()
        text_data = []
        for i in range(len(cls.BASE_DESC_DATA_ADDRESSES)):
            text_data.append(bytearray())
        text_data[0].append(0x00)

        # Track current base address for the text.  We have multiple banks to split the text across.
        current_bank = 0

        # Make list of blank descriptions for all items, and get description for each valid item we have based on index.
        descriptions = [""] * cls.NUM_ITEMS
        for item in world.items:
            # If this isn't an equipment, use the vanilla description, if any.
            if item.is_equipment:
                desc = item.build_equipment_description()
            else:
               desc = item.description
            descriptions[item.index] = desc

        # Now build the actual pointer data.
        for desc_index, desc in enumerate(descriptions):
            # If the description is empty, just use the null byte at the very beginning.
            if not desc:
                pointer = (
                    cls.BASE_DESC_DATA_ADDRESSES[0][0] - cls.DESC_DATA_POINTER_OFFSET
                )
                pointer_data += utils.ByteField(pointer, num_bytes=2).as_bytes()
                continue

            # Compute pointer from base address and current data length.  If we exceed the ending address of the current
            # data bank, move to the next one.  If we run out, it's an error.
            while True:
                pointer = cls.BASE_DESC_DATA_ADDRESSES[current_bank][0] + len(
                    text_data[current_bank]
                )
                if (pointer + len(desc) + 1) > cls.BASE_DESC_DATA_ADDRESSES[
                    current_bank
                ][1]:
                    current_bank += 1
                    if current_bank >= len(cls.BASE_DESC_DATA_ADDRESSES):
                        raise ValueError("Text descriptions too long")
                    continue

                # Subtract base pointer offset from computed final address.
                pointer -= cls.DESC_DATA_POINTER_OFFSET
                pointer_data += utils.ByteField(pointer, num_bytes=2).as_bytes()
                break

            # Add null byte to terminate the text string.
            desc = desc.encode("latin1")
            desc += bytes([0x00])
            text_data[current_bank] += desc

        # Sanity check that pointer data has the correct number of items.
        if len(pointer_data) != cls.NUM_ITEMS * 2:
            raise ValueError("Wrong length for pointer data, something went wrong...")

        # Sanity check that text data doesn't exceed size of each bank.
        for i, bank in enumerate(cls.BASE_DESC_DATA_ADDRESSES):
            data_len = len(text_data[i])
            bank_len = bank[1] - bank[0] + 1
            if data_len > bank_len:
                raise ValueError(
                    "Item description data bank {} too long: {} > max {}".format(
                        i, data_len, bank_len
                    )
                )

        # Add item description data to the patch data.
        patch.add_data(cls.BASE_DESC_POINTER_ADDRESS, pointer_data)
        for i, bank in enumerate(cls.BASE_DESC_DATA_ADDRESSES):
            patch.add_data(bank[0], text_data[i])

        return patch


class RegularItem(Item):
    chest_event = 3089
    npc_event = 160
    overworld_event = 165
    overworld_midas_event = 2820

    def __init__(self, world):
        """

        Args:
            world (randomizer.logic.main.GameWorld):

        """
        super().__init__(world)
        self.chest_70A7_lower = self.index

    def get_patch(self):
        """Get patch for this item.

        Returns:
            randomizer.logic.patch.Patch:
        """
        patch = super().get_patch()
        return patch


# *************************** Actual item classes


class Hammer(RegularItem):
    index = 5
    description = "Pounds\x01enemies"
    tier = 5
    order = 53
    equip_chars = [Mario]
    attack = 10
    variance = 1
    price = 70
    unique = ItemUnique.BalancedOnly
    model = npcs.Hammer
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Hammer”!\n I'm not sure if it does anything\n else.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Hammer”.\n I'm not sure if it does anything\n else.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Hammer”.\n I'm not sure if it does anything\n else.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class FroggieStick(RegularItem):
    index = 6
    description = "Frogfucius\x01made it"
    tier = 5
    order = 67
    equip_chars = [Mallow]
    attack = 20
    variance = 2
    price = 180
    special_equip = True
    unique = ItemUnique.BalancedOnly
    model = npcs.FroggieStick
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Caster's Staff”!\n It looks pretty good at bonking.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Caster's Staff”.\n It looks pretty good at bonking.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Caster's Staff”.\n It looks pretty good at bonking.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class NokNokShell(RegularItem):
    index = 7
    description = "Kick to attack"
    tier = 5
    order = 58
    equip_chars = [Mario]
    model = npcs.GreenShell
    attack = 20
    variance = 2
    price = 20
    unique = ItemUnique.BalancedOnly
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Green Shell”!\n There's no turtle inside of it.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Green Shell”.\n There's no turtle inside of it.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Green Shell”.\n There's no turtle inside of it.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class PunchGlove(RegularItem):
    index = 8
    description = "Knock out\x01power!"
    tier = 5
    order = 48
    equip_chars = [Mario]
    attack = 30
    variance = 3
    price = 36


class FingerShot(RegularItem):
    index = 9
    description = "Fingers shoot\x01bullets"
    tier = 5
    order = 70
    equip_chars = [Geno]
    attack = 12
    variance = 3
    price = 50


class Cymbals(RegularItem):
    index = 10
    description = "Scare enemies\x01with a clash"
    tier = 5
    order = 60
    equip_chars = [Mallow]
    attack = 30
    variance = 3
    price = 42
    model = npcs.Music


class Chomp(RegularItem):
    index = 11
    description = "Just spin me\x01at an enemy!"
    tier = 3
    order = 64
    equip_chars = [Bowser]
    attack = 10
    variance = 4
    price = 140
    unique = ItemUnique.BalancedOnly
    model = npcs.ChompItem
    special_equip = True
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Chain Chomp”!\n It's hungry to stir up some trouble.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Chain Chomp”.\n It's hungry to stir up some trouble.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Chain Chomp”.\n It's hungry to stir up some trouble.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class Masher(RegularItem):
    index = 12
    description = "Makes monster\x01mash!"
    tier = 3
    order = 54
    equip_chars = [Mario]
    attack = 50
    variance = 30
    price = 160
    unique = ItemUnique.BalancedOnly
    model = npcs.Hammer
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Hammer”!\n I'm not sure if it does anything\n else.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Hammer”.\n I'm not sure if it does anything\n else.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Hammer”.\n I'm not sure if it does anything\n else.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class ChompShell(RegularItem):
    index = 13
    description = "It~s a\x01Kinklink shell"
    model = npcs.ChompItem
    tier = 5
    order = 65
    equip_chars = [Bowser]
    attack = 9
    variance = 3
    price = 60


class SuperHammer(RegularItem):
    index = 14
    description = "The standard\x01for hammers!"
    tier = 5
    order = 55
    equip_chars = [Mario]
    attack = 40
    variance = 4
    price = 70
    model = npcs.Hammer


class HandGun(RegularItem):
    index = 15
    description = "It packs a kick"
    tier = 5
    order = 72
    equip_chars = [Geno]
    attack = 24
    variance = 4
    price = 75


class WhompGlove(RegularItem):
    index = 16
    description = "The old double\x01whammie!"
    tier = 5
    order = 52
    equip_chars = [Mallow]
    attack = 40
    variance = 4
    price = 72


class SlapGlove(RegularItem):
    index = 17
    description = "It slaps ~em\x01silly"
    tier = 5
    order = 49
    equip_chars = [Peach]
    attack = 40
    variance = 4
    price = 100
    unique = ItemUnique.BalancedOnly
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Little Glove”!\n You don't drink water out of it.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Little Glove”.\n You don't drink water out of it.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Little Glove”.\n You don't drink water out of it.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class TroopaShell(RegularItem):
    index = 18
    description = "Kick with it!"
    model = npcs.RedShell
    tier = 5
    order = 59
    equip_chars = [Mario]
    attack = 50
    variance = 5
    price = 90


class Parasol(RegularItem):
    index = 19
    description = "Inflicts\x01serious pain!"
    model = npcs.Parasol
    tier = 5
    order = 68
    equip_chars = [Peach]
    attack = 50
    variance = 5
    price = 84


class HurlyGloves(RegularItem):
    index = 20
    description = "A classic\x01Mario}toss\x01attack"
    tier = 5
    order = 46
    equip_chars = [Bowser]
    attack = 20
    variance = 5
    price = 92

    def get_patch(self):
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


class DoublePunch(RegularItem):
    index = 21
    description = "A handy double\x01rocket punch"
    tier = 5
    order = 44
    equip_chars = [Geno]
    attack = 35
    variance = 5
    price = 88


class RibbitStick(RegularItem):
    index = 22
    description = "It~ll come\x01in handy"
    model = npcs.FroggieStick
    tier = 5
    order = 69
    equip_chars = [Mallow]
    attack = 50
    variance = 5
    price = 86


class SpikedLink(RegularItem):
    index = 23
    description = "A studded ball\x01and chain!"
    tier = 4
    order = 66
    equip_chars = [Bowser]
    model = npcs.ChompItem
    attack = 30
    variance = 6
    price = 94


class MegaGlove(RegularItem):
    index = 24
    description = "Packs a mega\x01wallop!"
    tier = 4
    order = 47
    equip_chars = [Mario]
    attack = 60
    variance = 6
    price = 102


class WarFan(RegularItem):
    index = 25
    description = "A mysterious\x01battle fan!"
    model = npcs.Fan
    tier = 4
    order = 63
    equip_chars = [Peach]
    attack = 60
    variance = 6
    price = 100


class HandCannon(RegularItem):
    index = 26
    description = "Shoots bullets\x01from elbow!"
    tier = 3
    order = 71
    equip_chars = [Geno]
    attack = 45
    variance = 6
    price = 105


class StickyGlove(RegularItem):
    index = 27
    description = "Launches a\x01punch attack."
    tier = 4
    order = 50
    equip_chars = [Mallow]
    attack = 60
    variance = 6
    price = 98


class UltraHammer(RegularItem):
    index = 28
    description = "The ultimate\x01hammer!"
    tier = 2
    order = 56
    equip_chars = [Mario]
    attack = 70
    variance = 7
    price = 115
    model = npcs.Hammer
    unique = ItemUnique.BalancedOnly
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Hammer”!\n I'm not sure if it does anything\n else.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Hammer”.\n I'm not sure if it does anything\n else.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Hammer”.\n I'm not sure if it does anything\n else.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class SuperSlap(RegularItem):
    index = 29
    description = "The Princess~\x01mega}slap!"
    tier = 2
    order = 51
    equip_chars = [Peach]
    attack = 70
    variance = 7
    price = 110
    unique = ItemUnique.BalancedOnly
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Big Glove”!\n You don't drink water out of it.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Big Glove”.\n You don't drink water out of it.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Big Glove”.\n You don't drink water out of it.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class DrillClaw(RegularItem):
    index = 30
    description = "A drilling\x01claw!"
    tier = 2
    order = 45
    equip_chars = [Bowser]
    attack = 40
    variance = 7
    price = 118
    unique = ItemUnique.BalancedOnly
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Drilling Appendage”!\n I bet you could do some real damage\n with this.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Drilling Appendage”.\n I bet you could do some real damage\n with this.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Drilling Appendage”.\n I bet you could do some real damage\n with this.[await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class StarGun(RegularItem):
    index = 31
    description = "Try shooting\x01stars!"
    tier = 1
    order = 73
    equip_chars = [Geno]
    model = npcs.TinyStar
    attack = 57
    variance = 7
    price = 120
    unique = ItemUnique.BalancedOnly
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Celestial Launcher”!\n I bet you could do some real damage\n with this.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Celestial Launcher”.\n I bet you could do some real damage\n with this.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Celestial Launcher”.\n I bet you could do some real damage\n with this.[await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class SonicCymbal(RegularItem):
    index = 32
    description = "Puts noise to\x01work for you!"
    tier = 2
    order = 61
    equip_chars = [Mallow]
    attack = 70
    variance = 7
    price = 108
    model = npcs.Music
    unique = ItemUnique.BalancedOnly
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Psych Percussion”!\n This could catch monsters\n off-guard.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Psych Percussion”.\n This could catch monsters\n off-guard.[await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Psych Percussion”.\n This could catch monsters\n off-guard.[await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class LazyShellWeapon(RegularItem):
    index = 33
    description = "Toss a shell\x01at an enemy!"
    model = npcs.RedShell
    tier = 1
    order = 57
    equip_chars = [Mario]
    attack = 90
    variance = 40
    price = 200
    unique = ItemUnique.BalancedOnly
    special_equip = True
    dialog_replacements = [
        (
            2911,
            """ Item #1: An “Oversized Shell”!\n You could do some real damage\n with this.[await][await] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: An “Oversized Shell”.\n You could do some real damage\n with this.[await][await] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: An “Oversized Shell”.\n You could do some real damage\n with this.[await][await] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class FryingPan(RegularItem):
    index = 34
    description = "Enough iron to\x01be dangerous!"
    model = npcs.FryingPan
    tier = 1
    order = 62
    equip_chars = [Peach]
    attack = 90
    variance = 20
    price = 300
    unique = ItemUnique.BalancedOnly
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Metal Plate”![await]\n Don't know what it’s used for,\n but I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Metal Plate”.[await]\n Don't know what it’s used for,\n but it's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Metal Plate”.[await]\n Don't know what it’s used for,\n but I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class LuckyHammer(RegularItem):
    index = 35
    description = "A lucky hammer!"
    tier = 1
    order = 54
    equip_chars = [Mario]
    price = 123
    model = npcs.Hammer


class Shirt(RegularItem):
    index = 37
    description = "It~s a\x01shirt!"
    tier = 5
    order = 102
    item_type = 1
    equip_chars = [Mario]
    defense = 6
    magic_defense = 6
    price = 7


class Pants(RegularItem):
    index = 38
    description = "It~s a pair\x01of pants!"
    tier = 5
    order = 95
    item_type = 1
    equip_chars = [Mallow]
    defense = 6
    magic_defense = 3
    price = 7


class ThickShirt(RegularItem):
    index = 39
    description = "A padded shirt"
    tier = 5
    order = 106
    item_type = 1
    equip_chars = [Mario]
    defense = 12
    magic_defense = 8
    price = 14


class ThickPants(RegularItem):
    index = 40
    description = "Padded pants"
    tier = 5
    order = 105
    item_type = 1
    equip_chars = [Mallow]
    defense = 12
    magic_defense = 6
    price = 14


class MegaShirt(RegularItem):
    index = 41
    description = "Durable stay}\x01pressed shirt"
    tier = 5
    order = 93
    item_type = 1
    equip_chars = [Mario]
    defense = 18
    magic_defense = 10
    price = 22


class MegaPants(RegularItem):
    index = 42
    description = "Durable work\x01pants"
    tier = 5
    order = 92
    item_type = 1
    equip_chars = [Mallow]
    defense = 18
    magic_defense = 9
    price = 22


class WorkPants(RegularItem):
    index = 43
    description = "Sweaty\x01work pants!"
    tier = 5
    order = 107
    item_type = 1
    equip_chars = [Mario, Mallow, Geno, Bowser, Peach]
    speed = 5
    attack = 10
    defense = 15
    magic_attack = 10
    magic_defense = 5
    price = 22


class MegaCape(RegularItem):
    index = 44
    description = "Durable\x01pressed cape"
    tier = 5
    order = 91
    item_type = 1
    equip_chars = [Geno]
    defense = 6
    magic_defense = 3
    price = 22


class HappyShirt(RegularItem):
    index = 45
    description = "A lucky shirt"
    tier = 5
    order = 87
    item_type = 1
    equip_chars = [Mario]
    defense = 24
    magic_defense = 12
    price = 38


class HappyPants(RegularItem):
    index = 46
    description = "A lucky\x01pair of pants"
    tier = 5
    order = 85
    item_type = 1
    equip_chars = [Mallow]
    defense = 24
    magic_defense = 12
    price = 38


class HappyCape(RegularItem):
    index = 47
    description = "A lucky cape"
    tier = 5
    order = 84
    item_type = 1
    equip_chars = [Geno]
    defense = 12
    magic_defense = 6
    price = 38


class HappyShell(RegularItem):
    index = 48
    description = "A lucky shell"
    model = npcs.GreenShell
    tier = 5
    order = 86
    item_type = 1
    equip_chars = [Bowser]
    defense = 6
    magic_defense = 3
    price = 38


class PolkaDress(RegularItem):
    index = 49
    description = "A flashy dress"
    tier = 5
    order = 96
    item_type = 1
    equip_chars = [Peach]
    defense = 24
    magic_defense = 12
    price = 160
    unique = ItemUnique.BalancedOnly
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Casual Gown”!\n It's pink with little polka dots![await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Casual Gown”.\n It's pink with little polka dots![await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Casual Gown”.\n It's pink with little polka dots![await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class SailorShirt(RegularItem):
    index = 50
    description = "A sailor~s\x01suit"
    tier = 5
    order = 101
    item_type = 1
    equip_chars = [Mario]
    defense = 30
    magic_defense = 15
    price = 50


class SailorPants(RegularItem):
    index = 51
    description = "A sailor~s\x01pants"
    tier = 5
    order = 100
    item_type = 1
    equip_chars = [Mallow]
    defense = 30
    magic_defense = 15
    price = 50


class SailorCape(RegularItem):
    index = 52
    description = "A sailor~s\x01cape"
    tier = 5
    order = 99
    item_type = 1
    equip_chars = [Geno]
    defense = 18
    magic_defense = 9
    price = 50


class NauticaDress(RegularItem):
    index = 53
    description = "A female\x01sailor~s dress"
    tier = 5
    order = 94
    item_type = 1
    equip_chars = [Peach]
    defense = 30
    magic_defense = 15
    price = 50


class CourageShell(RegularItem):
    index = 54
    description = "A stout shell"
    model = npcs.GreenShell
    tier = 4
    order = 74
    item_type = 1
    equip_chars = [Bowser]
    defense = 12
    magic_defense = 6
    price = 60


class FuzzyShirt(RegularItem):
    index = 55
    description = "A fuzzy shirt"
    tier = 4
    order = 83
    item_type = 1
    equip_chars = [Mario]
    defense = 36
    magic_defense = 18
    price = 70


class FuzzyPants(RegularItem):
    index = 56
    description = "Fuzzy pants"
    tier = 4
    order = 82
    item_type = 1
    equip_chars = [Mallow]
    defense = 36
    magic_defense = 18
    price = 70


class FuzzyCape(RegularItem):
    index = 57
    description = "A fuzzy cape"
    tier = 4
    order = 80
    item_type = 1
    equip_chars = [Geno]
    defense = 24
    magic_defense = 12
    price = 70


class FuzzyDress(RegularItem):
    index = 58
    description = "A fuzzy dress"
    tier = 4
    order = 81
    item_type = 1
    equip_chars = [Peach]
    defense = 36
    magic_defense = 18
    price = 70


class FireShirt(RegularItem):
    index = 59
    description = "Determined\x01person~s shirt"
    tier = 4
    order = 79
    item_type = 1
    equip_chars = [Mario]
    defense = 42
    magic_defense = 21
    price = 90


class FirePants(RegularItem):
    index = 60
    description = "Determined\x01person~s pants"
    tier = 4
    order = 77
    item_type = 1
    equip_chars = [Mallow]
    defense = 42
    magic_defense = 21
    price = 90
    elemental_immunities = []


class FireCape(RegularItem):
    index = 61
    description = "Determined\x01person~s cape"
    tier = 4
    order = 75
    item_type = 1
    equip_chars = [Geno]
    defense = 30
    magic_defense = 15
    price = 90


class FireShell(RegularItem):
    index = 62
    description = "Determined\x01person~s shell"
    model = npcs.RedShell
    tier = 4
    order = 78
    item_type = 1
    equip_chars = [Bowser]
    defense = 18
    magic_defense = 9
    price = 90


class FireDress(RegularItem):
    index = 63
    description = "Determined\x01woman~s dress"
    tier = 4
    order = 76
    item_type = 1
    equip_chars = [Peach]
    defense = 42
    magic_defense = 21
    price = 90


class HeroShirt(RegularItem):
    index = 64
    description = "A legendary\x01shirt."
    tier = 3
    order = 89
    item_type = 1
    equip_chars = [Mario]
    defense = 48
    magic_defense = 24
    price = 100


class PrincePants(RegularItem):
    index = 65
    description = "Legendary\x01pants!"
    tier = 3
    order = 97
    item_type = 1
    equip_chars = [Mallow]
    defense = 48
    magic_defense = 24
    price = 100
    model = npcs.Crown


class StarCape(RegularItem):
    index = 66
    description = "A legendary\x01cape."
    model = npcs.TinyStar
    tier = 3
    order = 103
    item_type = 1
    equip_chars = [Geno]
    defense = 36
    magic_defense = 18
    price = 100


class HealShell(RegularItem):
    index = 67
    description = "A legendary\x01shell."
    model = npcs.GreenShell
    tier = 3
    order = 88
    item_type = 1
    equip_chars = [Bowser]
    defense = 24
    magic_defense = 12
    price = 100


class RoyalDress(RegularItem):
    index = 68
    description = "A legendary\x01dress!"
    tier = 3
    order = 98
    item_type = 1
    equip_chars = [Peach]
    defense = 48
    magic_defense = 24
    price = 100
    model = npcs.Crown


class SuperSuit(RegularItem):
    index = 69
    description = "A truly fine\x01suit!"
    tier = 1
    order = 104
    item_type = 1
    equip_chars = [Mario, Mallow, Geno, Bowser, Peach]
    speed = 30
    attack = 50
    defense = 50
    magic_attack = 50
    magic_defense = 50
    elemental_immunities = [4, 5, 6, 7]
    status_immunities = [0, 1, 2, 3, 4, 5, 6]
    price = 700
    special_equip = True
    effect_type = EffectType.ElementalImmunity
    unique = ItemUnique.BalancedOnly
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Jumpsuit”!\n It looks pretty powerful, right?[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Jumpsuit”.\n It looks pretty powerful, right?[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Jumpsuit”.\n It looks pretty powerful, right?[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class LazyShellArmor(RegularItem):
    index = 70
    description = "A stout and\x01durable shell."
    model = npcs.RedShell
    tier = 1
    order = 90
    item_type = 1
    equip_chars = [Mario, Mallow, Geno, Bowser, Peach]
    speed = -50
    attack = -50
    defense = 127
    magic_attack = -50
    magic_defense = 127
    elemental_immunities = [4, 5, 6, 7]
    status_immunities = [0, 1, 2, 3, 4, 5, 6]
    special_equip = True
    price = 222
    effect_type = EffectType.ElementalImmunity
    unique = ItemUnique.BalancedOnly
    dialog_replacements = [
        (
            2911,
            """ Item #1: An “Oversized Shell”!\n It's quite beefy and protective.[await]\n I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: An “Oversized Shell”.\n It's quite beefy and protective.[await]\n It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: An “Oversized Shell”.\n It's quite beefy and protective.[await]\n I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class ZoomShoes(RegularItem):
    index = 74
    description = "Speed up by 10!"
    tier = 4
    order = 128
    item_type = 2
    equip_chars = [Mario, Mallow, Geno, Bowser, Peach]
    speed = 10
    defense = 5
    magic_defense = 5
    price = 100
    model = npcs.Shoes
    unique = ItemUnique.BalancedOnly
    special_equip = True
    dialog_replacements = [
        (
            2911,
            """ Item #1: “Pegasus Boots”!\n These will make you fast like Sonic![await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: “Pegasus Boots”.\n These will make you fast like Sonic![await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: “Pegasus Boots”.\n These will make you fast like Sonic![await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class SafetyBadge(RegularItem):
    index = 75
    description = "Prevents Mute \x9c\x01Poison attacks"
    tier = 2
    order = 121
    item_type = 2
    equip_chars = [Mario, Mallow, Geno, Bowser, Peach]
    defense = 5
    magic_defense = 5
    status_immunities = [0, 1, 2, 3, 4, 5, 6]
    price = 500
    effect_type = EffectType.StatusProtection
    model = npcs.Brooch
    unique = ItemUnique.BalancedOnly
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Status Protector”!\n It can prevent weird things from\n happening to you.[await][pause] I'll sell it to\n you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Status Protector”.\n It can prevent weird things from\n happening to you.[await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Status Protector”.\n It can prevent weird things from\n happening to you.[await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class JumpShoes(RegularItem):
    index = 76
    description = "Use jump attacks\x01against any foe"
    tier = 5
    order = 118
    item_type = 2
    equip_chars = [Mario]
    speed = 2
    defense = 1
    magic_attack = 5
    magic_defense = 1
    price = 30
    model = npcs.Shoes


class SafetyRing(RegularItem):
    index = 77
    description = "Guards against\x01mortal blows."
    tier = 1
    order = 122
    item_type = 2
    equip_chars = [Mario, Mallow, Geno, Bowser, Peach]
    speed = 5
    defense = 5
    magic_defense = 5
    prevent_ko = True
    elemental_immunities = [4, 5, 6, 7]
    status_immunities = [0, 1, 2, 3, 4, 5, 6]
    price = 800
    effect_type = EffectType.ElementalImmunity
    unique = ItemUnique.BalancedOnly
    model = npcs.Ring
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Protective Charm”!\n Never go into battle without it.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Protective Charm”.\n Never go into battle without it.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Protective Charm”.\n Never go into battle without it.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class Amulet(RegularItem):
    index = 78
    description = "Great item,\x01bad smell!"
    tier = 2
    order = 108
    item_type = 2
    equip_chars = [Mario, Mallow, Geno, Bowser, Peach]
    speed = -5
    attack = 7
    defense = 7
    magic_attack = 7
    magic_defense = 7
    elemental_resistances = [4, 5, 6, 7]
    price = 200
    effect_type = EffectType.ElementalResistance
    unique = ItemUnique.BalancedOnly
    model = npcs.Brooch
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Stinky Charm”!\n It'll help you weather the elements.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Stinky Charm”.\n It'll help you weather the elements.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Stinky Charm”.\n It'll help you weather the elements.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class ScroogeRing(RegularItem):
    index = 79
    description = "Cuts FP use\x01in half\x01during battle"
    tier = 3
    order = 123
    item_type = 2
    equip_chars = [Mario, Mallow, Geno, Bowser, Peach]
    price = 50
    frog_coin_item = True
    model = npcs.Ring
    unique = ItemUnique.BalancedOnly
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Mage Totem”!\n It might help with spellcasting.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Mage Totem”.\n It might help with spellcasting.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Mage Totem”.\n It might help with spellcasting.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class ExpBooster(RegularItem):
    index = 80
    description = "Doubles Exp.\x01when equipped"
    tier = 3
    order = 113
    item_type = 2
    equip_chars = [Mario, Mallow, Geno, Bowser, Peach]
    price = 22
    frog_coin_item = True
    effect_type = EffectType.FewEffects
    unique = ItemUnique.BalancedOnly
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Training Device”!\n This'll make you strong in no time![await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Training Device”.\n This'll make you strong in no time![await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Training Device”.\n This'll make you strong in no time![await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class AttackScarf(RegularItem):
    index = 81
    description = "So comfy it~ll\x01make you jump!"
    tier = 1
    order = 110
    item_type = 2
    equip_chars = [Mario]
    speed = 30
    attack = 30
    defense = 30
    magic_attack = 30
    magic_defense = 30
    prevent_ko = True
    price = 1500
    unique = ItemUnique.BalancedOnly
    special_equip = True
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Jumper's Scarf”!\n It could save your life![await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Jumper's Scarf”.\n It could save your life![await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Jumper's Scarf”.\n It could save your life![await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class RareScarf(RegularItem):
    index = 82
    description = "Raises defense\x01power!"
    tier = 3
    order = 120
    item_type = 2
    equip_chars = [Mario, Mallow, Geno, Bowser, Peach]
    defense = 15
    magic_defense = 15
    price = 150
    unique = ItemUnique.BalancedOnly
    dialog_replacements = [
        (
            2911,
            """ Item #1: An “Unusual Garment”!\n I don't see these around often.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: An “Unusual Garment”.\n I don't see these around often.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: An “Unusual Garment”.\n I don't see these around often.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class BtubRing(RegularItem):
    index = 83
    description = "You~ll win her\x01heart with this!"
    tier = 2
    order = 111
    item_type = 2
    equip_chars = [Peach]
    elemental_resistances = [4, 5, 6, 7]
    price = 145
    model = npcs.Ring


class AntidotePin(RegularItem):
    index = 84
    description = "Prevents\x01poison damage"
    tier = 3
    order = 109
    item_type = 2
    equip_chars = [Mario, Mallow, Geno, Bowser, Peach]
    defense = 2
    magic_defense = 2
    status_immunities = [2]
    price = 28
    effect_type = EffectType.StatusProtection
    model = npcs.Brooch


class WakeUpPin(RegularItem):
    index = 85
    description = "Prevents Mute \x9c\x01Sleep attacks"
    tier = 3
    order = 127
    item_type = 2
    equip_chars = [Mario, Mallow, Geno, Bowser, Peach]
    defense = 3
    magic_defense = 3
    status_immunities = [0, 1]
    price = 42
    effect_type = EffectType.StatusProtection
    model = npcs.Brooch


class FearlessPin(RegularItem):
    index = 86
    description = "Prevents Fear\x01attacks"
    tier = 3
    order = 114
    item_type = 2
    equip_chars = [Mario, Mallow, Geno, Bowser, Peach]
    defense = 5
    magic_defense = 5
    status_immunities = [3]
    price = 130
    effect_type = EffectType.StatusProtection
    model = npcs.Brooch


class TrueformPin(RegularItem):
    index = 87
    description = "You won~t be\x01turned into\x01Mushrooms or\x01Scarecrows!"
    tier = 3
    order = 126
    item_type = 2
    equip_chars = [Mario, Mallow, Geno, Bowser, Peach]
    defense = 4
    magic_defense = 4
    status_immunities = [5, 6]
    price = 60
    effect_type = EffectType.StatusProtection
    model = npcs.Brooch


class CoinTrick(RegularItem):
    index = 88
    description = "Doubles the\x01coins you win\x01in battle"
    tier = 4
    order = 112
    item_type = 2
    equip_chars = [Mario]
    price = 36
    frog_coin_item = True
    effect_type = EffectType.FewEffects
    unique = ItemUnique.BalancedOnly
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Fortune Charm”!\n It's sure to make you very rich.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Fortune Charm”.\n It's sure to make you very rich.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Fortune Charm”.\n It's sure to make you very rich.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class GhostMedal(RegularItem):
    index = 89
    description = "Raises defense\x01while attacking"
    tier = 2
    order = 116
    item_type = 2
    equip_chars = [Mario, Mallow, Geno, Bowser, Peach]
    status_buffs = [5, 6]
    price = 1600
    effect_type = EffectType.Buffs
    unique = ItemUnique.BalancedOnly
    special_equip = True
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Scavenger's Prize”!\n It resembles a medal of honor.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Scavenger's Prize”.\n It resembles a medal of honor.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Scavenger's Prize”.\n It resembles a medal of honor.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class JinxBelt(RegularItem):
    index = 90
    description = "Jinx~s emblem\x01of power!"
    tier = 1
    order = 117
    item_type = 2
    equip_chars = [Mario, Mallow, Geno, Bowser, Peach]
    speed = 12
    attack = 27
    defense = 27
    prevent_ko = True
    special_equip = True
    price = 1998
    unique = ItemUnique.BalancedOnly
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Martial Sash”!\n A true fighter would love this.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Martial Sash”.\n A true fighter would love this.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Martial Sash”.\n A true fighter would love this.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class Feather(RegularItem):
    index = 91
    description = "Speed up by 20"
    tier = 2
    order = 115
    item_type = 2
    equip_chars = [Mario, Mallow, Geno, Bowser, Peach]
    speed = 20
    defense = 5
    magic_defense = 5
    price = 666
    unique = ItemUnique.BalancedOnly
    model = npcs.Feather
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Fluttering Quill”!\n It's pretty exotic, isn't it?[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Fluttering Quill”.\n It's pretty exotic, isn't it?[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Fluttering Quill”.\n It's pretty exotic, isn't it?[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class TroopaPin(RegularItem):
    index = 92
    description = 'Grants "Troopa#\x01confidence!'
    tier = 2
    order = 125
    item_type = 2
    equip_chars = [Mario, Mallow, Geno, Bowser, Peach]
    speed = 20
    status_buffs = [3, 4]
    price = 1000
    effect_type = EffectType.Buffs
    model = npcs.Brooch
    unique = ItemUnique.BalancedOnly
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Military Decoration”!\n I wonder what powers it bestows?[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Military Decoration”.\n I wonder what powers it bestows?[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Military Decoration”.\n I wonder what powers it bestows?[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class SignalRing(RegularItem):
    index = 93
    description = "Noise indicates\x01a hidden chest."
    tier = 4
    order = 124
    item_type = 2
    equip_chars = [Mario, Mallow, Geno, Bowser, Peach]
    speed = 10
    price = 600
    model = npcs.Ring
    unique = ItemUnique.Always
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Treasure Beacon”!\n I wonder what it can help you find?[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Treasure Beacon”.\n I wonder what it can help you find?[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Treasure Beacon”.\n I wonder what it can help you find?[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class QuartzCharm(RegularItem):
    index = 94
    description = "Shining source\x01of power!"
    tier = 1
    order = 119
    item_type = 2
    equip_chars = [Mario, Mallow, Geno, Bowser, Peach]
    prevent_ko = True
    status_buffs = [3, 4, 5, 6]
    price = 7
    effect_type = EffectType.Buffs
    model = npcs.Ring
    unique = ItemUnique.BalancedOnly
    special_equip = True
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Crystal Ring”!\n It could save your life![await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Crystal Ring”.\n It could save your life![await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Crystal Ring”.\n It could save your life![await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class Mushroom(RegularItem):
    index = 96
    description = "Recovers 30 HP"
    order = 15
    item_type = 3
    consumable = True
    price = 4
    tier = 5
    model = npcs.RedMushroom
    room_service = "Mushroom........"


class MidMushroom(RegularItem):
    index = 97
    description = "Recovers 80 HP"
    order = 13
    item_type = 3
    consumable = True
    price = 20
    tier = 4
    model = npcs.GreenMushroom
    room_service = "Mid Mushroom...."


class MaxMushroom(RegularItem):
    index = 98
    description = "Recovers all HP"
    order = 11
    item_type = 3
    consumable = True
    price = 78
    tier = 3
    model = npcs.YellowMushroom
    room_service = "Max Mushroom...."


class HoneySyrup(RegularItem):
    index = 99
    description = "Recovers 10 FP"
    model = npcs.RedSyrup
    order = 8
    item_type = 3
    consumable = True
    price = 10
    tier = 5
    room_service = "Honey Syrup......"


class MapleSyrup(RegularItem):
    index = 100
    description = "Recovers 40 FP"
    model = npcs.GreenSyrup
    order = 10
    item_type = 3
    consumable = True
    price = 30
    tier = 4
    room_service = "Maple Syrup......"


class RoyalSyrup(RegularItem):
    index = 101
    description = "Recovers all FP"
    model = npcs.YellowSyrup
    order = 21
    item_type = 3
    consumable = True
    price = 101
    tier = 3
    room_service = "Royal Syrup......"


class PickMeUp(RegularItem):
    index = 102
    description = "Revives downed\x01allies"
    order = 17
    item_type = 3
    consumable = True
    price = 5
    tier = 4
    room_service = "Pick Me Up......."
    model = npcs.StarDrink


class AbleJuice(RegularItem):
    index = 103
    description = "Heal status\x01ailments"
    model = npcs.RDrink
    item_type = 3
    consumable = True
    status_immunities = [0, 1, 2, 3, 4, 5, 6]
    price = 4
    tier = 5
    room_service = "Able Juice........"


class Bracer(RegularItem):
    index = 104
    description = "Raises ally~s\x01def. in battle"
    order = 2
    item_type = 3
    consumable = True
    status_buffs = [5, 6]
    price = 50
    frog_coin_item = True
    tier = 4
    rank_value = 10
    room_service = "Bracer..........."
    model = npcs.DDrink


class Energizer(RegularItem):
    index = 105
    description = "Raises ally~s\x01battle power\x01during battle"
    order = 5
    item_type = 3
    consumable = True
    status_buffs = [3, 4]
    price = 50
    frog_coin_item = True
    tier = 4
    room_service = "Energizer........"
    model = npcs.PDrink


class YoshiAde(RegularItem):
    index = 106
    description = "Power raised\x01during battle"
    model = npcs.GreenJuice
    order = 23
    item_type = 3
    consumable = True
    status_buffs = [3, 4, 5, 6]
    price = 200
    tier = 3
    room_service = "Yoshi Ade........"


class RedEssence(RegularItem):
    index = 107
    description = "Become invincible\x01for 3 turns"
    model = npcs.RedJuice
    order = 19
    item_type = 3
    consumable = True
    status_immunities = [7]
    price = 400
    tier = 1
    room_service = "Red Essence......"


class KerokeroCola(RegularItem):
    index = 108
    description = "All members\x01recover fully"
    order = 9
    item_type = 3
    consumable = True
    price = 400
    tier = 1
    room_service = "KerokeroCola....."
    model = npcs.FrogDrink


class YoshiCookie(RegularItem):
    index = 109
    description = "Summons Yoshi\x01during battle"
    order = 26
    item_type = 3
    consumable = True
    price = 100
    model = npcs.Cookie
    tier = 5
    room_service = "Yoshi Cookie......"


class PureWater(RegularItem):
    index = 110
    description = "Defeats ghosts\x01in a wink"
    model = npcs.BlueSyrup
    order = 30
    item_type = 3
    consumable = True
    price = 150
    tier = 4
    room_service = "Pure Water......."


class SleepyBomb(RegularItem):
    item_name = "Sleepy Bomb"
    index = 111
    description = "Puts enemies\x01to sleep"
    order = 32
    item_type = 3
    consumable = True
    status_immunities = [1]
    model = npcs.YellowBomb
    price = 25
    frog_coin_item = True
    tier = 4
    room_service = "Sleepy Bomb......"


class BadMushroom(RegularItem):
    item_name = "Bad Mushroom"
    index = 112
    description = "Poisons\x01an enemy"
    order = 1
    item_type = 3
    consumable = True
    status_immunities = [2]
    price = 30
    tier = 2
    model = npcs.RedMushroom
    room_service = "Bad Mushroom...."


class FireBomb(RegularItem):
    item_name = "Fire Bomb"
    index = 113
    description = "Hit all\x01enemies w/fire"
    model = npcs.RedBomb
    order = 27
    item_type = 3
    consumable = True
    price = 200
    tier = 3
    room_service = "Fire Bomb........."


class IceBomb(RegularItem):
    item_name = "Ice Bomb"
    index = 114
    description = "Hit all\x01enemies w/ice"
    model = npcs.BlueBomb
    order = 29
    item_type = 3
    consumable = True
    price = 250
    tier = 3
    room_service = "Ice Bomb.........."


class FlowerTab(RegularItem):
    index = 115
    description = "Raise FP by 1"
    order = 43
    item_type = 3
    consumable = True
    price = 200
    tier = 4
    room_service = "Flower Tab......."


class FlowerJar(RegularItem):
    index = 116
    description = "Raise FP by 3"
    order = 42
    item_type = 3
    consumable = True
    price = 600
    tier = 3
    room_service = "Flower Jar......."


class FlowerBox(RegularItem):
    index = 117
    description = "Raise FP by 5"
    order = 41
    item_type = 3
    consumable = True
    price = 1000
    tier = 2
    room_service = "Flower Box......."


class YoshiCandy(RegularItem):
    index = 118
    description = "Heals 100 HP"
    order = 25
    item_type = 3
    consumable = True
    price = 140
    model = npcs.GreenCandy
    tier = 4
    room_service = "Yoshi Candy......"


class FroggieDrink(RegularItem):
    index = 119
    description = "Party heals\x0130 HP"
    order = 7
    item_type = 3
    consumable = True
    price = 16
    tier = 4
    room_service = "FroggieDrink......"
    model = npcs.YellowMusicDrink


class MukuCookie(RegularItem):
    index = 120
    description = "Party heals\x0169 HP"
    order = 24
    item_type = 3
    consumable = True
    status_immunities = [0, 1, 2, 3, 4, 5, 6]
    model = npcs.Cookie
    price = 69
    tier = 3
    room_service = "Muku Cookie......"


class Elixir(RegularItem):
    index = 121
    description = "Party heals\x0180 HP"
    order = 4
    item_type = 3
    consumable = True
    price = 48
    tier = 3
    room_service = "Elixir............."
    model = npcs.BlueMusicDrink


class Megalixir(RegularItem):
    index = 122
    description = "Party heals\x01150 HP"
    order = 12
    item_type = 3
    consumable = True
    price = 120
    tier = 2
    room_service = "Megalixir.........."
    model = npcs.RedMusicDrink


class SeeYa(RegularItem):
    index = 123
    description = "Run away from\x01battles"
    order = 39
    item_type = 3
    price = 250
    frog_coin_item = True
    tier = 3
    unique = ItemUnique.Always
    dialog_replacements = [
        (
            2911,
            """ Item #1: An “Eject Button”!\n Sounds useful in a pinch, doesn't\n it?[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: An “Eject Button”.\n Sounds useful in a pinch, doesn't\n it?[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: An “Eject Button”.\n Sounds useful in a pinch, doesn't\n it?[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class TempleKey(RegularItem):
    index = 124
    order = 150
    item_type = 3
    is_key = True
    shuffle_type = ItemShuffleType.Required
    unique = ItemUnique.Always
    model = npcs.Key
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Golden Key”!\n I wonder what it opens?[await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Golden Key”.\n I wonder what it opens?[await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Golden Key”.\n I wonder what it opens?[await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class GoodieBag(RegularItem):
    index = 125
    order = 35
    item_type = 3
    price = 1110
    tier = 4
    unique = ItemUnique.Always
    description = "It's packed\x01full of coins"
    model = npcs.SmallCoin
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Coin Sack”!\n It could make you rich![await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Coin Sack”.\n It could make you rich![await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Coin Sack”.\n It could make you rich![await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class EarlierTimes(RegularItem):
    index = 126
    description = "Use it to start\x01a battle over"
    order = 34
    item_type = 3
    price = 375
    frog_coin_item = True
    tier = 5
    unique = ItemUnique.Always
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Reset Button”!\n Sounds useful in a pinch, doesn't\n it?[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Reset Button”.\n Sounds useful in a pinch, doesn't\n it?[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Reset Button”.\n Sounds useful in a pinch, doesn't\n it?[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class FreshenUp(RegularItem):
    index = 127
    description = "Heals party\x01status ailments"
    order = 6
    item_type = 3
    consumable = True
    status_immunities = [0, 1, 2, 3, 4, 5, 6]
    price = 50
    model = npcs.RDrink
    tier = 3
    room_service = "Freshen Up........"


class RareFrogCoin(RegularItem):
    index = 128
    order = 144
    item_type = 3
    is_key = True
    shuffle_type = ItemShuffleType.Required
    unique = ItemUnique.Always
    model = npcs.SmallFrogCoin
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Green Coin”!\n It looks different from most Frog\n Coins.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Green Coin”.\n It looks different from most Frog\n Coins.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Green Coin”.\n It looks different from most Frog\n Coins.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class Wallet(RegularItem):
    index = 129
    description = "A fat wallet"
    order = 152
    item_type = 3
    price = 246
    model = npcs.SmallCoin
    tier = 5
    unique = ItemUnique.Always
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Coin Sack”!\n It looks like it belongs to someone.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Coin Sack”.\n It looks like it belongs to someone.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Coin Sack”.\n It looks like it belongs to someone.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class CricketPie(RegularItem):
    index = 130
    order = 138
    is_key = True
    item_type = 3
    shuffle_type = ItemShuffleType.Required
    unique = ItemUnique.Always
    model = npcs.Cookie
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Baked Pastry”!\n Sorta makes you curious, doesn't\n it?[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Baked Pastry”.\n Sorta makes you curious, doesn't\n it?[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Baked Pastry”.\n Sorta makes you curious, doesn't\n it?[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class RockCandy(RegularItem):
    item_name = "Rock Candy"
    index = 131
    description = "Attack all\x01enemies"
    model = npcs.BlueCandy
    order = 31
    item_type = 3
    consumable = True
    price = 400
    tier = 1
    room_service = "Rock Candy......"


class CastleKey1(RegularItem):
    index = 132
    order = 135
    item_type = 3
    is_key = True
    shuffle_type = ItemShuffleType.Required
    unique = ItemUnique.Always
    model = npcs.Key
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Golden Key”!\n I wonder what it opens?[await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Golden Key”.\n I wonder what it opens?[await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Golden Key”.\n I wonder what it opens?[await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class CastleKey2(RegularItem):
    index = 134
    order = 136
    item_type = 3
    is_key = True
    shuffle_type = ItemShuffleType.Required
    unique = ItemUnique.Always
    model = npcs.Key
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Golden Key”!\n I wonder what it opens?[await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Golden Key”.\n I wonder what it opens?[await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Golden Key”.\n I wonder what it opens?[await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class BambinoBomb(RegularItem):
    index = 135
    order = 136
    item_type = 3
    is_key = True
    shuffle_type = ItemShuffleType.Required
    unique = ItemUnique.Always
    model = npcs.MicroBombItem


class SheepAttack(Item):
    index = 136
    description = "Baah, baah..."
    order = 40
    item_type = 3
    price = 150
    is_subitem = True
    tier = 3
    unique = ItemUnique.Always
    model = npcs.Egg
    dialog_replacements = [
        (
            2911,
            """ Item #1: “Shepherd's Bait”!\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class CarboCookie(RegularItem):
    index = 137
    description = "Kid's love 'em"
    order = 134
    item_type = 3
    unique = ItemUnique.Always
    is_subitem = True
    model = npcs.Cookie
    price = 2
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Trade Item”! It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(
            flags.FireworksSetting, FireworksOptions.shuffle1
        ) or world.settings.is_flag_value(
            flags.FireworksSetting, FireworksOptions.progressive
        ):
            self.price = 0
            self.description = ""


class ShinyStone(RegularItem):
    index = 138
    order = 148
    item_type = 3
    description = "A pretty stone!"
    is_subitem = True
    unique = ItemUnique.Always
    price = 4
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Trade Item”! It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(
            flags.FireworksSetting, FireworksOptions.shuffle1
        ) or world.settings.is_flag_value(
            flags.FireworksSetting, FireworksOptions.progressive
        ):
            self.price = 0
            self.description = ""


class RoomKey(RegularItem):
    index = 140
    order = 145
    item_type = 3
    is_key = True
    shuffle_type = ItemShuffleType.Required
    unique = ItemUnique.Always
    model = npcs.Key
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Golden Key”!\n I wonder what it opens?[await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Golden Key”.\n I wonder what it opens?[await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Golden Key”.\n I wonder what it opens?[await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class ElderKey(RegularItem):
    index = 141
    order = 140
    item_type = 3
    is_key = True
    shuffle_type = ItemShuffleType.Required
    unique = ItemUnique.Always
    model = npcs.Key
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Golden Key”!\n I wonder what it opens?[await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Golden Key”.\n I wonder what it opens?[await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Golden Key”.\n I wonder what it opens?[await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class ShedKey(RegularItem):
    index = 142
    order = 147
    item_type = 3
    is_key = True
    shuffle_type = ItemShuffleType.Required
    unique = ItemUnique.Always
    model = npcs.Key
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Golden Key”!\n I wonder what it opens?[await][pause] I'll sell it\n to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Golden Key”.\n I wonder what it opens?[await][pause] It's yours\n for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Golden Key”.\n I wonder what it opens?[await][pause] I'll sell it\n for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class LambsLure(RegularItem):
    index = 143
    description = "Baa, baa..."
    order = 36
    item_type = 3
    price = 40
    unique = ItemUnique.Always
    is_subitem = True
    model = npcs.Egg
    dialog_replacements = [
        (
            2911,
            """ Item #1: “Shepherd's Bait”!\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class FrightBomb(RegularItem):
    item_name = "Fright Bomb"
    index = 144
    description = "Inflict fear\x01on one enemy"
    model = npcs.GreenBomb
    order = 28
    item_type = 3
    consumable = True
    status_immunities = [3]
    price = 100
    tier = 3
    room_service = "Fright Bomb......"


class MysteryEgg(RegularItem):
    index = 145
    description = "A product of\x01pure love..."
    order = 38
    item_type = 3
    is_subitem = True
    price = 200
    unique = ItemUnique.Always
    model = npcs.Egg
    dialog_replacements = [
        (
            2911,
            """ Item #1: “Shepherd's Bait”!\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class BeetleBox(RegularItem):
    index = 146
    order = 130
    item_type = 3
    unique = ItemUnique.Always


class BeetleBox2(RegularItem):
    index = 147
    order = 131
    item_type = 3
    unique = ItemUnique.Always


class LuckyJewel(RegularItem):
    index = 148
    description = "Summons Luck\x01at will"
    order = 37
    item_type = 3
    price = 100
    unique = ItemUnique.Always
    tier = 5
    dialog_replacements = [
        (
            2911,
            """ Item #1: An “Lucky Jewel”!\n It’s sure to bring you plenty of\n good luck.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: An “Lucky Jewel”.\n It’s sure to bring you plenty of\n good luck.[await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: An “Lucky Jewel”.\n It’s sure to bring you plenty of\n good luck.[await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class SopranoCard(Item):
    index = 150
    order = 149
    item_type = 3
    is_key = True
    is_subitem = True
    unique = ItemUnique.Always
    model = npcs.Card
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Musical Card”!\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class AltoCard(Item):
    index = 151
    order = 129
    item_type = 3
    is_key = True
    is_subitem = True
    unique = ItemUnique.Always
    model = npcs.Card
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Musical Card”!\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class TenorCard(Item):
    index = 152
    order = 151
    item_type = 3
    is_key = True
    is_subitem = True
    unique = ItemUnique.Always
    model = npcs.Card
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Musical Card”!\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class Crystalline(RegularItem):
    index = 153
    description = "Raises party's\x01Defense in\x01battle"
    order = 3
    item_type = 3
    consumable = True
    status_buffs = [5, 6]
    price = 125
    frog_coin_item = True
    tier = 2
    room_service = "Crystalline......."
    model = npcs.DDrink


class PowerBlast(RegularItem):
    index = 154
    description = "Raises party's\x01Attack Power\x01in battle"
    order = 18
    item_type = 3
    consumable = True
    status_buffs = [3, 4]
    price = 125
    frog_coin_item = True
    tier = 2
    room_service = "Power Blast......"
    model = npcs.PDrink


class WiltShroom(RegularItem):
    index = 155
    description = "It's wilted..."
    order = 22
    item_type = 3
    consumable = True
    price = 8
    tier = 5
    model = npcs.Banana
    room_service = "Wilt Shroom......"


class RottenMush(RegularItem):
    index = 156
    description = "Eeew,\x01it's rotten!"
    order = 20
    item_type = 3
    consumable = True
    price = 4
    tier = 5
    model = npcs.Banana
    room_service = "Rotten Mush....."


class MoldyMush(RegularItem):
    index = 157
    description = "Gross!\x01There's mold\x01growing on it."
    order = 14
    item_type = 3
    consumable = True
    price = 2
    tier = 5
    model = npcs.Banana
    room_service = "Moldy Mush......."


class Seed(RegularItem):
    index = 158
    order = 146
    item_type = 3
    is_key = True
    shuffle_type = ItemShuffleType.Required
    unique = ItemUnique.Always
    model = npcs.Berry
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Mysterious Seed”!\n I wonder what will grow from it?[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Mysterious Seed”.\n I wonder what will grow from it?[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Mysterious Seed”.\n I wonder what will grow from it?[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class Fertilizer(RegularItem):
    index = 159
    order = 141
    item_type = 3
    is_key = True
    shuffle_type = ItemShuffleType.Required
    unique = ItemUnique.Always
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Bag of Dirt”!\n It seems different from the soil\n I dug it out of.[await][pause] I'll sell it to you\n for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Bag of Dirt”.\n It seems different from the soil\n I dug it out of.[await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Bag of Dirt”.\n It seems different from the soil\n I dug it out of.[await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class BigBooFlag(RegularItem):
    index = 161
    order = 132
    item_type = 3
    is_key = True
    shuffle_type = ItemShuffleType.Required
    model = npcs.Card
    unique = ItemUnique.Always
    dialog_replacements = [
        (
            2911,
            """ Item #1: An “Invisible Flag”!\n I wonder if someone is looking for\n this?[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: An “Invisible Flag”.\n I wonder if someone is looking for\n this?[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: An “Invisible Flag”.\n I wonder if someone is looking for\n this?[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class DryBonesFlag(RegularItem):
    index = 162
    order = 139
    item_type = 3
    is_key = True
    shuffle_type = ItemShuffleType.Required
    model = npcs.Card
    unique = ItemUnique.Always
    dialog_replacements = [
        (
            2911,
            """ Item #1: An “Invisible Flag”!\n I wonder if someone is looking for\n this?[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: An “Invisible Flag”.\n I wonder if someone is looking for\n this?[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: An “Invisible Flag”.\n I wonder if someone is looking for\n this?[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class GreaperFlag(RegularItem):
    index = 163
    order = 143
    item_type = 3
    is_key = True
    shuffle_type = ItemShuffleType.Required
    model = npcs.Card
    unique = ItemUnique.Always
    dialog_replacements = [
        (
            2911,
            """ Item #1: An “Invisible Flag”!\n I wonder if someone is looking for\n this?[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: An “Invisible Flag”.\n I wonder if someone is looking for\n this?[await][pause] It's yours for 200 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2914,
            """ Item #3: An “Invisible Flag”.\n I wonder if someone is looking for\n this?[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class CricketJam(RegularItem):
    index = 166
    order = 137
    item_type = 3
    shuffle_type = ItemShuffleType.Required
    model = npcs.GreenJuice
    is_key = True
    unique = ItemUnique.Always
    dialog_replacements = [
        (
            2911,
            """ Item #1: “Green Jelly”!\n Sorta makes you curious, doesn't\n it?[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: “Green Jelly”.\n Sorta makes you curious, doesn't\n it?[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: “Green Jelly”.\n Sorta makes you curious, doesn't\n it?[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class Fireworks(RegularItem):
    index = 172
    description = "A gorgeous\x01firework"
    item_type = 3
    unique = ItemUnique.Always
    chest_event = 3099
    npc_event = 184
    is_subitem = True
    overworld_event = 3112
    overworld_midas_event = 3398
    price = 500
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Trade Item”! It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(
            flags.FireworksSetting, FireworksOptions.shuffle1
        ) or world.settings.is_flag_value(
            flags.FireworksSetting, FireworksOptions.progressive
        ):
            self.price = 0
            self.description = ""
        if world.settings.is_flag_value(
            flags.FireworksSetting, FireworksOptions.shuffle1
        ):
            self.is_key = True
            self.is_subitem = False


class BrightCard(RegularItem):
    index = 174
    model = npcs.Card
    order = 133
    item_type = 3
    unique = ItemUnique.Always
    is_key = True
    tier = 1
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Shiny Card”!\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Shiny Card”.\n It's sure to bring you an air of\n prestige.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Shiny Card”.\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class Mushroom2(RegularItem):
    index = 175
    description = "Recoers 30 HP,\x01but..."
    order = 16
    item_type = 3
    consumable = True
    status_immunities = [5]
    price = 4
    tier = 5
    include_stats_in_patch = True
    model = npcs.RedMushroom
    room_service = "Mushroom........"


class StarEgg(RegularItem):
    index = 176
    description = "Reusable battle\x01item"
    order = 33
    item_type = 3
    price = 700
    tier = 1
    unique = ItemUnique.Always
    model = npcs.Egg
    dialog_replacements = [
        (
            2911,
            """ Item #1: An “Adorable Bomb”!\n Seems like it'll last a long time![await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: An “Adorable Bomb”.\n Seems like it'll last a long time![await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: An “Adorable Bomb”.\n Seems like it'll last a long time![await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


# ****************************** Other data classes


class MiscReward(Item):
    """Base class for items requiring special logic."""

    pass


# *** Progressive items


class ProgressiveItem(MiscReward):
    pass


class ProgressiveCard(ProgressiveItem):
    index = 195
    model = npcs.Card
    shuffle_type = ItemShuffleType.Required
    unique = ItemUnique.Always
    chest_event = 3086
    npc_event = 3097
    overworld_event = 3110
    overworld_midas_event = 3396
    item_type = 3
    is_key = True
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Musical Card”!\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Musical Card”.\n It's sure to bring you an air of\n prestige.[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class ProgressiveEgg(ProgressiveItem):
    index = 196
    model = npcs.Egg
    unique = ItemUnique.Always
    tier = 2
    chest_event = 3087
    npc_event = 3098
    overworld_event = 3111
    overworld_midas_event = 3397
    item_type = 3
    dialog_replacements = [
        (
            2911,
            """ Item #1: “Shepherd's Bait”!\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] It's yours for\n 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: “Shepherd's Bait”.\n You'll be the envy of sheep tamers\n everywhere![await][pause] I'll sell it for\n 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class ProgressiveFireworks(ProgressiveItem):
    index = 197
    unique = ItemUnique.Always
    chest_event = 3100
    npc_event = 185
    overworld_event = 3113
    overworld_midas_event = 3399
    item_type = 3
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Trade Item”! It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it to you for\n 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Trade Item”. It almost\n feels kind of sinister, somehow...[await][pause] I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


# *** Mimics


class MimicFight(MiscReward):
    """Base class for items requiring special logic."""

    pass


class PandoriteFight(MimicFight):
    index = 211
    unique = ItemUnique.Always
    tier = 1
    chest_event = 3124
    item_type = 3


class HidonFight(MimicFight):
    index = 212
    unique = ItemUnique.Always
    tier = 1
    chest_event = 3126
    item_type = 3


class BoxBoyFight(MimicFight):
    index = 213
    unique = ItemUnique.Always
    tier = 1
    chest_event = 2493
    item_type = 3


# *** Bosses


class BossFight(MiscReward):
    pass


class HammerBroBossFight(BossFight):
    related_class = bosses.HammerBroBoss
    index = 539


class Croco1BossFight(BossFight):
    related_class = bosses.Croco1Boss
    index = 540


class MackBossFight(BossFight):
    related_class = bosses.MackBoss
    index = 541


class PandoriteBossFight(BossFight):
    related_class = bosses.PandoriteBoss
    index = 542


class Belome1BossFight(BossFight):
    related_class = bosses.Belome1Boss
    index = 543


class BowyerBossFight(BossFight):
    related_class = bosses.BowyerBoss
    index = 544


class Croco2BossFight(BossFight):
    related_class = bosses.Croco2Boss
    index = 545


class PunchinelloBossFight(BossFight):
    related_class = bosses.PunchinelloBoss
    index = 546


class BoosterBossFight(BossFight):
    related_class = bosses.BoosterBoss
    index = 547


class GrateGuyBossFight(BossFight):
    related_class = bosses.GrateGuyBoss
    index = 548


class BundtBossFight(BossFight):
    related_class = bosses.BundtBoss
    index = 549


class KingCalamariBossFight(BossFight):
    related_class = bosses.KingCalamariBoss
    index = 550


class HidonBossFight(BossFight):
    related_class = bosses.HidonBoss
    index = 551


class JohnnyBossFight(BossFight):
    related_class = bosses.JohnnyBoss
    index = 552


class YaridovichBossFight(BossFight):
    related_class = bosses.YaridovichBoss
    index = 553


class MokuraBossFight(BossFight):
    related_class = bosses.MokuraBoss
    index = 554


class Belome2BossFight(BossFight):
    related_class = bosses.Belome2Boss
    index = 555


class JaggerBossFight(BossFight):
    related_class = bosses.JaggerBoss
    index = 556


class Jinx1BossFight(BossFight):
    related_class = bosses.Jinx1Boss
    index = 557


class Jinx2BossFight(BossFight):
    related_class = bosses.Jinx2Boss
    index = 558


class Jinx3BossFight(BossFight):
    related_class = bosses.Jinx3Boss
    index = 559


class CulexBossFight(BossFight):
    related_class = bosses.CulexBoss
    index = 560


class BoxBoyBossFight(BossFight):
    related_class = bosses.BoxBoyBoss
    index = 561


class MegaSmilaxBossFight(BossFight):
    related_class = bosses.MegaSmilaxBoss
    index = 562


class DodoBossFight(BossFight):
    related_class = bosses.DodoBoss
    index = 563


class BirdettaBossFight(BossFight):
    related_class = bosses.BirdettaBoss
    index = 564


class ValentinaBossFight(BossFight):
    related_class = bosses.ValentinaBoss
    index = 565


class CzarDragonBossFight(BossFight):
    related_class = bosses.CzarBoss
    index = 566


class AxemRangersBossFight(BossFight):
    related_class = bosses.AxemRangersBoss
    index = 567


class ChesterBossFight(BossFight):
    related_class = bosses.ChesterBoss
    index = 568


class MagikoopaBossFight(BossFight):
    related_class = bosses.MagikoopaBoss
    index = 569


class BoomerBossFight(BossFight):
    related_class = bosses.BoomerBoss
    index = 570


class ExorBossFight(BossFight):
    related_class = bosses.ExorBoss
    index = 571


class CountdownBossFight(BossFight):
    related_class = bosses.CountdownBoss
    index = 572


class CloakerDominoBossFight(BossFight):
    related_class = bosses.CloakerDominoBoss
    index = 573


class ClerkBossFight(BossFight):
    related_class = bosses.ClerkBoss
    index = 574


class ManagerBossFight(BossFight):
    related_class = bosses.ManagerBoss
    index = 575


class DirectorBossFight(BossFight):
    related_class = bosses.DirectorBoss
    index = 576


class GunyolkBossFight(BossFight):
    related_class = bosses.GunyolkBoss
    index = 577


class SmithyBossFight(BossFight):
    related_class = bosses.SmithyBoss
    index = 578


# *** Spells


class SpellLearn(MiscReward):
    damaging = True


class JumpLearn(SpellLearn):
    related_class = spells.Jump
    index = 512


class FireOrbLearn(SpellLearn):
    related_class = spells.FireOrb
    index = 513


class SuperJumpLearn(SpellLearn):
    related_class = spells.SuperJump
    index = 514


class SuperFlameLearn(SpellLearn):
    related_class = spells.SuperFlame
    index = 515


class UltraJumpLearn(SpellLearn):
    related_class = spells.UltraJump
    index = 516


class UltraFlameLearn(SpellLearn):
    related_class = spells.UltraFlame
    index = 517


class TherapyLearn(SpellLearn):
    related_class = spells.Therapy
    damaging = False
    index = 518


class GroupHugLearn(SpellLearn):
    related_class = spells.GroupHug
    damaging = False
    index = 519


class SleepyTimeLearn(SpellLearn):
    related_class = spells.SleepyTime
    index = 520


class ComeBackLearn(SpellLearn):
    related_class = spells.ComeBack
    damaging = False
    index = 521


class MuteLearn(SpellLearn):
    related_class = spells.Mute
    damaging = False
    index = 522


class PsychBombLearn(SpellLearn):
    related_class = spells.PsychBomb
    index = 523


class TerrorizeLearn(SpellLearn):
    related_class = spells.Terrorize
    index = 524


class PoisonGasLearn(SpellLearn):
    related_class = spells.PoisonGas
    index = 525


class CrusherLearn(SpellLearn):
    related_class = spells.Crusher
    index = 526


class BowserCrushLearn(SpellLearn):
    related_class = spells.BowserCrush
    index = 527


class GenoBeamLearn(SpellLearn):
    related_class = spells.GenoBeam
    index = 528


class GenoBoostLearn(SpellLearn):
    related_class = spells.GenoBoost
    damaging = False
    index = 529


class GenoWhirlLearn(SpellLearn):
    related_class = spells.GenoWhirl
    index = 530


class GenoBlastLearn(SpellLearn):
    related_class = spells.GenoBlast
    index = 531


class GenoFlashLearn(SpellLearn):
    related_class = spells.GenoFlash
    index = 532


class ThunderboltLearn(SpellLearn):
    related_class = spells.Thunderbolt
    index = 533


class HPRainLearn(SpellLearn):
    related_class = spells.HPRain
    damaging = False
    index = 534


class PsychopathLearn(SpellLearn):
    related_class = spells.Psychopath
    damaging = False
    index = 535


class ShockerLearn(SpellLearn):
    related_class = spells.Shocker
    index = 536


class SnowyLearn(SpellLearn):
    related_class = spells.Snowy
    index = 537


class StarRainLearn(SpellLearn):
    related_class = spells.StarRain
    index = 538


# *** Coins


class Coins(MiscReward):
    index = 192
    tier = 1
    amount = 0
    multiplier = 0
    chest_event = 3074
    quick_chest_event = 3080
    npc_event = 159
    item_type = 3

    # coins and multi frog coins need 6 different events
    # because they run on per-chest counters (0x70DA-0x70DD and 0x70F8-0x70F9)
    def get_chest_event(self, parent):
        if parent == 246:
            return 3401
        elif parent == 245:
            return 3402
        elif parent == 244:
            return 3403
        elif parent == 243:
            return 3404
        elif parent == 242:
            return 3405
        else:
            return 3074

    def __init__(self, amount, world=None):
        """

        Args:
            world (randomizer.logic.main.GameWorld):
            amount (int)

        """
        super().__init__(world)
        if amount < 10:
            self.chest_70A7_upper = 8
            self.chest_70A7_lower = amount
            self.model = npcs.SmallCoin
        else:
            self.model = npcs.BigCoin
            self.chest_70A7_upper = 10
            hits = amount // 10
            loops = hits // 16
            leftover = hits - 15 * loops
            self.multiplier = int(loops)
            self.chest_70A7_lower = int(leftover)
        self.amount = int(amount)


class Coins10(Coins):
    index = 193
    tier = 1
    overworld_event = 3146
    overworld_midas_event = 2818
    model = npcs.BigCoin
    amount = 10

    def __init__(self, world):
        super().__init__(10, world)


class Coins1(Coins):
    index = 194
    tier = 1
    overworld_event = 1293
    overworld_midas_event = 2819
    model = npcs.SmallCoin
    amount = 1

    def __init__(self, world):
        super().__init__(1, world)


# *** Misc.


class Beetlemania(MiscReward):
    index = 164
    unique = ItemUnique.Always
    model = npcs.Beetle
    tier = 1
    chest_event = 162
    npc_event = 161
    overworld_event = 3109
    overworld_midas_event = 3395
    price = 500
    item_type = 3
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Handheld Game”!\n Sounds pretty fun, doesn't it?[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Handheld Game”.\n Sounds pretty fun, doesn't it?[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Handheld Game”.\n Sounds pretty fun, doesn't it?[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


# slot machine needs to write its own events using data/eventscripts/utils/slot_machine, logic for this contained elsewhere


class SlotMachineChest(MiscReward):
    index = 214
    tier = 2
    unique = ItemUnique.BalancedOnly
    item_type = 3


class InfiniteCoins(MiscReward):
    index = 240
    unique = ItemUnique.Always
    chest_event = 3074
    tier = 2
    chest_70A7_lower = 0
    chest_70A7_upper = 15
    item_type = 3


class StarPiece(MiscReward):
    hint_bit = None
    index = 230
    tier = 4
    unique = ItemUnique.Always
    chest_event = 163
    npc_event = 164
    overworld_event = 166
    overworld_midas_event = 2821
    model = npcs.TinyStar
    item_type = 3
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Shooting Star”!\n It's sure to make all your wishes\n come true.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Shooting Star”.\n It's sure to make all your wishes\n come true.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Shooting Star”.\n It's sure to make all your wishes\n come true.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class StarPiece1(StarPiece):
    hint_bit = (0x7081, 5)


class StarPiece2(StarPiece):
    hint_bit = (0x7081, 6)


class StarPiece3(StarPiece):
    hint_bit = (0x7082, 1)


class StarPiece4(StarPiece):
    hint_bit = (0x7082, 2)


class StarPiece5(StarPiece):
    hint_bit = (0x7084, 4)


class StarPiece6(StarPiece):
    hint_bit = (0x7085, 5)


class StarPiece7(StarPiece):
    hint_bit = (0x7085, 6)


class Nothing(MiscReward):
    chest_event = 3081
    npc_event = 256
    model = npcs.Empty
    overworld_midas_event = 256
    overworld_event = 256
    item_type = 3


class Flower(MiscReward):
    index = 198
    tier = 1
    model = npcs.Flower
    chest_70A7_upper = 2
    packet = 35
    chest_event = 3072
    overworld_event = 1801
    overworld_midas_event = 2817
    item_type = 3


class RecoveryMushroom(MiscReward):
    index = 199
    tier = 1
    packet = 36
    chest_event = 3072
    overworld_event = 2822
    npc_event = 397
    overworld_midas_event = 2822
    model = npcs.RecoveryMushroom
    item_type = 3


class FrogCoin(MiscReward):
    index = 200
    tier = 1
    amount = 0
    model = npcs.FrogCoin
    chest_70A7_upper = 3
    chest_event = 3072
    npc_event = 157
    overworld_event = 3238
    overworld_midas_event = 2816
    item_type = 3


class MultiFrogCoin(MiscReward):
    index = 215
    tier = 2
    amount = 0
    multiplier = 0
    chest_event = 3091
    quick_chest_event = 3082
    model = npcs.FrogCoin
    npc_event = 158
    chest_70A7_upper = 0
    item_type = 3

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

    def __init__(self, world, amount):
        """

        Args:
            world (randomizer.logic.main.GameWorld):
            amount (int)

        """
        super().__init__(world)
        hits = amount
        loops = hits // 16
        leftover = hits - 15 * loops
        self.multiplier = int(loops)
        self.chest_70A7_lower = int(leftover)
        self.amount = int(amount)


class YouMissed(MiscReward):
    index = 210
    tier = 1
    chest_event = 3081
    item_type = 3


# *** Invincibility stars


class InvincibilityStar(MiscReward):
    """Base class for invincibility stars."""

    tier = 0
    chest_70A7_upper = 1
    chest_event = 3072
    item_type = 3
    pass


class BanditsWayStar(InvincibilityStar):
    index = 201
    tier = 1


class KeroSewersStar(InvincibilityStar):
    index = 202
    tier = 1
    chest_70A7_lower = 1


class MolevilleMinesStar(InvincibilityStar):
    index = 203
    tier = 2
    chest_70A7_lower = 2


class SeaStar(InvincibilityStar):
    index = 204
    tier = 3
    chest_70A7_lower = 3


class LandsEndVolcanoStar(InvincibilityStar):
    index = 205
    tier = 4
    chest_70A7_lower = 5


class NimbusLandStar(InvincibilityStar):
    index = 206
    tier = 2
    chest_70A7_lower = 7


class LandsEndStar2(InvincibilityStar):
    index = 207
    tier = 3
    chest_70A7_lower = 8


class LandsEndStar3(InvincibilityStar):
    index = 208
    tier = 3
    chest_70A7_lower = 9


# *** Characters


class RecruitedCharacter(Item):
    starter_script = None
    container_script = None
    model = None
    sprites_primary = {}
    sprites_secondary = {}
    item_type = 3
    doll = None
    placeholder = "`NAME`"
    gender = "man"
    gender_casual = "guy"
    honorific = "sir"
    title = "mister"
    title_short = "Mr"
    mole_greeting = "mate"
    mboy_greeting = ", man"


class MarioRecruit(RecruitedCharacter):
    index = 220
    description = PlayableCharacters.mario.value
    related_class = Mario
    placeholder = "`MARIO_NAME`"
    starter_script = 187
    container_script = 193
    model = npcs.Mario
    doll = npcs.MarioDoll
    sprites_primary = {
        "south": (0, 12, True),
        "defend": (2, 16, True),
        "face_north": (0, 1, False),
        "face_south": (0, 0, False),
        "shocked_loop": (3, 8, False),
        "shocked_loop_backwards": (3, 9, False),
        "shocked_backwards_sequence": (2, 3, False),
        "shocked_shadow": (3, 0, False),
        "shocked_shadow_backwards": (2, 8, True),
        "crying": (3, 3, False),
        "crying_backwards": (3, 4, False),
        "looking_down_static": (0, 6, True),
        "looking_down": (0, 6, False),
        "looking_down_away": (0, 7, False),
        "floored": (3, 1, True),
        "hurt": (0, 6, True),
        "shaking_head": (0, 8, False),
        "shaking_head_backward": (0, 9, False),
        "sleeping": (2, 6, False),
        "salute": (2, 9, False),
        "joy": (2, 9, False),
        "joy_behind": (3, 2, False),
        "joy_jump": (3, 2, False),
        "distracted": (0, 10, True),
        "displeased": (3, 4, False),
        "challenge": (4, 2, False),
        "look_to_side": (0, 8, True),
        "look_to_down": (0, 9, True),
        "look_to_side_behind": (0, 11, True),
        "cast_frame_1": (2, 12, True),
        "cast_frame_2": (2, 13, True),
        "cast_frame_3": (2, 14, True),
        "cast_frame_4": (2, 15, True),
        "look_up_slightly": (2, 23, True),
        "look_way_up": (2, 24, True),
        "victory_pose": (2, 10, True),
        "prince_neutral": (0, 0, True),
        "prince_down": (0, 9, True),
        "prince_left": (0, 8, True),
        "hammer": (2, 3, True),
        "hammer_static": (2, 3, True),
    }
    sprites_secondary = {
        "south": (0, 20, True),
        "defend": (1, 16, True),
        "face_north": (0, 1, False),
        "face_south": (0, 0, False),
        "shocked_loop": (2, 8, False),
        "shocked_loop_backwards": (2, 9, False),
        "shocked_backwards_sequence": (1, 3, False),
        "shocked_shadow": (2, 0, False),
        "shocked_shadow_backwards": (1, 8, True),
        "crying": (0, 4, False),
        "crying_backwards": (0, 5, False),
        "looking_down_static": (0, 14, True),
        "looking_down": (0, 6, False),
        "looking_down_away": (0, 7, False),
        "floored": (2, 1, True),
        "hurt": (0, 14, True),
        "shaking_head": (0, 8, False),
        "shaking_head_backward": (0, 9, False),
        "sleeping": (1, 6, False),
        "salute": (1, 9, False),
        "joy": (1, 9, False),
        "joy_behind": (2, 2, False),
        "joy_jump": (2, 2, False),
        "distracted": (0, 18, True),
        "displeased": (0, 5, False),
        "challenge": (3, 2, False),
        "look_to_side": (0, 16, True),
        "look_to_down": (0, 17, True),
        "look_to_side_behind": (0, 19, True),
        "cast_frame_1": (1, 12, True),
        "cast_frame_2": (1, 13, True),
        "cast_frame_3": (1, 14, True),
        "cast_frame_4": (1, 15, True),
        "look_up_slightly": (1, 23, True),
        "look_way_up": (1, 24, True),
        "victory_pose": (1, 10, True),
        "prince_neutral": (0, 0, True),
        "prince_down": (0, 17, True),
        "prince_left": (0, 16, True),
        "hammer": (1, 3, True),
        "hammer_static": (1, 3, True),
    }


class ToadstoolRecruit(RecruitedCharacter):
    index = 221
    description = PlayableCharacters.toadstool.value
    related_class = Peach
    placeholder = "`PEACH_NAME`"
    gender = "woman"
    gender_casual = "gal"
    honorific = "ma'am"
    title = "miss"
    title_short = "Ms"
    mole_greeting = "mate"
    mboy_greeting = ""
    starter_script = 191
    container_script = 197
    doll = npcs.ToadstoolDoll
    model = npcs.Toadstool
    sprites_primary = {
        "south": (0, 12, True),
        "defend": (2, 15, True),
        "face_north": (0, 1, False),
        "face_south": (0, 0, False),
        "shocked_loop": (3, 8, False),
        "shocked_loop_backwards": (3, 9, False),
        "shocked_backwards_sequence": (2, 3, False),
        "shocked_shadow": (3, 0, False),
        "shocked_shadow_backwards": (2, 8, True),
        "crying": (3, 3, False),
        "crying_backwards": (3, 4, False),
        "looking_down_static": (0, 6, True),
        "looking_down": (0, 6, False),
        "looking_down_away": (0, 7, False),
        "floored": (3, 1, True),
        "hurt": (0, 6, True),
        "shaking_head": (0, 8, False),
        "shaking_head_backward": (0, 9, False),
        "sleeping": (2, 6, False),
        "salute": (2, 9, False),
        "joy": (2, 9, False),
        "joy_jump": (3, 2, False),
        "joy_behind": (3, 2, False),
        "distracted": (0, 18, True),
        "displeased": (0, 5, False),
        "challenge": (4, 5, False),
        "look_to_side": (0, 8, True),
        "look_to_down": (0, 9, True),
        "look_to_side_behind": (0, 11, True),
        "cast_frame_1": (2, 10, True),
        "cast_frame_2": (2, 11, True),
        "cast_frame_3": (2, 12, True),
        "cast_frame_4": (2, 14, True),
        "look_up_slightly": (2, 22, True),
        "look_way_up": (2, 23, True),
        "victory_pose": (2, 10, True),
        "prince_neutral": (0, 0, True),
        "prince_down": (0, 9, True),
        "prince_left": (0, 8, True),
        "hammer": (2, 3, True),
        "hammer_static": (2, 3, True),
    }
    sprites_secondary = {
        "south": (0, 20, True),
        "defend": (1, 15, True),
        "face_north": (0, 1, False),
        "face_south": (0, 0, False),
        "shocked_loop": (2, 3, False),
        "shocked_loop_backwards": (2, 4, False),
        "shocked_backwards_sequence": (1, 3, False),
        "shocked_shadow": (2, 0, False),
        "shocked_shadow_backwards": (1, 8, True),
        "crying": (0, 13, False),
        "crying_backwards": (0, 14, False),
        "looking_down_static": (0, 14, True),
        "looking_down": (0, 6, False),
        "looking_down_away": (0, 7, False),
        "floored": (2, 1, True),
        "hurt": (5, 0, True),
        "shaking_head": (0, 8, False),
        "shaking_head_backward": (0, 9, False),
        "sleeping": (1, 6, False),
        "salute": (1, 9, False),
        "joy": (1, 9, False),
        "joy_behind": (2, 2, False),
        "joy_jump": (2, 5, False),
        "distracted": (0, 18, True),
        "displeased": (0, 5, False),
        "challenge": (3, 5, False),
        "look_to_side": (0, 16, True),
        "look_to_down": (0, 17, True),
        "look_to_side_behind": (0, 19, True),
        "cast_frame_1": (1, 10, True),
        "cast_frame_2": (1, 11, True),
        "cast_frame_3": (1, 12, True),
        "cast_frame_4": (1, 14, True),
        "look_up_slightly": (1, 22, True),
        "look_way_up": (1, 23, True),
        "victory_pose": (1, 10, True),
        "prince_neutral": (0, 0, True),
        "prince_down": (0, 17, True),
        "prince_left": (0, 16, True),
        "hammer": (1, 3, True),
        "hammer_static": (1, 3, True),
    }


class MallowRecruit(RecruitedCharacter):
    index = 222
    description = PlayableCharacters.mallow.value
    related_class = Mallow
    placeholder = "`MALLOW_NAME`"
    starter_script = 188
    container_script = 194
    doll = npcs.MallowDoll
    model = npcs.Mallow
    sprites_primary = {
        "south": (0, 12, True),
        "defend": (2, 15, True),
        "face_north": (0, 1, False),
        "face_south": (0, 0, False),
        "shocked_loop": (3, 8, False),
        "shocked_loop_backwards": (3, 9, False),
        "shocked_backwards_sequence": (2, 3, False),
        "shocked_shadow": (3, 0, False),
        "shocked_shadow_backwards": (2, 8, True),
        "crying": (3, 3, False),
        "crying_backwards": (3, 4, False),
        "looking_down_static": (0, 6, True),
        "looking_down": (0, 6, False),
        "looking_down_away": (0, 7, False),
        "floored": (3, 1, True),
        "hurt": (0, 6, True),
        "shaking_head": (0, 8, False),
        "shaking_head_backward": (0, 9, False),
        "sleeping": (2, 6, False),
        "salute": (2, 9, False),
        "joy": (2, 9, False),
        "joy_behind": (3, 2, False),
        "joy_jump": (3, 2, False),
        "distracted": (0, 10, True),
        "displeased": (3, 4, False),
        "challenge": (4, 5, False),
        "look_to_side": (0, 8, True),
        "look_to_down": (0, 9, True),
        "look_to_side_behind": (0, 11, True),
        "cast_frame_1": (2, 11, True),
        "cast_frame_2": (2, 12, True),
        "cast_frame_3": (2, 13, True),
        "cast_frame_4": (2, 10, True),
        "look_up_slightly": (2, 22, True),
        "look_way_up": (2, 23, True),
        "victory_pose": (2, 10, True),
        "prince_neutral": (0, 0, True),
        "prince_down": (0, 9, True),
        "prince_left": (0, 8, True),
        "hammer": (2, 3, True),
        "hammer_static": (2, 3, True),
    }
    sprites_secondary = {
        "south": (0, 20, True),
        "defend": (1, 15, True),
        "face_north": (0, 1, False),
        "face_south": (0, 0, False),
        "shocked_loop": (2, 8, False),
        "shocked_loop_backwards": (2, 9, False),
        "shocked_backwards_sequence": (1, 3, False),
        "shocked_shadow": (2, 0, False),
        "shocked_shadow_backwards": (1, 8, True),
        "crying": (0, 13, False),
        "crying_backwards": (0, 14, False),
        "looking_down_static": (0, 14, True),
        "looking_down": (0, 6, False),
        "looking_down_away": (0, 7, False),
        "floored": (2, 1, True),
        "hurt": (0, 14, True),
        "shaking_head": (0, 8, False),
        "shaking_head_backward": (0, 9, False),
        "sleeping": (1, 6, False),
        "salute": (2, 17, True),
        "joy": (1, 9, False),
        "joy_behind": (2, 2, False),
        "joy_jump": (2, 2, False),
        "distracted": (0, 18, True),
        "displeased": (0, 5, False),
        "challenge": (3, 5, False),
        "look_to_side": (0, 16, True),
        "look_to_down": (0, 17, True),
        "look_to_side_behind": (0, 19, True),
        "cast_frame_1": (1, 11, True),
        "cast_frame_2": (1, 12, True),
        "cast_frame_3": (1, 13, True),
        "cast_frame_4": (1, 10, True),
        "look_up_slightly": (1, 22, True),
        "look_way_up": (1, 23, True),
        "victory_pose": (1, 10, True),
        "prince_neutral": (2, 14, True),
        "prince_down": (2, 15, True),
        "prince_left": (2, 16, True),
        "hammer": (1, 3, True),
        "hammer_static": (1, 3, True),
    }


class GenoRecruit(RecruitedCharacter):
    index = 223
    description = PlayableCharacters.geno.value
    related_class = Geno
    placeholder = "`GENO_NAME`"
    starter_script = 189
    container_script = 195
    doll = npcs.GenoDoll
    model = npcs.Geno
    sprites_primary = {
        "south": (0, 12, True),
        "defend": (2, 16, True),
        "face_north": (0, 1, False),
        "face_south": (0, 0, False),
        "shocked_loop": (3, 8, False),
        "shocked_loop_backwards": (3, 9, False),
        "shocked_backwards_sequence": (2, 3, False),
        "shocked_shadow": (3, 0, False),
        "shocked_shadow_backwards": (2, 8, True),
        "crying": (3, 3, False),
        "crying_backwards": (3, 4, False),
        "looking_down_static": (0, 6, True),
        "looking_down": (0, 6, False),
        "looking_down_away": (0, 7, False),
        "floored": (3, 1, True),
        "hurt": (0, 6, True),
        "shaking_head": (0, 8, False),
        "shaking_head_backward": (0, 9, False),
        "sleeping": (2, 6, False),
        "salute": (2, 9, False),
        "joy": (2, 9, False),
        "joy_behind": (3, 2, False),
        "joy_jump": (3, 2, False),
        "distracted": (0, 10, True),
        "displeased": (3, 4, False),
        "challenge": (4, 0, False),
        "look_to_side": (0, 8, True),
        "look_to_down": (0, 9, True),
        "look_to_side_behind": (0, 11, True),
        "cast_frame_1": (2, 12, True),
        "cast_frame_2": (2, 13, True),
        "cast_frame_3": (2, 14, True),
        "cast_frame_4": (2, 15, True),
        "look_up_slightly": (2, 23, True),
        "look_way_up": (2, 24, True),
        "victory_pose": (2, 10, True),
        "prince_neutral": (0, 0, True),
        "prince_down": (0, 9, True),
        "prince_left": (0, 8, True),
        "hammer": (2, 3, True),
        "hammer_static": (2, 3, True),
    }
    sprites_secondary = {
        "south": (0, 20, True),
        "defend": (1, 16, True),
        "face_north": (0, 1, False),
        "face_south": (0, 0, False),
        "shocked_loop": (2, 8, False),
        "shocked_loop_backwards": (2, 9, False),
        "shocked_backwards_sequence": (1, 3, False),
        "shocked_shadow": (2, 0, False),
        "shocked_shadow_backwards": (1, 8, True),
        "crying": (0, 11, False),
        "crying_backwards": (0, 12, False),
        "looking_down_static": (0, 14, True),
        "looking_down": (0, 6, False),
        "looking_down_away": (0, 7, False),
        "floored": (2, 1, True),
        "hurt": (0, 22, True),
        "shaking_head": (0, 8, False),
        "shaking_head_backward": (0, 9, False),
        "sleeping": (1, 6, False),
        "salute": (1, 9, False),
        "joy": (1, 9, False),
        "joy_behind": (2, 2, False),
        "joy_jump": (2, 2, False),
        "distracted": (0, 19, True),
        "displeased": (0, 5, False),
        "challenge": (3, 0, False),
        "look_to_side": (0, 16, True),
        "look_to_down": (0, 17, True),
        "look_to_side_behind": (0, 19, True),
        "cast_frame_1": (1, 12, True),
        "cast_frame_2": (1, 13, True),
        "cast_frame_3": (1, 14, True),
        "cast_frame_4": (1, 15, True),
        "look_up_slightly": (1, 23, True),
        "look_way_up": (1, 24, True),
        "victory_pose": (1, 10, True),
        "prince_neutral": (0, 0, True),
        "prince_down": (0, 17, True),
        "prince_left": (0, 16, True),
        "hammer": (1, 3, True),
        "hammer_static": (1, 3, True),
    }


class BowserRecruit(RecruitedCharacter):
    index = 224
    model = npcs.Bowser
    related_class = Bowser
    description = PlayableCharacters.bowser.value
    placeholder = "`BOWSER_NAME`"
    starter_script = 190
    container_script = 196
    doll = npcs.BowserDoll
    sprites_primary = {
        "south": (0, 12, True),
        "defend": (2, 17, True),
        "face_north": (0, 1, False),
        "face_south": (0, 0, False),
        "shocked_loop": (3, 8, False),
        "shocked_loop_backwards": (3, 9, False),
        "shocked_backwards_sequence": (2, 3, False),
        "shocked_shadow": (3, 0, False),
        "shocked_shadow_backwards": (2, 8, True),
        "crying": (3, 3, False),
        "crying_backwards": (3, 4, False),
        "looking_down_static": (0, 6, True),
        "looking_down": (0, 6, False),
        "looking_down_away": (0, 7, False),
        "floored": (3, 1, True),
        "hurt": (0, 6, True),
        "shaking_head": (0, 8, False),
        "shaking_head_backward": (0, 9, False),
        "sleeping": (2, 6, False),
        "salute": (2, 9, False),
        "joy": (2, 9, False),
        "joy_behind": (3, 2, False),
        "joy_jump": (3, 2, False),
        "distracted": (0, 10, True),
        "displeased": (3, 4, False),
        "challenge": (4, 4, False),
        "look_to_side": (0, 8, True),
        "look_to_down": (0, 9, True),
        "look_to_side_behind": (0, 11, True),
        "cast_frame_1": (2, 10, True),
        "cast_frame_2": (2, 11, True),
        "cast_frame_3": (2, 12, True),
        "cast_frame_4": (2, 13, True),
        "look_up_slightly": (2, 24, True),
        "look_way_up": (2, 25, True),
        "victory_pose": (2, 10, True),
        "prince_neutral": (0, 0, True),
        "prince_down": (0, 9, True),
        "prince_left": (0, 8, True),
        "hammer": (2, 3, True),
        "hammer_static": (2, 3, True),
    }
    sprites_secondary = {
        "south": (0, 20, True),
        "defend": (1, 17, True),
        "face_north": (0, 1, False),
        "face_south": (0, 0, False),
        "shocked_loop": (2, 8, False),
        "shocked_loop_backwards": (2, 9, False),
        "shocked_backwards_sequence": (1, 3, False),
        "shocked_shadow": (2, 0, False),
        "shocked_shadow_backwards": (1, 8, True),
        "crying": (0, 13, False),
        "crying_backwards": (0, 14, False),
        "looking_down_static": (0, 14, True),
        "looking_down": (0, 6, False),
        "looking_down_away": (0, 7, False),
        "floored": (2, 1, True),
        "hurt": (0, 6, False),
        "shaking_head": (0, 8, False),
        "shaking_head_backward": (0, 9, False),
        "sleeping": (1, 6, False),
        "salute": (1, 9, False),
        "joy": (1, 9, False),
        "joy_behind": (2, 2, False),
        "joy_jump": (2, 2, False),
        "distracted": (0, 18, True),
        "displeased": (0, 5, False),
        "challenge": (3, 4, False),
        "look_to_side": (0, 16, True),
        "look_to_down": (0, 17, True),
        "look_to_side_behind": (0, 19, True),
        "cast_frame_1": (1, 10, True),
        "cast_frame_2": (1, 11, True),
        "cast_frame_3": (1, 12, True),
        "cast_frame_4": (1, 13, True),
        "look_up_slightly": (1, 24, True),
        "look_way_up": (1, 25, True),
        "victory_pose": (1, 10, True),
        "prince_neutral": (0, 0, True),
        "prince_down": (0, 17, True),
        "prince_left": (0, 16, True),
        "hammer": (2, 4, False),
        "hammer_static": (2, 13, True),
    }


class SpottedCharacter(Item):
    starter_script = None
    container_script = None
    item_type = 3


class MarioSpotted(SpottedCharacter):
    index = 225


class ToadstoolSpotted(SpottedCharacter):
    index = 226


class MallowSpotted(SpottedCharacter):
    index = 227


class GenoSpotted(SpottedCharacter):
    index = 228


class BowserSpotted(SpottedCharacter):
    index = 229


class MarrymoreGear(MiscReward):
    pass


class Shoes(MarrymoreGear):
    index = 230
    unique = ItemUnique.Always
    chest_event = 3943
    npc_event = 3931
    overworld_event = 3935
    overworld_midas_event = 3939
    model = npcs.Shoes
    price = 0
    item_type = 3
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Pair of Fancy Shoes”!\n I bet they would look great on you.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Pair of Fancy Shoes”.\n I bet they would look great on you.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Pair of Fancy Shoes”.\n I bet they would look great on you.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class Brooch(MarrymoreGear):
    index = 231
    unique = ItemUnique.Always
    chest_event = 3944
    npc_event = 3932
    overworld_event = 3936
    overworld_midas_event = 3940
    model = npcs.Brooch
    price = 0
    item_type = 3
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Shiny Brooch”! It\n looks made for special occasions.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Shiny Brooch”. It\n looks made for special occasions.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Shiny Brooch”. It\n looks made for special occasions.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class Ring(MarrymoreGear):
    index = 232
    unique = ItemUnique.Always
    chest_event = 3945
    npc_event = 3933
    overworld_event = 3937
    overworld_midas_event = 3941
    model = npcs.Ring
    item_type = 3
    price = 0
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Diamond Ring”! It's\n a great gift for someone special.[await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Diamond Ring”. It's\n a great gift for someone special.[await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Diamond Ring”. It's\n a great gift for someone special.[await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


class Crown(MarrymoreGear):
    index = 233
    unique = ItemUnique.Always
    chest_event = 3946
    npc_event = 3934
    overworld_event = 3938
    overworld_midas_event = 3942
    model = npcs.Crown
    item_type = 3
    price = 0
    dialog_replacements = [
        (
            2911,
            """ Item #1: A “Royal Crown”!\n It looks pretty important![await]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]""",
        ),
        (
            2908,
            """ Item #2: A “Royal Crown”.\n It looks pretty important![await]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]""",
        ),
        (
            2914,
            """ Item #3: A “Royal Crown”.\n It looks pretty important![await]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]""",
        ),
    ]


# ********************* Default item lists for world


def get_recruitable_characters(world):
    return [
        MarioRecruit(world),
        MallowRecruit(world),
        GenoRecruit(world),
        BowserRecruit(world),
        ToadstoolRecruit(world),
    ]


def get_default_items(world):
    """Get default vanilla item list for the world.

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        list[Item]: List of default item objects.

    """
    items = [
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
        RoomKey(world),
        ElderKey(world),
        ShedKey(world),
        FrightBomb(world),
        LuckyJewel(world),
        ProgressiveCard(world),
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
        BrightCard(world),
        Mushroom2(world),
        StarEgg(world),
        ProgressiveEgg(world),
        Fireworks(world),
        ShinyStone(world),
        CarboCookie(world),
        MysteryEgg(world),
        LambsLure(world),
        SheepAttack(world),
        AltoCard(world),
        SopranoCard(world),
        TenorCard(world)
    ]

    if world.settings.is_flag_value(
        flags.FireworksSetting, FireworksOptions.progressive
    ):
        items.append(ProgressiveFireworks(world))

    return items


def get_placeable_spells(world):
    return [
        JumpLearn(world),
        FireOrbLearn(world),
        SuperJumpLearn(world),
        SuperFlameLearn(world),
        UltraJumpLearn(world),
        UltraFlameLearn(world),
        TherapyLearn(world),
        GroupHugLearn(world),
        SleepyTimeLearn(world),
        ComeBackLearn(world),
        MuteLearn(world),
        PsychBombLearn(world),
        TerrorizeLearn(world),
        PoisonGasLearn(world),
        CrusherLearn(world),
        BowserCrushLearn(world),
        GenoBeamLearn(world),
        GenoBoostLearn(world),
        GenoWhirlLearn(world),
        GenoBlastLearn(world),
        GenoFlashLearn(world),
        ThunderboltLearn(world),
        HPRainLearn(world),
        PsychopathLearn(world),
        ShockerLearn(world),
        SnowyLearn(world),
        StarRainLearn(world),
    ]


def get_placeable_boss_fights(world):
    return [
        HammerBroBossFight(world),
        Croco1BossFight(world),
        MackBossFight(world),
        PandoriteBossFight(world),
        Belome1BossFight(world),
        BowyerBossFight(world),
        Croco2BossFight(world),
        PunchinelloBossFight(world),
        BoosterBossFight(world),
        GrateGuyBossFight(world),
        BundtBossFight(world),
        KingCalamariBossFight(world),
        HidonBossFight(world),
        JohnnyBossFight(world),
        YaridovichBossFight(world),
        MokuraBossFight(world),
        Belome2BossFight(world),
        JaggerBossFight(world),
        Jinx1BossFight(world),
        Jinx2BossFight(world),
        Jinx3BossFight(world),
        CulexBossFight(world),
        BoxBoyBossFight(world),
        MegaSmilaxBossFight(world),
        DodoBossFight(world),
        BirdettaBossFight(world),
        ValentinaBossFight(world),
        CzarDragonBossFight(world),
        AxemRangersBossFight(world),
        ChesterBossFight(world),
        MagikoopaBossFight(world),
        BoomerBossFight(world),
        ExorBossFight(world),
        CountdownBossFight(world),
        CloakerDominoBossFight(world),
        ClerkBossFight(world),
        ManagerBossFight(world),
        DirectorBossFight(world),
        GunyolkBossFight(world),
        SmithyBossFight(world),
    ]

def is_coin(item):
    return utils.isclass_or_instance(item, Coins) or utils.isclass_or_instance(item, FrogCoin) or utils.isclass_or_instance(item, MultiFrogCoin) or utils.isclass_or_instance(item, RareFrogCoin) or utils.isclass_or_instance(item, InfiniteCoinChest)