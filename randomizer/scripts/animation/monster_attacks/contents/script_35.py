# VenomDrool

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	SetOMEM60To072C(),
	DisplayMessageAtOMEM60As(BATTLE_DIALOGUE),
	SetAMEM8BitTo7E1x(0x6F, 0x7EE00F),
	JmpIfAMEM8BitEqualsConst(0x6F, 1, ["command_0x3518c5"]),
	JmpIfAMEM8BitEqualsConst(0x6F, 2, ["command_0x3518c9"]),
	RunSubroutine(["command_0x357b83"]),
	SpriteSequence(sequence=4, identifier="command_0x3518c5"),
	PauseScriptUntilSpriteSequenceDone(),
	ResetSpriteSequence(),
	PlaySound(sound=S0139_GUITAR_STRING, identifier="command_0x3518c9"),
	PlaySound(sound=S0161_SPORE_CHIMES_DOOM_REVERB),
	SetAMEM16BitToConst(0x60, 15),
	RunSubroutine(["command_0x352475"]),
	RunSubroutine(["command_0x3577f2"]),
	RunSubroutine(["command_0x352448"]),
	ReturnSubroutine()
])
