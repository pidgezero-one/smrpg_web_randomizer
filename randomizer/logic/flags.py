# Flag definitions and logic.

from django.utils.html import mark_safe
from markdown import markdown

TYPE_CHECKBOX = 1
TYPE_DROPDOWN = 2
TYPE_EXCLUSION = 3
TYPE_NUMBER = 4
TYPE_SLIDER = 5

delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum())

# ************************************** Flag classes

class FlagError(ValueError):
    pass

def safe_html_name(obj):
    return ''.join(ch for ch in obj.__class__.__name__ if ch.isalnum())

class Flag:
    """Class representing a flag with its description, and possible values/choices/options."""
    name = ''
    description = ''
    inverse_description = ''
    value = ''
    hard = False
    modes = ['linear', 'open']
    choices = []
    options = []
    max = None
    min = None
    default = None

    def has_children(self):
        return len(self.choices) > 0 or len(self.options) > 0

    def desc_length(self):
        return len(self.description)

    def htmlname(self):
        return safe_html_name(self)

    def description_as_markdown(cls):
        return mark_safe(markdown(cls.description, safe_mode='escape'))

    @classmethod
    def description_or_name_as_markdown(cls):
        if cls.description:
            return mark_safe(markdown(cls.description, safe_mode='escape'))
        else:
            return mark_safe(markdown(cls.name, safe_mode='escape'))

    @classmethod
    def inverse_description_as_markdown(cls):
        return mark_safe(markdown(cls.inverse_description, safe_mode='escape'))

    @classmethod
    def inverse_description_or_name_as_markdown(cls):
        if cls.inverse_description:
            return mark_safe(markdown(cls.inverse_description, safe_mode='escape'))
        else:
            return mark_safe(markdown("(" + cls.name + ")", safe_mode='escape'))

    @classmethod
    def available_in_mode(cls, mode):
        """

        Args:
            mode (str): Mode to check availability.

        Returns:
            bool: True if this flag is available in the given mode, False otherwise.

        """
        return mode in cls.modes






####### Shuffle Logic tab #######



# ******** Star piece shuffle



class StarsBossesOnly(Flag):
    name = 'Bosses only'
    description = ("Star pieces will be awarded randomly after defeating bosses, including the three unique mimic chests.")
    value = 0
class StarsAnywhere(Flag):
    name = 'Bosses and chests/rewards'
    description = ("Star pieces will be awarded randomly after defeating bosses (including the three unique mimic chests) as well as in chest and reward locations.")
    value = 1
class StarPieceShuffleLogic(Flag):
    type = TYPE_DROPDOWN
    name = 'Logic'
    description = ("Choose where Star Pieces can be found.")
    modes = ['open']
    choices = [
        StarsBossesOnly,
        StarsAnywhere
    ]
    default = 0

class CulexStarShuffle(Flag):
    type = TYPE_CHECKBOX
    name = "Include Culex's Lair"
    description = "If checked, Culex's Lair in Monstro Town could have a Star Piece."
    inverse_description = "(Culex's Lair in Monstro Town will not have a Star Piece.)"
    value = 1
    hard = True
    modes = ['open']
class StarInclude3DMaze(Flag):
    name = 'Include 3D Maze'
    description = 'If checked, the 3D Maze in Sunken Ship may reward a Star Piece.'
    inverse_description = "(3D Maze will not have a key item.)"
    value = 1
    hard = True
    type = TYPE_CHECKBOX
class StarInclude30(Flag):
    name = 'Include First Super Jump Reward'
    inverse_description = "If checked, the first Super Jump reward item in Monstro Town may reward a Star Piece."
    value = 1
    hard = True
    type = TYPE_CHECKBOX
class StarInclude100(Flag):
    name = 'Include Second Super Jump Reward'
    inverse_description = "If checked, the second Super Jump reward item in Monstro Town may reward a Star Piece."
    value = 1
    hard = True
    type = TYPE_CHECKBOX

class StarPieceShuffle(Flag):
    name = 'Shuffle star pieces'
    description = (
        "Assign the star pieces to random locations. Collect all the star pieces to progress to the end of the game.")
    inverse_description = "(The star pieces will stay in their original locations.)"
    value = 1
    modes = ['open']
    type = TYPE_CHECKBOX
    options = [
        StarPieceShuffleLogic,
        CulexStarShuffle,
        StarInclude3DMaze,
        StarInclude30,
        StarInclude100
    ]



# ******** Boss shuffle


class BossShuffleCulex(Flag):
    name = 'Include Culex'
    description = "If checked, Culex may appear at any boss location, and another boss will take his place in Monstro Town."
    inverse_description = "(Culex will remain in his door in Monstro Town.)"
    value = 1
    hard = True
    type = TYPE_CHECKBOX

class BossShuffleSmithy(Flag):
    name = 'Include Smithy'
    description = "If checked, Smithy may appear at any boss location, and another boss will take his place as the final Factory boss."
    inverse_description = "(Smithy will remain as the final boss.)"
    value = 1
    hard = True
    type = TYPE_CHECKBOX

class BossShuffle(Flag):
    name = 'Randomize bosses'
    description = ("The positions of bosses (including the three unique mimic chests) are shuffled. Their stats are scaled to approximately match the area they are placed in.")
    inverse_description = "(Bosses will stay in their original locations.)"
    modes = ['open']
    value = 1
    type = TYPE_CHECKBOX
    options = [
        BossShuffleCulex,
        BossShuffleSmithy
    ]


# ******** Character shuffle

class StartRandom(Flag):
    name = 'Random starter'
    value = 0
class StartMario(Flag):
    name = 'Start as Mario'
    value = 1
class StartMallow(Flag):
    name = 'Start as Mallow'
    value = 2
class StartGeno(Flag):
    name = 'Start as Geno'
    value = 3
class StartBowser(Flag):
    name = 'Start as Bowser'
    value = 4
class StartToadstool(Flag):
    name = 'Start as Toadstool'
    value = 5

class ChooseStarter(Flag):
    name = 'First character'
    description = "Choose the first character in your party. They will also be shown on the file select screen."
    value = 1
    type = TYPE_DROPDOWN
    choices = [
        StartRandom,
        StartMario,
        StartMallow,
        StartGeno,
        StartBowser,
        StartToadstool
    ]
    default = 0

class ExcludeMario(Flag):
    name = 'Exclude Mario'
    description = "If checked, Mario cannot be recruited."
    value = 1
    type = TYPE_CHECKBOX
class ExcludeMallow(Flag):
    name = 'Exclude Mallow'
    description = "If checked, Mallow cannot be recruited."
    value = 1
    type = TYPE_CHECKBOX
class ExcludeGeno(Flag):
    name = 'Exclude Geno'
    description = "If checked, Geno cannot be recruited."
    value = 1
    type = TYPE_CHECKBOX
