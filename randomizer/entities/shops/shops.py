"""Shop definitions."""

from typing import Sequence

from randomizer.types.items import Item
from randomizer.types.overworld_scripts.event_scripts.ids import (
    E0284_OPEN_MUSHROOM_KINGDOM_SHOP,
    E0525_ROSE_TOWN_ITEM_SHOP,
    E0526_ROSE_TOWN_EQUIP_SHOP,
    E0646_MARRYMORE_SHOP_EVENT_CONTAINER,
    E1112_FROG_COIN_EMPORIUM,
    E1140_SEASIDE_OCCUPIED_BOMB_SHOP,
    E1170_SEASIDE_HEALTH_FOOD_SHOP,
    E1171_SEASIDE_ACCESSORY_SHOP,
    E1173_SEASIDE_WEAPON_SHOP,
    E1174_SEASIDE_ARMOR_SHOP,
    E1179_JUICE_BAR_NO_CARD,
    E1180_JUICE_BAR_ALTO_CARD,
    E1181_JUICE_BAR_TENOR_CARD,
    E1182_JUICE_BAR_SOPRANO_CARD,
    E1183_VOLCANO_ITEM_SHOP,
    E1184_VOLCANO_ARMOR_SHOP,
    E1185_TOAD_SHOP,
    E1624_MOLEVILLE_SHOP,
    E1636_MOLEVILLE_SWAP_SHOP_LOGIC,
    E1862_CROCO_SHOP_1,
    E1863_CROCO_SHOP_2,
    E2053_MONSTRO_GOOMBETTE_SHOP,
    E2054_MONSTRO_MAIN_SHOP,
    E3297_SEA_SHOP,
    E3643_NIMBUS_SHOP,
    E3688_MARRYMORE_SERVICE_BELL)
from randomizer.types.shops import (
    EventShop,
    FrogCoinShop,
    FullJuiceBarShop,
    NonFrogCoinShop,
    PartialJuiceBarShop)

from randomizer.entities.items import (
    AbleJuice,
    AntidotePin,
    BadMushroom,
    Bracer,
    BtubRing,
    ChompShell,
    CoinTrick,
    CourageShell,
    Crystalline,
    Cymbals,
    DoublePunch,
    EarlierTimes,
    Elixir,
    Energizer,
    ExpBooster,
    FearlessPin,
    FingerShot,
    FireBomb,
    FireCape,
    FireDress,
    FirePants,
    FireShell,
    FireShirt,
    FreshenUp,
    FrightBomb,
    FroggieDrink,
    FuzzyCape,
    FuzzyDress,
    FuzzyPants,
    FuzzyShirt,
    HandCannon,
    HandGun,
    HappyCape,
    HappyPants,
    HappyShell,
    HappyShirt,
    HealShell,
    HeroShirt,
    HoneySyrup,
    HurlyGloves,
    IceBomb,
    JumpShoes,
    KerokeroCola,
    LuckyHammer,
    MapleSyrup,
    MaxMushroom,
    MegaCape,
    MegaGlove,
    MegaPants,
    MegaShirt,
    Megalixir,
    MidMushroom,
    MukuCookie,
    Mushroom,
    Mushroom2,
    NauticaDress,
    NokNokShell,
    Pants,
    Parasol,
    PickMeUp,
    PowerBlast,
    PrincePants,
    PunchGlove,
    RibbitStick,
    RockCandy,
    RoyalDress,
    SailorCape,
    SailorPants,
    SailorShirt,
    ScroogeRing,
    SeeYa,
    Shirt,
    SlapGlove,
    SleepyBomb,
    SpikedLink,
    StarCape,
    StickyGlove,
    SuperHammer,
    ThickPants,
    ThickShirt,
    TroopaShell,
    TrueformPin,
    WakeUpPin,
    WarFan,
    WhompGlove,
    WorkPants,
    ZoomShoes)


class MushroomKingdomShop(NonFrogCoinShop):
    """Shop definition for MushroomKingdomShop"""

    _shop_id: int = 0
    _original_items: Sequence[type[Item]] = [
        Mushroom,
        HoneySyrup,
        PickMeUp,
        AbleJuice,
        Shirt,
        Pants,
        JumpShoes,
        AntidotePin,
    ]
    _container_event: int = E0284_OPEN_MUSHROOM_KINGDOM_SHOP


class RoseTownItemShop(NonFrogCoinShop):
    """Shop definition for RoseTownItemShop"""

    _shop_id: int = 1
    _original_items: Sequence[type[Item]] = [
        Mushroom,
        HoneySyrup,
        PickMeUp,
        AbleJuice,
    ]
    _container_event: int = E0525_ROSE_TOWN_ITEM_SHOP


class RoseTownArmorShop(NonFrogCoinShop):
    """Shop definition for RoseTownArmorShop"""

    _shop_id: int = 2
    _original_items: Sequence[type[Item]] = [
        ThickShirt,
        ThickPants,
        JumpShoes,
        AntidotePin,
        WakeUpPin,
        TrueformPin,
        FearlessPin,
    ]
    _container_event: int = E0526_ROSE_TOWN_EQUIP_SHOP


