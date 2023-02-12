# E0682_MARRYMORE_LIBERATED_EXTERIOR_MOM

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_6,
            subscript=[
                ASSet700CToObjectCoord(object=NPC_6, coord=COORD_F, pixel=True),
                ASFaceSouthwest(),
            ],
        ),
        SetBit(TEMP_7043_1),
        RunDialog(
            dialog_id=DI2197_MARRYMORE_PHOTO,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        ActionQueueAsync(target=NPC_6, subscript=[ASFaceEast7C()]),
        ClearBit(TEMP_7043_1),
        Return(),
    ]
)
