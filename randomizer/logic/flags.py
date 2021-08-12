# Flag definitions and logic.

import re
from django.utils.html import mark_safe
from markdown import markdown
from randomizer.data.helpers import ShuffleLocationSelector
from randomizer.data.bosses import AvailableBosses
from randomizer.data.helpers import FireworksOptions, WinConditions, PlayableCharacters, LearnableSpells, EquipmentPropertiesOptions, EXPMultiplierOptions, BanditsWayGating, ForestMazeGating, PipeVaultGating, BoosterTowerGating, MarrymoreGating, SeaGating, YaridovichGating, MonstroTownGating, BarrelVolcanoGating, BowsersKeepGating, FactoryGating, StarProgressionchallengeOptions, EXPChallengeOptions, ItemQualities, ShopQualities, AvailableMusic, EquipmentCharactersOptions


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

    def get_option_slug(self, option):
        return re.sub(r'[^a-z0-9]+', '_', option.lower())
        
        
    @classmethod
    def id(cls):
        return re.sub(r'[^a-z0-9]+', '_', cls.__name__.lower())

    @classmethod
    def get_slug(cls):
        return re.sub(r'[^a-z0-9]+', '_', cls.__name__.lower())

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

    @property
    def options_dict(self):
        return [{"text": c, "id": re.sub(r'[^a-z0-9]+', '_', c.lower())} for c in self.options]

    @property
    def default_dict(self):
        return [re.sub(r'[^a-z0-9]+', '_', c.lower()) for c in self.enabled]
        # this really should be coming from its enum


class SelectOneFlag(Flag):
    """For things like choosing an area gating option can and cannot contain progression"""
    type = "select_one"
    choices = []
    value = None

    @property
    def choices_dict(self):
        return [{"text": c, "id": re.sub(r'[^a-z0-9]+', '_', c.lower())} for c in self.choices]
        # this really should be coming from its enum

    @property
    def default_dict(self):
        return {"text": self.default.value, "id": re.sub(r'[^a-z0-9]+', '_', self.default.value)}
        # this really should be coming from its enum

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

# ******** Star Pieces


class ShuffleStarPieces(BooleanFlag):
    name = 'Randomize the locations of Star Pieces'
    description = '''If enabled, the Star Pieces may be found in places other than their original locations.
<br>
<br>If disabled, they will be rewarded by defeating the final bosses of Mushroom Kindom, Forest Maze, Moleville, Seaside Town, and Barrel Volcano, as well as a freestanding piece on Star Hill.'''
    modes = ['open']
    default = False
# if this is disabled, no other options in this category can be changed


class TotalStarPieces(NumberThresholdFlag):
    name = 'Total Star Pieces available'
    description = "The total number of Star Pieces (0-7) that can appear in the seed."
    default = 6
    min = 0
    max = 7
    modes = ['open']


class StarPiecesRequired(NumberThresholdFlag):
    name = 'Star Pieces required to access the final Factory boss'
    description = "The total number of Star Pieces (0-7) that are required to access the final boss. Cannot be higher than Total Star Pieces."
    default = 6
    min = 0
    max = 7
    modes = ['open']


class WinCondition(SelectOneFlag):
    name = "Condition required to beat the game"
    description = '''<b>Beat the Factory</b>: When you collect the number of Star Pieces specified in your Required Star Pieces setting, the button in the Inner Factory (as well as any enabled warps) will be enabled to allow you to access the final boss and beat the game.
<br>
<br><b>Collect required Star Pieces</b>: When you collect the number of Star Pieces specified in your Required Star Pieces setting, the game is over and the credits will roll.
<br>
<br><b>Beat Monstro Town sealed door</b>: The game is over when you defeat the boss behind the sealed door in Monstro Town, regardless of your Star Piece count.'''
    choices = [o.value for o in WinConditions]
    default = WinConditions.FinalBoss


class StarPieceAvailability(BooleanFlag):
    name = 'Star Pieces can appear in the general item pool'
    description = "If enabled, some Star Pieces may be shuffled in with items instead of being only granted by boss fights."
    modes = ['open']
    default = False


