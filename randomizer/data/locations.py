# Data module for areas and location data and base classes for key item/chest shuffle..

from enum import Enum, auto
from inspect import isclass

from randomizer.logic import flags

from randomizer.data import items, spells
from randomizer.data.helpers import FireworksOptions, BanditsWayGating, ForestMazeGating, MarrymoreGating, BoosterTowerGating, SeaGating, YaridovichGating, BarrelVolcanoGating, BowsersKeepGating, FactoryGating, PipeVaultGating
from randomizer.data.characters import Mario, Mallow, Peach, Bowser, Geno
from randomizer.logic import utils
from randomizer.logic.patch import Patch


class Area(Enum):
    MariosPad = auto()
    MushroomWay = auto()
    MushroomKingdom = auto()
    BanditsWay = auto()
    KeroSewers = auto()
    MidasRiver = auto()
    TadpolePond = auto()
    RoseWay = auto()
    RoseTown = auto()
    RoseTownClouds = auto()
    ForestMaze = auto()
    Moleville = auto()
    MolevilleMines = auto()
    BoosterPass = auto()
    BoosterTower = auto()
    BoosterHill = auto()
    PipeVault = auto()
    YosterIsle = auto()
    Marrymore = auto()
    StarHill = auto()
    SeasideTown = auto()
    Sea = auto()
    SunkenShip = auto()
    LandsEnd = auto()
    BelomeTemple = auto()
    MonstroTown = auto()
    Casino = auto()
    BeanValley = auto()
    NimbusLand = auto()
    BarrelVolcano = auto()
    BowsersKeep = auto()
    Factory = auto()
    InnerFactory = auto()


class ItemLocation:
    """Base class for an item location, either a key item or quest reward or chest."""
    area = Area.MariosPad
    addresses = []
    _item = None
    missable = False
    access = 0
    not_depletable = False
    rooms = []
    script = None
    key = False
    coinsanity = False
    description = ""
    special_equip = False

    def __init__(self, world):
        """

        Args:
            world (randomizer.logic.main.GameWorld):

        """
        self.world = world

    def __str__(self):
        if isinstance(self.item, items.Item):
            item_str = self.item.name
        elif isclass(self.item):
            item_str = self.item.__name__
        else:
            item_str = str(self.item)
        return '<{}: item {}>'.format(self.__class__.__name__, item_str)

    def __repr__(self):
        return str(self)

    @property
    def name(self):
        return self.__class__.__name__

    def get_patch(self):
        """

        Returns:
            randomizer.logic.patch.Patch: Patch data

        """
        patch = Patch()

        for addr in self.addresses:
            patch.add_data(addr, utils.ByteField(self.item.index).as_bytes())

        return patch

    @staticmethod
    def can_access(inventory):
        """

        Args:
            inventory(Inventory): Current inventory of collected items.

        Returns:
            bool: True if this location is accessible with the given inventory, False otherwise.

        """
        return True

    def item_allowed(self, item):
        """

        Args:
            item(randomizer.data.items.Item|type): Item to check.

        Returns:
            bool: True if the given item is allowed to be placed in this spot, False otherwise.

        """
        # If this is a missable location, it cannot contain a key item.
        if self.missable and (item.is_key or utils.isclass_or_instance(item, items.MimicFight) or utils.isclass_or_instance(item, items.BrightCard) or utils.isclass_or_instance(item, items.SignalRing)):
            return False

        # If this is an excluded location, it cannot contain a key item.
        if item.is_key and (self.description in self.world.settings.get_flag(flags.EnabledRegularChecks).disabled or self.description in self.world.settings.get_flag(flags.EnabledFreestandingChecks).disabled or self.description in self.world.settings.get_flag(flags.EnabledFreestandingChecks).disabled or self.description in self.world.settings.get_flag(flags.EnabledBossChecks).disabled):
            return False

        return True

    @property
    def has_item(self):
        return self.item is not None

    @property
    def item(self):
        """
        Returns:
            randomizer.data.items.Item|type: Item in this spot.
        """
        return self._item

    @item.setter
    def item(self, value):
        """
        Args:
            value(randomizer.data.items.Item|type): Item to place in this location, if allowed.
        """
        if not utils.isclass_or_instance(value, items.Item):
            raise ValueError(
                "Location {} - Trying to assign value {} that isn't an item class".format(self, value))
        if not self.item_allowed(value):
            raise ValueError(
                "Location {} - Item {} not allowed".format(self, value))
        self._item = value




