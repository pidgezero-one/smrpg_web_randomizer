# Flag definitions and logic.

import enum
import re
from django.utils.html import mark_safe
from markdown import markdown
from randomizer.data.helpers import ShuffleLocationSelector


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
    def get_slug(cls):
        return re.sub(r'[^a-z0-9]+', '_', cls.name.lower())

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

    type = "categorization"
    options = []
    enabled = []
    disabled = []


class SelectOneFlag(Flag):
    """For things like choosing an area gating option can and cannot contain progression"""
    type = "select_one"
    choices = []
    value = None


class BooleanFlag(Flag):
    """For settings which can only be on or off"""
    type = "boolean"
    value = False


class NumberThresholdFlag(Flag):
    """For settings which require a number from a range"""
    type = "number"
    min = 0
    max = 0
    value = 0

# ******** Star pieces


class ShuffleStarPieces(BooleanFlag):
    name = 'Randomize the locations of Star Pieces'
    description = '''If enabled, the Star Pieces may be found in places other than their original locations.
    
    If disabled, they will be rewarded by defeating the final bosses of Mushroom Kindom, Forest Maze, Moleville, Seaside Town, and Barrel Volcano, as well as a freestanding piece on Star Hill.'''
    modes = ['open']
    default = False
# if this is disabled, no other options in this category can be changed


class TotalStarPieces(NumberThresholdFlag):
    name = 'Total star pieces'
    description = "The total number of star pieces (0-7) that can appear in the seed."
    default = 6
    min = 0
    max = 7
    modes = ['open']


class StarPiecesRequired(NumberThresholdFlag):
    name = 'Star pieces required to access the final boss'
    description = "The total number of star pieces (0-7) that are required to access the final boss. Cannot be higher than Total Star Pieces."
    default = 6
    min = 0
    max = 7
    modes = ['open']


class WinConditions(enum.Enum):
    """Enumeration for win condition options"""
    FinalBoss = "Beat the Factory"
    Culex = "Beat Monstro Town sealed door"
    StarPieces = "Collect required star pieces"


class WinCondition(SelectOneFlag):
    name = "Condition required to beat the game"
    """Enumeration for win condition options"""
    description = '''Beat the Factory: When you collect the number of Star Pieces specified in your Required Star Pieces setting, the button in the Inner Factory (as well as any enabled warps) will be enabled to allow you to access the final boss and beat the game.
    
    Collect required star pieces: When you collect the number of Star Pieces specified in your Required Star Pieces setting, the game is over and the credits will roll.
    
    Beat Monstro Town sealed door: The game is over when you defeat the boss behind the sealed door in Monstro Town, regardless of your Star Piece count.'''
    choices = [o for o in WinConditions]
    default = WinConditions.FinalBoss


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


boss_star_piece_locations = [
    ShuffleLocationSelector.BanditsWayStarPiece,
    ShuffleLocationSelector.BarrelVolcanoBoss1,
    ShuffleLocationSelector.BarrelVolcanoBoss2,
    ShuffleLocationSelector.BeanValleyBoss,
    ShuffleLocationSelector.BelomeTempleBoss,
    ShuffleLocationSelector.BoosterTowerStarPiece1,
    ShuffleLocationSelector.BoosterTowerStarPiece2,
    ShuffleLocationSelector.BowsersKeepBoss1,
    ShuffleLocationSelector.BowsersKeepBoss2,
    ShuffleLocationSelector.BowsersKeepBoss3,
    ShuffleLocationSelector.BowsersKeepBossChester,
    ShuffleLocationSelector.BoxBoyBoss,
    ShuffleLocationSelector.CulexBoss,
    ShuffleLocationSelector.DojoBoss1,
    ShuffleLocationSelector.DojoBoss2,
    ShuffleLocationSelector.DojoBoss3,
    ShuffleLocationSelector.DojoBoss4,
    ShuffleLocationSelector.FactoryBoss1,
    ShuffleLocationSelector.FactoryBoss2,
    ShuffleLocationSelector.ForestMazeBoss,
    ShuffleLocationSelector.HidonBoss,
    ShuffleLocationSelector.InnerFactoryBoss1,
    ShuffleLocationSelector.InnerFactoryBoss2,
    ShuffleLocationSelector.InnerFactoryBoss3,
    ShuffleLocationSelector.InnerFactoryBoss4,
    ShuffleLocationSelector.InnerFactoryBossFinal,
    ShuffleLocationSelector.InvasionStarPiece,
    ShuffleLocationSelector.KeroSewersBoss,
    ShuffleLocationSelector.LandsEndStarPiece1,
    ShuffleLocationSelector.MarrymoreStarPiece,
    ShuffleLocationSelector.MolevilleMinesBoss1,
    ShuffleLocationSelector.MolevilleMinesBoss2,
    ShuffleLocationSelector.MushroomWayStarPiece,
    ShuffleLocationSelector.NimbusCastleStarPiece2,
    ShuffleLocationSelector.NimbusCastleStarPiece3,
    ShuffleLocationSelector.NimbusLandStarPiece1,
    ShuffleLocationSelector.PandoriteBoss,
    ShuffleLocationSelector.SeasideTownBoss,
    ShuffleLocationSelector.StarHillStarPiece1,
    ShuffleLocationSelector.SunkenShipBoss,
    ShuffleLocationSelector.SunkenShipMidboss
    ]


class EnabledBossChecks(CategorizationFlag):
    name = 'Eligible Star Piece boss fights'
    description = '''If a check is in the left column, it is eligible to reward a Star Piece.
    
    If a check is in the right column, it will still house a boss fight, but is guaranteed to not reward a Star Piece.'''
    options = [o for o in boss_star_piece_locations]
    enabled = [o for o in boss_star_piece_locations]

class StarPiecesRestrictedByArea(BooleanFlag):
    name = 'Restrict number of star pieces in an area'
    description = '''If enabled, each of the seven overworld map areas may only contain up to one star piece each.
    
    Note: This may not be perfectly respected if Bowser's Keep and Factory are both gated by high star piece counts.'''
    modes = ['open']
    default = False

class StarPieceHints(BooleanFlag):
    name = 'Signal Ring hints at star pieces'
    description = '''If enabled, the Signal Ring (if equipped to your active party) will play a sound when you enter a world area that contains a Star Piece.  
    
    The Signal Ring will only sound off when you enter an area from the World Map, from loading a save, or from an area warp (ex: the Kero Sewers - Land's End pipe). Therefore, the chime does not necessarily indicate that your current room contains a star piece, but rather that at least one room in the area does.'''
    modes = ['open']
    default = False

# ******** Party


class ShuffleCharacters(BooleanFlag):
    name = 'Randomize the locations of recruited characters'
    description = '''If enabled, Mario, Mallow, Geno, Peach, and Bowser will join your party in a random order.
    
    If disabled, you will start with Mario and recruit characters near their original locations.'''
    modes = ['open']
    default = False
# if this is disabled, no starting/available options in this category can be changed


class StartingCharacters(NumberThresholdFlag):
    # remember to set switch bit if > 3
    name = 'Starting party size'
    description = "The number of characters you will have already recruited at the start of the seed, including your starter."
    default = 1
    min = 1
    max = 5
    modes = ['open']


class PlayableCharacters(enum.Enum):
    """Enumeration for win condition options"""
    Mario = "Mario"
    Mallow = "Mallow"
    Geno = "Geno"
    Bowser = "Bowser"
    Toadstool = "Toadstool"
    Random = "Random"


class StartingCharacter(SelectOneFlag):
    name = "Starting Character"
    description = '''The first character in your party, who will appear on your save menu.'''
    choices = [o for o in PlayableCharacters]
    default = PlayableCharacters.Mario


