"""SpikedLink miss animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [PlaySound(sound=S0137_BOWSER_CRUSH_STOMP), Jmp(["command_0x358251"])]
)