class RequireBossFights(BooleanFlag):
    name = 'Disable all boss fight skips'
    description = '''If set, the following actions will NOT grant you a Star Piece, and you must fight the associated boss in order to retrieve their Star Piece (if they have one):
<ul>
<li> Performing Mack Skip (the Chancellor will not advance the script)</li>
<li> Completing the Booster Tower curtain minigame (a copy of the boss will appear in the room corner)</li>
<li> Completing the Nimbus Castle statue minigame, or eliminating the boss in the final hallway with an EXP star (a copy of the boss will appear in the nearby save room)</li>
<li> Failing a Slot Machine chest and completing the forced mimic encounter (the mimic encounter is available on its own in a separate chest)</li>
</ul>
<br/>If unset, the above actions will grant you a Star Piece if one is assigned to the associated boss. Each boss' Star Piece can only be obtained once.'''
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
    name = 'Eligible Star Piece boss fight locations'
    description = '''If a check is highlighted (white text over blue), it is eligible to reward a Star Piece.
<br>
<br>If a check is not highlighted, it will still house a boss fight, but is guaranteed to not reward a Star Piece.'''
    options = [o.value for o in boss_star_piece_locations]
    enabled = [o.value for o in boss_star_piece_locations]


class StarPiecesRestrictedByArea(BooleanFlag):
    name = 'Restrict number of Star Pieces in a World Map area'
    description = '''If enabled, each of the seven overworld map areas may only contain up to one Star Piece each.
<br>
<br>Note: This may not be perfectly respected if Bowser's Keep and Factory are both gated by high Star Piece counts.'''
    modes = ['open']
    default = False


class StarPieceHints(BooleanFlag):
    name = 'Signal Ring Star Piece hints'
    description = '''If enabled, the Signal Ring (if equipped to your active party) will play a sound when you enter a world area that contains a Star Piece.  
<br>
<br>The Signal Ring will only sound off when you enter an area from the World Map, from loading a save, or from an area warp (ex: the Kero Sewers - Land's End pipe). Therefore, the chime does not necessarily indicate that your current room contains a Star Piece, but rather that at least one room in the area does.'''
    modes = ['open']
    default = False

# ******** Party


class ShuffleCharacters(BooleanFlag):
    name = 'Randomize the locations of recruited characters'
    description = '''If enabled, your characters will join your party in a random order.
<br>
<br>If disabled, you will start with Mario and recruit characters near their original locations.'''
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



class StartingCharacter(SelectOneFlag):
    name = "Starting Character"
    description = '''The first character in your party, who will appear on your save menu.'''
    choices = [o.value for o in PlayableCharacters]
    default = PlayableCharacters.Mario


class AvailableCharacters(CategorizationFlag):
    name = "Available Characters"
    description = '''If a character is highlighted (white text over blue), they will appear in the seed. Otherwise, they will not.'''
    options = [o.value for o in PlayableCharacters if o != PlayableCharacters.Random]
    enabled = [o.value for o in PlayableCharacters if o != PlayableCharacters.Random]


class CharacterStats(BooleanFlag):
    name = 'Randomize character stats'
    description = '''If enabled, stats and stat curves for each playable character will be randomized. This also randomizes the number of FP you start with.
<br>
<br>If disabled, playable characters retain their original stats and stat curves.'''
    default = False


class AvailableSpells(CategorizationFlag):
    name = "Available Player Spells"
    description = '''Highlighted (white text over blue) spells will be learned by at least one character. Spells that are not highlighted will not be learned by any character.
<br>
<br>Excluded spells are not replaced in characters' learnsets by other spells, so some characters will learn less than six total.
<br>
<br>Note: Excluding "Super Jump" may make some equips inaccessible depending on your other settings.'''
    options = [o.value for o in LearnableSpells]
    enabled =  [o.value for o in LearnableSpells]


class CharacterLearnedSpells(BooleanFlag):
    name = 'Randomize character learned spells'
    description = "The pool of spells learnable by each character will be randomized. This only covers spells originally learn-able by playable characters, and does not include enemy spells."
    default = False

class UncapSuperJumps(BooleanFlag):
    name = 'Uncap Super Jumps'
    description = "If enabled, you can do more than 100 Super Jumps at once."
    default = False
    # this needs testing


class CharacterSpellStats(BooleanFlag):
    name = 'Randomize character spell stats'
    description = "The power and FP cost of character magic spells will be randomized."
    default = False


class EquipmentProperties(SelectOneFlag):
    name = 'Equipment stats & buffs'
    description = '''<b>Default</b>: The stats and buffs on equipment are unchanged from the original game.
<br>
<br><b>Some buffs added</b>: The stats and buffs on equipment are mostly unchanged from the original game, except most armors are given one additional property (e.g. Fire Shirt nullifies damage from fire attacks). Additionally, some weapons will boost magic attack instead of physical attack.
<br>
<br><b>Completely random</b>: The stats and buffs on each piece of equipment is randomized.'''
    choices = [o.value for o in EquipmentPropertiesOptions]
    default = EquipmentPropertiesOptions.default