class ExcludeBowser(Flag):
    name = 'Exclude Bowser'
    description = "If checked, Bowser cannot be recruited."
    value = 1
    type = TYPE_CHECKBOX
class ExcludeToadstool(Flag):
    name = 'Exclude Toadstool'
    description = "If checked, Toadstool cannot be recruited."
    value = 1
    type = TYPE_CHECKBOX

class CharacterJoinOrder(Flag):
    name = 'Shuffle characters'
    description = ("Shuffle the characters you retrieve from game start, Mushroom Way, Forest Maze, Moleville, and Marrymore.")
    inverse_description = "(You will start with Mario, and retrieve the rest of the characters in original order.)"
    value = 1
    type = TYPE_CHECKBOX
    options = [
        ChooseStarter,
        ExcludeMario,
        ExcludeMallow,
        ExcludeGeno,
        ExcludeBowser,
        ExcludeToadstool
    ]



# ******** Shop shuffle flags

class ShopTier(Flag):
    name = 'Shop item quality'
    description = 'Choose the maximum quality of items allowed in shops (1 being the worst, 4 being the best).'
    type = TYPE_SLIDER
    min = 1
    max = 4
    default = 3

class ShopTierX(Flag):
    name = "Empty"
    description = "All shops contain only the Goodie Bag."
    value = 0
    hard = True
class ShopShuffleVanilla(Flag):
    name = "Vanilla"
    description = ("Shops will only contain items that were available in the original game's shops.")
    value = 1
class ShopShuffleBalanced(Flag):
    name = "Biased"
    description = "Shops that are harder to access will contain better items, within the quality constraints you choose."
    value = 2
class ShopShuffleChaotic(Flag):
    name = "Chaotic"
    description = "Any shop may contain anything, within the quality constraints you choose."
    value = 3
class ShopLogic(Flag):
    name = "Distribution"
    description = "Choose how shop items should be distributed."
    type = TYPE_DROPDOWN
    choices = [
        ShopTierX,
        ShopShuffleVanilla,
        ShopShuffleBalanced,
        ShopShuffleChaotic
    ]
    default = 2

class ShopNotGuaranteed(Flag):
    name = "Items not guaranteed"
    description = "If checked, some equips and single-use items may not appear in shops at all. <b>Be warned, this may include Pick-Me-Ups.</b>"
    inverse_description = "(Every single-use item and equip, except for key items and the Wallet, will appear in at least 1 shop.)"
    value = 1
    hard = True
    type = TYPE_CHECKBOX

class ShopShuffle(Flag):
    name = 'Randomize shops'
    description = "Randomize shop contents and prices."
    inverse_description = "(Shop contents and item prices remain unchanged from the original game.)"
    value = 1
    type = TYPE_CHECKBOX
    options = [
        ShopLogic,
        ShopTier,
        ShopNotGuaranteed
    ]



# ******** Chest shuffle flags

class ChestShuffleEmpty(Flag):
    name = 'Empty'
    description = 'All chests give the "You missed!" cutscene, and event rewards give you nothing.'
    value = 0
    hard = True
class ChestShuffle1(Flag):
    name = 'Vanilla'
    description = 'Chest and event rewards are the same as the original game, but shuffled within the same area.'
    value = 1
class ChestShuffleBiased(Flag):
    name = 'Biased'
    description = "Chests and events that are harder to access will reward better items, within the quality constraints you choose."
    value = 2
class ChestShuffleChaos(Flag):
    name = 'Chaotic'
    description = "Any chest or event reward can grant anything, within the quality constraints you choose."
    value = 3

class ChestRewardLogic(Flag):
    name = "Distribution"
    description = "Choose how chest and event rewards should be distributed."
    type = TYPE_DROPDOWN
    choices = [
        ShopTierX,
        ShopShuffleVanilla,
        ShopShuffleBalanced,
        ShopShuffleChaotic
    ]
    default = 3

class ChestRewardTier(Flag):
    name = 'Item quality'
    description = 'Choose the maximum quality of inventory items granted by chests and events (1 being the worst, 4 being the best).'
    type = TYPE_SLIDER
    min = 1
    max = 4
    default = 4

class ChestExcludeCoins(Flag):
    name = 'Exclude Coins'
    description = "If checked, chests will not contain coins, except for weak items replaced in the Entity Properties tab."
    inverse_description = "(Chests may contain coins.)"
    value = 1
    type = TYPE_CHECKBOX

class ChestExcludeFrogCoins(Flag):
    name = 'Exclude Frog Coins'
    description = "If checked, chests will not contain frog coins, except for weak items replaced in the Entity Properties tab."
    inverse_description = "(Chests may contain frog coins.)"
    value = 1
    type = TYPE_CHECKBOX

class ChestExcludeFlowers(Flag):
    name = 'Exclude Flowers'
    description = "If checked, chests will not contain FP flowers."
    inverse_description = "(Chests may contain FP flowers.)"
    value = 1
    type = TYPE_CHECKBOX

class ChestExcludeMushrooms(Flag):
    name = 'Exclude Recovery Mushrooms'
    description = "If checked, chests will not contain full recovery mushrooms."
    inverse_description = "(Chests may contain full recovery mushrooms.)"
    value = 1
    type = TYPE_CHECKBOX


class ChestExcludeStars(Flag):
    name = 'No Stars Anywhere'
    description = "Chests will not contain invincibility stars."
    value = 0
    hard = True
class ChestVanillaStars(Flag):
    name = 'Vanilla Stars'
    description = "The original game's EXP stars will stay where they are."
    value = 1
class ChestRandomizeStars(Flag):
    name = 'Random Stars'
    description = "The number and locations of EXP stars are randomized."
    value = 2
class ChestRewardStars(Flag):
    name = 'Levelup Stars'
    description = "Choose what do do with levelup stars."
    value = 1
    type = TYPE_DROPDOWN
    choices = [
        ChestExcludeStars,
        ChestVanillaStars,
        ChestRandomizeStars
    ]
    default = 1

class MonstroDoNotShuffleInclude(Flag):
    name = "Do not shuffle, allow elsewhere"
    description = ('The ten items will remain in their original locations, regardless of chest/reward shuffle settings. The items may appear in other shops, chests, or event rewards.')
    value = 0
class MonstroDoNotShuffleExclude(Flag):
    name = "Do not shuffle, disallow elsewhere"
    description = ('The ten items will remain in their original locations, regardless of chest/reward shuffle settings. The items will only appear in these locations, and nowhere else.')
    value = 1
class MonstroShuffleInclude(Flag):
    name = "Shuffle within each other, allow elsewhere"
    description = ('The ten items will be shuffled within each other\'s locations. The items may appear in other shops, chests, or event rewards.')
    value = 2
