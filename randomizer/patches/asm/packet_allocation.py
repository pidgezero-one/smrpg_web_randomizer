"""Packet allocation patch.

Allows low-VRAM packets to use the NPC slot allocation path instead of
requiring the extra sprite buffer.

Vanilla checks ``packet_id < 8`` at SNES ``$C0:9365``. We replace that
with a ``JSR`` to a routine at ``$C0:80C8`` that does a range-check
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

* ``$C0:9365`` (6 bytes) — replace::

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
  at ``$9547``. Our routine lives at ``$C0:80C8`` in repurposed
  debug-string space — same bank, no cross-bank JSL needed.

* ``$C0:80C8`` — inline range-check routine, generated at patch time
  from ``npc_slot_packet_ids``. Consecutive IDs collapse into one
  ``CMP/BCC/CMP/BCC`` range test, isolated IDs become ``CMP/BEQ``. The
  routine touches only A and flags (no PHP/PHX/SEP/REP) — same minimal
  register footprint as the original ``vram_size`` routine, so it can't
  disturb the surrounding packet allocator state.

  An earlier version saved/restored X around a ``SEP #$10`` to allow
  indexing a packet-ID list. That extra register manipulation broke
  downstream allocation for some chest packets in some seeds. Inline
  checks avoid it entirely.

  Routine starts at ``$C0:80C8``; the 39-byte tail
  ``$C0:8140-$C0:8166`` is reserved for the protagonist fade-in
  ``$69``-queue stub, leaving ``($8140 - $80C8) = 120`` bytes
  available.

* ``$C0:9137`` (7 bytes) + helper — make the treasure-chest partition
  buffer reserve VRAM *per room* via its own ``main_buffer_space``,
  instead of the vanilla fixed ``+4``.

  The chest-packet slot allocator at ``$C0:95DD`` stages up to 4 packets
  at ``[$01A4] + 2*index`` above clone buffer A's base. The chest buffer
  handler at ``$C0:9122`` reserves that space with a hardcoded ``+4`` and,
  unlike the FOUR/THREE handler at ``$C0:90FC``, never derives
  ``main_buffer_space`` — the shared value ``$81`` is computed only at
  ``$C0:90F6`` inside the FOUR/THREE path, which the chest path bypasses.
  So ``+4`` clears only ~2 slots (2 or 4 by cursor-packing alignment).
  Vanilla was safe: only IDs 0-7 took this path and were same-sprite
  (dedup to 1 slot). Widening the NPC-slot path to every ``ChestPacket``
  (~80 IDs) lets 2+ distinct-sprite chest packets coexist, so slots spill
  past buffer A into the next buffer's NPC tiles (R234 NPC 0 trampoline,
  R125 NPC 5 frog coin).

  A global bump is unworkable: near-capacity chest rooms (R234, R242)
  overflow VRAM if every chest room pays extra. Instead we replace the
  7-byte advance (``A5 6D 18 69 04 85 6D`` = ``LDA $6D; CLC; ADC #$04;
  STA $6D``) with a ``JSR`` to a helper that recomputes the reservation
  as ``4 + main_buffer_space*4`` (reading the type byte still live in
  ``$80``)::

      LDA $80 / AND #$70 / LSR / LSR   ; A = main_buffer_space * 4
      CLC / ADC #$04                   ; + vanilla +4 floor
      ADC $6D / STA $6D                ; cursor += 4 + space*4
      RTS

  Result: buffer A ``main_buffer_space=0`` → ``+4`` (byte-for-byte vanilla,
  so all unbumped chest rooms are unchanged); ``=1`` → ``+8`` (16 packed
  units, alignment-independent — holds all 4 slots). Bump only the few
  rooms where 2+ distinct-sprite chest packets coexist (R125; R234 with
  its ``extra_sprite_buffer_size`` trimmed to stay within VRAM). No packet
  exceeds sprite-195 mold 0, so 4 slots is the ceiling.

  The helper is emitted right after the allowlist routine in the same
  free region; its address is computed at patch time.

* ``$C0:97B9`` (6 bytes) + helper — **the root-cause fix for chest packets
  overwriting NPCs.** The per-despawn slot free at ``$C0:97D5``
  (``AND $01A5 / STA $01A5``) is gated at ``$C0:97BB`` by ``CMP #$C3`` —
  it only frees packets whose sprite is 195 (FLOWER). Vanilla was fine:
  every id-0-7 NPC-slot packet was flower/mushroom (sprite 195). But this
  module widens the NPC-slot path to every ``ChestPacket`` (~50 distinct
  sprites), and the free path still recognizes only flower, so **49/50
  sprites never clear their $01A5 bit** — slots leak for the whole room
  visit (reset only on partition reload). Leaked slots push later chest
  packets into high slots that spill past buffer A onto adjacent NPCs
  (R125: opening a frog-coin chest, sprite 234, leaks its slot; a later
  flower chest lands in slot 2 and clobbers NPC 5 — even after the frog
  coin has despawned). We replace the sprite gate
  (``A5 80 C9 C3 D0 1E``) with a ``JSR`` to a sprite-independent helper::

      LDA $19,X / SEC / SBC $01A4 / CMP #$08 / RTS   ; carry set if d>=8

  then ``BCS $97DD`` (not a live NPC slot → bitmap-free path) / ``NOP``.
  A live NPC slot has ``$19,X - $01A4`` in ``[0,8)`` (the allocator returns
  ``2*index + $01A4``); coins/bitmap packets store ``$19,X`` below
  ``$01A4``, so the subtraction wraps ``>= 8`` and they route correctly.
  Carry clear falls through to the existing ``$97BF`` clear, whose index
  math already recomputes the bit from ``$19,X`` (sprite-independent). This
  fixes the leak at zero VRAM cost — no reservation needed for the common
  sequential-open case.
"""

