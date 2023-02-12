# Data module for chest data.
import random
import copy
import uuid
import enum

from randomizer.logic import flags
from randomizer.logic.utils import isclass_or_instance, new_command

from randomizer.data import items, locations, npcs, bosses
from randomizer.data.bosses import AvailableBosses
from randomizer.data.items import ItemUnique
from randomizer.data.rooms.room import Partition, RegularNPC
from randomizer.helpers.flag_helpers import (
    ShuffleLocationSelector,
    FireworksOptions,
    ItemQualities,
    BanditsWayGating,
    ForestMazeGating,
    Moleville1Gating,
    PipeVaultGating,
    BoosterTowerGating,
    MarrymoreGating,
    YaridovichGating,
    SeaGating,
    BelomeTempleGating,
    MonstroTownGating,
    BarrelVolcanoGating,
    BowsersKeepGating,
    FactoryGating,
    PlayableCharacters,
    BossScaleOptions,
)
from randomizer.helpers.roomobjecttables import ObjectType, Initiator, RadialDirection
from randomizer.helpers.eventtables import AreaObjects, _0x60Flags

from randomizer.helpers.roomobjecttables import PartitionBufferTypes, PartitionMainSpace


# locations inherit world, and therefore settings
# inventory does not
# how to make work with optional gating?


# *** Helper functions to check access to certain areas.
def can_clear_mushroom_way(world, inventory):
    # return world.get_check_instance(HammerBrosBossFightLocation).item is not None
    return True


def can_access_bandits_way(world, inventory):
    # if world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.mario):
    #     return inventory.has_item(items.MarioRecruit)
    # elif world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.mallow):
    if world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.mallow):
        return inventory.has_item(items.MallowRecruit)
    # elif world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.geno):
    #     return inventory.has_item(items.GenoRecruit)
    # elif world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.bowser):
    #     return inventory.has_item(items.BowserRecruit)
    # elif world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.toadstool):
    #     return inventory.has_item(items.ToadstoolRecruit)
    elif world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.hammerbro):
        return inventory.has_item(items.HammerBroBossFight)
    else:
        return True


def can_clear_bandits_way(world, inventory):
    # return world.get_check_instance(Croco1BossFightLocation).item is not None# and can_access_bandits_way(world, inventory)
    return can_access_bandits_way(world, inventory)


def can_clear_invasion(world, inventory):
    # return world.get_check_instance(MackBossFightLocation).item is not None# and can_clear_bandits_way(world, inventory)
    return can_clear_bandits_way(world, inventory)


def can_beat_mimic_1(world, inventory):
    return inventory.has_item(
        items.PandoriteFight
    )  # and world.get_check_instance(PandoriteBossFightLocation).item is not None


def can_beat_mimic_2(world, inventory):
    return inventory.has_item(
        items.HidonFight
    )  # and world.get_check_instance(HidonBossFightLocation).item is not None


def can_beat_mimic_3(world, inventory):
    return inventory.has_item(
        items.BoxBoyFight
    )  # and world.get_check_instance(BoxBoyBossFightLocation).item is not None


def can_access_forest(world, inventory):
    # if world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.mario):
    #     return inventory.has_item(items.MarioRecruit) or inventory.has_item(items.MarioSpotted)
    # elif world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.mallow):
    #     return inventory.has_item(items.MallowRecruit) or inventory.has_item(items.MallowSpotted)
    # elif world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.geno):
    if world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.geno):
        return inventory.has_item(items.GenoRecruit) or inventory.has_item(
            items.GenoSpotted
        )
    # elif world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.bowser):
    #     return inventory.has_item(items.BowserRecruit) or inventory.has_item(items.BowserSpotted)
    # elif world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.toadstool):
    #     return inventory.has_item(items.ToadstoolRecruit) or inventory.has_item(items.ToadstoolSpotted)
    elif world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.pie):
        return inventory.has_item(items.CricketPie)
    else:
        return True


def can_clear_forest(world, inventory):
    return can_access_forest(
        world, inventory
    )  # and world.get_check_instance(BowyerBossFightLocation).item is not None


def can_access_pipe_vault(world, inventory):
    # if world.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.mario):
    #     return inventory.has_item(items.MarioRecruit) or inventory.has_item(items.MarioSpotted)
    # elif world.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.mallow):
    #     return inventory.has_item(items.MallowRecruit) or inventory.has_item(items.MallowSpotted)
    if world.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.geno):
        # elif world.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.geno):
        return inventory.has_item(items.GenoRecruit)
    # elif world.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.bowser):
    #     return inventory.has_item(items.BowserRecruit) or inventory.has_item(items.BowserSpotted)
    # elif world.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.toadstool):
    #     return inventory.has_item(items.ToadstoolRecruit) or inventory.has_item(items.ToadstoolSpotted)
    elif world.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.forest):
        return can_clear_forest(world, inventory)
    elif world.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.bowyer):
        return inventory.has_item(items.BowyerBossFight)
    else:
        return True


def can_access_moleville_entrance(world, inventory):
    # if world.settings.is_flag_value(flags.Moleville1Gate, Moleville1Gating.mario):
    #     return inventory.has_item(items.MarioRecruit) or inventory.has_item(items.MarioSpotted)
    # elif world.settings.is_flag_value(flags.Moleville1Gate, Moleville1Gating.mallow):
    #     return inventory.has_item(items.MallowRecruit) or inventory.has_item(items.MallowSpotted)
    if world.settings.is_flag_value(flags.Moleville1Gate, Moleville1Gating.geno):
        # elif world.settings.is_flag_value(flags.Moleville1Gate, Moleville1Gating.geno):
        return inventory.has_item(items.GenoRecruit)
    # elif world.settings.is_flag_value(flags.Moleville1Gate, Moleville1Gating.bowser):
    #     return inventory.has_item(items.BowserRecruit) or inventory.has_item(items.BowserSpotted)
    # elif world.settings.is_flag_value(flags.Moleville1Gate, Moleville1Gating.toadstool):
    #     return inventory.has_item(items.ToadstoolRecruit) or inventory.has_item(items.ToadstoolSpotted)
    elif world.settings.is_flag_value(flags.Moleville1Gate, Moleville1Gating.forest):
        return can_clear_forest(world, inventory)
    elif world.settings.is_flag_value(flags.Moleville1Gate, Moleville1Gating.bowyer):
        return inventory.has_item(items.BowyerBossFight)
    else:
        return True


def can_clear_mines(world, inventory):
    return can_access_moleville_entrance(world, inventory) and inventory.has_item(
        items.BambinoBomb
    )  # and world.get_check_instance(PunchinelloBossFightLocation).item is not None


def can_access_tower(world, inventory):
    if world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.mario):
        return inventory.has_item(items.MarioRecruit)
    elif world.settings.is_flag_value(
        flags.BoosterTowerGate, BoosterTowerGating.mallow
    ):
        return inventory.has_item(items.MallowRecruit)
    elif world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.geno):
        return inventory.has_item(items.GenoRecruit)
    elif world.settings.is_flag_value(
        flags.BoosterTowerGate, BoosterTowerGating.bowser
    ):
        return inventory.has_item(items.BowserRecruit)
    elif world.settings.is_flag_value(
        flags.BoosterTowerGate, BoosterTowerGating.toadstool
    ):
        return inventory.has_item(items.ToadstoolRecruit)
    elif world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.mines):
        return can_clear_mines(world, inventory)
    elif world.settings.is_flag_value(
        flags.BoosterTowerGate, BoosterTowerGating.punchinello
    ):
        return inventory.has_item(items.PunchinelloBossFight)
    else:
        return True


def can_clear_tower_1(world, inventory):
    access = can_access_tower(world, inventory)
    # fight = (world.settings.is_flag_enabled(flags.RequireBossFights) and world.get_check_instance(BoosterBossFightLocation).item is not None) or not world.settings.is_flag_enabled(flags.RequireBossFights)
    return access  # and fight


def can_clear_tower_2(world, inventory):
    return can_clear_tower_1(
        world, inventory
    )  # and world.get_check_instance(ClownBrosBossFightLocation).item is not None


def can_access_marrymore(world, inventory):
    if world.settings.is_flag_value(flags.MarrymoreGate, MarrymoreGating.tower):
        return can_clear_tower_2(world, inventory)
    elif world.settings.is_flag_value(flags.MarrymoreGate, MarrymoreGating.kggg):
        return inventory.has_item(items.GrateGuyBossFight)
    else:
        return True


def can_fight_marrymore(world, inventory):
    has_gear = True
    if world.settings.is_flag_enabled(flags.ShuffleWeddingGear):
        has_gear = (
            inventory.has_item(items.Shoes)
            and inventory.has_item(items.Ring)
            and inventory.has_item(items.Brooch)
            and inventory.has_item(items.Crown)
        )
    return has_gear and can_access_marrymore(world, inventory)


def can_clear_marrymore(world, inventory):
    return can_fight_marrymore(
        world, inventory
    )  # and world.get_check_instance(BundtBossFightLocation).item is not None


def can_access_sea(world, inventory):
    # if world.settings.is_flag_value(flags.SeaGate, SeaGating.mario):
    #     return inventory.has_item(items.MarioRecruit)
    # elif world.settings.is_flag_value(flags.SeaGate, SeaGating.mallow):
    #     return inventory.has_item(items.MallowRecruit)
    # elif world.settings.is_flag_value(flags.SeaGate, SeaGating.geno):
    #     return inventory.has_item(items.GenoRecruit)
    # elif world.settings.is_flag_value(flags.SeaGate, SeaGating.bowser):
    #     return inventory.has_item(items.BowserRecruit)
    # elif world.settings.is_flag_value(flags.SeaGate, SeaGating.toadstool):
    if world.settings.is_flag_value(flags.SeaGate, SeaGating.toadstool):
        return inventory.has_item(items.ToadstoolRecruit)
    # elif world.settings.is_flag_value(flags.SeaGate, SeaGating.star1):
    #     return inventory.has_item(items.StarPiece)
    # elif world.settings.is_flag_value(flags.SeaGate, SeaGating.star2):
    #     return inventory.has_item_count(items.StarPiece, 2)
    # elif world.settings.is_flag_value(flags.SeaGate, SeaGating.star3):
    #     return inventory.has_item_count(items.StarPiece, 3)
    elif world.settings.is_flag_value(flags.SeaGate, SeaGating.star4):
        return inventory.has_item_count(items.StarPiece, 4)
    # elif world.settings.is_flag_value(flags.SeaGate, SeaGating.star5):
    #     return inventory.has_item_count(items.StarPiece, 5)
    # elif world.settings.is_flag_value(flags.SeaGate, SeaGating.star6):
    #     return inventory.has_item_count(items.StarPiece, 6)
    elif world.settings.is_flag_value(flags.SeaGate, SeaGating.bundt):
        return inventory.has_item(items.BundtBossFight)
    else:
        return True


def can_clear_ship_midboss(world, inventory):
    return can_access_sea(
        world, inventory
    )  # and world.get_check_instance(KingCalamariBossFightLocation).item is not None


def can_clear_ship(world, inventory):
    return can_clear_ship_midboss(
        world, inventory
    )  # and world.get_check_instance(JohnnyBossFightLocation).item is not None


def can_access_yaridovich(world, inventory):
    if world.settings.is_flag_value(flags.YaridovichGate, YaridovichGating.ship):
        return can_clear_ship(world, inventory)
    elif world.settings.is_flag_value(flags.YaridovichGate, YaridovichGating.johnny):
        return inventory.has_item(items.JohnnyBossFight)
    else:
        return True


def can_clear_seaside(world, inventory):
    return can_access_yaridovich(
        world, inventory
    )  # and world.get_check_instance(YaridovichBossFightLocation).item is not None


def can_access_temple(world, inventory):
    if world.settings.is_flag_value(flags.BelomeTempleGate, BelomeTempleGating.seaside):
        return can_access_yaridovich(world, inventory)
    elif world.settings.is_flag_value(flags.BelomeTempleGate, BelomeTempleGating.yarid):
        return inventory.has_item(items.YaridovichBossFight)
    else:
        return True


def can_clear_temple(world, inventory):
    return can_access_temple(
        world, inventory
    )  # and world.get_check_instance(Belome2BossFightLocation).item is not None


def can_access_monstro_town(world, inventory):
    if world.settings.is_flag_value(flags.MonstroTownGate, MonstroTownGating.landsend):
        return can_clear_temple(world, inventory)
    elif world.settings.is_flag_value(flags.MonstroTownGate, MonstroTownGating.belome2):
        return inventory.has_item(items.Belome2BossFight)
    else:
        return True


def can_dojo_1(world, inventory):
    return can_access_monstro_town(
        world, inventory
    )  # and world.get_check_instance(JaggerBossFightLocation).item is not None


def can_dojo_2(world, inventory):
    return can_dojo_1(
        world, inventory
    )  # and world.get_check_instance(Jinx1BossFightLocation).item is not None


def can_dojo_3(world, inventory):
    return can_dojo_2(
        world, inventory
    )  # and world.get_check_instance(Jinx2BossFightLocation).item is not None


def can_dojo_4(world, inventory):
    return can_dojo_3(
        world, inventory
    )  # and world.get_check_instance(Jinx3BossFightLocation).item is not None


def can_access_culex(world, inventory):
    item_reqs = False
    if world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.shuffle1):
        item_reqs = inventory.has_item(items.Fireworks) and can_clear_mines(
            world, inventory
        )
    elif world.settings.is_flag_value(
        flags.FireworksSetting, FireworksOptions.progressive
    ):
        item_reqs = inventory.has_item_count(items.ProgressiveFireworks, 2)
    else:
        item_reqs = can_clear_mines(world, inventory)
    return item_reqs and can_access_monstro_town(world, inventory)


def can_clear_culex(world, inventory):
    return can_access_culex(
        world, inventory
    )  # and world.get_check_instance(CulexBossFightLocation).item is not None


def can_access_invisible_flags(world, inventory):
    if not world.settings.is_flag_enabled(flags.SkipMustyFearsSequence):
        return can_access_monstro_town(world, inventory)
    else:
        return True


def can_clear_nimbus_midboss(world, inventory):
    """

    Args:
        inventory (randomizer.logic.keys.Inventory):

    Returns:
        bool: True if this location is accessible with the given inventory, False otherwise.

    """
    # Castle Key 1 is needed to access this location.
    return inventory.has_item(
        items.CastleKey1
    )  # and world.get_check_instance(BirdettaBossFightLocation).item is not None


def can_access_nimbus_boss(world, inventory):
    return can_clear_nimbus_midboss(world, inventory) and inventory.has_item(
        items.CastleKey2
    )


def can_clear_nimbus_castle(world, inventory):
    """

    Args:
        inventory (randomizer.logic.keys.Inventory):

    Returns:
        bool: True if this location is accessible with the given inventory, False otherwise.

    """
    # Castle Key 2 is needed to access this location, plus defeating Birdo.
    return can_access_nimbus_boss(
        world, inventory
    )  # and world.get_check_instance(ValentinaBossFightLocation).item is not None


def can_access_volcano(world, inventory):
    if world.settings.is_flag_value(
        flags.BarrelVolcanoGate, BarrelVolcanoGating.nimbus
    ):
        return can_clear_nimbus_castle(world, inventory)
    elif world.settings.is_flag_value(
        flags.BarrelVolcanoGate, BarrelVolcanoGating.valentina
    ):
        return inventory.has_item(items.ValentinaBossFight)
    else:
        return True


def can_clear_volcano_midboss(world, inventory):
    return can_access_volcano(
        world, inventory
    )  # and world.get_check_instance(CzarDragonBossFightLocation).item is not None


def can_clear_volcano(world, inventory):
    return can_clear_volcano_midboss(
        world, inventory
    )  # and world.get_check_instance(AxemRangersBossFightLocation).item is not None


def can_access_keep(world, inventory):
    if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.volcano):
        return can_clear_volcano(world, inventory)
    # elif world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.star1):
    #     return inventory.has_item(items.StarPiece)
    # elif world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.star2):
    #     return inventory.has_item_count(items.StarPiece, 2)
    # elif world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.star3):
    #     return inventory.has_item_count(items.StarPiece, 3)
    # elif world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.star4):
    #     return inventory.has_item_count(items.StarPiece, 4)
    # elif world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.star5):
    #     return inventory.has_item_count(items.StarPiece, 5)
    elif world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.star6):
        return inventory.has_item_count(items.StarPiece, 6)
    elif world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.axem):
        return inventory.has_item(items.AxemRangersBossFight)
    else:
        return True


def can_pass_chester(world, inventory):
    if world.settings.is_flag_enabled(flags.BowserDoorShuffle):
        return can_access_keep(
            world, inventory
        )  # and world.get_check_instance(ChesterBossFightLocation).item is not None
    return can_access_keep(world, inventory)


def can_clear_doors(world, inventory):
    if world.settings.is_flag_value(flags.BowserDoorRequirements, 6):
        return can_pass_chester(world, inventory)
    return can_access_keep(world, inventory)


def can_beat_magikoopa(world, inventory):
    return can_clear_doors(
        world, inventory
    )  # and world.get_check_instance(MagikoopaBossFightLocation).item is not None


def can_beat_boomer(world, inventory):
    return can_beat_magikoopa(
        world, inventory
    )  # and world.get_check_instance(BoomerBossFightLocation).item is not None


def can_beat_exor(world, inventory):
    return can_beat_boomer(
        world, inventory
    )  # and world.get_check_instance(ExorBossFightLocation).item is not None


def can_access_factory(world, inventory):
    # if world.settings.is_flag_value(flags.FactoryGate, FactoryGating.star1):
    #     return inventory.has_item(items.StarPiece) and can_access_keep(world, inventory)
    # elif world.settings.is_flag_value(flags.FactoryGate, FactoryGating.star2):
    #     return inventory.has_item_count(items.StarPiece, 2) and can_access_keep(world, inventory)
    # elif world.settings.is_flag_value(flags.FactoryGate, FactoryGating.star3):
    #     return inventory.has_item_count(items.StarPiece, 3) and can_access_keep(world, inventory)
    # elif world.settings.is_flag_value(flags.FactoryGate, FactoryGating.star4):
    #     return inventory.has_item_count(items.StarPiece, 4) and can_access_keep(world, inventory)
    # elif world.settings.is_flag_value(flags.FactoryGate, FactoryGating.star5):
    #     return inventory.has_item_count(items.StarPiece, 5) and can_access_keep(world, inventory)
    # elif world.settings.is_flag_value(flags.FactoryGate, FactoryGating.star6):
    if world.settings.is_flag_value(flags.FactoryGate, FactoryGating.star6):
        return inventory.has_item_count(items.StarPiece, 6) and can_beat_exor(
            world, inventory
        )
    elif world.settings.is_flag_value(flags.FactoryGate, FactoryGating.exor):
        return inventory.has_item(items.ExorBossFight) and can_beat_exor(
            world, inventory
        )
    else:
        return can_beat_exor(world, inventory)


def can_clear_countdown(world, inventory):
    return can_access_factory(
        world, inventory
    )  # and world.get_check_instance(CountDownBossFightLocation).item is not None


def can_clear_snakes(world, inventory):
    return can_clear_countdown(
        world, inventory
    )  # and world.get_check_instance(CloakerDominoBossFightLocation).item is not None


def can_clear_clerk(world, inventory):
    return can_clear_snakes(
        world, inventory
    )  # and world.get_check_instance(ClerkBossFightLocation).item is not None


def can_clear_manager(world, inventory):
    return can_clear_clerk(
        world, inventory
    )  # and world.get_check_instance(ManagerBossFightLocation).item is not None


def can_clear_director(world, inventory):
    return can_clear_manager(
        world, inventory
    )  # and world.get_check_instance(DirectorBossFightLocation).item is not None


def can_clear_chief(world, inventory):
    return can_clear_director(
        world, inventory
    )  # and world.get_check_instance(GunyolkBossFightLocation).item is not None


def can_access_final_boss(world, inventory):
    value = world.settings.get_flag(flags.StarPiecesRequired).value
    has_stars = inventory.has_item_count(items.StarPiece, value)
    if world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.shuffle1):
        fireworks_access = inventory.has_item(items.ProgressiveFireworks)
    elif world.settings.is_flag_value(
        flags.FireworksSetting, FireworksOptions.progressive
    ):
        fireworks_access = inventory.has_item_count(items.ProgressiveFireworks, 3)
    can_access_bucket = (
        fireworks_access
        and can_clear_mines(world, inventory)
        and world.settings.is_flag_value(flags.BucketWarp, False)
    )
    can_access_casino = world.settings.is_flag_value(
        flags.CasinoWarp, True
    ) and inventory.has_item(items.BrightCard)
    return has_stars and (
        can_access_bucket or can_access_casino or can_clear_chief(world, inventory)
    )


def can_clear_final_boss(world, inventory):
    return can_access_final_boss(
        world, inventory
    )  # and world.get_check_instance(SmithyBossFightLocation).item is not None


# ******* Chest location classes


class Chest(locations.ItemLocation):
    """Subclass for treasure chest location."""

    access = 1
    shopsanity = False
    coinsanity = False
    manual_70A7 = False
    dialogs_to_replace = []
    nearby_star_rooms = []

    def item_allowed(self, item):
        # If scaling boss stats, it would defeat the purpose of the setting if a mimic chest with Box Boy's stats could appear in the earlygame.
        # Place some restrictions on where the mimics can appear.
        if self.world.settings.is_flag_value(
            flags.MimicsAnywhere, True
        ) and self.world.settings.is_flag_value(
            flags.BossShuffleScaleStats, BossScaleOptions.match
        ):
            if isclass_or_instance(item, items.PandoriteFight) and self.area in [
                locations.Area.MushroomWay,
                locations.Area.MushroomKingdom,
            ]:
                return False
            elif isclass_or_instance(item, items.HidonFight) and self.area in [
                locations.Area.MushroomWay,
                locations.Area.MushroomKingdom,
                locations.Area.BanditsWay,
                locations.Area.KeroSewers,
                locations.Area.RoseWay,
                locations.Area.RoseTown,
                locations.Area.ForestMaze,
                locations.Area.Moleville,
                locations.Area.MolevilleMines,
                locations.Area.PipeVault,
                locations.Area.YosterIsle,
            ]:
                return False
            elif isclass_or_instance(item, items.BoxBoyFight) and self.area in [
                locations.Area.MushroomWay,
                locations.Area.MushroomKingdom,
                locations.Area.BanditsWay,
                locations.Area.KeroSewers,
                locations.Area.RoseWay,
                locations.Area.RoseTown,
                locations.Area.ForestMaze,
                locations.Area.Moleville,
                locations.Area.MolevilleMines,
                locations.Area.BoosterPass,
                locations.Area.BoosterTower,
                locations.Area.PipeVault,
                locations.Area.YosterIsle,
                locations.Area.Marrymore,
                locations.Area.Sea,
                locations.Area.SunkenShip,
            ]:
                return False

        if (
            self.area
            not in [
                locations.Area.MushroomWay,
                locations.Area.BanditsWay,
                locations.Area.KeroSewers,
                locations.Area.RoseWay,
                locations.Area.ForestMaze,
                locations.Area.MolevilleMines,
                locations.Area.BoosterTower,
                locations.Area.Sea,
                locations.Area.SunkenShip,
                locations.Area.LandsEnd,
                locations.Area.NimbusLand,
                locations.Area.BarrelVolcano,
            ]
            and isclass_or_instance(item, items.InvincibilityStar)
        ):
            return False

        return super().item_allowed(item)


class SlotsNotAllowedChest(Chest):
    def item_allowed(self, item):
        # restricted for graphical reasons
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.SlotMachineChest
        )


class CoinsNotAllowedChest(SlotsNotAllowedChest):
    def item_allowed(self, item):
        # restricted for graphical reasons
        return (
            super().item_allowed(item)
            and not isclass_or_instance(item, items.InfiniteCoins)
            and not isclass_or_instance(item, items.FrogCoin)
            and not (
                self.world.settings.is_flag_value(flags.QuickHitCoins, False)
                and (
                    isclass_or_instance(item, items.Coins)
                    or isclass_or_instance(item, items.MultiFrogCoin)
                )
            )
        )


# ******* NPC reward data classes


class NPCReward(locations.ItemLocation):
    """Subclass for NPC reward location."""

    access = 1
    dialogs_to_replace = []

    def item_allowed(self, item):
        # NPC rewards cannot contain "You Missed!" or chest-only rewards.
        return super().item_allowed(item) and not isclass_or_instance(
            item,
            (
                items.MimicFight,
                items.SlotMachineChest,
                items.Flower,
                items.YouMissed,
                items.InvincibilityStar,
                items.InfiniteCoins,
            ),
        )


class StarterItem(NPCReward):
    def item_allowed(self, item):
        return super().item_allowed(item) and item.consumable == True


class TreasureSellerReward(NPCReward):
    """Subclass for Moleville treasure seller NPC to check access.  Need to beat mines to unlock this."""

    shopsanity = True

    def item_allowed(self, item):
        # update this when shuffle modes integrated
        return (
            super().item_allowed(item)
            and not (isclass_or_instance(item, items.MultiFrogCoin))
            and not (isclass_or_instance(item, items.FrogCoin))
            and not (isclass_or_instance(item, items.Coins))
            and (
                item.unique == ItemUnique.Always
                or item.unique == ItemUnique.BalancedOnly
            )
        )

    def can_access(self, inventory):
        return can_clear_mines(self.world, inventory)


class FrogCoinShopItem(NPCReward):
    shopsanity = True
    key = False

    def item_allowed(self, item):
        # update this when shuffle modes integrated
        return (
            super().item_allowed(item)
            and not (item.price == 0)
            and not (isclass_or_instance(item, items.MultiFrogCoin))
            and not (isclass_or_instance(item, items.Beetlemania))
            and not (isclass_or_instance(item, items.FrogCoin))
            and not (isclass_or_instance(item, items.Coins))
            and not item.is_key
            and (
                item.is_equipment
                or item.unique == ItemUnique.Always
                or item.unique == ItemUnique.BalancedOnly
            )
        )


# ******* Overworld item classes


class OverworldItem(locations.ItemLocation):
    """Subclass for NPC reward location."""

    access = 1

    coinsanity = True
    npc_ids = None
    dialogs_to_replace = []
    prefer_packet = None

    def force_packet(self):
        # Makes this item spawn as a packet NPC
        return (
            self.prefer_packet is not None
            and not self.is_vanilla
            and not (
                (
                    isclass_or_instance(self.item, items.Coins)
                    or isclass_or_instance(self.item, items.FrogCoin)
                )
                and (
                    isclass_or_instance(self.original_item, items.Coins)
                    or isclass_or_instance(self.original_item, items.FrogCoin)
                )
            )
        )

    def item_allowed(self, item):
        # NPC rewards cannot contain "You Missed!" or chest-only rewards.
        # FIXME: Non-KI NPC rewards don't work with progressive cards for now.  Remove this when fixed.

        return (
            super().item_allowed(item)
            and not (
                isclass_or_instance(item, items.Coins) and item.amount not in [1, 10]
            )
            and not isclass_or_instance(
                item,
                (
                    items.MimicFight,
                    items.SlotMachineChest,
                    items.MultiFrogCoin,
                    items.YouMissed,
                    items.InvincibilityStar,
                    items.InfiniteCoins,
                ),
            )
        )

    @property
    def is_vanilla(self):
        return (
            super().is_vanilla
            or (
                isclass_or_instance(self.item, items.Coins)
                and isclass_or_instance(self.original_item, items.Coins)
            )
            or (
                isclass_or_instance(self.item, items.FrogCoin)
                and isclass_or_instance(self.original_item, items.FrogCoin)
            )
        )


class PacketType(enum.Enum):
    """Enumeration for items that may need to be restricted by how many times they can appear."""

    Falling = enum.auto()
    Static = enum.auto()
    Chest = enum.auto()


class PacketItem(OverworldItem):
    """Subclass for NPC reward location."""

    script_id = None
    preferred = PacketType.Static

    def item_allowed(self, item):
        # NPC rewards cannot contain "You Missed!" or chest-only rewards.
        # FIXME: Non-KI NPC rewards don't work with progressive cards for now.  Remove this when fixed.

        return super().item_allowed(item) and not isclass_or_instance(
            item, (items.Coins, items.FrogCoin)
        )


class MidasRiverTunnelItem(OverworldItem):
    midas_action_script = None

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.RecoveryMushroom
        )


class BelomeTempleTreasure(OverworldItem):
    """Subclass for Belome Temple rewards."""

    def can_access(self, inventory):
        return inventory.has_item(items.TempleKey)


# ******* Boss star piece classes


class BossStarPiece(locations.ItemLocation):
    """Subclass for boss star piece location."""

    shopsanity = False
    coinsanity = False
    dialogs_to_replace = []
    item = None
    original_item = None
    star_location = True

    def item_allowed(self, item):
        # Can only be Star Piece, or empty
        return isclass_or_instance(item, items.StarPiece) or item == None


# ******* "3 Musty Fears Flags Anywhere"


class InvisibleFlagLocation(NPCReward):
    item = None
    original_item = None
    coords = (0, 0, 0)
    shift = (0, 0)
    clue = ""
    key = True
    access = 2

    def can_access(self, inventory):
        return can_access_invisible_flags(self.world, inventory)


# ******* Character recruitment classes


class CharacterRecruit(locations.ItemLocation):
    """Subclass for character recruit location."""

    shopsanity = False
    coinsanity = False
    dialogs_to_replace = []
    item = None
    original_item = None
    npcs = []
    credits_npcs = []
    is_character_recruit = True
    doll_npcs = []

    def item_allowed(self, item):
        # Can only be character
        return isclass_or_instance(item, items.RecruitedCharacter) or item == None