class MonstroShuffleExclude(Flag):
    name = "Shuffle within each other, disallow elsewhere"
    description = ('The ten items will be shuffled within each other\'s locations. The items will only appear in these locations, and nowhere else.')
    value = 3
class MonstroDoNotGuarantee(Flag):
    name = "Do not guarantee"
    description = ('These ten chest/reward locations are considered part of the general chest/reward pool. The ten equips are not guaranteed to be in these locations.')
    value = 4
class MonstroTownShuffle(Flag):
    name = 'Side boss & key item reward equips'
    description = ('Choose how the sideboss and key item reward special equips (Super Suit, Attack Scarf, Quartz Charm,'
                   ' Jinx Belt, Ghost Medal, FroggieStick, Zoom Shoes, '
                   'Chomp, Lazy Shell Weapon, and Lazy Shell Armor) will be distributed.')
    modes = ['open']
    value = 1
    type = TYPE_DROPDOWN
    choices = [
        MonstroDoNotShuffleInclude,
        MonstroDoNotShuffleExclude,
        MonstroShuffleInclude,
        MonstroShuffleExclude,
        MonstroDoNotGuarantee
    ]
    default = 0

class ChestShuffleFlag(Flag):
    name = 'Randomize items rewarded by chests and events'
    description = 'Randomize rewards granted to you by treasure chests and NPC events. <b>Note that all invisible chests have been made visible.</b>'
    inverse_description = "(Chest and event rewards will remain unchanged from the original game.)"
    modes = ['open']
    value = 1
    type = TYPE_CHECKBOX
    options = [
        ChestRewardLogic,
        ChestRewardTier,
        ChestRewardStars,
        ChestExcludeCoins,
        ChestExcludeFrogCoins,
        ChestExcludeFlowers,
        ChestExcludeMushrooms,
        MonstroTownShuffle
    ]


# ******** Key item shuffle


class KeyItemOriginalLocations(Flag):
    name = 'Within each other'
    description = "Key item locations will be shuffled within each other. For example, the Room Key may appear where they Shed Key normally appears, but cannot appear in a random chest that normally does not contain a key item."
    value = 0
class ChestIncludeKeyItems(Flag):
    name = 'Anywhere'
    description = "Any chest or sidequest reward may contain a key item."
    value = 1
    hard = True
class KeyItemDistribution(Flag):
    name = "Logic"
    description = "Choose where key items can appear."
    type = TYPE_DROPDOWN
    modes = ['open']
    choices = [
        KeyItemOriginalLocations,
        ChestIncludeKeyItems
    ]
    default = 0

class IncludeSeedFertilizer(Flag):
    name = 'Include Seed and Fertilizer'
    description = 'If checked, the Seed and Fertilizer will be included in the key item shuffle.'
    inverse_description = "(The Seed and Fertilizer will be found in their original locations.)"
    value = 1
    modes = ['open']
    type = TYPE_CHECKBOX
class IncludeBrightCard(Flag):
    name = 'Include Bright Card'
    description = 'If checked, the Bright Card, which opens Grate Guy\'s Casino, will be included in the key item shuffle.'
    inverse_description = "(The Bright Card can be found in Booster's Tower after completing it.)"
    value = 1
    modes = ['open']
    type = TYPE_CHECKBOX
class IncludeCarboCookie(Flag):
    name = 'Include Carbo Cookie'
    description = 'If checked, the Carbo Cookie, which opens the bucket in Moleville, will be included in the key item shuffle. The mimic chest in Monstro Town will become a key item check after defeating all three of the mimic chest enemies (Pandorite, Hidon, and Box Boy).'
    inverse_description = "(The mimic chest in Monstro Town will reward you a Carbo Cookie after defeating all three of the mimic chests (Pandorite, Hidon, and Box Boy).)"
    value = 1
    modes = ['open']
    type = TYPE_CHECKBOX
class ChestKIInclude3DMaze(Flag):
    name = 'Include 3D Maze'
    description = 'If checked, the 3D Maze in Sunken Ship may contain a key item.'
    inverse_description = "(3D Maze will not have a key item.)"
    value = 1
    hard = True
    type = TYPE_CHECKBOX
class ChestKIIncludeCulex(Flag):
    name = 'Include Culex\'s Lair Prize'
    description = 'If checked, the reward for defeating the boss in Culex\'s Lair in Monstro Town may be a key item.'
    inverse_description = "(Culex's lair will not have a key item.)"
    value = 1
    hard = True
    type = TYPE_CHECKBOX
class ChestKIInclude30(Flag):
    name = 'Include First Super Jump Reward'
    inverse_description = "If checked, the first Super Jump reward item in Monstro Town may be a key item."
    value = 1
    hard = True
    type = TYPE_CHECKBOX
class ChestKIInclude100(Flag):
    name = 'Include Second Super Jump Reward'
    inverse_description = "If checked, the second Super Jump reward item in Monstro Town may be a key item."
    value = 1
    hard = True
    type = TYPE_CHECKBOX

class KeyItemShuffle(Flag):
    name = 'Randomize key items'
    description = ("The locations of key (special) items are shuffled amongst each other. For example, you may find the"
                   " Shed Key at Croco 1 instead of the Rare Frog Coin.\n\nThe items randomized this way are the "
                   "Rare Frog Coin, Cricket Pie, Bambino Bomb, Castle Key 1, Castle Key 2, "
                   "Alto Card, Tenor Card, Soprano Card, Greaper Flag, Dry Bones Flag, "
                   "Big Boo Flag, Shed Key, Elder Key, Cricket Jam, Temple Key, and Room Key.")
    inverse_description = "(The key items will stay in their original locations.)"
    value = 1
    modes = ['open']
    type = TYPE_CHECKBOX
    options = [
        IncludeSeedFertilizer,
        IncludeBrightCard,
        IncludeCarboCookie,
        KeyItemDistribution,
        ChestKIInclude3DMaze,
        ChestKIIncludeCulex,
        ChestKIInclude30,
        ChestKIInclude100
    ]





####### Progression Requirements tab #######

# ******* Win condition

class WinOnFactoryClear(Flag):
    name = "Final Factory boss defeated"
    description = "Like in the original game, the game is over when you complete the Factory."
    value = 0
class WinOnStarsCollected(Flag):
    name = "All star pieces found"
    description = "The game is over when you find all required Star Pieces."
    value = 1
class WinOnCulexClear(Flag):
    name = "Culex's Lair defeated"
    description = "The game is over when you defeat the boss in Culex's Lair in Monstro Town."
    value = 2
