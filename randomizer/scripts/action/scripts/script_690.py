"""A0690_OPENING_CHEST"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [SetSpriteSequence(index=4, is_sequence=True, looping=True), Return()]
)