class BowserRoom:
    relative_room_id = 0
    next_room_address = 0
    next_coord_address = 0
    start_x = 0
    start_y = 0
    start_z = 0
    backward_exit_byte = 0
    backward_event_byte = 0
    change_event_byte = 0
    change_event = 0
    is_final = False
    event_2120_location = 0
    original_event = []
    original_event_location = 0
    jump_address = []
    jump_to_address = 0
    memory_700A_jump_address = 0
    needs_manual_run_on_exit = False


class BowserDoorQuiz(BowserRoom):
    relative_room_id = 0xD0
    next_room_address = 0x1E234F
    next_coord_address = 0x1E2351
    change_event_byte = 0x20ED2E
    start_x = 3
    start_y = 106
    event_2120_location = 0x1F7A50
    original_event = [0x0F, 0x00]
    original_event_location = 0x20FC03
    jump_address = [0xED, 0x22]
    jump_to_address = 0x1E22B4
    memory_700A_jump_address = 0x1E2293
    memory_700A_load_address = 0x1E2302
    needs_manual_run_on_exit = True


class BowserDoorBarrel(BowserRoom):
    relative_room_id = 0xCF
    next_room_address = 0x1E2356
    next_coord_address = 0x1E2358
    change_event_byte = 0x20EDD3
    start_x = 2
    start_y = 55
    event_2120_location = 0x1F7A55
    original_event = [0x1A, 0x0D]
    original_event_location = 0x20FC00
    jump_address = [0xF4, 0x22]
    jump_to_address = 0x1E22B9
    memory_700A_jump_address = 0x1E2299
    memory_700A_load_address = 0x1E2313
    needs_manual_run_on_exit = True


class BowserDoorMarathon(BowserRoom):
    relative_room_id = 0xD2
    next_room_address = 0x1E22ED
    next_coord_address = 0x1E22EF
    change_event_byte = 0x20FC11
    start_x = 12
    start_y = 97
    is_final = True
    original_event = [0x24, 0x0D]
    original_event_location = 0x20FC0F
    jump_address = [0xFB, 0x22]
    jump_to_address = 0x1E2295
    memory_700A_jump_address = 0x1E229F
    memory_700A_load_address = 0x1E2321


class BowserDoorCoin(BowserRoom):
    relative_room_id = 0xD3
    next_room_address = 0x1E235D
    next_coord_address = 0x1E235F
    change_event_byte = 0x20F0EE
    start_x = 22
    start_y = 83
    event_2120_location = 0x1F7A5A
    original_event = [0x0F, 0x00]
    original_event_location = 0x20FC18
    jump_address = [0x02, 0x23]
    jump_to_address = 0x1E22BE
    memory_700A_jump_address = 0x1E22A5
    memory_700A_load_address = 0x1E2332
    needs_manual_run_on_exit = True


class BowserDoorButton(BowserRoom):
    relative_room_id = 0xD1
    next_room_address = 0x1E2364
    next_coord_address = 0x1E2366
    change_event_byte = 0x20F2A4
    start_x = 22
    start_y = 33
    event_2120_location = 0x1F7A5F
    original_event = [0x1E, 0x0D]
    original_event_location = 0x20FC06
    jump_address = [0x09, 0x23]
    jump_to_address = 0x1E22C3
    memory_700A_jump_address = 0x1E22AB
    memory_700A_load_address = 0x1E2343
    needs_manual_run_on_exit = True


class BowserDoorSolitaire(BowserRoom):
    relative_room_id = 0xD4
    next_room_address = 0x1E22F4
    next_coord_address = 0x1E22F6
    change_event_byte = 0x20FC1D
    start_x = 22
    start_y = 123
    is_final = True
    original_event = [0xC2, 0x0E]
    original_event_location = 0x20FC1B
    jump_address = [0x10, 0x23]
    jump_to_address = 0x1E229A
    memory_700A_jump_address = 0x1E22B1
    memory_700A_load_address = 0x1E2358