class WinCondition(Flag):
    name = "Win condition"
    description = "Choose your objective required to complete this randomizer."
    modes = ['open']
    type = TYPE_DROPDOWN
    choices = [
        WinOnFactoryClear,
        WinOnStarsCollected,
        WinOnCulexClear
    ]
    default = 0




# ******* Open areas

class OpenMushroomKingdomShop(Flag):
    name = "Open Mushroom Kingdom Shop"
    description = "If checked, you can turn in the Rare Frog Coin anytime.<br><br>If unchecked, you need to clear the bosses in Bandit's Way and Mushroom Kingdom before the shopkeeper will accept the Frog Coin."
    inverse_description = "(You must clear the Bandit's Way and Mushroom Kingdom bosses before you can turn in the RareFrogCoin.)"
    value = 1
    modes = ['open']
    type = TYPE_CHECKBOX

class OpenBanditsWay(Flag):
    name = "Open Bandit's Way"
    description = "If checked, Bandit's Way is open from the start of the seed.<br><br>If unchecked, Bandit's Way will open when you recruit Mallow (or when you defeat the boss holding his sprite captive, if he is excluded from the seed)."
    inverse_description = "Bandit's Way will open when you recruit Mallow (if Mallow is excluded, it will open when you defeat the boss his sprite is held captive by)."
    value = 1
    modes = ['open']
    type = TYPE_CHECKBOX

class OpenForestMaze(Flag):
    name = "Open Forest Maze"
    description = "Forest Maze is open from the start of the seed.<br><br>If unchecked, Forest Maze will open when you turn in the Cricket Pie to Frogfucius."
    inverse_description = "Forest Maze will open when you turn in the Cricket Pie to Frogfucius."
    value = 1
    modes = ['open']
    type = TYPE_CHECKBOX

class OpenBoosterTower(Flag):
    name = "Open Booster Tower"
    description = "If checked, Booster Tower is open from the start of the seed..<br><br>If unchecked, the door will open when you recruit Bowser (or when you defeat the boss holding his sprite captive, if he is excluded from the seed)."
    inverse_description = "Booster Tower will open when you recruit Bowser (if Bowser is excluded, it will open when you defeat the boss his sprite is held captive by)."
    value = 1
    modes = ['open']
    type = TYPE_CHECKBOX

class OpenSea(Flag):
    name = "Open Sea"
    description = "If checked, Sea is open from the start of the seed.<br><br>If unchecked, the door will open when you recruit Toadstool (or when you defeat the boss holding her sprite captive, if she is excluded from the seed)."
    inverse_description = "Sea will open when you recruit Toadstool (if Toadstool is excluded, it will open when you defeat the boss her sprite is held captive by)."
    value = 1
    modes = ['open']
    type = TYPE_CHECKBOX

class OpenMonstroTown(Flag):
    name = "Open Monstro Town"
    description = "If checked, Monstro Town is open from the start of the seed.<br><br>If unchecked, Monstro Town will open when you clear Belome Temple."
    inverse_description = "Monstro Town will open when you clear Belome Temple."
    value = 1
    modes = ['open']
    type = TYPE_CHECKBOX

class OpenBarrelVolcano(Flag):
    name = "Open Barrel Volcano"
    description = "If checked, Barrel Volcano is open from the start of the seed.<br><br>If unchecked, Barrel Volcano will open when you use the rear exit of Nimbus Castle."
    inverse_description = "Barrel Volcano will open when you use Castle Key 2."
    value = 1
    modes = ['open']
    type = TYPE_CHECKBOX

class ShuffleBowsersKeep(Flag):
    name = 'Shuffle Bowser\'s Keep'
    description = 'Each of the 6 Bowser\'s Keep doors will contain 3 random rooms from any of the original 6 doors.'
    inverse_description = ('(Bowser\'s Keep door contents have not changed, but their order is still subject to '
                           'in-game RNG.)')
    modes = ['open']
    value = 1
    type = TYPE_CHECKBOX

class BowsersKeepOpen(Flag):
    name = "Open Bowser's Keep"
    description = "If checked, Bowser's Keep is open from the start of the seed.<br><br>If unchecked, Bowser's Keep is opened when you collect all your required Star Pieces."
    inverse_description = ("(Bowser's Keep is opened by collecting all your required Star Pieces.)")
    value = 1
    modes = ['open']
    type = TYPE_CHECKBOX

class FactoryOpen(Flag):
    name = "Always Open"
    description = "The Factory is open from the start of the seed."
    value = 0
class FactoryFindExor(Flag):
    name = "Find Exor"
    description = "The Factory opens when you defeat Exor, wherever he ends up in the boss shuffle."
    value = 1
class FactoryClearBK(Flag):
    name = "Clear Bowser's Keep"
    description = "The Factory opens when you clear the third boss in Bowser's Keep."
    value = 2
class FactoryAllStarPieces(Flag):
    name = "All Star Pieces"
    description = "The Factory opens when you collect all required Star Pieces."
    value = 3
class FactoryAllBosses(Flag):
    name = "All Bosses"
    description = "The Factory opens when you clear all other bosses."
    value = 4
class OpenFactory(Flag):
    name = "Open Factory"
    description = "Choose the conditions under which the Factory opens. Regardless of your selected condition, you cannot fight the final boss until you have enough Star Pieces. <b>Note that if you do not have \"Open Bowser's Keep\" checked, your Factory will not be accessible until Bowser's Keep is.</b>"
    inverse_description = ("(Bowser's Keep is opened by collecting all your required Star Pieces.)")
    modes = ['open']
    choices = [
        FactoryOpen,
        FactoryFindExor,
        FactoryClearBK,
        FactoryAllStarPieces,
        FactoryAllBosses
    ]
    type = TYPE_DROPDOWN
    default = 3



# ******* Numbers

class StarPiecesRequired(Flag):
    name = 'Star pieces'
    description = "The number of star pieces required to progress to the final boss. If set to 0, any flag objectives requiring Star Piece collection will be automatically unlocked."
    type = TYPE_SLIDER
    min = 0
    max = 7
    default = 6

class StartingPartyMembers(Flag):
    name = 'Starting party members'
    description = "Your party size at the start of the game. Additional party members, if available, may be recruited at Mushroom Way, Forest Maze, Moleville Mines, or Marrymore."
    type = TYPE_SLIDER
    min = 1
    max = 5
    default = 1

class BowserDoorsRequired(Flag):
    name = "Bowser's Keep trials"
    description = "The number of doors in Bowser's Keep you must complete to progress to the three boss battles."
    type = TYPE_SLIDER
    min = 1
    max = 6
    default = 4

class SuperJumpFirstItem(Flag):
    name = "First Super Jump reward"
    description = "The number of Super Jumps you must do to receive your first prize in Monstro Town."
    type = TYPE_NUMBER
    min = 1
    max = 99
    default = 30