class AvailableCharacters(CategorizationFlag):
    name = "Available Characters"
    description = '''Characters on the left will appear in the seed. Characters on the right will not.'''
    options = [o for o in [PlayableCharacters.Mario, PlayableCharacters.Mallow,
                                 PlayableCharacters.Geno, PlayableCharacters.Bowser, PlayableCharacters.Toadstool]]
    enabled = [o for o in [PlayableCharacters.Mario, PlayableCharacters.Mallow,
                                 PlayableCharacters.Geno, PlayableCharacters.Bowser, PlayableCharacters.Toadstool]]

class CharacterStats(BooleanFlag):
    name = 'Randomize character stats'
    description = '''If enabled, stats and stat curves for each playable character will be randomized.
    
    If disabled, playable characters retain their original stats and stat curves.'''
    default = False


class CharacterLearnedSpells(BooleanFlag):
    name = 'Randomize character learned spells'
    description = "The pool of spells learnable by each character will be randomized. This only covers spells originally learn-able by playable characters, and does not include enemy spells."
    default = False


class CharacterSpellStats(BooleanFlag):
    name = 'Randomize character spell stats'
    description = "The power and FP cost of character magic spells will be randomized."
    default = False


class EquipmentPropertiesOptions(enum.Enum):
    """Enumeration for win condition options"""
    default = "Default"
    some_buffs_added = "Some buffs added"
    completely_random = "Completely random"


class EquipmentProperties(BooleanFlag):
    name = 'Equipment stats & buffs'
    description = '''Default: The stats and buffs on equipment are unchanged from the original game.
    
    Some buffs added: The stats and buffs on equipment are mostly unchanged from the original game, except most armors are given one additional property (e.g. Fire Shirt nullifies damage from fire attacks) Additionally, some weapons will boost magic attack instead of physical attack.
    
    Completely random: The stats and buffs on each piece of equipment is randomized.'''
    choices = [o for o in EquipmentPropertiesOptions]
    default = EquipmentPropertiesOptions.default


class EquipmentCharacters(BooleanFlag):
    name = 'Randomize allowed characters'
    description = "Each equip's list of characters that can wear it will be randomized."
    default = False


class EquipmentNoSafety(BooleanFlag):
    name = 'No OHKO Safety'
    description = "If enabled, no equipment will protect against OHKO moves."
    default = False


class EXPMultiplierOptions(enum.Enum):
    default = "Default"
    double = "Double"
    triple = "Triple"


class EXPMultiplier(SelectOneFlag):
    name = 'EXP multiplier'
    description = '''If not set to "Default", all EXP gained will be doubled or tripled.'''
    choices = [o for o in EXPMultiplierOptions]
    default = EXPMultiplierOptions.default


# ******** Area Access


class BanditsWayGating(enum.Enum):
    """Enumeration for Bandit's Way gating flag option"""
    RecruitMario = "Recruit Mario"
    RecruitMallow = "Recruit Mallow"
    RecruitGeno = "Recruit Geno"
    RecruitBowser = "Recruit Bowser"
    RecruitToadstool = "Recruit Toadstool"
    FinishMushroomWay = "Finish Mushroom Way"
    AlwaysOpen = "Always open"


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
    choices = [o for o in BanditsWayGating]
    default = BanditsWayGating.RecruitMallow


class ForestMazeGating(enum.Enum):
    """Enumeration for Forest Maze gating flag option"""
    FindMario = "Find Mario"
    FindMallow = "Find Mallow"
    FindGeno = "Find Geno"
    FindBowser = "Find Bowser"
    FindToadstool = "Find Toadstool"
    ExchangeCricketPie = "Exchange Cricket Pie"
    AlwaysOpen = "Always open"


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
    choices = [o for o in ForestMazeGating]
    default = ForestMazeGating.FindGeno


class BoosterTowerGating(enum.Enum):
    """Enumeration for Booster Tower gating flag option"""
    RecruitMario = "Recruit Mario"
    RecruitMallow = "Recruit Mallow"
    RecruitGeno = "Recruit Geno"
    RecruitBowser = "Recruit Bowser"
    RecruitToadstool = "Recruit Toadstool"
    FinishMoleville = "Finish Moleville"
    AlwaysOpen = "Always open"


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
    choices = [o for o in BoosterTowerGating]
    default = BoosterTowerGating.RecruitBowser


class MarrymoreGating(enum.Enum):
    """Enumeration for Marrymore gating flag option"""
    FinishBoosterHill = "Finish Booster Hill"
    FinishBoosterTower = "Finish Booster Tower"
    AlwaysOpen = "Always open"


class MarrymoreGate(SelectOneFlag):
    name = '''Marrymore back door access'''
    description = '''Finish Booster Hill: The chapel back door will become available on the world map when you complete Booster Hill one time.
    
    Finish Booster Tower: The chapel back door will become available on the world map when you defeat the balcony boss of Booster Tower.
    
    Always Open: The chapel back door will be open from the start of the game.'''
    modes = ['open']
    choices = [o for o in MarrymoreGating]
    default = MarrymoreGating.FinishBoosterHill


class SeaGating(enum.Enum):
    """Enumeration for Sea & Sunken Ship gating flag option"""
    RecruitMario = "Recruit Mario"
    RecruitMallow = "Recruit Mallow"
    RecruitGeno = "Recruit Geno"
    RecruitBowser = "Recruit Bowser"
    RecruitToadstool = "Recruit Toadstool"
    Find1Star = "Collect 1 Star Piece"
    Find2Star = "Collect 2 Star Pieces"
    Find3Star = "Collect 3 Star Pieces"
    Find4Star = "Collect 4 Star Pieces"
    Find5Star = "Collect 5 Star Pieces"
    Find6Star = "Collect 6 Star Pieces"
    AlwaysOpen = "Always open"


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
    choices = [o for o in SeaGating]
    default = SeaGating.Find4Star


class YaridovichGating(enum.Enum):
    """Enumeration for Seaside boss gating flag option"""
    FinishSunkenShip = "Finish Sunken Ship"
    AlwaysOpen = "Always available"


class YaridovichGate(SelectOneFlag):
    name = '''Seaside boss fight access'''
    description = '''Finish Sunken Ship: The Seaside boss fight will become available after you defeat the final boss of Sunken Ship.
    
    Always Open: The Seaside boss will be available from the start of the game.'''
    modes = ['open']
    choices = [o for o in YaridovichGating]
    default = YaridovichGating.FinishSunkenShip


class MonstroTownGating(enum.Enum):
    """Enumeration for Monstro Town gating flag option"""
    FinishLandsEnd = "Finish Land's End"
    AlwaysOpen = "Always open"


class MonstroTownGate(SelectOneFlag):
    name = '''Monstro Town access'''
    description = '''Finish Land's End: Monstro Town will become available on the World Map once you take the pipe behind the boss of Belome Temple.
    
    Always Open: Monstro Town will be available on the World Map from the start of the game.'''
    modes = ['open']
    choices = [o for o in MonstroTownGating]
    default = MonstroTownGating.FinishLandsEnd


class BarrelVolcanoGating(enum.Enum):
    """Enumeration for Barrel Volcano gating flag option"""
    FinishNimbusLand = "Finish Nimbus Land"
    AlwaysOpen = "Always open"


class BarrelVolcanoGate(SelectOneFlag):
    name = '''Barrel Volcano access'''
    description = '''Finish Nimbus Land: Barrel Volcano will become available on the World Map once you defeat the final boss of Nimbus Castle.
    
    Always Open: Barrel Volcano will be available on the World Map from the start of the game.'''
    modes = ['open']
    choices = [o for o in BarrelVolcanoGating]
    default = BarrelVolcanoGating.FinishNimbusLand


