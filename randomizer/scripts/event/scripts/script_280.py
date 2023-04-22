# pylint: disable=C0301

"""E0280_SLEEP_IN_NIMBUS_INN"""

from randomizer.scripts.event.script_imports import *

script = EventScript([Jmp(["EVENT_273_fade_out_music_to_volume_17"])])
