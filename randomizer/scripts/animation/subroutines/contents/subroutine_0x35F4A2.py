# referenced by weapons DrillClaw, weapons Accessory

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 7, script = [
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=28, identifier="queuestart_0x35f4a2"),
	PlaySound(sound=S0039_CLAW),
	ReturnObjectQueue()
])
