# Flag definitions and logic.

import re
from django.utils.html import mark_safe
from markdown import markdown
from randomizer.data.helpers import ShuffleLocationSelector
from randomizer.data.bosses import AvailableBosses
from randomizer.data.helpers import FireworksOptions, WinConditions, PlayableCharacters, LearnableSpells, EquipmentPropertiesOptions, EXPMultiplierOptions, BanditsWayGating, ForestMazeGating, PipeVaultGating, BoosterTowerGating, MarrymoreGating, SeaGating, YaridovichGating, MonstroTownGating, BarrelVolcanoGating, BowsersKeepGating, FactoryGating, EXPChallengeOptions, ItemQualities, ShopQualities, AvailableMusic, EquipmentCharactersOptions, regular_checks, freestanding_checks


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
    id = ""
    requires_all = []
    requires_any = []

    # @classmethod
    # def id(cls):
    #     return cls.__name__
    # return cls.description_or_name_as_markdown

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
    optionEnum = None

    @property
    def options_dict(self):
        return [{"id": c.name, "text": c.value} for c in self.options]

    @property
    def default_dict(self):
        return [{"id": c.name, "text": c.value} for c in self.enabled]
        # this really should be coming from its enum


class SelectOneFlag(Flag):
    """For things like choosing an area gating option can and cannot contain progression"""
    type = "select_one"
    choices = []
    value = None
    optionEnum = None

    @property
    def choices_dict(self):
        return [{"id": c.name, "text": c.value} for c in self.choices]
        # this really should be coming from its enum

    @property
    def default_dict(self):
        return {"text": self.default.value, "id": self.default.name}
        # this really should be coming from its enum


class BooleanFlag(Flag):
    """For settings which can only be on or off"""
    type = "boolean"
    value = False
    default = False
    


class NumberThresholdFlag(Flag):
    """For settings which require a number from a range"""
    type = "number"
    min = 0
    max = 0
    value = 0


# ******** Party


class StartingCharacters(NumberThresholdFlag):
    # remember to set switch bit if > 3
    name = 'Starting party size'
    description = "The number of characters you will have already recruited at the start of the seed, including your starter."
    default = 1
    min = 1
    max = 5
    modes = ['open']
    id = "size"


class StartingCharacter(SelectOneFlag):
    name = "Starting Character"
    description = '''The first character in your party, who will appear on your save menu.'''
    optionEnum = PlayableCharacters
    choices = [o for o in PlayableCharacters]
    default = PlayableCharacters.mario
    id = "start"


class ShuffleCharacters(BooleanFlag):
    name = 'Randomize the locations of recruited characters'
    description = '''If enabled, your characters will join your party in a random order.
<br>
<br>If disabled, you will start with Mario and recruit characters near their original locations.'''
    modes = ['open']
    
    id = "random"
# if this is disabled, no starting/available options in this category can be changed


class AvailableCharacters(CategorizationFlag):
    name = "Available Characters"
    description = '''If a character is highlighted (white text over blue), they will appear in the seed. Otherwise, they will not.'''
    optionEnum = PlayableCharacters
    options = [o for o in PlayableCharacters if o != PlayableCharacters.random]
    enabled = [o for o in PlayableCharacters if o != PlayableCharacters.random]
    id = "avail"


# ******** Equipment


class EquipmentProperties(SelectOneFlag):
    name = 'Equipment stats & buffs'
    description = '''<b>Default</b>: The stats and buffs on equipment are unchanged from the original game.
<br>
<br><b>Some buffs added</b>: The stats and buffs on equipment are mostly unchanged from the original game, except most armors are given one additional property (e.g. Fire Shirt nullifies damage from fire attacks). Additionally, some weapons will boost magic attack instead of physical attack.
<br>
<br><b>Completely random</b>: The stats and buffs on each piece of equipment is randomized.'''
    optionEnum = EquipmentPropertiesOptions
    choices = [o for o in EquipmentPropertiesOptions]
    default = EquipmentPropertiesOptions.vanilla
    id = "stats"


class EquipmentCharacters(SelectOneFlag):
    name = 'Equipment permissions'
    description = '''<b>Vanilla</b>: The list of characters who are permitted to equip each item remains unchanged from the original game.
<br>
<br><b>Vanilla, except anyone can wear any accessory</b>: Armor and weapon permissions are unchanged from the original game, but all accessories (including the Attack Scarf) can be equipped by anyone.
<br>
<br><b>Random, except anyone can wear any accessory</b>: Armor and weapon permissions are randomized, but all accessories can be equipped by anyone.
<br>
<br><b>Completely random</b>: All equips' permissions are randomized.
<br>
<br><b>Anyone can equip anything</b>: No equips are character-restricted.'''
    optionEnum = EquipmentCharactersOptions
    choices = [o for o in EquipmentCharactersOptions]
    default = EquipmentCharactersOptions.vanilla
    id = "perms"


class EquipmentNoSafety(BooleanFlag):
    name = 'No OHKO Safety'
    description = "If enabled, no equipment will protect against OHKO moves."
    
    id = "unsafe"


class StarPieceHints(BooleanFlag):
    name = 'Signal Ring Star Piece hints'
    description = '''If enabled, the Signal Ring (if equipped to your active party) will play a sound when you enter a world area that contains a Star Piece.  
<br>
<br>The Signal Ring will only sound off when you enter an area from the World Map, from loading a save, or from an area warp (ex: the Kero Sewers - Land's End pipe). Therefore, the chime does not necessarily indicate that your current room contains a Star Piece, but rather that at least one room in the area does.'''
    modes = ['open']
    
    id = "hints"


# ******** Stats & Spells

class EXPMultiplier(SelectOneFlag):
    name = 'EXP multiplier'
    description = '''If not set to "Default", all EXP gained will be doubled or tripled.'''
    optionEnum = EXPMultiplierOptions
    choices = [o for o in EXPMultiplierOptions]
    default = EXPMultiplierOptions.vanilla
    id = "exp"


class CharacterStats(BooleanFlag):
    name = 'Randomize character stats'
    description = '''If enabled, stats and stat curves for each playable character will be randomized. This also randomizes the number of FP you start with.
<br>
<br>If disabled, playable characters retain their original stats and stat curves.'''
    
    id = "stats"


