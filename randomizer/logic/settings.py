# Flag definitions and logic.

from django.utils.html import mark_safe
from markdown import markdown


# ************************************** Flag classes

class FlagError(ValueError):
    pass


class Flag:
    """Class representing a flag with its description, and possible values/choices/options."""
    name = ''
    description = ''
    inverse_description = ''
    hard = False
    modes = ['linear', 'open']
    default = None

    @classmethod
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

class CategorizationFlag(Flag):
    """For things like selecting which locations can and cannot contain progression"""

    options = []

class SelectOneFlag(Flag):
    """For things like choosing an area gating option can and cannot contain progression"""

    choices = []

class BooleanFlag(Flag):
    """For settings which can only be on or off"""

    pass

class NumberThresholdFlag(Flag):
    """For settings which require a number from a range"""
    
    min = 0
    max = 0

# ******** Star pieces

class TotalStarPieces(NumberThresholdFlag):
    name = 'Total star pieces'
    description = "The total number of star pieces (0-7) that can appear in the seed."
    default = 6
    min = 0
    max = 7
    modes = ['open']

class StarPiecesRequired(NumberThresholdFlag):
    name = 'Star pieces required to beat the game'
    description = "The total number of star pieces (0-7) that are required to access the final boss. Cannot be higher than Total Star Pieces."
    default = 6
    min = 0
    max = 7
    modes = ['open']

class StarPieceAvailability(BooleanFlag):
    name = 'Star Pieces can appear in the general item pool'
    description = "If enabled, some Star Pieces may be shuffled in with items instead of being only granted by boss fights."
    modes = ['open']
    default = False

class RequireBossFights(BooleanFlag):
    name = 'Disable all boss fight skips'
    description = '''If set, the following actions will NOT grant you a Star Piece, and you must fight the associated boss in order to retrieve their Star Piece (if they have one):
    
    * Performing Mack Skip (the Chancellor will not advance the script)
    * Completing the Booster Tower curtain minigame (a copy of the boss will appear in the room corner)
    * Completing the Nimbus Castle statue minigame, or eliminating the boss in the final hallway with an EXP star (a copy of the boss will appear in the nearby save room)
    * Failing a Slot Machine chest and completing the forced mimic encounter (the mimic encounter is available on its own in a separate chest)
    
    If unset, the above actions will grant you a star piece if one is assigned to the associated boss. Each boss' star piece can only be obtained once.'''
    modes = ['open']
    default = False

# ******** Gating & Warps

class BanditsWayGating(enum.Enum):
    """Enumeration for Bandit's Way gating flag option"""
    RecruitMario = enum.value("Recruit Mario")
    RecruitMallow = enum.value("Recruit Mallow")
    RecruitGeno = enum.value("Recruit Geno")
    RecruitBowser = enum.value("Recruit Bowser")
    RecruitToadstool = enum.value("Recruit Toadstool")
    FinishMushroomWay = enum.value("Finish Mushroom Way")
    AlwaysOpen = enum.auto("Always open")

class BanditsWayGate(SelectOneFlag):
    name = '''Bandit's Way access'''
    description = '''Recruit Mario: Bandit's Way will become available on the world map when you recruit Mario.
    
    Recruit Mallow: Bandit's Way will become available on the world map when you recruit Mallow.
    
    Recruit Geno: Bandit's Way will become available on the world map when you recruit Geno.
    
    Recruit Bowser: Bandit's Way will become available on the world map when you recruit Bowser.
    
    Recruit Toadstool: Bandit's Way will become available on the world map when you recruit Toadstool.
    
    Finish Mushroom Way: Bandit's Way will become available on the world map when you defeat the boss of Mushroom Way.
    
    Always Open: Bandit's Way will be available on the world map from the start of the game.'''
    modes = ['open']
    choices = [o.value for o in BanditsWayGating]
    default = BanditsWayGating.RecruitMallow

class ForestMazeGating(enum.Enum):
    """Enumeration for Forest Maze gating flag option"""
    FindMario = enum.value("Find Mario")
    FindMallow = enum.value("Find Mallow")
    FindGeno = enum.value("Find Geno")
    FindBowser = enum.value("Find Bowser")
    FindToadstool = enum.value("Find Toadstool")
    FinishMushroomWay = enum.value("Exchange Cricket Pie")
    AlwaysOpen = enum.auto("Always open")

class ForestMazeGate(SelectOneFlag):
    name = '''ForestMaze access'''
    description = '''Find Mario: Forest Maze will become available on the world map when you determine where Mario is (whether or not you recruit him).
    
    Find Mallow: Forest Maze will become available on the world map when you determine where Mallow is (whether or not you recruit him).
    
    Find Geno: Forest Maze will become available on the world map when you determine where Geno is (whether or not you recruit him).
    
    Find Bowser: Forest Maze will become available on the world map when you determine where Bowser is (whether or not you recruit him).
    
    Find Toadstool: Forest Maze will become available on the world map when you determine where Toadstool is (whether or not you recruit her).
    
    Exchange Cricket Pie: Forest Maze will become available on the world map when you turn in the Cricket Pie to Frogfucius.
    
    Always Open: Forest Maze will be available on the world map from the start of the game.'''
    modes = ['open']
    choices = [o.value for o in ForestMazeGating]
    default = ForestMazeGating.FindGeno

class BoosterTowerGating(enum.Enum):
    """Enumeration for Booster Tower gating flag option"""
    RecruitMario = enum.value("Recruit Mario")
    RecruitMallow = enum.value("Recruit Mallow")
    RecruitGeno = enum.value("Recruit Geno")
    RecruitBowser = enum.value("Recruit Bowser")
    RecruitToadstool = enum.value("Recruit Toadstool")
    FinishMoleville = enum.value("Finish Moleville")
    AlwaysOpen = enum.auto("Always open")

class BoosterTowerGate(SelectOneFlag):
    name = '''Booster Tower access'''
    description = '''Recruit Mario: Booster Tower will become available on the world map when you recruit Mario.
    
    Recruit Mallow: Booster Tower will become available on the world map when you recruit Mallow.
    
    Recruit Geno: Booster Tower will become available on the world map when you recruit Geno.
    
    Recruit Bowser: Booster Tower will become available on the world map when you recruit Bowser.
    
    Recruit Toadstool: Booster Tower will become available on the world map when you recruit Toadstool.
    
    Finish Moleville: Booster Tower will become available on the world map when you defeat the final boss of Moleville.
    
    Always Open: Booster Tower will be available on the world map from the start of the game.'''
    modes = ['open']
    choices = [o.value for o in BoosterTowerGating]
    default = BoosterTowerGating.RecruitBowser

class MarrymoreGating(enum.Enum):
    """Enumeration for Marrymore gating flag option"""
    FinishBoosterHill = enum.value("Finish Booster Hill")
    FinishBoosterTower = enum.value("Finish Booster Tower")
    AlwaysOpen = enum.auto("Always open")