class EquipmentCharacters(SelectOneFlag):
    name = 'Equipment permissions'
    description = '''<b>Vanilla</b>: The list of characters who are permitted to equip each item remains unchanged from the original game.
<br>
<br><b>Vanilla, except anyone can wear any accessory</b>: Armor and weapon permissions are unchanged from the original game, but all accessories (including the Attack Scarf) can be equipped by anyone.
<br>
<br><b>Random, except anyone can wear any accessory</b>: Armor and weapon permissions are randomized, but all accessories can be equipped by anyone.
<br>
<br><b>Completely random</b>: All equips' permissions are randomized.'''
    default = False
    choices = [o.value for o in EquipmentCharactersOptions]
    default = EquipmentCharactersOptions.Default


class EquipmentNoSafety(BooleanFlag):
    name = 'No OHKO Safety'
    description = "If enabled, no equipment will protect against OHKO moves."
    default = False


class EXPMultiplier(SelectOneFlag):
    name = 'EXP multiplier'
    description = '''If not set to "Default", all EXP gained will be doubled or tripled.'''
    choices = [o.value for o in EXPMultiplierOptions]
    default = EXPMultiplierOptions.default


# ******** Area Access


class BanditsWayGate(SelectOneFlag):
    name = '''Bandit's Way access'''
    description = '''<b>Recruit character</b>: Bandit's Way will become available on the world map when you recruit the selected character.
<br>
<br><b>Finish Mushroom Way</b>: Bandit's Way will become available on the world map when you defeat the boss of Mushroom Way.
<br>
<br><b>Always Open</b>: Bandit's Way will be available on the world map from the start of the game.'''
    modes = ['open']
    choices = [o.value for o in BanditsWayGating]
    default = BanditsWayGating.RecruitMallow


class ForestMazeGate(SelectOneFlag):
    name = '''Forest Maze access'''
    description = '''<b>Find character</b>: Forest Maze will become available on the world map when you first see the selected character. "See" does not necessarily mean "recruit".
<br>
<br><b>Exchange Cricket Pie</b>: Forest Maze will become available on the world map when you turn in the Cricket Pie to Frogfucius.
<br>
<br><b>Always Open</b>: Forest Maze will be available on the world map from the start of the game.'''
    modes = ['open']
    choices = [o.value for o in ForestMazeGating]
    default = ForestMazeGating.FindGeno


class PipeVaultGate(SelectOneFlag):
    name = '''Pipe Vault access'''
    description = '''<b>Recruit character</b>: Pipe Vault will be unblocked when you recruit the selected character.
<br>
<br><b>Finish Forest Maze</b>: Pipe Vault will be unblocked when you defeat the final boss of Forest Maze.
<br>
<br><b>Always Open</b>: Pipe Vault will be unblocked from the start of the game.'''
    modes = ['open']
    choices = [o.value for o in PipeVaultGating]
    default = PipeVaultGating.AlwaysOpen


class BoosterTowerGate(SelectOneFlag):
    name = '''Booster Tower access'''
    description = '''<b>Recruit character</b>: Booster Tower's door can be unlocked when you recruit the selected character.
<br>
<br><b>Finish Moleville</b>: Booster Tower's door will unlock when you defeat the final boss of Moleville.
<br>
<br><b>Always Open</b>: Booster Tower's door will be unlocked from the start of the game.'''
    modes = ['open']
    choices = [o.value for o in BoosterTowerGating]
    default = BoosterTowerGating.RecruitBowser


class MarrymoreGate(SelectOneFlag):
    name = '''Marrymore back door access'''
    description = '''<b>Finish Booster Hill</b>: The chapel back door will become available on the world map when you complete Booster Hill one time.
<br>
<br><b>Finish Booster Tower</b>: The chapel back door will become available on the world map when you defeat the balcony boss of Booster Tower.
<br>
<br><b>Always Open</b>: The chapel back door will be open from the start of the game.'''
    modes = ['open']
    choices = [o.value for o in MarrymoreGating]
    default = MarrymoreGating.FinishBoosterHill


class SeaGate(SelectOneFlag):
    name = '''Sea & Sunken Ship access'''
    description = '''<b>Recruit character</b>: The Sea will become available on the world map when you recruit the selected character.
<br>
<br><b>Collect Star Pieces</b>: The Sea will become available on the world map when you collect the selected number of Star Pieces.
<br>
<br><b>Always Open</b>: The Sea & Sunken Ship will be available on the world map from the start of the game.'''
    modes = ['open']
    choices = [o.value for o in SeaGating]
    default = SeaGating.Find4Star