class BowsersKeepGating(enum.Enum):
    """Enumeration for Bowser's Keep gating flag option"""
    Find1Star = "Collect 1 Star Piece"
    Find2Star = "Collect 2 Star Pieces"
    Find3Star = "Collect 3 Star Pieces"
    Find4Star = "Collect 4 Star Pieces"
    Find5Star = "Collect 5 Star Pieces"
    Find6Star = "Collect 6 Star Pieces"
    FinishBarrelVolcano = "Finish Barrel Volcano"
    AlwaysOpen = "Always open"


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
    choices = [o for o in BowsersKeepGating]
    default = BowsersKeepGating.Find6Star


class FactoryGating(enum.Enum):
    """Enumeration for Factory gating flag option"""
    AlwaysOpen = "Open when Bowser's Keep is opened"
    FinishBowsersKeep = "Finish Bowser's Keep"
    Find1Star = "Collect 1 Star Piece"
    Find2Star = "Collect 2 Star Pieces"
    Find3Star = "Collect 3 Star Pieces"
    Find4Star = "Collect 4 Star Pieces"
    Find5Star = "Collect 5 Star Pieces"
    Find6Star = "Collect 6 Star Pieces"


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
    choices = [o for o in FactoryGating]
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


class BowserDoorRequirements(NumberThresholdFlag):
    name = 'Required Bowser\'s Keep obstacle doors'
    description = "The number of doors required to progress through Bowser's Keep."
    default = 4
    min = 1
    max = 6
    modes = ['open']

# ******** Item Check Access & Distribution


class ShuffleItems(BooleanFlag):
    name = 'Randomize the contents of item rewards'
    description = '''If enabled, the contents of treasure chests, quest rewards, and (optionally) freestanding small items will be shuffled.
    
    If disabled, chests, quest rewards, and freestanding small items will remain unchanged from the original game.'''
    modes = ['open']
    default = False
# if this is disabled, no options in this category can be changed


class FireworksOptions(enum.Enum):
    """Enumeration for Fireworks flag option"""
    Vanilla = "Vanilla"
    ShuffleFireworks = "Shuffle Fireworks"
    ProgressiveFireworks = "Shuffle Progressive Fireworks"


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
    choices = [o for o in FireworksOptions]
    default = FireworksOptions.Vanilla


class PoisonMushroom(BooleanFlag):
    name = 'Change Fake Mushroom\'s Status'
    description = ('Randomize the status effect inflicted on a party member with the Fake Mushroom. It will only give '
                   'one status effect per seed, which has a 1/8 chance of being Invincibility.')
    modes = ['open']
    default = False


class ShuffleBeetlemania(BooleanFlag):
    name = 'Shuffle Beetlemania'
    description = '''If enabled, Beetlemania will be unlocked by a random item check, and the Mushroom Kingdom inn kid will sell you a random item check.'''
    modes = ['open']
    default = False


class ShuffleMagikoopaChest(BooleanFlag):
    name = 'Shuffle Magikoopa\'s coin chest'
    description = '''If enabled, Magikoopa's infinite coin box could appear in any chest, and the chest in his room will be an item check.'''
    modes = ['open']
    default = False



class KeyItemsAnywhere(BooleanFlag):
    name = '"Special Items" can appear anywhere'
    description = '''If enabled, items belonging to your "Special Items" pocket can appear in any item location.
    
    If disabled, the "Special Items" will only be shuffled within each other's locations.
    
    The items targeted by this setting are the **Rare Frog Coin**, **Cricket Pie**, **Bambino Bomb**, **Castle Key 1**, **Castle Key 2**, *Alto Card**, **Tenor Card**, **Soprano Card**, **Greaper Flag**, **Dry Bones Flag**, **Big Boo Flag**, **Shed Key**, **Elder Key**, **Cricket Jam**, **Temple Key**, and **Room Key**.'''
    modes = ['open']
    default = False


class RestrictSpecialEquips(BooleanFlag):
    name = 'Restrict key item exchange equips & Monstro Town reward equips'
    description = '''If enabled, the FroggieStick, Chomp, Zoom Shoes, Attack Scarf, Super Suit, Quartz Charm, Jinx Belt, Ghost Medal, and both Lazy Shells will appear once each, shuffled only within each other's locations. This option ignores your chosen Item Quality setting.
    
    If disabled, these items can appear anywhere, subject to the restrictions of your chosen Item Quality setting.'''
    modes = ['open']
    default = False


class EXPStarsAnywhere(BooleanFlag):
    name = 'EXP stars can appear anywhere'
    description = '''If enabled, EXP stars may appear in any chest near monsters.
    
    If disabled, EXP stars will be restricted to their original locations within Bandit's Way, Kero Sewers, Moleville Mines, Sea, Land's End, Nimbus Land, and Barrel Volcano.'''
    modes = ['open']
    default = False


class StarProgressionchallengeOptions(enum.Enum):
    default = "Default"
    sp1 = "Star pieces (easy)"
    sp2 = "Star pieces (hard)"
    bosses = "Bosses"
    none = "No EXP"

class EXPChallengeOptions(enum.Enum):
    default = "Default"
    easystars = "Star pieces (easy)"
    hardstars = "Star pieces (hard)"
    easybosses = "Bosses (easy"
    hardbosses = "Bosses (hard)"
    none = "None"


class EXPChallenge(SelectOneFlag):
    name = 'EXP Star Challenge'
    description = '''Default: EXP stars can give you 1 to 11 EXP per hit as normal.
    
    Star pieces (easy): EXP stars can give you 2, 4, 5, 6, 8, 9, or 11 EXP per hit, based on the number of Star Pieces collected. This is not adjusted for lower max Star Piece counts.
    
    Star pieces (hard): EXP stars can give you 1, 2, 3, 5, 6, 7, or 11 EXP per hit, based on the number of Star Pieces collected. This is not adjusted for lower max Star Piece counts.
    
    Bosses (easy): EXP stars can give you 2, 4, 5, 6, 8, 9, or 11 EXP depending on how many bosses you have defeated. The scaling for this option is heavily front-loaded.
    
    Bosses (hard): EXP stars can give you 1, 2, 3, 5, 6, 7, or 11 EXP depending on how many bosses you have defeated. The scaling for this option is heavily front-loaded.
    
    No EXP: EXP stars give you 0 EXP.'''
    choices = [o for o in EXPChallengeOptions]
    default = EXPChallengeOptions.default


class SlotsAnywhere(BooleanFlag):
    name = 'Slot machines can appear anywhere'
    description = '''If enabled, any chest in the world could contain a slot machine.
    
    If disabled, slot machines will be restricted to their original locations in Bean Valley.
    
    Note that a bad roll on a slot machine will initiate a duplicate of the third mimic fight.'''
    modes = ['open']
    default = False


class ItemQualities(enum.Enum):
    """Enumeration for item shuffle quality option"""
    Original = "Original item pool"
    Tier4 = "Completely random, unrestricted"
    Tier3 = "Completely random, exclude top-tier items"
    Tier2 = "Completely random, include some good items"
    Tier1 = "Completely random, bad items only"
    Empty = "Completely empty"


class ItemQuality(SelectOneFlag):
    name = '''Item pool quality'''
    description = '''Restricts the incidence of certain items within the shuffled pool. 

    If "Original item pool" is selected, items which only appear once in the original game will also not appear in unlimited shops. Additionally, two copies of the progressive Mystery Egg will be added to the pool, replacing some small items.
    
    If "Completely empty" is selected, any chest which does not contain a required item will be a "You Missed" chest.'''
    modes = ['open']
    choices = [o for o in ItemQualities]
    default = ItemQualities.Original

class BetterTips(BooleanFlag):
    name = 'Better Consolation Prizes'
    description = '''If enabled, some repeatable item grants will give a better, or wider, variety of items. Example of this include Knife Guy's juggling game junk prizes, or tips from working in the Marrymore hotel. This setting has no impact on singular, clearable item checks.'''
    modes = ['open']
    default = False