class DiscipleShop(FrogCoinShop):
    """Shop definition for DiscipleShop"""

    _shop_id: int = 3
    _original_items: Sequence[type[Item]] = [
        SeeYa,
        EarlierTimes,
        ExpBooster,
        CoinTrick,
        ScroogeRing,
    ]


class MolevilleShop(NonFrogCoinShop):
    """Shop definition for MolevilleShop"""

    _shop_id: int = 4
    _original_items: Sequence[type[Item]] = [
        PunchGlove,
        FingerShot,
        Cymbals,
        MegaShirt,
        MegaPants,
        MegaCape,
        WorkPants,
        MidMushroom,
        MapleSyrup,
    ]
    _container_event: int = E1624_MOLEVILLE_SHOP


class MarrymoreShop(NonFrogCoinShop):
    """Shop definition for MarrymoreShop"""

    _shop_id: int = 5
    _original_items: Sequence[type[Item]] = [
        SuperHammer,
        HandGun,
        WhompGlove,
        ChompShell,
        HappyShirt,
        HappyPants,
        HappyCape,
        HappyShell,
        BtubRing,
        MidMushroom,
        MapleSyrup,
    ]
    _container_event: int = E0646_MARRYMORE_SHOP_EVENT_CONTAINER


class FrogCoinEmporiumShop(FrogCoinShop):
    """Shop definition for FrogCoinEmporiumShop"""

    _shop_id: int = 6
    _original_items: Sequence[type[Item]] = [
        SleepyBomb,
        Bracer,
        Energizer,
        Crystalline,
        PowerBlast,
    ]
    _container_event: int = E1112_FROG_COIN_EMPORIUM


class SeaShop(NonFrogCoinShop):
    """Shop definition for SeaShop"""

    _shop_id: int = 7
    _original_items: Sequence[type[Item]] = [
        HurlyGloves,
        SuperHammer,
        HandGun,
        WhompGlove,
        SailorShirt,
        SailorPants,
        SailorCape,
        NauticaDress,
        MidMushroom,
        MapleSyrup,
        PickMeUp,
        AbleJuice,
        FreshenUp,
    ]
    _container_event: int = E3297_SEA_SHOP


class SeasideYaridShop(NonFrogCoinShop):
    """Shop definition for SeasideYaridShop"""

    _shop_id: int = 8
    _original_items: Sequence[type[Item]] = [
        BadMushroom,
        MukuCookie,
        FrightBomb,
        FireBomb,
        IceBomb,
    ]
    _container_event: int = E1140_SEASIDE_OCCUPIED_BOMB_SHOP


class JuiceBarPartial1(PartialJuiceBarShop):
    """Shop definition for JuiceBarPartial1"""

    _shop_id: int = 9
    _original_items: Sequence[type[Item]] = [FroggieDrink]
    _container_event: int = E1179_JUICE_BAR_NO_CARD


class JuiceBarPartial2(PartialJuiceBarShop):
    """Shop definition for JuiceBarPartial2"""

    _shop_id: int = 10
    _original_items: Sequence[type[Item]] = [FroggieDrink, Elixir]
    _container_event: int = E1180_JUICE_BAR_ALTO_CARD


class JuiceBarPartial3(PartialJuiceBarShop):
    """Shop definition for JuiceBarPartial3"""

    _shop_id: int = 11
    _original_items: Sequence[type[Item]] = [FroggieDrink, Elixir, Megalixir]
    _container_event: int = E1181_JUICE_BAR_TENOR_CARD


class JuiceBarFull(FullJuiceBarShop):
    """Shop definition for JuiceBarFull"""

    _shop_id: int = 12
    _original_items: Sequence[type[Item]] = [
        FroggieDrink,
        Elixir,
        Megalixir,
        KerokeroCola,
    ]
    _container_event: int = E1182_JUICE_BAR_SOPRANO_CARD


class SeasideWeaponShop(NonFrogCoinShop):
    """Shop definition for SeasideWeaponShop"""

    _shop_id: int = 13
    _original_items: Sequence[type[Item]] = [
        TroopaShell,
        Parasol,
        HurlyGloves,
        DoublePunch,
        RibbitStick,
        NokNokShell,
        PunchGlove,
        FingerShot,
        Cymbals,
        ChompShell,
        SuperHammer,
        HandGun,
        WhompGlove,
        SlapGlove,
        LuckyHammer,
    ]
    _container_event: int = E1173_SEASIDE_WEAPON_SHOP


class SeasideArmorShop(NonFrogCoinShop):
    """Shop definition for SeasideArmorShop"""

    _shop_id: int = 14
    _original_items: Sequence[type[Item]] = [
        SailorShirt,
        SailorPants,
        SailorCape,
        NauticaDress,
        Shirt,
        Pants,
        ThickShirt,
        ThickPants,
        MegaShirt,
        MegaPants,
        MegaCape,
        HappyShirt,
        HappyPants,
        HappyCape,
        HappyShell,
    ]
    _container_event: int = E1174_SEASIDE_ARMOR_SHOP


