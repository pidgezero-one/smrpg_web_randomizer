# E3109_FREESTANDING_BEETLEMANIA_GRANT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(MEM_70A8),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASPlaySound(sound=SO027_FOUND_AN_ITEM, channel=4),
                ASPause(30),
                ASVisibilityOff(),
                ASDb(bytearray(b"\xfd\xf2")),
            ],
        ),
        SetBit(BEETLEMANIA_UNLOCKED),
        RunDialog(
            dialog_id=DI3077_GOT_BEETLEMANIA,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        Return(),
    ]
)