class BiasItemShuffle(BooleanFlag):
    name = 'Bias better items to gated locations'
    description = '''If enabled, harder-to-reach areas will generally house better items.'''
    modes = ['open']
    default = False


class ReplaceItems(BooleanFlag):
    name = 'Replace some chest items with coins'
    description = 'If enabled, the worst items (Wilt Shrooms, etc) will be replaced with coins in chests.'
    modes = ['open']
    default = False


class QuickHitCoins(BooleanFlag):
    name = 'Quick-hit coin chests'
    description = 'If enabled, all coin and frog coin chests will grant coins in a single hit instead of multiple hits.'
    modes = ['open']
    default = False


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
    max = 99
    modes = ['open']


class SuperJump2Threshold(NumberThresholdFlag):
    name = 'Required Super Jumps for prize #2'
    description = "The number of consecutive Super Jumps required for the second prize in Monstro Town"
    default = 100
    min = 2
    max = 100
    modes = ['open']


regular_checks = [
    ShuffleLocationSelector.BanditsWay1,
    ShuffleLocationSelector.BanditsWay2,
    ShuffleLocationSelector.BanditsWayCroco,
    ShuffleLocationSelector.BanditsWayDogJump,
    ShuffleLocationSelector.BanditsWayStarChest,
    ShuffleLocationSelector.BarrelVolcanoBeforeStar1,
    ShuffleLocationSelector.BarrelVolcanoBeforeStar2,
    ShuffleLocationSelector.BarrelVolcanoDonut1,
    ShuffleLocationSelector.BarrelVolcanoDonut2,
    ShuffleLocationSelector.BarrelVolcanoHinopio,
    ShuffleLocationSelector.BarrelVolcanoLavaPool,
    ShuffleLocationSelector.BarrelVolcanoSaveRoom1,
    ShuffleLocationSelector.BarrelVolcanoSaveRoom2,
    ShuffleLocationSelector.BarrelVolcanoSecret1,
    ShuffleLocationSelector.BarrelVolcanoSecret2,
    ShuffleLocationSelector.BarrelVolcanoStarRoom,
    ShuffleLocationSelector.BeanValley1,
    ShuffleLocationSelector.BeanValley2,
    ShuffleLocationSelector.BeanValleyBeanstalk,
    ShuffleLocationSelector.BeanValleyBottomLeftPiranhaPipe,
    ShuffleLocationSelector.BeanValleyBottomRightPiranhaPipeLower,
    ShuffleLocationSelector.BeanValleyBottomRightPiranhaPipeUpper,
    ShuffleLocationSelector.BeanValleyBoxBoyRoom1,
    ShuffleLocationSelector.BeanValleyBoxBoyRoom2,
    ShuffleLocationSelector.BeanValleyCloud1,
    ShuffleLocationSelector.BeanValleyCloud2,
    ShuffleLocationSelector.BeanValleyFall1,
    ShuffleLocationSelector.BeanValleyFall2,
    ShuffleLocationSelector.BeanValleyLeftPiranhaPipe,
    ShuffleLocationSelector.BeanValleyMegasmilaxRoom,
    ShuffleLocationSelector.BeanValleyPiranhaPlants,
    ShuffleLocationSelector.BelomeTempleAfterFortune1,
    ShuffleLocationSelector.BelomeTempleAfterFortune2,
    ShuffleLocationSelector.BelomeTempleAfterFortune3,
    ShuffleLocationSelector.BelomeTempleAfterFortune4,
    ShuffleLocationSelector.BelomeTempleFortune1,
    ShuffleLocationSelector.BelomeTempleFortune2,
    ShuffleLocationSelector.BelomeTempleFortune3,
    ShuffleLocationSelector.BelomeTempleFortune4,
    ShuffleLocationSelector.BelomeTempleFortuneTeller,
    ShuffleLocationSelector.BelomeTempleTreasure1,
    ShuffleLocationSelector.BelomeTempleTreasure2,
    ShuffleLocationSelector.BelomeTempleTreasure3,
    ShuffleLocationSelector.BoosterPass1,
    ShuffleLocationSelector.BoosterPass2,
    ShuffleLocationSelector.BoosterPassSecret1,
    ShuffleLocationSelector.BoosterPassSecret2,
    ShuffleLocationSelector.BoosterPassSecret3,
    ShuffleLocationSelector.BoosterTowerChomp,
    ShuffleLocationSelector.BoosterTowerKnifeGuy,
    ShuffleLocationSelector.BoosterTowerMasher,
    ShuffleLocationSelector.BoosterTowerParachute,
    ShuffleLocationSelector.BoosterTowerPortraits,
    ShuffleLocationSelector.BoosterTowerRailway,
    ShuffleLocationSelector.BoosterTowerRoomKey,
    ShuffleLocationSelector.BoosterTowerSpookum,
    ShuffleLocationSelector.BoosterTowerThwomp,
    ShuffleLocationSelector.BoosterTowerTop1,
    ShuffleLocationSelector.BoosterTowerTop2,
    ShuffleLocationSelector.BoosterTowerTop3,
    ShuffleLocationSelector.BoosterTowerZoomShoes,
    ShuffleLocationSelector.BowsersKeepCannonballRoom1,
    ShuffleLocationSelector.BowsersKeepCannonballRoom2,
    ShuffleLocationSelector.BowsersKeepCannonballRoom3,
    ShuffleLocationSelector.BowsersKeepCannonballRoom4,
    ShuffleLocationSelector.BowsersKeepCannonballRoom5,
    ShuffleLocationSelector.BowsersKeepCrocoShop1,
    ShuffleLocationSelector.BowsersKeepCrocoShop2,
    ShuffleLocationSelector.BowsersKeepDarkRoom,
    ShuffleLocationSelector.BowsersKeepDoorReward1,
    ShuffleLocationSelector.BowsersKeepDoorReward2,
    ShuffleLocationSelector.BowsersKeepDoorReward3,
    ShuffleLocationSelector.BowsersKeepDoorReward4,
    ShuffleLocationSelector.BowsersKeepDoorReward5,
    ShuffleLocationSelector.BowsersKeepDoorReward6,
    ShuffleLocationSelector.BowsersKeepElevatorPlatforms,
    ShuffleLocationSelector.BowsersKeepInvisibleBridge1,
    ShuffleLocationSelector.BowsersKeepInvisibleBridge2,
    ShuffleLocationSelector.BowsersKeepInvisibleBridge3,
    ShuffleLocationSelector.BowsersKeepInvisibleBridge4,
    ShuffleLocationSelector.BowsersKeepMagikoopa,
    ShuffleLocationSelector.BowsersKeepMovingPlatforms1,
    ShuffleLocationSelector.BowsersKeepMovingPlatforms2,
    ShuffleLocationSelector.BowsersKeepMovingPlatforms3,
    ShuffleLocationSelector.BowsersKeepMovingPlatforms4,
    ShuffleLocationSelector.BowsersKeepRotatingPlatforms1,
    ShuffleLocationSelector.BowsersKeepRotatingPlatforms2,
    ShuffleLocationSelector.BowsersKeepRotatingPlatforms3,
    ShuffleLocationSelector.BowsersKeepRotatingPlatforms4,
    ShuffleLocationSelector.BowsersKeepRotatingPlatforms5,
    ShuffleLocationSelector.BowsersKeepRotatingPlatforms6,
    ShuffleLocationSelector.BucketGirl,
    ShuffleLocationSelector.CasinoGrateGuyPrize,
    ShuffleLocationSelector.CricketJamReward,
    ShuffleLocationSelector.CricketPieReward,
    ShuffleLocationSelector.Croco1Reward,
    ShuffleLocationSelector.Croco1Reward2,
    ShuffleLocationSelector.Croco2Item,
    ShuffleLocationSelector.CulexReward,
    ShuffleLocationSelector.FactoryBehindSnakes1,
    ShuffleLocationSelector.FactoryBehindSnakes2,
    ShuffleLocationSelector.FactoryBoltPlatforms,
    ShuffleLocationSelector.FactoryConveyorPlatforms1,
    ShuffleLocationSelector.FactoryConveyorPlatforms2,
    ShuffleLocationSelector.FactoryFallingAxems,
    ShuffleLocationSelector.FactorySaveRoom,
    ShuffleLocationSelector.FactoryToadGift,
    ShuffleLocationSelector.FactoryTreasurePit1,
    ShuffleLocationSelector.FactoryTreasurePit2,
    ShuffleLocationSelector.FireworksShop,
    ShuffleLocationSelector.ForestMaze1,
    ShuffleLocationSelector.ForestMaze2,
    ShuffleLocationSelector.ForestMazeRedEssence,
    ShuffleLocationSelector.ForestMazeSecret1,
    ShuffleLocationSelector.ForestMazeSecret2,
    ShuffleLocationSelector.ForestMazeSecret3,
    ShuffleLocationSelector.ForestMazeSecret4,
    ShuffleLocationSelector.ForestMazeSecret5,
    ShuffleLocationSelector.ForestMazeUnderground1,
    ShuffleLocationSelector.ForestMazeUnderground2,
    ShuffleLocationSelector.ForestMazeUnderground3,
    ShuffleLocationSelector.FrogDisciple1,
    ShuffleLocationSelector.FrogDisciple2,
    ShuffleLocationSelector.FrogDisciple3,
    ShuffleLocationSelector.FrogDisciple4,
    ShuffleLocationSelector.FrogDisciple5,
    ShuffleLocationSelector.GardenerCloud1,
    ShuffleLocationSelector.GardenerCloud2,
    ShuffleLocationSelector.Gaz,
    ShuffleLocationSelector.GoombaThumping1,
    ShuffleLocationSelector.GoombaThumping2,
    ShuffleLocationSelector.HammerBrosReward,
    ShuffleLocationSelector.HidonReward1,
    ShuffleLocationSelector.HidonReward2,
    ShuffleLocationSelector.JinxDojoReward,
    ShuffleLocationSelector.KeroSewersBeforeBelomeLower,
    ShuffleLocationSelector.KeroSewersBeforeBelomeUpper2,
    ShuffleLocationSelector.KeroSewersPandoriteRoom,
    ShuffleLocationSelector.KeroSewersStarChest,
    ShuffleLocationSelector.LandsEndBeeRoom,
    ShuffleLocationSelector.LandsEndChowPit1,
    ShuffleLocationSelector.LandsEndChowPit2,
    ShuffleLocationSelector.LandsEndRedEssence,
    ShuffleLocationSelector.LandsEndSecret1,
    ShuffleLocationSelector.LandsEndSecret2,
    ShuffleLocationSelector.LandsEndShyAway,
    ShuffleLocationSelector.LandsEndStarChest1,
    ShuffleLocationSelector.LandsEndStarChest2,
    ShuffleLocationSelector.LandsEndStarChest3,
    ShuffleLocationSelector.MariosPadBed,
    ShuffleLocationSelector.MariosPadStarter1,
    ShuffleLocationSelector.MariosPadStarter2,
    ShuffleLocationSelector.MariosPadStarter3,
    ShuffleLocationSelector.MariosPadStarter4,
    ShuffleLocationSelector.MarrymoreInn,
    ShuffleLocationSelector.MarrymorePrize1,
    ShuffleLocationSelector.MarrymorePrize2,
    ShuffleLocationSelector.MarrymorePrize3,
    ShuffleLocationSelector.MarrymorePrize4,
    ShuffleLocationSelector.MarrymorePrize5,
    ShuffleLocationSelector.MarrymorePrize6,
    ShuffleLocationSelector.MelodyBay1,
    ShuffleLocationSelector.MelodyBay2,
    ShuffleLocationSelector.MelodyBay3,
    ShuffleLocationSelector.MidasRiverFirstTime,
    ShuffleLocationSelector.MolevilleMinesCoins,
    ShuffleLocationSelector.MolevilleMinesPunchinello1,
    ShuffleLocationSelector.MolevilleMinesPunchinello2,
    ShuffleLocationSelector.MonstroTownEntrance,
    ShuffleLocationSelector.MonstroTownThwomp,
    ShuffleLocationSelector.MushroomKingdomHallway,
    ShuffleLocationSelector.MushroomKingdomInn,
    ShuffleLocationSelector.MushroomKingdomStore,
    ShuffleLocationSelector.MushroomKingdomStoreBasement1,
    ShuffleLocationSelector.MushroomKingdomStoreBasement2,
    ShuffleLocationSelector.MushroomKingdomStoreExchange,
    ShuffleLocationSelector.MushroomKingdomVault1,
    ShuffleLocationSelector.MushroomKingdomVault2,
    ShuffleLocationSelector.MushroomKingdomVault3,
    ShuffleLocationSelector.MushroomWay1,
    ShuffleLocationSelector.MushroomWay2,
    ShuffleLocationSelector.MushroomWay3,
    ShuffleLocationSelector.MushroomWay4,
    ShuffleLocationSelector.NimbusCastleAfterEgg1,
    ShuffleLocationSelector.NimbusCastleAfterEgg2,
    ShuffleLocationSelector.NimbusCastleBeforeBirdetta2,
    ShuffleLocationSelector.NimbusCastleBirdetta,
    ShuffleLocationSelector.NimbusCastleCornerChestAfterValentina,
    ShuffleLocationSelector.NimbusCastleOutOfBounds1,
    ShuffleLocationSelector.NimbusCastleOutOfBounds2,
    ShuffleLocationSelector.NimbusCastleSingleGoldBird,
    ShuffleLocationSelector.NimbusCastleStarAfterValentina,
    ShuffleLocationSelector.NimbusLandCellar,
    ShuffleLocationSelector.NimbusLandInn,
    ShuffleLocationSelector.NimbusLandInn2,
    ShuffleLocationSelector.NimbusLandPrisoners,
    ShuffleLocationSelector.NimbusLandPrisoners2,
    ShuffleLocationSelector.NimbusLandRightSide,
    ShuffleLocationSelector.NimbusLandShop,
    ShuffleLocationSelector.NimbusLandSignalRing,
    ShuffleLocationSelector.PandoriteChest,
    ShuffleLocationSelector.PandoriteReward1,
    ShuffleLocationSelector.PandoriteReward2,
    ShuffleLocationSelector.PeachSurprise,
    ShuffleLocationSelector.PipeVaultNippers1,
    ShuffleLocationSelector.PipeVaultNippers2,
    ShuffleLocationSelector.PipeVaultSlide1,
    ShuffleLocationSelector.PipeVaultSlide2,
    ShuffleLocationSelector.PipeVaultSlide3,
    ShuffleLocationSelector.RoseTownFlag,
    ShuffleLocationSelector.RoseTownStore1,
    ShuffleLocationSelector.RoseTownStore2,
    ShuffleLocationSelector.RoseTownToad,
    ShuffleLocationSelector.RoseTownTreasureHouse1,
    ShuffleLocationSelector.RoseTownTreasureHouse2,
    ShuffleLocationSelector.RoseTownTreasureHouse3,
    ShuffleLocationSelector.RoseTownTreasureHouseMazeReward,
    ShuffleLocationSelector.RoseWayFiveChests1,
    ShuffleLocationSelector.RoseWayFiveChests2,
    ShuffleLocationSelector.RoseWayFiveChests3,
    ShuffleLocationSelector.RoseWayFiveChests4,
    ShuffleLocationSelector.RoseWayFiveChests5,
    ShuffleLocationSelector.RoseWayPlatform,
    ShuffleLocationSelector.SeaSaveRoom1,
    ShuffleLocationSelector.SeaSaveRoom2,
    ShuffleLocationSelector.SeaSaveRoom3,
    ShuffleLocationSelector.SeasideTownBossPrize,
    ShuffleLocationSelector.SeasideTownRescue,
    ShuffleLocationSelector.SeaStarChest,
    ShuffleLocationSelector.SeaWhirlpoolChest,
    ShuffleLocationSelector.SunkenShip3DMaze,
    ShuffleLocationSelector.SunkenShipBandanaReds,
    ShuffleLocationSelector.SunkenShipCannonballPuzzle,
    ShuffleLocationSelector.SunkenShipCloneRoom,
    ShuffleLocationSelector.SunkenShipCoins1,
    ShuffleLocationSelector.SunkenShipCoins2,
    ShuffleLocationSelector.SunkenShipFrogCoinRoom,
    ShuffleLocationSelector.HidonChest,
    ShuffleLocationSelector.SunkenShipHidonMushroom,
    ShuffleLocationSelector.SunkenShipRatStairs,
    ShuffleLocationSelector.SunkenShipSafetyRing,
    ShuffleLocationSelector.SunkenShipShop,
    ShuffleLocationSelector.SuperJumps100,
    ShuffleLocationSelector.SuperJumps30,
    ShuffleLocationSelector.ThreeMustyFears,
    ShuffleLocationSelector.TreasureSeller1,
    ShuffleLocationSelector.TreasureSeller2,
    ShuffleLocationSelector.TreasureSeller3,
    ShuffleLocationSelector.TroopaClimb,
    ShuffleLocationSelector.YosterIsleEntrance,
    ShuffleLocationSelector.YosterIsleFlag,
    ShuffleLocationSelector.YosterIsleRaceReward1,
    ShuffleLocationSelector.YosterIsleRaceReward2,
    ShuffleLocationSelector.YosterIsleRaceReward3
]


