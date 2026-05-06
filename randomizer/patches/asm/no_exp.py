"""Zero out the EXP table.

Used when one of the following is true:

* ``EXPChallenge`` is set to ``NONE`` (no-EXP run).
* ``BossShuffleScaleStats`` is set to ``GODMODE``.
* Debug mode is enabled.

Writes 32 zero bytes at ROM ``$39:BC44`` — the table the battle engine
indexes for per-action EXP rewards.
"""


def get_patch() -> dict[int, bytes]:
    return {0x39BC44: bytes(32)}