class SuperJumpSecondItem(Flag):
    name = "Second Super Jump reward"
    description = "The number of Super Jumps you must do to receive your second prize in Monstro Town."
    type = TYPE_NUMBER
    min = 2
    max = 100
    default = 100

class MarrymoreFirstItem(Flag):
    name = "First Marrymore reward"
    description = "The number of times you must stay at the Marrymore Suite to receive your first prize."
    type = TYPE_NUMBER
    min = 1
    max = 250
    default = 1

class MarrymoreSecondItem(Flag):
    name = "Second Marrymore reward"
    description = "The number of times you must stay at the Marrymore Suite to receive your second prize."
    type = TYPE_NUMBER
    min = 2
    max = 251
    default = 3

class MarrymoreThirdItem(Flag):
    name = "Third Marrymore reward"
    description = "The number of times you must stay at the Marrymore Suite to receive your third prize."
    type = TYPE_NUMBER
    min = 3
    max = 252
    default = 5

class MarrymoreFourthItem(Flag):
    name = "Fourth Marrymore reward"
    description = "The number of times you must stay at the Marrymore Suite to receive your fourth prize."
    type = TYPE_NUMBER
    min = 4
    max = 253
    default = 10

class MarrymoreFifthItem(Flag):
    name = "Fifth Marrymore reward"
    description = "The number of times you must stay at the Marrymore Suite to receive your fifth prize."
    type = TYPE_NUMBER
    min = 5
    max = 254
    default = 15

class MarrymoreSixthItem(Flag):
    name = "Sixth Marrymore reward"
    description = "The number of times you must stay at the Marrymore Suite to receive your sixth prize."
    type = TYPE_NUMBER
    min = 6
    max = 255
    default = 255

class KnifeGuyItem(Flag):
    name = "Knife Guy reward"
    description = "The number of <b>net wins</b> you must get to receive Knife Guy's juggling reward."
    type = TYPE_NUMBER
    min = 1
    max = 255
    default = 12

class GrateGuyItem(Flag):
    name = "Grate Guy reward"
    description = "The number of <b>cumulative wins</b> you must get to receive Grate Guy's 'Look The Other Way' award."
    type = TYPE_NUMBER
    min = 1
    max = 255
    default = 100



# ******** Warp flags

class CasinoWarp(Flag):
    name = "Enable Casino Warp"
    description = "If checked, Grate Guy in the Casino will offer to warp you to the final boss if you've collected all your star pieces. (If you decline his offer, you may continue playing \"Look The Other Way\" as normal, and he will ask you again next time you talk to him.)"
    inverse_description = "(There is no factory warp in Grate Guy's Casino.)"
    modes = ['open']
    value = 1
    type = TYPE_CHECKBOX

class MolevilleWarp(Flag):
    name = "Enable Moleville Warp"
    description = "If checked, once you collect all your Star Pieces, you can trade in the Carbo Cookie in Moleville to use the bucket to warp directly to the final boss."
    inverse_description = "(There is no factory warp in Moleville.)"
    modes = ['open']
    value = 1
    type = TYPE_CHECKBOX



# ******** Minigame challenges

class ShipPasswordShuffle(Flag):
    name = 'Randomize Ship Password'
    description = 'If checked, the Sunken Ship password will be a random combination of symbols, and there will be hints for it scattered around the world.<br><br>If unchecked, the password remains "Pearls".'
    inverse_description = '(The Sunken Ship password is Pearls.)'
    value = 1
    modes = ['open']
    type = TYPE_CHECKBOX

class TadpolePondShuffle(Flag):
    name = 'Randomize Tadpole Pond Songs'
    description = 'If checked, the Tadpole Pond songs will be changed, and there will be hints for them scattered around the world.'
    inverse_description = '(The Tadpole Pond songs remain unchanged.)'
    value = 1
    modes = ['open']
    type = TYPE_CHECKBOX

class BoosterPortraitShuffle(Flag):
    name = "Randomize Booster's Portrait Game"
    description = "If checked, the order of Booster's ancestors portraits will be randomized and shown in the first room of Booster Tower.<br><br>If unchecked, the order remains 6-5-3-1-2-4."
    inverse_description = '(The Booster Portrait game will remain as 6-5-3-1-2-4.)'
    value = 1
    type = TYPE_CHECKBOX

class BallSolitaireShuffle(Flag):
    name = 'Randomize Ball Solitaire'
    description = 'If checked, the layout for the Ball Solitaire minigame will be randomized.'
    inverse_description = '(Ball Solitaire minigame will be the same as vanilla.)'
    value = 1
    type = TYPE_CHECKBOX

class MagicButtonShuffle(Flag):
    name = 'Randomize Magic Buttons'
    description = 'If checked, the layout for the Magic Buttons minigame will be randomized.'
    inverse_description = '(Magic Buttons minigame will be the same as vanilla.)'
    value = 1
    type = TYPE_CHECKBOX

class QuizShuffle(Flag):
    name = 'Randomize Dr. Topper Quiz'
    description = 'If checked, the question pool for the Dr. Topper quiz will include new questions provided by the community.'
    inverse_description = '(Dr. Topper quiz question pool will be the same as vanilla.)'
    value = 1
    type = TYPE_CHECKBOX



# ******** Hint flags

class GeneralHints(Flag):
    name = "Text hints"
    description = "If checked, some NPCs will give you hints on the locations of items."
    value = 1
    type = TYPE_CHECKBOX
    modes = ['open']

class SignalRingHints(Flag):
    name = "Signal Ring hints"
    description = "If checked, the Signal Ring (if equipped) will sound off if a Star Piece is nearby. This would make Signal Ring considered a Level 4 item in 'Balanced' chest/shop distribution logic."
    value = 1
    type = TYPE_CHECKBOX
    modes = ['open']






####### Entity Properties flags #######



# ******** Character shuffle flags

class RemoveSuperJumpCap(Flag):
    name = 'Remove Super Jump cap'
    description = "If checked, you can do more than 100 Super Jumps."
    inverse_description = ("(Super Jumps are capped at 100.)")
    value = 1
    type = TYPE_CHECKBOX

class CharacterLearnedSpells(Flag):
    name = 'Randomize character learned spells'
    description = "If checked, the spells each character learns and what level they learn them are randomized."
    inverse_description = "(Characters retain their original spell lists.)"
    value = 1
    type = TYPE_CHECKBOX

class CharacterSpellStats(Flag):
    name = 'Randomize character spell stats'
    description = "If checked, the power and FP cost of character magic spells will be randomized."
    inverse_description = "(Base power and FP cost of party spells are unchanged from the original game.)"
    value = 1
    type = TYPE_CHECKBOX