class BowserDoorInvisible(BowserRoom):
    relative_room_id = 0x42
    next_room_address = 0x1E2317
    next_coord_address = 0x1E2319
    change_event_byte = 0x20F38C
    start_x = 8
    start_y = 115
    start_z = 2
    event_2120_location = 0x1F7A64
    original_event = [0x22, 0x07]
    original_event_location = 0x20F466
    jump_address = [0x17, 0x23]
    jump_to_address = 0x1E22C8
    memory_700A_jump_address = 0x1E22B7
    memory_700A_load_address = 0x1E2369
    needs_manual_run_on_exit = True


class BowserDoorXY(BowserRoom):
    relative_room_id = 0xCA
    next_room_address = 0x1E231E
    next_coord_address = 0x1E2320
    change_event_byte = 0x20F38F
    start_x = 7
    start_y = 117
    start_z = 2
    backward_exit_byte = 0x1D46F1
    backward_event_byte = 0x20FB8B
    event_2120_location = 0x1F7A69
    original_event = [0x23, 0x07]
    original_event_location = 0x20FB85
    jump_address = [0x1E, 0x23]
    jump_to_address = 0x1E22CD
    memory_700A_jump_address = 0x1E22BD
    memory_700A_load_address = 0x1E237A
    needs_manual_run_on_exit = True


class BowserDoorDonkey(BowserRoom):
    relative_room_id = 0xC8
    next_room_address = 0x1E22FB
    next_coord_address = 0x1E22FD
    change_event_byte = 0x20FB75
    start_x = 22
    start_y = 123
    is_final = True
    backward_exit_byte = 0x1D46D6
    original_event = [0x2C, 0x07]
    original_event_location = 0x20FB73
    jump_address = [0x25, 0x23]
    jump_to_address = 0x1E229F
    memory_700A_jump_address = 0x1E22C3
    memory_700A_load_address = 0x1E238B


class BowserDoorZ(BowserRoom):
    relative_room_id = 0x41
    next_room_address = 0x1E2325
    next_coord_address = 0x1E2327
    change_event_byte = 0x20F392
    start_x = 4
    start_y = 58
    start_z = 5
    event_2120_location = 0x1F7A6E
    original_event = [0x20, 0x07]
    original_event_location = 0x20F463
    jump_address = [0x2C, 0x23]
    jump_to_address = 0x1E22D2
    memory_700A_jump_address = 0x1E22C9
    memory_700A_load_address = 0x1E239C
    needs_manual_run_on_exit = True


class BowserDoorCannonball(BowserRoom):
    relative_room_id = 0xC9
    next_room_address = 0x1E232C
    next_coord_address = 0x1E232E
    change_event_byte = 0x20F395
    start_x = 2
    start_y = 57
    backward_exit_byte = 0x1D46DF
    backward_event_byte = 0x20FB82
    event_2120_location = 0x1F7A73
    original_event = [0x2B, 0x07]
    original_event_location = 0x20FB7C
    jump_address = [0x33, 0x23]
    jump_to_address = 0x1E22D7
    memory_700A_jump_address = 0x1E22CF
    memory_700A_load_address = 0x1E23AD
    needs_manual_run_on_exit = True


class BowserDoorRotating(BowserRoom):
    relative_room_id = 0xC7
    next_room_address = 0x1E2302
    next_coord_address = 0x1E2304
    change_event_byte = 0x20FB6C
    start_x = 6
    start_y = 47
    start_z = 1
    is_final = True
    backward_exit_byte = 0x1D46CD
    original_event = [0x21, 0x07]
    original_event_location = 0x20FB6A
    jump_address = [0x3A, 0x23]
    jump_to_address = 0x1E22A4
    memory_700A_jump_address = 0x1E22D5
    memory_700A_load_address = 0x1E23BE


class BowserDoorTerraCotta(BowserRoom):
    relative_room_id = 0xCB
    next_room_address = 0x1E2333
    next_coord_address = 0x1E2335
    change_event_byte = 0x20F398
    start_x = 2
    start_y = 63
    event_2120_location = 0x1F7A78
    original_event = [0x70, 0x08]
    original_event_location = 0x20FB8E
    jump_address = [0x41, 0x23]
    jump_to_address = 0x1E22DC
    memory_700A_jump_address = 0x1E22DB
    memory_700A_load_address = 0x1E23CF
    needs_manual_run_on_exit = True