class MarrymoreGate(SelectOneFlag):
    name = '''Marrymore back door access'''
    description = '''Finish Booster Hill: The chapel back door will become available on the world map when you complete Booster Hill one time.
    
    Finish Booster Tower: The chapel back door will become available on the world map when you defeat the balcony boss of Booster Tower.
    
    Always Open: The chapel back door will be open from the start of the game.'''
    modes = ['open']
    choices = [o.value for o in MarrymoreGating]
    default = MarrymoreGating.FinishBoosterHill

class SeaGating(enum.Enum):
    """Enumeration for Sea & Sunken Ship gating flag option"""
    RecruitMario = enum.value("Recruit Mario")
    RecruitMallow = enum.value("Recruit Mallow")
    RecruitGeno = enum.value("Recruit Geno")
    RecruitBowser = enum.value("Recruit Bowser")
    RecruitToadstool = enum.value("Recruit Toadstool")
    Find1Star = enum.value("Collect 1 Star Piece")
    Find2Star = enum.value("Collect 2 Star Pieces")
    Find3Star = enum.value("Collect 3 Star Pieces")
    Find4Star = enum.value("Collect 4 Star Pieces")
    Find5Star = enum.value("Collect 5 Star Pieces")
    Find6Star = enum.value("Collect 6 Star Pieces")
    AlwaysOpen = enum.auto("Always open")

class SeaGate(SelectOneFlag):
    name = '''Sea & Sunken Ship access'''
    description = '''Recruit Mario: The Sea will become available on the world map when you recruit Mario.
    
    Recruit Mallow: The Sea will become available on the world map when you recruit Mallow.
    
    Recruit Geno: The Sea will become available on the world map when you recruit Geno.
    
    Recruit Bowser: The Sea will become available on the world map when you recruit Bowser.
    
    Recruit Toadstool: The Sea will become available on the world map when you recruit Toadstool.
    
    Collect 1 Star Piece: The Sea will become available on the world map when you collect 1 Star Piece.
    
    Collect 2 Star Pieces: The Sea will become available on the world map when you collect 2 Star Pieces.
    
    Collect 3 Star Pieces: The Sea will become available on the world map when you collect 3 Star Pieces.
    
    Collect 4 Star Pieces: The Sea will become available on the world map when you collect 4 Star Piece.
    
    Collect 5 Star Pieces: The Sea will become available on the world map when you collect 5 Star Piece.
    
    Collect 6 Star Pieces: The Sea will become available on the world map when you collect 6 Star Pieces.
    
    Always Open: The Sea & Sunken Ship will be available on the world map from the start of the game.'''
    modes = ['open']
    choices = [o.value for o in SeaGating]
    default = SeaGating.Find4Star

class YaridovichGating(enum.Enum):
    """Enumeration for Seaside boss gating flag option"""
    FinishSunkenShip = enum.value("Finish Sunken Ship")
    AlwaysOpen = enum.auto("Always available")

class YaridovichGate(SelectOneFlag):
    name = '''Seaside boss fight access'''
    description = '''Finish Sunken Ship: The Seaside boss fight will become available after you defeat the final boss of Sunken Ship.
    
    Always Open: The Seaside boss will be available from the start of the game.'''
    modes = ['open']
    choices = [o.value for o in YaridovichGating]
    default = YaridovichGating.FinishSunkenShip

class MonstroTownGating(enum.Enum):
    """Enumeration for Monstro Town gating flag option"""
    FinishLandsEnd = enum.value("Finish Land's End")
    AlwaysOpen = enum.auto("Always open")

class MonstroTownGate(SelectOneFlag):
    name = '''Monstro Town access'''
    description = '''Finish Land's End: Monstro Town will become available on the World Map once you take the pipe behind the boss of Belome Temple.
    
    Always Open: Monstro Town will be available on the World Map from the start of the game.'''
    modes = ['open']
    choices = [o.value for o in MonstroTownGating]
    default = MonstroTownGating.FinishLandsEnd

class BarrelVolcanoGating(enum.Enum):
    """Enumeration for Barrel Volcano gating flag option"""
    FinishNimbusLand = enum.value("Finish Nimbus Land")
    AlwaysOpen = enum.auto("Always open")

class BarrelVolcanoGate(SelectOneFlag):
    name = '''Barrel Volcano access'''
    description = '''Finish Nimbus Land: Barrel Volcano will become available on the World Map once you defeat the final boss of Nimbus Castle.
    
    Always Open: Barrel Volcano will be available on the World Map from the start of the game.'''
    modes = ['open']
    choices = [o.value for o in BarrelVolcanoGating]
    default = BarrelVolcanoGating.FinishNimbusLand

class BowsersKeepGating(enum.Enum):
    """Enumeration for Bowser's Keep gating flag option"""
    Find1Star = enum.value("Collect 1 Star Piece")
    Find2Star = enum.value("Collect 2 Star Pieces")
    Find3Star = enum.value("Collect 3 Star Pieces")
    Find4Star = enum.value("Collect 4 Star Pieces")
    Find5Star = enum.value("Collect 5 Star Pieces")
    Find6Star = enum.value("Collect 6 Star Pieces")
    FinishBarrelVolcano = enum.value("Finish Barrel Volcano")
    AlwaysOpen = enum.auto("Always open")

class BowsersKeepGate(SelectOneFlag):
    name = '''Bowser's Keep access'''
    description = '''Collect 1 Star Piece: Bowser's Keep will become available on the world map when you collect 1 Star Piece.
    
    Collect 2 Star Pieces: Bowser's Keep will become available on the world map when you collect 2 Star Pieces.
    
    Collect 3 Star Pieces: Bowser's Keep will become available on the world map when you collect 3 Star Pieces.
    
    Collect 4 Star Pieces: Bowser's Keep will become available on the world map when you collect 4 Star Piece.
    
    Collect 5 Star Pieces: Bowser's Keep will become available on the world map when you collect 5 Star Piece.
    
    Collect 6 Star Pieces: Bowser's Keep will become available on the world map when you collect 6 Star Pieces.
    
    Finish Barrel Volcano: Bowser's Keep will become available on the World Map once you defeat the final boss of Barrel Volcano.
    
    Always Open: Bowser's Keep will be available on the world map from the start of the game.'''
    modes = ['open']
    choices = [o.value for o in BowsersKeepGating]
    default = BowsersKeepGating.Find6Star

class FactoryGating(enum.Enum):
    """Enumeration for Factory gating flag option"""
    AlwaysOpen = enum.auto("Open when Bowser's Keep is opened")
    FinishBowsersKeep = enum.value("Finish Bowser's Keep")
    Find1Star = enum.value("Collect 1 Star Piece")
    Find2Star = enum.value("Collect 2 Star Pieces")
    Find3Star = enum.value("Collect 3 Star Pieces")
    Find4Star = enum.value("Collect 4 Star Pieces")
    Find5Star = enum.value("Collect 5 Star Pieces")
    Find6Star = enum.value("Collect 6 Star Pieces")