class CharacterSpotted(locations.ItemLocation):
    """Subclass for character recruit location."""

    shopsanity = False
    coinsanity = False
    dialogs_to_replace = []
    item = None
    original_item = None

    def item_allowed(self, item):
        # Can only be corresponding character
        return isclass_or_instance(item, items.SpottedCharacter)


class StarterCharacterRecruit(CharacterRecruit):
    pass


# ******* Boss fight location classes


class BossFightLocation(locations.ItemLocation):
    related_class = None
    is_boss_fight = True

    def item_allowed(self, item):
        return isclass_or_instance(item, items.BossFight)


# ******* Spell learner classes


class CharacterSpellSlot(locations.ItemLocation):
    is_spell_slot = True

    def item_allowed(self, item):
        return isclass_or_instance(item, items.SpellLearn)


# ****************************** Actual chest classes

# *** Spells


class MarioSpell(CharacterSpellSlot):
    def can_access(self, inventory):
        return inventory.has_item(items.MarioRecruit)

    def item_allowed(self, item):
        if not super().item_allowed(item):
            return False
        existing_spell_checks = [
            self.world.get_check_instance(c)
            for c in [
                MarioSpell1,
                MarioSpell2,
                MarioSpell3,
                MarioSpell4,
                MarioSpell5,
                MarioSpell6,
            ]
        ]
        existing_spells = [c.item for c in existing_spell_checks if c.item is not None]
        for spell in existing_spells:
            if type(spell) == type(item):
                return False
        return True


class NonBaseMarioSpell(MarioSpell):
    def can_access(
        self, inventory
    ):  # prohibit non-1st spell being filled before required spell placements have been placed in a 1st char spell slot
        if (
            self.world.settings.is_flag_enabled(flags.ExperienceNoRegular)
            and self.world.get_check_instance(MarioSpell1).item is None
        ):
            return False
        return super().can_access(inventory)


class MarioSpell1(MarioSpell):
    item = items.JumpLearn
    original_item = items.JumpLearn


class MarioSpell2(NonBaseMarioSpell):
    item = items.FireOrbLearn
    original_item = items.FireOrbLearn


class MarioSpell3(NonBaseMarioSpell):
    item = items.SuperJumpLearn
    original_item = items.SuperJumpLearn


class MarioSpell4(NonBaseMarioSpell):
    item = items.SuperFlameLearn
    original_item = items.SuperFlameLearn


class MarioSpell5(NonBaseMarioSpell):
    item = items.UltraJumpLearn
    original_item = items.UltraJumpLearn


class MarioSpell6(NonBaseMarioSpell):
    item = items.UltraFlameLearn
    original_item = items.UltraFlameLearn


class MallowSpell(CharacterSpellSlot):
    def can_access(self, inventory):
        return inventory.has_item(items.MallowRecruit)

    def item_allowed(self, item):
        if not super().item_allowed(item):
            return False
        existing_spell_checks = [
            self.world.get_check_instance(c)
            for c in [
                MallowSpell1,
                MallowSpell2,
                MallowSpell3,
                MallowSpell4,
                MallowSpell5,
                MallowSpell6,
            ]
        ]
        existing_spells = [c.item for c in existing_spell_checks if c.item is not None]
        # print(existing_spells)
        for spell in existing_spells:
            if type(spell) == type(item):
                return False
        return True


class NonBaseMallowSpell(MallowSpell):
    def can_access(
        self, inventory
    ):  # prohibit non-1st spell being filled before required spell placements have been placed in a 1st char spell slot
        if (
            self.world.settings.is_flag_enabled(flags.ExperienceNoRegular)
            and self.world.get_check_instance(MallowSpell1).item is None
        ):
            return False
        return super().can_access(inventory)


class MallowSpell1(MallowSpell):
    item = items.ThunderboltLearn
    original_item = items.ThunderboltLearn


class MallowSpell2(NonBaseMallowSpell):
    item = items.HPRainLearn
    original_item = items.HPRainLearn


class MallowSpell3(NonBaseMallowSpell):
    item = items.PsychopathLearn
    original_item = items.PsychopathLearn


class MallowSpell4(NonBaseMallowSpell):
    item = items.ShockerLearn
    original_item = items.ShockerLearn


class MallowSpell5(NonBaseMallowSpell):
    item = items.SnowyLearn
    original_item = items.SnowyLearn


class MallowSpell6(NonBaseMallowSpell):
    item = items.StarRainLearn
    original_item = items.StarRainLearn


class GenoSpell(CharacterSpellSlot):
    def can_access(self, inventory):
        return inventory.has_item(items.GenoRecruit)

    def item_allowed(self, item):
        if not super().item_allowed(item):
            return False
        existing_spell_checks = [
            self.world.get_check_instance(c)
            for c in [
                GenoSpell1,
                GenoSpell2,
                GenoSpell3,
                GenoSpell4,
                GenoSpell5,
                GenoSpell6,
            ]
        ]
        existing_spells = [c.item for c in existing_spell_checks if c.item is not None]
        for spell in existing_spells:
            if type(spell) == type(item):
                return False
        return True


class NonBaseGenoSpell(GenoSpell):
    def can_access(
        self, inventory
    ):  # prohibit non-1st spell being filled before required spell placements have been placed in a 1st char spell slot
        if (
            self.world.settings.is_flag_enabled(flags.ExperienceNoRegular)
            and self.world.get_check_instance(GenoSpell1).item is None
        ):
            return False
        return super().can_access(inventory)


class GenoSpell1(GenoSpell):
    item = items.GenoBeamLearn
    original_item = items.GenoBeamLearn


class GenoSpell2(NonBaseGenoSpell):
    item = items.GenoBoostLearn
    original_item = items.GenoBoostLearn


class GenoSpell3(NonBaseGenoSpell):
    item = items.GenoWhirlLearn
    original_item = items.GenoWhirlLearn


class GenoSpell4(NonBaseGenoSpell):
    item = items.GenoBlastLearn
    original_item = items.GenoBlastLearn


class GenoSpell5(NonBaseGenoSpell):
    item = items.GenoFlashLearn
    original_item = items.GenoFlashLearn


class GenoSpell6(NonBaseGenoSpell):
    item = None
    original_item = None


class BowserSpell(CharacterSpellSlot):
    def can_access(self, inventory):
        return inventory.has_item(items.BowserRecruit)

    def item_allowed(self, item):
        if not super().item_allowed(item):
            return False
        existing_spell_checks = [
            self.world.get_check_instance(c)
            for c in [
                BowserSpell1,
                BowserSpell2,
                BowserSpell3,
                BowserSpell4,
                BowserSpell5,
                BowserSpell6,
            ]
        ]
        existing_spells = [c.item for c in existing_spell_checks if c.item is not None]
        for spell in existing_spells:
            if type(spell) == type(item):
                return False
        return True


class NonBaseBowserSpell(BowserSpell):
    def can_access(
        self, inventory
    ):  # prohibit non-1st spell being filled before required spell placements have been placed in a 1st char spell slot
        if (
            self.world.settings.is_flag_enabled(flags.ExperienceNoRegular)
            and self.world.get_check_instance(BowserSpell1).item is None
        ):
            return False
        return super().can_access(inventory)


class BowserSpell1(BowserSpell):
    item = items.TerrorizeLearn
    original_item = items.TerrorizeLearn


class BowserSpell2(NonBaseBowserSpell):
    item = items.PoisonGasLearn
    original_item = items.PoisonGasLearn


class BowserSpell3(NonBaseBowserSpell):
    item = items.CrusherLearn
    original_item = items.CrusherLearn


class BowserSpell4(NonBaseBowserSpell):
    item = items.BowserCrushLearn
    original_item = items.BowserCrushLearn


class BowserSpell5(NonBaseBowserSpell):
    item = None
    original_item = None


class BowserSpell6(NonBaseBowserSpell):
    item = None
    original_item = None


class ToadstoolSpell(CharacterSpellSlot):
    def can_access(self, inventory):
        return inventory.has_item(items.ToadstoolRecruit)

    def item_allowed(self, item):
        if not super().item_allowed(item):
            return False
        existing_spell_checks = [
            self.world.get_check_instance(c)
            for c in [
                ToadstoolSpell1,
                ToadstoolSpell2,
                ToadstoolSpell3,
                ToadstoolSpell4,
                ToadstoolSpell5,
                ToadstoolSpell6,
            ]
        ]
        existing_spells = [c.item for c in existing_spell_checks if c.item is not None]
        for spell in existing_spells:
            if type(spell) == type(item):
                return False
        return True


class NonBaseToadstoolSpell(ToadstoolSpell):
    def can_access(
        self, inventory
    ):  # prohibit non-1st spell being filled before required spell placements have been placed in a 1st char spell slot
        if (
            self.world.settings.is_flag_enabled(flags.ExperienceNoRegular)
            and self.world.get_check_instance(ToadstoolSpell1).item is None
        ):
            return False
        return super().can_access(inventory)


class ToadstoolSpell1(ToadstoolSpell):
    item = items.TherapyLearn
    original_item = items.TherapyLearn


class ToadstoolSpell2(NonBaseToadstoolSpell):
    item = items.GroupHugLearn
    original_item = items.GroupHugLearn


class ToadstoolSpell3(NonBaseToadstoolSpell):
    item = items.SleepyTimeLearn
    original_item = items.SleepyTimeLearn


class ToadstoolSpell4(NonBaseToadstoolSpell):
    item = items.ComeBackLearn
    original_item = items.ComeBackLearn


class ToadstoolSpell5(NonBaseToadstoolSpell):
    item = items.MuteLearn
    original_item = items.MuteLearn


class ToadstoolSpell6(NonBaseToadstoolSpell):
    item = items.PsychBombLearn
    original_item = items.PsychBombLearn


# *** Marios Pad


class StarterCharacter1(StarterCharacterRecruit):
    area = locations.Area.MariosPad
    description = ShuffleLocationSelector.StarterCharacter1.value
    item = items.MarioRecruit
    original_item = items.MarioRecruit
    event = 192
    npcs = [(179, 0, [], [])]


class StarterCharacter2(StarterCharacterRecruit):
    area = locations.Area.MariosPad
    description = ShuffleLocationSelector.StarterCharacter2.value
    event = 192


class StarterCharacter3(StarterCharacterRecruit):
    area = locations.Area.MariosPad
    description = ShuffleLocationSelector.StarterCharacter3.value
    event = 192


class StarterCharacter4(StarterCharacterRecruit):
    area = locations.Area.MariosPad
    description = ShuffleLocationSelector.StarterCharacter4.value
    event = 192


class StarterCharacter5(StarterCharacterRecruit):
    area = locations.Area.MariosPad
    description = ShuffleLocationSelector.StarterCharacter5.value
    event = 192


class MariosPadBed(NPCReward):
    description = ShuffleLocationSelector.MariosPadBed.value
    area = locations.Area.MariosPad
    item = items.DryBonesFlag
    original_item = items.DryBonesFlag
    rooms = [189]
    event = 253
    key = True

    def item_allowed(self, item):
        if self.world.settings.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

    def can_access(self, inventory):
        return can_access_invisible_flags(self.world, inventory)


class MariosPadStarter1(StarterItem):
    description = ShuffleLocationSelector.MariosPadStarter1.value
    area = locations.Area.MariosPad
    item = items.Mushroom
    original_item = items.Mushroom
    rooms = [189]
    event = 252


class MariosPadStarter2(StarterItem):
    description = ShuffleLocationSelector.MariosPadStarter2.value
    area = locations.Area.MariosPad
    item = items.Mushroom
    original_item = items.Mushroom
    rooms = [189]
    event = 251


class MariosPadStarter3(StarterItem):
    description = ShuffleLocationSelector.MariosPadStarter3.value
    area = locations.Area.MariosPad
    item = items.Mushroom
    original_item = items.Mushroom
    rooms = [189]
    event = 250


class MariosPadStarter4(StarterItem):
    description = ShuffleLocationSelector.MariosPadStarter4.value
    area = locations.Area.MariosPad
    item = items.Mushroom
    original_item = items.Mushroom
    rooms = [189]
    event = 249


# *** Mushroom Way


class MushroomWayCharacterSpotted(CharacterSpotted):
    area = locations.Area.MushroomWay
    description = ShuffleLocationSelector.MushroomWayCharacter.value
    item = items.MallowSpotted
    original_item = items.MallowSpotted


class MushroomWay1(Chest):
    description = ShuffleLocationSelector.MushroomWay1.value
    area = locations.Area.MushroomWay
    item = items.Coins(5)
    original_item = items.Coins(5)
    rooms = [203]
    npc_ids = [0]
    event = 247


class MushroomWay2(Chest):
    description = ShuffleLocationSelector.MushroomWay2.value
    area = locations.Area.MushroomWay
    item = items.Coins(8)
    original_item = items.Coins(8)
    rooms = [203]
    npc_ids = [1]
    event = 246


class MushroomWay3(Chest):
    description = ShuffleLocationSelector.MushroomWay3.value
    area = locations.Area.MushroomWay
    item = items.Flower
    original_item = items.Flower
    rooms = [204]
    npc_ids = [0]
    event = 247


class MushroomWay4(Chest):
    description = ShuffleLocationSelector.MushroomWay4.value
    area = locations.Area.MushroomWay
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom
    rooms = [204]
    npc_ids = [1]
    event = 246

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class ToadRescue1(NPCReward):
    description = ShuffleLocationSelector.ToadRescue1.value
    area = locations.Area.MushroomWay
    item = items.HoneySyrup
    original_item = items.HoneySyrup
    missable = True
    rooms = [203]
    event = 253


class ToadRescue2(NPCReward):
    description = ShuffleLocationSelector.ToadRescue2.value
    area = locations.Area.MushroomWay
    item = items.FlowerTab
    original_item = items.FlowerTab
    missable = True
    rooms = [204]
    event = 253


class HammerBrosBossFightLocation(BossFightLocation):
    related_class = bosses.HammerBros
    description = AvailableBosses.HammerBro.value
    area = locations.Area.MushroomWay
    item = items.HammerBroBossFight
    original_item = items.HammerBroBossFight
    rooms = [205]
    event = 353


class HammerBrosReward(NPCReward):
    description = ShuffleLocationSelector.HammerBrosReward.value
    area = locations.Area.MushroomWay
    item = items.Hammer
    original_item = items.Hammer
    rooms = [205]
    event = 253

    def can_access(self, inventory):
        return can_clear_mushroom_way(self.world, inventory)


class MushroomWayCharacter(CharacterRecruit):
    area = locations.Area.MushroomWay
    description = ShuffleLocationSelector.MushroomWayCharacter.value
    item = items.MallowRecruit
    original_item = items.MallowRecruit
    rooms = [205]
    event = 186
    npcs = [
        (203, 8, [], []),
        (204, 7, [], []),
        (205, 5, [], []),
    ]
    credits_npcs = [
        (269, 0, [3804], []),
        (496, 20, [3885], []),
        (88, 2, [3950], []),
        (375, 1, [3951], []),
    ]

    def can_access(self, inventory):
        return can_clear_mushroom_way(self.world, inventory)


class MushroomWayStarPiece(BossStarPiece):
    area = locations.Area.MushroomWay
    description = ShuffleLocationSelector.MushroomWayStarPiece.value
    rooms = [205]
    event = 167

    def can_access(self, inventory):
        return can_clear_mushroom_way(self.world, inventory)


# *** Mushroom Kingdom


class MushroomKingdomHallway(Chest):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.MushroomKingdomHallway.value
    item = items.FrogCoin
    original_item = items.FrogCoin
    rooms = [17, 325]
    npc_ids = [2, 6]
    event = 247


class MushroomKingdomVault1(Chest):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.MushroomKingdomVault1.value
    rooms = [31]
    npc_ids = [0]
    event = 247
    item = items.Coins10
    original_item = items.Coins10


class MushroomKingdomVault2(Chest):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.MushroomKingdomVault2.value
    rooms = [31]
    npc_ids = [1]
    event = 246
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom


class MushroomKingdomVault3(Chest):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.MushroomKingdomVault3.value
    rooms = [31]
    npc_ids = [2]
    event = 245
    item = items.Flower
    original_item = items.Flower


class MushroomKingdomStoreBasement1(Chest):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.MushroomKingdomStoreBasement1.value
    rooms = [492]
    npc_ids = [0]
    event = 247
    item = items.Flower
    original_item = items.Flower


class MushroomKingdomStoreBasement2(Chest):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.MushroomKingdomStoreBasement2.value
    rooms = [492]
    npc_ids = [1]
    event = 246
    item = items.Flower
    original_item = items.Flower


class PeachSurprise(NPCReward):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.PeachSurprise.value
    item = items.Mushroom
    original_item = items.Mushroom
    rooms = [20, 328]
    event = 253


class MushroomKingdomStore(NPCReward):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.MushroomKingdomStore.value
    rooms = [483, 491]
    event = 253
    item = items.PickMeUp
    original_item = items.PickMeUp


# *** Bandit's Way


class BanditsWay1(Chest):
    description = ShuffleLocationSelector.BanditsWay1.value
    area = locations.Area.BanditsWay
    rooms = [207]
    npc_ids = [9]
    event = 247
    item = items.KerokeroCola
    original_item = items.KerokeroCola

    def can_access(self, inventory):
        return can_access_bandits_way(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BanditsWayCoin1(OverworldItem):
    description = ShuffleLocationSelector.BanditsWayCoin1.value
    area = locations.Area.BanditsWay
    rooms = [207]
    event = 239
    npc_ids = [3]
    item = items.Coins1
    original_item = items.Coins1

    def can_access(self, inventory):
        return can_access_bandits_way(self.world, inventory)


class BanditsWayCoin2(OverworldItem):
    description = ShuffleLocationSelector.BanditsWayCoin2.value
    area = locations.Area.BanditsWay
    rooms = [207]
    event = 240
    npc_ids = [4]
    item = items.Coins1
    original_item = items.Coins1

    def can_access(self, inventory):
        return can_access_bandits_way(self.world, inventory)


class BanditsWayCoin3(OverworldItem):
    description = ShuffleLocationSelector.BanditsWayCoin3.value
    area = locations.Area.BanditsWay
    rooms = [207]
    event = 241
    npc_ids = [5]
    item = items.Coins1
    original_item = items.Coins1

    def can_access(self, inventory):
        return can_access_bandits_way(self.world, inventory)


class BanditsWay2(Chest):
    description = ShuffleLocationSelector.BanditsWay2.value
    area = locations.Area.BanditsWay
    rooms = [77]
    npc_ids = [0]
    event = 247
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom

    def can_access(self, inventory):
        return can_access_bandits_way(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BanditsWayStarChest(CoinsNotAllowedChest):
    description = ShuffleLocationSelector.BanditsWayStarChest.value
    area = locations.Area.BanditsWay
    rooms = [78]
    npc_ids = [0]
    event = 247
    item = items.BanditsWayStar
    original_item = items.BanditsWayStar

    def can_access(self, inventory):
        return can_access_bandits_way(self.world, inventory)


class BanditsWayDogJump(CoinsNotAllowedChest):
    description = ShuffleLocationSelector.BanditsWayDogJump.value
    rooms = [78]
    npc_ids = [1]
    event = 246
    area = locations.Area.BanditsWay
    item = items.Flower
    original_item = items.Flower

    def can_access(self, inventory):
        return can_access_bandits_way(self.world, inventory)


class BanditsWayCroco(SlotsNotAllowedChest):
    description = ShuffleLocationSelector.BanditsWayCroco.value
    area = locations.Area.BanditsWay
    rooms = [206]
    npc_ids = [0]
    event = 247
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom

    def can_access(self, inventory):
        return can_access_bandits_way(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class Croco1BossFightLocation(BossFightLocation):
    related_class = bosses.Croco1
    description = AvailableBosses.Croco1.value
    area = locations.Area.BanditsWay
    item = items.Croco1BossFight
    original_item = items.Croco1BossFight
    rooms = [206]
    event = 353

    def can_access(self, inventory):
        return can_access_bandits_way(self.world, inventory)


class Croco1Reward(NPCReward):
    description = ShuffleLocationSelector.Croco1Reward.value
    area = locations.Area.BanditsWay
    rooms = [206]
    event = 253
    item = items.RareFrogCoin
    original_item = items.RareFrogCoin
    key = True

    def item_allowed(self, item):
        if self.world.settings.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

    def can_access(self, inventory):
        return can_clear_bandits_way(self.world, inventory)


class Croco1Reward2(NPCReward):
    description = ShuffleLocationSelector.Croco1Reward2.value
    area = locations.Area.BanditsWay
    rooms = [206]
    event = 252
    item = items.Wallet
    original_item = items.Wallet

    def can_access(self, inventory):
        return can_clear_bandits_way(self.world, inventory)


class BanditsWayStarPiece(BossStarPiece):
    area = locations.Area.BanditsWay
    description = ShuffleLocationSelector.BanditsWayStarPiece.value
    rooms = [206]
    event = 167

    def can_access(self, inventory):
        return can_clear_bandits_way(self.world, inventory)


# Invasion


class InvasionVault1(Chest):
    area = locations.Area.MushroomKingdomOccupiedOnly
    description = ShuffleLocationSelector.InvasionVault1.value
    item = items.Coins10
    original_item = items.Coins10
    rooms = [331]
    npc_ids = [0]
    event = 247
    missable = True
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(
            flags.BanditsWayGate, BanditsWayGating.open
        ) or world.settings.is_flag_value(
            flags.BanditsWayGate, BanditsWayGating.mushroomway
        ):
            self.access = 1

    def can_access(self, inventory):
        return can_clear_bandits_way(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class InvasionVault2(Chest):
    area = locations.Area.MushroomKingdomOccupiedOnly
    description = ShuffleLocationSelector.InvasionVault2.value
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom
    rooms = [331]
    npc_ids = [1]
    event = 246
    missable = True
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(
            flags.BanditsWayGate, BanditsWayGating.open
        ) or world.settings.is_flag_value(
            flags.BanditsWayGate, BanditsWayGating.mushroomway
        ):
            self.access = 1

    def can_access(self, inventory):
        return can_clear_bandits_way(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class InvasionVault3(Chest):
    area = locations.Area.MushroomKingdomOccupiedOnly
    description = ShuffleLocationSelector.InvasionVault3.value
    item = items.Flower
    original_item = items.Flower
    rooms = [331]
    npc_ids = [2]
    event = 245
    missable = True
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(
            flags.BanditsWayGate, BanditsWayGating.open
        ) or world.settings.is_flag_value(
            flags.BanditsWayGate, BanditsWayGating.mushroomway
        ):
            self.access = 1

    def can_access(self, inventory):
        return can_clear_bandits_way(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class InvasionEasternGuard(NPCReward):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.InvasionEasternGuard.value
    rooms = [190]
    event = 253
    item = items.Coins10
    original_item = items.Coins10
    missable = True
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(
            flags.BanditsWayGate, BanditsWayGating.open
        ) or world.settings.is_flag_value(
            flags.BanditsWayGate, BanditsWayGating.mushroomway
        ):
            self.access = 1

    def can_access(self, inventory):
        return can_clear_bandits_way(self.world, inventory)


class WalletGuy1(NPCReward):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.WalletGuy1.value
    rooms = [190, 191]
    event = 252
    item = items.FlowerTab
    original_item = items.FlowerTab
    missable = True
    access = 2

    def can_access(self, inventory):
        return can_clear_bandits_way(self.world, inventory)


class WalletGuy2(NPCReward):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.WalletGuy2.value
    rooms = [190, 191]
    event = 251
    item = items.FrogCoin
    original_item = items.FrogCoin
    missable = True
    access = 2

    def can_access(self, inventory):
        return can_clear_bandits_way(self.world, inventory) and can_access_marrymore(
            self.world, inventory
        )


class InvasionToadRescue(NPCReward):
    description = ShuffleLocationSelector.InvasionToadRescue.value
    item = items.FlowerTab
    original_item = items.FlowerTab
    missable = True
    rooms = [20, 328]
    event = 252
    access = 2

    def can_access(self, inventory):
        return can_clear_bandits_way(self.world, inventory)


class InvasionFamily(NPCReward):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.InvasionFamily.value
    rooms = [480, 481]
    event = 253
    item = items.FlowerTab
    original_item = items.FlowerTab
    missable = True
    access = 2

    def can_access(self, inventory):
        return can_clear_bandits_way(self.world, inventory)


class InvasionGuestRoom(NPCReward):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.InvasionGuestRoom.value
    rooms = [330]
    event = 253
    item = items.WakeUpPin
    original_item = items.WakeUpPin
    missable = True
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(
            flags.BanditsWayGate, BanditsWayGating.open
        ) or world.settings.is_flag_value(
            flags.BanditsWayGate, BanditsWayGating.mushroomway
        ):
            self.access = 1

    def can_access(self, inventory):
        return can_clear_bandits_way(self.world, inventory)


class MackBossFightLocation(BossFightLocation):
    related_class = bosses.Mack
    description = AvailableBosses.Mack.value
    area = locations.Area.MushroomKingdom
    item = items.MackBossFight
    original_item = items.MackBossFight
    rooms = [326]
    event = 353

    def can_access(self, inventory):
        return can_clear_bandits_way(self.world, inventory)


class InvasionStarPiece(BossStarPiece):
    description = ShuffleLocationSelector.InvasionStarPiece.value
    area = locations.Area.MushroomKingdom
    rooms = [18]
    event = 167
    item = items.StarPiece1
    original_item = items.StarPiece1

    def can_access(self, inventory):
        return can_clear_invasion(self.world, inventory)


class MushroomKingdomStoreExchange(NPCReward):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.MushroomKingdomStoreExchange.value
    rooms = [483, 491]
    event = 252
    item = items.CricketPie
    original_item = items.CricketPie
    key = True
    access = 2

    def item_allowed(self, item):
        if self.world.settings.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

    def can_access(self, inventory):
        return can_clear_invasion(self.world, inventory) and inventory.has_item(
            items.RareFrogCoin
        )


class MushroomKingdomInn(NPCReward):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.MushroomKingdomInn.value
    rooms = [493]
    event = 253
    item = items.Beetlemania
    original_item = items.Beetlemania
    access = 2
    key = True

    def can_access(self, inventory):
        return can_clear_invasion(self.world, inventory)


# *** Kero Sewers


class KeroSewersPandoriteRoom(Chest):
    description = ShuffleLocationSelector.KeroSewersPandoriteRoom.value
    area = locations.Area.KeroSewers
    item = items.Flower
    original_item = items.Flower
    rooms = [60]
    npc_ids = [0]
    event = 247

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class PandoriteChest(Chest):
    description = ShuffleLocationSelector.PandoriteChest.value
    area = locations.Area.KeroSewers
    item = items.PandoriteFight
    original_item = items.PandoriteFight
    rooms = [60]
    npc_ids = [1]
    event = 246

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class PandoriteBossFightLocation(BossFightLocation):
    related_class = bosses.Pandorite
    description = AvailableBosses.Pandorite.value
    item = items.PandoriteBossFight
    original_item = items.PandoriteBossFight
    rooms = [512]
    event = 353

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.MimicsAnywhere, False):
            self.area = locations.Area.KeroSewers

    def can_access(self, inventory):
        return inventory.has_item(items.PandoriteFight)


class PandoriteBoss(BossStarPiece):
    description = ShuffleLocationSelector.PandoriteBoss.value
    rooms = [512]
    event = 167

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.MimicsAnywhere, False):
            self.area = locations.Area.KeroSewers

    def can_access(self, inventory):
        return can_beat_mimic_1(self.world, inventory)


class PandoriteReward1(NPCReward):
    description = ShuffleLocationSelector.PandoriteReward1.value
    item = items.TrueformPin
    original_item = items.TrueformPin
    rooms = [512]
    event = 253
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.MimicsAnywhere, False):
            self.area = locations.Area.KeroSewers

    def can_access(self, inventory):
        return can_beat_mimic_1(self.world, inventory)


class PandoriteReward2(Chest):
    description = ShuffleLocationSelector.PandoriteReward2.value
    item = items.Coins(50)
    original_item = items.Coins(50)
    rooms = [512]
    manual_70A7 = True
    event = 245
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.MimicsAnywhere, False):
            self.area = locations.Area.KeroSewers

    def can_access(self, inventory):
        return can_beat_mimic_1(self.world, inventory)

    def item_allowed(self, item):
        return (
            super().item_allowed(item)
            and not isclass_or_instance(item, items.MimicFight)
            and not isclass_or_instance(item, items.SlotMachineChest)
            and not isclass_or_instance(item, items.InvincibilityStar)
            and not isclass_or_instance(item, items.InfiniteCoins)
        )


class KeroSewersStarChest(Chest):
    description = ShuffleLocationSelector.KeroSewersStarChest.value
    area = locations.Area.KeroSewers
    item = items.KeroSewersStar
    original_item = items.KeroSewersStar
    rooms = [59]
    npc_ids = [0]
    event = 247


class KeroSewersBeforeBelomeLower(Chest):
    description = ShuffleLocationSelector.KeroSewersBeforeBelomeLower.value
    area = locations.Area.KeroSewers
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom
    rooms = [301]
    npc_ids = [0]
    event = 247

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class KeroSewersBeforeBelomeUpper1(Chest):
    description = ShuffleLocationSelector.KeroSewersBeforeBelomeUpper1.value
    area = locations.Area.KeroSewers
    item = items.Flower
    original_item = items.Flower
    npc_ids = [1]
    rooms = [301]
    event = 246
    missable = True

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class KeroSewersBeforeBelomeUpper2(Chest):
    description = ShuffleLocationSelector.KeroSewersBeforeBelomeUpper2.value
    area = locations.Area.KeroSewers
    item = items.CricketJam
    original_item = items.CricketJam
    rooms = [301]
    event = 245
    manual_70A7 = True
    key = True

    def item_allowed(self, item):
        if self.world.settings.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class Belome1BossFightLocation(BossFightLocation):
    related_class = bosses.Belome1
    description = AvailableBosses.Belome1.value
    area = locations.Area.KeroSewers
    item = items.Belome1BossFight
    original_item = items.Belome1BossFight
    rooms = [302]
    event = 353


class KeroSewersBoss(BossStarPiece):
    description = ShuffleLocationSelector.KeroSewersBoss.value
    area = locations.Area.KeroSewers
    rooms = [301]
    event = 167

    def can_access(self, inventory):
        return self.world.get_check_instance(Belome1BossFightLocation).item is not None


# *** Midas River


class MidasRiverFirstTime(NPCReward):
    description = ShuffleLocationSelector.MidasRiverFirstTime.value
    area = locations.Area.MidasRiver
    item = items.NokNokShell
    original_item = items.NokNokShell
    rooms = [67]
    event = 253


class MidasRiverBottomLeftCave(MidasRiverTunnelItem):
    description = ShuffleLocationSelector.MidasRiverBottomLeftCave.value
    area = locations.Area.MidasRiver
    item = items.FrogCoin
    original_item = items.FrogCoin
    midas_action_script = 43
    rooms = [72]
    event = 241
    npc_ids = [1]


class MidasRiverBottomRightCave(MidasRiverTunnelItem):
    description = ShuffleLocationSelector.MidasRiverBottomRightCave.value
    area = locations.Area.MidasRiver
    item = items.Flower
    original_item = items.Flower
    midas_action_script = 333
    rooms = [73]
    event = 241
    npc_ids = [4]


# *** Tadpole Pond


class CricketPieReward(NPCReward):
    description = ShuffleLocationSelector.CricketPieReward.value
    area = locations.Area.TadpolePond
    item = items.FroggieStick
    original_item = items.FroggieStick
    rooms = [75]
    event = 253
    special_equip = True

    def can_access(self, inventory):
        return inventory.has_item(items.CricketPie)


class CricketJamReward(NPCReward):
    description = ShuffleLocationSelector.CricketJamReward.value
    area = locations.Area.TadpolePond
    rooms = [75]
    event = 252
    item = items.MultiFrogCoin(NPCReward, 10)
    original_item = items.MultiFrogCoin(NPCReward, 10)

    def can_access(self, inventory):
        return inventory.has_item(items.CricketJam) and inventory.has_item(
            items.CricketPie
        )


class MelodyBay1(NPCReward):
    description = ShuffleLocationSelector.MelodyBay1.value
    area = locations.Area.TadpolePond
    item = items.ProgressiveCard
    original_item = items.ProgressiveCard
    rooms = [74]
    event = 253
    key = True

    def item_allowed(self, item):
        if self.world.settings.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)


class MelodyBay2(NPCReward):
    description = ShuffleLocationSelector.MelodyBay2.value
    area = locations.Area.TadpolePond
    item = items.ProgressiveCard
    original_item = items.ProgressiveCard
    rooms = [74]
    event = 252
    key = True
    access = 2

    def item_allowed(self, item):
        if self.world.settings.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

    def can_access(self, inventory):
        return can_clear_mines(self.world, inventory)


class MelodyBay3(NPCReward):
    description = ShuffleLocationSelector.MelodyBay3.value
    area = locations.Area.TadpolePond
    item = items.ProgressiveCard
    original_item = items.ProgressiveCard
    rooms = [74]
    event = 251
    key = True
    access = 2

    def item_allowed(self, item):
        if self.world.settings.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

    def can_access(self, inventory):
        return can_clear_mines(self.world, inventory) and can_clear_temple(
            self.world, inventory
        )


# *** Rose Way


class RoseWayPlatform(Chest):
    description = ShuffleLocationSelector.RoseWayPlatform.value
    area = locations.Area.RoseWay
    rooms = [80]
    npc_ids = [0]
    event = 247
    item = items.FrogCoin
    original_item = items.FrogCoin

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class RoseWayFlower(OverworldItem):
    description = ShuffleLocationSelector.RoseWayFlower.value
    area = locations.Area.RoseWay
    item = items.Flower
    original_item = items.Flower
    rooms = [79]
    event = 241
    npc_ids = [7]


class RoseWayMushroom(OverworldItem):
    description = ShuffleLocationSelector.RoseWayMushroom.value
    area = locations.Area.RoseWay
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom
    rooms = [79]
    event = 240
    npc_ids = [8]


class RoseWayCoin1(OverworldItem):
    description = ShuffleLocationSelector.RoseWayCoin1.value
    area = locations.Area.RoseWay
    item = items.Coins10
    original_item = items.Coins10
    rooms = [79]
    event = 235
    npc_ids = [17]


class RoseWayCoin2(OverworldItem):
    description = ShuffleLocationSelector.RoseWayCoin2.value
    area = locations.Area.RoseWay
    item = items.Coins10
    original_item = items.Coins10
    rooms = [79]
    event = 236
    npc_ids = [18]


class RoseWayCoin3(OverworldItem):
    description = ShuffleLocationSelector.RoseWayCoin3.value
    area = locations.Area.RoseWay
    item = items.Coins10
    original_item = items.Coins10
    rooms = [79]
    event = 237
    npc_ids = [19]


class RoseWayCoin4(OverworldItem):
    description = ShuffleLocationSelector.RoseWayCoin4.value
    area = locations.Area.RoseWay
    item = items.Coins10
    original_item = items.Coins10
    rooms = [79]
    event = 238
    npc_ids = [20]


class RoseWayCoin5(OverworldItem):
    description = ShuffleLocationSelector.RoseWayCoin5.value
    area = locations.Area.RoseWay
    item = items.Coins10
    original_item = items.Coins10
    rooms = [79]
    event = 239
    npc_ids = [21]


class RoseWayFiveChests1(Chest):
    description = ShuffleLocationSelector.RoseWayFiveChests1.value
    area = locations.Area.RoseWay
    rooms = [81]
    npc_ids = [0]
    event = 247
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom


class RoseWayFiveChests2(Chest):
    description = ShuffleLocationSelector.RoseWayFiveChests2.value
    area = locations.Area.RoseWay
    rooms = [81]
    npc_ids = [1]
    event = 246
    item = items.Coins(5)
    original_item = items.Coins(5)


class RoseWayFiveChests3(Chest):
    description = ShuffleLocationSelector.RoseWayFiveChests3.value
    area = locations.Area.RoseWay
    rooms = [81]
    npc_ids = [2]
    event = 245
    item = items.Coins(5)
    original_item = items.Coins(5)


class RoseWayFiveChests4(Chest):
    description = ShuffleLocationSelector.RoseWayFiveChests4.value
    area = locations.Area.RoseWay
    rooms = [81]
    npc_ids = [3]
    event = 244
    item = items.Coins(5)
    original_item = items.Coins(5)


class RoseWayFiveChests5(Chest):
    description = ShuffleLocationSelector.RoseWayFiveChests5.value
    area = locations.Area.RoseWay
    rooms = [81]
    npc_ids = [4]
    event = 243
    item = items.Coins(5)
    original_item = items.Coins(5)


# *** Rose Town


class RoseTownFlag(NPCReward):
    description = ShuffleLocationSelector.RoseTownFlag.value
    rooms = [83, 84]
    event = 253
    area = locations.Area.RoseTown
    item = items.GreaperFlag
    original_item = items.GreaperFlag
    key = True

    def item_allowed(self, item):
        if self.world.settings.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

    def can_access(self, inventory):
        return can_access_invisible_flags(self.world, inventory)


class RoseTownStore1(Chest):
    area = locations.Area.RoseTown
    description = ShuffleLocationSelector.RoseTownStore1.value
    rooms = [87]
    npc_ids = [4]
    event = 247
    item = items.Flower
    original_item = items.Flower


class RoseTownStore2(Chest):
    area = locations.Area.RoseTown
    description = ShuffleLocationSelector.RoseTownStore2.value
    rooms = [87]
    npc_ids = [5]
    event = 246
    item = items.FrogCoin
    original_item = items.FrogCoin


class GardenerCloud1(Chest):
    area = locations.Area.RoseTown
    description = ShuffleLocationSelector.GardenerCloud1.value
    rooms = [419]
    npc_ids = [0]
    event = 247
    item = items.LazyShellArmor
    original_item = items.LazyShellArmor
    access = 2
    special_equip = True

    def can_access(self, inventory):
        return (
            can_clear_marrymore(self.world, inventory)
            and can_clear_forest(self.world, inventory)
            and inventory.has_item(items.Seed)
            and inventory.has_item(items.Fertilizer)
        )


class GardenerCloud2(Chest):
    area = locations.Area.RoseTown
    description = ShuffleLocationSelector.GardenerCloud2.value
    rooms = [419]
    npc_ids = [1]
    event = 246
    item = items.LazyShellWeapon
    original_item = items.LazyShellWeapon
    access = 2
    special_equip = True

    def can_access(self, inventory):
        return (
            can_clear_marrymore(self.world, inventory)
            and can_clear_forest(self.world, inventory)
            and inventory.has_item(items.Seed)
            and inventory.has_item(items.Fertilizer)
        )


class RoseTownToad(NPCReward):
    description = ShuffleLocationSelector.RoseTownToad.value
    area = locations.Area.RoseTown
    rooms = [95, 96]
    event = 253
    item = items.FlowerTab
    original_item = items.FlowerTab


class Gaz(NPCReward):
    area = locations.Area.RoseTown
    description = ShuffleLocationSelector.Gaz.value
    rooms = [86]
    event = 253
    item = items.FingerShot
    original_item = items.FingerShot
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_clear_forest(self.world, inventory)


class RoseTownTreasureHouse1(Chest):
    description = ShuffleLocationSelector.RoseTownTreasureHouse1.value
    area = locations.Area.RoseTown
    rooms = [93, 94]
    npc_ids = [0, 0]
    event = 247
    item = items.Flower
    original_item = items.Flower


class RoseTownTreasureHouse2(Chest):
    description = ShuffleLocationSelector.RoseTownTreasureHouse2.value
    area = locations.Area.RoseTown
    rooms = [93, 94]
    npc_ids = [1, 1]
    event = 246
    item = items.Flower
    original_item = items.Flower


class RoseTownTreasureHouseMazeReward(NPCReward):
    description = ShuffleLocationSelector.RoseTownTreasureHouseMazeReward.value
    area = locations.Area.RoseTown
    rooms = [93, 94]
    event = 253
    item = items.FrogCoin
    original_item = items.FrogCoin
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_access_forest(self.world, inventory)


class RoseTownTreasureHouse3(Chest):
    description = ShuffleLocationSelector.RoseTownTreasureHouse3.value
    area = locations.Area.RoseTown
    rooms = [97, 98]
    npc_ids = [1, 1]
    event = 247
    item = items.FrogCoin
    original_item = items.FrogCoin

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.Flower
        )  # flower is broken in this chest for some reason