class BowserDoorAlleyRat(BowserRoom):
    relative_room_id = 0xCC
    next_room_address = 0x1E233A
    next_coord_address = 0x1E233C
    change_event_byte = 0x20F39B
    start_x = 2
    start_y = 63
    event_2120_location = 0x1F7A7D
    original_event = [0x75, 0x08]
    original_event_location = 0x20FBA9
    jump_address = [0x48, 0x23]
    jump_to_address = 0x1E22E1
    memory_700A_jump_address = 0x1E22E1
    memory_700A_load_address = 0x1E23E0
    needs_manual_run_on_exit = True


class BowserDoorBobomb(BowserRoom):
    relative_room_id = 0xCD
    next_room_address = 0x1E2309
    next_coord_address = 0x1E230B
    change_event_byte = 0x20FBDE
    start_x = 2
    start_y = 63
    is_final = True
    original_event = [0x7A, 0x08]
    original_event_location = 0x20FBC4
    jump_address = [0x4F, 0x23]
    jump_to_address = 0x1E22A9
    memory_700A_jump_address = 0x1E22E7
    memory_700A_load_address = 0x1E23F1


class BowserDoorGuGoomba(BowserRoom):
    relative_room_id = 0xCE
    next_room_address = 0x1E2341
    next_coord_address = 0x1E2343
    change_event_byte = 0x20F39E
    start_x = 2
    start_y = 63
    event_2120_location = 0x1F7A82
    original_event = [0x7F, 0x08]
    original_event_location = 0x20FBE5
    jump_address = [0x56, 0x23]
    jump_to_address = 0x1E22E6
    memory_700A_jump_address = 0x1E22ED
    memory_700A_load_address = 0x1E2402
    needs_manual_run_on_exit = True


class BowserDoorChewy(BowserRoom):
    relative_room_id = 0x78
    next_room_address = 0x1E2348
    next_coord_address = 0x1E234A
    change_event_byte = 0x20F3A1
    start_x = 2
    start_y = 63
    event_2120_location = 0x1F7A87
    original_event = [0x84, 0x08]
    original_event_location = 0x20F6CE
    jump_address = [0x5D, 0x23]
    jump_to_address = 0x1E22EB
    memory_700A_jump_address = 0x1E22F3
    memory_700A_load_address = 0x1E2413
    needs_manual_run_on_exit = True


class BowserDoorSparky(BowserRoom):
    relative_room_id = 0x79
    next_room_address = 0x1E2310
    next_coord_address = 0x1E2312
    change_event_byte = 0x20F703
    start_x = 2
    start_y = 63
    is_final = True
    original_event = [0x89, 0x08]
    original_event_location = 0x20F6E9
    jump_address = [0x64, 0x23]
    jump_to_address = 0x1E22AE
    memory_700A_jump_address = 0x1E22F9
    memory_700A_load_address = 0x1E2424


# *** Helper functions to check access to certain areas.

def can_access_mines_back(inventory):
    """

    Args:
        inventory (randomizer.logic.keys.Inventory):

    Returns:
        bool: True if this location is accessible with the given inventory, False otherwise.

    """
    # Bambino Bomb is needed to access this location.
    return inventory.has_item(items.BambinoBomb)


def can_access_birdo(inventory):
    """

    Args:
        inventory (randomizer.logic.keys.Inventory):

    Returns:
        bool: True if this location is accessible with the given inventory, False otherwise.

    """
    # Castle Key 1 is needed to access this location.
    return inventory.has_item(items.CastleKey1)


def can_clear_nimbus_castle(inventory):
    """

    Args:
        inventory (randomizer.logic.keys.Inventory):

    Returns:
        bool: True if this location is accessible with the given inventory, False otherwise.

    """
    # Castle Key 2 is needed to access this location, plus defeating Birdo.
    return can_access_birdo(inventory) and inventory.has_item(items.CastleKey2)