class YaridovichGate(SelectOneFlag):
    name = '''Seaside boss fight access'''
    description = '''<b>Finish Sunken Ship</b>: The Seaside boss fight will become available after you defeat the final boss of Sunken Ship.
<br>
<br><b>Always Open</b>: The Seaside boss will be available from the start of the game.'''
    modes = ['open']
    choices = [o.value for o in YaridovichGating]
    default = YaridovichGating.FinishSunkenShip


class MonstroTownGate(SelectOneFlag):
    name = '''Monstro Town access'''
    description = '''<b>Finish Land's End</b>: Monstro Town will become available on the World Map once you take the pipe behind the boss of Belome Temple.
<br>
<br><b>Always Open</b>: Monstro Town will be available on the World Map from the start of the game.'''
    modes = ['open']
    choices = [o.value for o in MonstroTownGating]
    default = MonstroTownGating.FinishLandsEnd


class BarrelVolcanoGate(SelectOneFlag):
    name = '''Barrel Volcano access'''
    description = '''<b>Finish Nimbus Land</b>: Barrel Volcano will become available on the World Map once you defeat the final boss of Nimbus Castle.
<br>
<br><b>Always Open</b>: Barrel Volcano will be available on the World Map from the start of the game.'''
    modes = ['open']
    choices = [o.value for o in BarrelVolcanoGating]
    default = BarrelVolcanoGating.FinishNimbusLand

class BowsersKeepGate(SelectOneFlag):
    name = '''Bowser's Keep access'''
    description = '''<b>Collect Star Pieces</b>: Bowser's Keep will become available on the world map when you collect the selected number of Star Pieces.
<br>
<br><b>Finish Barrel Volcano</b>: Bowser's Keep will become available on the World Map once you defeat the final boss of Barrel Volcano.
<br>
<br><b>Always Open</b>: Bowser's Keep will be available on the world map from the start of the game.'''
    modes = ['open']
    choices = [o.value for o in BowsersKeepGating]
    default = BowsersKeepGating.Find6Star


class FactoryGate(SelectOneFlag):
    name = '''Factory access'''
    description = '''<b>Open when Bowser's Keep is opened</b>: When Bowser's Keep becomes available on the world map, Factory will also be immediately available on the world map.
<br>
<br><b>Finish Bowser's Keep</b>: Factory will become available on the world map when you complete Bowser's Keep for the first time.
<br>
<br><b>Collect Star Pieces</b>: Factory will become available on the world map when you collect the selected number of Star Pieces and Bowser's Keep has been opened. Cannot be higher than 'Star Pieces required to beat the game'.'''
    modes = ['open']
    choices = [o.value for o in FactoryGating]
    default = FactoryGating.FinishBowsersKeep


class CasinoWarp(BooleanFlag):
    name = 'Casino Warp'
    description = "If enabled, a trampoline warping directly to the final boss will become available in Grate Guy's Casino once you have collected the number of Star Pieces specified in 'Star Pieces required to beat the game'. The Bright Card becomes a key item, and Knife Guy's juggling reward becomes a key item check."
    modes = ['open']
    default = False


class BucketWarp(BooleanFlag):
    name = 'Bucket Warp'
    description = "If enabled, trading a Carbo Cookie to the bucket girl in Moleville will reveal a warp to the final boss once you have collected the number of Star Pieces specified in 'Star Pieces required to beat the game'."
    modes = ['open']
    default = False


class FastTravel(BooleanFlag):
    name = 'Fast travel'
    description = '''If enabled, the following changes will be applied to the game:
<ol>
<li>Traveling to the top of Booster Tower after defeating the balcony boss will always warp you to the ground.</li>
<li>Reaching the Inner Factory will reveal a trampoline that warps you to the world map.</li>
<li>Reaching the Inner Factory will enable a world map shortcut that places you in Inner Factory.</li>
</ol>'''
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
    name = 'Randomize the contents of treasure chests and item rewards'
    description = '''If enabled, the contents of treasure chests, quest rewards, and (optionally) freestanding small items will be shuffled.
<br>
<br>If disabled, chests, quest rewards, and freestanding small items will remain unchanged from the original game.'''
    modes = ['open']
    default = False
# if this is disabled, no options in this category can be changed