class CharacterStats(Flag):
    name = 'Randomize character stats'
    description = "If checked, the stats for each character will be randomized."
    inverse_description = ("(The characters will retain their original attack, defense, magic attack, magic defense, "
                           "and speed stats.)")
    value = 1
    type = TYPE_CHECKBOX

class EquipmentCharacters(Flag):
    name = "Randomize characters' equipment rosters"
    description = "If checked, each equip's list of characters that can wear it will be randomized."
    inverse_description = ("(Each equip's list of characters that can wear it will remain unchanged from the original "
                           "game.)")
    value = 1
    type = TYPE_CHECKBOX

class VanillaEquipment(Flag):
    name = 'Vanilla'
    description = "Equipment remains unchanged from the original game."
    value = 0
class FrenchVanillaEquipment(Flag):
    name = 'Vanilla with some static buffs'
    description = "Equipment remains mostly unchanged from the original game, but the following equips receive buffs:<ul style='text-align: left;'>" \
                  "<li>Basic equips resist Mushroom</li>" \
                  "<li>Thick equips boost defense</li>" \
                  "<li>Mega equips boost magic defense</li>" \
                  "<li>Happy equips resist KO</li>" \
                  "<li>Sailor items resist ice</li>" \
                  "<li>CourageShell resists fear</li>" \
                  "<li>Fuzzy equips resist lightning</li>" \
                  "<li>Fire equips resist fire</li>" \
                  "<li>Hero Shirt resists scarecrow</li>" \
                  "<li>Prince Pants resist mute</li>" \
                  "<li>Royal Dress resists sleep</li>" \
                  "<li>Heal Shell resists poison</li>" \
                  "<li>Star Cape resists berserk</li>" \
                  "<li>The FroggieStick, Cymbals, Ribbit Stick, Sonic Cymbal, War Fan, and Parasol increase magic attack instead of attack.</li></ul>"
    value = 1
class TotallyRandomEquipment(Flag):
    name = 'Totally random'
    description = "You may choose which features of equips you want to be randomized."
    value = 2
class EquipmentProperties(Flag):
    name = 'Equipment properties'
    description = "Choose what equipment does. Equipment descriptions in-game have been replaced with a legend stating its stats and buffs. You can read more about understanding the symbols in the player's guide on this site."
    type = TYPE_DROPDOWN
    choices = [
        VanillaEquipment,
        FrenchVanillaEquipment,
        TotallyRandomEquipment
    ]
    default = 0

class EquipmentBuffs(Flag):
    name = 'Randomize equipment buffs'
    description = ("If checked, special buffs granted by equipment will be randomized (attack/defense boost, "
                   "elemental/status immunities).  See Resources page for an explanation of these.")
    inverse_description = ("(Immunities and boost multipliers granted by equipment remain unchanged from the original "
                           "game.)")
    value = 1
    type = TYPE_CHECKBOX

class EquipmentStats(Flag):
    name = 'Randomize equipment stats'
    description = "If checked, attack, defense, magic attack, magic defense, and speed granted by equipment will be randomized"
    inverse_description = ("(Attack, defense, magic attack, magic defense, and speed granted by equipment remain "
                           "unchanged from the original game.)")
    value = 1
    type = TYPE_CHECKBOX

class EquipmentNoSafetyChecks(Flag):
    name = 'No equipment buff safety checks'
    description = ("Normally certain namesake items retain their protections: Fearless Pin, Antidote Pin, "
                   "Trueform Pin, and Wakeup Pin.  In addition, at least four equipment will have instant KO "
                   "protection. If checked, this flag <b>removes</b> those checks.")
    inverse_description = ("(Namesake properties such as Fearless Pin, Antidote Pin, Trueform Pin, and "
                           "Wakeup Pin remain intact, and at least four pieces of equipment will have instant "
                           "KO protection.)")
    value = 1
    hard = True
    type = TYPE_CHECKBOX



# ******** Enemy shuffle flags

class EnemyStats(Flag):
    name = 'Randomize enemy stats'
    description = "If checked, enemy stats and immunities/weaknesses will be randomized."
    inverse_description = ("(The enemies will retain their original attack, defense, m.attack, m.defense, speed, "
                           "weaknesses, and immunities.)")
    value = 1
    type = TYPE_CHECKBOX

class EnemyDrops(Flag):
    name = 'Randomize enemy drops'
    description = "If checked, the EXP and items received from enemies will be randomized."
    inverse_description = "(Battle prize drops are unchanged from the original game.)"
    value = 1
    type = TYPE_CHECKBOX

class EnemyFormations(Flag):
    name = 'Randomize enemy formations'
    description = "If checked, normal enemy battle formations will be randomized.  Boss formations are not affected."
    inverse_description = "(Random battle formations remain the same as in the original game.)"
    value = 1
    type = TYPE_CHECKBOX

class EnemyAttacks(Flag):
    name = 'Randomize enemy attacks'
    description = "If checked, enemy spells and attacks will have their power and potential status effects randomized."
    inverse_description = ("(Base power and status casts of enemy spells and attacks are unchanged from the original "
                           "game.)")
    value = 1
    type = TYPE_CHECKBOX

class EnemySpells(Flag):
    name = 'Randomize enemy spells'
    description = "If checked, enemies can cast random spells. I.E. Mack could cast Blast instead of Flame."
    inverse_description = ("(Enemies cast the normal spells they're expected to.)")
    value = 1
    type = TYPE_CHECKBOX
    hard = True
    modes = ['open']

class BossShuffleKeepStats(Flag):
    name = "Disable area-based stat scaling for bosses"
    description = "If checked, boss stats will <b>not</b> be scaled to match the battle it's replacing. This means you may end up with a fully-powered endgame boss in an early area."
    inverse_description = "(Turning this flag off affirms that boss stats will indeed be scaled.)"
    value = 1
    type = TYPE_CHECKBOX
    hard = True

class EnemyNoSafetyChecks(Flag):
    name = 'No enemy stat safety checks'
    description = "If checked, removes the safety checks on enemy attack shuffle that prevent abnormally large effects."
    inverse_description = "(Enemy stat shuffling should not skew abnormally high.)"
    value = 1
    type = TYPE_CHECKBOX
    hard = True

class NoGenoWhirlExor(Flag):
    name = 'No Geno Whirl on Exor'
    description = 'If checked, Exor will not be susceptible to Geno Whirl when the eyes are disabled.'
    inverse_description = ('(You may used a Timed Hit Geno Whirl to instantly KO Exor when its eye protection is '
                           'removed.)')
    value = 1
    type = TYPE_CHECKBOX
    hard = True

class FixMagikoopa(Flag):
    name = "Fix Magikoopa"
    description = 'If checked, Magikoopa will not be permanently disabled after King Bomb uses Big Bang.'
    inverse_description = '(Magikoopa will remain disabled for the remainder of the fight if King Bomb uses Big Bang.)'
    value = 1
    type = TYPE_CHECKBOX