# *** Forest Maze


class ForestMaze1(Chest):
    description = ShuffleLocationSelector.ForestMaze1.value
    area = locations.Area.ForestMaze
    rooms = [224]
    npc_ids = [2]
    event = 247
    item = items.KerokeroCola
    original_item = items.KerokeroCola

    def can_access(self, inventory):
        return can_access_forest(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class ForestMaze2(Chest):
    description = ShuffleLocationSelector.ForestMaze2.value
    area = locations.Area.ForestMaze
    rooms = [228]
    npc_ids = [2]
    event = 247
    item = items.FrogCoin
    original_item = items.FrogCoin

    def can_access(self, inventory):
        return can_access_forest(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class ForestMazeUnderground1(CoinsNotAllowedChest):
    description = ShuffleLocationSelector.ForestMazeUnderground1.value
    area = locations.Area.ForestMaze
    rooms = [242]
    npc_ids = [2]
    event = 247
    item = items.KerokeroCola
    original_item = items.KerokeroCola
    manual_70A7 = True

    def can_access(self, inventory):
        return can_access_forest(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class ForestMazeUnderground2(CoinsNotAllowedChest):
    description = ShuffleLocationSelector.ForestMazeUnderground2.value
    area = locations.Area.ForestMaze
    rooms = [242]
    npc_ids = [3]
    event = 246
    item = items.Flower
    original_item = items.Flower
    manual_70A7 = True

    def can_access(self, inventory):
        return can_access_forest(self.world, inventory)


class ForestMazeUnderground3(CoinsNotAllowedChest):
    description = ShuffleLocationSelector.ForestMazeUnderground3.value
    area = locations.Area.ForestMaze
    rooms = [242]
    npc_ids = [4]
    event = 245
    item = items.YouMissed
    original_item = items.YouMissed
    manual_70A7 = True

    def can_access(self, inventory):
        return can_access_forest(self.world, inventory)


class ForestMazeRedEssence(Chest):
    description = ShuffleLocationSelector.ForestMazeRedEssence.value
    area = locations.Area.ForestMaze
    rooms = [227]
    npc_ids = [4]
    event = 247
    item = items.RedEssence
    original_item = items.RedEssence

    def can_access(self, inventory):
        return can_access_forest(self.world, inventory)


class ForestMazeSecret1(Chest):
    description = ShuffleLocationSelector.ForestMazeSecret1.value
    area = locations.Area.ForestMaze
    rooms = [234]
    npc_ids = [1]
    event = 247
    item = items.FrogCoin
    original_item = items.FrogCoin

    def can_access(self, inventory):
        return can_access_forest(self.world, inventory)


class ForestMazeSecret2(Chest):
    description = ShuffleLocationSelector.ForestMazeSecret2.value
    area = locations.Area.ForestMaze
    rooms = [234]
    npc_ids = [2]
    event = 246
    item = items.Flower
    original_item = items.Flower

    def can_access(self, inventory):
        return can_access_forest(self.world, inventory)


class ForestMazeSecret3(Chest):
    description = ShuffleLocationSelector.ForestMazeSecret3.value
    area = locations.Area.ForestMaze
    rooms = [234]
    npc_ids = [3]
    event = 245
    item = items.Flower
    original_item = items.Flower

    def can_access(self, inventory):
        return can_access_forest(self.world, inventory)


class ForestMazeSecret4(Chest):
    description = ShuffleLocationSelector.ForestMazeSecret4.value
    area = locations.Area.ForestMaze
    rooms = [234]
    npc_ids = [4]
    event = 244
    item = items.Flower
    original_item = items.Flower

    def can_access(self, inventory):
        return can_access_forest(self.world, inventory)


class ForestMazeSecret5(Chest):
    description = ShuffleLocationSelector.ForestMazeSecret5.value
    area = locations.Area.ForestMaze
    rooms = [234]
    npc_ids = [5]
    event = 243
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom

    def can_access(self, inventory):
        return can_access_forest(self.world, inventory)


class BowyerBossFightLocation(BossFightLocation):
    related_class = bosses.Bowyer
    description = AvailableBosses.Bowyer.value
    area = locations.Area.ForestMaze
    item = items.BowyerBossFight
    original_item = items.BowyerBossFight
    rooms = [232]
    event = 353

    def can_access(self, inventory):
        return can_access_forest(self.world, inventory)


class ForestMazeCharacter(CharacterRecruit):
    area = locations.Area.ForestMaze
    description = ShuffleLocationSelector.ForestMazeCharacter.value
    item = items.GenoRecruit
    original_item = items.GenoRecruit
    rooms = [232]
    event = 186
    npcs = [(230, 11, [], [488]), (232, 10, [2448], [])]
    credits_npcs = [(496, 21, [3885], [])]
    doll_npcs = [(496, 22, [3885], []), (88, 3, [3950], []), (375, 2, [3951], [])]

    def can_access(self, inventory):
        return can_clear_forest(self.world, inventory)


class ForestMazeBoss(BossStarPiece):
    area = locations.Area.ForestMaze
    description = ShuffleLocationSelector.ForestMazeBoss.value
    rooms = [232]
    event = 167
    item = items.StarPiece2
    original_item = items.StarPiece2

    def can_access(self, inventory):
        return can_clear_forest(self.world, inventory)


# *** Pipe Vault


class PipeVaultSlide1(Chest):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.PipeVaultSlide1.value
    rooms = [125]
    npc_ids = [8]
    event = 245
    item = items.Flower
    original_item = items.Flower

    def can_access(self, inventory):
        return can_access_pipe_vault(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class PipeVaultSlide2(Chest):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.PipeVaultSlide2.value
    rooms = [125]
    npc_ids = [9]
    event = 246
    item = items.FrogCoin
    original_item = items.FrogCoin

    def can_access(self, inventory):
        return can_access_pipe_vault(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class PipeVaultSlide3(Chest):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.PipeVaultSlide3.value
    rooms = [125]
    npc_ids = [10]
    event = 247
    item = items.FrogCoin
    original_item = items.FrogCoin

    def can_access(self, inventory):
        return can_access_pipe_vault(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class PipeVaultSlideCoin1(OverworldItem):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.PipeVaultSlideCoin1.value
    rooms = [125]
    event = 237
    item = items.Coins1
    original_item = items.Coins1
    npc_ids = [0]

    def can_access(self, inventory):
        return can_access_pipe_vault(self.world, inventory)


class PipeVaultSlideCoin2(OverworldItem):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.PipeVaultSlideCoin2.value
    rooms = [125]
    event = 238
    item = items.Coins1
    original_item = items.Coins1
    npc_ids = [1]

    def can_access(self, inventory):
        return can_access_pipe_vault(self.world, inventory)


class PipeVaultSlideCoin3(OverworldItem):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.PipeVaultSlideCoin3.value
    rooms = [125]
    event = 239
    item = items.Coins1
    original_item = items.Coins1
    npc_ids = [2]

    def can_access(self, inventory):
        return can_access_pipe_vault(self.world, inventory)


class PipeVaultSlideCoin4(OverworldItem):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.PipeVaultSlideCoin4.value
    rooms = [125]
    event = 240
    item = items.Coins1
    original_item = items.Coins1
    npc_ids = [3]

    def can_access(self, inventory):
        return can_access_pipe_vault(self.world, inventory)


class PipeVaultSlideCoin5(OverworldItem):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.PipeVaultSlideCoin5.value
    rooms = [125]
    event = 241
    item = items.Coins1
    original_item = items.Coins1
    npc_ids = [4]

    def can_access(self, inventory):
        return can_access_pipe_vault(self.world, inventory)


class PipeVaultSlideFrogCoin(OverworldItem):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.PipeVaultSlideFrogCoin.value
    rooms = [125]
    event = 236
    item = items.FrogCoin
    original_item = items.FrogCoin
    npc_ids = [5]
    prefer_packet = True

    def can_access(self, inventory):
        return can_access_pipe_vault(self.world, inventory)


class PipeVaultNippers1(Chest):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.PipeVaultNippers1.value
    rooms = [128]
    npc_ids = [0]
    event = 247
    item = items.Flower
    original_item = items.Flower
    npc_ids = [6]

    def can_access(self, inventory):
        return can_access_pipe_vault(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class PipeVaultNippers2(Chest):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.PipeVaultNippers2.value
    rooms = [128]
    npc_ids = [1]
    event = 246
    item = items.Coins(20)
    original_item = items.Coins(20)

    def can_access(self, inventory):
        return can_access_pipe_vault(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class GoombaThumping1(NPCReward):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.GoombaThumping1.value
    rooms = [143]
    event = 253
    item = items.FlowerTab
    original_item = items.FlowerTab

    def can_access(self, inventory):
        return can_access_pipe_vault(self.world, inventory)


class GoombaThumping2(NPCReward):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.GoombaThumping2.value
    rooms = [143]
    event = 252
    item = items.FlowerJar
    original_item = items.FlowerJar

    def can_access(self, inventory):
        return can_access_pipe_vault(self.world, inventory)


# *** Yo'ster Isle


class YosterIsleEntrance(Chest):
    description = ShuffleLocationSelector.YosterIsleEntrance.value
    area = locations.Area.YosterIsle
    rooms = [33]
    npc_ids = [1]
    item = items.FrogCoin
    original_item = items.FrogCoin
    event = 247

    def can_access(self, inventory):
        return can_access_pipe_vault(self.world, inventory)


class YosterIsleRaceReward1(NPCReward):
    description = ShuffleLocationSelector.YosterIsleRaceReward1.value
    area = locations.Area.YosterIsle
    rooms = [34]
    item = items.YoshiCookie
    original_item = items.YoshiCookie
    event = 253

    def can_access(self, inventory):
        return can_access_pipe_vault(self.world, inventory)


class YosterIsleRaceReward2(NPCReward):
    description = ShuffleLocationSelector.YosterIsleRaceReward2.value
    area = locations.Area.YosterIsle
    rooms = [34]
    item = items.YoshiCookie
    original_item = items.YoshiCookie
    event = 251

    def can_access(self, inventory):
        return can_access_pipe_vault(self.world, inventory)


class YosterIsleRaceReward3(NPCReward):
    description = ShuffleLocationSelector.YosterIsleRaceReward3.value
    area = locations.Area.YosterIsle
    rooms = [34]
    item = items.YoshiCookie
    original_item = items.YoshiCookie
    event = 250

    def can_access(self, inventory):
        return can_access_pipe_vault(self.world, inventory)


class YosterIsleFlag(NPCReward):
    description = ShuffleLocationSelector.YosterIsleFlag.value
    area = locations.Area.YosterIsle
    rooms = [34]
    item = items.BigBooFlag
    original_item = items.BigBooFlag
    event = 252
    key = True

    def item_allowed(self, item):
        if self.world.settings.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

    def can_access(self, inventory):
        return can_access_pipe_vault(
            self.world, inventory
        ) and can_access_invisible_flags(self.world, inventory)


# *** Moleville


class BucketGirl(NPCReward):
    description = ShuffleLocationSelector.BucketGirl.value
    area = locations.Area.Moleville
    rooms = [108]
    event = 253
    item = items.FrogCoin
    original_item = items.FrogCoin
    dialogs_to_replace = [2911]
    access = 2

    def item_allowed(self, item):
        if self.world.settings.is_flag_value(
            flags.FireworksSetting, FireworksOptions.vanilla
        ) or self.world.settings.is_flag_value(flags.BucketWarp, True):
            return False
        return super().item_allowed(item)

    def can_access(self, inventory):
        fireworks_access = can_clear_mines(self.world, inventory)
        if self.world.settings.is_flag_value(
            flags.FireworksSetting, FireworksOptions.shuffle1
        ):
            fireworks_access = fireworks_access and inventory.has_item(items.Fireworks)
        elif self.world.settings.is_flag_value(
            flags.FireworksSetting, FireworksOptions.progressive
        ):
            fireworks_access = fireworks_access and inventory.has_item_count(
                items.ProgressiveFireworks, 3
            )
        return fireworks_access and self.world.settings.is_flag_value(
            flags.BucketWarp, False
        )


class TreasureSeller1(TreasureSellerReward):
    description = ShuffleLocationSelector.TreasureSeller1.value
    area = locations.Area.Moleville
    rooms = [336]
    event = 253
    item = items.LuckyJewel
    original_item = items.LuckyJewel
    dialogs_to_replace = [2911]
    access = 2

    def can_access(self, inventory):
        return can_clear_mines(self.world, inventory)


class TreasureSeller2(TreasureSellerReward):
    description = ShuffleLocationSelector.TreasureSeller2.value
    area = locations.Area.Moleville
    rooms = [336]
    event = 252
    item = items.ProgressiveEgg
    original_item = items.ProgressiveEgg
    dialogs_to_replace = [2908]
    access = 2

    def can_access(self, inventory):
        return can_clear_mines(self.world, inventory) and can_clear_seaside(
            self.world, inventory
        )


class TreasureSeller3(TreasureSellerReward):
    description = ShuffleLocationSelector.TreasureSeller3.value
    area = locations.Area.Moleville
    rooms = [336]
    event = 251
    item = items.FryingPan
    original_item = items.FryingPan
    dialogs_to_replace = [2914]
    access = 2

    def can_access(self, inventory):
        return can_clear_mines(self.world, inventory) and can_clear_volcano(
            self.world, inventory
        )


class FireworksShop(NPCReward):
    # Fireworks shuffle/progressive ONLY
    description = ShuffleLocationSelector.FireworksShop.value
    area = locations.Area.Moleville
    rooms = [339]
    event = 253
    item = items.Fireworks
    original_item = items.Fireworks
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if self.world.settings.is_flag_value(
            flags.FireworksSetting, FireworksOptions.progressive
        ):
            self.item = items.ProgressiveFireworks
        elif self.world.settings.is_flag_value(
            flags.FireworksSetting, FireworksOptions.shuffle1
        ):
            self.key = True

    def item_allowed(self, item):
        if self.world.settings.is_flag_value(flags.KeyItemsAnywhere, False) and (
            self.world.settings.is_flag_value(
                flags.FireworksSetting, FireworksOptions.shuffle1
            )
            or self.world.settings.is_flag_value(
                flags.FireworksSetting, FireworksOptions.progressive
            )
        ):
            return super().item_allowed(item) and item.is_key
        else:
            return super().item_allowed(item)

    def can_access(self, inventory):
        return can_clear_mines(self.world, inventory)


# *** Moleville Mines


class CrocoFlunkie1(NPCReward):
    description = ShuffleLocationSelector.CrocoFlunkie1.value
    area = locations.Area.MolevilleMines
    rooms = [273]
    event = 253
    item = items.FlowerTab
    original_item = items.FlowerTab
    missable = True

    def can_access(self, inventory):
        return can_access_moleville_entrance(self.world, inventory)


class CrocoFlunkie2(NPCReward):
    description = ShuffleLocationSelector.CrocoFlunkie2.value
    area = locations.Area.MolevilleMines
    rooms = [277]
    event = 253
    item = items.FlowerTab
    original_item = items.FlowerTab
    missable = True

    def can_access(self, inventory):
        return can_access_moleville_entrance(self.world, inventory)


class CrocoFlunkie3(NPCReward):
    description = ShuffleLocationSelector.CrocoFlunkie3.value
    area = locations.Area.MolevilleMines
    rooms = [283]
    event = 253
    item = items.FlowerTab
    original_item = items.FlowerTab
    missable = True

    def can_access(self, inventory):
        return can_access_moleville_entrance(self.world, inventory)


class Croco2BossFightLocation(BossFightLocation):
    related_class = bosses.Croco2
    description = AvailableBosses.Croco2.value
    area = locations.Area.MolevilleMines
    item = items.Croco2BossFight
    original_item = items.Croco2BossFight
    rooms = [518]
    event = 353

    def can_access(self, inventory):
        return can_access_moleville_entrance(self.world, inventory)


class Croco2Item(NPCReward):
    description = ShuffleLocationSelector.Croco2Item.value
    area = locations.Area.MolevilleMines
    rooms = [518]
    event = 253
    item = items.BambinoBomb
    original_item = items.BambinoBomb
    key = True

    def item_allowed(self, item):
        if self.world.settings.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

    def can_access(self, inventory):
        return (
            can_access_moleville_entrance(self.world, inventory)
            and self.world.get_check_instance(Croco2BossFightLocation).item is not None
        )


class MolevilleMinesBoss1(BossStarPiece):
    description = ShuffleLocationSelector.MolevilleMinesBoss1.value
    area = locations.Area.MolevilleMines
    rooms = [518]
    event = 167

    def can_access(self, inventory):
        return (
            can_access_moleville_entrance(self.world, inventory)
            and self.world.get_check_instance(Croco2BossFightLocation).item is not None
        )


class MolevilleMinesStarChest(Chest):
    description = ShuffleLocationSelector.MolevilleMinesStarChest.value
    area = locations.Area.MolevilleMines
    rooms = [285]
    npc_ids = [0]
    event = 247
    item = items.MolevilleMinesStar
    original_item = items.MolevilleMinesStar
    access = 2

    def can_access(self, inventory):
        return can_access_moleville_entrance(
            self.world, inventory
        ) and inventory.has_item(items.BambinoBomb)


class MolevilleMinesShyGuy(PacketItem):
    area = locations.Area.MolevilleMines
    description = ShuffleLocationSelector.MolevilleMinesShyGuy.value
    rooms = [286]
    event = 241
    script_id = 3412
    item = items.FrogCoin
    original_item = items.FrogCoin
    access = 2

    def can_access(self, inventory):
        return can_access_moleville_entrance(
            self.world, inventory
        ) and inventory.has_item(items.BambinoBomb)


class MolevilleMinesCoins(Chest):
    description = ShuffleLocationSelector.MolevilleMinesCoins.value
    area = locations.Area.MolevilleMines
    rooms = [280]
    npc_ids = [0]
    event = 247
    item = items.Coins(150)
    original_item = items.Coins(150)
    access = 2

    def can_access(self, inventory):
        return can_access_moleville_entrance(
            self.world, inventory
        ) and inventory.has_item(items.BambinoBomb)


class MolevilleMinesPunchinello1(Chest):
    description = ShuffleLocationSelector.MolevilleMinesPunchinello1.value
    area = locations.Area.MolevilleMines
    rooms = [288]
    npc_ids = [0]
    event = 247
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom
    access = 2

    def can_access(self, inventory):
        return can_access_moleville_entrance(
            self.world, inventory
        ) and inventory.has_item(items.BambinoBomb)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class MolevilleMinesPunchinello2(Chest):
    description = ShuffleLocationSelector.MolevilleMinesPunchinello2.value
    area = locations.Area.MolevilleMines
    rooms = [288]
    npc_ids = [1]
    event = 246
    item = items.Flower
    original_item = items.Flower
    access = 2

    def can_access(self, inventory):
        return can_access_moleville_entrance(
            self.world, inventory
        ) and inventory.has_item(items.BambinoBomb)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class PunchinelloBossFightLocation(BossFightLocation):
    related_class = bosses.Punchinello
    description = AvailableBosses.Punchinello.value
    area = locations.Area.MolevilleMines
    item = items.PunchinelloBossFight
    original_item = items.PunchinelloBossFight
    rooms = [271]
    event = 353

    def can_access(self, inventory):
        return can_access_moleville_entrance(
            self.world, inventory
        ) and inventory.has_item(items.BambinoBomb)


class MolevilleMinesBoss2(BossStarPiece):
    description = ShuffleLocationSelector.MolevilleMinesBoss2.value
    area = locations.Area.MolevilleMines
    rooms = [271]
    event = 167
    item = items.StarPiece3
    original_item = items.StarPiece3
    access = 2

    def can_access(self, inventory):
        return can_clear_mines(self.world, inventory)


class MolevilleMinesCharacter(CharacterRecruit):
    area = locations.Area.ForestMaze
    description = ShuffleLocationSelector.MolevilleMinesCharacter.value
    item = items.BowserRecruit
    original_item = items.BowserRecruit
    rooms = [284]
    event = 186
    npcs = [
        (284, 1, [], []),
    ]
    credits_npcs = [
        (435, 7, [], [969]),
        (496, 23, [3885], []),
        (88, 4, [3950], []),
        (375, 4, [3951], []),
    ]

    def can_access(self, inventory):
        return can_clear_mines(self.world, inventory)


# *** Booster Pass


class BoosterPass1(Chest):
    description = ShuffleLocationSelector.BoosterPass1.value
    area = locations.Area.BoosterPass
    rooms = [100]
    npc_ids = [8]
    event = 247
    item = items.Flower
    original_item = items.Flower

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.SlotMachineChest
        )


class BoosterPass2(Chest):
    description = ShuffleLocationSelector.BoosterPass2.value
    area = locations.Area.BoosterPass
    rooms = [100]
    npc_ids = [9]
    event = 246
    item = items.RockCandy
    original_item = items.RockCandy

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.SlotMachineChest
        )


class BoosterPassBush(NPCReward):
    description = ShuffleLocationSelector.BoosterPassBush.value
    area = locations.Area.BoosterPass
    rooms = [100]
    event = 253
    item = items.FrogCoin
    original_item = items.FrogCoin
    coinsanity = True


class BoosterPassFlower(OverworldItem):
    description = ShuffleLocationSelector.BoosterPassFlower.value
    area = locations.Area.BoosterPass
    rooms = [101]
    event = 241
    npc_ids = [6]
    item = items.Flower
    original_item = items.Flower


class BoosterPassSecret1(Chest):
    area = locations.Area.BoosterPass
    description = ShuffleLocationSelector.BoosterPassSecret1.value
    rooms = [405]
    npc_ids = [10]
    event = 247
    item = items.FrogCoin
    original_item = items.FrogCoin
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(
            flags.BoosterTowerGate, BoosterTowerGating.open
        ):
            self.access = 1

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)


class BoosterPassSecret2(Chest):
    area = locations.Area.BoosterPass
    description = ShuffleLocationSelector.BoosterPassSecret2.value
    rooms = [405]
    npc_ids = [11]
    event = 246
    item = items.Flower
    original_item = items.Flower
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(
            flags.BoosterTowerGate, BoosterTowerGating.open
        ):
            self.access = 1

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)


class BoosterPassSecret3(Chest):
    area = locations.Area.BoosterPass
    description = ShuffleLocationSelector.BoosterPassSecret3.value
    rooms = [405]
    npc_ids = [12]
    event = 245
    item = items.KerokeroCola
    original_item = items.KerokeroCola
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(
            flags.BoosterTowerGate, BoosterTowerGating.open
        ):
            self.access = 1

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)


# *** Booster Tower


class BoosterTowerSpookum(Chest):
    description = ShuffleLocationSelector.BoosterTowerSpookum.value
    area = locations.Area.BoosterTower
    item = items.FrogCoin
    original_item = items.FrogCoin
    rooms = [196]
    npc_ids = [6]
    event = 247

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)


class BoosterTowerThwomp(Chest):
    description = ShuffleLocationSelector.BoosterTowerThwomp.value
    area = locations.Area.BoosterTower
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom
    rooms = [36]
    npc_ids = [2]
    event = 247

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BoosterTowerKnifeGuy(NPCReward):
    description = ShuffleLocationSelector.BoosterTowerKnifeGuy.value
    area = locations.Area.BoosterTower
    item = items.BrightCard
    original_item = items.BrightCard
    rooms = [39]
    event = 253
    access = 2
    key = True

    def item_allowed(self, item):
        if self.world.settings.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

    def can_access(self, inventory):
        return can_clear_tower_2(self.world, inventory)


class BoosterTowerRoomKey(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerRoomKey.value
    area = locations.Area.BoosterTower
    item = items.RoomKey
    original_item = items.RoomKey
    coinsanity = False
    rooms = [41]
    event = 228
    npc_ids = [5]
    key = True

    def item_allowed(self, item):
        if self.world.settings.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)


class BoosterTowerFrogCoin1(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerFrogCoin1.value
    area = locations.Area.BoosterTower
    item = items.FrogCoin
    original_item = items.FrogCoin
    rooms = [41]
    event = 241
    npc_ids = [0]

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)


class BoosterTowerFrogCoin2(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerFrogCoin2.value
    area = locations.Area.BoosterTower
    item = items.FrogCoin
    original_item = items.FrogCoin
    rooms = [41]
    event = 240
    npc_ids = [1]

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)


class BoosterTowerFrogCoin3(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerFrogCoin3.value
    area = locations.Area.BoosterTower
    item = items.FrogCoin
    original_item = items.FrogCoin
    rooms = [41]
    event = 239
    npc_ids = [2]

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)


class BoosterTowerFrogCoin4(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerFrogCoin4.value
    area = locations.Area.BoosterTower
    item = items.FrogCoin
    original_item = items.FrogCoin
    rooms = [41]
    event = 238
    npc_ids = [3]

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)


class BoosterTowerCoin1(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerCoin1.value
    area = locations.Area.BoosterTower
    item = items.Coins1
    original_item = items.Coins1
    rooms = [41]
    event = 237
    npc_ids = [7]

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)


class BoosterTowerCoin2(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerCoin2.value
    area = locations.Area.BoosterTower
    item = items.Coins1
    original_item = items.Coins1
    rooms = [41]
    event = 236
    npc_ids = [8]

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)


class BoosterTowerCoin3(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerCoin3.value
    area = locations.Area.BoosterTower
    item = items.Coins1
    original_item = items.Coins1
    rooms = [41]
    event = 235
    npc_ids = [9]

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)


class BoosterTowerCoin4(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerCoin4.value
    area = locations.Area.BoosterTower
    item = items.Coins1
    original_item = items.Coins1
    rooms = [41]
    event = 234
    npc_ids = [10]

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)


class BoosterTowerCoin5(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerCoin5.value
    area = locations.Area.BoosterTower
    item = items.Coins1
    original_item = items.Coins1
    rooms = [41]
    event = 233
    npc_ids = [11]

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)


class BoosterTowerCoin6(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerCoin6.value
    area = locations.Area.BoosterTower
    item = items.Coins1
    original_item = items.Coins1
    rooms = [41]
    event = 232
    npc_ids = [12]

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)


class BoosterTowerCoin7(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerCoin7.value
    area = locations.Area.BoosterTower
    item = items.Coins1
    original_item = items.Coins1
    rooms = [41]
    event = 231
    npc_ids = [13]

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)


class BoosterTowerCoin8(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerCoin8.value
    area = locations.Area.BoosterTower
    item = items.Coins1
    original_item = items.Coins1
    rooms = [41]
    event = 230
    npc_ids = [14]

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)


class BoosterTowerCoin9(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerCoin9.value
    area = locations.Area.BoosterTower
    item = items.Coins1
    original_item = items.Coins1
    rooms = [41]
    event = 229
    npc_ids = [15]

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)


class BoosterTowerMasher(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerMasher.value
    area = locations.Area.BoosterTower
    rooms = [197]
    event = 253
    item = items.Masher
    original_item = items.Masher
    npc_ids = [3]

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)

    def item_allowed(self, item):
        return (
            super().item_allowed(item) and item.npc_event is not None
        )  # this looks like a chest, requires an overworld item, but acts like a npc reward


class BoosterTowerParachute(SlotsNotAllowedChest):
    description = ShuffleLocationSelector.BoosterTowerParachute.value
    area = locations.Area.BoosterTower
    item = items.FrogCoin
    original_item = items.FrogCoin
    rooms = [35]
    npc_ids = [9]
    event = 247

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BoosterTowerParachuteCrevice(NPCReward):
    description = ShuffleLocationSelector.BoosterTowerParachuteCrevice.value
    area = locations.Area.BoosterTower
    item = items.FrogCoin
    original_item = items.FrogCoin
    coinsanity = True
    rooms = [35]
    event = 253

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)


class BoosterTowerZoomShoes(Chest):
    description = ShuffleLocationSelector.BoosterTowerZoomShoes.value
    area = locations.Area.BoosterTower
    item = items.ZoomShoes
    original_item = items.ZoomShoes
    rooms = [48]
    npc_ids = [0]
    event = 247
    access = 2
    special_equip = True

    def can_access(self, inventory):
        return inventory.has_item(items.RoomKey) and can_access_tower(
            self.world, inventory
        )

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BoosterTowerTop1(Chest):
    description = ShuffleLocationSelector.BoosterTowerTop1.value
    area = locations.Area.BoosterTower
    rooms = [199]
    npc_ids = [0]
    event = 247
    item = items.FrogCoin
    original_item = items.FrogCoin

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BoosterTowerTop2(Chest):
    description = ShuffleLocationSelector.BoosterTowerTop2.value
    area = locations.Area.BoosterTower
    rooms = [199]
    npc_ids = [1]
    event = 246
    item = items.GoodieBag
    original_item = items.GoodieBag

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BoosterTowerTop3(Chest):
    description = ShuffleLocationSelector.BoosterTowerTop3.value
    area = locations.Area.BoosterTower
    rooms = [199]
    npc_ids = [9]
    event = 245
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BoosterTowerRailway(NPCReward):
    area = locations.Area.BoosterTower
    description = ShuffleLocationSelector.BoosterTowerRailway.value
    rooms = [194]
    event = 253
    item = items.FlowerTab
    original_item = items.FlowerTab

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)