class FireworksSetting(SelectOneFlag):
    name = '''Fireworks trade sequence'''
    description = '''<b>Vanilla</b>: Unchanged from the original game. Fireworks may be purchased in any amount from the Moleville house after completing the Mines.
<br>
<br><b>Shuffle Fireworks</b>: One Fireworks is shuffled somewhere in the game. The trading sequence is otherwise unchanged. If needed, you may get your Shiny Stone back from the shop girl after you have completed the trade sequence.
<br>
<br><b>Shuffle Progressive Fireworks</b>: One Fireworks, Shiny Stone, and Carbo Cookie are each shuffled somewhere in the game, and you will always receive them in order. The Monstro Town sealed door is unlocked when you find the Shiny Stone.
<br>
<br>Note: If you do not have Bucket Warp enabled, completing the Carbo Cookie trade sequence will give you a random item if "Shuffle Fireworks" or "Shuffle Progressive Fireworks" is selected.'''
    modes = ['open']
    choices = [o.value for o in FireworksOptions]
    default = FireworksOptions.Vanilla


class PoisonMushroom(BooleanFlag):
    name = 'Change Fake Mushroom\'s Effect'
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
<br>
<br>If disabled, the "Special Items" will only be shuffled within each other's locations.
<br>
<br>The items targeted by this setting are the <b>Rare Frog Coin</b>, <b>Cricket Pie</b>, <b>Bambino Bomb</b>, <b>Castle Key 1</b>, <b>Castle Key 2</b>, <b>Alto Card</b>, <b>Tenor Card</b>, <b>Soprano Card</b>, <b>Greaper Flag</b>, <b>Dry Bones Flag</b>, <b>Big Boo Flag</b>, <b>Shed Key</b>, <b>Elder Key</b>, <b>Cricket Jam</b>, <b>Temple Key</b>, <b>Room Key</b>, <b>Seed</b>, and <b>Fertilizer</b> (and sometimes <b>Bright Card</b> and <b>Fireworks</b>).'''
    modes = ['open']
    default = False


class InvisibleFlagsSetting(BooleanFlag):
    name = 'Move invisible flag checks'
    description = '''Chooses where the invisible items placed by the Three Musty Fears are located. 
<br>
<br>If "Default locations" is selected, these checks will remain in their default locations (Mario's Pad bed, Rose Town sign, Yo'ster Isle goalpost).
<br>
<br>If enabled, the three checks will be located somewhere random in the world as an invisible item. The Three Musty Fears will give you hints as to their locations. The three default item locations will be disabled.'''
    modes = ['open']
    default = False


class GateInvisibleFlags(BooleanFlag):
    name = 'Skip 3 Musty Fears sequence'
    description = '''This flag affects the Musty Fears checks (normally Mario's Pad bed, Rose Town sign, and Yo'ster Isle goalpost; or whichever three locations are added to the seed when "Move invisible flag checks" is set to "Any landmark").
<br>
<br>If disabled, the affected checks will become available after you visit the Musty Fears Inn in Monstro Town.
<br>
<br>If enabled, the affected checks will be available from the start of the seed.'''
    modes = ['open']
    default = False


class RestrictSpecialEquips(BooleanFlag):
    name = 'Restrict key item exchange equips & Monstro Town reward equips'
    description = '''If enabled, the FroggieStick, Chomp, Zoom Shoes, Attack Scarf, Super Suit, Quartz Charm, Jinx Belt, Ghost Medal, and both Lazy Shells will appear once each, shuffled only within each other's locations. This option ignores your chosen Item Quality setting.
<br>
<br>If disabled, these items can appear anywhere, subject to the restrictions of your chosen Item Quality setting.'''
    modes = ['open']
    default = False


class EXPStarsAnywhere(BooleanFlag):
    name = 'EXP stars can appear anywhere'
    description = '''If enabled, EXP stars may appear in any chest near monsters.
<br>
<br>If disabled, EXP stars will be restricted to their original locations within Bandit's Way, Kero Sewers, Moleville Mines, Sea, Land's End, Nimbus Land, and Barrel Volcano.'''
    modes = ['open']
    default = False


class EXPChallenge(SelectOneFlag):
    name = 'EXP Star Behaviour'
    description = '''<b>Default</b>: EXP stars can give you 1 to 11 EXP per hit as normal.