class EnabledRegularChecks(CategorizationFlag):
    name = 'Chest & reward checks'
    description = '''If a check is in the left column, it is eligible to contain items required to complete the seed.
    
    If a check is in the right column, its contents will be shuffled, but it will not contain any items required to complete the seed.'''
    options = [o for o in regular_checks]
    enabled = [o for o in regular_checks]

freestanding_checks = [
    ShuffleLocationSelector.BanditsWayCoin1,
    ShuffleLocationSelector.BanditsWayCoin2,
    ShuffleLocationSelector.BanditsWayCoin3,
    ShuffleLocationSelector.BarrelVolcanoReverse,
    ShuffleLocationSelector.BeanValleyBeanstalkCoin1,
    ShuffleLocationSelector.BeanValleyBeanstalkCoin2,
    ShuffleLocationSelector.BeanValleyBeanstalkCoin3,
    ShuffleLocationSelector.BeanValleyBeanstalkFrogCoin,
    ShuffleLocationSelector.BeanValleyEastBeanstalkCoin1,
    ShuffleLocationSelector.BeanValleyEastBeanstalkCoin2,
    ShuffleLocationSelector.BeanValleyEastBeanstalkCoin3,
    ShuffleLocationSelector.BeanValleyEastBeanstalkCoin4,
    ShuffleLocationSelector.BeanValleyEastBeanstalkCoin5,
    ShuffleLocationSelector.BeanValleyFirstVineRoomFrogCoin,
    ShuffleLocationSelector.BeanValleyFirstVineRoomLowerCoin,
    ShuffleLocationSelector.BeanValleyFirstVineRoomMiddleCoin,
    ShuffleLocationSelector.BeanValleyFirstVineRoomUpperCoin,
    ShuffleLocationSelector.BeanValleyWestBeanstalkCoin1,
    ShuffleLocationSelector.BeanValleyWestBeanstalkCoin2,
    ShuffleLocationSelector.BeanValleyWestBeanstalkCoin3,
    ShuffleLocationSelector.BeanValleyWestBeanstalkFrogCoin,
    ShuffleLocationSelector.BelomeTempleTreasureFlower1,
    ShuffleLocationSelector.BelomeTempleTreasureFlower2,
    ShuffleLocationSelector.BelomeTempleTreasureFlower3,
    ShuffleLocationSelector.BelomeTempleTreasureFlower4,
    ShuffleLocationSelector.BelomeTempleTreasureFrogCoin1,
    ShuffleLocationSelector.BelomeTempleTreasureFrogCoin2,
    ShuffleLocationSelector.BelomeTempleTreasureFrogCoin3,
    ShuffleLocationSelector.BelomeTempleTreasureFrogCoin4,
    ShuffleLocationSelector.BelomeTempleTreasureFrogCoin5,
    ShuffleLocationSelector.BelomeTempleTreasureFrogCoin6,
    ShuffleLocationSelector.BelomeTempleTreasureFrogCoin7,
    ShuffleLocationSelector.BelomeTempleTreasureFrogCoin8,
    ShuffleLocationSelector.BoosterPassBush,
    ShuffleLocationSelector.BoosterPassFlower,
    ShuffleLocationSelector.BoosterTowerCoin1,
    ShuffleLocationSelector.BoosterTowerCoin2,
    ShuffleLocationSelector.BoosterTowerCoin3,
    ShuffleLocationSelector.BoosterTowerCoin4,
    ShuffleLocationSelector.BoosterTowerCoin5,
    ShuffleLocationSelector.BoosterTowerCoin6,
    ShuffleLocationSelector.BoosterTowerCoin7,
    ShuffleLocationSelector.BoosterTowerCoin8,
    ShuffleLocationSelector.BoosterTowerCoin9,
    ShuffleLocationSelector.BoosterTowerFrogCoin1,
    ShuffleLocationSelector.BoosterTowerFrogCoin2,
    ShuffleLocationSelector.BoosterTowerFrogCoin3,
    ShuffleLocationSelector.BoosterTowerFrogCoin4,
    ShuffleLocationSelector.BoosterTowerParachuteCrevice,
    ShuffleLocationSelector.BowsersKeepCannonballRoomCoin1,
    ShuffleLocationSelector.BowsersKeepCannonballRoomCoin2,
    ShuffleLocationSelector.BowsersKeepCannonballRoomCoin3,
    ShuffleLocationSelector.BowsersKeepCannonballRoomCoin4,
    ShuffleLocationSelector.BowsersKeepCannonballRoomCoin5,
    ShuffleLocationSelector.BowsersKeepCannonballRoomCoin6,
    ShuffleLocationSelector.BowsersKeepCannonballRoomCoin7,
    ShuffleLocationSelector.BowsersKeepCannonballRoomCoin8,
    ShuffleLocationSelector.BowsersKeepInvisibleBridgeCoin1,
    ShuffleLocationSelector.BowsersKeepInvisibleBridgeCoin2,
    ShuffleLocationSelector.BowsersKeepInvisibleBridgeCoin3,
    ShuffleLocationSelector.BowsersKeepInvisibleBridgeCoin4,
    ShuffleLocationSelector.MidasRiverBottomLeftCave,
    ShuffleLocationSelector.MidasRiverBottomRightCave,
    ShuffleLocationSelector.MolevilleMinesShyGuy,
    ShuffleLocationSelector.PipeVaultSlideCoin1,
    ShuffleLocationSelector.PipeVaultSlideCoin2,
    ShuffleLocationSelector.PipeVaultSlideCoin3,
    ShuffleLocationSelector.PipeVaultSlideCoin4,
    ShuffleLocationSelector.PipeVaultSlideCoin5,
    ShuffleLocationSelector.PipeVaultSlideFrogCoin,
    ShuffleLocationSelector.RoseWayCoin1,
    ShuffleLocationSelector.RoseWayCoin2,
    ShuffleLocationSelector.RoseWayCoin3,
    ShuffleLocationSelector.RoseWayCoin4,
    ShuffleLocationSelector.RoseWayCoin5,
    ShuffleLocationSelector.RoseWayFlower,
    ShuffleLocationSelector.RoseWayMushroom,
    ShuffleLocationSelector.SunkenShip3DMaze,
    ShuffleLocationSelector.SunkenShipBarrelPuzzle,
    ShuffleLocationSelector.SunkenShipBlooberRoom,
    ShuffleLocationSelector.SunkenShipCannonballPuzzle,
    ShuffleLocationSelector.SunkenShipCoinSnake,
    ShuffleLocationSelector.SunkenShipRatStairsFlower,
    ShuffleLocationSelector.SunkenShipTrampolinePuzzle,
    ShuffleLocationSelector.SunkenShipTroopaPuzzle,
    ShuffleLocationSelector.SunkenShipUnderwaterFrogCoin1,
    ShuffleLocationSelector.SunkenShipUnderwaterFrogCoin2,
    ShuffleLocationSelector.SunkenShipUnderwaterFrogCoin3,
    ShuffleLocationSelector.SunkenShipUnderwaterFrogCoin4
]