class CharacterLearnedSpells(BooleanFlag):
    name = 'Randomize character learned spells'
    description = "The pool of spells learnable by each character will be randomized. This only covers spells originally learn-able by playable characters, and does not include enemy spells."
    
    id = "spells"


class CharacterSpellStats(BooleanFlag):
    name = 'Randomize character spell stats'
    description = "The power and FP cost of character magic spells will be randomized."
    
    id = "spellstats"


class UncapSuperJumps(BooleanFlag):
    name = 'Uncap Super Jumps'
    description = "If enabled, you can do more than 100 Super Jumps at once."
    
    # this needs testing
    id = "uncap"


class AvailableSpells(CategorizationFlag):
    name = "Available Player Spells"
    description = '''Highlighted (white text over blue) spells will be learned by at least one character. Spells that are not highlighted will not be learned by any character.
<br>
<br>Excluded spells are not replaced in characters' learnsets by other spells, so some characters will learn less than six total.
<br>
<br>Note: Excluding "Super Jump" may make some equips inaccessible depending on your other settings.'''
    optionEnum = LearnableSpells
    options = [o for o in LearnableSpells]
    enabled = [o for o in LearnableSpells]
    id = "avail"


# ******** Star Pieces


class ShuffleStarPieces(BooleanFlag):
    name = 'Randomize the locations of Star Pieces'
    description = '''If enabled, the Star Pieces may be found in places other than their original locations.
<br>
<br>If disabled, they will be rewarded by defeating the final bosses of Mushroom Kindom, Forest Maze, Moleville, Seaside Town, and Barrel Volcano, as well as a freestanding piece on Star Hill.'''
    modes = ['open']
    
    id = "random"
# if this is disabled, no other options in this category can be changed


class TotalStarPieces(NumberThresholdFlag):
    name = 'Total Star Pieces available'
    description = "The total number of Star Pieces (0-7) that can appear in the seed."
    default = 6
    min = 0
    max = 7
    modes = ['open']
    id = "avail"


boss_star_piece_locations = [
    ShuffleLocationSelector.MushroomWayStarPiece,
    ShuffleLocationSelector.BanditsWayStarPiece,
    ShuffleLocationSelector.InvasionStarPiece,
    ShuffleLocationSelector.PandoriteBoss,
    ShuffleLocationSelector.KeroSewersBoss,
    ShuffleLocationSelector.ForestMazeBoss,
    ShuffleLocationSelector.MolevilleMinesBoss1,
    ShuffleLocationSelector.MolevilleMinesBoss2,
    ShuffleLocationSelector.BoosterTowerStarPiece1,
    ShuffleLocationSelector.BoosterTowerStarPiece2,
    ShuffleLocationSelector.MarrymoreStarPiece,
    ShuffleLocationSelector.StarHillStarPiece1,
    ShuffleLocationSelector.SunkenShipMidboss,
    ShuffleLocationSelector.HidonBoss,
    ShuffleLocationSelector.SunkenShipBoss,
    ShuffleLocationSelector.SeasideTownBoss,
    ShuffleLocationSelector.LandsEndStarPiece1,
    ShuffleLocationSelector.BelomeTempleBoss,
    ShuffleLocationSelector.DojoBoss1,
    ShuffleLocationSelector.DojoBoss2,
    ShuffleLocationSelector.DojoBoss3,
    ShuffleLocationSelector.DojoBoss4,
    ShuffleLocationSelector.CulexBoss,
    ShuffleLocationSelector.BoxBoyBoss,
    ShuffleLocationSelector.BeanValleyBoss,
    ShuffleLocationSelector.NimbusLandStarPiece1,
    ShuffleLocationSelector.NimbusCastleStarPiece2,
    ShuffleLocationSelector.NimbusCastleStarPiece3,
    ShuffleLocationSelector.BarrelVolcanoBoss1,
    ShuffleLocationSelector.BarrelVolcanoBoss2,
    ShuffleLocationSelector.BowsersKeepBossChester,
    ShuffleLocationSelector.BowsersKeepBoss1,
    ShuffleLocationSelector.BowsersKeepBoss2,
    ShuffleLocationSelector.BowsersKeepBoss3,
    ShuffleLocationSelector.FactoryBoss1,
    ShuffleLocationSelector.FactoryBoss2,
    ShuffleLocationSelector.InnerFactoryBoss1,
    ShuffleLocationSelector.InnerFactoryBoss2,
    ShuffleLocationSelector.InnerFactoryBoss3,
    ShuffleLocationSelector.InnerFactoryBoss4,
    ShuffleLocationSelector.InnerFactoryBossFinal,
]


class EnabledBossChecks(CategorizationFlag):
    name = 'Eligible Star Piece boss fight locations'
    description = '''If a check is highlighted (white text over blue), it is eligible to reward a Star Piece.
<br>
<br>If a check is not highlighted, it will still house a boss fight, but is guaranteed to not reward a Star Piece.
<br>
<br>Note: "Nimbus Land statue keeper" will always be the same fight as the enemy running through the final Nimbus Land hallway. You can fight either instance of this boss to get its star piece, but you will never get 2 star pieces from doing both copies of the fight.'''
    optionEnum = ShuffleLocationSelector
    options = [o for o in boss_star_piece_locations]
    enabled = [o for o in boss_star_piece_locations]
    id = "fights"


class StarPiecesRestrictedByArea(BooleanFlag):
    name = 'Restrict number of Star Pieces in a World Map area'
    description = '''If enabled, each of the seven overworld map areas may only contain up to one Star Piece each.
<br>
<br>Note: This may not be perfectly respected if Bowser's Keep and Factory are both gated by high Star Piece counts.'''
    modes = ['open']
    
    id = "restrict_map"


# ******** Item shuffle


class ShuffleItems(BooleanFlag):
    name = 'Randomize the contents of treasure chests and item rewards'
    description = '''If enabled, the contents of treasure chests, quest rewards, and (optionally) freestanding small items will be shuffled.
<br>
<br>If disabled, chests, quest rewards, and freestanding small items will remain unchanged from the original game.'''
    modes = ['open']
    
    id = "random"
# if this is disabled, no options in this category can be changed