class FactoryGate(SelectOneFlag):
    name = '''Bowser's Keep access'''
    description = '''If dependent on Star Pieces, cannot be higher than 'Star pieces required to beat the game'.
    
    Open when Bowser's Keep is opened: When Bowser's Keep becomes available on the world map, Factory will also be immediately available on the world map.
    
    Collect 1 Star Piece: Factory will become available on the world map when you collect 1 Star Piece and Bowser's Keep has been opened.
    
    Collect 2 Star Pieces: Factory will become available on the world map when you collect 2 Star Pieces and Bowser's Keep has been opened.
    
    Collect 3 Star Pieces: Factory will become available on the world map when you collect 3 Star Pieces and Bowser's Keep has been opened.
    
    Collect 4 Star Pieces: Factory will become available on the world map when you collect 4 Star Pieces and Bowser's Keep has been opened.
    
    Collect 5 Star Pieces: Factory will become available on the world map when you collect 5 Star Pieces and Bowser's Keep has been opened.
    
    Collect 6 Star Pieces: Factory will become available on the world map when you collect 6 Star Pieces and Bowser's Keep has been opened.
    
    Finish Bowser's Keep: Factory will become available on the world map when you complete Bowser's Keep for the first time.'''
    modes = ['open']
    choices = [o.value for o in FactoryGating]
    default = FactoryGating.FinishBowsersKeep

class CasinoWarp(BooleanFlag):
    name = 'Casino Warp'
    description = "If enabled, a trampoline warping directly to the final boss will become available in Grate Guy's Casino once you have collected the number of star pieces specified in 'Star pieces required to beat the game'. The Bright Card becomes a key item, and Knife Guy's juggling reward becomes a key item check."
    modes = ['open']
    default = False

class BucketWarp(BooleanFlag):
    name = 'Bucket Warp'
    description = "If enabled, trading a Carbo Cookie to the bucket girl in Moleville will reveal a warp to the final boss once you have collected the number of star pieces specified in 'Star pieces required to beat the game'."
    modes = ['open']
    default = False

class FastTravel(BooleanFlag):
    name = 'Fast travel'
    description = '''If enabled, the following changes will be applied to the game:
    
    1) Traveling to the top of Booster Tower after defeating the balcony boss will always warp you to the ground.
    
    2) Reaching the Inner Factory will reveal a trampoline that warps you to the world map.
    
    3) Reaching the Inner Factory will enable a world map shortcut that places you in Inner Factory.'''
    modes = ['open']
    default = False

# Item Location Settings

class FireworksOptions(enum.Enum):
    """Enumeration for Fireworks flag option"""
    Vanilla = enum.value("Vanilla")
    ShuffleFireworks = enum.value("Shuffle Fireworks")
    ProgressiveFireworks = enum.value("Shuffle Progressive Fireworks")

class FireworksSetting(SelectOneFlag):
    name = '''Fireworks distribution'''
    description = '''Vanilla: Unchanged from the original game. Fireworks may be purchased in any amount from the Moleville house after completing the Mines.
    
    Shuffle Fireworks: 
    * One Fireworks is shuffled somewhere in the game.
    * The ending credits fireworks are random. 
    * Fireworks, Shiny Stone, and Carbo Cookie are key items. 
    * The Fireworks shop sells a single item check after completing the Mines. 
    * The Fireworks, Shiny Stone, and Carbo Cookie are still traded in their normal places.
    * If Bucket Warp is disabled, exchanging the Carbo Cookie is a single item check. 
    * You may ask the Item Shop girl for your Shiny Stone back if you need it in Monstro Town.
    
    Shuffle Progressive Fireworks: 
    * Fireworks, Shiny Stone, and Carbo Cookie are each shuffled somewhere in the game, and you will always receive them in order. 
    * The ending credits fireworks are random. 
    * Fireworks, Shiny Stone, and Carbo Cookie are key items. 
    * The Fireworks shop sells a single item check after completing the Mines.  
    * The Pur-tend store and Moleville item shop trade girl are disabled.
    * If Bucket Warp is disabled, exchanging the Carbo Cookie is a single item check. 
    * The Monstro Town sealed door is automatically opened when you find the Shiny Stone.'''
    modes = ['open']
    choices = [o.value for o in FireworksOptions]
    default = FireworksOptions.Vanilla

class GrateGuyPrizeThreshold(NumberThresholdFlag):
    name = 'Required "Look The Other Way" wins'
    description = "The number of times required to win Grate Guy's casino minigame to receive its ultimate prize."
    default = 100
    min = 1
    max = 255
    modes = ['open']

class KnifeGuyPrizeThreshold(NumberThresholdFlag):
    name = 'Required juggling wins'
    description = "The number of wins minus losses required to win Knife Guy's ultimate juggling game prize."
    default = 12
    min = 1
    max = 254
    modes = ['open']

class SuitePrize1Threshold(NumberThresholdFlag):
    name = 'Required Suite prize #1 stays'
    description = "The number of times required to stay in the Marrymore Suite to receive the first special gift"
    default = 1
    min = 1
    max = 254
    modes = ['open']

class SuitePrize2Threshold(NumberThresholdFlag):
    name = 'Required Suite prize #2 stays'
    description = "The number of times required to stay in the Marrymore Suite to receive the second special gift"
    default = 3
    min = 1
    max = 254
    modes = ['open']

class SuitePrize3Threshold(NumberThresholdFlag):
    name = 'Required Suite prize #3 stays'
    description = "The number of times required to stay in the Marrymore Suite to receive the third special gift"
    default = 5
    min = 1
    max = 254
    modes = ['open']

class SuitePrize4Threshold(NumberThresholdFlag):
    name = 'Required Suite prize #4 stays'
    description = "The number of times required to stay in the Marrymore Suite to receive the fourth special gift"
    default = 10
    min = 1
    max = 254
    modes = ['open']

class SuitePrize5Threshold(NumberThresholdFlag):
    name = 'Required Suite prize #5 stays'
    description = "The number of times required to stay in the Marrymore Suite to receive the fifth special gift"
    default = 15
    min = 1
    max = 254
    modes = ['open']

class SuitePrize6Threshold(NumberThresholdFlag):
    name = 'Required Suite prize #6 stays'
    description = "The number of times required to stay in the Marrymore Suite to receive the sixth special gift"
    default = 200
    min = 1
    max = 254
    modes = ['open']

class SuperJump1Threshold(NumberThresholdFlag):
    name = 'Required Super Jumps for prize #1'
    description = "The number of consecutive Super Jumps required for the first prize in Monstro Town"
    default = 30
    min = 1
    max = 100
    modes = ['open']

