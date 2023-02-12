from typing import Sequence, Type
from randomizer.types.items.classes import Item
from randomizer.types.overworld_scripts.event_scripts.constants.script_ids import (
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
    E3688_MARRYMORE_SERVICE_BELL,
)
from randomizer.types.shops.classes import (
    EventShop,
    FrogCoinShop,
    FullJuiceBarShop,
    NormalShop,
    PartialJuiceBarShop,
)
from randomizer.entities.items.items import (
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
    ZoomShoes,
)


class MushroomKingdomShop(NormalShop):
    _shop_id: int = 0
    _original_items: Sequence[Type[Item]] = [
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


class RoseTownItemShop(NormalShop):
    _shop_id: int = 1
    _original_items: Sequence[Type[Item]] = [
        Mushroom,
        HoneySyrup,
        PickMeUp,
        AbleJuice,
    ]
    _container_event: int = E0525_ROSE_TOWN_ITEM_SHOP


class RoseTownArmorShop(NormalShop):
    _shop_id: int = 2
    _original_items: Sequence[Type[Item]] = [
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
    _shop_id: int = 3
    _original_items: Sequence[Type[Item]] = [
        SeeYa,
        EarlierTimes,
        ExpBooster,
        CoinTrick,
        ScroogeRing,
    ]


class MolevilleShop(NormalShop):
    _shop_id: int = 4
    _original_items: Sequence[Type[Item]] = [
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


class MarrymoreShop(NormalShop):
    _shop_id: int = 5
    _original_items: Sequence[Type[Item]] = [
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
    _shop_id: int = 6
    _original_items: Sequence[Type[Item]] = [
        SleepyBomb,
        Bracer,
        Energizer,
        Crystalline,
        PowerBlast,
    ]
    _container_event: int = E1112_FROG_COIN_EMPORIUM


class SeaShop(NormalShop):
    _shop_id: int = 7
    _original_items: Sequence[Type[Item]] = [
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


class SeasideYaridShop(NormalShop):
    _shop_id: int = 8
    _original_items: Sequence[Type[Item]] = [
        BadMushroom,
        MukuCookie,
        FrightBomb,
        FireBomb,
        IceBomb,
    ]
    _container_event: int = E1140_SEASIDE_OCCUPIED_BOMB_SHOP


class JuiceBarPartial1(PartialJuiceBarShop):
    _shop_id: int = 9
    _original_items: Sequence[Type[Item]] = [FroggieDrink]
    _container_event: int = E1179_JUICE_BAR_NO_CARD


class JuiceBarPartial2(PartialJuiceBarShop):
    _shop_id: int = 10
    _original_items: Sequence[Type[Item]] = [FroggieDrink, Elixir]
    _container_event: int = E1180_JUICE_BAR_ALTO_CARD


class JuiceBarPartial3(PartialJuiceBarShop):
    _shop_id: int = 11
    _original_items: Sequence[Type[Item]] = [FroggieDrink, Elixir, Megalixir]
    _container_event: int = E1181_JUICE_BAR_TENOR_CARD


class JuiceBarFull(FullJuiceBarShop):
    _shop_id: int = 12
    _original_items: Sequence[Type[Item]] = [
        FroggieDrink,
        Elixir,
        Megalixir,
        KerokeroCola,
    ]
    _container_event: int = E1182_JUICE_BAR_SOPRANO_CARD


class SeasideWeaponShop(NormalShop):
    _shop_id: int = 13
    _original_items: Sequence[Type[Item]] = [
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


class SeasideArmorShop(NormalShop):
    _shop_id: int = 14
    _original_items: Sequence[Type[Item]] = [
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


class SeasideAccessoryShop(NormalShop):
    _shop_id: int = 15
    _original_items: Sequence[Type[Item]] = [
        JumpShoes,
        AntidotePin,
        WakeUpPin,
        FearlessPin,
        TrueformPin,
        ZoomShoes,
    ]
    _container_event: int = E1171_SEASIDE_ACCESSORY_SHOP


class SeasideItemShop(NormalShop):
    _shop_id: int = 16
    _original_items: Sequence[Type[Item]] = [
        Mushroom,
        MidMushroom,
        HoneySyrup,
        MapleSyrup,
        PickMeUp,
        AbleJuice,
        FreshenUp,
    ]
    _container_event: int = E1170_SEASIDE_HEALTH_FOOD_SHOP


class MonstroTownShop(NormalShop):
    _shop_id: int = 17
    _original_items: Sequence[Type[Item]] = [
        SpikedLink,
        CourageShell,
        MidMushroom,
        MapleSyrup,
        PickMeUp,
        AbleJuice,
        FreshenUp,
    ]
    _container_event: int = E2054_MONSTRO_MAIN_SHOP


class HinopioItemShop(NormalShop):
    _shop_id: int = 18
    _original_items: Sequence[Type[Item]] = [
        MidMushroom,
        MapleSyrup,
        PickMeUp,
        AbleJuice,
        FreshenUp,
    ]
    _container_event: int = E1183_VOLCANO_ITEM_SHOP


class HinopioArmorShop(NormalShop):
    _shop_id: int = 19
    _original_items: Sequence[Type[Item]] = [
        FireShirt,
        FirePants,
        FireCape,
        FireShell,
        FireDress,
    ]
    _container_event: int = E1184_VOLCANO_ARMOR_SHOP


class BabyGoombaShop(NormalShop):
    _shop_id: int = 20
    _original_items: Sequence[Type[Item]] = [Mushroom2]
    _container_event: int = E2053_MONSTRO_GOOMBETTE_SHOP


class NimbusShop(NormalShop):
    _shop_id: int = 21
    _original_items: Sequence[Type[Item]] = [
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


class CrocoShop1(NormalShop):
    _shop_id: int = 22
    _original_items: Sequence[Type[Item]] = [
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


class CrocoShop2(NormalShop):
    _shop_id: int = 23
    _original_items: Sequence[Type[Item]] = [
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


class ToadShop(NormalShop):
    _shop_id: int = 24
    _original_items: Sequence[Type[Item]] = [
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
    _original_items: Sequence[Type[Item]] = [PickMeUp, KerokeroCola]
    _container_event: int = E3688_MARRYMORE_SERVICE_BELL


class MolevilleSwapShop(EventShop):
    _original_items: Sequence[Type[Item]] = [FrightBomb, FireBomb, IceBomb]
    _container_event: int = E1636_MOLEVILLE_SWAP_SHOP_LOGIC

    def can_accept(self, item: Item):
        allowed = [BadMushroom, SleepyBomb, FrightBomb, FireBomb, IceBomb, RockCandy]
        for cls in allowed:
            if isinstance(item, cls):
                return True
        return False
