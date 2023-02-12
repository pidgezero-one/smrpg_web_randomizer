# E1148_FROG_SHOP

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSpriteSequence(
                    index=1, is_sequence=True, looping=True, mirror_sprite=True
                )
            ],
        ),
        JmpIfBitClear(FROG_DISCIPLE_ITEM_1_PURCHASED, ["EVENT_1148_open_shop_19"]),
        JmpIfBitClear(FROG_DISCIPLE_ITEM_2_PURCHASED, ["EVENT_1148_open_shop_19"]),
        JmpIfBitClear(FROG_DISCIPLE_ITEM_3_PURCHASED, ["EVENT_1148_open_shop_19"]),
        JmpIfBitClear(FROG_DISCIPLE_ITEM_4_PURCHASED, ["EVENT_1148_open_shop_19"]),
        JmpIfBitClear(FROG_DISCIPLE_ITEM_5_PURCHASED, ["EVENT_1148_open_shop_19"]),
        RunDialog(
            dialog_id=DI2927_FROG_DISCIPLE_OUT_OF_ITEMS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
        OpenShop(SH03_FROG_DISCIPLE, identifier="EVENT_1148_open_shop_19"),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSpriteSequence(
                    index=0, is_sequence=True, looping=True, mirror_sprite=True
                )
            ],
        ),
        Return(),
    ]
)