class SuperJump2Threshold(NumberThresholdFlag):
    name = 'Required Super Jumps for prize #2'
    description = "The number of consecutive Super Jumps required for the second prize in Monstro Town"
    default = 100
    min = 1
    max = 100
    modes = ['open']

# move location descriptions into an enum to be used in the setting
# and reference those enum values in the location classes

class BowsersKeepOpen(Flag):
    name = "Include Bowser's Keep locations"
    description = ("Bowser's Keep is open from the start and the boss locations inside the keep may have Star Pieces.  "
                   "The Factory will be opened once you find all Star Pieces.")
    inverse_description = ("(Bowser's Keep will not contain any Star Pieces, and will be opened when you find all your "
                           "Star Pieces.)")
    value = 'Rk'
    modes = ['open']


class CulexStarShuffle(Flag):
    name = "Include Culex's Lair"
    description = "Culex's Lair in Monstro Town may have a Star Piece."
    inverse_description = "(Culex's Lair in Monstro Town will not have a Star Piece.)"
    value = 'Rc'
    hard = True
    modes = ['open']


class StarPieceShuffle(Flag):
    name = 'Randomize star pieces'
    description = ("Assigns six star pieces to random boss locations, excluding Culex's Lair, Bowser's Keep, and the "
                   "Factory. Collect all the star pieces to open Bowser's Keep and progress to the end of the game.")
    inverse_description = "(The star pieces will stay in their original locations.)"
    value = 'R'
    modes = ['open']
    options = [
        SevenStarHunt,
        BowsersKeepOpen,
        CulexStarShuffle,
    ]


# ******** Key item shuffle

class IncludeSeedFertilizer(Flag):
    name = 'Include Seed and Fertilizer'
    description = 'The **Seed** and **Fertilizer** will be included in the key item shuffle.'
    inverse_description = "(The Seed and Fertilizer can be found in their original locations.)"
    value = 'Ks'
    modes = ['open']


class IncludeBrightCard(Flag):
    name = 'Include Bright Card'
    description = 'The **Bright Card** will be included in the key item shuffle.'
    inverse_description = "(The Bright Card can be found in Booster's Tower after completing it.)"
    value = 'Kb'
    modes = ['open']


class KeyItemShuffle(Flag):
    name = 'Randomize key items'
    description = ("The locations of key items are shuffled amongst each other.  For example, you may find the "
                   "Shed Key at Croco 1 instead of the Rare Frog Coin.\n\nThe items randomized this way are the "
                   "**Rare Frog Coin**, **Cricket Pie**, **Bambino Bomb**, **Castle Key 1**, **Castle Key 2**, "
                   "**Alto Card**, **Tenor Card**, **Soprano Card**, **Greaper Flag**, **Dry Bones Flag**, "
                   "**Big Boo Flag**, **Shed Key**, **Elder Key**, **Cricket Jam**, **Temple Key**, and **Room Key**.")
    inverse_description = "(The key items will stay in their original locations.)"
    value = 'K'
    modes = ['open']
    options = [
        IncludeSeedFertilizer,
        IncludeBrightCard,
    ]


# ******** Character shuffle flags

class CharacterStats(Flag):
    name = 'Randomize character stats'
    description = "Stats for each character will be randomized."
    inverse_description = ("(The characters will retain their original attack, defense, magic attack, magic defense, "
                           "and speed stats.)")
    value = 'Cs'


class CharacterJoinOrder(Flag):
    name = 'Randomize character join order'
    description = ("Characters join your party at the same spots, but the character you get there is randomized.  The "
                   "character that joins the party will have their stats and starting level scaled for that spot.")
    inverse_description = "(You will start with Mario, Mallow, and Geno, and must recruit Bowser and Peach.)"
    value = 'Cj'


class CharacterLearnedSpells(Flag):
    name = 'Randomize character learned spells'
    description = "The spells each character learns and what level they learn them are randomized."
    inverse_description = "(Characters retain their original spell lists.)"
    value = 'Cl'


class CharacterSpellStats(Flag):
    name = 'Randomize character spell stats'
    description = "The power and FP cost of character magic spells will be randomized."
    inverse_description = "(Base power and FP cost of party spells are unchanged from the original game.)"
    value = 'Cp'


class CharacterShuffle(Flag):
    name = 'Randomize characters'
    value = '@C'
    options = [
        CharacterStats,
        CharacterSpellStats,
        CharacterJoinOrder,
        CharacterLearnedSpells,
    ]


class StartMario(Flag):
    name = 'Start as Mario'
    value = 'Ym'
class StartMallow(Flag):
    name = 'Start as Mallow'
    value = 'Yw'
class StartGeno(Flag):
    name = 'Start as Geno'
    value = 'Yg'
class StartBowser(Flag):
    name = 'Start as Bowser'
    value = 'Yb'
class StartToadstool(Flag):
    name = 'Start as Toadstool'
    value = 'Yt'

class ExcludeMario(Flag):
    name = 'Exclude Mario'
    description = "Mario cannot be recruited."
    value = 'Zm'
class ExcludeMallow(Flag):
    name = 'Exclude Mallow'
    description = "Mallow cannot be recruited."
    value = 'Zw'
class ExcludeGeno(Flag):
    name = 'Exclude Geno'
    description = "Geno cannot be recruited."
    value = 'Zg'
class ExcludeBowser(Flag):
    name = 'Exclude Bowser'
    description = "Bowser cannot be recruited."
    value = 'Zb'
class ExcludeToadstool(Flag):
    name = 'Exclude Toadstool'
    description = "Toadstool cannot be recruited."
    value = 'Zt'

class ExcludeMario(Flag):
    name = 'Exclude Mario'
    description = "Mario cannot be recruited."
    value = 'Zm'
class ExcludeMallow(Flag):
    name = 'Exclude Mallow'
    description = "Mallow cannot be recruited."
    value = 'Zw'
class ExcludeGeno(Flag):
    name = 'Exclude Geno'
    description = "Geno cannot be recruited."
    value = 'Zg'
class ExcludeBowser(Flag):
    name = 'Exclude Bowser'
    description = "Bowser cannot be recruited."
    value = 'Zb'
class ExcludeToadstool(Flag):
    name = 'Exclude Toadstool'
    description = "Toadstool cannot be recruited."
    value = 'Zt'

class NoFreeCharacters(Flag):
    name = 'No Free Characters'
    description = "Instead of starting with 3 characters, you start off with only one. Mushroom Way and Moleville Mines area bosses will add characters to your party in addition to Marrymore and Forest Maze."
    modes = ['open']
    value = '-nfc'

class ExcludeCharacters(Flag):
    name = 'Exclude characters'
    description = "If a character is excluded, their designated recruitment spot will be empty."
    modes = ['open']
    value = '@Z'
    options = [
        ExcludeMario,
        ExcludeMallow,
        ExcludeGeno,
        ExcludeBowser,
        ExcludeToadstool
    ]

