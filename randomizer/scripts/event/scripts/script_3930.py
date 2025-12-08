# pylint: disable=C0301

"""E3930_MARRYMORE_GEAR_PRELOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_0, subscript=[ASTransferToXYZF(x=16, y=84, z=0, direction=EAST)]
        ),
        ActionQueueSync(
            target=NPC_1, subscript=[ASTransferToXYZF(x=19, y=78, z=0, direction=EAST)]
        ),
        ActionQueueSync(
            target=NPC_2, subscript=[ASTransferToXYZF(x=13, y=90, z=0, direction=EAST)]
        ),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASTransferToXYZF(x=22, y=72, z=2, direction=EAST),
                ASFaceNortheast(),
                ASSetSpriteSequence(
                    index=14, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ]),
        ActionQueueSync(
            target=NPC_7,
            subscript=[
                ASTransferToXYZF(x=22, y=73, z=2, direction=EAST),
                ASWalkSoutheastPixels(5),
                ASFaceNortheast(),
            ]),
        JmpIfObjectInSpecificLevel(
            NPC_5, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER, ["EVENT_3930_phold"]
        ),
        Jmp(["EVENT_3930_pause_368"]),
        Pause(1, identifier="EVENT_3930_phold"),
        ActionQueueAsync(
            target=NPC_5,
            subscript=[
                ASTransferToObjectXYZ(NPC_7),
                ASShiftZUpSteps(2),
                ASSetSolidityBits(
                    cant_jump_through=True, bit_4=True, cant_walk_through=True
                ),
            ]),
        Pause(30, identifier="EVENT_3930_pause_368"),
        Jmp(["EVENT_3809_set_action_script_sync_384"]),
    ]
)
