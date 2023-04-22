# pylint: disable=C0301

"""E0257_FADE_IN_ASYNC"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeInFromBlack(sync=False, identifier="EVENT_257_fade_in_from_black_async_0"),
        Return(),
    ]
)