from typing import Iterable


_HOOK_OFFSET = 0x009365
_HOOK_BYTES = bytes([
    0x20, 0xC8, 0x80,   # JSR $80C8       lookup packet ID, set carry
    0xB0, 0x17,         # BCS $9381       not in list → bitmap path
    0xEA,               # NOP
])

_ROUTINE_OFFSET = 0x0080C8
# $C0:80C8..$C0:812F only — learn_special_event.py owns $C0:8130-8136 and is
# applied later (last-writer-wins), so anything we place at $8130+ is silently
# eaten. The 22 B of vanilla copyright padding at $C0:8137-814C is still free.
_ROUTINE_MAX_BYTES = 0x8130 - 0x80C8  # 104

# Chest-packet slot reservation (per-room). See docstring, site ``$C0:9137``.
# The helper recomputes the treasure-chest buffer's cursor advance as
# `4 + main_buffer_space*4`, so buffer A's own main_buffer_space controls how
# much VRAM is reserved above it for the 4-slot chest-packet allocator at
# $C0:95DD. main_buffer_space=0 → +4 (byte-identical to vanilla); =1 → +8.
_CHEST_HOOK_OFFSET = 0x009137
_CHEST_RESERVE_HELPER = bytes([
    0xA5, 0x80,   # LDA $80        buffer A type byte (main_buffer_space in bits 4-6)
    0x29, 0x70,   # AND #$70       isolate main_buffer_space bits
    0x4A,         # LSR A
    0x4A,         # LSR A          A = main_buffer_space * 4
    0x18,         # CLC
    0x69, 0x04,   # ADC #$04       A = 4 (vanilla floor) + main_buffer_space*4
    0x65, 0x6D,   # ADC $6D        A = cursor + reservation (carry clear: A<=32)
    0x85, 0x6D,   # STA $6D        advance cursor for the next buffer
    0x60,         # RTS
])