class ChooseStarter(Flag):
    name = 'Choose starting character'
    description = "Guarantees that your first party slot will be the chosen character"
    modes = ['open']
    value = '@Y'
    choices = [
        StartMario,
        StartMallow,
        StartGeno,
        StartBowser,
        StartToadstool
    ]


# ******** Enemy shuffle flags

class EnemyStats(Flag):
    name = 'Randomize enemy stats'
    description = "Enemy stats and immunities/weaknesses will be randomized."
    inverse_description = ("(The enemies will retain their original attack, defense, m.attack, m.defense, speed, "
                           "weaknesses, and immunities.)")
    value = 'Es'


class EnemyDrops(Flag):
    name = 'Randomize enemy drops'
    description = "The EXP and items received from enemies will be randomized."
    inverse_description = "(Battle prize drops are unchanged from the original game.)"
    value = 'Ed'


class EnemyFormations(Flag):
    name = 'Randomize enemy formations'
    description = "Normal enemy battle formations will be randomized.  Boss formations are not affected."
    inverse_description = "(Random battle formations remain the same as in the original game.)"
    value = 'Ef'


class EnemyAttacks(Flag):
    name = 'Randomize enemy attacks'
    description = "Enemy spells and attacks will have their power and potential status effects randomized."
    inverse_description = ("(Base power and status casts of enemy spells and attacks are unchanged from the original "
                           "game.)")
    value = 'Ea'


class EnemySpells(Flag):
    name = 'Randomize enemy spells'
    description = "Enemies can cast random spells. I.E. Mack could cast Blast instead of Flame."
    inverse_description = ("(Enemies cast the normal spells they're expected to.)")
    value = 'Ec'
    hard = True
    modes = ['open']


class EnemyNoSafetyChecks(Flag):
    name = 'No safety checks'
    description = "Removes safety checks on enemy attack shuffle that prevent abnormally large effects."
    inverse_description = "(Enemy stat shuffling should not skew abnormally high.)"
    value = 'E!'
    hard = True


class EnemyShuffle(Flag):
    name = 'Randomize enemies'
    value = '@E'
    options = [
        EnemyDrops,
        EnemyFormations,
        EnemyStats,
        EnemyAttacks,
        EnemySpells,
        EnemyNoSafetyChecks,
    ]


class BossShuffleCulex(Flag):
    name = 'Include Culex'
    inverse_description = "(Culex will remain in his door in Monstro Town.)"
    value = 'Bc'
    hard = True


class BossShuffleKeepStats(Flag):
    name = "Don't scale stats"
    description = "Boss stats will **not** be scaled to match the battle it's replacing."
    inverse_description = "(Turning the Bs flag off affirms that boss stats will indeed be scaled.)"
    value = 'Bs'
    hard = True


class BossShuffleMusic(Flag):
    name = 'Randomize boss music'
    description = 'Battle music will be randomized for each boss fight.'
    inverse_description = "(Battle music for each location will remain unchanged from the original game.)"
    value = 'Bm'


class BossShuffle(Flag):
    name = 'Randomize bosses'
    description = ("The positions of bosses (including Pandorite, Hidon, and Box Boy) are shuffled. By default, when a "
                   "boss is moved, its stats are scaled to match its new location.")
    inverse_description = "(Bosses will stay in their original locations.)"
    modes = ['open']
    value = 'B'
    options = [
        BossShuffleMusic,
        BossShuffleCulex,
        BossShuffleKeepStats,
    ]


# ******** Chest shuffle flags


class ChestTier1(Flag):
    name = "Restrict to worst items"
    description = "Only the very worst items will appear in chests and as sidequest rewards."
    value = 'T1'
    hard = True


class ChestTier2(Flag):
    name = "Restrict to weak items"
    description = "Only weak equipment and some support/healing items will appear in chests and as sidequest rewards."
    value = 'T2'


class ChestTier3(Flag):
    name = "Exclude best items"
    description = ("Out of all items that could appear in chests and as sidequest rewards, the very best items will be "
                   "left out.")
    value = 'T3'


class ChestTier4(Flag):
    name = "Include all items"
    description = "Any item may appear in a chest or sidequest reward (besides key items)."
    value = 'T4'


class ChestExcludeRewards(Flag):
    name = 'Exclude sidequest reward spots'
    description = "Only actual treasure chests will be shuffled, sidequest reward spots will be left alone."
    inverse_description = "(Sidequest rewards are randomized.)"
    value = 'Tn'


class ChestExcludeCoins(Flag):
    name = 'No Coins'
    description = "Chests will not contain coins."
    inverse_description = "(Chests may contain coins.)"
    value = 'Ty'


class ChestExcludeFrogCoins(Flag):
    name = 'No Frog Coins'
    description = "Chests will not contain frog coins."
    inverse_description = "(Chests may contain frog coins.)"
    value = 'Tz'


class ChestExcludeFlowers(Flag):
    name = 'No Flowers'
    description = "Chests will not contain FP flowers."
    inverse_description = "(Chests may contain FP flowers.)"
    value = 'Tf'


class ChestExcludeMushrooms(Flag):
    name = 'No Recovery Mushrooms'
    description = "Chests will not contain heal mushrooms."
    inverse_description = "(Chests may contain heal mushrooms.)"
    value = 'Tm'


class ChestExcludeStars(Flag):
    name = 'No Stars'
    description = "Chests will not contain invincibility stars."
    value = 'T!'
    hard = True


class ChestRandomizeStars(Flag):
    name = 'Shuffle Stars'
    description = "The number and locations of EXP stars are randomized."
    value = 'Tr'


class ChestStarShuffle(Flag):
    name = 'EXP Stars'
    inverse_description = "(EXP stars are not affected by chest shuffle.)"
    value = 'Ts'
    choices = [
        ChestRandomizeStars,
        ChestExcludeStars,
    ]


class ChestKIInclude3DMaze(Flag):
    name = 'Include 3D Maze'
    inverse_description = "(3D Maze will not have a key item.)"
    value = 'Td'


class ChestKIIncludeCulex(Flag):
    name = 'Include Culex\'s Lair'
    inverse_description = "(Culex's lair will not have a key item.)"
    value = 'Tu'
    hard = True


class ChestKIInclude30(Flag):
    name = 'Include 30 Super Jumps'
    inverse_description = "(30 Super Jumps will not have a key item.)"
    value = 'Th'
    hard = True


class ChestKIInclude100(Flag):
    name = 'Include 100 Super Jumps'
    inverse_description = "(100 Super Jumps will not have a key item.)"
    value = 'Ti'
    hard = True


class ChestIncludeKeyItems(Flag):
    name = 'Include Key Items'
    description = "Shuffled chests or sidequest rewards may contain a key item."
    inverse_description = ("(Chests and sidequest rewards will not contain key items, with the exception of the "
                           "Kero Sewers chest.)")
    value = 'Tk'
    hard = True
    options = [
        ChestKIInclude3DMaze,
        ChestKIIncludeCulex,
        ChestKIInclude30,
        ChestKIInclude100,
    ]