class SeasideAccessoryShop(NonFrogCoinShop):
    """Shop definition for SeasideAccessoryShop"""

    _shop_id: int = 15
    _original_items: Sequence[type[Item]] = [
        JumpShoes,
        AntidotePin,
        WakeUpPin,
        FearlessPin,
        TrueformPin,
        ZoomShoes,
    ]
    _container_event: int = E1171_SEASIDE_ACCESSORY_SHOP


class SeasideItemShop(NonFrogCoinShop):
    """Shop definition for SeasideItemShop"""

    _shop_id: int = 16
    _original_items: Sequence[type[Item]] = [
        Mushroom,
        MidMushroom,
        HoneySyrup,
        MapleSyrup,
        PickMeUp,
        AbleJuice,
        FreshenUp,
    ]
    _container_event: int = E1170_SEASIDE_HEALTH_FOOD_SHOP


class MonstroTownShop(NonFrogCoinShop):
    """Shop definition for MonstroTownShop"""

    _shop_id: int = 17
    _original_items: Sequence[type[Item]] = [
        SpikedLink,
        CourageShell,
        MidMushroom,
        MapleSyrup,
        PickMeUp,
        AbleJuice,
        FreshenUp,
    ]
    _container_event: int = E2054_MONSTRO_MAIN_SHOP


class HinopioItemShop(NonFrogCoinShop):
    """Shop definition for HinopioItemShop"""

    _shop_id: int = 18
    _original_items: Sequence[type[Item]] = [
        MidMushroom,
        MapleSyrup,
        PickMeUp,
        AbleJuice,
        FreshenUp,
    ]
    _container_event: int = E1183_VOLCANO_ITEM_SHOP


class HinopioArmorShop(NonFrogCoinShop):
    """Shop definition for HinopioArmorShop"""

    _shop_id: int = 19
    _original_items: Sequence[type[Item]] = [
        FireShirt,
        FirePants,
        FireCape,
        FireShell,
        FireDress,
    ]
    _container_event: int = E1184_VOLCANO_ARMOR_SHOP


class BabyGoombaShop(NonFrogCoinShop):
    """Shop definition for BabyGoombaShop"""

    _shop_id: int = 20
    _original_items: Sequence[type[Item]] = [Mushroom2]
    _container_event: int = E2053_MONSTRO_GOOMBETTE_SHOP


class NimbusShop(NonFrogCoinShop):
    """Shop definition for NimbusShop"""

    _shop_id: int = 21
    _original_items: Sequence[type[Item]] = [
        MidMushroom,
        MapleSyrup,
        PickMeUp,
        AbleJuice,
        FreshenUp,
        MegaGlove,
        WarFan,
        HandCannon,
        StickyGlove,
        FuzzyShirt,
        FuzzyPants,
        FuzzyCape,
        FuzzyDress,
    ]
    _container_event: int = E3643_NIMBUS_SHOP


class CrocoShop1(NonFrogCoinShop):
    """Shop definition for CrocoShop1"""

    _shop_id: int = 22
    _original_items: Sequence[type[Item]] = [
        MidMushroom,
        MapleSyrup,
        PickMeUp,
        FreshenUp,
        FireShirt,
        FirePants,
        FireCape,
        FireShell,
        FireDress,
    ]
    _container_event: int = E1862_CROCO_SHOP_1


class CrocoShop2(NonFrogCoinShop):
    """Shop definition for CrocoShop2"""

    _shop_id: int = 23
    _original_items: Sequence[type[Item]] = [
        MidMushroom,
        MapleSyrup,
        PickMeUp,
        FreshenUp,
        HeroShirt,
        PrincePants,
        StarCape,
        HealShell,
        RoyalDress,
    ]
    _container_event: int = E1863_CROCO_SHOP_2


class ToadShop(NonFrogCoinShop):
    """Shop definition for ToadShop"""

    _shop_id: int = 24
    _original_items: Sequence[type[Item]] = [
        MidMushroom,
        MaxMushroom,
        MapleSyrup,
        PickMeUp,
        AbleJuice,
        FreshenUp,
        FroggieDrink,
    ]
    _container_event: int = E1185_TOAD_SHOP


class RoomServiceShop(EventShop):
    """Shop definition for RoomServiceShop"""

    _original_items: Sequence[type[Item]] = [PickMeUp, KerokeroCola]
    _container_event: int = E3688_MARRYMORE_SERVICE_BELL


class MolevilleSwapShop(EventShop):
    """Shop definition for MolevilleSwapShop"""

    _original_items: Sequence[type[Item]] = [FrightBomb, FireBomb, IceBomb]
    _container_event: int = E1636_MOLEVILLE_SWAP_SHOP_LOGIC

    def can_accept(self, item: Item):
        allowed = [BadMushroom, SleepyBomb, FrightBomb, FireBomb, IceBomb, RockCandy]
        for cls in allowed:
            if isinstance(item, cls):
                return True
        return False
