# pylint: disable=C0301

"""E3686_MARRYMORE_SHOWER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7044_6, ["EVENT_3584_ret_0"]),
        SetBit(TEMP_7044_6),
        ActionQueueAsync(
            target=MARIO, subscript=[ASFaceSouthwest(), ASVisibilityOff()]
        ),
        Pause(30),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        ApplyTileModToLevel(
            use_alternate=False, room_id=R012_MARRYMORE_INN_SUITE_ROOM, mod_id=1
        ),
        Pause(60),
        PlaySound(sound=SO155_POSTCREDITS_MARIO_THEME_WHISTLE, channel=6),
        Pause(120),
        PlaySound(sound=SO006_RUNNING_WATER, channel=4),
        Pause(480),
        StartLoopNTimes(2),
        PlaySound(sound=SO018_SUDDEN_STOP, channel=6),
        Pause(8),
        StopSound(),
        Pause(20),
        EndLoop(),
        Pause(120),
        PaletteSet(palette_set=142, row=1),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASTransferToXYZF(x=10, y=13, z=0, direction=EAST),
                ASTransferXYZFPixels(x=252, y=4, z=0, direction=EAST),
                ASVisibilityOn(),
                ASPause(30),
                ASClearSolidityBits(cant_pass_walls=True),
            ]),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R012_MARRYMORE_INN_SUITE_ROOM, mod_id=1
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASWalkSouthwestSteps(2),
                ASPause(60),
                ASFaceWest(),
                ASPause(2),
                ASFaceNorthwest(),
                ASPause(2),
                ASFaceNorth(),
                ASPause(2),
                ASFaceNortheast(),
            ]),
        Pause(30),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        ApplyTileModToLevel(
            use_alternate=False, room_id=R012_MARRYMORE_INN_SUITE_ROOM, mod_id=1
        ),
        Pause(30),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceEast(),
                ASPause(2),
                ASFaceSoutheast(),
                ASPause(2),
                ASFaceSouth(),
            ]),
        SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        ClearBit(TEMP_7044_7),
        ClearBit(TEMP_7044_6),
        Return(),
    ]
)