class ItemQuality(SelectOneFlag):
    name = '''Item pool quality'''
    description = '''Restricts the incidence of certain items within the shuffled pool. 
<br>
<br>If "Original item pool" is selected, items which only appear once in the original game will also not appear in unlimited shops. Additionally, two copies of the progressive Mystery Egg will be added to the pool, replacing some small items.
<br>
<br>If "Completely empty" is selected, any chest which does not contain a required item will be a "You Missed" chest.'''
    modes = ['open']
    optionEnum = ItemQualities
    choices = [o for o in ItemQualities]
    default = ItemQualities.original
    id = "quality"


class BiasItemShuffle(BooleanFlag):
    name = 'Bias better items to gated locations'
    description = '''If enabled, harder-to-reach areas will generally house better items.'''
    modes = ['open']
    
    id = "bias"


class RestrictSpecialEquips(BooleanFlag):
    name = 'Restrict key item exchange equips & Monstro Town reward equips'
    description = '''If enabled, the FroggieStick, Chomp, Zoom Shoes, Attack Scarf, Super Suit, Quartz Charm, Jinx Belt, Ghost Medal, and both Lazy Shells will appear once each, shuffled only within each other's locations. This option ignores your chosen Item Quality setting.
<br>
<br>If disabled, these items can appear anywhere, subject to the restrictions of your chosen Item Quality setting.'''
    modes = ['open']
    
    id = "restrict_monstro"


class BetterTips(BooleanFlag):
    name = 'Better Consolation Prizes'
    description = '''If enabled, some repeatable item grants will give a better, or wider, variety of items. Example of this include Knife Guy's juggling game junk prizes, or tips from working in the Marrymore hotel. This setting has no impact on singular, clearable item checks.'''
    modes = ['open']
    
    id = "tips"


class EXPStarsAnywhere(BooleanFlag):
    name = 'EXP stars can appear anywhere'
    description = '''If enabled, EXP stars may appear in any chest near monsters.
<br>
<br>If disabled, EXP stars will be restricted to their original locations within Bandit's Way, Kero Sewers, Moleville Mines, Sea, Land's End, Nimbus Land, and Barrel Volcano.'''
    modes = ['open']
    
    id = "xpstars_anywhere"


class SlotsAnywhere(BooleanFlag):
    name = 'Slot machines can appear anywhere'
    description = '''If enabled, any chest in the world could contain a slot machine.
<br>
<br>If disabled, slot machines will be restricted to their original locations in Bean Valley.
<br>
<br>Note that a bad roll on a slot machine will initiate a duplicate of the third mimic chest fight.'''
    modes = ['open']
    
    id = "slots_anywhere"


class ShuffleBeetlemania(BooleanFlag):
    name = 'Shuffle Beetlemania'
    description = '''If enabled, Beetlemania will be unlocked by a random item check, and the Mushroom Kingdom inn kid will sell you a random item check.'''
    modes = ['open']
    
    id = "beetle"


class ShuffleMagikoopaChest(BooleanFlag):
    name = 'Shuffle Magikoopa\'s coin chest'
    description = '''If enabled, Magikoopa's infinite coin box could appear in any chest, and the chest in his room will be an item check.'''
    modes = ['open']
    
    id = "kamek"


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
    optionEnum = FireworksOptions
    choices = [o for o in FireworksOptions]
    default = FireworksOptions.vanilla
    id = "fireworks"


# ******** Progression availability


class KeyItemsAnywhere(BooleanFlag):
    name = '"Special Items" can appear anywhere'
    description = '''If enabled, items belonging to your "Special Items" pocket can appear in any item location.
<br>
<br>If disabled, the "Special Items" will only be shuffled within each other's locations.
<br>
<br>The items targeted by this setting are the <b>Rare Frog Coin</b>, <b>Cricket Pie</b>, <b>Bambino Bomb</b>, <b>Castle Key 1</b>, <b>Castle Key 2</b>, <b>Alto Card</b>, <b>Tenor Card</b>, <b>Soprano Card</b>, <b>Greaper Flag</b>, <b>Dry Bones Flag</b>, <b>Big Boo Flag</b>, <b>Shed Key</b>, <b>Elder Key</b>, <b>Cricket Jam</b>, <b>Temple Key</b>, <b>Room Key</b>, <b>Seed</b>, and <b>Fertilizer</b> (and sometimes <b>Bright Card</b> and <b>Fireworks</b>).'''
    modes = ['open']
    
    id = "keys_anywhere"


class StarPieceAvailability(BooleanFlag):
    name = 'Star Pieces can appear in the general item pool'
    description = "If enabled, some Star Pieces may be shuffled in with items instead of being only granted by boss fights."
    modes = ['open']
    
    id = "stars_anywhere"


class InvisibleFlagsSetting(BooleanFlag):
    name = 'Move invisible flag checks'
    description = '''Chooses where the invisible items placed by the Three Musty Fears are located. 
<br>
<br>If "Default locations" is selected, these checks will remain in their default locations (Mario's Pad bed, Rose Town sign, Yo'ster Isle goalpost).
<br>
<br>If enabled, the three checks will be located somewhere random in the world as an invisible item. The Three Musty Fears will give you hints as to their locations.'''
    modes = ['open']
    
    id = "moveflags"




class EnabledRegularChecks(CategorizationFlag):
    name = 'Chest & reward checks'
    description = '''If a check is highlighted (white text over blue), it is eligible to contain items required to complete the seed.
<br>
<br>If a check is not highlighted, its contents will still be shuffled, but it will not contain any items required to complete the seed.
<br>
<br>This setting only applies if you have "Special Items can appear anywhere" or "Star Pieces can appear in the general item pool" enabled.'''
    optionEnum = ShuffleLocationSelector
    options = [o for o in regular_checks]
    enabled = [o for o in regular_checks]
    id = "chests"




class EnabledFreestandingChecks(CategorizationFlag):
    name = 'Freestanding coin/flower/mushroom checks'
    description = '''If a check is highlighted (white text over blue), it is eligible to contain items required to complete the seed.
<br>
<br>If a check is not highlighted, it will not be shuffled, nor can it contain any items required to complete the seed.
<br>
<br>If item quality is set to "Completely empty", only highlighted checks will be affected.'''
    optionEnum = ShuffleLocationSelector
    options = [o for o in freestanding_checks]
    id = "coins"


# ******** Item behaviour


class ReplaceItems(BooleanFlag):
    name = 'Replace some chest items with coins'
    description = 'If enabled, the worst items (Wilt Shrooms, etc) will be replaced with coins in chests.'
    modes = ['open']
    
    id = "replace"


