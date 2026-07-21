"""Play the "Victory Against Culex" fanfare behind the Monstro Town door(s).

The battle-end music selector at ``$C2:4C8D`` picks the victory jingle by
comparing the current formation ID against Culex's *vanilla* formation::

    C2/4C8D  AF 0E FA 7E  LDA $7EFA0E   ; current formation id
    C2/4C91  C9 5E 01     CMP #$015E    ; 350 = Culex in vanilla
    C2/4C94  D0 05        BNE +
    C2/4C96  A9 3C 00     LDA #$003C    ; song $3C "Victory Against Culex"
    C2/4C99  80 03        BRA ++
    C2/4C9B  A9 09 00     LDA #$0009    ; song $09 "Victory"
    C2/4C9E  85 E0        STA $E0       ; -> JSR $9EA5 (play song)

We renumber every formation, so ID 350 lands on an unrelated fight and the
real Culex never plays it. The 17-byte vanilla block (``$4C8D-$4C9D``) is a
single hardcoded compare with no room to add a second, so a one-value operand
patch cannot cover both Monstro Town doors (the story boss *and* the postgame
Culex 3D rematch).

Instead, redirect the block to a tiny helper in the ``$FF`` padding right after
the play-song routine (``$C2:9FCA``, 54 free bytes). The helper compares the
formation ID against each door's formation and returns song ``$3C`` on a match,
``$09`` otherwise -- so the fanfare follows whichever bosses boss-shuffle drops
behind the doors, and it trivially extends to any number of formations.

Both sites are battle-engine code in bank ``$C2`` running on SA-1, so the hook
uses a same-bank ``JSR``/``RTS`` (no cross-bank ``JSL`` that SA-1 can't reach).
The accumulator is 16-bit here (``BIT #$4000`` / ``LDA #$0007`` immediately
above), matching the helper's 16-bit ``LDA``/``CMP``/immediate loads.
"""

from typing import Sequence

# ROM offset of the `LDA $7EFA0E` block ($C2:4C8D). We overwrite 17 bytes
# ($4C8D-$4C9D) and leave `STA $E0` at $4C9E untouched.
HOOK_ADDR = 0x024C8D
HOOK_LEN = 17

# ROM offset / SNES address of the helper, in bank $C2's trailing $FF padding.
HELPER_ADDR = 0x029FCA
HELPER_SNES = HELPER_ADDR & 0xFFFF  # $9FCA
HELPER_MAX_LEN = 54  # $9FCA-$9FFF, before the $A000 jump table

CULEX_VICTORY_SONG = 0x3C  # "Victory Against Culex"
NORMAL_VICTORY_SONG = 0x09  # "Victory"


def _helper_bytes(formation_ids: Sequence[int]) -> bytes:
    """Assemble the compare-and-return helper.

    Layout (song id returned in A)::

        LDA $7EFA0E                 ; AF 0E FA 7E
        <for each id:> CMP #id      ; C9 lo hi
                       BEQ hit       ; F0 rr
        LDA #NORMAL_VICTORY_SONG    ; A9 09 00   (miss)
        RTS                         ; 60
        hit: LDA #CULEX_VICTORY_SONG; A9 3C 00
             RTS                     ; 60
    """
    n = len(formation_ids)
    out = bytearray([0xAF, 0x0E, 0xFA, 0x7E])  # LDA $7EFA0E
    for k, formation_id in enumerate(formation_ids):
        out += bytes([0xC9, formation_id & 0xFF, (formation_id >> 8) & 0xFF])
        # Every BEQ targets the single `hit` label past the miss path. Each
        # remaining (CMP+BEQ) pair is 5 bytes and the miss path is 4 bytes, so
        # from the byte after this BEQ the distance to `hit` is 5*(n-k) - 1.
        branch = 5 * (n - k) - 1
        assert 0 < branch < 128, f"BEQ offset {branch} out of range"
        out += bytes([0xF0, branch])
    out += bytes([0xA9, NORMAL_VICTORY_SONG, 0x00, 0x60])  # miss: LDA #$0009 / RTS
    out += bytes([0xA9, CULEX_VICTORY_SONG, 0x00, 0x60])   # hit:  LDA #$003C / RTS
    assert len(out) == 12 + 5 * n
    return bytes(out)


def get_patch(formation_ids: Sequence[int]) -> dict[int, bytes]:
    """Hook + helper that play the Culex fanfare for the given formations.

    Args:
        formation_ids: Formation IDs that should trigger the Culex victory
            fanfare (typically the formations behind the Monstro Town doors).
    """
    # Preserve order, drop duplicates (both doors could resolve to one boss).
    unique_ids: list[int] = list(dict.fromkeys(formation_ids))
    assert unique_ids, "at least one formation id is required"
    for formation_id in unique_ids:
        assert 0 <= formation_id <= 0x1FF, f"formation id out of range: {formation_id}"

    helper = _helper_bytes(unique_ids)
    assert len(helper) <= HELPER_MAX_LEN, (
        f"helper is {len(helper)} bytes, only {HELPER_MAX_LEN} free at "
        f"{HELPER_ADDR:#08x}"
    )

    # JSR $9FCA then NOP-fill the rest of the vanilla block; `STA $E0` at $4C9E
    # then stores the song id the helper left in A.
    hook = bytes([0x20, HELPER_SNES & 0xFF, (HELPER_SNES >> 8) & 0xFF])
    hook += b"\xEA" * (HOOK_LEN - len(hook))
    assert len(hook) == HOOK_LEN

    return {HOOK_ADDR: hook, HELPER_ADDR: helper}
