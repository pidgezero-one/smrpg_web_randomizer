"""Battlefield underwater-palette: disable the per-battlefield underwater
visual effect entirely.

Three battlefields trigger SMRPG's "underwater mode":

* BF14_KERO_SEWERS_UNDERWATER (battlefield index $0E)
* BF34_SEA_ENCLAVE            (battlefield index $22)
* BF38_SEA                    (battlefield index $26)

When entered, $C2:91D3-91EA reads the battlefield index from
$00:004B and, on a match, executes TSB $3050 to set bit 1 of
$00:3050. That bit is later checked at $C2:9528 and $C2:978A
to swap the engine onto an alternate sprite/packet code path that
applies a "+4" effect to every actor's OBJ palette field.

For monsters that have an underwater-palette variant baked into the
data (Goby, Bloober, Crusty, Leuko, Muckle, Mr. Kipper, Zeostar,
Starslap, Star Cruster, Toadstool 2/3, Mario/Mallow/Geno/Bowser
Clones/Copy-S, Bowser Copy S - i.e. enemies that vanilla can place in
these battlefields), the +4 path resolves to a legit darker palette.
For monsters the randomizer can place there but vanilla never did,
there is no +4 variant - the engine reads garbage from a neighboring
palette region, producing visually broken sprites (e.g. Croco 1
rendering with another monster's palette in BF38).

Why this patch
--------------

The "+4" effect is split across multiple sites: a per-actor palette
load offset at $C2:88DE (already in vanilla) **and** a sprite-side
OAM palette field shift driven by $3050 bit 1. Empirical bsnes-plus
debugging (May 2026) confirmed that gating the per-actor side alone is
not sufficient - the OAM palette field is set during sprite construction
on a path I could not statically isolate, and even with the per-actor
underwater path skipped, sprites still render with the +4 OAM palette
that points at the wrong CGRAM slot.

The simplest, robust fix is to **never set $3050 bit 1**, which
removes the underwater branch from both the palette-load and the OAM
construction sides. The visual cost is that the three underwater
battlefields no longer render with their darker "underwater tint"
(vanilla underwater monsters now look like they would on land), but
this is uniform across all monsters - vastly better than the random
"some monsters look correct, others render with completely wrong
palettes" mismatch that the randomizer otherwise produces.

ROM site
--------

* $C2:91EA (3 bytes, ROM $0291EA) - the TSB $3050
  instruction inside the battlefield-index gate. Replaced with three
  NOPs so the gate runs but the flag is never set::

      0C 50 30   TSB $3050
      EA EA EA   NOP NOP NOP

  The surrounding LDA #$0002 (at $C2:91E7) and the BEQ/BNE
  comparisons ($C2:91D8-91E5) are left unchanged - they are now
  dead-effect but harmless, and leaving them in place makes the patch
  trivially revertible.

History
-------

An earlier version of this file installed a 5-byte JML hook at
$C2:8898 and a 148-byte helper at $CF:FE80 that filtered the
per-actor underwater BNE on a hardcoded monster whitelist. That hook
fired correctly but did not solve the visible problem, because the +4
on the OAM palette field is set independently of the per-actor flag
the hook gated. See git history for the JML/whitelist version if
per-monster gating is ever revisited.
"""


# -----------------------------------------------------------------------
# Patch site
# -----------------------------------------------------------------------
TSB_ROM_OFFSET = 0x0291EA            # SNES $C2:91EA -- TSB $3050
TSB_LEN = 3
NOP_BYTES = bytes([0xEA, 0xEA, 0xEA])
assert len(NOP_BYTES) == TSB_LEN


def get_patch() -> dict[int, bytes]:
    """Return {rom_offset: bytes} - three NOPs at $C2:91EA."""
    return {TSB_ROM_OFFSET: NOP_BYTES}
