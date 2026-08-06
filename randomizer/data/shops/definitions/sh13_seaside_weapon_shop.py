from randomizer.data.items.items import (
    ChompShellItem,
    CymbalsItem,
    DoublePunchItem,
    FingerShotItem,
    HandGunItem,
    HurlyGlovesItem,
    LuckyHammerItem,
    NokNokShellItem,
    ParasolItem,
    PunchGloveItem,
    RibbitStickItem,
    SlapGloveItem,
    SuperHammerItem,
    TroopaShellItem,
    WhompGloveItem,
)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH13_SEASIDE_WEAPON_SHOP = Shop(
    index=13,
    items=[
        TroopaShellItem,
        ParasolItem,
        HurlyGlovesItem,
        DoublePunchItem,
        RibbitStickItem,
        NokNokShellItem,
        PunchGloveItem,
        FingerShotItem,
        CymbalsItem,
        ChompShellItem,
        SuperHammerItem,
        HandGunItem,
        WhompGloveItem,
        SlapGloveItem,
        LuckyHammerItem,
    ])


__all__ = ["SH13_SEASIDE_WEAPON_SHOP"]
