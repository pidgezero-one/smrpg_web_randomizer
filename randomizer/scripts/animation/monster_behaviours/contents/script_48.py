# behaviour_48_0x350F1A

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=42,
    script=[
        ResetTargetMappingMemory(),
        ResetObjectMappingMemory(),
        Db(bytearray(b"T")),
        Db(bytearray(b">")),
        Db(bytearray(b"W")),
        Db(bytearray(b";")),
        Db(bytearray(b"U")),
        Db(bytearray(b";")),
        Db(bytearray(b"V")),
        JmpIfTargetEnabled(["command_0x350f40"]),
        PlaySound(sound=S0089_COMMON_MONSTER_EXPLOSION),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0516_ENEMY_DEFEATED_EXPLOSION_STARS, sequence=0
        ),
        SetAMEM8BitToConst(0x60, 40),
        SetOMEMCurrentToAMEM8Bit(omem=0x2D, amem=0x60),
        Db(bytearray(b"\x1c ")),
        Pause1Frame(),
        Pause1Frame(),
        VisibilityOn(),
        PauseScriptUntilSpriteSequenceDone(),
        VisibilityOff(),
        Db(bytearray(b"\x98")),
        Db(bytearray(b"F"), identifier="command_0x350f40"),
        Jmp(["command_0x350e93"]),
    ],
)