class EnabledFreestandingChecks(CategorizationFlag):
    name = 'Freestanding coin/flower/mushroom checks'
    description = '''If a check is in the left column, it is eligible to contain items required to complete the seed.
    
    If a check is in the right column, it will not be shuffled, nor can it contain any items required to complete the seed.
    
    If item quality is set to "Completely empty", only checks on the left will be affected.'''
    options = [o for o in freestanding_checks]
    enabled = [o for o in freestanding_checks]

# ******** Shops


class ShuffleShops(BooleanFlag):
    name = 'Randomize the contents of shops'
    description = '''If enabled, the contents of all regular shops and Frog Coin shops, including the Moleville treasure shop, Marrymore Suite room service menu, and Moleville swap shop will be randomized.'''
    modes = ['open']
    default = False
# if this is disabled, no options in this category can be changed


class ShopQualities(enum.Enum):
    """Enumeration for shop shuffle quality option"""
    Original = "Original shop pool"
    Tier4 = "Completely random, unrestricted"
    Tier3 = "Completely random, exclude top-tier items"
    Tier2 = "Completely random, include some good items"
    Tier1 = "Completely random, bad items only"
    Empty = "Completely empty"


class ShopQuality(SelectOneFlag):
    name = '''Shop quality'''
    description = '''Restricts the incidence of certain items in shops. 

    "Completely random" means that some items which originally did not appear in shops may now appear in shops, but only a small pool of items are guaranteed to appear. Some items will never appear in non-depletable shops. 
    
    If "Completely empty" is selected, all shops will be disabled.'''
    modes = ['open']
    choices = [o for o in ShopQualities] # maybe just o for o
    default = ShopQualities.Original