class ChestShuffleEmpty(Flag):
    name = 'Empty chests'
    description = 'All chests give the "You missed!" cutscene, and sidequest rewards give you nothing.'
    value = 'Tx'
    hard = True


class ChestShuffle1(Flag):
    name = 'Vanilla shuffle'
    description = ('Chest and sidequest reward contents are the same as the original game, but shuffled within the '
                   'same area.')
    value = 'Tv'
    choices = [
        ChestTier4,
        ChestTier3,
        ChestTier2,
        ChestTier1,
    ]
    options = [
        ChestExcludeCoins,
        ChestExcludeFrogCoins,
        ChestExcludeFlowers,
        ChestExcludeMushrooms,
        ChestExcludeStars,
    ]


class ChestShuffleBiased(Flag):
    name = 'Biased shuffle'
    description = "Chests and sidequest rewards that are harder to access will contain better items."
    value = 'Tb'
    choices = [
        ChestTier4,
        ChestTier3,
        ChestTier2
    ]
    options = [
        ChestExcludeRewards,
        ChestExcludeCoins,
        ChestExcludeFrogCoins,
        ChestExcludeFlowers,
        ChestExcludeMushrooms,
        ChestStarShuffle,
        ChestIncludeKeyItems,
    ]


class ChestShuffleChaos(Flag):
    name = 'Chaotic shuffle'
    description = "Any chest or sidequest reward may contain anything."
    value = 'Tc'
    choices = [
        ChestTier4,
        ChestTier3,
        ChestTier2,
        ChestTier1,
    ]
    options = [
        ChestExcludeRewards,
        ChestExcludeCoins,
        ChestExcludeFrogCoins,
        ChestExcludeFlowers,
        ChestExcludeMushrooms,
        ChestStarShuffle,
        ChestIncludeKeyItems,
    ]


class ChestShuffleFlag(Flag):
    name = 'Randomize untrapped chest contents & sidequest rewards'
    # description = '(note that some locations will not be affected)'
    inverse_description = "(Chest and reward contents will remain unchanged from the original game.)"
    modes = ['open']
    value = '@T'
    choices = [
        ChestShuffleChaos,
        ChestShuffleBiased,
        ChestShuffle1,
        ChestShuffleEmpty,
    ]


class MonstroTownLite(Flag):
    name = 'Monstro rewards only'
    description = ('The Super Suit, Attack Scarf, Quartz Charm, Jinx Belt, and Ghost Medal locations will be shuffled '
                   'within each other.')
    value = 'M1'


class MonstroTownHard(Flag):
    name = 'Monstro rewards and key item rewards'
    description = ('The Super Suit, Attack Scarf, Quartz Charm, Jinx Belt, Ghost Medal, FroggieStick, Zoom Shoes, '
                   'Chomp, Lazy Shell Weapon, and Lazy Shell Armor locations will be shuffled within each other.')
    value = 'M2'


class MonstroExcludeElsewhere(Flag):
    name = 'Exclude elsewhere'
    description = ('The items shuffled by your selected option will not appear in any shops or any other chests or '
                   'reward spots.')
    inverse_description = '(The items listed under the M flag may still appear in shops and other chests.)'
    value = 'Mx'
    hard = True


class MonstroTownShuffle(Flag):
    name = 'Monstro Town Shuffle'
    description = 'Randomize the locations of some special equips. This flag overrides all T flags except Tx.'
    inverse_description = ('(The Monstro Town and key item equip rewards are shuffled the same as all other '
                           'chest/reward slots.)')
    modes = ['open']
    value = '@M'
    choices = [
        MonstroTownLite,
        MonstroTownHard,
    ]
    options = [
        MonstroExcludeElsewhere,
    ]


class ReplaceItems(Flag):
    name = 'Replace worst chest items with coins'
    description = 'The lowest ranked items will be replaced with coins in chests.'
    inverse_description = '(You may find low-ranked items in chests.)'
    modes = ['open']
    value = '$'


# ******** Shop shuffle flags


class ShopTier1(Flag):
    name = "Restrict to worst items"
    description = "Only the very worst equipment and support/healing items will appear in shops."
    value = 'S1'
    hard = True


class ShopTier2(Flag):
    name = "Restrict to weak items"
    description = "Only weak equipment and some support/healing items will appear in shops."
    value = 'S2'


class ShopTier3(Flag):
    name = "Exclude best items"
    description = "Out of all items that could appear in shops, the very best items will be left out."
    value = 'S3'


class ShopTier4(Flag):
    name = "Include all items"
    description = "Any non-key item may appear in a shop."
    value = 'S4'


class ShopNotGuaranteed(Flag):
    name = "Items not guaranteed"
    description = "Some items may not appear in shops at all."
    inverse_description = "(Every item, except for key items and the Wallet, will appear in at least 1 shop.)"
    value = 'Sn'
    hard = True


class ShopShuffleVanilla(Flag):
    name = "Vanilla shop inventory"
    description = ("Shops will only contain items that were available in the original game's shops, shuffled amongst "
                   "each other.")
    value = 'Sv'
    choices = [
        ShopTier4,
        ShopTier3,
        ShopTier2,
        ShopTier1
    ]
    options = [
        ShopNotGuaranteed
    ]


class ShopShuffleBalanced(Flag):
    name = "Biased shop inventory"
    description = "Shops that are harder to access will contain better items."
    value = 'Sb'
    choices = [
        ShopTier4,
        ShopTier3,
        ShopTier2
    ]
    options = [
        ShopNotGuaranteed
    ]


class ShopShuffleChaotic(Flag):
    name = "Chaotic shop inventory"
    description = "Any shop may contain anything."
    value = 'Sc'
    choices = [
        ShopTier4,
        ShopTier3,
        ShopTier2,
        ShopTier1
    ]
    options = [
        ShopNotGuaranteed
    ]


class ShopTierX(Flag):
    name = "Empty shops"
    description = "All shops contain only the Goodie Bag."
    value = 'Sx'
    hard = True


class ShopShuffle(Flag):
    name = 'Randomize shops'
    description = "Shop contents and prices will be shuffled"
    inverse_description = "(Shop contents and item prices remain unchanged from the original game.)"
    value = '@S'
    choices = [
        ShopShuffleChaotic,
        ShopShuffleBalanced,
        ShopShuffleVanilla,
        ShopTierX
    ]


class FreeShops(Flag):
    name = "'Free' Shops"
    description = "All shop items will cost 1 coin. You will start with 9999 coins and 99 frog coins."
    inverse_description = "(Shops are not free, and you start with 0 coins.)"
    value = '-freeshops'


# ******** Item shuffle flags

