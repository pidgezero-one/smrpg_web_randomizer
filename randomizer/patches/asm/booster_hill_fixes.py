"""Booster Hill (room 14) cold-entry hard freeze + slide + splash — ROOT fix.

All three symptoms (SA-1 deadlock, player "slide", water "splash") are a single
bug that only surfaces on a *cold* Booster Hill entry (world-map -> room 14
without first passing through a Booster Tower / Booster Pass area-load). See the
``project_booster_hill_sa1_deadlock`` session memory (esp. update #85) for the
full multi-day trace; the short version is below.

Root cause: a 1-byte SA-1 stack leak
------------------------------------
The randomized prize packet is overworld object ``$6600``. Its animation is run
by the SA-1 sprite-animation interpreter (``$C0:CE00`` .. bank ``$E1`` script).
One animation command is handled at ``$C0:E0A2``:

    C0/E0B4  LDA $30,X        ; X = anim-part index * 2; tests bit7 of a $00:00xx flag
    C0/E0B6  BPL $E0BF        ; bit7 CLEAR -> skip (this is the *warm* path)
    C0/E0B8  LDA #$E1
    C0/E0BA  STA $31,X
    C0/E0BC  PHB / PHA / PLB  ; sets DB=$E1 -- but DB is ALREADY $E1 (set at frame
                              ;   entry $CE1E), so this is redundant AND the PHB
                              ;   byte is never popped -> a 1-byte stack LEAK
    C0/E0BF  BRL $CE36

The frame's single exit ``$C0:E380 PLB`` is reserved for the ``$CE1E`` entry
``PHB``; there is no second ``PLB`` to balance ``$E0BC``. So when that flag's
bit7 is SET, the anim frame runs with the SA-1 stack one byte low. At frame exit
(``$E380 PLB`` then ``$E395 RTS``) the misaligned unwind pops the stale ``$E1``
as the data bank and the stale ``$5100`` as the return address, so instead of
returning to the animation loop (``$C0:CA52``) it lands on ``$C0:5101 BRL $3E93``
— the *event*-script interpreter. The event interpreter then decodes ``$6600``'s
animation bytes as event commands, one of which (``$C0:3F68 STA $31,X`` with
X=$6000) stamps the *player* object's animation bank to ``$E1``. The player then
runs a garbage animation that (a) stages an SA-1 graphics command that never
completes -> the S-CPU/SA-1 handshake deadlock, (b) drives the player east ->
the slide, and (c) draws stale water molds -> the splash.

A *warm* entry leaves that flag's bit7 CLEAR (Booster Tower / Booster Pass area
loads clear it — the entire "196/197" asymmetry), so ``$E0B6 BPL`` is taken, the
leak never happens, and ``$6600`` stays in the animation engine. Confirmed by
diffing the cold vs warm SA-1 trace logs: at the shared ``$C0:DBC8`` the cold
stack is ``S:07F5`` and the warm stack is ``S:07F6`` — exactly one byte.

The fix
-------
Reproduce the warm behaviour on a cold Booster Hill entry: when the leaky path
would run (bit7 SET) *and* we are in Booster Hill (IRAM ``$003030`` == ``$000E``),
skip the redundant ``LDA #$E1 / STA $31,X / PHB/PHA/PLB`` block entirely — i.e.
take the same ``BRL $CE36`` the warm branch takes, with no orphaned byte. Every
other room, and every bit7-CLEAR invocation, runs the exact vanilla bytes.

``$C0:E0A2`` is shared engine code, so the hook is area-gated to be completely
inert outside Booster Hill. In practice the handler only ever runs for ``$6600``
in this scenario (verified 1x in the trace), but the gate keeps it safe.

This single patch replaces the earlier ``$5754`` deadlock trampoline (proven
inert — reverting it still crashed) and the ``$3F66`` slide stamp (a downstream
band-aid): both are deleted.

Run the ``smrpg-patch-audit`` skill if the hook site or free-space range moves.
"""

from randomizer.data.nmi_hook import Asm65816

# --- Hook site (ROM offset; HiROM $C0:xxxx -> ROM $00xxxx) ---
# Vanilla $C0:E0B4 = B5 30 10 07  (LDA $30,X / BPL $E0BF). Replaced by a 4-byte
# JML to the trampoline. The following LDA #$E1 / STA $31,X / PHB/PHA/PLB at
# $E0B8-$E0BE become dead inline code (only reached via the trampoline, which
# reproduces them).
_LEAK_HOOK = 0x00E0B4
_E0BF_SNES = 0xC0E0BF        # vanilla BRL $CE36 — where every path rejoins

