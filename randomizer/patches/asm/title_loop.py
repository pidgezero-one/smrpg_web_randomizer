"""Title screen loops forever — no attract-mode demo (open-mode base).

``$C9:E6FE``: ``DEY`` -> ``NOP``. Removes the attract-mode/demo countdown
decrement so the title screen never times out to the demo. Render-disjoint
engine code relocated from open_mode.json (verified byte-identical via
``diff_open_mode``).
"""


def get_patch() -> dict[int, bytes]:
    return {
        0x09E6FE: bytes([0xEA]),
    }
