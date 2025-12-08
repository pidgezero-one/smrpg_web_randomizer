"""A0177_FOREST_ARROW"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        VisibilityOff(),
        SetPriority(3),
        SetVarToRandom(
            PRIMARY_TEMP_700C, 255, identifier="ACTION_177_set_var_to_random_2"
        ),
        LoadMemory(PRIMARY_TEMP_700C),
        Pause(1),
        EndLoop(),
        JmpIfRandom2of3(
            ["ACTION_177_transfer_to_xyzf_19", "ACTION_177_transfer_to_xyzf_31"]
        ),
        TransferToXYZF(x=12, y=92, z=17, direction=EAST),
        VisibilityOn(),
        OverwriteSolidity(bit_4=True, cant_walk_through=True),
        Db(bytearray(b" \x07")),
        Db(bytearray(b"$\x80\xfb\x00\x02")),
        Db(bytearray(b"%\x00\x00`\xff")),
        Pause(16),
        Db(bytearray(b"$\xe0\xff\x00\x01")),
        Pause(9),
        BPL262728(),
        OverwriteSolidity(),
        Jmp(["ACTION_177_play_sound_42"]),
        TransferToXYZF(
            x=4, y=98, z=17, direction=EAST, identifier="ACTION_177_transfer_to_xyzf_19"
        ),
        VisibilityOn(),
        OverwriteSolidity(bit_4=True, cant_walk_through=True),
        Db(bytearray(b" \x07")),
        Db(bytearray(b"$\x80\x04P\x02")),
        Db(bytearray(b"%\x00\x00`\xff")),
        Pause(16),
        Db(bytearray(b"$ \x00\x00\x01")),
        Pause(9),
        BPL262728(),
        OverwriteSolidity(),
        Jmp(["ACTION_177_play_sound_42"]),
        TransferToXYZF(
            x=9,
            y=121,
            z=0,
            direction=SOUTH,
            identifier="ACTION_177_transfer_to_xyzf_31"),
        VisibilityOn(),
        OverwriteSolidity(bit_4=True, cant_walk_through=True),
        Db(bytearray(b" \x07")),
        Db(bytearray(b"$\x80\xfeP\xfe")),
        Db(bytearray(b"%\x00\x00`\xff")),
        Pause(38),
        Db(bytearray(b"$\xe0\xff\x00\xff")),
        Pause(9),
        BPL262728(),
        OverwriteSolidity(),
        PlaySound(
            sound=SO033_JUMPING_BOUNCING_FISH,
            channel=6,
            identifier="ACTION_177_play_sound_42"),
        SetSpriteSequence(index=0, looping=False),
        Pause(80),
        StartLoopNTimes(3),
        VisibilityOff(),
        Pause(3),
        VisibilityOn(),
        Pause(3),
        EndLoop(),
        VisibilityOff(),
        ShiftToXYCoords(x=14, y=122),
        Jmp(["ACTION_177_set_var_to_random_2"]),
    ]
)