# Trampoline in C1 free space (the region the old slide trampoline used; the
# always-on uncap_max_fp module owns $C1:C6C0-$C6DD, this sits just past it).
_LEAK_TRAMP = 0x01C700       # ROM offset -> SNES $C1:C700
_LEAK_TRAMP_SNES = 0xC1C700

_AREA_ID = 0x003030          # IRAM overworld area id (16-bit)
_BOOSTER_HILL = 0x000E       # Booster Hill area id
_ANIM_DB = 0xE1              # the (redundant) data bank the leaky block sets


def _leak_trampoline() -> bytes:
    """Skip the leaky bank-dance in Booster Hill; run vanilla bytes elsewhere.

    Entry width matches the hook site ($C0:E0B4): M=8, X=16. X (the anim-part
    index) must be preserved for ``STA $31,X``; A and flags are free — the
    vanilla code past ``$E0BF`` reloads A at ``$CE36`` and never reads them.
    """
    a = Asm65816(base_addr=_LEAK_TRAMP & 0xFFFF)
    # Reproduce "LDA $30,X / BPL $E0BF": bit7 clear -> vanilla skip.
    a.emit(0xB5, 0x30)              # LDA $30,X
    a.and_imm8(0x80)               # AND #$80   (isolate bit7; == BPL test)
    a.beq("done")                  # bit7 clear -> skip (vanilla BPL $E0BF)
    # bit7 SET: only deviate from vanilla inside Booster Hill.
    a.rep(0x20)                    # 16-bit area compare
    a.lda_long(_AREA_ID)           # LDA $003030 (long: bank $00 regardless of DB)
    a.cmp_imm16(_BOOSTER_HILL)     # CMP #$000E
    a.sep(0x20)                    # restore M=8
    a.beq("done")                  # Booster Hill -> skip the leaky block (== warm)
    # Any other room, bit7 set: reproduce the exact vanilla block (incl. leak).
    a.lda_imm8(_ANIM_DB)           # LDA #$E1
    a.emit(0x95, 0x31)             # STA $31,X
    a.emit(0x8B)                   # PHB
    a.emit(0x48)                   # PHA
    a.emit(0xAB)                   # PLB
    a.label("done")
    a.jml(_E0BF_SNES)              # JML $C0:E0BF  (vanilla BRL $CE36)
    return a.finalize()


def _jml(addr: int) -> bytes:
    """JML $addr (opcode 5C + 24-bit little-endian; 4 bytes)."""
    return bytes([0x5C, addr & 0xFF, (addr >> 8) & 0xFF, (addr >> 16) & 0xFF])


def get_patch() -> dict[int, bytes]:
    return {
        _LEAK_HOOK: _jml(_LEAK_TRAMP_SNES),   # $C0:E0B4: JML $C1:C700  (5C 00 C7 C1)
        _LEAK_TRAMP: _leak_trampoline(),
    }


if __name__ == "__main__":
    t = _leak_trampoline()
    # Structure self-check: the assembled trampoline must
    #   * start by reproducing LDA $30,X / AND #$80  (B5 30 29 80),
    #   * end with JML $C0:E0BF                       (5C BF E0 C0),
    #   * contain exactly one leaky PHB/PHA/PLB       (8B 48 AB) for the
    #     non-Booster-Hill path,
    #   * contain the 16-bit Booster-Hill area compare (AF 30 30 00 / C9 0E 00).
    assert t[:4] == bytes([0xB5, 0x30, 0x29, 0x80]), "tramp must open LDA $30,X/AND #$80"
    assert t.endswith(bytes([0x5C, 0xBF, 0xE0, 0xC0])), "tramp must end JML $C0:E0BF"
    assert t.count(bytes([0x8B, 0x48, 0xAB])) == 1, "exactly one vanilla PHB/PHA/PLB"
    assert bytes([0xAF, 0x30, 0x30, 0x00]) in t, "must read LDA $003030 (long)"
    assert bytes([0xC9, 0x0E, 0x00]) in t, "must compare CMP #$000E"

    p = get_patch()
    assert p[_LEAK_HOOK] == bytes([0x5C, 0x00, 0xC7, 0xC1]), "hook = JML $C1:C700"
    assert len(p[_LEAK_HOOK]) == 4, "hook must be exactly 4 bytes (B5 30 10 07)"
    print(f"leak trampoline ({len(t)}B @ $C1:C700): {t.hex()}")
    print(f"hook @ $C0:E0B4: {p[_LEAK_HOOK].hex()}")
    print("ok")