class EquipmentStats(Flag):
    name = 'Randomize equipment stats'
    description = "Attack, defense, magic attack, magic defense, and speed granted by equipment will be randomized"
    inverse_description = ("(Attack, defense, magic attack, magic defense, and speed granted by equipment remain "
                           "unchanged from the original game.)")
    value = 'Qs'


class EquipmentBuffs(Flag):
    name = 'Randomize equipment buffs'
    description = ("Special buffs granted by equipment will be randomized (attack/defense boost, "
                   "elemental/status immunities).  See Resources page for an explanation of these.")
    inverse_description = ("(Immunities and boost multipliers granted by equipment remain unchanged from the original "
                           "game.)")
    value = 'Qb'


class EquipmentCharacters(Flag):
    name = 'Randomize allowed characters'
    description = "Each equip's list of characters that can wear it will be randomized."
    inverse_description = ("(Each equip's list of characters that can wear it will remain unchanged from the original "
                           "game.)")
    value = 'Qa'


class EquipmentNoSafetyChecks(Flag):
    name = 'No safety checks'
    description = ("Normally certain namesake items retain their protections: **Fearless Pin**, **Antidote Pin**, "
                   "**Trueform Pin**, and **Wakeup Pin**.  In addition, at least four equipment will have instant KO "
                   "protection.  This flag removes those checks.")
    inverse_description = ("(Namesake properties such as **Fearless Pin**, **Antidote Pin**, **Trueform Pin**, and "
                           "**Wakeup Pin** remain intact, and at least four pieces of equipment will have instant "
                           "KO protection.)")
    value = 'Q!'
    hard = True


class EquipmentShuffle(Flag):
    name = 'Randomize equipment'
    value = '@Q'
    options = [
        EquipmentStats,
        EquipmentBuffs,
        EquipmentCharacters,
        EquipmentNoSafetyChecks,
    ]


# ******** Experience

class ExperienceBoost2x(Flag):
    name = 'Double XP'
    description = 'XP is doubled'
    value = 'X2'


class ExperienceBoost3x(Flag):
    name = 'Triple XP'
    description = 'XP is tripled to simulate no XP split'
    value = 'X3'


class ExperienceBoost(Flag):
    name = 'XP boost'
    description = 'Earned experience points are increased for faster levelling.'
    inverse_description = "(Earned experience points are the same as the vanilla game.)"
    value = '@X'
    choices = [
        ExperienceBoost2x,
        ExperienceBoost3x,
    ]


class ExperienceNoRegular(Flag):
    name = 'No XP from regular encounters'
    description = 'Bosses still award XP.'
    inverse_description = "(You will receive EXP from non-boss fights.)"
    value = '-noexp'
    hard = True

class ExperienceNoBosses(Flag):
    name = 'No XP from bosses'
    description = 'Bosses don\'t reward XP.'
    inverse_description = "(You will receive EXP from boss fights.)"
    value = '-nobossexp'
    hard = True



# ******** Star exp progression challenge

class StarExp1(Flag):
    name = 'Balanced'
    description = ("* 0 stars - 2 exp\n"
                   "* 1 star - 4 exp\n"
                   "* 2 stars - 5 exp\n"
                   "* 3 stars - 6 exp\n"
                   "* 4 stars - 8 exp\n"
                   "* 5 stars - 9 exp\n"
                   "* 6/7 stars - 11 exp")
    value = 'P1'


class StarExp2(Flag):
    name = 'Difficult'
    description = ("* 0 stars - 1 exp\n"
                   "* 1 star - 2 exp\n"
                   "* 2 stars - 3 exp\n"
                   "* 3 stars - 5 exp\n"
                   "* 4 stars - 6 exp\n"
                   "* 5 stars - 7 exp\n"
                   "* 6/7 stars - 11 exp")
    value = 'P2'
    hard = True

class StarExp3(Flag):
    name = 'None'
    description = ("All stars give 0 XP")
    value = 'PZ'
    hard = True


class StarExpChallenge(Flag):
    name = 'Star EXP progression challenge'
    description = 'Invincibility stars give exp based on the number of star pieces collected.'
    inverse_description = '(Invincibility stars grant the amount of EXP given in the original game.)'
    modes = ['open']
    value = '@P'
    choices = [
        StarExp1,
        StarExp2,
        StarExp3,
    ]


# ******** Minigame challenges

class BallSolitaireShuffle(Flag):
    name = 'Randomize Ball Solitaire'
    description = 'The layout for the Ball Solitaire minigame will be randomized.'
    inverse_description = '(Ball Solitaire minigame will be the same as vanilla.)'
    value = 'Nb'


class MagicButtonShuffle(Flag):
    name = 'Randomize Magic Buttons'
    description = 'The layout for the Magic Buttons minigame will be randomized.'
    inverse_description = '(Magic Buttons minigame will be the same as vanilla.)'
    value = 'Nm'


class QuizShuffle(Flag):
    name = 'Randomize Dr. Topper Quiz'
    description = 'The question pool for the Dr. Topper quiz will include new questions provided by the community.'
    inverse_description = '(Dr. Topper quiz question pool will be the same as vanilla.)'
    value = 'Nq'


class Minigames(Flag):
    name = 'Minigames'
    modes = ['open']
    value = '@N'
    options = [
        BallSolitaireShuffle,
        MagicButtonShuffle,
        QuizShuffle,
    ]


# ******** Glitches

class NoGenoWhirlExor(Flag):
    name = 'No Geno Whirl on Exor'
    description = 'Fixes the Exor bug where he is vulnerable to Geno Whirl when the eyes are stunned.'
    inverse_description = ('(You may used a Timed Hit Geno Whirl to instantly KO Exor when its eye protection is '
                           'removed.)')
    value = 'Ge'
    hard = True


class FixMagikoopa(Flag):
    name = "Fix Magikoopa"
    description = 'Fixes Magikoopa bug after King Bomb explodes that prevents him from taking further actions.'
    inverse_description = '(Magikoopa will remain disabled for the remainder of the fight if King Bomb uses Big Bang.)'
    value = 'Gm'


class NoMackSkip(Flag):
    name = "No Mack Skip"
    description = 'You will not be able to skip the boss in Mushroom Kingdom.'
    inverse_description = '(You may attempt to skip the boss in Mushroom Kingdom.)'
    value = 'Gs'


class NoOHKO(Flag):
    name = "No instant KOs on boss allies"
    description = ('You will not be able to use Geno Whirl or Pure Water to OHKO any allies to a boss (Mallow Clone, '
                   'Mad Mallet, Fautso, etc).')
    inverse_description = ('(Some boss allies may be susceptible to Geno Whirl, and Belome 2\'s clones will still be '
                           'susceptible to Pure Water.)')
    value = 'Gk'