class BoosterTowerPortraits(OverworldItem):
    area = locations.Area.BoosterTower
    description = ShuffleLocationSelector.BoosterTowerPortraits.value
    rooms = [195]
    event = 241
    npc_ids = [7]
    item = items.ElderKey
    original_item = items.ElderKey
    coinsanity = False
    key = True

    def item_allowed(self, item):
        if self.world.settings.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)


class BoosterTowerChomp(OverworldItem):
    area = locations.Area.BoosterTower
    description = ShuffleLocationSelector.BoosterTowerChomp.value
    rooms = [200]
    event = 241
    npc_ids = [0]
    item = items.Chomp
    original_item = items.Chomp
    coinsanity = False
    access = 2
    special_equip = True

    def can_access(self, inventory):
        return inventory.has_item(items.ElderKey) and can_access_tower(
            self.world, inventory
        )


class BoosterTowerCurtainGame(NPCReward):
    area = locations.Area.BoosterTower
    description = ShuffleLocationSelector.BoosterTowerCurtainGame.value
    rooms = [192]
    event = 253
    item = items.Amulet
    original_item = items.Amulet
    missable = True
    access = 2

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)


class BoosterBossFightLocation(BossFightLocation):
    related_class = bosses.Booster
    description = AvailableBosses.Booster.value
    area = locations.Area.BoosterTower
    item = items.BoosterBossFight
    original_item = items.BoosterBossFight
    rooms = [192]
    event = 353

    def can_access(self, inventory):
        return can_access_tower(self.world, inventory)


class BoosterTowerStarPiece1(BossStarPiece):
    area = locations.Area.BoosterTower
    description = ShuffleLocationSelector.BoosterTowerStarPiece1.value
    rooms = [192]
    event = 167

    def can_access(self, inventory):
        return can_clear_tower_1(self.world, inventory)


class ClownBrosBossFightLocation(BossFightLocation):
    related_class = bosses.ClownBros
    description = AvailableBosses.KnifeGuyGrateGuy.value
    area = locations.Area.BoosterTower
    item = items.GrateGuyBossFight
    original_item = items.GrateGuyBossFight
    rooms = [258]
    event = 353

    def can_access(self, inventory):
        return can_clear_tower_1(self.world, inventory)


class BoosterTowerStarPiece2(BossStarPiece):
    area = locations.Area.BoosterTower
    description = ShuffleLocationSelector.BoosterTowerStarPiece2.value
    rooms = [202]
    event = 167

    def can_access(self, inventory):
        return can_clear_tower_2(self.world, inventory)


# *** Marrymore


class MarrymorePrize1(NPCReward):
    area = locations.Area.Marrymore
    description = ShuffleLocationSelector.MarrymorePrize1.value
    item = items.FlowerTab
    original_item = items.FlowerTab
    rooms = [7]
    event = 253


class MarrymorePrize2(NPCReward):
    area = locations.Area.Marrymore
    description = ShuffleLocationSelector.MarrymorePrize2.value
    item = items.FlowerJar
    original_item = items.FlowerJar
    rooms = [7]
    event = 252


class MarrymorePrize3(NPCReward):
    area = locations.Area.Marrymore
    item = items.MultiFrogCoin(NPCReward, 1)
    original_item = items.MultiFrogCoin(NPCReward, 1)
    description = ShuffleLocationSelector.MarrymorePrize3.value
    rooms = [7]
    event = 251


class MarrymorePrize4(NPCReward):
    area = locations.Area.Marrymore
    item = items.MultiFrogCoin(NPCReward, 2)
    original_item = items.MultiFrogCoin(NPCReward, 2)
    description = ShuffleLocationSelector.MarrymorePrize4.value
    rooms = [7]
    event = 250


class MarrymorePrize5(NPCReward):
    area = locations.Area.Marrymore
    item = items.MultiFrogCoin(NPCReward, 3)
    original_item = items.MultiFrogCoin(NPCReward, 3)
    description = ShuffleLocationSelector.MarrymorePrize5.value
    rooms = [7]
    event = 249


class MarrymorePrize6(NPCReward):
    area = locations.Area.Marrymore
    item = items.MultiFrogCoin(NPCReward, 20)
    original_item = items.MultiFrogCoin(NPCReward, 20)
    description = ShuffleLocationSelector.MarrymorePrize6.value
    rooms = [7]
    event = 248


class MarrymoreInn(Chest):
    area = locations.Area.Marrymore
    description = ShuffleLocationSelector.MarrymoreInn.value
    item = items.FrogCoin
    original_item = items.FrogCoin
    rooms = [9]
    npc_ids = [0]
    event = 247


class MarrymoreSnifit1(NPCReward):
    area = locations.Area.Marrymore
    description = ShuffleLocationSelector.MarrymoreSnifit1.value
    item = items.Brooch
    original_item = items.Brooch
    rooms = [154]
    event = 253

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.MarrymoreGate, MarrymoreGating.tower):
            self.access = 2
        if world.settings.is_flag_enabled(flags.ShuffleWeddingGear):
            self.missable = True

    def can_access(self, inventory):
        return can_access_marrymore(self.world, inventory)


class MarrymoreSnifit2(NPCReward):
    area = locations.Area.Marrymore
    description = ShuffleLocationSelector.MarrymoreSnifit2.value
    item = items.Ring
    original_item = items.Ring
    rooms = [154]
    event = 252

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.MarrymoreGate, MarrymoreGating.tower):
            self.access = 2
        if world.settings.is_flag_enabled(flags.ShuffleWeddingGear):
            self.missable = True

    def can_access(self, inventory):
        return can_access_marrymore(self.world, inventory)


class MarrymoreSnifit3(NPCReward):
    area = locations.Area.Marrymore
    description = ShuffleLocationSelector.MarrymoreSnifit3.value
    item = items.Shoes
    original_item = items.Shoes
    rooms = [154]
    event = 251

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.MarrymoreGate, MarrymoreGating.tower):
            self.access = 2
        if world.settings.is_flag_enabled(flags.ShuffleWeddingGear):
            self.missable = True

    def can_access(self, inventory):
        return can_access_marrymore(self.world, inventory)


class MarrymoreAltarHead(OverworldItem):
    area = locations.Area.Marrymore
    description = ShuffleLocationSelector.MarrymoreAltar.value
    item = items.Crown
    original_item = items.Crown
    rooms = [154]
    npc_ids = [5]
    event = 241

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.MarrymoreGate, MarrymoreGating.tower):
            self.access = 2
        if world.settings.is_flag_enabled(flags.ShuffleWeddingGear):
            self.missable = True

    def can_access(self, inventory):
        return can_access_marrymore(self.world, inventory)


class BundtBossFightLocation(BossFightLocation):
    related_class = bosses.Bundt
    description = AvailableBosses.Bundt.value
    area = locations.Area.Marrymore
    item = items.BundtBossFight
    original_item = items.BundtBossFight
    rooms = [154]
    event = 353

    def can_access(self, inventory):
        return can_fight_marrymore(self.world, inventory)


class MarrymoreStarPiece(BossStarPiece):
    area = locations.Area.Marrymore
    description = ShuffleLocationSelector.MarrymoreStarPiece.value
    rooms = [154]
    event = 167
    access = 1

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.MarrymoreGate, MarrymoreGating.tower):
            self.access = 2

    def can_access(self, inventory):
        return can_clear_marrymore(self.world, inventory)


class MarrymoreCharacter(CharacterRecruit):
    area = locations.Area.Marrymore
    description = ShuffleLocationSelector.MarrymoreCharacter.value
    item = items.ToadstoolRecruit
    original_item = items.ToadstoolRecruit
    rooms = [154]
    event = 186
    npcs = [(154, 8, [3809, 3930], []), (54, 8, [3499, 3502, 3506], [])]
    credits_npcs = [(496, 19, [3885], []), (88, 0, [3950], []), (375, 0, [3951], [])]

    def can_access(self, inventory):
        return can_clear_marrymore(self.world, inventory)


# populate this with the corresponding character in MarrymoreCharacter


class MarrymoreCharacterSpotted(CharacterSpotted):
    area = locations.Area.BoosterHill
    description = ShuffleLocationSelector.MarrymoreCharacter.value
    item = items.ToadstoolSpotted
    original_item = items.ToadstoolSpotted


# *** Star Hill


class StarHillStarPiece1(BossStarPiece):
    area = locations.Area.StarHill
    description = ShuffleLocationSelector.StarHillStarPiece1.value
    rooms = [159]
    event = 167
    item = items.StarPiece4
    original_item = items.StarPiece4


# *** Seaside Town


class FrogDisciple1(FrogCoinShopItem):
    description = ShuffleLocationSelector.FrogDisciple1.value
    area = locations.Area.SeasideTown
    item = items.SeeYa
    original_item = items.SeeYa


class FrogDisciple2(FrogCoinShopItem):
    description = ShuffleLocationSelector.FrogDisciple2.value
    area = locations.Area.SeasideTown
    item = items.EarlierTimes
    original_item = items.EarlierTimes


class FrogDisciple3(FrogCoinShopItem):
    description = ShuffleLocationSelector.FrogDisciple3.value
    area = locations.Area.SeasideTown
    item = items.ExpBooster
    original_item = items.ExpBooster


class FrogDisciple4(FrogCoinShopItem):
    description = ShuffleLocationSelector.FrogDisciple4.value
    area = locations.Area.SeasideTown
    item = items.CoinTrick
    original_item = items.CoinTrick


class FrogDisciple5(FrogCoinShopItem):
    description = ShuffleLocationSelector.FrogDisciple5.value
    area = locations.Area.SeasideTown
    item = items.ScroogeRing
    original_item = items.ScroogeRing


class YaridovichBossFightLocation(BossFightLocation):
    related_class = bosses.Yaridovich
    description = AvailableBosses.Yaridovich.value
    area = locations.Area.SeasideTown
    item = items.YaridovichBossFight
    original_item = items.YaridovichBossFight
    rooms = [315]
    event = 353

    def can_access(self, inventory):
        return can_access_yaridovich(self.world, inventory)


class SeasideTownBoss(BossStarPiece):
    description = ShuffleLocationSelector.SeasideTownBoss.value
    area = locations.Area.SeasideTown
    rooms = [316]
    event = 167
    item = items.StarPiece5
    original_item = items.StarPiece5

    def can_clear_seaside(self, inventory):
        return can_access_yaridovich(self.world, inventory)


class SeasideTownBossPrize(OverworldItem):
    area = locations.Area.SeasideTown
    description = ShuffleLocationSelector.SeasideTownBossPrize.value
    rooms = [316]
    event = 241
    npc_ids = [0]
    item = items.ShedKey
    original_item = items.ShedKey
    coinsanity = False
    key = True
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.YaridovichGate, YaridovichGating.open):
            self.access = 1

    def item_allowed(self, item):
        if self.world.settings.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

    def can_clear_seaside(self, inventory):
        return can_access_yaridovich(self.world, inventory)


class SeasideTownRescue(NPCReward):
    area = locations.Area.SeasideTown
    description = ShuffleLocationSelector.SeasideTownRescue.value
    rooms = [314]
    event = 253
    item = items.FlowerBox
    original_item = items.FlowerBox
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.YaridovichGate, YaridovichGating.open):
            self.access = 1

    def can_access(self, inventory):
        return inventory.has_item(items.ShedKey) and can_clear_seaside(
            self.world, inventory
        )


# *** Sea


class SeaStarChest(Chest):
    area = locations.Area.Sea
    description = ShuffleLocationSelector.SeaStarChest.value
    rooms = [134]
    npc_ids = [0]
    event = 247
    item = items.SeaStar
    original_item = items.SeaStar
    access = 1

    def __init__(self, world):
        super().__init__(world)
        # for option in [SeaGating.star1, SeaGating.star2, SeaGating.star3, SeaGating.star4, SeaGating.star5, SeaGating.star6]:
        if world.settings.is_flag_value(flags.SeaGate, SeaGating.star4):
            self.access = 2

    def can_access(self, inventory):
        return can_access_sea(self.world, inventory)