class QuickHitCoins(BooleanFlag):
    name = 'Quick-hit coin chests'
    description = 'If enabled, all coin and frog coin chests will grant coins in a single hit instead of multiple hits.'
    modes = ['open']
    
    id = "quick"


class PoisonMushroom(BooleanFlag):
    name = 'Change Fake Mushroom\'s Effect'
    description = ('Randomize the status effect inflicted on a party member with the Fake Mushroom. It will only give '
                   'one status effect per seed, which has a 1/8 chance of being Invincibility.')
    modes = ['open']
    
    id = "fake"


class EXPChallenge(SelectOneFlag):
    name = 'EXP Star Behaviour'
    description = '''<b>Default</b>: EXP stars can give you 1 to 11 EXP per hit as normal.
<br>
<br><b>Star Pieces (easy/hard)</b>: EXP per star increases with the number of Star Pieces collected. This is not adjusted for lower max Star Piece counts.
<br>
<br><b>Bosses (easy/hard)</b>: EXP per star increases with the number of bosses you have defeated.
<br>
<br><b>No EXP</b>: EXP stars give you 0 EXP.
<br>
<br>"Easy" settings grant 2, 4, 5, 6, 8, 9, or 11 EXP depending on your progress, and "Hard" settings grant 1, 2, 3, 5, 6, 7, or 11 EXP.'''
    optionEnum = EXPChallengeOptions
    choices = [o for o in EXPChallengeOptions]
    default = EXPChallengeOptions.vanilla
    id = "xpstar"


class GrateGuyPrizeThreshold(NumberThresholdFlag):
    name = 'Required "Look The Other Way" wins'
    description = "The number of times required to win Grate Guy's casino minigame to receive its ultimate prize."
    default = 100
    min = 1
    max = 255
    modes = ['open']
    id = "gg"


class KnifeGuyPrizeThreshold(NumberThresholdFlag):
    name = 'Required juggling wins'
    description = "The number of wins minus losses required to win Knife Guy's ultimate juggling game prize."
    default = 12
    min = 1
    max = 254
    modes = ['open']
    id = "kg"


class SuitePrize1Threshold(NumberThresholdFlag):
    name = 'Required Suite prize #1 stays'
    description = "The number of times required to stay in the Marrymore Suite to receive the first special gift"
    default = 1
    min = 1
    max = 254
    modes = ['open']
    id = "s1"


class SuitePrize2Threshold(NumberThresholdFlag):
    name = 'Required Suite prize #2 stays'
    description = "The number of times required to stay in the Marrymore Suite to receive the second special gift"
    default = 3
    min = 1
    max = 254
    modes = ['open']
    id = "s2"


class SuitePrize3Threshold(NumberThresholdFlag):
    name = 'Required Suite prize #3 stays'
    description = "The number of times required to stay in the Marrymore Suite to receive the third special gift"
    default = 5
    min = 1
    max = 254
    modes = ['open']
    id = "s3"


class SuitePrize4Threshold(NumberThresholdFlag):
    name = 'Required Suite prize #4 stays'
    description = "The number of times required to stay in the Marrymore Suite to receive the fourth special gift"
    default = 10
    min = 1
    max = 254
    modes = ['open']
    id = "s4"


class SuitePrize5Threshold(NumberThresholdFlag):
    name = 'Required Suite prize #5 stays'
    description = "The number of times required to stay in the Marrymore Suite to receive the fifth special gift"
    default = 15
    min = 1
    max = 254
    modes = ['open']
    id = "s5"


class SuitePrize6Threshold(NumberThresholdFlag):
    name = 'Required Suite prize #6 stays'
    description = "The number of times required to stay in the Marrymore Suite to receive the sixth special gift"
    default = 200
    min = 1
    max = 254
    modes = ['open']
    id = "s6"


class SuperJump1Threshold(NumberThresholdFlag):
    name = 'Required Super Jumps for prize #1'
    description = "The number of consecutive Super Jumps required for the first prize in Monstro Town"
    default = 30
    min = 1
    max = 99
    modes = ['open']
    id = "sj1"


class SuperJump2Threshold(NumberThresholdFlag):
    name = 'Required Super Jumps for prize #2'
    description = "The number of consecutive Super Jumps required for the second prize in Monstro Town"
    default = 100
    min = 2
    max = 100
    modes = ['open']
    id = "sj2"


# ******** Area Access


class BanditsWayGate(SelectOneFlag):
    name = '''Bandit's Way access'''
    description = '''<b>Recruit character</b>: Bandit's Way will become available on the world map when you recruit the selected character.
<br>
<br><b>Finish Mushroom Way</b>: Bandit's Way will become available on the world map when you defeat the boss of Mushroom Way.
<br>
<br><b>Always Open</b>: Bandit's Way will be available on the world map from the start of the game.'''
    modes = ['open']
    optionEnum = BanditsWayGating
    choices = [o for o in BanditsWayGating]
    default = BanditsWayGating.mallow
    id = "bw"


class ForestMazeGate(SelectOneFlag):
    name = '''Forest Maze access'''
    description = '''<b>Find character</b>: Forest Maze will become available on the world map when you first see the selected character. "See" does not necessarily mean "recruit".
<br>
<br><b>Exchange Cricket Pie</b>: Forest Maze will become available on the world map when you turn in the Cricket Pie to Frogfucius.
<br>
<br><b>Always Open</b>: Forest Maze will be available on the world map from the start of the game.'''
    optionEnum = ForestMazeGating
    modes = ['open']
    choices = [o for o in ForestMazeGating]
    default = ForestMazeGating.geno
    id = "fm"


class PipeVaultGate(SelectOneFlag):
    name = '''Pipe Vault access'''
    description = '''<b>Recruit character</b>: Pipe Vault will be unblocked when you recruit the selected character.
<br>
<br><b>Finish Forest Maze</b>: Pipe Vault will be unblocked when you defeat the final boss of Forest Maze.
<br>
<br><b>Always Open</b>: Pipe Vault will be unblocked from the start of the game.'''
    modes = ['open']
    optionEnum = PipeVaultGating
    choices = [o for o in PipeVaultGating]
    default = PipeVaultGating.open
    id = "pv"


