"""Packet allocation patch.

Allows low-VRAM packets to use the NPC slot allocation path instead of
requiring the extra sprite buffer.

Vanilla checks ``packet_id < 8`` at SNES ``$C1:9365``. We replace that
with a ``JSR`` to a routine at ``$C1:80C8`` that does a range-check
against an allowlist built from the
:attr:`~randomizer.data.packets.packets.Packet.goes_to_npc_slot_buffer`
class flag.

Source of truth lives on the packet classes in
``randomizer/data/packets/packets.py``: ``ChestPacket`` and
``BoosterHillPacket`` set the flag to ``True``. To change which packets
take the NPC slot path, edit those class flags or override per
instance — don't maintain a parallel ID list here.

ROM sites
---------

* ``$C1:9365`` (6 bytes) — replace::

      A5 1C  LDA $1C
      C9 08  CMP #$08
      B0 16  BCS $9381

  with::

      20 C8 80  JSR $80C8     ; sets carry based on allowlist
      B0 17     BCS $9381     ; not in list → bitmap path ($9547)
      EA        NOP

  ``BCS`` operand = ``$9381 - ($9368 + 2) = $17``.

  Packets with carry clear continue to the NPC slot allocator at
  ``$95DD``; packets with carry set fall through to the bitmap allocator
  at ``$9547``. Our routine lives at ``$C1:80C8`` in repurposed
  debug-string space — same bank, no cross-bank JSL needed.

* ``$C1:80C8`` — inline range-check routine, generated at patch time
  from ``npc_slot_packet_ids``. Consecutive IDs collapse into one
  ``CMP/BCC/CMP/BCC`` range test, isolated IDs become ``CMP/BEQ``. The
  routine touches only A and flags (no PHP/PHX/SEP/REP) — same minimal
  register footprint as the original ``vram_size`` routine, so it can't
  disturb the surrounding packet allocator state.

  An earlier version saved/restored X around a ``SEP #$10`` to allow
  indexing a packet-ID list. That extra register manipulation broke
  downstream allocation for some chest packets in some seeds. Inline
  checks avoid it entirely.

  Routine starts at ``$C1:80C8``; the 39-byte tail
  ``$C1:8140-$C1:8166`` is reserved for the protagonist fade-in
  ``$69``-queue stub, leaving ``($8140 - $80C8) = 120`` bytes
  available.
"""

from typing import Iterable


_HOOK_OFFSET = 0x009365
_HOOK_BYTES = bytes([
    0x20, 0xC8, 0x80,   # JSR $80C8       lookup packet ID, set carry
    0xB0, 0x17,         # BCS $9381       not in list → bitmap path
    0xEA,               # NOP
])

_ROUTINE_OFFSET = 0x0080C8
_ROUTINE_MAX_BYTES = 120


def _build_npc_slot_lookup_routine(packet_ids: Iterable[int]) -> bytes:
    sorted_ids = sorted(packet_ids)
    assert all(0 <= pid <= 0xFE for pid in sorted_ids), (
        "Packet IDs in npc_slot_packet_ids must be in [0, 254] "
        "(255 cannot be in the list — range upper bound would overflow)"
    )

    # Group consecutive IDs into [lo, hi] runs.
    runs: list[tuple[int, int]] = []
    if sorted_ids:
        start = prev = sorted_ids[0]
        for x in sorted_ids[1:]:
            if x == prev + 1:
                prev = x
            else:
                runs.append((start, prev))
                start = prev = x
        runs.append((start, prev))

    # Sizes: singleton = 4 bytes (CMP/BEQ), range = 8 bytes
    # (CMP/BCC/CMP/BCC).
    check_sizes = [4 if lo == hi else 8 for lo, hi in runs]
    prelude_size = 2  # LDA $1C
    # Each tail does SEC/CLC + LDA $1C + RTS = 4 bytes. The trailing
    # LDA $1C exists to normalize N/Z flags on exit so callers see the
    # same flag state vanilla left after `LDA $1C; CMP #$08` (A loaded
    # from $1C, N reflecting bit 7 of packet_id rather than whatever
    # the last range-check CMP set). The OLD vram_size routine ended
    # with LDA $1C for the same reason.
    miss_pos = prelude_size + sum(check_sizes)
    hit_pos = miss_pos + 4  # SEC; LDA $1C; RTS = 4 bytes

    buf = bytearray()
    # Prelude — load packet ID into A. CMPs below all reference $1C
    # too so the preserved A on exit equals packet ID either way.
    buf.append(0xA5)
    buf.append(0x1C)

    # Pre-compute where each check starts so range tests can branch
    # over their own block to the next check.
    check_starts: list[int] = []
    cur = prelude_size
    for sz in check_sizes:
        check_starts.append(cur)
        cur += sz

    def _signed_byte(off: int, what: str) -> int:
        assert -128 <= off <= 127, (
            f"{what} branch offset {off} out of 8-bit range"
        )
        return off & 0xFF

    for i, (lo, hi) in enumerate(runs):
        if lo == hi:
            # CMP #lo / BEQ .hit
            buf.append(0xC9)
            buf.append(lo)
            buf.append(0xF0)
            buf.append(_signed_byte(hit_pos - (len(buf) + 1), "BEQ .hit"))
        else:
            # CMP #lo / BCC .next / CMP #(hi+1) / BCC .hit
            next_pos = check_starts[i] + 8  # byte after this 8-byte block
            buf.append(0xC9)
            buf.append(lo)
            buf.append(0x90)
            buf.append(_signed_byte(next_pos - (len(buf) + 1), "BCC .next"))
            buf.append(0xC9)
            buf.append(hi + 1)
            buf.append(0x90)
            buf.append(_signed_byte(hit_pos - (len(buf) + 1), "BCC .hit"))

    assert len(buf) == miss_pos
    buf.append(0x38)        # SEC          not in list → bitmap path
    buf.append(0xA5)        # LDA $1C      normalize A and N/Z flags
    buf.append(0x1C)
    buf.append(0x60)        # RTS

    assert len(buf) == hit_pos
    buf.append(0x18)        # CLC          in list → NPC slot path
    buf.append(0xA5)        # LDA $1C      normalize A and N/Z flags
    buf.append(0x1C)
    buf.append(0x60)        # RTS

    return bytes(buf)


def get_patch(packet_ids: Iterable[int]) -> dict[int, bytes]:
    """Build the hook + routine bytes from ``packet_ids``.

    ``packet_ids`` is the set of packet IDs that should take the NPC
    slot allocation path.
    """
    routine = _build_npc_slot_lookup_routine(packet_ids)
    if len(routine) > _ROUTINE_MAX_BYTES:
        raise RuntimeError(
            f"npc_slot lookup routine is {len(routine)} bytes; max "
            f"{_ROUTINE_MAX_BYTES} (rest of $C1:80C8-$C1:8166 reserved). "
            f"Reduce npc_slot_packet_ids or split into a separate ROM "
            f"region."
        )
    return {
        _HOOK_OFFSET: _HOOK_BYTES,
        _ROUTINE_OFFSET: routine,
    }
