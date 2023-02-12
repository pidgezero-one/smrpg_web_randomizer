# BE0026_INTRO_SCENE_TENTACLES_RISE_FROM_HOLES

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a69a6"]),
	RunSubroutine(["command_0x3a7531"]),
	Db(bytearray(b'\xba\x03\x03\x00')),
	NewSpriteAtCoords(sprite_id=SPR1023_EMPTY, sequence=13, priority=1, vram_address=0x8000, palette_row=8, looping=True, param_2_and_0x10=True, overwrite_palette=True),
	SpriteQueue(field_object=0, destinations=["queuestart_0x3ac505"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ac51f"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=2, destinations=["queuestart_0x3ac539"], bit_2=True, bit_4=True),
	RunSubroutine(["command_0x3a771e"]),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=60),
	Jmp(["command_0x3a7550"])
])
