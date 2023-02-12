# E0685_MARRYMORE_LIBERATED_EXTERIOR_WIFE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASSet700CToObjectCoord(object=NPC_3, coord=COORD_F, pixel=True),
                ASFaceSouthwest(),
            ],
        ),
        RunDialog(
            dialog_id=DI2194_MARRYMORE_PHOTO,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        ActionQueueAsync(target=NPC_3, subscript=[ASFaceEast7C()]),
        Return(),
    ]
)