class BoosterTowerGate(SelectOneFlag):
    name = '''Booster Tower access'''
    description = '''<b>Recruit character</b>: Booster Tower's door can be unlocked when you recruit the selected character.
<br>
<br><b>Finish Moleville</b>: Booster Tower's door will unlock when you defeat the final boss of Moleville.
<br>
<br><b>Always Open</b>: Booster Tower's door will be unlocked from the start of the game.'''
    modes = ['open']
    optionEnum = BoosterTowerGating
    choices = [o for o in BoosterTowerGating]
    default = BoosterTowerGating.bowser
    id = "bt"


class MarrymoreGate(SelectOneFlag):
    name = '''Marrymore back door access'''
    description = '''<b>Finish Booster Hill</b>: The chapel back door will become available on the world map when you complete Booster Hill one time.
<br>
<br><b>Finish Booster Tower</b>: The chapel back door will become available on the world map when you defeat the balcony boss of Booster Tower.
<br>
<br><b>Always Open</b>: The chapel back door will be open from the start of the game.'''
    modes = ['open']
    optionEnum = MarrymoreGating
    choices = [o for o in MarrymoreGating]
    default = MarrymoreGating.hill
    id = "mm"


class SeaGate(SelectOneFlag):
    name = '''Sea & Sunken Ship access'''
    description = '''<b>Recruit character</b>: The Sea will become available on the world map when you recruit the selected character.
<br>
<br><b>Collect Star Pieces</b>: The Sea will become available on the world map when you collect the selected number of Star Pieces.
<br>
<br><b>Always Open</b>: The Sea & Sunken Ship will be available on the world map from the start of the game.'''
    modes = ['open']
    optionEnum = SeaGating
    choices = [o for o in SeaGating]
    default = SeaGating.star4
    id = "sea"


class MonstroTownGate(SelectOneFlag):
    name = '''Monstro Town access'''
    description = '''<b>Finish Land's End</b>: Monstro Town will become available on the World Map once you take the pipe behind the boss of Belome Temple.
<br>
<br><b>Always Open</b>: Monstro Town will be available on the World Map from the start of the game.'''
    modes = ['open']
    optionEnum = MonstroTownGating
    choices = [o for o in MonstroTownGating]
    default = MonstroTownGating.landsend
    id = "mt"


class BarrelVolcanoGate(SelectOneFlag):
    name = '''Barrel Volcano access'''
    description = '''<b>Finish Nimbus Land</b>: Barrel Volcano will become available on the World Map once you defeat the final boss of Nimbus Castle.
<br>
<br><b>Always Open</b>: Barrel Volcano will be available on the World Map from the start of the game.'''
    modes = ['open']
    optionEnum = BarrelVolcanoGating
    choices = [o for o in BarrelVolcanoGating]
    default = BarrelVolcanoGating.nimbus
    id = "bv"


class BowsersKeepGate(SelectOneFlag):
    name = '''Bowser's Keep access'''
    description = '''<b>Collect Star Pieces</b>: Bowser's Keep will become available on the world map when you collect the selected number of Star Pieces.
<br>
<br><b>Finish Barrel Volcano</b>: Bowser's Keep will become available on the World Map once you defeat the final boss of Barrel Volcano.
<br>
<br><b>Always Open</b>: Bowser's Keep will be available on the world map from the start of the game.'''
    modes = ['open']
    optionEnum = BowsersKeepGating
    choices = [o for o in BowsersKeepGating]
    default = BowsersKeepGating.volcano
    id = "bk"


class FactoryGate(SelectOneFlag):
    name = '''Factory access'''
    description = '''<b>Open when Bowser's Keep is opened</b>: When Bowser's Keep becomes available on the world map, Factory will also be immediately available on the world map.
<br>
<br><b>Finish Bowser's Keep</b>: Factory will become available on the world map when you complete Bowser's Keep for the first time.
<br>
<br><b>Collect Star Pieces</b>: Factory will become available on the world map when you collect the selected number of Star Pieces and Bowser's Keep has been opened. Cannot be higher than 'Star Pieces required to beat the game'.'''
    modes = ['open']
    optionEnum = FactoryGating
    choices = [o for o in FactoryGating]
    default = FactoryGating.keep
    id = "wf"


# ******** Boss & Endgame Access


class YaridovichGate(SelectOneFlag):
    name = '''Seaside boss fight access'''
    description = '''<b>Finish Sunken Ship</b>: The Seaside boss fight will become available after you defeat the final boss of Sunken Ship.
<br>
<br><b>Always Open</b>: The Seaside boss will be available from the start of the game.'''
    modes = ['open']
    optionEnum = YaridovichGating
    choices = [o for o in YaridovichGating]
    default = YaridovichGating.ship
    id = "seaside"


class SkipMustyFearsSequence(BooleanFlag):
    name = 'Skip 3 Musty Fears sequence'
    description = '''This flag affects the Musty Fears checks (normally Mario's Pad bed, Rose Town sign, and Yo'ster Isle goalpost; or whichever three locations are added to the seed when "Move invisible flag checks" is set to "Any landmark").
<br>
<br>If disabled, the affected checks will become available after you visit the Musty Fears Inn in Monstro Town.
<br>
<br>If enabled, the affected checks will be available from the start of the seed.'''
    modes = ['open']
    
    id = "skip_musty"


class BowserDoorRequirements(NumberThresholdFlag):
    name = 'Required Bowser\'s Keep obstacle doors'
    description = "The number of doors required to progress through Bowser's Keep."
    default = 4
    min = 1
    max = 6
    modes = ['open']
    id = "doors"


class StarPiecesRequired(NumberThresholdFlag):
    name = 'Star Pieces required to access the final Factory boss'
    description = "The total number of Star Pieces (0-7) that are required to access the final boss. Cannot be higher than Total Star Pieces."
    default = 6
    min = 0
    max = 7
    modes = ['open']
    id = "endgame"


class CasinoWarp(BooleanFlag):
    name = 'Casino Warp'
    description = "If enabled, a trampoline warping directly to the final boss will become available in Grate Guy's Casino once you have collected the number of Star Pieces specified in 'Star Pieces required to beat the game'. The Bright Card becomes a key item, and Knife Guy's juggling reward becomes a key item check."
    modes = ['open']
    
    id = "cwarp"