<br>
<br><b>Star Pieces (easy)</b>: EXP stars can give you 2, 4, 5, 6, 8, 9, or 11 EXP per hit, based on the number of Star Pieces collected. This is not adjusted for lower max Star Piece counts.
<br>
<br><b>Star Pieces (hard)</b>: EXP stars can give you 1, 2, 3, 5, 6, 7, or 11 EXP per hit, based on the number of Star Pieces collected. This is not adjusted for lower max Star Piece counts.
<br>
<br><b>Bosses (easy)</b>: EXP stars can give you 2, 4, 5, 6, 8, 9, or 11 EXP depending on how many bosses you have defeated. The scaling for this option is heavily front-loaded.
<br>
<br><b>Bosses (hard)</b>: EXP stars can give you 1, 2, 3, 5, 6, 7, or 11 EXP depending on how many bosses you have defeated. The scaling for this option is heavily front-loaded.
<br>
<br><b>No EXP</b>: EXP stars give you 0 EXP.'''
    choices = [o.value for o in EXPChallengeOptions]
    default = EXPChallengeOptions.default


class SlotsAnywhere(BooleanFlag):
    name = 'Slot machines can appear anywhere'
    description = '''If enabled, any chest in the world could contain a slot machine.
<br>
<br>If disabled, slot machines will be restricted to their original locations in Bean Valley.
<br>
<br>Note that a bad roll on a slot machine will initiate a duplicate of the third mimic chest fight.'''
    modes = ['open']
    default = False


class ItemQuality(SelectOneFlag):
    name = '''Item pool quality'''
    description = '''Restricts the incidence of certain items within the shuffled pool. 
<br>
<br>If "Original item pool" is selected, items which only appear once in the original game will also not appear in unlimited shops. Additionally, two copies of the progressive Mystery Egg will be added to the pool, replacing some small items.
<br>
<br>If "Completely empty" is selected, any chest which does not contain a required item will be a "You Missed" chest.'''
    modes = ['open']
    choices = [o.value for o in ItemQualities]
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
    description = '''If a check is highlighted (white text over blue), it is eligible to contain items required to complete the seed.
<br>
<br>If a check is not highlighted, its contents will still be shuffled, but it will not contain any items required to complete the seed.
<br>
<br>This setting only applies if you have "Special Items can appear anywhere" or "Star Pieces can appear in the general item pool" enabled.'''
    options = [o.value for o in regular_checks]
    enabled = [o.value for o in regular_checks]


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
    description = '''If a check is highlighted (white text over blue), it is eligible to contain items required to complete the seed.
<br>
<br>If a check is not highlighted, it will not be shuffled, nor can it contain any items required to complete the seed.
<br>
<br>If item quality is set to "Completely empty", only highlighted checks will be affected.'''
    options = [o.value for o in freestanding_checks]

# ******** Shops


class ShuffleShops(BooleanFlag):
    name = 'Randomize the contents of shops'
    description = '''If enabled, the contents of all regular shops and Frog Coin shops (including the Moleville treasure shop, Marrymore Suite room service menu, and Moleville swap shop) will be randomized.'''
    modes = ['open']
    default = False
# if this is disabled, no options in this category can be changed


class ShopQuality(SelectOneFlag):
    name = '''Shop contents quality'''
    description = '''Restricts the incidence of certain items in shops. 
<br>
<br>"Completely random" means that some items which originally did not appear in shops may now appear in shops, but only a small pool of items are guaranteed to appear. Some items will never appear in non-depletable shops. 
<br>
<br>If "Completely empty" is selected, all shops will be disabled.'''
    modes = ['open']
    choices = [o.value for o in ShopQualities]  # maybe just o for o
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
    name = 'Always show all permitted characters on equips'
    description = 'Always show who can equip what in stores.'
    default = False

# ******** Enemies & Bosses


class BossShuffle(BooleanFlag):
    name = 'Randomize boss positions'
    description = (
        "If enabled, the positions of bosses (including Pandorite, Hidon, Box Boy, Chester, and Mokura) are shuffled.")
    modes = ['open']
    default = False
    # if false, disable stat scaling and mimics anywhere


class BossShuffleScaleStats(BooleanFlag):
    name = "Scale boss stats to area difficulty"
    description = '''If enabled: A boss fight that has been shuffled into a different area will have its stats scaled to match the area's original boss.
<br>
<br>If disabled: Boss fights retain their original stats, regardless of where they are placed.'''
    default = True


class BossReplaceMinigameSprites(BooleanFlag):
    name = "Replace important NPCs to match shuffled bosses"
    description = '''If enabled: All sprites related to an area boss will be changed to match the shuffled positions of bosses.
<br>
<br>If disabled: Some sprites will be left unchanged from the original game to accommodate visual cues (such as the Booster Hill snifits, or Dodo in his statue room) or progression knowledge on required sub-fights (such as the Bandana Reds in Sunken Ship).'''
    default = False


class MimicsAnywhere(BooleanFlag):
    name = 'Mimics can appear anywhere'
    description = '''If enabled, the three mimics could be in any chest in the world. If you have "Scale boss stats to area difficulty" enabled, each mimic will be restricted to areas that are appropriate for its stats. However you should save often with this setting turned on, especially if item-hunting at the start of the seed.
