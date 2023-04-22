"""A0808_NIMBUS_EXTERIOR_LAYER_3"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(NORMAL, identifier="ACTION_808_set_animation_speed_0"),
        Walk1StepNortheast(),
        Jmp(["ACTION_808_set_animation_speed_0"]),
    ]
)