class BucketWarp(BooleanFlag):
    name = 'Bucket Warp'
    description = "If enabled, trading a Carbo Cookie to the bucket girl in Moleville will reveal a warp to the final boss once you have collected the number of Star Pieces specified in 'Star Pieces required to beat the game'."
    modes = ['open']
    
    id = "bwarp"


class FastTravel(BooleanFlag):
    name = 'Fast travel'
    description = '''If enabled, the following changes will be applied to the game:
<ol>
<li>Traveling to the top of Booster Tower after defeating the balcony boss will always warp you to the ground.</li>
<li>Reaching the Inner Factory will reveal a trampoline that warps you to the world map.</li>
<li>Reaching the Inner Factory will enable a world map shortcut that places you in Inner Factory.</li>
</ol>'''
    modes = ['open']
    
    id = "fasttravel"


class WinCondition(SelectOneFlag):
    name = "Condition required to beat the game"
    description = '''<b>Beat the Factory</b>: When you collect the number of Star Pieces specified in your Required Star Pieces setting, the button in the Inner Factory (as well as any enabled warps) will be enabled to allow you to access the final boss and beat the game.
<br>
<br><b>Collect required Star Pieces</b>: When you collect the number of Star Pieces specified in your Required Star Pieces setting, the game is over and the credits will roll.
<br>
<br><b>Beat Monstro Town sealed door</b>: The game is over when you defeat the boss behind the sealed door in Monstro Town, regardless of your Star Piece count.'''
    optionEnum = WinConditions
    choices = [o for o in WinConditions]
    default = WinConditions.factory
    id = "objective"


# ******** Puzzles

class BallSolitaireShuffle(BooleanFlag):
    name = 'Randomize Ball Solitaire'
    description = 'The layout for the Ball Solitaire minigame will be randomized.'
    
    id = "ball"


class MagicButtonShuffle(BooleanFlag):
    name = 'Randomize Magic Buttons'
    description = 'The layout for the Magic Buttons minigame will be randomized.'
    
    id = "button"


class QuizShuffle(BooleanFlag):
    name = 'Randomize Dr. Topper Quiz'
    description = 'The question pool for the Dr. Topper quiz will include new questions provided by the community.'
    
    id = "quiz"


class RandomTadpolePondSong(BooleanFlag):
    name = 'Randomize Tadpole Pond songs'
    description = '''If enabled, the songs required for the three Tadpole Pond songs will be selected from a random pool, submitted by players. Hints will be available in their normal locations within Tadpole Pond, Moleville Mines, and Monstro Town.'''
    modes = ['open']
    
    id = "melody"


class RandomSunkenShipPassword(BooleanFlag):
    name = 'Randomize Sunken Ship password'
    description = '''If enabled, the password for the Sunken Ship will be changed. Hints are available in the 6 ship puzzles, and occasionally on posted notes within the Sunken Ship.'''
    modes = ['open']
    
    id = "pwd"


class BowserDoorShuffle(BooleanFlag):
    name = "Randomize Bowser\'s Keep room sequences"
    description = '''If enabled, the 18 rooms making up the six Bowser's Keep obstacle course doors will be shuffled into six random sequences of three rooms each.'''
    modes = ['open']
    
    id = "doors"


class SkipMinecart(BooleanFlag):
    name = "Skip Minecart minigame"
    description = '''If enabled, boarding the minecart for the first time will teleport you back to Moleville. Subsequent visits to the minecart room will play the minigame as normal.'''
    modes = ['open']
    
    id = "skipcart"

# ******** Shops


class ShuffleShops(BooleanFlag):
    name = 'Randomize the contents of shops'
    description = '''If enabled, the contents of all regular shops and Frog Coin shops (including the Moleville treasure shop, Marrymore Suite room service menu, and Moleville swap shop) will be randomized.'''
    modes = ['open']
    
    id = "random"
# if this is disabled, no options in this category can be changed


class ShopQuality(SelectOneFlag):
    name = '''Shop contents quality'''
    description = '''Restricts the incidence of certain items in shops. 
<br>
<br>"Completely random" means that some items which originally did not appear in shops may now appear in shops, but only a small pool of items are guaranteed to appear. Some items will never appear in non-depletable shops. 
<br>
<br>If "Completely empty" is selected, all shops will be disabled.'''
    modes = ['open']
    optionEnum = ShopQualities
    choices = [o for o in ShopQualities]  # maybe just o for o
    default = ShopQualities.original
    id = "quality"
    requires_all = [(ShuffleShops(), True)]


class BiasShopShuffle(BooleanFlag):
    name = 'Bias better items to gated shops'
    description = '''If enabled, harder-to-reach shops will generally sell better items.'''
    modes = ['open']
    
    id = "bias"
    requires_all = [(ShuffleShops(), True), (ShopQuality(), [o for o in ShopQualities if o != ShopQualities.original])]


class ShowEquips(BooleanFlag):
    name = 'Always show all permitted characters on equips'
    description = 'Always show who can equip what in stores.'
    
    id = "showperms"


class FreeShops(BooleanFlag):
    name = "'Free' Shops"
    description = '''If enabled, all shop items will cost 1 coin. You will start with 9999 coins and 999 frog coins.'''
    modes = ['open']
    
    id = "free"

# ******** Enemies & Bosses


class BossShuffle(BooleanFlag):
    name = 'Randomize boss positions'
    description = (
        "If enabled, the positions of bosses (including Pandorite, Hidon, Box Boy, Chester, and Mokura) are shuffled.")
    modes = ['open']
    
    id = "random"
    # if false, disable stat scaling and mimics anywhere


class BossShuffleScaleStats(BooleanFlag):
    name = "Scale boss stats to area difficulty"
    description = '''If enabled: A boss fight that has been shuffled into a different area will have its stats scaled to match the area's original boss.
<br>
<br>If disabled: Boss fights retain their original stats, regardless of where they are placed.'''
    
    id = "scale"
    requires_all = [(BossShuffle(), True)]


class BossReplaceMinigameSprites(BooleanFlag):
    name = "Replace important NPCs to match shuffled bosses"
    description = '''If enabled: All sprites related to an area boss will be changed to match the shuffled positions of bosses.
<br>
<br>If disabled: Some sprites will be left unchanged from the original game to accommodate visual cues (such as the Booster Hill snifits, or Dodo in his statue room) or progression knowledge on required sub-fights (such as the Bandana Reds in Sunken Ship).'''
    
    id = "allsprites"
    requires_all = [(BossShuffle(), True)]