<br>
<br>If disabled, mimic chests will remain in their original locations in Kero Sewers, Sunken Ship, and Bean Valley.'''
    modes = ['open']
    default = False


class EnemyStats(BooleanFlag):
    name = 'Randomize enemy stats'
    description = '''If enabled, enemy stats and immunities/weaknesses will be randomized.
<br>
<br>If disabled, enemies retain their original stats (subject to placement shuffling, if enabled), immunities, and vulnerabilities.'''
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


class ShuffledBosses(CategorizationFlag):
    name = 'Shuffled boss fights'
    description = '''If a boss is highlighted (white text over blue), it will be shuffled into a pool and placed in a random boss location.
<br>
<br>If a boss is not highlighted, it will stay in its original location.'''
    options = [o.value for o in AvailableBosses]
    enabled = [o.value for o in AvailableBosses]


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


class RandomTadpolePondSong(BooleanFlag):
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


class SkipMinecart(BooleanFlag):
    name = "Skip Minecart minigame"
    description = '''If enabled, boarding the minecart for the first time will teleport you back to Moleville. Subsequent visits to the minecart room will play the minigame as normal.'''
    modes = ['open']
    default = False

# ******** Cosmetic


class BossShuffleMusic(BooleanFlag):
    name = 'Randomize boss music'
    description = 'Battle music will be randomized for each boss fight.'
    inverse_description = "(Battle music for each location will remain unchanged from the original game.)"
    value = 'Bm'

    # Add selector to remove certain songs from pool


class ShuffledMusic(CategorizationFlag):
    name = 'Allowable shuffled music'
    description = '''If a song is highlighted (white text over blue), it can appear in any boss fight.
<br>
<br>If a song is not highlighted, it will never appear in a boss fight.'''
    options = [o.value for o in AvailableMusic]
    enabled = [o.value for o in AvailableMusic]


class PaletteSwaps(BooleanFlag):
    name = 'Palette Swaps'
    description = 'Your party members get a change of wardrobe!'
    inverse_description = '(Sprite colours are not modified.)'
    value = '-palette'


class ChangeNames(BooleanFlag):  # not available unless PaletteSwaps enabled
    name = 'Change character names'
    description = '''Some palette swaps are references to other media. If this flag is enabled, the character's name will be changed to match the palette.'''
    inverse_description = '(Sprite colours are not modified.)'
    value = '-palette'

class RemoveFlashes(BooleanFlag):
    name = "Remove flashes"
    description = '''Removes some flashing animations (from spells, attacks, etc). 
<br>
<br>Disclaimer: While this feature is intended to promote accessibility, developers cannot promise that every feature in the game with screen flashes has had them removed. Players and viewers with photosensitivity should continue to engage with this randomizer at their own risk. 
<br>
<br>If you would like to suggest an animation that should have flashes removed by this feature, please see the "Contributing" section and fill out the form.'''


# ************************************** Category classes

class FlagCategory:
    name = ''
    subcategories = []
    flags = []
    size = 3


    @classmethod
    def get_slug(cls):
        return re.sub(r'[^a-z0-9]+', '_', cls.name.lower())
    


class CharacterRecruitmentSubcategory(FlagCategory):
    flags = [
        StartingCharacters,
        StartingCharacter,
        ShuffleCharacters,
        AvailableCharacters,
    ]
    size = 4

class CharacterStatsSpellsSubcategory(FlagCategory):
    flags = [
        EXPMultiplier,
        CharacterStats,
        CharacterLearnedSpells,
        CharacterSpellStats,
        UncapSuperJumps,
        AvailableSpells
    ]
    size = 4

class CharacterEquipmentSubcategory(FlagCategory):
    flags = [
        EquipmentProperties,
        EquipmentCharacters,
        EquipmentNoSafety,
        StarPieceHints
    ]
    size = 4


class PartyCategory(FlagCategory):
    name = 'Party & Equipment'
    subcategories = [
        CharacterRecruitmentSubcategory,
        CharacterEquipmentSubcategory,
        CharacterStatsSpellsSubcategory
    ]

class AreaAccessSubcategory(FlagCategory):
    flags = [
        BanditsWayGate,
        ForestMazeGate,
        PipeVaultGate,
        BoosterTowerGate,
        MarrymoreGate,
        SeaGate,
        MonstroTownGate,
        BarrelVolcanoGate,
    ]
    size = 3

