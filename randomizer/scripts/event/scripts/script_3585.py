# pylint: disable=C0301

"""E3585_NIMBUS_FADE_IN_ASYNC"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeInFromBlack(sync=False, identifier="EVENT_3585_fade_in_from_black_async_0"),
        Return(),
    ]
)