class MimicsAnywhere(BooleanFlag):
    name = 'Mimics can appear anywhere'
    description = '''If enabled, the three mimics could be in any chest in the world. If you have "Scale boss stats to area difficulty" enabled, each mimic will be restricted to areas that are appropriate for its stats. However you should save often with this setting turned on, especially if item-hunting at the start of the seed.
<br>
<br>If disabled, mimic chests will remain in their original locations in Kero Sewers, Sunken Ship, and Bean Valley.'''
    modes = ['open']
    
    id = "mimics_anywhere"
    requires_all = [(ShuffleItems(), True)]


class ShuffledBosses(CategorizationFlag):
    name = 'Shuffled boss fights'
    description = '''If a boss is highlighted (white text over blue), it will be shuffled into a pool and placed in a random boss location.
<br>
<br>If a boss is not highlighted, it will stay in its original location.'''
    optionEnum = AvailableBosses
    options = [o for o in AvailableBosses]
    enabled = [o for o in AvailableBosses]
    id = "pool"
    requires_all = [(ShuffleItems(), True)]


class EnemyStats(BooleanFlag):
    name = 'Randomize enemy stats'
    description = '''If enabled, enemy stats and immunities/weaknesses will be randomized.
<br>
<br>If disabled, enemies retain their original stats (subject to placement shuffling, if enabled), immunities, and vulnerabilities.'''
    
    id = "stats"


class EnemyDrops(BooleanFlag):
    name = 'Randomize enemy drops'
    description = "If enabled, the EXP and in-battle items received from battles will be randomized."
    
    id = "drops"


class EnemyFormations(BooleanFlag):
    name = 'Randomize formations'
    description = "If enabled, enemy encounters may contain random unexpected additional enemies and be laid out erratically. Boss formations are not affected."
    
    id = "formations"


class EnemyAttacks(BooleanFlag):
    name = 'Randomize attacks'
    description = "If enabled, enemy spells and attacks will have their power randomized. Attacks which cast statuses will have the status effects randomized, and attacks which normally don't inflict statuses may inflict unexpected statuses."
    
    id = "attacks"


class EnemyNoSafetyChecks(BooleanFlag):
    name = 'No safety checks'
    description = "If enabled, removes safety checks on enemy attack shuffle that prevent abnormally large effects."
    
    hard = True
    id = "unsafe"
    requires_all = [(EnemyAttacks(), True)]


class EnemySpells(BooleanFlag):
    name = 'Randomize enemy spells'
    description = "If enabled, enemies can cast random spells. I.E. Mack could cast Blast instead of Flame."
    
    hard = True
    modes = ['open']
    id = "spells"


class ExperienceNoRegular(BooleanFlag):
    name = 'Remove EXP from regular enemy encounters'
    
    hard = True
    id = "noregexp"


class ExperienceNoBosses(BooleanFlag):
    name = 'Remove EXP from boss encounters'
    
    hard = True
    id = "nobossexp"


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
    
    id = "noskips"


class NoGenoWhirlExor(BooleanFlag):
    name = 'No Geno Whirl on Exor'
    description = 'Removes the Exor exploit where he is vulnerable to Geno Whirl when the eyes are stunned.'
    
    id = "nowhirl"


class FixMagikoopa(BooleanFlag):
    name = "Fix Magikoopa"
    description = 'Removes the Magikoopa oversight where he permanently skips turns after a King Bomb explosion.'
    
    id = "nobigbang"


class NoOHKO(BooleanFlag):
    name = "No instant KOs on boss allies"
    description = ('You will not be able to use Geno Whirl or Pure Water to OHKO any allies to a boss (Mallow Clone, '
                   'Mad Mallet, Fautso, etc).')
    
    id = "noko"

# ******** Cosmetic


class PaletteSwaps(BooleanFlag):
    name = 'Palette Swaps'
    description = 'Your party members get a change of wardrobe!'
    inverse_description = '(Sprite colours are not modified.)'
    value = '-palette'
    id = "palette"


class ChangeNames(BooleanFlag):  # not available unless PaletteSwaps enabled
    name = 'Change character names'
    description = '''Some palette swaps are references to other media. If this flag is enabled, the character's name will be changed to match the palette.'''
    inverse_description = '(Sprite colours are not modified.)'
    id = "names"
    requires_all = [(PaletteSwaps(), True)]



class BossShuffleMusic(BooleanFlag):
    name = 'Randomize boss music'
    description = 'Battle music will be randomized for each boss fight.'
    inverse_description = "(Battle music for each location will remain unchanged from the original game.)"
    id = "music"


class ShuffledMusic(CategorizationFlag):
    name = 'Allowable shuffled music'
    description = '''If a song is highlighted (white text over blue), it can appear in any boss fight.
<br>
<br>If a song is not highlighted, it will never appear in a boss fight.'''
    optionEnum = AvailableMusic
    options = [o for o in AvailableMusic]
    enabled = [o for o in AvailableMusic]
    id = "avail"

class RemoveFlashes(BooleanFlag):
    name = "Remove flashes"
    description = '''Removes some flashing animations (from spells, attacks, etc). 
<br>
<br>Disclaimer: While this feature is intended to promote accessibility, developers cannot promise that every feature in the game with screen flashes has had them removed. Players and viewers with photosensitivity should continue to engage with this randomizer at their own risk. 
<br>
<br>If you would like to suggest an animation that should have flashes removed by this feature, please see the "Contributing" section and fill out the form.'''
    id = "noflash"


# ************************************** Category classes

class FlagCategory:
    name = ''
    subcategories = []
    flags = []
    size = 3
    id = ""


class CharacterRecruitmentSubcategory(FlagCategory):
    flags = [
        ShuffleCharacters,
        StartingCharacters,
        StartingCharacter,
        AvailableCharacters,
    ]
    size = 4
    id = "P"


class CharacterEquipmentSubcategory(FlagCategory):
    flags = [
        EquipmentProperties,
        EquipmentCharacters,
        EquipmentNoSafety,
        StarPieceHints
    ]
    size = 4
    id = "Q"


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
    id = "C"