def can_access_bandits_way(world, inventory):
    if world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.RecruitMario):
        return inventory.has_item(items.MarioRecruit)
    elif world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.RecruitMallow):
        return inventory.has_item(items.MallowRecruit)
    elif world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.RecruitGeno):
        return inventory.has_item(items.GenoRecruit)
    elif world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.RecruitBowser):
        return inventory.has_item(items.BowserRecruit)
    elif world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.RecruitToadstool):
        return inventory.has_item(items.ToadstoolRecruit)
    else:
        return True


def can_access_tower(world, inventory):
    if world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.RecruitMario):
        return inventory.has_item(items.MarioRecruit)
    elif world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.RecruitMallow):
        return inventory.has_item(items.MallowRecruit)
    elif world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.RecruitGeno):
        return inventory.has_item(items.GenoRecruit)
    elif world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.RecruitBowser):
        return inventory.has_item(items.BowserRecruit)
    elif world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.RecruitToadstool):
        return inventory.has_item(items.ToadstoolRecruit)
    elif world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.FinishMoleville):
        return inventory.has_item(items.BambinoBomb)
    else:
        return True


def can_access_marrymore(world, inventory):
    if world.settings.is_flag_value(flags.MarrymoreGate, MarrymoreGating.FinishBoosterTower):
        return can_access_tower(world, inventory)
    else:
        return True


def can_access_forest(world, inventory):
    if world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindMario):
        return inventory.has_item(items.MarioRecruit) or inventory.has_item(items.MarioSpotted)
    elif world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindMallow):
        return inventory.has_item(items.MallowRecruit) or inventory.has_item(items.MallowSpotted)
    elif world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindGeno):
        return inventory.has_item(items.GenoRecruit) or inventory.has_item(items.GenoSpotted)
    elif world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindBowser):
        return inventory.has_item(items.BowserRecruit) or inventory.has_item(items.BowserSpotted)
    elif world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindToadstool):
        return inventory.has_item(items.ToadstoolRecruit) or inventory.has_item(items.ToadstoolSpotted)
    elif world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.ExchangeCricketPie):
        return inventory.has_item(items.CricketPie)
    else:
        return True


def can_access_pipe_vault(world, inventory):
    if world.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.RecruitMario):
        return inventory.has_item(items.MarioRecruit) or inventory.has_item(items.MarioSpotted)
    elif world.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.RecruitMallow):
        return inventory.has_item(items.MallowRecruit) or inventory.has_item(items.MallowSpotted)
    elif world.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.RecruitGeno):
        return inventory.has_item(items.GenoRecruit) or inventory.has_item(items.GenoSpotted)
    elif world.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.RecruitBowser):
        return inventory.has_item(items.BowserRecruit) or inventory.has_item(items.BowserSpotted)
    elif world.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.RecruitToadstool):
        return inventory.has_item(items.ToadstoolRecruit) or inventory.has_item(items.ToadstoolSpotted)
    elif world.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.FinishForestMaze):
        return can_access_forest(world, inventory)
    else:
        return True


def can_access_sea(world, inventory):
    if world.settings.is_flag_value(flags.SeaGate, SeaGating.RecruitMario):
        return inventory.has_item(items.MarioRecruit)
    elif world.settings.is_flag_value(flags.SeaGate, SeaGating.RecruitMallow):
        return inventory.has_item(items.MallowRecruit)
    elif world.settings.is_flag_value(flags.SeaGate, SeaGating.RecruitGeno):
        return inventory.has_item(items.GenoRecruit)
    elif world.settings.is_flag_value(flags.SeaGate, SeaGating.RecruitBowser):
        return inventory.has_item(items.BowserRecruit)
    elif world.settings.is_flag_value(flags.SeaGate, SeaGating.RecruitToadstool):
        return inventory.has_item(items.ToadstoolRecruit)
    elif world.settings.is_flag_value(flags.SeaGate, SeaGating.Find1Star):
        return inventory.has_item(items.StarPiece)
    elif world.settings.is_flag_value(flags.SeaGate, SeaGating.Find2Star):
        return inventory.has_item_count(items.StarPiece, 2)
    elif world.settings.is_flag_value(flags.SeaGate, SeaGating.Find3Star):
        return inventory.has_item_count(items.StarPiece, 3)
    elif world.settings.is_flag_value(flags.SeaGate, SeaGating.Find4Star):
        return inventory.has_item_count(items.StarPiece, 4)
    elif world.settings.is_flag_value(flags.SeaGate, SeaGating.Find5Star):
        return inventory.has_item_count(items.StarPiece, 5)
    elif world.settings.is_flag_value(flags.SeaGate, SeaGating.Find6Star):
        return inventory.has_item_count(items.StarPiece, 6)
    else:
        return True