class BiasShopShuffle(BooleanFlag):
    name = 'Bias better items to gated shops'
    description = '''If enabled, harder-to-reach shops will generally sell better items.'''
    modes = ['open']
    default = False


class FreeShops(BooleanFlag):
    name = "'Free' Shops"
    description = '''If enabled, all shop items will cost 1 coin. You will start with 9999 coins and 999 frog coins.'''
    modes = ['open']
    default = False

class ShowEquips(BooleanFlag):
    name = 'Show Equips'
    description = 'Always show who can equip what in stores.'
    inverse_description = '(Only current party members know what they can wear.)'
    value = '-showequips'

# ******** Enemies & Bosses


class BossShuffle(BooleanFlag):
    name = 'Randomize bosses'
    description = (
        "If enabled, the positions of bosses (including Pandorite, Hidon, Box Boy, Chester, and Mokura) are shuffled.")
    modes = ['open']
    default = False
    # if false, disable stat scaling and mimics anywhere


class BossShuffleScaleStats(BooleanFlag):
    name = "Scale boss stats to area difficulty"
    description = '''If enabled: A boss fight that has been shuffled into a different area will have its stats scaled to match the area's original boss.
    
    If disabled: Boss fights retain their original stats, regardless of where they are placed.'''
    default = True


class BossReplaceMinigameSprites(BooleanFlag):
    name = "Replace important NPCs to match shuffled bosses"
    description = '''If enabled: All sprites related to an area boss will be changed to match the shuffled positions of bosses. Battle packs, such as the Snifits in Booster Tower, will also be changed accordingly.
    
    If disabled: Most sprites related to an area boss will be changed to match the shuffled positions of bosses, but some will be left unchanged to accommodate for minigame visual cues. Examples of this include: Booster Hill snifits, Dodo in the statue polishing game.'''
    default = False

class MimicsAnywhere(BooleanFlag):
    name = 'Mimics can appear anywhere'
    description = '''If enabled, the three mimic chests could be in any chest in the world. Save often with this setting turned on, especially if item-hunting at the start of the seed.
    
    If disabled, they will remain in their original locations in Kero Sewers, Sunken Ship, and Bean Valley.'''
    modes = ['open']
    default = False


class EnemyStats(BooleanFlag):
    name = 'Randomize enemy stats'
    description = '''If enabled, enemy stats and immunities/weaknesses will be randomized.
    
    If disabled, enemies retain their original stats (subject to placement shuffling, if enabled), immunities, and vulnerabilities.'''
    default = False


class EnemyDrops(BooleanFlag):
    name = 'Randomize enemy drops'
    description = "If enabled, the EXP and in-battle items received from battles will be randomized."
    default = False


class EnemyFormations(BooleanFlag):
    name = 'Randomize formations'
    description = "If enabled, enemy encounters may contain random unexpected additional enemies and be laid out erratically. Boss formations are not affected."
    default = False


class EnemyAttacks(BooleanFlag):
    name = 'Randomize attacks'
    description = "If enabled, enemy spells and attacks will have their power randomized. Attacks which cast statuses will have the status effects randomized, and attacks which normally don't inflict statuses may inflict unexpected statuses."
    default = False


class EnemySpells(BooleanFlag):
    name = 'Randomize enemy spells'
    description = "If enabled, enemies can cast random spells. I.E. Mack could cast Blast instead of Flame."
    default = False
    hard = True
    modes = ['open']


class EnemyNoSafetyChecks(BooleanFlag):
    name = 'No safety checks'
    description = "If enabled, removes safety checks on enemy attack shuffle that prevent abnormally large effects."
    default = False
    hard = True


class ExperienceNoRegular(BooleanFlag):
    name = 'Remove EXP from enemy encounters'
    default = False
    hard = True


class ExperienceNoBosses(BooleanFlag):
    name = 'Remove EXP from boss encounters'
    default = False
    hard = True


class NoGenoWhirlExor(BooleanFlag):
    name = 'No Geno Whirl on Exor'
    description = 'Removes the Exor exploit where he is vulnerable to Geno Whirl when the eyes are stunned.'
    default = False


class FixMagikoopa(BooleanFlag):
    name = "Fix Magikoopa"
    description = 'Removes the Magikoopa oversight where he permanently skips turns after a King Bomb explosion.'
    default = False


class NoOHKO(BooleanFlag):
    name = "No instant KOs on boss allies"
    description = ('You will not be able to use Geno Whirl or Pure Water to OHKO any allies to a boss (Mallow Clone, '
                   'Mad Mallet, Fautso, etc).')
    default = False


