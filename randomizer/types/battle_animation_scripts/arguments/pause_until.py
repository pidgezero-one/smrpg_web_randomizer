"""Int subclass instances representing the behaviour of a script pause."""

from .types import PauseUntil

SPRITE_SHIFT_COMPLETE = PauseUntil(6)
BUTTON_PRESSED = PauseUntil(8)
FRAMES_ELAPSED = PauseUntil(0x10)
SEQ_4BPP_COMPLETE = bytearray([0x04, 0x00])
SEQ_2BPP_COMPLETE = bytearray([0x08, 0x00])
FADE_IN_COMPLETE = bytearray([0x00, 0x02])
FADE_4BPP_COMPLETE = bytearray([0x00, 0x04])
FADE_2BPP_COMPLETE = bytearray([0x00, 0x08])