# Chest-packet slot LEAK fix. See docstring, site ``$C0:97B9``. The despawn
# free at $C0:97D5 (`AND $01A5`) is gated at $C0:97BB by `CMP #$C3`
# (sprite 195/FLOWER) — vanilla's only NPC-slot packet sprite. This patch
# routes ~50 distinct sprites through the NPC-slot allocator, but the free
# path still recognizes only flower, so 49/50 sprites never clear their slot
# bit → slots leak until room reload → later chest packets get high slots
# that spill onto NPCs. Replace the sprite gate ($C0:97B9-97BE) with a
# sprite-independent check: a live NPC slot has `($19,X - $01A4)` in [0,8);
# coins/bitmap packets sit below $01A4, so the subtraction wraps >= 8 and they
# correctly fall through to the bitmap-free path at $97DD. The index/mask math
# at $97BF already recomputes the bit from $19,X, so only the gate changes.
_LEAK_HOOK_OFFSET = 0x0097B9
# Lives in the second free block ($C0:8137-814C, 22 B of vanilla copyright
# padding) rather than trailing the allowlist routine — the first block ends at
# $8130 where learn_special_event.py's opcode-$CE handler starts.
_LEAK_HELPER_OFFSET = 0x008137
_LEAK_HELPER_MAX_BYTES = 0x814D - 0x8137  # 22
_LEAK_VALIDATE_HELPER = bytes([
    0xB5, 0x19,         # LDA $19,X      packet's stored VRAM offset
    0x38,               # SEC
    0xED, 0xA4, 0x01,   # SBC $01A4      d = offset - buffer A base
    0xC9, 0x08,         # CMP #$08       carry set if d >= 8 (not an NPC slot)
    0x60,               # RTS            caller BCS -> bitmap free ($97DD)
])


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
    # The allowlist routine and the chest-reserve helper share the first free
    # block; addresses computed at patch time so they never collide with the
    # (variable-length) routine. The leak helper sits in the second block.
    reserve_offset = _ROUTINE_OFFSET + len(routine)
    used = (reserve_offset + len(_CHEST_RESERVE_HELPER)) - _ROUTINE_OFFSET
    if used > _ROUTINE_MAX_BYTES:
        raise RuntimeError(
            f"npc_slot routine ({len(routine)} B) + chest-reserve helper "
            f"({len(_CHEST_RESERVE_HELPER)} B) = {used} B exceed the "
            f"{_ROUTINE_MAX_BYTES} B free region at $C0:80C8 (before "
            f"learn_special_event's handler at $C0:8130). "
            f"Reduce npc_slot_packet_ids."
        )
    leak_offset = _LEAK_HELPER_OFFSET
    if len(_LEAK_VALIDATE_HELPER) > _LEAK_HELPER_MAX_BYTES:
        raise RuntimeError(
            f"leak-fix helper ({len(_LEAK_VALIDATE_HELPER)} B) exceeds the "
            f"{_LEAK_HELPER_MAX_BYTES} B free region at $C0:8137."
        )
    # Same-bank ($C0) JSRs; HiROM $C0:xxxx ROM low-16.
    reserve_snes = reserve_offset & 0xFFFF
    leak_snes = leak_offset & 0xFFFF
    chest_hook = bytes([
        0x20, reserve_snes & 0xFF, (reserve_snes >> 8) & 0xFF,   # JSR reserve helper
        0xEA, 0xEA, 0xEA, 0xEA,                                   # pad advance to 7 B
    ])
    # Replace the sprite-195 free gate at $97B9-97BE: JSR validate; BCS $97DD
    # (not an NPC slot -> bitmap free); NOP. Carry clear falls through to the
    # existing $97BF clear. BCS operand is fixed: $97DD-($97BC+2)=$1F.
    leak_hook = bytes([
        0x20, leak_snes & 0xFF, (leak_snes >> 8) & 0xFF,   # JSR validate
        0xB0, 0x1F,                                          # BCS $97DD
        0xEA,                                                # NOP
    ])
    return {
        _HOOK_OFFSET: _HOOK_BYTES,
        _ROUTINE_OFFSET: routine,
        reserve_offset: _CHEST_RESERVE_HELPER,
        _CHEST_HOOK_OFFSET: chest_hook,
        leak_offset: _LEAK_VALIDATE_HELPER,
        _LEAK_HOOK_OFFSET: leak_hook,
    }
