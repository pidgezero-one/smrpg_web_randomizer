"""Protagonist-static overworld engine substrate (always-on).

Three always-on engine edits from ``open_mode.json`` that make "the
protagonist" a fixed slot-0 / char-0 concept on the overworld. They are the
engine *substrate* that the per-character :mod:`non_mario_character` patches
build on top of: that module sets the protagonist's *sprite base* (``$0:9B86``)
and clone handler (``$0:94AF``) when the overworld walker isn't Mario; THIS
module forces the engine to *use* slot 0 / char 0 as the protagonist
regardless of who occupies it. ``non_mario_character`` does NOT write any of
the offsets below — they are always applied for every seed (Mario included).

LOAD-BEARING — relocate the *patched* bytes verbatim; do **not** restore the
vanilla code. An overworld-follower feature built on restoring ``$9009`` (a
hybrid ``JSR`` hook in the now-deleted ``overworld_ally_loader.py``) was fully
scrapped 2026-05-20 because it broke Bowser VRAM (6-slot lead sprite overlaps
the adjacent object slot) and the clone-protagonist. Working state = char-0
collapse; followers render as the protagonist (accepted limitation). See
memory ``reference_c0_9b4e_sprite_loader`` /
``project_open_mode_deconstruction``.

Sites (raw file offsets; HiROM+SA-1 ``$C0:xxxx`` -> file ``0x0xxxx``). Bytes
verified IDENTICAL to the legacy open_mode.json entries via
``manage.py diff_open_mode --module randomizer.patches.asm.protagonist_static``:

1. ``$C0:9009`` (file ``0x09009``) — ally-loader char-index collapse. Vanilla
   ``B9 00 00`` (``LDA $0000,Y``) -> ``A9 00 EA`` (``LDA #$00`` / ``NOP``),
   forcing the ``$9B4E`` loader's char id (dp ``$60``) to 0 on every
   party-slot iteration, so every overworld party object loads slot 0's sprite
   arm at ``$9B86``. (For Mario seeds ``$9B86`` stays vanilla ``$00`` = Mario;
   non_mario_character only changes it when the walker isn't Mario.)

2. ``$C0:3EB2`` (file ``0x03EB2``) — name-targeted script resolver gutting.
   Vanilla is an 11-byte ``CMP $00,X`` / loop that resolves
   MARIO/PEACH/BOWSER/GENO/MALLOW name targets to a party slot; open_mode NOPs
   it (11x ``EA``) so name-targeted scripts always resolve to slot 0
   (protagonist-static).

3. ``$C0:E42C`` (file ``0x0E42C``) — sibling resolver loop
   (``CMP $00,X`` / ... / ``CMP $00303F`` / ``BNE``), NOP'd (15x ``EA``) for
   the same reason. This is also the ``$E42C-$E43A`` NOP region the scrapped
   hybrid hook had repurposed; with ``overworld_ally_loader.py`` deleted it is
   back to plain NOPs.
"""


def get_patch() -> dict[int, bytes]:
    return {
        # $C0:9009 — ally-loader char-0 collapse (B9 00 00 -> A9 00 EA)
        0x09009: bytes([0xA9, 0x00, 0xEA]),
        # $C0:3EB2 — name-targeted script resolver gutting (11 NOPs)
        0x03EB2: bytes([0xEA] * 11),
        # $C0:E42C — sibling resolver loop gutting (15 NOPs)
        0x0E42C: bytes([0xEA] * 15),
    }