def can_access_yaridovich(world, inventory):
    if world.settings.is_flag_value(flags.YaridovichGate, YaridovichGating.FinishSunkenShip):
        return can_access_sea(world, inventory)
    else:
        return True


def can_access_volcano(world, inventory):
    if world.settings.is_flag_value(flags.BarrelVolcanoGate, BarrelVolcanoGating.FinishNimbusLand):
        return can_clear_nimbus_castle(inventory)
    else:
        return True


def can_access_keep(world, inventory):
    if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.FinishBarrelVolcano):
        return can_access_volcano(world, inventory)
    elif world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.Find1Star):
        return inventory.has_item(items.StarPiece)
    elif world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.Find2Star):
        return inventory.has_item_count(items.StarPiece, 2)
    elif world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.Find3Star):
        return inventory.has_item_count(items.StarPiece, 3)
    elif world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.Find4Star):
        return inventory.has_item_count(items.StarPiece, 4)
    elif world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.Find5Star):
        return inventory.has_item_count(items.StarPiece, 5)
    elif world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.Find6Star):
        return inventory.has_item_count(items.StarPiece, 6)
    else:
        return True


def can_access_factory(world, inventory):
    if world.settings.is_flag_value(flags.FactoryGate, FactoryGating.Find1Star):
        return inventory.has_item(items.StarPiece) and can_access_keep(world, inventory)
    elif world.settings.is_flag_value(flags.FactoryGate, FactoryGating.Find2Star):
        return inventory.has_item_count(items.StarPiece, 2) and can_access_keep(world, inventory)
    elif world.settings.is_flag_value(flags.FactoryGate, FactoryGating.Find3Star):
        return inventory.has_item_count(items.StarPiece, 3) and can_access_keep(world, inventory)
    elif world.settings.is_flag_value(flags.FactoryGate, FactoryGating.Find4Star):
        return inventory.has_item_count(items.StarPiece, 4) and can_access_keep(world, inventory)
    elif world.settings.is_flag_value(flags.FactoryGate, FactoryGating.Find5Star):
        return inventory.has_item_count(items.StarPiece, 5) and can_access_keep(world, inventory)
    elif world.settings.is_flag_value(flags.FactoryGate, FactoryGating.Find6Star):
        return inventory.has_item_count(items.StarPiece, 6) and can_access_keep(world, inventory)
    else:
        return can_access_keep(world, inventory)


def can_access_final_boss(world, inventory):
    value = world.settings.get_flag(flags.StarPiecesRequired).value
    has_stars = inventory.has_item_count(items.StarPiece, value)
    if world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.ShuffleFireworks):
        fireworks_access = inventory.has_item(items.ProgressiveFireworks)
    elif world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.ProgressiveFireworks):
        fireworks_access = inventory.has_item_count(items.ProgressiveFireworks, 3)
    can_access_bucket = fireworks_access and inventory.has_item(items.BambinoBomb) and world.settings.is_flag_value(flags.BucketWarp, False)
    can_access_casino = world.settings.is_flag_value(flags.CasinoWarp, True) and inventory.has_item(items.BrightCard)
    return has_stars and (can_access_bucket or can_access_casino or can_access_factory(world, inventory))


def can_super_jump(world, inventory):
    can_access = False
    for c in world.characters:
        has_super_jump = len(
            [s for s in c.learned_spells if s == spells.SuperJump]) > 0
        if has_super_jump and ((utils.isclass_or_instance(c, Mario) and inventory.has_item(items.MarioRecruit)) or (utils.isclass_or_instance(c, Mallow) and inventory.has_item(items.MallowRecruit)) or (utils.isclass_or_instance(c, Geno) and inventory.has_item(items.GenoRecruit)) or (utils.isclass_or_instance(c, Bowser) and inventory.has_item(items.BowserRecruit)) or (utils.isclass_or_instance(c, Peach) and inventory.has_item(items.ToadstoolRecruit))):
            can_access = True
    return can_access