class Glitches(Flag):
    name = 'Boss Glitch & Exploit Removals'
    modes = ['open']
    value = '@G'
    options = [
        NoMackSkip,
        FixMagikoopa,
        NoOHKO,
        NoGenoWhirlExor,
    ]


class PoisonMushroom(Flag):
    name = 'Change Fake Mushroom\'s Status'
    description = ('Randomize the status effect inflicted on a party member with the Fake Mushroom. It will only give '
                   'one status effect per seed, which has a 1/8 chance of being Invincibility.')
    inverse_description = '(The Fake Mushroom will always turn you into a mushroom.)'
    modes = ['open']
    value = '-fakeout'


class BowsersKeep1(Flag):
    name = '1 Bowser Door'
    description = 'You must complete 1 door in Bowser\'s Keep to proceed to the first boss fight.'
    modes = ['open']
    value = 'D1'


class BowsersKeep2(Flag):
    name = '2 Bowser Doors'
    description = 'You must complete 2 doors in Bowser\'s Keep to proceed to the first boss fight.'
    modes = ['open']
    value = 'D2'


class BowsersKeep3(Flag):
    name = '3 Bowser Doors'
    description = 'You must complete 3 doors in Bowser\'s Keep to proceed to the first boss fight.'
    modes = ['open']
    value = 'D3'


class BowsersKeep4(Flag):
    name = '4 Bowser Doors'
    description = 'You must complete 4 doors in Bowser\'s Keep to proceed to the first boss fight.'
    modes = ['open']
    value = 'D4'


class BowsersKeep5(Flag):
    name = '5 Bowser Doors'
    description = 'You must complete 5 doors in Bowser\'s Keep to proceed to the first boss fight.'
    modes = ['open']
    value = 'D5'
    hard = True


class BowsersKeep6(Flag):
    name = '6 Bowser Doors'
    description = 'You must complete all 6 doors in Bowser\'s Keep to proceed to the first boss fight.'
    modes = ['open']
    value = 'D6'
    hard = True


class ShuffleBowsersKeep(Flag):
    name = 'Shuffle Bowser\'s Keep'
    description = 'Each of the 6 Bowser\'s Keep doors will contain 3 random rooms from any of the original 6 doors.'
    inverse_description = ('(Bowser\'s Keep door contents have not changed, but their order is still subject to '
                           'in-game RNG.)')
    modes = ['open']
    value = 'Ds'


class RandomizeBowsersKeep(Flag):
    name = 'Randomize Bowser\'s Keep Door Contents'
    choices = [
        BowsersKeep1,
        BowsersKeep2,
        BowsersKeep3,
        BowsersKeep4,
        BowsersKeep5,
        BowsersKeep6,
    ]
    options = [
        ShuffleBowsersKeep
    ]
    modes = ['open']
    value = '@D'


class CasinoWarp(Flag):
    name = "Enable Factory Warp"
    description = "Once you collect all your Star Pieces, you can talk to Grate Guy to warp directly to the final boss."
    inverse_description = "(There is no factory warp in Grate Guy's Casino.)"
    modes = ['open']
    value = 'W'


class PaletteSwaps(Flag):
    name = 'Palette Swaps'
    description = 'Your party members get a change of wardrobe!'
    inverse_description = '(Sprite colours are not modified.)'
    value = '-palette'


# ************************************** Category classes

class FlagCategory:
    name = ''
    flags = []


class KeyItemsCategory(FlagCategory):
    name = 'Key Items/Star Pieces'
    flags = [
        KeyItemShuffle,
        StarPieceShuffle,
    ]


class CharactersCategory(FlagCategory):
    name = 'Characters'
    flags = [
        CharacterShuffle,
        NoFreeCharacters,
        ChooseStarter,
        ExcludeCharacters,
        PaletteSwaps
    ]


class EnemiesCategory(FlagCategory):
    name = 'Enemies/Bosses'
    flags = [
        EnemyShuffle,
        BossShuffle,
    ]


class ChestCategory(FlagCategory):
    name = 'Treasures & Rewards'
    flags = [
        ChestShuffleFlag,
        ReplaceItems,
        MonstroTownShuffle,
    ]


class ShopsItemsCategory(FlagCategory):
    name = 'Shops'
    flags = [
        ShopShuffle,
        FreeShops
    ]


class EquipsCategory(FlagCategory):
    name = 'Equipment'
    flags = [
        EquipmentShuffle,
    ]


class BattlesCategory(FlagCategory):
    name = 'Battles'
    flags = [
        ExperienceBoost,
        ExperienceNoRegular,
        ExperienceNoBosses,
    ]


class ChallengesCategory(FlagCategory):
    name = 'Challenges'
    flags = [
        StarExpChallenge,
        Minigames,
    ]


class TweaksCategory(FlagCategory):
    name = 'Tweaks'
    flags = [
        Glitches,
        PoisonMushroom,
        RandomizeBowsersKeep,
        CasinoWarp,
    ]


# ************************************** Preset classes

class Preset:
    name = ''
    description = ''
    flags = ''


class CasualPreset(Preset):
    name = 'Casual'
    description = 'Basic flags for a casual playthrough of the game.'
    flags = 'K R Csj Tc4y $ M1 Sc4 Edf B Qa X2 P1 Nbmq D1s W'


class IntermediatePreset(Preset):
    name = 'Intermediate'
    description = 'A mild increase in difficulty compared to casual.'
    flags = 'Ks R7 Cspjl Tc3y $ M1 Sb4 Edf B Qsa X2 Nbmq D2s W'


class AdvancedPreset(Preset):
    name = 'Advanced'
    description = 'More difficult options for advanced players, requiring you to manage your equips more.'
    flags = 'Ks R7k Cspjl -nfc Tb2kd $ M2 Sb2 Edfsa Bc Qsba X2 P1 Nbmq Gm -fakeout D4s'


class ExpertPreset(Preset):
    name = 'Expert'
    description = 'A highly chaotic shuffle with everything difficult enabled and helpful glitches disabled.'
    flags = 'Ks R7kc Cspjl -nfc Tb2kduhi $ M2x Sv1 Edfsac! Bmcs Qsba! X2 P2 Nbmq Gsmke -fakeout D4s'


class QuickPreset(Preset):
    name = 'Quick'
    description = 'A faster playthrough with free shops and XP acceleration for faster progression'
    flags = 'K Rk Csjl Tc4yzm $ M2 Sc4 -freeshops Ed Bm Qsba X3 D1 W'


# ************************************** Default lists for the site.

# List of categories for the site.
CATEGORIES = (
    KeyItemsCategory,
    CharactersCategory,
    ChestCategory,
    ShopsItemsCategory,
    EnemiesCategory,
    EquipsCategory,
    BattlesCategory,
    ChallengesCategory,
    TweaksCategory
)

# List of presets.
PRESETS = (
    CasualPreset,
    IntermediatePreset,
    AdvancedPreset,
    ExpertPreset,
    QuickPreset,
)