class OtherAccessSubcategory(FlagCategory):
    flags = [
        YaridovichGate,
        GateInvisibleFlags,
        BowsersKeepGate,
        BowserDoorRequirements,
        FactoryGate,
        StarPiecesRequired,
        CasinoWarp,
        BucketWarp,
        FastTravel,
        WinCondition,
    ]
    size = 3


class PuzzleCategory(FlagCategory):
    name = 'Puzzles & Minigames'
    flags = [
        BallSolitaireShuffle,
        MagicButtonShuffle,
        QuizShuffle,
        RandomTadpolePondSong,
        RandomSunkenShipPassword,
        BowserDoorShuffle,
        SkipMinecart
    ]
    size = 3


class ShopsCategory(FlagCategory):
    flags = [
        ShuffleShops,
        ShopQuality,
        BiasShopShuffle,
        ShowEquips,
        FreeShops
    ]
    size = 3

class AccessCategory(FlagCategory):
    name = 'Progression & Shops'
    subcategories=[AreaAccessSubcategory, OtherAccessSubcategory, PuzzleCategory, ShopsCategory]


class StarPiecesCategory(FlagCategory):
    flags = [
        ShuffleStarPieces,
        TotalStarPieces,
        EnabledBossChecks,
    ]
    size = 3

class ItemLocationSubcategory(FlagCategory):
    flags = [
        ShuffleItems,
        ItemQuality,
        BiasItemShuffle,
        RestrictSpecialEquips,
        StarPiecesRestrictedByArea,
        BetterTips,
        EXPStarsAnywhere,
        SlotsAnywhere,
        ShuffleBeetlemania,
        ShuffleMagikoopaChest,
        FireworksSetting,
    ]

class QualitySubcategory(FlagCategory):
    flags = [
        InvisibleFlagsSetting,
        ReplaceItems,
        QuickHitCoins,
        PoisonMushroom,
        EXPChallenge,
        GrateGuyPrizeThreshold,
        KnifeGuyPrizeThreshold,
        SuitePrize1Threshold,
        SuitePrize2Threshold,
        SuitePrize3Threshold,
        SuitePrize4Threshold,
        SuitePrize5Threshold,
        SuitePrize6Threshold,
        SuperJump1Threshold,
        SuperJump2Threshold
    ]

class ItemCheckSubcategory(FlagCategory):
    flags = [
        KeyItemsAnywhere,
        StarPieceAvailability,
        EnabledRegularChecks,
        EnabledFreestandingChecks
    ]



class ItemsCategory(FlagCategory):
    name = 'Items & Star Pieces'
    subcategories = [
        StarPiecesCategory,
        ItemLocationSubcategory,
        ItemCheckSubcategory,
        QualitySubcategory
    ]

class BossPositionSubcategory(FlagCategory):
    flags = [
        BossShuffle,
        BossShuffleScaleStats,
        BossReplaceMinigameSprites,
        MimicsAnywhere,
    ]
    size = 3

class BossCheeseSubcategory(FlagCategory):
    flags = [
        RequireBossFights,
        NoGenoWhirlExor,
        FixMagikoopa,
        NoOHKO,
    ]
    size = 3

class BossStatSubcategory(FlagCategory):
    flags = [
        EnemyStats,
        EnemyDrops,
        EnemyFormations,
        EnemyAttacks,
        EnemyNoSafetyChecks,
        EnemySpells,
        ExperienceNoRegular,
        ExperienceNoBosses,
    ]
    size = 3

class AvailableBossesSubcategory(FlagCategory):
    flags = [
        ShuffledBosses
    ]
    size = 3


class BossCategory(FlagCategory):
    name = 'Enemies & Boss Fights'
    subcategories = [
        BossPositionSubcategory,
        AvailableBossesSubcategory,
        BossStatSubcategory,
        BossCheeseSubcategory
    ]

class AccessibilitySubcategory(FlagCategory):
    flags = [
        RemoveFlashes
    ]
    size = 4

class MusicSubcategory(FlagCategory):
    flags = [
        BossShuffleMusic,
        ShuffledMusic,
    ]
    size = 4

class PaletteSubcategory(FlagCategory):
    flags = [
        PaletteSwaps,
        ChangeNames,
    ]
    size = 4


class CosmeticCategory(FlagCategory):
    name = 'Cosmetics'
    subcategories = [
        PaletteSubcategory,
        MusicSubcategory,
        AccessibilitySubcategory
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
    PartyCategory,
    ItemsCategory,
    AccessCategory,
    BossCategory,
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
