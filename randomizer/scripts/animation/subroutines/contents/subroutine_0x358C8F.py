# referenced by ally_spells Come Back, ally_spells Shocker, ally_spells Super Jump, ally_spells Psychopath, ally_spells Super Flame, ally_spells Crusher, ally_spells Fire Orb, ally_spells Geno Boost, ally_spells Geno Whirl, ally_spells Poison Gas, ally_spells HP Rain, ally_spells Snowy, ally_spells Thunderbolt, ally_spells Jump, ally_spells Group Hug, ally_spells Psych Bomb, ally_spells Geno Flash, ally_spells Sleepy Time, ally_spells Terrorize, ally_spells Therapy, ally_spells Bowser Crush, ally_spells Ultra Flame, ally_spells Geno Blast, ally_spells Mute, ally_spells Ultra Jump, ally_spells Star Rain, ally_spells Geno Beam

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=1469,
    script=[
        ClearAMEM8Bit(0x6D, identifier="command_0x358c8f"),
        ClearAMEM8Bit(0x6E),
        ClearAMEM8Bit(0x6F),
        ClearAMEM16Bit(0x60),
        Db(bytearray(b"\x89")),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x35924C),
        SetAMEM8BitTo7E5x(0x6D, 0x7E0040),
        JmpIfAMEM8BitEqualsConst(0x6D, 64, ["command_0x358cac"]),
        DrawSpriteAtAMEM32Coords(sprite_id=SPR0581_MARIO_JUMP_ATTACKS, sequence=4),
        PauseScriptUntilAMEMBitsSet(0x6E, [0], identifier="command_0x358cac"),
        AttackTimerBegins(),
        PauseScriptUntilAMEMBitsSet(0x6F, [0]),
        Db(bytearray(b"\x88")),
        JmpIfAMEM8BitEqualsConst(0x6D, 64, ["command_0x358cc0"]),
        RunSubroutine(["240"]),
    ],
)