class SeaSaveRoom1(Chest):
    area = locations.Area.Sea
    description = ShuffleLocationSelector.SeaSaveRoom1.value
    rooms = [132]
    npc_ids = [0]
    event = 245
    item = items.FrogCoin
    original_item = items.FrogCoin
    access = 1

    def __init__(self, world):
        super().__init__(world)
        # for option in [SeaGating.star1, SeaGating.star2, SeaGating.star3, SeaGating.star4, SeaGating.star5, SeaGating.star6]:
        if world.settings.is_flag_value(flags.SeaGate, SeaGating.star4):
            self.access = 2

    def can_access(self, inventory):
        return can_access_sea(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class SeaSaveRoom2(Chest):
    area = locations.Area.Sea
    description = ShuffleLocationSelector.SeaSaveRoom2.value
    rooms = [132]
    npc_ids = [1]
    event = 246
    item = items.Flower
    original_item = items.Flower
    access = 1

    def __init__(self, world):
        super().__init__(world)
        # for option in [SeaGating.star1, SeaGating.star2, SeaGating.star3, SeaGating.star4, SeaGating.star5, SeaGating.star6]:
        if world.settings.is_flag_value(flags.SeaGate, SeaGating.star4):
            self.access = 2

    def can_access(self, inventory):
        return can_access_sea(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class SeaSaveRoom3(Chest):
    area = locations.Area.Sea
    description = ShuffleLocationSelector.SeaSaveRoom3.value
    rooms = [132]
    npc_ids = [2]
    event = 247
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom
    access = 1

    def __init__(self, world):
        super().__init__(world)
        # for option in [SeaGating.star1, SeaGating.star2, SeaGating.star3, SeaGating.star4, SeaGating.star5, SeaGating.star6]:
        if world.settings.is_flag_value(flags.SeaGate, SeaGating.star4):
            self.access = 2

    def can_access(self, inventory):
        return can_access_sea(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class SeaWhirlpoolChest(Chest):
    description = ShuffleLocationSelector.SeaWhirlpoolChest.value
    area = locations.Area.Sea
    rooms = [133]
    npc_ids = [0]
    event = 247
    item = items.MaxMushroom
    original_item = items.MaxMushroom
    access = 1

    def __init__(self, world):
        super().__init__(world)
        # for option in [SeaGating.star1, SeaGating.star2, SeaGating.star3, SeaGating.star4, SeaGating.star5, SeaGating.star6]:
        if world.settings.is_flag_value(flags.SeaGate, SeaGating.star4):
            self.access = 2

    def can_access(self, inventory):
        return can_access_sea(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


# *** Sunken Ship


class SunkenShipRatStairs(Chest):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipRatStairs.value
    rooms = [167]
    npc_ids = [0]
    event = 247
    item = items.Coins(100)
    original_item = items.Coins(100)
    access = 1

    def __init__(self, world):
        super().__init__(world)
        # for option in [SeaGating.star1, SeaGating.star2, SeaGating.star3, SeaGating.star4, SeaGating.star5, SeaGating.star6]:
        if world.settings.is_flag_value(flags.SeaGate, SeaGating.star4):
            self.access = 2

    def can_access(self, inventory):
        return can_access_sea(self.world, inventory)

    def item_allowed(self, item):
        if isclass_or_instance(item, items.InvincibilityStar):
            return True
        return super().item_allowed(item)


class SunkenShipRatStairsFlower(PacketItem):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipRatStairsFlower.value
    rooms = [167]
    script_id = 3385
    event = 241
    item = items.Flower
    original_item = items.Flower
    access = 1
    preferred = PacketType.Chest

    def __init__(self, world):
        super().__init__(world)
        # for option in [SeaGating.star1, SeaGating.star2, SeaGating.star3, SeaGating.star4, SeaGating.star5, SeaGating.star6]:
        if world.settings.is_flag_value(flags.SeaGate, SeaGating.star4):
            self.access = 2

    def can_access(self, inventory):
        return can_access_sea(self.world, inventory)


class SunkenShipShop(Chest):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipShop.value
    rooms = [169]
    npc_ids = [0]
    event = 247
    item = items.Coins(100)
    original_item = items.Coins(100)
    access = 1

    def __init__(self, world):
        super().__init__(world)
        # for option in [SeaGating.star1, SeaGating.star2, SeaGating.star3, SeaGating.star4, SeaGating.star5, SeaGating.star6]:
        if world.settings.is_flag_value(flags.SeaGate, SeaGating.star4):
            self.access = 2

    def can_access(self, inventory):
        return can_access_sea(self.world, inventory)


class SunkenShipTrampolinePuzzle(PacketItem):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipTrampolinePuzzle.value
    rooms = [163]
    event = 241
    script_id = 3383
    item = items.Flower
    original_item = items.Flower
    preferred = PacketType.Falling

    def can_access(self, inventory):
        return can_access_sea(self.world, inventory)


class SunkenShipTroopaPuzzle(PacketItem):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipTroopaPuzzle.value
    rooms = [166]
    event = 241
    script_id = 3384
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom
    preferred = PacketType.Falling

    def can_access(self, inventory):
        return can_access_sea(self.world, inventory)


class SunkenShip3DMaze(PacketItem):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShip3DMaze.value
    rooms = [168]
    event = 241
    script_id = 3386
    item = items.RoyalSyrup
    original_item = items.RoyalSyrup
    coinsanity = False
    access = 2
    preferred = PacketType.Falling

    def can_access(self, inventory):
        return can_access_sea(self.world, inventory)


class SunkenShipCoinSnake(NPCReward):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipCoinSnake.value
    rooms = [171]
    event = 253
    npc_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    item = items.Coins(150)
    original_item = items.Coins(150)
    # Needs special considerations for the sound played in 3216
    # and the sequences performed in 3216 and 3215
    # depending on the item
    # ship access

    def can_access(self, inventory):
        return can_access_sea(self.world, inventory)


class SunkenShipCannonballPuzzle(PacketItem):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipCannonballPuzzle.value
    rooms = [172]
    event = 241
    script_id = 3387
    item = items.Mushroom
    original_item = items.Mushroom
    coinsanity = False
    preferred = PacketType.Falling

    def can_access(self, inventory):
        return can_access_sea(self.world, inventory)


class SunkenShipBarrelPuzzle(PacketItem):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipBarrelPuzzle.value
    rooms = [176]
    event = 241
    script_id = 3389
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom
    preferred = PacketType.Falling

    def can_access(self, inventory):
        return can_access_sea(self.world, inventory)


class KingCalamariBossFightLocation(BossFightLocation):
    related_class = bosses.KingCalamari
    description = AvailableBosses.KingCalamari.value
    area = locations.Area.SunkenShip
    item = items.KingCalamariBossFight
    original_item = items.KingCalamariBossFight
    rooms = [177]
    event = 353

    def can_access(self, inventory):
        return can_access_sea(self.world, inventory)


class SunkenShipMidboss(BossStarPiece):
    description = ShuffleLocationSelector.SunkenShipMidboss.value
    area = locations.Area.SunkenShip
    rooms = [173]
    event = 167

    def can_access(self, inventory):
        return can_clear_ship_midboss(self.world, inventory)


class SunkenShipCoins1(Chest):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipCoins1.value
    rooms = [175]
    npc_ids = [0]
    event = 247
    item = items.Coins(100)
    original_item = items.Coins(100)
    access = 2

    def can_access(self, inventory):
        return can_clear_ship_midboss(self.world, inventory)


class SunkenShipCoins2(Chest):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipCoins2.value
    rooms = [175]
    npc_ids = [1]
    event = 246
    item = items.Coins(100)
    original_item = items.Coins(100)
    access = 2

    def can_access(self, inventory):
        return can_clear_ship_midboss(self.world, inventory)


class SunkenShipCloneRoom(Chest):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipCloneRoom.value
    rooms = [179]
    npc_ids = [2]
    event = 247
    item = items.KerokeroCola
    original_item = items.KerokeroCola
    access = 2

    def can_access(self, inventory):
        return can_clear_ship_midboss(self.world, inventory)


class SunkenShipFrogCoinRoom(Chest):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipFrogCoinRoom.value
    rooms = [183]
    npc_ids = [0]
    event = 247
    item = items.FrogCoin
    original_item = items.FrogCoin
    access = 2

    def can_access(self, inventory):
        return can_clear_ship_midboss(self.world, inventory)


class SunkenShipHidonMushroom(Chest):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipHidonMushroom.value
    rooms = [184]
    npc_ids = [1]
    event = 247
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom
    access = 2

    def can_access(self, inventory):
        return can_clear_ship_midboss(self.world, inventory)


class HidonChest(Chest):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.HidonChest.value
    rooms = [184]
    npc_ids = [2]
    event = 246
    item = items.HidonFight
    original_item = items.HidonFight
    access = 2

    def can_access(self, inventory):
        return can_clear_ship_midboss(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class HidonBossFightLocation(BossFightLocation):
    related_class = bosses.Hidon
    description = AvailableBosses.Hidon.value
    item = items.HidonBossFight
    original_item = items.HidonBossFight
    rooms = [513]
    event = 353

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.MimicsAnywhere, False):
            self.area = locations.Area.SunkenShip

    def can_access(self, inventory):
        return inventory.has_item(items.HidonFight)


class HidonBoss(BossStarPiece):
    description = ShuffleLocationSelector.HidonBoss.value
    rooms = [513]
    event = 167

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.MimicsAnywhere, False):
            self.area = locations.Area.SunkenShip

    def can_access(self, inventory):
        return can_beat_mimic_2(self.world, inventory)


class HidonReward1(NPCReward):
    description = ShuffleLocationSelector.HidonReward1.value
    rooms = [513]
    event = 253
    item = items.SafetyBadge
    original_item = items.SafetyBadge
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.MimicsAnywhere, False):
            self.area = locations.Area.SunkenShip

    def can_access(self, inventory):
        return can_beat_mimic_2(self.world, inventory)


class HidonReward2(Chest):
    description = ShuffleLocationSelector.HidonReward2.value
    rooms = [513]
    event = 245
    manual_70A7 = True
    item = items.Coins(100)
    original_item = items.Coins(100)
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.MimicsAnywhere, False):
            self.area = locations.Area.SunkenShip

    def can_access(self, inventory):
        return can_beat_mimic_2(self.world, inventory)

    def item_allowed(self, item):
        return (
            super().item_allowed(item)
            and not isclass_or_instance(item, items.MimicFight)
            and not isclass_or_instance(item, items.SlotMachineChest)
            and not isclass_or_instance(item, items.InvincibilityStar)
            and not isclass_or_instance(item, items.InfiniteCoins)
        )


class SunkenShipUnderwaterFrogCoin1(OverworldItem):
    description = ShuffleLocationSelector.SunkenShipUnderwaterFrogCoin1.value
    area = locations.Area.SunkenShip
    item = items.FrogCoin
    original_item = items.FrogCoin
    rooms = [187]
    event = 241
    npc_ids = [0]
    access = 2

    def can_access(self, inventory):
        return can_clear_ship_midboss(self.world, inventory)


class SunkenShipUnderwaterFrogCoin2(OverworldItem):
    description = ShuffleLocationSelector.SunkenShipUnderwaterFrogCoin2.value
    area = locations.Area.SunkenShip
    item = items.FrogCoin
    original_item = items.FrogCoin
    rooms = [187]
    event = 240
    npc_ids = [1]
    access = 2

    def can_access(self, inventory):
        return can_clear_ship_midboss(self.world, inventory)


class SunkenShipUnderwaterFrogCoin3(OverworldItem):
    description = ShuffleLocationSelector.SunkenShipUnderwaterFrogCoin3.value
    area = locations.Area.SunkenShip
    item = items.FrogCoin
    original_item = items.FrogCoin
    rooms = [187]
    event = 239
    npc_ids = [2]
    access = 2

    def can_access(self, inventory):
        return can_clear_ship_midboss(self.world, inventory)


class SunkenShipUnderwaterFrogCoin4(OverworldItem):
    description = ShuffleLocationSelector.SunkenShipUnderwaterFrogCoin4.value
    area = locations.Area.SunkenShip
    item = items.FrogCoin
    original_item = items.FrogCoin
    rooms = [187]
    event = 238
    npc_ids = [3]
    access = 2

    def can_access(self, inventory):
        return can_clear_ship_midboss(self.world, inventory)


class SunkenShipSafetyRing(Chest):
    description = ShuffleLocationSelector.SunkenShipSafetyRing.value
    area = locations.Area.SunkenShip
    rooms = [185]
    npc_ids = [0]
    event = 247
    item = items.SafetyRing
    original_item = items.SafetyRing
    access = 2

    def can_access(self, inventory):
        return can_clear_ship_midboss(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class SunkenShipBandanaReds(Chest):
    description = ShuffleLocationSelector.SunkenShipBandanaReds.value
    area = locations.Area.SunkenShip
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom
    rooms = [24]
    npc_ids = [4]
    event = 247
    access = 2

    def can_access(self, inventory):
        return can_clear_ship_midboss(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class SunkenShipBlooberRoom(OverworldItem):
    description = ShuffleLocationSelector.SunkenShipBlooberRoom.value
    area = locations.Area.SunkenShip
    item = items.FrogCoin
    original_item = items.FrogCoin
    rooms = [27]
    event = 241
    npc_ids = [5]
    access = 2

    def can_access(self, inventory):
        return can_clear_ship_midboss(self.world, inventory)


class JohnnyBossFightLocation(BossFightLocation):
    related_class = bosses.Johnny
    description = AvailableBosses.Johnny.value
    area = locations.Area.SunkenShip
    item = items.JohnnyBossFight
    original_item = items.JohnnyBossFight
    rooms = [28]
    event = 353

    def can_access(self, inventory):
        return can_clear_ship_midboss(self.world, inventory)


class SunkenShipBoss(BossStarPiece):
    description = ShuffleLocationSelector.SunkenShipBoss.value
    area = locations.Area.SunkenShip
    rooms = [28]
    event = 167

    def can_access(self, inventory):
        return can_clear_ship(self.world, inventory)


# *** Land's End


class LandsEndRedEssence(Chest):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.LandsEndRedEssence.value
    rooms = [137]
    npc_ids = [4]
    event = 247
    item = items.RedEssence
    original_item = items.RedEssence

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class LandsEndChowPit1(Chest):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.LandsEndChowPit1.value
    rooms = [138]
    npc_ids = [6]
    event = 247
    item = items.KerokeroCola
    original_item = items.KerokeroCola


class LandsEndChowPit2(Chest):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.LandsEndChowPit2.value
    rooms = [138]
    npc_ids = [7]
    event = 246
    item = items.FrogCoin
    original_item = items.FrogCoin


class LandsEndBeeRoom(Chest):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.LandsEndBeeRoom.value
    rooms = [141]
    npc_ids = [6]
    event = 247
    item = items.FrogCoin
    original_item = items.FrogCoin


class LandsEndSecret1(Chest):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.LandsEndSecret1.value
    rooms = [270]
    npc_ids = [7]
    event = 247
    item = items.FrogCoin
    original_item = items.FrogCoin


class LandsEndSecret2(Chest):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.LandsEndSecret2.value
    rooms = [270]
    npc_ids = [6]
    event = 246
    item = items.Flower
    original_item = items.Flower

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class LandsEndShyAway(Chest):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.LandsEndShyAway.value
    rooms = [401]
    npc_ids = [6]
    event = 247
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class LandsEndStarChest1(Chest):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.LandsEndStarChest1.value
    rooms = [263]
    npc_ids = [5]
    event = 247
    item = items.LandsEndVolcanoStar
    original_item = items.LandsEndVolcanoStar

    def item_allowed(self, item):
        if isclass_or_instance(item, items.InvincibilityStar):
            return True
        return super().item_allowed(item)


class LandsEndStarChest2(Chest):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.LandsEndStarChest2.value
    rooms = [262]
    npc_ids = [18]
    event = 247
    item = items.LandsEndStar2
    original_item = items.LandsEndStar2

    def item_allowed(self, item):
        if isclass_or_instance(item, items.InvincibilityStar):
            return True
        return super().item_allowed(item)


class LandsEndStarChest3(Chest):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.LandsEndStarChest3.value
    rooms = [262]
    npc_ids = [19]
    event = 246
    item = items.LandsEndStar3
    original_item = items.LandsEndStar3

    def item_allowed(self, item):
        if isclass_or_instance(item, items.InvincibilityStar):
            return True
        return super().item_allowed(item)


class TroopaClimb(NPCReward):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.TroopaClimb.value
    rooms = [407]
    event = 253
    item = items.TroopaPin
    original_item = items.TroopaPin

    def can_access(self, inventory):
        return can_clear_temple(self.world, inventory)

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class MokuraBossFightLocation(BossFightLocation):
    related_class = bosses.Mokura
    area = locations.Area.LandsEnd
    description = AvailableBosses.Mokura.value
    item = items.MokuraBossFight
    original_item = items.MokuraBossFight
    rooms = [519]
    event = 353


class LandsEndStarPiece1(BossStarPiece):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.LandsEndStarPiece1.value
    rooms = [519]
    event = 167


# *** Belome Temple


class BelomeTempleFortuneTeller(Chest):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleFortuneTeller.value
    rooms = [420]
    npc_ids = [5]
    event = 247
    item = items.Coins(50)
    original_item = items.Coins(50)


class BelomeTempleFortune1(SlotsNotAllowedChest):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleFortune1.value
    rooms = [421]
    npc_ids = [6]
    event = 247
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom
    access = 2

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory)

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class BelomeTempleFortune2(SlotsNotAllowedChest):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleFortune2.value
    rooms = [421]
    npc_ids = [7]
    event = 246
    item = items.YoshiCookie
    original_item = items.YoshiCookie
    access = 2

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory)

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class BelomeTempleFortune3(SlotsNotAllowedChest):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleFortune3.value
    rooms = [421]
    npc_ids = [8]
    event = 245
    item = items.Flower
    original_item = items.Flower
    access = 2

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory)

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class BelomeTempleFortune4(SlotsNotAllowedChest):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleFortune4.value
    rooms = [421]
    npc_ids = [9]
    event = 244
    item = items.Coins(100)
    original_item = items.Coins(100)
    access = 2

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory)

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class BelomeTempleAfterFortune1(Chest):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleAfterFortune1.value
    rooms = [425]
    npc_ids = [0]
    event = 247
    item = items.FrogCoin
    original_item = items.FrogCoin

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory)

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class BelomeTempleAfterFortune2(Chest):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleAfterFortune2.value
    rooms = [425]
    npc_ids = [1]
    event = 246
    item = items.Coins(150)
    original_item = items.Coins(150)

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory)

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class BelomeTempleAfterFortune3(Chest):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleAfterFortune3.value
    rooms = [425]
    npc_ids = [2]
    event = 245
    item = items.FrogCoin
    original_item = items.FrogCoin

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory)

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class BelomeTempleAfterFortune4(Chest):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleAfterFortune4.value
    rooms = [425]
    npc_ids = [3]
    event = 244
    item = items.FrogCoin
    original_item = items.FrogCoin

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory)

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class BelomeTempleTreasureFlower1(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFlower1.value
    rooms = [422]
    npc_ids = [0]
    event = 241
    item = items.Flower
    original_item = items.Flower
    access = 2

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory) and inventory.has_item(
            items.TempleKey
        )

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class BelomeTempleTreasureFlower2(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFlower2.value
    rooms = [422]
    npc_ids = [1]
    event = 240
    item = items.Flower
    original_item = items.Flower
    access = 2

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory) and inventory.has_item(
            items.TempleKey
        )

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class BelomeTempleTreasureFlower3(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFlower3.value
    rooms = [422]
    npc_ids = [2]
    event = 239
    item = items.Flower
    original_item = items.Flower
    access = 2

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory) and inventory.has_item(
            items.TempleKey
        )

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class BelomeTempleTreasureFlower4(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFlower4.value
    rooms = [422]
    npc_ids = [3]
    event = 238
    item = items.Flower
    original_item = items.Flower
    access = 2

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory) and inventory.has_item(
            items.TempleKey
        )

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class BelomeTempleTreasureFrogCoin1(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFrogCoin1.value
    rooms = [422]
    npc_ids = [4]
    event = 237
    item = items.FrogCoin
    original_item = items.FrogCoin
    access = 2

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory) and inventory.has_item(
            items.TempleKey
        )

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class BelomeTempleTreasureFrogCoin2(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFrogCoin2.value
    rooms = [422]
    npc_ids = [5]
    event = 236
    item = items.FrogCoin
    original_item = items.FrogCoin
    access = 2

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory) and inventory.has_item(
            items.TempleKey
        )

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class BelomeTempleTreasureFrogCoin3(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFrogCoin3.value
    rooms = [422]
    npc_ids = [6]
    event = 235
    item = items.FrogCoin
    original_item = items.FrogCoin
    access = 2

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory) and inventory.has_item(
            items.TempleKey
        )

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class BelomeTempleTreasureFrogCoin4(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFrogCoin4.value
    rooms = [422]
    npc_ids = [7]
    event = 234
    item = items.FrogCoin
    original_item = items.FrogCoin
    access = 2

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory) and inventory.has_item(
            items.TempleKey
        )

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class BelomeTempleTreasureFrogCoin5(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFrogCoin5.value
    rooms = [422]
    npc_ids = [8]
    event = 233
    item = items.FrogCoin
    original_item = items.FrogCoin
    access = 2

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory) and inventory.has_item(
            items.TempleKey
        )

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class BelomeTempleTreasureFrogCoin6(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFrogCoin6.value
    rooms = [422]
    npc_ids = [9]
    event = 232
    item = items.FrogCoin
    original_item = items.FrogCoin
    access = 2

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory) and inventory.has_item(
            items.TempleKey
        )

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class BelomeTempleTreasureFrogCoin7(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFrogCoin7.value
    rooms = [422]
    npc_ids = [10]
    event = 231
    item = items.FrogCoin
    original_item = items.FrogCoin
    access = 2

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory) and inventory.has_item(
            items.TempleKey
        )

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class BelomeTempleTreasureFrogCoin8(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFrogCoin8.value
    rooms = [422]
    npc_ids = [11]
    event = 230
    item = items.FrogCoin
    original_item = items.FrogCoin
    access = 2

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory) and inventory.has_item(
            items.TempleKey
        )

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class BelomeTempleTreasure1(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasure1.value
    rooms = [422]
    npc_ids = [14]
    event = 228
    item = items.RoyalSyrup
    original_item = items.RoyalSyrup
    coinsanity = False
    access = 2

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory) and inventory.has_item(
            items.TempleKey
        )

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class BelomeTempleTreasure2(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasure2.value
    rooms = [422]
    npc_ids = [13]
    event = 229
    item = items.MaxMushroom
    original_item = items.MaxMushroom
    coinsanity = False
    access = 2

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory) and inventory.has_item(
            items.TempleKey
        )

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class BelomeTempleTreasure3(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasure3.value
    rooms = [422]
    npc_ids = [15]
    event = 227
    item = items.FireBomb
    original_item = items.FireBomb
    coinsanity = False
    access = 2

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory) and inventory.has_item(
            items.TempleKey
        )

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


class Belome2BossFightLocation(BossFightLocation):
    related_class = bosses.Belome2
    description = AvailableBosses.Belome2.value
    area = locations.Area.BelomeTemple
    item = items.Belome2BossFight
    original_item = items.Belome2BossFight
    rooms = [268]
    event = 353

    def can_access(self, inventory):
        return can_access_temple(self.world, inventory)


class BelomeTempleBoss(BossStarPiece):
    description = ShuffleLocationSelector.BelomeTempleBoss.value
    area = locations.Area.BelomeTemple
    rooms = [268]
    event = 167

    def can_access(self, inventory):
        return can_clear_temple(self.world, inventory)

    def __init__(self, world):
        super().__init__(world)
        if not world.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.open
        ):
            self.access = 2


# *** Monstro Town


class MonstroTownEntrance(Chest):
    area = locations.Area.MonstroTown
    description = ShuffleLocationSelector.MonstroTownEntrance.value
    rooms = [267]
    npc_ids = [1]
    event = 247
    item = items.FrogCoin
    original_item = items.FrogCoin
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.MonstroTownGate, MonstroTownGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_access_monstro_town(self.world, inventory)


class MonstroTownThwomp(OverworldItem):
    area = locations.Area.MonstroTown
    description = ShuffleLocationSelector.MonstroTownThwomp.value
    rooms = [324]
    event = 241
    npc_ids = [0]
    item = items.TempleKey
    original_item = items.TempleKey
    key = True
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.MonstroTownGate, MonstroTownGating.open):
            self.access = 1

    def item_allowed(self, item):
        if self.world.settings.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

    def can_access(self, inventory):
        return can_access_monstro_town(self.world, inventory)


class JaggerBossFightLocation(BossFightLocation):
    related_class = bosses.Jagger
    description = AvailableBosses.Jagger.value
    area = locations.Area.MonstroTown
    item = items.JaggerBossFight
    original_item = items.JaggerBossFight
    rooms = [255]
    event = 353

    def can_access(self, inventory):
        return can_access_monstro_town(self.world, inventory)


class DojoBoss1(BossStarPiece):
    description = ShuffleLocationSelector.DojoBoss1.value
    area = locations.Area.MonstroTown
    rooms = [255]
    event = 167

    def can_access(self, inventory):
        return can_dojo_1(self.world, inventory)


class Jinx1BossFightLocation(BossFightLocation):
    related_class = bosses.Jinx1
    description = AvailableBosses.Jinx1.value
    area = locations.Area.MonstroTown
    item = items.Jinx1BossFight
    original_item = items.Jinx1BossFight
    rooms = [515]
    event = 353

    def can_access(self, inventory):
        return can_dojo_1(self.world, inventory)


class DojoBoss2(BossStarPiece):
    description = ShuffleLocationSelector.DojoBoss2.value
    area = locations.Area.MonstroTown
    rooms = [515]
    event = 167

    def can_access(self, inventory):
        return can_dojo_2(self.world, inventory)


class Jinx2BossFightLocation(BossFightLocation):
    related_class = bosses.Jinx2
    description = AvailableBosses.Jinx2.value
    area = locations.Area.MonstroTown
    item = items.Jinx2BossFight
    original_item = items.Jinx2BossFight
    rooms = [516]
    event = 353

    def can_access(self, inventory):
        return can_dojo_2(self.world, inventory)


class DojoBoss3(BossStarPiece):
    description = ShuffleLocationSelector.DojoBoss3.value
    area = locations.Area.MonstroTown
    rooms = [516]
    event = 167

    def can_access(self, inventory):
        return can_dojo_3(self.world, inventory)


class Jinx3BossFightLocation(BossFightLocation):
    related_class = bosses.Jinx3
    description = AvailableBosses.Jinx3.value
    area = locations.Area.MonstroTown
    item = items.Jinx3BossFight
    original_item = items.Jinx3BossFight
    rooms = [517]
    event = 353

    def can_access(self, inventory):
        return can_dojo_3(self.world, inventory)


class DojoBoss4(BossStarPiece):
    description = ShuffleLocationSelector.DojoBoss4.value
    area = locations.Area.MonstroTown
    rooms = [517]
    event = 167

    def can_access(self, inventory):
        return can_dojo_4(self.world, inventory)


class JinxDojoReward(NPCReward):
    area = locations.Area.MonstroTown
    description = ShuffleLocationSelector.JinxDojoReward.value
    rooms = [255]
    event = 253
    item = items.JinxBelt
    original_item = items.JinxBelt
    access = 2
    special_equip = True

    def can_access(self, inventory):
        return can_dojo_4(self.world, inventory)


class CulexBossFightLocation(BossFightLocation):
    related_class = bosses.Culex
    description = AvailableBosses.Culex.value
    area = locations.Area.MonstroTown
    item = items.CulexBossFight
    original_item = items.CulexBossFight
    rooms = [351]
    event = 353

    def can_access(self, inventory):
        return can_access_culex(self.world, inventory)


class CulexBoss(BossStarPiece):
    description = ShuffleLocationSelector.CulexBoss.value
    area = locations.Area.MonstroTown
    rooms = [324]
    event = 167

    def can_access(self, inventory):
        return can_clear_culex(self.world, inventory)


class CulexReward(NPCReward):
    area = locations.Area.MonstroTown
    description = ShuffleLocationSelector.CulexReward.value
    rooms = [351]
    event = 253
    item = items.QuartzCharm
    original_item = items.QuartzCharm
    access = 2
    special_equip = True

    def can_access(self, inventory):
        return can_clear_culex(self.world, inventory)


class SuperJumps30(NPCReward):
    area = locations.Area.MonstroTown
    description = ShuffleLocationSelector.SuperJumps30.value
    rooms = [397]
    event = 253
    item = items.AttackScarf
    original_item = items.AttackScarf
    access = 2
    special_equip = True

    def __init__(self, world):
        super().__init__(world)
        if world.settings.get_flag(flags.SuperJump1Threshold).value < 30:
            self.access = 1

    def can_access(self, inventory):
        return inventory.has_item(items.SuperJumpLearn) and can_access_monstro_town(
            self.world, inventory
        )


class SuperJumps100(NPCReward):
    area = locations.Area.MonstroTown
    description = ShuffleLocationSelector.SuperJumps100.value
    rooms = [397]
    event = 252
    item = items.SuperSuit
    original_item = items.SuperSuit
    access = 2
    special_equip = True

    # you can lower it if you want, buuuut...
    def __init__(self, world):
        super().__init__(world)
        if world.settings.get_flag(flags.SuperJump2Threshold).value < 100:
            self.access = 1

    def can_access(self, inventory):
        return inventory.has_item(items.SuperJumpLearn) and can_access_monstro_town(
            self.world, inventory
        )


class ThreeMustyFears(NPCReward):
    area = locations.Area.MonstroTown
    description = ShuffleLocationSelector.ThreeMustyFears.value
    rooms = [399]
    event = 253
    item = items.GhostMedal
    original_item = items.GhostMedal
    access = 2
    special_equip = True

    def can_access(self, inventory):
        return (
            inventory.has_item(items.BigBooFlag)
            and inventory.has_item(items.GreaperFlag)
            and inventory.has_item(items.DryBonesFlag)
        ) and can_access_monstro_town(self.world, inventory)


# *** Bean Valley


class BeanValley1(Chest):
    description = ShuffleLocationSelector.BeanValley1.value
    area = locations.Area.BeanValley
    rooms = [252]
    npc_ids = [3]
    event = 247
    item = items.Flower
    original_item = items.Flower


class BeanValley2(Chest):
    description = ShuffleLocationSelector.BeanValley2.value
    area = locations.Area.BeanValley
    rooms = [252]
    npc_ids = [4]
    event = 246
    item = items.FrogCoin
    original_item = items.FrogCoin


class BeanValleyLeftPiranhaPipe(Chest):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyLeftPiranhaPipe.value
    rooms = [334]
    npc_ids = [0]
    event = 247
    item = items.SlotMachineChest
    original_item = items.SlotMachineChest


class BeanValleyBottomLeftPiranhaPipe(Chest):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyBottomLeftPiranhaPipe.value
    rooms = [348]
    npc_ids = [0]
    event = 247
    item = items.SlotMachineChest
    original_item = items.SlotMachineChest


class BeanValleyBottomRightPiranhaPipeUpper(Chest):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyBottomRightPiranhaPipeUpper.value
    rooms = [349]
    npc_ids = [0]
    event = 247
    item = items.SlotMachineChest
    original_item = items.SlotMachineChest


class BeanValleyBottomRightPiranhaPipeLower(Chest):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyBottomRightPiranhaPipeLower.value
    rooms = [349]
    npc_ids = [2]
    event = 246
    item = items.KerokeroCola
    original_item = items.KerokeroCola


class BeanValleyBoxBoyRoom1(Chest):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyBoxBoyRoom1.value
    rooms = [335]
    npc_ids = [5]
    event = 247
    item = items.BoxBoyFight
    original_item = items.BoxBoyFight


class BoxBoyBossFightLocation(BossFightLocation):
    related_class = bosses.BoxBoy
    description = AvailableBosses.BoxBoy.value
    item = items.BoxBoyBossFight
    original_item = items.BoxBoyBossFight
    rooms = [514]
    event = 353

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.MimicsAnywhere, False):
            self.area = locations.Area.BeanValley

    def can_access(self, inventory):
        return inventory.has_item(items.BoxBoyFight)


class BoxBoyBoss(BossStarPiece):
    description = ShuffleLocationSelector.BoxBoyBoss.value
    rooms = [514]
    event = 167

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.MimicsAnywhere, False):
            self.area = locations.Area.BeanValley

    def can_access(self, inventory):
        return can_beat_mimic_3(self.world, inventory)


class BeanValleyBoxBoyRoom2(Chest):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyBoxBoyRoom2.value
    rooms = [335]
    event = 246
    npc_ids = [7]
    item = items.RedEssence
    original_item = items.RedEssence


class BeanValleyBoxBoyRoomHidden(NPCReward):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyBoxBoyRoomHidden.value
    rooms = [335]
    event = 253
    item = items.FrogCoin
    original_item = items.FrogCoin
    coinsanity = True


class BeanValleyPiranhaPlants(Chest):
    description = ShuffleLocationSelector.BeanValleyPiranhaPlants.value
    area = locations.Area.BeanValley
    rooms = [251]
    npc_ids = [13]
    event = 247
    item = items.FrogCoin
    original_item = items.FrogCoin


class MegaSmilaxBossFightLocation(BossFightLocation):
    related_class = bosses.MegaSmilax
    description = AvailableBosses.Megasmilax.value
    area = locations.Area.BeanValley
    item = items.MegaSmilaxBossFight
    original_item = items.MegaSmilaxBossFight
    rooms = [254]
    event = 353


class BeanValleyBoss(BossStarPiece):
    description = ShuffleLocationSelector.BeanValleyBoss.value
    area = locations.Area.BeanValley
    rooms = [254]
    event = 167

    def can_access(self, inventory):
        return (
            self.world.get_check_instance(MegaSmilaxBossFightLocation).item is not None
        )


class BeanValleyMegasmilaxRoom(NPCReward):
    description = ShuffleLocationSelector.BeanValleyMegasmilaxRoom.value
    area = locations.Area.BeanValley
    rooms = [254]
    event = 253
    item = items.Seed
    original_item = items.Seed
    key = True
    access = 2

    def item_allowed(self, item):
        if self.world.settings.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

    def can_access(self, inventory):
        return (
            self.world.get_check_instance(MegaSmilaxBossFightLocation).item is not None
        )


class BeanValleyBeanstalk(Chest):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyBeanstalk.value
    rooms = [379]
    npc_ids = [0]
    event = 247
    item = items.Flower
    original_item = items.Flower