class PartyCategory(FlagCategory):
    name = 'Party & Equipment'
    subcategories = [
        CharacterRecruitmentSubcategory,
        CharacterEquipmentSubcategory,
        CharacterStatsSpellsSubcategory
    ]
    id = "PartyCategory"


class StarPiecesCategory(FlagCategory):
    flags = [
        ShuffleStarPieces,
        TotalStarPieces,
        EnabledBossChecks,
        StarPiecesRestrictedByArea,
    ]
    size = 3
    id = "X"


class ItemShuffleSubcategory(FlagCategory):
    flags = [
        ShuffleItems,
        ItemQuality,
        BiasItemShuffle,
        RestrictSpecialEquips,
        EXPStarsAnywhere,
        SlotsAnywhere,
        ShuffleBeetlemania,
        ShuffleMagikoopaChest,
        FireworksSetting,
        BetterTips,
    ]
    id = "T"


class ItemLocationSubcategory(FlagCategory):
    flags = [
        InvisibleFlagsSetting,
        KeyItemsAnywhere,
        StarPieceAvailability,
        EnabledRegularChecks,
        EnabledFreestandingChecks
    ]
    id = "L"


class BehaviourSubcategory(FlagCategory):
    flags = [
        PoisonMushroom,
        ReplaceItems,
        QuickHitCoins,
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
    id = "I"


class ItemsCategory(FlagCategory):
    name = 'Items & Star Pieces'
    subcategories = [
        StarPiecesCategory,
        ItemShuffleSubcategory,
        ItemLocationSubcategory,
        BehaviourSubcategory
    ]
    id = "ItemsCategory"


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
        BowsersKeepGate,
        FactoryGate,
    ]
    size = 3
    id = "A"


class OtherAccessSubcategory(FlagCategory):
    flags = [
        YaridovichGate,
        SkipMustyFearsSequence,
        BowserDoorRequirements,
        StarPiecesRequired,
        CasinoWarp,
        BucketWarp,
        FastTravel,
        WinCondition,
    ]
    size = 3
    id = "O"


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
    id = "G"


class ShopsCategory(FlagCategory):
    flags = [
        ShuffleShops,
        ShopQuality,
        BiasShopShuffle,
        ShowEquips,
        FreeShops
    ]
    size = 3
    id = "S"


class AccessCategory(FlagCategory):
    name = 'Progression & Shops'
    subcategories = [
        AreaAccessSubcategory,
        OtherAccessSubcategory, 
        PuzzleCategory, 
        ShopsCategory
    ]
    id = "AccessCategory"


class BossPositionSubcategory(FlagCategory):
    flags = [
        BossShuffle,
        BossShuffleScaleStats,
        BossReplaceMinigameSprites,
        MimicsAnywhere,
        ShuffledBosses
    ]
    size = 4
    id = "B"


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
    size = 4
    id = "E"


class BossCheeseSubcategory(FlagCategory):
    flags = [
        RequireBossFights,
        NoGenoWhirlExor,
        FixMagikoopa,
        NoOHKO,
    ]
    size = 4
    id = "F"


class BossCategory(FlagCategory):
    name = 'Enemies & Boss Fights'
    subcategories = [
        BossPositionSubcategory,
        BossStatSubcategory,
        BossCheeseSubcategory
    ]
    id = "BossCategory"


class AccessibilitySubcategory(FlagCategory):
    flags = [
        RemoveFlashes
    ]
    size = 4
    id = "R"


class MusicSubcategory(FlagCategory):
    flags = [
        BossShuffleMusic,
        ShuffledMusic,
    ]
    size = 4
    id = "R"


class PaletteSubcategory(FlagCategory):
    flags = [
        PaletteSwaps,
        ChangeNames,
    ]
    size = 4
    id = "R"


class CosmeticCategory(FlagCategory):
    name = 'Cosmetics'
    subcategories = [
        PaletteSubcategory,
        MusicSubcategory,
        AccessibilitySubcategory
    ]
    id = "CosmeticCategory"

# ************************************** Preset classes

# decide what to do with these later


class Preset:
    name = ''
    description = ''
    flags = ''

    @classmethod
    def id(cls):
        return cls.__name__


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

class ExplorerPreset(Preset):
    name = "Explorer"
    description = "A flagset that draws on strong knowledge of the original game, and will require a lot of hunting."
    flags = "Psize:1|start:random|random|avail:f     Qstats:some|perms:v_accessories_all|hints     Cexp:double|spells|uncap|avail:////H     Xrandom|avail:6|fights://////f     Trandom|quality:original|restrict_monstro|xpstars_anywhere|slots_anywhere|beetle|kamek|fireworks:progressive|tips     Lmoveflags|keys_anywhere|chests://////////////////////////////////////H|coins:4BgPAgN4/PAAAAA     Ifake|replace|xpstar:easybosses|gg:1|kg:1|s1:1|s2:2|s3:3|s4:4|s5:5|s6:6|sj1:30|sj2:100     Abw:mallow|fm:geno|pv:forest|bt:bowser|mm:tower|sea:star4|mt:landsend|bv:nimbus|bk:volcano|wf:open     Oseaside:ship|doors:1|endgame:6|cwarp|bwarp|fasttravel|objective:factory     Gquiz|melody|pwd|skipcart     Srandom|quality:original|bias|showperms     Brandom|scale|allsprites|mimics_anywhere|pool://////P"

class Spring2021AsyncTourneyPreset(Preset):
    name = "Spring 2021 Async Tournament (approximate)"
    description = "Flagset for the 2021 Async Tourney"
    flags = "Psize:1|start:random|random|avail:f     Qstats:random|perms:random     Cexp:triple|stats|spells|spellstats|avail:////H     Xrandom|avail:6|fights://vv/OA     Trandom|quality:t4|restrict_monstro|fireworks:vanilla     Ifake|xpstar:vanilla|gg:100|kg:12|s1:1|s2:3|s3:5|s4:10|s5:15|s6:200|sj1:30|sj2:100     Abw:open|fm:open|pv:open|bt:open|mm:open|sea:open|mt:open|bv:open|bk:open|wf:star6     Oseaside:open|skip_musty|doors:2|endgame:6|cwarp|objective:factory     Gdoors     Srandom|quality:t4|showperms     Brandom|scale|pool://3/f/H     Estats|drops|formations|attacks"
    # needs m2 without x

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
    ExplorerPreset,
    Spring2021AsyncTourneyPreset
)