class NoMackSkip(Flag):
    name = "No Mack Skip"
    description = 'If checked, you will not be able to skip the boss in Mushroom Kingdom.'
    inverse_description = '(You may attempt to skip the boss in Mushroom Kingdom.)'
    value = 1
    type = TYPE_CHECKBOX

class NoOHKO(Flag):
    name = "No instant KOs on boss allies"
    description = ('If checked, you will not be able to use Geno Whirl or Pure Water to OHKO any allies to a boss (Mallow Clone, '
                   'Mad Mallet, Fautso, etc).')
    inverse_description = ('(Some boss allies may be susceptible to Geno Whirl, and Belome 2\'s clones will still be '
                           'susceptible to Pure Water.)')
    value = 1
    type = TYPE_CHECKBOX



# ******** EXP

class VanillaEXP(Flag):
    name = "Vanilla"
    description = 'XP gained from battles is unchanged'
    value = 0
class ExperienceBoost2x(Flag):
    name = 'Double'
    description = 'XP gained from battles is doubled'
    value = 1
class ExperienceBoost3x(Flag):
    name = 'Triple'
    description = 'XP gained from battles is tripled'
    value = 2
class BattleEXP(Flag):
    name = "Battle EXP"
    description = 'You can upscale earned experience points for faster levelling.'
    type = TYPE_DROPDOWN
    choices = [
        VanillaEXP,
        ExperienceBoost2x,
        ExperienceBoost3x
    ]
    default = 0

class ExperienceNoRegular(Flag):
    name = 'No XP from regular encounters'
    description = 'If checked, bosses still award XP based on your selection from the Battle EXP flag, but regular encounters award none.'
    inverse_description = "(You will receive EXP from non-boss fights.)"
    value = 1
    type = TYPE_CHECKBOX
    hard = True

class StarExp0(Flag):
    name = "Vanilla"
    description = "The per-hit value of EXP stars is not hindered by your in-game progress."
    value = 0
class StarExp1(Flag):
    name = 'Based on star pieces obtained (easy)'
    description = ("<ul style='text-align: left;'><li>0 stars - 2 exp</li>"
                   "<li>1 star - 4 exp</li>"
                   "<li>2 stars - 5 exp</li>"
                   "<li>3 stars - 6 exp</li>"
                   "<li>4 stars - 8 exp</li>"
                   "<li>5 stars - 9 exp</li>"
                   "<li>6/7 stars - 11 exp</li></ul>")
    value = 1
class StarExp2(Flag):
    name = 'Based on star pieces obtained (hard)'
    description = ("<ul style='text-align: left;'><li>0 stars - 1 exp</li>"
                   "<li>1 star - 2 exp</li>"
                   "<li>2 stars - 3 exp</li>"
                   "<li>3 stars - 5 exp</li>"
                   "<li>4 stars - 6 exp</li>"
                   "<li>5 stars - 7 exp</li>"
                   "<li>6/7 stars - 11 exp</li></ul>")
    hard = True
    value = 2
class StarExp3(Flag):
    name = 'Based on bosses defeated'
    description = "Every second defeated boss increases the EXP value of a star by 1 point per hit, starting at 1."
    value = 3
class StarEXP(Flag):
    name = 'Levelup Star EXP'
    description = 'Levelup star EXP grants can be based on certain challenge conditions.'
    modes = ['open']
    type = TYPE_DROPDOWN
    choices = [
        StarExp0,
        StarExp1,
        StarExp2,
        StarExp3
    ]
    default = 0



# ******** Shop properties

class FreeShops(Flag):
    name = "'Free' Shops"
    description = "If checked, all shop items will cost 1 coin. You will start with 9999 coins and 99 frog coins."
    inverse_description = "(Shops are not free, and you start with 0 coins.)"
    value = 1
    type = TYPE_CHECKBOX



# ******** Consumable properties

class PoisonMushroom(Flag):
    name = 'Change Fake Mushroom\'s Status'
    description = ('If checked, the status effect inflicted on a party member with the Fake Mushroom (the item named "Mushroom" whose description states "Recoers 30 HP, but..." and normally turns the target into a Mushroom) will be random. It will only give '
                   'one status effect per seed, which has a 1/8 chance of being Red Essence invincibility.')
    inverse_description = '(The Fake Mushroom will always turn you into a mushroom.)'
    modes = ['open']
    value = 1
    type = TYPE_CHECKBOX



# ******** Money chest properties

class ReplaceItems(Flag):
    name = 'Replace worst chest items with coins'
    description = 'If checked, the lowest ranked items will be replaced with coins in chests.'
    inverse_description = '(You may find low-ranked items in chests.)'
    modes = ['open']
    value = 1
    type = TYPE_CHECKBOX






####### Aesthetics #######



# ******** Party palettes

class MarioPalette(Flag):
    name = "Mario palette"
    type = TYPE_DROPDOWN
    choices = [

    ]

class MallowPalette(Flag):
    name = "Mallow palette"
    type = TYPE_DROPDOWN
    choices = [

    ]

class GenoPalette(Flag):
    name = "Geno palette"
    type = TYPE_DROPDOWN
    choices = [

    ]

class BowserPalette(Flag):
    name = "Bowser palette"
    type = TYPE_DROPDOWN
    choices = [

    ]

class ToadstoolPalette(Flag):
    name = "Toadstool palette"
    type = TYPE_DROPDOWN
    choices = [

    ]



# ******** Enemy palettes

class EnemyPalettes(Flag):
    name = "Randomize enemy palettes"
    type = TYPE_CHECKBOX
    value = 1



# ******** Music

class BossShuffleMusic(Flag):
    name = 'Randomize boss music'
    description = 'If checked, battle music will be randomized for each boss fight.'
    inverse_description = "(Battle music for each location will remain unchanged from the original game.)"
    value = 1
    type = TYPE_CHECKBOX






# ************************************** Category classes

class FlagCategory:
    name = ''
    flags = []

    def htmlname(self):
        return safe_html_name(self)


class ShuffleLogicStarPieceLocations(FlagCategory):
    name = "Star locations"
    flags = [
        StarPieceShuffle
    ]

class ShuffleLogicBossLocations(FlagCategory):
    name = "Boss locations"
    flags = [
        BossShuffle
    ]

class ShuffleLogicCharacters(FlagCategory):
    name = "Playable characters"
    flags = [
        CharacterJoinOrder
    ]

class ShuffleLogicShops(FlagCategory):
    name = "Shops"
    flags = [
        ShopShuffle
    ]

class ShuffleLogicChestsRewards(FlagCategory):
    name = "Chests and rewards"
    flags = [
        ChestShuffleFlag
    ]

