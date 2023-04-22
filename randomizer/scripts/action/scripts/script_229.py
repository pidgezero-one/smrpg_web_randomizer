"""A0229_ENDING_CUTSCENE_EFFECT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [SequencePlaybackOff(), SetWalkingSpeed(VERY_SLOW), Walk1StepNorthwest(), Return()]
)