class BeanValleyBeanstalkFrogCoin(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyBeanstalkFrogCoin.value
    rooms = [379]
    event = 241
    npc_ids = [6]
    item = items.FrogCoin
    original_item = items.FrogCoin


class BeanValleyBeanstalkCoin1(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyBeanstalkCoin1.value
    rooms = [379]
    event = 240
    npc_ids = [3]
    item = items.Coins10
    original_item = items.Coins10


class BeanValleyBeanstalkCoin2(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyBeanstalkCoin2.value
    rooms = [379]
    event = 239
    npc_ids = [4]
    item = items.Coins10
    original_item = items.Coins10


class BeanValleyBeanstalkCoin3(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyBeanstalkCoin3.value
    rooms = [379]
    event = 238
    npc_ids = [5]
    item = items.Coins10
    original_item = items.Coins10


class BeanValleyEastBeanstalkCoin1(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyEastBeanstalkCoin1.value
    rooms = [380]
    event = 241
    npc_ids = [3]
    item = items.Coins10
    original_item = items.Coins10


class BeanValleyEastBeanstalkCoin2(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyEastBeanstalkCoin2.value
    rooms = [380]
    event = 240
    npc_ids = [4]
    item = items.Coins10
    original_item = items.Coins10


class BeanValleyEastBeanstalkCoin3(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyEastBeanstalkCoin3.value
    rooms = [380]
    event = 239
    npc_ids = [5]
    item = items.Coins10
    original_item = items.Coins10


class BeanValleyEastBeanstalkCoin4(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyEastBeanstalkCoin4.value
    rooms = [380]
    event = 238
    npc_ids = [6]
    item = items.Coins10
    original_item = items.Coins10


class BeanValleyEastBeanstalkCoin5(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyEastBeanstalkCoin5.value
    rooms = [380]
    event = 237
    npc_ids = [7]
    item = items.Coins10
    original_item = items.Coins10


class BeanValleyWestBeanstalkCoin1(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyWestBeanstalkCoin1.value
    rooms = [381]
    event = 241
    npc_ids = [4]
    item = items.Coins10
    original_item = items.Coins10


class BeanValleyWestBeanstalkCoin2(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyWestBeanstalkCoin2.value
    rooms = [381]
    event = 240
    npc_ids = [5]
    item = items.Coins10
    original_item = items.Coins10


class BeanValleyWestBeanstalkCoin3(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyWestBeanstalkCoin3.value
    rooms = [381]
    event = 239
    npc_ids = [6]
    item = items.Coins10
    original_item = items.Coins10


class BeanValleyWestBeanstalkFrogCoin(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyWestBeanstalkFrogCoin.value
    rooms = [381]
    event = 238
    npc_ids = [7]
    item = items.FrogCoin
    original_item = items.FrogCoin


class BeanValleyCloud1(Chest):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyCloud1.value
    rooms = [372]
    npc_ids = [1]
    event = 247
    item = items.FrogCoin
    original_item = items.FrogCoin
    access = 2


class BeanValleyCloud2(Chest):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyCloud2.value
    rooms = [372]
    npc_ids = [2]
    event = 246
    item = items.RareScarf
    original_item = items.RareScarf
    access = 2


class BeanValleyFall1(Chest):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyFall1.value
    rooms = [373]
    npc_ids = [1]
    event = 247
    item = items.Flower
    original_item = items.Flower
    access = 2


class BeanValleyFall2(Chest):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyFall2.value
    rooms = [373]
    npc_ids = [2]
    event = 246
    item = items.Flower
    original_item = items.Flower
    access = 2


class BeanValleyFirstVineRoomFrogCoin(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyFirstVineRoomFrogCoin.value
    rooms = [378]
    event = 241
    npc_ids = [3]
    item = items.FrogCoin
    original_item = items.FrogCoin


class BeanValleyFirstVineRoomMiddleCoin(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyFirstVineRoomMiddleCoin.value
    rooms = [378]
    event = 240
    npc_ids = [4]
    item = items.Coins10
    original_item = items.Coins10


class BeanValleyFirstVineRoomUpperCoin(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyFirstVineRoomUpperCoin.value
    rooms = [378]
    event = 239
    npc_ids = [5]
    item = items.Coins10
    original_item = items.Coins10


class BeanValleyFirstVineRoomLowerCoin(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyFirstVineRoomLowerCoin.value
    rooms = [378]
    event = 238
    npc_ids = [6]
    item = items.Coins10
    original_item = items.Coins10


# *** Grate Guy's Casino


class CasinoGrateGuyPrize(NPCReward):
    area = locations.Area.Casino
    description = ShuffleLocationSelector.CasinoGrateGuyPrize.value
    rooms = [92]
    event = 253
    item = items.StarEgg
    original_item = items.StarEgg
    access = 2

    def can_access(self, inventory):
        return inventory.has_item(items.BrightCard)


# *** Nimbus Land


class NimbusLandShop(Chest):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusLandShop.value
    rooms = [344]
    npc_ids = [0]
    event = 247
    item = items.FrogCoin
    original_item = items.FrogCoin

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class NimbusLandInn(NPCReward):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusLandInn.value
    rooms = [346]
    event = 253
    item = items.RedEssence
    original_item = items.RedEssence


class NimbusLandInn2(NPCReward):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusLandInn2.value
    rooms = [346]
    event = 252
    item = items.RedEssence
    original_item = items.RedEssence


class DodoBossFightLocation(BossFightLocation):
    related_class = bosses.Dodo
    description = AvailableBosses.Dodo.value
    area = locations.Area.NimbusLand
    item = items.DodoBossFight
    original_item = items.DodoBossFight
    rooms = [520]
    event = 353


class NimbusLandStarPiece1(BossStarPiece):
    description = ShuffleLocationSelector.NimbusLandStarPiece1.value
    area = locations.Area.NimbusLand
    rooms = [520]
    event = 167

    def can_access(self, inventory):
        return self.world.get_check_instance(DodoBossFightLocation).item is not None


class DodoReward(NPCReward):
    description = ShuffleLocationSelector.DodoReward.value
    area = locations.Area.NimbusLand
    rooms = [110]
    event = 253
    item = items.Feather
    original_item = items.Feather
    missable = True
    access = 2

    def can_access(self, inventory):
        return self.world.get_check_instance(DodoBossFightLocation).item is not None


class NimbusLandPrisoners(NPCReward):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusLandPrisoners.value
    rooms = [414]
    event = 253
    item = items.FlowerJar
    original_item = items.FlowerJar


class NimbusLandPrisoners2(NPCReward):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusLandPrisoners2.value
    rooms = [414]
    event = 252
    item = items.CastleKey1
    original_item = items.CastleKey1
    key = True

    def item_allowed(self, item):
        if self.world.settings.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)


class NimbusCastleBeforeBirdetta1(Chest):
    description = ShuffleLocationSelector.NimbusCastleBeforeBirdetta1.value
    area = locations.Area.NimbusLand
    rooms = [118]
    npc_ids = [0]
    event = 247
    item = items.Flower
    original_item = items.Flower
    missable = True


class NimbusCastleBeforeBirdetta2(Chest):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusCastleBeforeBirdetta2.value
    rooms = [111, 500]
    npc_ids = [2, 0]
    event = 247
    item = items.Flower
    original_item = items.Flower


class NimbusCastleOutOfBounds1(Chest):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusCastleOutOfBounds1.value
    rooms = [410]
    npc_ids = [0]
    event = 247
    item = items.FrogCoin
    original_item = items.FrogCoin

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class NimbusCastleOutOfBounds2(Chest):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusCastleOutOfBounds2.value
    rooms = [410]
    npc_ids = [1]
    event = 246
    item = items.FrogCoin
    original_item = items.FrogCoin

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class NimbusCastleSingleGoldBird(Chest):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusCastleSingleGoldBird.value
    rooms = [113]
    npc_ids = [1]
    event = 247
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom


class NimbusCastleAfterEgg1(Chest):
    description = ShuffleLocationSelector.NimbusCastleAfterEgg1.value
    area = locations.Area.NimbusLand
    rooms = [114, 498]
    npc_ids = [0, 0]
    event = 247
    item = items.Flower
    original_item = items.Flower
    access = 2

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BirdettaBossFightLocation(BossFightLocation):
    related_class = bosses.Birdetta
    description = AvailableBosses.Birdetta.value
    area = locations.Area.NimbusLand
    item = items.BirdettaBossFight
    original_item = items.BirdettaBossFight
    rooms = [409]
    event = 353

    def can_access(self, inventory):
        return inventory.has_item(items.CastleKey1)

    # graphical restrictions
    def item_allowed(self, item):
        return (
            super().item_allowed(item)
            and not isclass_or_instance(item, items.ExorBossFight)
            and not isclass_or_instance(item, items.CloakerDominoBossFight)
            and not isclass_or_instance(item, items.KingCalamariBossFight)
            and not isclass_or_instance(item, items.CountdownBossFight)
            and not isclass_or_instance(item, items.SmithyBossFight)
            and not isclass_or_instance(item, items.AxemRangersBossFight)
            and not isclass_or_instance(item, items.MackBossFight)
            and not isclass_or_instance(item, items.Belome1BossFight)
            and not isclass_or_instance(item, items.BowyerBossFight)
            and not isclass_or_instance(item, items.GrateGuyBossFight)
            and not isclass_or_instance(item, items.JohnnyBossFight)
            and not isclass_or_instance(item, items.YaridovichBossFight)
            and not isclass_or_instance(item, items.Belome2BossFight)
            and not isclass_or_instance(item, items.CulexBossFight)
            and not isclass_or_instance(item, items.BoxBoyBossFight)
            and not isclass_or_instance(item, items.DodoBossFight)
            and not isclass_or_instance(item, items.ValentinaBossFight)
            and not isclass_or_instance(item, items.CzarDragonBossFight)
            and not isclass_or_instance(item, items.ChesterBossFight)
            and not isclass_or_instance(item, items.MagikoopaBossFight)
            and not isclass_or_instance(item, items.BoomerBossFight)
            and not isclass_or_instance(item, items.ClerkBossFight)
            and not isclass_or_instance(item, items.ManagerBossFight)
            and not isclass_or_instance(item, items.DirectorBossFight)
            and not isclass_or_instance(item, items.GunyolkBossFight)
            and not isclass_or_instance(item, items.SmithyBossFight)
        )


class NimbusCastleStarPiece2(BossStarPiece):
    description = ShuffleLocationSelector.NimbusCastleStarPiece2.value
    area = locations.Area.NimbusLand
    rooms = [409]
    event = 167
    access = 2

    def can_access(self, inventory):
        return can_clear_nimbus_midboss(self.world, inventory)


class NimbusCastleBirdetta(NPCReward):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusCastleBirdetta.value
    rooms = [409]
    event = 253
    item = items.CastleKey2
    original_item = items.CastleKey2
    key = True
    access = 2

    def item_allowed(self, item):
        if self.world.settings.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

    def can_access(self, inventory):
        return can_clear_nimbus_midboss(self.world, inventory)


class NimbusCastleAfterEgg2(Chest):
    description = ShuffleLocationSelector.NimbusCastleAfterEgg2.value
    area = locations.Area.NimbusLand
    rooms = [114, 498]
    npc_ids = [1, 1]
    event = 246
    item = items.FrogCoin
    original_item = items.FrogCoin
    access = 2

    def can_access(self, inventory):
        return can_access_nimbus_boss(self.world, inventory)


class NimbusCastleStarChest(Chest):
    description = ShuffleLocationSelector.NimbusCastleStarChest.value
    area = locations.Area.NimbusLand
    rooms = [121]
    npc_ids = [0]
    event = 247
    item = items.NimbusLandStar
    original_item = items.NimbusLandStar
    missable = True
    access = 2

    def can_access(self, inventory):
        return can_access_nimbus_boss(self.world, inventory)


class ValentinaBossFightLocation(BossFightLocation):
    related_class = bosses.Valentina
    description = AvailableBosses.Valentina.value
    area = locations.Area.NimbusLand
    item = items.ValentinaBossFight
    original_item = items.ValentinaBossFight
    rooms = [430]
    event = 353

    def can_access(self, inventory):
        return can_access_nimbus_boss(self.world, inventory)


class NimbusCastleStarPiece3(BossStarPiece):
    description = ShuffleLocationSelector.NimbusCastleStarPiece3.value
    area = locations.Area.NimbusLand
    rooms = [438]
    event = 167

    def can_access(self, inventory):
        return can_clear_nimbus_castle(self.world, inventory)


class NimbusCastleStarAfterValentina(Chest):
    description = ShuffleLocationSelector.NimbusCastleStarAfterValentina.value
    area = locations.Area.NimbusLand
    rooms = [121]
    npc_ids = [1]
    event = 246
    item = items.Flower
    original_item = items.Flower
    access = 2

    def can_access(self, inventory):
        return can_clear_nimbus_castle(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class NimbusCastleCornerChestAfterValentina(Chest):
    description = ShuffleLocationSelector.NimbusCastleCornerChestAfterValentina.value
    area = locations.Area.NimbusLand
    rooms = [499]
    npc_ids = [0]
    event = 247
    item = items.FrogCoin
    original_item = items.FrogCoin
    access = 2

    def can_access(self, inventory):
        return can_clear_nimbus_castle(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class NimbusLandRightSide(NPCReward):
    description = ShuffleLocationSelector.NimbusLandRightSide.value
    area = locations.Area.NimbusLand
    rooms = [438]
    event = 253
    item = items.Fertilizer
    original_item = items.Fertilizer
    key = True
    access = 2

    def item_allowed(self, item):
        if self.world.settings.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

    def can_access(self, inventory):
        return can_clear_nimbus_castle(self.world, inventory)


class NimbusLandSignalRing(OverworldItem):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusLandSignalRing.value
    rooms = [345]
    npc_ids = [5]
    event = 241
    item = items.SignalRing
    original_item = items.SignalRing
    coinsanity = False
    access = 2

    def can_access(self, inventory):
        return can_clear_nimbus_castle(self.world, inventory)


class NimbusLandCellar(NPCReward):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusLandCellar.value
    rooms = [413]
    event = 253
    item = items.FlowerJar
    original_item = items.FlowerJar
    access = 2

    def can_access(self, inventory):
        return can_clear_nimbus_castle(self.world, inventory)


# *** Barrel Volcano


class BarrelVolcanoSecret1(Chest):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoSecret1.value
    rooms = [355]
    npc_ids = [1]
    event = 247
    item = items.Flower
    original_item = items.Flower
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(
            flags.BarrelVolcanoGate, BarrelVolcanoGating.open
        ):
            self.access = 1

    def can_access(self, inventory):
        return can_access_volcano(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BarrelVolcanoSecret2(Chest):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoSecret2.value
    rooms = [355]
    npc_ids = [2]
    event = 246
    item = items.Flower
    original_item = items.Flower
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(
            flags.BarrelVolcanoGate, BarrelVolcanoGating.open
        ):
            self.access = 1

    def can_access(self, inventory):
        return can_access_volcano(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BarrelVolcanoReverse(OverworldItem):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoReverse.value
    rooms = [383]
    event = 241
    npc_ids = [4]
    item = items.FrogCoin
    original_item = items.FrogCoin
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(
            flags.BarrelVolcanoGate, BarrelVolcanoGating.open
        ):
            self.access = 1

    def can_access(self, inventory):
        return can_access_volcano(self.world, inventory)


class BarrelVolcanoDonut1(OverworldItem):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoDonut1.value
    rooms = [358]
    npc_ids = [1]
    event = 241
    item = items.FrogCoin
    original_item = items.FrogCoin
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(
            flags.BarrelVolcanoGate, BarrelVolcanoGating.open
        ):
            self.access = 1

    def can_access(self, inventory):
        return can_access_volcano(self.world, inventory)


class BarrelVolcanoDonut2(OverworldItem):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoDonut2.value
    rooms = [358]
    npc_ids = [2]
    event = 240
    item = items.FrogCoin
    original_item = items.FrogCoin
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(
            flags.BarrelVolcanoGate, BarrelVolcanoGating.open
        ):
            self.access = 1

    def can_access(self, inventory):
        return can_access_volcano(self.world, inventory)


class BarrelVolcanoLavaPool(OverworldItem):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoLavaPool.value
    rooms = [361]
    npc_ids = [1]
    event = 241
    item = items.FrogCoin
    original_item = items.FrogCoin
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(
            flags.BarrelVolcanoGate, BarrelVolcanoGating.open
        ):
            self.access = 1

    def can_access(self, inventory):
        return can_access_volcano(self.world, inventory)


class BarrelVolcanoBeforeStar1(Chest):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoBeforeStar1.value
    rooms = [384]
    npc_ids = [0]
    event = 247
    item = items.Flower
    original_item = items.Flower
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(
            flags.BarrelVolcanoGate, BarrelVolcanoGating.open
        ):
            self.access = 1

    def can_access(self, inventory):
        return can_access_volcano(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BarrelVolcanoBeforeStar2(Chest):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoBeforeStar2.value
    rooms = [384]
    npc_ids = [1]
    event = 246
    item = items.Coins(100)
    original_item = items.Coins(100)
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(
            flags.BarrelVolcanoGate, BarrelVolcanoGating.open
        ):
            self.access = 1

    def can_access(self, inventory):
        return can_access_volcano(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BarrelVolcanoStarRoom(Chest):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoStarRoom.value
    rooms = [385]
    npc_ids = [0]
    event = 247
    item = items.LandsEndVolcanoStar
    original_item = items.LandsEndVolcanoStar
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(
            flags.BarrelVolcanoGate, BarrelVolcanoGating.open
        ):
            self.access = 1

    def can_access(self, inventory):
        return can_access_volcano(self.world, inventory)


class BarrelVolcanoSaveRoom1(Chest):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoSaveRoom1.value
    rooms = [366]
    npc_ids = [0]
    event = 247
    item = items.Flower
    original_item = items.Flower
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(
            flags.BarrelVolcanoGate, BarrelVolcanoGating.open
        ):
            self.access = 1

    def can_access(self, inventory):
        return can_access_volcano(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BarrelVolcanoSaveRoom2(Chest):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoSaveRoom2.value
    rooms = [366]
    npc_ids = [1]
    event = 246
    item = items.FrogCoin
    original_item = items.FrogCoin
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(
            flags.BarrelVolcanoGate, BarrelVolcanoGating.open
        ):
            self.access = 1

    def can_access(self, inventory):
        return can_access_volcano(self.world, inventory)


class BarrelVolcanoHinopio(Chest):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoHinopio.value
    rooms = [367]
    npc_ids = [0]
    event = 247
    item = items.Coins(100)
    original_item = items.Coins(100)
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(
            flags.BarrelVolcanoGate, BarrelVolcanoGating.open
        ):
            self.access = 1

    def can_access(self, inventory):
        return can_access_volcano(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class CzarDragonBossFightLocation(BossFightLocation):
    related_class = bosses.CzarDragon
    description = AvailableBosses.CzarDragon.value
    area = locations.Area.BarrelVolcano
    item = items.CzarDragonBossFight
    original_item = items.CzarDragonBossFight
    rooms = [352]
    event = 353

    def can_access(self, inventory):
        return can_access_volcano(self.world, inventory)


class BarrelVolcanoBoss1(BossStarPiece):
    description = ShuffleLocationSelector.BarrelVolcanoBoss1.value
    area = locations.Area.BarrelVolcano
    rooms = [352]
    event = 167

    def can_access(self, inventory):
        return can_clear_volcano_midboss(self.world, inventory)


class AxemRangersBossFightLocation(BossFightLocation):
    related_class = bosses.AxemRangers
    description = AvailableBosses.AxemRangers.value
    area = locations.Area.BarrelVolcano
    item = items.AxemRangersBossFight
    original_item = items.AxemRangersBossFight
    rooms = [393]
    event = 353

    def can_access(self, inventory):
        return can_clear_volcano_midboss(self.world, inventory)


class BarrelVolcanoBoss2(BossStarPiece):
    description = ShuffleLocationSelector.BarrelVolcanoBoss2.value
    area = locations.Area.BarrelVolcano
    rooms = [393]
    event = 167
    item = items.StarPiece6
    original_item = items.StarPiece6

    def can_access(self, inventory):
        return can_clear_volcano(self.world, inventory)


# *** Bowser's Keep


class BowsersKeepDarkRoom(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepDarkRoom.value
    rooms = [453]
    npc_ids = [0]
    event = 247
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_access_keep(self.world, inventory)


class BowsersKeepCrocoShop1(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCrocoShop1.value
    rooms = [451]
    npc_ids = [0]
    event = 247
    item = items.Coins(150)
    original_item = items.Coins(150)
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_access_keep(self.world, inventory)


class BowsersKeepCrocoShop2(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCrocoShop2.value
    rooms = [451]
    npc_ids = [1]
    event = 246
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_access_keep(self.world, inventory)


class ChesterBossFightLocation(BossFightLocation):
    related_class = bosses.Chester
    description = AvailableBosses.Chester.value
    area = locations.Area.BowsersKeep
    item = items.ChesterBossFight
    original_item = items.ChesterBossFight
    rooms = [461]
    event = 353

    def can_access(self, inventory):
        return can_access_keep(self.world, inventory)


class BowsersKeepBossChester(BossStarPiece):
    description = ShuffleLocationSelector.BowsersKeepBossChester.value
    area = locations.Area.BowsersKeep
    rooms = [461]
    event = 167

    def can_access(self, inventory):
        return (
            can_access_keep(self.world, inventory)
            and self.world.get_check_instance(ChesterBossFightLocation).item is not None
        )


class BowsersKeepInvisibleBridge1(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepInvisibleBridge1.value
    rooms = [322]
    npc_ids = [4]
    event = 247
    item = items.FrightBomb
    original_item = items.FrightBomb
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BowsersKeepInvisibleBridge2(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepInvisibleBridge2.value
    rooms = [322]
    npc_ids = [5]
    event = 246
    item = items.RoyalSyrup
    original_item = items.RoyalSyrup
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BowsersKeepInvisibleBridge3(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepInvisibleBridge3.value
    rooms = [322]
    npc_ids = [6]
    event = 245
    item = items.IceBomb
    original_item = items.IceBomb
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BowsersKeepInvisibleBridge4(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepInvisibleBridge4.value
    rooms = [322]
    npc_ids = [7]
    event = 244
    item = items.RockCandy
    original_item = items.RockCandy
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BowsersKeepInvisibleBridgeCoin1(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepInvisibleBridgeCoin1.value
    rooms = [322]
    event = 241
    npc_ids = [8]
    item = items.Coins10
    original_item = items.Coins10
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)


class BowsersKeepInvisibleBridgeCoin2(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepInvisibleBridgeCoin2.value
    rooms = [322]
    event = 240
    npc_ids = [9]
    item = items.Coins10
    original_item = items.Coins10
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)


class BowsersKeepInvisibleBridgeCoin3(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepInvisibleBridgeCoin3.value
    rooms = [322]
    event = 239
    npc_ids = [10]
    item = items.Coins10
    original_item = items.Coins10
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)


class BowsersKeepInvisibleBridgeCoin4(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepInvisibleBridgeCoin4.value
    rooms = [322]
    event = 238
    npc_ids = [11]
    item = items.Coins10
    original_item = items.Coins10
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)


class BowsersKeepMovingPlatforms1(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepMovingPlatforms1.value
    rooms = [458]
    npc_ids = [10]
    event = 247
    item = items.Flower
    original_item = items.Flower
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BowsersKeepMovingPlatforms2(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepMovingPlatforms2.value
    rooms = [458]
    npc_ids = [11]
    event = 246
    item = items.RedEssence
    original_item = items.RedEssence
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BowsersKeepMovingPlatforms3(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepMovingPlatforms3.value
    rooms = [458]
    npc_ids = [12]
    event = 245
    item = items.MaxMushroom
    original_item = items.MaxMushroom
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BowsersKeepMovingPlatforms4(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepMovingPlatforms4.value
    rooms = [458]
    npc_ids = [13]
    event = 244
    item = items.FireBomb
    original_item = items.FireBomb
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BowsersKeepElevatorPlatforms(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepElevatorPlatforms.value
    rooms = [321]
    npc_ids = [8]
    event = 247
    item = items.KerokeroCola
    original_item = items.KerokeroCola
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BowsersKeepCannonballRoom1(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoom1.value
    rooms = [457]
    npc_ids = [3]
    event = 247
    item = items.Flower
    original_item = items.Flower
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BowsersKeepCannonballRoom2(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoom2.value
    rooms = [457]
    npc_ids = [4]
    event = 246
    item = items.Flower
    original_item = items.Flower
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BowsersKeepCannonballRoom3(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoom3.value
    rooms = [457]
    npc_ids = [5]
    event = 245
    item = items.PickMeUp
    original_item = items.PickMeUp
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BowsersKeepCannonballRoom4(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoom4.value
    rooms = [457]
    npc_ids = [6]
    event = 244
    item = items.RockCandy
    original_item = items.RockCandy
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BowsersKeepCannonballRoom5(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoom5.value
    rooms = [457]
    npc_ids = [7]
    event = 243
    item = items.MaxMushroom
    original_item = items.MaxMushroom
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BowsersKeepCannonballRoomCoin1(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoomCoin1.value
    rooms = [457]
    event = 241
    npc_ids = [8]
    item = items.Coins10
    original_item = items.Coins10
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)


class BowsersKeepCannonballRoomCoin2(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoomCoin2.value
    rooms = [457]
    event = 240
    npc_ids = [9]
    item = items.Coins10
    original_item = items.Coins10
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)


class BowsersKeepCannonballRoomCoin3(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoomCoin3.value
    rooms = [457]
    event = 239
    npc_ids = [10]
    item = items.Coins10
    original_item = items.Coins10
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)


class BowsersKeepCannonballRoomCoin4(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoomCoin4.value
    rooms = [457]
    event = 238
    npc_ids = [11]
    item = items.Coins10
    original_item = items.Coins10
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)


class BowsersKeepCannonballRoomCoin5(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoomCoin5.value
    rooms = [457]
    event = 237
    npc_ids = [12]
    item = items.Coins10
    original_item = items.Coins10
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)


class BowsersKeepCannonballRoomCoin6(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoomCoin6.value
    rooms = [457]
    event = 236
    npc_ids = [13]
    item = items.Coins10
    original_item = items.Coins10
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)


class BowsersKeepCannonballRoomCoin7(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoomCoin7.value
    rooms = [457]
    event = 235
    npc_ids = [14]
    item = items.Coins10
    original_item = items.Coins10
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)


class BowsersKeepCannonballRoomCoin8(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoomCoin8.value
    rooms = [457]
    event = 234
    npc_ids = [15]
    item = items.Coins10
    original_item = items.Coins10
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)


class BowsersKeepRotatingPlatforms1(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepRotatingPlatforms1.value
    rooms = [455]
    npc_ids = [1]
    event = 247
    item = items.Flower
    original_item = items.Flower
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BowsersKeepRotatingPlatforms2(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepRotatingPlatforms2.value
    rooms = [455]
    npc_ids = [2]
    event = 246
    item = items.Flower
    original_item = items.Flower
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BowsersKeepRotatingPlatforms3(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepRotatingPlatforms3.value
    rooms = [455]
    npc_ids = [3]
    event = 245
    item = items.FireBomb
    original_item = items.FireBomb
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BowsersKeepRotatingPlatforms4(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepRotatingPlatforms4.value
    rooms = [455]
    npc_ids = [4]
    event = 244
    item = items.RoyalSyrup
    original_item = items.RoyalSyrup
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BowsersKeepRotatingPlatforms5(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepRotatingPlatforms5.value
    rooms = [455]
    npc_ids = [5]
    event = 243
    item = items.PickMeUp
    original_item = items.PickMeUp
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BowsersKeepRotatingPlatforms6(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepRotatingPlatforms6.value
    rooms = [455]
    npc_ids = [6]
    event = 242
    item = items.KerokeroCola
    original_item = items.KerokeroCola
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class BowsersKeepDoorReward1(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepDoorReward1.value
    rooms = [144, 446]
    event = 247
    item = items.SonicCymbal
    original_item = items.SonicCymbal
    manual_70A7 = True
    access = 2

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return (
            super().item_allowed(item)
            and not isclass_or_instance(item, items.InvincibilityStar)
            and not isclass_or_instance(item, items.InfiniteCoins)
        )


class BowsersKeepDoorReward2(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepDoorReward2.value
    rooms = [144, 446]
    event = 246
    item = items.SuperSlap
    original_item = items.SuperSlap
    manual_70A7 = True
    access = 2

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return (
            super().item_allowed(item)
            and not isclass_or_instance(item, items.InvincibilityStar)
            and not isclass_or_instance(item, items.InfiniteCoins)
        )


class BowsersKeepDoorReward3(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepDoorReward3.value
    rooms = [144, 446]
    event = 245
    item = items.DrillClaw
    original_item = items.DrillClaw
    manual_70A7 = True
    access = 2

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return (
            super().item_allowed(item)
            and not isclass_or_instance(item, items.InvincibilityStar)
            and not isclass_or_instance(item, items.InfiniteCoins)
        )


class BowsersKeepDoorReward4(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepDoorReward4.value
    rooms = [144, 446]
    event = 244
    item = items.StarGun
    original_item = items.StarGun
    manual_70A7 = True
    access = 2

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return (
            super().item_allowed(item)
            and not isclass_or_instance(item, items.InvincibilityStar)
            and not isclass_or_instance(item, items.InfiniteCoins)
        )


class BowsersKeepDoorReward5(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepDoorReward5.value
    rooms = [144, 446]
    event = 243
    item = items.RockCandy
    original_item = items.RockCandy
    manual_70A7 = True
    access = 2

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return (
            super().item_allowed(item)
            and not isclass_or_instance(item, items.InvincibilityStar)
            and not isclass_or_instance(item, items.InfiniteCoins)
        )


class BowsersKeepDoorReward6(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepDoorReward6.value
    rooms = [144, 446]
    event = 242
    item = items.RockCandy
    original_item = items.RockCandy
    manual_70A7 = True
    access = 2

    def can_access(self, inventory):
        return can_pass_chester(self.world, inventory)

    def item_allowed(self, item):
        return (
            super().item_allowed(item)
            and not isclass_or_instance(item, items.InvincibilityStar)
            and not isclass_or_instance(item, items.InfiniteCoins)
        )


class MagikoopaBossFightLocation(BossFightLocation):
    related_class = bosses.Magikoopa
    description = AvailableBosses.Magikoopa.value
    area = locations.Area.BowsersKeep
    item = items.MagikoopaBossFight
    original_item = items.MagikoopaBossFight
    rooms = [266]
    event = 353

    def can_access(self, inventory):
        return can_clear_doors(self.world, inventory)


class BowsersKeepBoss1(BossStarPiece):
    description = ShuffleLocationSelector.BowsersKeepBoss1.value
    area = locations.Area.BowsersKeep
    rooms = [266]
    event = 167

    def can_access(self, inventory):
        return can_beat_magikoopa(self.world, inventory)


class BowsersKeepMagikoopa(Chest):
    description = ShuffleLocationSelector.BowsersKeepMagikoopa.value
    area = locations.Area.BowsersKeep
    rooms = [266]
    event = 247
    npc_ids = [0]
    item = items.InfiniteCoins
    original_item = items.InfiniteCoins
    access = 2

    def can_access(self, inventory):
        return can_beat_magikoopa(self.world, inventory)


class BoomerBossFightLocation(BossFightLocation):
    related_class = bosses.Boomer
    description = AvailableBosses.Boomer.value
    area = locations.Area.BowsersKeep
    item = items.BoomerBossFight
    original_item = items.BoomerBossFight
    rooms = [521]
    event = 353

    def can_access(self, inventory):
        return can_beat_magikoopa(self.world, inventory)


class BowsersKeepBoss2(BossStarPiece):
    description = ShuffleLocationSelector.BowsersKeepBoss2.value
    area = locations.Area.BowsersKeep
    rooms = [521]
    event = 167

    def can_access(self, inventory):
        return can_beat_boomer(self.world, inventory)


class ExorBossFightLocation(BossFightLocation):
    related_class = bosses.Exor
    description = AvailableBosses.Exor.value
    area = locations.Area.Factory
    item = items.ExorBossFight
    original_item = items.ExorBossFight
    rooms = [522]
    event = 353

    def can_access(self, inventory):
        return can_beat_boomer(self.world, inventory)


class BowsersKeepBoss3(BossStarPiece):
    description = ShuffleLocationSelector.BowsersKeepBoss3.value
    area = locations.Area.BowsersKeep
    rooms = [522]
    event = 167

    def can_access(self, inventory):
        return can_beat_exor(self.world, inventory)


# *** Factory


class FactorySaveRoom(Chest):
    area = locations.Area.Factory
    description = ShuffleLocationSelector.FactorySaveRoom.value
    rooms = [237]
    npc_ids = [1]
    event = 247
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.FactoryGate, FactoryGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_access_factory(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class FactoryBoltPlatforms(Chest):
    area = locations.Area.Factory
    description = ShuffleLocationSelector.FactoryBoltPlatforms.value
    rooms = [239]
    npc_ids = [7]
    event = 247
    item = items.UltraHammer
    original_item = items.UltraHammer
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.FactoryGate, FactoryGating.open):
            self.access = 1

    def can_access(self, inventory):
        return can_access_factory(self.world, inventory)

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.InvincibilityStar
        )


class CountDownBossFightLocation(BossFightLocation):
    related_class = bosses.Countdown
    description = AvailableBosses.CountDown.value
    area = locations.Area.Factory
    item = items.CountdownBossFight
    original_item = items.CountdownBossFight
    rooms = [223]
    event = 353

    def can_access(self, inventory):
        return can_access_factory(self.world, inventory)


class FactoryBoss1(BossStarPiece):
    description = ShuffleLocationSelector.FactoryBoss1.value
    area = locations.Area.Factory
    rooms = [433]
    event = 167

    def can_access(self, inventory):
        return can_clear_countdown(self.world, inventory)


class FactoryFallingAxems(Chest):
    area = locations.Area.Factory
    description = ShuffleLocationSelector.FactoryFallingAxems.value
    rooms = [434]
    npc_ids = [6]
    event = 247
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom
    access = 2

    def can_access(self, inventory):
        return can_clear_countdown(self.world, inventory)


class FactoryTreasurePit1(Chest):
    area = locations.Area.Factory
    description = ShuffleLocationSelector.FactoryTreasurePit1.value
    rooms = [443]
    npc_ids = [0]
    event = 247
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom
    access = 2

    def can_access(self, inventory):
        return can_clear_countdown(self.world, inventory)


class FactoryTreasurePit2(Chest):
    area = locations.Area.Factory
    description = ShuffleLocationSelector.FactoryTreasurePit2.value
    rooms = [443]
    npc_ids = [2]
    event = 245
    item = items.Flower
    original_item = items.Flower
    access = 2

    def can_access(self, inventory):
        return can_clear_countdown(self.world, inventory)


class FactoryConveyorPlatforms1(Chest):
    area = locations.Area.Factory
    description = ShuffleLocationSelector.FactoryConveyorPlatforms1.value
    rooms = [475]
    npc_ids = [8]
    event = 247
    item = items.RoyalSyrup
    original_item = items.RoyalSyrup
    access = 2

    def can_access(self, inventory):
        return can_clear_countdown(self.world, inventory)


class FactoryConveyorPlatforms2(Chest):
    area = locations.Area.Factory
    description = ShuffleLocationSelector.FactoryConveyorPlatforms2.value
    rooms = [475]
    npc_ids = [9]
    event = 246
    item = items.MaxMushroom
    original_item = items.MaxMushroom
    access = 2

    def can_access(self, inventory):
        return can_clear_countdown(self.world, inventory)


class FactoryBehindSnakes1(Chest):
    area = locations.Area.Factory
    description = ShuffleLocationSelector.FactoryBehindSnakes1.value
    rooms = [443]
    npc_ids = [1]
    event = 246
    item = items.RecoveryMushroom
    original_item = items.RecoveryMushroom
    access = 2

    def can_access(self, inventory):
        return can_clear_countdown(self.world, inventory)


class FactoryBehindSnakes2(Chest):
    area = locations.Area.Factory
    description = ShuffleLocationSelector.FactoryBehindSnakes2.value
    rooms = [443]
    npc_ids = [3]
    event = 244
    item = items.Flower
    original_item = items.Flower
    access = 2

    def can_access(self, inventory):
        return can_clear_countdown(self.world, inventory)


class CloakerDominoBossFightLocation(BossFightLocation):
    related_class = bosses.CloakerDomino
    description = AvailableBosses.CloakerDomino.value
    area = locations.Area.Factory
    item = items.CloakerDominoBossFight
    original_item = items.CloakerDominoBossFight
    rooms = [103]
    event = 353

    def can_access(self, inventory):
        return can_clear_countdown(self.world, inventory)


class FactoryBoss2(BossStarPiece):
    description = ShuffleLocationSelector.FactoryBoss2.value
    area = locations.Area.Factory
    rooms = [103]
    event = 167
    access = 2

    def can_access(self, inventory):
        return can_clear_snakes(self.world, inventory)


class ClerkBossFightLocation(BossFightLocation):
    related_class = bosses.Clerk
    description = AvailableBosses.Clerk.value
    area = locations.Area.Factory
    item = items.ClerkBossFight
    original_item = items.ClerkBossFight
    rooms = [469]
    event = 353

    def can_access(self, inventory):
        return can_clear_snakes(self.world, inventory)


class InnerFactoryBoss1(BossStarPiece):
    description = ShuffleLocationSelector.InnerFactoryBoss1.value
    area = locations.Area.InnerFactory
    rooms = [406]
    event = 167

    def can_access(self, inventory):
        return can_clear_clerk(self.world, inventory)


class FactoryToadGift(NPCReward):
    area = locations.Area.InnerFactory
    description = ShuffleLocationSelector.FactoryToadGift.value
    rooms = [406]
    event = 253
    item = items.RockCandy
    original_item = items.RockCandy
    access = 2

    def can_access(self, inventory):
        return can_clear_clerk(self.world, inventory)


class ManagerBossFightLocation(BossFightLocation):
    related_class = bosses.Manager
    description = AvailableBosses.Manager.value
    area = locations.Area.Factory
    item = items.ManagerBossFight
    original_item = items.ManagerBossFight
    rooms = [471]
    event = 353

    def can_access(self, inventory):
        return can_clear_clerk(self.world, inventory)


class InnerFactoryBoss2(BossStarPiece):
    description = ShuffleLocationSelector.InnerFactoryBoss2.value
    area = locations.Area.InnerFactory
    rooms = [470]
    event = 167

    def can_access(self, inventory):
        return can_clear_manager(self.world, inventory)


class DirectorBossFightLocation(BossFightLocation):
    related_class = bosses.Director
    description = AvailableBosses.Director.value
    area = locations.Area.Factory
    item = items.DirectorBossFight
    original_item = items.DirectorBossFight
    rooms = [472]
    event = 353

    def can_access(self, inventory):
        return can_clear_manager(self.world, inventory)


class InnerFactoryBoss3(BossStarPiece):
    description = ShuffleLocationSelector.InnerFactoryBoss3.value
    area = locations.Area.InnerFactory
    rooms = [471]
    event = 167

    def can_access(self, inventory):
        return can_clear_director(self.world, inventory)


class GunyolkBossFightLocation(BossFightLocation):
    related_class = bosses.Gunyolk
    description = AvailableBosses.Gunyolk.value
    area = locations.Area.Factory
    item = items.GunyolkBossFight
    original_item = items.GunyolkBossFight
    rooms = [470]
    event = 353

    def can_access(self, inventory):
        return can_clear_director(self.world, inventory)


class InnerFactoryBoss4(BossStarPiece):
    description = ShuffleLocationSelector.InnerFactoryBoss4.value
    area = locations.Area.InnerFactory
    rooms = [472]
    event = 167

    def can_access(self, inventory):
        return can_clear_chief(self.world, inventory)


class SmithyBossFightLocation(BossFightLocation):
    related_class = bosses.Smithy
    description = AvailableBosses.Smithy.value
    area = locations.Area.Factory
    item = items.SmithyBossFight
    original_item = items.SmithyBossFight
    rooms = [496]
    event = 353

    def can_access(self, inventory):
        return can_access_final_boss(self.world, inventory)


class InnerFactoryBossFinal(BossStarPiece):
    description = ShuffleLocationSelector.InnerFactoryBossFinal.value
    area = locations.Area.InnerFactory
    rooms = [523]
    event = 167

    def can_access(self, inventory):
        return can_clear_final_boss(self.world, inventory)


# "Musty Fears Flag Anywhere" locations


class MariosPadSteamwhistle(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (11, 34, 1)
    area = locations.Area.MariosPad
    clue = "\n  Mine is underneath a steamwhistle.[await]"
    rooms = [16]


class MariosPadLantern(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (13, 35, 0)
    shift = (8, -8)
    area = locations.Area.MariosPad
    clue = "\n    Mine is under a white lantern.[await]"
    rooms = [16]


class MushroomWayTree(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (11, 16, 3)
    shift = (-16, 0)
    area = locations.Area.MushroomWay
    clue = " Mine's under a tree, up on a ledge\n by itself.[await]"
    rooms = [204]


class MushroomKingdomSign(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (22, 116, 2)
    shift = (0, -8)
    area = locations.Area.MushroomKingdom
    clue = "\n  Mine's behind a wooden mushroom.[await]"
    rooms = [190, 191]


class MushroomKingdomEmptyHouse(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (14, 61, 0)
    shift = (0, 8)
    area = locations.Area.MushroomKingdom
    clue = " Mine is under the bed in an empty\n house.[await]"
    rooms = [482, 490]


class ChancellorThrone(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (19, 24, 3)
    area = locations.Area.MushroomKingdom
    clue = "\n       Mine's under a blue chair.[await]"
    rooms = [18, 326]


class BanditsWayFlower(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (25, 89, 0)
    shift = (16, 0)
    area = locations.Area.BanditsWay
    clue = "\n      Mine's on a landing flower.[await]"
    rooms = [207]


class KeroStairs(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (5, 41, 4)
    shift = (0, 8)
    area = locations.Area.KeroSewers
    clue = " Mine's in a corner, nearby lots of\n dank stairs.[await]"
    rooms = [60]


class KeroGate(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (4, 88, 4)
    shift = (-16, 0)
    area = locations.Area.KeroSewers
    clue = "\n Mine is by a lone metal spike fence.[await]"
    rooms = [62]


class MidasTrees(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (24, 26, 0)
    shift = (-8, 0)
    area = locations.Area.MidasRiver
    clue = " Mine's between a lone pair of\n palm trees.[await]"
    rooms = [67]


class TadpoleCabinet(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (25, 29, 2)
    shift = (8, 8)
    area = locations.Area.TadpolePond
    clue = "\n       Mine is in a frog cabinet.[await]"
    rooms = [75]


class RoseWayDirtPatch(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (25, 88, 0)
    area = locations.Area.RoseWay
    clue = " Mine is in the middle of a HUGE\n patch of dirt.[await]"
    rooms = [66]


class RoseTownHydrant(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (15, 63, 0)
    shift = (0, -8)
    area = locations.Area.RoseTown
    clue = "\n  Mine is under a low steel hydrant.[await]"
    rooms = [83, 84]


class RoseTownBowser(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (7, 21, 0)
    area = locations.Area.RoseTown
    clue = "\n   Mine's under a miniature turtle.[await]"
    rooms = [85, 86]


class RoseTownGardenerHydrant(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (2, 85, 0)
    shift = (0, -8)
    area = locations.Area.RoseTown
    clue = "\n   Mine is under a private hydrant.[await]"
    rooms = [417]

    def can_access(self, inventory):
        return (
            super().can_access(inventory)
            and can_clear_marrymore(self.world, inventory)
            and can_clear_forest(self.world, inventory)
        )


class RoseTownGardenerBucket(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (5, 87, 0)
    area = locations.Area.RoseTown
    clue = "\n   Mine is under a private bucket.[await]"
    rooms = [417]

    def can_access(self, inventory):
        return (
            super().can_access(inventory)
            and can_clear_marrymore(self.world, inventory)
            and can_clear_forest(self.world, inventory)
        )


class RoseTownGardenerLeaf(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (4, 111, 10)
    area = locations.Area.RoseTown
    clue = "\n Mine's on a big leaf between\n two chests.[await]"
    rooms = [419]

    def can_access(self, inventory):
        return (
            super().can_access(inventory)
            and can_clear_marrymore(self.world, inventory)
            and can_clear_forest(self.world, inventory)
            and inventory.has_item(items.Seed)
            and inventory.has_item(items.Fertilizer)
        )


class ForestMazeSecretStump(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (18, 72, 0)
    shift = (16, 0)
    area = locations.Area.ForestMaze
    clue = " Mine is behind a brightly\n illuminated tree stump.[await]"
    rooms = [231]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_forest(
            self.world, inventory
        )


class ForestMazeSecretMushrooms(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (25, 93, 0)
    shift = (-8, 8)
    area = locations.Area.ForestMaze
    clue = " Mine is on an illuminated pack of\n 5 mushrooms.[await]"
    rooms = [235]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_forest(
            self.world, inventory
        )


class ForestMazeSecretWiggler(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (2, 39, 0)
    area = locations.Area.ForestMaze
    clue = "\n        Mine is on a sleepy bug.[await]"
    rooms = [236]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_forest(
            self.world, inventory
        )


class PipeVaultExterior(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (17, 19, 0)
    shift = (-8, 8)
    area = locations.Area.PipeVault
    clue = " Mine is by a pipe in the middle of\n the road.[await]"
    rooms = [55]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_pipe_vault(
            self.world, inventory
        )


class PipeVaultRedPipe(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (21, 107, 0)
    shift = (-8, -8)
    area = locations.Area.PipeVault
    clue = "\n     Mine is behind a low red pipe.[await]"
    rooms = [129]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_pipe_vault(
            self.world, inventory
        )


class YosterIsleHut(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (11, 70, 0)
    area = locations.Area.YosterIsle
    clue = "\n         Mine's in a fruity hut.[await]"
    rooms = [34]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_pipe_vault(
            self.world, inventory
        )


class MolevilleHydrant(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (6, 63, 0)
    shift = (0, -8)
    area = locations.Area.Moleville
    clue = "\n     Mine's under a gold hydrant.[await]"
    rooms = [102, 108]


class MolevilleMountainBush(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (19, 31, 12)
    area = locations.Area.Moleville
    clue = " Mine's in a bush at the top of\n a mountain.[await]"
    rooms = [102, 108]


class MolevilleBed(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (6, 12, 0)
    shift = (16, 0)
    area = locations.Area.Moleville
    clue = "\n       Mine's under a middle bed.[await]"
    rooms = [337]


class MolevilleMinesArrows(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (5, 51, 0)
    area = locations.Area.Moleville
    clue = " Mine's between two arrows,\n pointing away from each other.[await]"
    rooms = [273]


class MolevilleMinesCeiling(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (8, 13, 4)
    area = locations.Area.Moleville
    clue = " Mine's in a zig-zag room, in a\n corner up above a lantern.[await]"
    rooms = [283]


class MolevilleMinesCartEntry(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (22, 23, 3)
    shift = (16, 0)
    area = locations.Area.Moleville
    clue = "\n My flag?[delay]\n ...[delay]It's on the word “IN”,\n [delay]above a big hole.[await]"
    rooms = [290]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_clear_mines(self.world, inventory)


class BoosterPassCornerBush(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (17, 112, 0)
    shift = (-8, -8)
    area = locations.Area.BoosterPass
    clue = "\n        Mine's in a corner bush.[await]"
    rooms = [101]


class BoosterTowerExteriorSign(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (4, 110, 0)
    shift = (16, 0)
    area = locations.Area.BoosterTower
    clue = " Mine's behind a sign with Japanese\n letters.[await]"
    rooms = [202]


class BoosterTowerDesk(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (24, 113, 0)
    shift = (16, 0)
    area = locations.Area.BoosterTower
    clue = "\n      Mine's under “B” and “K”.[await]"
    rooms = [43]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_tower(self.world, inventory)


class BoosterTowerMasherRoom(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (19, 122, 0)
    shift = (0, 8)
    area = locations.Area.BoosterTower
    clue = "\n Mine's on a lightly-loaded see-saw.[await]"
    rooms = [197]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_tower(self.world, inventory)


class BoosterTowerCurtain(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (7, 64, 9)
    shift = (0, 8)
    area = locations.Area.BoosterTower
    clue = " Mine's in a corner, between a\n window and a red curtain.[await]"
    rooms = [193]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_tower(self.world, inventory)


class BoosterTowerThwompInvisible(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (5, 114, 12)
    area = locations.Area.BoosterTower
    clue = "\n     Mine is near a lonely thwomp.[await]"
    rooms = [36]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_tower(self.world, inventory)


class BoosterTowerBrokenFrame(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (15, 83, 0)
    shift = (-8, -8)
    area = locations.Area.BoosterTower
    clue = "\n       Mine is in a broken frame.[await]"
    rooms = [38]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_tower(self.world, inventory)


class BoosterTowerBeetleCage(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (7, 18, 0)
    area = locations.Area.BoosterTower
    clue = "\n     Mine is on an insect's cage.[await]"
    rooms = [192]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_tower(self.world, inventory)


class BoosterTowerToyBox(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (7, 24, 0)
    shift = (16, 0)
    area = locations.Area.BoosterTower
    clue = "\n       Mine is behind a toy box.[await]"
    rooms = [192]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_tower(self.world, inventory)


class MarrymoreOutsideCrate(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (23, 60, 6)
    shift = (-8, -8)
    area = locations.Area.Marrymore
    clue = "\n  Mine is under a lone backyard box.[await]"
    rooms = [5, 64]


class MarrymoreSuiteBed(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (7, 13, 6)
    shift = (-16, 0)
    area = locations.Area.Marrymore
    clue = " Mine's beneath two adjoined\n red beds.[await]"
    rooms = [12]


class MarrymoreKitchen(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (2, 20, 0)
    shift = (-8, 8)
    area = locations.Area.Marrymore
    clue = " Mine is in a big cabinet full of\n dishes.[await]"
    rooms = [155]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_marrymore(
            self.world, inventory
        )


class MarrymoreFireplace(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (9, 33, 2)
    shift = (0, -8)
    area = locations.Area.Marrymore
    clue = "\n    Mine is in an empty fireplace.[await]"
    rooms = [152]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_marrymore(
            self.world, inventory
        )


class MarrymoreOrgan(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (23, 65, 1)
    shift = (-16, 0)
    area = locations.Area.Marrymore
    clue = " Mine is behind a big musical\n instrument.[await]"
    rooms = [65, 154]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_marrymore(
            self.world, inventory
        )


class MarrymoreAltar(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (23, 70, 1)
    area = locations.Area.Marrymore
    clue = "\n        Mine's behind an altar.[await]"
    rooms = [65, 154]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_marrymore(
            self.world, inventory
        )


class StarHillNorthStar(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (8, 69, 2)
    shift = (-10, 0)
    area = locations.Area.StarHill
    clue = "\n     Mine is atop the North Star.[await]"
    rooms = [158]


class SeasideTownAnchor(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (14, 57, 0)
    shift = (16, 0)
    area = locations.Area.SeasideTown
    clue = "\n       Mine is behind an anchor.[await]"
    rooms = [208]


class SeasideTownHydrant(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (16, 25, 5)
    shift = (0, -8)
    area = locations.Area.SeasideTown
    clue = "\n  Mine is under a high steel hydrant.[await]"
    rooms = [208]


class SeasideTownBucket(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (20, 31, 3)
    area = locations.Area.SeasideTown
    clue = "\n     Mine is in a stairway bucket.[await]"
    rooms = [208]


class SeasideTownFlowers(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (26, 60, 0)
    shift = (0, 8)
    area = locations.Area.SeasideTown
    clue = " Mine's in the middle of three\n pink flowers.[await]"
    rooms = [217, 313]


class SeasideTownShedBox(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (5, 23, 0)
    shift = (0, 8)
    area = locations.Area.SeasideTown
    clue = " Mine's under a lone crate in an\n empty house.[await]"
    rooms = [314]

    def can_access(self, inventory):
        return (
            super().can_access(inventory)
            and inventory.has_item(items.ShedKey)
            and can_clear_seaside(self.world, inventory)
        )


class SeaArrow(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (8, 21, 0)
    shift = (-8, -8)
    area = locations.Area.Sea
    clue = "\n   Mine is beside a mossy up-arrow.[await]"
    rooms = [130]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_sea(self.world, inventory)


class SeaBoxes(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (9, 36, 0)
    shift = (0, -8)
    area = locations.Area.Sea
    clue = "\n    Mine's in some V-shaped boxes.[await]"
    rooms = [130]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_sea(self.world, inventory)


class SeaStalagnate(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (18, 43, 6)
    shift = (-8, -8)
    area = locations.Area.Sea
    clue = " Mine is behind a big gray\n stalagnate.[await]"
    rooms = [133]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_sea(self.world, inventory)


class SeaSail(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (4, 41, 0)
    area = locations.Area.Sea
    clue = "\n        Mine's behind a big sail.[await]"
    rooms = [174]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_sea(self.world, inventory)


class ShipBarrelPile(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (7, 66, 3)
    area = locations.Area.SunkenShip
    clue = "\n  Mine is atop a big pile of barrels.[await]"
    rooms = [162]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_sea(self.world, inventory)


class ShipDoorMarker(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (18, 82, 1)
    shift = (0, 8)
    area = locations.Area.SunkenShip
    clue = " Mine is on a stack of boxes.[await][pause]\n[delay] Hm?[delay] Is that not specific enough?[await][page]\n Well,[delay] the boxes act as a door\n marker.[delay] They represent the\n number “4”.[await]"
    rooms = [165]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_sea(self.world, inventory)


class ShipButton(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (16, 133, 0)
    area = locations.Area.SunkenShip
    clue = "\n   Mine is under a floating button.[await]"
    rooms = [166]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_sea(self.world, inventory)


class ShipSwitch(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (17, 121, 0)
    area = locations.Area.SunkenShip
    clue = "\n  Mine is underneath a floating “J”.[await]"
    rooms = [179]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_clear_ship_midboss(
            self.world, inventory
        )


class LandsEndPlatform(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (6, 29, 0)
    area = locations.Area.LandsEnd
    clue = "\n   Mine is under a rising platform.[await]"
    rooms = [137]


class LandsEndCannon(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (11, 115, 0)
    shift = (0, -8)
    area = locations.Area.LandsEnd
    clue = " Mine's under a big and quiet\n cannon.[await]"
    rooms = [139]


class LandsEndArrow(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (28, 29, 0)
    shift = (16, 0)
    area = locations.Area.LandsEnd
    clue = "\n Mine is beside an orange up-arrow.[await]"
    rooms = [401]


class LandsEndHill(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (23, 96, 0)
    shift = (8, 8)
    area = locations.Area.LandsEnd
    clue = " Mine is on a short, red hill in a\n remote area.[await]"
    rooms = [404]


class LandsEndStalagmite(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (22, 80, 0)
    shift = (-4, 4)
    area = locations.Area.LandsEnd
    clue = " Mine's on a big stalagmite\n formation, in an underground cave.[await]"
    rooms = [265]


class LandsEndCliffBush(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (23, 103, 22)
    area = locations.Area.LandsEnd
    clue = " Mine is on a bush, way up high on\n a cliff.[await]"
    rooms = [407]

    def can_clear_temple(self, inventory):
        return super().can_access(inventory) and can_clear_ship_midboss(
            self.world, inventory
        )


class BeanValleyPipe(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (17, 85, 1)
    shift = (-16, 0)
    area = locations.Area.BeanValley
    clue = " Mine's on an isolated, dead-end\n pipe.[await]"
    rooms = [252]


class BeanValleyBeanstalkBlock(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (27, 27, 0)
    area = locations.Area.BeanValley
    clue = "\n  Mine's underneath a big beanstalk.[await]"
    rooms = [253]


class DojoBonsai(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (6, 9, 0)
    shift = (0, 8)
    area = locations.Area.MonstroTown
    clue = "\n   Mine's underneath a bonsai tree.[await]"
    rooms = [255]

    def can_access(self, inventory):
        return can_access_monstro_town(self.world, inventory)


class MonstroEntrance(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (9, 102, 0)
    area = locations.Area.MonstroTown
    clue = "\n     Mine's in a lone flowery bush.[await]"
    rooms = [267]

    def can_access(self, inventory):
        return can_access_monstro_town(self.world, inventory)


class MonstroBat(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (5, 51, 4)
    shift = (0, 8)
    area = locations.Area.MonstroTown
    clue = "\n     Mine's behind a wooden bat.[await]"
    rooms = [324]

    def can_access(self, inventory):
        return can_access_monstro_town(self.world, inventory)


class MonstroFan(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (12, 80, 1)
    shift = (-16, 0)
    area = locations.Area.MonstroTown
    clue = "\n       Mine's beside a room fan.[await]"
    rooms = [395]

    def can_access(self, inventory):
        return can_access_monstro_town(self.world, inventory)


class MonstroShell(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (16, 15, 1)
    shift = (0, 8)
    area = locations.Area.MonstroTown
    clue = "\n   Mine's beneath a spinning shell.[await]"
    rooms = [398]

    def can_access(self, inventory):
        return can_access_monstro_town(self.world, inventory)


class CasinoBell(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (14, 19, 0)
    shift = (8, 8)
    area = locations.Area.Casino
    clue = "\n       Mine is beside a tiny bell.[await]"
    rooms = [92]

    def can_access(self, inventory):
        return super().can_access(inventory) and inventory.has_item(items.BrightCard)


class NimbusGoldGoomba(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (5, 14, 1)
    area = locations.Area.NimbusLand
    clue = "\n     Mine is on a golden Goomba.[await]"
    rooms = [341]


class NimbusInnLobby(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (6, 84, 2)
    shift = (-8, -8)
    area = locations.Area.NimbusLand
    clue = " Mine is under a stove, between\n two pots.[await]"
    rooms = [343]


class NimbusPlant(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (27, 74, 1)
    area = locations.Area.NimbusLand
    clue = " Mine is behind a big potted plant\n in a corner.[await]"
    rooms = [117]


class NimbusBird(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (28, 48, 0)
    shift = (0, -8)
    area = locations.Area.NimbusLand
    clue = " Mine is under a birdcage, in a\n restricted dead-end area.[await]"
    rooms = [413]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_clear_nimbus_castle(inventory)


class NimbusHotSprings(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (19, 114, 5)
    area = locations.Area.NimbusLand
    clue = " Mine's on the right side of a\n hot pool.[await]"
    rooms = [447]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_volcano(
            self.world, inventory
        )


class VolcanoShips(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (11, 61, 2)
    area = locations.Area.BarrelVolcano
    clue = "\n    Mine is between two vehicles.[await]"
    rooms = [353]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_volcano(
            self.world, inventory
        )


class KeepMagikoopaRoom(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (26, 97, 0)
    shift = (8, 8)
    area = locations.Area.BowsersKeep
    clue = "\n  Mine is between two big red doors.[await]"
    rooms = [266]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_clear_doors(self.world, inventory)


class KeepThwomp(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (19, 47, 0)
    area = locations.Area.BowsersKeep
    clue = "\n      Mine is under a big thwomp.[await]"
    rooms = [449]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_beat_magikoopa(
            self.world, inventory
        )


class FactoryButton(InvisibleFlagLocation):
    item = None
    original_item = None
    coords = (4, 36, 5)
    area = locations.Area.InnerFactory
    clue = " Mine is on a jammed machine\n button.[await]"
    rooms = [406]

    def can_access(self, inventory):
        return super().can_access(inventory) and can_access_factory(
            self.world, inventory
        )


# ********************* Default objects for world


def get_default_chests(world):
    """Get default vanilla chest and reward list for the world.

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        list[ItemLocation]: List of default chest objects.
    """
    chests = [
        # Chests
        MariosPadStarter1(world),
        MariosPadStarter2(world),
        MariosPadStarter3(world),
        MariosPadStarter4(world),
        MushroomWay1(world),
        MushroomWay2(world),
        MushroomWay3(world),
        MushroomWay4(world),
        ToadRescue1(world),
        ToadRescue2(world),
        HammerBrosReward(world),
        MushroomKingdomHallway(world),
        MushroomKingdomVault1(world),
        MushroomKingdomVault2(world),
        MushroomKingdomVault3(world),
        InvasionVault1(world),
        InvasionVault2(world),
        InvasionVault3(world),
        InvasionEasternGuard(world),
        WalletGuy1(world),
        WalletGuy2(world),
        MushroomKingdomStore(world),
        MushroomKingdomStoreExchange(world),
        MushroomKingdomStoreBasement1(world),
        MushroomKingdomStoreBasement2(world),
        PeachSurprise(world),
        InvasionToadRescue(world),
        InvasionFamily(world),
        InvasionGuestRoom(world),
        MushroomKingdomInn(world),
        BanditsWay1(world),
        BanditsWay2(world),
        BanditsWayStarChest(world),
        BanditsWayDogJump(world),
        BanditsWayCroco(world),
        Croco1Reward(world),
        Croco1Reward2(world),
        KeroSewersPandoriteRoom(world),
        PandoriteChest(world),
        PandoriteReward1(world),
        PandoriteReward2(world),
        KeroSewersStarChest(world),
        KeroSewersBeforeBelomeLower(world),
        KeroSewersBeforeBelomeUpper1(world),
        KeroSewersBeforeBelomeUpper2(world),
        MidasRiverFirstTime(world),
        CricketPieReward(world),
        CricketJamReward(world),
        MelodyBay1(world),
        MelodyBay2(world),
        MelodyBay3(world),
        RoseWayPlatform(world),
        RoseWayFiveChests1(world),
        RoseWayFiveChests2(world),
        RoseWayFiveChests3(world),
        RoseWayFiveChests4(world),
        RoseWayFiveChests5(world),
        RoseTownStore1(world),
        RoseTownStore2(world),
        GardenerCloud1(world),
        GardenerCloud2(world),
        RoseTownToad(world),
        Gaz(world),
        RoseTownTreasureHouse1(world),
        RoseTownTreasureHouse2(world),
        RoseTownTreasureHouseMazeReward(world),
        RoseTownTreasureHouse3(world),
        ForestMaze1(world),
        ForestMaze2(world),
        ForestMazeUnderground1(world),
        ForestMazeUnderground2(world),
        ForestMazeUnderground3(world),
        ForestMazeRedEssence(world),
        ForestMazeSecret1(world),
        ForestMazeSecret2(world),
        ForestMazeSecret3(world),
        ForestMazeSecret4(world),
        ForestMazeSecret5(world),
        PipeVaultSlide1(world),
        PipeVaultSlide2(world),
        PipeVaultSlide3(world),
        PipeVaultNippers1(world),
        PipeVaultNippers2(world),
        GoombaThumping1(world),
        GoombaThumping2(world),
        YosterIsleEntrance(world),
        YosterIsleRaceReward1(world),
        YosterIsleRaceReward2(world),
        YosterIsleRaceReward3(world),
        BucketGirl(world),
        TreasureSeller1(world),
        TreasureSeller2(world),
        TreasureSeller3(world),
        FireworksShop(world),
        MolevilleMinesStarChest(world),
        MolevilleMinesShyGuy(world),
        MolevilleMinesCoins(world),
        MolevilleMinesPunchinello1(world),
        MolevilleMinesPunchinello2(world),
        CrocoFlunkie1(world),
        CrocoFlunkie2(world),
        CrocoFlunkie3(world),
        Croco2Item(world),
        BoosterPass1(world),
        BoosterPass2(world),
        BoosterPassSecret1(world),
        BoosterPassSecret2(world),
        BoosterPassSecret3(world),
        BoosterTowerSpookum(world),
        BoosterTowerThwomp(world),
        BoosterTowerKnifeGuy(world),
        BoosterTowerRoomKey(world),
        BoosterTowerMasher(world),
        BoosterTowerParachute(world),
        BoosterTowerZoomShoes(world),
        BoosterTowerTop1(world),
        BoosterTowerTop2(world),
        BoosterTowerTop3(world),
        BoosterTowerRailway(world),
        BoosterTowerPortraits(world),
        BoosterTowerChomp(world),
        BoosterTowerCurtainGame(world),
        MarrymorePrize1(world),
        MarrymorePrize2(world),
        MarrymorePrize3(world),
        MarrymorePrize4(world),
        MarrymorePrize5(world),
        MarrymorePrize6(world),
        MarrymoreSnifit1(world),
        MarrymoreSnifit2(world),
        MarrymoreSnifit3(world),
        MarrymoreInn(world),
        SeasideTownBossPrize(world),
        SeasideTownRescue(world),
        SeaStarChest(world),
        SeaSaveRoom1(world),
        SeaSaveRoom2(world),
        SeaSaveRoom3(world),
        SeaWhirlpoolChest(world),
        SunkenShipRatStairs(world),
        SunkenShipShop(world),
        SunkenShipCoins1(world),
        SunkenShipCoins2(world),
        SunkenShipCloneRoom(world),
        SunkenShipFrogCoinRoom(world),
        SunkenShipHidonMushroom(world),
        HidonChest(world),
        HidonReward1(world),
        HidonReward2(world),
        SunkenShipSafetyRing(world),
        SunkenShipBandanaReds(world),
        SunkenShip3DMaze(world),
        SunkenShipCannonballPuzzle(world),
        LandsEndRedEssence(world),
        LandsEndChowPit1(world),
        LandsEndChowPit2(world),
        LandsEndBeeRoom(world),
        LandsEndSecret1(world),
        LandsEndSecret2(world),
        LandsEndShyAway(world),
        LandsEndStarChest1(world),
        LandsEndStarChest2(world),
        LandsEndStarChest3(world),
        TroopaClimb(world),
        BelomeTempleFortuneTeller(world),
        BelomeTempleFortune1(world),
        BelomeTempleFortune2(world),
        BelomeTempleFortune3(world),
        BelomeTempleFortune4(world),
        BelomeTempleAfterFortune1(world),
        BelomeTempleAfterFortune2(world),
        BelomeTempleAfterFortune3(world),
        BelomeTempleAfterFortune4(world),
        BelomeTempleTreasure1(world),
        BelomeTempleTreasure2(world),
        BelomeTempleTreasure3(world),
        MonstroTownEntrance(world),
        MonstroTownThwomp(world),
        JinxDojoReward(world),
        CulexReward(world),
        ThreeMustyFears(world),
        BeanValley1(world),
        BeanValley2(world),
        BeanValleyLeftPiranhaPipe(world),
        BeanValleyBottomLeftPiranhaPipe(world),
        BeanValleyBottomRightPiranhaPipeUpper(world),
        BeanValleyBottomRightPiranhaPipeLower(world),
        BeanValleyBoxBoyRoom1(world),
        BeanValleyBoxBoyRoom2(world),
        BeanValleyPiranhaPlants(world),
        BeanValleyMegasmilaxRoom(world),
        BeanValleyBeanstalk(world),
        BeanValleyBeanstalkFrogCoin(world),
        BeanValleyCloud1(world),
        BeanValleyCloud2(world),
        BeanValleyFall1(world),
        BeanValleyFall2(world),
        CasinoGrateGuyPrize(world),
        NimbusLandShop(world),
        NimbusLandInn(world),
        NimbusLandInn2(world),
        NimbusCastleBeforeBirdetta1(world),
        NimbusCastleBeforeBirdetta2(world),
        NimbusCastleBirdetta(world),
        NimbusCastleOutOfBounds1(world),
        NimbusCastleOutOfBounds2(world),
        NimbusCastleSingleGoldBird(world),
        NimbusCastleAfterEgg1(world),
        NimbusCastleAfterEgg2(world),
        NimbusCastleStarChest(world),
        NimbusCastleStarAfterValentina(world),
        NimbusCastleCornerChestAfterValentina(world),
        NimbusLandRightSide(world),
        DodoReward(world),
        NimbusLandPrisoners(world),
        NimbusLandPrisoners2(world),
        NimbusLandSignalRing(world),
        NimbusLandCellar(world),
        BarrelVolcanoSecret1(world),
        BarrelVolcanoSecret2(world),
        BarrelVolcanoBeforeStar1(world),
        BarrelVolcanoBeforeStar2(world),
        BarrelVolcanoStarRoom(world),
        BarrelVolcanoSaveRoom1(world),
        BarrelVolcanoSaveRoom2(world),
        BarrelVolcanoHinopio(world),
        BowsersKeepDarkRoom(world),
        BowsersKeepCrocoShop1(world),
        BowsersKeepCrocoShop2(world),
        BowsersKeepMagikoopa(world),
        BowsersKeepInvisibleBridge1(world),
        BowsersKeepInvisibleBridge2(world),
        BowsersKeepInvisibleBridge3(world),
        BowsersKeepInvisibleBridge4(world),
        BowsersKeepMovingPlatforms1(world),
        BowsersKeepMovingPlatforms2(world),
        BowsersKeepMovingPlatforms3(world),
        BowsersKeepMovingPlatforms4(world),
        BowsersKeepElevatorPlatforms(world),
        BowsersKeepCannonballRoom1(world),
        BowsersKeepCannonballRoom2(world),
        BowsersKeepCannonballRoom3(world),
        BowsersKeepCannonballRoom4(world),
        BowsersKeepCannonballRoom5(world),
        BowsersKeepRotatingPlatforms1(world),
        BowsersKeepRotatingPlatforms2(world),
        BowsersKeepRotatingPlatforms3(world),
        BowsersKeepRotatingPlatforms4(world),
        BowsersKeepRotatingPlatforms5(world),
        BowsersKeepRotatingPlatforms6(world),
        BowsersKeepDoorReward1(world),
        BowsersKeepDoorReward2(world),
        BowsersKeepDoorReward3(world),
        BowsersKeepDoorReward4(world),
        BowsersKeepDoorReward5(world),
        BowsersKeepDoorReward6(world),
        FactorySaveRoom(world),
        FactoryBoltPlatforms(world),
        FactoryFallingAxems(world),
        FactoryTreasurePit1(world),
        FactoryTreasurePit2(world),
        FactoryConveyorPlatforms1(world),
        FactoryConveyorPlatforms2(world),
        FactoryBehindSnakes1(world),
        FactoryBehindSnakes2(world),
        FactoryToadGift(world),
        FrogDisciple1(world),
        FrogDisciple2(world),
        FrogDisciple3(world),
        FrogDisciple4(world),
        FrogDisciple5(world),
    ]
    world.eventscripts[91] = [
        {
            "identifier": "EVENT_91_jmp_if_set",
            "command": "jmp_if_bit_set",
            "args": [0x705F, 2, "EVENT_91_ret"],
        },
        {"identifier": "EVENT_91_set_bit", "command": "set_bit", "args": [0x705F, 2]},
    ]

    # these locations should be disabled if "Move invisible flag" checks is set
    if world.settings.is_flag_value(flags.InvisibleFlagsSetting, False):
        chests.extend(
            [
                MariosPadBed(world),
                RoseTownFlag(world),
                YosterIsleFlag(world),
            ]
        )
        world.eventscripts[91].extend(
            [
                {
                    "identifier": "EVENT_91_remove_0",
                    "command": "summon_to_level",
                    "args": [0x14 + 1, 189],
                },
                {
                    "identifier": "EVENT_91_remove_1",
                    "command": "summon_to_level",
                    "args": [0x14 + 3, 83],
                },
                {
                    "identifier": "EVENT_91_remove_2",
                    "command": "summon_to_level",
                    "args": [0x14 + 13, 84],
                },
                {
                    "identifier": "EVENT_91_remove_3",
                    "command": "summon_to_level",
                    "args": [0x14 + 16, 34],
                },
            ]
        )
        # hide these NPCs
        for t in [(189, 1), (83, 3), (84, 13), (34, 16)]:
            world.rooms[t[0]].objects[t[1]].visible = False

    else:
        # disable marios pad / rose town / yoster isle invis item checks
        world.eventscripts[2084] = [
            {"identifier": "EVENT_2084_jmp", "command": "jmp_to_event", "args": [256]}
        ]
        world.eventscripts[3823] = [
            {"identifier": "EVENT_3823_jmp", "command": "jmp_to_event", "args": [256]}
        ]
        world.eventscripts[3822] = [
            {"identifier": "EVENT_3822_jmp", "command": "jmp_to_event", "args": [256]}
        ]
        # pick 3 locations to replace them
        invisible_checks = random.sample(get_invisible_flag_choices(world), 3)
        # make the musty fears say the hint dialogs & associate their flags to locations
        world.replace_dialog(1109, invisible_checks[0].clue)
        invisible_checks[0].item = items.GreaperFlag
        invisible_checks[0].event = 88
        world.replace_dialog(1107, invisible_checks[1].clue)
        invisible_checks[1].item = items.BigBooFlag
        invisible_checks[1].event = 89
        world.replace_dialog(1108, invisible_checks[2].clue)
        invisible_checks[2].item = items.DryBonesFlag
        invisible_checks[2].event = 90
        # add checks to pool
        chests.extend(invisible_checks)
        for check, as_assignment, es_assignment in zip(
            invisible_checks, [460, 462, 204], [85, 86, 87]
        ):
            # set shifts in action scripts
            script = []
            x_pixels, y_pixels = check.shift
            if x_pixels < 0:
                script.append(
                    {
                        "identifier": "shift",
                        "command": "shift_west_pixels",
                        "args": [x_pixels * -1],
                    }
                )
            elif x_pixels > 0:
                script.append(
                    {
                        "identifier": "shift",
                        "command": "shift_east_pixels",
                        "args": [x_pixels],
                    }
                )
            if y_pixels < 0:
                script.append(
                    {
                        "identifier": "shift",
                        "command": "shift_south_pixels",
                        "args": [y_pixels * -1],
                    }
                )
            elif y_pixels > 0:
                script.append(
                    {
                        "identifier": "shift",
                        "command": "shift_north_pixels",
                        "args": [y_pixels],
                    }
                )
            script.append({"identifier": "ret", "command": "ret"})
            world.actionscripts[as_assignment] = copy.deepcopy([{**s} for s in script])

            eventscript = []
            x, y, z = check.coords

            is_visible = world.settings.is_flag_value(
                flags.SkipMustyFearsSequence, True
            )

            # write scripts to despawn the npc and grant the item, accounting for multiple versions of the same room
            eventscript.append(
                {
                    "identifier": "EVENT_%i_remove___" % (es_assignment),
                    "command": "remove_object_at_70A8_from_current_level",
                }
            )
            for index, room in enumerate(check.rooms):
                number_of_objects = len(world.rooms[room].objects)
                eventscript.append(
                    {
                        "identifier": "EVENT_%i_remove__%i" % (es_assignment, index),
                        "command": "remove_from_level",
                        "args": [0x14 + number_of_objects, room],
                    }
                )
                eventscript.append(
                    {
                        "identifier": "EVENT_%i_remove_-_%i" % (es_assignment, index),
                        "command": "remove_from_current_level",
                        "args": [0x14 + number_of_objects],
                    }
                )
                # add the npc to the rooms

                if world.rooms[room].partition is None:
                    world.rooms[room].partition = Partition()

                world.rooms[room].objects.append(
                    RegularNPC(
                        occupant=npcs.Empty,
                        initiator=Initiator.PRESS_A_FROM_ANY_SIDE,
                        event_script=es_assignment,
                        action_script=as_assignment,
                        visible=is_visible,
                        x=x,
                        y=y,
                        z=z,
                        cant_jump_through=True,
                        slidable_along_walls=True,
                        cant_move_if_in_air=True,
                        byte7_upper2=3,
                    )
                )
                # add summoner
                world.eventscripts[91].append(
                    {
                        "identifier": "EVENT_91_remove_%s" % (uuid.uuid4()),
                        "command": "summon_to_level",
                        "args": [0x14 + number_of_objects, room],
                    }
                )

            eventscript.extend(
                [
                    {
                        "identifier": "EVENT_%i_current_lvl" % es_assignment,
                        "command": "set_7000_to_current_level",
                    },
                    {
                        "identifier": "EVENT_%i_grant" % es_assignment,
                        "command": "jmp_to_event",
                        "args": [check.event],
                    },
                ]
            )
            world.eventscripts[es_assignment] = copy.deepcopy(
                [{**s} for s in eventscript]
            )

    world.eventscripts[91].append({"identifier": "EVENT_91_ret", "command": "ret"})

    # don't consider these as locations at all if super jump is turned off
    if (
        flags.LearnableSpells.SuperJump
        in world.settings.get_flag(flags.AvailableSpells).enabled
    ):
        chests.extend([SuperJumps30(world), SuperJumps100(world)])

    return chests


def get_invisible_flag_choices(world):
    return [
        MariosPadSteamwhistle(world),
        MariosPadLantern(world),
        MushroomWayTree(world),
        MushroomKingdomSign(world),
        MushroomKingdomEmptyHouse(world),
        ChancellorThrone(world),
        BanditsWayFlower(world),
        KeroGate(world),
        KeroStairs(world),
        MidasTrees(world),
        TadpoleCabinet(world),
        RoseWayDirtPatch(world),
        RoseTownHydrant(world),
        RoseTownBowser(world),
        RoseTownGardenerHydrant(world),
        RoseTownGardenerBucket(world),
        ForestMazeSecretStump(world),
        ForestMazeSecretMushrooms(world),
        ForestMazeSecretWiggler(world),
        PipeVaultExterior(world),
        PipeVaultRedPipe(world),
        YosterIsleHut(world),
        MolevilleHydrant(world),
        MolevilleMountainBush(world),
        MolevilleBed(world),
        MolevilleMinesArrows(world),
        MolevilleMinesCeiling(world),
        MolevilleMinesCartEntry(world),
        BoosterPassCornerBush(world),
        BoosterTowerExteriorSign(world),
        BoosterTowerDesk(world),
        BoosterTowerMasherRoom(world),
        BoosterTowerCurtain(world),
        BoosterTowerBrokenFrame(world),
        BoosterTowerThwompInvisible(world),
        BoosterTowerBeetleCage(world),
        BoosterTowerToyBox(world),
        MarrymoreOutsideCrate(world),
        MarrymoreSuiteBed(world),
        MarrymoreKitchen(world),
        MarrymoreFireplace(world),
        MarrymoreOrgan(world),
        MarrymoreAltar(world),
        StarHillNorthStar(world),
        SeasideTownAnchor(world),
        SeasideTownHydrant(world),
        SeasideTownBucket(world),
        SeasideTownFlowers(world),
        SeasideTownShedBox(world),
        SeaArrow(world),
        SeaBoxes(world),
        SeaStalagnate(world),
        SeaSail(world),
        ShipBarrelPile(world),
        ShipDoorMarker(world),
        ShipButton(world),
        ShipSwitch(world),
        LandsEndPlatform(world),
        LandsEndCannon(world),
        LandsEndArrow(world),
        LandsEndHill(world),
        LandsEndStalagmite(world),
        LandsEndCliffBush(world),
        BeanValleyPipe(world),
        BeanValleyBeanstalkBlock(world),
        DojoBonsai(world),
        MonstroEntrance(world),
        MonstroBat(world),
        MonstroFan(world),
        CasinoBell(world),
        NimbusGoldGoomba(world),
        NimbusInnLobby(world),
        NimbusPlant(world),
        NimbusBird(world),
        NimbusHotSprings(world),
        VolcanoShips(world),
        KeepMagikoopaRoom(world),
        KeepThwomp(world),
        FactoryButton(world),
    ]


def get_freestanding_item_checks(world):
    """Get reward lists for freestanding coins, frog coins, flowers, and mushrooms.

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        list[ItemLocation]: List of default freestanding objects.
    """
    return [
        # Chests
        BanditsWayCoin1(world),
        BanditsWayCoin2(world),
        BanditsWayCoin3(world),
        MidasRiverBottomLeftCave(world),
        MidasRiverBottomRightCave(world),
        RoseWayFlower(world),
        RoseWayMushroom(world),
        RoseWayCoin1(world),
        RoseWayCoin2(world),
        RoseWayCoin3(world),
        RoseWayCoin4(world),
        RoseWayCoin5(world),
        PipeVaultSlideCoin1(world),
        PipeVaultSlideCoin2(world),
        PipeVaultSlideCoin3(world),
        PipeVaultSlideCoin4(world),
        PipeVaultSlideCoin5(world),
        PipeVaultSlideFrogCoin(world),
        BoosterPassBush(world),
        BoosterPassFlower(world),
        BoosterTowerFrogCoin1(world),
        BoosterTowerFrogCoin2(world),
        BoosterTowerFrogCoin3(world),
        BoosterTowerFrogCoin4(world),
        BoosterTowerCoin1(world),
        BoosterTowerCoin2(world),
        BoosterTowerCoin3(world),
        BoosterTowerCoin4(world),
        BoosterTowerCoin5(world),
        BoosterTowerCoin6(world),
        BoosterTowerCoin7(world),
        BoosterTowerCoin8(world),
        BoosterTowerCoin9(world),
        BoosterTowerParachuteCrevice(world),
        MarrymoreAltarHead(world),
        SunkenShipRatStairsFlower(world),
        SunkenShipUnderwaterFrogCoin1(world),
        SunkenShipUnderwaterFrogCoin2(world),
        SunkenShipUnderwaterFrogCoin3(world),
        SunkenShipUnderwaterFrogCoin4(world),
        SunkenShipBlooberRoom(world),
        SunkenShipTrampolinePuzzle(world),
        SunkenShipTroopaPuzzle(world),
        SunkenShipCoinSnake(world),
        SunkenShipBarrelPuzzle(world),
        BelomeTempleTreasureFlower1(world),
        BelomeTempleTreasureFlower2(world),
        BelomeTempleTreasureFlower3(world),
        BelomeTempleTreasureFlower4(world),
        BelomeTempleTreasureFrogCoin1(world),
        BelomeTempleTreasureFrogCoin2(world),
        BelomeTempleTreasureFrogCoin3(world),
        BelomeTempleTreasureFrogCoin4(world),
        BelomeTempleTreasureFrogCoin5(world),
        BelomeTempleTreasureFrogCoin6(world),
        BelomeTempleTreasureFrogCoin7(world),
        BelomeTempleTreasureFrogCoin8(world),
        BeanValleyBoxBoyRoomHidden(world),
        BeanValleyBeanstalkFrogCoin(world),
        BeanValleyBeanstalkCoin1(world),
        BeanValleyBeanstalkCoin2(world),
        BeanValleyBeanstalkCoin3(world),
        BeanValleyEastBeanstalkCoin1(world),
        BeanValleyEastBeanstalkCoin2(world),
        BeanValleyEastBeanstalkCoin3(world),
        BeanValleyEastBeanstalkCoin4(world),
        BeanValleyEastBeanstalkCoin5(world),
        BeanValleyWestBeanstalkCoin1(world),
        BeanValleyWestBeanstalkCoin2(world),
        BeanValleyWestBeanstalkCoin3(world),
        BeanValleyWestBeanstalkFrogCoin(world),
        BeanValleyFirstVineRoomFrogCoin(world),
        BeanValleyFirstVineRoomMiddleCoin(world),
        BeanValleyFirstVineRoomUpperCoin(world),
        BeanValleyFirstVineRoomLowerCoin(world),
        BarrelVolcanoReverse(world),
        BarrelVolcanoDonut1(world),
        BarrelVolcanoDonut2(world),
        BarrelVolcanoLavaPool(world),
        BowsersKeepInvisibleBridgeCoin1(world),
        BowsersKeepInvisibleBridgeCoin2(world),
        BowsersKeepInvisibleBridgeCoin3(world),
        BowsersKeepInvisibleBridgeCoin4(world),
        BowsersKeepCannonballRoomCoin1(world),
        BowsersKeepCannonballRoomCoin2(world),
        BowsersKeepCannonballRoomCoin3(world),
        BowsersKeepCannonballRoomCoin4(world),
        BowsersKeepCannonballRoomCoin5(world),
        BowsersKeepCannonballRoomCoin6(world),
        BowsersKeepCannonballRoomCoin7(world),
        BowsersKeepCannonballRoomCoin8(world),
    ]


def get_boss_fight_placements(world):
    return [
        HammerBrosBossFightLocation(world),
        Croco1BossFightLocation(world),
        MackBossFightLocation(world),
        PandoriteBossFightLocation(world),
        Belome1BossFightLocation(world),
        BowyerBossFightLocation(world),
        Croco2BossFightLocation(world),
        PunchinelloBossFightLocation(world),
        BoosterBossFightLocation(world),
        ClownBrosBossFightLocation(world),
        BundtBossFightLocation(world),
        KingCalamariBossFightLocation(world),
        HidonBossFightLocation(world),
        JohnnyBossFightLocation(world),
        YaridovichBossFightLocation(world),
        MokuraBossFightLocation(world),
        Belome2BossFightLocation(world),
        JaggerBossFightLocation(world),
        Jinx1BossFightLocation(world),
        Jinx2BossFightLocation(world),
        Jinx3BossFightLocation(world),
        CulexBossFightLocation(world),
        BoxBoyBossFightLocation(world),
        MegaSmilaxBossFightLocation(world),
        DodoBossFightLocation(world),
        BirdettaBossFightLocation(world),
        ValentinaBossFightLocation(world),
        CzarDragonBossFightLocation(world),
        AxemRangersBossFightLocation(world),
        ChesterBossFightLocation(world),
        MagikoopaBossFightLocation(world),
        BoomerBossFightLocation(world),
        ExorBossFightLocation(world),
        CountDownBossFightLocation(world),
        CloakerDominoBossFightLocation(world),
        ClerkBossFightLocation(world),
        ManagerBossFightLocation(world),
        DirectorBossFightLocation(world),
        GunyolkBossFightLocation(world),
        SmithyBossFightLocation(world),
    ]


def get_boss_star_piece_checks(world):
    """Get list of star piece exclusive locations.

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        list[ItemLocation]: List of exclusive star piece location objects.
    """
    return [
        MushroomWayStarPiece(world),
        InvasionStarPiece(world),
        BanditsWayStarPiece(world),
        PandoriteBoss(world),
        KeroSewersBoss(world),
        ForestMazeBoss(world),
        MolevilleMinesBoss1(world),
        MolevilleMinesBoss2(world),
        BoosterTowerStarPiece1(world),
        BoosterTowerStarPiece2(world),
        MarrymoreStarPiece(world),
        StarHillStarPiece1(world),
        SeasideTownBoss(world),
        HidonBoss(world),
        SunkenShipMidboss(world),
        SunkenShipBoss(world),
        LandsEndStarPiece1(world),
        BelomeTempleBoss(world),
        DojoBoss1(world),
        DojoBoss2(world),
        DojoBoss3(world),
        DojoBoss4(world),
        CulexBoss(world),
        BoxBoyBoss(world),
        BeanValleyBoss(world),
        NimbusLandStarPiece1(world),
        NimbusCastleStarPiece2(world),
        NimbusCastleStarPiece3(world),
        BarrelVolcanoBoss1(world),
        BarrelVolcanoBoss2(world),
        BowsersKeepBossChester(world),
        BowsersKeepBoss1(world),
        BowsersKeepBoss2(world),
        BowsersKeepBoss3(world),
        FactoryBoss1(world),
        FactoryBoss2(world),
        InnerFactoryBoss1(world),
        InnerFactoryBoss2(world),
        InnerFactoryBoss3(world),
        InnerFactoryBoss4(world),
        InnerFactoryBossFinal(world),
    ]


def get_starter_character_checks(world):
    """Get list of starter character placeholders.

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        list[ItemLocation]: List of starter character placeholder objects.
    """
    return [
        StarterCharacter1(world),
        StarterCharacter2(world),
        StarterCharacter3(world),
        StarterCharacter4(world),
        StarterCharacter5(world),
    ]


def get_recruitable_character_checks(world):
    """Get list of recruitable character locations.

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        list[ItemLocation]: List of recruitable character location objects..
    """
    return [
        MushroomWayCharacter(world),
        ForestMazeCharacter(world),
        MolevilleMinesCharacter(world),
        MarrymoreCharacter(world),
    ]


def get_spotted_character_checks(world):
    """Get list of recruitable character locations.

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        list[ItemLocation]: List of recruitable character location objects..
    """
    return [MarrymoreCharacterSpotted(world)]


def get_spell_slots(world):
    slots = []

    if (
        PlayableCharacters.mario
        not in world.settings.get_flag(flags.AvailableCharacters).disabled
    ):
        slots.extend(
            [
                MarioSpell1(world),
                MarioSpell2(world),
                MarioSpell3(world),
                MarioSpell4(world),
                MarioSpell5(world),
                MarioSpell6(world),
            ]
        )
    if (
        PlayableCharacters.mallow
        not in world.settings.get_flag(flags.AvailableCharacters).disabled
    ):
        slots.extend(
            [
                MallowSpell1(world),
                MallowSpell2(world),
                MallowSpell3(world),
                MallowSpell4(world),
                MallowSpell5(world),
                MallowSpell6(world),
            ]
        )
    if (
        PlayableCharacters.geno
        not in world.settings.get_flag(flags.AvailableCharacters).disabled
    ):
        slots.extend(
            [
                GenoSpell1(world),
                GenoSpell2(world),
                GenoSpell3(world),
                GenoSpell4(world),
                GenoSpell5(world),
                GenoSpell6(world),
            ]
        )
    if (
        PlayableCharacters.bowser
        not in world.settings.get_flag(flags.AvailableCharacters).disabled
    ):
        slots.extend(
            [
                BowserSpell1(world),
                BowserSpell2(world),
                BowserSpell3(world),
                BowserSpell4(world),
                BowserSpell5(world),
                BowserSpell6(world),
            ]
        )
    if (
        PlayableCharacters.toadstool
        not in world.settings.get_flag(flags.AvailableCharacters).disabled
    ):
        slots.extend(
            [
                ToadstoolSpell1(world),
                ToadstoolSpell2(world),
                ToadstoolSpell3(world),
                ToadstoolSpell4(world),
                ToadstoolSpell5(world),
                ToadstoolSpell6(world),
            ]
        )

    return slots