class ShuffleLogicKeyItems(FlagCategory):
    name = "Key items"
    flags = [
        KeyItemShuffle
    ]

class ProgressionRequirementsGameplay(Flag):
    name = "Objectives"
    flags = [
        WinCondition,
        StarPiecesRequired,
        StartingPartyMembers,
        BowserDoorsRequired
    ]

class ProgressionRequirementsOpenAreas(FlagCategory):
    name = "Open areas and shortcuts"
    flags = [
        OpenMushroomKingdomShop,
        OpenBanditsWay,
        OpenForestMaze,
        OpenBoosterTower,
        OpenSea,
        OpenMonstroTown,
        OpenBarrelVolcano,
        BowsersKeepOpen,
        ShuffleBowsersKeep,
        OpenFactory,
        CasinoWarp,
        MolevilleWarp
    ]


class ProgressionRequirementsItemValues(FlagCategory):
    name = "Item numbers"
    flags = [
        SuperJumpFirstItem,
        SuperJumpSecondItem,
        MarrymoreFirstItem,
        MarrymoreSecondItem,
        MarrymoreThirdItem,
        MarrymoreFourthItem,
        MarrymoreFifthItem,
        MarrymoreSixthItem,
        KnifeGuyItem,
        GrateGuyItem
    ]


class ProgressionRequirementsMinigames(FlagCategory):
    name = "Minigames"
    flags = [
        ShipPasswordShuffle,
        TadpolePondShuffle,
        BoosterPortraitShuffle,
        QuizShuffle,
        MagicButtonShuffle,
        BallSolitaireShuffle
    ]

class ProgressionRequirementsHints(FlagCategory):
    name = "Hints"
    flags = [
        GeneralHints,
        SignalRingHints
    ]

class EntityPropertiesParty(FlagCategory):
    name = "Party properties"
    flags = [
        CharacterLearnedSpells,
        CharacterSpellStats,
        RemoveSuperJumpCap,
        CharacterStats,
        EquipmentCharacters,
        EquipmentProperties,
        EquipmentStats,
        EquipmentBuffs,
        EquipmentNoSafetyChecks
    ]

class EntityPropertiesEnemies(FlagCategory):
    name = "Enemy properties"
    flags = [
        NoMackSkip,
        FixMagikoopa,
        NoGenoWhirlExor,
        NoOHKO,
        EnemyStats,
        EnemyAttacks,
        EnemySpells,
        EnemyDrops,
        EnemyFormations,
        BossShuffleKeepStats,
        EnemyNoSafetyChecks,
    ]

class EntityPropertiesEXP(FlagCategory):
    name = "Experience points"
    flags = [
        StarEXP,
        BattleEXP,
        ExperienceNoRegular
    ]

class EntityPropertiesShops(FlagCategory):
    name = "Shop properties"
    flags = [
        FreeShops
    ]

class EntityPropertiesFakeMushroom(FlagCategory):
    name = "Consumables"
    flags = [
        PoisonMushroom
    ]

class EntityPropertiesMoneyChests(FlagCategory):
    name = "Money chests"
    flags = [
        ReplaceItems
    ]

class AestheticsPartyPalette(FlagCategory):
    name = "Party palettes"
    flags = [
        MarioPalette,
        MallowPalette,
        GenoPalette,
        BowserPalette,
        ToadstoolPalette
    ]

class AestheticsEnemyPalette(FlagCategory):
    name = "Enemy palettes"
    flags = [
        EnemyPalettes
    ]

class AestheticsBossMusic(FlagCategory):
    name = "Boss music"
    flags = [
        BossShuffleMusic
    ]

# ************************************** Tab classes

class Tab:
    name = ''
    categories = []

    def htmlname(self):
        return safe_html_name(self)


class ShuffleLogicTab(Tab):
    name = 'Shuffle logic'
    categories = [
        ShuffleLogicChestsRewards,
        ShuffleLogicKeyItems,
        ShuffleLogicStarPieceLocations,
        ShuffleLogicBossLocations,
        ShuffleLogicCharacters,
        ShuffleLogicShops
    ]

class ProgressionRequirementsTab(Tab):
    name = 'Progression requirements'
    categories = [
        ProgressionRequirementsGameplay,
        ProgressionRequirementsOpenAreas,
        ProgressionRequirementsItemValues,
        ProgressionRequirementsMinigames,
        ProgressionRequirementsHints
    ]

class EntityPropertiesTab(Tab):
    name = 'Entity properties'
    categories = [
        EntityPropertiesParty,
        EntityPropertiesEnemies,
        EntityPropertiesEXP,
        EntityPropertiesShops,
        EntityPropertiesFakeMushroom,
        EntityPropertiesMoneyChests
    ]

class AestheticsTab(Tab):
    name = 'Aesthetics'
    categories = [
        #AestheticsPartyPalette,
        #AestheticsEnemyPalette,
        AestheticsBossMusic
    ]


# ************************************** Preset classes

class Preset:
    name = ''
    description = ''
    flags = ''


class CasualPreset(Preset):
    name = 'Casual'
    description = 'Basic flags for a casual playthrough of the game.'
    flags = 'K R Csj Edf B Tc4yg M1 Sc4 Qa X2'


class IntermediatePreset(Preset):
    name = 'Intermediate'
    description = 'A mild increase in difficulty compared to casual.'
    flags = 'Ks R7 Cspjl Edf B Tc3yg M1 Sb4 Qsa X2'


class AdvancedPreset(Preset):
    name = 'Advanced'
    description = 'More difficult options for advanced players, requiring you to manage your equips more.'
    flags = 'Ks R7k Cspjl Edfsa Bc Tb2kd M2 Sb2 Qsba X2 P1 Gm -fakeout'


class ExpertPreset(Preset):
    name = 'Expert'
    description = 'A highly chaotic shuffle with everything difficult enabled and helpful glitches disabled.'
    flags = 'Ks R7kc Cspjl Edfsa! Bmcs Tb2kduhi M2x Sv1 Qsba! X2x P2 Gsmke -fakeout'


class QuickPreset(Preset):
    name = 'Quick'
    description = 'A faster playthrough with free shops and XP acceleration for faster progression'
    flags = 'K Rk Csjl Tc4yzm M2 Sc4 -freeshops Ed Bm Qsba X3 D1'


# ************************************** Default lists for the site.

# List of categories for the site.

TABS = [
    ShuffleLogicTab,
    ProgressionRequirementsTab,
    EntityPropertiesTab,
    AestheticsTab
]

# List of presets.
PRESETS = (
    CasualPreset,
    IntermediatePreset,
    AdvancedPreset,
    ExpertPreset,
    QuickPreset,
)
