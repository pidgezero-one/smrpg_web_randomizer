# E1568_MIDAS_RIVER_BEGIN_BARREL_SECTION

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeOutMusicToVolume(duration=0, volume=127),
        PlaySound(sound=SO019_LONG_FALL, channel=6),
        ActionQueueAsync(
            target=MARIO, subscript=[ASObjectMemorySetBit(arg_1=0x0B, bits=[3])]
        ),
        RunEventAtReturn(E1571_MIDAS_RIVER_BARREL_SECTION_BUSINESS_LOGIC),
        Return(),
    ]
)