class AvailableBosses(enum.Enum):
    HammerBro = "Hammer Bros"
    Mack = "Mack"
    Croco1 = "Croco 1"
    Pandorite = "Pandorite"
    Belome1 = "Belome 1"
    Bowyer = "Bowyer"
    Croco2 = "Croco 2"
    Punchinello = "Punchinello"
    Booster = "Booster"
    KnifeGuyGrateGuy = "Knife Guy & Grate Guy"
    Bundt = "Bundt"
    KingCalamari = "King Calamari"
    Hidon = "Hidon"
    Johnny = "Johnny"
    Yaridovich = "Yaridovich"
    Mokura = "Mokura"
    Belome2 = "Belome 2"
    Jagger = "Jagger"
    Jinx1 = "Jinx 1"
    Jinx2 = "Jinx 2"
    Jinx3 = "Jinx 3"
    Culex = "Culex"
    BoxBoy = "Box Boy"
    Megasmilax = "Megasmilax"
    Dodo = "Dodo"
    Birdetta = "Birdetta"
    Valentina = "Valentina"
    CzarDragon = "Czar Dragon"
    AxemRangers = "Axem Rangers"
    Chester = "Chester"
    Magikoopa = "Magikoopa"
    Boomer = "Boomer"
    Exor = "Exor"
    CountDown = "Count Down"
    CloakerDomino = "Cloaker & Domino"
    Clerk = "Clerk"
    Manager = "Manager"
    Director = "Director"
    Gunyolk = "Gunyolk & Factory Chief"
    Smithy = "Smithy"


class ShuffledBosses(CategorizationFlag):
    name = 'Shuffled boss fights'
    description = '''If a boss is in the left column, it will be shuffled into a pool and placed in a random boss location.
    
    If a boss is in the right column, it will stay in its original location.'''
    options = [o for o in AvailableBosses]
    enabled = [o for o in AvailableBosses]


# ******** Puzzles

class BallSolitaireShuffle(BooleanFlag):
    name = 'Randomize Ball Solitaire'
    description = 'The layout for the Ball Solitaire minigame will be randomized.'
    default = False


class MagicButtonShuffle(BooleanFlag):
    name = 'Randomize Magic Buttons'
    description = 'The layout for the Magic Buttons minigame will be randomized.'
    default = False


class QuizShuffle(BooleanFlag):
    name = 'Randomize Dr. Topper Quiz'
    description = 'The question pool for the Dr. Topper quiz will include new questions provided by the community.'
    default = False


class RandomTadpolePongSong(BooleanFlag):
    name = 'Randomize Tadpole Pond songs'
    description = '''If enabled, the songs required for the three Tadpole Pond songs will be selected from a random pool, submitted by players. Hints will be available in their normal locations within Tadpole Pond, Moleville Mines, and Monstro Town.'''
    modes = ['open']
    default = False


class RandomSunkenShipPassword(BooleanFlag):
    name = 'Randomize Sunken Ship password'
    description = '''If enabled, the password for the Sunken Ship will be changed. Hints are available in the 6 ship puzzles, and occasionally on posted notes within the Sunken Ship.'''
    modes = ['open']
    default = False


class BowserDoorShuffle(BooleanFlag):
    name = "Randomize Bowser\'s Keep room sequences"
    description = '''If enabled, the 18 rooms making up the six Bowser's Keep obstacle course doors will be shuffled into six random sequences of three rooms each.'''
    modes = ['open']
    default = False

# ******** Cosmetic


class BossShuffleMusic(BooleanFlag):
    name = 'Randomize boss music'
    description = 'Battle music will be randomized for each boss fight.'
    inverse_description = "(Battle music for each location will remain unchanged from the original game.)"
    value = 'Bm'

    # Add selector to remove certain songs from pool

class AvailableMusic(enum.Enum):
    Normal = "Regular encounter theme"
    Boss1 = "Midboss theme"
    Boss2 = "Smithy Gang theme"
    Smithy = "Smithy phase 1 theme"
    Culex = "Final Fantasy 4 boss theme"
    Corn = "Moleville Minecart theme"


class ShuffledMusic(CategorizationFlag):
    name = 'Allowable shuffled music'
    description = '''If a song is in the left column, it can appear in any boss fight.
    
    If a boss is in the right column, it will never appear in a boss fight.'''
    options = [o for o in AvailableMusic]
    enabled = [o for o in AvailableMusic]


class PaletteSwaps(BooleanFlag):
    name = 'Palette Swaps'
    description = 'Your party members get a change of wardrobe!'
    inverse_description = '(Sprite colours are not modified.)'
    value = '-palette'


# ************************************** Category classes

class FlagCategory:
    name = ''
    flags = []

class StarPiecesCategory(FlagCategory):
    name = 'Star Pieces'
    flags = [
        ShuffleStarPieces,
        TotalStarPieces,
        StarPiecesRequired,
        WinCondition,
        StarPieceAvailability,
        RequireBossFights,
        EnabledBossChecks,
        StarPiecesRestrictedByArea,
        StarPieceHints
    ]

class PartyCategory(FlagCategory):
    name = 'Party'
    flags = [
        ShuffleCharacters,
        StartingCharacters,
        StartingCharacter,
        AvailableCharacters,
        CharacterStats,
        CharacterLearnedSpells,
        CharacterSpellStats,
        EquipmentProperties,
        EquipmentCharacters,
        EquipmentNoSafety,
        EXPMultiplier
    ]

class AccessCategory(FlagCategory):
    name = 'Area Access'
    flags = [
        BanditsWayGate,
        ForestMazeGate,
        BoosterTowerGate,
        MarrymoreGate,
        SeaGate,
        YaridovichGate,
        MonstroTownGate,
        BarrelVolcanoGate,
        BowsersKeepGate,
        FactoryGate,
        CasinoWarp,
        BucketWarp,
        FastTravel,
        BowserDoorRequirements
    ]

class ItemsCategory(FlagCategory):
    name = 'Items'
    flags = [
        ShuffleItems,
        FireworksSetting,
        PoisonMushroom,
        ShuffleBeetlemania,
        ShuffleMagikoopaChest,
        KeyItemsAnywhere,
        RestrictSpecialEquips,
        EXPStarsAnywhere,
        EXPChallenge,
        SlotsAnywhere,
        ItemQuality,
        BetterTips, 
        BiasItemShuffle,
        ReplaceItems, 
        QuickHitCoins, 
        GrateGuyPrizeThreshold,
        KnifeGuyPrizeThreshold,
        SuitePrize1Threshold,
        SuitePrize2Threshold,
        SuitePrize3Threshold,
        SuitePrize4Threshold,
        SuitePrize5Threshold,
        SuitePrize6Threshold,
        SuperJump1Threshold,
        SuperJump2Threshold,
        EnabledRegularChecks,
        EnabledFreestandingChecks
    ]

class ShopsCategory(FlagCategory):
    name = 'Shops'
    flags = [
        ShuffleShops,
        ShopQuality,
        BiasShopShuffle,
        FreeShops
    ]

class BossCategory(FlagCategory):
    name = 'Enemies & Bosses'
    flags = [
        BossShuffle,
        BossShuffleScaleStats,
        BossReplaceMinigameSprites,
        MimicsAnywhere,
        EnemyStats,
        EnemyDrops,
        EnemyFormations,
        EnemyAttacks,
        EnemySpells,
        EnemyNoSafetyChecks,
        ExperienceNoRegular,
        ExperienceNoBosses,
        NoGenoWhirlExor,
        FixMagikoopa,
        NoOHKO,
        ShuffledBosses
    ]

class PuzzleCategory(FlagCategory):
    name = 'Puzzles'
    flags = [
        BallSolitaireShuffle,
        MagicButtonShuffle,
        QuizShuffle,
        RandomTadpolePongSong,
        RandomSunkenShipPassword,
        BowserDoorShuffle
    ]

class CosmeticCategory(FlagCategory):
    name = 'Cosmetics'
    flags = [
        BossShuffleMusic,
        ShuffledMusic,
        PaletteSwaps
    ]

# ************************************** Preset classes

# decide what to do with these later
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
    StarPiecesCategory,
    PartyCategory,
    AccessCategory,
    ItemsCategory,
    ShopsCategory,
    BossCategory,
    PuzzleCategory,
    CosmeticCategory
)

# List of presets.
PRESETS = (
    CasualPreset,
    IntermediatePreset,
    AdvancedPreset,
    ExpertPreset,
    QuickPreset,
)
