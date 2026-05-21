"""StaticData: open-mode base ROM content the randomizer does not regenerate.

Carries the *render-disjoint* bytes of the open-mode base ROM — spell/effect
animation graphics + molds + palettes (``$F3``/``$F4``), object/effect palettes
(``$E5``), compressed tilesets (``$FD``), and assorted gap data
(``$D4``/``$DD``/``$E0``/``$E4``/``$F7``/``$F9``/``$FA``/``$FE``/``$FF``) that no
``smrpgpatchbuilder`` ``render()`` method writes. The randomizer only renders a
subset of animation banks (``_02``/``_35``/``_3A``), so these banks fall
through; without this module the data would revert to vanilla when
``open_mode.json`` is retired (verified: dropping it changes a real ROM).

Stored as a checked-in binary asset (``static_data.bin``) rather than inline
literals (~137 KB). The loader streams it into the patch as ``{offset: bytes}``.
Record format (same as ``title_screen.bin``)::

    [u32 file_offset LE][u32 length LE][length bytes] ...

Only the render-disjoint bytes are carried (per-byte, so partially-rendered
entries don't clobber the bytes their collection owns).

ORDERING: this must be applied **before** the palette cosmetic renders
(``sprite_palettes`` / ``event_palettes`` / spell palettes) so those override
the effect-palette base where they overlap.

To regenerate ``static_data.bin``, re-extract the render-disjoint bytes for
file offsets ``>= 0x140000`` (banks ``$D4``+) — see the deconstruction notes.
"""

import os
import struct

_ASSET = os.path.join(os.path.dirname(__file__), "static_data.bin")


def get_patch() -> dict[int, bytes]:
    """Stream the render-disjoint base-ROM records from ``static_data.bin``."""
    out: dict[int, bytes] = {}
    with open(_ASSET, "rb") as handle:
        blob = handle.read()
    pos = 0
    while pos < len(blob):
        offset, length = struct.unpack_from("<II", blob, pos)
        pos += 8
        out[offset] = blob[pos : pos + length]
        pos += length
    return out
